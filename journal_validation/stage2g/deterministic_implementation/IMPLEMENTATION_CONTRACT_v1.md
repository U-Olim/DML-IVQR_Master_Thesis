# Implementation contract 2G-D.1

The statistical objectives, literal binary64 penalty inputs, GMM moments,
historical density proxy, transformed ordinary intercept, unweighted
residualization and chi-square cutoff are preserved. This is numerical policy
**B**, not a new calibration policy C and not bitwise identity to historical A.

For fixed numerical inputs, the outcome problem is

`min_beta sum rho_tau(y*-X beta) + sum lambda_j |beta_j| / 2`,

including the original positive intercept penalty. The independently assembled
LP uses nonnegative blocks `(beta+, beta-, e+, e-)`, equality
`X beta+ - X beta- + e+ - e- = y*`, and costs
`(lambda/2, lambda/2, tau, 1-tau)`. SciPy HiGHS IPM is used with serial settings
and the tolerances in CONFIG_v1.json. This differs from the historical R
solver and the earlier free-beta/epigraph HiGHS dual-simplex formulation.

The LP proposes a support and tied rows. The 1e-7 threshold selects a proposed
basis only. Exact rational primal feasibility, dual box/penalty feasibility,
zero objective gap, KKT conditions and a uniqueness proof authorize its use.
All residuals and their <=0 ranks are then evaluated rationally. Exact zeros
are rank one. Each exact residual is rounded once to binary64 for density.
Rounded coefficients are diagnostic and never determine the authoritative
ranks. A failed/degenerate/unproved basis returns OUTCOME_UNRESOLVED. No
relaxed rank tolerance or alternative optimal-face tie selection is allowed.

On those residuals, frozen R 3.4.3 / hdm 0.2.0 computes
`f=dnorm(e, mean(e), var(e))`, using sample variance as the normal SCALE.
The transformed regressions retain their ordinary unpenalized intercept.
Original saved post-outcome-penalty RNG states are restored. The present
heteroscedastic X-independent adaptive calibration consumes no new random
numbers, and the before/after states must match. Its initializer, penalties,
finite shooting fits and stopping rules are preserved. It is re-executed
online here, not replaced with stored final penalties. All records are saved.

For each instrument, export its centered binary64 `(Xc,yc)`, centering means
and **last-used** lambda. Reported next lambda is retained separately. Then
solve the SAME fixed objective

`F(b)=||yc-Xc b||^2 + sum lambda_used,j |b_j|`

with zero initialization, ascending-coordinate descent, serial `np.longdouble`
Gram/crossproduct accumulation, and deterministic direct active-set polish.
On this Windows build `longdouble` has 53 significand bits (8 bytes), so it
provides no precision beyond binary64. Accuracy comes from the converged
solution, direct polish and exact checks; extra accumulator precision is not
assumed or claimed.
KKT target is 1e-10 absolute; maximum 10,000 sweeps. A proposed final active set
is independently reconstructed rationally and checked for exact KKT and
primal=dual. A freshly computed approximate inverse Gram witness is verified
with exact integer arithmetic, proving strict convexity/uniqueness and an
objective-gap-to-coefficient error bound. No ridge or changed penalty is used.

Crucially, refined coefficients are NOT fed into adaptive calibration. Doing
that can alter subsequent penalty vectors and would be policy C (a modified
calibration pathway). Mathematical equivalence is established for B's final
fixed objectives and their original penalty bytes; equivalence to a
high-accuracy recalibrated trajectory is not claimed. Finite coefficients
and W need not be bitwise equal to historical A or native Policy C.

Recover `gamma0=mean_y-mean_X'b`, then
`psi=Z-[1,X]gamma`, without a weighted-intercept substitution. Compute
`s=tau-r`, `z_i=psi_i*s_i`, `g=sum(z_i)`, `S=sum(z_i z_i')`, and
`W=g' solve(S,g)`. Preserve the archived cutoff bytes, displayed as
5.99146454710798. S is the unnormalized second-moment sum.

Exact rational W reconstruction checks exported coefficients/scores. Rational
interval bounds enclose both final fixed-objective sublevels and the verified
intercept/psi arithmetic envelope; positive determinant and a cutoff-separated
W interval authorize ACCEPT_CERTIFIED / REJECT_CERTIFIED for this version's
fixed objective contract. These are not exhaustive error-propagation
certificates of every historical adaptive branch, which are not a prerequisite
for this stage. Native density/calibration are reproducible finite operations.

INSTRUMENT_UNRESOLVED / INFERENCE_UNRESOLVED is returned on failed
optimization, certificate, nonsingularity or decision qualification. Unresolved
cases stay in reporting denominators; no failed inverse means acceptance.
This validation adapter deliberately uses only the saved 24 n=1000 cases.
The LP, exact outcome and coordinate solvers are dimension-generic; no claim
of an empirically validated n=500 adapter or new-sample degeneracy rate follows.

This computational contract does not establish identification, regularity,
asymptotic inference, coverage or validity of any future DGP modification.
