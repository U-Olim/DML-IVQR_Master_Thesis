# Stage 2F: exact optimal-face analysis of two saved problems

Only pilot_002 at alpha0-.5 and pilot_006 at alpha0. All observations,
candidate-adjusted responses, penalties, coefficients and downstream paths
are read from Stage 2E. No new candidate problem, Monte Carlo dataset, outcome
fit, pilot continuation, historical edit, commit or push is permitted.

## Method fixed before reconstruction

Use the independently fitted LP vector only to PROPOSE an active coefficient
set and tied residual rows (numerical bands 1e-7, not estimator tie rules).
Reconstruct beta on that basis with exact integer elimination. Verify its
actual nonzero support and exact zero residual set without tolerance. Construct
an exact dual witness by setting nonzero-residual scores to their required
endpoints and solving active-coefficient gradient equations exactly. Verify
box/penalty constraints, complementarity and zero primal-dual gap.

Attempt both tau=9/10 and literal binary64 tau. Do not call a near-optimum an
exact optimizer. If reconstruction or strict checks fail, retain evidence and
report unresolved, without fitting another problem or changing objectives.

Uniqueness sufficient condition: dual scores are strictly interior on the
certified tied rows; inactive-coefficient dual gradients are strictly inside
their penalty intervals; tied-row/active-column design is nonsingular. Then
every optimizer has zeros on the inactive coefficients and zero residuals on
the tied rows, forcing the same beta. All inequalities and rank witnesses are
checked exactly. This proves a singleton optimal face when satisfied.

Read the two original Stage 2E downstream branches as they stand. Decompose
rank-induced score and second-moment changes observation by observation, and
separate frozen-psi changes from complete-path psi changes. Exact optimum
scores under fixed saved psi are diagnostics, never substituted into historical
results. No new tie-breaking or selection rule is implemented.

## Execution

From repository root, journal-validation, existing Python/NumPy only:

```powershell
python -B journal_validation/stage2f/analyze.py
# RUN is the unique output/exact_face_UTCSTAMP directory printed above:
python -B journal_validation/stage2f/verify.py RUN
python -B journal_validation/stage2f/near_optimal.py RUN
python -B journal_validation/stage2f/verify_near_optimal.py RUN
python -B journal_validation/stage2f/representation_split.py RUN
python -B journal_validation/stage2f/finalize.py RUN
```

Exact certificate arithmetic uses Python integers/Fractions and the preserved
Bareiss helper as a computational primitive. The separate verifier uses its
own rational evaluation of feasibility, objectives, strict margins and inference.
No numerical outcome solver or instrument fit is called in this stage.

Both input problems and all prior outputs are preserved with SHA-256 manifest
checks and pre/post snapshots of every file outside stage2f except Git
metadata. New outputs are uniquely named and never overwrite inputs. Raw
output/ is ignored by Git and needs separate preservation when archiving.

The near-optimal direction analysis constructs mathematical rational witnesses
inside the SAME two objectives, not new candidate problems or another solver
fit. Its uniform-in-epsilon proof concerns frozen historical psi only. It does
not assert that extremely small rational steps are distinguishable in binary64
or prove a full native-path limit. The representation diagnostic separates
rounding the certified unique beta from re-evaluating that rounded beta; it is
not an adopted solution-selection policy and never replaces historical scores.

Completed analysis: `output/exact_face_20261029T102755Z/`. An initial attempt
`output/exact_face_20261029T102522Z/` is preserved. It encountered an inverted
equality assertion in the new analysis source, corrected without changing
inputs, basis proposal, tolerance or any historical fitting code. A subsequent
independent-audit JSON integer serialization correction affected reporting only;
the existing representation files were retained rather than recomputed.
