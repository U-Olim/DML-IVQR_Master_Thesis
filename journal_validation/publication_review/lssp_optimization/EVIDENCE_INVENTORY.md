# Full evidence locator inventory

This document accompanies both proposed PDFs. It relocates the original E1--E6 inventory without claiming new public access. The old uncommitted-status wording is corrected; EVIDENCE_INVENTORY_ORIGINAL.tex preserves the original inventory verbatim. Scientific keys and source paths are unchanged. Public access checks remain those reported on 10 November 2026, not a new network verification. Local-only exclusions, missing freeze resolution and RNG limitations remain applicable.

## Full original inventory (readable transcription)

## Frozen-evidence map

All paths below are repository-relative. The checked accessible evidence revision is `15b8b4dc`; it is distinct from both the unresolved historical freeze identifier and the present manuscript version. Full identifiers and access limitations appear in the data and code availability statement. Keys E1--E6 connect the principal findings to saved evidence, including cells omitted from compact main-text displays. This map identifies sources; it does not recompute descriptive comparison counts or rerun historical checks.

| Key | Finding | Original manuscript location |
|---|---|---|
| E1 | Designed relevance ordering | Section 4.1 |
| E2 | Point errors and qualified implementation rankings | Section 4.2 |
| E3 | Direct truth acceptance and false-candidate rejection | Sections 4.3–4.4 |
| E4 | Grid informativeness | Section 4.5 |
| E5 | Domain expansion | Appendix A and Technical Supplement |
| E6 | Selected-case numerical sensitivity | Appendix D |






### E1: Relevance.

 `thesis_extension/calibration/instrument_strength_100rep/kappa_strength_summary.csv`; presentation: `journal_article/tables/table_strength_calibration.tex`.


### E2: Full performance.

 `thesis_extension/final/output/n500/summary.csv` and `thesis_extension/final/output/n1000/summary.csv` contain Bias, MAE, RMSE, historical `Coverage`/`Size`, accepted-measure and boundary/full-grid summaries. Replication-level sources are `thesis_extension/final/output/n500/results.csv` and `thesis_extension/final/output/n1000/results.csv`; stored candidate statistics are `thesis_extension/final/output/n500/profiles.csv` and `thesis_extension/final/output/n1000/profiles.csv`. Full presentation assets: `journal_article/tables/generated/appendix_point_performance.tex`, `journal_article/tables/generated/appendix_coverage.tex`, and `journal_article/tables/generated/appendix_cr_informativeness.tex`; compact table: `journal_article/tables/table_main_performance.tex`. Existing RMSE images are `journal_article/figures/generated/rmse_n500.png` and `journal_article/figures/generated/rmse_n1000.png`.


### E3: Truth testing and power.

 Use E2's `Coverage`, `Size` and replication `W\_true` fields for direct-at-truth evaluations. False-candidate summaries are `thesis_extension/final/output/n500/power_summary.csv` and `thesis_extension/final/output/n1000/power_summary.csv`; replication records are `thesis_extension/final/output/n500/power.csv` and `thesis_extension/final/output/n1000/power.csv`. Full presentation: `journal_article/tables/generated/appendix_power.tex`; figures: `journal_article/figures/generated/coverage_heatmap.pdf` and `journal_article/figures/generated/power_median_combined.pdf`. The abstract's $0.942/3.900/0.094$ contrast selects E2's `Coverage`/`median\_grid\_accepted\_set\_measure` and this power summary's `power`, respectively, at $n=1000$, $\tau=0.50$, $\kappa=0.10$, estimator `DML-IVQR-BC`, with $\Delta=0.50$ for power only. These are different summaries, not a joint event or validated grid-set coverage.


### E4: Grid informativeness.

 In addition to E2's summaries/profiles, `thesis_extension/reporting/output/table_cr_informativeness_full.csv` contains all design cells. Existing images are `journal_article/figures/generated/accepted_measure_n500.png`, `journal_article/figures/generated/accepted_measure_n1000.png`, and `journal_article/figures/generated/full_domain_acceptance_heatmap.pdf`. Grid quadrature and all-grid acceptance are distinct diagnostics on the maintained domain.


### E5: Domain expansion.

 Tracked sources: `thesis_extension/diagnostics/grid_sensitivity/output/stage1/stage1_summary.csv`, `thesis_extension/diagnostics/grid_sensitivity/output/stage1/stage1_expansion_summary.csv`, `thesis_extension/diagnostics/grid_sensitivity/output/stage2/stage2_summary.csv`, and `thesis_extension/diagnostics/grid_sensitivity/output/stage2/stage2_expansion_summary.csv`. Combined reporting view: `thesis_extension/reporting/output/table_grid_domain_diagnostic.csv`; table and figure: `journal_article/tables/generated/appendix_grid_diagnostic.tex` and `journal_article/figures/grid_domain_expansion.png`. Design, failure and local-only artifact scope are in `thesis_extension/diagnostics/grid_sensitivity/GRID_RESULTS_PROVENANCE.md` and `thesis_extension/diagnostics/grid_sensitivity/GRID_RESULTS_MANIFEST.csv`. This separate diagnostic uses 100 intended replications; the recorded Stage 1 failure remains excluded from complete-profile summaries, not counted as acceptance. Large profiles and saved primitives are Git-ignored; tracked summaries do not supply full stochastic replay.


### E6: Numerical sensitivity.

 `journal_validation/stage2g/full_path_validation/FULL_PATH_REPORT.md` records the selected 24-problem comparison and five Policy A/C decision differences. `journal_validation/stage2g/deterministic_implementation/DETERMINISTIC_IMPLEMENTATION_REPORT.md` and `journal_validation/stage2g/deterministic_implementation/IMPLEMENTATION_CONTRACT_v1.md` specify the fixed-objective and input scope of later certificates. Earlier rank-stability evidence is in `journal_validation/stage2c/stability/STABILITY_REPORT.md`. These reports are not population error rates or replacements for E2--E5.


The inventories `thesis_extension/reporting/EMPIRICAL_RESULTS_MANIFEST.csv` and `thesis_extension/reporting/REPORTING_OUTPUT_MANIFEST.csv` retain historical input/output hashes and provenance. An entry in a manifest alone does not establish public availability: local-only exclusions are stated in the data and code availability statement.


## Relocated administrative paragraphs from Appendix D.1

The computational archive is the project repository \url{https://github.com/U-Olim/DML-IVQR_Master_Thesis}. This reference identifies the archived workflow; it is not a claim of bit-for-bit regeneration from a seed on arbitrary systems. Preserved source is in \path{simulation/}, \path{Empirical_work/}, and \path{example/}; extension wrappers and configuration are in \path{thesis_extension/src/} and \path{thesis_extension/config/extension_config.R}. The checked accessible evidence archive is commit \texttt{15b8b4dc}; it contains the earlier editorial batches. Current manuscript revisions are local and uncommitted. The freeze record's historical identifier \texttt{ac9a9cca} (2 September 2026) remains unresolved; full identifiers and access limits appear in the data and code availability statement.

Frozen CSVs permit deterministic reporting without re-estimation. Input/output manifests in \path{thesis_extension/reporting/}, diagnostic provenance records, reporting consistency checks, and figure validation records connect the reported numbers to archived outputs. Historical manifests describe their archived presentation state and can retain former asset paths. The original figure check covered 480 plotted values; selected-figure validation separately covered 120 coverage values, 120 full-grid frequencies, and 168 median rejection probabilities. The coverage summary is reconstructed from integer direct-at-truth counts; the variance illustration is analytical. This editorial conversion does not rerun those historical validations or simulations.

The quoted historical paragraph above records the original build-time uncommitted status; it is not a statement of current Git status.
