# Stage 2G-C: end-to-end numerical certification attempt

This directory implements the attached request after Stage 2G-F. All writes
are confined here. No data generation, Monte Carlo, Stage 2C/2H work,
historical estimator edits, manuscript edits, commits or pushes are performed.

Read [END_TO_END_REPORT.md](END_TO_END_REPORT.md) and
[results/candidate_bounds.csv](results/candidate_bounds.csv) for the decision.
An `UNAVAILABLE` end-to-end bound is intentional and must never be interpreted
as acceptance or replaced by the old fixed-input interval.

From the repository root, use the installed Python with NumPy/SciPy and the
frozen R 3.4.3 / hdm 0.2.0 environment:

```powershell
python -B journal_validation/stage2g/end_to_end_certification/run.py
python -B journal_validation/stage2g/end_to_end_certification/finalize.py
```

`run.py` checks the full Stage 2G-F manifest before reconstructing all 72
native paths, then stops on any reconstruction failure. It exports all 138
primary shooting calls, including their Gram matrices, crossproducts, initial
coefficient vectors, every sweep and final thresholded coefficients.

`density_bounds.py` uses rational mean/variance, Machin pi bounds and outward
90-digit Decimal intervals. It encloses the real historical variance-as-scale
density formula and sqrt weights. Separate a posteriori hulls enclose both
the exact-real formula and the actual saved density; conservative binary64
rounding bounds extend these through weighting/centering. These are fixed-input
error enclosures, not a universal libm accuracy specification.

`branch_bounds.py` attempts outward interval propagation through each shooting
call, with exported Gram, response crossproduct, penalty and initializer FIXED.
It stops on ambiguous branches. Even a successful call is Category A, never
Category B (fully adaptive). `adaptive_analysis.py` reconstructs initializer
selection and every outer update, retaining numerical margins as diagnostics.

`independent_verify.py` uses rational arithmetic tests, a separate 130-digit
density evaluation and exact score reconstruction. `reaudit_primary.py`
re-executes the prior independent exact verifier for all 24 primary paths,
redirecting every output into this directory. Its exact executed source and
source hashes are retained. No original verifier output is overwritten.

`finalize.py` writes the report, category-indexed input hashes, final protected
snapshot, preservation result and a self-excluding SHA-256 manifest. The
protected snapshot excludes only this directory and Git metadata. Full-path
certification has **not** been achieved: preserve all unresolved statuses.
