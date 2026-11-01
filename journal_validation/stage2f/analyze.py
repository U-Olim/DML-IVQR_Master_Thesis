"""Exact primal/dual face reconstruction for TWO saved problems. No fit solver."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import csv,hashlib,json,math,os,subprocess,sys
import numpy as np

HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[1]
SOURCE=ROOT/'journal_validation/stage2e/output/paired_20261029T093009Z'
CASES=['pilot_002_minus','pilot_006_truth']
sys.path.insert(0,str(ROOT/'journal_validation/stage2c/certification'))
from exact_bounds import dyadic,bareiss_solve,record


def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for block in iter(lambda:f.read(1024*1024),b''):h.update(block)
 return h.hexdigest()


def dump(p,x):
 def convert(v):
  if isinstance(v,np.ndarray):return v.tolist()
  if isinstance(v,np.generic):return v.item()
  raise TypeError(str(type(v)))
 p.write_text(json.dumps(x,indent=2,default=convert),encoding='utf-8')


def read(p):
 with p.open(newline='',encoding='utf-8-sig') as f:return list(csv.DictReader(f))


def table(p,rows):
 keys=list(dict.fromkeys(k for r in rows for k in r))
 with p.open('w',newline='',encoding='utf-8') as f:
  w=csv.DictWriter(f,fieldnames=keys);w.writeheader();w.writerows(rows)


def snapshot():
 result={}
 for directory,subdirs,files in os.walk(ROOT):
  base=Path(directory);subdirs[:]=[d for d in subdirs if base/d!=HERE and not(base==ROOT and d=='.git')]
  for name in files:
   p=base/name;result[p.relative_to(ROOT).as_posix()]=sha(p)
 return result


def integer_solve_rational_rhs(A,rhs):
 L=math.lcm(*(v.denominator for v in rhs))
 result=bareiss_solve(A,[v.numerator*(L//v.denominator) for v in rhs])
 return [r/L for r in result]


def determinant(A):
 a=[row.copy() for row in A];n=len(a);previous=1;sign=1;pivots=[]
 for k in range(n-1):
  row=next((i for i in range(k,n) if a[i][k]),None)
  if row is None:return 0,pivots
  if row!=k:a[k],a[row]=a[row],a[k];sign=-sign
  pivot=a[k][k];pivots.append(str(pivot))
  for i in range(k+1,n):
   for j in range(k+1,n):
    value,remainder=divmod(a[i][j]*pivot-a[i][k]*a[k][j],previous)
    assert remainder==0;a[i][j]=value
   a[i][k]=0
  previous=pivot
 pivots.append(str(a[-1][-1]));return sign*a[-1][-1],pivots


def exact_objective(Xi,EX,yi,EY,beta,lam,tau):
 L=math.lcm(*(b.denominator for b in beta));bn=[b.numerator*(L//b.denominator) for b in beta]
 PD=(1 << EX)*L;D=math.lcm(PD,1 << EY)
 pred=[sum(a*b for a,b in zip(row,bn)) for row in Xi]
 e=[yi[i]*(D//(1 << EY))-pred[i]*(D//PD) for i in range(len(yi))]
 loss=sum((tau if r>=0 else tau-1)*F(r,D) for r in e)
 penalty=sum(l*abs(b)/2 for l,b in zip(lam,beta))
 return loss+penalty,e,D,pred,PD,bn,L


def reconstruct(X,y,lam,proposed_beta,proposed_e,tau):
 XX,EX=dyadic(X);YY,EY=dyadic(y);Xi=XX.tolist();yi=YY.tolist();pen=list(map(lambda z:F(float(z)),lam))
 active=np.flatnonzero(abs(proposed_beta)>1e-7).tolist();ties=np.flatnonzero(abs(proposed_e)<=1e-7).tolist()
 assert len(active)==len(ties)>0,'No square reduced active basis; unresolved without further analysis'
 A=[[Xi[i][j] for j in active] for i in ties]
 det,pivots=determinant(A);assert det!=0,'Singular proposed primal basis'
 solution=integer_solve_rational_rhs(A,[F(yi[i],1 << EY)*(1 << EX) for i in ties])
 beta=[F(0)]*101
 for j,b in zip(active,solution):beta[j]=b
 P,e,D,pred,PD,bn,LB=exact_objective(Xi,EX,yi,EY,beta,pen,tau)
 exact_ties=[i for i,v in enumerate(e) if v==0]
 assert exact_ties==ties and [j for j,b in enumerate(beta) if b]==active,'Proposed support/ties not verified exactly'
 fixed=[i for i in range(1000) if i not in set(ties)]
 v=[None]*1000
 for i in fixed:v[i]=tau if e[i]>0 else tau-1
 rhs=[]
 for j in active:
  sign=1 if beta[j]>0 else -1
  rhs.append(pen[j]*sign*(1 << EX)/2-sum(Xi[i][j]*v[i] for i in fixed))
 AT=[[Xi[i][j] for i in ties] for j in active]
 vt=integer_solve_rational_rhs(AT,rhs)
 for i,t in zip(ties,vt):v[i]=t
 assert all(tau-1<=z<=tau for z in v)
 LV=math.lcm(*(z.denominator for z in v));vn=[z.numerator*(LV//z.denominator) for z in v]
 gradient=[F(sum(row[j]*z for row,z in zip(Xi,vn)),(1 << EX)*LV) for j in range(101)]
 assert all(abs(g)<=l/2 for g,l in zip(gradient,pen))
 dual=F(sum(a*b for a,b in zip(yi,vn)),(1 << EY)*LV)
 assert P==dual,'No zero-gap exact certificate'
 for i in fixed:assert v[i]==(tau if e[i]>0 else tau-1)
 for j in active:assert gradient[j]==pen[j]*(1 if beta[j]>0 else -1)/2
 inactive=[j for j in range(101) if j not in set(active)]
 score_margins=[min(v[i]-(tau-1),tau-v[i]) for i in ties]
 penalty_margins=[pen[j]/2-abs(gradient[j]) for j in inactive]
 strict_scores=min(score_margins)>0;strict_penalties=min(penalty_margins)>0
 unique=strict_scores and strict_penalties and det!=0
 return {'status':'EXACT_OPTIMUM_CERTIFIED','tau':record(tau),'primal':record(P),'dual':record(dual),
  'gap':record(P-dual),'beta_numerators':[str(z) for z in bn],'beta_denominator':str(LB),
  'residual_numerators':[str(z) for z in e],'residual_denominator':str(D),
  'fitted_numerators':[str(z) for z in pred],'fitted_denominator':str(PD),
  'dual_numerators':[str(z) for z in vn],'dual_denominator':str(LV),
  'active_coefficients_zero_based':active,'tied_observations_one_based':[i+1 for i in ties],
  'inactive_coefficients_zero_based':inactive,
  'basis_integer_determinant':str(det),'basis_integer_pivots':pivots,
  'basis_real_determinant':record(F(det,1 << (EX*len(active)))),
  'minimum_tied_dual_box_margin':record(min(score_margins)),
  'minimum_inactive_penalty_margin':record(min(penalty_margins)),
  'unique_beta_and_fitted_values':unique,
  'uniqueness_proof':'Strict interior dual scores force every optimum to fit tied rows exactly; strict inactive penalty gradients force inactive beta=0; nonsingular tied/active basis forces the same beta.',
  'active_basis_condition_float_diagnostic':float(np.linalg.cond(X[ties][:,active]))}


def exact_W(psi,scores,cutoff):
 xx,E=dyadic(psi);ss,ES=dyadic(scores)
 z=[[int(a)*int(s) for a in row] for row,s in zip(xx.tolist(),ss.tolist())]
 g=[sum(row[j] for row in z) for j in [0,1]]
 a=sum(row[0]**2 for row in z);b=sum(row[0]*row[1] for row in z);c=sum(row[1]**2 for row in z)
 assert a*c-b*b>0
 W=F(c*g[0]**2-2*b*g[0]*g[1]+a*g[1]**2,a*c-b*b)
 return {'W':record(W),'accepted':W<=cutoff,'margin':record(W-cutoff),
  'score_sum_1':record(F(g[0],1 << (E+ES))),'score_sum_2':record(F(g[1],1 << (E+ES))),
  'S11':record(F(a,1 << (2*(E+ES)))),'S12':record(F(b,1 << (2*(E+ES)))),'S22':record(F(c,1 << (2*(E+ES))))}


def main():
 assert subprocess.check_output(['git','branch','--show-current'],cwd=ROOT,text=True).strip()=='journal-validation'
 for id in CASES:
  for f in ['X_row_major.bin','response.bin','lambda.bin','historical_beta.bin','independent_beta.bin',
            'historical_residual.bin','independent_residual.bin','historical_psi.bin','independent_psi.bin']:
   assert (SOURCE/id/f).is_file(),'Missing '+str(SOURCE/id/f)
 run=HERE/'output'/('exact_face_'+datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ'));run.mkdir(parents=True,exist_ok=False)
 print('RUN',run,flush=True)
 dump(run/'initial_state.json',{'git_status':subprocess.check_output(['git','status','--short','--branch'],cwd=ROOT,text=True),
  'commit':subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),
  'source_hashes_before_analysis':{p.name:sha(p) for p in HERE.iterdir() if p.is_file()},'cases':CASES})
 print('Hashing protected files',flush=True);before=snapshot();dump(run/'protected_before.json',before)
 status='FAILED';summaries=[]
 try:
  manifest=json.loads((SOURCE/'SHA256_MANIFEST.json').read_text())
  for name,r in manifest.items():assert sha(SOURCE/name)==r['sha256'],name
  dump(run/'Stage2E_integrity_check.json',{'status':'PASS','artifacts':len(manifest)})
  cutoff=F(float(np.fromfile(SOURCE/'cutoff.bin',dtype='<f8')[0]))
  prior=read(SOURCE/'complete_24_problem_table.csv')
  for id in CASES:
   print('RECONSTRUCT',id,flush=True);src=SOURCE/id;out=run/id;out.mkdir()
   X=np.fromfile(src/'X_row_major.bin',dtype='<f8').reshape(1000,101);y=np.fromfile(src/'response.bin',dtype='<f8');lam=np.fromfile(src/'lambda.bin',dtype='<f8')
   hb=np.fromfile(src/'historical_beta.bin',dtype='<f8');ib=np.fromfile(src/'independent_beta.bin',dtype='<f8')
   he=np.fromfile(src/'historical_residual.bin',dtype='<f8');ie=np.fromfile(src/'independent_residual.bin',dtype='<f8')
   hp=np.fromfile(src/'historical_psi.bin',dtype='<f8').reshape(1000,2);ip=np.fromfile(src/'independent_psi.bin',dtype='<f8').reshape(1000,2)
   np.savez(out/'saved_inputs.npz',X=X,y=y,lambda_vector=lam,historical_beta=hb,independent_beta=ib,
    historical_residual=he,independent_residual=ie,historical_psi=hp,independent_psi=ip)
   task=next(r for r in prior if r['id']==id);assert task['classification']=='B'
   try:
    decimal=reconstruct(X,y,lam,ib,ie,F(9,10));literal=reconstruct(X,y,lam,ib,ie,F(float(.9)))
    dump(out/'exact_decimal_optimum.json',decimal);dump(out/'exact_binary_optimum.json',literal)
    assert decimal['beta_numerators']==literal['beta_numerators'] and decimal['beta_denominator']==literal['beta_denominator']
    beta=[F(int(z),int(decimal['beta_denominator'])) for z in decimal['beta_numerators']]
    rounded=np.array([float(b) for b in beta]);rounded.astype('<f8').tofile(out/'exact_optimum_nearest_binary64_beta.bin')
    ranges=[{'quantity':'intercept','index':0,'minimum':float(beta[0]),'maximum':float(beta[0]),'range_proof':'Singleton optimal face (exact certificate)'}]
    ranges.extend({'quantity':'fitted_value','index':i+1,'minimum':float(F(int(v),int(decimal['fitted_denominator']))),
      'maximum':float(F(int(v),int(decimal['fitted_denominator']))),'range_proof':'Singleton optimal face (exact certificate)'} for i,v in enumerate(decimal['fitted_numerators']))
    table(out/'optimal_face_ranges.csv',ranges)
    XX,EX=dyadic(X);YY,EY=dyadic(y);Xi=XX.tolist();yi=YY.tolist();pen=[F(float(z)) for z in lam]
    gaps={}
    for side,b in [('historical',hb),('independent',ib)]:
     g={}
     for label,tau,cert in [('decimal',F(9,10),decimal),('binary',F(float(.9)),literal)]:
      P,e,D,_,_,_,_=exact_objective(Xi,EX,yi,EY,[F(float(z)) for z in b],pen,tau)
      optimum=F(int(cert['primal']['numerator']),int(cert['primal']['denominator']));assert P>=optimum
      g[label]={'primal':record(P),'exact_suboptimality':record(P-optimum)}
     g['maximum_coefficient_error_from_exact_optimum']=float(max(abs(F(float(v))-b0) for v,b0 in zip(b,beta)))
     g['maximum_fitted_error_from_exact_optimum']=float(max(abs(sum(F(float(a))*(F(float(v))-b0) for a,v,b0 in zip(row,b,beta))) for row in X))
     gaps[side]=g
    dump(out/'exact_errors_of_saved_solutions.json',gaps)
    hs=.9-(he<=0).astype(float);Is=.9-(ie<=0).astype(float)
    er=[int(z) for z in decimal['residual_numerators']];os=.9-np.array([r<=0 for r in er]).astype(float)
    inference={'historical':exact_W(hp,hs,cutoff),'independent_layer_A':exact_W(hp,Is,cutoff),
     'independent_complete_path':exact_W(ip,Is,cutoff),
     'exact_optimum_score_fixed_historical_psi':exact_W(hp,os,cutoff),
     'exact_optimum_score_fixed_independent_psi':exact_W(ip,os,cutoff),
     'exact_optimum_scope':'Exact outcome ranks evaluated at saved psi choices; not a newly recomputed complete path at exact beta.'}
    dump(out/'inference.json',inference)
    changed=np.flatnonzero((he<=0)!=(ie<=0));T=set(decimal['tied_observations_one_based'])
    contributions=[]
    for i in range(1000):
     ds=Is[i]-hs[i];dgA=hp[i]*ds;dgProjection=(ip[i]-hp[i])*Is[i]
     dSA=np.outer(hp[i],hp[i])*(Is[i]**2-hs[i]**2)
     dSProjection=(np.outer(ip[i],ip[i])-np.outer(hp[i],hp[i]))*Is[i]**2
     row={'observation':i+1,'historical_residual_R':he[i],'independent_residual_R':ie[i],
      'exact_optimum_residual_is_zero':i+1 in T,'historical_rank':bool(he[i]<=0),'independent_rank':bool(ie[i]<=0),
      'exact_optimum_rank':er[i]<=0,'rank_changed':bool(i in changed),
      'historical_score':hs[i],'independent_score':Is[i],
      'historical_psi1':hp[i,0],'historical_psi2':hp[i,1],
      'independent_psi1':ip[i,0],'independent_psi2':ip[i,1],
      'delta_g1_frozen':dgA[0],'delta_g2_frozen':dgA[1],
      'delta_g1_projection':dgProjection[0],'delta_g2_projection':dgProjection[1],
      'delta_S11_frozen':dSA[0,0],'delta_S12_frozen':dSA[0,1],'delta_S22_frozen':dSA[1,1],
      'delta_S11_projection':dSProjection[0,0],'delta_S12_projection':dSProjection[0,1],'delta_S22_projection':dSProjection[1,1]}
     contributions.append(row)
    table(out/'observation_decomposition.csv',contributions)
    table(out/'changed_observations.csv',[r for r in contributions if r['rank_changed']])
    summary={'id':id,'status':'EXACT_OPTIMUM_RECONSTRUCTED','unique_decimal':decimal['unique_beta_and_fitted_values'],
     'unique_binary':literal['unique_beta_and_fitted_values'],
     'active_coefficients':len(decimal['active_coefficients_zero_based']),
     'exact_zero_residuals':len(decimal['tied_observations_one_based']),
     'changed_observations_one_based':(changed+1).tolist(),'all_changed_observations_exact_optimum_ties':all(i+1 in T for i in changed),
     'historical_W':inference['historical']['W']['float'],'independent_A_W':inference['independent_layer_A']['W']['float'],
     'independent_B_W':inference['independent_complete_path']['W']['float'],
     'classification':'B: unique exact optimum, numerically near-optimal solutions yield different indicators; C residual evaluation may coexist.'}
    dump(out/'summary.json',summary);summaries.append(summary);print(json.dumps(summary),flush=True)
   except Exception as exc:
    result={'id':id,'status':'UNRESOLVED','error':repr(exc)};dump(out/'UNRESOLVED.json',result);summaries.append(result)
    print('UNRESOLVED',id,repr(exc),flush=True)
  dump(run/'case_summaries.json',summaries);status='COMPLETE'
 finally:
  after=snapshot();dump(run/'protected_after.json',after)
  preservation={'status':status,'files_checked':len(before),'changed':[p for p in before if p in after and before[p]!=after[p]],
   'missing':sorted(before.keys()-after.keys()),'added_outside_stage2f':sorted(after.keys()-before.keys())}
  dump(run/'preservation.json',preservation);assert not any(preservation[k] for k in ['changed','missing','added_outside_stage2f'])
  dump(run/'run_status.json',{'status':status,'problems':2});print('PRESERVATION',preservation,flush=True)


if __name__=='__main__':main()
