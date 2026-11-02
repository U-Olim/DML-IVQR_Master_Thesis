"""Outward intervals for the REAL historical formula, not a libm error theorem.

Decimal exp/sqrt are correctly rounded to nearest; one Decimal neighbor on
each side encloses them. Rational sums give exact mean and sample variance.
Pi is bounded by Machin's identity and alternating-series remainder bounds.
The distinction between this target and native R arithmetic is intentional.
"""
from support import *
from fractions import Fraction as F
from decimal import Decimal as D, localcontext, ROUND_FLOOR, ROUND_CEILING
PREC=90
def fd(x,rounding):
 with localcontext() as c:
  c.prec=PREC;c.rounding=rounding
  return D(x.numerator)/D(x.denominator)
def rational(x):return fd(x,ROUND_FLOOR),fd(x,ROUND_CEILING)
def op(a,b,kind):
 values=[]
 for rnd in (ROUND_FLOOR,ROUND_CEILING):
  with localcontext() as c:
   c.prec=PREC;c.rounding=rnd
   values.append([{'add':lambda:x+y,'mul':lambda:x*y,'div':lambda:x/y}[kind]() for x in a for y in b])
 return min(values[0]),max(values[1])
def add(a,b):return op(a,b,'add')
def mul(a,b):return op(a,b,'mul')
def neg(a):return a[1].copy_negate(),a[0].copy_negate()
def sub(a,b):return add(a,neg(b))
def div(a,b):
 assert b[0]>0
 return op(a,b,'div')
def square(a):
 v=mul(a,a)
 return (D(0) if a[0]<=0<=a[1] else v[0]),v[1]
def unary(a,method):
 with localcontext() as c:
  c.prec=PREC
  return getattr(a[0],method)().next_minus(),getattr(a[1],method)().next_plus()
def atan(q,n):
 s=sum((F((-1)**k,(2*k+1)*q**(2*k+1)) for k in range(n)),F(0))
 t=F((-1)**n,(2*n+1)*q**(2*n+1))
 return min(s,s+t),max(s,s+t)
def pi_bounds():
 a,b=atan(5,110),atan(239,32)
 return rational(16*a[0]-4*b[1])[0],rational(16*a[1]-4*b[0])[1]
def exact_parameters(e):
 v=[F(float(z)) for z in e]; m=sum(v,F(0))/len(v)
 var=sum(((x-m)**2 for x in v),F(0))/(len(v)-1)
 return m,var
def bounds(e):
 m,v=exact_parameters(e);mi,vi=rational(m),rational(v)
 norm=mul(unary(mul((D(2),D(2)),pi_bounds()),'sqrt'),vi)
 result=[]
 for x in e:
  z=div(sub(rational(F(float(x))),mi),vi)
  exponent=mul((D('-.5'),D('-.5')),square(z))
  f=div(unary(exponent,'exp'),norm);w=unary(f,'sqrt')
  result.append([str(f[0]),str(f[1]),str(w[0]),str(w[1])])
 return m,v,result
def main():
 from branch_bounds import mul as imul, sub as isub, sumv, div as idiv, point, down, up
 summary=[]
 for id in cases():
  folder=OLD/id/'C'; e=read(folder/'outcome_residual.bin'); native=read(folder/'density.bin')
  m,v,b=bounds(e)
  contained=[D.from_float(float(z))>=D(r[0]) and D.from_float(float(z))<=D(r[1]) for z,r in zip(native,b)]
  diff=max(float(abs(D.from_float(float(z))-(D(r[0])+D(r[1]))/2)/D(r[0])) for z,r in zip(native,b))
  dump(OUT/id/'real_density_intervals.json',{'scope':'REAL_FORMULA_ON_EXPORTED_BINARY64_RESIDUALS_NOT_NATIVE_R_ERROR_BOUNDS',
   'precision':PREC,'mean':{'numerator':str(m.numerator),'denominator':str(m.denominator)},
   'variance':{'numerator':str(v.numerator),'denominator':str(v.denominator)},
   'columns':['density_lower','density_upper','sqrt_lower','sqrt_upper'],'intervals':b})
  # Extend the ideal-real-formula enclosure through sqrt, weighting and centering.
  # These arrays do NOT enclose every implementation of native dnorm.
  weights=(down(np.array([float(r[2]) for r in b])),up(np.array([float(r[3]) for r in b])))
  X=read(E/id/'X_row_major.bin',(1000,101))[:,1:]
  Z=read(folder/'Z_row_major.bin',(1000,2))
  wx=imul((weights[0][:,None],weights[1][:,None]),point(X))
  means=[idiv(sumv((wx[0][:,j],wx[1][:,j])),point(1000.)) for j in range(100)]
  mx=(np.array([r[0] for r in means]),np.array([r[1] for r in means]))
  xc=isub(wx,mx); store={'X_lower':xc[0],'X_upper':xc[1],'means_lower':mx[0],'means_upper':mx[1]}
  centered_native_misses=0
  for j in (1,2):
   yw=imul(weights,point(Z[:,j-1]));my=idiv(sumv(yw),point(1000.));yc=isub(yw,my)
   store.update({f'y{j}_lower':yc[0],f'y{j}_upper':yc[1]})
   native_x=read(folder/f'instrument_{j}_centered_X.bin',(1000,100))
   centered_native_misses+=int(np.sum((native_x<xc[0])|(native_x>xc[1])))
  np.savez_compressed(OUT/id/'ideal_real_centered_bounds.npz',**store)
  # A posteriori fixed-residual enclosure: exact-real density AND the actual
  # executed binary64 density. This is a measured, rigorous error enclosure
  # at these fixed inputs, not a universal dnorm/libm specification.
  fl=down(np.array([min(float(r[0]),float(z)) for r,z in zip(b,native)]))
  fh=up(np.array([max(float(r[1]),float(z)) for r,z in zip(b,native)]))
  wl,wh=down(np.sqrt(fl)),up(np.sqrt(fh))
  hx=imul((wl[:,None],wh[:,None]),point(X))
  hm=[idiv(sumv((hx[0][:,j],hx[1][:,j])),point(1000.)) for j in range(100)]
  hmx=(np.array([r[0] for r in hm]),np.array([r[1] for r in hm]));hc=isub(hx,hmx)
  hull={'density_lower':fl,'density_upper':fh,'weight_lower':wl,'weight_upper':wh,
        'X_lower':hc[0],'X_upper':hc[1],'means_lower':hmx[0],'means_upper':hmx[1]}
  hull_misses=0
  for j in (1,2):
   hy=imul((wl,wh),point(Z[:,j-1]));mu=idiv(sumv(hy),point(1000.));cy=isub(hy,mu)
   hull.update({f'y{j}_lower':cy[0],f'y{j}_upper':cy[1]})
   nx=read(folder/f'instrument_{j}_centered_X.bin',(1000,100));ny=read(folder/f'instrument_{j}_centered_y.bin')
   hull_misses+=int(np.sum((nx<hc[0])|(nx>hc[1])))+int(np.sum((ny<cy[0])|(ny>cy[1])))
  assert hull_misses==0
  np.savez_compressed(OUT/id/'saved_and_real_centered_bounds.npz',**hull)
  native_params=read(folder/'density_parameters.bin')
  summary.append({'id':id,'real_formula_status':'OUTWARD_BOUNDED','native_values_inside_real_formula_intervals':sum(contained),
   'observations':len(e),'native_relative_deviation':diff,'native_libm_error_bound':'UNRESOLVED',
   'native_mean_variance_rounding':'UNRESOLVED','native_weighted_centering_rounding':'UNRESOLVED',
   'ideal_real_centered_design_status':'OUTWARD_BOUNDED','native_centered_entries_outside_ideal_bounds':centered_native_misses})
  summary[-1].update({'saved_density_error_enclosure':'RIGOROUS_A_POSTERIORI_AT_FIXED_RESIDUALS',
   'saved_and_real_centered_containment_misses':hull_misses,
   'saved_mean_absolute_error':float(abs(F(float(native_params[0]))-m)),
   'saved_variance_absolute_error':float(abs(F(float(native_params[1]))-v)),
   'density_hull_max_width':float(np.max(fh-fl)),'centered_X_hull_max_width':float(np.max(hc[1]-hc[0]))})
  print(id,'real-density bounds complete; native libm/aggregation proof unresolved',flush=True)
 table(OUT/'density_summary.csv',summary)
if __name__=='__main__':main()
