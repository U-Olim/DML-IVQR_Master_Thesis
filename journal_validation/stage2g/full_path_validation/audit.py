"""Independent downstream arithmetic and exact fixed-final-penalty certificates."""
from common import *
from decimal import Decimal,localcontext
import math,time

PI=Decimal('3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628')

def rational_stat(psi,score,cutoff):
 z=[(a*s,b*s) for (a,b),s in zip(psi,score)]
 g=[sum((row[j] for row in z),F(0)) for j in range(2)]
 a=sum((x*x for x,y in z),F(0));b=sum((x*y for x,y in z),F(0));c=sum((y*y for x,y in z),F(0))
 det=a*c-b*b;assert det>0
 W=(c*g[0]**2-2*b*g[0]*g[1]+a*g[1]**2)/det
 return {'g':[record(v) for v in g],'S':[record(a),record(b),record(c)],'W':record(W),'accepted':W<=cutoff}

def sqrt_upper(q,bits=60):
 assert q>=0
 k=math.isqrt((q.numerator<<(2*bits))//q.denominator)
 if F(k*k,1<<(2*bits))<q:k+=1
 return F(k,1<<bits)

def modular_full_rank(Xi):
 prime=1000003;a=np.array([[int(x)%prime for x in row] for row in Xi[:100]],dtype=np.int64);det=1
 for k in range(100):
  rows=np.flatnonzero(a[k:,k]);assert len(rows)>0,'rank witness failed'
  j=k+int(rows[0])
  if j!=k:a[[k,j]]=a[[j,k]];det=-det
  pivot=int(a[k,k]);det=det*pivot%prime;a[k]=(a[k]*pow(pivot,-1,prime))%prime
  if k<99:a[k+1:]=(a[k+1:]-a[k+1:,k,None]*a[k])%prime
 assert det%prime
 return {'prime':prime,'first_100_rows_determinant_mod_prime':int(det%prime),'full_column_rank_proved':True}

def quadratic_values(Xi,EX,yi,EY,b,lam):
 L=math.lcm(*(v.denominator for v in b));bn=[v.numerator*(L//v.denominator) for v in b]
 den=math.lcm((1<<EX)*L,1<<EY)
 en=[y*(den//(1<<EY))-sum(a*v for a,v in zip(row,bn))*(den//((1<<EX)*L)) for row,y in zip(Xi,yi)]
 P=F(sum(v*v for v in en),den*den)+sum(l*abs(v) for l,v in zip(lam,b))
 gradient=[F(2*sum(row[j]*v for row,v in zip(Xi,en)),(1<<EX)*den) for j in range(100)]
 return P,en,den,gradient

def instrument(folder,j,native,unweighted_X,Z):
 prefix=f'instrument_{j}_';xc=readbin(folder/(prefix+'centered_X.bin'),(1000,100));yc=readbin(folder/(prefix+'centered_y.bin'))
 lam=[F(float(v)) for v in readbin(folder/(prefix+'last_penalty.bin'))];cent=readbin(folder/(prefix+'centering.bin'))
 xx,EX=dyadic(xc);yy,EY=dyadic(yc);Xi=xx.tolist();yi=yy.tolist();b0=[F(float(v)) for v in native[1:]]
 P0,en0,d0,g0=quadratic_values(Xi,EX,yi,EY,b0,lam)
 support=np.flatnonzero(native[1:]!=0).tolist()
 Gint=xx.T@xx;rhsint=xx.T@yy
 A=Gint[np.ix_(support,support)].tolist()
 rhs=[F(int(rhsint[j]),1<<(EX+EY))*(1<<(2*EX))-lam[j]*(1 if b0[j]>0 else -1)*(1<<(2*EX))/2 for j in support]
 sol=integer_solve_rational_rhs(A,rhs);b=[F(0)]*100
 for k,v in zip(support,sol):b[k]=v
 P,en,d,grad=quadratic_values(Xi,EX,yi,EY,b,lam)
 assert all((b[k]>0)==(b0[k]>0) and b[k]!=0 for k in support),'Active-sign mismatch'
 assert all(grad[k]==lam[k]*(1 if b[k]>0 else -1) for k in support)
 assert all(abs(grad[k])<=lam[k] for k in range(100) if k not in support),'Inactive KKT failed'
 dual=F(2*sum(a*v for a,v in zip(yi,en)),(1<<EY)*d)-F(sum(v*v for v in en),d*d)
 assert P==dual and P0>=P
 rank=modular_full_rank(Xi)
 # Certified spectral lower bound from an approximate inverse, checked using integers.
 Gfloat=np.array(Gint,dtype=float)/(2.0**(2*EX));R=np.linalg.inv(Gfloat);R=(R+R.T)/2
 rr,ER=dyadic(R);rg=rr@Gint;den=1<<(ER+2*EX)
 error=np.eye(100,dtype=object)*den-rg
 norm=max(max(sum(abs(int(v)) for v in row) for row in error),max(sum(abs(int(v)) for v in row) for row in error.T))
 eta=F(norm,den);Rnorm=F(max(sum(abs(int(v)) for v in row) for row in rr),1<<ER)
 assert eta<1;mu=(1-eta)/Rnorm;radius=sqrt_upper((P0-P)/mu)
 R.astype('<f8').tofile(folder/(prefix+'inverse_gram_witness.bin'))
 mean_y=F(float(cent[0]));mean_x=[F(float(v)) for v in cent[1:]]
 intercept=mean_y-sum(a*v for a,v in zip(mean_x,b));bnative_intercept=mean_y-sum(a*v for a,v in zip(mean_x,b0))
 reference=[F(float(z))-intercept-sum(F(float(a))*v for a,v in zip(row,b)) for row,z in zip(unweighted_X,Z)]
 native_exact=[F(float(z))-F(float(native[0]))-sum(F(float(a))*v for a,v in zip(row,b0)) for row,z in zip(unweighted_X,Z)]
 # Objective region is in centered slopes. Floating intercept and psi arithmetic get a separate envelope.
 saved_psi=readbin(folder/'psi.bin',(1000,2))[:,j-1]
 arithmetic=max(abs(F(float(v))-r) for v,r in zip(saved_psi,native_exact))+abs(F(float(native[0]))-bnative_intercept)
 assert np.all((unweighted_X>=0)&(unweighted_X<=1)) and all(0<=v<=1 for v in mean_x)
 psi_radius=10*radius+arithmetic
 active=set(support)
 kkt0=max(abs(g0[k]-lam[k]*(1 if b0[k]>0 else -1)) if k in active else max(F(0),abs(g0[k])-lam[k]) for k in range(100))
 numerical_residual=readbin(folder/(prefix+'centered_residual.bin'))
 residual_error=max(abs(F(float(v))-F(r,d0)) for v,r in zip(numerical_residual,en0))
 result={'status':'EXACT_FIXED_PENALTY_OPTIMUM','objective_definition':'sum (yc-Xc b)^2 + sum lambda_j abs(b_j); centered binary64 arrays and last-used penalties interpreted exactly',
  'native_primal':record(P0),'optimal_primal':record(P),'optimal_dual':record(dual),'native_true_gap':record(P0-P),
  'native_KKT_max':record(kkt0),'native_R_objective_error':record(abs(P0-F(float(readbin(folder/(prefix+'objective.bin'))[0])))),
  'native_centered_residual_error':record(residual_error),'beta':[record(v) for v in b],'intercept':record(intercept),
  'active':support,'maximum_native_coefficient_error':float(max([abs(a-v) for a,v in zip(b0,b)]+[abs(F(float(native[0]))-intercept)])),
  'minimum_inactive_KKT_margin':record(min(lam[k]-abs(grad[k]) for k in range(100) if k not in active)),
  'rank_certificate':rank,'approximate_inverse_residual_bound':record(eta),'approximate_inverse_norm_bound':record(Rnorm),'gram_min_eigenvalue_lower_bound':record(mu),
  'coefficient_L2_radius_for_native_objective_sublevel':record(radius),'psi_uniform_radius':record(psi_radius),'floating_psi_and_intercept_envelope':record(arithmetic),
  'native_psi_arithmetic_error':float(max(abs(F(float(v))-r) for v,r in zip(saved_psi,native_exact))),
  'design_condition_diagnostic':float(np.linalg.cond(xc)), 'scope':'Fixed exported density, centered design, mean values and final penalties. No adaptive fixed-point or density-error propagation claim.'}
 dump(folder/(prefix+'certificate.json'),result)
 return result,reference,psi_radius

def add(a,b):return a[0]+b[0],a[1]+b[1]
def mul(a,b):
 v=[a[i]*b[j] for i in [0,1] for j in [0,1]];return min(v),max(v)
def scale(a,v):return mul(a,(v,v))
def square(a):return (F(0) if a[0]<=0<=a[1] else min(a[0]**2,a[1]**2),max(a[0]**2,a[1]**2))
def sub(a,b):return a[0]-b[1],a[1]-b[0]

def bound_W(psi,radii,scores,cutoff):
 g=[(F(0),F(0))]*2;S=[(F(0),F(0))]*3
 for (a,b),s in zip(psi,scores):
  u=scale((a-radii[0],a+radii[0]),s);v=scale((b-radii[1],b+radii[1]),s)
  g=[add(g[0],u),add(g[1],v)];S=[add(S[0],square(u)),add(S[1],mul(u,v)),add(S[2],square(v))]
 det=sub(mul(S[0],S[2]),square(S[1]))
 if det[0]<=0:return {'status':'INCONCLUSIVE_DETERMINANT'}
 num=add(sub(mul(S[2],square(g[0])),scale(mul(S[1],mul(g[0],g[1])),F(2))),mul(S[0],square(g[1])))
 lo=max(F(0),num[0]/det[1]);hi=max(F(0),num[1]/det[0])
 status='ACCEPT_CERTIFIED' if hi<=cutoff else 'REJECT_CERTIFIED' if lo>cutoff else 'UNRESOLVED'
 return {'status':status,'lower':record(lo),'upper':record(hi),'determinant_lower':record(det[0]),'scope':'Both fixed-final-penalty objective sublevels F_j(b)<=F_j(native), exact centered-mean mapping, with declared floating psi/intercept envelope; fixed ranks.'}

def density_check(e,f,params):
 with localcontext() as ctx:
  ctx.prec=80;d=[Decimal(float(v)) for v in e];n=Decimal(len(d));mean=sum(d)/n;var=sum((v-mean)**2 for v in d)/(n-1)
  normalizer=var*(2*PI).sqrt();values=[(-((v-mean)/var)**2/2).exp()/normalizer for v in d]
  err=max(abs(Decimal(float(a))-b)/abs(b) for a,b in zip(f,values))
  return {'precision_digits':80,'method':'Decimal exp and sqrt; 84-digit pi constant; independent unrounded mean/variance of exported residuals','relative_error_max':float(err),'mean_error':float(abs(Decimal(float(params[0]))-mean)),'variance_error':float(abs(Decimal(float(params[1]))-var)),'passed':bool(err<=Decimal('1e-12')),'rigorous_interval_certificate':False}

def main():
 start=time.perf_counter();tasks=list(csv.DictReader((OUT/'tasks.csv').open()));rows=[]
 cutoff=F(float(readbin(E/'cutoff.bin')[0]))
 for task in tasks:
  id=task['id'];name=task['variant'];folder=OUT/id/name;t=time.perf_counter()
  if (folder/'FAILURE.txt').exists():rows.append({'id':id,'variant':name,'status':'NATIVE_FAILURE'});continue
  e=readbin(folder/'outcome_residual.bin');r=readbin(folder/'rank.bin');s=readbin(folder/'score.bin');psi=readbin(folder/'psi.bin',(1000,2))
  assert np.array_equal(s,.9-r)
  cert=json.loads((folder/'outcome_certificate.json').read_text());exact_e=[F(int(v),int(cert['residual_denominator'])) for v in cert['residual_numerators']]
  assert all(float(a)==b and (a<=0)==bool(c) for a,b,c in zip(exact_e,e,r))
  density=density_check(e,readbin(folder/'density.bin'),readbin(folder/'density_parameters.bin'));assert density['passed'];dump(folder/'density_validation.json',density)
  inf=exact_W(psi,s,cutoff);native_W=float(readbin(folder/'W.bin')[0]);Werr=abs(native_W-inf['W']['float']);assert Werr<=1e-10*(1+abs(native_W))
  moment=readbin(folder/'second_moment.bin',(2,2));inv=readbin(folder/'inverse.bin',(2,2))
  obs=psi*s[:,None];assert np.allclose(obs,readbin(folder/'observation_scores.bin',(1000,2)),rtol=0,atol=0)
  exactS=np.array([[inf['S11']['float'],inf['S12']['float']],[inf['S12']['float'],inf['S22']['float']]])
  exactg=np.array([inf['score_sum_1']['float'],inf['score_sum_2']['float']])
  checks={'W_absolute_error':Werr,'S_absolute_error':float(np.max(abs(moment-exactS))),'g_absolute_error':float(np.max(abs(readbin(folder/'score_sum.bin')-exactg))),
   'condition_2':float(np.linalg.cond(moment)),'inverse_residual_inf':float(np.linalg.norm(moment@inv-np.eye(2),ord=np.inf)),'exact_conditional_inference':inf}
  dump(folder/'inference_validation.json',checks)
  X=readbin(E/id/'X_row_major.bin',(1000,101))[:,1:];Z=readbin(OUT/id/'C/Z_row_major.bin',(1000,2));coef=readbin(folder/'instrument_coefficients.bin',(101,2))
  instruments=[];references=[];radii=[];failures=[]
  for j in [1,2]:
   try:
    rec,ref,rad=instrument(folder,j,coef[:,j-1],X,Z[:,j-1]);instruments.append(rec);references.append(ref);radii.append(rad)
   except Exception as exc:
    failures.append({'instrument':j,'error':repr(exc)});dump(folder/f'instrument_{j}_UNRESOLVED.json',failures[-1])
  bounds={'status':'UNRESOLVED_INSTRUMENT'};refinf=None
  if not failures:
   refpsi=list(zip(*references));scores=[F(float(v)) for v in s]
   refinf=rational_stat(refpsi,scores,cutoff);bounds=bound_W(refpsi,radii,scores,cutoff)
   dump(folder/'fixed_penalty_reference_inference.json',refinf)
  dump(folder/'decision_bounds.json',bounds)
  row={'id':id,'variant':name,'status':'PASS' if not failures else 'PARTIAL','density_relative_error':density['relative_error_max'],
   'W':inf['W']['float'],'accepted':inf['accepted'],'W_R_error':Werr,'S_condition':checks['condition_2'],'inverse_residual':checks['inverse_residual_inf'],
   'instrument_optima_certified':len(instruments),'instrument_max_true_gap':max((z['native_true_gap']['float'] for z in instruments),default=None),
   'instrument_max_coefficient_error':max((z['maximum_native_coefficient_error'] for z in instruments),default=None),
   'decision_bound_status':bounds['status'],'W_lower':bounds.get('lower',{}).get('float'),'W_upper':bounds.get('upper',{}).get('float'),
   'fixed_penalty_reference_W':refinf['W']['float'] if refinf else None,'fixed_penalty_reference_accepted':refinf['accepted'] if refinf else None,'seconds':time.perf_counter()-t}
  rows.append(row);print('AUDIT',id,name,row['status'],bounds['status'],'seconds',row['seconds'],flush=True)
 table(OUT/'downstream_audit.csv',rows);dump(OUT/'audit_run.json',{'paths':len(rows),'seconds':time.perf_counter()-start,'failed_or_partial':sum(r['status']!='PASS' for r in rows)})
if __name__=='__main__':main()
