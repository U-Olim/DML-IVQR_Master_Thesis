# Appendix reporting and organisation

Run `python thesis/tools/build_appendix_tables.py` from the repository root,
then `latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex` from
`thesis/`. Requires Python 3.9+. No simulation or estimation is run.

The active appendix inputs in `thesis/main.tex` are:

- A: `appendix_numerical_domain.tex` — Numerical-Domain Diagnostics.
- B: `appendix_kappa_derivation.tex` — Derivation and Properties of the κ-Extension.
- C: `appendix_coverage_audit_minimal.tex` — Coverage Audit and Inferential Informativeness.
- D: `appendix_reproducibility_note.tex` — Reproducibility and Implementation Notes.

Semantic labels are retained for the relocated audit, reproducibility material,
and full-domain heatmap. The latter is now Figure C.1. Its approved PDF and
6.48-point numerical typography are unchanged. Table A.1 and Figure A.1 retain
their numerical content. Obsolete inactive appendix wrappers were removed
after checking nested inputs and all repository build/reporting scripts.

## Source-directory cleanup

The four files listed above are the only active appendix sources; none includes
an obsolete draft. Reporting scripts produce CSVs or files under `thesis/tables`,
not the deleted appendix wrappers, so no generator rewrite is needed.

- Removed `appendix_boundary.tex`: domain argument and failure-count disclosure
  duplicated A; unique replication/candidate details consolidated into the
  reproducibility reference.
- Removed `appendix_coverage.tex`: audit duplicated C; the coverage range is
  retained in its summary table and supplementary documentation.
- Removed `appendix_coverage_reproducibility.tex`: combined draft duplicated
  C/D and the preserved implementation reference.
- Removed `appendix_reproducibility.tex`: detailed architecture, environment,
  configuration, workflow restrictions, failure handling and provenance
  consolidated into the existing `docs/REPRODUCIBILITY_NOTES.md`.
- Removed `appendix_supplementary_results.tex`: inactive input wrapper; all
  referenced generated tables, figures and final CSVs remain, with an index
  in the same reproducibility document.

Appendices A--D use locally scoped ragged-bottom page alignment. A/B retain
one-baseline float-to-text spacing; C/D use fixed 8pt textfloatsep, intextsep,
and floatsep. Table C.1 and Figure C.1 allow here/top placement with [!ht].
This prevents
the global flush-bottom setting from stretching the float-to-text and heading
gaps after Figure A.1. No margin, figure size, or document-wide spacing changes
are needed. The float barrier retains the figure-before-paragraph reading order.

## Evidence and generated outputs

The new reporting script reads both final `results.csv` files and
`diagnostics/coverage_audit/output/coverage_audit_all_cells.csv` under
`thesis_extension/`. It implements the two-sided 95% Wilson score formula
without continuity correction documented in `coverage_audit_functions.R`.
Integer acceptance counts come from saved direct-at-truth W statistics;
denominators are verified from all replication IDs, never reconstructed from
rounded percentages. Unrounded endpoints agree with the archived audit.

Results: 120 cells, 500 evaluations each, 60,000 evaluations total; 53 intervals
entirely below 0.95 and one entirely above, totaling 54 exclusions. No missing,
nonfinite or failed direct-at-truth evaluations. Missing and nonfinite counts
are not added together, since the frozen audit's nonfinite count includes missing.

Generated files:

- `thesis/tables/appendix_coverage_audit_summary.tex` (Table C.1).
- `thesis/tables/appendix_kappa_illustration.tex` (Table B.1).
- `thesis_extension/reporting/output/appendix_coverage_audit_cells.csv`.
- `thesis_extension/reporting/output/appendix_coverage_audit_summary.csv`.
- `thesis_extension/reporting/output/appendix_kappa_illustration.csv`.
- `thesis_extension/reporting/output/appendix_tables_validation.json`.

The validation JSON records source hashes, audit totals, the minimum
truth-to-boundary distance (0.7184484344553992), and domain-table checks.
The κ illustration is evaluated analytically, not simulated. The derivation
is checked against `src/dgp_kappa.R`: transformed X controls in the observed
instruments, jointly normal (u, epsilon) with covariance 0.3, and independent
normal z, v, x, w primitives. The squared κ in the compensating variance is
essential.

## Domain diagnostic qualification

`diagnostics/grid_sensitivity/grid_sensitivity_config.R` and saved
`output/stage2/stage2_config.txt` specify n=1000, 100 replications, κ in
{1,0.25,0.10}, and step 0.1 on [-1,3], [-3,5], [-5,7]. The saved stage-two
summary contains 135 domain-specific cells. The original Table A.1 values
match its rounded medians and means.

One DML-IVQR profile at τ=0.90, κ=0.10 is failed in each expanded domain,
leaving 99 usable measures in those two summary cells. All other displayed
cells use 100. The preserved diagnostic aggregates nonmissing measures;
Table A.1 now explicitly discloses that treatment, rather than changing
denominators or results. The diagnostic is distinct from the complete main
simulation coverage records and does not create an audit-count discrepancy.

All previous audit paragraphs and all three previous reproducibility
paragraphs remain, including the parallel-RNG limitation and the dnorm
variance-versus-standard-deviation implementation disclosure.
