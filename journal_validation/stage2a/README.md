# Stage 2A controlled diagnostics

Run from the repository root, on branch `journal-validation`:

```powershell
python -B journal_validation/stage2a/run_stage2a.py --run-id YOUR_NEW_RUN_ID
python -B journal_validation/stage2a/verify_outputs.py journal_validation/stage2a/output/YOUR_NEW_RUN_ID
```

The runner requires the existing R 3.4.3 executable at
`C:\Program Files\R\R-3.4.3\bin\x64\Rscript.exe` and the existing historical library.
It installs nothing. It refuses to reuse an output directory. Do not run canonical
production or reporting entry points to reproduce these diagnostics.

## Design fixed before execution

- A: three independently generated primitive samples for each n in {500,1000};
  each is reused at kappa in {1,.1}, tau in {.5,.9}, and ten independent penalty
  streams. Total: 240 baseline true-parameter evaluations on 24 fixed
  dataset/quantile settings. Observations remain fixed within every setting.
- B: one SD-proxy partner for each A evaluation (240 pairs). Only the scale
  argument in `dnorm` changes. Both fits begin with exactly the same task RNG state.
- C: 40 new paired samples at n=1000, tau=.9, kappa=1; Oracle, Full, and DML,
  each with baseline variance-proxy and alternative SD-proxy (120 pairs).
- No alpha grids, no full 500-replication runs, no post-Lasso, new tolerances,
  altered cutoffs, or cross-fitting.
- Cutoff: `qchisq(.95,2)`. All evaluations are at exact `1+qnorm(tau)`.

## Randomization and validation

Data master seed: 20261022. Penalty master seed: 20261023.
RNG: L'Ecuyer-CMRG with Inversion normal generation. Complete seven-integer
task states are allocated with `parallel::nextRNGStream`, saved in
`rng_streams.rds`, sample manifests, and paired evaluation CSVs.
Data stream indices 1:6 generate fixed samples; 7:46 generate pilot samples.
Penalty indices 1:240 serve A/B; 241:280 serve pilot replications.
There are two persistent PSOCK workers. Every fit explicitly overwrites its RNG
state, so worker startup seeds and task scheduling do not affect its draws.
Worker PIDs and session information are saved. A baseline and its SD partner
execute together on one worker, resetting the same state before each fit.

Validation precedes A/B and the pilot. It checks original baseline primitive
draw order and kappa=1 data, synthetic density values, reversal of exactly one
AST edit, and exact agreement of instrumented and canonical baseline candidates
for 24 cases. Every pair checks unchanged data, matching outcome coefficients
and residuals, and matching pivotal penalty vectors/draw hashes for DML.
There is no change in stream-control policy between the two density variants.

`hdm` 0.2.0 has an internal `post=FALSE` default override to penalty c=.5;
this is retained. All installed solver defaults remain unchanged.

## Files and outputs

- `diagnostic_functions.R`: detailed local candidates and paired task execution.
- `run_diagnostics.R`: validation, A/B, and pilot phases with gates.
- `summarize.R`: finite-aware summaries, Wilson coverage intervals, paired
  differences and Monte Carlo standard errors, and the paired W plot.
- `run_stage2a.py`: logs child command arguments, exit codes, and preservation.
- `verify_outputs.py`: independently checks raw CSV identities, streams,
  decisions, coverage/uncertainty arithmetic, stability, and preservation.
- `STAGE2A_REPORT.md`: reviewed results and limitations.

All runtime artifacts go to ignored `output/<run-id>/`:

- `commands.json`, master/worker logs, version inventory, configuration;
- immutable sample RDS files and their SHA-256 identities;
- `details/*.rds`: complete outcome coefficients, all pivotal penalties,
  instrument coefficients/penalties/loadings/options, residuals, density weights,
  residualized instruments, W, condition estimates, warnings/errors, and RNG states;
- `ab_pairs.csv`, `pilot_pairs.csv`: per-evaluation outcomes and pair assertions;
- `A_summary.csv`, `A_per_dataset.csv`, `A_evaluations.csv`, `B_summary.csv`,
  `C_coverage_summary.csv`, `C_paired_summary.csv`, `numerical_stability.csv`;
- `paired_W_differences.png`;
- `protected_before.json`, `protected_after.json`, `preservation.json`.

The preservation scan hashes every existing file outside `.git/` and this Stage
2A directory, including ignored canonical outputs and local historical libraries.
The runner checks content equality, missing files, and newly added external files
even if a computational command fails. No historical output is overwritten.

For A/B, repeated streams on one dataset are algorithmic replicates, not
independent Monte Carlo data samples. B's pooled differences are descriptive.
For C, coverage intervals use successful evaluations as denominator; failures
are separately reported. Paired coverage differences use complete pairs and
`sd(paired acceptance difference)/sqrt(number of pairs)` as MCSE.
No comparison with archived coverage is a paired comparison, and numerical
improvement is not a proof of theoretical validity.
