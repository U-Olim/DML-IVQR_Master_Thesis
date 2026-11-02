# Stage 2G-C — End-to-end numerical certification

2 November 2026, Asia/Tashkent. Saved-input validation following Stage 2G-F.

## 1. Executive conclusion

**NOT READY for the requested end-to-end certification gate; Stage 2H may not begin.**

All 72 native paths were independently rerun and reproduced exactly, including
all 24 primary Policy C cases. The 48 primary final instrument objectives
again pass the exact rational audit. No changed native W or decision was
observed. However, **0/24 primary decisions have an end-to-end certificate**:
the new outward bounds have not been propagated jointly through initialization,
all adaptive penalties and all shooting/stopping branches. All 24 remain
explicitly unresolved. The old conditional W intervals are not promoted.

This recommendation applies the requested strict readiness criterion. It is
not evidence of an observed native numerical failure, nor a proof that a
better certification method cannot succeed. Unlike the earlier conditional
recommendation, the attempted simple interval method now has a measured
failure to close branches; a short remaining validation cannot be promised.

## 2. Certified and uncertified components

| Component | Result and scope |
|---|---|
| Input availability / preservation | All 24 primary cases and 48 secondary paths available; full Stage 2G-F manifest verified; category-indexed input hashes saved |
| Native reconstruction | 72/72 exact repeats of density, coefficients, psi, S and W; RNG unchanged; R exit status 0 |
| Exact outcome residuals and ranks | Rechecked by the rational primary verifier against original X, response, penalties and exact optimum |
| Real residual mean / sample variance | Exact rational evaluation of the once-rounded residual inputs |
| Historical real density / sqrt | 24,000 outward 90-digit intervals; Machin identity with rational alternating-series remainder bounds |
| Independent density check | All 24,000 density and sqrt pairs contain separate 130-digit evaluations |
| Saved density arithmetic error | Rigorous a posteriori hulls enclose the real formula and saved binary64 density at these fixed residual inputs |
| Weighted / centered arrays | Outward bounds for the real formula and for saved-density/real-density hulls; all saved primary centered X/y entries contained |
| Fixed exported shooting calls | 11/138 complete Category A interval checks; 127/138 unresolved under natural interval propagation |
| Signed-correlation selection / QR initialization | Actual selection and independent OLS reconstructed; no propagated QR/selection certificate |
| Adaptive recalibration / stopping | All 138 primary outer updates reconstructed; margins are diagnostics, not certified joint adaptive bounds |
| Final fixed-penalty objectives | 48/48 exact KKT, primal-dual equality, strict-convexity / uniqueness and objective-sublevel checks pass again |
| Scores / S / W at exported psi | Exact rational reconstruction passes; fixed-input W intervals remain conclusive for 24/24 primary paths |
| S nonsingularity over full adaptive uncertainty | Unresolved; established only for the old fixed-input coefficient regions |
| Full adaptive W / decision regions | Unavailable for all 24 primary cases |

The density convention is unchanged: `dnorm(e, mean(e), var(e))`, using
sample variance as the normal scale. The transformed ordinary intercept,
unweighted psi reconstruction, penalties, stopping rules and cutoff are
unchanged. No alternative solver replaces the historical algorithm.

The saved-density/real-density hull is a candidate-specific a posteriori
enclosure. It does not bound arbitrary libm implementations or hypothetical
reevaluations at different residuals. Exact outcome residuals are rounded once,
as before. Binary64 basic-operation / reduction bounds assume finite normal
arithmetic, no flush-to-zero, and the frozen evaluation environment. The
sqrt/weighting/centering enclosures include basic-operation rounding; they
have not been threaded through the complete adaptive estimator.

Maximum saved native versus real-density relative deviation on primary cases:
**5.46712e-15**.
Maximum saved mean absolute error: **5.33489e-17**;
variance absolute error: **5.29623e-17**.
Maximum density hull width: **6.66134e-16**;
centered-X hull width: **1.71974e-13**.
Containment misses for saved centered arrays: **0**.

## 3. Candidate-level decision-certification results

Cutoff for every row: **5.99146454710798**, with original binary64 bytes used
in calculations. “Accept” means failure to reject at that cutoff. Unavailable
full bounds are not zero-width intervals, unbounded certificates or acceptance.
The last column is the older Category A fixed-density/final-penalty bound,
independently reverified here; it is included only for comparison.

| Candidate | Native W | Native decision | Full lower | Full upper | Full status | Conditional fixed-input W interval |
|---|---:|---|---|---|---|---|
| pilot_002_minus | 5.174445 | ACCEPT | unavailable | unavailable | unresolved | [5.170592, 5.178302] |
| pilot_006_truth | 2.806474 | ACCEPT | unavailable | unavailable | unresolved | [2.804178, 2.808773] |
| pilot_001_minus | 19.636635 | REJECT | unavailable | unavailable | unresolved | [19.626638, 19.646632] |
| pilot_001_plus | 25.460307 | REJECT | unavailable | unavailable | unresolved | [25.453789, 25.466818] |
| pilot_001_truth | 1.090510 | ACCEPT | unavailable | unavailable | unresolved | [1.088602, 1.092416] |
| pilot_002_plus | 37.997096 | REJECT | unavailable | unavailable | unresolved | [37.984020, 38.010178] |
| pilot_002_truth | 3.956812 | ACCEPT | unavailable | unavailable | unresolved | [3.953031, 3.960594] |
| pilot_003_minus | 6.748437 | REJECT | unavailable | unavailable | unresolved | [6.742616, 6.754259] |
| pilot_003_plus | 50.840703 | REJECT | unavailable | unavailable | unresolved | [50.827178, 50.854231] |
| pilot_003_truth | 4.958924 | ACCEPT | unavailable | unavailable | unresolved | [4.954423, 4.963434] |
| pilot_004_minus | 8.970357 | REJECT | unavailable | unavailable | unresolved | [8.963737, 8.976977] |
| pilot_004_plus | 39.305314 | REJECT | unavailable | unavailable | unresolved | [39.290778, 39.319842] |
| pilot_004_truth | 8.083667 | REJECT | unavailable | unavailable | unresolved | [8.077929, 8.089411] |
| pilot_005_minus | 1.337125 | ACCEPT | unavailable | unavailable | unresolved | [1.334473, 1.339781] |
| pilot_005_plus | 66.771221 | REJECT | unavailable | unavailable | unresolved | [66.759207, 66.783235] |
| pilot_005_truth | 20.312172 | REJECT | unavailable | unavailable | unresolved | [20.300891, 20.323462] |
| pilot_006_minus | 2.822513 | ACCEPT | unavailable | unavailable | unresolved | [2.817966, 2.827060] |
| pilot_006_plus | 41.899745 | REJECT | unavailable | unavailable | unresolved | [41.881933, 41.917565] |
| pilot_007_minus | 9.813158 | REJECT | unavailable | unavailable | unresolved | [9.803611, 9.822707] |
| pilot_007_plus | 39.772902 | REJECT | unavailable | unavailable | unresolved | [39.765051, 39.780751] |
| pilot_007_truth | 3.393074 | ACCEPT | unavailable | unavailable | unresolved | [3.390857, 3.395293] |
| pilot_014_minus | 4.322082 | ACCEPT | unavailable | unavailable | unresolved | [4.317644, 4.326525] |
| pilot_014_plus | 35.878769 | REJECT | unavailable | unavailable | unresolved | [35.872239, 35.885297] |
| pilot_014_truth | 4.501609 | ACCEPT | unavailable | unavailable | unresolved | [4.496676, 4.506546] |

Machine-readable authoritative table: `results/candidate_bounds.csv`, with
cutoff, explicit scopes and unresolved sources for each case.

## 4. Adaptive-branch analysis and remaining risks

Category A: fixed exported Gram, response crossproduct, penalty and starting
coefficient vector for each call. The outward interval implementation checks
every coordinate threshold, L1 convergence test and final zero threshold until
the first ambiguous comparison. It retains every failure and confirms saved
iterates lie inside the computed bounds through each completed certified sweep.
It does not jump across an uncertain branch or continue using a preferred one.

Category B: fully adaptive propagated certificates. **None obtained.** The
11 successful Category A calls cannot be chained together: each starts from
its own fixed native initializer and penalties, rather than uncertainty
propagated from previous operations.

Category C: unresolved branch uncertainty. Of 138 primary shooting calls,
the unresolved first-comparison types are **{'SOFT_THRESHOLD_BRANCH': 46, 'INNER_STOPPING_BRANCH': 81}**. Natural interval
dependency/wrapping enlarges the bounds over successive sweeps. This is a
limitation of the enclosure, not a demonstrated branch flip or W reversal.

For example, `pilot_002_minus`, instrument 1, call 1, reaches an ambiguous
soft-threshold comparison at sweep 8, coordinate 100. Its S0 interval is
[-36.322983735577345, -35.36251767849088], while lambda is
36.268271181488004. Even this fixed-input bound cannot select the branch.
No descendant adaptive path or decision is certified from that point.

Outer traces provide useful scales: minimum stopping-threshold margin
**2.11435e-06**, minimum fifth/sixth signed-correlation
gap **3.37128e-05**, maximum initialization OLS
condition diagnostic **6.45597**, and maximum
independent penalty-reconstruction difference **1.42109e-14**.
Those margins cannot substitute for error propagation through QR, correlated
coefficient errors, penalty recalibration and all possible stopping branches.

All **224,100** native coordinate updates
were reconstructed from the exported within-sweep coefficient histories,
with **2,241** inner L1 stopping checks recorded.
Maximum long-double versus native coordinate-update discrepancy was
**6.66134e-16**; minimum observed
native soft-threshold distance was
**0.000148793**. These additional
diagnostics do not remove the interval dependency/wrapping problem.

The full uncertainty set for psi, scores and S has not been constructed.
Consequently no full-path nonsingularity theorem, W interval or inferential
decision certificate follows. Exact fixed-final-penalty certificates do not
bound all intermediate approximate-solver trajectories. Near-optimal outcome
instability demonstrated in Stage 2G-F is also unchanged.

The additional 48 near-optimal paths were reproduced exactly, separately from
the primary analysis. Their existing 24/24 opposite-decision pairs remain
saved full-path counterexamples. No new adaptive interval certification of
these secondary paths was attempted, to prioritize the 24 primary cases.

## 5. Independent verification and feasibility

The separate verification program passes **10,000 exact-rational arithmetic
tests**, independent 130-digit density/sqrt containment checks for all 24,000
observations, saved-density and centered-array containment, and exact score/W
reconstruction for all primary cases. Manufactured arithmetic operands are
implementation tests, not generated statistical datasets or Monte Carlo.

The original independent rational verifier was then re-executed on all 24
primary paths (48 instrument objectives), with output redirected here. It
checks residual signs, original objectives, KKT feasibility, primal=dual,
Gram inverse witnesses, objective radii, every fixed-input decision interval,
and positive score determinants over those fixed-input regions. All pass.
Elapsed time for that audit: **149.00 seconds**. The executed
source and its SHA-256 are retained. This is automated independent arithmetic
verification, not an external human review or a formal verification of the
entire adaptive implementation. No claim of a full independent end-to-end
audit is made while the adaptive certificate itself is missing.

Native replay took about 22.6 seconds on this saved panel. The initial
density/branch/independent diagnostic passes took about 6.6/6.9/5.6 seconds;
density and independent containment checks were repeated after adding the
a posteriori centered hulls. Current local artifacts occupy approximately
101.4 MiB before final manifests. These are saved-panel measurements,
not Monte Carlo-scale benchmarks. Exact fixed-input auditing dominates time.

**Complete formal certification was not computationally achieved by this
implementation. Computational infeasibility in principle has not been proved.**
Naive natural-interval shooting is not presently a practical full-path
certificate, even before scaling: its enclosures fail on most fixed-input
calls. Affine/correlated error bounds, verified QR and branch-enclosing
methods could improve this, but their cost and success have not been measured.
There is no basis for an indefinite sequence of promised “small final checks”.

## 6. One recommended implementation policy

Keep the frozen historical Policy C path as the reproducible audit comparator,
retain unresolved candidate statuses, and **stop the present certification
attempt at this report**. Do not silently increase shooting accuracy or
replace an adaptive fit with its exact final-penalty reference.

For subsequent development, a **separately versioned, high-accuracy deterministic
numerical implementation with an explicit arithmetic/stopping contract** is
the more practical direction to assess than exhaustive certification of all
historical approximate-solver branches. Preserve exact outcome ranks and the
same statistical objective/density/instrument conventions, predeclare error
budgets independently of decisions, and validate candidate-level W error before
using it. This is a recommendation only: no new implementation, statistical
procedure, solver change, dataset or DGP is introduced here. Such a version
would not retroactively certify the historical finite adaptive algorithm and
must not inherit a READY label without its own validation.

## 7. Stage 2H decision and preservation

**NOT READY. Stage 2H may not begin under the requested gate.** All 24 primary
native decisions reproduce and their fixed-input certificates pass, but all
24 end-to-end statuses remain unresolved. Numerical reproducibility and
fixed-penalty uniqueness do not establish complete adaptive-path certification
or statistical/asymptotic validity.

All new files reside in `journal_validation/stage2g/end_to_end_certification/`.
`INPUT_SHA256_MANIFEST.json` indexes original observations/tasks, exact outcome
solutions/signs, penalties, all density/regression/adaptive/inference artifacts
for all 72 paths, and the unchanged cutoff. `results/preservation.json` records
the final protected-file comparison. `SHA256_MANIFEST.json` excludes itself.
No historical file, manuscript or saved result was changed. No simulation,
Stage 2C continuation, Stage 2H work, commit or push was performed.
