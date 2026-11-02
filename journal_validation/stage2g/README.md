# Stage 2G: numerical score-evaluation policy

Scope: the 24 preserved Stage 2E candidate problems, with the two Stage 2F
disagreements assessed first. No data generation, historical estimator edit,
Stage 2C continuation, manuscript edit, commit or push.

Read `NUMERICAL_POLICIES.md` for the policy contract and `STAGE2G_REPORT.md`
for results and Stage 2H prerequisites.

From the repository root, using the existing Python/NumPy environment:

```powershell
python -B journal_validation/stage2g/validate.py
python -B journal_validation/stage2g/verify.py
python -B journal_validation/stage2g/report.py
python -B journal_validation/stage2g/finalize.py
```

The validator refuses to overwrite `results/`. Archive that directory outside
this source directory before a fresh run. Input directories are fixed in the
script. `-B` prevents bytecode writes to imported historical directories.
The recorded first attempt stopped during manifest selection before any case
analysis; `--resume-integrity` was used only to retain that initial snapshot.
See `EXECUTION_NOTES.json` for the correction and environment provenance.
Read-only reuse: Stage 2F exact reconstruction and fast integer statistic
evaluation; independent audit uses Fraction evaluation and elimination from
Stage 2F's separate verifier, without invoking its historical-writing main.
No numerical optimizer is rerun: the independently fitted Stage 2E solutions
propose bases for new exact certificates.

Results include rectangular policy tables, per-case primal/dual/uniqueness
certificates, exact inference records, same-vector residual arithmetic checks,
observation sign tables and sensitivity witnesses. Protected-file snapshots
cover the entire repository outside Stage 2G and Git metadata. Final manifests
cover Stage 2G source and result files except the manifest itself.
