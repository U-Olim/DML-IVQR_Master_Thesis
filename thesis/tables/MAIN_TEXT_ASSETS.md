# Current main-text tables and figures

This inventory describes the assets currently included by
`thesis/sections/05_results.tex`. It replaces the earlier presentation plan;
the archived numerical CSVs and historical manifests remain unchanged.

## Active main-text assets

| Number | LaTeX source | Data graphic or table |
|---|---|---|
| Table 1 | `table_strength_calibration.tex` | Instrument-strength calibration |
| Table 2 | `table_main_performance.tex` | Selected point, coverage and accepted-set results |
| Figure 1 | `figure_coverage_main.tex` | `coverage_heatmap.pdf` |
| Figure 2 | `figure_power_main.tex` | `power_median_combined.pdf` |
| Figure 3 | `figure_accepted_measure_main.tex` | `accepted_measure_n500_thesis.png`, `accepted_measure_n1000_thesis.png` |

Appendix Figure C.1 uses `figure_full_domain_acceptance.tex` and
`full_domain_acceptance_heatmap.pdf`.

`thesis/tools/validate_selected_figures.py` verifies the coverage, median-power
and full-domain values against final saved evaluations.
`thesis/tools/build_selected_figures.R` renders the current vector PDFs.
`thesis/tools/build_thesis_figures.R` is retained for the current accepted-set
images and supplementary RMSE images only.

## Retained supplementary evidence

The complete reporting CSVs remain under `thesis_extension/reporting/output/`,
including full point performance, coverage, power and accepted-set results.
The generated supplementary tables `appendix_point_performance.tex`,
`appendix_coverage.tex`, `appendix_power.tex`, and
`appendix_cr_informativeness.tex` remain available even where they are not
included in the thesis PDF.

The superseded preview, wrappers, standalone coverage render, paired coverage
PNGs, and two signed-deviation power PNGs were intentionally removed in the
September 2026 presentation cleanup. Their numerical content remains in the
retained reporting CSVs. Historical provenance manifests were preserved and
therefore continue to record those former files and their hashes.
