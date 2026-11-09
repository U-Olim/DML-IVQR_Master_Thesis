# Stage 2H paired diagnostic pilot — stopped at the resource guardrail

Run `paired_20261102T112532Z`. Fixed design: n=500/1000, p=100, s=7, rho=.3, tau=.1/.5/.9, kappa=1/.1, R=20 per cell, arms original and .05+.90 Phi(T), candidates truth+{-.5,0,.5}. Seed 2026110281, R 3.4.3 L’Ecuyer-CMRG/Inversion. Two one-thread workers; unchanged 2G-D.1/H0 numerical policy.

Planned **1,440 individual evaluations (720 pairs)**; attempted **1069**, numerically qualified **1064**, unresolved/not executed **376**. At truth: 354 qualified of 480 planned. Successful counts require every certificate and independent audit; missing decisions remain in denominator 20. The four prespecified same-input replays were not executed after the resource stop; pilot result repeatability is therefore unverified. Primitive/penalty RNG replay and independent numerical audits remain separately documented.

Measured candidate wall time including host interruption: 15.235 hours; sampled PID-tree aggregate peak RSS in the resumed phase: 3000.9 MiB. This sampled RSS counts shared pages and is not a continuous maximum. The original supervisor peak was not retained after interruption; candidate-level OS/RSS records remain available, so the full-run aggregate maximum is unknown. Preparation/replay/audit costs and raw logs remain separately available. Planning base/twofold estimates were 2.52/5.04 hours and 9.34/18.69 GiB; resource envelopes were 12 hours, 20 GiB and at least 2 GiB available memory. External candidate limit: 180 seconds.

## What the completed n=500 cells show, and what remains missing

The fixed pilot did not complete. Of 1,440 planned unique evaluations, 1,069 were attempted and 1,064 qualified; five are TIME_LIMIT_UNRESOLVED and 371 RESOURCE_NOT_EXECUTED. There were 1,071 actual process attempts because two interrupted incomplete attempts were retained and resumed on the same input IDs. The four fixed reproducibility replays were not launched after resource exhaustion. No new statistical samples or streams were substituted. All 40 primitive samples and 720 paired input/penalty sets had been prepared and independently replayed before fitting.

All six n=500 cells have 20 qualified truth observations per arm and 20 complete pairs. Bounded treatment raises observed truth inclusion in five cells and lowers it in the median/weak-instrument cell (1.00 to .90; paired difference −.10, MCSE .0688). With strong instruments, inclusion changes .85→1.00 at tau=.10 (paired +.15, MCSE .0819), .90→.95 at the median (+.05, MCSE .0500), and .75→.85 at tau=.90 (+.10, MCSE .1000). These are small-sample point estimates with pointwise exact intervals in the tables, not simultaneous evidence or proof of nominal coverage.

The upper-tail strong-instrument cell therefore still has observed undercoverage under bounded treatment, while the weak-instrument median changes adversely. The bounded arm is not a universal coverage repair. Mean-W paired changes are also mixed: for example, the completed weak-instrument median has B−A mean W +.715 (MCSE .528), whereas the strong-instrument lower tail has −1.027 (MCSE .485). The direction is not uniform across quantiles/instrument strengths.

Weak-instrument off-truth rejection remains low in the completed n=500 cells: original-arm frequencies range 0–.15 and bounded-arm frequencies 0–.10 at the two false candidates. At the strong-instrument median, both arms reject each false candidate in 19/20 samples (.95). Tail asymmetry persists: at tau=.10 with strong instruments, rejection at offsets −.50/+ .50 is .90/.20 in A and .75/.10 in B; at tau=.90 it is .20/.95 in A and .25/.90 in B. These describe the two fixed false candidates only; they do not establish interval geometry or global identification.

The n=1000 truth cells have only 8–10 qualified observations per arm out of 20 planned. Their full-planned-design coverage and paired-effect bounds remain wide; all six paired coverage-difference bounds include zero. Qualified-only or complete-pair summaries are additional selected diagnostics and cannot be substituted for the missing full design. No dependent tau/kappa cells are pooled as new independent samples.

This pattern survives the DGP change: weak-instrument power remains limited, tail behavior remains asymmetric, and statistical validity remains unsettled despite exact numerical qualification of completed fixed objectives. What changes is cell-dependent coverage, score levels and off-truth rejection. Affine relevance-scale changes (.90 covariance and .81 treatment variance) coexist with unchanged first-stage partial R²/F; the experiment does not isolate density regularity as the sole mechanism.

The actual elapsed candidate period was 15.235 calendar hours including host interruptions, exceeding the 12-hour envelope while the host was interrupted. The persistent deadline was not extended. At the next execution opportunity the driver stopped further fits and wrote all remaining IDs as not executed. The 2.52-hour base/5.04-hour planning allowance is not validated as the cost of a completed pilot by this interrupted run. Resumed sampled PID-tree RSS peaked at 2.931 GiB; the full-run aggregate maximum is unknown. The PID-tree method is sampled and can overcount shared pages or misattribute reused process IDs over long interruptions. These are measurement limitations, not proof of a future memory bound.

Retained run storage before final reporting is 7.696 GiB, below the 20-GiB envelope. All 720 unique original 1,000-draw penalty calculations were performed during preparation, with 83.050 summed internal R seconds (excludes independent replay, process launch and I/O). Candidate execution/certification/audit component times are retained in raw result JSON and the qualified-only numerical diagnostics table; late/interrupted times are preserved rather than replaced by timing averages.

Recommended next scientific task: map the retained score, historical variance-as-scale density proxy and ordinary transformed-intercept residualization to an explicit inference theorem, checking conditioning sets, nuisance orthogonality/rates and weak-instrument conditions. Any future attempt to finish or enlarge simulation after this final resource stop needs a new frozen execution protocol with a stable host and persistent wall-clock enforcement. Do not silently resume the 371 unexecuted IDs under an extended budget. The manuscript remains unchanged.

## Partial-pilot truth inclusion bounds and paired comparisons

Each row has 20 planned independent base samples. Intervals are pointwise. Coverage bounds include all unresolved/not-executed decisions; qualified-only comparisons are additional diagnostics.

| n | tau | kappa | A coverage bounds | B coverage bounds | qualified pairs | paired coverage B−A bounds | complete-pair MCSE | paired W B−A (MCSE) |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 500 | 0.1 | 1.0 | [0.850,0.850] | [1.000,1.000] | 20 | [0.150,0.150] | 0.082 | -1.027 (0.485) |
| 500 | 0.1 | 0.1 | [0.950,0.950] | [1.000,1.000] | 20 | [0.050,0.050] | 0.050 | 0.059 (0.297) |
| 500 | 0.5 | 1.0 | [0.900,0.900] | [0.950,0.950] | 20 | [0.050,0.050] | 0.050 | -0.583 (0.307) |
| 500 | 0.5 | 0.1 | [1.000,1.000] | [0.900,0.900] | 20 | [-0.100,-0.100] | 0.069 | 0.715 (0.528) |
| 500 | 0.9 | 1.0 | [0.750,0.750] | [0.850,0.850] | 20 | [0.100,0.100] | 0.100 | -0.453 (0.513) |
| 500 | 0.9 | 0.1 | [0.850,0.850] | [0.900,0.900] | 20 | [0.050,0.050] | 0.088 | -0.168 (0.454) |
| 1000 | 0.1 | 1.0 | [0.350,0.850] | [0.400,0.900] | 10 | [-0.450,0.550] | 0.100 | -1.059 (0.547) |
| 1000 | 0.1 | 0.1 | [0.450,0.950] | [0.400,0.900] | 10 | [-0.550,0.450] | 0.100 | 1.356 (0.697) |
| 1000 | 0.5 | 1.0 | [0.500,1.000] | [0.450,0.950] | 10 | [-0.550,0.450] | 0.100 | 1.118 (0.420) |
| 1000 | 0.5 | 0.1 | [0.500,1.000] | [0.450,0.950] | 10 | [-0.550,0.450] | 0.100 | 0.606 (0.740) |
| 1000 | 0.9 | 1.0 | [0.450,1.000] | [0.450,1.000] | 9 | [-0.550,0.550] | 0.000 | -0.741 (0.296) |
| 1000 | 0.9 | 0.1 | [0.400,1.000] | [0.400,1.000] | 8 | [-0.600,0.600] | 0.000 | -0.600 (0.377) |

The full `coverage_rejection_summary.csv` supplies truth rejection, off-truth rejection/power separately at −.50 and +.50, exact Clopper–Pearson intervals for both extreme completions, plug-in MCSEs, qualified-only W means/SD/median/quantiles and counts. `paired_comparisons.csv` gives all-planned missing-decision bounds, complete-pair differences/MCSEs, discordances and exact discordance bounds. Zero plug-in MCSE is not certainty. Cells sharing primitives are never pooled as independent replications.

## Numerical status and validation

A second long host interruption carried the calendar wall time beyond the immutable 12-hour deadline. At the next execution opportunity the operational driver marked both active fits TIME_LIMIT_UNRESOLVED and stopped launching fits, recording every remaining planned ID RESOURCE_NOT_EXECUTED. The pilot is therefore STOPPED AT THE RESOURCE GUARDRAIL and incomplete. The elapsed envelope was exceeded while the host was interrupted; it must not be reported as a completed within-budget experiment. No replication count, grid, seed or deadline was extended. The four result-repeatability fits were also withheld after the stop. Only reporting and integrity checks continued.

Execution was interrupted by a long host interruption and a stale monitoring host. Three original numerical PASS records exceeded the 180-second elapsed wall limit and are explicitly TIME_LIMIT_UNRESOLVED through immutable sidecar overrides; their decisions are excluded from qualification and remain in missing-decision bounds. Incomplete attempts were retained and audited, then resumed on the exact same frozen input IDs and RNG streams in a separate output directory. The operational v2 driver adds repeated deadline checks and a post-completion elapsed-time check. No estimator, solver tolerance, objective, penalty, numerical certificate, DGP parameter or stream changed. The 12-hour total envelope remains anchored conservatively at original run creation, including preparation and interruption. See INTERRUPTION_REPAIR_v2.json, status_overrides.json, interruption_audits and resume_execution.jsonl.

The original input verifier rejected the prescribed floating expression at an original Phi value rounded to one. Version 2 checks the unchanged literal transformation against its representable endpoints. Maximum upper-end rounding excess is 1.11e-16. The failed log and both verifier versions are preserved. This changes validation only; no DGP, numerical policy, penalty, stream or sample was changed. See VALIDATOR_FIX_v2.json and treatment_rounding.csv.

Evaluation statuses: {"PASS": 1064, "TIME_LIMIT_UNRESOLVED": 5, "RESOURCE_NOT_EXECUTED": 371}. Failure components: {"TIME_LIMIT_UNRESOLVED": 3}.

`input_validation.csv` independently replays all 40 primitive streams and 720 penalty streams, reconstructs both arms and structural truth, and checks primitive/penalty pairing and before/after RNG states. `numerical_validation.csv` independently reconstructs every qualified saved score/moment/W; each candidate retains direct rational certificates and independent audits, including failed-attempt audit records. `reproducibility.csv` records the four-case replay panel as NOT_EXECUTED_RESOURCE_STOP; no pilot bitwise result-repeatability claim is made. The cutoff bytes remain 5.99146454710798. `preservation.json` verifies all protected repository files and Git metadata.

## DGP mechanisms and theory

Sample covariance scales by .90, treatment variance by .81, and first-stage partial R²/F remain unchanged to maximum absolute error 6.25e-13. `instrument_relevance.csv` retains every sample, including kappa=.10; `numerical_diagnostics.csv` records instrument residual variances, score eigenvalues/conditioning, density extrema, KKT/objective bounds and W certificate widths. The historical density proxy remains dnorm(e,mean(e),var(e)), with variance as scale; its meaning is not silently replaced by the true conditional density.

The structural effect remains 1+Phi⁻¹(tau), and the structural residual is D(u−Phi⁻¹(tau)); primitive ranks and rank moments are preserved. The bounded arm changes support, dispersion, endogeneity covariance and instrument covariance while preserving linear first-stage R². It therefore does not isolate density regularity as the only changed mechanism. Bounded mixed residual densities are finite and positive; the original mixed density at zero diverges. The uniform density lower bound conditional on D,X,Z remains zero. Treatment itself is not uniform and its density can diverge at support edges. See the frozen readiness derivation for the proofs and analytical local-profile Jacobians.

These numerical certificates qualify the computed fixed objectives, not the statistical approximation. Any paired statistical difference is conditional on this numerical policy and subject to Monte Carlo sampling error; R=20 has ideal .95-coverage MCSE about .0487. Near-95% acceptance or an improvement in B cannot establish asymptotic validity. Sparse/restricted eigenvalues, nuisance rates and orthogonality of the retained proxy/residualization, generated-score theory, cross-fitting/empirical-process conditions and weak-instrument approximation remain unproved.

## Manuscript implications and next scientific task after the guardrail stop

Use these incomplete results as a partial prespecified DGP-sensitivity diagnostic with explicit missing-decision bounds, with full numerical resolution rates and pointwise Monte Carlo uncertainty. Do not report continuous interval geometry from a three-point profile or claim that bounded treatment validates the original inference theorem. The manuscript was not modified. The next task is an explicit assumption-by-assumption mapping to the intended inference theorem, focusing on conditioning sets, nuisance orthogonality/rates and weak-instrument validity; any larger simulation or revised policy needs a separately frozen protocol.

## Reproduction and preservation

Commands, adapters and RNG layout are in the pilot README and `CONFIG.json`; logs, environment/session information, source/input hashes and raw binary/RDS records are retained under the immutable run directory. No historical output was overwritten. No commit or push was made.
