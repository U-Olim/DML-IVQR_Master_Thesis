# Stage 2C: outcome penalty decomposition

Prespecified pilot: 40 fresh datasets, n=1000, p=100, tau=.90, kappa=1;
original DGP and DML candidate test at alpha0=1+qnorm(.90). No grid,
cross-fitting, DGP change, density repair, manuscript change, commit or push.

## Arms and fixed quantities

P11 retains original outcome intercept and slope penalties. P01 sets only
the intercept penalty to zero. P10 sets only slope penalties to zero. P00
sets all penalties to zero. Each arm jointly fits all outcome coefficients
with historical quantreg 5.34 `rq(...,method="lasso",lambda=vector)`.
The objective is sum(check loss)+sum(lambda*abs(beta))/2. The penalty vector
is generated once per dataset using the original pivotal algorithm; alternatives
only zero the prescribed entries. KNOWN uses structural coefficients as an
infeasible diagnostic anchor, not a feasible estimator.

P11 determines the original `dnorm(e,mean(e),var(e))` weights and original
DML instrument residuals, frozen in all five arms. The chi-square(2) .95
cutoff, raw score indicator <=0, and uncentered second moment are unchanged.
This is a frozen-component ablation, not five refitted complete estimators.

The primary estimand is mean(rank score P01)-mean(rank score P11), paired
over independent datasets. Secondary quantities include W, acceptance,
coefficient/prediction errors, support, rank disagreement, raw/residualized
instrument moments, score sum and second-moment entries, and factorial
interaction P11-P10-P01+P00. No arm is chosen by closeness to .95 acceptance.

## Randomness and stopping

L'Ecuyer-CMRG/Inversion. Pilot data/penalty master seeds 2026102901/2026102902;
preflight seeds 2026102903/2026102904. Stream index equals replication index;
full states and samples are retained. No earlier pilot samples are reused.
Two separate validation datasets are excluded from the 40 pilot replications.
Data and pivotal streams are distinct from Stage 2A/2B. Dataset hashes are
checked against both earlier pilots. Execution is sequential and scheduling
cannot change streams. Stop at exactly 40; stop earlier for any critical gate
failure, preserve partial outputs, and do not automatically retry or expand.

## Preservation and execution

Use only journal-validation. `config.json` records the verified external
Stage 2A/2B backup and manifest. The runner verifies its archive hash and all
801 source hashes before fitting. A pre/post SHA-256 snapshot covers every
file outside Stage 2C except Git metadata. Existing outputs cannot be overwritten.

From repository root, once, using a new configured run ID:

```powershell
python -B journal_validation/stage2c/run_stage2c.py
```

The historical R 3.4.3 executable/library are required. Python uses NumPy and
SciPy only for independent arithmetic/subgradient validation, never to replace
the outcome solver. No package is installed. All output stays in ignored
`output/<run-id>/`. Do not run a production runner or canonical report builder.

## Gates and evidence

Every dataset replays the original candidate under the matched full RNG state.
All arms must share data, density, projection and original penalty hashes.
Zero penalties are checked against the historical implementation and P00
against ordinary QR objective/fitted values (coefficients need not be unique).
`verify_one.py` independently reconstructs W and solves a linear program for
valid check-loss/L1 subgradients. It accommodates residual/coefficient numerical
ties at 1e-7; maximum stationarity residual divided by n must be <=1e-7.
P00 objective relative discrepancy must be <1e-7 and maximum fitted-value
discrepancy <1e-4. Canonical differences must be <=1e-11. All exact/numerical
ties, approximate dual gaps, conditions and failures remain recorded.

Each dataset directory retains full RDS fits, raw CSV observations, coefficients
and support, full design, density and instrument quantities, RNG states,
canonical checks, independent checks, library function body, warnings and session
information. Top-level files retain commands, exit codes, backup verification,
config, protected-file snapshots and completion/failure records. Summary and
report are prepared only after execution, including any failure.
