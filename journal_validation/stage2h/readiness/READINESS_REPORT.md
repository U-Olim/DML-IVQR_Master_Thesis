# Stage 2H-0 — Numerical and computational readiness

2 November 2026, Asia/Tashkent. Branch `journal-validation`; HEAD `dd40beeecede0abdda69bfba56b47789efa42811`.

## Decision

**READY for the prespecified limited paired diagnostic pilot.** The numerical
implementation passed all 12 requested settings, repeated execution and
two-worker execution. The bounded-DGP structural quantile/rank model is
coherent, with proved mixed residual-density bounds, moments, instrument
relevance and local ideal-profile identification. The pilot budget is modest
under the measured two-worker configuration and an explicit twofold allowance.

This readiness decision is for a diagnostic experiment, not a theorem of
95% coverage or an authorization to launch a production simulation. Important
high-dimensional assumptions remain open, and a full-conditioning uniform
density lower bound is actually false. These limitations are explicit below
and in `BOUNDED_DGP_DERIVATION.md`. They are not concealed as established
assumptions. No bounded-DGP implementation or Stage 2H Monte Carlo is run here.

## 1. Fixed numerical generalization test

The design was locked before fitting in `DESIGN.csv` / `DESIGN_LOCK.json`:
n={500,1000}, tau={.10,.50,.90}, kappa={1,.10}, 100 controls, seven
nonzero outcome slopes, one truth candidate per cell. Two fixed original-DGP
primitive samples (one per n) are shared across tau/kappa. Thus this is **12
diagnostic settings, not 12 independent statistical replications**. No failed
setting was replaced. Seed, stream/substream allocation, complete inputs and
original penalty RNG states are retained.

All three cohorts use exactly those inputs: sequential, separate sequential
repeat, and two simultaneous one-thread candidate workers. There are
**36/36 successful measured executions**; an initial same-input smoke check
also passed and is excluded from cohort timings. All 12 rows remain present.
The unchanged original DGP and pivotal penalty rule were independently
replayed from their recorded states, matching every stored numerical input.
The bounded DGP was not used in these tests.

The existing version 2G-D.1 numerical routines are imported read-only. The
readiness adapter supplies actual n and literal tau; it changes neither
statistical objectives nor solver tolerances. The original adaptive
calibration remains intact; only the version-1 final fixed-penalty refinement
is used. Refined coefficients never feed back into recalibration. Every last
penalty vector is hashed immediately after native calibration and checked
again after optimization/audit. The original cutoff bytes remain unchanged:
**5.99146454710798**. W is rounded for display; displayed interval endpoints
are rounded outward from exact rational bounds.

| n | tau | kappa | W at truth | Decision | Certified W lower | Certified W upper | Three-cohort status |
|---:|---:|---:|---:|---|---:|---:|---|
| 500 | 0.10 | 1.00 | 0.596019075435 | accept | 0.59601907543 | 0.59601907544 | PASS / identical |
| 500 | 0.10 | 0.10 | 0.093744345640 | accept | 0.09374434563 | 0.09374434565 | PASS / identical |
| 500 | 0.50 | 1.00 | 0.982300245264 | accept | 0.98230024525 | 0.98230024527 | PASS / identical |
| 500 | 0.50 | 0.10 | 0.032479107668 | accept | 0.03247910766 | 0.03247910767 | PASS / identical |
| 500 | 0.90 | 1.00 | 0.321465565207 | accept | 0.32146556520 | 0.32146556521 | PASS / identical |
| 500 | 0.90 | 0.10 | 2.317468147769 | accept | 2.31746814776 | 2.31746814778 | PASS / identical |
| 1000 | 0.10 | 1.00 | 2.504316343170 | accept | 2.50431634316 | 2.50431634318 | PASS / identical |
| 1000 | 0.10 | 0.10 | 7.162196887141 | reject | 7.16219688712 | 7.16219688716 | PASS / identical |
| 1000 | 0.50 | 1.00 | 8.039677449409 | reject | 8.03967744937 | 8.03967744944 | PASS / identical |
| 1000 | 0.50 | 0.10 | 1.363356732480 | accept | 1.36335673246 | 1.36335673250 | PASS / identical |
| 1000 | 0.90 | 1.00 | 7.819745573470 | reject | 7.81974557345 | 7.81974557349 | PASS / identical |
| 1000 | 0.90 | 0.10 | 4.149427328812 | accept | 4.14942732880 | 4.14942732883 | PASS / identical |

All **9,000 residual signs per cohort** are certified from exact rational
outcome optima. Raw floating LP residuals disagree with those signs in
**132** observations, reinforcing
the need for exact ranks rather than arbitrary residual tolerances. All
outcome primal/dual/KKT, zero-gap and strict uniqueness certificates pass.
Both final instrument objectives in every run pass exact KKT/primal-dual,
positive Gram, uniqueness and objective-gap checks: **72 verified instrument
objectives** across the measured executions.

W reconstructed independently from exact exported score arithmetic differs
by at most **1.24345e-14**. Every positive-determinant
fixed-objective W interval excludes the cutoff; maximum width is
**5.96874e-11**. All decisions agree with exact reference
inference and with the corresponding native Policy C calibration fit.
No singular S, unresolved sign, candidate failure or ambiguous decision was
observed. This is numerical success on fixed samples, not an estimated
population failure or rejection rate.

Numerical fingerprints match bitwise across all three cohorts for LP
coefficients, outcome certificates/residuals/ranks, density, final instrument
penalties and coefficients, psi, scores, S, W and inference bounds. Performance
counters, PIDs and timings are not required to repeat bitwise. Separate
contract checks verify tau-dependent scores, observation scores, moments,
cutoff bytes and penalty integrity in all 36 runs. The dimension-adapted
independent verifier's exact source and change list are retained; its rational
KKT/uniqueness/Gram/interval calculations are unchanged.

The qualification bounds have the same scope as version B: exact outcome
ranks and final fixed-penalty instrument objective regions with explicit
psi/intercept arithmetic envelopes. This stage does not revive exhaustive
interval propagation through every historical adaptive branch.

## 2. Actual runtime, certification, audit, memory and storage

These measurements come from the **new 12-setting panel**, not extrapolation
from the old 24 cases. Each worker is a separate process; native calibration
is a real frozen-R subprocess. The table includes its startup cost. Core plus
I/O is worker elapsed time less separately measured certification and audit.
Worker totals exclude Python import/launch before main; the cohort wall times
and pilot budget below include that launch overhead.

| n | Core execution + I/O seconds | Certification seconds | Independent audit seconds | Total worker seconds | Output MiB/candidate |
|---:|---:|---:|---:|---:|---:|
| 500 | 2.044 | 1.656 | 3.793 | 7.493 | 2.489 |
| 1000 | 2.468 | 2.964 | 7.890 | 13.322 | 4.919 |

Average certification cost across all cells is
**2.310 s**; independent audit adds
**5.841 s**. Costs are separately recorded
by candidate and mode. The original 1,000-draw pivotal penalty calibration is
actually executed and timed during input preparation, with repeated exact
input/RNG replay. Its shared-pair cost and preparation allowance enter the
pilot budget; it is not silently omitted as in saved-penalty-only estimates.

The 12-case sequential cohort took **136.49 s**;
the separate sequential repeat took
**142.04 s**;
two workers took **74.79 s**, an observed
**1.825x speedup**. Allocated candidate-worker
slot time was 136.49 versus
149.59 seconds. This is a wall-time/allocated-slot
comparison, not a claim to have measured CPU cycles or ideal scaling to five
workers. Two-worker efficiency relative to ideal doubling is
91.2%.

Peak aggregate live-process RSS sampled every 50 ms was
**364.0 MiB sequentially** and
**577.9 MiB with two workers**. The complete
per-process OS working-set high-water marks are retained separately. Aggregate
RSS includes the supervisor, workers and R children; shared pages count in
each process. It is an observed sampled maximum, not an exact continuous tree
peak or a rigorous future memory upper bound. This distinction matters when
provisioning headroom. No third-party memory package was installed.

Mean retained output is **3.704 MiB/candidate**,
with original input storage also recorded separately. The pilot estimate
charges duplicated original input payloads conservatively for both arms;
actual deduplication may save space but is not assumed. Shared manifests and
small run-level metadata are additional. Timing, memory and storage are
available in `runtime_storage_memory.csv`, `cohort_benchmarks.csv`,
`sample_size_benchmarks.csv` and `pilot_budget.csv`.

## 3. Bounded-DGP mathematical readiness

The full derivation is `BOUNDED_DGP_DERIVATION.md`. It analyzes the unchanged
primitive law with rho=.3, T variance 3, and proposed
D_delta=.05+.90 Phi(T), retaining Y_delta=1+X'b+D_delta+u D_delta.
The original outcome must be recomputed conceptually with the changed D;
changing D while holding old Y fixed would not be this structural experiment.

**Established analytically:**

- The structural quantile effect remains alpha_tau=1+Phi^(-1)(tau), with
  values approximately -.2815515655, 1 and 2.2815515655. The structural rank
  U=Phi(u) stays uniform conditional on X,Z. Since D_delta>0, the residual
  sign is exactly 1{u<=Phi^(-1)(tau)}; the conditional moment restriction
  is preserved despite endogeneity.
- With Q=Z-h(X), v=3-kappa^2, mu_Q=kappa(Q1+Q2)/2, conditional u|T,Q is
  normal with mean rho(T-mu_Q)/v and variance 1-rho^2/v. Thus the FULLY
  conditioned residual density at zero is phi((q-m)/sigma)/(D_delta sigma).
  It is pointwise positive and uniformly finite above, but its uniform
  lower bound is **zero**, because the conditional mean is unbounded.
- In contrast, the mixed density conditional on X,Z is
  phi(q) E[1/D_delta|u=q,Q]. It obeys
  phi(q)/.95 <= f_{R_tau|X,Z}(0) <= phi(q)/.05. Across tau in [.1,.9],
  common bounds are **[0.184735,
  7.978846]**. The same bounds hold conditional
  on X. Scalar quadrature independently verifies the mixing identity and
  conditional rank restriction at 18 representative (tau,kappa,Q) points.
- For original D=Phi(T), the analogous inverse-treatment expectation
  diverges: T|u=q,Q has variance 1.91 or 2.90, greater than one. Mills' tail
  asymptotics show the original mixed density at zero is infinite. Bounded
  treatment repairs this specific regularity issue; it does not prove every
  inference assumption. The tail proof and scalar truncation checks are saved.
- D_delta has support (.05,.95), mean .5 and variance
  **0.109328**. Its distribution is not uniform; its
  density may diverge at support edges even though treatment is bounded.
  All inverse treatment moments and raw finite-order polynomial moments
  needed for fixed finite population-score coefficients are finite.
- Cov(D_delta,Q_j)=.90*kappa/[2 sqrt(2pi)] is nonzero. The linear first-stage
  R-squared is approximately **0.294790** at kappa=1
  and **0.002948** at kappa=.1, UNCHANGED by the affine
  transformation. Local ideal-population QR-profile identification follows
  from phi(q)*kappa*E[h'(T)|u=q]/E[h(T)|u=q] being finite and nonzero,
  where h=1/D_delta and h'<0. Independent quadrature/Stein calculations agree.
- Centered population control covariance is I/12. For any fixed finite
  population residualization, oracle score covariance is bounded below by
  2*tau*(1-tau) I_2, hence at least .18 I_2 over [.1,.9]. This does not
  establish corresponding generated-score asymptotics automatically.

**Not established / remaining theory assumptions:** global identification
over a large candidate grid; adequate weak-instrument approximation at kappa=.1;
sample sparse/restricted eigenvalues and growing-dimension rates; approximate
sparsity and nuisance-error products for instrument/density estimation;
Neyman orthogonality of the retained variance-as-normal-scale proxy and
ordinary transformed intercept; and empirical-process/cross-fitting conditions
for the implemented estimator. No unimplemented sample split is claimed.
The working density proxy is not silently identified with the true conditional
residual density derived above.

If a desired theorem requires a uniform positive density lower bound given
D,X,Z, **this proposed DGP does not satisfy that assumption**. A theorem using
the bounded mixed density needs an explicit assumption mapping. The pilot
is therefore a DGP/numerical diagnostic, not a proof of asymptotic inference.

Original-DGP sample relevance is retained even where weak: conventional
first-stage F ranges from
0.677 to
1.398 at kappa=.10,
versus 95.830 to
177.574 at kappa=1.
These are one-sample diagnostics, not guarantees of instrument strength.

## 4. Prespecified paired pilot and realistic budget

`STAGE2H_PILOT_PROTOCOL.md` freezes a small proposed experiment:
20 primitive samples per n, all 12 n/tau/kappa cells, original versus bounded
DGP with identical numerical policy, and three candidates alpha_true+{-.5,0,.5}.
That is **1,440 candidate evaluations**, including 480 at truth. Matched
primitive draws and matched original penalty draws within each A/B candidate
pair separate DGP changes from numerical-policy changes. The truth appears
exactly in each three-point profile. This pilot does not estimate full-grid
interval geometry.

Prespecified outputs include truth coverage/inclusion, mean W, truth/off-truth
rejection, numerical failure and unresolved counts, certified decisions,
instrument diagnostics, paired differences and Monte Carlo uncertainty.
Unresolved cases remain in denominator-R bounds; they are never counted as
acceptance. Complete-pair/qualified-only summaries retain their counts and
selection labels. Per-cell exact binomial intervals, paired uncertainty and
mean-W MCSEs are specified. R=20 has ideal .95-coverage MCSE about .0487;
the pilot cannot prove nominal or asymptotic validity.

| Planning allowance | Serial hours | Two-worker hours using measured speedup | Retained GiB | Provisioned working GiB |
|---|---:|---:|---:|---:|
| 1x | 4.60 | 2.52 | 9.34 | 2.0 |
| 2x | 9.20 | 5.04 | 18.69 | 2.0 |

The base estimate uses all new measured sample-size/cell costs, certificates,
independent audits, process launch overhead and original penalty preparation.
Two-worker estimates use observed 1.825x scaling,
not ideal five-worker scaling. The twofold allowance is a planning margin,
not a proved bound: bounded-arm data and off-truth costs have not been
measured because neither was run. The protocol caps the pilot at two workers,
12 elapsed hours, 20 GiB retained output, 2 GiB available working memory
plus normal host needs, and 180 seconds per candidate. Any resource cap
produces retained unresolved/not-executed statuses, not replacement samples
or tolerance changes. Both budget rows fit those planning envelopes.

## 5. Preservation, reproducibility and stopping point

Frozen version-1 numerical source/configuration and original DGP/penalty code
were read-only. Python 3.11.9, NumPy 2.4.4, SciPy
1.17.1, HiGHS 1.12.0, R 3.4.3 and hdm 0.2.0 are recorded with
one-thread numerical settings. `np.longdouble` has
53 significand bits on this Windows build;
no extra precision is assumed. Exact certificates provide the qualification.
R locale and SciPy option-forwarding warnings are retained in logs, with
successful R return codes and numerical checks; no estimator failure occurred.

`INPUT_SHA256_MANIFEST.json` covers original/frozen source inputs and all
new diagnostic inputs. `SHA256_MANIFEST.json` covers readiness code, design,
results, mathematical derivation and protocol, excluding itself. Protected
snapshots cover the repository outside this directory and Git metadata; final
preservation must pass. `README.md` gives complete reproduction commands.

**Final recommendation: READY for this limited, explicitly diagnostic paired
pilot.** Numerical execution beyond the old panel is demonstrated and the
structural bounded-DGP analysis supports an informative controlled experiment.
Statistical validity remains a separate open question. Work stops here:
the bounded DGP has not been implemented, no Stage 2H Monte Carlo has run,
and no historical file, manuscript, commit or push is changed/performed.
