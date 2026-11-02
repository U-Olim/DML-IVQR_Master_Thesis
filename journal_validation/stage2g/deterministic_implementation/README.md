# Stage 2G-D — deterministic high-accuracy implementation feasibility

Version **2G-D.1**, numerical policy **B**: independent LP + exact outcome
ranks; historical native adaptive penalty calibration; high-accuracy final
fixed-penalty instrument optimization. No new statistical calibration rule.

Read [IMPLEMENTATION_CONTRACT_v1.md](IMPLEMENTATION_CONTRACT_v1.md) and
[DETERMINISTIC_IMPLEMENTATION_REPORT.md](DETERMINISTIC_IMPLEMENTATION_REPORT.md).
The final [comparison table](results/three_path_comparison.csv) retains all
24 original problems, disagreements and unresolved statuses.

From the repository root with the existing Python/NumPy/SciPy installation
and frozen R 3.4.3 / hdm 0.2.0:

```powershell
python -B journal_validation/stage2g/deterministic_implementation/run_v1.py
python -B journal_validation/stage2g/deterministic_implementation/finalize_v1.py
```

All writes stay in this directory. Replays overwrite current version-1 outputs
here; they never write previous validation artifacts. `run_v1.py` verifies the
previous manifests and records a protected snapshot before analysis. It sets
one-thread numerical environments and records Python, NumPy, SciPy, HiGHS,
BLAS/build information and R session details. It stops on script failures;
candidate-level numerical failures stay as explicit unresolved rows.

`outcome_v1.py` independently assembles the split-variable HiGHS-IPM LP and
repeats each solve. `outcome_exact_v1.py` certifies its proposed basis without
reading saved reference ranks/bases. Stage 2G certificates are consulted only
after construction for comparison. No raw floating residual determines a rank.

`calibration_v1.R` recomputes density and historical adaptive penalties with
the original saved RNG states; it checks penalty/fit bytes against Policy C.
`instrument_v1.py` solves the final fixed objectives afresh, repeats each new
solve, builds fresh exact certificates and inference bounds, and then compares
the optima with Policy C reference certificates. Refined fits never enter the
adaptive loop. The certificate uses a fresh inverse-Gram witness rather than
requiring an archived one.

`verify_v1.py` is a separate direct-rational audit of original outcome KKT,
uniqueness, signs, new fixed-penalty instrument KKT/objectives, Gram witnesses,
psi arithmetic, score moments, positive determinant and decision intervals.
It calls no optimization or active-set reconstruction. Shared low-level
integer arithmetic and rational interval utilities are imported read-only
from prior stages, with bytecode writes disabled.

`compare_v1.py` produces optimization/decision comparisons, observed component
benchmarks and clearly qualified runtime projections. Only the existing 24
n=1000 problems are evaluated; n=500 is an unmeasured planning proxy, not a
new subsample or generated dataset. No pivotal-penalty simulation is rerun.

`finalize_v1.py` writes the report, preservation check, categorized input hashes
and self-excluding SHA-256 manifest. Development errors and their superseded
failure logs are retained and explicitly distinguished from the final validated
run in `EXECUTION_NOTES.json`. An unresolved certificate is never acceptance.

No Stage 2H, new Monte Carlo, historical edit, manuscript edit, commit, push or
merge is performed by these scripts. Determinism does not establish valid
asymptotic inference.
