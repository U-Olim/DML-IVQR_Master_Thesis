# Stage 2H-0 readiness — diagnostics and protocol, no pilot execution

Read [READINESS_REPORT.md](READINESS_REPORT.md),
[BOUNDED_DGP_DERIVATION.md](BOUNDED_DGP_DERIVATION.md) and the unexecuted
[STAGE2H_PILOT_PROTOCOL.md](STAGE2H_PILOT_PROTOCOL.md).

The fixed diagnostic design is frozen in `DESIGN.csv` / `DESIGN_LOCK.json`:
12 cells, one truth candidate each; two new original-DGP primitive samples
(n=500/1000), deliberately shared across tau/kappa. Repeated and two-worker
evaluations reuse exactly those inputs. These are numerical diagnostics, not
independent coverage replications. No bounded-treatment dataset or outcome is
generated. Scalar quadrature checks of its mathematical formulas are separate.

Use the existing Python/NumPy/SciPy environment and frozen R 3.4.3 / hdm 0.2.0.
From the repository root:

```powershell
python -B journal_validation/stage2h/readiness/run_readiness.py prepare
python -B journal_validation/stage2h/readiness/build_auditor.py
python -B journal_validation/stage2h/readiness/run_readiness.py sequential repeat parallel
python -B journal_validation/stage2h/readiness/verify_contract.py
& 'C:/Program Files/R/R-3.4.3/bin/x64/Rscript.exe' --vanilla journal_validation/stage2h/readiness/verify_original_inputs.R
python -B journal_validation/stage2h/readiness/verify_derivation.py
python -B journal_validation/stage2h/readiness/summarize_readiness.py
python -B journal_validation/stage2h/readiness/finalize_readiness.py
```

All writes stay here. Replays overwrite only this readiness run's local outputs;
previous-stage files remain read-only. The preservation baseline expects
protected files to remain unchanged. The previous deterministic version's full
manifest is checked before fitting. Single-thread settings apply inside each
candidate; the limited parallel benchmark uses two candidate processes, not
two numerical threads. Python bytecode writes to imported historical code are
disabled. `EXECUTION_NOTES.json` distinguishes the initial same-input smoke
check from the 36 formally measured cohort executions.

`candidate_h0.py` calls unchanged dimension-generic version-1 solver and exact
certificate routines. It supplies each cell's actual n and literal tau,
generates no substitute basis from old reference results, and performs original
native calibration through `calibrate_original.R`. Final penalties are never
changed or recalibrated from refined fits. The old fixed-n audit is adapted
only in this directory: `AUDITOR_ADAPTATION.json` records exact changes and
source hashes, with the executed source retained. The separate contract check
verifies tau/rank scores, observation scores, moments, cutoff bytes and locked
penalties in all 36 executions. R independently replays original inputs/RNGs.

Every candidate retains exact outcome and instrument certificates, native
calibration traces, returned/exact-reference inference and independent audit.
Failed cases would remain unresolved, with error records and no replacement.
Numerical repeatability compares only mathematical/numerical artifacts;
timings, PIDs, memory counters and compressed-container timestamps are not
expected to repeat bitwise.

Memory uses Windows OS process working-set high-water marks plus a 50 ms
sampled sum of live-process RSS. The latter counts shared pages per process
and is not an exact continuous-time peak. No third-party memory package is
required. All benchmark measurement scopes and unmeasured bounded-arm /
off-truth costs are explicit in the report and CSV tables.

The protocol describes a possible future paired pilot; it is not runnable
Monte Carlo code. No manuscript edit, historical edit, bounded-DGP
implementation, Stage 2H experiment, commit or push occurs here.
