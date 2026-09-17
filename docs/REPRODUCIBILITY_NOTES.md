# Reproducibility notes

Empirical manifests contain SHA-256 hashes of the canonical Windows working-tree files. Git or GitHub archive/export representations may use LF line endings for tracked text files instead of the Windows working tree's CRLF line endings. Raw SHA-256 values can therefore differ even when textual content is identical.

Integrity checks performed on the canonical Windows project remain authoritative, and no result discrepancy was detected. Binary and result artifacts should be verified against their canonical manifests without line-ending normalization unless such normalization is explicitly documented.


## Detailed archived implementation reference

The following material was consolidated from an inactive appendix draft. It
documents the original frozen workflow, not an instruction to rerun simulations
or replace current outputs. The active thesis appendices are listed in
`thesis/tools/APPENDIX_REPORTING.md`. That file also describes the current
presentation-only appendix-table workflow.

This appendix records the repository materials needed to understand and reproduce the computational workflow. All paths are relative to the repository root. The archived outputs and manifests permit verification of the reported evidence, but the material is not described as bit-for-bit reproducible across arbitrary systems.

### Preserved Source and Extension Architecture

The authors' source code remains unmodified in `Empirical_work/`, `example/`, and `simulation/`. Thesis-specific code is separated into `thesis_extension/src/`, with the frozen design in `thesis_extension/config/extension_config.R`. The wrapper files `author_oracle_wrapper.R`, `author_full_wrapper.R`, and `author_bc_dml_wrapper.R` reproduce the estimator logic used by the extension without modifying the preserved source directories. Main outputs are stored by sample size under `thesis_extension/final/output/n500/` and `thesis_extension/final/output/n1000/`. Diagnostic and reporting code occupy separate namespaces under `thesis_extension/diagnostics/` and `thesis_extension/reporting/`.

### Computational Environment

The canonical runtime is R 3.4.3 dated 30 November 2017 on 64-bit Windows, and the simulations use five workers. The complete captured session is in `thesis_extension/environment/sessionInfo_R343.txt`, while `thesis_extension/environment/library_manifest_R343.csv` records the installed library inventory. The attached packages in the captured session are `doSNOW` 1.0.16, `snow` 0.4-2, `iterators` 1.0.8, `foreach` 1.4.3, `mvtnorm` 1.0-6, `hqreg` 1.4, `hdm` 0.2.0, `quantreg` 5.34, and `SparseM` 1.77. The session record also lists the loaded namespace versions, including `Matrix` 1.2-12, `MatrixModels` 0.4-1, and `Formula` 1.2-2.

### Frozen Simulation Configuration

The main design uses $n\in\{500,1000\}$, $\tau\in\{0.10,0.25,0.50,0.75,0.90\}$, $\kappa\in\{1,0.50,0.25,0.10\}$, and 500 Monte Carlo replications per design. The estimators are Oracle-GMM, Full-GMM, and DML-IVQR. Power is evaluated at offsets $\Delta\in\{-1,-0.5,-0.25,0.25,0.5,1\}$. The primary candidate grid contains 41 values from $-1$ to $3$ in increments of $0.1$. Inference uses a 95\% confidence level and the 0.95 quantile of a chi-square distribution with two degrees of freedom. The DML quantile-Lasso penalty follows the BC pivotal route with 1,000 simulated draws, scale factor 2, and penalty-tail probability 0.1. These settings are recorded in `thesis_extension/config/extension_config.R` and summarized in `thesis_extension/reporting/EMPIRICAL_RESULTS_FREEZE.md`.

### Randomness and Seeds

The main simulation seed is 675, set in `thesis_extension/final/run_final.R` from the frozen extension configuration. The grid-domain diagnostic separately sets seed 675 in `thesis_extension/diagnostics/grid_sensitivity/grid_sensitivity_config.R`; its Stage 2 reuses the saved Stage 1 primitives rather than generating replacement samples. The instrument-strength calibration uses pilot seed 20260813, recorded in `thesis_extension/calibration/instrument_strength_100rep/run_strength_calibration.R`. No distinct seed is asserted for a task unless it is recorded in these repository files.

### Reproduction Workflow

This workflow documents how the archived analysis was produced and how it can be regenerated from the repository; it is not a one-command or bit-for-bit reproduction claim. Begin from the repository root with the canonical R 3.4.3 `Rscript` executable and the preserved package library described above. The reproduction workflow should be run from a clean or deliberately prepared output location. The simulation scripts do not provide a general safeguard against overwriting existing output files, so canonical archived results should be preserved before rerunning the workflow. The frozen manifests record the archived file hashes and can be used to compare newly generated outputs, but they do not constitute a general locking mechanism.

After the environment and output locations have been prepared, the empirical inputs are generated in the following dependency order:

1. Run the main simulation through `thesis_extension/final/run_final.R` with `--sample-size=500` and `--execute-final`, followed separately by `--sample-size=1000` and `--execute-final`.
1. Generate the reported instrument-strength calibration with `thesis_extension/calibration/instrument_strength_100rep/run_strength_calibration.R` and `--execute-calibration`.
1. Run the grid-domain diagnostic through `thesis_extension/diagnostics/grid_sensitivity/run_grid_sensitivity.R`, first with `--execute-stage1` and then, after checking the prespecified trigger, with `--execute-stage2`.
1. Run the coverage forensic audit through `thesis_extension/diagnostics/coverage_audit/run_coverage_audit.R` with `--execute-coverage-audit`; this audit reads the completed main-run outputs.
1. Only after all preceding empirical inputs exist, run `thesis_extension/reporting/build_thesis_results.R` with `--build-reporting`. The reporting builder reads the main-run, calibration, grid-diagnostic, coverage-audit, validation, and environment records; it does not rerun estimation or simulation.
1. Review the generated reporting consistency checks and the empirical-input and reporting-output manifests together with the diagnostic provenance records listed below.


For the frozen reporting build, the repository must be checked out at commit `ac9a9ccad027cde05488abb633e66cc02f87cc46`; the builder verifies this exact `HEAD` value but does not itself certify that the worktree is clean. All required empirical inputs must already be present. The directories `thesis_extension/reporting/output/` and `thesis_extension/reporting/figures/` must be empty or deliberately prepared as empty, and `EMPIRICAL_RESULTS_MANIFEST.csv` and `REPORTING_OUTPUT_MANIFEST.csv` must be absent from the reporting directory, because the builder refuses to replace nonempty reporting directories or existing reporting manifests.

### Failure Handling

The canonical main-run summaries record zero numerical failures, as confirmed by `thesis_extension/reporting/output/reporting_consistency_checks.csv`. The grid-domain diagnostic records one Stage 1 failure: replication 35, $\tau=0.90$, $\kappa=0.10$, DML-IVQR, and candidate $a=-2.1$, with the message ```Error info = 95 in stepy2: singular design`.'' Stage 2 records no new evaluation failure. Candidate evaluation is wrapped in error handling: an error or nonfinite statistic is stored with its replication, design, estimator, candidate, stage, and message; the affected statistic is set to missing. A profile containing a failed evaluation is flagged as incomplete, and its aggregate accepted-set measures are reported as missing rather than being computed from a partial profile.

### Theory and Code Correspondence

The preserved DML implementation estimates nuisance quantities and evaluates scores on the same sample; it does not use sample splitting or cross-fitting. It uses the BC pivotal penalty and the fitted-normal density proxy documented in Section 3.3. The implementation-specific density-call detail is documented in Appendix D (Reproducibility and Implementation Notes). Instrument residualization regresses $\sqrt{\widehat f_i}Z_{ji}$ on transformed controls with an ordinary unpenalized intercept. The score subtracts that retained constant term and the fitted slopes from the untransformed instrument, without dividing the constant term by $\sqrt{\widehat f_i}$. As explained in Section 3.3, this constant term is implementation specific and is not the exact sample version of the constant term in the population projection including the controls.

### Provenance and Verification Records

The empirical-results freeze is identified by commit `ac9a9ccad027cde05488abb633e66cc02f87cc46`, dated 2 September 2026; the pre-writing integration checkpoint is commit `911e0861114426b5aad314a6f2b7f0c1f92b3fcd`. The primary verification records are `PROJECT_STATUS.md`; `thesis_extension/validation/R343_final_audit/FINAL_PRE_RUN_AUDIT.md`; `thesis_extension/reporting/EMPIRICAL_RESULTS_FREEZE.md`; the input and output hash inventories `EMPIRICAL_RESULTS_MANIFEST.csv` and `REPORTING_OUTPUT_MANIFEST.csv` in the reporting directory; `thesis_extension/reporting/output/reporting_consistency_checks.csv`; and `thesis/figures/THESIS_FIGURE_DATA_CHECK.csv`. The grid diagnostic is documented by `GRID_RESULTS_PROVENANCE.md` and `GRID_RESULTS_MANIFEST.csv` in its directory, while the coverage check is documented by `COVERAGE_AUDIT_REPORT.md` and `COVERAGE_AUDIT_MANIFEST.csv`. Together these files record configuration, environment, source roles, output checks, and file hashes used to connect the archived computations to the reported thesis results.


## Supplementary results retained outside the PDF

The removed supplementary appendix wrapper contained no numerical results of
its own. Its complete frozen tables and RMSE graphic remain available:

- `thesis/tables/generated/appendix_point_performance.tex`
- `thesis/tables/generated/appendix_cr_informativeness.tex`
- `thesis/tables/generated/appendix_power.tex`
- `thesis/tables/generated/appendix_coverage.tex`
- `thesis/tables/generated/figure_rmse.tex`

These report both sample sizes, all five quantiles, all four relevance settings
and all three estimators. Corresponding machine-readable tables remain under
`thesis_extension/reporting/output/`. The full audit's empirical coverage range
is 0.442--0.976, also represented in the active audit summary table. The
source audit and its manifest remain under
`thesis_extension/diagnostics/coverage_audit/`.

The combined coverage/reproducibility draft duplicated the active appendices
and the detailed reference above. The boundary draft's unique failure record
(replication 35, tau 0.90, kappa 0.10, DML-IVQR, candidate -2.1; no new Stage 2
evaluation errors) is retained in the reference above; active Appendix A
retains the corresponding failure-count and denominator disclosure.

## September 2026 presentation cleanup

The final thesis uses the selected coverage heatmap, median-power figure,
accepted-set figure, and consolidated main-results table. After exact checks
against the frozen reporting CSVs, the superseded standalone coverage render,
paired coverage PNGs, signed-deviation power PNGs, obsolete LaTeX figure
wrappers, two obsolete presentation tables, and the review-only asset preview
were removed. The complete multi-quantile power, coverage, point-performance,
and accepted-set results remain in `thesis_extension/reporting/output/` and in
the retained supplementary tables under `thesis/tables/generated/`.

`thesis/tools/build_thesis_figures.R` now renders only the retained RMSE and
accepted-set PNGs; the current coverage and power PDFs are generated by
`thesis/tools/build_selected_figures.R`. The obsolete standalone coverage
renderer was removed. Root-level LaTeX scratch files and the copied author
replication log were also removed as disposable build artifacts; the source
R Markdown, compiled replication report, tables, figures, and the historical
integrity inventory remain.

Historical provenance records, including `thesis/ASSET_PROVENANCE.md`,
`thesis/figures/THESIS_FIGURE_MANIFEST.csv`,
`thesis/figures/THESIS_FIGURE_DATA_CHECK.csv`, and
`docs/author_replication_report/SOURCE.md`, were deliberately left unchanged.
They therefore retain the former paths and hashes as a record of the archived
presentation state rather than as an inventory of files currently present.
