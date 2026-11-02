"""Policy B high-accuracy final objectives; calibration penalties never change."""
from common_v1 import *
import math
sys.path.insert(0,str(G/'full_path_validation'))
from audit import bound_W,rational_stat,sqrt_upper
def optimize(X,y,lam,settings):
 # The accumulator is platform np.longdouble (53 significand bits on this
 # Windows build, so no extra precision is assumed). Serial CD and direct
 # active-set polish solve the SAME lasso objective and penalties.
 xx=X.astype(np.longdouble);yy=y.astype(np.longdouble)
 Gm=xx.T@xx;h=xx.T@yy;b=np.zeros(X.shape[1],dtype=np.longdouble);target=settings['KKT_absolute_target']
 for sweep in range(1,settings['max_sweeps']+1):
  for j in range(len(b)):
   z=h[j]-Gm[j]@b+Gm[j,j]*b[j]
   b[j]=np.sign(z)*max(abs(z)-np.longdouble(lam[j])/2,0)/Gm[j,j]
  grad=2*(h-Gm@b);violation=np.where(b!=0,abs(grad-lam*np.sign(b)),np.maximum(abs(grad)-lam,0))
  if np.max(violation)<=target:break
 else:raise ArithmeticError('INSTRUMENT_UNRESOLVED: CD iteration limit')
 active=np.flatnonzero(b!=0)
 if settings['active_set_polish'] and len(active):
  polished=np.zeros(len(b));polished[active]=np.linalg.solve(np.asarray(Gm[np.ix_(active,active)],dtype=float),
    np.asarray(h[active]-lam[active]*np.sign(b[active])/2,dtype=float))
  g=2*(h-Gm@polished);v=np.where(polished!=0,abs(g-lam*np.sign(polished)),np.maximum(abs(g)-lam,0))
  if np.all(np.sign(polished[active])==np.sign(b[active])) and np.max(v)<=target:b=polished.astype(np.longdouble)
 result=np.asarray(b,dtype=float);grad=2*(h-Gm@result)
 kkt=float(np.max(np.where(result!=0,abs(grad-lam*np.sign(result)),np.maximum(abs(grad)-lam,0))))
 if kkt>target:raise ArithmeticError('INSTRUMENT_UNRESOLVED: returned coefficient KKT failure')
 return result,{'sweeps':sweep,'KKT_max':kkt,'active':active.tolist()}
def certificate(folder,j,b,Xraw,Z,cent):
 n,p=Xraw.shape
 prefix=f'instrument_{j}_';X=read(folder/(prefix+'centered_X.bin'),(n,p));y=read(folder/(prefix+'centered_y.bin'))
 lam=[F(float(v)) for v in read(folder/(prefix+'last_penalty.bin'))]
 xx,EX=dyadic(X);yy,EY=dyadic(y);gi=xx.T@xx;hi=xx.T@yy
 # Active set is proposed by the new solver, not read from the reference.
 active=np.flatnonzero(b!=0).tolist();bn=[F(float(v)) for v in b]
 rhs=[F(int(hi[k]),1<<(EX+EY))*(1<<(2*EX))-lam[k]*(1 if b[k]>0 else -1)*(1<<(2*EX))/2 for k in active]
 solved=integer_solve_rational_rhs(gi[np.ix_(active,active)].tolist(),rhs)
 br=[F(0)]*p
 for k,v in zip(active,solved):br[k]=v
 assert all(br[k]!=0 and (br[k]>0)==(b[k]>0) for k in active)
 Gq=lambda k,l:F(int(gi[k,l]),1<<(2*EX))
 hq=[F(int(v),1<<(EX+EY)) for v in hi]
 grad=[2*(hq[k]-sum((Gq(k,l)*br[l] for l in active),F(0))) for k in range(p)]
 assert all(grad[k]==lam[k]*(1 if br[k]>0 else -1) if br[k] else abs(grad[k])<=lam[k] for k in range(p))
 y2=F(sum(int(v)**2 for v in yy),1<<(2*EY))
 def objective(beta):
  s=[k for k,v in enumerate(beta) if v]
  return y2-2*sum((hq[k]*beta[k] for k in s),F(0))+sum((Gq(k,l)*beta[k]*beta[l] for k in s for l in s),F(0))+sum(l*abs(v) for l,v in zip(lam,beta))
 primal=objective(br);dual=y2-sum((Gq(k,l)*br[k]*br[l] for k in active for l in active),F(0))
 assert primal==dual
 native=objective(bn);assert native>=primal;gap=native-primal
 # A fresh approximate inverse is merely a witness; rationals check it.
 R=np.linalg.inv(np.asarray(gi,dtype=float)/(2.**(2*EX)));R=(R+R.T)/2
 put(folder/(prefix+'inverse_gram_witness.bin'),R);ri,ER=dyadic(R)
 den=1<<(ER+2*EX);err=np.eye(p,dtype=object)*den-ri@gi
 norm=max(max(sum(abs(int(z)) for z in row) for row in err),max(sum(abs(int(z)) for z in row) for row in err.T))
 eta=F(norm,den);rn=F(max(sum(abs(int(z)) for z in row) for row in ri),1<<ER);assert eta<1
 mu=(1-eta)/rn;radius=sqrt_upper(gap/mu)
 m=[F(float(v)) for v in cent];intercept=m[0]-sum(a*v for a,v in zip(m[1:],br))
 actual_coef=read(folder/'instrument_coefficients.bin',(p+1,2))[:,j-1]
 psi=read(folder/'psi.bin',(n,2))[:,j-1]
 ref=[];arith=F(0)
 for row,z,psi_value in zip(Xraw,Z,psi):
  xr=[F(float(v)) for v in row]
  exact=F(float(z))-intercept-sum((xr[k]*br[k] for k in active),F(0));ref.append(exact)
  literal=F(float(z))-F(float(actual_coef[0]))-sum((xr[k]*bn[k] for k in active),F(0))
  arith=max(arith,abs(F(float(psi_value))-literal))
 center_error=abs(F(float(actual_coef[0]))-(m[0]-sum(a*v for a,v in zip(m[1:],bn))))
 assert np.all((Xraw>=0)&(Xraw<=1)) and all(0<=v<=1 for v in m[1:])
 rownorm=sqrt_upper(F(p));psi_radius=rownorm*radius+arith+center_error
 cert={'version':'2G-D.1','objective':'||yc-Xc b||^2 + sum lambda_j |b_j|; fixed original last-used lambda',
  'beta':[record(v) for v in br],'intercept':record(intercept),'active':active,
  'optimal_primal':record(primal),'optimal_dual':record(dual),'returned_primal':record(native),'returned_true_gap':record(gap),
  'Gram_witness_sha256':sha(folder/(prefix+'inverse_gram_witness.bin')),
  'inverse_residual_bound':record(eta),'inverse_norm_bound':record(rn),'gram_min_eigenvalue_lower_bound':record(mu),
  'coefficient_L2_radius':record(radius),'psi_mapping_row_norm_bound':record(rownorm),'psi_uniform_radius':record(psi_radius),'psi_rounding_envelope':record(arith+center_error),
  'coefficient_max_error':float(max(abs(v-r) for v,r in zip(bn,br))),
  'scope':'Final fixed-penalty objective, exact exported arrays; no exhaustive adaptive-branch certificate'}
 dump(folder/(prefix+'certificate.json'),cert)
 return cert,ref,psi_radius
def main():
 cfg=load(HERE/'CONFIG_v1.json');summary=[];instruments=[]
 hist={r['id']:r for r in rows(E/'complete_24_problem_table.csv')}
 for outcome in rows(OUT/'outcome_validation.csv'):
  id=outcome['id'];folder=OUT/id;t=time.perf_counter()
  if outcome['status']!='PASS':summary.append({'id':id,'status':'OUTCOME_UNRESOLVED'});continue
  try:
   Xraw=read(E/id/'X_row_major.bin',(1000,101))[:,1:];Z=read(folder/'Z_row_major.bin',(1000,2));coeff=np.zeros((101,2))
   solves=[]
   for j in (1,2):
    p=f'instrument_{j}_';X=read(folder/(p+'centered_X.bin'),(1000,100));y=read(folder/(p+'centered_y.bin'))
    lam=read(folder/(p+'last_penalty.bin'));cent=read(folder/(p+'centering.bin'))
    t0=time.perf_counter();b,diagnostic=optimize(X,y,lam,cfg['instrument']);seconds=time.perf_counter()-t0
    t0=time.perf_counter();b2,diag2=optimize(X,y,lam,cfg['instrument']);repeat_seconds=time.perf_counter()-t0
    assert np.array_equal(b,b2),'Instrument solver not bitwise reproducible'
    coeff[1:,j-1]=b;coeff[0,j-1]=cent[0]-cent[1:]@b
    solves.append({'id':id,'instrument':j,'solver_seconds':seconds,'repeat_seconds':repeat_seconds,
      'sweeps':diagnostic['sweeps'],'KKT_max':diagnostic['KKT_max'],'repeat_identical':True})
   psi=Z-np.column_stack([np.ones(1000),Xraw])@coeff
   score=.9-read(folder/'rank.bin');obs=psi*score[:,None];g=obs.sum(axis=0);S=obs.T@obs;W=float(g@np.linalg.solve(S,g))
   put(folder/'instrument_coefficients.bin',coeff);put(folder/'psi.bin',psi);put(folder/'score.bin',score)
   put(folder/'observation_scores.bin',obs);put(folder/'score_sum.bin',g);put(folder/'second_moment.bin',S);put(folder/'W.bin',[W])
   refs=[];radii=[];certs=[];certificate_seconds=0
   for j in (1,2):
    t0=time.perf_counter();cert,ref,radius=certificate(folder,j,coeff[1:,j-1],Xraw,Z[:,j-1],read(folder/f'instrument_{j}_centering.bin'))
    elapsed=time.perf_counter()-t0;certificate_seconds+=elapsed;certs.append(cert);refs.append(ref);radii.append(radius)
    prior=load(OLD/id/'C'/f'instrument_{j}_certificate.json')
    assert [val(v) for v in cert['beta']]==[val(v) for v in prior['beta']],'Same fixed-penalty optimum disagrees with reference'
    solves[j-1].update({'certificate_seconds':elapsed,'true_objective_gap':cert['returned_true_gap']['float'],
     'coefficient_max_error':cert['coefficient_max_error'],'unique_optimum':True,'status':'PASS'})
   cutoff=F(float(read(E/'cutoff.bin')[0]));scores=[F(float(v)) for v in score]
   reference=rational_stat(list(zip(*refs)),scores,cutoff);bounds=bound_W(list(zip(*refs)),radii,scores,cutoff)
   bounds['scope']='Version B final fixed-penalty objective sublevels and explicit psi rounding; no exhaustive historical branch propagation'
   assert bounds['status'] in ['ACCEPT_CERTIFIED','REJECT_CERTIFIED']
   assert val(bounds['lower'])<=F(W)<=val(bounds['upper'])
   inf=exact_W(psi,score,cutoff);assert inf['accepted']==(F(W)<=cutoff)==reference['accepted']
   dump(folder/'exact_returned_score_inference.json',inf);dump(folder/'exact_fixed_objective_reference_inference.json',reference);dump(folder/'decision_bounds.json',bounds)
   Cpsi=read(OLD/id/'C/psi.bin',(1000,2));Ccoef=read(OLD/id/'C/instrument_coefficients.bin',(101,2));Cw=float(read(OLD/id/'C/W.bin')[0])
   Acoef=read(E/id/'historical_projection_coef.bin',(101,2)) if (E/id/'historical_projection_coef.bin').exists() else None
   instruments.extend(solves)
   summary.append({'id':id,'status':'PASS','historical_W':float(hist[id]['historical_W']),'historical_accepted':hist[id]['historical_accepted'],
    'Policy_C_W':Cw,'Policy_C_accepted':Cw<=float(cutoff),'proposed_W':W,'proposed_accepted':W<=float(cutoff),
    'decision_agrees_Policy_C':(W<=float(cutoff))==(Cw<=float(cutoff)),
    'decision_agrees_historical':(W<=float(cutoff))==(hist[id]['historical_accepted'].upper()=='TRUE'),
    'instrument_coefficient_max_change_from_C':float(np.max(abs(coeff-Ccoef))),
    'psi_max_change_from_C':float(np.max(abs(psi-Cpsi))),'observation_score_max_change_from_C':float(np.max(abs(obs-Cpsi*score[:,None]))),
    'rank_score_changes_from_C':int(np.sum(score!=read(OLD/id/'C/score.bin'))),'W_change_from_C':W-Cw,
    'W_lower':bounds['lower']['float'],'W_upper':bounds['upper']['float'],'decision_bound_status':bounds['status'],
    'W_exact_reconstruction_error':abs(W-inf['W']['float']),'S_condition':float(np.linalg.cond(S)),
    'instrument_solver_seconds':sum(r['solver_seconds'] for r in solves),'instrument_exact_seconds':certificate_seconds,
    'instrument_phase_total_seconds':time.perf_counter()-t})
   print('INSTRUMENT',id,'PASS','W',W,flush=True)
  except Exception as exc:
   dump(folder/'NUMERICALLY_UNRESOLVED.json',{'error':repr(exc)});summary.append({'id':id,'status':'INSTRUMENT_OR_INFERENCE_UNRESOLVED','error':repr(exc)})
   print('INSTRUMENT',id,'UNRESOLVED',repr(exc),flush=True)
 table(OUT/'candidate_comparison.csv',summary);table(OUT/'instrument_validation.csv',instruments)
if __name__=='__main__':main()
