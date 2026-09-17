# Selected thesis figures

## Reproduction (from the repository root)

```powershell
python thesis/tools/validate_selected_figures.py
& 'C:\Program Files\R\R-3.4.3\bin\x64\Rscript.exe' thesis/tools/build_selected_figures.R
Set-Location thesis
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

Requires Python 3.9+, base R with Cairo, and installed Arial/Arial Narrow/Symbol
fonts. The validator and renderer only read saved simulation results; they
never run estimators, simulations, or random-number generators. All output
dependencies are permanent. The renderer checks the final configuration and
compares all plotted values to the final summaries again.

## Inputs and validation

`thesis_extension/final/output/n500/` and `n1000/` each supply `summary.csv`,
`results.csv`, `profiles.csv`, `power_summary.csv`, and `power.csv`.
`thesis_extension/config/extension_config.R` supplies design/grid/inference
settings; definitions follow `thesis_extension/src/metrics.R` and
`thesis_extension/src/run_extension.R`.

The cutoff is chi-square(2), 95th percentile, 5.9914645471: nominal coverage
95%, nominal test size 5%. Every cell has 500 complete replications with IDs
1--500. No failures or missing values were discarded. Validation fails if
any arise, rather than silently altering the existing denominators.

The validator writes `selected_heatmap_values.csv`, `selected_power_values.csv`,
and `selected_figures_validation.json` under `thesis/figures/generated/`.
The JSON includes SHA-256 hashes of the final data inputs.

- All 120 coverage values match direct-at-truth acceptance, not rounded-grid
  membership. Observed coverage range: 44.2--97.6%.
- All 120 full-domain frequencies match acceptance of all 41 saved grid
  points in [-1,3], step 0.1. All 2,460,000 saved grid evaluations were checked.
  Observed frequencies: 0--61.6%. This event does not imply unrestricted
  confidence-region unboundedness.
- Median power uses 144 saved alternative cells plus 24 direct-at-truth size
  cells, giving 168 plotted probabilities. Delta is candidate minus truth;
  lowercase delta in the figure denotes this same saved deviation. All six
  saved nonzero deviations are plotted, with no interpolation of evaluations.

## Permanent assets and integration

All three vector PDFs are in `thesis/figures/generated/`:

| Asset | Final number | Displayed size |
|---|---|---|
| `coverage_heatmap.pdf` | 1 | 10.44 x 8.89 cm |
| `power_median_combined.pdf` | 2 | 14.5 x 16.002 cm |
| `full_domain_acceptance_heatmap.pdf` | C.1 | 10.44 x 8.89 cm |

The actual thesis text width is 14.5 cm (A4 less 2.5/4 cm margins). Existing
heatmaps use 0.72 textwidth = 10.44 cm, while Figures 2 and 3 use the full
14.5 cm line width. The supplied local university template confirms this text
width and 10-point captions/9-point figure notes; the current preamble already
implements them.
Graphics use embedded Arial/Symbol at 9 points. Heatmap cell annotations now
use regular 6.48-point Arial Narrow (7.2 points times 0.90, applied once).
Quantile, kappa and colour-bar numeric labels use the same 6.48-point size;
quantile labels remain horizontal and centred. All other text and graphic
dimensions are unchanged. Power typography is unchanged. Pass
`--heatmaps-only` to the R script to regenerate only the two heatmaps.

Before integration, compiled numbering differed from the requested ordering:
accepted-set measure was Figure 2 and old power was Figure 3. The final sequence
follows the requested coverage/power/retained-measure ordering. The retained
accepted-set measure assets, caption, label, and original generation script
remain available. Its two 3600 x 2200 images display at approximately
14.5 x 8.86 cm each, plus existing vertical spacing. The superseded coverage
and signed-deviation power presentation assets were removed after their values
were verified against the retained full reporting CSVs. Complete multi-quantile
power results remain in `table_power_full.csv`, `appendix_power.csv`, and
`appendix_power.tex`.

Figure 1 is anchored after the coverage introduction; Figure 2 follows the
median-power introduction. Both allow top/bottom placement. Appendix C.1
now follows the coverage-audit summary table and the full-domain acceptance
introduction in Appendix C. Appendix A and the main text cross-reference this diagnostic. Short captions and
separate notes use the existing template environments.

## Verification

The integrated PDF was visually checked at reading size for panel assignments,
all quantile labels, ordering, colour scales, annotations, marker clipping,
legend, captions/notes, and float placement. Fonts are embedded in all three
PDFs. The document compiles with resolved references/citations and no overfull
boxes. Existing underfull-box diagnostics remain; R/Perl also report the
environment's unsupported C.UTF-8 locale and fall back to the system locale.
The temporary candidate gallery was removed after these checks. Validation,
regeneration and a forced thesis rebuild then succeeded without that directory.
Subsequent appendix revisions relocate the approved heatmap to Figure C.1
without regenerating or modifying its asset. Page numbers follow LaTeX's
automatic placement; see `APPENDIX_REPORTING.md` for the current structure.
