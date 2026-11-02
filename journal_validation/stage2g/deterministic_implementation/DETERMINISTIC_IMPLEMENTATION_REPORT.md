# Stage 2G-D — Deterministic high-accuracy implementation feasibility

2 November 2026, Asia/Tashkent. Version **2G-D.1**. Branch
`journal-validation`, starting HEAD `dd40beeecede0abdda69bfba56b47789efa42811`.

## Executive conclusion

**CONDITIONAL for Stage 2H overall. The numerical core is promising and
practical for a limited n=1000 pilot, but the full planned design is not yet
costed or validated at n=500 / other quantiles.** Stop after this feasibility
report; no Stage 2H or Monte Carlo was started.

All **24/24** fixed-panel candidates pass the new pipeline and the independent
audit, with **0 unresolved cases**. All **24,000 residual ranks agree with
Policy C**, and all **24 rejection decisions agree**. All **48** new final
instrument optima are certified unique for exactly the original final penalty
inputs. Maximum W change from native Policy C is
**4.83139e-06**, with no cutoff crossing. Historical A
differs in **5/24** decisions, retained
explicitly rather than suppressed.

The measured cost is **0.579 s/candidate** for
point computation and **3.449 s/candidate**
when the new certificates and inference qualification are included. A separate
independent audit costs another **7.512 s/candidate**.
Raw prototype artifacts average **6.02 MiB/candidate**. Solver success
alone therefore understates both computational and storage cost substantially.

## 1. Numerical policy selected and pathway changes

Select **B-v1: exact-certified outcome ranks, preserved native adaptive
calibration, and deterministic high-accuracy final fixed-penalty solves**.
The precise contract is `IMPLEMENTATION_CONTRACT_v1.md`; settings are frozen
in `CONFIG_v1.json`, without decision- or coverage-driven tuning.

| Path | Outcome / signs | Instrument calibration and final solve |
|---|---|---|
| A: historical | Archived approximate outcome and historical residual evaluation | Archived historical native adaptive path |
| Policy C reference | Exact certified optimum and <=0 ranks | Original native adaptive path and its finite final fit |
| Proposed B-v1 | Independently assembled HiGHS-IPM LP, new exact basis certificate, exact <=0 ranks | Replay original adaptive path; preserve last-used penalties; replace only final fixed-objective numerical solve |
| Modified calibration C | Not implemented | Would feed refined fits into recalibration, potentially changing penalties; not equivalent to B without new evidence |

The new LP uses split positive/negative coefficients and residuals, rather
than the older free-coefficient/epigraph dual-simplex formulation. It uses
recorded deterministic solver settings, single-thread operation and repeats
each solve. Its proposed support/tied rows undergo exact rational checks.
The saved Stage 2G optimum is consulted only after reconstruction to compare
results, never to supply the basis or rank vector.

Instrument optimization uses zero initialization, ascending-column cyclic
coordinate descent (absolute KKT target 1e-10, at most 10,000 sweeps) and
direct active-set polish. Its proposed active set is then verified rationally.
A fresh inverse-Gram witness is built and checked exactly. The numerical
optimizer is not replaced by the archived exact reference coefficients.

`np.longdouble` has **53 significand bits** and
8 bytes on this Windows build: it gives no extra
precision over binary64. High accuracy here comes from convergence, polish
and exact verification, not an assumed extended-precision accumulator.

## 2. Mathematical equivalence: established scope

The original objective is preserved:
`sum rho_tau(y*-X beta) + sum lambda_j |beta_j|/2`, with the original positive
intercept penalty, saved numerical lambda and literal binary64 tau. Each
accepted outcome certificate proves exact primal feasibility, dual feasibility,
KKT, primal=dual and uniqueness for these input bytes.

The density remains `dnorm(e, mean(e), var(e))`, using sample variance as the
normal scale. Residuals are rounded once from the exact rational optimum;
authoritative ranks are carried separately. The transformed regression retains
an ordinary unpenalized intercept, followed by the original unweighted
`psi=Z-[1,X]gamma`. No weighted-intercept substitution, ridge, corrected
density formula or changed penalty is introduced.

The original R adaptive calibration was rerun online for all 24 cases.
**All density, native calibration-fit and final penalty bytes match Policy C**.
Original post-outcome-penalty RNG states are restored and unchanged. No new
random draws or pivotal-penalty simulation occur. Captured calibration traces,
last-used lambda and subsequently reported next lambda are stored separately.

For each exported centered design and last-used lambda, the new solver targets
the same mathematical problem:
`F(b)=||yc-Xc b||^2 + sum lambda_used,j |b_j|`.
All 48 exact reference optima reconstructed from the new solver agree exactly
with Policy C's fixed-objective reference optima. This establishes mathematical
equivalence of these final objectives and their penalty inputs, while the
returned approximate coefficients improve substantially.

Equivalence is **not** claimed to a recalibrated high-accuracy adaptive
trajectory, an adaptive fixed point, or bitwise historical A output. Refined
fits are never fed back into penalty calibration. Historical A and exact
outcome inference differ because approximate outcome ranks can differ.

The GMM moments are unchanged: `s=tau-r`, `z_i=psi_i*s_i`, `g=sum z_i`,
`S=sum z_i z_i'`, `W=g' solve(S,g)`. S is unnormalized. The unchanged cutoff
bytes display as **5.99146454710798**. Numerical equivalence and reproducibility
do not establish identification, regularity, asymptotic validity or coverage.

## 3. Outcome optimization, accuracy and ambiguity

| Check | Fixed-panel result |
|---|---:|
| Independent LP solves / repeated solutions | 24 pass; all repeats bitwise identical |
| Exact primal / dual / KKT / zero-gap optimum certificates | 24 pass |
| Exact uniqueness proofs | 24 pass |
| Exact ties | 751 |
| Certified rank disagreements with Policy C | 0 / 24,000 |
| Raw floating LP rank disagreements | 316 / 24,000 |
| Maximum LP true objective gap above certified optimum | 8.57502e-13 |
| Maximum raw LP fitted-value error | 3.68671e-13 |
| Maximum raw LP coefficient error | 2.31848e-13 |
| Maximum split-LP equality violation | 2.20268e-13 |
| Maximum numerical dual box violation | 0 |
| Maximum numerical dual penalty violation | 1.56675e-12 |
| Maximum split-LP stationarity residual | 1.33937e-12 |
| Maximum split-LP complementarity residual | 0 |

Numerical LP residuals are diagnostics; exact certification supplies the
authoritative feasible zero-gap optimum. High LP accuracy alone does not
resolve rank ambiguity: the 316 raw disagreements
persist even with fitted-value errors below 3.69e-13.
Every authoritative rank is computed from exact residuals, with exact zero
assigned rank one under the unchanged <=0 convention.

The 1e-7 basis proposal threshold does not define a residual tie. A proposed
square basis must pass exact equations, all residual signs, dual box and
penalty feasibility, zero gap and strict-margin uniqueness. If it fails,
return OUTCOME_UNRESOLVED; non-square/degenerate/nonunique/unproved cases are
not resolved by a larger tie tolerance or arbitrary optimal-face selection.
No such failure occurred on this panel. New-sample degeneracy/failure rates
remain unmeasured. Dimension-generic numerical cores support future n=500,
but the saved validation adapter is deliberately restricted to these 24 n=1000
problems.

## 4. Instrument, score and decision validation

| Check | Result |
|---|---:|
| Independent new instrument solves / bitwise repeats | 48 / 48 |
| Exact KKT, primal=dual, positive Gram / uniqueness | 48 / 48 |
| Maximum returned fixed-objective true gap | 2.53223e-27 |
| Native Policy C maximum true gap, same 48 objectives | 2.94445e-10 |
| Maximum returned coefficient discrepancy from exact optimum | 5.27433e-15 |
| Maximum numerical instrument KKT residual | 7.81597e-14 |
| Maximum instrument coefficient change from native C | 1.52363e-06 |
| Maximum residualized-instrument change from C | 2.77352e-06 |
| Maximum observation-score change from C | 1.95762e-06 |
| Scalar rank-score changes from C | 0 |
| Maximum score-matrix condition number | 1.51101 |
| Maximum W versus exact exported-score reconstruction error | 1.56319e-13 |
| Maximum W change from C | 4.83139e-06 |
| Maximum certified fixed-objective W interval width | 1.28118e-10 |
| Cutoff-separated W bounds / positive interval determinants | 24 / 24 |
| Policy C decision disagreements | 0 / 24 |
| Final numerical failures / unresolved cases | 0 / 24 |

For each new final solve, its exact returned objective gap and a certified
Gram eigenvalue lower bound enclose the coefficient error. Rational intervals
map the two objective regions through centering, psi, score sums and every
entry of S. Explicit verified intercept/psi arithmetic envelopes include the
returned floating quantities. The determinant is positive throughout these
fixed-objective regions, and every W interval excludes the cutoff.

These bounds certify B-v1's final fixed-objective qualification. They are not
the historical end-to-end adaptive-branch certificates attempted in Stage
2G-C. Exhaustive propagation through those historical branches is not used
as a gate here. Replay and independent trace evidence support the specified
finite calibration procedure; its mathematical accuracy is not silently
reinterpreted as an exact adaptive fixed point.

The independent verifier calls no optimizer or active-set reconstruction. It
uses direct rational residuals, a separate fraction-elimination determinant,
KKT gradients, primal/dual values, fresh Gram witnesses, exact psi arithmetic,
score moments and a separately assembled interval calculation. All **24**
primary paths and **48** instrument objectives pass; elapsed audit time is
**180.29 seconds**. This is numerical/arithmetic
verification, not a claim of statistical validity or external human review.

## 5. All 24 candidate decisions

“Accept” means failure to reject at the original cutoff. Intervals below are
B-v1 fixed-final-objective bounds with exact outcome ranks and declared psi
arithmetic envelopes. Full machine precision, coefficient/score differences,
raw LP diagnostics, signs and certificates are retained in CSV/JSON/binaries.

| Candidate | Historical A W / decision | Policy C W / decision | Proposed B-v1 W / decision | Proposed conditional W bounds |
|---|---:|---:|---:|---:|
| pilot_002_minus | 6.336102 / reject | 5.174445 / accept | 5.174446 / accept | [5.174445797057, 5.174445797079] |
| pilot_006_truth | 5.490874 / accept | 2.806474 / accept | 2.806475 / accept | [2.806474989162, 2.806474989179] |
| pilot_001_minus | 20.788991 / reject | 19.636635 / reject | 19.636634 / reject | [19.636633564717, 19.636633564777] |
| pilot_001_plus | 30.064169 / reject | 25.460307 / reject | 25.460303 / reject | [25.460303272142, 25.460303272195] |
| pilot_001_truth | 0.488466 / accept | 1.090510 / accept | 1.090508 / accept | [1.090508323772, 1.090508323785] |
| pilot_002_plus | 44.738021 / reject | 37.997096 / reject | 37.997097 / reject | [37.997097131176, 37.997097131243] |
| pilot_002_truth | 6.857863 / reject | 3.956812 / accept | 3.956811 / accept | [3.956811471956, 3.956811471977] |
| pilot_003_minus | 5.179703 / accept | 6.748437 / reject | 6.748436 / reject | [6.748435596244, 6.748435596269] |
| pilot_003_plus | 55.495969 / reject | 50.840703 / reject | 50.840703 / reject | [50.840703200338, 50.840703200466] |
| pilot_003_truth | 14.436100 / reject | 4.958924 / accept | 4.958927 / accept | [4.958926573244, 4.958926573270] |
| pilot_004_minus | 8.057616 / reject | 8.970357 / reject | 8.970355 / reject | [8.970355098528, 8.970355098568] |
| pilot_004_plus | 42.826281 / reject | 39.305314 / reject | 39.305309 / reject | [39.305308708132, 39.305308708219] |
| pilot_004_truth | 13.490802 / reject | 8.083667 / reject | 8.083668 / reject | [8.083667651735, 8.083667651755] |
| pilot_005_minus | 1.120578 / accept | 1.337125 / accept | 1.337126 / accept | [1.337125504664, 1.337125504671] |
| pilot_005_plus | 76.218252 / reject | 66.771221 / reject | 66.771220 / reject | [66.771220269066, 66.771220269160] |
| pilot_005_truth | 26.867613 / reject | 20.312172 / reject | 20.312174 / reject | [20.312173570433, 20.312173570473] |
| pilot_006_minus | 3.613931 / accept | 2.822513 / accept | 2.822511 / accept | [2.822511392185, 2.822511392206] |
| pilot_006_plus | 43.891059 / reject | 41.899745 / reject | 41.899747 / reject | [41.899746994922, 41.899746995010] |
| pilot_007_minus | 11.134964 / reject | 9.813158 / reject | 9.813156 / reject | [9.813156443829, 9.813156443876] |
| pilot_007_plus | 48.339223 / reject | 39.772902 / reject | 39.772901 / reject | [39.772900642940, 39.772900643037] |
| pilot_007_truth | 3.709285 / accept | 3.393074 / accept | 3.393075 / accept | [3.393074622726, 3.393074622744] |
| pilot_014_minus | 5.244829 / accept | 4.322082 / accept | 4.322083 / accept | [4.322083180078, 4.322083180099] |
| pilot_014_plus | 44.067797 / reject | 35.878769 / reject | 35.878768 / reject | [35.878767991188, 35.878767991257] |
| pilot_014_truth | 6.343335 / reject | 4.501609 / accept | 4.501610 / accept | [4.501609876801, 4.501609876822] |

`results/three_path_comparison.csv` retains outcome, density, instrument,
scalar-score and observation-score comparisons against both historical A and
Policy C. No disagreement, numerical failure or unresolved case is excluded
to obtain favorable decisions. The same exact-rank policy is used throughout;
coverage closer to 95% is never a tuning target.

## 6. Benchmarks and Monte Carlo feasibility

All timings are observed on the original saved **n=1000, p=100, tau=.90**
panel: 24 candidates on eight archived datasets, not 24 independent
replications. No new Monte Carlo replications were run. Both LP and new instrument
solves were repeated bitwise. Production-like component sums exclude those
deliberate repeats, trace-capture replay and the separate independent audit.
The qualified proxy includes measured exact outcome / instrument certificates,
W qualification and residual inference/validation overhead; it is not a
timed new-sample Monte Carlo runner.

| Component | Mean seconds per candidate |
|---|---:|
| Point pipeline: LP + native density/calibration + refined instrument solves | 0.579 |
| Qualified pipeline including exact certificates / inference overhead | 3.449 |
| Qualified pipeline panel 95th-percentile runtime | 3.813 |
| Additional independent direct-rational audit | 7.512 |
| Qualified pipeline plus independent audit on every candidate | 10.961 |

The existing `thesis_extension/config/extension_config.R` specifies 500
replications, five tau values, four kappa values, 41 candidate points, sample
sizes 500/1000 and five workers. The following are arithmetic projections for
the **DML candidate component only**, not an approved Stage 2H design or an
observed full simulation. Other estimators and all unmeasured costs are extra.

| Planning scenario | Candidates | Qualified serial hours | Ideal five-worker hours | Serial hours with independent audit on every candidate | Current payload storage GiB |
|---|---:|---:|---:|---:|---:|
| 40 samples, one tau/kappa, 41-candidate DML profiles | 1,640 | 1.57 | 0.31 | 4.99 | 9.6 |
| 500 samples, 5 tau, 4 kappa, 41 candidates; ONE sample size | 410,000 | 392.83 | 78.57 | 1248.39 | 2409.6 |
| Same design across BOTH n=500 and n=1000 | 820,000 | 785.66 | 157.13 | 2496.77 | 4819.2 |

Five-worker projections assume ideal scaling, which was not benchmarked.
The mean panel runtime is not a worst-case bound. Penalty simulation, data
generation, new-DGP effects, other quantiles, all other estimators, scheduler
overhead and new-sample degeneracy are not measured. All original outcome
penalties were saved inputs; their future simulation cost cannot be inferred
from the LP benchmark. Exact-certification feasibility is assessed using
observed certificate costs, not inferred from solver success alone.

**n=1000:** limited-pilot core computation is practical on these saved
problems. Large production is materially more expensive once certificates,
audits and storage are retained; the whole repository design requires an
explicit budget and retention strategy.

**n=500 with 100 controls:** no member of the required 24-problem panel has
n=500. No rows were truncated and no new candidate/dataset was constructed.
There is therefore **no direct n=500 benchmark or validation claim**. The
two-sample-size projection assigns n=500 the measured n=1000 cost solely as
a planning proxy, not a proved upper bound. Smaller n alone does not prove
LP basis or degeneracy behavior. A bounded authorized pilot must measure
these cases and failure rates before a broad n=500 production claim.

The retained prototype averages **6.02 MiB/candidate**; extrapolation
is about 4.71 TiB
for the two-size DML component before shared metadata and backups. This
prototype deliberately duplicates inputs to preserve evidence. A production
store should deduplicate immutable observations and record reproducible
bases/traces/certificates with unresolved statuses preserved. This task does
not change retention policy or discard evidence.

## 7. Remaining issues, numerical decision policy and Stage 2H

No ambiguous residual sign or fixed-panel decision remains in this version.
The remaining feasibility conditions are specific:

1. Validate the dimension-generic numerical cores and R adapter at n=500 and
   the other intended tau settings in a bounded, separately authorized pilot;
   record degeneracy, unresolved cases and actual full pipeline cost.
2. Budget per-candidate exact certificates, independent audit frequency,
   pivotal-penalty generation, parallel scaling and evidence storage. Do not
   use the 0.58-second point solver timing as the certified simulation cost.
3. Keep B-v1's historical calibration / final fixed-objective distinction
   explicit. Feeding refined fits back into calibration requires a new
   version and evidence for changed penalty inputs; it is not this policy.
4. Keep any bounded-treatment DGP and its identification/regularity review
   separate from this numerical feasibility result.

Recommended decision policy: use exact-certified outcome ranks and qualified
B-v1 final fits. Emit OUTCOME_UNRESOLVED, INSTRUMENT_UNRESOLVED or
INFERENCE_UNRESOLVED on failed certificates/decision qualification, retain
all cases in denominators, and never apply an arbitrary residual tie tolerance
or interpret a failure as acceptance. No exhaustive certification of every
historical adaptive branch is required before a bounded pilot.

**Recommendation: CONDITIONAL for Stage 2H overall.** The n=1000 saved-panel
numerical evidence supports a limited pilot of this separately versioned
implementation; it does not establish readiness of the entire two-size,
multi-quantile production design or validate asymptotic inference. The next
step should be the bounded feasibility/assumption review above, not renewed
indefinite interval propagation of the historical algorithm. Stage 2H is not
started by this task.

## Reproducibility, development errors and preservation

Environment: Python 3.11.9, NumPy 2.4.4, SciPy 1.17.1, bundled
HiGHS 1.12.0, frozen R 3.4.3 / hdm 0.2.0, single-thread settings and
recorded original RNG streams. Build details and complete numerical options
are saved. Bitwise reproducibility is demonstrated in this environment;
cross-platform bitwise identity is not asserted.

Two development errors were caught and corrected: an R matrix-versus-vector
attribute comparison and a shadowed dimension in an intermediate row-norm
bound. The independent verifier rejected the latter; all affected instrument
and inference certificates were regenerated and the final full audit passed.
Superseded failure logs/records are retained under explicit development names.
`EXECUTION_NOTES.json` and `results/processes.json` distinguish those attempts
from final statuses. No failed certificate is treated as a successful case.

SciPy's warning that serial/seed options are forwarded to HiGHS verbatim is
recorded per candidate. The R startup locale warning is preserved; direct
successful R return codes and unchanged native result bytes are checked.
These warnings are not suppressed or counted as statistical failures.

All writes are confined to this directory. Input hashes cover original
observations/candidates, penalties and RNG records, reference certificates,
calibration inputs/traces, instrument coefficients, scores and inference
artifacts. The local manifest covers the new versioned code, copied LP inputs,
configurations, results and certificates. Preservation snapshots exclude
only this directory and Git metadata; final comparisons must show no changes
outside scope. No historical estimator, prior validation, manuscript or saved
Monte Carlo output was modified. No new dataset, Monte Carlo, Stage 2H,
commit, push or merge was performed. Work stops after reporting.
