# Stage 2H paired diagnostic pilot

The authoritative design is the three Stage 2H readiness documents. This pilot
uses 1,440 individual evaluations (720 A/B pairs), 480 at truth, and no extra
statistical replications. All new files remain below this directory. The original
DGP, numerical code, historical outputs and manuscript are read-only.

Use the installed Python 3.11 executable explicitly. The PATH `python` command
was unreliable in this shell. From the repository root in PowerShell:

```powershell
$pilotPython = 'C:/Users/User/AppData/Local/Programs/Python/Python311/python.exe'
& $pilotPython -B journal_validation/stage2h/pilot/setup_pilot.py
& $pilotPython -B journal_validation/stage2h/pilot/run_pilot.py init
& $pilotPython -B journal_validation/stage2h/pilot/run_pilot.py prepare
$env:STAGE2H_RUN = (Get-Content journal_validation/stage2h/pilot/LATEST_RUN.txt -Raw).Trim()
& 'C:/Program Files/R/R-3.4.3/bin/x64/Rscript.exe' --vanilla journal_validation/stage2h/pilot/verify_inputs_v2.R
& 'C:/Program Files/R/R-3.4.3/bin/x64/Rscript.exe' --vanilla journal_validation/stage2h/pilot/verify_binary_inputs.R
& $pilotPython -B journal_validation/stage2h/pilot/export_analytical_diagnostics.py
& $pilotPython -B journal_validation/stage2h/pilot/seal_inputs.py
& $pilotPython -B journal_validation/stage2h/pilot/run_pilot.py execute
& $pilotPython -B journal_validation/stage2h/pilot/summarize_pilot.py
& $pilotPython -B journal_validation/stage2h/pilot/finalize_pilot_v2.py
```

`init` creates a unique run and freezes design, source, preflight and protection
snapshots. `LATEST_RUN.txt` identifies it. Other commands accept an explicit run
directory as their final argument. Do not regenerate adapters or initialize over
an existing experiment. Preparation and verification logs use exclusive creation.
Execution resumes the same frozen IDs and inputs, skipping existing result
records, retaining unresolved results. It never replaces a failed sample.

R 3.4.3, hdm 0.2.0 and the original 1,000-draw pivotal calibration are required.
The installed NumPy/SciPy versions and frozen source manifests are checked before
fitting. The R session information and native calibration traces are retained.
The historical locale warning is preserved in logs.

The original `verify_inputs.R` and failed `verify.log` are retained. Before any
candidate fitting, version 2 corrected a strict floating endpoint comparison:
R's literal `.05+.90*1` equals `0.9500000000000001`. The generator is unchanged;
the verifier checks the exact prescribed expression and its representable
endpoints. `VALIDATOR_FIX_v2.json` and `treatment_rounding.csv` record the one-ULP
overshoot and saturated original Phi values. No outcome/instrument/inference
tolerance changed. `PREFIT_FINAL_SOURCE_LOCK.json` seals all final pre-fit source,
including this validation correction and the supplemental binary audit.

Seed 2026110281 is partitioned into 40 successive L'Ecuyer-CMRG stream families
in n, replication order. Primitive draws start at the family origin, preserving
the original generator's draw order and correlation. Eighteen successive
substreams per family correspond to tau, kappa, candidate order; each A/B pair
shares one original penalty draw and byte-identical lambda. Full before/after
states are recorded in `inputs/rng_streams.csv` and task/primitive RDS files.
Scheduling never determines streams. T is constructed once per kappa per sample;
the B arm replaces D and recomputes Y, retaining all primitives and Z/X.

The adapters change storage roots and failure reporting only. Exact score,
LP/KKT/uniqueness, final fixed-objective instrument certification and independent
audit arithmetic remain those of 2G-D.1 and the H0 dimension adapter. Numerical
tolerances, historical density proxy, instrument projection, adaptive calibration,
rank <=0 rule, moments and cutoff are unchanged. `ADAPTER_CHANGES.json` records
source hashes. Outcome penalties match between arms; instrument penalties can
differ. Qualification concerns the final fixed objectives, not exhaustive
propagation through every historical adaptive branch.

Four reproducibility replays are selected before fitting: replication 1, tau=.5,
kappa=1, truth, both n and arms. They reuse inputs, compare numerical fingerprints,
and add no statistical observations or design cells. All 720 input pairs undergo
independent R primitive/DGP/penalty replay before any fitting.

Results are saved per candidate with an external 180-second process-tree limit,
at most two workers and one numerical thread per worker. Unresolved and
not-executed decisions remain in denominator 20. Raw records include every planned
ID. Summaries distinguish attempts, qualification, missing-decision bounds,
qualified-only W and complete pairs. Exact binomial intervals are pointwise;
paired MCSEs use sample variance of within-pair differences. No pooling of
dependent quantile/kappa cells is performed. Missing W is never zero-imputed.

`PREFLIGHT.json` identifies the verified external Stage 2A/2B backup and its scope.
`protected_before.json`, `git_before.json`, source/input locks and final
`preservation.json` protect historical content. `SHA256_MANIFEST.json` covers new
artifacts. Sampled RSS and per-process OS high-water values have distinct scopes.

Read `STAGE2H_REPORT.md` for execution status, results and limitations. The bounded
DGP changes relevance scale and treatment dispersion as well as mixed density.
It leaves the fully conditioned uniform density lower bound at zero and does
not establish high-dimensional or asymptotic validity. No manuscript edits,
commit, push, broader grid or additional simulation are authorized by this run.
