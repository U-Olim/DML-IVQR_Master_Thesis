# Stage 2C-S: saved-fit score/inference stability

No outcome fitting, Monte Carlo generation, pilot continuation, historical
edits, commits or pushes. All new artifacts remain in this stability directory.

`PROTOCOL.md` defines the common objective envelope, classifications, fixed
probe set and baseline gate before inference comparisons. The envelope is
derived exactly from all 92 prior objective certificates/response scales.
It is a sensitivity-study reference, not an authorized new validation gate.

Run from repository root with existing Python/NumPy and R 3.4.3:

```powershell
python -B journal_validation/stage2c/stability/analyze.py
# RUN is the unique saved_stability_UTCSTAMP directory printed above:
python -B journal_validation/stage2c/stability/verify.py RUN
python -B journal_validation/stage2c/stability/finalize.py RUN
```

The R helper `scores.R` only reads saved RDS objects, recomputes the original
candidate response/residuals and evaluates scores/moments/W. No estimation
function, estimator source or random-number generator is called. It checks
every baseline before a separate probe phase. Both phases retain complete
binary64 residual, score and coefficient arrays, plus frozen psi/density and
R session information. Existing folders/files cannot be overwritten.

Only Stage 2C-P's fixed +/-2**(-40,-30,-20,-10) intercept perturbations are
examined. Original coefficient vectors remain unchanged. Saved exactly feasible
dual witnesses independently certify the objective-error upper bound for
each alternative. The subset within the frozen common envelope is analyzed
separately; other probes are retained but never labeled near-optimal under
that envelope. None is claimed to be an exact optimizer or independent fit.

All 828 inference evaluations receive exact rational W calculations using the
saved binary64 score values and frozen instruments, compared with the unchanged
historical binary64 cutoff. The independent audit uses direct Fraction
arithmetic and also rechecks prior primal/dual/probe certificates. These exact
calculations certify inference conditional on the R-computed ranks; they do
not remove ambiguity of numerical near-zero residuals or replace the original
rank indicator with dual subgradients.

All source/output outside stability except Git metadata is protected by
pre/post SHA-256 snapshots. Stage 2C-P and original Stage 2C artifact manifests
are verified. Frozen protocol/generator hashes are recorded before execution.
Finalization creates final tables and source/artifact manifests.

Completed run: `saved_stability_20261029T084737Z/`.
Raw directories are ignored by Git and must be preserved separately.
