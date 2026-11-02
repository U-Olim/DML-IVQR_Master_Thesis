# Stage 2G-F — complete downstream-path validation

2 November 2026, Asia/Tashkent. Branch `journal-validation`; HEAD `50412fe7b6858b86eebb8874a820bf7651eb83cf`. All new material is under `journal_validation/stage2g/full_path_validation/`.

## Readiness decision

**B — Conditional.** The complete Policy C computational path was implemented and validated on all 24 saved candidates. All 72 newly evaluated paths passed the numerical checks and independent certificate audit. Exact outcome signs, 144 unique fixed-final-penalty instrument optima, and conditional decision bounds are established. The remaining limitation is specific: the certified decision bounds freeze the exported density/centering values and final adaptive penalties; they do not propagate density arithmetic uncertainty through the adaptive penalty trajectory and stopping branches. Therefore this report does not claim an unconditional full-path mathematical certificate or authorize Stage 2H to begin.

The remaining condition is about the scope of proof, not an observed numerical failure. High-precision density and independent penalty-trace checks passed, the paths reproduce bitwise, and no conditional decision bound crosses the cutoff. A versioned finite-precision implementation is concretely specified in [POLICY_C_SPECIFICATION.md](POLICY_C_SPECIFICATION.md). A limited local interval-propagation validation on these same saved inputs is the minimum remaining work for strict complete-path certification.

## What was evaluated

All 24 original Stage 2E problems were retained, prioritizing `pilot_002_minus` and `pilot_006_truth`. Stage 2G outcome optima and signs were checked against their exact rational inputs, and no outcome solver, data generator or pivotal-penalty simulation was rerun. The 12 Stage 2G sensitivity cases each contributed the two already selected minimum/maximum rank patterns at fixed objective budgets 1e-8 and 1e-20: 48 near-optimal paths plus 24 exact-optimum paths.

Every path recomputed the historical candidate-specific density proxy, both adaptive instrument fits, residualized instruments, score vector, g, S, W and cutoff decision. The 48 archived A/B baseline paths were reconstructed from their saved coefficients and verified against their saved residual, density and psi arrays. Instrument fits for all 72 new paths were repeated natively, yielding identical coefficients. All used the corresponding saved post-outcome-penalty RNG state and left it unchanged. No replacement sample, additional favorable case or coverage-based selection was used.

## Exact computational contract

At each certified outcome optimum, rational evaluation gives e_i=y_i*-x_i beta and r_i=1{e_i<=0}. Residuals are rounded once to binary64 for the density calculation, while ranks are carried separately from exact arithmetic. Subtracting predictions from rounded beta would reintroduce the earlier sign problem and is not used. The exact objective is the original sum rho_tau(e_i)+sum lambda_j|beta_j|/2, with the positive intercept penalty and literal binary64 tau preserved.

The density remains `dnorm(e, mean(e), var(e))`: the sample variance is passed as the normal scale. The original ordinary intercept in transformed instrument regression is preserved, followed by the original unweighted reconstruction psi_j=Z_j-[1,X]gamma_j. This is not a replacement with a weighted intercept or corrected density formula. R 3.4.3 and hdm 0.2.0, historical options, ordering and streams are fixed.

For s_i=tau-r_i, z_i=psi_i s_i, g=sum z_i and S=sum z_i z_i', W=g'S^{-1}g. The historical cutoff is 5.99146454710798. S is the unnormalized second-moment sum. Exact W certificates interpret exported binary64 psi and scores as rational inputs. R W and its inversion error are reported separately.

## Complete 24-problem decision comparison

A is the archived historical full path; B is the archived independent-outcome full path; C is the newly recomputed certified-outcome full path. Decimal W values below are rounded for display; certificate comparisons use exact rationals and the unchanged cutoff.

| Candidate | A W / decision | B W / decision | C W / decision | C conditional W bounds |
|---|---:|---:|---:|---:|
| pilot_002_minus | 6.336102 / reject | 3.017456 / accept | 5.174445 / accept | [5.170592, 5.178302] |
| pilot_006_truth | 5.490874 / accept | 6.041387 / reject | 2.806474 / accept | [2.804178, 2.808773] |
| pilot_001_minus | 20.788991 / reject | 18.458926 / reject | 19.636635 / reject | [19.626638, 19.646632] |
| pilot_001_plus | 30.064169 / reject | 30.529468 / reject | 25.460307 / reject | [25.453789, 25.466818] |
| pilot_001_truth | 0.488466 / accept | 0.306202 / accept | 1.090510 / accept | [1.088602, 1.092416] |
| pilot_002_plus | 44.738021 / reject | 45.924754 / reject | 37.997096 / reject | [37.984020, 38.010178] |
| pilot_002_truth | 6.857863 / reject | 6.905276 / reject | 3.956812 / accept | [3.953031, 3.960594] |
| pilot_003_minus | 5.179703 / accept | 5.509242 / accept | 6.748437 / reject | [6.742616, 6.754259] |
| pilot_003_plus | 55.495969 / reject | 59.396705 / reject | 50.840703 / reject | [50.827178, 50.854231] |
| pilot_003_truth | 14.436100 / reject | 9.461010 / reject | 4.958924 / accept | [4.954423, 4.963434] |
| pilot_004_minus | 8.057616 / reject | 7.900804 / reject | 8.970357 / reject | [8.963737, 8.976977] |
| pilot_004_plus | 42.826281 / reject | 39.706640 / reject | 39.305314 / reject | [39.290778, 39.319842] |
| pilot_004_truth | 13.490802 / reject | 15.528197 / reject | 8.083667 / reject | [8.077929, 8.089411] |
| pilot_005_minus | 1.120578 / accept | 1.007009 / accept | 1.337125 / accept | [1.334473, 1.339781] |
| pilot_005_plus | 76.218252 / reject | 72.234786 / reject | 66.771221 / reject | [66.759207, 66.783235] |
| pilot_005_truth | 26.867613 / reject | 30.390196 / reject | 20.312172 / reject | [20.300891, 20.323462] |
| pilot_006_minus | 3.613931 / accept | 3.446248 / accept | 2.822513 / accept | [2.817966, 2.827060] |
| pilot_006_plus | 43.891059 / reject | 45.423010 / reject | 41.899745 / reject | [41.881933, 41.917565] |
| pilot_007_minus | 11.134964 / reject | 9.169114 / reject | 9.813158 / reject | [9.803611, 9.822707] |
| pilot_007_plus | 48.339223 / reject | 49.455222 / reject | 39.772902 / reject | [39.765051, 39.780751] |
| pilot_007_truth | 3.709285 / accept | 3.157995 / accept | 3.393074 / accept | [3.390857, 3.395293] |
| pilot_014_minus | 5.244829 / accept | 2.293761 / accept | 4.322082 / accept | [4.317644, 4.326525] |
| pilot_014_plus | 44.067797 / reject | 35.763925 / reject | 35.878769 / reject | [35.872239, 35.885297] |
| pilot_014_truth | 6.343335 / reject | 9.598156 / reject | 4.501609 / accept | [4.496676, 4.506546] |

A/B differ in 2/24 decisions. C differs from A in 5/24 and from B in 5/24. These are comparisons on a fixed panel, not coverage rates. The machine-readable `complete_24_problem_comparison.csv` contains all three pairwise comparisons of outcome coefficients, residual ranks, density values, residualized instruments, scalar rank scores, observation-score vectors, W and decisions, with explicit certification scopes.

`pilot_002_minus`: A rejects (6.336102), B accepts (3.017456), C accepts (5.174445). `pilot_006_truth`: A accepts (5.490874), B rejects (6.041387), C accepts (2.806474). Thus the exact Policy C path yields a definite acceptance in both priority cases. It agrees with B in the first and A in the second. The archived A/B disagreements remain historical facts; they are not overwritten or reclassified as identical computations.

## Downstream numerical validation

Independent 80-digit Decimal mean/variance/normal-density evaluation differs from the native density by at most 9.31868e-15 relatively. This validates the historical variance-as-scale formula numerically; it is not an outward-rounded interval proof. Transformed designs, response centering and residualized instruments were independently reconstructed. Exact score sums, all entries of S and W were independently recomputed.

The largest native-versus-exact W difference is 8.52651e-14; the largest S condition number is 1.51101; the maximum inverse residual infinity norm is 2.42076e-16. No singular score matrix, nonpositive density, native fitting failure, estimator warning or decision mismatch in exact W reconstruction occurred. The R startup locale warning is recorded separately in execution notes.

All 144 instrument fits passed independent initialization and adaptive loading checks. The initializer uses the five largest SIGNED correlations, then OLS with an intercept; it does not select by absolute correlation. Independent trace penalty values differ by at most 2.13163e-14. The smallest observed outer stopping-threshold margin is 2.11435e-06. These are numerical diagnostics, not interval proofs over perturbed inputs. The last penalty actually used is exported separately from the subsequently reported next penalty; certificates use only the former.

## Instrument objective, uniqueness and certified decision regions

For each exported centered design and last-used penalty, the audited objective is F(b)=||yc-Xc b||^2+sum lambda_j|b_j|. Its dual is maximize yc'v-||v||^2/4 subject to |Xc'v|<=lambda. Rational active-set reconstruction produces b*, residual r*, v=2r*, exact KKT conditions and equal primal/dual values. Native coefficients are retained; these references are diagnostic certificates, not replacements in the adaptive loop.

All 144 fixed-penalty objectives have unique optima. Full rank is shown by a nonzero modular minor and independently by an exact approximate-inverse residual bound. If G=Xc'Xc, R is the saved approximate inverse, eta bounds ||I-RG||_2 with eta<1, and M bounds ||R||_2, then lambda_min(G)>=(1-eta)/M. All eta and M inequalities are verified with integer/rational arithmetic. This certifies strict convexity without trusting a floating rank threshold.

The smallest certified Gram eigenvalue lower bound is 5.20644; the largest centered-design condition diagnostic is 10.4752. There is no evidence here of exact nonuniqueness or severe ill-conditioning of the final centered objectives. The largest native true objective gap is 2.94445e-10 and the largest native coefficient discrepancy from its exact reference is 1.52363e-06. These are finite solver errors, not multiple exact solutions.

For any b satisfying F(b)<=F(native), strong convexity gives ||b-b*||_2<=sqrt((F(native)-F*)/mu), where mu is the certified Gram lower bound. For this panel each unweighted X entry and transformed design mean lies in [0,1], so the historical psi reconstruction has row norm at most sqrt(100)=10. The resulting psi intervals also include the verified native intercept/psi rounding envelope. Rational interval arithmetic then bounds g, S, its determinant and W over both fixed-penalty objective sublevels.

All 72 resulting W intervals lie entirely on the same side of the cutoff as their native full paths. The independent verifier checks every bound, not just its endpoint decisions. These are genuine enclosing bounds over the stated instrument-coefficient regions; they are not minima/maxima from a search. They remain conditional on the exported weights, centering quantities and final penalties. They do not cover all adaptive trajectories induced by density or intermediate-solver perturbations.

Using the exact fixed-penalty reference instrument coefficients diagnostically changes W by at most 5.43023e-06, with 0 decision changes across 72 paths. The original native path is the reported Policy C path. Exact certificates for centered exported arrays are not silently described as exact minimizers of an unrounded transformed/intercept problem.

## Near-optimal full-path instability

For each selected direction, solve the exact tied/active linear system, preserve all non-tied signs, and choose a rational step bounded by both a sign-preserving radius and the check-loss/L1 Lipschitz objective bound. Independent rational evaluation verifies the actual positive objective gap and all 1,000 ranks. The two budgets were fixed at 1e-8 and 1e-20 before examining downstream results. At 1e-20, rounded coefficient vectors may coincide with the rounded optimum; residuals are evaluated from rational vectors before export. These witnesses are not claims that every perturbation is distinguishable as a binary64 coefficient vector.

| Case | Budget 1e-8: low / high full W | Budget 1e-20: low / high full W | Opposite decisions at both budgets |
|---|---:|---:|---|
| pilot_002_minus | 0.953411 / 9.119658 | 0.953411 / 9.119658 | Yes |
| pilot_006_truth | 1.875315 / 15.799875 | 1.875315 / 15.799875 | Yes |
| pilot_002_truth | 2.237966 / 17.111404 | 2.237966 / 17.111404 | Yes |
| pilot_003_minus | 0.588276 / 12.449202 | 0.588276 / 12.449202 | Yes |
| pilot_003_truth | 3.137603 / 22.381152 | 3.137603 / 22.381152 | Yes |
| pilot_004_minus | 3.425757 / 16.401917 | 3.425757 / 16.401917 | Yes |
| pilot_004_truth | 4.138917 / 26.180553 | 4.138917 / 26.180553 | Yes |
| pilot_006_minus | 0.682735 / 7.410671 | 0.682735 / 7.410671 | Yes |
| pilot_007_minus | 5.829432 / 17.690536 | 5.829432 / 17.690536 | Yes |
| pilot_007_truth | 0.937108 / 11.505817 | 0.937108 / 11.505817 | Yes |
| pilot_014_minus | 0.358539 / 11.611344 | 0.358539 / 11.611344 | Yes |
| pilot_014_truth | 2.562331 / 20.036249 | 2.562331 / 20.036249 | Yes |

All 12 cases retain opposite decisions after complete downstream recomputation, at both budgets: 24/24 tested pairs. The exact fixed-final-penalty decision bounds are also conclusive for all their endpoints. Full density/psi changes, actual objective gaps and frozen-versus-full W values are retained in `near_optimal_full_path_comparison.csv`. The finite paths establish these concrete full-path counterexamples. They do not prove a full-path uniform-in-epsilon result, enumerate every admissible coefficient vector or establish global decision stability in any other case.

## Assessment of Policy C and remaining condition

| Criterion | Finding |
|---|---|
| Original outcome objective | Preserved exactly for the archived numerical inputs |
| Residual signs | Exact rational <=0 signs; all evaluated paths verified |
| Reproducibility | All native repeats bitwise; all RNG states matched and unchanged |
| Historical instrument procedure | Retained density proxy, transformed ordinary intercept, adaptive penalties and stopping rules |
| Downstream accuracy | Independent numerical cross-checks and 144 exact fixed-penalty optimum certificates pass |
| Decision uncertainty | Certified over fixed-weight/fixed-penalty native-objective sublevels; propagation through density/adaptation remains conditional |
| Computational feasibility | Practical on this saved panel; new-sample scalability, degeneracy and failure rates are not measured |

Recommendation: retain Policy C as the numerical policy under development, preserving the native downstream procedure and exact outcome ranks. Do not switch to a new tie convention or refine the adaptive fits silently. Return explicit unresolved statuses on failed outcome, instrument or inference certificates. Keep both legacy paths as audit comparators and keep unresolved cases in reporting denominators.

The precise remaining proof gap is between certified outcome residuals and the final adaptive penalties: high-precision density agreement and replayed adaptive traces do not enclose all values/branches allowed by floating density, centering, initialization and intermediate shooting error. To close it, derive outward density/centering bounds and propagate them through the local adaptive path, certifying its selections and stopping branches or enclosing alternative branches. Then propagate the resulting penalty/coefficient regions to W. This is limited saved-input validation; it does not require new datasets or a Monte Carlo. Current results provide all traces, margins and certificates needed to target that work.

## Cost, reproducibility and preservation

Preparation took 39.45 seconds including exact near-optimal construction and input protection. Native paths, repeated fits and captured penalty replays totaled 42.80 seconds. Primary exact downstream audit took 255.15 seconds; independent rational verification took 488.97 seconds. These exclude a future independent outcome solver, data generation and broader grids. Exact certification dominates cost. The retained audit artifacts are deliberately extensive; a future implementation needs an explicit storage/certification strategy, without discarding unresolved cases.

The initial protected snapshot contains 10,958 existing files outside this subdirectory/Git metadata, including all Stage 2G sources and certificates. Stage 2E, Stage 2F and Stage 2G input manifests were checked. Final preservation and the self-excluding SHA-256 manifest are generated by `finalize.py`; they must pass before this task is considered complete. No historical code, output, manuscript or prior certificate was edited. No commit, push, Stage 2C continuation, DGP implementation or Monte Carlo was performed.

The first native R launch completed all 72 records but the PowerShell redirection wrapper reported status 1 after a startup locale warning; its actual R exit code was not captured directly. Subsequent direct subprocess verification returned R status 0 and reconstructed all 72 new and 48 archived paths. `run_r.py` records direct R return codes for reproducible fresh runs. This orchestration anomaly is not counted as a fit failure; it is retained in execution notes. The verification exporter was extended to expose adaptive traces and rerun within this new directory.

## Required conclusions

1. **Exact versus near-optimal inference:** exact Policy C ranks define an unambiguous outcome-score input. All 12 selected cases also have concrete near-optimal alternatives with opposite fully recomputed decisions at both tested budgets.
2. **Complete-path comparisons:** all 24 C paths were evaluated; both priority cases accept. A/B differ in two decisions, A/C in five, and B/C in five. No result is presented as a coverage estimate.
3. **Remaining limitations:** density/adaptive-path uncertainty is independently checked numerically but not propagated in the exact decision certificates. Global full-path stability, general degeneracy handling beyond unresolved status, and inference validity are not established.
4. **Recommended numerical policy:** exact outcome optimization/sign certification with the preserved native density/projection path, explicit certificate scope and unresolved statuses; no coverage-driven tie or solver selection.
5. **Stage 2H:** B — Conditional; do not begin yet under a strict complete-path certification requirement. Complete the specified local downstream propagation check, then keep the bounded-treatment DGP and its analytical assumption review separate from the numerical implementation. Numerical reproducibility does not establish asymptotic validity. Stage 2G-F stops after reporting.
