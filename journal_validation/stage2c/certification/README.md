# Stage 2C-V: saved-input numerical certification

No Monte Carlo samples, outcome fits, changed historical gates, or pilot
continuation. All inputs come from Stage 2C saved CSV/RDS files. Only files
inside this certification directory may be created. No commit/push.

From repository root:

```powershell
python -B journal_validation/stage2c/certification/certify.py
# Replace RUN with the new uniquely named directory printed by the command:
python -B journal_validation/stage2c/certification/audit_certificates.py RUN
python -B journal_validation/stage2c/certification/rounding_review.py RUN
python -B journal_validation/stage2c/certification/finalize.py RUN
```

Each certification invocation creates a unique `saved_inputs_UTCSTAMP` directory
and refuses to overwrite outputs. The historical R 3.4.3 executable is used only
to read RDS files and export their doubles to little-endian binary64 files.
It never sources an estimator, fits a model, or draws random numbers. Python
requires existing NumPy/SciPy; no installation is performed.

Two input scopes are separate: historical CSV inputs reconstruct the original
validator bit for bit; binary RDS exports assess full-precision inputs with the
same tie/penalty classification. Both scopes retain every complete LP input,
two solver results (original HiGHS settings and tighter dual simplex settings),
actual stationarity diagnostics, exact rational primal/dual witnesses and bounds.
Tighter LP solver settings are certification calculations only: no historical
fit parameter or gate is changed. Exact rational verification, not solver
success flags or requested tolerances, determines gate classifications.

For min ||Cx-r||_infinity on a finite box, a box-feasible x provides an upper
bound. Any vector q provides a lower bound
`max(0,(q'r-support_box(C'q))/sum(abs(q)))`. Both bounds are evaluated with
exact integers/rationals representing the stored binary64 coefficients.
The independently implemented Fraction audit checks every witness again
without calling an optimization solver. LP-assembly rounding is separately
bounded for replication 21 P10.

For the outcome objective, a rational dual basis reconstruction for P10
provides an exactly feasible dual witness, 100 exact zero-penalty equalities,
and exact objective/complementarity calculations. It treats tau as exact 9/10
and stored full-precision response/design/coefficients/penalties as exact
rationals, recomputing residuals exactly. Other floating dual solutions are
explicitly approximate and their floating gaps are not certified bounds.

All seven alternative residual tie classifications are diagnostic only.
They never replace the historical 1e-7 tie rule or gate. KNOWN is not fitted
and has no optimizer KKT gate; the 92 fitted arms comprise 23 datasets x 4.

Historical source/output and all other repository files except Git metadata
are protected by pre/post SHA-256 snapshots. The external prior backup hash
is checked before reconstruction. Raw certification directories are ignored
and must be preserved separately; source/report files alone are insufficient
to archive the numerical certificates.

Completed run: `saved_inputs_20261029T080821Z/`. An earlier attempt at
`saved_inputs_20261029T080751Z/` is retained: its certification-only P11 summary
encountered an empty zero-penalty group. The corrected implementation uses 0
for that vacuous maximum. No fit, source dataset or historical gate changed.
