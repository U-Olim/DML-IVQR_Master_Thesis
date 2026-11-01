# Stage 2C-V - Independent numerical certification

29 October 2026, Asia/Tashkent. Branch `journal-validation`.
Historical Stage 2C run: `../output/controlled_20261029_01/`.
Completed certification run: `saved_inputs_20261029T080821Z/`.

## Executive decision

**B - Certified failure of the original replication-21 P10 gate.**

Exact rational upper/lower bounds enclose the original CSV-based validation
LP optimum in

**[1.0044854602993909e-7, 1.0044854732729425e-7]**.

The entire enclosure is above the unchanged historical gate 1e-7. The result
is no longer numerically indeterminate. The previous concern about a 1e-9
LP feasibility setting was justified as a reason to investigate; it is not
evidence that the historical classification was wrong. Actual residuals and
independent exact witnesses now resolve that uncertainty.

This is a failure of the specified approximate KKT/tie-classification gate,
not proof of material outcome-optimization failure. An independently
constructed EXACTLY dual-feasible quantile-regression certificate gives

**0 <= Q(saved P10 coefficients) - Q(optimum) <= 1.1776241822846186e-8**,

approximately 1.39e-10 relative to the primal objective. A positive certificate
gap is an upper bound on suboptimality, not proof the saved coefficients are
strictly suboptimal. No outcome fit was repeated. The historical failure is
retained, and no simulation was resumed.

## Preservation and scope

Before creating certification files: branch was `journal-validation`;
historical Stage 2C output and external Stage 2A/2B archive existed; Git status
showed only the existing untracked Stage 2C directory. The external archive
SHA-256 was verified as
`184f7270ac65bd0886e0515e2f2c1944a4d08eeb5f924a97200dad480c7b0fb7`.

Its path remains
`C:/Users/User/DML-IVQR_validation_backups/stage2ab_before_stage2c_20261029T074433Z.zip`.

All new files are inside `journal_validation/stage2c/certification/`.
Pre/post SHA-256 comparisons protect **4,535 existing files**, excluding only
this certification directory and Git metadata. Zero changes, missing files,
or additions outside certification were found. Historical summaries, fit
code, configurations, original datasets, wrappers, RNG records, Stage 2A/2B,
thesis and journal manuscript remain unchanged. No commit or push occurred.

The R helper only reads existing RDS objects and writes binary64 exports;
it loads no estimator code, makes no random draws and performs no fits.
The Python solvers operate only on saved-input validation/certificate LPs.
No Monte Carlo samples or replications 22-40 were generated.

## Inputs and exact reconstruction

Two input scopes are deliberately distinguished:

1. **Historical CSV LP:** the original `verify_one.py` parses CSVs, computes
   its numerical tie sets, dot products and normalizations, and hands binary64
   LP arrays to HiGHS. These arrays are reconstructed with the same operations.
   Replication-21 P10 reproduces the recorded epigraph
   `1.0044854692833311e-7` exactly.
2. **Full-precision LP:** original RDS doubles are exported without decimal
   truncation, and the same formulation/classifications are applied.

Across all 92 fitted arms, maximum design CSV/binary difference is
5.551115123125783e-16 and maximum saved-residual difference is
5.329070518200751e-15. There are zero tie-classification changes. Both scopes
give identical gate classifications.

For each scope, `lp_inputs.npz` stores design, coefficients, residuals,
penalties, score, tie sets, variable bounds, C, r, A, b and objective. Complete
solver results, primal witnesses, dual-direction witnesses and diagnostics
are retained. Full-precision exports use little-endian IEEE754 binary64.

## Mathematical certification

The unchanged validation problem is

    minimize ||C x - r||_infinity, subject to lo <= x <= hi.

The box variables comprise numerical-tie check-loss subgradients and numerical
zero-coefficient penalty subgradients. All check-loss and half-L1 factors,
coefficient threshold 1e-7, residual threshold 1e-7, n=1000 normalization and
historical gate remain unchanged.

For any box-feasible x, U=||Cx-r||_infinity is a primal upper bound.
For any nonzero q,

    L = max(0, (q'r - support_box(C' q)) / ||q||_1)

is a lower bound. This follows from Holder's inequality and maximizing the
linear function over the box. q need not satisfy an approximately solved
dual stationarity system. The support function is evaluated exactly.

`exact_bounds.py` treats every binary64 LP coefficient/witness as an exact
dyadic rational, clamps x to its exact box, and evaluates U and L with integer
arithmetic. Numerators/denominators and outward-rounded displays are retained.
The threshold comparison uses the exact binary64 value of historical 1e-7.
The corresponding decimal 1/10,000,000 gives the same classifications.

`audit_certificates.py` independently implements the dot products and support
bounds using Python Fraction arithmetic, without calling a solver. It verified
**191 LP problems and 382 witnesses**: two representations of 92 fitted arms,
plus seven diagnostic tie classifications, with two algorithm witnesses each.

Original LP settings: SciPy 1.17.1 `linprog(method='highs')`, primal and dual
feasibility settings 1e-9. Additional certificate witnesses use `highs-ds`
with feasibility settings 1e-10. These are certificate-LP settings, not changes
to an outcome fit or the historical gate. Exact rational bounds determine
classification, not requested solver tolerances. HiGHS shares a solver
library across these algorithms; independent arithmetic supplies the
solver-independent verification.

For full-precision P10, LP-assembly rounding was additionally bounded against
the mathematical LP formed without rounded sums/divisions. Its uniform
objective perturbation is at most 9.320171819995998e-17. The resulting
unrounded-LP enclosure is approximately
**[1.0044854628322962e-7, 1.0044854842730563e-7]**, also a certified failure.
The proof and exact rational bounds are in `assembly_rounding_certificate.json`.

## Replication-21 P10: attained discrepancies and coordinates

Historical CSV original algorithm:

| Quantity | Value |
|---|---:|
| Returned epigraph | 1.0044854692833311e-7 |
| Independently recomputed floating maximum | 1.0044854733236297e-7 |
| Maximum original inequality violation | 4.0419056990259605e-16 |
| Exact box-feasible upper-bound display | 1.0044854732729425e-7 |
| Best exact lower-bound display | 1.0044854602993909e-7 |

The attained maximum is not assumed equal to the epigraph. Its exact value
at the clamped rational witness is evaluated separately; the small difference
from the floating maximum is dot-product rounding.

At the reconstructed original witness, the exact largest discrepancy is at
**coordinate 11 (X11)**, an active slope with zero penalty. Many slope
constraints are nearly binding; the supporting lower-bound direction has
nonzero components on **all slopes except X35**, and zero on the intercept.
The largest individual discrepancy for the additional dual-simplex witness
is X2 because that witness has slightly different floating feasibility error.
This does not change the certified optimum enclosure and does not identify
X11 as a unique scientific cause.

The intercept is 8.14924229239866e-13 and is classified as numerical zero.
Its retained penalty is 52.7887649201011, permitting a penalty subgradient
in [-26.39438246005055,26.39438246005055]. The original witness chooses
approximately 1.9916364554; its score sum is approximately 1.9915360069.
The intercept penalty interval is far from its bounds and its lower-bound
multiplier is zero. Its discrepancy can be removed by choosing the matching
interior penalty subgradient; the irreducible obstruction is in the jointly
constrained zero-penalty slopes.

The 98 tie subgradient choices are all interior to [-.1,.9] in this witness.
Complete coordinate gradients, penalty subgradients, supporting directions,
observation indices, tie values, raw inequality slacks/marginals, solver
statuses and diagnostic active-constraint lists are saved. Approximate active
lists are explicitly numerical diagnostics, not exact assertions about a
unique optimal basis.

## Independent quantile-regression primal-dual certificate

With candidate-adjusted response y*=Y-(1+qnorm(.90))*D, the exact objective is

    Q(beta) = sum rho_.90(y* - X beta) + sum lambda_j |beta_j|/2.

Its dual is maximize y*'v subject to -.1<=v_i<=.9 and
|X_j'v|<=lambda_j/2. Zero-penalty slopes require exact equalities X_j'v=0.

An approximate dual LP supplies a basis. For P10, 100 free dual coordinates
are reconstructed using exact integer Bareiss elimination and rational back
substitution; the remaining coordinates are exact box endpoints. This is a
certificate reconstruction, not a refit of outcome coefficients.

The saved full-precision design/response/coefficients/penalties are treated
as exact rational inputs and tau as exact 9/10. Residuals and primal objective
are recomputed exactly, rather than substituting rounded saved residuals.
Candidate adjustment is performed by the same R arithmetic as the original
run before exporting the full-precision response.

All 100 zero-penalty equalities were verified **exactly**, every score lies
within the exact box, and the intercept gradient is approximately 1.9915349752,
strictly inside its permitted penalty interval.

| Quantity | Display of exact rational calculation |
|---|---:|
| Primal objective | 84.84584974882415 |
| Dual objective | 84.8458497370479 |
| Primal-dual gap | 1.1776241822846186e-8 |
| Check-loss complementarity sum | 1.1756355351168346e-8 |
| Penalty complementarity sum | 1.9886471677840074e-11 |

The complementarity sums are nonnegative and sum exactly to the gap. The
full rational dual vector, denominator, objective values and decomposition
are saved. The separate Fraction/integer audit reverified the exact dual
constraints and objective gap.

Consequently, the saved P10 fit is within the displayed small absolute
objective gap of the optimum for the specified exact input problem. This
does not prove exact optimality, coefficient accuracy, or statistical validity.
It also does not convert the original KKT-gate failure to a pass.

Floating dual solutions for the other replication-21 arms are saved with
constraint violations and complementarity diagnostics. Their small floating
gaps are NOT labeled certified bounds. A zero dual is always an exactly
feasible but uninformative baseline. Useful exact dual basis reconstruction
was performed for the requested failing P10 arm, not every other arm.

## Numerical-tie sensitivity: diagnostic only

The P10 saved solution has no exact-zero residuals. Two residual magnitudes
near the historical boundary are 1.55288088166117e-7 and 9.51238384061526e-7.
Changing the tie set enlarges/restricts the feasible subgradient box and hence
changes the validation problem itself. It does not change the saved fit.

| Diagnostic tie threshold | Interval-score observations | Certified optimum enclosure, rounded for display |
|---|---:|---|
| 0 | 0 | approximately .00448702334788907 |
| 1e-8 | 95 | [1.4488038606e-6,1.4488038795e-6] |
| 5e-8 | 98 | [1.0044854637e-7,1.0044854834e-7] |
| **1e-7: historical** | **98** | **[1.0044854637e-7,1.0044854834e-7]** |
| 2e-7 | 99 | [8.2952687816e-8,8.2952689438e-8] |
| 5e-7 | 99 | [8.2952687816e-8,8.2952689438e-8] |
| 1e-6 | 100 | [0,1.0667459112e-16] |

Exact rational bounds and outward-rounded displays are in the JSON records;
this compact table is only a readable summary. Broader bands show numerical
tie sensitivity but **cannot retroactively pass replication 21**. The solver's
eps=1e-6 is not automatically an absolute residual-error bound or a justified
replacement tie threshold.

## All saved fitted arms

Two preflight datasets plus pilot replications 1-21 comprise **92 fitted
arms**. Both historical and full-precision LP scopes yield:

| Classification | Count |
|---|---:|
| Certified pass | 91 |
| Certified failure | 1: pilot_021 P10 |
| Numerically indeterminate | 0 |
| Not assessable with saved evidence | 0 |

All 80 arms in pilot 1-20 and all eight preflight arms are certified passes.
Pilot 21 P11/P01/P00 are now independently certified passes, while the original
record that the dataset lacked complete validation is retained. KNOWN has no
outcome optimizer and its KKT classification is not applicable; these 23
diagnostic anchors are not counted as fitted arms.

The largest upper bound among historical-scope passes is
8.19237774828873e-8 (validation_001 P11), still below the historical gate.
The complete case table includes every original recorded validation result,
current classification and both bounds. The original 20-replication scientific
summaries were neither changed nor pooled with replication 21.

## Decision and safe continuation

Retain decision **B** and the historical stopped status. Neither a looser tie
band nor the small objective-gap certificate authorizes automatic continuation.
The gate is demonstrably violated under its original definition, while saved
inputs support high objective accuracy. These are compatible findings.

The next review should decide whether a revised, scale-aware numerical
verification protocol is scientifically justified, using objective/dual
feasibility and backward-error evidence rather than a favorable pass/fail
outcome. Any amendment must be documented and applied uniformly to all saved
arms, retain the original gate classification as provenance, and specify how
failed/indeterminate tasks enter subsequent summaries. Do not merely increase
the threshold, replace dataset 21, or report a completed 40-replication study.

Only after explicit authorization of that protocol and continuation plan
could indices 22-40 be generated from the original recorded data/penalty
master seeds and stream-index rule. Existing evidence must remain immutable.
No continuation capability was implemented or executed here.

## Deliverables and execution

- `README.md`: execution instructions and exact scope.
- `export_saved.R`: read-only RDS-to-binary exporter.
- `certify.py`: reconstruction, solver diagnostics, all-case assessment.
- `exact_bounds.py`: exact rational LP bounds and QR dual reconstruction.
- `audit_certificates.py`: independent no-solver witness verification.
- `rounding_review.py`: exact uniform assembly-rounding bound.
- `finalize.py`: classification/coordinate tables, final preservation and hashes.

Under the completed uniquely named run:

- `all_case_summary.json`, `classification_summary.csv`.
- `replication21_P10_coordinate_diagnostics.csv`.
- Per-arm/per-input-scope `lp_inputs.npz`, full solver results and diagnostics.
- P10 `qr_exact_certificate.json`, `qr_dual_diagnostics.json` and solver result.
- `tie_sensitivity_summary.csv`, P10 full sensitivity witnesses and residual list.
- `independent_rational_audit.json`, `assembly_rounding_certificate.json`.
- Full-precision binary exports for all 23 saved datasets/arms.
- Protected-file snapshots, `preservation.json`, `final_preservation.json`.
- `source_sha256.json`, `SHA256_MANIFEST.json`, `final_status.json`.

An initial certification-only attempt `saved_inputs_20261029T080751Z` stopped
on a reporting reduction over an empty zero-penalty group in P11. It is retained
with its outputs and unchanged-file preservation record. The vacuous maximum
was corrected in certification code, and a new unique run was used. No outcome
fit was retried and no historical validation code/configuration was modified.

All certification commands and final hashes are reproducible from the saved
inputs; raw certificate directories are ignored by Git and require separate
preservation when sharing. Stage 2C-V ends here for review.
