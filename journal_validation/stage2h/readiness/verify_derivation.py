"""Scalar quadrature/identity checks only; no bounded-DGP data generator."""
from common_h0 import *
from scipy.stats import norm
from scipy.integrate import quad
import math
delta=.05;c=.9;rho=.3
def expectation(fn,mu,sd):
 return quad(lambda z:fn(mu+sd*z)*norm.pdf(z),-12,12,epsabs=1e-10,epsrel=1e-10,limit=300)
def main():
 results=[]
 for tau in (.1,.5,.9):
  q=norm.ppf(tau);phi=norm.pdf(q)
  assert abs(norm.cdf(q)-tau)<1e-14
  # Integrands are scalar formula checks, not transformed sample arrays.
  h=lambda t:1/(delta+c*norm.cdf(t))
  hp=lambda t:-c*norm.pdf(t)/(delta+c*norm.cdf(t))**2
  H,err=expectation(h,rho*q,math.sqrt(3-rho*rho))
  Hp,e2=expectation(hp,rho*q,math.sqrt(3-rho*rho))
  assert 1/.95<=H<=20 and Hp<0
  for kappa in (1.,.1):
   v=3-kappa*kappa;sigma=math.sqrt(1-rho*rho/v)
   for total_Q in (-4.,0.,4.):
    mu=kappa*total_Q/2;sd=math.sqrt(v-rho*rho)
    conditional_H,error=expectation(h,mu+rho*q,sd)
    density=phi*conditional_H;lower=phi/.95;upper=phi/.05
    assert lower<=density<=upper
    # Independently integrate the full conditioning formula over T|Q.
    def direct(t):
     m=rho*(t-mu)/v
     return norm.pdf((q-m)/sigma)/(sigma*(delta+c*norm.cdf(t)))
    other,other_error=expectation(direct,mu,math.sqrt(v))
    assert abs(other-density)<1e-8
    rank_probability,rank_error=expectation(lambda t:norm.cdf((q-rho*(t-mu)/v)/sigma),mu,math.sqrt(v))
    assert abs(rank_probability-tau)<1e-12
    stein,e3=expectation(lambda t:(t-rho*q)*h(t),rho*q,math.sqrt(3-rho*rho))
    direct_J=phi*kappa*stein/((3-rho*rho)*H)
    assert abs(direct_J-phi*kappa*Hp/H)<1e-10
    results.append({'tau':tau,'kappa':kappa,'Q1_plus_Q2':total_Q,'mixed_density_at_zero':density,
     'lower_bound':lower,'upper_bound':upper,'direct_integral_difference':abs(other-density),
     'quadrature_error_estimate':max(error,other_error),'conditional_rank_probability':rank_probability,
     'rank_probability_error':abs(rank_probability-tau),'local_profile_Jacobian_per_instrument':phi*kappa*Hp/H,
     'independent_Stein_Jacobian_difference':abs(direct_J-phi*kappa*Hp/H)})
 variance=math.asin(.75)/(2*math.pi)
 phi_mean,error=expectation(lambda t:norm.pdf(t),0,math.sqrt(3));assert abs(phi_mean-1/(2*math.sqrt(2*math.pi)))<1e-12
 mean,e1=expectation(lambda t:delta+c*norm.cdf(t),0,math.sqrt(3))
 second,e2=expectation(lambda t:(delta+c*norm.cdf(t))**2,0,math.sqrt(3))
 assert abs(mean-.5)<1e-12 and abs(second-mean**2-c*c*variance)<1e-12
 # Verify inverse transformation/CDF algebra at deterministic scalar points.
 inversion=[]
 for t in (-4.,-1.,0.,1.,4.):
  d=delta+c*norm.cdf(t);recovered=norm.ppf((d-delta)/c)
  assert abs(t-recovered)<1e-10
  inversion.append({'T_scalar':t,'CDF':float(norm.cdf(recovered/math.sqrt(3))),'inverse_error':abs(t-recovered)})
 original=[]
 for kappa in (1.,.1):
  sd=math.sqrt(3-kappa*kappa-rho*rho)
  for L in (4,6,8,10):
   value,error=quad(lambda t:math.exp(norm.logpdf(t,scale=sd)-norm.logcdf(t)),-L,0,epsrel=1e-10,limit=300)
   original.append({'kappa':kappa,'left_truncation':-L,'original_negative_tail_inverse_D_integral':value,
    'scope':'finite truncation illustrates the analytically proved divergent tail; not itself a divergence certificate'})
 table(OUT/'original_density_tail_checks.csv',original)
 table(OUT/'analytical_density_checks.csv',results);table(OUT/'distribution_identity_checks.csv',inversion)
 dump(OUT/'analytical_verification.json',{'status':'PASS','scalar_density_cases':len(results),
  'delta':delta,'structural_effects':{str(t):1+norm.ppf(t) for t in (.1,.5,.9)},
  'common_mixed_density_lower':norm.pdf(norm.ppf(.1))/.95,'common_mixed_density_upper':norm.pdf(0)/.05,
  'full_conditioning_uniform_lower_bound':0,'treatment_mean':mean,'treatment_variance':c*c*variance,
  'original_linear_R2_k1':1/(8*math.pi*variance),'bounded_linear_R2_k1':1/(8*math.pi*variance),
  'bounded_linear_R2_k01':.01/(8*math.pi*variance),
  'covariance_D_Q_k1':c/(2*math.sqrt(2*math.pi)),
  'scope':'Quadrature verifies identities; analytic proofs are in BOUNDED_DGP_DERIVATION.md; no bounded data or outcome generated',
  'quadrature_tail_note':'standard-normal integration truncated to +/-12; bounded integrands make omitted mass negligible at the reported tolerance; not a mathematical interval certificate'})
if __name__=='__main__':main()
