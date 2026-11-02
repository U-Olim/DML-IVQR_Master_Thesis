# Stage 2G — numerical score-evaluation policy

2 November 2026, Asia/Tashkent. Branch `journal-validation`; base HEAD `50412fe7b6858b86eebb8874a820bf7651eb83cf`.

## Result and scope

All 24 saved Stage 2E candidate problems admit independently verified exact primal/dual certificates and unique exact optima. Policy C certifies all 24,000 residual signs, including 751 exact zeros (25–39 per problem). There are zero unresolved optimum reconstructions, zero singular score matrices and zero excluded cases. This extends Stage 2F to the entire fixed panel, including `pilot_007_minus`; its earlier Stage 2E classification C is preserved and is not retroactively relabeled.

Exact <=0 outcome ranks remove the ambiguity about what the unique mathematical outcome optimum implies. They do not make floating near-optimal ranks stable. Twelve cases have exact opposite-decision witnesses among locally admissible tied-sign configurations for every positive objective budget, conditional on fixed historical psi. Search did not establish global stability for the remaining twelve.

Recommended direction: versioned Policy C, with independent numerical optimization only proposing the exact basis and unresolved certification explicitly returned. **Stage 2H is not ready to simulate:** a complete density/instrument-projection arithmetic contract and end-to-end saved-panel validation remain prerequisites. No claim of inferential calibration follows from these certificates.

## Formal numerical problem and policies

See [NUMERICAL_POLICIES.md](NUMERICAL_POLICIES.md) for the exact penalized objective, dual, rank score, second moment, W and policy contracts. All coefficients of the exported binary64 problems, including tau, are interpreted as exact rationals. The mathematical optimum, numerical coefficient approximation, floating residual calculation, rank vector and rejection decision are separately recorded. Positive intercept and slope penalties, candidate-adjusted responses, ordering and the historical cutoff 5.99146454710798 are unchanged.

| Policy | Fidelity | Reproducibility / accuracy | Stability and cost | Future feasibility |
|---|---|---|---|---|
| A historical | Archived executable | Fixed software and streams; true objective gaps now known | Objective accuracy does not certify ranks; no new fit cost here | Baseline audit only |
| B independent floating | Identical objective and <=0 formula | Saved independent solver plus exact objective bounds | Better coefficients still have uncertain optimum signs | Suitable basis proposal; inadequate alone |
| C certified exact signs | Preserves unique exact optimum and <=0 | Rational primal/dual, uniqueness, exact ranks and conditional W | Exact outcome ranks; downstream arithmetic still needs specification | Conditional recommendation; degeneracy fallback required |
| D strict exact ties | Changes finite-sample score | Deterministic and fully explicit | Can change W and decision; no calibration justification | Separate variant only |

## Fixed-panel results

W below uses saved historical psi throughout. B uses the saved independent R residual signs; C uses exact-optimum <=0; D uses exact-optimum <0. A/R indicate acceptance/rejection at the unchanged cutoff. Full sums and second moments, both saved instrument branches, rank differences and exact rational inference certificates are in `results/policy_results.csv` and each case directory.

| Case | Exact ties | A W | B W | C W | D W | Opposite local decisions proved |
|---|---:|---:|---:|---:|---:|---|
| pilot_002_minus | 29 | 6.336102 R | 3.017456 A | 5.174445 A | 3.162989 A | Yes |
| pilot_006_truth | 33 | 5.490874 A | 6.041387 R | 2.806474 A | 13.578634 R | Yes |
| pilot_001_minus | 27 | 20.788991 R | 18.458926 R | 19.636635 R | 14.068879 R | Not established |
| pilot_001_plus | 25 | 30.064169 R | 30.529468 R | 25.460307 R | 33.255300 R | Not established |
| pilot_001_truth | 32 | 0.488466 A | 0.306202 A | 1.090510 A | 0.812075 A | Not established |
| pilot_002_plus | 32 | 44.738021 R | 45.924754 R | 37.997096 R | 53.624881 R | Not established |
| pilot_002_truth | 30 | 6.857863 R | 6.905266 R | 3.956804 A | 13.582885 R | Yes |
| pilot_003_minus | 37 | 5.179703 A | 5.509242 A | 6.748437 R | 2.962748 A | Yes |
| pilot_003_plus | 28 | 55.495969 R | 59.396705 R | 50.840703 R | 66.476774 R | Not established |
| pilot_003_truth | 36 | 14.436100 R | 9.461010 R | 4.958924 A | 19.410338 R | Yes |
| pilot_004_minus | 28 | 8.057616 R | 7.900804 R | 8.970357 R | 8.645789 R | Yes |
| pilot_004_plus | 35 | 42.826281 R | 39.706640 R | 39.305314 R | 50.041198 R | Not established |
| pilot_004_truth | 34 | 13.490802 R | 15.528197 R | 8.083667 R | 19.986476 R | Yes |
| pilot_005_minus | 28 | 1.120578 A | 1.007009 A | 1.337125 A | 0.378472 A | Not established |
| pilot_005_plus | 35 | 76.218252 R | 72.234786 R | 66.771220 R | 75.232254 R | Not established |
| pilot_005_truth | 27 | 26.867613 R | 30.390196 R | 20.312172 R | 36.130944 R | Not established |
| pilot_006_minus | 29 | 3.613931 A | 3.446248 A | 2.822513 A | 3.426872 A | Yes |
| pilot_006_plus | 35 | 43.891059 R | 45.423010 R | 41.899745 R | 53.043972 R | Not established |
| pilot_007_minus | 31 | 11.134964 R | 9.169114 R | 9.813158 R | 12.145190 R | Yes |
| pilot_007_plus | 26 | 48.339223 R | 49.455222 R | 39.772902 R | 56.074286 R | Not established |
| pilot_007_truth | 30 | 3.709285 A | 3.157995 A | 3.393074 A | 8.547755 R | Yes |
| pilot_014_minus | 39 | 5.244829 A | 2.293761 A | 4.322082 A | 4.470764 A | Yes |
| pilot_014_plus | 28 | 44.067797 R | 35.763925 R | 35.878769 R | 50.725209 R | Not established |
| pilot_014_truth | 37 | 6.343335 R | 9.598156 R | 4.501609 A | 16.200065 R | Yes |

C changes the historical frozen-psi decision in 5/24 problems; this is a fixed-panel comparison, not a Monte Carlo coverage estimate. C decisions agree between the historical and independent saved psi branches for all 24 problems. Neither branch is a recomputed C downstream path.

## Accuracy, signs and independent verification

All exact-optimum primal and dual bounds coincide, so their objective gaps are exactly zero. Historical true suboptimalities range from 1.41395e-11 to 4.47763e-8; independent true suboptimalities range from 9.14735e-14 to 8.64949e-13. Per-case `accuracy.json` reports these rational bounds, maximum coefficient and fitted-value errors relative to the exact optimum, and exact reevaluation of each saved coefficient vector. C and D share the exact coefficient/fitted vector and zero error relative to that certified optimum; they differ only in ranks.

Floating R residual signs versus exact residual signs of the SAME stored vector differ at 0 historical and 57 independent observations in aggregate. These representation effects are separate from differences between a stored vector and the exact optimum. All exact zero signs are certified at the singleton optimum; no tolerance-based zero convention is used.

`signs.csv` identifies all tied and untied observations. Untied signs are locally stable; tied signs are locally ambiguous over every positive objective budget. No global stability over a specified positive sublevel is claimed for untied signs. A/B certified-optimum-sign counts are zero by policy guarantee, not a claim that every archived sign is incorrect. C/D certify all signs of their explicitly defined statistics.

The separate verifier imports no reconstruction routine. It recomputes residuals, primal and dual objectives, feasibility, strict complementary margins, nonsingularity, both saved-vector objective gaps, all six conditional inference records per case (144 total), and both sensitivity endpoints. It uses Fraction sums and independent elimination rather than the primary integer reconstruction/statistic implementation. Its audit status is PASS for all 24 problems. Certificates concern outcome optimization and conditional inference; instrument fits are not certified exact optimizers.

## What can be certified about rejection?

At the exact singleton optimum with declared saved psi, W and its comparison to the archived cutoff are certified exactly for every case. At positive objective budgets, the nonsingular tied/active design realizes any tied residual sign pattern locally. Continuity preserves untied signs and the check-loss/L1 Lipschitz bound makes its objective gap arbitrarily small. Therefore two opposite certified W decisions on those patterns prove failure of decision invariance for every positive budget under that fixed psi.

Deterministic coordinate searches find such pairs in 12 cases, including both original disagreements. Their exact ranks and rational W values are retained; the verifier checks non-tie agreement and endpoint inference. The search is neither exhaustive nor a global enclosure of W. In the other cases, no certificate of stability is obtained. Universal conditional bounds 0 <= W <= 1000 for nonsingular S are valid but inconclusive at the cutoff. No positive-budget full downstream-path stability claim is made.

Intervals can prove a sign when zero is excluded, but an interval crossing zero is ambiguous. Fitted-value LP extrema over a certified objective sublevel can provide global certificates when their bounds separate zero; this more expensive approach was assessed conceptually, not executed here. Exact basis reconstruction is decisive for this panel because it proves exact zeros and uniqueness. A small objective gap alone provides neither sign nor decision certification.

## The two historical disagreements

`pilot_002_minus`: A rejects (6.336102); floating B accepts (3.017456); certified C accepts (5.174445). `pilot_006_truth`: A accepts (5.490874); floating B rejects (6.041387); certified C accepts (2.806474). These outcomes resolve the exact-outcome-score question conditional on saved psi, while retaining the archived disagreements as historical facts. They do not prove solver-invariant floating behavior or a certified new complete path. D rejects the second case (13.578634), demonstrating why a changed tie convention is a distinct statistic.

## Bounded-treatment transition: analytical specification only

The proposed D_delta=.05+.9 Phi(T) lies strictly in (.05,.95), with T equal to the existing latent treatment index. Retain the primitive dependence, instruments and outcome equation y=1+D_delta+X b+u D_delta; alpha0=1+qnorm(tau) follows because D_delta>0 and u is independent of the instruments and X. At truth the structural residual is D_delta(u-q_tau), so its rank is the same as u<=q_tau. This does not remove sample quantile-fit ties.

For the current normal primitives, conditionally on T and primitive z1,z2,w, epsilon is known and u|epsilon is N(.3 epsilon,1-.3^2). The conditional structural residual density at zero is therefore phi((q_tau-.3 epsilon)/sqrt(.91))/(D_delta sqrt(.91)); conditioning on fewer variables requires taking the appropriate conditional expectation. It is bounded above by 1/(.05 sqrt(.91) sqrt(2 pi)); inverse treatment moments are bounded by 20^k. This gives useful upper/moment bounds, not a uniform positive lower bound conditional on unbounded epsilon, nor a proof of all identification/restricted-eigenvalue conditions.

Before Stage 2H derive the density under the actual conditioning set used by its theorem, check the required lower-density/local-smoothness and weighted-moment assumptions, and assess relevance, endogeneity and sparse-design identification after the monotone transformation. Keep the historical density call (which passes var(e) as the normal scale) explicitly separate from any proposed oracle/corrected density arm. Do not silently correct it as part of outcome-sign certification.

For a future implementation: generate a separately versioned bounded-DGP sample on new matched streams, compute each candidate response and penalty once, use the frozen C outcome/sign contract, apply a separately frozen density/projection contract, compute certified conditional W and return unresolved statuses explicitly. Separate changes to DGP, optimization, residual evaluation and density arms. This document implements none of that DGP or simulation.

## Cost, integrity and limitations

Saved-panel reconstruction, exact accuracy evaluation and sensitivity search took 12.09 seconds summed over 24 cases (0.37–0.69 seconds each). The completed validator took 21.26 seconds including its post-check; the initial whole-repository snapshot was taken in an earlier attempt and is not included in that resumed runtime. Independent Fraction verification took 55.20 seconds. These measurements exclude original Stage 2E numerical optimization and any new projection fit; they do not predict full Monte Carlo runtime or scaling under larger/degenerate bases.

The initial run stopped before case analysis because a Windows case-insensitive manifest glob also matched historical_manifest_verification.json. The code was corrected to select SHA256_MANIFEST.json explicitly, then resumed from the original protected snapshot. No historical input was edited. This execution correction and initial state are retained in `EXECUTION_NOTES.json`.

Stage 2E and Stage 2F manifests verified 859 and 50 artifacts. Pre/post protection checks cover 10,795 existing files outside Stage 2G/Git metadata: zero changed, missing or added. All new files are in Stage 2G. The final self-excluding SHA256 manifest covers its source and results. No original estimator, historical output, earlier validation result or manuscript was modified; no commit/push or Monte Carlo was performed.

## Required conclusions and Stage 2H prerequisites

1. Established problem: discontinuous residual ranks at exact optimization ties make objective accuracy insufficient for numerical inference stability, even at a unique optimum.
2. Validated policies: A/B were independently re-evaluated as saved computational outputs; C certifies the exact outcome optimum and conditional inference in all 24 cases; D is validated only as an explicitly changed statistic.
3. Both historical disagreements are resolved at the exact outcome-score level conditional on either saved psi, with C accepting both. Full newly recomputed C paths remain unvalidated.
4. Exact-singleton conditional decisions are certified in all 24 cases; positive-budget conditional noninvariance is proved in 12. Global stability in the others and full-path stability are unresolved.
5. Recommend C conditionally, with fail-closed unresolved statuses and B supplying basis proposals. No complete simulation-ready policy is claimed; coverage played no role in selection.
6. Cost is modest on this saved panel; degeneracy, multiple optima, failed basis proposals, complete projection arithmetic and larger-scale performance require additional work.
7. Before Stage 2H: freeze the complete C computational version (including density/projection arithmetic and failure handling); recompute and validate its full paths on all 24 saved candidates; test a predeclared unresolved/degenerate-case protocol without changing the objective; review the bounded-DGP analytical assumptions and predeclare density arms, streams, diagnostics and reporting denominators. Then explicitly authorize the separate DGP experiment. Stage 2G stops here.
