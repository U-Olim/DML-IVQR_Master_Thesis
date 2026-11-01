# Stage 2C - Outcome penalty decomposition: stopped validation run

Date: 29 October 2026 (Asia/Tashkent). Branch: `journal-validation`.
HEAD at execution: `d48972324e4c23e416a157958fcc4a0b26fa9b8a`.
Run: `output/controlled_20261029_01/`.

## 1. Executive status and mandatory stopping rule

**The prespecified 40-replication experiment is NOT COMPLETE.** Two separate
preflight datasets passed every gate. Pilot replications 1-20 then passed every
gate. Replication 21 completed its four outcome fits and known-nuisance score,
but its P10 independent KKT/subgradient gate failed. Execution stopped before
replication 22. No threshold was relaxed, solver substituted, fit retried,
sample replaced, or sample count enlarged. Replications 22-40 were not executed.

The failed stationarity discrepancy divided by n was
`1.0044854692833311e-7`, exceeding the predeclared `1e-7` threshold by
`4.4854692833311e-10` (about 0.449%). This is a validation failure, not a
recorded solver exception or demonstrated statistical failure. The existing
evidence cannot establish its cause. The explicit stopping rule takes priority
over completing 40 replications.

All 21 computed datasets and 105 score evaluations are retained. Tables below
describe ONLY the 20 fully validated replications. `all_computed_evaluations.csv`
also preserves all five arms of replication 21, explicitly marked FAILED_GATE.
`summary_scope.json` makes the distinction machine readable. This truncated
prefix is not a completed fixed-40 study; conventional MCSEs/intervals below
are descriptive and do not correct for the data-dependent stopping event.

## 2. Preservation and backup

The initial working tree was clean on `journal-validation`; no AGENTS.md was
found by the repository search. Stage 2A/2B saved PASS records and outputs were
present. An external prior backup could not be verified from accessible paths.
Before any experiment, a new archive was created outside the repository:

`C:/Users/User/DML-IVQR_validation_backups/stage2ab_before_stage2c_20261029T074433Z.zip`

Its sidecar is the same basename with suffix `.sha256.json`. All 801 files
(both complete stage directories, including scripts, reports and ignored
outputs) were hashed, archived, read back and checked; ZIP CRC also passed.
Archive size: 316,082,838 bytes. The launcher rechecked the archive SHA-256 and
all source hashes before fitting; `backup_verified.json` records the identity.

The pre/post protected-file check covered **4,132 files** outside Stage 2C,
excluding Git metadata: zero changed, missing, or newly added files. Stage 2A,
Stage 2B, canonical source/configuration, manuscript, thesis and historical
outputs were unchanged. No commit, push, pull, merge, or reset occurred.
All newly created repository files are under Stage 2C. The external backup is
the specifically requested exception.

## 3. Prespecified design and exact interventions

Original DGP, n=1000, p=100, tau=.90, kappa=1. Test only exact
alpha0=1+qnorm(.90), with original chi-square(2) .95 cutoff 5.99146454710798.
Forty genuinely fresh datasets were planned, using data master 2026102901
and pivotal master 2026102902. Preflight uses distinct masters
2026102903/2026102904 and is not counted as pilot evidence. RNG is
L'Ecuyer-CMRG/Inversion; index i is the ith `nextRNGStream` state, with full
states saved before data generation and penalty draws. Earlier pilot samples
are neither reused nor pooled. Dataset hashes are checked against earlier
Stage 2A pilot and Stage 2B outputs and against every new sample.

The outcome objective is sum(check loss)+sum(lambda*abs(beta))/2.

| Arm | Intercept penalty | Slope penalties |
|---|---|---|
| P11 | Original | Original |
| P01 | Zero | Same original numeric vector |
| P10 | Same original numeric value | Zero |
| P00 | Zero | Zero |
| KNOWN | No fit: structural intercept 1, slopes 5 for X1-X7, others 0 | Infeasible anchor |

Each fitted arm jointly estimates intercept and all slopes with historical
`quantreg::rq(...,method="lasso",lambda=vector)`. The original pivotal penalty
is computed once per dataset. P11 determines variance-proxy density weights
and original DML instrument residuals, frozen in every arm. Only outcome
coefficients change. No density refit, instrument refit, adaptive projection
penalty change, cross-fitting, test-cutoff change, or DGP modification is made
between arms. These are frozen-component diagnostics, not complete estimators.

P01-P11 and P00-P10 change the intercept penalty setting; P10-P11 and P00-P01
change slope penalty settings. Refitting is joint: these interventions do not
hold fitted slopes or intercept fixed. P00-P11 changes two settings. The
interaction is P11-P10-P01+P00; its sign convention is explicit in CSVs.

## 4. Validation and solver semantics

Historical environment: R 3.4.3, quantreg 5.34, hdm 0.2.0, hqreg 1.4,
mvtnorm 1.0-6 and doSNOW 1.0.16. Session records accompany every dataset.
The captured `rq.fit.lasso` body constructs diagonal penalty pseudo-rows,
removes rows whose supplied penalty is zero, and uses the historical `rqfnb`
Fortran routine. All-zero vector penalties therefore remove every penalty
pseudo-row. No alternative solver is used for an experimental arm. Ordinary
QR is fitted only as an independent P00 reference.

Two preflight datasets and pilot 1-20 passed:

- Canonical P11 W, beta and instrument residual replay under matched data/RNG:
  exactly zero discrepancies in saved R checks.
- Exact intended numerical penalty entries; frozen data/density/projection
  hashes; no additional random draws consumed by fitting.
- P00 versus ordinary QR objective and fitted-value comparisons. Across the
  20 validated pilot datasets, maximum fitted-value discrepancy is
  1.67587361943333e-6, below predeclared 1e-4. Coefficient equality was not
  required; fitted values and objective values were explicitly compared.
- Known residual identity D*(u-qnorm(tau)) and exact structural-rank agreement.
- Independent two-dimensional W reconstruction from per-observation score
  vectors and their crossproduct; direct inversions remained finite.
- Linear-program feasibility of check-loss/L1 subgradients, allowing interval
  scores for |residual|<=1e-7 and interval L1 derivatives for numerical zero
  coefficients. The maximum normalized stationarity discrepancy in pilot
  1-20 was 2.961512343544509e-8. Exact ties and numerical ties are separately
  recorded; a raw <=0 indicator need not equal an optimizing subgradient.

### Failed gate at replication 21

P11 and P01 independent checks completed before P10 exceeded the threshold.
No full independent PASS was issued for this dataset; later-arm checks in
that verifier were not reached. R-side computations and canonical checks did
complete for all arms. P11 canonical discrepancies remain zero. P00 versus
ordinary QR objective discrepancy is 5.11022335558664e-11 and fitted discrepancy
3.49244189123965e-10. There were no estimator warnings.

For P10, 98 residuals are within the declared 1e-7 tie band, while 100 are
within 1e-6. The two additional residual magnitudes are
1.55288088166117e-7 and 9.51238384061526e-7. The historical solver's default
eps is 1e-6. This motivates reviewing numerical-tie treatment versus the
solver's accuracy, but does not prove that the gate or solution is incorrect.
No wider tie band was used to authorize continuation; no post-hoc passing
criterion was substituted.

There are **zero recorded outcome/projection solver exceptions**, zero estimator
warnings, and **one critical independent validation failure**. R startup's
`Setting LC_CTYPE=C.UTF-8 failed` warning is separate and sessions use locale C.

## 5. Partial numerical results: validated prefix only (R=20)

| Arm | Mean W | Acceptance | Mean rank score | Intercept error | Slope L2 error | Prediction RMS | Selected slopes | Rank mismatches / 1000 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| P11 | 7.1840 | 10/20 | .02485 | -.08272 | .07904 | .02321 | 30.3 | 44.25 |
| P01 | 5.9424 | 11/20 | -.00045 | 3.39365 | 2.16365 | .83636 | 7.0 | 133.35 |
| P10 | 7.2995 | 10/20 | -.00275 | -1.00000 | .66179 | .19654 | 100.0 | 85.85 |
| P00 | 6.2156 | 11/20 | -.00415 | .03330 | .59429 | .17826 | 100.0 | 83.25 |
| KNOWN | 2.1353 | 19/20 | .00310 | 0 | 0 | 0 | 7 | 0 |

Rejection frequencies are .50, .45, .50, .45, and .05. Descriptive marginal
Wilson intervals: 10/20 [.299,.701], 11/20 [.342,.742], 19/20 [.764,.991].
These are not post-stopping-adjusted inferential intervals, and 19/20 does
not validate the infeasible benchmark's reference distribution.

The primary P01-P11 mean-rank-score difference is **-.02530**, with descriptive
paired MCSE **.00050835**. Its W difference is **-1.24162 (1.29182)** and
acceptance difference **+.050 (.11413)**, with three gains and two losses.

| Comparison | Mean delta rank score (MCSE) | Mean delta W (MCSE) | Delta acceptance (MCSE) |
|---|---:|---:|---:|
| P01-P11 | -.02530 (.000508) | -1.2416 (1.2918) | +.050 (.1141) |
| P10-P11 | -.02760 (.000832) | +.1155 (.9207) | .000 (.1026) |
| P00-P11 | -.02900 (.000962) | -.9685 (.7889) | +.050 (.1141) |
| P00-P10 | -.00140 (.001230) | -1.0840 (.5580) | +.050 (.1141) |
| P00-P01 | -.00370 (.000788) | +.2732 (1.0035) | .000 (.1257) |
| P01-P10 | +.00230 (.000821) | -1.3571 (1.1472) | +.050 (.0881) |
| KNOWN-P11 | -.02175 (.002092) | -5.0487 (1.2185) | +.450 (.1141) |
| Interaction | +.02390 (.001218) | +.1577 (1.3771) | .000 (.1777) |

MCSE is sample SD of the paired differences divided by sqrt(20); marginal
acceptance MCSE is sqrt(p*(1-p)/20). All six arm comparisons, four KNOWN
comparisons, and interactions are retained for every reported metric in
`paired_summary.csv` and `paired_differences.csv`. No correlated arm is
counted as another independent replication.

### Nuisance and support interpretation

P01 selects exactly X1-X7 in this prefix, but its average first-seven slope
coefficient is 4.19022 rather than 5, and mean intercept is 4.39365 rather
than 1. Removing intercept penalization centers the average rank score while
the jointly fitted coefficients redistribute the fit between an unpenalized
constant and penalized uncentered controls. This is observed numerical
behavior, not a universal explanation. P11's corresponding mean active slope
is 4.98908; it selects 23.3 additional irrelevant slopes on average.

P10's intercept is numerically zero while all 100 slopes are selected; P00
also selects all 100. Thus keeping the intercept penalty while freeing slopes
can substantially change the jointly fitted intercept. Mean score centering
alone is not a sufficient diagnostic of nuisance accuracy or valid inference.
The original <=0 rule is retained; numerical near-ties make its raw score
different from an exact optimality subgradient.

Identities of every selected control are in `selected_supports.csv`; per-control
selection counts are in `selection_frequency.csv`. Selection uses |beta|>1e-7.

### Score numerator versus second moment

The per-observation normalized second moment is S=(1/n)*sum(psi_i psi_i' s_i^2).

| Arm | Mean score sum vector | Mean S11 | Mean S12 | Mean S22 |
|---|---|---:|---:|---:|
| P11 | (-19.1754,-24.9965) | .22795 | .00887 | .22652 |
| P01 | (-15.7126,-23.1732) | .17479 | -.00190 | .17487 |
| P10 | (-21.9570,-22.4735) | .18036 | .00530 | .17511 |
| P00 | (-17.9273,-22.0984) | .17678 | .00756 | .17508 |
| KNOWN | (-2.2912,-5.5421) | .19056 | .00154 | .19047 |

These changes show that frozen psi does not freeze the studentizing matrix:
the changed indicator enters s_i^2. Neither W nor its expectation can be
reconstructed by plugging these across-replication averages into the nonlinear
formula. Raw instrument moments and all paired matrix-entry changes are saved.

### Computed replication 21: excluded from validated-prefix tables

All arms accepted: W(P11)=.160925, W(P01)=3.670772, W(P10)=.531325,
W(P00)=1.799516, W(KNOWN)=2.825965. These are unvalidated raw outputs, not
additional accepted scientific replications. Their presence is explicitly
retained rather than silently dropping a failed task.

## 6. Classification and scientific limits

| Statement | Classification |
|---|---|
| Penalty settings change coefficients, support, rank indicators, scores and W on saved validated datasets | Confirmed numerical effect |
| P01 centers the rank score but does not approach the known coefficients in the validated prefix | Confirmed numerical effect |
| Better average rank-score centering guarantees nuisance accuracy or smaller W | Contradicted by numerical examples; confirmed numerical counterexample |
| Acceptance improvement of P01/P00 in the partial prefix | No detectable effect in this pilot prefix; large descriptive paired uncertainty |
| Intercept penalty alone explains historical .498 coverage | Inconclusive |
| The remaining subgradient discrepancy is a solver defect rather than tie/tolerance sensitivity | Inconclusive |
| Any arm has valid theoretical 95% inference | Inconclusive |
| Complete 40-replication Stage 2C study | Not executed: stopped at mandatory gate |
| Replications 22-40, cross-fitting, DGP changes, new cutoff, manuscript revision | Not executed |

The original theoretical density-regularity obstacle remains unchanged.
KNOWN still uses frozen P11-estimated weights and same-sample projections;
it is infeasible and its 19/20 acceptance is not population calibration
evidence. No arm is recommended by proximity to nominal coverage. The partial
prefix cannot substitute for the planned study or establish asymptotic behavior.

## 7. Required next review and regularity-controlled DGP proposal

First review the failed P10 subgradient gate from saved replication 21:
historical solver accuracy, residual tie classification, objective/dual gaps,
and scale-aware tolerances. Any revised numerical validation protocol must
be justified and frozen before an explicitly authorized continuation/new run.
Do not simply widen the threshold to finish this experiment. No automatic
continuation is provided here; the runner refuses to overwrite the run.

Subsequent DGP candidate: D_delta=delta+(1-2*delta)*Phi(T), delta=.05,
with the existing primitive dependence, instruments and structural outcome
equation, giving alpha0=1+qnorm(tau) and positive D bounded away from zero.
Before simulation, derive the conditional residual density and required
weighted moments; do not assume bounded D alone establishes every theorem
condition. Explicitly measure changes in marginal treatment distribution,
instrument relevance and endogeneity. This is an alternative DGP, not the
unchanged original experiment. Specify estimator/density arms prospectively
and use new matched streams; do not choose a DGP or cutoff by favorable size.
No such experiment was run.

## 8. Execution record and artifact index

Executed from repository root:

```powershell
python -B journal_validation/stage2c/run_stage2c.py
python -B journal_validation/stage2c/summarize.py journal_validation/stage2c/output/controlled_20261029_01
python -B journal_validation/stage2c/finalize.py journal_validation/stage2c/output/controlled_20261029_01
```

The launcher exits 1 because the independent validation gate failed, after
running its finally-block preservation check. All 23 R child commands (two
preflight, 21 pilot) exited 0. Exact expanded arguments/timestamps/statuses
are in `commands.json`; full stdout/stderr logs remain. Initial read-only
environment inspection had a PowerShell quoting error, corrected by supplying
R code on stdin; no scientific fit or package modification occurred in that
inspection. Parent-directory listing was inaccessible; the explicitly requested
external backup was created with approved filesystem access.

Partial-summary handling and final archival tooling were added AFTER the
failure, without changing `config.json`, `run_one.R`, `verify_one.py` or any
experimental fit. They label the incomplete scope and never convert failure
to PASS. Final source/artifact hashes record this final documentation state.

- Design: `config.json`, `README.md`.
- Execution: `run_stage2c.py`, `run_one.R`.
- Independent numerical gates: `verify_one.py`.
- Deterministic partial summaries: `summarize.py`.
- Artifact verification: `finalize.py`.
- Raw computation including failed gate: `all_computed_evaluations.csv`.
- Validated prefix: `all_evaluations.csv`, `variant_summary.csv`,
  `paired_summary.csv`, `paired_differences.csv`, `summary_scope.json`.
- Coefficients/support: per-dataset `coefficients.csv`, `selected_supports.csv`,
  `selection_frequency.csv`.
- Observations/design: per-dataset `observations.csv`, `design.csv`,
  `data_diagnostics.csv`, `sample.rds`, `details.rds`.
- Numerical gates: per-dataset `r_validation.csv`, `verification.json` where
  completed; `canonical_and_qr_checks.csv`, `independent_checks.csv`.
- Failure: `FAILURE.txt`, `failure_review.json`, complete `pilot_021/` directory.
- Preservation/RNG: `backup_verified.json`, `protected_before.json`,
  `protected_after.json`, `preservation.json`, per-dataset full RNG states.
- Final inventory: `source_sha256.json`, `artifact_manifest.json`,
  `python_environment.json`, `output_verification.json` (STOPPED status).

No plot is needed to clarify this incomplete run. All output is deliberately
ignored by Git and needs separate archival preservation when sharing the work.
Stage 2C stops here for scientific and numerical review.
