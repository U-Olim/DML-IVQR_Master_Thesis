# Stage 2B: outcome nuisance and weighted projection diagnostics

Work only on `journal-validation`. From the repository root:

```powershell
python -B journal_validation/stage2b/run_stage2b.py --run-id NEW_UNIQUE_RUN_ID
& 'C:\Program Files\R\R-3.4.3\bin\x64\Rscript.exe' --vanilla journal_validation/stage2b/verify_details.R journal_validation/stage2b/output/NEW_UNIQUE_RUN_ID
python -B journal_validation/stage2b/verify_outputs.py journal_validation/stage2b/output/NEW_UNIQUE_RUN_ID
python -B journal_validation/stage2b/finalize.py journal_validation/stage2b/output/NEW_UNIQUE_RUN_ID
```

Requires the existing historical executable
`C:\Program Files\R\R-3.4.3\bin\x64\Rscript.exe` and historical library.
Nothing is installed. All generated artifacts are inside ignored `output/`.
Run IDs cannot be reused. The runner sources canonical functions read-only;
it never executes production or manuscript/reporting entry points.

## Prespecified design

- Primary: 40 replications, n=1000, tau=.90, kappa=1, all three estimators.
- Limited contrasts: first 12 saved samples, tau=.50/kappa=1 and
  tau=.90/kappa=.10, all three estimators.
- Samples reuse the Stage 2A pilot primitive sets. Primary datasets and pivotal
  streams are exactly the Stage 2A baseline ones. Contrasts reuse the same
  primitives; no new data distribution is introduced. Data are copied to new
  Stage 2B RDS artifacts without modifying Stage 2A.
- V00: estimated outcome coefficients; original instrument projection.
- V10: known structural coefficients; original instrument projection.
- V01: estimated outcome coefficients; modified instrument projection.
- V11: known structural coefficients; modified instrument projection.
- True outcome coefficients: intercept 1, first seven slopes 5, others 0.
- All tests evaluate exact `1+qnorm(tau)` at `qchisq(.95,2)`.
- Per estimator/sample/design, density weights are calculated ONCE from V00 as
  `dnorm(e_est,mean(e_est),var(e_est))` and frozen in all four cells.
  The SD proxy is not evaluated here. Known-nuisance residuals do not trigger
  density re-estimation, instrument refitting, or penalty recalibration.

## Exact projection treatment and important library limitation

Oracle/Full compare the original no-constant weighted matrix projection against
the constant-inclusive projection on `[1,X]`, using identical positive weights.

For DML, historical `hdm` has an ordinary unpenalized intercept option but no
API for an arbitrary unpenalized `sqrt(f)` column. Calling it with that column
as an ordinary covariate would penalize it; switching `intercept=FALSE` would
also change the penalty calibration inputs. Neither is an exact intercept-only
intervention, so neither shortcut is used.

Instead, a private in-memory copy of `rlasso.default` captures the penalty
vector actually supplied to its LAST `LassoShooting.fit` call. The original
library namespace/files remain unchanged. The returned `fit$lambda` is not
assumed to be that vector: the adaptive routine updates its penalty after
solving, so it can store a next-iteration vector that was never used.

First replay the original final quadratic fit using that actual vector and
verify original coefficients. For the modified projection, partial out
`sqrt(f)` from both `sqrt(f)*Z` and `sqrt(f)*X`, then use the SAME historical
quadratic solver, SAME numeric slope-penalty vector, SAME solver defaults,
and no penalization of the transformed constant. Recover its constant coefficient
analytically. This changes the constant column of the final penalized objective.
It does NOT rerun the full adaptive penalty loop on the modified design.
This is a controlled final-objective ablation, not a proposed feasible DML method.

Reported orthogonality is `crossprod(cbind(1,X), f*raw_instrument_residual)/n`.
Penalized slopes are not expected to have zero weighted moments. Saved KKT
diagnostics use the objective `sum(error^2)+sum(lambda*abs(slopes))`, including
the historical numerical tolerances. Modified transformed constants are
unpenalized. Original raw-scale residuals retain the original intercept convention.

## Randomization

- Original data master 20261022, CMRG data streams 7:46 from Stage 2A.
- Original primary pivotal master 20261023, streams 241:280 from Stage 2A.
- Contrast pivotal master 20261024, CMRG streams 1:12 for median and 13:24 for weak.
- L'Ecuyer-CMRG / Inversion; two PSOCK workers; task-specific full states reset
  before outcome fitting and canonical reference replay.
- The estimated outcome fit is reused in V00/V01; known coefficients in
  V10/V11 need no outcome penalty draws. Instrument projections consume no RNG.

Full states and source paths are saved in `rng_streams.rds`,
`sample_stream_manifest.csv`, and task detail records. Each task checks its
data hash and that instrument fitting consumes no extra RNG.

## Validation and outputs

Validation runs the first two samples of every design/estimator (18 factorial
tasks) before the pilot. Every pilot task ALSO replays the canonical candidate.
Assertions cover V00 agreement, penalty replay, true residual algebra/rank,
fixed data/density/residual/projection identities, matrix dimensions and rank,
and the unpenalized weighted constant. Failures remain explicit rows, not drops.

`output/<run-id>/` contains:

- exact expanded child commands, exit codes, logs, environment and library bodies;
- configurations, copied samples, full random states and sample/stream manifests;
- `details/*.rds`: coefficients, frozen weights, outcome residuals, projections,
  actual solver penalty traces, orthogonality matrices, moments and W;
- `all_evaluations.csv`, `variant_summary.csv`, `compact_factorial.csv/.md`;
- `paired_factorial.csv`, `paired_effect_summary.csv` (including interactions);
- `outcome_diagnostics.csv`, `outcome_summary.csv`, raw and binned moments;
- `weighted_orthogonality.csv`, `projection_penalty_conditions.csv`;
- `isolation_checks.csv`, `failures.csv`, `warnings.csv`;
- `primary_factorial_W.png`;
- pre/post SHA-256 snapshots of every file outside Stage 2B, including Stage 2A;
- independent output-verification results.

`verify_details.R` independently reconstructs coefficients, weighted moment
matrices, and W from saved objects; `verify_outputs.py` independently verifies
pairing, Stage 2A replay, coverage, Wilson intervals, factorial arithmetic and
Monte Carlo standard errors. Neither verification command fits new models.
`finalize.py` repeats the CSV check and protected-file comparison, records source
hashes, and inventories all output artifacts for separate archival preservation.

Conditional diagnostics use fixed bins of X1 and observable instrument components
`Z1-X2-X3-X4`, `Z2-X7-X8-X9-X10`. These are descriptive conditional-moment
checks, not a proof of the full conditional restriction. D bins are also saved,
with the nonzero endogeneity-compatible target derived from
`u | T ~ N(.1*T,.97)`; zero is NOT asserted conditional on endogenous D.

Coverage for known-nuisance cells means acceptance of a diagnostic benchmark,
not coverage of a feasible published estimator. Monte Carlo uncertainty uses
independent samples within each design, not the four correlated variants as
additional replications. Read `STAGE2B_REPORT.md` for results and limitations.
