# Stage 2C-P: saved-fit numerical protocol and reassessment

`PROTOCOL.md` was written and SHA-256 recorded before the 92-arm reassessment.
It defines a conservative classification system without inventing a relaxed
gate or an application accuracy budget. Historical KKT results remain separate.

Requirements: existing Python/NumPy/SciPy and the Stage 2C-V full-precision
binary exports. R 3.4.3 is used only for exporting saved ordinary-QR reference
coefficients; no outcome model is fitted and no random numbers are generated.
No package is installed. Work on journal-validation only.

From repository root:

```powershell
python -B journal_validation/stage2c/validation_protocol/reassess.py
# RUN is the unique reassessment directory printed by that command:
python -B journal_validation/stage2c/validation_protocol/audit.py RUN
python -B journal_validation/stage2c/validation_protocol/reference_review.py RUN
python -B journal_validation/stage2c/validation_protocol/finalize.py RUN
```

Each reassessment creates a unique UTC-named directory and never overwrites
historical evidence. All new files are inside validation_protocol. Solver LPs
construct dual certificate witnesses only, holding every outcome coefficient
fixed. No continuation code or production runner is used.

Certificate algorithm:

1. Read Stage 2C-V full-precision saved design, candidate-adjusted response,
   coefficients, penalties and residuals; verify its integrity manifest.
2. Solve the quantile-regression dual for a numerical witness. Select a
   certificate basis for zero-penalty equations and solve it with exact integer
   elimination. This solves for dual subgradients, never outcome coefficients.
3. Scale the rational witness toward zero, if necessary, to satisfy all box
   and penalty constraints exactly. Equalities remain exact under scaling.
4. Compute exact primal/dual objectives, gap and complementarity. Independently
   recheck these with a separate integer/Fraction implementation.
5. Evaluate the predeclared fixed coefficient perturbations as numerical
   sensitivity probes, not alternative fits. Save exact probe-objective upper
   bounds and rank-sign changes, without computing acceptance rates or using
   them to select criteria.
6. Compare saved P00 and ordinary-QR reference coefficients; no reference refit.

`arm_summary.json` and the final classification CSV distinguish objective-error
certification from application-level accuracy classification. A finite positive
certified gap is an error upper bound; it does not prove either acceptable or
unacceptable rank-score error without an independently justified budget and
transfer argument. Indeterminate is therefore an intentional possible outcome.

Snapshots protect every repository file outside this directory except Git
metadata. Source hashes before reassessment identify the frozen protocol and
generator. Final source/artifact hashes cover report, scripts, witnesses and
audits. Ignored raw reassessment directories must be preserved separately.

Completed reassessment: `reassessment_20261029T083111Z/`.
Stop after the report; do not generate indices 22-40.
