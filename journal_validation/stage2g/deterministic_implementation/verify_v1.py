"""Independent direct rational residual / KKT / primal-dual / moment audit.

No optimizer or active-set reconstruction is called. Intervals are reassembled
with exact fractions; this audit is for version B's fixed final objectives.
"""
from common_v1 import *
sys.path.insert(0,str(G/'full_path_validation'))
from verify_certificates import plus,times,minus,squared
import importlib.util
spec=importlib.util.spec_from_file_location('independent_fraction_elimination',ROOT/'journal_validation/stage2f/verify.py')
elim=importlib.util.module_from_spec(spec);spec.loader.exec_module(elim)
def stat(psi,scores):
 z=[tuple(a*s for a in row) for row,s in zip(psi,scores)]
 g0=sum((a for a,b in z),F(0));g1=sum((b for a,b in z),F(0))
 a=sum((x*x for x,y in z),F(0));b=sum((x*y for x,y in z),F(0));c=sum((y*y for x,y in z),F(0));det=a*c-b*b
 assert det>0
 return (c*g0*g0-2*b*g0*g1+a*g1*g1)/det,[g0,g1,a,b,c]
def verify_outcome(id):
 f=OUT/id;c=load(f/'outcome_certificate.json');Xf=read(E/id/'X_row_major.bin',(1000,101))
 X=[[F(float(v)) for v in row] for row in Xf];y=[F(float(v)) for v in read(E/id/'response.bin')]
 lam=[F(float(v)) for v in read(E/id/'lambda.bin')];tau=val(c['tau']);b=[F(int(v),int(c['beta_denominator'])) for v in c['beta_numerators']]
 v=[F(int(z),int(c['dual_denominator'])) for z in c['dual_numerators']];support=[j for j,z in enumerate(b) if z]
 e=[a-sum((row[j]*b[j] for j in support),F(0)) for row,a in zip(X,y)]
 assert e==[F(int(z),int(c['residual_denominator'])) for z in c['residual_numerators']]
 P=sum(((tau if z>=0 else tau-1)*z for z in e),F(0))+sum(l*abs(z)/2 for l,z in zip(lam,b))
 assert all(tau-1<=z<=tau for z in v)
 grad=[sum((row[j]*z for row,z in zip(X,v)),F(0)) for j in range(101)]
 assert all(abs(g)<=l/2 for g,l in zip(grad,lam));dual=sum(a*z for a,z in zip(y,v))
 assert P==dual==val(c['primal'])==val(c['dual'])
 assert all(grad[j]==lam[j]*(1 if b[j]>0 else -1)/2 for j in support)
 ties=[i for i,z in enumerate(e) if not z];inactive=[j for j,z in enumerate(b) if not z]
 assert all(tau-1<v[i]<tau for i in ties) and all(abs(grad[j])<lam[j]/2 for j in inactive)
 determinant=elim.det_fraction([[X[i][j] for j in support] for i in ties]);assert determinant!=0
 assert np.array_equal(read(f/'rank.bin'),[z<=0 for z in e])
 assert all(float(a)==z for a,z in zip(e,read(f/'outcome_residual.bin')))
 return X
def verify_instruments(id,X):
 f=OUT/id;coeff=read(f/'instrument_coefficients.bin',(101,2));psi=read(f/'psi.bin',(1000,2));Z=read(f/'Z_row_major.bin',(1000,2));refs=[];radii=[]
 for j in (1,2):
  prefix=f'instrument_{j}_';c=load(f/(prefix+'certificate.json'))
  xf=read(f/(prefix+'centered_X.bin'),(1000,100));yf=read(f/(prefix+'centered_y.bin'));lam=[F(float(v)) for v in read(f/(prefix+'last_penalty.bin'))]
  assert np.array_equal(read(f/(prefix+'last_penalty.bin')),read(OLD/id/'C'/(prefix+'last_penalty.bin')))
  XR=[[F(float(v)) for v in row] for row in xf];yr=[F(float(v)) for v in yf];b=[val(v) for v in c['beta']];active=[k for k,z in enumerate(b) if z]
  r=[a-sum((row[k]*b[k] for k in active),F(0)) for row,a in zip(XR,yr)]
  gradient=[2*sum((row[k]*z for row,z in zip(XR,r)),F(0)) for k in range(100)]
  assert all(gradient[k]==lam[k]*(1 if b[k]>0 else -1) if b[k] else abs(gradient[k])<=lam[k] for k in range(100))
  P=sum(z*z for z in r)+sum(l*abs(z) for l,z in zip(lam,b));D=2*sum(a*z for a,z in zip(yr,r))-sum(z*z for z in r)
  assert P==D==val(c['optimal_primal'])==val(c['optimal_dual'])
  native=[F(float(v)) for v in coeff[1:,j-1]];rn=[a-sum((row[k]*native[k] for k in active),F(0)) for row,a in zip(XR,yr)]
  pn=sum(z*z for z in rn)+sum(l*abs(z) for l,z in zip(lam,native))
  assert pn==val(c['returned_primal']) and pn-P==val(c['returned_true_gap'])>=0
  xi,EX=dyadic(xf);ri,ER=dyadic(read(f/(prefix+'inverse_gram_witness.bin'),(100,100)))
  den=1<<(EX*2+ER);err=np.eye(100,dtype=object)*den-ri@(xi.T@xi)
  eta=F(max(max(sum(abs(int(z)) for z in row) for row in err),max(sum(abs(int(z)) for z in row) for row in err.T)),den)
  norm=F(max(sum(abs(int(z)) for z in row) for row in ri),1<<ER)
  assert eta<1 and eta==val(c['inverse_residual_bound']) and norm==val(c['inverse_norm_bound'])
  mu=(1-eta)/norm;assert mu==val(c['gram_min_eigenvalue_lower_bound'])>0
  radius=val(c['coefficient_L2_radius']);assert radius*radius*mu>=pn-P
  means=[F(float(v)) for v in read(f/(prefix+'centering.bin'))]
  intercept=means[0]-sum(a*z for a,z in zip(means[1:],b));assert intercept==val(c['intercept'])
  ref=[F(float(z))-intercept-sum((row[k+1]*b[k] for k in active),F(0)) for row,z in zip(X,Z[:,j-1])]
  literal=[F(float(z))-F(float(coeff[0,j-1]))-sum((row[k+1]*native[k] for k in active),F(0)) for row,z in zip(X,Z[:,j-1])]
  rounding=max(abs(F(float(z))-a) for z,a in zip(psi[:,j-1],literal))
  rounding+=abs(F(float(coeff[0,j-1]))-(means[0]-sum(a*z for a,z in zip(means[1:],native))))
  assert rounding==val(c['psi_rounding_envelope'])
  rownorm=val(c['psi_mapping_row_norm_bound']);assert rownorm*rownorm>=100
  assert rownorm*radius+rounding==val(c['psi_uniform_radius'])
  refs.append(ref);radii.append(rownorm*radius+rounding)
 scores=[F(float(v)) for v in read(f/'score.bin')];refpsi=list(zip(*refs));cut=F(float(read(E/'cutoff.bin')[0]))
 W,_=stat([[F(float(v)) for v in row] for row in psi],scores);refW,_=stat(refpsi,scores)
 assert W==val(load(f/'exact_returned_score_inference.json')['W'])
 sums=[(F(0),F(0)) for _ in range(5)]
 for (a,b),s in zip(refpsi,scores):
  u=times((a-radii[0],a+radii[0]),(s,s));v=times((b-radii[1],b+radii[1]),(s,s))
  for k,z in enumerate([u,v,squared(u),times(u,v),squared(v)]):sums[k]=plus(sums[k],z)
 g,h,a,b,c=sums;det=minus(times(a,c),squared(b));assert det[0]>0
 num=plus(minus(times(c,squared(g)),times((F(2),F(2)),times(b,times(g,h)))),times(a,squared(h)))
 lo=max(F(0),num[0]/det[1]);hi=max(F(0),num[1]/det[0]);bound=load(f/'decision_bounds.json')
 assert lo==val(bound['lower']) and hi==val(bound['upper'])
 assert lo<=W<=hi and lo<=refW<=hi and lo<=F(float(read(f/'W.bin')[0]))<=hi
 assert hi<=cut or lo>cut
 return float(hi-lo)
def main():
 results=[];start=time.perf_counter()
 for row in rows(OUT/'candidate_comparison.csv'):
  id=row['id'];t=time.perf_counter()
  if row['status']!='PASS':results.append({'id':id,'status':'UNRESOLVED_RETAINED'});continue
  X=verify_outcome(id);width=verify_instruments(id,X)
  result={'id':id,'status':'PASS','outcome_unique_and_signs_exact':True,'fixed_instrument_optima_verified':2,
   'score_nonsingularity_over_fixed_objective_regions':True,'W_interval_width':width,'seconds':time.perf_counter()-t}
  results.append(result);dump(OUT/id/'independent_verification.json',result);print('VERIFIED',id,'PASS',flush=True)
 table(OUT/'independent_verification.csv',results)
 dump(OUT/'independent_verification.json',{'paths':24,'passed':sum(r['status']=='PASS' for r in results),
  'unresolved':sum(r['status']!='PASS' for r in results),'seconds':time.perf_counter()-start,
  'scope':'New LP optimum/signs and new final fixed-penalty objectives / inference; no historical exhaustive adaptive interval requirement'})
if __name__=='__main__':main()
