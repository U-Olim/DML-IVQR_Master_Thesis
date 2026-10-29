# Stage 2B — Outcome nuisance and instrument projection diagnostics

22 October 2026, Asia/Tashkent. Branch: `journal-validation`.
Base commit: `90509cbd8ed093f90554e417756f0d1913a29ed3`.
Run directory: `output/controlled_20261022_01/` (local, untracked).

## 1. Executive summary

**Confirmed numerical effect:** replacing estimated outcome coefficients with
the known structural coefficients materially changes W and acceptance in the
primary pilot, with density weights and instrument projections held exactly
fixed. DML acceptance changes from 25/40 to 39/40; Full-GMM from 21/40 to
38/40. These are diagnostic benchmarks, not feasible-estimator coverage results.

**Confirmed numerical effect:** a constant-inclusive weighted projection removes
the missing weighted-constant moment for Oracle/Full. The DML transformed
constant treatment likewise removes that constant moment while retaining
nonzero, penalty-related slope moments. Improved weighted orthogonality does
not generally improve acceptance: primary DML projection-only acceptance is
24/40 versus 25/40 under V00.

**Inconclusive:** population calibration, the causal explanation of the archived
.498 coverage, and theoretical validity. The known-nuisance benchmarks being
near .95 in this small primary pilot do not resolve these questions.

All 768 factorial variant evaluations completed, covering 192 estimator/sample/
design tasks. There were no numerical failures or estimator warnings. All
canonical candidate replays agree exactly. Independent W recomputation agrees
within 4.62e-14. A pre/post SHA-256 comparison found no changes to any of
3,795 protected files, including all 464 Stage 2A files/artifacts. No manuscript,
canonical estimator/configuration, historical output, or Stage 2A file changed.
Nothing was committed or pushed.

## 2. Design and all implementation variants

All designs have n=1000 and all three estimators. The primary uses the same
40 samples and pivotal streams as the Stage 2A pilot, not an independent new
Monte Carlo replication. Two limited contrasts use the first 12 primitive sets:

| Design | tau | kappa | Replications per estimator |
|---|---:|---:|---:|
| primary | .90 | 1.00 | 40 |
| median | .50 | 1.00 | 12 |
| weak | .90 | .10 | 12 |

The full primary set and contrast subset sizes were fixed before execution.
No sample, variant, stream, or outlier was selected or removed based on results.
Contrasts and the primary share primitive draws and must not be treated as
independent evidence across designs.

| Variant | Outcome nuisance | Instrument projection |
|---|---|---|
| V00 | Original candidate-specific QR/quantile Lasso | Original |
| V10 | Structural intercept 1, seven slopes 5, others 0 | Original |
| V01 | Same fitted outcome nuisance as V00 | Modified weighted constant |
| V11 | Same known coefficients as V10 | Same modified projection as V01 |

For each sample/design/estimator, calculate the archived density proxy ONCE:

`f = dnorm(e_V00, mean(e_V00), var(e_V00))`.

**Both the convention and the actual vector f are frozen in all four cells.**
Known-nuisance residuals do not cause density re-estimation. This isolates
outcome nuisance replacement from density and projection changes. It also
means these cells are not new end-to-end estimators that refit every dependent
component. Density vectors can differ across estimators because their original
outcome fits differ. No SD-proxy arm was evaluated here.

All tests use exact alpha0 = 1+qnorm(tau), the uncentered original score second
moment, direct `solve()`, and cutoff qchisq(.95,2)=5.99146454710798. There is
no grid search, cross-fitting, ridge, generalized inverse, or new solver tuning.

### Exact projection definitions and library limitation

Write w=sqrt(f), Xt=[1,X]. Oracle/Full compare the original weighted projection
on X alone against the weighted projection on Xt, using identical f. Original
raw residuals have no fitted constant; modified raw residuals do.

For DML, the original final penalized quadratic objective is

\[
 \|w Z_j-c-wX\gamma_j\|^2+\sum_k\lambda_{jk}|\gamma_{jk}|.
\]

Its raw score residual remains Z_j-c-X gamma_j. The ordinary transformed
intercept thus differs from a properly weighted raw-scale constant.

The modified objective is

\[
 \|w(Z_j-c-X\gamma_j)\|^2+\sum_k\lambda_{jk}|\gamma_{jk}|.
\]

Here c is unpenalized and **the numerical slope penalty vector is identical**
to the one actually used in the original final solve. Let
M_w=I-w(w'w)^(-1)w'. The modified fit solves the penalized regression of
M_w(w Z_j) on M_w(wX), then recovers
c=w'(w Z_j-wX gamma_j)/(w'w). This is an exact profiling of the unpenalized
transformed constant in the stated objective.

Historical `hdm` has no API for an arbitrary unpenalized sqrt(f) column.
Adding that column as an ordinary slope would penalize it; using a different
intercept setting and rerunning adaptive calibration would also change penalty
inputs. Those are not the isolated comparison requested here.

Instead, a private in-memory copy of `rlasso.default` records the penalty
actually passed to its last `LassoShooting.fit` call. Its original final solve
is replayed first and reproduces the original coefficients exactly. The modified
solve uses the same historical solver, numerical slope penalties, and default
tolerances. No package namespace or installed file is modified.

This is a **controlled final-objective intercept ablation**, not a rerun of the
full adaptive penalty algorithm on the modified design. The latter was not
executed. This limitation matters when generalizing the comparison to a proposed
feasible estimator. The library's effective c=.5, gamma=.1/log(n), post=FALSE,
and original loading/penalty history are retained and recorded.

The returned `fit$lambda` is not assumed to be the last-used vector: the adaptive
routine updates its penalty after solving. In all 64 DML tasks, its stored
next vector differed from the actually-used vector by more than 1e-12; the
largest coordinate discrepancy was .005347. Capturing the actual vector avoids
this otherwise subtle tuning change.

## 3. Exact isolation and validation checks

Before the primary run, 18 complete factorial tasks were validated: the first
two samples in all three designs, for all three estimators. All passed. Every
one of the subsequent 192 tasks also replays the actual canonical candidate
using the matched data and full RNG state.

| Check | Executed result |
|---|---|
| V00 vs canonical candidate W | Exactly equal in 192/192 tasks |
| V00 vs Stage 2A primary baseline W | Exactly equal in all 120 primary tasks |
| Primary data and pivotal hashes vs Stage 2A | Identical |
| Same data across variants and estimators | Passed for all 64 sample/design settings |
| Same density values across four cells | Passed in all 192 tasks |
| Same residual within V00/V01 and V10/V11 | Passed in all 192 tasks |
| Same projection within V00/V10 and V01/V11 | Passed in all 192 tasks |
| Actual DML final penalty replay | Exact original coefficient reproduction in all 64 tasks |
| Known outcome coefficients and rank indicators | Passed; zero known rank-indicator mismatches |
| Projection dimensions/rank | All designs full column rank |
| Density weights | All finite and positive; no zeros |
| Instrument fitting consumes no further RNG | Passed |
| Independent W calculation | Maximum discrepancy 4.62e-14 |
| Independent orthogonality/coefficient reconstruction | Passed |
| Protected-file SHA-256 checks | 3,795/3,795 unchanged, including Stage 2A |

The independent calculation forms per-observation scores, uses row sums and
`tcrossprod()` for the second moment, and solves the two-dimensional quadratic
form without the candidate's n-by-n diagonal construction.

No scientific assertion failed. Presentation review caught factor-coded labels
in the first generated Markdown table and clipped plot labels; these were fixed
inside the Stage 2B summarizer. Only deterministic summaries/plots were regenerated,
with no data or experimental model rerun. Original computation logs are retained.

## 4. Outcome nuisance diagnostics

The DGP gives, at truth,

\[
Y-\alpha_0D=1+5\sum_{j=1}^7X_j+D(u-q_\tau),
\qquad q_\tau=\Phi^{-1}(\tau).
\]

Thus the stated intercept/slopes are correct, and the known residual is
D(u-q_tau). It was checked against both the executable DGP and direct residual
substitution. Because D>0 in these samples, its sign exactly matches u-q_tau.
Since u is independent of X and observed Z, the structural rank restriction
E[tau-1{u<=q_tau}|X,Z]=0 holds under this DGP. This does not require claiming
that the density-weighted orthogonal construction is regular.

Primary results, averaged across the same 40 samples:

| Estimator | Mean intercept error | Mean coefficient L2 error | Mean nuisance prediction RMS | Mean estimated score | Mean rank-indicator mismatch |
|---|---:|---:|---:|---:|---:|
| Oracle-GMM | .01734 | .07269 | .02448 | -.001975 | .02693 |
| Full-GMM | .09523 | .69629 | .18430 | .012725 | .09288 |
| DML-IVQR-BC | -.08512 | .12894 | .02718 | .025025 | .04738 |

The known-nuisance mean score is .000850, with across-sample MCSE .001455,
for all three estimators. Estimated-score MCSEs are .000501, .004216, and
.000244 respectively. All known rank-indicator mismatch counts are zero.

The DML mean intercept-penalty score target lambda_intercept/(2n) is .025719
in the primary design. Under the preserved objective, a positive penalized
intercept permits a nonzero score sum through its KKT equation. Exact ties,
subgradient choices and numerical tolerances prevent equating the supplied
`<=0` indicator score to that target exactly. This is a documented estimating-
equation relationship, **not an isolated test that intercept penalization causes
the coverage distortion**. Outcome intercept and slopes were replaced together.

Conditional diagnostics use fixed quartile bins of X1 and observable excluded
components Z1-X2-X3-X4 and Z2-X7-X8-X9-X10. For example, primary DML mean
scores in X1 bins 1–4 are .01489, .02119, .02975, .03375 under fitted
nuisances, versus .00356, .00403, .00032, -.00507 with known nuisances.
The corresponding across-replication MCSEs are approximately .0023–.0029
and .0027–.0031. These are descriptive binned diagnostics, not tests of every
conditional moment or a multiple-testing-adjusted significance analysis.

Primary raw instrument moments E_n[Z_j*s], averaged across replications:

| Estimator / nuisance | Z1 moment | Z2 moment |
|---|---:|---:|
| Oracle / estimated | -.00559 | -.00751 |
| Full / estimated | -.00353 | .00033 |
| DML / estimated | .01937 | .02584 |
| Known, all three | .00181 | .00300 |

D-bin diagnostics use a nonzero target: u|T is N(.1*T,.97), so the target is
tau-Phi((q_tau-.1*T)/sqrt(.97)). Zero is not asserted conditional on endogenous
D. Full raw and conditional moments, counts, and uncertainty are saved in CSVs.

Classification: **Confirmed numerical effect** on nuisance errors, scores, W
and some decisions; **Inconclusive** about which outcome-nuisance feature is
responsible in general or how much of the archived distortion it explains.

## 5. Projection orthogonality diagnostics

For each instrument, all entries of

\[
 n^{-1}\widetilde X'\operatorname{diag}(f)\Psi'
\]

are saved in `weighted_orthogonality.csv`. The table shows the primary mean
of the maximum absolute constant entry and maximum absolute slope entry per
sample, not a maximum of signed averages:

| Estimator | Projection | Constant residual | Slope residual |
|---|---|---:|---:|
| Oracle | Original | .004094 | 1.10e-15 |
| Oracle | Modified | 3.79e-15 | 2.53e-15 |
| Full | Original | .001217 | 4.95e-15 |
| Full | Modified | 1.23e-13 | 6.52e-14 |
| DML | Original | .028713 | .024377 |
| DML | Modified | 3.36e-17 | .013946 |

Oracle/Full weighted slope equations already hold; adding the constant supplies
the missing constant equation. For DML, the modified constant is unpenalized,
but slopes remain penalized and their weighted moments should not be assumed
zero. For the fixed final objective, 2*(wX)'error equals lambda*sign(gamma)
at active coordinates and is bounded by lambda at inactive coordinates, up to
solver tolerances.

Across all settings, maximum recorded slope KKT violation divided by n was
2.66e-7 for the original fit and 1.21e-8 for the modified fit. Original ordinary
transformed-intercept gradients were near zero (maximum 4.90e-13); modified
weighted-intercept gradients were near zero (maximum 1.27e-13). These are
different equations. Improved proxy-weighted orthogonality does not establish
orthogonality under the theoretical conditional density.

All weighted designs were full rank. R `kappa()` condition estimates ranged:

| Estimator | Original control Gram | Modified control Gram |
|---|---|---|
| Oracle | 17.74–22.17 | 60.36–82.82 |
| Full | 80.72–96.98 | 743.55–1113.30 |
| DML | 23.65–35.57 | 11.08–14.89 |

DML Grams refer to slope designs after partialling out the corresponding
constant. Adding a constant need not improve conditioning. All two-instrument
second-moment inversions succeeded. No density clipping or matrix stabilization
was introduced.

Classification: **Confirmed numerical effect** on weighted constant conditions
and W; **No detectable effect in the pilot** on Oracle projection-only decisions;
**Inconclusive** for inferential validity.

## 6. Compact factorial results for every estimator/design

Each variant cell contains **mean W / acceptance frequency**. For V10/V11,
acceptance is diagnostic known-nuisance coverage, not published-estimator coverage.
All cells have zero failures.

| Design | Estimator | N | V00 | V10 | V01 | V11 |
|---|---|---:|---:|---:|---:|---:|
| primary | Oracle-GMM | 40 | 2.108 / .925 | 1.847 / .975 | 2.110 / .925 | 1.856 / .975 |
| primary | Full-GMM | 40 | 7.440 / .525 | 2.008 / .950 | 7.410 / .575 | 1.999 / .950 |
| primary | DML-IVQR-BC | 40 | 5.812 / .625 | 1.906 / .975 | 6.126 / .600 | 1.929 / .950 |
| median | Oracle-GMM | 12 | 3.255 / .917 | 2.316 / .917 | 3.242 / .917 | 2.325 / .917 |
| median | Full-GMM | 12 | 2.488 / .917 | 2.189 / .917 | 2.491 / .917 | 2.108 / .917 |
| median | DML-IVQR-BC | 12 | 4.047 / .750 | 2.321 / .917 | 4.180 / .750 | 2.308 / .917 |
| weak | Oracle-GMM | 12 | 1.928 / 1.000 | 2.166 / 1.000 | 1.933 / 1.000 | 2.182 / 1.000 |
| weak | Full-GMM | 12 | 2.374 / .917 | 2.048 / .917 | 2.378 / .917 | 2.064 / .917 |
| weak | DML-IVQR-BC | 12 | 1.381 / 1.000 | 2.105 / 1.000 | 1.388 / 1.000 | 2.209 / .917 |

Known coefficients do not uniformly lower W across designs: the weak-instrument
contrast has higher mean W under V10 for Oracle and DML. Small changes can
cross a threshold, while large W changes need not change a decision.

Primary paired changes in W, with MCSE in parentheses:

| Estimator | V10−V00 | V01−V00 | V11−V00 | Interaction W11−W10−W01+W00 |
|---|---:|---:|---:|---:|
| Oracle | -.260 (.312) | .0025 (.0040) | -.252 (.312) | .0058 (.0082) |
| Full | -5.432 (.933) | -.0303 (.0137) | -5.441 (.932) | .0211 (.0121) |
| DML | -3.905 (.767) | .3140 (.0574) | -3.883 (.763) | -.2911 (.0454) |

The interaction is a controlled numerical nonadditivity measure for these
specific components, not a general causal effect of estimator properties.
All per-replication interactions and both W/acceptance interaction MCSEs are
saved. DML's primary mean acceptance interaction is zero with MCSE .0358,
despite its nonzero mean W interaction.

Plot: [primary_factorial_W.png](output/controlled_20261022_01/primary_factorial_W.png).

## 7. Pilot rejection, diagnostic coverage and uncertainty

Primary acceptance counts and marginal Wilson 95% Monte Carlo intervals:

| Estimator | V00 | V10 | V01 | V11 |
|---|---|---|---|---|
| Oracle | 37/40 [.801,.974] | 39/40 [.871,.996] | 37/40 [.801,.974] | 39/40 [.871,.996] |
| Full | 21/40 [.375,.671] | 38/40 [.835,.986] | 23/40 [.422,.715] | 38/40 [.835,.986] |
| DML | 25/40 [.470,.758] | 39/40 [.871,.996] | 24/40 [.446,.737] | 38/40 [.835,.986] |

Rejection frequency is one minus the reported acceptance frequency and is
stored explicitly for every cell in `variant_summary.csv`. For example,
primary DML rejection frequencies are .375, .025, .400, .050. These intervals
describe uncertainty in Monte Carlo frequencies, not structural-parameter sets.

Primary paired acceptance changes, with MCSE:

| Estimator | V10−V00 | V01−V00 | V11−V00 |
|---|---:|---:|---:|
| Oracle | +.050 (.050) | .000 (.000) | +.050 (.050) |
| Full | +.425 (.0869) | +.050 (.0349) | +.425 (.0869) |
| DML | +.350 (.0764) | -.025 (.0250) | +.325 (.0750) |

Under primary V10, Oracle has three rejection-to-acceptance and one reverse
change, Full has 18 and one, and DML has 14 and zero. Projection-only V01
has no Oracle changes, two Full rejection-to-acceptance changes, and one DML
acceptance-to-rejection change. Thus unchanged net frequencies should not
automatically be interpreted as identical decisions.

Marginal coverage MCSE is sqrt(p*(1-p)/R); paired change/interaction MCSE is
the sample SD of per-replication differences divided by sqrt(number of complete
pairs). The correlated four variants are not counted as additional replications.
All 36 variant cells have their individual denominators, failures, marginal
MCSEs and Wilson intervals recorded. All 36 paired-effect summaries include
complete-pair counts and MCSEs. With 12 contrast samples, uncertainty is large;
12/12 acceptance still has Wilson lower bound .758. A zero empirical MCSE at
all-acceptance or zero-discordance does not imply zero population uncertainty.
No conclusive significance or population-calibration claim is made.

## 8. Execution record, environment and failures

Executed orchestration:

```powershell
python -B journal_validation/stage2b/run_stage2b.py --run-id controlled_20261022_01
```

It exited 0. With `R343` denoting the explicit historical executable and `OUT`
the absolute run directory, child/review commands were:

| Command | Exit |
|---|---:|
| `R343 --vanilla journal_validation/stage2b/run_diagnostics.R validate OUT` | 0 |
| `R343 --vanilla journal_validation/stage2b/run_diagnostics.R primary OUT` | 0 |
| `R343 --vanilla journal_validation/stage2b/run_diagnostics.R contrasts OUT` | 0 |
| `R343 --vanilla journal_validation/stage2b/summarize.R OUT` | 0 |
| Same summary command after presentation fixes/additional saved-fit diagnostics | 0 |
| `R343 --vanilla journal_validation/stage2b/verify_details.R OUT` | 0 |
| `python -B journal_validation/stage2b/verify_outputs.py OUT` | 0 |
| `python -B journal_validation/stage2b/finalize.py OUT` (final verification/preservation/inventory, no model fitting) | 0 |

Exact expanded arguments, working directories, timestamps and exit codes are
in `commands.json` and `review_commands.json`; all R master/worker outputs are
retained. Preparatory shell commands read the request, branch/status, existing
Stage 2A code and installed hdm function bodies. The initial compound inspection
exited 1 because `rg --files -g AGENTS.md` found no instruction file; this was
not a failed scientific check. Subsequent source and saved-fit inspections
exited 0. No other scientific/compatibility check failed.

Historical environment check passed in master and workers: R 3.4.3 (2017-11-30),
x86_64-w64-mingw32 on Windows, quantreg 5.34, hdm 0.2.0, hqreg 1.4,
mvtnorm 1.0-6, doSNOW 1.0.16, snow 0.4-2, foreach 1.4.3,
iterators 1.0.8, SparseM 1.77, MatrixModels 0.4-1, Matrix 1.2-12,
digest 0.6.12. Full package paths/versions and session information are saved.
No dependency was installed or modified.

Randomization: L'Ecuyer-CMRG/Inversion, two task-seeded PSOCK workers.
Data reuse Stage 2A master seed 20261022, data stream indices 7–46.
Primary penalty reuse master 20261023, indices 241–280. Contrast penalty
master 20261024, indices 1–12 for median and 13–24 for weak. All complete
seven-integer states and sample/source paths are stored. The estimated outcome
fit is shared by V00/V01; known coefficients need no outcome penalty draw.
No instrument regression consumes additional randomness. Primary W/data/draw
identity with Stage 2A was independently checked, not inferred from seed labels.

Completed: 40 primary replications plus 12 per contrast; 192 estimator tasks,
768 factorial variant evaluations, plus the 18 preflight validation tasks and
canonical reference checks. Failure count is zero, and no successful result
was silently dropped. `failures.csv` preserves the empty failure schema.
Task/variant failures would be saved explicitly and counted if they occurred.

Technical limitations: R startup emits `Setting LC_CTYPE=C.UTF-8 failed` and
continues in locale C. These startup warnings are separate from the zero
recorded estimator warnings. Native DML transformed-intercept support is limited
as described above. Local ignored Stage 2A artifacts are required for reproduction;
an ordinary clone without them is insufficient. The runner refuses to overwrite
any existing run directory. All outputs remain inside Stage 2B.

## 9. Mathematical interpretation and limitations

The experiment separates five questions:

1. **Numerical sensitivity:** W changes under controlled component replacements;
   this is directly demonstrated.
2. **Rejection frequencies:** some decisions and pilot frequencies change; their
   denominators, paired dependence and Monte Carlo uncertainty are explicit.
3. **Moment validity:** known structural rank moments are justified algebraically
   by the DGP. Sample bins alone cannot establish full conditional validity.
4. **Proxy-weighted orthogonality:** the weighted constant equation improves by
   construction; penalized slope moments remain nonzero. This does not validate
   the proxy as the theoretical conditional density.
5. **Inference validity:** no variant has been established theoretically valid.

In particular, frozen V00 weights/projections are estimated using the same
observations and depend on estimated residuals. Even known outcome coefficients
do not remove every nuisance or sample-dependence issue. The unresolved
non-finite conditional-density concern of the original DGP remains. No DGP
modification, density repair, or cross-fitting was introduced here.

V10/V11 are infeasible diagnostic benchmarks. They cannot be presented as the
coverage of the published DML estimator. Their primary acceptance near .95
is not evidence that the theoretical problem has been repaired. The full-
adaptive modified-intercept DML implementation was not evaluated. The archived
.498 is not a paired comparator for this analysis; Stage 2A's saved primary
samples and streams, which V00 reproduces exactly, are the relevant baseline.

No variant is selected because its pilot acceptance happens to be closest to
.95. The small, reused sample set and exploratory contrasts do not support a
general causal explanation or an asymptotic conclusion.

## 10. Recommended next experiment and conclusion classification

**Proposed Stage 2C, not executed:** a narrowly controlled outcome-intercept
penalty ablation. On matched samples/draws, set only the supplied quantile-Lasso
intercept penalty to zero while preserving the original numeric slope penalty
vector, frozen density vector, and instrument projection. Record intercept/slopes,
rank-score centering, conditional raw moments, W and paired decisions. This is
motivated by the large known-outcome replacement effect, modest projection-only
effect, nonzero DML score mean, and its relationship to the intercept penalty.
It would separate a specific feasible fitting convention from replacing the
entire nuisance vector with truth. It must be prespecified and reviewed, not
selected by proximity of coverage to .95.

Theoretical density regularity still requires a separate resolution before
submission claims about calibrated weak-instrument inference. A larger Monte
Carlo should follow a defined question and precision target, not precede them.

| Finding | Classification |
|---|---|
| Primary W/decisions change under known outcome coefficients | Confirmed numerical effect |
| Modified projections improve the weighted constant equation | Confirmed numerical effect |
| Primary DML projection-only change raises mean W and changes one rejection | Confirmed numerical effect |
| Oracle projection-only rejection decisions do not change in tested samples | No detectable effect in the pilot |
| Known outcome replacement lowers W uniformly across designs | Not supported; weak-contrast counterexamples observed |
| A particular modification restores population calibration | Inconclusive |
| The archived .498 distortion is causally explained by one nuisance feature | Inconclusive |
| Full adaptive transformed-intercept DML, intercept-penalty ablation, new DGP, 500-replication run, manuscript revisions | Not executed |

Instructions are in `README.md`. Main machine-readable tables are
`compact_factorial.csv`, `variant_summary.csv`, `paired_effect_summary.csv`,
`outcome_summary.csv`, and `conditional_moment_summary.csv`. Detailed fitted
objects, full orthogonality matrices and actual penalty traces are retained
under the run directory. `output_verification.json` records independent checks;
`preservation.json` records original/Stage 2A preservation.
`final_preservation.json` repeats that check after report preparation;
`source_sha256.json` and `artifact_manifest.csv` inventory the final local
scripts, documentation and outputs. Ignored runtime artifacts require separate
backup when sharing this branch.

Stage 2B stops here. Stage 2C awaits review.
