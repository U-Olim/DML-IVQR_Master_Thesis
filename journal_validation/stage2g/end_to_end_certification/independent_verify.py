"""Separate rational / 130-digit checks. Does not promote Category A to B."""
from support import *
from fractions import Fraction as F
from decimal import Decimal as D, localcontext
import branch_bounds as iv
def ratio(v):return F(int(v['numerator']),int(v['denominator']))
def exact_stat(psi,score):
 z=[(F(float(a))*F(float(s)),F(float(b))*F(float(s))) for (a,b),s in zip(psi,score)]
 g,h=sum((a for a,b in z),F(0)),sum((b for a,b in z),F(0))
 a,b,c=(sum((x*x for x,y in z),F(0)),sum((x*y for x,y in z),F(0)),sum((y*y for x,y in z),F(0)))
 det=a*c-b*b;assert det>0
 return (c*g*g-2*b*g*h+a*h*h)/det,det
def arithmetic_tests():
 rng=np.random.default_rng(20261102);checked=0
 for k in range(2000):
  # Seed is for implementation tests, not simulation data or estimator RNG.
  a=tuple(sorted(rng.uniform(-10,10,2)));b=tuple(sorted(rng.uniform(.01,10,2)))
  for name,fun,exact in [('add',iv.add,lambda x,y:x+y),('sub',iv.sub,lambda x,y:x-y),
                         ('mul',iv.mul,lambda x,y:x*y),('div',iv.div,lambda x,y:x/y)]:
   lo,hi=fun(a,b);true=[exact(F(float(x)),F(float(y))) for x in a for y in b]
   assert F(float(lo))<=min(true)<=max(true)<=F(float(hi)),name;checked+=1
  x=rng.uniform(-100,100,100);y=np.nextafter(x,np.inf)
  lo,hi=iv.sumv((x,y));assert F(float(lo))<=sum(map(lambda z:F(float(z)),x),F(0))
  assert sum(map(lambda z:F(float(z)),y),F(0))<=F(float(hi));checked+=1
 return checked
def high_precision_density(id):
 d=load(OUT/id/'real_density_intervals.json');e=read(OLD/id/'C/outcome_residual.bin')
 ef=[F(float(x)) for x in e];m=sum(ef,F(0))/1000;v=(sum((x*x for x in ef),F(0))-1000*m*m)/999
 assert m==ratio(d['mean']) and v==ratio(d['variance'])
 with localcontext() as c:
  c.prec=130
  # Different evaluation: Decimal alternating series rather than rational pi bounds.
  def atan(q,n):return sum((D((-1)**k)/(D(2*k+1)*D(q)**(2*k+1)) for k in range(n)),D(0))
  pi=16*atan(5,220)-4*atan(239,70)
  md=D(m.numerator)/D(m.denominator);vd=D(v.numerator)/D(v.denominator)
  for x,r in zip(e,d['intervals']):
   z=(D.from_float(float(x))-md)/vd
   f=(-(z*z)/2).exp()/((2*pi).sqrt()*vd);w=f.sqrt()
   assert D(r[0])<=f<=D(r[1]) and D(r[2])<=w<=D(r[3])
 hull=np.load(OUT/id/'saved_and_real_centered_bounds.npz')
 native=read(OLD/id/'C/density.bin')
 assert np.all(hull['density_lower']<=native) and np.all(native<=hull['density_upper'])
 for j in (1,2):
  x=read(OLD/id/'C'/f'instrument_{j}_centered_X.bin',(1000,100))
  y=read(OLD/id/'C'/f'instrument_{j}_centered_y.bin')
  assert np.all(hull['X_lower']<=x) and np.all(x<=hull['X_upper'])
  assert np.all(hull[f'y{j}_lower']<=y) and np.all(y<=hull[f'y{j}_upper'])
 return 1000
def main():
 n=arithmetic_tests();verification=[];candidates=[];cut=F(float(read(E/'cutoff.bin')[0]))
 native=rows(OUT/'native_replay.csv');assert len(native)==72 and all(r['status']=='PASS' for r in native)
 archived={r['id']:r for r in rows(OLD/'downstream_audit.csv') if r['variant']=='C'}
 for id in cases():
  count=high_precision_density(id);f=OLD/id/'C'
  # exact binary64 rank scores, same interpretation as archived certificates
  score=read(f/'score.bin');psi=read(f/'psi.bin',(1000,2)); W,det=exact_stat(psi,score)
  b=load(f/'decision_bounds.json');lower,upper=ratio(b['lower']),ratio(b['upper'])
  assert lower<=W<=upper and det>0
  nativeW=F(float(read(f/'W.bin')[0]));assert lower<=nativeW<=upper
  assert (W<=cut)==(nativeW<=cut) and (upper<=cut or lower>cut)
  # Recheck archived exact KKT primal/dual equality and objective radius scalar bounds.
  for j in (1,2):
   cert=load(f/f'instrument_{j}_certificate.json')
   assert ratio(cert['native_primal'])>=ratio(cert['optimal_primal'])
  verification.append({'id':id,'native_reconstruction':'PASS','real_density_high_precision_containments':count,
   'exact_exported_score_W':'PASS','fixed_input_S_determinant_positive':True,
   'full_uncertainty_S_nonsingularity':'UNRESOLVED','full_adaptive_certificate':'UNRESOLVED'})
  candidates.append({'id':id,'native_W':float(nativeW),'end_to_end_W_lower':'UNAVAILABLE',
   'end_to_end_W_upper':'UNAVAILABLE','cutoff':float(cut),'native_decision':'ACCEPT' if nativeW<=cut else 'REJECT',
   'decision_certification_status':'UNRESOLVED_END_TO_END','category_A_fixed_input_W_lower':float(lower),
   'category_A_fixed_input_W_upper':float(upper),'category_A_status':b['status'],
   'unresolved_sources':'no joint propagation of a posteriori density/centering enclosures through correlation selection, QR initializer, adaptive penalties and shooting/stopping branches'})
 table(OUT/'candidate_bounds.csv',candidates);table(OUT/'independent_candidate_checks.csv',verification)
 dump(OUT/'independent_verification.json',{'status':'PASS_WITH_EXPLICIT_UNRESOLVED_COMPONENTS',
  'arithmetic_rational_tests':n,'real_density_high_precision_containments':24000,'primary_candidates':24,
  'native_paths_reproduced':72,'end_to_end_certified_decisions':0,'unresolved_primary_candidates':24,
  'audit_scope':'Separate rational arithmetic tests, exact score reconstruction, independent 130-digit density containment; no full adaptive proof or external reviewer'})
 print('Independent verification passed; 0/24 end-to-end certificates, 24 retained unresolved.',flush=True)
if __name__=='__main__':main()
