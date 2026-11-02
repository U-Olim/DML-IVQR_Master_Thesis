# Bounded-treatment DGP: analytical readiness, no implementation

All statements here concern the mathematical population DGP. No transformed
treatment sample or bounded-DGP outcome is generated in this task. The source
is the unchanged `thesis_extension/src/dgp_kappa.R`. Numerical quadrature in
`verify_derivation.py` checks scalar identities and bounds, not new datasets.

## 1. Primitive model and proposed transformation

Let (u,epsilon) be standard jointly normal with correlation rho=0.3, independent
of independent standard normals z1,z2,v1,v2,w and the independent controls
X_j=Phi(x_j), x_j standard normal. Thus controls are independent Uniform(0,1).
Put

T = kappa(z1+z2) + sqrt(2(1-kappa^2)) w + epsilon,

Z1=z1+v1+X2+X3+X4,
Z2=z2+v2+X7+X8+X9+X10.

Write Q_j=Z_j-h_j(X)=z_j+v_j. Then Q~N(0,2 I_2), Var(T)=3,
Cov(T,Q_j)=kappa, Cov(u,T)=rho and u is independent of (X,Q), hence of (X,Z).
The proposed structural treatment is

g_delta(T)=D_delta=delta+c Phi(T), delta=0.05, c=1-2delta=0.90.

Its support is (0.05,0.95); endpoints are bounds/limits, not atoms in the
population. Retain the structural equation

Y_delta=1 + X'b + D_delta + u D_delta,
b=(5,...,5,0,...,0), seven nonzero entries.

This changes both treatment and outcome. Replacing D in the regressor while
leaving the old Y fixed would be a different, misspecified experiment.

## 2. Structural quantile effect and structural rank

Define U=Phi(u). U is Uniform(0,1), independent of (X,Z). For any fixed d>0,

Y_delta(d)=1+X'b+d[1+Phi^{-1}(U)]

is strictly increasing in U. Its structural quantile function is

q_tau(d,X)=1+X'b+d[1+q_tau], q_tau=Phi^{-1}(tau).

The structural quantile treatment effect is alpha_tau=1+Phi^{-1}(tau),
unchanged by delta or kappa. For tau=.10,.50,.90 it is approximately
-0.2815515655, 1, 2.2815515655.

At the structural truth, R_tau=Y_delta-alpha_tau D_delta-(1+X'b)
=D_delta(u-q_tau). Because D_delta>0,

1{R_tau<=0}=1{u<=q_tau},
P(R_tau<=0 | X,Z)=tau.

This proves the structural rank/exclusion restriction and conditional moment
restriction. It does NOT assert U is uniform conditional on D_delta. Treatment
is endogenous through epsilon. In particular the observed conditional
quantile Y|D_delta,X,Z is generally not the structural quantile function.

## 3. Conditional density: specify the conditioning set

Let v_kappa=3-kappa^2 and mu_Q=(kappa/2)(Q1+Q2). Gaussian conditioning gives

T|Q ~ N(mu_Q,v_kappa),
u|T,Q ~ N(m,sigma^2),
m=rho(T-mu_Q)/v_kappa,
sigma^2=1-rho^2/v_kappa.

For the requested kappas, sigma^2>=0.955. At observed d=g_delta(T),

f_{R_tau|D_delta,X,Z}(0)
= phi((q_tau-m)/sigma)/(d sigma).

It is strictly positive and finite at every finite T,Q. Uniformly it is at
most 1/[delta sqrt(0.955) sqrt(2pi)]. However **there is no uniform positive
lower bound** over D_delta,X,Z: m can be arbitrarily large while d remains
bounded; the normal density tends to zero. The same issue exists conditional
on D_delta,X alone (u|T has mean rho T/3 and variance 1-rho^2/3).
Bounded treatment does not remove this conditional Gaussian tail feature.

For the conditional residual density actually mixing over treatment, Bayes'
formula instead yields

f_{R_tau|X,Z}(0)
=phi(q_tau) E[1/g_delta(T) | u=q_tau,Q],

where T|u=q_tau,Q ~ N(mu_Q+rho q_tau, v_kappa-rho^2).
Consequently, uniformly in X,Z,

phi(q_tau)/(1-delta) <= f_{R_tau|X,Z}(0) <= phi(q_tau)/delta.

Both constants are positive and finite at each prespecified interior tau.
The same bounds hold for f_{R_tau|X}(0); X is independent of (T,u), and
T|u=q_tau ~ N(rho q_tau,3-rho^2). Over tau in [.1,.9], common constants are
phi(Phi^{-1}(.1))/.95 and phi(0)/.05. Uniform upper bounds on finitely many
residual-density derivatives also follow from d>=delta and sigma bounded
away from zero, since normal-density derivatives are bounded; this does not
give a full-conditioning density lower bound.

These bounds concern the TRUE structural residual density, not the historical
working proxy `dnorm(e,mean(e),var(e))`. That proxy passes sample variance as
the normal scale. The readiness experiment does not replace it with this
analytical density or claim it is a consistent estimate of it.

### What the transformation repairs in the original DGP

For original D=Phi(T), the analogous expression contains E[1/Phi(T)|u=q,Q].
Its conditional Gaussian variance is v_kappa-rho^2: 1.91 at kappa=1 and 2.90
at kappa=.1, both greater than one. As t tends to -infinity,
1/Phi(t) is asymptotic to |t|/phi(t). Integrating against a normal with
variance s^2>1 gives an integrand proportional to
|t| exp((1-1/s^2)t^2/2 + O(t)), whose negative tail diverges.
Thus the ORIGINAL f_{R_tau|X,Z}(0) is infinite at the truth for these kappas;
also f_{R_tau|X}(0) is infinite because 3-rho^2=2.91>1.

The bounded transformation makes these mixed residual densities finite.
This is an analytical improvement and a reason for a paired diagnostic pilot;
it is not proof that every other assumption of a DML-IVQR theorem holds.

## 4. Treatment distribution and moments

D_delta is an affine transform of Phi(T), T~N(0,3). It is NOT uniform.
For d in (delta,1-delta), set t=Phi^{-1}((d-delta)/c). Then

F_{D_delta}(d)=Phi(t/sqrt(3)),
f_{D_delta}(d)=phi(t/sqrt(3))/(c sqrt(3) phi(t)).

The density can diverge near support endpoints despite bounded support;
do not infer a bounded treatment density from bounded treatment values.
There are no endpoint atoms in exact arithmetic. Symmetry gives E D_delta=.5
and

Var(D_delta)=c^2 arcsin(3/4)/(2pi).

All positive and negative treatment moments are finite, with
E[D_delta^{-r}]<=delta^{-r} for r>0. Controls are bounded, primitive
instruments are Gaussian plus bounded controls, u is Gaussian, and
|Y_delta|<=1+35+.95(1+|u|). Hence all finite-order polynomial moments of
Y_delta, instruments, treatment and structural residuals exist, including
cross moments needed for ordinary score second moments when the population
instrument coefficients are finite constants. These are moment
existence statements, not sparse-design or estimator-rate results. The
original Y also has finite positive moments; its failure above concerns
inverse treatment moments and mixed density at zero.

Cov(u,D_delta)=c rho/[2 sqrt(2pi)] is nonzero. Endogeneity is retained, not
eliminated. Treatment rank ordering in T is preserved; treatment variance is
multiplied by c^2, and instrument covariances by c relative to original D.

## 5. Instrument relevance and local population identification

E[D_delta|Q]=delta+c Phi(mu_Q/sqrt(1+v_kappa)). Its derivative in each Q_j is
strictly positive for kappa>0. Gaussian integration by parts gives

Cov(D_delta,Q_j)=c kappa E[phi(T)]
=c kappa/[2 sqrt(2pi)] > 0.

The population linear first-stage R^2 using the two Q instruments is

R^2 = kappa^2/[8pi Var(Phi(T))].

It is unchanged by the affine treatment transformation; kappa=.1 has one
hundredth of the kappa=1 R^2. Bounded treatment does not strengthen weak
instruments in this linear-R^2 sense. Sample relevance must still be reported.

One can also prove **local**, ideal-population QR-profile identification.
At a candidate a, because X is independent of (D_delta,u), its population
nuisance quantile is 1+X'b+c_tau(a), the tau-quantile of D_delta(1+u-a).
At a=alpha_tau, c_tau=0. Write h(t)=1/g_delta(t),
H=E[h(T)|u=q_tau]. Differentiating the profiled quantile equation is justified
by the bounded positive mixed density and gives c_tau'(alpha_tau)=-1/H.
For m_j(a)=E[Q_j(tau-1{Y_delta-aD_delta<=1+X'b+c_tau(a)})],

m_j'(alpha_tau)
=phi(q_tau) kappa E[h'(T)|u=q_tau]/H,
h'(t)=-c phi(t)/g_delta(t)^2 < 0.

This is finite and strictly nonzero for kappa>0, establishing rank one of
the two-by-one profiled Jacobian locally. Its magnitude scales by kappa;
kappa=.1 has one tenth of the kappa=1 derivative at a fixed tau/delta.
It does not prove global uniqueness of all profiled moment roots, uniform
identification as kappa tends to zero, or finite-sample strong identification.

For ANY population instrument residualization Z-[1,X]gamma, its additional
X-measurable part contributes zero to an EXACT population QR-profile moment,
since that profile has zero conditional score given X. Thus this local
profile argument is not invalidated merely by a different population gamma.
It does not make arbitrary estimated residualization Neyman-orthogonal to
finite-sample nuisance error.

## 6. Population design and oracle score covariance

Independent Uniform(0,1) controls have Cov(X)=I_p/12, proving nonsingularity
of the centered population control design. Weighting by the true residual
density conditional on X gives f_{R_tau|X}(0) I_p/12 at the truth, since
(T,u) is independent of X. Its eigenvalues inherit the mixed-density bounds.
Sample restricted eigenvalues and estimator convergence rates do not follow
from this population statement alone.

For any fixed finite population coefficient matrix gamma, write
psi=Z-[1,X]gamma=Q+a(X). Since Q is independent of X, has zero mean and
covariance 2 I_2, E[psi psi']>=2 I_2. At truth s=tau-1{u<=q_tau} is independent
of (Q,X), has mean zero and variance tau(1-tau). Thus the oracle score
covariance is

Omega=E[s^2 psi psi']=tau(1-tau) E[psi psi']
>=2 tau(1-tau) I_2.

Its eigenvalue lower bound is at least .18 for tau in [.1,.9]. Finiteness
holds for fixed finite gamma by the polynomial moment argument. This proves
oracle population score nonsingularity; it does not prove uniform behavior
of the sample-estimated gamma or a high-dimensional CLT with generated scores.

## 7. Remaining high-dimensional and inference assumptions

Established analytically: structural quantile effect; rank/exclusion;
mixed residual-density bounds; polynomial/inverse-treatment moments;
population control-design and oracle score-covariance nonsingularity;
nonzero population instrument covariance and local ideal-profile Jacobian;
changed treatment distribution. Quadrature verifies representative scalar
values, derivative signs and distribution/moment identities independently.

Still requiring justification or evidence:

- The precise inference theorem and its conditioning requirements. If it
  requires a uniform lower density bound given D,X,Z, this proposed DGP does
  NOT meet it. A theorem using the bounded mixed density needs its own mapping.
- Neyman orthogonality / nuisance robustness of the retained density proxy
  and transformed ordinary-intercept residualization. The proxy is not proved
  to estimate the conditional density needed by a particular orthogonal score.
- Restricted/sparse eigenvalues, approximate sparsity of instrument and
  density nuisance regressions, prediction/rate bounds, and the required
  products of nuisance errors for the actual n,p,s sequences. The outcome
  nuisance has exact seven-slope sparsity, but the other nuisance properties
  do not follow automatically. Fixed n=500/1000,p=100 is not an asymptotic
  rate demonstration.
- Transfer of oracle score-covariance bounds to estimated scores, adequate local Jacobian magnitude
  for kappa=.1, global identification over a broad candidate search, and
  validity of any claimed weak-instrument approximation.
- Independence/empirical-process or cross-fitting conditions appropriate to
  this particular estimator. Do not claim an unimplemented sample split.
- Uniform numerical resolution and failure rates on unseen draws. Exact
  certificates qualify numerical problems, not statistical approximations.

These open assumptions prevent a claim of proved asymptotic validity. They
do not prevent a clearly labeled finite, prespecified paired diagnostic pilot
whose purpose is to measure how a DGP change affects the same numerical policy.
