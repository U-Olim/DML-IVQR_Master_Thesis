# Stage 2G-F: complete downstream-path validation

Read `FULL_PATH_REPORT.md` for findings and `POLICY_C_SPECIFICATION.md` for the
versioned computational contract and certification limits.

All 24 saved candidates are evaluated with exact outcome ranks and freshly
computed historical density/projection paths. The 12 previously identified
instability cases also receive two rational perturbation directions at two
fixed objective budgets: 72 newly evaluated paths in total. Existing datasets,
outcome penalties, candidate values, streams and Stage 2G certificates remain
read-only. No data or outcome penalty draws occur here.

From the repository root, using existing Python/NumPy/SciPy and historical R:

```powershell
python -B journal_validation/stage2g/full_path_validation/prepare.py
python -B journal_validation/stage2g/full_path_validation/run_r.py native
python -B journal_validation/stage2g/full_path_validation/audit.py
python -B journal_validation/stage2g/full_path_validation/run_r.py verify
python -B journal_validation/stage2g/full_path_validation/verify_adaptive.py
python -B journal_validation/stage2g/full_path_validation/verify_certificates.py
python -B journal_validation/stage2g/full_path_validation/compare.py
python -B journal_validation/stage2g/full_path_validation/report.py
python -B journal_validation/stage2g/full_path_validation/finalize.py
```

`prepare.py` refuses to overwrite `results/`; archive the complete directory
before a fresh run. Native exports and verification trace exports also refuse
to overwrite their binary files. All imports of historical arithmetic helpers
are read-only, and `-B` prevents bytecode writes. The scripts require the same
archived Stage 2E inputs and Stage 2G manifest. No package installation is used.
The separate `inspect_environment.R` can export the historical function sources
into this directory for inspection; it is not required to reproduce numbers.

The primary audit reconstructs fixed-penalty lasso optima and builds exact
conditional decision bounds. The independent verifier calls no reconstruction
or audit function: it checks rational objectives/KKT conditions, inverse-Gram
witnesses, outcome perturbations and moments directly. The adaptive verifier
independently implements initialization and penalty update calculations.

Main artifacts in `results/`:

- `complete_24_problem_comparison.csv`: A/B/C, all pairwise differences and status.
- `near_optimal_full_path_comparison.csv`: all 24 paired comparisons (12 cases,
  two budgets); full downstream refits, actual objective gaps and differences.
- `downstream_audit.csv`, `native_summary.csv`, `adaptive_verification.csv`,
  `independent_verification.json`, baseline/native reconstruction checks.
- Each case/variant: exact outcome records, all native numeric arrays and fits,
  adaptive traces and RNG states, density checks, two instrument certificates,
  inverse-Gram witnesses, exact W, interval decision bounds and independent audit.
- Initial state, source-manifest checks, protected-file snapshots and final
  preservation report. The self-excluding SHA-256 manifest is in this directory.

The historical Stage 2G manifest is preserved and continues to validate all
files it lists; it intentionally does not list this newly added subdirectory.
See `EXECUTION_NOTES.json` for the first native launch's shell-status anomaly
and direct R verifier confirmation. Raw outputs here are not ignored by Git;
retain the complete artifact set when archiving. No commit is made.
