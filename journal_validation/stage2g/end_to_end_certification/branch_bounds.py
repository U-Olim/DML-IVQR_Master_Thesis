"""Category A only: outward binary64 shooting bounds at fixed exported inputs.

Every shooting call starts at its exported native initializer. No propagated
claim about QR initialization, density, centering, or adaptive penalties is made.
Ambiguous comparisons stop certification of that call, never pick a branch.
"""
from support import *
down=lambda x:np.nextafter(x,-np.inf)
up=lambda x:np.nextafter(x,np.inf)
def add(a,b):return down(a[0]+b[0]),up(a[1]+b[1])
def sub(a,b):return down(a[0]-b[1]),up(a[1]-b[0])
def mul(a,b):
 v=np.stack([a[0]*b[0],a[0]*b[1],a[1]*b[0],a[1]*b[1]])
 return down(np.min(v,axis=0)),up(np.max(v,axis=0))
def div(a,b):
 assert np.all(b[0]>0)
 return mul(a,(down(1/b[1]),up(1/b[0])))
def sumv(a):
 # gamma_(n-1) covers any ordinary reduction tree; enlarge n to 2n+2
 # and include one extra final rounding for R's extended-precision sum.
 n=a[0].size;u=2.**-53;k=2*n+2;g=up((k*u)/(1-k*u))
 ab=up(np.sum(np.maximum(abs(a[0]),abs(a[1])))/(1-(n+1)*u))
 error=up(g*ab)
 return down(np.sum(a[0])-error),up(np.sum(a[1])+error)
def absolute(a):
 return np.where((a[0]<=0)&(a[1]>=0),0,np.minimum(abs(a[0]),abs(a[1]))),up(np.maximum(abs(a[0]),abs(a[1])))
def point(x):return np.asarray(x),np.asarray(x)
def call_bound(rec):
 d=OUT/rec['id']; p=rec['prefix']; sweeps=int(rec['sweeps'])
 xx=read(d/(p+'XX.bin'),(100,100));xy=read(d/(p+'Xy.bin'))
 lam=read(d/(p+'lambda.bin'));hist=read(d/(p+'iterates.bin'),(100,sweeps+1))
 final=read(d/(p+'final.bin')); xx2=xx*2;xy2=xy*2
 lo=hist[:,0].copy();hi=lo.copy(); checked=0;failure=None;containment=True
 for t in range(sweeps):
  prev=(lo.copy(),hi.copy())
  for j in range(100):
   s=sub(sub(sumv(mul(point(xx2[j]),(lo,hi))),mul(point(xx2[j,j]),(lo[j],hi[j]))),point(xy2[j]))
   if s[0]>lam[j]:v=div(sub(point(lam[j]),s),point(xx2[j,j]))
   elif s[1]<-lam[j]:v=div(sub(point(-lam[j]),s),point(xx2[j,j]))
   elif s[0]>=-lam[j] and s[1]<=lam[j]:v=(0.,0.)
   else:failure={'kind':'SOFT_THRESHOLD_BRANCH','sweep':t+1,'coordinate':j+1,'S0_lower':float(s[0]),'S0_upper':float(s[1]),'lambda':float(lam[j])};break
   lo[j],hi[j]=v;checked+=1
  if failure:break
  containment=bool(containment and np.all(lo<=hist[:,t+1]) and np.all(hist[:,t+1]<=hi))
  if not containment:raise AssertionError(('Native iterate outside fixed-input enclosure',rec,t))
  change=sumv(absolute(sub((lo,hi),prev)))
  native_stop=t==sweeps-1 and int(rec['reported_iterations'])<1000
  if not (change[1]<1e-5 if native_stop else change[0]>=1e-5):
   failure={'kind':'INNER_STOPPING_BRANCH','sweep':t+1,'change_lower':float(change[0]),'change_upper':float(change[1]),'threshold':1e-5};break
 if not failure:
  for j in range(100):
   a=absolute((lo[j],hi[j]))
   if a[1]<1e-6:lo[j]=hi[j]=0
   elif a[0]>=1e-6:pass
   else:failure={'kind':'FINAL_ZERO_THRESHOLD','coordinate':j+1,'absolute_lower':float(a[0]),'absolute_upper':float(a[1]),'threshold':1e-6};break
 if not failure:
  assert np.all(lo<=final) and np.all(final<=hi)
 status='A_FIXED_INPUT_SHOOTING_CERTIFIED' if not failure else 'C_FIXED_INPUT_SHOOTING_UNRESOLVED'
 result={'id':rec['id'],'instrument':int(rec['instrument']),'call':int(rec['call']),'status':status,
  'coordinates_certified':checked,'sweeps':sweeps,'native_containment_until_stop':containment,
  'max_coefficient_width_at_stop':float(np.max(hi-lo)),
  'full_adaptive_status':'UNRESOLVED_DENSITY_CENTERING_QR_AND_PENALTY_INPUTS','first_uncertain_branch':failure}
 dump(d/(p+'interval_result.json'),result)
 return result
def main():
 results=[call_bound(r) for r in rows(OUT/'shooting_calls.csv')]
 dump(OUT/'branch_analysis.json',{'scope':'A_FIXED_EXPORTED_GRAM_XY_LAMBDA_AND_INITIAL_COEFFICIENTS_ONLY',
  'rounding_model':'IEEE binary64 basic ops, finite normal inputs, no flush-to-zero; conservative sum gamma bound',
  'fully_adaptive_certificates':0,'calls':results})
 table(OUT/'branch_summary.csv',[{k:v for k,v in r.items() if k!='first_uncertain_branch'}|{'first_uncertain_branch':json.dumps(r['first_uncertain_branch'])} for r in results])
 print('Calls',len(results),'fixed-input certificates',sum(r['status']=='A_FIXED_INPUT_SHOOTING_CERTIFIED' for r in results),flush=True)
if __name__=='__main__':main()
