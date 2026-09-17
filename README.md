# DML-IVQR under Weak Instruments — Master’s Thesis

This master’s thesis extends the Chen et al. simulation design to investigate how weaker instrument relevance affects double machine learning for instrumental variable quantile regression (DML-IVQR). It evaluates estimation accuracy, confidence-set coverage, statistical power, and confidence-set informativeness across instrument-strength settings, quantiles, and sample sizes.

The repository brings together the manuscript, preserved source materials, extension code, saved simulation outputs, and supporting documentation.

| Location | Contents |
| --- | --- |
| [thesis/](thesis/) | LaTeX manuscript, bibliography, appendices, figures, tables, and compiled thesis PDF. |
| [Empirical_work/](Empirical_work/), [simulation/](simulation/), [example/](example/) | Preserved original authors’ empirical, simulation, and example materials. |
| [thesis_extension/src/](thesis_extension/src/), [config/](thesis_extension/config/) | Extension implementation and simulation settings. |
| [thesis_extension/final/output/n500/](thesis_extension/final/output/n500/), [n1000/](thesis_extension/final/output/n1000/) | Saved main simulation results for both sample sizes. |
| [thesis_extension/calibration/](thesis_extension/calibration/), [diagnostics/](thesis_extension/diagnostics/) | Instrument-strength calibration, grid-domain diagnostics, and coverage audit. |
| [thesis_extension/reporting/](thesis_extension/reporting/) | Reporting scripts and supplementary results. |
| [thesis_extension/environment/](thesis_extension/environment/) | Historical R environment and dependency records. |
| [docs/](docs/) | Reproducibility and supporting documentation. |

The original authors’ repository is [https://github.com/FieldTien/DML-IVQR](https://github.com/FieldTien/DML-IVQR). Their materials are preserved in the three directories identified above; this thesis’s implementation, calibration, diagnostics, and reporting extensions reside in `thesis_extension/`, with the manuscript in `thesis/`.

Read the [thesis PDF](thesis/main.pdf) for the analysis. The preserved simulation workflow uses Windows R 3.4.3. Consult the [environment setup guide](thesis_extension/environment/SETUP_SECOND_LAPTOP.md) and [reproducibility notes](docs/REPRODUCIBILITY_NOTES.md) for setup, execution, dependency records, and reproducibility limitations across systems.

See [LICENSE](LICENSE) for the terms and scope applicable to original contributions; preserved third-party materials retain their respective terms.
