# G1 — Complete repository inventory and publication cleanup audit

Date: 12 November 2026 (Asia/Tashkent). Audited branch: journal-validation. HEAD: dc2a6bb33df15f8c01b1282332273b2944f2ad9f.
**Final classification: PARTIAL.** All accessible current files were inventoried, hashed and assigned a disposition; all reachable historical blob identities/sizes were enumerated. Historical content/privacy and dynamic research dependency closure are not exhaustively verified. This is an audit-completeness limit, not permission to remove evidence.

Only this report and the four requested CSVs were created. Existing material was not edited, moved, deleted, compiled or executed. No estimator, simulation, numerical validation, commit, push or repository creation was performed. Snapshot excludes the five new audit deliverables themselves.

## 1. Executive assessment

Recommend **Option B: prepare a separate journal-specific repository in a later authorized stage**, preserving this repository and explicit thesis/external-code provenance. Current code and evidence depend extensively on paths containing thesis; these are scientifically essential, not disposable. Retain relative paths initially or test all path rewrites in a separately authorized migration. The selected public package is not yet a verified portable reproduction environment.

The corrected PDF is the distinct 34-page build at journal_validation/publication_review/lssp_canonical_build/manuscript_canonical_corrected.pdf. The earlier named historical PDF is also 34 pages; page count alone cannot identify the version. The cancelled optimization is 29 pages plus a separate supplement and must remain archival.


Key findings:

- R020–R023 are present, tracked and readable on the public journal-validation branch; anonymous-review packaging is separate.
- Stage 2F code and saved-output paths are absent from the current tree although later cited validation code imports them. Historical source exists at 50412fe7; saved-output recoverability is unverified.
- Existing evidence manifests: 3,154 SHA256 matches, two differences needing review, zero missing entries. All 124 grid records match.
- No credential-pattern matches were found in the bounded current text scan; this is not a historical/binary secret-free certification.

## 2. Repository size and inventory

Working tree: **83,184 files / 10,917,039,682 bytes**. Physical .git: **382 files / 3,886,533,338 bytes**.
Reachable history: **14 commits, 54,177 unique blobs, 6,736,627,665 uncompressed blob bytes** (unique-object total, not checkout size). No git fetch was performed. A later read-only connected GitHub API check confirmed public visibility and both remote branch tips; historical enumeration remains limited to local reachable refs.

### Top-level directory counts and sizes

| Directory | Files | Bytes |
|---|---|---|
| journal_validation | 75611 | 10210269494 |
| thesis_extension | 3062 | 522096917 |
| journal_article | 4309 | 169310152 |
| simulation | 24 | 4045691 |
| docs | 33 | 3763590 |
| thesis | 61 | 3033903 |
| Empirical_work | 73 | 2436070 |
| example | 7 | 2078564 |
| [root] | 3 | 5261 |
| .vscode | 1 | 40 |

### Git status

| Status | Files | Bytes |
|---|---|---|
| ignored | 71982 | 9733955446 |
| tracked | 11202 | 1183084236 |

### File type counts and sizes

| Extension | Files | Bytes |
|---|---|---|
| .rds | 3960 | 4727796288 |
| .bin | 49565 | 3525949616 |
| .json | 14946 | 1673634267 |
| .npz | 1492 | 336358876 |
| .csv | 1649 | 331906717 |
| .dll | 181 | 63865906 |
| .png | 388 | 43296766 |
| .zip | 33 | 36829112 |
| .pm | 2143 | 35095359 |
| .dat | 3 | 26001426 |
| .pdf | 71 | 21833608 |
| .fmt | 1 | 10226889 |
| .pl | 1420 | 9796448 |
| .html | 1110 | 8072660 |
| .c | 8 | 7903617 |
| .rdb | 77 | 7590724 |
| .h | 398 | 6679046 |
| .gz | 10 | 4419622 |
| .txt | 2002 | 4357405 |
| .log | 2326 | 3363615 |
| [none] | 271 | 2695931 |
| .map | 10 | 2428943 |
| .rdata | 9 | 2346345 |
| .cache-7 | 11 | 1778368 |
| .tex | 185 | 1634397 |
| .md | 95 | 1248927 |
| .r | 268 | 1122883 |
| .bcf | 9 | 1090179 |
| .fndb-5 | 3 | 1077248 |
| .7 | 1 | 1048697 |
| .3 | 1 | 1048671 |
| .5 | 1 | 1048650 |
| .9 | 1 | 1048646 |
| .8 | 1 | 1048630 |
| .2 | 1 | 1048611 |
| .1 | 1 | 1048606 |
| .6 | 1 | 1048593 |
| .4 | 1 | 1048589 |
| .10 | 1 | 1048582 |
| .py | 98 | 642613 |
| .rra | 1 | 560196 |
| .rmd | 28 | 501804 |
| .sav | 1 | 401937 |
| .diff | 4 | 393418 |
| .rnw | 13 | 303865 |
| .out | 11 | 273254 |
| .xml | 10 | 270793 |
| .bib | 10 | 243097 |
| .cpp | 64 | 239157 |
| .aaa | 2 | 235520 |
| .pem | 1 | 222971 |
| .bbl | 8 | 215440 |
| .aux | 10 | 175037 |
| .fls | 2 | 160738 |
| .m | 1 | 148317 |
| .jsonl | 2 | 148316 |
| .rng | 2 | 127489 |
| .rd | 13 | 122225 |
| .rda | 11 | 119651 |
| .rdx | 77 | 84155 |
| .exe | 1 | 78848 |
| .conf | 4 | 73942 |
| .xsl | 1 | 64944 |
| .al | 75 | 55171 |
| .types | 1 | 49815 |
| .rnc | 2 | 48887 |
| .css | 36 | 48677 |
| .fdb_latexmk | 1 | 46066 |
| .deb | 2 | 32408 |
| .xst | 1 | 23880 |
| .blg | 7 | 10051 |
| .pc | 2 | 10009 |
| .sh | 8 | 4178 |
| .hpp | 3 | 3712 |
| .toc | 1 | 3704 |
| .rua | 1 | 3455 |
| .ix | 3 | 1841 |
| .ps1 | 2 | 1240 |
| .ini | 2 | 391 |
| .js | 1 | 247 |
| .bat | 1 | 228 |
| .yml | 1 | 225 |
| .tag | 1 | 204 |
| .yaml | 1 | 103 |
| .lock | 1 | 0 |
| .bs | 2 | 0 |


Every individual directory can be grouped from the CSV directory field. Git internals are metadata-only and separate from working files. Tracked-but-missing paths: 0; current inventory read errors: 0. No AGENTS.md was found by initial repository search or tracked-path search.

SHA256 computed by streaming all accessible current files; no binary was dumped. **6,352 duplicate content groups**, 19,158 additional identical copies. duplicate_of is a content relationship, never automatic deletion authorization. Canonical inputs and essential evidence remain KEEP_PUBLIC even when duplicated. SHA256 byte differences can include line-ending differences.

### Largest current files

| Path | Bytes | Status |
|---|---|---|
| thesis_extension/final/output/n1000/profiles.csv | 70297487 | tracked |
| thesis_extension/final/output/n500/profiles.csv | 68975248 | tracked |
| thesis_extension/diagnostics/grid_sensitivity/output/stage2/combined_profiles_-5_7.csv | 30793233 | ignored |
| thesis_extension/environment/legacy_R343_library/stringi/libs/icudt55l.dat | 25908416 | tracked |
| thesis_extension/diagnostics/grid_sensitivity/output/stage1/stage1_profiles.csv | 20611776 | ignored |
| thesis_extension/final/output/n1000/power.csv | 15422615 | tracked |
| thesis_extension/final/output/n500/power.csv | 15302540 | tracked |
| thesis_extension/environment/package_archives_R343/stringi_1.1.6.zip | 14452067 | tracked |
| journal_validation/stage2h/pilot/SHA256_MANIFEST.json | 12397404 | ignored |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/SHA256_MANIFEST_BEFORE_REPORT_INTERPRETATION.json | 12396213 | ignored |
| journal_article/qa/batch4/runtime/data/miktex/data/le/pdftex/pdflatex.fmt | 10226889 | ignored |
| thesis_extension/diagnostics/grid_sensitivity/output/stage2/stage2_tail_profiles.csv | 10181521 | ignored |
| journal_article/qa/batch4/runtime/inc/lib/auto/share/dist/DBD-SQLite/sqlite3.c | 7898916 | ignored |
| thesis_extension/final/output/n1000/results.csv | 6319843 | tracked |
| thesis_extension/final/output/n500/results.csv | 6209864 | tracked |
| journal_article/qa/batch4/runtime/inc/lib/auto/Encode/HanExtra/HanExtra.xs.dll | 5784576 | ignored |
| thesis_extension/environment/legacy_R343_library/stringi/libs/i386/stringi.dll | 4695054 | tracked |
| journal_validation/stage2b/output/controlled_20261022_01/weighted_orthogonality.csv | 4671791 | ignored |
| thesis_extension/environment/package_archives_R343/Rcpp_0.12.14.zip | 4381112 | tracked |
| thesis_extension/environment/legacy_R343_library/stringi/libs/x64/stringi.dll | 4289536 | tracked |

### Largest reachable historical blobs

| Historical path association | Bytes | Git object |
|---|---|---|
| thesis_extension/final/output/n1000/profiles.csv | 69067486 | 026e34989f64385191012ef819a928e0d70ac0fc |
| thesis_extension/final/output/n500/profiles.csv | 67745247 | e78b772a6e6ad71e619b2a38b9e50e4c4a12bcc3 |
| thesis_extension/environment/legacy_R343_library/stringi/libs/icudt55l.dat | 25908416 | 75ddabe1f37528244aa078505ec608e78db3a720 |
| thesis_extension/final/output/n1000/power.csv | 15242614 | 60ad49aaa4adacc5e3ff0b2070528202b5935dac |
| thesis_extension/final/output/n500/power.csv | 15122539 | 8a48f0d499e0f852682d09ed211399680a8ebe83 |
| thesis_extension/environment/package_archives_R343/stringi_1.1.6.zip | 14452067 | 842e45ae38d38c0c92c11a49cb3ac7781b0320d9 |
| journal_validation/stage2h/pilot/SHA256_MANIFEST.json | 12156107 | f71a9961d514157707991b3ef7a84567b3c611af |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/SHA256_MANIFEST_BEFORE_REPORT_INTERPRETATION.json | 12154944 | b28d3e21b99cf5b77cdb68b235bc9848173160bf |
| thesis_extension/final/output/n1000/results.csv | 6289842 | b09369b1a1ad00bf3fb9e34fbb72d053bdd8dd29 |
| thesis_extension/final/output/n500/results.csv | 6179863 | 6cb12111c444e7af8b433af4a5371a4923810cee |
| thesis_extension/environment/legacy_R343_library/stringi/libs/i386/stringi.dll | 4695054 | 3b6ed14af5001edaf9461efd0a71b8de00348f85 |
| thesis_extension/environment/package_archives_R343/Rcpp_0.12.14.zip | 4381112 | 0d5932b4af6353b5d8f4f183d9110dd4ffce4a6d |
| thesis_extension/environment/legacy_R343_library/stringi/libs/x64/stringi.dll | 4289536 | bbf40daf2d5ee62359fb3339feda80480ccdfe50 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/protected_before.json | 3144460 | 3450eb2189a634b158e312dc661c5105f3bc896b |
| thesis_extension/environment/package_archives_R343/ggplot2_2.2.1.zip | 3050133 | d02ba446baec8e980f6a7d44356965551612ee77 |
| journal_validation/stage2h/readiness/results/protected_after.json | 2876851 | e66af53c1daab5dbc172886c215e925de3e9096d |
| journal_validation/stage2g/deterministic_implementation/results/protected_after.json | 2679345 | 6e1d4ab8531a74c50d5b86d1a073db1ba8122bcf |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r08_t90_k010_c0_B/outcome_certificate.json | 2524324 | 0687a58530e93b799d7cc27091fb6003a1966bd5 |
| journal_validation/stage2g/end_to_end_certification/results/protected_after.json | 2515510 | 8043593fff9aa4bd2cca658bcdf204ebaa52fe4f |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r08_t90_k010_c0_A/outcome_certificate.json | 2483764 | a51e225b97914c998443093c6435d15d2d2a1f9f |

Historical object paths from rev-list are one representative association per unique blob, not a full path-by-commit Cartesian inventory. The CSV manuscript map includes historical source/PDF/Word/Markdown blob variants with object IDs; historical titles/page counts and last path-specific commits are deliberately unclaimed where not decoded.

## 3. Master's thesis remnants

The root README explicitly presents a master's thesis, links thesis/main.pdf and identifies original authors' material. The repository name DML-IVQR_Master_Thesis and thesis/thesis_extension directory names preserve that identity. Do not erase its academic origin; replace public presentation later with a concise provenance statement and retain the original archive.

thesis/main.tex contains Bonn examination formatting (lines 74/78), UBonn corporate colors (125–130), university title-page text (333/422), supervisor/instructor fields (370), and declaration/examination-office wording (1224–1231). docs/university_template contains the original university template and SOURCE.md with upstream commit attribution. Those presentation files belong in the private historical archive unless publication of a separately licensed historical thesis is expressly intended. Supervisor and examination details require privacy review; their existence is not evidence they should appear in the article.

Do not exclude thesis/tools, thesis_extension/src, final outputs, calibration, domain diagnostics, coverage audit or reporting assets because of their names. The current journal reuses these scientific components. Appendix derivations/domain/coverage content has a current scientific role; thesis-specific declaration/title-page macros do not.

Bounded text scans found thesis/Bonn markers in **17 files**; exact paths and marker types are in REPOSITORY_FILE_INVENTORY.csv. Text scans exclude files over 4 MiB and binary/Word/PDF body content; PDF metadata was inspected for manuscript candidates. No claim of complete binary-body personal-information detection is made.

## 4. Manuscript version map and exact current dependency tree

MANUSCRIPT_VERSION_MAP.csv has 346 rows: all candidate current source/PDF/Word/Markdown components selected by document location/name plus reachable historical manuscript blob variants. Current rows record Git status, filesystem mtime, latest discovered path commit across local refs, metadata title/page count where available, role and classification. A component is not an independently titled article. last_commit is a path event and can be a rename/deletion, not a claim that every byte was authored then.

The user-designated master is journal_article/main.tex with approved M1–M3/E1–E3 corrections. Its build report is historical evidence, not proof of current Git status: it described then-uncommitted changes; this audit began with a clean current tree.

### Recursive local build graph

| Parent | Dependency kind | Resolved path |
|---|---|---|
| journal_article/main.tex | input | journal_article/preamble.tex |
| journal_article/preamble.tex | addbibresource | journal_article/references.bib |
| journal_article/main.tex | input | journal_article/sections/01_introduction.tex |
| journal_article/main.tex | input | journal_article/sections/02_framework.tex |
| journal_article/main.tex | input | journal_article/sections/03_design.tex |
| journal_article/main.tex | input | journal_article/sections/04_results.tex |
| journal_article/sections/04_results.tex | input | journal_article/tables/table_strength_calibration.tex |
| journal_article/sections/04_results.tex | input | journal_article/tables/table_main_performance.tex |
| journal_article/sections/04_results.tex | input | journal_article/tables/figure_coverage_main.tex |
| journal_article/tables/figure_coverage_main.tex | includegraphics | journal_article/figures/generated/coverage_heatmap.pdf |
| journal_article/sections/04_results.tex | input | journal_article/tables/figure_power_main.tex |
| journal_article/tables/figure_power_main.tex | includegraphics | journal_article/figures/generated/power_median_combined.pdf |
| journal_article/sections/04_results.tex | input | journal_article/tables/figure_accepted_measure_main.tex |
| journal_article/tables/figure_accepted_measure_main.tex | includegraphics | journal_article/figures/generated/accepted_measure_n500.png |
| journal_article/tables/figure_accepted_measure_main.tex | includegraphics | journal_article/figures/generated/accepted_measure_n1000.png |
| journal_article/main.tex | input | journal_article/sections/05_discussion.tex |
| journal_article/main.tex | input | journal_article/sections/06_conclusion.tex |
| journal_article/main.tex | input | journal_article/sections/submission_declarations.tex |
| journal_article/main.tex | input | journal_article/sections/data_availability.tex |
| journal_article/main.tex | input | journal_article/supplementary/A_numerical_domain.tex |
| journal_article/supplementary/A_numerical_domain.tex | input | journal_article/tables/generated/appendix_grid_diagnostic.tex |
| journal_article/supplementary/A_numerical_domain.tex | input | journal_article/tables/generated/figure_grid_domain.tex |
| journal_article/tables/generated/figure_grid_domain.tex | includegraphics | journal_article/figures/grid_domain_expansion.png |
| journal_article/main.tex | input | journal_article/supplementary/B_kappa_derivation.tex |
| journal_article/supplementary/B_kappa_derivation.tex | input | journal_article/tables/appendix_kappa_illustration.tex |
| journal_article/main.tex | input | journal_article/supplementary/C_coverage_audit.tex |
| journal_article/supplementary/C_coverage_audit.tex | input | journal_article/tables/appendix_coverage_audit_summary.tex |
| journal_article/supplementary/C_coverage_audit.tex | input | journal_article/tables/figure_full_domain_acceptance.tex |
| journal_article/tables/figure_full_domain_acceptance.tex | includegraphics | journal_article/figures/generated/full_domain_acceptance_heatmap.pdf |
| journal_article/main.tex | input | journal_article/supplementary/D_implementation.tex |
| journal_article/supplementary/D_implementation.tex | input | journal_article/supplementary/D_evidence_map.tex |

Static closure: **32 files**, missing local dependencies: **0** (none).
TeX package/runtime inputs are additional: journal_article/preamble.tex defines them, and the corrected build .fls recorder records actual installed TeX inputs, including private machine paths. Preserve portable package names/version records rather than publishing machine paths. The graph covers static input/include/graphics/bibliography directives; no new build was run. Existing canonical build QA source_manifest.json, verification.json and .fls provide the previously captured runtime recorder evidence.

### Corrected and historical PDF identification

| Path | Pages | SHA256 | Classification |
|---|---|---|---|
| journal_article/submission/named/manuscript_named.pdf |  | 4fecad9e125211689910104b8b533cb5e03f1d96e24752dc58bb62b5e77e3388 | ARCHIVE_PRIVATE |
| journal_article/submission/review/manuscript_review.pdf |  | bc8ef361d7d46546412735d40ba2b4203876569c041fe24081fd8cee42ea7645 | ARCHIVE_PRIVATE |
| journal_validation/publication_review/lssp_canonical_build/manuscript_canonical_corrected.pdf |  | 4e9800270d35afd6332abe109bae7eb6fce4a0d8bdb24cbebef30370fc088e7b | KEEP_ACTIVE |
| journal_validation/publication_review/lssp_optimization/manuscript_optimized.pdf |  | e67fec34b55995677e5cc8cdbde1349c6b59fbc8523eca6ebdfbb8b3c9f11fc9 | ARCHIVE_PRIVATE |
| thesis/main.pdf |  | 76bc297de822633bb3c9450027ac7c9e678407122c01a63b2f0c9f5c78624437 | ARCHIVE_PRIVATE |


KEEP_ACTIVE applies to the exact canonical source closure and corrected PDF. ARCHIVE_PRIVATE applies to prior submission snapshots, older PDFs, thesis sources and cancelled optimization. Other reports/inactive sources are REVIEW_MANUALLY, rather than presumed redundant. Generated intermediary exclusion applies in the disposition register; archival provenance must still be retained.

## 5. Research code dependency map

RESEARCH_DEPENDENCY_MAP.csv has 3,398 records, combining semantic E1–E6 evidence chains, all canonical include edges and static imports/literal references for project R/Python files.
A = published-result machinery; B = supporting numerical diagnostics; C = historical/experimental; D = development/document utilities; E = upstream/external software. Static source rows classify project roles conservatively; no runtime execution or complete dynamic import tracing is claimed.

| Component | Source / generator | Role and downstream evidence |
|---|---|---|
| Controlled relevance DGP | thesis_extension/src/dgp_kappa.R | A: controlled signal scaling and compensating noise; main and calibration |
| Oracle / Full GMM | thesis_extension/src/author_oracle_wrapper.R; author_full_wrapper.R | A: quantreg fits, instrument projections, g/W and candidate profiles |
| DML-IVQR and quantile Lasso | thesis_extension/src/author_bc_dml_wrapper.R | A/E: lambda_BC_author, quantreg::rq lasso, hdm::rlasso residualization; snow/foreach candidates |
| Inference and metrics | thesis_extension/src/run_extension.R; metrics.R | A: direct truth evaluation distinct from grid set; power candidates and summaries |
| Main MC | thesis_extension/final/run_final.R; config/extension_config.R | A: n=500/1000, R=500, 5 quantiles, 4 kappa, 41 grid points; frozen final/output |
| Strength calibration | thesis_extension/calibration/instrument_strength_100rep/run_strength_calibration.R | A: 100-rep primary descriptive strength summary; legacy pilot distinct |
| Grid diagnostics | thesis_extension/diagnostics/grid_sensitivity/ | B: grid config/functions, stage1/stage2 summaries, local raw profiles/primitives |
| Coverage diagnostics | thesis_extension/diagnostics/coverage_audit/ | B: saved forensic audit of main-run direct-truth statistics |
| Reporting and graphics | thesis_extension/reporting/build_thesis_results.R; thesis/tools/build_appendix_tables.py; build_thesis_figures.R; build_selected_figures.R | A: frozen inputs to full tables and compact journal displays |
| Selected numerical sensitivity | journal_validation/stage2c/stability/; stage2g/deterministic_implementation/; stage2g/full_path_validation/ | B: R020–R023, selected-case decision sensitivity, not replacement MC |
| Other validation stages | journal_validation/stage2a, stage2b, stage2e, stage2g, stage2h | B/C: retain stage reports/contracts, classify exploratory scope separately |
| Original empirical/examples | Empirical_work/; simulation/; example/ | E/C: external author provenance and historical workflows; not automatically article dependencies |
| Publication QA/build scripts | journal_article/qa/; submission/; publication_review/ | D: document utilities, snapshots and audit provenance |

Runtime guard requires Windows R 3.4.3 and historical library precedence. Important pinned versions are quantreg 5.34, hdm 0.2.0, hqreg 1.4, mvtnorm 1.0-6 and doSNOW 1.0.16, plus transitive packages in environment manifests. This does not prove portable installation or exact penalty-stream replay. Python stage-specific solver versions and complete transitive dynamic closure remain for manual environment review. Do not claim a lockfile/container exists without inspecting one.

## 6. Numerical evidence coverage

### Canonical cited files and selected-case records

| Evidence path | Current availability | Bytes |
|---|---|---|
| journal_article/figures/generated/accepted_measure_n1000.png | tracked | 223965 |
| journal_article/figures/generated/accepted_measure_n500.png | tracked | 218907 |
| journal_article/figures/generated/coverage_heatmap.pdf | tracked | 45274 |
| journal_article/figures/generated/full_domain_acceptance_heatmap.pdf | tracked | 42103 |
| journal_article/figures/generated/power_median_combined.pdf | tracked | 29145 |
| journal_article/figures/generated/rmse_n1000.png | tracked | 184927 |
| journal_article/figures/generated/rmse_n500.png | tracked | 189246 |
| journal_article/figures/grid_domain_expansion.png | tracked | 19560 |
| journal_article/tables/generated/appendix_coverage.tex | tracked | 11000 |
| journal_article/tables/generated/appendix_cr_informativeness.tex | tracked | 19654 |
| journal_article/tables/generated/appendix_grid_diagnostic.tex | tracked | 20950 |
| journal_article/tables/generated/appendix_point_performance.tex | tracked | 7522 |
| journal_article/tables/generated/appendix_power.tex | tracked | 49248 |
| journal_article/tables/table_main_performance.tex | tracked | 3384 |
| journal_article/tables/table_strength_calibration.tex | tracked | 1001 |
| journal_validation/stage2c/stability/STABILITY_REPORT.md | tracked | 15878 |
| journal_validation/stage2g/deterministic_implementation/DETERMINISTIC_IMPLEMENTATION_REPORT.md | tracked | 21524 |
| journal_validation/stage2g/deterministic_implementation/IMPLEMENTATION_CONTRACT_v1.md | tracked | 4961 |
| journal_validation/stage2g/full_path_validation/FULL_PATH_REPORT.md | tracked | 19181 |
| thesis_extension/calibration/instrument_strength_100rep/kappa_strength_summary.csv | tracked | 2355 |
| thesis_extension/diagnostics/grid_sensitivity/GRID_RESULTS_MANIFEST.csv | tracked | 24664 |
| thesis_extension/diagnostics/grid_sensitivity/GRID_RESULTS_PROVENANCE.md | tracked | 2151 |
| thesis_extension/diagnostics/grid_sensitivity/output/stage1/stage1_expansion_summary.csv | tracked | 6195 |
| thesis_extension/diagnostics/grid_sensitivity/output/stage1/stage1_summary.csv | tracked | 11480 |
| thesis_extension/diagnostics/grid_sensitivity/output/stage2/stage2_expansion_summary.csv | tracked | 8565 |
| thesis_extension/diagnostics/grid_sensitivity/output/stage2/stage2_summary.csv | tracked | 17152 |
| thesis_extension/final/output/n1000/power.csv | tracked | 15422615 |
| thesis_extension/final/output/n1000/power_summary.csv | tracked | 19508 |
| thesis_extension/final/output/n1000/profiles.csv | tracked | 70297487 |
| thesis_extension/final/output/n1000/results.csv | tracked | 6319843 |
| thesis_extension/final/output/n1000/summary.csv | tracked | 11513 |
| thesis_extension/final/output/n500/power.csv | tracked | 15302540 |
| thesis_extension/final/output/n500/power_summary.csv | tracked | 19314 |
| thesis_extension/final/output/n500/profiles.csv | tracked | 68975248 |
| thesis_extension/final/output/n500/results.csv | tracked | 6209864 |
| thesis_extension/final/output/n500/summary.csv | tracked | 11421 |
| thesis_extension/reporting/EMPIRICAL_RESULTS_MANIFEST.csv | tracked | 575278 |
| thesis_extension/reporting/REPORTING_OUTPUT_MANIFEST.csv | tracked | 5787 |
| thesis_extension/reporting/output/table_cr_informativeness_full.csv | tracked | 25589 |
| thesis_extension/reporting/output/table_grid_domain_diagnostic.csv | tracked | 11262 |


R020–R023 availability here is distinct from anonymous reviewer access. Prior SUBMISSION_GATE_REPORT.md states those reports were absent from inspected reviewer ZIPs. This audit checks the repository files, not portal access and not a new anonymous package.

Main frozen summary/results/profiles/power files support E2–E4; primary 100-rep calibration supports E1. E5 domain expansion summaries and manifest are separate 100-rep diagnostics. Existing provenance records one Stage 1 singular-design failure and no new Stage 2 errors; these statements were read, not recomputed. The reported abstract contrast is a selection across distinct acceptance/measure/power summaries, not a joint event.

EMPIRICAL_RESULTS_FREEZE.md records ac9a9ccad027cde05488abb633e66cc02f87cc46. Local object resolution in this audit: **UNRESOLVED**. Preserve the identifier as historical provenance; do not relabel it a verified checkout. The canonical availability statement instead cites the checked evidence revision 15b8b4dc95e3658f3b858a6f792ea2983299aaa6. A read-only GitHub metadata check on 12 November 2026 confirmed public visibility and branch tips. R020–R023 were readable through the connected GitHub tool; anonymous reviewer-package access was not established.

Large grid profiles and primitives are local/ignored and must not be reconstructed. All local files are indexed by current Git status; public tracked summaries do not imply full stochastic replay. The main run's worker penalty RNG states are not recovered by the parent seed alone.

Stage 2A–2H is not one completed inferential certification. Physical top-level directories include stage2a, stage2b, stage2c, stage2e, stage2g and stage2h; stage2d/stage2f top-level directories were not found. Related work may be embedded in later stage subprojects; no missing stage is invented. All files appear in the inventory and static source map.

Stage 2H pilot is explicitly incomplete and later exploratory work, not the manuscript's frozen MC. Existing report records 1,064 PASS, 5 TIME_LIMIT_UNRESOLVED, 371 RESOURCE_NOT_EXECUTED, with four repeatability fits not executed. Preserve unexecuted IDs, overrides, failed-attempt logs and bounds; do not infer completed-design coverage from selected qualified observations. The ignored runs and manifest are private/local evidence, not disposable debug output.

## 7. Third-party and license findings

Root LICENSE is MIT only for original software/documentation contributions; it explicitly excludes the thesis manuscript, original authors' Empirical_work/simulation/example materials, bundled R packages, reference documents and university templates. Journal manuscript rights are not automatically resolved by this scope note. Author must decide manuscript/supplement/result licensing and verify all upstream redistribution terms.

Original-author repository attribution is present in README.md (FieldTien/DML-IVQR). University template SOURCE.md records HolgerGerhardt/ThesisTemplates and an upstream commit. Retain those attribution records in the original archive and retain any required notices for migrated components. Template presentation itself need not enter the journal package.

Vendored historical R library contains package-specific licenses, compiled binaries and documentation; package presence does not establish redistribution compliance or modern platform portability. Prefer a reviewed manifest plus permitted source archives rather than copying installed Windows libraries blindly. Modified wrapper code retains external-method/source provenance and needs explicit third-party notices. There is no tracked .gitmodules found; gitlink inspection is reported below.

Gitlinks: 0.

## 8. Git history and privacy risks

Configured origin repository identity: https://github.com/U-Olim/DML-IVQR_Master_Thesis.git. Public visibility was checked through the connected GitHub tool on 12 November 2026 (private=false, visibility=public). Default branch is main; remote journal-validation tip dc2a6bb33df15f8c01b1282332273b2944f2ad9f and main tip 90509cbd8ed093f90554e417756f0d1913a29ed3 match local remote-tracking refs.

Branches/ref tips:
| Ref | Commit |
|---|---|
| refs/codex/turn-diffs/captures/1794461090695/cc0422f7-c2b4-4197-be09-b5c086de46ce/base | 20d03564705b1a2425d3403ffcaf6ab75f869a10 |
| refs/codex/turn-diffs/checkpoints/15126ac9a4a639fff3718fc0c4e64adc/37f2274a6e65b7b219c973112b83adfe/1794399754612/6996fa83-6d64-43aa-9e3a-66daa41ea4dc | 20d03564705b1a2425d3403ffcaf6ab75f869a10 |
| refs/codex/turn-diffs/checkpoints/7afd82538a62bd4f2ea04edfa9bd4909/95a9f64f4bbfe0ee00dc05adb8843652/1794307418199/749bbd11-c718-468e-896b-4a5fec207abb | b9229ad08fba3bf1817dc15c6795891abf130cd4 |
| refs/codex/turn-diffs/checkpoints/bc53372d5a522ceac54696c1a3a7040e/e3bf897b32a4cfdf44cc9a138c31c353/1794226500907/b1ab13dd-06a5-4e20-9806-d508dde737e2 | 2b6cc2e89b644e5355eee9e2bd799010091a967a |
| refs/codex/turn-diffs/checkpoints/cfe1aea31348e0ff9cbf53084c8f6fae/499b9e6fbcb0f0d4845a57a1e336f24e/1793874781672/867a595c-9d8d-4716-b9cc-2a934b867d96 | 47262ccc7e58c598c12dc5c943b9dd780025a6de |
| refs/heads/backup/journal-validation-before-push-fix-20261109 | cd19462f07a272572fd52248644f750c725aba10 |
| refs/heads/journal-validation | dc2a6bb33df15f8c01b1282332273b2944f2ad9f |
| refs/heads/main | 90509cbd8ed093f90554e417756f0d1913a29ed3 |
| refs/remotes/origin/HEAD | 90509cbd8ed093f90554e417756f0d1913a29ed3 |
| refs/remotes/origin/journal-validation | dc2a6bb33df15f8c01b1282332273b2944f2ad9f |
| refs/remotes/origin/main | 90509cbd8ed093f90554e417756f0d1913a29ed3 |

History includes the backup branch and local remote-tracking refs. Cleaning HEAD preserves Bonn template/thesis presentation, old PDFs, external code and large artifacts in reachable history. Current Git object count report:

\`\`\`text
count: 323
size: 13226
in-pack: 57632
packs: 4
size-pack: 3780207
prune-packable: 0
garbage: 0
size-garbage: 0
\`\`\`

Bounded current text scan flagged **209 files** with email, absolute user paths or credential-like patterns. The inventory stores only flag types and paths, never matching secret values. Emails in author metadata or upstream attribution can be intentional public scholarly information; do not silently strip attribution or contact details. .vscode settings, environment/session logs, .fls/QA logs and archived documents need privacy review before new publication.

Credential-pattern matches: **0 files**. A pattern match is not proof of a working credential. No claim that history/binary bodies are secret-free is justified. Git config, commit-author emails and other Git internals were not dumped into the deliverables. Historical blob contents, unreachable objects/reflogs and remote-only history were not exhaustively scanned; deleting current files cannot cure prior exposure.

### Flagged current paths (types only)

| Path | Flag types |
|---|---|
| docs/university_template/Template_BA-MA-Thesis_Term-Paper_ORIGINAL.tex | email |
| journal_article/EDIT_REPORT.md | email |
| journal_article/main.log | absolute_private_path |
| journal_article/main.tex | email |
| journal_article/qa/article_text.txt | email |
| journal_article/qa/final_build.log | absolute_private_path |
| journal_article/qa/revise_article.py | email |
| journal_article/qa/verify_revision.py | email |
| journal_article/qa/batch4/article_text.txt | email |
| journal_article/qa/batch4/article_text_utf8.txt | email |
| journal_article/qa/batch4/attempt1_biber.txt | absolute_private_path |
| journal_article/qa/batch4/attempt1_latex1.txt | absolute_private_path |
| journal_article/qa/batch4/attempt1_latex2.txt | absolute_private_path |
| journal_article/qa/batch4/attempt1_latex3.txt | absolute_private_path |
| journal_article/qa/batch4/attempt1_main.log | absolute_private_path |
| journal_article/qa/batch4/attempt2_biber.txt | absolute_private_path |
| journal_article/qa/batch4/attempt2_latex1.txt | absolute_private_path |
| journal_article/qa/batch4/attempt2_latex2.txt | absolute_private_path |
| journal_article/qa/batch4/attempt2_latex3.txt | absolute_private_path |
| journal_article/qa/batch4/attempt2_main.log | absolute_private_path |
| journal_article/qa/batch4/biber.txt | absolute_private_path |
| journal_article/qa/batch4/latex1.txt | absolute_private_path |
| journal_article/qa/batch4/latex2.txt | absolute_private_path |
| journal_article/qa/batch4/latex3.txt | absolute_private_path |
| journal_article/qa/batch4/main.log | absolute_private_path |
| journal_article/qa/batch4/runtime/miktexstartup.ini | absolute_private_path |
| journal_article/qa/batch4/runtime/data/miktex/log/biber.log | absolute_private_path |
| journal_article/qa/batch4/runtime/data/miktex/log/kpsewhich.log | absolute_private_path |
| journal_article/qa/batch4/runtime/data/miktex/log/miktex-fc-cache.log | absolute_private_path |
| journal_article/qa/batch4/runtime/data/miktex/log/miktex-makefmt.log | absolute_private_path |
| journal_article/qa/batch4/runtime/data/miktex/log/miktex-pdftex.log | absolute_private_path |
| journal_article/qa/batch4/runtime/data/miktex/log/miktex.log | absolute_private_path |
| journal_article/qa/batch4/runtime/data/miktex/log/pdfdetach.log | absolute_private_path |
| journal_article/qa/batch4/runtime/data/miktex/log/pdfinfo.log | absolute_private_path |
| journal_article/qa/batch4/runtime/data/miktex/log/pdflatex.log | absolute_private_path |
| journal_article/qa/batch4/runtime/data/miktex/log/pdftoppm.log | absolute_private_path |
| journal_article/qa/batch4/runtime/data/miktex/log/pdftotext.log | absolute_private_path |
| journal_article/qa/batch4/runtime/data/miktex/log/makefmt/pdflatex/2026-11-10-14-16-23.log | absolute_private_path |
| journal_article/qa/batch4/runtime/data/miktex/log/makefmt/pdflatex/2026-11-10-14-17-13.log | absolute_private_path |
| journal_article/qa/batch4/runtime/data/miktex/log/makefmt/pdflatex/2026-11-10-14-19-51.log | absolute_private_path |
| journal_article/qa/batch4/runtime/data/miktex/log/makefmt/pdflatex/2026-11-10-14-23-40.log | absolute_private_path |
| journal_article/qa/batch4/runtime/data/miktex/log/makefmt/pdflatex/2026-11-10-14-58-39.log | absolute_private_path |
| journal_article/qa/batch4/runtime/data/miktex/log/makefmt/pdflatex/2026-11-10-14-59-38.log | absolute_private_path |
| journal_article/qa/batch4/runtime/data/miktex/log/makefmt/pdflatex/2026-11-10-15-00-22.log | absolute_private_path |
| journal_article/qa/batch4/runtime/data/miktex/log/makefmt/pdflatex/2026-11-10-15-01-12.log | absolute_private_path |
| journal_article/qa/batch4/runtime/data/miktex/log/makefmt/pdflatex/2026-11-10-15-02-02.log | absolute_private_path |
| journal_article/qa/batch4/runtime/data/miktex/log/makefmt/pdflatex/2026-11-10-15-02-51.log | absolute_private_path |
| journal_article/qa/batch4/runtime/data/miktex/log/makefmt/pdflatex/2026-11-10-15-03-33.log | absolute_private_path |
| journal_article/qa/batch4/runtime/data/miktex/log/makefmt/pdflatex/2026-11-11-17-01-13.log | absolute_private_path |
| journal_article/qa/batch4/runtime/data/miktex/log/makefmt/pdflatex/2026-11-11-17-01-52.log | absolute_private_path |
| journal_article/qa/batch4/runtime/data/miktex/log/makefmt/pdflatex/2026-11-11-17-02-31.log | absolute_private_path |
| journal_article/qa/batch4/runtime/data/miktex/log/makefmt/pdflatex/2026-11-11-17-03-09.log | absolute_private_path |
| journal_article/qa/batch4/runtime/data/miktex/log/makefmt/pdflatex/2026-11-11-17-16-44.log | absolute_private_path |
| journal_article/qa/batch4/runtime/data/miktex/log/makefmt/pdflatex/2026-11-11-17-17-24.log | absolute_private_path |
| journal_article/submission/qa/named_biber.txt | absolute_private_path |
| journal_article/submission/qa/named_latex1.txt | absolute_private_path |
| journal_article/submission/qa/named_latex2.txt | absolute_private_path |
| journal_article/submission/qa/named_latex3.txt | absolute_private_path |
| journal_article/submission/qa/review_biber.txt | absolute_private_path |
| journal_article/submission/qa/review_latex1.txt | absolute_private_path |
| journal_article/submission/qa/review_latex2.txt | absolute_private_path |
| journal_article/submission/qa/review_latex3.txt | absolute_private_path |
| journal_article/submission/qa/tables_latex1.txt | absolute_private_path |
| journal_article/submission/qa/tables_latex2.txt | absolute_private_path |
| journal_article/submission/qa/named/text.txt | email |
| journal_article/submission/qa/named/urls.txt | email |
| journal_article/submission/work/named_build/main.log | absolute_private_path |
| journal_article/submission/work/named_source/main.tex | email |
| journal_article/submission/work/review_build/main.log | absolute_private_path |
| journal_article/submission/work/tables_build/supplementary_tables.log | absolute_private_path |
| journal_validation/publication_review/BATCH1_CHANGE_REPORT.md | email,absolute_private_path |
| journal_validation/publication_review/BATCH2_CHANGE_REPORT.md | email |
| journal_validation/publication_review/BATCH4_CHANGE_REPORT.md | email,absolute_private_path |
| journal_validation/publication_review/FINAL_PACKAGE_REPORT.md | email |
| journal_validation/publication_review/FINAL_SUBMISSION_CHECKLIST.md | email |
| journal_validation/publication_review/lssp_canonical_build/build/main.fls | absolute_private_path |
| journal_validation/publication_review/lssp_canonical_build/build/main.log | absolute_private_path |
| journal_validation/publication_review/lssp_canonical_build/qa/biber.txt | absolute_private_path |
| journal_validation/publication_review/lssp_canonical_build/qa/latex1.txt | absolute_private_path |
| journal_validation/publication_review/lssp_canonical_build/qa/latex2.txt | absolute_private_path |
| journal_validation/publication_review/lssp_canonical_build/qa/latex3.txt | absolute_private_path |
| journal_validation/publication_review/lssp_canonical_build/qa/text.txt | email |
| journal_validation/publication_review/lssp_canonical_build/source/main.tex | email |
| journal_validation/publication_review/lssp_optimization/CONTENT_ITEM_MAP.json | email |
| journal_validation/publication_review/lssp_optimization/build/main/main.log | absolute_private_path |
| journal_validation/publication_review/lssp_optimization/build/technical_supplement/technical_supplement.log | absolute_private_path |
| journal_validation/publication_review/lssp_optimization/qa/main_biber.txt | absolute_private_path |
| journal_validation/publication_review/lssp_optimization/qa/main_latex1.txt | absolute_private_path |
| journal_validation/publication_review/lssp_optimization/qa/main_latex2.txt | absolute_private_path |
| journal_validation/publication_review/lssp_optimization/qa/main_latex3.txt | absolute_private_path |
| journal_validation/publication_review/lssp_optimization/qa/optimized_text.txt | email |
| journal_validation/publication_review/lssp_optimization/qa/original_text.txt | email |
| journal_validation/publication_review/lssp_optimization/qa/technical_supplement_latex1.txt | absolute_private_path |
| journal_validation/publication_review/lssp_optimization/qa/technical_supplement_latex2.txt | absolute_private_path |
| journal_validation/publication_review/lssp_optimization/qa/technical_supplement_latex3.txt | absolute_private_path |
| journal_validation/publication_review/lssp_optimization/source/main.tex | email |
| journal_validation/stage2a/output/controlled_20261022_01/ab_master.log | absolute_private_path |
| journal_validation/stage2a/output/controlled_20261022_01/ab_workers.log | absolute_private_path |
| journal_validation/stage2a/output/controlled_20261022_01/packages.csv | absolute_private_path |
| journal_validation/stage2a/output/controlled_20261022_01/pilot_master.log | absolute_private_path |
| journal_validation/stage2a/output/controlled_20261022_01/pilot_sample_manifest.csv | absolute_private_path |
| journal_validation/stage2a/output/controlled_20261022_01/pilot_workers.log | absolute_private_path |
| journal_validation/stage2a/output/controlled_20261022_01/sample_manifest.csv | absolute_private_path |
| journal_validation/stage2a/output/controlled_20261022_01/validate_master.log | absolute_private_path |
| journal_validation/stage2b/output/controlled_20261022_01/contrasts_master.log | absolute_private_path |
| journal_validation/stage2b/output/controlled_20261022_01/contrasts_workers.log | absolute_private_path |
| journal_validation/stage2b/output/controlled_20261022_01/packages.csv | absolute_private_path |
| journal_validation/stage2b/output/controlled_20261022_01/primary_master.log | absolute_private_path |
| journal_validation/stage2b/output/controlled_20261022_01/primary_workers.log | absolute_private_path |
| journal_validation/stage2b/output/controlled_20261022_01/review_2.log | absolute_private_path |
| journal_validation/stage2b/output/controlled_20261022_01/sample_stream_manifest.csv | absolute_private_path |
| journal_validation/stage2b/output/controlled_20261022_01/validate_master.log | absolute_private_path |
| journal_validation/stage2c/config.json | absolute_private_path |
| journal_validation/stage2c/STAGE2C_REPORT.md | absolute_private_path |
| journal_validation/stage2c/certification/CERTIFICATION_REPORT.md | absolute_private_path |
| journal_validation/stage2c/output/controlled_20261029_01/config.json | absolute_private_path |
| journal_validation/stage2c/output/controlled_20261029_01/pilot_001.log | absolute_private_path |
| journal_validation/stage2c/output/controlled_20261029_01/pilot_002.log | absolute_private_path |
| journal_validation/stage2c/output/controlled_20261029_01/pilot_003.log | absolute_private_path |
| journal_validation/stage2c/output/controlled_20261029_01/pilot_004.log | absolute_private_path |
| journal_validation/stage2c/output/controlled_20261029_01/pilot_005.log | absolute_private_path |
| journal_validation/stage2c/output/controlled_20261029_01/pilot_006.log | absolute_private_path |
| journal_validation/stage2c/output/controlled_20261029_01/pilot_007.log | absolute_private_path |
| journal_validation/stage2c/output/controlled_20261029_01/pilot_008.log | absolute_private_path |
| journal_validation/stage2c/output/controlled_20261029_01/pilot_009.log | absolute_private_path |
| journal_validation/stage2c/output/controlled_20261029_01/pilot_010.log | absolute_private_path |
| journal_validation/stage2c/output/controlled_20261029_01/pilot_011.log | absolute_private_path |
| journal_validation/stage2c/output/controlled_20261029_01/pilot_012.log | absolute_private_path |
| journal_validation/stage2c/output/controlled_20261029_01/pilot_013.log | absolute_private_path |
| journal_validation/stage2c/output/controlled_20261029_01/pilot_014.log | absolute_private_path |
| journal_validation/stage2c/output/controlled_20261029_01/pilot_015.log | absolute_private_path |
| journal_validation/stage2c/output/controlled_20261029_01/pilot_016.log | absolute_private_path |
| journal_validation/stage2c/output/controlled_20261029_01/pilot_017.log | absolute_private_path |
| journal_validation/stage2c/output/controlled_20261029_01/pilot_018.log | absolute_private_path |
| journal_validation/stage2c/output/controlled_20261029_01/pilot_019.log | absolute_private_path |
| journal_validation/stage2c/output/controlled_20261029_01/pilot_020.log | absolute_private_path |
| journal_validation/stage2c/output/controlled_20261029_01/pilot_021.log | absolute_private_path |
| journal_validation/stage2c/output/controlled_20261029_01/validation_001.log | absolute_private_path |
| journal_validation/stage2c/output/controlled_20261029_01/validation_002.log | absolute_private_path |
| journal_validation/stage2e/output/paired_20261029T093009Z/evaluate.log | absolute_private_path |
| journal_validation/stage2e/output/paired_20261029T093009Z/prepare.log | absolute_private_path |
| journal_validation/stage2e/output/paired_20261029T093009Z/R_packages.csv | absolute_private_path |
| journal_validation/stage2g/validate.py | email |
| journal_validation/stage2g/deterministic_implementation/instrument_v1.py | email |
| journal_validation/stage2g/deterministic_implementation/outcome_v1.py | email |
| journal_validation/stage2g/deterministic_implementation/results/environment.json | absolute_private_path |
| journal_validation/stage2g/deterministic_implementation/results/verify_dimension_shadowing_failure.log | absolute_private_path |
| journal_validation/stage2g/full_path_validation/audit.py | email |
| journal_validation/stage2h/pilot/candidate_h0.py | email |
| journal_validation/stage2h/pilot/finish_reporting.py | email |
| journal_validation/stage2h/pilot/INTERRUPTION_README.md | absolute_private_path |
| journal_validation/stage2h/pilot/LATEST_RUN.txt | absolute_private_path |
| journal_validation/stage2h/pilot/README.md | absolute_private_path |
| journal_validation/stage2h/pilot/RESOURCE_STOP_README.md | absolute_private_path |
| journal_validation/stage2h/pilot/run_pilot.py | absolute_private_path |
| journal_validation/stage2h/pilot/summarize_pilot.py | email |
| journal_validation/stage2h/pilot/summarize_pilot_v2.py | email |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/time_limit_numerical_validation.csv | absolute_private_path |
| journal_validation/stage2h/readiness/candidate_h0.py | email |
| journal_validation/stage2h/readiness/summarize_readiness.py | email |
| thesis/main.fls | absolute_private_path |
| thesis/main.log | absolute_private_path |
| thesis_extension/diagnostics/grid_sensitivity/SMOKE_TEST_REPORT.txt | absolute_private_path |
| thesis_extension/diagnostics/grid_sensitivity/output/stage1/stage1_manifest.txt | absolute_private_path |
| thesis_extension/diagnostics/grid_sensitivity/output/stage2/stage2_manifest.txt | absolute_private_path |
| thesis_extension/environment/AUTHOR_R343_ENVIRONMENT_REPORT.md | absolute_private_path |
| thesis_extension/environment/installed_packages_R343.csv | absolute_private_path |
| thesis_extension/environment/package_versions_R343.txt | absolute_private_path |
| thesis_extension/environment/SETUP_SECOND_LAPTOP.md | absolute_private_path |
| thesis_extension/environment/legacy_R343_library/backports/DESCRIPTION | email |
| thesis_extension/environment/legacy_R343_library/checkmate/DESCRIPTION | email |
| thesis_extension/environment/legacy_R343_library/colorspace/DESCRIPTION | email |
| thesis_extension/environment/legacy_R343_library/dichromat/DESCRIPTION | email |
| thesis_extension/environment/legacy_R343_library/digest/DESCRIPTION | email |
| thesis_extension/environment/legacy_R343_library/doSNOW/DESCRIPTION | email,absolute_private_path |
| thesis_extension/environment/legacy_R343_library/foreach/DESCRIPTION | email |
| thesis_extension/environment/legacy_R343_library/Formula/DESCRIPTION | email |
| thesis_extension/environment/legacy_R343_library/ggplot2/DESCRIPTION | email |
| thesis_extension/environment/legacy_R343_library/glmnet/DESCRIPTION | email |
| thesis_extension/environment/legacy_R343_library/gtable/DESCRIPTION | email |
| thesis_extension/environment/legacy_R343_library/hdm/DESCRIPTION | email |
| thesis_extension/environment/legacy_R343_library/hqreg/DESCRIPTION | email,absolute_private_path |
| thesis_extension/environment/legacy_R343_library/iterators/DESCRIPTION | email |
| thesis_extension/environment/legacy_R343_library/labeling/DESCRIPTION | email |
| thesis_extension/environment/legacy_R343_library/lazyeval/DESCRIPTION | email |
| thesis_extension/environment/legacy_R343_library/magrittr/DESCRIPTION | email |
| thesis_extension/environment/legacy_R343_library/MatrixModels/DESCRIPTION | email |
| thesis_extension/environment/legacy_R343_library/munsell/DESCRIPTION | email |
| thesis_extension/environment/legacy_R343_library/mvtnorm/DESCRIPTION | email |
| thesis_extension/environment/legacy_R343_library/mvtnorm/C_API_Example/DESCRIPTION | email |
| thesis_extension/environment/legacy_R343_library/plyr/DESCRIPTION | email |
| thesis_extension/environment/legacy_R343_library/quantreg/DESCRIPTION | email,absolute_private_path |
| thesis_extension/environment/legacy_R343_library/R6/DESCRIPTION | email |
| thesis_extension/environment/legacy_R343_library/RColorBrewer/DESCRIPTION | email |
| thesis_extension/environment/legacy_R343_library/Rcpp/DESCRIPTION | email |
| thesis_extension/environment/legacy_R343_library/Rcpp/unitTests/runit.Rcpp.package.skeleton.R | email |
| thesis_extension/environment/legacy_R343_library/Rcpp/unitTests/testRcppClass/DESCRIPTION | email |
| thesis_extension/environment/legacy_R343_library/Rcpp/unitTests/testRcppModule/DESCRIPTION | email |
| thesis_extension/environment/legacy_R343_library/Rcpp/unitTests/testRcppPackage/DESCRIPTION | email |
| thesis_extension/environment/legacy_R343_library/reshape2/DESCRIPTION | email |

Additional flagged paths are in the complete inventory.

## 9. Option A versus Option B

| Criterion | A: reorganize existing history | B: selected journal repository |
|---|---|---|
| Transparency | Full thesis chronology and attribution retained by default | Keep thesis archive/reference and explicit derivation/provenance; document selected source commit/hashes |
| History/privacy | Old names, documents and large objects remain reachable; HEAD cleanup insufficient | Selected reviewed files reduce accidental disclosure; original repository remains historically exposed |
| Maintenance | One repository, but mixed workflows and historical branches remain | Clear article scope, but two archives require cross-links and stable version mapping |
| Reproducibility | Existing relative paths work; full history includes irrelevant/binary runtime baggage | Can keep selected paths initially; moving paths risks broken source/config/reporting links |
| Size/distribution | Large clone and generated artifacts retained | Compact verified package with separate licensed environment and large evidence deposits |
| Risk | History rewriting would be disruptive and is not authorized | Omission of essential evidence/attribution is the main risk; prevent with claim map and hashes |


Recommendation: B after author decisions and complete publication-manifest review. Do not rewrite history or create a new repository at this stage. Option A is viable if retaining the existing historical exposure and size is intentional. Neither option resolves a missing freeze commit, unrecoverable random streams or unestablished inference validity.

## 10. Proposed public directory structure

\`\`\`text
README.md
LICENSE
THIRD_PARTY_NOTICES.md
CITATION.cff
PROVENANCE.md
manuscript/               # one canonical main.tex tree, references, required tables/figures
supplement/              # explicit supplementary source; keep inline until deliberate split
src/                     # dgp, estimators, metrics, runner
config/                  # main and diagnostic settings
results/main/n500/
results/main/n1000/
results/calibration/
results/reporting/
diagnostics/grid/
diagnostics/coverage/
diagnostics/numerical/   # R020–R023 and verified required companions
scripts/reporting/
environment/             # version records, reviewed dependency sources/setup
reproduce/README.md
reproduce/CLAIM_EVIDENCE_MAP.csv
reproduce/FILE_MANIFEST.csv
DATA_CODE_AVAILABILITY.md
\`\`\`

A minimal source tree still includes every canonical build dependency and full cited machine-readable results. Generated final scientific tables/figures and corrected PDF are useful reproducibility evidence, unlike transient TeX logs/cache. Stable E1–E6 and R020–R023 identifiers must survive all path changes. Keep the complete thesis/validation archive outside the minimal publication package without disguising provenance.

## 11. Exact cleanup and migration plan — proposals only

1. Preserve this original repository, current HEAD and backup branch; archive current audit CSVs and hash manifest. No destructive cleanup is needed for preparation.
2. Resolve the author decisions below and finish privacy/rights review; choose the proposed publication scope. Historical privacy review requires bounded blob content inspection beyond this stage's completed metadata enumeration.
3. Build a reviewed allowlist from PUBLIC_PACKAGE_DISPOSITION.csv. KEEP_PUBLIC is a candidate set, not a certification that every path is ready to upload. THIRD_PARTY_REVIEW, SENSITIVE_REVIEW and NEEDS_AUTHOR_DECISION block automatic copying. KEEP_PRIVATE_ARCHIVE retains material; EXCLUDE_GENERATED and DUPLICATE mean exclusion from the future public package, never deletion here.
4. Copy, in a separately authorized stage, selected files to a staging package with SHA256/source-commit mappings; preserve byte-identical evidence and original manifests. Do not replace frozen statistics with later numerical work.
5. Apply the exact source-prefix mapping below; retain an old-path/new-path manifest. Update all source(), read/write, LaTeX, configuration, README and evidence-map paths together. Per-file proposed_destination values are preliminary buckets; this table is the intended final layout.
6. Verify package completeness from static imports and canonical recorder; include reviewed licenses and environment records. Preserve selected-case reports and all companions needed to inspect their claims. Decide separate deposit/private preservation of large local grid evidence and incomplete pilot records.
7. Later validation may compile the selected manuscript and verify deterministic reporting against existing hashes, under a separate authorization. No full MC replay is implied or required by this audit; replay limitations must remain explicit.
8. Only after review, create/publish a journal repository if authorized. Cross-link the thesis provenance/archive, record source HEAD and manifest, and avoid ambiguous final/latest/version2 directories. Do not automatically copy Git internals, old submission ZIPs or private pilot runs.

| Existing path/prefix | Proposed path | Condition |
|---|---|---|
| journal_article/main.tex, preamble.tex, sections/, supplementary/, references.bib | manuscript/ (same relative tree) | retain full approved canonical content; no automatic supplementary split |
| journal_article/tables/ and figures/ canonical closure | manuscript/tables/ and manuscript/figures/ | keep exact dependencies, plus cited full tables |
| publication_review/lssp_canonical_build/manuscript_canonical_corrected.pdf | manuscript/manuscript.pdf | copy corrected PDF only; verify inventory SHA256 |
| thesis_extension/src/ | src/ | update source paths; retain external attribution |
| thesis_extension/config/ | config/ | retain frozen main settings |
| thesis_extension/final/run_final.R | scripts/run_main.R | update runner paths only in future authorized migration |
| thesis_extension/final/output/n500/ and n1000/ | results/main/n500/ and n1000/ | preserve all archived main evidence |
| thesis_extension/calibration/instrument_strength_100rep/ | results/calibration/ + scripts/calibration/ | separate code/results; retain calibration provenance |
| thesis_extension/reporting/output/ | results/reporting/ | preserve full machine-readable results |
| thesis_extension/reporting/ scripts and thesis/tools/ generators | scripts/reporting/ | keep scripts still generating selected article assets |
| thesis_extension/diagnostics/grid_sensitivity/ | diagnostics/grid/ | track summaries/provenance; explicit decision for ignored profiles/primitives |
| thesis_extension/diagnostics/coverage_audit/ | diagnostics/coverage/ | retain saved reports, generator and required records |
| R020–R023 paths listed in section 6 | diagnostics/numerical/R020/ through R023/ | retain IDs and map shared R021/R022 directory without duplicate code ambiguity |
| thesis_extension/environment/ | environment/ | review archives/licensing/privacy; installed library not copied by default |
| thesis/main.tex, old thesis/submission PDFs, docs/university_template/ | private historical archive | preserve thesis origin and required notices |
| journal_validation/stage2h/pilot/runs/ and later unrelated exploration | private exploratory archive | preserve incomplete statuses and contracts; no article-result substitution |


## 12. Unresolved author decisions and inspection limits

- Confirm separate publication repository identity, history/archive availability and an honest thesis-origin statement.
- Confirm manuscript/supplement/result licenses, upstream-code permissions and package archive redistribution.
- Approve public author contact details; review private paths and sensitive-pattern flags before copying.
- Decide verified reviewer/public access for R020–R023 and supporting inputs/contracts; current file existence is not reviewer access.
- Decide preservation/deposit of ignored grid profiles/primitives and incomplete Stage 2H local records, with manifest/status qualifications.
- Resolve or explicitly retain the unresolved historical freeze identifier; never reconstruct missing results or invent a release.
- Complete exact dynamic research/solver environment closure and historical privacy/content inspection if claiming an exhaustive publication clearance.
- Manuscript titles/page counts are obtained from current text/PDF metadata where possible; historical binary bodies and Word bodies were not decoded, and no article version equivalence is inferred from filenames.
- Historical scope is all locally reachable refs; no Git fetch, unreachable-object scan or Git history rewrite occurred.
- Files above 4 MiB were hashed/inventoried but not text-scanned; binary bodies were not generally searched. This bounds credential/thesis-remnant detection.
- Read/traversal failures: none recorded. Symlink targets were not intentionally followed by directory traversal. Git internals were inventoried by metadata only.

The four CSVs are proposals and evidence indexes, not authorization to delete any file. **PARTIAL** is the appropriate final classification because complete historical-content/privacy and dynamic dependency verification remain unresolved.

## Additional inspected dependency and stage findings

| Stage | Record | Scope / status |
|---|---|---|
| 2A | journal_validation/stage2a/STAGE2A_REPORT.md | Completed diagnostic experiments; penalty randomness and density-proxy sensitivity; no calibration validity established. |
| 2B | journal_validation/stage2b/STAGE2B_REPORT.md | Known-nuisance and projection diagnostics; benchmark changes are not feasible-estimator coverage. |
| 2C | journal_validation/stage2c/STAGE2C_REPORT.md | Stopped after replication 21 failed prespecified gate; only 20 fully validated replications; 22–40 not executed. |
| 2C-S / R020 | journal_validation/stage2c/stability/STABILITY_REPORT.md | Saved perturbation/rank-stability analysis; Stage 2C remains stopped. |
| 2D | journal_validation/stage2d/ | No current directory or path-specific all-ref history found; stage label alone is not evidence of a missing experiment. |
| 2E | journal_validation/stage2e/STAGE2E_REPORT.md | 24 fixed paired candidate comparisons; classifications A=21 B=2 C=1; no population certification. |
| 2F | journal_validation/stage2f/STAGE2F_REPORT.md | Absent current tree, available historically at 50412fe7; unique-optimum/tied-rank analysis for two disagreements. |
| 2G | journal_validation/stage2g/STAGE2G_REPORT.md | 24-candidate exact-outcome policy panel; downstream dynamic dependencies include missing Stage 2F code. |
| 2G-D / R021–R022 | journal_validation/stage2g/deterministic_implementation/DETERMINISTIC_IMPLEMENTATION_REPORT.md | Deterministic implementation/contract: SciPy HiGHS IPM plus exact rational verification; configuration CONFIG_v1.json. |
| 2G-F / R023 | journal_validation/stage2g/full_path_validation/FULL_PATH_REPORT.md | 72 selected full paths / 24 baseline candidates; fixed-export conditional decision bounds; five A/C decision differences. |
| 2H readiness | journal_validation/stage2h/readiness/READINESS_REPORT.md | Readiness/derivation evidence distinct from later incomplete pilot. |
| 2H pilot | journal_validation/stage2h/pilot/STAGE2H_REPORT.md | Resource-stopped incomplete bounded-DGP paired pilot; not the published main Monte Carlo. |

**Concrete missing supporting dependency:** journal_validation/stage2f/analyze.py and verify.py are imported by stage2g/validate.py, stage2g/verify.py, deterministic_implementation/common_v1.py and verify_v1.py, and full_path_validation/common.py. Saved Stage 2F output/exact_face_20261029T102755Z is referenced by stage2g/validate.py and full_path_validation/prepare.py. These current-tree dependencies are absent, not merely ignored. Historical source and STAGE2F_REPORT.md can be inspected at commit 50412fe7 (and its appropriate tree); path deletion events appear in cd19462f and 2ceec58a across local refs. No historical file was restored. Presence of historical source does not prove the ignored Stage 2F output directory is recoverable: inspect its recorded manifests before claiming recovery.

This gap matters to E6 numerical-evidence replay, not to the presence of frozen main CSV summaries. Future selected-case packaging must include an explicitly verified historically sourced dependency bundle or disclose the replay limitation. Do not silently reconstruct missing saved results.

R021's contract specifically uses SciPy HiGHS IPM for proposed LP bases, NumPy/binary64 arrays, exact rational verification, R 3.4.3/hdm instrument pathways and saved frozen quantities; use its CONFIG_v1.json and environment/manifests rather than inferring modern defaults. All such code was read only.

**Licensing refinement:** environment/package_archives_R343 contains 39 archived packages (37,236,441 bytes). Treat these as THIRD_PARTY_REVIEW rather than automatically MIT-licensed original material. Their existence is separate from installed legacy_R343_library/ and from any absent cran-source/ directory.

### Per-directory file totals (working tree)

| Directory | Files | Bytes |
|---|---|---|
| thesis_extension/diagnostics/grid_sensitivity/output/stage1/primitives | 100 | 157663854 |
| journal_validation/stage2b/output/controlled_20261022_01/samples | 64 | 156491968 |
| journal_validation/stage2a/output/controlled_20261022_01/samples | 52 | 119816056 |
| thesis_extension/final/output/n1000 | 6 | 92071039 |
| thesis_extension/final/output/n500 | 6 | 90518460 |
| thesis_extension/diagnostics/grid_sensitivity/output/stage2 | 11 | 43044305 |
| thesis_extension/environment/package_archives_R343 | 39 | 37236441 |
| thesis_extension/environment/legacy_R343_library/stringi/libs | 2 | 25926649 |
| journal_validation/stage2a/output/controlled_20261022_01/details | 360 | 22584928 |
| thesis_extension/diagnostics/grid_sensitivity/output/stage1 | 13 | 22081915 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z | 41 | 19279235 |
| journal_article/qa/batch4/runtime | 151 | 17508542 |
| journal_validation/stage2b/output/controlled_20261022_01/details | 192 | 13351949 |
| journal_validation/stage2h/pilot | 32 | 12558596 |
| journal_article/qa/batch4/runtime/data/miktex/log | 21 | 11400665 |
| journal_article/qa/batch4/runtime/data/miktex/data/le/pdftex | 1 | 10226889 |
| journal_validation/stage2b/output/controlled_20261022_01 | 52 | 10105672 |
| journal_article/qa/batch4 | 78 | 10017627 |
| journal_article/qa/batch4/runtime/inc/lib/Date/Manip/TZ | 406 | 9725188 |
| journal_validation/stage2c/output/controlled_20261029_01/pilot_015 | 15 | 8878966 |
| journal_validation/stage2c/output/controlled_20261029_01/pilot_002 | 15 | 8878784 |
| journal_validation/stage2c/output/controlled_20261029_01/pilot_017 | 15 | 8878733 |
| journal_validation/stage2c/output/controlled_20261029_01/pilot_019 | 15 | 8878717 |
| journal_validation/stage2c/output/controlled_20261029_01/pilot_011 | 15 | 8878685 |
| journal_validation/stage2c/output/controlled_20261029_01/pilot_018 | 15 | 8878667 |
| journal_validation/stage2c/output/controlled_20261029_01/pilot_013 | 15 | 8878661 |
| journal_validation/stage2c/output/controlled_20261029_01/pilot_009 | 15 | 8878613 |
| journal_validation/stage2c/output/controlled_20261029_01/validation_001 | 15 | 8878530 |
| journal_validation/stage2c/output/controlled_20261029_01/pilot_008 | 15 | 8878458 |
| journal_validation/stage2c/output/controlled_20261029_01/pilot_020 | 15 | 8878453 |
| journal_validation/stage2c/output/controlled_20261029_01/pilot_004 | 15 | 8878310 |
| journal_validation/stage2c/output/controlled_20261029_01/pilot_005 | 15 | 8878246 |
| journal_validation/stage2c/output/controlled_20261029_01/pilot_016 | 15 | 8878198 |
| journal_validation/stage2c/output/controlled_20261029_01/pilot_010 | 15 | 8878114 |
| journal_validation/stage2c/output/controlled_20261029_01/validation_002 | 15 | 8878111 |
| journal_validation/stage2c/output/controlled_20261029_01/pilot_007 | 15 | 8878096 |
| journal_validation/stage2c/output/controlled_20261029_01/pilot_012 | 15 | 8878047 |
| journal_validation/stage2c/output/controlled_20261029_01/pilot_006 | 15 | 8877966 |
| journal_validation/stage2c/output/controlled_20261029_01/pilot_014 | 15 | 8877882 |
| journal_validation/stage2c/output/controlled_20261029_01/pilot_003 | 15 | 8877795 |
| journal_validation/stage2c/output/controlled_20261029_01/pilot_001 | 15 | 8876543 |
| journal_validation/stage2c/output/controlled_20261029_01/pilot_021 | 14 | 8876257 |
| journal_article/qa/batch4/runtime/inc/lib/auto/share/dist/DBD-SQLite | 3 | 8494474 |
| journal_validation/stage2c/stability/saved_stability_20261029T084737Z | 30 | 7426401 |
| journal_validation/stage2g/deterministic_implementation/results/pilot_014_minus | 45 | 6733264 |
| journal_validation/stage2g/deterministic_implementation/results/pilot_014_truth | 45 | 6635487 |
| journal_validation/stage2g/deterministic_implementation/results/pilot_003_minus | 44 | 6615428 |
| journal_validation/stage2g/deterministic_implementation/results/pilot_003_truth | 44 | 6557726 |
| journal_validation/stage2g/deterministic_implementation/results/pilot_004_plus | 45 | 6539187 |
| journal_validation/stage2g/deterministic_implementation/results/pilot_005_plus | 45 | 6533065 |
| journal_validation/stage2g/deterministic_implementation/results/pilot_006_plus | 44 | 6515616 |
| journal_validation/stage2g/deterministic_implementation/results/pilot_004_truth | 45 | 6460110 |
| journal_validation/stage2g/deterministic_implementation/results/pilot_006_truth | 44 | 6389241 |
| journal_validation/stage2g/deterministic_implementation/results/pilot_002_plus | 45 | 6357883 |
| journal_validation/stage2g/deterministic_implementation/results/pilot_001_truth | 45 | 6352925 |
| journal_article/submission/qa/named | 46 | 6308231 |
| journal_article/qa/batch4/runtime/inc/shlib/MSWin32-x64-multi-thread | 9 | 6282206 |
| journal_validation/stage2g/deterministic_implementation/results/pilot_007_minus | 44 | 6280276 |
| journal_validation/stage2g/deterministic_implementation/results/pilot_002_truth | 45 | 6230864 |
| journal_validation/stage2g/deterministic_implementation/results/pilot_007_truth | 44 | 6223180 |
| journal_validation/stage2g/deterministic_implementation/results/pilot_006_minus | 44 | 6175752 |
| journal_validation/stage2g/deterministic_implementation/results/pilot_002_minus | 45 | 6161139 |
| journal_validation/stage2g/deterministic_implementation/results/pilot_003_plus | 44 | 6141592 |
| journal_validation/stage2g/deterministic_implementation/results/pilot_004_minus | 45 | 6141443 |
| journal_validation/stage2g/deterministic_implementation/results/pilot_005_minus | 45 | 6119368 |
| journal_validation/stage2g/deterministic_implementation/results/pilot_014_plus | 45 | 6118975 |
| journal_validation/stage2g/deterministic_implementation/results/pilot_001_minus | 45 | 6090451 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r08_t90_k010_c0_B | 40 | 6089550 |
| journal_validation/stage2g/deterministic_implementation/results/pilot_005_truth | 45 | 6082636 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r08_t90_k010_c0_A | 40 | 6043617 |
| journal_article/submission/qa/review | 44 | 6028203 |
| journal_validation/stage2g/deterministic_implementation/results/pilot_007_plus | 44 | 6013018 |
| journal_validation/stage2g/deterministic_implementation/results/pilot_001_plus | 45 | 5982621 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r08_t90_k100_c1_A | 40 | 5858933 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r08_t90_k100_c0_B | 40 | 5840277 |
| journal_validation/stage2h/readiness/results | 21 | 5816423 |
| journal_article/qa/batch4/runtime/inc/lib/auto/Encode/HanExtra | 1 | 5784576 |
| journal_validation/publication_review/lssp_canonical_build/qa | 48 | 5777495 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r07_t50_k010_c0_A | 40 | 5728261 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r06_t90_k010_c0_A | 40 | 5704456 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r03_t90_k010_c2_A | 40 | 5702172 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r04_t90_k100_c1_B | 40 | 5675887 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r07_t50_k010_c1_B | 40 | 5675502 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r09_t90_k010_c0_A | 40 | 5672426 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r03_t90_k010_c1_B | 40 | 5645370 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r03_t90_k010_c2_B | 40 | 5632194 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r03_t90_k010_c1_A | 40 | 5630843 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r07_t50_k100_c1_B | 40 | 5612731 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r04_t90_k010_c0_B | 40 | 5591726 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r06_t90_k010_c1_A | 40 | 5567847 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r07_t50_k100_c1_A | 40 | 5564965 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r03_t90_k100_c1_B | 40 | 5562199 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r04_t90_k100_c2_B | 40 | 5560812 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r10_t90_k100_c0_A | 42 | 5555124 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r08_t90_k010_c1_B | 40 | 5552310 |
| journal_validation/stage2g/end_to_end_certification/results | 24 | 5547118 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r09_t50_k010_c0_A | 40 | 5541666 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r08_t90_k010_c1_A | 40 | 5540148 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r08_t90_k100_c1_B | 40 | 5527969 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r01_t50_k010_c0_B | 40 | 5524857 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r06_t90_k010_c0_B | 40 | 5520220 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r07_t90_k010_c0_B | 40 | 5517338 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r07_t50_k010_c2_B | 40 | 5516850 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r09_t90_k010_c1_A | 40 | 5510817 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r04_t50_k010_c0_A | 40 | 5510813 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r08_t50_k010_c0_B | 40 | 5507426 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r04_t90_k100_c0_A | 40 | 5494947 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r07_t50_k100_c0_A | 40 | 5492318 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r07_t50_k100_c0_B | 40 | 5492129 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r03_t90_k010_c0_B | 40 | 5486426 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r04_t90_k010_c0_A | 40 | 5483048 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r01_t90_k100_c2_A | 40 | 5476839 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r05_t90_k100_c2_A | 40 | 5471106 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r03_t90_k010_c0_A | 40 | 5471004 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r04_t90_k010_c1_A | 40 | 5465145 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r01_t50_k010_c0_A | 40 | 5460565 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r03_t50_k010_c0_B | 40 | 5458717 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r01_t90_k010_c2_A | 40 | 5455377 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r08_t90_k100_c0_A | 40 | 5454453 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r03_t90_k100_c1_A | 40 | 5453771 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r02_t90_k100_c2_A | 40 | 5452326 |
| journal_validation/stage2g/deterministic_implementation/results | 26 | 5451790 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r04_t90_k100_c1_A | 40 | 5451287 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r03_t90_k100_c0_A | 40 | 5446853 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r03_t90_k100_c0_B | 40 | 5445086 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r04_t50_k100_c0_B | 40 | 5443202 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r04_t10_k010_c0_B | 40 | 5437561 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r08_t90_k010_c2_A | 40 | 5434832 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r08_t90_k100_c2_B | 40 | 5423445 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r05_t90_k100_c1_A | 40 | 5423388 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r06_t50_k100_c0_B | 40 | 5421851 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r03_t90_k100_c2_B | 40 | 5419591 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r06_t90_k100_c2_A | 40 | 5403642 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r04_t50_k010_c1_B | 40 | 5403060 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r09_t90_k010_c1_B | 40 | 5402601 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r05_t90_k100_c1_B | 40 | 5400968 |
| journal_validation/stage2e/output/paired_20261029T093009Z/pilot_003_plus | 35 | 5400387 |
| journal_validation/stage2e/output/paired_20261029T093009Z/pilot_004_minus | 35 | 5396850 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r03_t50_k100_c2_B | 40 | 5393379 |
| journal_validation/stage2e/output/paired_20261029T093009Z/pilot_001_plus | 35 | 5393278 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r04_t90_k010_c1_B | 40 | 5393212 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r06_t90_k100_c0_A | 40 | 5390286 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r08_t50_k100_c2_B | 40 | 5388279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r09_t50_k100_c2_A | 40 | 5386948 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r08_t90_k010_c2_B | 40 | 5386130 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r07_t10_k100_c2_A | 40 | 5385154 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r01_t50_k100_c0_A | 40 | 5377061 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r09_t90_k010_c0_B | 40 | 5376499 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r04_t50_k100_c2_B | 40 | 5373732 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r03_t50_k100_c1_B | 40 | 5370784 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r05_t10_k100_c0_B | 40 | 5370596 |
| journal_validation/stage2e/output/paired_20261029T093009Z/pilot_007_minus | 35 | 5368079 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r08_t90_k100_c2_A | 40 | 5368062 |
| journal_validation/stage2e/output/paired_20261029T093009Z/pilot_005_minus | 35 | 5367718 |
| journal_validation/stage2e/output/paired_20261029T093009Z/pilot_002_plus | 35 | 5366496 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r02_t50_k100_c2_A | 40 | 5365427 |
| journal_validation/stage2e/output/paired_20261029T093009Z/pilot_007_plus | 35 | 5364660 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r04_t50_k010_c1_A | 40 | 5364168 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r07_t90_k010_c0_A | 40 | 5363502 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r03_t50_k010_c1_B | 40 | 5363431 |
| journal_validation/stage2e/output/paired_20261029T093009Z/pilot_006_minus | 35 | 5363183 |
| journal_validation/stage2e/output/paired_20261029T093009Z/pilot_003_minus | 35 | 5362908 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r05_t10_k010_c1_B | 40 | 5362239 |
| journal_validation/stage2e/output/paired_20261029T093009Z/pilot_014_minus | 35 | 5362131 |
| journal_validation/stage2e/output/paired_20261029T093009Z/pilot_005_plus | 35 | 5361529 |
| journal_validation/stage2e/output/paired_20261029T093009Z/pilot_014_plus | 35 | 5360858 |
| journal_validation/stage2e/output/paired_20261029T093009Z/pilot_004_plus | 35 | 5360790 |
| journal_validation/stage2e/output/paired_20261029T093009Z/pilot_002_minus | 35 | 5358302 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r07_t90_k010_c1_B | 40 | 5358175 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r01_t50_k100_c0_B | 40 | 5354564 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r04_t50_k010_c0_B | 40 | 5352753 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r09_t90_k010_c2_A | 40 | 5350795 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r05_t10_k100_c1_B | 40 | 5350620 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r04_t90_k100_c2_A | 40 | 5348756 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r04_t90_k100_c0_B | 40 | 5348022 |
| journal_validation/stage2h/readiness/results/sequential/n1000_t90_k010 | 40 | 5347257 |
| journal_validation/stage2h/readiness/results/parallel/n1000_t90_k010 | 40 | 5347255 |
| journal_validation/stage2h/readiness/results/repeat/n1000_t90_k010 | 40 | 5347246 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r04_t90_k010_c2_B | 40 | 5347244 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r07_t50_k010_c0_B | 40 | 5346929 |
| journal_validation/stage2e/output/paired_20261029T093009Z/pilot_006_plus | 35 | 5342368 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r09_t90_k100_c2_A | 40 | 5340926 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r06_t90_k010_c1_B | 40 | 5340736 |
| journal_validation/stage2e/output/paired_20261029T093009Z/pilot_001_minus | 35 | 5340517 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r02_t10_k100_c0_B | 40 | 5339008 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r07_t50_k010_c1_A | 40 | 5338918 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r08_t50_k100_c0_A | 40 | 5338773 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r02_t90_k100_c1_A | 40 | 5336515 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r07_t10_k100_c1_A | 40 | 5335575 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r02_t10_k010_c1_A | 40 | 5335441 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r02_t90_k010_c2_A | 40 | 5333213 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r02_t10_k100_c0_A | 40 | 5332741 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r04_t50_k100_c1_A | 40 | 5330294 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r02_t50_k100_c1_B | 40 | 5330002 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r04_t50_k100_c2_A | 40 | 5325089 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r05_t10_k010_c1_A | 40 | 5314928 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r05_t90_k010_c2_B | 40 | 5313528 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r06_t90_k010_c2_A | 40 | 5313128 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r01_t50_k010_c1_B | 40 | 5310531 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r08_t10_k010_c2_A | 40 | 5304368 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r05_t90_k010_c2_A | 40 | 5303088 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r01_t50_k010_c1_A | 40 | 5300240 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r08_t50_k100_c0_B | 40 | 5296463 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r03_t50_k010_c0_A | 40 | 5295951 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r07_t10_k010_c2_B | 40 | 5295203 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r02_t90_k010_c2_B | 40 | 5294707 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r09_t50_k010_c2_A | 40 | 5294075 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r06_t90_k100_c0_B | 40 | 5288733 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r08_t50_k010_c1_A | 40 | 5288175 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r02_t90_k100_c2_B | 40 | 5287446 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r09_t90_k100_c0_B | 40 | 5285463 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r07_t10_k100_c0_A | 40 | 5285030 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r10_t50_k100_c1_B | 40 | 5282291 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r02_t90_k010_c1_A | 40 | 5281928 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r09_t90_k100_c2_B | 40 | 5280933 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r09_t50_k010_c0_B | 40 | 5277664 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r09_t10_k010_c2_A | 40 | 5277225 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r09_t50_k010_c2_B | 40 | 5275604 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r01_t10_k010_c1_B | 40 | 5269469 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r04_t50_k100_c1_B | 40 | 5268507 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r03_t50_k100_c1_A | 40 | 5265435 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r01_t90_k010_c2_B | 40 | 5264964 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r01_t10_k100_c0_B | 40 | 5262439 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r06_t50_k010_c2_B | 40 | 5261342 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r04_t10_k100_c1_A | 40 | 5259293 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r06_t50_k100_c0_A | 40 | 5257948 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r09_t50_k100_c0_A | 40 | 5252749 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r06_t50_k010_c2_A | 40 | 5252472 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r06_t10_k100_c0_A | 40 | 5252256 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r06_t90_k010_c2_B | 40 | 5252066 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r07_t90_k010_c2_B | 40 | 5245459 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r04_t50_k010_c2_B | 40 | 5245212 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r01_t90_k100_c1_B | 40 | 5244816 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r07_t90_k010_c1_A | 40 | 5243215 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r06_t90_k100_c1_B | 40 | 5242118 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r07_t10_k010_c0_B | 40 | 5240693 |
| journal_validation/stage2h/readiness/results/sequential/n1000_t10_k100 | 40 | 5239759 |
| journal_validation/stage2h/readiness/results/parallel/n1000_t10_k100 | 40 | 5239754 |
| journal_validation/stage2h/readiness/results/repeat/n1000_t10_k100 | 40 | 5239754 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r09_t90_k100_c0_A | 40 | 5237305 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r02_t90_k010_c1_B | 40 | 5236133 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r05_t90_k010_c1_A | 40 | 5233728 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r06_t90_k100_c1_A | 40 | 5233502 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r08_t50_k010_c0_A | 40 | 5229644 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r08_t50_k100_c1_B | 40 | 5228354 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r09_t10_k010_c2_B | 40 | 5228103 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r07_t10_k100_c2_B | 40 | 5222908 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r04_t50_k100_c0_A | 40 | 5220698 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r07_t50_k100_c2_B | 40 | 5219074 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r02_t50_k100_c0_B | 40 | 5218880 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r09_t50_k010_c1_B | 40 | 5218838 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r07_t50_k100_c2_A | 40 | 5217798 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r01_t10_k010_c0_B | 40 | 5213733 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r09_t50_k010_c1_A | 40 | 5209487 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r06_t10_k010_c2_A | 40 | 5208585 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r08_t50_k010_c1_B | 40 | 5208270 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r05_t90_k100_c2_B | 40 | 5207087 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r01_t90_k100_c2_B | 40 | 5205165 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r08_t10_k010_c2_B | 40 | 5204492 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r09_t50_k100_c0_B | 40 | 5204057 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r04_t10_k010_c0_A | 40 | 5203426 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r05_t90_k010_c0_B | 40 | 5203310 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r05_t10_k010_c0_B | 40 | 5203177 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r04_t10_k100_c2_B | 40 | 5199141 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r02_t50_k100_c2_B | 40 | 5197141 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r01_t10_k100_c2_A | 40 | 5196728 |
| journal_validation/stage2h/readiness/results/sequential/n1000_t50_k010 | 40 | 5196441 |
| journal_validation/stage2h/readiness/results/parallel/n1000_t50_k010 | 40 | 5196439 |
| journal_validation/stage2h/readiness/results/repeat/n1000_t50_k010 | 40 | 5196435 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r08_t50_k010_c2_B | 40 | 5196238 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r01_t90_k010_c0_B | 40 | 5195710 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r03_t50_k010_c1_A | 40 | 5195670 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r07_t90_k100_c2_A | 40 | 5191899 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r04_t90_k010_c2_A | 40 | 5191849 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r01_t90_k010_c1_B | 40 | 5191648 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r07_t10_k100_c1_B | 40 | 5190030 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r07_t90_k100_c1_A | 40 | 5189117 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r07_t10_k010_c2_A | 40 | 5181235 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r07_t10_k010_c1_B | 40 | 5179432 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r02_t10_k100_c1_A | 40 | 5174522 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r05_t50_k100_c0_A | 40 | 5172531 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r02_t50_k100_c1_A | 40 | 5166306 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r02_t90_k100_c0_A | 40 | 5165787 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r08_t50_k100_c2_A | 40 | 5162640 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r08_t50_k100_c1_A | 40 | 5162443 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r02_t50_k010_c2_A | 40 | 5160567 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r02_t50_k010_c2_B | 40 | 5159535 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r10_t50_k100_c0_B | 40 | 5154962 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r03_t50_k010_c2_A | 40 | 5154527 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r01_t90_k010_c1_A | 40 | 5152952 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r05_t50_k010_c0_B | 40 | 5151796 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r05_t10_k010_c2_A | 40 | 5142864 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r08_t10_k100_c1_B | 40 | 5136284 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r05_t10_k100_c1_A | 40 | 5134804 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r08_t50_k010_c2_A | 40 | 5134468 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r04_t50_k010_c2_A | 40 | 5133674 |
| journal_validation/stage2h/readiness/results/parallel/n1000_t10_k010 | 40 | 5132265 |
| journal_validation/stage2h/readiness/results/sequential/n1000_t10_k010 | 40 | 5132263 |
| journal_validation/stage2h/readiness/results/repeat/n1000_t10_k010 | 40 | 5132259 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r05_t10_k100_c0_A | 40 | 5132247 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r07_t90_k100_c1_B | 40 | 5131183 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r07_t90_k100_c0_A | 40 | 5130440 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r06_t50_k100_c2_B | 40 | 5129268 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r04_t10_k100_c2_A | 40 | 5128993 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r06_t90_k100_c2_B | 40 | 5128140 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r05_t50_k010_c1_A | 40 | 5122460 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r08_t10_k100_c2_A | 40 | 5121336 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r02_t50_k100_c0_A | 40 | 5121319 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r01_t50_k100_c1_B | 40 | 5120964 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r02_t90_k010_c0_B | 40 | 5118759 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r10_t50_k010_c2_B | 42 | 5116331 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r02_t90_k100_c0_B | 40 | 5115767 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r09_t10_k010_c0_B | 40 | 5112409 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r09_t50_k100_c2_B | 40 | 5111146 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r10_t50_k010_c1_B | 40 | 5105087 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r04_t10_k010_c1_B | 40 | 5104756 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r10_t50_k010_c1_A | 40 | 5103917 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r03_t50_k010_c2_B | 40 | 5100473 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r01_t10_k100_c1_A | 40 | 5098623 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r01_t50_k010_c2_B | 40 | 5098120 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r04_t10_k100_c1_B | 40 | 5097449 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r01_t10_k100_c2_B | 40 | 5095445 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r06_t50_k010_c1_B | 40 | 5095183 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r10_t50_k100_c0_A | 40 | 5094403 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r05_t90_k010_c1_B | 40 | 5090291 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r08_t10_k010_c0_A | 40 | 5088372 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r06_t10_k100_c2_B | 40 | 5087858 |
| journal_validation/stage2g/full_path_validation/results/pilot_014_minus/minimum_e20 | 51 | 5087450 |
| journal_validation/stage2g/full_path_validation/results/pilot_014_minus/maximum_e20 | 51 | 5087397 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r06_t10_k010_c2_B | 40 | 5087018 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r08_t10_k010_c1_B | 40 | 5085621 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r05_t90_k100_c0_A | 40 | 5085386 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r08_t10_k100_c1_A | 40 | 5084501 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r05_t50_k010_c1_B | 40 | 5082047 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r05_t50_k100_c2_A | 40 | 5080272 |
| journal_validation/stage2g/full_path_validation/results/pilot_014_minus/maximum_e8 | 51 | 5079177 |
| journal_validation/stage2g/full_path_validation/results/pilot_014_minus/minimum_e8 | 51 | 5079171 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r05_t50_k010_c2_B | 40 | 5076436 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r06_t50_k010_c1_A | 40 | 5075869 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r05_t90_k100_c0_B | 40 | 5075624 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r03_t50_k100_c2_A | 40 | 5072342 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r05_t50_k100_c1_B | 40 | 5067161 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r07_t50_k010_c2_A | 40 | 5067088 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r03_t50_k100_c0_B | 40 | 5066986 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r01_t50_k100_c1_A | 40 | 5065879 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r09_t10_k100_c1_B | 40 | 5063665 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r02_t10_k100_c2_B | 40 | 5063192 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r06_t50_k010_c0_A | 40 | 5061597 |
| journal_validation/stage2h/readiness/results/sequential/n1000_t50_k100 | 40 | 5059698 |
| journal_validation/stage2h/readiness/results/parallel/n1000_t50_k100 | 40 | 5059694 |
| journal_validation/stage2h/readiness/results/repeat/n1000_t50_k100 | 40 | 5059692 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r09_t10_k010_c1_B | 40 | 5058609 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r02_t50_k010_c1_A | 40 | 5057712 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r01_t10_k100_c1_B | 40 | 5056836 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r09_t90_k100_c1_B | 40 | 5052481 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r02_t10_k010_c0_B | 40 | 5052244 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r09_t50_k100_c1_B | 40 | 5051001 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r05_t10_k010_c2_B | 40 | 5044900 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r04_t10_k010_c2_B | 40 | 5041915 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r02_t50_k010_c1_B | 40 | 5038365 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r04_t10_k010_c1_A | 40 | 5032345 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r06_t10_k100_c0_B | 40 | 5031271 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r01_t10_k010_c2_B | 40 | 5031049 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r03_t10_k010_c2_B | 40 | 5030726 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r02_t50_k010_c0_B | 40 | 5027727 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r01_t10_k100_c0_A | 40 | 5026423 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r02_t10_k100_c2_A | 40 | 5023568 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r05_t50_k010_c2_A | 40 | 5022936 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r05_t50_k100_c2_B | 40 | 5022707 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r03_t10_k100_c2_A | 40 | 5020547 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r06_t10_k100_c2_A | 40 | 5020173 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r08_t10_k100_c2_B | 40 | 5019398 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r05_t90_k010_c0_A | 40 | 5019268 |
| journal_validation/stage2g/full_path_validation/results/pilot_014_truth/minimum_e20 | 51 | 5016885 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r02_t90_k010_c0_A | 40 | 5016827 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r05_t10_k100_c2_B | 40 | 5016674 |
| journal_validation/stage2g/full_path_validation/results/pilot_014_truth/maximum_e20 | 51 | 5016427 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r02_t10_k010_c2_B | 40 | 5015549 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r07_t10_k010_c1_A | 40 | 5012098 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r03_t10_k100_c2_B | 40 | 5011629 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r07_t90_k100_c0_B | 40 | 5009773 |
| journal_validation/stage2g/full_path_validation/results/pilot_014_truth/minimum_e8 | 51 | 5008601 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r07_t10_k010_c0_A | 40 | 5007984 |
| journal_validation/stage2g/full_path_validation/results/pilot_014_truth/maximum_e8 | 51 | 5007914 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r01_t10_k010_c1_A | 40 | 5007832 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r01_t90_k100_c0_B | 40 | 5007406 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r07_t10_k100_c0_B | 40 | 5006392 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r05_t50_k100_c0_B | 40 | 5005598 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r02_t10_k010_c0_A | 40 | 5005557 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r03_t10_k100_c1_B | 40 | 5003220 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r08_t10_k010_c1_A | 40 | 4998885 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r02_t10_k010_c1_B | 40 | 4998781 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r10_t10_k100_c1_A | 40 | 4998532 |
| journal_validation/stage2g/full_path_validation/results/pilot_003_minus/minimum_e20 | 51 | 4998245 |
| journal_validation/stage2g/full_path_validation/results/pilot_003_minus/maximum_e20 | 51 | 4997694 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r10_t10_k010_c0_A | 40 | 4997245 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r05_t50_k100_c1_A | 40 | 4991208 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r06_t10_k010_c0_A | 40 | 4990966 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r01_t90_k010_c0_A | 40 | 4990378 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r03_t10_k010_c1_A | 40 | 4989937 |
| journal_validation/stage2g/full_path_validation/results/pilot_003_minus/minimum_e8 | 51 | 4989931 |
| journal_validation/stage2g/full_path_validation/results/pilot_003_minus/maximum_e8 | 51 | 4989399 |
| journal_article/qa/batch4/runtime/inc/lib/auto/share/dist/DateTime-Locale | 786 | 4987105 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r04_t10_k010_c2_A | 40 | 4982079 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r03_t90_k100_c2_A | 40 | 4982071 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r09_t10_k010_c0_A | 40 | 4981283 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r06_t10_k010_c1_A | 40 | 4980236 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r03_t10_k010_c2_A | 40 | 4979663 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r03_t10_k010_c1_B | 40 | 4977917 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r07_t90_k010_c2_A | 40 | 4976444 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r06_t10_k010_c1_B | 40 | 4973301 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r05_t10_k100_c2_A | 40 | 4971135 |
| journal_validation/stage2h/readiness/results/sequential/n1000_t90_k100 | 40 | 4970939 |
| journal_validation/stage2h/readiness/results/repeat/n1000_t90_k100 | 40 | 4970935 |
| journal_validation/stage2h/readiness/results/parallel/n1000_t90_k100 | 40 | 4970933 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r03_t10_k100_c1_A | 40 | 4968778 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r02_t50_k010_c0_A | 40 | 4967698 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r10_t50_k010_c0_B | 40 | 4960123 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r03_t50_k100_c0_A | 40 | 4960027 |
| journal_validation/stage2g/full_path_validation/results/pilot_003_truth/minimum_e20 | 51 | 4957872 |
| journal_validation/stage2g/full_path_validation/results/pilot_003_truth/maximum_e20 | 51 | 4957831 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r01_t50_k100_c2_B | 40 | 4957313 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r05_t10_k100_c2_B | 34 | 4956044 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r02_t10_k100_c1_B | 40 | 4955367 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r09_t90_k100_c1_A | 40 | 4951465 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r10_t10_k100_c2_A | 40 | 4950410 |
| journal_validation/stage2g/full_path_validation/results/pilot_003_truth/minimum_e8 | 51 | 4949596 |
| journal_validation/stage2g/full_path_validation/results/pilot_003_truth/maximum_e8 | 51 | 4949535 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r05_t10_k010_c0_A | 40 | 4938497 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r09_t10_k100_c1_A | 40 | 4937845 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r08_t10_k010_c0_B | 40 | 4934456 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r05_t50_k010_c0_A | 40 | 4928809 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r01_t90_k100_c1_A | 40 | 4927936 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r04_t10_k100_c0_A | 40 | 4923630 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r06_t50_k010_c0_B | 40 | 4920064 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r06_t50_k100_c1_B | 40 | 4919903 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r09_t90_k010_c2_B | 40 | 4918201 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r02_t10_k010_c2_A | 40 | 4917978 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r01_t50_k010_c2_A | 40 | 4917819 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r01_t90_k100_c0_A | 40 | 4910498 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r06_t50_k100_c2_A | 40 | 4903121 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r02_t90_k100_c1_B | 40 | 4902027 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r09_t10_k010_c1_A | 40 | 4901261 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r10_t50_k010_c2_A | 40 | 4894733 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r10_t50_k100_c2_B | 40 | 4894472 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r10_t10_k100_c2_B | 40 | 4893845 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r09_t10_k100_c2_A | 40 | 4890297 |
| journal_validation/stage2g/full_path_validation/results/pilot_004_truth/maximum_e20 | 51 | 4890250 |
| journal_validation/stage2g/full_path_validation/results/pilot_004_truth/minimum_e20 | 51 | 4889702 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r10_t50_k100_c1_A | 40 | 4885858 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r09_t50_k100_c1_A | 40 | 4885609 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r10_t50_k100_c2_A | 40 | 4882831 |
| journal_validation/stage2g/full_path_validation/results/pilot_004_truth/maximum_e8 | 51 | 4881914 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r01_t10_k010_c0_A | 40 | 4881823 |
| journal_validation/stage2g/full_path_validation/results/pilot_004_truth/minimum_e8 | 51 | 4881478 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r06_t10_k100_c1_B | 40 | 4869934 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r04_t10_k100_c0_B | 40 | 4864636 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r08_t10_k100_c0_B | 40 | 4864379 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r07_t90_k100_c2_B | 40 | 4861382 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r03_t10_k100_c0_A | 40 | 4854384 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r10_t50_k010_c0_A | 40 | 4852833 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r10_t10_k100_c0_A | 40 | 4840254 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r10_t10_k100_c1_B | 40 | 4834774 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r09_t10_k100_c2_B | 40 | 4834595 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r01_t10_k010_c2_A | 40 | 4828237 |
| journal_validation/stage2g/full_path_validation/results/pilot_006_truth/minimum_e20 | 51 | 4827804 |
| journal_validation/stage2g/full_path_validation/results/pilot_006_truth/maximum_e20 | 51 | 4827768 |
| journal_validation/stage2g/full_path_validation/results/pilot_006_truth/minimum_e8 | 51 | 4819493 |
| journal_validation/stage2g/full_path_validation/results/pilot_006_truth/maximum_e8 | 51 | 4819482 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r03_t10_k010_c0_A | 40 | 4806415 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r06_t50_k100_c1_A | 40 | 4805461 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r10_t10_k010_c1_B | 40 | 4803123 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r06_t10_k010_c0_B | 40 | 4798224 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r01_t50_k100_c2_A | 40 | 4794880 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r10_t10_k010_c0_B | 40 | 4793423 |
| journal_validation/publication_review/lssp_optimization/qa | 50 | 4763962 |
| journal_validation/stage2g/full_path_validation/results/pilot_007_minus/maximum_e20 | 51 | 4749891 |
| journal_validation/stage2g/full_path_validation/results/pilot_007_minus/minimum_e20 | 51 | 4749361 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r03_t10_k100_c0_B | 40 | 4745768 |
| journal_validation/stage2g/full_path_validation/results/pilot_007_minus/maximum_e8 | 51 | 4741612 |
| journal_validation/stage2g/full_path_validation/results/pilot_007_minus/minimum_e8 | 51 | 4741115 |
| journal_validation/stage2g/full_path_validation/results/pilot_002_truth/minimum_e20 | 51 | 4713792 |
| journal_validation/stage2g/full_path_validation/results/pilot_002_truth/maximum_e20 | 51 | 4713750 |
| journal_validation/stage2g/full_path_validation/results/pilot_007_truth/maximum_e20 | 51 | 4706162 |
| journal_validation/stage2g/full_path_validation/results/pilot_002_truth/minimum_e8 | 51 | 4705301 |
| journal_validation/stage2g/full_path_validation/results/pilot_002_truth/maximum_e8 | 51 | 4705237 |
| journal_validation/stage2g/full_path_validation/results/pilot_007_truth/minimum_e20 | 51 | 4705166 |
| journal_validation/stage2g/full_path_validation/results/pilot_007_truth/maximum_e8 | 51 | 4697926 |
| journal_validation/stage2g/full_path_validation/results/pilot_007_truth/minimum_e8 | 51 | 4696878 |
| thesis_extension/environment/legacy_R343_library/stringi/libs/i386 | 1 | 4695054 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r09_t10_k100_c0_B | 40 | 4687407 |
| journal_validation/stage2g/full_path_validation/results/pilot_006_minus/maximum_e20 | 51 | 4669710 |
| journal_validation/stage2g/full_path_validation/results/pilot_006_minus/minimum_e20 | 51 | 4669681 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r09_t10_k100_c0_A | 40 | 4666467 |
| journal_validation/stage2g/full_path_validation/results/pilot_006_minus/minimum_e8 | 51 | 4661466 |
| journal_validation/stage2g/full_path_validation/results/pilot_006_minus/maximum_e8 | 51 | 4661463 |
| journal_validation/stage2g/full_path_validation/results/pilot_002_minus/maximum_e20 | 51 | 4660268 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r03_t10_k010_c0_B | 40 | 4658908 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r08_t10_k100_c0_A | 40 | 4658868 |
| journal_validation/stage2g/full_path_validation/results/pilot_002_minus/minimum_e20 | 51 | 4658198 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r10_t10_k010_c2_B | 40 | 4655079 |
| journal_validation/stage2g/full_path_validation/results/pilot_002_minus/maximum_e8 | 51 | 4651799 |
| journal_validation/stage2g/full_path_validation/results/pilot_004_minus/minimum_e20 | 51 | 4650655 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r06_t10_k100_c1_A | 40 | 4650291 |
| journal_validation/stage2g/full_path_validation/results/pilot_004_minus/maximum_e20 | 51 | 4650191 |
| journal_validation/stage2g/full_path_validation/results/pilot_002_minus/minimum_e8 | 51 | 4649696 |
| journal_validation/stage2g/full_path_validation/results/pilot_004_minus/minimum_e8 | 51 | 4642502 |
| journal_validation/stage2g/full_path_validation/results/pilot_004_minus/maximum_e8 | 51 | 4641885 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r10_t10_k010_c1_A | 40 | 4639588 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r10_t10_k100_c0_B | 40 | 4620894 |
| journal_validation/stage2e/output/paired_20261029T093009Z/pilot_004_truth | 33 | 4583350 |
| journal_validation/stage2e/output/paired_20261029T093009Z/pilot_007_truth | 33 | 4579008 |
| journal_validation/stage2e/output/paired_20261029T093009Z/pilot_014_truth | 33 | 4578848 |
| journal_validation/stage2e/output/paired_20261029T093009Z/pilot_003_truth | 33 | 4578733 |
| journal_validation/stage2e/output/paired_20261029T093009Z/pilot_001_truth | 33 | 4576356 |
| journal_validation/stage2e/output/paired_20261029T093009Z/pilot_005_truth | 33 | 4574784 |
| journal_validation/stage2e/output/paired_20261029T093009Z/pilot_006_truth | 33 | 4556101 |
| journal_validation/stage2e/output/paired_20261029T093009Z/pilot_002_truth | 33 | 4555949 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r10_t10_k010_c2_A | 40 | 4442259 |
| journal_validation/stage2e/output/paired_20261029T093009Z | 36 | 4380688 |
| journal_validation/publication_review/lssp_optimization | 16 | 4315084 |
| thesis_extension/environment/legacy_R343_library/stringi/libs/x64 | 1 | 4289536 |
| journal_validation/stage2g/full_path_validation/results/pilot_014_minus/C | 52 | 4250643 |
| journal_validation/stage2g/full_path_validation/results/pilot_014_truth/C | 52 | 4232277 |
| journal_validation/stage2g/full_path_validation/results/pilot_003_minus/C | 52 | 4214896 |
| journal_validation/stage2g/full_path_validation/results/pilot_004_plus/C | 52 | 4211243 |
| journal_validation/stage2g/full_path_validation/results/pilot_003_truth/C | 52 | 4201995 |
| journal_validation/stage2g/full_path_validation/results/pilot_005_plus/C | 52 | 4200197 |
| journal_validation/stage2g/end_to_end_certification/results/pilot_004_minus | 39 | 4188083 |
| journal_validation/stage2g/full_path_validation/results/pilot_006_plus/C | 52 | 4185725 |
| journal_validation/stage2g/full_path_validation/results/pilot_004_truth/C | 52 | 4183778 |
| journal_validation/stage2g/end_to_end_certification/results/pilot_001_minus | 39 | 4183144 |
| journal_validation/stage2g/end_to_end_certification/results/pilot_001_truth | 39 | 4182111 |
| journal_validation/stage2g/end_to_end_certification/results/pilot_004_truth | 39 | 4177900 |
| journal_validation/stage2g/end_to_end_certification/results/pilot_002_truth | 39 | 4170259 |
| journal_validation/stage2g/end_to_end_certification/results/pilot_007_minus | 39 | 4168214 |
| journal_validation/stage2g/end_to_end_certification/results/pilot_003_truth | 39 | 4156150 |
| journal_validation/stage2g/end_to_end_certification/results/pilot_002_plus | 39 | 4155994 |
| journal_validation/stage2g/full_path_validation/results/pilot_001_truth/C | 52 | 4155895 |
| journal_validation/stage2g/end_to_end_certification/results/pilot_004_plus | 39 | 4154801 |
| journal_validation/stage2g/end_to_end_certification/results/pilot_014_minus | 39 | 4153476 |
| journal_validation/stage2g/end_to_end_certification/results/pilot_001_plus | 39 | 4152482 |
| journal_validation/stage2g/end_to_end_certification/results/pilot_006_minus | 39 | 4151295 |
| journal_validation/stage2g/end_to_end_certification/results/pilot_007_truth | 39 | 4151031 |
| journal_validation/stage2g/full_path_validation/results/pilot_002_plus/C | 52 | 4150908 |
| journal_validation/stage2g/end_to_end_certification/results/pilot_003_plus | 39 | 4150745 |
| journal_validation/stage2g/end_to_end_certification/results/pilot_005_plus | 39 | 4145524 |
| journal_validation/stage2g/end_to_end_certification/results/pilot_006_truth | 39 | 4143576 |
| journal_validation/stage2g/full_path_validation/results/pilot_006_truth/C | 52 | 4142704 |
| journal_validation/stage2g/end_to_end_certification/results/pilot_007_plus | 39 | 4138918 |
| journal_validation/stage2g/end_to_end_certification/results/pilot_006_plus | 39 | 4134140 |
| journal_validation/stage2g/full_path_validation/results/pilot_007_minus/C | 52 | 4113971 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r20_t90_k100_c2_A | 11 | 4111190 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r20_t90_k010_c1_A | 11 | 4111185 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r20_t90_k100_c0_A | 11 | 4111178 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r20_t90_k100_c1_A | 11 | 4111172 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r20_t10_k100_c2_A | 11 | 4111169 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r20_t90_k010_c1_B | 11 | 4111168 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r20_t90_k100_c2_B | 11 | 4111167 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r20_t10_k100_c0_A | 11 | 4111165 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r20_t90_k010_c0_A | 11 | 4111163 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r20_t90_k010_c2_A | 11 | 4111163 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r20_t10_k010_c1_B | 11 | 4111162 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r20_t90_k100_c0_B | 11 | 4111161 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r20_t50_k010_c2_A | 11 | 4111160 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r20_t90_k100_c1_B | 11 | 4111160 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r20_t50_k010_c0_A | 11 | 4111159 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r20_t50_k010_c0_B | 11 | 4111159 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r20_t10_k100_c1_B | 11 | 4111157 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r20_t90_k010_c0_B | 11 | 4111157 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r20_t10_k100_c2_B | 11 | 4111156 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r20_t50_k010_c1_A | 11 | 4111156 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r20_t50_k100_c1_A | 11 | 4111156 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r20_t50_k100_c2_A | 11 | 4111156 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r20_t10_k100_c1_A | 11 | 4111154 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r20_t10_k010_c0_A | 11 | 4111153 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r20_t10_k100_c0_B | 11 | 4111152 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r20_t50_k100_c2_B | 11 | 4111152 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r20_t90_k010_c2_B | 11 | 4111152 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r20_t50_k100_c0_A | 11 | 4111151 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r20_t10_k010_c1_A | 11 | 4111149 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r20_t50_k010_c2_B | 11 | 4111149 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r20_t50_k010_c1_B | 11 | 4111148 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r20_t10_k010_c2_A | 11 | 4111147 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r20_t10_k010_c2_B | 11 | 4111147 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r20_t10_k010_c0_B | 11 | 4111146 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r20_t50_k100_c0_B | 11 | 4111143 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r20_t50_k100_c1_B | 11 | 4111139 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r17_t90_k010_c0_B | 11 | 4111106 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r17_t90_k010_c1_A | 11 | 4111106 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r17_t90_k010_c0_A | 11 | 4111103 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r06_t90_k010_c2_A | 11 | 4111099 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r17_t90_k010_c2_A | 11 | 4111095 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r17_t90_k100_c2_A | 11 | 4111095 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r06_t90_k010_c1_A | 11 | 4111094 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r17_t10_k100_c0_A | 11 | 4111094 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r17_t90_k010_c1_B | 11 | 4111092 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r17_t90_k100_c0_B | 11 | 4111092 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r17_t90_k100_c2_B | 11 | 4111092 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r17_t90_k010_c2_B | 11 | 4111091 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r17_t50_k010_c1_A | 11 | 4111090 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r06_t50_k010_c1_A | 11 | 4111089 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r17_t90_k100_c0_A | 11 | 4111088 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r06_t10_k010_c1_A | 11 | 4111086 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r17_t10_k100_c0_B | 11 | 4111086 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r06_t90_k100_c0_A | 11 | 4111085 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r06_t90_k100_c2_A | 11 | 4111085 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r06_t90_k010_c0_A | 11 | 4111084 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r17_t10_k010_c1_A | 11 | 4111084 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r06_t10_k010_c2_A | 11 | 4111083 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r06_t50_k100_c2_A | 11 | 4111083 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r17_t50_k010_c2_A | 11 | 4111083 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r06_t10_k010_c0_A | 11 | 4111082 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r17_t10_k010_c2_B | 11 | 4111082 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r17_t90_k100_c1_A | 11 | 4111082 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r06_t10_k100_c1_A | 11 | 4111081 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r06_t90_k010_c1_B | 11 | 4111081 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r17_t50_k010_c0_A | 11 | 4111081 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r17_t90_k100_c1_B | 11 | 4111081 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r06_t50_k010_c2_A | 11 | 4111080 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r06_t90_k100_c0_B | 11 | 4111080 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r06_t90_k100_c1_A | 11 | 4111080 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r17_t10_k010_c0_B | 11 | 4111079 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r06_t10_k100_c0_A | 11 | 4111078 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r17_t50_k010_c1_B | 11 | 4111078 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r06_t50_k010_c0_A | 11 | 4111077 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r06_t90_k010_c2_B | 11 | 4111077 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r17_t10_k010_c2_A | 11 | 4111077 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r17_t10_k100_c2_B | 11 | 4111077 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r17_t50_k010_c0_B | 11 | 4111077 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r17_t50_k100_c2_B | 11 | 4111074 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r06_t90_k100_c1_B | 11 | 4111073 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r06_t90_k100_c2_B | 11 | 4111073 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r17_t10_k010_c0_A | 11 | 4111073 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r17_t10_k100_c1_A | 11 | 4111073 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r17_t50_k010_c2_B | 11 | 4111073 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r05_t90_k010_c1_B | 11 | 4111072 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r06_t10_k100_c2_A | 11 | 4111071 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r17_t10_k100_c1_B | 11 | 4111071 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r17_t10_k100_c2_A | 11 | 4111070 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r17_t50_k100_c1_B | 11 | 4111070 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r06_t50_k100_c1_A | 11 | 4111069 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r17_t50_k100_c2_A | 11 | 4111068 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r06_t10_k100_c0_B | 11 | 4111067 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r06_t90_k010_c0_B | 11 | 4111067 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r06_t10_k100_c1_B | 11 | 4111066 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r06_t50_k100_c0_B | 11 | 4111065 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r17_t50_k100_c0_B | 11 | 4111065 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r06_t10_k100_c2_B | 11 | 4111064 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r17_t10_k010_c1_B | 11 | 4111064 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r17_t50_k100_c1_A | 11 | 4111064 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r06_t50_k100_c0_A | 11 | 4111062 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r05_t90_k010_c1_A | 11 | 4111061 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r06_t10_k010_c0_B | 11 | 4111061 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r06_t50_k010_c1_B | 11 | 4111061 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r06_t50_k010_c2_B | 11 | 4111061 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r05_t90_k010_c0_A | 11 | 4111060 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r14_t90_k010_c1_A | 11 | 4111060 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r06_t10_k010_c2_B | 11 | 4111059 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r06_t50_k100_c2_B | 11 | 4111059 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r14_t90_k100_c1_A | 11 | 4111059 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r14_t90_k100_c1_B | 11 | 4111059 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r05_t50_k010_c0_B | 11 | 4111058 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r17_t50_k100_c0_A | 11 | 4111058 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r05_t10_k100_c0_B | 11 | 4111057 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r06_t10_k010_c1_B | 11 | 4111057 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r05_t90_k010_c2_B | 11 | 4111056 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r06_t50_k100_c1_B | 11 | 4111055 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r05_t90_k010_c0_B | 11 | 4111054 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r06_t50_k010_c0_B | 11 | 4111054 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r14_t90_k100_c0_A | 11 | 4111054 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r05_t90_k100_c1_B | 11 | 4111053 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r14_t50_k010_c2_B | 11 | 4111052 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r15_t10_k100_c0_A | 11 | 4111052 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r05_t10_k100_c0_A | 11 | 4111051 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r14_t10_k100_c1_B | 11 | 4111051 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r14_t90_k010_c1_B | 11 | 4111051 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r14_t90_k010_c2_A | 11 | 4111050 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r05_t90_k100_c2_B | 11 | 4111049 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r14_t10_k100_c1_A | 11 | 4111048 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r14_t90_k100_c2_A | 11 | 4111048 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r05_t10_k010_c1_B | 11 | 4111047 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r14_t90_k010_c2_B | 11 | 4111047 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r05_t10_k010_c0_A | 11 | 4111046 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r14_t90_k100_c0_B | 11 | 4111046 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r05_t10_k010_c0_B | 11 | 4111045 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r05_t90_k010_c2_A | 11 | 4111045 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r05_t90_k100_c1_A | 11 | 4111045 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r14_t10_k010_c2_A | 11 | 4111044 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r14_t10_k100_c2_B | 11 | 4111043 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r14_t90_k100_c2_B | 11 | 4111043 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r14_t50_k010_c1_A | 11 | 4111042 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r14_t10_k100_c0_A | 11 | 4111041 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r15_t90_k100_c2_A | 11 | 4111041 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r05_t10_k010_c1_A | 11 | 4111040 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r05_t10_k010_c2_B | 11 | 4111039 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r14_t50_k010_c0_A | 11 | 4111039 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r14_t50_k010_c0_B | 11 | 4111039 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r14_t90_k010_c0_A | 11 | 4111039 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r14_t90_k010_c0_B | 11 | 4111039 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r05_t10_k100_c2_B | 11 | 4111038 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r05_t90_k100_c0_B | 11 | 4111038 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r15_t90_k100_c0_A | 11 | 4111038 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r05_t50_k010_c0_A | 11 | 4111037 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r05_t50_k010_c1_B | 11 | 4111037 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r05_t10_k100_c2_A | 11 | 4111036 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r14_t10_k010_c2_B | 11 | 4111036 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r14_t10_k100_c0_B | 11 | 4111036 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r14_t10_k100_c2_A | 11 | 4111036 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r14_t50_k010_c1_B | 11 | 4111036 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r05_t10_k010_c2_A | 11 | 4111035 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r05_t50_k010_c1_A | 11 | 4111035 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r05_t90_k100_c2_A | 11 | 4111035 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r05_t50_k010_c2_A | 11 | 4111034 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r14_t50_k100_c0_A | 11 | 4111034 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r15_t90_k010_c1_A | 11 | 4111034 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r14_t50_k010_c2_A | 11 | 4111033 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r14_t50_k100_c2_B | 11 | 4111033 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r05_t10_k100_c1_B | 11 | 4111032 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r15_t90_k010_c1_B | 11 | 4111032 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r05_t90_k100_c0_A | 11 | 4111030 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r14_t10_k010_c1_B | 11 | 4111030 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r14_t10_k010_c0_B | 11 | 4111029 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r15_t10_k100_c0_B | 11 | 4111029 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r15_t90_k010_c2_A | 11 | 4111029 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r15_t90_k100_c1_A | 11 | 4111029 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r05_t50_k010_c2_B | 11 | 4111028 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r14_t10_k010_c0_A | 11 | 4111028 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r14_t50_k100_c0_B | 11 | 4111028 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r15_t10_k010_c1_A | 11 | 4111028 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r15_t10_k100_c1_A | 11 | 4111028 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r05_t50_k100_c2_B | 11 | 4111027 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r14_t50_k100_c2_A | 11 | 4111027 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r15_t10_k010_c0_A | 11 | 4111027 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r15_t90_k010_c2_B | 11 | 4111027 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r05_t50_k100_c0_A | 11 | 4111026 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r15_t90_k010_c0_A | 11 | 4111025 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r15_t90_k010_c0_B | 11 | 4111024 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r15_t90_k100_c1_B | 11 | 4111024 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r05_t50_k100_c0_B | 11 | 4111023 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r14_t50_k100_c1_A | 11 | 4111023 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r15_t10_k010_c2_A | 11 | 4111022 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r15_t10_k100_c2_A | 11 | 4111022 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r15_t50_k100_c2_A | 11 | 4111022 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r05_t10_k100_c1_A | 11 | 4111021 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r15_t50_k010_c0_A | 11 | 4111021 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r15_t90_k100_c0_B | 11 | 4111021 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r14_t50_k100_c1_B | 11 | 4111020 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r15_t50_k010_c2_A | 11 | 4111020 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r14_t10_k010_c1_A | 11 | 4111017 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r15_t50_k010_c1_B | 11 | 4111017 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r15_t90_k100_c2_B | 11 | 4111017 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r15_t50_k010_c2_B | 11 | 4111016 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r05_t50_k100_c2_A | 11 | 4111015 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r15_t50_k010_c1_A | 11 | 4111015 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r15_t50_k100_c1_A | 11 | 4111015 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r05_t50_k100_c1_A | 11 | 4111014 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r16_t10_k100_c0_B | 11 | 4111014 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r05_t50_k100_c1_B | 11 | 4111013 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r15_t10_k010_c1_B | 11 | 4111013 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r15_t10_k010_c2_B | 11 | 4111013 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r15_t50_k010_c0_B | 11 | 4111013 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r16_t90_k010_c1_A | 11 | 4111013 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r15_t50_k100_c0_A | 11 | 4111012 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r16_t90_k100_c2_B | 11 | 4111012 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r15_t10_k010_c0_B | 11 | 4111011 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r15_t10_k100_c2_B | 11 | 4111011 |
| journal_validation/stage2h/readiness/inputs/n1000_t90_k010 | 11 | 4111009 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r16_t90_k010_c0_A | 11 | 4111007 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r16_t90_k100_c1_B | 11 | 4111007 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r15_t10_k100_c1_B | 11 | 4111006 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r16_t10_k100_c1_B | 11 | 4111006 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r16_t10_k100_c2_B | 11 | 4111006 |
| journal_validation/stage2h/readiness/inputs/n1000_t90_k100 | 11 | 4111004 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r16_t90_k010_c1_B | 11 | 4111003 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r16_t90_k010_c2_A | 11 | 4111003 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r15_t50_k100_c2_B | 11 | 4111002 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r16_t50_k100_c2_B | 11 | 4111002 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r16_t90_k100_c0_B | 11 | 4111001 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r15_t50_k100_c0_B | 11 | 4111000 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r15_t50_k100_c1_B | 11 | 4111000 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r16_t10_k010_c1_A | 11 | 4111000 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r16_t90_k010_c2_B | 11 | 4111000 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r16_t10_k010_c0_A | 11 | 4110998 |
| journal_validation/stage2h/readiness/inputs/n1000_t50_k010 | 11 | 4110998 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r09_t90_k100_c1_A | 11 | 4110997 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r16_t10_k010_c2_A | 11 | 4110996 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r16_t10_k100_c1_A | 11 | 4110996 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r16_t10_k100_c0_A | 11 | 4110995 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r16_t90_k010_c0_B | 11 | 4110995 |
| journal_validation/stage2h/readiness/inputs/n1000_t10_k010 | 11 | 4110995 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r16_t90_k100_c2_A | 11 | 4110994 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r16_t50_k010_c0_A | 11 | 4110992 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r16_t50_k010_c1_A | 11 | 4110991 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r16_t50_k010_c2_B | 11 | 4110991 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r09_t90_k100_c0_A | 11 | 4110989 |
| journal_validation/stage2h/readiness/inputs/n1000_t10_k100 | 11 | 4110989 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r16_t10_k100_c2_A | 11 | 4110988 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r16_t90_k100_c1_A | 11 | 4110987 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r16_t50_k100_c2_A | 11 | 4110986 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r09_t90_k010_c2_A | 11 | 4110985 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r09_t10_k100_c0_A | 11 | 4110984 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r16_t50_k010_c2_A | 11 | 4110983 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r16_t50_k100_c0_B | 11 | 4110983 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r16_t50_k100_c1_A | 11 | 4110983 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r16_t50_k100_c1_B | 11 | 4110983 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r09_t10_k100_c1_A | 11 | 4110982 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r09_t10_k100_c2_A | 11 | 4110982 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r16_t50_k010_c1_B | 11 | 4110981 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r16_t90_k100_c0_A | 11 | 4110980 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r09_t90_k100_c2_A | 11 | 4110977 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r16_t50_k100_c0_A | 11 | 4110977 |
| journal_validation/stage2h/readiness/inputs/n1000_t50_k100 | 11 | 4110976 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r16_t10_k010_c2_B | 11 | 4110975 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r09_t90_k010_c0_A | 11 | 4110974 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r09_t90_k010_c1_A | 11 | 4110973 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r16_t50_k010_c0_B | 11 | 4110972 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r16_t10_k010_c0_B | 11 | 4110971 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r09_t10_k010_c1_A | 11 | 4110970 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r16_t10_k010_c1_B | 11 | 4110966 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r09_t10_k010_c2_A | 11 | 4110965 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r09_t50_k010_c1_A | 11 | 4110965 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r09_t50_k010_c2_A | 11 | 4110964 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r09_t50_k100_c0_A | 11 | 4110963 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r09_t10_k010_c0_A | 11 | 4110960 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r09_t50_k100_c1_A | 11 | 4110956 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r09_t50_k100_c2_A | 11 | 4110956 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r01_t90_k010_c1_B | 11 | 4110955 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r09_t90_k010_c0_B | 11 | 4110955 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r09_t90_k010_c2_B | 11 | 4110954 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r01_t90_k010_c2_A | 11 | 4110952 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r01_t90_k010_c2_B | 11 | 4110951 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r09_t90_k010_c1_B | 11 | 4110951 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r10_t10_k010_c0_A | 11 | 4110951 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r01_t90_k100_c0_A | 11 | 4110949 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r10_t90_k010_c1_A | 11 | 4110949 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r09_t50_k010_c2_B | 11 | 4110948 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r11_t90_k100_c2_A | 11 | 4110948 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r09_t50_k010_c0_A | 11 | 4110947 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r09_t50_k010_c0_B | 11 | 4110947 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r11_t90_k100_c0_A | 11 | 4110947 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r01_t50_k010_c2_A | 11 | 4110946 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r09_t10_k010_c1_B | 11 | 4110946 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r11_t10_k100_c1_A | 11 | 4110946 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r10_t90_k010_c1_B | 11 | 4110945 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r11_t50_k010_c1_A | 11 | 4110945 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r01_t90_k010_c0_A | 11 | 4110944 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r03_t90_k010_c2_A | 11 | 4110944 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r11_t10_k100_c0_A | 11 | 4110944 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r11_t90_k010_c0_A | 11 | 4110944 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r03_t50_k010_c2_A | 11 | 4110943 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r03_t90_k010_c0_A | 11 | 4110943 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r09_t10_k100_c1_B | 11 | 4110943 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r10_t90_k010_c2_A | 11 | 4110943 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r19_t90_k010_c0_B | 11 | 4110943 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r19_t90_k010_c2_B | 11 | 4110943 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r19_t90_k100_c0_B | 11 | 4110943 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r19_t90_k100_c2_A | 11 | 4110943 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r01_t90_k010_c0_B | 11 | 4110942 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r09_t90_k100_c0_B | 11 | 4110942 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r09_t90_k100_c2_B | 11 | 4110942 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r10_t50_k010_c2_A | 11 | 4110942 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r19_t90_k010_c1_B | 11 | 4110942 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r01_t10_k100_c0_A | 11 | 4110941 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r01_t50_k010_c1_A | 11 | 4110941 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r01_t90_k010_c1_A | 11 | 4110941 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r01_t90_k100_c2_A | 11 | 4110941 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r09_t50_k010_c1_B | 11 | 4110941 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r10_t90_k010_c0_A | 11 | 4110941 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r19_t10_k100_c2_B | 11 | 4110940 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r01_t50_k010_c1_B | 11 | 4110939 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r09_t10_k100_c2_B | 11 | 4110939 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r10_t50_k010_c1_B | 11 | 4110939 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r10_t90_k010_c2_B | 11 | 4110939 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r11_t90_k010_c1_A | 11 | 4110939 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r11_t90_k010_c2_A | 11 | 4110939 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r19_t90_k010_c0_A | 11 | 4110939 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r01_t10_k100_c0_B | 11 | 4110938 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r01_t10_k100_c1_A | 11 | 4110938 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r09_t10_k010_c0_B | 11 | 4110938 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r11_t10_k010_c0_A | 11 | 4110938 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r11_t50_k010_c2_A | 11 | 4110938 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r19_t10_k100_c1_B | 11 | 4110938 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r09_t10_k010_c2_B | 11 | 4110937 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r10_t90_k010_c0_B | 11 | 4110937 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r11_t10_k010_c2_A | 11 | 4110937 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r19_t10_k010_c2_B | 11 | 4110937 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r19_t10_k100_c2_A | 11 | 4110937 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r01_t10_k010_c0_A | 11 | 4110936 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r01_t10_k100_c2_A | 11 | 4110936 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r03_t10_k010_c2_A | 11 | 4110936 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r11_t90_k100_c1_A | 11 | 4110936 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r19_t10_k100_c0_A | 11 | 4110936 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r19_t90_k100_c0_A | 11 | 4110936 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r03_t10_k010_c0_A | 11 | 4110935 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r11_t10_k100_c2_A | 11 | 4110935 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r01_t10_k010_c0_B | 11 | 4110934 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r01_t10_k100_c1_B | 11 | 4110934 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r01_t50_k010_c2_B | 11 | 4110934 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r10_t50_k010_c1_A | 11 | 4110934 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r19_t90_k010_c2_A | 11 | 4110934 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r19_t90_k100_c2_B | 11 | 4110934 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r01_t10_k010_c2_B | 11 | 4110933 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r01_t90_k100_c2_B | 11 | 4110933 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r09_t90_k100_c1_B | 11 | 4110933 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r10_t10_k010_c0_B | 11 | 4110933 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r10_t90_k100_c1_A | 11 | 4110933 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r10_t90_k100_c1_B | 11 | 4110933 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r19_t90_k100_c1_B | 11 | 4110933 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r01_t10_k010_c2_A | 11 | 4110932 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r01_t90_k100_c0_B | 11 | 4110932 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r10_t90_k100_c0_A | 11 | 4110932 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r10_t90_k100_c2_A | 11 | 4110932 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r11_t10_k010_c2_B | 11 | 4110932 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r11_t90_k010_c0_B | 11 | 4110932 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r11_t90_k100_c2_B | 11 | 4110932 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r19_t10_k100_c1_A | 11 | 4110932 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r01_t10_k010_c1_B | 11 | 4110931 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r03_t90_k010_c1_A | 11 | 4110931 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r10_t10_k010_c2_A | 11 | 4110931 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r01_t50_k010_c0_A | 11 | 4110930 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r01_t90_k100_c1_A | 11 | 4110930 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r03_t50_k010_c0_A | 11 | 4110930 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r09_t10_k100_c0_B | 11 | 4110930 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r10_t50_k010_c2_B | 11 | 4110930 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r11_t10_k010_c1_A | 11 | 4110930 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r09_t50_k100_c2_B | 11 | 4110929 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r10_t10_k010_c1_A | 11 | 4110929 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r10_t10_k010_c2_B | 11 | 4110929 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r10_t10_k100_c2_A | 11 | 4110929 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r11_t10_k010_c0_B | 11 | 4110929 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r11_t90_k010_c1_B | 11 | 4110929 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r19_t10_k100_c0_B | 11 | 4110929 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r11_t50_k100_c2_A | 11 | 4110928 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r19_t90_k100_c1_A | 11 | 4110928 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r10_t10_k100_c1_B | 11 | 4110927 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r11_t50_k010_c0_A | 11 | 4110927 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r11_t50_k010_c2_B | 11 | 4110927 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r19_t50_k010_c0_B | 11 | 4110927 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r01_t50_k010_c0_B | 11 | 4110926 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r01_t90_k100_c1_B | 11 | 4110926 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r10_t10_k100_c0_A | 11 | 4110926 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r19_t50_k100_c2_B | 11 | 4110926 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r19_t50_k010_c1_A | 11 | 4110925 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r03_t10_k010_c1_A | 11 | 4110924 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r10_t10_k100_c0_B | 11 | 4110924 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r10_t90_k100_c0_B | 11 | 4110924 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r11_t10_k100_c1_B | 11 | 4110924 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r19_t10_k010_c1_B | 11 | 4110924 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r19_t90_k010_c1_A | 11 | 4110924 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r11_t50_k100_c0_A | 11 | 4110922 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r11_t50_k100_c1_A | 11 | 4110922 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r11_t90_k100_c0_B | 11 | 4110922 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r19_t10_k010_c0_A | 11 | 4110922 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r01_t10_k010_c1_A | 11 | 4110921 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r01_t10_k100_c2_B | 11 | 4110921 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r10_t50_k010_c0_A | 11 | 4110921 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r10_t90_k100_c2_B | 11 | 4110921 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r19_t50_k010_c1_B | 11 | 4110921 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r03_t50_k010_c1_A | 11 | 4110920 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r11_t50_k010_c1_B | 11 | 4110920 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r11_t50_k100_c1_B | 11 | 4110920 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r11_t90_k010_c2_B | 11 | 4110920 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r01_t50_k100_c0_B | 11 | 4110919 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r19_t10_k010_c0_B | 11 | 4110919 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r19_t10_k010_c2_A | 11 | 4110919 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r19_t50_k100_c0_B | 11 | 4110919 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r11_t10_k010_c1_B | 11 | 4110918 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r19_t50_k010_c0_A | 11 | 4110918 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r19_t50_k010_c2_B | 11 | 4110918 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r19_t50_k100_c2_A | 11 | 4110918 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r10_t10_k010_c1_B | 11 | 4110916 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r10_t10_k100_c1_A | 11 | 4110916 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r11_t50_k010_c0_B | 11 | 4110916 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r01_t50_k100_c2_A | 11 | 4110915 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r09_t50_k100_c1_B | 11 | 4110915 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r19_t50_k100_c0_A | 11 | 4110915 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r01_t50_k100_c1_A | 11 | 4110914 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r01_t50_k100_c2_B | 11 | 4110914 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r10_t50_k100_c1_A | 11 | 4110914 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r19_t10_k010_c1_A | 11 | 4110914 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r19_t50_k100_c1_B | 11 | 4110914 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r10_t50_k010_c0_B | 11 | 4110913 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r11_t10_k100_c2_B | 11 | 4110913 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r01_t50_k100_c0_A | 11 | 4110911 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r01_t50_k100_c1_B | 11 | 4110910 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r11_t90_k100_c1_B | 11 | 4110910 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r10_t50_k100_c0_A | 11 | 4110909 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r10_t50_k100_c1_B | 11 | 4110909 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r19_t50_k010_c2_A | 11 | 4110909 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r03_t50_k010_c0_B | 11 | 4110908 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r09_t50_k100_c0_B | 11 | 4110908 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r11_t10_k100_c0_B | 11 | 4110908 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r10_t10_k100_c2_B | 11 | 4110906 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r03_t90_k010_c0_B | 11 | 4110905 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r10_t50_k100_c2_A | 11 | 4110905 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r10_t50_k100_c2_B | 11 | 4110905 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r03_t90_k010_c2_B | 11 | 4110903 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r10_t50_k100_c0_B | 11 | 4110903 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r11_t50_k100_c2_B | 11 | 4110902 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r03_t50_k010_c1_B | 11 | 4110901 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r19_t50_k100_c1_A | 11 | 4110901 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r03_t90_k010_c1_B | 11 | 4110899 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r03_t10_k010_c1_B | 11 | 4110897 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r11_t50_k100_c0_B | 11 | 4110896 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r03_t10_k100_c0_A | 11 | 4110895 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r03_t10_k100_c1_A | 11 | 4110892 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r03_t50_k010_c2_B | 11 | 4110892 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r03_t10_k010_c2_B | 11 | 4110891 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r03_t90_k100_c2_A | 11 | 4110887 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r03_t90_k100_c1_A | 11 | 4110886 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r03_t10_k010_c0_B | 11 | 4110885 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r03_t90_k100_c1_B | 11 | 4110885 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r03_t10_k100_c1_B | 11 | 4110883 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r03_t10_k100_c2_B | 11 | 4110881 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r03_t90_k100_c2_B | 11 | 4110879 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r03_t50_k100_c0_A | 11 | 4110877 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r03_t90_k100_c0_A | 11 | 4110874 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r03_t10_k100_c0_B | 11 | 4110873 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r03_t50_k100_c0_B | 11 | 4110873 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r03_t50_k100_c2_A | 11 | 4110873 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r03_t90_k100_c0_B | 11 | 4110873 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r03_t10_k100_c2_A | 11 | 4110872 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r03_t50_k100_c1_A | 11 | 4110868 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r02_t90_k010_c2_A | 11 | 4110867 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r12_t90_k100_c1_A | 11 | 4110864 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r03_t50_k100_c2_B | 11 | 4110860 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r12_t90_k010_c1_B | 11 | 4110857 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r02_t50_k010_c2_B | 11 | 4110856 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r02_t50_k010_c0_A | 11 | 4110855 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r03_t50_k100_c1_B | 11 | 4110855 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r07_t90_k010_c0_A | 11 | 4110855 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r07_t90_k010_c2_A | 11 | 4110855 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r12_t90_k100_c2_A | 11 | 4110852 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r02_t50_k010_c2_A | 11 | 4110850 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r12_t90_k010_c2_A | 11 | 4110850 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r02_t90_k010_c1_B | 11 | 4110849 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r07_t10_k010_c1_A | 11 | 4110848 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r12_t10_k100_c0_A | 11 | 4110848 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r02_t90_k010_c2_B | 11 | 4110847 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r02_t90_k010_c0_B | 11 | 4110846 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r04_t90_k010_c0_A | 11 | 4110846 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r07_t90_k010_c1_A | 11 | 4110845 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r02_t90_k010_c1_A | 11 | 4110844 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r02_t10_k010_c2_B | 11 | 4110843 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r12_t90_k010_c1_A | 11 | 4110843 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r02_t10_k010_c1_A | 11 | 4110842 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r02_t90_k010_c0_A | 11 | 4110842 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r12_t90_k010_c2_B | 11 | 4110842 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r12_t90_k100_c0_A | 11 | 4110842 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r02_t10_k100_c0_A | 11 | 4110841 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r02_t90_k100_c0_A | 11 | 4110841 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r04_t90_k010_c2_B | 11 | 4110841 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r02_t10_k010_c2_A | 11 | 4110840 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r07_t10_k010_c2_A | 11 | 4110840 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r07_t50_k010_c2_A | 11 | 4110840 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r02_t50_k010_c1_A | 11 | 4110839 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r02_t50_k100_c2_A | 11 | 4110838 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r12_t50_k100_c2_A | 11 | 4110838 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r02_t90_k100_c1_A | 11 | 4110836 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r04_t90_k010_c0_B | 11 | 4110836 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r07_t50_k010_c1_A | 11 | 4110836 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r02_t10_k010_c0_A | 11 | 4110835 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r02_t50_k010_c0_B | 11 | 4110835 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r02_t90_k100_c2_A | 11 | 4110835 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r12_t10_k100_c0_B | 11 | 4110835 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r12_t10_k100_c2_A | 11 | 4110835 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r12_t90_k010_c0_B | 11 | 4110835 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r04_t90_k010_c2_A | 11 | 4110834 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r12_t50_k010_c0_B | 11 | 4110834 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r02_t10_k010_c1_B | 11 | 4110833 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r04_t10_k100_c2_A | 11 | 4110833 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r07_t10_k010_c0_A | 11 | 4110833 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r07_t50_k010_c0_A | 11 | 4110833 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r12_t90_k100_c2_B | 11 | 4110833 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r02_t10_k010_c0_B | 11 | 4110831 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r04_t50_k010_c0_A | 11 | 4110831 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r04_t90_k100_c2_A | 11 | 4110831 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r12_t10_k010_c0_B | 11 | 4110831 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r12_t10_k100_c1_A | 11 | 4110831 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r12_t50_k100_c1_A | 11 | 4110831 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r02_t10_k100_c1_A | 11 | 4110830 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r02_t50_k010_c1_B | 11 | 4110830 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r04_t50_k010_c0_B | 11 | 4110830 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r04_t50_k010_c2_A | 11 | 4110830 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r04_t90_k010_c1_B | 11 | 4110830 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r12_t50_k010_c1_B | 11 | 4110830 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r12_t90_k100_c1_B | 11 | 4110830 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r04_t90_k010_c1_A | 11 | 4110829 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r02_t90_k100_c0_B | 11 | 4110828 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r04_t10_k010_c2_B | 11 | 4110828 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r12_t50_k100_c0_A | 11 | 4110828 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r02_t90_k100_c2_B | 11 | 4110827 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r04_t50_k010_c1_B | 11 | 4110827 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r07_t10_k100_c1_A | 11 | 4110827 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r12_t90_k010_c0_A | 11 | 4110827 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r07_t10_k100_c0_A | 11 | 4110826 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r04_t90_k100_c0_A | 11 | 4110825 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r07_t90_k100_c2_A | 11 | 4110825 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r12_t50_k010_c2_B | 11 | 4110825 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r12_t90_k100_c0_B | 11 | 4110825 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r04_t10_k010_c1_A | 11 | 4110824 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r04_t50_k010_c2_B | 11 | 4110824 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r04_t90_k100_c2_B | 11 | 4110824 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r02_t10_k100_c2_A | 11 | 4110823 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r04_t10_k100_c1_B | 11 | 4110823 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r04_t50_k010_c1_A | 11 | 4110823 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r12_t50_k100_c1_B | 11 | 4110823 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r04_t10_k010_c0_B | 11 | 4110822 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r04_t90_k100_c0_B | 11 | 4110822 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r12_t10_k010_c2_B | 11 | 4110822 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r12_t50_k010_c0_A | 11 | 4110822 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r07_t90_k100_c1_A | 11 | 4110821 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r12_t50_k010_c2_A | 11 | 4110821 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r12_t10_k100_c1_B | 11 | 4110820 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r04_t90_k100_c1_A | 11 | 4110819 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r12_t10_k010_c1_A | 11 | 4110819 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r12_t10_k010_c1_B | 11 | 4110819 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r12_t50_k010_c1_A | 11 | 4110819 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r02_t50_k100_c2_B | 11 | 4110818 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r04_t10_k100_c1_A | 11 | 4110818 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r07_t90_k100_c0_A | 11 | 4110818 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r12_t50_k100_c0_B | 11 | 4110818 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r04_t10_k010_c0_A | 11 | 4110817 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r04_t90_k100_c1_B | 11 | 4110817 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r12_t10_k010_c2_A | 11 | 4110817 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r12_t50_k100_c2_B | 11 | 4110817 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r02_t50_k100_c0_A | 11 | 4110816 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r02_t90_k100_c1_B | 11 | 4110816 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r04_t10_k100_c2_B | 11 | 4110816 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r07_t10_k100_c2_A | 11 | 4110816 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r02_t50_k100_c1_A | 11 | 4110815 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r07_t50_k100_c2_A | 11 | 4110815 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r04_t10_k010_c2_A | 11 | 4110814 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r02_t10_k100_c0_B | 11 | 4110813 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r04_t50_k100_c2_A | 11 | 4110813 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r07_t90_k010_c2_B | 11 | 4110812 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r02_t10_k100_c1_B | 11 | 4110810 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r04_t10_k100_c0_B | 11 | 4110810 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r07_t50_k010_c1_B | 11 | 4110809 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r07_t90_k010_c1_B | 11 | 4110809 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r04_t50_k100_c0_A | 11 | 4110808 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r07_t90_k010_c0_B | 11 | 4110808 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r04_t10_k100_c0_A | 11 | 4110807 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r04_t50_k100_c2_B | 11 | 4110807 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r07_t10_k010_c2_B | 11 | 4110807 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r12_t10_k010_c0_A | 11 | 4110807 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r07_t90_k100_c2_B | 11 | 4110806 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r12_t10_k100_c2_B | 11 | 4110806 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r02_t10_k100_c2_B | 11 | 4110805 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r07_t50_k100_c1_A | 11 | 4110805 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r07_t10_k010_c0_B | 11 | 4110804 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r04_t50_k100_c0_B | 11 | 4110803 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r04_t50_k100_c1_B | 11 | 4110802 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r07_t10_k010_c1_B | 11 | 4110802 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r04_t10_k010_c1_B | 11 | 4110801 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r07_t90_k100_c1_B | 11 | 4110800 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r02_t50_k100_c1_B | 11 | 4110799 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r02_t50_k100_c0_B | 11 | 4110797 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r07_t50_k010_c0_B | 11 | 4110797 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r07_t50_k100_c2_B | 11 | 4110797 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r07_t90_k100_c0_B | 11 | 4110797 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r07_t10_k100_c0_B | 11 | 4110796 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r07_t50_k100_c0_A | 11 | 4110795 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r04_t50_k100_c1_A | 11 | 4110794 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r07_t50_k010_c2_B | 11 | 4110792 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r07_t10_k100_c1_B | 11 | 4110789 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r08_t90_k010_c0_A | 11 | 4110789 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r08_t90_k100_c0_B | 11 | 4110789 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r08_t90_k010_c2_A | 11 | 4110784 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r07_t10_k100_c2_B | 11 | 4110783 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r07_t50_k100_c1_B | 11 | 4110783 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r08_t90_k100_c1_A | 11 | 4110783 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r08_t50_k010_c2_A | 11 | 4110782 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r08_t90_k010_c1_A | 11 | 4110782 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r08_t90_k100_c2_B | 11 | 4110778 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r08_t10_k100_c0_B | 11 | 4110774 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r08_t10_k100_c2_B | 11 | 4110774 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r08_t90_k100_c2_A | 11 | 4110773 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r07_t50_k100_c0_B | 11 | 4110772 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r08_t10_k100_c2_A | 11 | 4110771 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r08_t10_k010_c1_A | 11 | 4110769 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r08_t10_k010_c0_A | 11 | 4110768 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r08_t90_k100_c0_A | 11 | 4110768 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r08_t10_k100_c0_A | 11 | 4110767 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r08_t90_k100_c1_B | 11 | 4110766 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r08_t50_k010_c1_A | 11 | 4110765 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r08_t50_k100_c2_B | 11 | 4110765 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r08_t10_k100_c1_A | 11 | 4110764 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r08_t10_k010_c2_A | 11 | 4110762 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r13_t50_k010_c2_A | 11 | 4110762 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r13_t90_k010_c1_A | 11 | 4110762 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r08_t10_k100_c1_B | 11 | 4110761 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r08_t50_k010_c0_A | 11 | 4110759 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r13_t90_k010_c0_A | 11 | 4110758 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r13_t90_k010_c2_A | 11 | 4110757 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r08_t90_k010_c2_B | 11 | 4110756 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r08_t50_k100_c2_A | 11 | 4110755 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r13_t10_k010_c2_A | 11 | 4110755 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r08_t50_k100_c0_A | 11 | 4110753 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r08_t50_k100_c0_B | 11 | 4110753 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r08_t90_k010_c0_B | 11 | 4110752 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r13_t90_k010_c0_B | 11 | 4110752 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r08_t50_k010_c2_B | 11 | 4110751 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r13_t50_k010_c1_A | 11 | 4110751 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r08_t90_k010_c1_B | 11 | 4110750 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r13_t10_k100_c2_A | 11 | 4110749 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r13_t50_k010_c2_B | 11 | 4110749 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r08_t50_k100_c1_A | 11 | 4110748 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r13_t90_k010_c1_B | 11 | 4110748 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r13_t90_k100_c1_A | 11 | 4110747 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r13_t50_k010_c0_A | 11 | 4110745 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r13_t90_k100_c2_A | 11 | 4110744 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r08_t50_k100_c1_B | 11 | 4110743 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r13_t10_k100_c1_A | 11 | 4110743 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r08_t50_k010_c1_B | 11 | 4110742 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r13_t90_k010_c2_B | 11 | 4110742 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r08_t10_k010_c2_B | 11 | 4110741 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r13_t10_k010_c0_A | 11 | 4110741 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r13_t10_k010_c1_A | 11 | 4110741 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r13_t10_k100_c0_A | 11 | 4110741 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r13_t50_k010_c1_B | 11 | 4110741 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r08_t10_k010_c0_B | 11 | 4110736 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r13_t10_k010_c1_B | 11 | 4110736 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r13_t50_k010_c0_B | 11 | 4110736 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r08_t50_k010_c0_B | 11 | 4110735 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r13_t50_k100_c1_A | 11 | 4110735 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r13_t10_k010_c2_B | 11 | 4110733 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r13_t10_k010_c0_B | 11 | 4110732 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r13_t90_k100_c0_A | 11 | 4110732 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r13_t90_k100_c2_B | 11 | 4110732 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r08_t10_k010_c1_B | 11 | 4110731 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r13_t10_k100_c1_B | 11 | 4110728 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r13_t10_k100_c2_B | 11 | 4110728 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r13_t50_k100_c2_A | 11 | 4110727 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r13_t50_k100_c0_A | 11 | 4110725 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r13_t90_k100_c1_B | 11 | 4110724 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r13_t90_k100_c0_B | 11 | 4110722 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r13_t10_k100_c0_B | 11 | 4110720 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r13_t50_k100_c2_B | 11 | 4110716 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r13_t50_k100_c0_B | 11 | 4110713 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r13_t50_k100_c1_B | 11 | 4110705 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r18_t90_k010_c1_A | 11 | 4110681 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r18_t90_k010_c0_A | 11 | 4110674 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r18_t10_k010_c1_A | 11 | 4110672 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r18_t90_k010_c2_A | 11 | 4110672 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r18_t90_k010_c2_B | 11 | 4110668 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r18_t10_k010_c0_A | 11 | 4110667 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r18_t50_k010_c0_A | 11 | 4110666 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r18_t50_k010_c2_A | 11 | 4110666 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r18_t90_k010_c1_B | 11 | 4110666 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r18_t90_k100_c2_B | 11 | 4110665 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r18_t10_k100_c1_B | 11 | 4110662 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r18_t90_k010_c0_B | 11 | 4110662 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r18_t90_k100_c1_A | 11 | 4110661 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r18_t10_k010_c2_A | 11 | 4110659 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r18_t90_k100_c2_A | 11 | 4110658 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r18_t10_k100_c2_A | 11 | 4110657 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r18_t90_k100_c0_A | 11 | 4110653 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r18_t10_k100_c2_B | 11 | 4110652 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r18_t10_k100_c1_A | 11 | 4110651 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r18_t50_k010_c1_A | 11 | 4110651 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r18_t90_k100_c1_B | 11 | 4110651 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r18_t10_k010_c2_B | 11 | 4110650 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r18_t10_k100_c0_A | 11 | 4110650 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r18_t10_k100_c0_B | 11 | 4110650 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r18_t50_k010_c2_B | 11 | 4110650 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r18_t90_k100_c0_B | 11 | 4110650 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r18_t50_k010_c0_B | 11 | 4110647 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r18_t50_k010_c1_B | 11 | 4110647 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r18_t10_k010_c0_B | 11 | 4110644 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r18_t50_k100_c0_A | 11 | 4110638 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r18_t10_k010_c1_B | 11 | 4110634 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r18_t50_k100_c1_A | 11 | 4110634 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r18_t50_k100_c2_A | 11 | 4110632 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r18_t50_k100_c2_B | 11 | 4110631 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r18_t50_k100_c1_B | 11 | 4110626 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r18_t50_k100_c0_B | 11 | 4110623 |
| journal_validation/stage2g/full_path_validation/results/pilot_002_truth/C | 52 | 4105031 |
| journal_validation/stage2g/full_path_validation/results/pilot_007_truth/C | 52 | 4094132 |
| journal_validation/stage2g/full_path_validation/results/pilot_004_minus/C | 52 | 4078839 |
| journal_validation/stage2g/full_path_validation/results/pilot_003_plus/C | 52 | 4078151 |
| journal_validation/stage2g/full_path_validation/results/pilot_006_minus/C | 52 | 4077477 |
| journal_validation/stage2g/full_path_validation/results/pilot_002_minus/C | 52 | 4076620 |
| journal_validation/stage2g/full_path_validation/results/pilot_014_plus/C | 52 | 4071395 |
| journal_validation/stage2g/end_to_end_certification/results/pilot_002_minus | 33 | 4069830 |
| journal_validation/stage2g/end_to_end_certification/results/pilot_014_truth | 33 | 4069773 |
| journal_validation/stage2g/end_to_end_certification/results/pilot_003_minus | 33 | 4068398 |
| journal_validation/stage2g/full_path_validation/results/pilot_001_minus/C | 52 | 4065000 |
| journal_validation/stage2g/end_to_end_certification/results/pilot_005_minus | 33 | 4064773 |
| journal_validation/stage2g/full_path_validation/results/pilot_005_minus/C | 52 | 4062437 |
| journal_validation/stage2g/full_path_validation/results/pilot_005_truth/C | 52 | 4056636 |
| journal_validation/stage2g/end_to_end_certification/results/pilot_005_truth | 33 | 4056275 |
| journal_validation/stage2g/end_to_end_certification/results/pilot_014_plus | 33 | 4056109 |
| journal_validation/stage2g/full_path_validation/results/pilot_001_plus/C | 52 | 4034244 |
| journal_validation/stage2g/full_path_validation/results/pilot_007_plus/C | 52 | 4032201 |
| thesis_extension/environment/legacy_R343_library/Rcpp/include/Rcpp/module | 21 | 3979753 |
| simulation | 18 | 3966131 |
| journal_validation/stage2g/full_path_validation/results | 24 | 3882269 |
| journal_validation/stage2g/results | 10 | 3704926 |
| journal_article/qa | 17 | 3341944 |
| journal_article/submission/qa/supplement | 39 | 3147321 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r14_t90_k100_c1_B | 40 | 3092396 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r08_t90_k010_c1_B | 40 | 3088965 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r11_t50_k010_c0_B | 40 | 3069806 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r10_t90_k010_c0_A | 40 | 3066124 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r06_t90_k010_c0_B | 40 | 3062873 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r01_t90_k010_c2_A | 40 | 3062772 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r03_t90_k010_c0_B | 40 | 3042829 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r03_t90_k100_c0_B | 40 | 3042133 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r07_t50_k010_c1_A | 40 | 3035737 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r10_t90_k010_c0_B | 40 | 3032620 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r06_t90_k010_c0_A | 40 | 3032158 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r07_t50_k010_c2_B | 40 | 3029697 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r10_t90_k010_c1_A | 40 | 3025242 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r17_t50_k100_c0_A | 40 | 3019602 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r03_t90_k010_c0_A | 40 | 3014036 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r11_t50_k100_c0_A | 40 | 2998208 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r07_t50_k010_c2_A | 40 | 2995741 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r07_t50_k010_c1_B | 40 | 2988558 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r05_t90_k010_c1_B | 40 | 2986033 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r03_t90_k010_c1_A | 40 | 2983452 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r03_t90_k010_c2_B | 40 | 2981860 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r03_t90_k100_c1_A | 40 | 2981121 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r03_t90_k100_c1_B | 40 | 2978294 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r06_t90_k010_c1_B | 40 | 2977133 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r05_t90_k100_c1_A | 40 | 2976224 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r08_t90_k100_c2_B | 40 | 2970662 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r20_t90_k100_c0_B | 40 | 2969761 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r03_t50_k100_c0_B | 40 | 2969676 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r14_t90_k100_c2_B | 40 | 2965730 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r14_t90_k100_c1_A | 40 | 2963478 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r11_t90_k010_c2_A | 40 | 2961893 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r05_t90_k010_c2_B | 40 | 2959032 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r08_t90_k010_c1_A | 40 | 2957533 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r03_t90_k010_c2_A | 40 | 2957522 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r17_t90_k100_c0_B | 40 | 2953902 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r05_t90_k100_c1_B | 40 | 2953496 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r14_t90_k010_c1_A | 40 | 2950881 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r13_t90_k010_c0_B | 40 | 2946580 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r11_t50_k100_c0_B | 40 | 2944311 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r04_t90_k100_c2_B | 40 | 2941331 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r07_t90_k100_c1_A | 40 | 2940603 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r05_t50_k010_c2_B | 40 | 2936117 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r01_t90_k010_c2_B | 40 | 2936003 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r15_t90_k010_c1_A | 40 | 2935449 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r14_t50_k100_c1_A | 40 | 2934853 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r15_t90_k010_c0_B | 40 | 2932548 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r03_t50_k010_c2_A | 40 | 2931711 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r03_t90_k100_c2_A | 40 | 2931558 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r03_t90_k100_c0_A | 40 | 2931275 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r17_t90_k010_c0_A | 40 | 2925265 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r03_t50_k010_c1_B | 40 | 2923743 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r05_t50_k100_c0_B | 40 | 2923124 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r17_t90_k100_c1_A | 40 | 2921988 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r11_t90_k010_c2_B | 40 | 2921317 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r05_t50_k100_c0_A | 40 | 2921183 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r10_t90_k100_c1_B | 40 | 2920573 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r20_t90_k010_c2_B | 40 | 2919061 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r08_t90_k100_c2_A | 40 | 2916812 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r19_t90_k100_c0_A | 40 | 2916632 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r20_t90_k100_c1_B | 40 | 2914616 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r15_t90_k100_c1_B | 40 | 2913291 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r08_t50_k010_c1_B | 40 | 2912941 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r16_t90_k010_c2_B | 40 | 2911678 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r11_t50_k010_c0_A | 40 | 2909855 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r05_t90_k010_c1_A | 40 | 2908182 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r13_t90_k010_c0_A | 40 | 2906701 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r08_t50_k010_c2_B | 40 | 2905373 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r17_t90_k100_c0_A | 40 | 2904079 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r19_t90_k100_c0_B | 40 | 2903426 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r09_t50_k010_c1_A | 40 | 2903347 |
| journal_validation/stage2g/results/pilot_014_minus | 6 | 2902499 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r05_t90_k010_c2_A | 40 | 2897858 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r20_t90_k100_c1_A | 40 | 2897143 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r13_t50_k010_c0_B | 40 | 2896686 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r03_t50_k100_c0_A | 40 | 2895617 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r11_t90_k100_c0_B | 40 | 2895182 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r03_t50_k010_c2_B | 40 | 2894891 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r07_t90_k100_c1_B | 40 | 2894520 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r03_t50_k010_c1_A | 40 | 2894051 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r07_t50_k010_c0_A | 40 | 2891144 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r15_t50_k010_c1_A | 40 | 2891025 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r06_t90_k010_c2_B | 40 | 2889771 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r13_t90_k100_c1_A | 40 | 2888658 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r02_t90_k010_c0_B | 40 | 2887007 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r09_t90_k010_c1_A | 40 | 2886150 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r06_t90_k010_c1_A | 40 | 2885689 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r14_t90_k010_c1_B | 40 | 2883819 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r13_t90_k100_c1_B | 40 | 2883190 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r17_t90_k010_c0_B | 40 | 2881620 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r08_t50_k010_c1_A | 40 | 2881532 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r08_t90_k010_c2_B | 40 | 2881524 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r13_t90_k100_c0_A | 40 | 2881260 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r09_t50_k010_c1_B | 40 | 2879913 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r02_t90_k010_c2_A | 40 | 2879536 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r03_t90_k010_c1_B | 40 | 2879093 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r06_t90_k100_c0_A | 40 | 2878821 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r13_t90_k010_c1_B | 40 | 2878350 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r09_t90_k010_c1_B | 40 | 2878286 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r06_t50_k010_c0_A | 40 | 2877995 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r10_t50_k010_c2_B | 40 | 2875515 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r19_t50_k010_c0_A | 40 | 2875178 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r15_t90_k100_c1_A | 40 | 2874400 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r10_t90_k100_c0_B | 40 | 2874058 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r15_t90_k010_c1_B | 40 | 2872736 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r14_t90_k010_c2_B | 40 | 2872260 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r03_t50_k010_c0_B | 40 | 2871665 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r06_t90_k100_c0_B | 40 | 2871636 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r11_t90_k100_c2_B | 40 | 2871244 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r15_t90_k100_c0_A | 40 | 2869774 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r12_t90_k100_c2_A | 40 | 2869566 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r12_t90_k010_c2_B | 40 | 2869380 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r08_t50_k010_c0_A | 40 | 2869017 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r05_t90_k100_c0_A | 40 | 2868611 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r17_t50_k010_c2_A | 40 | 2867964 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r08_t50_k010_c0_B | 40 | 2867281 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r13_t90_k100_c2_B | 40 | 2867125 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r05_t50_k010_c0_A | 40 | 2867032 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r20_t90_k010_c2_A | 40 | 2866684 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r01_t90_k010_c1_A | 40 | 2865745 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r15_t90_k100_c2_A | 40 | 2865732 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r04_t90_k100_c2_A | 40 | 2865205 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r14_t90_k100_c0_B | 40 | 2864989 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r20_t90_k010_c1_A | 40 | 2864286 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r07_t90_k100_c2_A | 40 | 2862184 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r17_t90_k010_c2_A | 40 | 2861675 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r14_t90_k100_c0_A | 40 | 2860684 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r07_t90_k010_c2_A | 40 | 2859267 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r07_t90_k010_c1_A | 40 | 2858913 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r11_t90_k100_c2_A | 40 | 2857298 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r05_t50_k010_c2_A | 40 | 2857070 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r15_t50_k010_c2_A | 40 | 2855926 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r10_t50_k010_c2_A | 40 | 2854667 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r06_t90_k010_c2_A | 40 | 2854292 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r15_t90_k100_c0_B | 40 | 2851800 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r20_t90_k100_c2_B | 40 | 2851229 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r13_t90_k010_c1_A | 40 | 2850541 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r09_t50_k100_c2_A | 40 | 2849753 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r04_t90_k010_c2_B | 40 | 2849696 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r11_t90_k010_c1_A | 40 | 2848125 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r03_t90_k100_c2_B | 40 | 2844840 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r07_t50_k100_c0_B | 40 | 2844531 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r01_t90_k010_c1_B | 40 | 2844288 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r05_t10_k100_c2_B | 40 | 2844029 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r07_t90_k100_c0_B | 40 | 2842262 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r12_t90_k100_c2_B | 40 | 2841536 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r05_t90_k010_c0_A | 40 | 2841167 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r07_t90_k010_c1_B | 40 | 2841134 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r13_t50_k010_c0_A | 40 | 2840649 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r08_t90_k010_c0_B | 40 | 2840353 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r09_t90_k010_c0_A | 40 | 2840165 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r02_t90_k010_c1_B | 40 | 2840163 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r17_t50_k100_c0_B | 40 | 2839228 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r08_t50_k010_c2_A | 40 | 2838096 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r07_t50_k100_c2_B | 40 | 2837926 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r05_t50_k100_c2_B | 40 | 2837750 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r08_t90_k010_c2_A | 40 | 2836398 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r20_t50_k100_c0_B | 40 | 2832644 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r05_t50_k100_c1_B | 40 | 2832112 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r04_t50_k010_c2_A | 40 | 2829185 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r20_t90_k100_c0_A | 40 | 2829108 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r01_t50_k100_c0_A | 40 | 2826785 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r07_t90_k010_c2_B | 40 | 2826257 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r09_t50_k100_c2_B | 40 | 2825478 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r08_t90_k100_c1_A | 40 | 2824508 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r09_t50_k100_c0_B | 40 | 2823800 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r18_t50_k010_c0_A | 40 | 2823166 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r07_t50_k100_c1_A | 40 | 2822499 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r12_t90_k010_c0_B | 40 | 2822428 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r19_t50_k010_c0_B | 40 | 2821928 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r14_t90_k100_c2_A | 40 | 2819576 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r12_t50_k010_c2_B | 40 | 2818689 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r10_t50_k010_c1_B | 40 | 2817403 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r16_t90_k010_c1_A | 40 | 2817154 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r05_t50_k010_c0_B | 40 | 2815719 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r12_t50_k010_c1_B | 40 | 2815683 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r11_t90_k100_c0_A | 40 | 2815413 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r17_t90_k100_c2_B | 40 | 2815119 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r01_t50_k010_c2_A | 40 | 2814380 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r19_t10_k100_c0_B | 40 | 2814140 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r05_t10_k100_c2_A | 40 | 2813935 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r10_t50_k100_c2_A | 40 | 2813364 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r02_t90_k010_c0_A | 40 | 2813057 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r04_t90_k010_c0_B | 40 | 2811279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r17_t90_k010_c2_B | 40 | 2811270 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r07_t50_k010_c0_B | 40 | 2810454 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r17_t10_k010_c1_A | 40 | 2810280 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r14_t90_k010_c0_B | 40 | 2809635 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r05_t50_k010_c1_A | 40 | 2809414 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r01_t50_k100_c2_A | 40 | 2809362 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r03_t50_k100_c2_B | 40 | 2809354 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r20_t90_k010_c0_B | 40 | 2808826 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r02_t90_k100_c2_B | 40 | 2808736 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r10_t90_k010_c1_B | 40 | 2807755 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r20_t90_k010_c1_B | 40 | 2807265 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r17_t90_k100_c2_A | 40 | 2805727 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r12_t90_k100_c1_B | 40 | 2805457 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r05_t90_k100_c0_B | 40 | 2805237 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r15_t90_k010_c2_A | 40 | 2804437 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r15_t90_k010_c0_A | 40 | 2803835 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r11_t90_k010_c1_B | 40 | 2803412 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r01_t90_k100_c0_A | 40 | 2803201 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r10_t90_k100_c0_A | 40 | 2802640 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r03_t50_k100_c1_B | 40 | 2802372 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r10_t50_k100_c1_A | 40 | 2801086 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r02_t90_k100_c0_B | 40 | 2799212 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r02_t90_k010_c2_B | 40 | 2798861 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r07_t50_k100_c0_A | 40 | 2797924 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r08_t90_k010_c0_A | 40 | 2796711 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r10_t50_k100_c0_B | 40 | 2796617 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r09_t90_k100_c2_A | 40 | 2796358 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r07_t90_k100_c0_A | 40 | 2796057 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r16_t90_k010_c2_A | 40 | 2795990 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r16_t90_k100_c1_A | 40 | 2795970 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r13_t90_k100_c0_B | 40 | 2795699 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r01_t50_k100_c0_B | 40 | 2795586 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r11_t50_k010_c2_B | 40 | 2795309 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r04_t50_k100_c0_B | 40 | 2794517 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r08_t50_k100_c1_B | 40 | 2794341 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r11_t50_k010_c1_B | 40 | 2794286 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r16_t90_k100_c2_B | 40 | 2794195 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r16_t90_k100_c0_A | 40 | 2793617 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r18_t50_k010_c0_B | 40 | 2793055 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r17_t90_k010_c1_A | 40 | 2791472 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r09_t50_k100_c1_A | 40 | 2791110 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r17_t50_k010_c0_B | 40 | 2790394 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r09_t50_k100_c1_B | 40 | 2789673 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r12_t50_k010_c1_A | 40 | 2788332 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r18_t90_k100_c2_A | 40 | 2788313 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r19_t90_k010_c1_B | 40 | 2788035 |
| journal_validation/stage2h/readiness/results/parallel/n500_t50_k010 | 40 | 2787809 |
| journal_validation/stage2h/readiness/results/sequential/n500_t50_k010 | 40 | 2787808 |
| journal_validation/stage2h/readiness/results/repeat/n500_t50_k010 | 40 | 2787806 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r12_t90_k010_c0_A | 40 | 2786136 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r05_t90_k010_c0_B | 40 | 2786126 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r12_t90_k010_c1_A | 40 | 2786012 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r17_t50_k010_c1_A | 40 | 2785839 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r09_t50_k010_c2_B | 40 | 2785651 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r01_t50_k010_c0_B | 40 | 2785374 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r17_t50_k010_c2_B | 40 | 2784870 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r07_t90_k100_c2_B | 40 | 2784360 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r13_t50_k010_c2_A | 40 | 2784359 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r11_t90_k100_c1_A | 40 | 2783614 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r06_t50_k100_c1_B | 40 | 2783482 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r07_t50_k100_c1_B | 40 | 2782184 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r19_t90_k100_c1_B | 40 | 2781701 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r11_t50_k100_c1_B | 40 | 2781570 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r02_t50_k010_c2_B | 40 | 2781356 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r13_t50_k010_c1_B | 40 | 2781252 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r15_t50_k010_c2_B | 40 | 2781138 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r12_t50_k010_c0_A | 40 | 2780265 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r04_t90_k010_c2_A | 40 | 2780173 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r12_t50_k010_c0_B | 40 | 2779006 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r05_t50_k100_c1_A | 40 | 2778669 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r03_t50_k100_c1_A | 40 | 2778536 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r20_t90_k010_c0_A | 40 | 2778431 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r13_t90_k100_c2_A | 40 | 2777251 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r15_t90_k010_c2_B | 40 | 2777051 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r09_t50_k010_c0_A | 40 | 2775022 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r08_t90_k100_c0_B | 40 | 2774763 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r13_t90_k010_c2_A | 40 | 2774583 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r13_t50_k100_c1_A | 40 | 2774457 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r06_t50_k010_c1_B | 40 | 2772774 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r07_t50_k100_c2_A | 40 | 2772470 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r04_t50_k010_c0_B | 40 | 2772354 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r14_t50_k100_c0_B | 40 | 2771763 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r20_t50_k010_c1_B | 40 | 2771696 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r11_t50_k010_c2_A | 40 | 2771319 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r17_t50_k010_c0_A | 40 | 2771195 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r04_t90_k010_c0_A | 40 | 2769967 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r14_t90_k010_c2_A | 40 | 2769777 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r03_t10_k010_c2_B | 40 | 2768977 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r20_t50_k100_c0_A | 40 | 2768729 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r05_t10_k100_c1_A | 40 | 2768723 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r06_t50_k010_c0_B | 40 | 2768198 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r12_t50_k100_c0_A | 40 | 2767364 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r05_t10_k010_c1_B | 40 | 2766973 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r14_t90_k010_c0_A | 40 | 2765918 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r01_t90_k100_c1_A | 40 | 2765049 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r02_t90_k100_c2_A | 40 | 2765036 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r15_t90_k100_c2_B | 40 | 2764576 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r01_t90_k100_c1_B | 40 | 2764129 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r08_t50_k100_c1_A | 40 | 2763944 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r12_t90_k010_c2_A | 40 | 2763671 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r16_t90_k100_c1_B | 40 | 2762806 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r13_t50_k010_c1_A | 40 | 2761045 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r09_t90_k010_c0_B | 40 | 2760978 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r06_t50_k010_c2_B | 40 | 2760905 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r17_t10_k010_c1_B | 40 | 2760736 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r10_t50_k100_c2_B | 40 | 2756927 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r17_t90_k010_c1_B | 40 | 2756088 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r06_t50_k010_c2_A | 40 | 2755352 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r19_t10_k100_c0_A | 40 | 2755190 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r11_t10_k100_c2_B | 40 | 2754429 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r02_t50_k100_c0_A | 40 | 2754388 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r01_t90_k100_c2_A | 40 | 2754000 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r07_t90_k010_c0_B | 40 | 2753928 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r04_t90_k100_c1_A | 40 | 2753856 |
| journal_validation/stage2g/results/pilot_014_truth | 6 | 2753629 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r04_t90_k100_c1_B | 40 | 2753506 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r02_t10_k010_c2_B | 40 | 2753085 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r20_t50_k010_c0_B | 40 | 2752207 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r02_t90_k010_c1_A | 40 | 2751235 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r05_t10_k100_c0_B | 40 | 2749820 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r14_t50_k010_c1_B | 40 | 2748715 |
| journal_validation/stage2g/results/pilot_003_minus | 6 | 2747786 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r02_t10_k100_c0_B | 40 | 2746746 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r09_t90_k100_c0_A | 40 | 2745895 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r01_t50_k100_c1_B | 40 | 2745256 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r01_t50_k010_c2_B | 40 | 2745173 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r16_t90_k100_c0_B | 40 | 2745046 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r11_t50_k010_c1_A | 40 | 2743870 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r14_t50_k010_c1_A | 40 | 2743560 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r06_t90_k100_c1_B | 40 | 2743533 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r09_t50_k010_c0_B | 40 | 2742598 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r10_t90_k100_c1_A | 40 | 2741768 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r01_t50_k100_c2_B | 40 | 2741541 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r17_t10_k010_c2_A | 40 | 2740845 |
| thesis_extension/environment/legacy_R343_library/Rcpp/doc | 31 | 2740176 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r04_t90_k010_c1_A | 40 | 2738946 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r02_t50_k010_c2_A | 40 | 2738430 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r14_t50_k100_c2_B | 40 | 2736649 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r10_t50_k010_c1_A | 40 | 2735911 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r13_t50_k100_c0_B | 40 | 2735134 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r04_t50_k100_c0_A | 40 | 2734804 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r20_t10_k100_c1_A | 40 | 2734010 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r01_t90_k010_c0_B | 40 | 2733413 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r13_t50_k100_c0_A | 40 | 2732506 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r03_t50_k010_c0_A | 40 | 2732503 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r14_t50_k100_c2_A | 40 | 2731293 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r16_t50_k100_c0_A | 40 | 2729120 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r12_t50_k010_c2_A | 40 | 2728784 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r18_t50_k100_c0_B | 40 | 2728610 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r04_t10_k100_c2_B | 40 | 2728480 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r05_t50_k010_c1_B | 40 | 2728160 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r13_t50_k100_c2_B | 40 | 2727500 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r06_t50_k010_c1_A | 40 | 2727293 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r02_t50_k010_c0_B | 40 | 2727137 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r04_t50_k010_c0_A | 40 | 2726897 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r11_t50_k100_c2_A | 40 | 2726784 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r09_t90_k010_c2_A | 40 | 2726779 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r10_t50_k010_c0_A | 40 | 2725755 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r17_t50_k100_c1_A | 40 | 2725142 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r18_t90_k100_c2_B | 40 | 2724882 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r02_t50_k010_c0_A | 40 | 2723970 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r20_t50_k010_c1_A | 40 | 2723634 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r17_t50_k100_c1_B | 40 | 2723225 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r14_t50_k010_c0_B | 40 | 2723112 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r10_t90_k010_c2_A | 40 | 2723046 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r09_t90_k100_c1_A | 40 | 2722972 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r08_t90_k100_c1_B | 40 | 2722416 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r11_t10_k010_c2_B | 40 | 2721570 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r13_t90_k010_c2_B | 40 | 2721470 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r02_t10_k010_c2_A | 40 | 2721318 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r04_t50_k010_c1_A | 40 | 2720666 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r11_t10_k010_c1_B | 40 | 2720615 |
| journal_validation/stage2c/validation_protocol/reassessment_20261029T083111Z | 17 | 2720296 |
| journal_validation/stage2h/readiness/results/sequential/n500_t90_k010 | 40 | 2719686 |
| journal_validation/stage2h/readiness/results/parallel/n500_t90_k010 | 40 | 2719683 |
| journal_validation/stage2h/readiness/results/repeat/n500_t90_k010 | 40 | 2719683 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r01_t90_k100_c0_B | 40 | 2718662 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r12_t90_k100_c1_A | 40 | 2716874 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r11_t10_k010_c1_A | 40 | 2716820 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r03_t10_k010_c2_A | 40 | 2716693 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r14_t50_k010_c0_A | 40 | 2715841 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r09_t90_k100_c2_B | 40 | 2715532 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r01_t50_k100_c1_A | 40 | 2715470 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r11_t10_k010_c2_A | 40 | 2715393 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r12_t50_k100_c2_A | 40 | 2715367 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r02_t90_k100_c0_A | 40 | 2714998 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r01_t90_k100_c2_B | 40 | 2714829 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r05_t10_k100_c0_A | 40 | 2714471 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r10_t90_k010_c2_B | 40 | 2714096 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r14_t50_k100_c0_A | 40 | 2713959 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r12_t90_k100_c0_B | 40 | 2713579 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r18_t90_k100_c0_A | 40 | 2712987 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r05_t90_k100_c2_B | 40 | 2712701 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r11_t10_k100_c2_A | 40 | 2712601 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r08_t50_k100_c2_B | 40 | 2711990 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r04_t50_k010_c1_B | 40 | 2711302 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r08_t90_k100_c0_A | 40 | 2711089 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r19_t50_k010_c1_B | 40 | 2709962 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r11_t50_k100_c2_B | 40 | 2709768 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r11_t90_k100_c1_B | 40 | 2709197 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r05_t10_k010_c2_B | 40 | 2707653 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r12_t90_k010_c1_B | 40 | 2707457 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r14_t10_k100_c1_B | 40 | 2706721 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r02_t90_k100_c1_B | 40 | 2706532 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r01_t50_k010_c1_A | 40 | 2706297 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r08_t50_k100_c0_A | 40 | 2704817 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r18_t50_k100_c1_B | 40 | 2704215 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r14_t10_k100_c1_A | 40 | 2703111 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r19_t50_k100_c1_B | 40 | 2702574 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r19_t10_k100_c1_A | 40 | 2702380 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r08_t50_k100_c0_B | 40 | 2702185 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r01_t90_k010_c0_A | 40 | 2701582 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r02_t50_k100_c2_B | 40 | 2701240 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r06_t50_k100_c2_A | 40 | 2699993 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r02_t50_k010_c1_A | 40 | 2699629 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r20_t90_k100_c2_A | 40 | 2699309 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r19_t90_k010_c1_A | 40 | 2699081 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r07_t10_k010_c2_A | 40 | 2697707 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r02_t10_k010_c0_B | 40 | 2697159 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r03_t50_k100_c2_A | 40 | 2697006 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r07_t90_k010_c0_A | 40 | 2696463 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r10_t50_k010_c0_B | 40 | 2696103 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r04_t50_k010_c2_B | 40 | 2695344 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r06_t50_k100_c1_A | 40 | 2695098 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r09_t90_k010_c2_B | 40 | 2695072 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r06_t50_k100_c0_B | 40 | 2694812 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r15_t50_k010_c1_B | 40 | 2694696 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r19_t90_k010_c0_B | 40 | 2694654 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r02_t50_k100_c1_B | 40 | 2694130 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r05_t50_k100_c2_A | 40 | 2694023 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r06_t10_k010_c0_A | 40 | 2694020 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r19_t50_k100_c0_B | 40 | 2693660 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r07_t10_k010_c0_A | 40 | 2692448 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r05_t10_k010_c1_A | 40 | 2691839 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r10_t50_k100_c1_B | 40 | 2691376 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r20_t50_k010_c2_B | 40 | 2687472 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r04_t90_k100_c0_B | 40 | 2686675 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r05_t10_k010_c2_A | 40 | 2686605 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r17_t10_k010_c2_B | 40 | 2685748 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r12_t50_k100_c0_B | 40 | 2685664 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r04_t90_k010_c1_B | 40 | 2685631 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r14_t50_k010_c2_A | 40 | 2685405 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r09_t50_k100_c0_A | 40 | 2684738 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r08_t50_k100_c2_A | 40 | 2684033 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r07_t10_k100_c0_B | 40 | 2683850 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r14_t50_k100_c1_B | 40 | 2683462 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r18_t90_k100_c1_A | 40 | 2683217 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r20_t50_k010_c2_A | 40 | 2682461 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r19_t50_k100_c1_A | 40 | 2681345 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r07_t10_k100_c2_B | 40 | 2681086 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r02_t90_k100_c1_A | 40 | 2681004 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r05_t90_k100_c2_A | 40 | 2680882 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r18_t10_k010_c1_A | 40 | 2680018 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r01_t50_k010_c1_B | 40 | 2679069 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r17_t10_k100_c1_A | 40 | 2678629 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r16_t90_k010_c1_B | 40 | 2678254 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r15_t10_k010_c0_A | 40 | 2678172 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r18_t90_k100_c0_B | 40 | 2677945 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r17_t90_k100_c1_B | 40 | 2677460 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r07_t10_k010_c1_A | 40 | 2676550 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r16_t90_k100_c2_A | 40 | 2675648 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r17_t10_k100_c2_B | 40 | 2675469 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r10_t50_k100_c0_A | 40 | 2675433 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r20_t50_k010_c0_A | 40 | 2673646 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r06_t10_k100_c0_A | 40 | 2673397 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r14_t10_k100_c2_B | 40 | 2673129 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r11_t50_k100_c1_A | 40 | 2673102 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r12_t50_k100_c1_B | 40 | 2672379 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r09_t50_k010_c2_A | 40 | 2672108 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r14_t10_k100_c2_A | 40 | 2672065 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r04_t50_k100_c1_A | 40 | 2671714 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r02_t50_k010_c1_B | 40 | 2671017 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r06_t50_k100_c2_B | 40 | 2670767 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r04_t50_k100_c1_B | 40 | 2670064 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r13_t50_k010_c2_B | 40 | 2669523 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r06_t90_k100_c2_B | 40 | 2667277 |
| journal_validation/stage2g/results/pilot_003_truth | 6 | 2663618 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r09_t90_k100_c0_B | 40 | 2663309 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r16_t90_k010_c0_B | 40 | 2662423 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r04_t90_k100_c0_A | 40 | 2661892 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r09_t90_k100_c1_B | 40 | 2661290 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r19_t90_k010_c2_A | 40 | 2660506 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r03_t10_k100_c1_A | 40 | 2660474 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r11_t10_k100_c1_B | 40 | 2660386 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r07_t10_k100_c2_A | 40 | 2658701 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r05_t10_k100_c1_B | 40 | 2657995 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r11_t90_k010_c0_B | 40 | 2657201 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r14_t50_k010_c2_B | 40 | 2655855 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r18_t50_k010_c1_B | 40 | 2654333 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r17_t10_k100_c0_B | 40 | 2653239 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r20_t50_k100_c1_A | 40 | 2653221 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r15_t10_k010_c2_B | 40 | 2652461 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r02_t10_k100_c0_A | 40 | 2652287 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r05_t10_k010_c0_A | 40 | 2651772 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r15_t10_k010_c2_A | 40 | 2650567 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r17_t50_k010_c1_B | 40 | 2650160 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r02_t50_k100_c0_B | 40 | 2649496 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r13_t50_k100_c1_B | 40 | 2647570 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r02_t10_k100_c1_B | 40 | 2645859 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r08_t10_k010_c2_A | 40 | 2645291 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r15_t50_k100_c2_A | 40 | 2644794 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r19_t90_k010_c0_A | 40 | 2643365 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r10_t10_k100_c0_B | 40 | 2643269 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r20_t50_k100_c1_B | 40 | 2643171 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r12_t90_k100_c0_A | 40 | 2642597 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r13_t50_k100_c2_A | 40 | 2641823 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r15_t50_k100_c2_B | 40 | 2641552 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r07_t10_k010_c2_B | 40 | 2640860 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r14_t10_k100_c0_B | 40 | 2640322 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r09_t10_k100_c1_B | 40 | 2640140 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r11_t10_k010_c0_A | 40 | 2639863 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r19_t90_k100_c1_A | 40 | 2639186 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r09_t10_k100_c0_B | 40 | 2638863 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r04_t10_k100_c2_A | 40 | 2638589 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r19_t90_k010_c2_B | 40 | 2637307 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r10_t10_k100_c2_A | 40 | 2637206 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r19_t10_k010_c1_B | 40 | 2637069 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r20_t10_k010_c2_A | 40 | 2635801 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r18_t10_k100_c2_B | 40 | 2634908 |
| journal_validation/stage2h/readiness/results/sequential/n500_t50_k100 | 40 | 2634726 |
| journal_validation/stage2h/readiness/results/parallel/n500_t50_k100 | 40 | 2634723 |
| journal_validation/stage2h/readiness/results/repeat/n500_t50_k100 | 40 | 2634722 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r11_t90_k010_c0_A | 40 | 2634550 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r18_t10_k100_c2_A | 40 | 2632873 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r03_t10_k010_c1_A | 40 | 2632508 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r16_t50_k010_c1_A | 40 | 2632290 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r15_t50_k010_c0_B | 40 | 2631801 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r06_t90_k100_c1_A | 40 | 2631069 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r06_t10_k100_c0_B | 40 | 2630078 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r19_t50_k010_c2_B | 40 | 2628826 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r20_t10_k100_c0_B | 40 | 2628202 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r04_t50_k100_c2_B | 40 | 2626931 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r12_t50_k100_c2_B | 40 | 2626753 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r17_t10_k100_c0_A | 40 | 2625238 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r04_t50_k100_c2_A | 40 | 2624953 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r18_t50_k010_c2_B | 40 | 2624692 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r16_t50_k100_c2_B | 40 | 2623901 |
| journal_validation/stage2g/results/pilot_005_plus | 6 | 2623089 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r18_t10_k010_c2_B | 40 | 2623019 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r17_t10_k100_c1_B | 40 | 2622277 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r19_t10_k100_c1_B | 40 | 2622068 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r18_t50_k100_c0_A | 40 | 2620279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r15_t10_k100_c1_A | 40 | 2619500 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r18_t10_k100_c1_A | 40 | 2619267 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r10_t10_k010_c2_A | 40 | 2618696 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r17_t50_k100_c2_B | 40 | 2618120 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r16_t50_k100_c0_B | 40 | 2617492 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r12_t50_k100_c1_A | 40 | 2616884 |
| journal_validation/stage2g/results/pilot_006_plus | 6 | 2616371 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r18_t10_k100_c1_B | 40 | 2616214 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r17_t50_k100_c2_A | 40 | 2616066 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r09_t10_k100_c1_A | 40 | 2615744 |
| journal_validation/stage2g/results/pilot_004_plus | 6 | 2614941 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r07_t10_k100_c0_A | 40 | 2614812 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r07_t10_k100_c1_B | 40 | 2613175 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r08_t10_k100_c2_B | 40 | 2612796 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r09_t10_k010_c2_B | 40 | 2612122 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r11_t10_k100_c0_B | 40 | 2612068 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r02_t50_k100_c1_A | 40 | 2611548 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r18_t90_k010_c1_A | 40 | 2610554 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r18_t90_k010_c1_B | 40 | 2609937 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r10_t90_k100_c2_B | 40 | 2608981 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r02_t10_k010_c1_B | 40 | 2608273 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r19_t50_k010_c1_A | 40 | 2608092 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r10_t90_k100_c2_A | 40 | 2607563 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r19_t10_k010_c0_B | 40 | 2606450 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r05_t10_k010_c0_B | 40 | 2606317 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r06_t50_k100_c0_A | 40 | 2605172 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r10_t10_k100_c0_A | 40 | 2603128 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r08_t10_k100_c2_A | 40 | 2602985 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r03_t10_k100_c2_B | 40 | 2602772 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r16_t50_k010_c0_A | 40 | 2602711 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r08_t10_k100_c0_B | 40 | 2601633 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r18_t10_k010_c0_B | 40 | 2600436 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r06_t10_k100_c1_A | 40 | 2598837 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r18_t90_k100_c1_B | 40 | 2598373 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r20_t10_k100_c1_B | 40 | 2598182 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r18_t50_k010_c1_A | 40 | 2597768 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r19_t50_k010_c2_A | 40 | 2597675 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r07_t10_k010_c0_B | 40 | 2596905 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r19_t10_k100_c2_B | 40 | 2596788 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r10_t10_k010_c0_A | 40 | 2595970 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r15_t10_k100_c1_B | 40 | 2595696 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r19_t10_k100_c2_A | 40 | 2595056 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r07_t10_k100_c1_A | 40 | 2594223 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r15_t10_k010_c1_A | 40 | 2592630 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r06_t90_k100_c2_A | 40 | 2592294 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r08_t10_k010_c2_B | 40 | 2592236 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r14_t10_k010_c1_B | 40 | 2591648 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r16_t50_k100_c1_A | 40 | 2591089 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r18_t50_k100_c1_A | 40 | 2590149 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r02_t10_k100_c1_A | 40 | 2589664 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r19_t50_k100_c0_A | 40 | 2587466 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r06_t10_k010_c2_A | 40 | 2587038 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r13_t10_k010_c2_A | 40 | 2586218 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r18_t50_k100_c2_A | 40 | 2586070 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r19_t90_k100_c2_A | 40 | 2585860 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r08_t10_k010_c0_A | 40 | 2585405 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r19_t90_k100_c2_B | 40 | 2583968 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r03_t10_k100_c0_A | 40 | 2583866 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r09_t10_k010_c0_B | 40 | 2581565 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r16_t90_k010_c0_A | 40 | 2580836 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r13_t10_k100_c2_A | 40 | 2579848 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r18_t90_k010_c0_B | 40 | 2579845 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r16_t50_k010_c0_B | 40 | 2579306 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r02_t10_k100_c2_A | 40 | 2578938 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r18_t10_k100_c0_B | 40 | 2578161 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r03_t10_k010_c1_B | 40 | 2577868 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r15_t50_k100_c0_A | 40 | 2577827 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r18_t50_k010_c2_A | 40 | 2577514 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r06_t10_k010_c0_B | 40 | 2576022 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r18_t90_k010_c2_A | 40 | 2576018 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r03_t10_k100_c2_A | 40 | 2573535 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r19_t10_k010_c0_A | 40 | 2572894 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r20_t10_k100_c0_A | 40 | 2571834 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r18_t90_k010_c0_A | 40 | 2571771 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r17_t10_k100_c2_A | 40 | 2569381 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r03_t10_k100_c1_B | 40 | 2569119 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r14_t10_k010_c1_A | 40 | 2569095 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r18_t10_k010_c2_A | 40 | 2568823 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r04_t10_k100_c0_B | 40 | 2568017 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r08_t10_k100_c1_B | 40 | 2567264 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r16_t10_k010_c0_B | 40 | 2566983 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r17_t10_k010_c0_A | 40 | 2566814 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r19_t50_k100_c2_A | 40 | 2565976 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r18_t50_k100_c2_B | 40 | 2563989 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r13_t10_k010_c1_B | 40 | 2561862 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r02_t50_k100_c2_A | 40 | 2561394 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r20_t50_k100_c2_B | 40 | 2560255 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r09_t10_k010_c2_A | 40 | 2559752 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r07_t10_k010_c1_B | 40 | 2559597 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r18_t90_k010_c2_B | 40 | 2558921 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r09_t10_k010_c0_A | 40 | 2558059 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r11_t10_k100_c0_A | 40 | 2557111 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r04_t10_k010_c2_A | 40 | 2556791 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r10_t10_k100_c2_B | 40 | 2553556 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r02_t10_k010_c1_A | 40 | 2550665 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r02_t10_k010_c0_A | 40 | 2550213 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r01_t50_k010_c0_A | 40 | 2549295 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r11_t10_k100_c1_A | 40 | 2549076 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r10_t10_k010_c0_B | 40 | 2548654 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r15_t10_k010_c0_B | 40 | 2547111 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r12_t10_k100_c0_B | 40 | 2546550 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r16_t50_k010_c1_B | 40 | 2545461 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r18_t10_k010_c1_B | 40 | 2545133 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r19_t50_k100_c2_B | 40 | 2544645 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r15_t50_k010_c0_A | 40 | 2543138 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r06_t10_k100_c2_A | 40 | 2542752 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r15_t10_k010_c1_B | 40 | 2542598 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r03_t10_k010_c0_A | 40 | 2540329 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r09_t10_k010_c1_B | 40 | 2540104 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r11_t10_k010_c0_B | 40 | 2539317 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r06_t10_k100_c1_B | 40 | 2539209 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r15_t10_k100_c0_A | 40 | 2539139 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r06_t10_k010_c2_B | 40 | 2538420 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r16_t50_k100_c2_A | 40 | 2537875 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r08_t10_k010_c0_B | 40 | 2533133 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r03_t10_k100_c0_B | 40 | 2531722 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r15_t10_k100_c2_A | 40 | 2530918 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r14_t10_k100_c0_A | 40 | 2529866 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r20_t10_k010_c1_A | 40 | 2529235 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r13_t10_k100_c1_B | 40 | 2528677 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r20_t10_k100_c2_B | 40 | 2527945 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r18_t10_k100_c0_A | 40 | 2527776 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r15_t50_k100_c0_B | 40 | 2527582 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r13_t10_k100_c1_A | 40 | 2527455 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r01_t10_k100_c1_A | 40 | 2526848 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r09_t10_k100_c2_B | 40 | 2526219 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r01_t10_k100_c0_A | 40 | 2524892 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r20_t10_k010_c2_B | 40 | 2524464 |
| journal_validation/stage2h/readiness/results/parallel/n500_t10_k010 | 40 | 2520998 |
| journal_validation/stage2h/readiness/results/sequential/n500_t10_k010 | 40 | 2520993 |
| journal_validation/stage2h/readiness/results/repeat/n500_t10_k010 | 40 | 2520992 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r20_t10_k010_c0_A | 40 | 2520829 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r14_t10_k010_c2_A | 40 | 2520488 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r19_t10_k010_c2_A | 40 | 2519321 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r20_t10_k010_c0_B | 40 | 2516923 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r02_t10_k100_c2_B | 40 | 2516271 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r14_t10_k010_c0_A | 40 | 2516126 |
| journal_validation/stage2g/results/pilot_004_truth | 6 | 2514013 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r16_t50_k100_c1_B | 40 | 2511135 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r16_t10_k100_c2_B | 40 | 2510246 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r20_t10_k100_c2_A | 40 | 2508624 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r10_t10_k010_c2_B | 40 | 2508227 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r16_t10_k100_c2_A | 40 | 2507839 |
| journal_validation/stage2h/readiness/results/parallel/n500_t90_k100 | 40 | 2507466 |
| journal_validation/stage2h/readiness/results/sequential/n500_t90_k100 | 40 | 2507466 |
| journal_validation/stage2h/readiness/results/repeat/n500_t90_k100 | 40 | 2507462 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r04_t10_k010_c0_A | 40 | 2506737 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r12_t10_k100_c1_A | 40 | 2506706 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r04_t10_k010_c2_B | 40 | 2505867 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r16_t50_k010_c2_A | 40 | 2505800 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r13_t10_k010_c2_B | 40 | 2505020 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r13_t10_k100_c2_B | 40 | 2502004 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r09_t10_k100_c0_A | 40 | 2496538 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r04_t10_k010_c1_B | 40 | 2495951 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r13_t10_k010_c1_A | 40 | 2494249 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r04_t10_k100_c1_A | 40 | 2493022 |
| journal_validation/stage2h/readiness/results/parallel/n500_t10_k100 | 40 | 2491776 |
| journal_validation/stage2h/readiness/results/sequential/n500_t10_k100 | 40 | 2491775 |
| journal_validation/stage2h/readiness/results/repeat/n500_t10_k100 | 40 | 2491774 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r18_t10_k010_c0_A | 40 | 2490986 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r03_t10_k010_c0_B | 40 | 2490496 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r15_t10_k100_c0_B | 40 | 2487425 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r04_t10_k010_c0_B | 40 | 2485038 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r09_t10_k010_c1_A | 40 | 2484234 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r08_t10_k100_c0_A | 40 | 2479877 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r15_t50_k100_c1_A | 40 | 2479186 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r15_t10_k100_c2_B | 40 | 2478123 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r17_t10_k010_c0_B | 40 | 2477458 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r12_t10_k010_c2_A | 40 | 2477140 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r10_t10_k100_c1_B | 40 | 2475846 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r14_t10_k010_c2_B | 40 | 2474338 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r10_t10_k010_c1_A | 40 | 2473076 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r13_t10_k010_c0_B | 40 | 2472228 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r08_t10_k010_c1_A | 40 | 2470641 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r20_t10_k010_c1_B | 40 | 2470612 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r14_t10_k010_c0_B | 40 | 2468843 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r19_t10_k010_c2_B | 40 | 2468638 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r10_t10_k100_c1_A | 40 | 2468224 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r01_t10_k100_c1_B | 40 | 2468129 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r06_t10_k100_c2_B | 40 | 2465837 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r16_t10_k100_c1_B | 40 | 2463593 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r16_t10_k010_c1_B | 40 | 2460721 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r12_t10_k100_c1_B | 40 | 2458397 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r08_t10_k100_c1_A | 40 | 2458237 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r15_t50_k100_c1_B | 40 | 2457347 |
| journal_validation/stage2g/results/pilot_006_truth | 6 | 2456753 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r12_t10_k100_c0_A | 40 | 2455327 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r16_t10_k010_c0_A | 40 | 2453836 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r12_t10_k010_c0_A | 40 | 2453689 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r16_t10_k100_c0_A | 40 | 2453196 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r20_t50_k100_c2_A | 40 | 2451231 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r06_t10_k010_c1_A | 40 | 2451026 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r10_t10_k010_c1_B | 40 | 2449235 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r19_t10_k010_c1_A | 40 | 2447232 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r01_t10_k100_c0_B | 40 | 2447031 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r08_t10_k010_c1_B | 40 | 2445346 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r12_t10_k100_c2_B | 40 | 2444831 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r13_t10_k100_c0_B | 40 | 2444619 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r16_t10_k100_c1_A | 40 | 2436773 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r01_t10_k100_c2_B | 40 | 2436628 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r09_t10_k100_c2_A | 40 | 2436319 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r01_t10_k010_c0_B | 40 | 2435460 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r12_t10_k010_c2_B | 40 | 2433751 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r04_t10_k100_c0_A | 40 | 2432515 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r01_t10_k010_c1_B | 40 | 2432048 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r04_t10_k010_c1_A | 40 | 2429676 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r01_t10_k010_c0_A | 40 | 2427473 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r16_t10_k010_c2_A | 40 | 2427021 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r12_t10_k010_c1_A | 40 | 2422811 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r16_t10_k010_c2_B | 40 | 2422456 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r12_t10_k100_c2_A | 40 | 2422205 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r12_t10_k010_c0_B | 40 | 2419729 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r06_t10_k010_c1_B | 40 | 2419599 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r12_t10_k010_c1_B | 40 | 2418587 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r01_t10_k010_c2_A | 40 | 2418442 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r13_t10_k010_c0_A | 40 | 2416040 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r16_t50_k010_c2_B | 40 | 2404354 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r01_t10_k010_c2_B | 40 | 2391923 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r04_t10_k100_c1_B | 40 | 2387905 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r01_t10_k100_c2_A | 40 | 2385899 |
| journal_validation/stage2g/results/pilot_002_plus | 6 | 2384584 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r16_t10_k010_c1_A | 40 | 2382404 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r16_t10_k100_c0_B | 40 | 2382359 |
| journal_validation/stage2h/readiness/inputs | 5 | 2369487 |
| journal_validation/stage2g/results/pilot_001_truth | 6 | 2364619 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r01_t10_k010_c1_A | 40 | 2357043 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n500_r13_t10_k100_c0_A | 40 | 2331899 |
| journal_validation/stage2g/results/pilot_007_minus | 6 | 2306242 |
| journal_article/qa/batch4/runtime/inc/lib/DateTime/TimeZone/America | 105 | 2300200 |
| journal_validation/stage2g/results/pilot_007_truth | 6 | 2235905 |
| journal_validation/stage2g/results/pilot_002_truth | 6 | 2227988 |
| journal_validation/stage2g/results/pilot_006_minus | 6 | 2176383 |
| journal_article/submission/named | 5 | 2157029 |
| journal_validation/stage2g/results/pilot_002_minus | 6 | 2149134 |
| journal_article/submission/review | 4 | 2122951 |
| journal_validation/stage2g/results/pilot_004_minus | 6 | 2112232 |
| journal_validation/stage2g/results/pilot_003_plus | 6 | 2111997 |
| journal_validation/stage2g/results/pilot_005_minus | 6 | 2097391 |
| journal_validation/stage2g/results/pilot_014_plus | 6 | 2079695 |
| example | 7 | 2078564 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r04_t90_k010_c0_A | 11 | 2057367 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r04_t90_k100_c0_A | 11 | 2057366 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r04_t10_k100_c0_A | 11 | 2057358 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r04_t90_k100_c1_A | 11 | 2057357 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r04_t10_k100_c1_A | 11 | 2057355 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r04_t90_k010_c1_A | 11 | 2057353 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r04_t90_k100_c2_A | 11 | 2057352 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r04_t50_k010_c0_A | 11 | 2057351 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r04_t50_k010_c1_A | 11 | 2057350 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r04_t90_k010_c2_A | 11 | 2057350 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r04_t50_k010_c2_A | 11 | 2057348 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r04_t50_k100_c0_A | 11 | 2057348 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r04_t50_k100_c1_A | 11 | 2057347 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r04_t10_k100_c2_A | 11 | 2057343 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r04_t90_k100_c0_B | 11 | 2057343 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r04_t90_k100_c1_B | 11 | 2057343 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r04_t90_k100_c2_B | 11 | 2057343 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r04_t10_k010_c0_A | 11 | 2057342 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r04_t10_k010_c1_A | 11 | 2057341 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r04_t10_k100_c0_B | 11 | 2057341 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r04_t10_k100_c1_B | 11 | 2057341 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r04_t10_k010_c2_A | 11 | 2057340 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r04_t10_k010_c1_B | 11 | 2057339 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r04_t50_k100_c0_B | 11 | 2057339 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r04_t50_k100_c2_A | 11 | 2057339 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r04_t10_k100_c2_B | 11 | 2057338 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r04_t90_k010_c0_B | 11 | 2057335 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r04_t90_k010_c1_B | 11 | 2057332 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r04_t50_k100_c2_B | 11 | 2057330 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r04_t90_k010_c2_B | 11 | 2057330 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r04_t50_k010_c1_B | 11 | 2057327 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r04_t50_k010_c0_B | 11 | 2057326 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r04_t50_k100_c1_B | 11 | 2057326 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r04_t10_k010_c0_B | 11 | 2057325 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r04_t50_k010_c2_B | 11 | 2057324 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r04_t10_k010_c2_B | 11 | 2057313 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r11_t50_k010_c1_A | 11 | 2057312 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r11_t90_k010_c0_A | 11 | 2057311 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r11_t10_k010_c1_A | 11 | 2057310 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r11_t90_k010_c2_A | 11 | 2057310 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r07_t10_k100_c1_A | 11 | 2057308 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r11_t90_k010_c0_B | 11 | 2057308 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r11_t10_k010_c0_A | 11 | 2057307 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r11_t90_k010_c1_A | 11 | 2057306 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r11_t90_k010_c2_B | 11 | 2057306 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r11_t90_k100_c0_A | 11 | 2057305 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r07_t90_k100_c2_A | 11 | 2057304 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r11_t10_k100_c1_A | 11 | 2057304 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r11_t50_k010_c0_A | 11 | 2057304 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r07_t10_k100_c2_A | 11 | 2057303 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r11_t10_k010_c2_A | 11 | 2057302 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r11_t10_k100_c0_A | 11 | 2057301 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r11_t10_k010_c1_B | 11 | 2057300 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r11_t50_k010_c1_B | 11 | 2057300 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r11_t10_k010_c0_B | 11 | 2057299 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r11_t10_k100_c2_A | 11 | 2057299 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r11_t50_k010_c0_B | 11 | 2057298 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r07_t90_k100_c0_A | 11 | 2057297 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r11_t10_k010_c2_B | 11 | 2057296 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r07_t10_k100_c0_A | 11 | 2057295 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r07_t90_k100_c1_A | 11 | 2057295 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r11_t90_k100_c2_A | 11 | 2057294 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r11_t90_k010_c1_B | 11 | 2057293 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r11_t90_k100_c1_A | 11 | 2057293 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r07_t90_k100_c0_B | 11 | 2057290 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r11_t50_k010_c2_A | 11 | 2057289 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r07_t90_k010_c1_A | 11 | 2057288 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r07_t90_k100_c2_B | 11 | 2057288 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r11_t10_k100_c1_B | 11 | 2057288 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r11_t50_k100_c0_A | 11 | 2057288 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r07_t50_k100_c2_A | 11 | 2057287 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r07_t90_k100_c1_B | 11 | 2057287 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r07_t10_k100_c1_B | 11 | 2057286 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r11_t50_k010_c2_B | 11 | 2057286 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r11_t90_k100_c0_B | 11 | 2057286 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r05_t10_k010_c0_A | 11 | 2057285 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r07_t10_k010_c2_A | 11 | 2057285 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r07_t50_k010_c0_A | 11 | 2057285 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r07_t10_k010_c0_A | 11 | 2057284 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r07_t50_k100_c1_A | 11 | 2057284 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r07_t90_k010_c0_B | 11 | 2057284 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r07_t90_k010_c1_B | 11 | 2057284 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r07_t10_k100_c0_B | 11 | 2057283 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r07_t10_k100_c2_B | 11 | 2057283 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r07_t50_k100_c0_A | 11 | 2057283 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r07_t90_k010_c0_A | 11 | 2057283 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r05_t90_k010_c0_A | 11 | 2057282 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r11_t50_k100_c2_A | 11 | 2057282 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r11_t90_k100_c1_B | 11 | 2057282 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r11_t90_k100_c2_B | 11 | 2057282 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r07_t10_k010_c2_B | 11 | 2057281 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r07_t50_k010_c0_B | 11 | 2057281 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r05_t10_k100_c1_B | 11 | 2057280 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r07_t50_k100_c2_B | 11 | 2057280 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r07_t90_k010_c2_A | 11 | 2057280 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r07_t50_k010_c2_A | 11 | 2057279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r07_t50_k100_c0_B | 11 | 2057279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r07_t90_k010_c2_B | 11 | 2057279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r07_t50_k010_c1_A | 11 | 2057278 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r07_t10_k010_c0_B | 11 | 2057276 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r05_t90_k010_c2_A | 11 | 2057275 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r05_t90_k100_c1_B | 11 | 2057275 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r05_t90_k100_c2_B | 11 | 2057275 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r07_t10_k010_c1_B | 11 | 2057275 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r11_t50_k100_c2_B | 11 | 2057275 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r11_t10_k100_c0_B | 11 | 2057274 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r11_t10_k100_c2_B | 11 | 2057274 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r11_t50_k100_c1_A | 11 | 2057274 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r05_t90_k010_c1_A | 11 | 2057272 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r13_t90_k010_c2_A | 11 | 2057272 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r05_t50_k010_c1_A | 11 | 2057271 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r05_t90_k100_c2_A | 11 | 2057271 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r07_t50_k010_c1_B | 11 | 2057271 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r11_t50_k100_c0_B | 11 | 2057270 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r11_t50_k100_c1_B | 11 | 2057270 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r05_t50_k100_c0_B | 11 | 2057269 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r05_t50_k010_c0_A | 11 | 2057268 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r05_t50_k010_c2_A | 11 | 2057268 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r07_t10_k010_c1_A | 11 | 2057268 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r12_t90_k100_c0_A | 11 | 2057268 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r05_t90_k010_c2_B | 11 | 2057267 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r07_t50_k010_c2_B | 11 | 2057267 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r07_t50_k100_c1_B | 11 | 2057267 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r05_t50_k010_c1_B | 11 | 2057266 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r05_t90_k010_c0_B | 11 | 2057266 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r05_t90_k100_c0_A | 11 | 2057265 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r05_t90_k100_c1_A | 11 | 2057264 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r05_t10_k010_c1_A | 11 | 2057263 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r05_t10_k010_c1_B | 11 | 2057263 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r13_t50_k010_c1_A | 11 | 2057263 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r05_t10_k100_c2_B | 11 | 2057262 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r08_t10_k100_c2_B | 11 | 2057262 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r08_t90_k100_c0_B | 11 | 2057262 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r08_t90_k100_c2_A | 11 | 2057262 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r12_t90_k100_c1_A | 11 | 2057262 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r13_t90_k010_c0_A | 11 | 2057262 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r03_t10_k100_c0_A | 11 | 2057261 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r05_t90_k010_c1_B | 11 | 2057261 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r05_t90_k100_c0_B | 11 | 2057261 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r12_t10_k100_c0_A | 11 | 2057261 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r13_t10_k010_c2_A | 11 | 2057261 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r05_t10_k010_c2_B | 11 | 2057260 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r05_t50_k100_c1_B | 11 | 2057260 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r05_t50_k100_c2_B | 11 | 2057260 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r03_t90_k100_c0_A | 11 | 2057259 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r05_t10_k010_c0_B | 11 | 2057259 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r05_t10_k010_c2_A | 11 | 2057259 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r08_t90_k100_c2_B | 11 | 2057258 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r05_t50_k010_c2_B | 11 | 2057257 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r08_t10_k100_c0_A | 11 | 2057257 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r08_t50_k100_c2_A | 11 | 2057257 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r08_t90_k100_c0_A | 11 | 2057257 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r05_t10_k100_c1_A | 11 | 2057255 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r13_t10_k010_c0_A | 11 | 2057255 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r03_t10_k100_c2_A | 11 | 2057254 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r05_t10_k100_c0_B | 11 | 2057254 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r08_t90_k100_c1_A | 11 | 2057254 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r08_t90_k100_c1_B | 11 | 2057254 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r12_t10_k100_c2_A | 11 | 2057254 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r12_t90_k010_c0_A | 11 | 2057254 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r03_t90_k100_c1_A | 11 | 2057253 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r05_t10_k100_c2_A | 11 | 2057253 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r08_t10_k100_c0_B | 11 | 2057253 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r13_t90_k010_c1_A | 11 | 2057253 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r03_t50_k010_c1_A | 11 | 2057252 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r05_t50_k010_c0_B | 11 | 2057252 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r05_t50_k100_c0_A | 11 | 2057252 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r12_t10_k100_c1_A | 11 | 2057252 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r12_t50_k010_c0_A | 11 | 2057252 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r12_t90_k100_c1_B | 11 | 2057252 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r08_t50_k100_c2_B | 11 | 2057251 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r08_t90_k010_c0_A | 11 | 2057251 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r13_t10_k010_c1_A | 11 | 2057251 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r13_t90_k100_c2_B | 11 | 2057251 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r03_t10_k100_c0_B | 11 | 2057250 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r03_t90_k010_c0_A | 11 | 2057250 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r03_t90_k010_c1_A | 11 | 2057250 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r08_t90_k010_c1_A | 11 | 2057250 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r05_t50_k100_c2_A | 11 | 2057249 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r12_t10_k010_c2_A | 11 | 2057249 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r12_t90_k100_c2_A | 11 | 2057249 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r13_t90_k100_c0_A | 11 | 2057249 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r05_t50_k100_c1_A | 11 | 2057248 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r08_t50_k010_c0_A | 11 | 2057248 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r08_t50_k100_c1_A | 11 | 2057248 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r12_t90_k010_c2_A | 11 | 2057248 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r13_t50_k010_c0_A | 11 | 2057248 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r08_t90_k010_c0_B | 11 | 2057247 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r12_t50_k100_c1_A | 11 | 2057247 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r03_t90_k100_c2_A | 11 | 2057246 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r08_t10_k100_c2_A | 11 | 2057246 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r08_t90_k010_c2_A | 11 | 2057246 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r12_t50_k010_c2_A | 11 | 2057246 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r03_t10_k100_c1_A | 11 | 2057245 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r03_t10_k100_c2_B | 11 | 2057245 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r12_t10_k010_c1_A | 11 | 2057245 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r12_t50_k100_c0_A | 11 | 2057245 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r13_t90_k100_c1_A | 11 | 2057245 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r08_t10_k010_c1_A | 11 | 2057244 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r08_t10_k100_c1_B | 11 | 2057244 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r08_t50_k010_c1_A | 11 | 2057244 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r03_t50_k010_c2_A | 11 | 2057243 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r12_t10_k100_c0_B | 11 | 2057243 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r12_t90_k010_c1_A | 11 | 2057242 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r13_t50_k010_c2_A | 11 | 2057242 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r03_t50_k100_c2_A | 11 | 2057241 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r05_t10_k100_c0_A | 11 | 2057241 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r08_t50_k100_c0_B | 11 | 2057241 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r08_t90_k010_c2_B | 11 | 2057241 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r13_t90_k100_c2_A | 11 | 2057241 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r03_t10_k010_c1_A | 11 | 2057240 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r08_t50_k100_c0_A | 11 | 2057240 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r08_t50_k100_c1_B | 11 | 2057240 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r12_t90_k010_c2_B | 11 | 2057240 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r03_t50_k010_c0_A | 11 | 2057239 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r08_t10_k010_c0_A | 11 | 2057239 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r12_t10_k100_c2_B | 11 | 2057239 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r12_t50_k100_c2_A | 11 | 2057239 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r13_t10_k100_c0_B | 11 | 2057239 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r03_t10_k010_c0_A | 11 | 2057238 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r03_t90_k010_c2_A | 11 | 2057238 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r03_t90_k100_c2_B | 11 | 2057238 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r08_t10_k100_c1_A | 11 | 2057238 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r08_t50_k010_c0_B | 11 | 2057238 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r12_t90_k010_c0_B | 11 | 2057238 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r08_t90_k010_c1_B | 11 | 2057237 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r12_t50_k010_c1_A | 11 | 2057237 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r13_t10_k100_c2_A | 11 | 2057237 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r13_t10_k100_c2_B | 11 | 2057237 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r13_t90_k100_c0_B | 11 | 2057237 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r03_t10_k010_c2_A | 11 | 2057236 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r12_t10_k100_c1_B | 11 | 2057236 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r13_t50_k100_c0_B | 11 | 2057236 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r03_t50_k100_c0_A | 11 | 2057235 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r08_t50_k010_c2_A | 11 | 2057235 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r12_t10_k010_c0_A | 11 | 2057235 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r13_t10_k100_c1_B | 11 | 2057235 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r13_t50_k100_c2_A | 11 | 2057235 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r03_t90_k100_c0_B | 11 | 2057234 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r03_t90_k100_c1_B | 11 | 2057234 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r08_t50_k010_c2_B | 11 | 2057234 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r12_t50_k100_c1_B | 11 | 2057234 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r12_t90_k100_c0_B | 11 | 2057234 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r15_t90_k010_c1_A | 11 | 2057234 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r12_t90_k100_c2_B | 11 | 2057233 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r13_t10_k010_c0_B | 11 | 2057233 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r13_t10_k100_c0_A | 11 | 2057233 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r13_t90_k010_c2_B | 11 | 2057233 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r03_t50_k010_c1_B | 11 | 2057232 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r12_t90_k010_c1_B | 11 | 2057232 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r15_t10_k010_c1_B | 11 | 2057232 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r15_t90_k010_c2_B | 11 | 2057232 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r03_t90_k010_c0_B | 11 | 2057231 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r08_t10_k010_c0_B | 11 | 2057231 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r12_t10_k010_c1_B | 11 | 2057231 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r13_t50_k100_c2_B | 11 | 2057231 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r20_t90_k100_c1_A | 11 | 2057231 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r03_t50_k100_c0_B | 11 | 2057230 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r12_t50_k010_c0_B | 11 | 2057230 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r12_t50_k010_c1_B | 11 | 2057230 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r13_t10_k100_c1_A | 11 | 2057230 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r13_t90_k010_c0_B | 11 | 2057230 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r15_t90_k010_c1_B | 11 | 2057230 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r03_t50_k100_c1_A | 11 | 2057229 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r08_t50_k010_c1_B | 11 | 2057229 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r12_t50_k100_c0_B | 11 | 2057229 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r15_t90_k010_c2_A | 11 | 2057229 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r20_t10_k100_c0_A | 11 | 2057229 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r13_t50_k010_c1_B | 11 | 2057228 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r13_t90_k010_c1_B | 11 | 2057228 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r13_t90_k100_c1_B | 11 | 2057228 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r12_t10_k010_c2_B | 11 | 2057227 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r13_t50_k100_c0_A | 11 | 2057227 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r03_t90_k010_c1_B | 11 | 2057226 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r08_t10_k010_c1_B | 11 | 2057226 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r12_t10_k010_c0_B | 11 | 2057226 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r15_t90_k010_c0_A | 11 | 2057226 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r03_t10_k100_c1_B | 11 | 2057225 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r03_t90_k010_c2_B | 11 | 2057225 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r03_t50_k010_c2_B | 11 | 2057224 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r03_t50_k100_c2_B | 11 | 2057224 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r08_t10_k010_c2_A | 11 | 2057224 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r13_t10_k010_c2_B | 11 | 2057224 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r15_t90_k010_c0_B | 11 | 2057224 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r12_t50_k010_c2_B | 11 | 2057223 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r12_t50_k100_c2_B | 11 | 2057223 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r13_t10_k010_c1_B | 11 | 2057223 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r15_t10_k010_c0_B | 11 | 2057223 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r15_t50_k010_c1_B | 11 | 2057223 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r20_t90_k100_c0_A | 11 | 2057222 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r20_t90_k100_c2_A | 11 | 2057222 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r01_t90_k010_c2_B | 11 | 2057221 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r13_t50_k010_c0_B | 11 | 2057221 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r15_t10_k010_c1_A | 11 | 2057221 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r01_t90_k010_c0_B | 11 | 2057220 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r03_t10_k010_c0_B | 11 | 2057219 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r13_t50_k100_c1_A | 11 | 2057219 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r15_t10_k100_c2_B | 11 | 2057219 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r20_t10_k100_c2_A | 11 | 2057219 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r01_t50_k010_c0_B | 11 | 2057218 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r03_t10_k010_c1_B | 11 | 2057218 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r03_t50_k010_c0_B | 11 | 2057218 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r08_t10_k010_c2_B | 11 | 2057218 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r15_t10_k010_c2_A | 11 | 2057218 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r03_t10_k010_c2_B | 11 | 2057217 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r15_t50_k010_c1_A | 11 | 2057217 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r15_t90_k100_c2_B | 11 | 2057217 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r20_t10_k100_c1_A | 11 | 2057217 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r20_t90_k010_c0_B | 11 | 2057216 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r01_t90_k010_c2_A | 11 | 2057215 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r03_t50_k100_c1_B | 11 | 2057215 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r13_t50_k010_c2_B | 11 | 2057215 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r15_t50_k010_c2_B | 11 | 2057215 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r20_t90_k010_c2_B | 11 | 2057215 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r15_t10_k010_c2_B | 11 | 2057214 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r20_t50_k010_c0_B | 11 | 2057214 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r20_t90_k010_c1_B | 11 | 2057214 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r01_t10_k100_c1_A | 11 | 2057213 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r01_t90_k100_c1_A | 11 | 2057213 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r15_t10_k010_c0_A | 11 | 2057213 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r20_t90_k100_c2_B | 11 | 2057213 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r01_t50_k010_c2_B | 11 | 2057212 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r15_t50_k010_c2_A | 11 | 2057212 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r15_t90_k100_c1_B | 11 | 2057212 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r20_t10_k010_c1_A | 11 | 2057212 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r01_t90_k010_c1_B | 11 | 2057211 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r15_t50_k100_c1_B | 11 | 2057211 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r20_t10_k010_c2_B | 11 | 2057211 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r20_t90_k010_c2_A | 11 | 2057211 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r01_t10_k100_c2_A | 11 | 2057210 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r01_t50_k100_c2_A | 11 | 2057210 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r01_t90_k010_c0_A | 11 | 2057210 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r15_t10_k100_c1_B | 11 | 2057210 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r20_t10_k010_c0_B | 11 | 2057210 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r20_t10_k100_c0_B | 11 | 2057210 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r20_t10_k100_c2_B | 11 | 2057210 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r20_t90_k100_c0_B | 11 | 2057210 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r01_t10_k010_c2_B | 11 | 2057209 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r20_t50_k010_c2_B | 11 | 2057209 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r15_t50_k010_c0_A | 11 | 2057208 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r15_t90_k100_c1_A | 11 | 2057208 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r15_t90_k100_c2_A | 11 | 2057208 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r20_t10_k010_c0_A | 11 | 2057208 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r20_t10_k010_c1_B | 11 | 2057208 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r20_t50_k100_c0_A | 11 | 2057208 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r20_t90_k010_c1_A | 11 | 2057208 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r01_t10_k100_c2_B | 11 | 2057207 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r01_t50_k010_c2_A | 11 | 2057207 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r01_t50_k100_c1_A | 11 | 2057207 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r01_t90_k100_c0_A | 11 | 2057207 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r01_t90_k100_c2_A | 11 | 2057207 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r15_t90_k100_c0_B | 11 | 2057207 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r01_t50_k010_c0_A | 11 | 2057206 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r01_t50_k010_c1_B | 11 | 2057206 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r01_t50_k100_c0_A | 11 | 2057206 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r15_t50_k010_c0_B | 11 | 2057206 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r20_t10_k010_c2_A | 11 | 2057206 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r20_t90_k100_c1_B | 11 | 2057206 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r01_t10_k010_c1_B | 11 | 2057205 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r01_t90_k100_c2_B | 11 | 2057205 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r01_t10_k010_c0_A | 11 | 2057204 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r01_t10_k100_c0_A | 11 | 2057204 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r01_t90_k010_c1_A | 11 | 2057204 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r15_t10_k100_c0_B | 11 | 2057204 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r20_t10_k100_c1_B | 11 | 2057204 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r01_t10_k010_c0_B | 11 | 2057203 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r01_t10_k010_c1_A | 11 | 2057203 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r01_t10_k010_c2_A | 11 | 2057203 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r13_t50_k100_c1_B | 11 | 2057203 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r15_t10_k100_c1_A | 11 | 2057203 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r20_t50_k010_c1_B | 11 | 2057203 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r20_t90_k010_c0_A | 11 | 2057202 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r20_t50_k010_c1_A | 11 | 2057200 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r20_t50_k100_c1_B | 11 | 2057200 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r20_t50_k100_c2_A | 11 | 2057200 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r01_t50_k010_c1_A | 11 | 2057199 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r15_t50_k100_c2_A | 11 | 2057199 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r15_t50_k100_c2_B | 11 | 2057199 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r20_t50_k010_c2_A | 11 | 2057199 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r15_t10_k100_c0_A | 11 | 2057198 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r20_t50_k010_c0_A | 11 | 2057198 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r15_t10_k100_c2_A | 11 | 2057197 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r20_t50_k100_c1_A | 11 | 2057197 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r01_t10_k100_c0_B | 11 | 2057196 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r01_t10_k100_c1_B | 11 | 2057195 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r01_t90_k100_c1_B | 11 | 2057195 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r15_t90_k100_c0_A | 11 | 2057195 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r01_t50_k100_c1_B | 11 | 2057194 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r20_t50_k100_c0_B | 11 | 2057192 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r01_t50_k100_c0_B | 11 | 2057191 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r15_t50_k100_c0_A | 11 | 2057191 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r15_t50_k100_c1_A | 11 | 2057191 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r19_t90_k100_c1_B | 11 | 2057191 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r01_t50_k100_c2_B | 11 | 2057190 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r20_t50_k100_c2_B | 11 | 2057190 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r01_t90_k100_c0_B | 11 | 2057187 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r09_t90_k010_c1_A | 11 | 2057183 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r09_t90_k010_c2_B | 11 | 2057183 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r09_t90_k100_c2_A | 11 | 2057181 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r15_t50_k100_c0_B | 11 | 2057181 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r09_t90_k010_c1_B | 11 | 2057180 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r17_t90_k010_c2_A | 11 | 2057180 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r09_t10_k010_c0_A | 11 | 2057178 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r09_t10_k100_c2_A | 11 | 2057178 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r19_t10_k100_c0_B | 11 | 2057178 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r09_t90_k100_c0_A | 11 | 2057177 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r17_t90_k100_c0_A | 11 | 2057177 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r17_t90_k100_c1_A | 11 | 2057175 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r17_t90_k100_c2_A | 11 | 2057175 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r09_t90_k010_c0_A | 11 | 2057174 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r09_t90_k010_c0_B | 11 | 2057174 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r09_t90_k010_c2_A | 11 | 2057174 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r17_t90_k010_c1_A | 11 | 2057174 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r17_t10_k100_c1_A | 11 | 2057173 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r09_t50_k010_c2_B | 11 | 2057172 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r17_t90_k010_c0_A | 11 | 2057172 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r19_t10_k100_c2_B | 11 | 2057171 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r09_t10_k100_c1_A | 11 | 2057170 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r09_t90_k100_c0_B | 11 | 2057170 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r19_t10_k100_c1_B | 11 | 2057170 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r09_t50_k100_c0_A | 11 | 2057169 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r09_t10_k010_c1_A | 11 | 2057168 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r09_t10_k010_c2_B | 11 | 2057168 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r17_t10_k100_c2_A | 11 | 2057168 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r17_t90_k100_c0_B | 11 | 2057168 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r19_t90_k010_c0_A | 11 | 2057168 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r19_t90_k010_c0_B | 11 | 2057168 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r19_t90_k100_c0_B | 11 | 2057168 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r09_t10_k010_c2_A | 11 | 2057167 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r09_t50_k010_c2_A | 11 | 2057167 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r09_t10_k100_c0_A | 11 | 2057166 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r09_t10_k100_c2_B | 11 | 2057166 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r09_t90_k100_c2_B | 11 | 2057166 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r17_t50_k010_c1_A | 11 | 2057166 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r17_t50_k100_c0_A | 11 | 2057166 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r17_t50_k100_c2_A | 11 | 2057166 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r09_t10_k010_c0_B | 11 | 2057165 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r09_t10_k010_c1_B | 11 | 2057165 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r09_t50_k100_c1_A | 11 | 2057164 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r17_t50_k010_c2_A | 11 | 2057164 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r17_t50_k100_c1_A | 11 | 2057164 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r17_t90_k010_c2_B | 11 | 2057164 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r19_t50_k100_c0_B | 11 | 2057164 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r19_t90_k100_c1_A | 11 | 2057164 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r09_t90_k100_c1_A | 11 | 2057163 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r17_t10_k100_c0_A | 11 | 2057163 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r17_t10_k010_c0_A | 11 | 2057162 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r17_t10_k100_c1_B | 11 | 2057162 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r17_t10_k100_c2_B | 11 | 2057162 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r19_t90_k010_c2_A | 11 | 2057162 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r17_t10_k010_c2_A | 11 | 2057161 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r17_t50_k010_c1_B | 11 | 2057161 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r17_t90_k010_c0_B | 11 | 2057161 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r19_t90_k010_c1_A | 11 | 2057161 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r09_t10_k100_c0_B | 11 | 2057160 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r09_t50_k010_c1_B | 11 | 2057160 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r17_t10_k100_c0_B | 11 | 2057160 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r09_t50_k100_c2_A | 11 | 2057159 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r17_t10_k010_c1_A | 11 | 2057159 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r17_t90_k100_c1_B | 11 | 2057159 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r19_t50_k010_c2_A | 11 | 2057159 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r19_t90_k100_c2_B | 11 | 2057159 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r09_t50_k010_c1_A | 11 | 2057158 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r19_t90_k010_c2_B | 11 | 2057158 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r17_t10_k010_c0_B | 11 | 2057157 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r17_t50_k100_c1_B | 11 | 2057157 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r17_t50_k100_c2_B | 11 | 2057157 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r17_t90_k100_c2_B | 11 | 2057157 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r09_t50_k010_c0_B | 11 | 2057156 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r17_t90_k010_c1_B | 11 | 2057156 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r09_t50_k010_c0_A | 11 | 2057155 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r09_t10_k100_c1_B | 11 | 2057153 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r19_t50_k100_c2_B | 11 | 2057153 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r17_t50_k010_c0_A | 11 | 2057152 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r19_t50_k010_c2_B | 11 | 2057152 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r17_t50_k010_c2_B | 11 | 2057151 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r09_t50_k100_c1_B | 11 | 2057150 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r16_t50_k010_c1_B | 11 | 2057149 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r19_t50_k010_c1_B | 11 | 2057149 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r19_t50_k100_c1_B | 11 | 2057149 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r09_t50_k100_c0_B | 11 | 2057148 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r09_t50_k100_c2_B | 11 | 2057148 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r09_t90_k100_c1_B | 11 | 2057148 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r17_t10_k010_c2_B | 11 | 2057148 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r19_t10_k010_c1_A | 11 | 2057148 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r19_t10_k100_c1_A | 11 | 2057148 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r19_t90_k100_c0_A | 11 | 2057148 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r19_t10_k100_c0_A | 11 | 2057147 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r19_t10_k100_c2_A | 11 | 2057147 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r17_t50_k100_c0_B | 11 | 2057146 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r18_t10_k100_c2_B | 11 | 2057146 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r19_t10_k010_c2_A | 11 | 2057144 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r17_t10_k010_c1_B | 11 | 2057143 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r19_t10_k010_c1_B | 11 | 2057143 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r18_t10_k100_c1_A | 11 | 2057142 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r19_t10_k010_c0_A | 11 | 2057142 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r19_t10_k010_c0_B | 11 | 2057142 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r19_t50_k100_c0_A | 11 | 2057142 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r19_t90_k010_c1_B | 11 | 2057142 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r16_t10_k010_c0_B | 11 | 2057141 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r16_t90_k010_c1_B | 11 | 2057141 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r19_t10_k010_c2_B | 11 | 2057141 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r19_t90_k100_c2_A | 11 | 2057141 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r17_t50_k010_c0_B | 11 | 2057139 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r19_t50_k010_c0_A | 11 | 2057139 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r19_t50_k010_c1_A | 11 | 2057138 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r16_t90_k010_c0_B | 11 | 2057137 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r18_t90_k100_c1_B | 11 | 2057137 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r16_t90_k010_c2_B | 11 | 2057135 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r19_t50_k100_c2_A | 11 | 2057135 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r18_t90_k100_c0_B | 11 | 2057134 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r18_t90_k100_c2_B | 11 | 2057134 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r16_t10_k010_c1_B | 11 | 2057133 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r18_t10_k100_c1_B | 11 | 2057133 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r19_t50_k010_c0_B | 11 | 2057133 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r16_t10_k100_c2_B | 11 | 2057132 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r18_t10_k100_c2_A | 11 | 2057132 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r18_t90_k100_c1_A | 11 | 2057132 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r18_t10_k100_c0_A | 11 | 2057131 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r18_t90_k010_c1_A | 11 | 2057131 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r18_t90_k100_c2_A | 11 | 2057131 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r16_t10_k010_c2_B | 11 | 2057130 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r16_t10_k100_c2_A | 11 | 2057129 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r18_t90_k100_c0_A | 11 | 2057129 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r16_t50_k010_c2_B | 11 | 2057128 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r16_t10_k100_c0_B | 11 | 2057127 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r18_t10_k100_c0_B | 11 | 2057127 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r18_t90_k010_c2_A | 11 | 2057127 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r16_t10_k100_c1_B | 11 | 2057124 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r16_t90_k010_c0_A | 11 | 2057124 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r16_t10_k010_c0_A | 11 | 2057123 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r16_t90_k010_c1_A | 11 | 2057123 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r16_t90_k100_c2_B | 11 | 2057123 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r19_t50_k100_c1_A | 11 | 2057123 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r16_t10_k010_c2_A | 11 | 2057122 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r16_t90_k100_c1_B | 11 | 2057122 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r18_t90_k010_c0_A | 11 | 2057122 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r16_t10_k100_c1_A | 11 | 2057121 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r16_t90_k100_c0_B | 11 | 2057121 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r16_t90_k100_c1_A | 11 | 2057121 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r18_t50_k010_c2_B | 11 | 2057121 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r16_t50_k010_c0_B | 11 | 2057120 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r16_t50_k100_c0_B | 11 | 2057120 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r16_t90_k010_c2_A | 11 | 2057120 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r18_t10_k010_c0_B | 11 | 2057120 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r18_t90_k010_c2_B | 11 | 2057120 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r18_t50_k010_c2_A | 11 | 2057119 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r18_t50_k100_c1_A | 11 | 2057119 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r16_t90_k100_c2_A | 11 | 2057118 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r18_t10_k010_c0_A | 11 | 2057118 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r18_t10_k010_c1_B | 11 | 2057117 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r18_t50_k010_c0_A | 11 | 2057117 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r18_t90_k010_c1_B | 11 | 2057116 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r16_t10_k100_c0_A | 11 | 2057115 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r18_t10_k010_c2_B | 11 | 2057115 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r16_t90_k100_c0_A | 11 | 2057114 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r18_t10_k010_c1_A | 11 | 2057114 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r18_t50_k010_c0_B | 11 | 2057114 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r18_t50_k010_c1_B | 11 | 2057114 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r18_t10_k010_c2_A | 11 | 2057113 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r18_t50_k010_c1_A | 11 | 2057113 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r18_t50_k100_c0_B | 11 | 2057113 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r18_t50_k100_c2_B | 11 | 2057113 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r16_t10_k010_c1_A | 11 | 2057112 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r16_t50_k100_c0_A | 11 | 2057112 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r18_t50_k100_c0_A | 11 | 2057112 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r18_t90_k010_c0_B | 11 | 2057112 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r16_t50_k010_c0_A | 11 | 2057111 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r16_t50_k010_c1_A | 11 | 2057111 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r18_t50_k100_c1_B | 11 | 2057111 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r16_t50_k010_c2_A | 11 | 2057108 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r16_t50_k100_c2_B | 11 | 2057107 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r18_t50_k100_c2_A | 11 | 2057106 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r16_t50_k100_c1_A | 11 | 2057104 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r16_t50_k100_c1_B | 11 | 2057101 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r16_t50_k100_c2_A | 11 | 2057099 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r10_t10_k010_c2_A | 11 | 2057089 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r10_t50_k010_c1_A | 11 | 2057083 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r10_t90_k010_c0_A | 11 | 2057078 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r10_t90_k010_c1_B | 11 | 2057077 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r10_t10_k010_c1_A | 11 | 2057076 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r10_t50_k010_c0_A | 11 | 2057073 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r10_t90_k010_c1_A | 11 | 2057073 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r10_t90_k100_c1_B | 11 | 2057071 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r10_t90_k010_c2_A | 11 | 2057069 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r14_t90_k100_c1_A | 11 | 2057069 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r10_t10_k010_c2_B | 11 | 2057068 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r06_t90_k010_c1_B | 11 | 2057067 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r10_t10_k100_c0_B | 11 | 2057067 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r10_t10_k100_c2_A | 11 | 2057067 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r10_t50_k010_c2_A | 11 | 2057067 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r14_t90_k100_c2_A | 11 | 2057067 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r10_t90_k100_c1_A | 11 | 2057066 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r10_t10_k100_c2_B | 11 | 2057065 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r10_t50_k010_c1_B | 11 | 2057065 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r10_t90_k010_c0_B | 11 | 2057065 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r10_t90_k010_c2_B | 11 | 2057065 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r06_t90_k010_c0_B | 11 | 2057064 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r10_t50_k010_c0_B | 11 | 2057064 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r14_t10_k100_c0_B | 11 | 2057064 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r06_t10_k010_c1_A | 11 | 2057063 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r06_t50_k010_c2_A | 11 | 2057063 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r06_t90_k010_c1_A | 11 | 2057063 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r10_t10_k100_c1_B | 11 | 2057063 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r10_t50_k100_c2_B | 11 | 2057062 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r10_t90_k100_c0_B | 11 | 2057062 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r06_t50_k010_c2_B | 11 | 2057061 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r10_t50_k100_c2_A | 11 | 2057061 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r10_t10_k010_c1_B | 11 | 2057060 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r10_t10_k100_c0_A | 11 | 2057060 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r10_t10_k100_c1_A | 11 | 2057060 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r10_t50_k100_c1_B | 11 | 2057060 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r14_t10_k100_c2_B | 11 | 2057060 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r06_t50_k010_c0_A | 11 | 2057059 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r06_t90_k010_c0_A | 11 | 2057059 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r14_t10_k100_c0_A | 11 | 2057059 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r14_t50_k010_c1_A | 11 | 2057059 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r14_t90_k100_c0_A | 11 | 2057059 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r06_t90_k010_c2_A | 11 | 2057058 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r10_t90_k100_c2_B | 11 | 2057058 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r14_t10_k100_c2_A | 11 | 2057058 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r14_t50_k100_c0_A | 11 | 2057058 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r14_t50_k100_c2_A | 11 | 2057058 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r10_t50_k010_c2_B | 11 | 2057057 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r14_t10_k100_c1_B | 11 | 2057057 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r14_t90_k100_c1_B | 11 | 2057057 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r06_t10_k010_c2_A | 11 | 2057056 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r14_t90_k010_c0_A | 11 | 2057056 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r06_t50_k010_c1_A | 11 | 2057055 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r14_t50_k100_c2_B | 11 | 2057055 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r06_t10_k010_c0_B | 11 | 2057054 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r10_t10_k010_c0_A | 11 | 2057054 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r14_t90_k010_c2_B | 11 | 2057054 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r14_t90_k100_c2_B | 11 | 2057054 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r10_t50_k100_c1_A | 11 | 2057053 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r14_t10_k100_c1_A | 11 | 2057053 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r14_t50_k100_c0_B | 11 | 2057053 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r06_t10_k010_c1_B | 11 | 2057052 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r06_t90_k010_c2_B | 11 | 2057052 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r10_t10_k010_c0_B | 11 | 2057052 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r14_t10_k010_c1_A | 11 | 2057052 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r14_t10_k010_c2_A | 11 | 2057052 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r10_t90_k100_c0_A | 11 | 2057051 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r10_t90_k100_c2_A | 11 | 2057051 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r14_t90_k010_c2_A | 11 | 2057050 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r06_t10_k010_c0_A | 11 | 2057049 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r14_t10_k010_c2_B | 11 | 2057049 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r14_t90_k010_c1_A | 11 | 2057049 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r14_t90_k100_c0_B | 11 | 2057049 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r06_t90_k100_c2_A | 11 | 2057048 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r14_t10_k010_c0_B | 11 | 2057048 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r14_t90_k010_c0_B | 11 | 2057048 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r14_t90_k010_c1_B | 11 | 2057048 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r06_t10_k010_c2_B | 11 | 2057047 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r14_t10_k010_c0_A | 11 | 2057047 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r14_t50_k010_c2_A | 11 | 2057047 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r06_t50_k010_c0_B | 11 | 2057046 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r14_t50_k010_c0_A | 11 | 2057046 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r14_t50_k100_c1_B | 11 | 2057046 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r06_t10_k100_c0_A | 11 | 2057045 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r10_t50_k100_c0_A | 11 | 2057045 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r14_t50_k010_c2_B | 11 | 2057045 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r06_t90_k100_c1_B | 11 | 2057042 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r06_t10_k100_c1_B | 11 | 2057040 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r06_t50_k010_c1_B | 11 | 2057040 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r14_t50_k010_c0_B | 11 | 2057040 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r14_t50_k010_c1_B | 11 | 2057040 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r06_t90_k100_c2_B | 11 | 2057039 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r14_t10_k010_c1_B | 11 | 2057038 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r14_t50_k100_c1_A | 11 | 2057038 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r06_t90_k100_c1_A | 11 | 2057037 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r06_t10_k100_c1_A | 11 | 2057036 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r06_t10_k100_c0_B | 11 | 2057035 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r10_t50_k100_c0_B | 11 | 2057035 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r06_t90_k100_c0_A | 11 | 2057034 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r06_t90_k100_c0_B | 11 | 2057033 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r06_t10_k100_c2_A | 11 | 2057030 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r06_t50_k100_c2_A | 11 | 2057030 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r06_t10_k100_c2_B | 11 | 2057029 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r06_t50_k100_c0_B | 11 | 2057029 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r06_t50_k100_c0_A | 11 | 2057028 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r06_t50_k100_c1_A | 11 | 2057027 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r06_t50_k100_c1_B | 11 | 2057027 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r06_t50_k100_c2_B | 11 | 2057026 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r02_t10_k010_c0_A | 11 | 2057001 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r02_t90_k010_c1_A | 11 | 2056999 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r02_t10_k010_c1_A | 11 | 2056997 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r02_t90_k010_c0_A | 11 | 2056997 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r02_t10_k010_c2_A | 11 | 2056995 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r02_t50_k010_c2_A | 11 | 2056995 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r02_t90_k010_c2_A | 11 | 2056993 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r02_t50_k010_c1_A | 11 | 2056989 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r02_t10_k010_c1_B | 11 | 2056988 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r02_t90_k010_c2_B | 11 | 2056988 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r02_t50_k010_c2_B | 11 | 2056986 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r02_t90_k010_c1_B | 11 | 2056986 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r02_t10_k010_c0_B | 11 | 2056984 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r02_t10_k010_c2_B | 11 | 2056984 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r02_t90_k100_c1_A | 11 | 2056982 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r02_t50_k010_c1_B | 11 | 2056981 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r02_t90_k010_c0_B | 11 | 2056980 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r02_t90_k100_c0_A | 11 | 2056978 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r02_t50_k100_c0_A | 11 | 2056977 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r02_t90_k100_c2_A | 11 | 2056977 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r02_t10_k100_c1_A | 11 | 2056975 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r02_t90_k100_c2_B | 11 | 2056974 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r02_t50_k010_c0_A | 11 | 2056972 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r02_t10_k100_c2_A | 11 | 2056971 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r02_t10_k100_c0_A | 11 | 2056970 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r02_t10_k100_c0_B | 11 | 2056970 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r02_t10_k100_c2_B | 11 | 2056969 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r02_t50_k100_c1_A | 11 | 2056969 |
| journal_validation/stage2h/readiness/inputs/n500_t10_k100 | 11 | 2056969 |
| journal_validation/stage2h/readiness/inputs/n500_t90_k100 | 11 | 2056968 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r02_t50_k100_c2_B | 11 | 2056967 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r02_t50_k100_c0_B | 11 | 2056966 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r02_t90_k100_c1_B | 11 | 2056966 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r02_t50_k100_c1_B | 11 | 2056965 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r02_t50_k100_c2_A | 11 | 2056965 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r02_t10_k100_c1_B | 11 | 2056964 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r02_t50_k010_c0_B | 11 | 2056963 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r02_t90_k100_c0_B | 11 | 2056963 |
| journal_validation/stage2h/readiness/inputs/n500_t50_k100 | 11 | 2056958 |
| journal_validation/stage2h/readiness/inputs/n500_t50_k010 | 11 | 2056957 |
| journal_validation/stage2h/readiness/inputs/n500_t10_k010 | 11 | 2056950 |
| journal_validation/stage2h/readiness/inputs/n500_t90_k010 | 11 | 2056949 |
| journal_validation/stage2g/results/pilot_001_minus | 6 | 2040696 |
| journal_validation/stage2g/results/pilot_005_truth | 6 | 2039498 |
| docs/university_template | 4 | 2026678 |
| journal_article/qa/batch4/runtime/inc/lib/Unicode/Collate | 3 | 2011158 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_021/P10 | 6 | 2009562 |
| journal_validation/stage2c/validation_protocol/reassessment_20261029T083111Z/pilot_020/P10 | 4 | 1964237 |
| journal_validation/stage2c/validation_protocol/reassessment_20261029T083111Z/pilot_019/P10 | 4 | 1962316 |
| journal_validation/stage2c/validation_protocol/reassessment_20261029T083111Z/pilot_017/P10 | 4 | 1961186 |
| journal_validation/stage2c/validation_protocol/reassessment_20261029T083111Z/pilot_009/P00 | 4 | 1960327 |
| journal_validation/stage2c/validation_protocol/reassessment_20261029T083111Z/pilot_014/P10 | 4 | 1959301 |
| journal_validation/stage2c/validation_protocol/reassessment_20261029T083111Z/pilot_019/P00 | 4 | 1959293 |
| journal_validation/stage2c/validation_protocol/reassessment_20261029T083111Z/pilot_002/P10 | 4 | 1959232 |
| journal_validation/stage2c/validation_protocol/reassessment_20261029T083111Z/pilot_009/P10 | 4 | 1959206 |
| journal_validation/stage2c/validation_protocol/reassessment_20261029T083111Z/pilot_001/P10 | 4 | 1958158 |
| journal_validation/stage2c/validation_protocol/reassessment_20261029T083111Z/pilot_020/P00 | 4 | 1957212 |
| journal_validation/stage2c/validation_protocol/reassessment_20261029T083111Z/validation_002/P10 | 4 | 1956178 |
| journal_validation/stage2c/validation_protocol/reassessment_20261029T083111Z/pilot_021/P00 | 4 | 1956104 |
| journal_validation/stage2c/validation_protocol/reassessment_20261029T083111Z/validation_001/P10 | 4 | 1955102 |
| journal_validation/stage2c/validation_protocol/reassessment_20261029T083111Z/pilot_004/P10 | 4 | 1955063 |
| journal_validation/stage2c/validation_protocol/reassessment_20261029T083111Z/pilot_007/P10 | 4 | 1955059 |
| journal_validation/stage2c/validation_protocol/reassessment_20261029T083111Z/pilot_006/P10 | 4 | 1955015 |
| journal_validation/stage2c/validation_protocol/reassessment_20261029T083111Z/pilot_008/P10 | 4 | 1954961 |
| journal_validation/stage2c/validation_protocol/reassessment_20261029T083111Z/pilot_011/P10 | 4 | 1954940 |
| journal_validation/stage2c/validation_protocol/reassessment_20261029T083111Z/pilot_008/P00 | 4 | 1954172 |
| journal_validation/stage2c/validation_protocol/reassessment_20261029T083111Z/pilot_003/P10 | 4 | 1954130 |
| journal_validation/stage2g/results/pilot_007_plus | 6 | 1953697 |
| journal_validation/stage2c/validation_protocol/reassessment_20261029T083111Z/pilot_021/P10 | 4 | 1953047 |
| journal_validation/stage2c/validation_protocol/reassessment_20261029T083111Z/pilot_001/P00 | 4 | 1953036 |
| journal_validation/stage2c/validation_protocol/reassessment_20261029T083111Z/pilot_016/P00 | 4 | 1953032 |
| journal_validation/stage2c/validation_protocol/reassessment_20261029T083111Z/pilot_002/P00 | 4 | 1951101 |
| journal_validation/stage2c/validation_protocol/reassessment_20261029T083111Z/pilot_013/P00 | 4 | 1951101 |
| journal_validation/stage2c/validation_protocol/reassessment_20261029T083111Z/pilot_015/P00 | 4 | 1951033 |
| journal_validation/stage2c/validation_protocol/reassessment_20261029T083111Z/pilot_016/P10 | 4 | 1951030 |
| journal_validation/stage2c/validation_protocol/reassessment_20261029T083111Z/pilot_011/P00 | 4 | 1949981 |
| journal_validation/stage2c/validation_protocol/reassessment_20261029T083111Z/pilot_006/P00 | 4 | 1949007 |
| journal_validation/stage2c/validation_protocol/reassessment_20261029T083111Z/pilot_013/P10 | 4 | 1948889 |
| journal_validation/stage2c/validation_protocol/reassessment_20261029T083111Z/pilot_015/P10 | 4 | 1948850 |
| journal_validation/stage2c/validation_protocol/reassessment_20261029T083111Z/validation_002/P00 | 4 | 1948040 |
| journal_validation/stage2c/validation_protocol/reassessment_20261029T083111Z/pilot_005/P10 | 4 | 1947917 |
| journal_validation/stage2c/validation_protocol/reassessment_20261029T083111Z/pilot_017/P00 | 4 | 1947017 |
| journal_validation/stage2c/validation_protocol/reassessment_20261029T083111Z/pilot_007/P00 | 4 | 1947006 |
| journal_validation/stage2c/validation_protocol/reassessment_20261029T083111Z/pilot_018/P10 | 4 | 1946952 |
| journal_validation/stage2c/validation_protocol/reassessment_20261029T083111Z/pilot_005/P00 | 4 | 1945988 |
| journal_validation/stage2c/validation_protocol/reassessment_20261029T083111Z/pilot_010/P10 | 4 | 1945841 |
| journal_validation/stage2c/validation_protocol/reassessment_20261029T083111Z/pilot_003/P00 | 4 | 1944962 |
| journal_validation/stage2c/validation_protocol/reassessment_20261029T083111Z/pilot_004/P00 | 4 | 1944934 |
| journal_validation/stage2c/validation_protocol/reassessment_20261029T083111Z/pilot_014/P00 | 4 | 1943894 |
| journal_validation/stage2c/validation_protocol/reassessment_20261029T083111Z/validation_001/P00 | 4 | 1943797 |
| journal_validation/stage2c/validation_protocol/reassessment_20261029T083111Z/pilot_010/P00 | 4 | 1942878 |
| journal_validation/stage2c/validation_protocol/reassessment_20261029T083111Z/pilot_018/P00 | 4 | 1941893 |
| journal_validation/stage2c/validation_protocol/reassessment_20261029T083111Z/pilot_012/P00 | 4 | 1939877 |
| journal_validation/stage2c/validation_protocol/reassessment_20261029T083111Z/pilot_012/P10 | 4 | 1939705 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z | 17 | 1904835 |
| journal_validation/stage2g/results/pilot_001_plus | 6 | 1891655 |
| journal_article/qa/batch4/runtime/data/fontconfig/cache | 12 | 1778572 |
| thesis | 14 | 1740408 |
| journal_validation/stage2c/output/controlled_20261029_01 | 50 | 1703333 |
| journal_article/qa/batch4/runtime/inc/lib | 64 | 1702205 |
| journal_article/qa/batch4/runtime/inc/lib/unicore | 10 | 1700644 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r20 | 4 | 1608908 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r14 | 4 | 1608856 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r17 | 4 | 1608819 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r12 | 4 | 1608796 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r05 | 4 | 1608795 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r16 | 4 | 1608790 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r06 | 4 | 1608788 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r01 | 4 | 1608784 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r19 | 4 | 1608753 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r03 | 4 | 1608746 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r09 | 4 | 1608741 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r15 | 4 | 1608735 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r04 | 4 | 1608730 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r11 | 4 | 1608713 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r08 | 4 | 1608700 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r02 | 4 | 1608698 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r13 | 4 | 1608688 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r10 | 4 | 1608675 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r07 | 4 | 1608649 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n1000_r18 | 4 | 1608595 |
| thesis_extension/environment/legacy_R343_library/ggplot2/doc | 7 | 1584468 |
| journal_validation/stage2a/output/controlled_20261022_01 | 44 | 1529489 |
| journal_article/qa/batch4/runtime/inc/lib/DateTime/TimeZone/Europe | 46 | 1506757 |
| thesis_extension/environment/legacy_R343_library/quantreg/doc | 17 | 1480067 |
| journal_validation/stage2g/end_to_end_certification | 14 | 1477681 |
| journal_article/qa/batch4/runtime/data/fonts/map/dvips | 6 | 1402138 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot/n1000_r05_t10_k010_c0_A | 6 | 1396575 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080751Z | 7 | 1366797 |
| journal_validation/publication_review/lssp_canonical_build/build | 9 | 1324857 |
| journal_article/qa/batch4/runtime/inc/lib/auto/Encode/JP | 1 | 1297408 |
| journal_validation/stage2b/output/controlled_20261022_01/validation_details | 18 | 1254377 |
| journal_article/submission/work/named_build | 8 | 1251089 |
| journal_validation/publication_review/lssp_optimization/build/main | 8 | 1236414 |
| journal_article | 16 | 1234327 |
| journal_article/submission/work/review_build | 8 | 1229973 |
| journal_article/qa/batch4/runtime/inc/lib/auto/Encode/KR | 1 | 1200128 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_018/P00/full_precision_lp | 6 | 1173069 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_018/P00/historical_csv_lp | 6 | 1173024 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_014/P10/historical_csv_lp | 6 | 1172872 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_014/P10/full_precision_lp | 6 | 1172830 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_011/P00/historical_csv_lp | 6 | 1172786 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_011/P00/full_precision_lp | 6 | 1172760 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_021/P10/sensitivity_2e-07 | 6 | 1172589 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_021/P10/sensitivity_5e-07 | 6 | 1172589 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_021/P10/full_precision_lp | 6 | 1170346 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_021/P10/sensitivity_1e-07 | 6 | 1170346 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_021/P10/sensitivity_5e-08 | 6 | 1170346 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_021/P10/historical_csv_lp | 6 | 1170326 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_010/P10/full_precision_lp | 6 | 1170208 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_010/P10/historical_csv_lp | 6 | 1170192 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_001/P00/historical_csv_lp | 6 | 1170186 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_001/P10/full_precision_lp | 6 | 1170108 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/validation_002/P00/full_precision_lp | 6 | 1170103 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/validation_002/P00/historical_csv_lp | 6 | 1170089 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_014/P00/full_precision_lp | 6 | 1170081 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_005/P00/full_precision_lp | 6 | 1170074 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_014/P00/historical_csv_lp | 6 | 1170058 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_001/P00/full_precision_lp | 6 | 1170051 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_010/P00/historical_csv_lp | 6 | 1170047 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/validation_001/P10/full_precision_lp | 6 | 1170033 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_015/P10/full_precision_lp | 6 | 1169988 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_013/P00/historical_csv_lp | 6 | 1169952 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/validation_001/P00/historical_csv_lp | 6 | 1169945 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_005/P00/historical_csv_lp | 6 | 1169943 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_004/P00/full_precision_lp | 6 | 1169925 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_017/P00/full_precision_lp | 6 | 1169925 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_009/P10/historical_csv_lp | 6 | 1169918 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_003/P00/full_precision_lp | 6 | 1169915 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_005/P10/historical_csv_lp | 6 | 1169910 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_016/P10/historical_csv_lp | 6 | 1169904 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_001/P10/historical_csv_lp | 6 | 1169886 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_010/P00/full_precision_lp | 6 | 1169882 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_004/P00/historical_csv_lp | 6 | 1169878 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_015/P00/historical_csv_lp | 6 | 1169876 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_002/P10/historical_csv_lp | 6 | 1169863 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_015/P10/historical_csv_lp | 6 | 1169859 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_021/P00/historical_csv_lp | 6 | 1169855 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_008/P10/historical_csv_lp | 6 | 1169845 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/validation_001/P00/full_precision_lp | 6 | 1169842 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/validation_001/P10/historical_csv_lp | 6 | 1169826 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_006/P10/full_precision_lp | 6 | 1169821 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_009/P00/full_precision_lp | 6 | 1169821 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_013/P00/full_precision_lp | 6 | 1169820 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_019/P00/full_precision_lp | 6 | 1169817 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_002/P10/full_precision_lp | 6 | 1169807 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_021/P00/full_precision_lp | 6 | 1169802 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_017/P10/historical_csv_lp | 6 | 1169797 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_009/P10/full_precision_lp | 6 | 1169796 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_016/P10/full_precision_lp | 6 | 1169791 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_019/P00/historical_csv_lp | 6 | 1169786 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_018/P10/full_precision_lp | 6 | 1169780 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/validation_002/P10/historical_csv_lp | 6 | 1169780 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_005/P10/full_precision_lp | 6 | 1169755 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_020/P00/full_precision_lp | 6 | 1169747 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_013/P10/historical_csv_lp | 6 | 1169742 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_012/P10/historical_csv_lp | 6 | 1169733 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_007/P00/historical_csv_lp | 6 | 1169732 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_004/P10/historical_csv_lp | 6 | 1169727 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/validation_002/P10/full_precision_lp | 6 | 1169726 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_007/P10/full_precision_lp | 6 | 1169708 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_017/P00/historical_csv_lp | 6 | 1169702 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_004/P10/full_precision_lp | 6 | 1169701 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_015/P00/full_precision_lp | 6 | 1169700 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_012/P10/full_precision_lp | 6 | 1169694 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_006/P10/historical_csv_lp | 6 | 1169687 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_019/P10/full_precision_lp | 6 | 1169687 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_012/P00/full_precision_lp | 6 | 1169658 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_003/P00/historical_csv_lp | 6 | 1169656 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_019/P10/historical_csv_lp | 6 | 1169594 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_013/P10/full_precision_lp | 6 | 1169592 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_017/P10/full_precision_lp | 6 | 1169587 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_007/P00/full_precision_lp | 6 | 1169583 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_006/P00/full_precision_lp | 6 | 1169579 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_021/P10/sensitivity_1e-06 | 6 | 1169575 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_020/P00/historical_csv_lp | 6 | 1169573 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_020/P10/full_precision_lp | 6 | 1169564 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_006/P00/historical_csv_lp | 6 | 1169561 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_011/P10/historical_csv_lp | 6 | 1169540 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_018/P10/historical_csv_lp | 6 | 1169536 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_020/P10/historical_csv_lp | 6 | 1169521 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_012/P00/historical_csv_lp | 6 | 1169472 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_002/P00/full_precision_lp | 6 | 1169448 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_009/P00/historical_csv_lp | 6 | 1169399 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_011/P10/full_precision_lp | 6 | 1169374 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_002/P00/historical_csv_lp | 6 | 1169338 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_007/P10/historical_csv_lp | 6 | 1169316 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_008/P10/full_precision_lp | 6 | 1169289 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_003/P10/full_precision_lp | 6 | 1169259 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_008/P00/full_precision_lp | 6 | 1169093 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_003/P10/historical_csv_lp | 6 | 1169049 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_016/P00/full_precision_lp | 6 | 1168973 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_016/P00/historical_csv_lp | 6 | 1168871 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_008/P00/historical_csv_lp | 6 | 1168653 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_010/P11/full_precision_lp | 6 | 1167888 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_003/P11/historical_csv_lp | 6 | 1167735 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_018/P11/full_precision_lp | 6 | 1167699 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_010/P11/historical_csv_lp | 6 | 1167650 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_009/P11/full_precision_lp | 6 | 1167580 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_017/P11/historical_csv_lp | 6 | 1167558 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_014/P11/historical_csv_lp | 6 | 1167551 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_017/P11/full_precision_lp | 6 | 1167504 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_009/P11/historical_csv_lp | 6 | 1167502 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_013/P11/full_precision_lp | 6 | 1167488 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_001/P11/full_precision_lp | 6 | 1167453 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_012/P11/full_precision_lp | 6 | 1167452 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_016/P11/full_precision_lp | 6 | 1167437 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_019/P11/historical_csv_lp | 6 | 1167425 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_014/P11/full_precision_lp | 6 | 1167387 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_006/P11/full_precision_lp | 6 | 1167379 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_018/P11/historical_csv_lp | 6 | 1167352 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_019/P11/full_precision_lp | 6 | 1167297 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_001/P11/historical_csv_lp | 6 | 1167286 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_016/P11/historical_csv_lp | 6 | 1167263 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_003/P11/full_precision_lp | 6 | 1167141 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_012/P11/historical_csv_lp | 6 | 1167108 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_004/P11/historical_csv_lp | 6 | 1167097 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_006/P11/historical_csv_lp | 6 | 1167055 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_007/P11/full_precision_lp | 6 | 1167040 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_004/P11/full_precision_lp | 6 | 1166954 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_013/P11/historical_csv_lp | 6 | 1166858 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_020/P11/full_precision_lp | 6 | 1166824 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_007/P11/historical_csv_lp | 6 | 1166778 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_011/P11/full_precision_lp | 6 | 1166770 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_005/P11/full_precision_lp | 6 | 1166720 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_020/P11/historical_csv_lp | 6 | 1166713 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080751Z/pilot_021/P11/full_precision_lp | 6 | 1166568 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_021/P11/full_precision_lp | 6 | 1166568 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/validation_001/P11/full_precision_lp | 6 | 1166537 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_015/P11/historical_csv_lp | 6 | 1166514 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/validation_001/P11/historical_csv_lp | 6 | 1166498 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_015/P11/full_precision_lp | 6 | 1166484 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_008/P11/historical_csv_lp | 6 | 1166462 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080751Z/pilot_021/P11/historical_csv_lp | 6 | 1166459 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_021/P11/historical_csv_lp | 6 | 1166459 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_005/P11/historical_csv_lp | 6 | 1166407 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_002/P11/full_precision_lp | 6 | 1166314 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/validation_002/P11/full_precision_lp | 6 | 1166241 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_002/P11/historical_csv_lp | 6 | 1166225 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_008/P11/full_precision_lp | 6 | 1166117 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/validation_002/P11/historical_csv_lp | 6 | 1165997 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_011/P11/historical_csv_lp | 6 | 1165932 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_001/P01/full_precision_lp | 6 | 1164006 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_004/P01/full_precision_lp | 6 | 1163914 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_021/P01/full_precision_lp | 6 | 1163891 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_008/P01/historical_csv_lp | 6 | 1163814 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/validation_001/P01/full_precision_lp | 6 | 1163812 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_002/P01/full_precision_lp | 6 | 1163755 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_018/P01/historical_csv_lp | 6 | 1163706 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_016/P01/historical_csv_lp | 6 | 1163692 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_004/P01/historical_csv_lp | 6 | 1163689 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_021/P01/historical_csv_lp | 6 | 1163683 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_009/P01/historical_csv_lp | 6 | 1163601 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_011/P01/full_precision_lp | 6 | 1163582 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_010/P01/historical_csv_lp | 6 | 1163539 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_017/P01/historical_csv_lp | 6 | 1163539 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_009/P01/full_precision_lp | 6 | 1163511 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_005/P01/full_precision_lp | 6 | 1163467 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_002/P01/historical_csv_lp | 6 | 1163435 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_013/P01/full_precision_lp | 6 | 1163433 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_008/P01/full_precision_lp | 6 | 1163418 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_016/P01/full_precision_lp | 6 | 1163380 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_015/P01/full_precision_lp | 6 | 1163365 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/validation_001/P01/historical_csv_lp | 6 | 1163350 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_003/P01/full_precision_lp | 6 | 1163315 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_014/P01/full_precision_lp | 6 | 1163283 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_007/P01/full_precision_lp | 6 | 1163267 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_005/P01/historical_csv_lp | 6 | 1163245 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_010/P01/full_precision_lp | 6 | 1163241 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_012/P01/full_precision_lp | 6 | 1163230 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_020/P01/full_precision_lp | 6 | 1163194 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_014/P01/historical_csv_lp | 6 | 1163147 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_001/P01/historical_csv_lp | 6 | 1163112 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_012/P01/historical_csv_lp | 6 | 1163102 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/validation_002/P01/full_precision_lp | 6 | 1163083 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_007/P01/historical_csv_lp | 6 | 1163081 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_011/P01/historical_csv_lp | 6 | 1163059 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/validation_002/P01/historical_csv_lp | 6 | 1163024 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_015/P01/historical_csv_lp | 6 | 1162969 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_003/P01/historical_csv_lp | 6 | 1162895 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_013/P01/historical_csv_lp | 6 | 1162883 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_006/P01/full_precision_lp | 6 | 1162878 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_019/P01/historical_csv_lp | 6 | 1162796 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_006/P01/historical_csv_lp | 6 | 1162760 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_019/P01/full_precision_lp | 6 | 1162728 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_020/P01/historical_csv_lp | 6 | 1162688 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_018/P01/full_precision_lp | 6 | 1162661 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_017/P01/full_precision_lp | 6 | 1162279 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_021/P10/sensitivity_1e-08 | 6 | 1161681 |
| journal_article/qa/batch4/runtime/data/miktex/log/makefmt/pdflatex | 17 | 1160233 |
| journal_article/qa/batch4/runtime/inc/lib/auto/DBD/SQLite | 1 | 1156608 |
| journal_article/qa/batch4/runtime/inc/lib/auto/Encode/JIS2K | 1 | 1110528 |
| journal_article/qa/batch4/runtime/inc/lib/unicore/To | 44 | 1085962 |
| journal_article/qa/batch4/runtime/data/miktex/data/le | 4 | 1077279 |
| journal_article/qa/batch4/runtime/inc/lib/auto/Encode/CN | 1 | 1073664 |
| thesis_extension/environment/legacy_R343_library/Rcpp/libs/i386 | 1 | 1071630 |
| journal_article/qa/batch4/runtime/inc/lib/auto/Encode/TW | 1 | 1062912 |
| Empirical_work/hqreg_data | 35 | 1057343 |
| thesis_extension/environment/legacy_R343_library/hdm/data | 4 | 1044518 |
| journal_article/qa/batch4/runtime/data/fonts/map/pdftex | 3 | 1026625 |
| journal_validation/publication_review/lssp_canonical_build | 2 | 1024446 |
| thesis_extension/environment/legacy_R343_library/Rcpp/libs/x64 | 1 | 1007616 |
| journal_article/qa/batch4/runtime/inc/lib/DateTime/TimeZone/Asia | 77 | 995944 |
| journal_article/qa/batch4/runtime/inc/lib/Module | 5 | 958087 |
| thesis/figures/generated | 10 | 947155 |
| journal_article/qa/batch4/runtime/inc/lib/DBD | 14 | 933797 |
| journal_article/figures/generated | 7 | 933567 |
| journal_article/submission/work/named_source/figures/generated | 7 | 933567 |
| journal_article/submission/work/review_source/figures/generated | 7 | 933567 |
| journal_validation/publication_review/lssp_canonical_build/source/figures/generated | 7 | 933567 |
| journal_validation/publication_review/lssp_optimization/source/figures/generated | 7 | 933567 |
| journal_article/qa/batch4/runtime/inc/lib/Unicode/Collate/Locale | 87 | 932463 |
| journal_validation/stage2g/deterministic_implementation | 16 | 927906 |
| docs/author_replication_report | 3 | 922143 |
| journal_article/qa/batch4/runtime/inc/lib/auto/CryptX | 1 | 912384 |
| Empirical_work/quantreg_data | 29 | 909034 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_021/P10/sensitivity_0 | 6 | 893625 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080751Z/full_precision/pilot_001 | 18 | 864169 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080751Z/full_precision/pilot_002 | 18 | 864169 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080751Z/full_precision/pilot_003 | 18 | 864169 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080751Z/full_precision/pilot_004 | 18 | 864169 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080751Z/full_precision/pilot_005 | 18 | 864169 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080751Z/full_precision/pilot_006 | 18 | 864169 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080751Z/full_precision/pilot_007 | 18 | 864169 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080751Z/full_precision/pilot_008 | 18 | 864169 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080751Z/full_precision/pilot_009 | 18 | 864169 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080751Z/full_precision/pilot_010 | 18 | 864169 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080751Z/full_precision/pilot_011 | 18 | 864169 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080751Z/full_precision/pilot_012 | 18 | 864169 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080751Z/full_precision/pilot_013 | 18 | 864169 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080751Z/full_precision/pilot_014 | 18 | 864169 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080751Z/full_precision/pilot_015 | 18 | 864169 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080751Z/full_precision/pilot_016 | 18 | 864169 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080751Z/full_precision/pilot_017 | 18 | 864169 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080751Z/full_precision/pilot_018 | 18 | 864169 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080751Z/full_precision/pilot_019 | 18 | 864169 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080751Z/full_precision/pilot_020 | 18 | 864169 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080751Z/full_precision/pilot_021 | 18 | 864169 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080751Z/full_precision/validation_001 | 18 | 864169 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080751Z/full_precision/validation_002 | 18 | 864169 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/full_precision/pilot_001 | 18 | 864169 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/full_precision/pilot_002 | 18 | 864169 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/full_precision/pilot_003 | 18 | 864169 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/full_precision/pilot_004 | 18 | 864169 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/full_precision/pilot_005 | 18 | 864169 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/full_precision/pilot_006 | 18 | 864169 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/full_precision/pilot_007 | 18 | 864169 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/full_precision/pilot_008 | 18 | 864169 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/full_precision/pilot_009 | 18 | 864169 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/full_precision/pilot_010 | 18 | 864169 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/full_precision/pilot_011 | 18 | 864169 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/full_precision/pilot_012 | 18 | 864169 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/full_precision/pilot_013 | 18 | 864169 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/full_precision/pilot_014 | 18 | 864169 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/full_precision/pilot_015 | 18 | 864169 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/full_precision/pilot_016 | 18 | 864169 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/full_precision/pilot_017 | 18 | 864169 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/full_precision/pilot_018 | 18 | 864169 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/full_precision/pilot_019 | 18 | 864169 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/full_precision/pilot_020 | 18 | 864169 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/full_precision/pilot_021 | 18 | 864169 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/full_precision/validation_001 | 18 | 864169 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/full_precision/validation_002 | 18 | 864169 |
| journal_article/qa/batch4/runtime/inc/lib/auto/Unicode/Collate | 1 | 852480 |
| thesis_extension/environment/legacy_R343_library/tibble/libs/i386 | 1 | 830478 |
| thesis_extension/environment/legacy_R343_library/reshape2/libs/i386 | 1 | 824846 |
| journal_article/qa/batch4/runtime/inc/lib/Date/Manip | 11 | 810625 |
| thesis_extension/environment/legacy_R343_library/scales/libs/i386 | 1 | 806414 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r11 | 4 | 804816 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r04 | 4 | 804798 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r07 | 4 | 804797 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r12 | 4 | 804790 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r05 | 4 | 804760 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r13 | 4 | 804752 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r15 | 4 | 804746 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r08 | 4 | 804743 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r01 | 4 | 804736 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r17 | 4 | 804730 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r20 | 4 | 804723 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r03 | 4 | 804720 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r09 | 4 | 804717 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r18 | 4 | 804688 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r19 | 4 | 804688 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r16 | 4 | 804681 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r02 | 4 | 804678 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r06 | 4 | 804637 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r10 | 4 | 804634 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs/n500_r14 | 4 | 804625 |
| thesis_extension/environment/legacy_R343_library/ggplot2/data | 3 | 799874 |
| thesis_extension/environment/legacy_R343_library/tibble/libs/x64 | 1 | 783872 |
| thesis_extension/environment/legacy_R343_library/SparseM/extdata | 3 | 783747 |
| thesis_extension/environment/legacy_R343_library/plyr/libs/i386 | 1 | 780814 |
| thesis_extension/environment/legacy_R343_library/reshape2/libs/x64 | 1 | 777216 |
| journal_article/qa/batch4/runtime/inc/lib/auto/re | 1 | 768512 |
| docs/author_replication_report/figures | 8 | 763490 |
| thesis_extension/environment/legacy_R343_library/scales/libs/x64 | 1 | 763392 |
| journal_validation/stage2g/full_path_validation | 21 | 762519 |
| thesis_extension/environment/legacy_R343_library/glmnet/doc | 7 | 743164 |
| thesis_extension/environment/legacy_R343_library/plyr/libs/x64 | 1 | 737792 |
| journal_article/qa/batch4/runtime/inc/lib/Biber | 22 | 714606 |
| thesis_extension/environment/legacy_R343_library/ggplot2/html | 165 | 644130 |
| thesis_extension/reporting | 7 | 630843 |
| thesis_extension/environment/legacy_R343_library/R6/doc | 13 | 582814 |
| thesis_extension/environment/legacy_R343_library/glmnet/libs/i386 | 1 | 579598 |
| thesis_extension/environment/legacy_R343_library/ggplot2/help | 5 | 571652 |
| journal_article/qa/batch4/runtime/inc/lib/auto/Net/SSLeay | 77 | 541184 |
| thesis_extension/environment/legacy_R343_library/glmnet/libs/x64 | 1 | 539648 |
| journal_validation/publication_review | 13 | 531479 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/inputs | 4 | 529731 |
| journal_article/qa/batch4/runtime/inc/lib/Unicode/Collate/CJK | 7 | 523509 |
| thesis_extension/environment/legacy_R343_library/glmnet/data | 8 | 494136 |
| thesis_extension/environment/legacy_R343_library/SparseM/doc | 4 | 475757 |
| thesis_extension/environment/legacy_R343_library/plyr/data | 3 | 472915 |
| Empirical_work | 7 | 469042 |
| journal_article/qa/batch4/runtime/inc/lib/Math | 3 | 467186 |
| thesis_extension/environment/legacy_R343_library/stringi/html | 95 | 463892 |
| journal_article/qa/batch4/runtime/inc/lib/ExtUtils | 21 | 448200 |
| thesis_extension/environment/legacy_R343_library/quantreg/libs/i386 | 1 | 442382 |
| journal_article/qa/batch4/runtime/inc/lib/auto/DBI | 9 | 435305 |
| journal_validation/stage2h/readiness | 23 | 430639 |
| thesis_extension/environment/legacy_R343_library/hdm/doc | 3 | 411741 |
| journal_article/qa/batch4/runtime/inc/lib/Date/Manip/Offset | 445 | 409452 |
| thesis_extension/environment/legacy_R343_library/Rcpp/include/Rcpp/generated | 9 | 405582 |
| thesis_extension/environment/legacy_R343_library/ggplot2/R | 3 | 400198 |
| journal_article/qa/batch4/runtime/inc/lib/auto/Unicode/Normalize | 1 | 386560 |
| thesis_extension/environment/legacy_R343_library/stringi/help | 5 | 383183 |
| thesis_extension/environment/legacy_R343_library/quantreg/libs/x64 | 1 | 380928 |
| thesis_extension/environment/legacy_R343_library/rlang/html | 128 | 375997 |
| journal_article/qa/batch4/runtime/inc/lib/auto/Encode/Byte | 2 | 372736 |
| journal_article/qa/batch4/runtime/inc/lib/auto/Encode/EUCJPASCII | 1 | 368640 |
| journal_article/qa/batch4/runtime/inc/lib/Text | 9 | 355400 |
| journal_article/qa/batch4/runtime/inc/lib/DateTime/TimeZone | 17 | 351765 |
| journal_article/qa/batch4/runtime/inc/lib/auto/XML/LibXML | 1 | 349696 |
| thesis_extension/environment/legacy_R343_library/checkmate/html | 61 | 349244 |
| journal_article/qa/batch4/runtime/inc/lib/auto/DBD/Oracle | 5 | 346556 |
| thesis_extension/environment/legacy_R343_library/foreach/doc | 7 | 339433 |
| thesis_extension/environment/legacy_R343_library/checkmate/doc | 4 | 335397 |
| thesis_extension/environment/legacy_R343_library/SparseM/libs/x64 | 1 | 329622 |
| thesis_extension/environment/legacy_R343_library/rlang/help | 5 | 325915 |
| journal_article/qa/batch4/runtime/inc/lib/File | 14 | 318202 |
| journal_validation/publication_review/lssp_optimization/build/technical_supplement | 6 | 314433 |
| thesis_extension/environment/legacy_R343_library/quantreg/html | 68 | 298770 |
| journal_article/qa/batch4/runtime/inc/lib/Regexp/Common | 14 | 297310 |
| thesis_extension/environment/legacy_R343_library/checkmate/help | 5 | 294067 |
| thesis_extension/environment/legacy_R343_library/iterators/doc | 7 | 288832 |
| journal_article/qa/batch4/runtime/inc/lib/XML | 6 | 286302 |
| thesis_extension/environment/legacy_R343_library/Rcpp/include/Rcpp/sugar/functions | 51 | 285370 |
| journal_article/qa/batch4/runtime/inc/lib/DateTime/Locale | 6 | 283927 |
| thesis_extension/diagnostics/coverage_audit/figures | 28 | 281694 |
| journal_article/qa/batch4/runtime/inc/lib/Unicode | 5 | 277870 |
| thesis_extension/environment/legacy_R343_library/Rcpp/unitTests | 41 | 274388 |
| journal_article/qa/batch4/runtime/inc/lib/Log/Log4perl | 15 | 271890 |
| thesis_extension/reporting/figures | 11 | 267339 |
| journal_article/qa/batch4/runtime/inc/lib/DateTime/TimeZone/Australia | 12 | 267128 |
| thesis_extension/environment/legacy_R343_library/MatrixModels/R | 3 | 263808 |
| journal_article/qa/batch4/runtime/inc/lib/Win32 | 6 | 256196 |
| journal_article/qa/batch4/runtime/inc/lib/auto/DBD/Pg | 1 | 253952 |
| journal_article/qa/batch4/runtime/inc/lib/auto/Math/BigInt/GMP | 1 | 251392 |
| journal_article/qa/batch4/runtime/inc/lib/Net | 11 | 249804 |
| journal_article/qa/batch4/runtime/inc/lib/DateTime/TimeZone/Africa | 20 | 246578 |
| journal_article/submission/work/tables_build | 6 | 243915 |
| thesis_extension/environment/legacy_R343_library/quantreg/help | 5 | 242039 |
| thesis_extension/environment/legacy_R343_library/colorspace/doc | 4 | 235400 |
| journal_article/qa/batch4/runtime/inc/lib/DateTime/TimeZone/Atlantic | 9 | 233295 |
| journal_article/qa/batch4/runtime/inc/lib/Business/ISBN | 2 | 232415 |
| journal_article/qa/batch4/runtime/inc/lib/IO/Socket/SSL | 1 | 229678 |
| thesis_extension/reporting/output | 21 | 228738 |
| thesis_extension/environment/legacy_R343_library/Rcpp/include/Rcpp | 48 | 224709 |
| thesis_extension/validation/R343_final_audit/smoke_output | 6 | 223491 |
| journal_article/qa/batch4/runtime/inc/lib/Mozilla/CA | 1 | 222971 |
| journal_article/qa/batch4/runtime/inc/lib/Parse | 1 | 222044 |
| thesis_extension/calibration/instrument_strength_100rep | 6 | 216791 |
| journal_article/qa/batch4/runtime/inc/lib/DateTime/TimeZone/Pacific | 36 | 213009 |
| journal_article/qa/batch4/runtime/inc/lib/DateTime/TimeZone/America/Indiana | 8 | 212980 |
| thesis_extension/environment/legacy_R343_library/plyr/html | 95 | 211354 |
| journal_article/qa/batch4/runtime/inc/lib/B | 1 | 210212 |
| journal_validation/stage2c/stability/saved_stability_20261029T084737Z/pilot_009/P00 | 29 | 207566 |
| journal_validation/stage2c/stability/saved_stability_20261029T084737Z/pilot_019/P10 | 29 | 207560 |
| journal_validation/stage2c/stability/saved_stability_20261029T084737Z/pilot_016/P00 | 29 | 207558 |
| journal_validation/stage2c/stability/saved_stability_20261029T084737Z/pilot_019/P00 | 29 | 207546 |
| journal_validation/stage2c/stability/saved_stability_20261029T084737Z/pilot_014/P10 | 29 | 207528 |
| journal_validation/stage2c/stability/saved_stability_20261029T084737Z/pilot_020/P10 | 29 | 207505 |
| journal_validation/stage2c/stability/saved_stability_20261029T084737Z/pilot_002/P10 | 29 | 207501 |
| journal_validation/stage2c/stability/saved_stability_20261029T084737Z/pilot_016/P10 | 29 | 207496 |
| journal_validation/stage2c/stability/saved_stability_20261029T084737Z/pilot_006/P10 | 29 | 207488 |
| journal_validation/stage2c/stability/saved_stability_20261029T084737Z/pilot_008/P00 | 29 | 207481 |
| journal_validation/stage2c/stability/saved_stability_20261029T084737Z/pilot_009/P10 | 29 | 207471 |
| journal_validation/stage2c/stability/saved_stability_20261029T084737Z/pilot_017/P10 | 29 | 207464 |
| journal_validation/stage2c/stability/saved_stability_20261029T084737Z/pilot_020/P00 | 29 | 207461 |
| journal_validation/stage2c/stability/saved_stability_20261029T084737Z/pilot_003/P10 | 29 | 207458 |
| journal_validation/stage2c/stability/saved_stability_20261029T084737Z/pilot_015/P00 | 29 | 207449 |
| journal_validation/stage2c/stability/saved_stability_20261029T084737Z/pilot_002/P00 | 29 | 207438 |
| journal_validation/stage2c/stability/saved_stability_20261029T084737Z/pilot_006/P00 | 29 | 207429 |
| journal_validation/stage2c/stability/saved_stability_20261029T084737Z/pilot_013/P00 | 29 | 207425 |
| journal_validation/stage2c/stability/saved_stability_20261029T084737Z/pilot_005/P00 | 29 | 207424 |
| journal_validation/stage2c/stability/saved_stability_20261029T084737Z/validation_002/P10 | 29 | 207424 |
| journal_validation/stage2c/stability/saved_stability_20261029T084737Z/pilot_004/P10 | 29 | 207420 |
| journal_validation/stage2c/stability/saved_stability_20261029T084737Z/pilot_007/P10 | 29 | 207415 |
| journal_validation/stage2c/stability/saved_stability_20261029T084737Z/pilot_001/P10 | 29 | 207413 |
| journal_validation/stage2c/stability/saved_stability_20261029T084737Z/pilot_008/P10 | 29 | 207413 |
| journal_validation/stage2c/stability/saved_stability_20261029T084737Z/pilot_021/P00 | 29 | 207408 |
| journal_validation/stage2c/stability/saved_stability_20261029T084737Z/pilot_005/P10 | 29 | 207388 |
| journal_validation/stage2c/stability/saved_stability_20261029T084737Z/pilot_015/P10 | 29 | 207385 |
| journal_validation/stage2c/stability/saved_stability_20261029T084737Z/pilot_001/P00 | 29 | 207383 |
| journal_validation/stage2c/stability/saved_stability_20261029T084737Z/pilot_014/P00 | 29 | 207383 |
| journal_validation/stage2c/stability/saved_stability_20261029T084737Z/validation_002/P00 | 29 | 207381 |
| journal_validation/stage2c/stability/saved_stability_20261029T084737Z/pilot_018/P10 | 29 | 207360 |
| journal_validation/stage2c/stability/saved_stability_20261029T084737Z/pilot_007/P00 | 29 | 207359 |
| journal_validation/stage2c/stability/saved_stability_20261029T084737Z/validation_001/P10 | 29 | 207356 |
| journal_validation/stage2c/stability/saved_stability_20261029T084737Z/pilot_011/P00 | 29 | 207352 |
| journal_validation/stage2c/stability/saved_stability_20261029T084737Z/pilot_010/P00 | 29 | 207351 |
| journal_validation/stage2c/stability/saved_stability_20261029T084737Z/pilot_003/P00 | 29 | 207344 |
| journal_validation/stage2c/stability/saved_stability_20261029T084737Z/pilot_011/P10 | 29 | 207342 |
| journal_validation/stage2c/stability/saved_stability_20261029T084737Z/pilot_012/P00 | 29 | 207336 |
| journal_validation/stage2c/stability/saved_stability_20261029T084737Z/pilot_021/P10 | 29 | 207335 |
| journal_validation/stage2c/stability/saved_stability_20261029T084737Z/pilot_017/P00 | 29 | 207328 |
| journal_validation/stage2c/stability/saved_stability_20261029T084737Z/pilot_013/P10 | 29 | 207324 |
| journal_validation/stage2c/stability/saved_stability_20261029T084737Z/pilot_004/P00 | 29 | 207321 |
| journal_validation/stage2c/stability/saved_stability_20261029T084737Z/pilot_018/P00 | 29 | 207319 |
| journal_validation/stage2c/stability/saved_stability_20261029T084737Z/pilot_010/P10 | 29 | 207286 |
| journal_validation/stage2c/stability/saved_stability_20261029T084737Z/pilot_012/P10 | 29 | 207265 |
| journal_validation/stage2c/stability/saved_stability_20261029T084737Z/validation_001/P00 | 29 | 207217 |
| thesis_extension/environment/legacy_R343_library/checkmate/R | 3 | 199388 |
| journal_article/qa/batch4/runtime/inc/lib/DateTime/TimeZone/America/Argentina | 12 | 195688 |
| thesis_extension/environment/legacy_R343_library/plyr/help | 5 | 192786 |
| journal_article/qa/batch4/runtime/inc/lib/auto/Unicode/LineBreak | 1 | 192512 |
| thesis_extension/environment/legacy_R343_library/SparseM/R | 3 | 190488 |
| journal_article/qa/batch4/runtime/inc/lib/IO/Socket | 5 | 185551 |
| journal_validation/stage2c/stability/saved_stability_20261029T084737Z/pilot_015/P01 | 29 | 179479 |
| journal_validation/stage2c/stability/saved_stability_20261029T084737Z/pilot_019/P11 | 29 | 179443 |
| journal_validation/stage2c/stability/saved_stability_20261029T084737Z/pilot_005/P01 | 29 | 179439 |
| journal_validation/stage2c/stability/saved_stability_20261029T084737Z/pilot_016/P01 | 29 | 179429 |
| journal_validation/stage2c/stability/saved_stability_20261029T084737Z/pilot_016/P11 | 29 | 179421 |
| journal_validation/stage2c/stability/saved_stability_20261029T084737Z/pilot_012/P01 | 29 | 179417 |
| journal_validation/stage2c/stability/saved_stability_20261029T084737Z/pilot_012/P11 | 29 | 179415 |
| journal_validation/stage2c/stability/saved_stability_20261029T084737Z/pilot_003/P11 | 29 | 179411 |
| journal_validation/stage2c/stability/saved_stability_20261029T084737Z/pilot_018/P01 | 29 | 179409 |
| journal_validation/stage2c/stability/saved_stability_20261029T084737Z/pilot_002/P11 | 29 | 179392 |
| journal_validation/stage2c/stability/saved_stability_20261029T084737Z/pilot_015/P11 | 29 | 179387 |
| journal_validation/stage2c/stability/saved_stability_20261029T084737Z/pilot_014/P01 | 29 | 179376 |
| journal_validation/stage2c/stability/saved_stability_20261029T084737Z/pilot_003/P01 | 29 | 179373 |
| journal_validation/stage2c/stability/saved_stability_20261029T084737Z/pilot_019/P01 | 29 | 179370 |
| journal_validation/stage2c/stability/saved_stability_20261029T084737Z/pilot_006/P01 | 29 | 179369 |
| journal_validation/stage2c/stability/saved_stability_20261029T084737Z/pilot_014/P11 | 29 | 179367 |
| journal_validation/stage2c/stability/saved_stability_20261029T084737Z/pilot_020/P11 | 29 | 179367 |
| journal_validation/stage2c/stability/saved_stability_20261029T084737Z/pilot_008/P11 | 29 | 179359 |
| journal_validation/stage2c/stability/saved_stability_20261029T084737Z/pilot_001/P01 | 29 | 179355 |
| journal_validation/stage2c/stability/saved_stability_20261029T084737Z/pilot_020/P01 | 29 | 179348 |
| journal_validation/stage2c/stability/saved_stability_20261029T084737Z/pilot_008/P01 | 29 | 179347 |
| journal_validation/stage2c/stability/saved_stability_20261029T084737Z/pilot_006/P11 | 29 | 179346 |
| journal_validation/stage2c/stability/saved_stability_20261029T084737Z/pilot_010/P11 | 29 | 179346 |
| journal_validation/stage2c/stability/saved_stability_20261029T084737Z/validation_002/P01 | 29 | 179343 |
| journal_validation/stage2c/stability/saved_stability_20261029T084737Z/pilot_017/P11 | 29 | 179333 |
| journal_validation/stage2c/stability/saved_stability_20261029T084737Z/pilot_017/P01 | 29 | 179330 |
| journal_validation/stage2c/stability/saved_stability_20261029T084737Z/pilot_007/P01 | 29 | 179326 |
| journal_validation/stage2c/stability/saved_stability_20261029T084737Z/pilot_011/P11 | 29 | 179323 |
| journal_validation/stage2c/stability/saved_stability_20261029T084737Z/validation_001/P01 | 29 | 179320 |
| journal_validation/stage2c/stability/saved_stability_20261029T084737Z/pilot_018/P11 | 29 | 179319 |
| journal_validation/stage2c/stability/saved_stability_20261029T084737Z/validation_002/P11 | 29 | 179319 |
| journal_validation/stage2c/stability/saved_stability_20261029T084737Z/pilot_004/P11 | 29 | 179318 |
| journal_validation/stage2c/stability/saved_stability_20261029T084737Z/pilot_021/P01 | 29 | 179317 |
| journal_validation/stage2c/stability/saved_stability_20261029T084737Z/pilot_013/P11 | 29 | 179315 |
| journal_validation/stage2c/stability/saved_stability_20261029T084737Z/pilot_021/P11 | 29 | 179314 |
| journal_validation/stage2c/stability/saved_stability_20261029T084737Z/pilot_010/P01 | 29 | 179313 |
| journal_validation/stage2c/stability/saved_stability_20261029T084737Z/pilot_013/P01 | 29 | 179311 |
| journal_validation/stage2c/stability/saved_stability_20261029T084737Z/pilot_001/P11 | 29 | 179299 |
| journal_validation/stage2c/stability/saved_stability_20261029T084737Z/pilot_007/P11 | 29 | 179295 |
| journal_validation/stage2c/stability/saved_stability_20261029T084737Z/pilot_009/P11 | 29 | 179285 |
| journal_validation/stage2c/stability/saved_stability_20261029T084737Z/pilot_004/P01 | 29 | 179284 |
| journal_validation/stage2c/stability/saved_stability_20261029T084737Z/pilot_002/P01 | 29 | 179275 |
| journal_validation/stage2c/stability/saved_stability_20261029T084737Z/pilot_009/P01 | 29 | 179269 |
| journal_article/qa/batch4/runtime/inc/lib/Math/BigInt | 6 | 179244 |
| journal_validation/stage2c/stability/saved_stability_20261029T084737Z/pilot_011/P01 | 29 | 179243 |
| journal_validation/stage2c/stability/saved_stability_20261029T084737Z/validation_001/P11 | 29 | 179215 |
| journal_validation/stage2c/stability/saved_stability_20261029T084737Z/pilot_005/P11 | 29 | 179138 |
| thesis_extension/environment/legacy_R343_library/Rcpp | 8 | 171813 |
| journal_article/qa/batch4/runtime/inc/lib/DBD/ODBC | 3 | 171001 |
| thesis_extension/environment/legacy_R343_library/Rcpp/R | 3 | 169069 |
| journal_article/qa/batch4/runtime/inc/lib/auto/DBD/ODBC | 1 | 166400 |
| journal_validation/stage2c/validation_protocol/reassessment_20261029T083111Z/pilot_002/P11 | 4 | 164133 |
| journal_validation/stage2c/validation_protocol/reassessment_20261029T083111Z/pilot_019/P11 | 4 | 164043 |
| journal_validation/stage2c/validation_protocol/reassessment_20261029T083111Z/pilot_020/P11 | 4 | 163999 |
| thesis_extension/environment/legacy_R343_library/Rcpp/unitTests/cpp | 34 | 163894 |
| journal_validation/stage2c/validation_protocol/reassessment_20261029T083111Z/pilot_014/P11 | 4 | 163133 |
| journal_validation/stage2c/validation_protocol/reassessment_20261029T083111Z/pilot_004/P11 | 4 | 163027 |
| journal_validation/stage2c/validation_protocol/reassessment_20261029T083111Z/pilot_008/P11 | 4 | 163017 |
| journal_article/qa/batch4/runtime/inc/lib/unicore/lib/In | 22 | 162932 |
| journal_validation/stage2c/validation_protocol/reassessment_20261029T083111Z/pilot_003/P11 | 4 | 162169 |
| journal_validation/stage2c/validation_protocol/reassessment_20261029T083111Z/pilot_010/P11 | 4 | 162105 |
| journal_validation/stage2c/validation_protocol/reassessment_20261029T083111Z/pilot_021/P11 | 4 | 162045 |
| journal_validation/stage2c/validation_protocol/reassessment_20261029T083111Z/validation_001/P11 | 4 | 162002 |
| journal_validation/stage2c/validation_protocol/reassessment_20261029T083111Z/pilot_011/P11 | 4 | 161982 |
| journal_validation/stage2c/validation_protocol/reassessment_20261029T083111Z/pilot_012/P11 | 4 | 161954 |
| journal_validation/stage2c/validation_protocol/reassessment_20261029T083111Z/pilot_015/P11 | 4 | 161941 |
| journal_validation/stage2c/validation_protocol/reassessment_20261029T083111Z/pilot_007/P11 | 4 | 161928 |
| journal_validation/stage2c/validation_protocol/reassessment_20261029T083111Z/pilot_013/P11 | 4 | 161922 |
| journal_validation/stage2c/validation_protocol/reassessment_20261029T083111Z/pilot_017/P11 | 4 | 161885 |
| journal_validation/stage2c/validation_protocol/reassessment_20261029T083111Z/pilot_014/P01 | 4 | 161227 |
| journal_validation/stage2c/validation_protocol/reassessment_20261029T083111Z/pilot_016/P01 | 4 | 161200 |
| journal_validation/stage2c/validation_protocol/reassessment_20261029T083111Z/pilot_018/P11 | 4 | 161069 |
| thesis_extension/environment/legacy_R343_library/magrittr/doc | 4 | 161060 |
| journal_validation/stage2c/validation_protocol/reassessment_20261029T083111Z/pilot_006/P11 | 4 | 160940 |
| journal_validation/stage2c/validation_protocol/reassessment_20261029T083111Z/pilot_001/P11 | 4 | 160931 |
| journal_validation/stage2c/validation_protocol/reassessment_20261029T083111Z/validation_002/P11 | 4 | 160796 |
| journal_article/qa/batch4/runtime/inc/lib/Win32API | 2 | 160384 |
| journal_validation/stage2c/validation_protocol/reassessment_20261029T083111Z/pilot_015/P01 | 4 | 160266 |
| journal_validation/stage2c/validation_protocol/reassessment_20261029T083111Z/pilot_005/P01 | 4 | 160217 |
| journal_validation/stage2c/validation_protocol/reassessment_20261029T083111Z/validation_001/P01 | 4 | 160201 |
| journal_validation/stage2c/validation_protocol/reassessment_20261029T083111Z/pilot_010/P01 | 4 | 160073 |
| journal_validation/stage2c/validation_protocol/reassessment_20261029T083111Z/pilot_009/P11 | 4 | 160029 |
| journal_validation/stage2c/validation_protocol/reassessment_20261029T083111Z/pilot_016/P11 | 4 | 160009 |
| journal_article/qa/batch4/runtime/inc/lib/CPAN/Meta | 6 | 159497 |
| journal_validation/stage2c/validation_protocol/reassessment_20261029T083111Z/pilot_012/P01 | 4 | 159266 |
| journal_validation/stage2c/validation_protocol/reassessment_20261029T083111Z/pilot_008/P01 | 4 | 159195 |
| journal_validation/stage2c/validation_protocol/reassessment_20261029T083111Z/pilot_007/P01 | 4 | 159164 |
| journal_validation/stage2c/validation_protocol/reassessment_20261029T083111Z/pilot_004/P01 | 4 | 159139 |
| journal_validation/stage2c/validation_protocol/reassessment_20261029T083111Z/pilot_013/P01 | 4 | 159137 |
| journal_validation/stage2c/validation_protocol/reassessment_20261029T083111Z/pilot_011/P01 | 4 | 159134 |
| journal_validation/stage2c/validation_protocol/reassessment_20261029T083111Z/pilot_021/P01 | 4 | 159101 |
| journal_validation/stage2c/validation_protocol/reassessment_20261029T083111Z/pilot_002/P01 | 4 | 159050 |
| journal_validation/stage2c/validation_protocol/reassessment_20261029T083111Z/pilot_006/P01 | 4 | 159001 |
| journal_validation/stage2c/validation_protocol/reassessment_20261029T083111Z/validation_002/P01 | 4 | 158239 |
| journal_validation/stage2c/validation_protocol/reassessment_20261029T083111Z/pilot_019/P01 | 4 | 158238 |
| journal_article/qa/batch4/runtime/inc/lib/auto/Win32API/Registry | 1 | 158208 |
| journal_validation/stage2c/validation_protocol/reassessment_20261029T083111Z/pilot_020/P01 | 4 | 158204 |
| journal_validation/stage2c/validation_protocol/reassessment_20261029T083111Z/pilot_009/P01 | 4 | 158141 |
| journal_validation/stage2c/validation_protocol/reassessment_20261029T083111Z/pilot_003/P01 | 4 | 158134 |
| journal_validation/stage2c/validation_protocol/reassessment_20261029T083111Z/pilot_001/P01 | 4 | 158131 |
| journal_validation/stage2c/validation_protocol/reassessment_20261029T083111Z/pilot_017/P01 | 4 | 158116 |
| journal_article/qa/batch4/runtime/inc/lib/HTTP | 9 | 158047 |
| journal_validation/stage2c/validation_protocol/reassessment_20261029T083111Z/pilot_018/P01 | 4 | 157167 |
| journal_article/qa/batch4/runtime/inc/lib/IO/Uncompress | 5 | 156738 |
| journal_article/qa/batch4/runtime/inc/lib/Lingua/Translit | 1 | 155495 |
| thesis_extension/environment/legacy_R343_library/Rcpp/include/Rcpp/vector | 26 | 152582 |
| thesis_extension/environment/legacy_R343_library/Formula/doc | 4 | 151435 |
| journal_article/submission/qa | 14 | 151111 |
| thesis_extension/environment/legacy_R343_library/glmnet/mortran | 1 | 148317 |
| journal_article/qa/batch4/runtime/inc/lib/LWP | 6 | 147555 |
| journal_validation/stage2c/validation_protocol/reassessment_20261029T083111Z/pilot_005/P11 | 4 | 144539 |
| journal_article/qa/batch4/runtime/inc/lib/Biber/Input/file | 2 | 143124 |
| journal_article/qa/batch4/runtime/inc/lib/auto/Compress/Raw/Zlib | 1 | 139776 |
| journal_article/qa/batch4/runtime/inc/lib/Pod | 4 | 139457 |
| journal_article/qa/batch4/runtime/inc/lib/auto/DBD/mysql | 1 | 136192 |
| thesis_extension/environment/legacy_R343_library/lazyeval/doc | 7 | 133389 |
| journal_article/qa/batch4/runtime/inc/lib/auto/POSIX | 1 | 132096 |
| journal_article/qa/batch4/runtime/inc/lib/IO/Compress | 5 | 132094 |
| journal_validation/publication_review/lssp_optimization/source/tables/generated | 9 | 130228 |
| thesis_extension/environment/legacy_R343_library/scales/html | 76 | 129107 |
| journal_article/qa/batch4/runtime/inc/lib/auto/Storable | 1 | 125952 |
| journal_article/qa/batch4/runtime/inc/lib/Log | 2 | 125412 |
| thesis_extension/environment/legacy_R343_library/foreach/examples | 24 | 125250 |
| thesis_extension/environment/legacy_R343_library/dichromat/R | 5 | 124223 |
| journal_article/qa/batch4/runtime/inc/lib/Biber/Output | 6 | 123434 |
| journal_article/qa/batch4/runtime/inc | 2 | 122635 |
| journal_article/qa/batch4/runtime/inc/lib/Text/BibTeX | 6 | 121710 |
| thesis_extension/environment/legacy_R343_library/quantreg | 7 | 119912 |
| journal_article/qa/batch4/runtime/inc/lib/auto/Win32/OLE | 1 | 119808 |
| journal_article/qa/batch4/runtime/inc/lib/List | 4 | 118597 |
| journal_article/qa/batch4/runtime/inc/lib/Test | 2 | 116270 |
| journal_article/qa/batch4/runtime/inc/lib/Encode | 20 | 113914 |
| thesis_extension/environment/legacy_R343_library/hdm/html | 30 | 111505 |
| journal_article/qa/batch4/runtime/inc/lib/auto/List/MoreUtils/XS | 1 | 110080 |
| thesis_extension/environment/legacy_R343_library/scales/help | 5 | 109734 |
| journal_article/submission/work/named_source/tables/generated | 7 | 109593 |
| journal_article/submission/work/review_source/tables/generated | 7 | 109593 |
| journal_article/tables/generated | 7 | 109593 |
| journal_validation/publication_review/lssp_canonical_build/source/tables/generated | 7 | 109593 |
| journal_article/qa/batch4/runtime/inc/lib/DateTime/TimeZone/America/North_Dakota | 3 | 109353 |
| thesis/tables/generated | 7 | 109340 |
| journal_article/qa/batch4/runtime/inc/lib/auto/Encode | 2 | 109056 |
| thesis_extension/environment/legacy_R343_library/stringr/doc | 7 | 107484 |
| thesis_extension/environment/legacy_R343_library/Rcpp/html | 35 | 107080 |
| journal_article/qa/batch4/runtime/inc/lib/auto/Compress/Raw/Bzip2 | 1 | 107008 |
| journal_article/qa/batch4/runtime/inc/lib/Date/Manip/Lang | 17 | 106862 |
| thesis/sections | 6 | 106833 |
| journal_article/qa/batch4/runtime/inc/lib/IPC | 3 | 105669 |
| journal_article/qa/batch4/runtime/inc/lib/unicore/lib/Perl | 23 | 101742 |
| thesis_extension/environment/legacy_R343_library/quantreg/R | 3 | 101664 |
| journal_article/qa/batch4/runtime/inc/lib/IO | 9 | 101505 |
| journal_article/qa/batch4/runtime/inc/lib/Class | 6 | 100987 |
| journal_article/qa/batch4/runtime/inc/lib/JSON | 1 | 100557 |
| journal_article/qa/batch4/runtime/inc/lib/Log/Log4perl/Appender | 13 | 99931 |
| thesis_extension/environment/legacy_R343_library/SparseM/html | 26 | 97993 |
| journal_article/qa/batch4/runtime/inc/lib/Pod/Simple | 6 | 97944 |
| thesis_extension/environment/legacy_R343_library/digest/libs/i386 | 1 | 97806 |
| journal_article/qa/batch4/runtime/inc/lib/unicore/lib/Gc | 32 | 96820 |
| thesis_extension/environment/legacy_R343_library/rlang/R | 3 | 95641 |
| thesis_extension/environment/legacy_R343_library/munsell/raw | 3 | 95293 |
| thesis_extension/environment/legacy_R343_library/checkmate/libs/i386 | 1 | 95246 |
| thesis_extension/environment/legacy_R343_library/Rcpp/help | 5 | 94038 |
| thesis_extension/environment/legacy_R343_library/mvtnorm/doc | 4 | 92892 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_021/P11 | 3 | 91702 |
| thesis_extension/environment/legacy_R343_library/colorspace/R | 3 | 91610 |
| journal_article/qa/batch4/runtime/inc/lib/auto/Text/CSV_XS | 1 | 91136 |
| journal_article/qa/batch4/runtime/inc/lib/Data | 5 | 90744 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_021/P01 | 3 | 90603 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080751Z/pilot_021/P11 | 1 | 88453 |
| journal_article/qa/batch4/runtime/inc/lib/DateTime | 9 | 88038 |
| thesis_extension/environment/legacy_R343_library/ggplot2 | 7 | 87775 |
| thesis_extension/environment/legacy_R343_library/Rcpp/include/Rcpp/sugar/operators | 12 | 87687 |
| journal_validation/stage2e | 11 | 87240 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_021/P00 | 3 | 86010 |
| thesis_extension/environment/legacy_R343_library/SparseM/help | 5 | 85785 |
| journal_article/qa/batch4/runtime/inc/lib/Test2 | 4 | 85195 |
| thesis_extension/environment/legacy_R343_library/digest/libs/x64 | 1 | 84992 |
| thesis_extension/environment/legacy_R343_library/Rcpp/include/Rcpp/internal | 15 | 84809 |
| thesis_extension/environment/legacy_R343_library/mvtnorm/libs/i386 | 1 | 84494 |
| thesis_extension/environment/legacy_R343_library/hdm/help | 5 | 84305 |
| journal_article/qa/batch4/runtime/inc/lib/URI | 42 | 83795 |
| journal_article/qa/batch4/runtime/inc/lib/Getopt | 1 | 83322 |
| thesis_extension/environment/legacy_R343_library/mvtnorm/libs/x64 | 1 | 82432 |
| journal_validation/stage2b | 11 | 81233 |
| journal_article/qa/batch4/runtime/inc/lib/DateTime/TimeZone/America/Kentucky | 2 | 80802 |
| journal_article/qa/batch4/runtime/inc/lib/auto/B | 1 | 80384 |
| journal_article/qa/batch4/runtime/inc/lib/auto/List/SomeUtils/XS | 1 | 79872 |
| thesis_extension/diagnostics/coverage_audit/output | 8 | 79850 |
| simulation/simulation_quantreg | 6 | 79560 |
| journal_article/qa/batch4/runtime/inc/lib/Params | 4 | 78396 |
| thesis_extension/environment/legacy_R343_library/checkmate/libs/x64 | 1 | 77312 |
| journal_article/qa/batch4/runtime/inc/lib/Biber/LaTeX | 2 | 76935 |
| thesis_extension/environment/legacy_R343_library/Rcpp/include/Rcpp/traits | 42 | 76718 |
| journal_article/qa/batch4/runtime/inc/lib/Term | 2 | 75822 |
| journal_article/qa/batch4/runtime/inc/lib/auto/Win32API/File | 1 | 75776 |
| journal_article/qa/batch4/runtime/inc/lib/DBI/Const/GetInfo | 2 | 75721 |
| journal_validation/stage2g | 9 | 75702 |
| journal_article/qa/batch4/runtime/inc/lib/Log/Dispatch | 14 | 75174 |
| thesis_extension/environment/legacy_R343_library/stringr/html | 31 | 74986 |
| journal_article/qa/batch4/runtime/inc/lib/DateTime/TimeZone/Antarctica | 10 | 73301 |
| journal_article/qa/batch4/runtime/inc/lib/auto/Win32 | 1 | 73216 |
| thesis_extension/diagnostics/grid_sensitivity | 7 | 71900 |
| journal_article/qa/batch4/runtime/inc/lib/auto/XML/Parser/Expat | 1 | 71680 |
| thesis_extension/environment/legacy_R343_library/colorspace/html | 24 | 70922 |
| journal_article/qa/batch4/runtime/inc/lib/auto/Win32/Console | 1 | 70144 |
| journal_article/qa/batch4/runtime/inc/lib/DateTime/Format | 2 | 69998 |
| thesis_extension/environment/legacy_R343_library/munsell/R | 5 | 67906 |
| thesis_extension/environment/legacy_R343_library/SparseM/data | 2 | 67713 |
| thesis_extension/environment/legacy_R343_library/colorspace/help | 5 | 67585 |
| thesis_extension/environment/legacy_R343_library/glmnet/html | 14 | 66317 |
| journal_article/qa/batch4/runtime/inc/lib/DBD/SQLite | 3 | 65631 |
| journal_article/qa/batch4/runtime/inc/lib/auto/Data/Dumper | 1 | 65536 |
| journal_article/qa/batch4/runtime/inc/lib/DBI/DBD | 1 | 65095 |
| thesis_extension/environment/legacy_R343_library/colorspace/libs/i386 | 1 | 65038 |
| thesis_extension/environment/legacy_R343_library/stringr/help | 5 | 64579 |
| journal_article/qa/batch4/runtime/inc/lib/HTML | 3 | 63116 |
| journal_article/qa/batch4/runtime/inc/lib/LWP/Protocol | 11 | 63110 |
| journal_article/qa/batch4/runtime/inc/lib/Regexp/Common/URI | 18 | 61438 |
| thesis_extension/environment/legacy_R343_library/glmnet/help | 5 | 61318 |
| journal_article/qa/batch4/runtime/inc/lib/Specio | 10 | 61232 |
| thesis_extension/environment/legacy_R343_library/MatrixModels/html | 16 | 60244 |
| journal_article/qa/batch4/runtime/inc/lib/Win32/Unicode | 9 | 60095 |
| journal_article/qa/batch4/runtime/inc/lib/auto/Crypt/SSLeay | 1 | 59904 |
| thesis_extension/diagnostics/coverage_audit | 5 | 58893 |
| journal_article/qa/batch4/runtime/inc/lib/Compress/Raw | 2 | 58677 |
| thesis_extension/environment/legacy_R343_library/stringi/include | 2 | 58187 |
| journal_article/qa/batch4/runtime/inc/lib/Sub | 4 | 58148 |
| journal_validation/stage2a | 8 | 57719 |
| journal_article/qa/batch4/runtime/inc/lib/unicore/lib/Nv | 65 | 56709 |
| thesis_extension/environment/legacy_R343_library/stringi/R | 3 | 56488 |
| journal_article/qa/batch4/runtime/inc/lib/auto/List/Util | 1 | 56320 |
| journal_article/qa/batch4/runtime/inc/lib/unicore/lib/Scx | 68 | 55738 |
| thesis_extension/environment/legacy_R343_library/MatrixModels/help | 5 | 55544 |
| thesis_extension/environment/legacy_R343_library/colorspace/libs/x64 | 1 | 54272 |
| journal_article/qa/batch4/runtime/inc/lib/Test2/API | 3 | 53880 |
| thesis_extension/environment/legacy_R343_library/lazyeval/html | 28 | 53066 |
| journal_article/qa/batch4/runtime/inc/lib/auto/Params/Validate/XS | 2 | 52736 |
| journal_article/qa/batch4/runtime/inc/lib/auto/XML/LibXSLT | 1 | 52736 |
| thesis_extension/environment/legacy_R343_library/hdm/R | 3 | 52555 |
| journal_article/qa/batch4/runtime/inc/lib/Log/Log4perl/Config | 4 | 52246 |
| journal_validation/stage2c | 9 | 52147 |
| journal_article/qa/batch4/runtime/inc/lib/auto/Socket6 | 1 | 51712 |
| journal_article/qa/batch4/runtime/inc/lib/Sys | 2 | 51586 |
| journal_article/qa/batch4/runtime/inc/lib/auto/HTML/Parser | 1 | 51200 |
| journal_article/sections | 8 | 50815 |
| journal_validation/publication_review/lssp_canonical_build/source/sections | 8 | 50815 |
| journal_article/submission/work/named_source/sections | 8 | 50429 |
| journal_article/qa/batch4/runtime/inc/lib/Specio/Constraint | 12 | 50386 |
| thesis_extension/environment/legacy_R343_library/hqreg/libs/i386 | 1 | 50190 |
| thesis_extension/environment/legacy_R343_library/stringi | 8 | 50065 |
| journal_validation/stage2c/certification | 9 | 50049 |
| journal_article/submission/work/review_source/sections | 8 | 49881 |
| journal_validation/publication_review/lssp_optimization/source/sections | 8 | 49713 |
| thesis_extension/environment/legacy_R343_library/hqreg/libs/x64 | 1 | 49664 |
| journal_validation/stage2c/validation_protocol | 9 | 49585 |
| thesis_extension/environment/legacy_R343_library/tibble/R | 3 | 49437 |
| thesis_extension/environment/legacy_R343_library/scales/R | 3 | 48628 |
| thesis_extension/environment/legacy_R343_library/tibble/doc | 7 | 48536 |
| thesis_extension/environment/legacy_R343_library/rlang/libs/i386 | 1 | 48142 |
| journal_article/qa/batch4/runtime/inc/lib/Authen/SASL/Perl | 7 | 48000 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/pilot | 871 | 47641 |
| journal_validation/stage2c/stability | 8 | 46597 |
| journal_article/qa/batch4/runtime/inc/lib/unicore/lib/SB | 12 | 46441 |
| thesis_extension/environment/legacy_R343_library/lazyeval/help | 5 | 46160 |
| thesis_extension/environment/legacy_R343_library/hqreg/html | 10 | 46005 |
| journal_article/qa/batch4/runtime/inc/lib/MIME | 3 | 45351 |
| journal_article/qa/batch4/runtime/inc/lib/auto/Class/XSAccessor | 1 | 45056 |
| thesis_extension/environment/legacy_R343_library/glmnet/R | 3 | 45055 |
| thesis_extension/environment/legacy_R343_library/digest/doc | 4 | 44989 |
| thesis_extension/environment/legacy_R343_library/munsell/html | 28 | 44897 |
| journal_article/qa/batch4/runtime/inc/lib/Business | 5 | 44809 |
| thesis_extension/environment/legacy_R343_library/plyr/R | 3 | 44748 |
| journal_article/qa/batch4/runtime/inc/lib/XML/LibXML | 8 | 44026 |
| thesis_extension/environment/legacy_R343_library/Rcpp/include/Rcpp/utils | 1 | 43503 |
| journal_article/qa/batch4/runtime/inc/lib/unicore/lib/Lb | 20 | 43381 |
| thesis_extension/environment/legacy_R343_library/quantreg/data | 8 | 43342 |
| journal_article/qa/batch4/runtime/inc/lib/Mail | 6 | 43311 |
| thesis_extension/environment/legacy_R343_library/colorspace/data | 3 | 43261 |
| thesis_extension/environment/legacy_R343_library/mvtnorm/html | 9 | 43215 |
| thesis_extension/environment/legacy_R343_library/Rcpp/include/Rcpp/stats/random | 22 | 43186 |
| journal_article/qa/batch4/runtime/inc/lib/auto/Socket | 1 | 43008 |
| thesis/tools | 6 | 42842 |
| journal_article/qa/batch4/runtime/inc/lib/DBI/Gofer | 3 | 42595 |
| journal_article/qa/batch4/runtime/inc/lib/Time | 2 | 42001 |
| thesis_extension/environment/legacy_R343_library/rlang/libs/x64 | 1 | 41984 |
| thesis_extension/environment/legacy_R343_library/tibble/html | 18 | 41970 |
| thesis_extension/environment/legacy_R343_library/gtable/html | 22 | 41817 |
| journal_article/qa/batch4/runtime/inc/lib/unicore/lib/Age | 20 | 40788 |
| thesis_extension/environment/legacy_R343_library/Rcpp/include/Rcpp/macros | 10 | 40271 |
| journal_article/qa/batch4/runtime/inc/lib/Win32/API | 2 | 39688 |
| journal_article/qa/batch4/runtime/inc/lib/Win32/OLE | 3 | 39234 |
| journal_article/qa/batch4/runtime/inc/lib/DBI | 1 | 38813 |
| docs/author_replication_report/tables | 17 | 38658 |
| thesis_extension/environment/legacy_R343_library/Rcpp/include/Rcpp/api/meat | 17 | 38613 |
| thesis_extension/environment/legacy_R343_library/Rcpp/include/Rcpp/stats | 23 | 38597 |
| journal_article/qa/batch4/runtime/inc/script | 2 | 38507 |
| thesis_extension/environment/legacy_R343_library/munsell/help | 5 | 38404 |
| journal_article/supplementary | 5 | 38166 |
| journal_validation/publication_review/lssp_canonical_build/source/supplementary | 5 | 38166 |
| journal_article/submission/work/named_source/supplementary | 5 | 38088 |
| journal_article/qa/batch4/runtime/inc/lib/auto/threads/shared | 1 | 37888 |
| thesis_extension/environment/legacy_R343_library/reshape2/html | 18 | 37827 |
| thesis_extension/environment/legacy_R343_library/digest/html | 7 | 37789 |
| thesis_extension/environment/legacy_R343_library/colorspace/hclwizard | 3 | 37729 |
| thesis_extension/environment/legacy_R343_library/hqreg/help | 5 | 37700 |
| journal_article/qa/batch4/runtime/inc/lib/auto/Encode/Symbol | 1 | 37376 |
| thesis_extension/environment/legacy_R343_library/mvtnorm/help | 5 | 37355 |
| thesis_extension/environment/legacy_R343_library/tibble/help | 5 | 37234 |
| journal_article/qa/batch4/runtime/inc/lib/auto/Text/BibTeX | 2 | 36864 |
| journal_article/qa/batch4/runtime/inc/lib/auto/Variable/Magic | 1 | 36864 |
| thesis/tables | 11 | 36816 |
| thesis_extension/environment/legacy_R343_library/rlang/doc | 4 | 36392 |
| journal_article/qa/batch4/runtime/inc/lib/auto/threads | 1 | 35840 |
| journal_article/qa/batch4/runtime/inc/lib/auto/Win32/Unicode | 1 | 35840 |
| journal_article/qa/batch4/runtime/inc/lib/DBD/Gofer/Transport | 5 | 35428 |
| journal_article/qa/batch4/runtime/inc/lib/XML/Parser | 1 | 35152 |
| journal_article/qa/batch4/runtime/inc/lib/unicore/lib/IdType | 11 | 35125 |
| thesis_extension/environment/legacy_R343_library/gtable/help | 5 | 35108 |
| journal_article/submission/work/review_source/supplementary | 5 | 35014 |
| journal_article/qa/batch4/runtime/inc/lib/I18N | 2 | 34669 |
| thesis_extension/environment/legacy_R343_library/magrittr/html | 14 | 34611 |
| thesis_extension/environment/legacy_R343_library/Rcpp/announce | 6 | 34563 |
| journal_article/qa/batch4/runtime/inc/lib/CPAN | 2 | 34445 |
| journal_article/qa/batch4/runtime/inc/lib/Log/Log4perl/Layout | 3 | 32857 |
| thesis_extension/environment | 9 | 32857 |
| journal_validation/publication_review/lssp_optimization/source/supplementary | 5 | 32659 |
| thesis_extension/environment/legacy_R343_library/stringr | 6 | 32614 |
| journal_article/qa/batch4/runtime/inc/lib/File/Spec | 4 | 32613 |
| journal_article/qa/batch4/runtime/inc/lib/auto/Package/Stash/XS | 1 | 32256 |
| journal_validation/stage2c/stability/saved_stability_20261029T084737Z/pilot_001 | 3 | 32000 |
| journal_validation/stage2c/stability/saved_stability_20261029T084737Z/pilot_002 | 3 | 32000 |
| journal_validation/stage2c/stability/saved_stability_20261029T084737Z/pilot_003 | 3 | 32000 |
| journal_validation/stage2c/stability/saved_stability_20261029T084737Z/pilot_004 | 3 | 32000 |
| journal_validation/stage2c/stability/saved_stability_20261029T084737Z/pilot_005 | 3 | 32000 |
| journal_validation/stage2c/stability/saved_stability_20261029T084737Z/pilot_006 | 3 | 32000 |
| journal_validation/stage2c/stability/saved_stability_20261029T084737Z/pilot_007 | 3 | 32000 |
| journal_validation/stage2c/stability/saved_stability_20261029T084737Z/pilot_008 | 3 | 32000 |
| journal_validation/stage2c/stability/saved_stability_20261029T084737Z/pilot_009 | 3 | 32000 |
| journal_validation/stage2c/stability/saved_stability_20261029T084737Z/pilot_010 | 3 | 32000 |
| journal_validation/stage2c/stability/saved_stability_20261029T084737Z/pilot_011 | 3 | 32000 |
| journal_validation/stage2c/stability/saved_stability_20261029T084737Z/pilot_012 | 3 | 32000 |
| journal_validation/stage2c/stability/saved_stability_20261029T084737Z/pilot_013 | 3 | 32000 |
| journal_validation/stage2c/stability/saved_stability_20261029T084737Z/pilot_014 | 3 | 32000 |
| journal_validation/stage2c/stability/saved_stability_20261029T084737Z/pilot_015 | 3 | 32000 |
| journal_validation/stage2c/stability/saved_stability_20261029T084737Z/pilot_016 | 3 | 32000 |
| journal_validation/stage2c/stability/saved_stability_20261029T084737Z/pilot_017 | 3 | 32000 |
| journal_validation/stage2c/stability/saved_stability_20261029T084737Z/pilot_018 | 3 | 32000 |
| journal_validation/stage2c/stability/saved_stability_20261029T084737Z/pilot_019 | 3 | 32000 |
| journal_validation/stage2c/stability/saved_stability_20261029T084737Z/pilot_020 | 3 | 32000 |
| journal_validation/stage2c/stability/saved_stability_20261029T084737Z/pilot_021 | 3 | 32000 |
| journal_validation/stage2c/stability/saved_stability_20261029T084737Z/validation_001 | 3 | 32000 |
| journal_validation/stage2c/stability/saved_stability_20261029T084737Z/validation_002 | 3 | 32000 |
| thesis_extension/environment/legacy_R343_library/reshape2/help | 5 | 31348 |
| journal_article/qa/batch4/runtime/inc/lib/DateTime/TimeZone/Local | 4 | 31081 |
| journal_article/qa/batch4/runtime/inc/lib/auto/Encode/EBCDIC | 1 | 30720 |
| journal_article/qa/batch4/runtime/inc/lib/auto/Sort/Key | 1 | 30720 |
| journal_article/qa/batch4/runtime/inc/lib/auto/Win32/API | 1 | 30720 |
| journal_article/qa/batch4/runtime/inc/lib/Params/ValidationCompiler | 2 | 30689 |
| journal_article/tables | 9 | 30443 |
| journal_article/qa/batch4/runtime/inc/lib/Locale | 1 | 30385 |
| journal_article/qa/batch4/runtime/inc/lib/DBI/SQL | 1 | 30218 |
| journal_article/qa/batch4/runtime/inc/lib/auto/autovivification | 1 | 30208 |
| journal_article/qa/batch4/runtime/inc/lib/auto/File/Glob | 1 | 30208 |
| thesis_extension/environment/legacy_R343_library/snow/html | 8 | 29878 |
| journal_article/qa/batch4/runtime/inc/lib/Hash/Util | 1 | 29790 |
| journal_article/qa/batch4/runtime/inc/lib/auto/Sys/Syslog | 2 | 29696 |
| thesis_extension/environment/legacy_R343_library/checkmate | 7 | 29128 |
| journal_article/qa/batch4/runtime/inc/lib/unicore/lib/WB | 12 | 29007 |
| journal_article/qa/batch4/runtime/inc/lib/auto/PerlIO/encoding | 1 | 28672 |
| journal_article/qa/batch4/runtime/inc/lib/auto/Time/HiRes | 1 | 28672 |
| thesis_extension/environment/legacy_R343_library/foreach/html | 10 | 28626 |
| journal_article/qa/batch4/runtime/inc/lib/Specio/Constraint/Role | 4 | 28288 |
| thesis_extension/environment/legacy_R343_library/magrittr/help | 5 | 28139 |
| thesis_extension/environment/legacy_R343_library/snow/R | 3 | 27964 |
| thesis_extension/environment/legacy_R343_library/snow/help | 5 | 27803 |
| thesis_extension/environment/legacy_R343_library/viridisLite/help/figures | 1 | 27799 |
| journal_article/qa/batch4/runtime/inc/lib/ExtUtils/MakeMaker/version | 2 | 27551 |
| thesis/figures | 3 | 27451 |
| thesis_extension/environment/legacy_R343_library/Rcpp/include/Rcpp/sugar/logical | 7 | 27373 |
| thesis_extension/environment/legacy_R343_library/tibble/help/figures | 1 | 27136 |
| thesis_extension/environment/legacy_R343_library/SparseM | 5 | 26983 |
| thesis_extension/environment/legacy_R343_library/digest/help | 5 | 26874 |
| thesis_extension/environment/legacy_R343_library/Rcpp/include/Rcpp/sugar/block | 6 | 26748 |
| thesis_extension/environment/legacy_R343_library/labeling/html | 14 | 26611 |
| journal_article/qa/batch4/runtime/inc/lib/Regexp | 1 | 26469 |
| thesis_extension/environment/legacy_R343_library/Rcpp/bib | 1 | 26418 |
| thesis_extension/environment/legacy_R343_library/magrittr/R | 3 | 26335 |
| thesis_extension/environment/legacy_R343_library/rlang | 5 | 26204 |
| journal_article/qa/batch4/runtime/inc/lib/auto/Encode/Unicode | 1 | 26112 |
| journal_article/qa/batch4/runtime/inc/lib/auto/mro | 1 | 26112 |
| journal_article/qa/batch4/runtime/inc/lib/auto/Opcode | 1 | 26112 |
| thesis_extension/environment/legacy_R343_library/Rcpp/examples/RcppInline | 6 | 25832 |
| journal_article/qa/batch4/runtime/inc/lib/unicore/lib/GCB | 7 | 25814 |
| journal_article/qa/batch4/runtime/inc/lib/unicore/lib/InSC | 24 | 25688 |
| journal_article/qa/batch4/runtime/inc/lib/auto/DateTime | 1 | 25600 |
| journal_article/qa/batch4/runtime/inc/lib/DBD/ADO | 3 | 25389 |
| journal_article/qa/batch4/runtime/inc/lib/namespace | 2 | 25269 |
| thesis_extension/environment/legacy_R343_library/Rcpp/include/Rcpp/proxy | 11 | 25244 |
| journal_article/qa/batch4/runtime/inc/lib/ExtUtils/Liblist | 1 | 25126 |
| journal_article/qa/batch4/runtime/inc/lib/auto/Digest/MD5 | 1 | 25088 |
| journal_article/qa/batch4/runtime/inc/lib/auto/IO | 1 | 25088 |
| thesis_extension/environment/legacy_R343_library/iterators/html | 12 | 24785 |
| thesis_extension/environment/legacy_R343_library/ggplot2/Meta | 8 | 24323 |
| thesis_extension/environment/legacy_R343_library/Rcpp/include/Rcpp/date_datetime | 7 | 24297 |
| journal_article/qa/batch4/runtime/inc/lib/unicore/lib/Sc | 32 | 24151 |
| journal_article/qa/batch4/runtime/inc/lib/Variable | 1 | 23850 |
| journal_article/qa/batch4/runtime/inc/lib/DBD/SQLite/VirtualTable | 2 | 23823 |
| journal_article/qa/batch4/runtime/inc/lib/DateTime/TimeZone/OlsonDB | 4 | 23709 |
| thesis_extension/environment/legacy_R343_library/viridisLite/data | 3 | 23581 |
| thesis_extension/environment/legacy_R343_library/quantreg/demo | 20 | 23570 |
| thesis_extension/environment/legacy_R343_library/lazyeval/libs/i386 | 1 | 23566 |
| journal_article/qa/batch4/runtime/inc/lib/auto/Fcntl | 1 | 23552 |
| thesis_extension/environment/legacy_R343_library/lazyeval/libs/x64 | 1 | 23552 |
| thesis/appendix | 4 | 23058 |
| journal_article/qa/batch4/runtime/inc/lib/auto/Cwd | 1 | 23040 |
| journal_article/qa/batch4/runtime/inc/lib/auto/Hash/Util/FieldHash | 1 | 23040 |
| journal_article/qa/batch4/runtime/inc/lib/auto/Params/Util | 1 | 23040 |
| thesis_extension/environment/legacy_R343_library/foreach/help | 5 | 22850 |
| thesis_extension/environment/legacy_R343_library/labeling/help | 5 | 22845 |
| thesis_extension/environment/legacy_R343_library/tibble | 6 | 22784 |
| journal_article/qa/batch4/runtime/inc/lib/IO/Compress/Base | 1 | 22771 |
| journal_article/qa/batch4/runtime/inc/lib/Role | 1 | 22724 |
| thesis_extension/environment/legacy_R343_library/lazyeval/R | 3 | 22585 |
| thesis_extension/environment/legacy_R343_library/digest | 5 | 22301 |
| thesis_extension/environment/legacy_R343_library/R6/html | 5 | 22163 |
| journal_article/qa/batch4/runtime/inc/lib/auto/Math/BigInt/FastCalc | 1 | 22016 |
| journal_article/qa/batch4/runtime/inc/lib/auto/MIME/Base64 | 1 | 22016 |
| thesis_extension/environment/legacy_R343_library/foreach/R | 3 | 21999 |
| journal_article/qa/batch4/runtime/inc/lib/unicore/lib/Bc | 13 | 21837 |
| journal_article/qa/batch4/runtime/inc/lib/Params/Validate | 3 | 21807 |
| thesis_extension/environment/legacy_R343_library/Formula/html | 4 | 21675 |
| journal_article/submission | 3 | 21370 |
| journal_article/qa/batch4/runtime/inc/lib/auto/PerlIO/scalar | 1 | 20992 |
| journal_article/qa/batch4/runtime/inc/lib/auto/PerlIO/utf8_strict | 1 | 20992 |
| thesis_extension/environment/legacy_R343_library/iterators/R | 3 | 20903 |
| journal_validation/stage2g/end_to_end_certification/results/primary_exact_reaudit | 1 | 20736 |
| journal_article/qa/batch4/runtime/inc/lib/Try | 1 | 20730 |
| journal_article/qa/batch4/runtime/inc/lib/File/Find | 1 | 20605 |
| journal_article/qa/batch4/runtime/inc/lib/threads | 1 | 20552 |
| journal_article/qa/batch4/runtime/inc/lib/Encode/MIME | 2 | 20484 |
| journal_article/qa/batch4/runtime/inc/lib/Biber/Entry | 2 | 20448 |
| thesis_extension/environment/legacy_R343_library/backports/html | 17 | 20430 |
| thesis_extension/environment/legacy_R343_library/Rcpp/include/Rcpp/stats/dpq | 2 | 20363 |
| thesis_extension/environment/legacy_R343_library/iterators/help | 5 | 20268 |
| thesis_extension/environment/legacy_R343_library/scales | 6 | 20200 |
| thesis_extension/environment/legacy_R343_library/backports/help | 5 | 20079 |
| journal_article/qa/batch4/runtime/inc/lib/Devel | 2 | 19998 |
| journal_validation/stage2c/validation_protocol/reassessment_20261029T083111Z/ordinary_references | 25 | 19972 |
| journal_article/qa/batch4/runtime/inc/lib/Log/Log4perl/JavaMap | 7 | 19962 |
| journal_article/qa/batch4/runtime/inc/lib/DateTime/Format/Builder/Parser | 5 | 19805 |
| journal_article/qa/batch4/runtime/inc/lib/List/MoreUtils | 2 | 19664 |
| journal_article/figures | 1 | 19560 |
| journal_article/submission/work/named_source/figures | 1 | 19560 |
| journal_article/submission/work/review_source/figures | 1 | 19560 |
| journal_validation/publication_review/lssp_canonical_build/source/figures | 1 | 19560 |
| journal_validation/publication_review/lssp_optimization/source/figures | 1 | 19560 |
| journal_article/qa/batch4/runtime/inc/lib/auto/I18N/Langinfo | 1 | 19456 |
| journal_article/qa/batch4/runtime/inc/lib/Log/Log4perl/Filter | 5 | 19381 |
| journal_article/qa/batch4/runtime/inc/lib/Module/Load | 1 | 19315 |
| journal_article/qa/batch4/runtime/inc/lib/Test2/Event | 9 | 19081 |
| thesis_extension/environment/legacy_R343_library/mvtnorm/R | 3 | 19062 |
| journal_article/qa/batch4/runtime/inc/lib/auto/Clone | 2 | 19031 |
| journal_article/qa/batch4/runtime/inc/lib/DateTime/Format/Builder | 1 | 18998 |
| thesis_extension/environment/legacy_R343_library/stringr/data | 3 | 18490 |
| journal_article/qa/batch4/runtime/inc/lib/auto/attributes | 1 | 18432 |
| thesis_extension/environment/legacy_R343_library/stringr/R | 3 | 18314 |
| thesis_extension/environment/legacy_R343_library/Rcpp/include/Rcpp/sugar/matrix | 9 | 18082 |
| journal_article/qa/batch4/runtime/inc/lib/Specio/Library | 3 | 17960 |
| thesis_extension/environment/legacy_R343_library/colorspace | 7 | 17920 |
| journal_article/qa/batch4/runtime/inc/lib/Test2/Util | 3 | 17851 |
| thesis_extension/environment/legacy_R343_library/Rcpp/examples/ConvolveBenchmarks | 21 | 17774 |
| thesis_extension/environment/legacy_R343_library/gtable/R | 3 | 17567 |
| journal_article/qa/batch4/runtime/inc/lib/Crypt | 1 | 17524 |
| journal_article/qa/batch4/runtime/inc/lib/auto/Sub/Identify | 1 | 17408 |
| journal_article/qa/batch4/runtime/inc/lib/Net/HTTP | 1 | 17333 |
| journal_article/qa/batch4/runtime/inc/lib/unicore/lib/Dt | 14 | 17194 |
| journal_article/qa/batch4/runtime/inc/lib/Exception | 1 | 17097 |
| journal_article/qa/batch4/runtime/inc/lib/unicore/lib/InPC | 13 | 17094 |
| thesis_extension/environment/legacy_R343_library/R6/help | 5 | 17049 |
| journal_article/qa/batch4/runtime/inc/lib/Class/Method | 1 | 16969 |
| journal_article/qa/batch4/runtime/inc/lib/Package/Stash | 2 | 16934 |
| thesis_extension/environment/legacy_R343_library/backports/libs/x64 | 1 | 16896 |
| journal_article/qa/batch4/runtime/inc/lib/Digest | 4 | 16751 |
| journal_article/qa/batch4/runtime/inc/lib/Tie | 4 | 16567 |
| thesis_extension/src | 6 | 16470 |
| thesis_extension/environment/legacy_R343_library/Formula/help | 5 | 16405 |
| thesis_extension/environment/legacy_R343_library/backports/libs/i386 | 1 | 16398 |
| journal_article/qa/batch4/runtime/inc/lib/Exception/Class | 1 | 16296 |
| thesis_extension/environment/legacy_R343_library/Rcpp/unitTests/bin/amd64 | 1 | 16266 |
| journal_article/qa/batch4/runtime/inc/lib/HTTP/Request | 1 | 16194 |
| thesis_extension/environment/legacy_R343_library/rlang/Meta | 7 | 16176 |
| thesis_extension/environment/legacy_R343_library/Rcpp/unitTests/bin/i386 | 1 | 16142 |
| journal_article/qa/batch4/runtime/inc/lib/DBD/mysql | 1 | 16114 |
| journal_article/qa/batch4/runtime/inc/lib/auto/File/DosGlob | 1 | 15872 |
| journal_article/qa/batch4/runtime/inc/lib/auto/Sys/Hostname | 1 | 15872 |
| thesis_extension/environment/legacy_R343_library/mvtnorm | 5 | 15848 |
| thesis_extension/environment/legacy_R343_library/Rcpp/include/Rcpp/exceptions/cpp98 | 1 | 15669 |
| thesis_extension/environment/legacy_R343_library/plyr | 6 | 15450 |
| journal_article/qa/batch4/runtime/inc/lib/DBD/Oracle | 2 | 15380 |
| thesis_extension/environment/legacy_R343_library/dichromat/html | 5 | 15133 |
| journal_article/qa/batch4/runtime/inc/lib/Log/Log4perl/Util | 2 | 14654 |
| journal_validation/publication_review/lssp_optimization/source | 4 | 14351 |
| journal_article/qa/batch4/runtime/inc/lib/List/SomeUtils | 2 | 14290 |
| journal_article/qa/batch4/runtime/inc/lib/unicore/lib/Jt | 6 | 14078 |
| thesis_extension/environment/legacy_R343_library/Rcpp/examples/FastLM | 6 | 13824 |
| journal_article/qa/batch4/runtime/inc/lib/Test/Builder/IO | 1 | 13640 |
| thesis_extension/environment/legacy_R343_library/RColorBrewer/R | 3 | 13578 |
| journal_article/qa/batch4/runtime/inc/lib/Test2/IPC/Driver | 1 | 13559 |
| journal_article/submission/work/named_source | 3 | 13145 |
| journal_validation/publication_review/lssp_canonical_build/source | 3 | 13145 |
| journal_article/qa/batch4/runtime/inc/lib/Encode/compat | 3 | 12995 |
| journal_article/qa/batch4/runtime/inc/lib/DBD/CSV | 2 | 12869 |
| journal_article/qa/batch4/runtime/inc/lib/Digest/Perl | 1 | 12762 |
| thesis_extension/environment/legacy_R343_library/Rcpp/examples/RcppGibbs | 2 | 12678 |
| thesis_extension/environment/legacy_R343_library/digest/R | 3 | 12637 |
| docs | 1 | 12621 |
| thesis_extension/environment/legacy_R343_library/foreach/unitTests | 11 | 12497 |
| thesis_extension/environment/legacy_R343_library/stringi/Meta | 6 | 12368 |
| journal_article/submission/work/review_source | 3 | 12293 |
| thesis_extension/environment/legacy_R343_library/reshape2/R | 3 | 12286 |
| journal_article/qa/batch4/runtime/inc/lib/IPC/Run3 | 3 | 12269 |
| thesis_extension/environment/legacy_R343_library/Formula/R | 3 | 12242 |
| thesis_extension/environment/legacy_R343_library/checkmate/Meta | 7 | 12232 |
| thesis_extension/environment/legacy_R343_library/labeling/R | 3 | 12212 |
| thesis_extension/environment/legacy_R343_library/Rcpp/include/Rcpp/hash | 3 | 12099 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2 | 200 | 11955 |
| journal_article/qa/batch4/runtime/inc/lib/unicore/lib/Ccc | 11 | 11893 |
| journal_article/qa/batch4/runtime/inc/lib/unicore/lib/GrBase | 1 | 11798 |
| journal_article/qa/batch4/runtime/inc/lib/Lingua | 1 | 11691 |
| thesis_extension/environment/legacy_R343_library/hqreg/R | 3 | 11675 |
| journal_article/qa/batch4/runtime/inc/lib/Log/Dispatch/Email | 4 | 11507 |
| journal_article/qa/batch4/runtime/inc/lib/DateTime/TimeZone/Indian | 8 | 11350 |
| journal_article/qa/batch4/runtime/inc/lib/unicore/lib/NFKDQC | 2 | 11241 |
| thesis_extension/environment/legacy_R343_library/backports/R | 3 | 11239 |
| journal_article/qa/batch4/runtime/inc/lib/DBD/Gofer/Policy | 4 | 11227 |
| thesis_extension/environment/legacy_R343_library/quantreg/Meta | 9 | 11202 |
| thesis_extension/environment/legacy_R343_library/dichromat/help | 5 | 11063 |
| journal_article/qa/batch4/runtime/inc/lib/MRO | 1 | 10974 |
| journal_article/qa/batch4/runtime/inc/lib/unicore/lib/CWKCF | 1 | 10844 |
| thesis_extension/environment/legacy_R343_library/iterators/examples | 11 | 10769 |
| journal_article/qa/batch4/runtime/inc/lib/unicore/lib/Jg | 18 | 10759 |
| journal_article/qa/batch4/runtime/inc/lib/Parse/CPAN | 1 | 10743 |
| thesis_extension/environment/legacy_R343_library/R6/R | 3 | 10674 |
| thesis_extension/environment/legacy_R343_library/lazyeval | 5 | 10522 |
| thesis_extension/environment/legacy_R343_library/RColorBrewer/html | 3 | 10506 |
| journal_article/qa/batch4/runtime/inc/lib/LWP/Authen | 3 | 10450 |
| thesis_extension/environment/legacy_R343_library/reshape2/data | 3 | 10361 |
| journal_article/qa/batch4/runtime/inc/lib/unicore/lib/XIDC | 1 | 10353 |
| thesis_extension/validation | 5 | 10281 |
| journal_article/qa/batch4/runtime/inc/lib/unicore/lib/IDC | 1 | 10255 |
| journal_article/qa/batch4/runtime/inc/lib/Scalar | 1 | 10189 |
| journal_article/qa/batch4/runtime/inc/lib/Algorithm | 1 | 10096 |
| journal_article/qa/batch4/runtime/inc/lib/unicore/lib/IdStatus | 2 | 10063 |
| thesis_extension/environment/legacy_R343_library/Rcpp/skeleton | 11 | 10007 |
| journal_article/qa/batch4/runtime/inc/lib/unicore/lib/Ea | 5 | 9994 |
| journal_article/qa/batch4/runtime/inc/lib/XML/Parser/Style | 5 | 9956 |
| journal_article/qa/batch4/runtime/inc/lib/Eval | 1 | 9913 |
| journal_validation/publication_review/lssp_canonical_build/source/tables | 8 | 9868 |
| journal_article/submission/work/named_source/tables | 8 | 9841 |
| journal_article/submission/work/review_source/tables | 8 | 9841 |
| journal_validation/publication_review/lssp_optimization/source/tables | 8 | 9815 |
| journal_article/qa/batch4/runtime/inc/lib/Locale/Maketext | 1 | 9792 |
| journal_article/qa/batch4/runtime/inc/lib/unicore/lib/Alpha | 1 | 9765 |
| journal_article/qa/batch4/runtime/inc/lib/Dist | 1 | 9715 |
| thesis_extension/environment/legacy_R343_library/Rcpp/include/Rcpp/sugar | 5 | 9604 |
| thesis_extension/environment/legacy_R343_library/plyr/Meta | 7 | 9505 |
| journal_article/qa/batch4/runtime/inc/lib/Encode/JP | 2 | 9404 |
| thesis_extension/environment/legacy_R343_library/viridisLite/html | 4 | 9114 |
| journal_article/qa/batch4/runtime/inc/lib/unicore/lib/XIDS | 1 | 8915 |
| journal_article/qa/batch4/runtime/inc/lib/Sort | 1 | 8834 |
| journal_article/qa/batch4/runtime/inc/lib/unicore/lib/IDS | 1 | 8817 |
| thesis_extension/environment/legacy_R343_library/scales/Meta | 6 | 8799 |
| thesis_extension/environment/legacy_R343_library/snow | 16 | 8756 |
| journal_article/qa/batch4/runtime/inc/lib/Package | 1 | 8740 |
| thesis_extension/environment/legacy_R343_library/colorspace/hclwizard/html | 4 | 8720 |
| thesis_extension/environment/legacy_R343_library/dichromat/data | 1 | 8596 |
| journal_article/qa/batch4/runtime/inc/lib/Authen/SASL | 3 | 8592 |
| journal_article/qa/batch4/runtime/inc/lib/unicore/lib/Lower | 1 | 8484 |
| thesis_extension/environment/legacy_R343_library/doSNOW/R | 3 | 8471 |
| thesis_extension/audit | 3 | 8463 |
| thesis_extension/environment/legacy_R343_library/Rcpp/examples/SugarPerformance | 3 | 8456 |
| thesis_extension/environment/legacy_R343_library/Rcpp/include/Rcpp/platform | 2 | 8449 |
| journal_article/qa/batch4/runtime/inc/lib/unicore/lib/Upper | 1 | 8386 |
| journal_article/qa/batch4/runtime/inc/lib/Net/FTP | 5 | 8169 |
| journal_article/qa/batch4/runtime/inc/lib/unicore/lib/NFKCQC | 2 | 8165 |
| journal_article/qa/batch4/runtime/inc/lib/URI/file | 7 | 8146 |
| thesis_extension/environment/legacy_R343_library/Rcpp/unitTests/testRcppModule/src | 6 | 8137 |
| thesis_extension/environment/legacy_R343_library/Rcpp/include/Rcpp/sugar/functions/strings | 3 | 8133 |
| journal_article/qa/batch4/runtime/inc/lib/unicore/lib/CWU | 1 | 7946 |
| journal_article/qa/batch4/runtime/inc/lib/unicore/lib/CWT | 1 | 7932 |
| thesis_extension/environment/legacy_R343_library/glmnet | 5 | 7922 |
| thesis_extension/environment/legacy_R343_library/iterators/unitTests | 7 | 7913 |
| journal_article/qa/batch4/runtime/inc/lib/unicore/lib/CWCF | 1 | 7900 |
| journal_article/qa/batch4/runtime/inc/lib/XML/DOM | 3 | 7898 |
| thesis_extension/environment/legacy_R343_library/Formula | 6 | 7815 |
| journal_article/qa/batch4/runtime/inc/lib/Log/Dispatch/FileRotate | 2 | 7807 |
| journal_article/qa/batch4/runtime/inc/lib/unicore/lib/CWL | 1 | 7748 |
| thesis_extension/environment/legacy_R343_library/R6 | 6 | 7687 |
| thesis_extension/environment/legacy_R343_library/SparseM/Meta | 9 | 7570 |
| journal_validation/stage2g/full_path_validation/results/pilot_003_truth | 1 | 7553 |
| journal_validation/stage2g/full_path_validation/results/pilot_005_truth | 1 | 7552 |
| journal_validation/stage2g/full_path_validation/results/pilot_003_minus | 1 | 7547 |
| journal_validation/stage2g/full_path_validation/results/pilot_006_truth | 1 | 7547 |
| journal_validation/stage2g/full_path_validation/results/pilot_005_plus | 1 | 7542 |
| journal_validation/stage2g/full_path_validation/results/pilot_002_minus | 1 | 7535 |
| journal_validation/stage2g/full_path_validation/results/pilot_006_plus | 1 | 7533 |
| journal_validation/stage2g/full_path_validation/results/pilot_005_minus | 1 | 7531 |
| journal_validation/stage2g/full_path_validation/results/pilot_014_truth | 1 | 7527 |
| journal_validation/stage2g/full_path_validation/results/pilot_002_plus | 1 | 7526 |
| journal_validation/stage2g/full_path_validation/results/pilot_004_plus | 1 | 7522 |
| journal_validation/stage2g/full_path_validation/results/pilot_001_plus | 1 | 7521 |
| journal_validation/stage2g/full_path_validation/results/pilot_006_minus | 1 | 7519 |
| journal_validation/stage2g/full_path_validation/results/pilot_003_plus | 1 | 7518 |
| journal_validation/stage2g/full_path_validation/results/pilot_007_plus | 1 | 7518 |
| journal_validation/stage2g/full_path_validation/results/pilot_002_truth | 1 | 7516 |
| journal_validation/stage2g/full_path_validation/results/pilot_007_truth | 1 | 7516 |
| journal_validation/stage2g/full_path_validation/results/pilot_004_truth | 1 | 7512 |
| journal_validation/stage2g/full_path_validation/results/pilot_014_plus | 1 | 7512 |
| journal_validation/stage2g/full_path_validation/results/pilot_004_minus | 1 | 7511 |
| journal_validation/stage2g/full_path_validation/results/pilot_001_minus | 1 | 7500 |
| journal_validation/stage2g/full_path_validation/results/pilot_001_truth | 1 | 7499 |
| journal_validation/stage2g/full_path_validation/results/pilot_014_minus | 1 | 7489 |
| journal_validation/stage2g/full_path_validation/results/pilot_007_minus | 1 | 7485 |
| thesis_extension/validation/R343_final_audit | 7 | 7371 |
| journal_article/qa/batch4/runtime/inc/lib/IO/Compress/Zlib | 2 | 7369 |
| journal_article/qa/batch4/runtime/inc/lib/Test/Builder | 3 | 7282 |
| thesis_extension/environment/legacy_R343_library/munsell | 6 | 7191 |
| thesis_extension/environment/legacy_R343_library/Rcpp/examples/OpenMP | 4 | 7123 |
| thesis_extension/environment/legacy_R343_library/hdm | 4 | 7118 |
| thesis_extension/environment/legacy_R343_library/Rcpp/include/Rcpp/sugar/functions/mapply | 2 | 7112 |
| thesis_extension/environment/legacy_R343_library/MatrixModels | 4 | 7057 |
| journal_article/qa/batch4/runtime/inc/lib/Data/Dump | 2 | 7008 |
| journal_article/qa/batch4/runtime/inc/lib/unicore/lib/NFDQC | 2 | 6761 |
| journal_article/qa/batch4/runtime/inc/lib/unicore/lib/Nt | 3 | 6735 |
| journal_article/qa/batch4/runtime/inc/lib/I18N/LangTags | 1 | 6649 |
| thesis_extension/environment/legacy_R343_library/viridisLite/help | 5 | 6649 |
| thesis_extension/environment/legacy_R343_library/Rcpp/include | 2 | 6636 |
| thesis_extension/environment/legacy_R343_library/Rcpp/Meta | 7 | 6579 |
| journal_article/qa/batch4/runtime/inc/lib/Exporter | 1 | 6561 |
| thesis_extension/environment/legacy_R343_library/hdm/Meta | 8 | 6521 |
| journal_article/qa/batch4/runtime/inc/lib/Win32API/File | 1 | 6272 |
| thesis_extension/environment/legacy_R343_library/RColorBrewer/help | 5 | 6213 |
| journal_article/qa/batch4/runtime/inc/lib/Devel/StackTrace | 1 | 6133 |
| journal_article/qa/batch4/runtime/inc/lib/DateTime/Calendar | 1 | 6096 |
| journal_article/qa/batch4/runtime/inc/lib/Encode/CN | 1 | 6084 |
| journal_article/qa/batch4/runtime/inc/lib/Test2/EventFacet | 1 | 6073 |
| thesis_extension/environment/legacy_R343_library/Rcpp/examples/Misc | 5 | 5959 |
| thesis_extension/environment/legacy_R343_library/gtable | 5 | 5872 |
| journal_article/qa/batch4/runtime/inc/lib/unicore/lib/CI | 1 | 5849 |
| journal_article/qa/batch4/runtime/inc/lib/IO/Compress/Adapter | 2 | 5740 |
| journal_article/qa/batch4/runtime/inc/lib/Biber/Date | 1 | 5575 |
| thesis_extension/environment/legacy_R343_library/Rcpp/include/Rcpp/api/bones | 4 | 5554 |
| journal_article/qa/batch4/runtime/inc/lib/unicore/lib/Vo | 4 | 5541 |
| thesis_extension/environment/legacy_R343_library/Rcpp/include/doxygen | 1 | 5385 |
| thesis_extension/environment/legacy_R343_library/stringr/Meta | 8 | 5353 |
| journal_article/qa/batch4/runtime/inc/lib/IO/Uncompress/Adapter | 2 | 5320 |
| journal_article/qa/batch4/runtime/inc/lib/B/Hooks/EndOfScope | 2 | 5314 |
| . | 3 | 5261 |
| journal_article/qa/batch4/runtime/inc/lib/Sort/Key | 1 | 5255 |
| thesis_extension/environment/legacy_R343_library/colorspace/hclwizard/www/images | 44 | 5236 |
| thesis_extension/environment/legacy_R343_library/reshape2 | 6 | 5148 |
| thesis_extension/environment/legacy_R343_library/colorspace/Meta | 8 | 5110 |
| journal_article/qa/batch4/runtime/inc/lib/HTTP/Headers | 1 | 5071 |
| journal_article/qa/batch4/runtime/inc/lib/DBI/Gofer/Transport | 1 | 5044 |
| journal_article/qa/batch4/runtime/inc/lib/unicore/lib/GrExt | 1 | 5025 |
| thesis_extension/environment/legacy_R343_library/lazyeval/Meta | 7 | 4982 |
| thesis_extension/environment/legacy_R343_library/Rcpp/include/Rcpp/sugar/tools | 1 | 4955 |
| thesis_extension/environment/legacy_R343_library/Rcpp/unitTests/testRcppClass/src | 6 | 4911 |
| thesis_extension/environment/legacy_R343_library/glmnet/Meta | 8 | 4904 |
| thesis_extension/environment/legacy_R343_library/backports | 5 | 4879 |
| thesis_extension/environment/legacy_R343_library/Rcpp/include/Rcpp/protection | 4 | 4851 |
| thesis_extension/environment/legacy_R343_library/tibble/Meta | 7 | 4819 |
| journal_article/qa/batch4/runtime/inc/lib/Sub/Exporter | 1 | 4812 |
| thesis_extension/environment/legacy_R343_library/MatrixModels/Meta | 6 | 4637 |
| thesis_extension/environment/legacy_R343_library/magrittr | 5 | 4426 |
| thesis_extension/environment/legacy_R343_library/Rcpp/include/Rcpp/Benchmark | 1 | 4412 |
| journal_article/qa/batch4/runtime/inc/lib/DBI/Gofer/Serializer | 3 | 4253 |
| journal_article/qa/batch4/runtime/inc/lib/B/Hooks/EndOfScope/PP | 2 | 4231 |
| thesis_extension/environment/legacy_R343_library/foreach | 4 | 4171 |
| journal_article/qa/batch4/runtime/inc/lib/B/Hooks | 1 | 4164 |
| journal_article/qa/batch4/runtime/inc/lib/Test2/Hub | 2 | 4073 |
| journal_article/qa/batch4/runtime/inc/lib/version | 1 | 4072 |
| thesis_extension/environment/legacy_R343_library/viridisLite/R | 3 | 4070 |
| journal_article/qa/batch4/runtime/inc/lib/Class/Data | 1 | 4067 |
| thesis_extension/environment/legacy_R343_library/RColorBrewer | 5 | 4002 |
| thesis_extension/environment/legacy_R343_library/Rcpp/examples/performance | 2 | 3994 |
| journal_article/qa/batch4/runtime/inc/lib/IO/Compress/Gzip | 1 | 3903 |
| journal_article/qa/batch4/runtime/inc/lib/Encode/Unicode | 1 | 3875 |
| thesis_extension/environment/legacy_R343_library/snow/Meta | 6 | 3873 |
| thesis_extension/environment/legacy_R343_library/doSNOW/html | 3 | 3868 |
| journal_article/qa/batch4/runtime/inc/lib/PerlIO | 3 | 3834 |
| journal_article/qa/batch4/runtime/inc/lib/Win32API/Registry | 1 | 3737 |
| thesis_extension/environment/legacy_R343_library/hqreg | 4 | 3686 |
| thesis_extension/environment/legacy_R343_library/munsell/Meta | 6 | 3637 |
| thesis_extension/environment/legacy_R343_library/magrittr/Meta | 7 | 3596 |
| thesis_extension/environment/legacy_R343_library/reshape2/Meta | 7 | 3543 |
| thesis_extension/environment/legacy_R343_library/digest/Meta | 7 | 3522 |
| thesis_extension/environment/legacy_R343_library/gtable/Meta | 6 | 3511 |
| journal_article/qa/batch4/runtime/inc/lib/unicore/lib/Bpt | 3 | 3507 |
| thesis_extension/environment/legacy_R343_library/foreach/Meta | 8 | 3503 |
| journal_article/qa/batch4/runtime/inc/lib/HTTP/Cookies | 1 | 3371 |
| thesis_extension/environment/legacy_R343_library/labeling | 5 | 3265 |
| thesis_extension/environment/legacy_R343_library/viridisLite | 5 | 3244 |
| journal_article/qa/batch4/runtime/inc/lib/MIME/Charset | 1 | 3243 |
| thesis_extension/environment/legacy_R343_library/iterators/Meta | 7 | 3236 |
| thesis_extension/environment/legacy_R343_library/SparseM/demo | 6 | 3225 |
| journal_article/qa/batch4/runtime/inc/lib/Encode/MIME/Header | 1 | 3200 |
| thesis_extension/environment/legacy_R343_library/digest/include | 1 | 3165 |
| journal_article/qa/batch4/runtime/inc/lib/Specio/Role | 1 | 3119 |
| journal_article/qa/batch4/runtime/config/fontconfig/config | 3 | 3105 |
| thesis_extension/environment/legacy_R343_library/colorspace/hclwizard/www | 1 | 3103 |
| journal_article/qa/batch4/runtime/inc/lib/XML/SAX | 1 | 3033 |
| thesis_extension/environment/legacy_R343_library/Rcpp/examples/Attributes | 4 | 2976 |
| journal_article/qa/batch4/runtime/inc/lib/ExtUtils/MakeMaker | 2 | 2961 |
| thesis_extension/environment/legacy_R343_library/backports/Meta | 6 | 2924 |
| journal_article/qa/batch4/runtime/inc/lib/unicore/lib/NFCQC | 2 | 2904 |
| journal_article/qa/batch4/runtime/inc/lib/namespace/clean | 1 | 2880 |
| thesis_extension/environment/legacy_R343_library/mvtnorm/Meta | 7 | 2861 |
| thesis_extension/environment/legacy_R343_library/Rcpp/include/Rcpp/sugar/nona | 1 | 2851 |
| journal_article/qa/batch4/runtime/inc/lib/unicore/lib/Dia | 1 | 2773 |
| thesis_extension/environment/legacy_R343_library/labeling/Meta | 6 | 2744 |
| journal_article/qa/batch4/runtime/inc/lib/Business/ISMN | 1 | 2739 |
| journal_article/qa/batch4/runtime/inc/lib/Authen | 1 | 2738 |
| thesis_extension/environment/legacy_R343_library/hqreg/Meta | 6 | 2708 |
| thesis_extension/environment/legacy_R343_library/Rcpp/include/Rcpp/iostream | 1 | 2703 |
| journal_article/qa/batch4/runtime/inc/lib/Log/Dispatch/File | 1 | 2654 |
| thesis_extension/environment/legacy_R343_library/Formula/Meta | 7 | 2653 |
| thesis_extension/environment/legacy_R343_library/dichromat | 4 | 2652 |
| journal_article/qa/batch4/runtime/inc/lib/unicore/lib/Emoji | 1 | 2620 |
| thesis_extension/environment/legacy_R343_library/R6/Meta | 7 | 2561 |
| journal_article/qa/batch4/runtime/inc/lib/Log/Log4perl/Layout/PatternLayout | 1 | 2559 |
| journal_article/qa/batch4/runtime/inc/lib/Encode/JIS2K | 1 | 2540 |
| thesis_extension/environment/legacy_R343_library/Rcpp/include/Rcpp/storage | 3 | 2509 |
| thesis_extension/environment/legacy_R343_library/Rcpp/examples/functionCallback | 2 | 2495 |
| thesis_extension/environment/legacy_R343_library/doSNOW/examples | 1 | 2493 |
| thesis_extension/environment/legacy_R343_library/viridisLite/Meta | 7 | 2478 |
| thesis_extension/environment/legacy_R343_library/Rcpp/include/Rcpp/exceptions/cpp11 | 1 | 2439 |
| journal_article/qa/batch4/runtime/inc/lib/Unicode/LineBreak | 1 | 2411 |
| journal_article/qa/batch4/runtime/inc/lib/Number | 1 | 2398 |
| journal_article/qa/batch4/runtime/inc/lib/unicore/lib/Math | 1 | 2387 |
| journal_article/qa/batch4/runtime/inc/lib/unicore/lib/Cased | 1 | 2349 |
| journal_article/qa/batch4/runtime/inc/lib/Class/C3 | 1 | 2238 |
| thesis_extension/environment/legacy_R343_library/dichromat/Meta | 7 | 2236 |
| thesis_extension/environment/legacy_R343_library/Rcpp/include/Rcpp/r | 1 | 2202 |
| thesis_extension/environment/legacy_R343_library/doSNOW | 4 | 2182 |
| thesis_extension/environment/legacy_R343_library/doSNOW/Meta | 6 | 2107 |
| journal_article/qa/batch4/runtime/inc/lib/DateTime/Format/Strptime | 1 | 2104 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_018/P00 | 1 | 2101 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_014/P10 | 1 | 2095 |
| thesis_extension | 1 | 2094 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_011/P00 | 1 | 2087 |
| thesis_extension/environment/legacy_R343_library/iterators | 3 | 2086 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/validation_001/P11 | 1 | 2079 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_002/P11 | 1 | 2078 |
| thesis_extension/environment/legacy_R343_library/mvtnorm/include | 2 | 2042 |
| journal_article/qa/batch4/runtime/inc/lib/unicore/lib/BidiM | 1 | 1985 |
| journal_article/qa/batch4/runtime/inc/lib/unicore/lib/CWCM | 1 | 1985 |
| journal_article/qa/batch4/runtime/inc/lib/Encode/KR | 1 | 1977 |
| journal_article/qa/batch4/runtime/inc/lib/overload | 1 | 1951 |
| thesis_extension/environment/legacy_R343_library/RColorBrewer/Meta | 6 | 1943 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_020/P10 | 1 | 1901 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/validation_001/P00 | 1 | 1900 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_016/P00 | 1 | 1899 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_019/P10 | 1 | 1899 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_002/P00 | 1 | 1898 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_010/P00 | 1 | 1898 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_012/P10 | 1 | 1898 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/validation_001/P10 | 1 | 1898 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_006/P11 | 1 | 1897 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_019/P00 | 1 | 1897 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/validation_002/P10 | 1 | 1897 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_009/P11 | 1 | 1896 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_016/P10 | 1 | 1896 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_017/P10 | 1 | 1896 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_011/P11 | 1 | 1895 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_014/P11 | 1 | 1895 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/validation_001/P01 | 1 | 1895 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_007/P10 | 1 | 1894 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_008/P00 | 1 | 1894 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_001/P10 | 1 | 1893 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_005/P10 | 1 | 1893 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_015/P01 | 1 | 1893 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_018/P11 | 1 | 1893 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_004/P00 | 1 | 1892 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_010/P10 | 1 | 1892 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_012/P00 | 1 | 1892 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_015/P00 | 1 | 1892 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_017/P00 | 1 | 1892 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_003/P10 | 1 | 1891 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_003/P11 | 1 | 1891 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_006/P00 | 1 | 1891 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_014/P00 | 1 | 1891 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_016/P11 | 1 | 1891 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_020/P00 | 1 | 1891 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_002/P10 | 1 | 1890 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_003/P00 | 1 | 1890 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_004/P10 | 1 | 1890 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_005/P11 | 1 | 1890 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_009/P10 | 1 | 1890 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_012/P01 | 1 | 1890 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_013/P00 | 1 | 1890 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_015/P10 | 1 | 1890 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/validation_002/P11 | 1 | 1890 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_005/P01 | 1 | 1889 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_007/P00 | 1 | 1889 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_009/P00 | 1 | 1889 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_009/P01 | 1 | 1889 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_011/P01 | 1 | 1889 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_012/P11 | 1 | 1889 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/validation_002/P01 | 1 | 1889 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_006/P10 | 1 | 1888 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_014/P01 | 1 | 1888 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_002/P01 | 1 | 1887 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_007/P11 | 1 | 1887 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_015/P11 | 1 | 1887 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/validation_002/P00 | 1 | 1887 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_001/P00 | 1 | 1886 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_001/P11 | 1 | 1886 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_008/P01 | 1 | 1886 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_018/P01 | 1 | 1886 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_019/P01 | 1 | 1886 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_003/P01 | 1 | 1885 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_004/P11 | 1 | 1885 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_007/P01 | 1 | 1885 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_011/P10 | 1 | 1885 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_004/P01 | 1 | 1884 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_005/P00 | 1 | 1884 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_008/P11 | 1 | 1884 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_013/P10 | 1 | 1884 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_017/P11 | 1 | 1884 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_018/P10 | 1 | 1884 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_019/P11 | 1 | 1884 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_001/P01 | 1 | 1883 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_010/P01 | 1 | 1883 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_013/P01 | 1 | 1883 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_006/P01 | 1 | 1882 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_008/P10 | 1 | 1882 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_013/P11 | 1 | 1882 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_010/P11 | 1 | 1881 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_016/P01 | 1 | 1881 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_020/P11 | 1 | 1880 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_020/P01 | 1 | 1877 |
| journal_validation/stage2c/certification/saved_inputs_20261029T080821Z/pilot_017/P01 | 1 | 1868 |
| thesis_extension/environment/legacy_R343_library/doSNOW/unitTests | 1 | 1868 |
| journal_article/qa/batch4/runtime/inc/lib/unicore/lib/Term | 1 | 1867 |
| thesis_extension/environment/legacy_R343_library/doSNOW/help | 5 | 1837 |
| journal_article/qa/batch4/runtime/inc/lib/unicore/lib/EPres | 1 | 1695 |
| thesis_extension/environment/legacy_R343_library/Rcpp/unitTests/testRcppClass/R | 2 | 1670 |
| journal_article/qa/batch4/runtime/inc/lib/DBI/Util | 1 | 1666 |
| thesis_extension/environment/legacy_R343_library/Rcpp/discovery | 1 | 1656 |
| journal_article/qa/batch4/runtime/inc/lib/unicore/lib/ExtPict | 1 | 1606 |
| journal_article/qa/batch4/runtime/inc/lib/Class/XSAccessor | 1 | 1593 |
| thesis_extension/environment/legacy_R343_library/Rcpp/include/Rcpp/api/meat/module | 1 | 1578 |
| journal_article/qa/batch4/runtime/inc/lib/Crypt/SSLeay | 3 | 1522 |
| journal_article/qa/batch4/runtime/inc/lib/unicore/lib/STerm | 1 | 1511 |
| journal_article/qa/batch4/runtime/inc/lib/Mozilla | 1 | 1474 |
| journal_article/qa/batch4/runtime/inc/lib/unicore/lib/CompEx | 1 | 1423 |
| journal_article/qa/batch4/runtime/inc/lib/Encode/TW/Unisys | 2 | 1402 |
| thesis_extension/final | 1 | 1354 |
| journal_article/qa/batch4/runtime/inc/lib/unicore/lib/Blk | 1 | 1314 |
| journal_article/qa/batch4/runtime/inc/lib/Math/BigFloat | 1 | 1269 |
| thesis_extension/environment/legacy_R343_library/Rcpp/unitTests/testRcppClass/man | 3 | 1263 |
| journal_article/qa/batch4/runtime/inc/lib/Date | 1 | 1247 |
| thesis_extension/environment/legacy_R343_library/Rcpp/unitTests/testRcppModule/man | 3 | 1203 |
| journal_article/qa/batch4/runtime/inc/lib/DBI/Const | 1 | 1195 |
| journal_article/qa/batch4/runtime/inc/lib/unicore/lib/EBase | 1 | 1104 |
| thesis_extension/calibration | 2 | 1051 |
| journal_article/qa/batch4/runtime/inc/lib/unicore/lib/Ext | 1 | 932 |
| journal_article/qa/batch4/runtime/inc/lib/unicore/lib/CE | 1 | 930 |
| journal_article/qa/batch4/runtime/inc/lib/unicore/lib/SD | 1 | 922 |
| thesis_extension/environment/legacy_R343_library/foreach/demo | 1 | 907 |
| thesis_extension/environment/legacy_R343_library/checkmate/include | 2 | 887 |
| thesis_extension/environment/legacy_R343_library/mvtnorm/C_API_Example/R | 1 | 878 |
| journal_article/qa/batch4/runtime/inc/lib/unicore/lib/PatSyn | 1 | 821 |
| journal_article/qa/batch4/runtime/inc/lib/JSON/PP | 1 | 810 |
| journal_article/qa/batch4/runtime/inc/lib/unicore/lib/Ideo | 1 | 795 |
| journal_article/qa/batch4/runtime/inc/lib/unicore/lib/Dash | 1 | 792 |
| journal_validation/stage2g/end_to_end_certification/results/primary_exact_reaudit/pilot_014_plus/C | 1 | 779 |
| journal_validation/stage2g/end_to_end_certification/results/primary_exact_reaudit/pilot_003_plus/C | 1 | 778 |
| journal_validation/stage2g/end_to_end_certification/results/primary_exact_reaudit/pilot_004_truth/C | 1 | 778 |
| journal_validation/stage2g/end_to_end_certification/results/primary_exact_reaudit/pilot_007_plus/C | 1 | 777 |
| journal_validation/stage2g/end_to_end_certification/results/primary_exact_reaudit/pilot_007_truth/C | 1 | 777 |
| journal_validation/stage2g/end_to_end_certification/results/primary_exact_reaudit/pilot_014_minus/C | 1 | 777 |
| journal_validation/stage2g/end_to_end_certification/results/primary_exact_reaudit/pilot_006_minus/C | 1 | 776 |
| journal_validation/stage2g/end_to_end_certification/results/primary_exact_reaudit/pilot_006_plus/C | 1 | 776 |
| journal_article/qa/batch4/runtime/inc/lib/Carp | 1 | 773 |
| journal_article/qa/batch4/runtime/inc/lib/warnings | 1 | 759 |
| journal_article/qa/batch4/runtime/inc/lib/Role/Tiny | 1 | 745 |
| journal_validation/stage2g/end_to_end_certification/results/primary_exact_reaudit/pilot_001_plus/C | 1 | 742 |
| journal_validation/stage2g/end_to_end_certification/results/primary_exact_reaudit/pilot_002_truth/C | 1 | 742 |
| journal_validation/stage2g/end_to_end_certification/results/primary_exact_reaudit/pilot_003_minus/C | 1 | 742 |
| journal_validation/stage2g/end_to_end_certification/results/primary_exact_reaudit/pilot_004_minus/C | 1 | 742 |
| journal_validation/stage2g/end_to_end_certification/results/primary_exact_reaudit/pilot_005_minus/C | 1 | 742 |
| journal_validation/stage2g/end_to_end_certification/results/primary_exact_reaudit/pilot_005_truth/C | 1 | 742 |
| journal_validation/stage2g/end_to_end_certification/results/primary_exact_reaudit/pilot_014_truth/C | 1 | 742 |
| journal_validation/stage2g/end_to_end_certification/results/primary_exact_reaudit/pilot_002_minus/C | 1 | 741 |
| journal_validation/stage2g/end_to_end_certification/results/primary_exact_reaudit/pilot_004_plus/C | 1 | 741 |
| journal_validation/stage2g/end_to_end_certification/results/primary_exact_reaudit/pilot_005_plus/C | 1 | 741 |
| journal_validation/stage2g/end_to_end_certification/results/primary_exact_reaudit/pilot_002_plus/C | 1 | 740 |
| journal_validation/stage2g/end_to_end_certification/results/primary_exact_reaudit/pilot_003_truth/C | 1 | 740 |
| journal_validation/stage2g/end_to_end_certification/results/primary_exact_reaudit/pilot_006_truth/C | 1 | 740 |
| journal_validation/stage2g/end_to_end_certification/results/primary_exact_reaudit/pilot_007_minus/C | 1 | 740 |
| journal_validation/stage2g/end_to_end_certification/results/primary_exact_reaudit/pilot_001_minus/C | 1 | 739 |
| journal_validation/stage2g/end_to_end_certification/results/primary_exact_reaudit/pilot_001_truth/C | 1 | 739 |
| journal_article/qa/batch4/runtime/inc/lib/Test2/Hub/Interceptor | 1 | 736 |
| journal_article/qa/batch4/runtime/inc/lib/unicore/lib/DI | 1 | 730 |
| journal_article/qa/batch4/runtime/inc/lib/unicore/lib/UIdeo | 1 | 730 |
| thesis_extension/environment/legacy_R343_library/Rcpp/unitTests/testRcppClass | 2 | 722 |
| journal_article/qa/batch4/runtime/inc/lib/unicore/lib/QMark | 1 | 666 |
| Empirical_work/original_reg | 2 | 651 |
| thesis_extension/environment/legacy_R343_library/Rcpp/unitTests/testRcppPackage/src | 2 | 642 |
| journal_article/qa/batch4/runtime/inc/lib/unicore/lib/EComp | 1 | 634 |
| journal_article/qa/batch4/runtime/inc/lib/unicore/lib/Hyphen | 1 | 632 |
| journal_validation/stage2h/readiness/results/sequential | 12 | 614 |
| journal_article/qa/batch4/runtime/inc/lib/unicore/lib/Dep | 1 | 606 |
| thesis_extension/config | 1 | 601 |
| thesis_extension/environment/legacy_R343_library/mvtnorm/C_API_Example/src | 1 | 596 |
| journal_validation/stage2h/readiness/results/parallel | 12 | 590 |
| journal_article/qa/batch4/runtime/inc/lib/unicore/lib/PCM | 1 | 584 |
| journal_article/qa/batch4/runtime/inc/lib/unicore/lib/Hst | 1 | 579 |
| journal_article/qa/batch4/runtime/inc/lib/unicore/lib/Hex | 1 | 575 |
| journal_validation/stage2h/readiness/results/repeat | 12 | 566 |
| thesis_extension/environment/legacy_R343_library/Rcpp/unitTests/testRcppModule | 2 | 563 |
| journal_article/qa/batch4/runtime/inc/lib/unicore/lib/BidiC | 1 | 555 |
| journal_article/qa/batch4/runtime/config/tex/generic/config | 1 | 545 |
| thesis_extension/environment/legacy_R343_library/Rcpp/prompt | 1 | 540 |
| thesis_extension/environment/legacy_R343_library/Rcpp/unitTests/testRcppClass/tests | 1 | 462 |
| thesis_extension/environment/legacy_R343_library/Rcpp/unitTests/testRcppModule/R | 2 | 439 |
| thesis_extension/environment/legacy_R343_library/Rcpp/unitTests/testRcppPackage | 2 | 395 |
| thesis_extension/environment/legacy_R343_library/Rcpp/unitTests/testRcppModule/tests | 1 | 391 |
| thesis_extension/environment/legacy_R343_library/mvtnorm/C_API_Example/tests | 1 | 389 |
| thesis_extension/environment/legacy_R343_library/Rcpp/unitTests/testRcppPackage/man | 1 | 388 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/interruption_audits | 2 | 356 |
| thesis_extension/environment/legacy_R343_library/stringr/htmlwidgets | 2 | 350 |
| thesis_extension/environment/legacy_R343_library/mvtnorm/C_API_Example | 2 | 348 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r10_t90_k010_c0_A | 1 | 280 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r10_t90_k010_c0_B | 1 | 280 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r10_t90_k100_c0_B | 1 | 280 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r11_t10_k010_c0_A | 1 | 280 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r11_t10_k010_c0_B | 1 | 280 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r11_t10_k100_c0_A | 1 | 280 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r11_t10_k100_c0_B | 1 | 280 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r11_t50_k010_c0_A | 1 | 280 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r11_t50_k010_c0_B | 1 | 280 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r11_t50_k100_c0_A | 1 | 280 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r11_t50_k100_c0_B | 1 | 280 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r11_t90_k010_c0_A | 1 | 280 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r11_t90_k010_c0_B | 1 | 280 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r11_t90_k100_c0_A | 1 | 280 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r11_t90_k100_c0_B | 1 | 280 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r12_t10_k010_c0_A | 1 | 280 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r12_t10_k010_c0_B | 1 | 280 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r12_t10_k100_c0_A | 1 | 280 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r12_t10_k100_c0_B | 1 | 280 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r12_t50_k010_c0_A | 1 | 280 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r12_t50_k010_c0_B | 1 | 280 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r12_t50_k100_c0_A | 1 | 280 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r12_t50_k100_c0_B | 1 | 280 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r12_t90_k010_c0_A | 1 | 280 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r12_t90_k010_c0_B | 1 | 280 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r12_t90_k100_c0_A | 1 | 280 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r12_t90_k100_c0_B | 1 | 280 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r13_t10_k010_c0_A | 1 | 280 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r13_t10_k010_c0_B | 1 | 280 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r13_t10_k100_c0_A | 1 | 280 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r13_t10_k100_c0_B | 1 | 280 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r13_t50_k010_c0_A | 1 | 280 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r13_t50_k010_c0_B | 1 | 280 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r13_t50_k100_c0_A | 1 | 280 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r13_t50_k100_c0_B | 1 | 280 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r13_t90_k010_c0_A | 1 | 280 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r13_t90_k010_c0_B | 1 | 280 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r13_t90_k100_c0_A | 1 | 280 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r13_t90_k100_c0_B | 1 | 280 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r14_t10_k010_c0_A | 1 | 280 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r14_t10_k010_c0_B | 1 | 280 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r14_t10_k100_c0_A | 1 | 280 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r14_t10_k100_c0_B | 1 | 280 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r14_t50_k010_c0_A | 1 | 280 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r14_t50_k010_c0_B | 1 | 280 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r14_t50_k100_c0_A | 1 | 280 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r14_t50_k100_c0_B | 1 | 280 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r14_t90_k010_c0_A | 1 | 280 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r14_t90_k010_c0_B | 1 | 280 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r14_t90_k100_c0_A | 1 | 280 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r14_t90_k100_c0_B | 1 | 280 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r15_t10_k010_c0_A | 1 | 280 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r15_t10_k010_c0_B | 1 | 280 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r15_t10_k100_c0_A | 1 | 280 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r15_t10_k100_c0_B | 1 | 280 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r15_t50_k010_c0_A | 1 | 280 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r15_t50_k010_c0_B | 1 | 280 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r15_t50_k100_c0_A | 1 | 280 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r15_t50_k100_c0_B | 1 | 280 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r15_t90_k010_c0_A | 1 | 280 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r15_t90_k010_c0_B | 1 | 280 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r15_t90_k100_c0_A | 1 | 280 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r15_t90_k100_c0_B | 1 | 280 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r16_t10_k010_c0_A | 1 | 280 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r16_t10_k010_c0_B | 1 | 280 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r16_t10_k100_c0_A | 1 | 280 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r16_t10_k100_c0_B | 1 | 280 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r16_t50_k010_c0_A | 1 | 280 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r16_t50_k010_c0_B | 1 | 280 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r16_t50_k100_c0_A | 1 | 280 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r16_t50_k100_c0_B | 1 | 280 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r16_t90_k010_c0_A | 1 | 280 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r16_t90_k010_c0_B | 1 | 280 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r16_t90_k100_c0_A | 1 | 280 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r16_t90_k100_c0_B | 1 | 280 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r17_t10_k010_c0_A | 1 | 280 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r17_t10_k010_c0_B | 1 | 280 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r17_t10_k100_c0_A | 1 | 280 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r17_t10_k100_c0_B | 1 | 280 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r17_t50_k010_c0_A | 1 | 280 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r17_t50_k010_c0_B | 1 | 280 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r17_t50_k100_c0_A | 1 | 280 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r17_t50_k100_c0_B | 1 | 280 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r17_t90_k010_c0_A | 1 | 280 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r17_t90_k010_c0_B | 1 | 280 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r17_t90_k100_c0_A | 1 | 280 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r17_t90_k100_c0_B | 1 | 280 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r18_t10_k010_c0_A | 1 | 280 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r18_t10_k010_c0_B | 1 | 280 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r18_t10_k100_c0_A | 1 | 280 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r18_t10_k100_c0_B | 1 | 280 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r18_t50_k010_c0_A | 1 | 280 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r18_t50_k010_c0_B | 1 | 280 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r18_t50_k100_c0_A | 1 | 280 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r18_t50_k100_c0_B | 1 | 280 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r18_t90_k010_c0_A | 1 | 280 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r18_t90_k010_c0_B | 1 | 280 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r18_t90_k100_c0_A | 1 | 280 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r18_t90_k100_c0_B | 1 | 280 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r19_t10_k010_c0_A | 1 | 280 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r19_t10_k010_c0_B | 1 | 280 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r19_t10_k100_c0_A | 1 | 280 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r19_t10_k100_c0_B | 1 | 280 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r19_t50_k010_c0_A | 1 | 280 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r19_t50_k010_c0_B | 1 | 280 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r19_t50_k100_c0_A | 1 | 280 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r19_t50_k100_c0_B | 1 | 280 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r19_t90_k010_c0_A | 1 | 280 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r19_t90_k010_c0_B | 1 | 280 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r19_t90_k100_c0_A | 1 | 280 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r19_t90_k100_c0_B | 1 | 280 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r20_t10_k010_c0_A | 1 | 280 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r20_t10_k010_c0_B | 1 | 280 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r20_t10_k100_c0_A | 1 | 280 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r20_t10_k100_c0_B | 1 | 280 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r20_t50_k010_c0_A | 1 | 280 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r20_t50_k010_c0_B | 1 | 280 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r20_t50_k100_c0_A | 1 | 280 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r20_t50_k100_c0_B | 1 | 280 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r20_t90_k010_c0_A | 1 | 280 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r20_t90_k010_c0_B | 1 | 280 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r20_t90_k100_c0_A | 1 | 280 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r20_t90_k100_c0_B | 1 | 280 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r10_t90_k010_c1_A | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r10_t90_k010_c1_B | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r10_t90_k010_c2_A | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r10_t90_k010_c2_B | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r10_t90_k100_c1_A | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r10_t90_k100_c1_B | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r10_t90_k100_c2_A | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r10_t90_k100_c2_B | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r11_t10_k010_c1_A | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r11_t10_k010_c1_B | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r11_t10_k010_c2_A | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r11_t10_k010_c2_B | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r11_t10_k100_c1_A | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r11_t10_k100_c1_B | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r11_t10_k100_c2_A | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r11_t10_k100_c2_B | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r11_t50_k010_c1_A | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r11_t50_k010_c1_B | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r11_t50_k010_c2_A | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r11_t50_k010_c2_B | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r11_t50_k100_c1_A | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r11_t50_k100_c1_B | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r11_t50_k100_c2_A | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r11_t50_k100_c2_B | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r11_t90_k010_c1_A | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r11_t90_k010_c1_B | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r11_t90_k010_c2_A | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r11_t90_k010_c2_B | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r11_t90_k100_c1_A | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r11_t90_k100_c1_B | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r11_t90_k100_c2_A | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r11_t90_k100_c2_B | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r12_t10_k010_c1_A | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r12_t10_k010_c1_B | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r12_t10_k010_c2_A | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r12_t10_k010_c2_B | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r12_t10_k100_c1_A | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r12_t10_k100_c1_B | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r12_t10_k100_c2_A | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r12_t10_k100_c2_B | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r12_t50_k010_c1_A | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r12_t50_k010_c1_B | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r12_t50_k010_c2_A | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r12_t50_k010_c2_B | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r12_t50_k100_c1_A | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r12_t50_k100_c1_B | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r12_t50_k100_c2_A | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r12_t50_k100_c2_B | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r12_t90_k010_c1_A | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r12_t90_k010_c1_B | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r12_t90_k010_c2_A | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r12_t90_k010_c2_B | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r12_t90_k100_c1_A | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r12_t90_k100_c1_B | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r12_t90_k100_c2_A | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r12_t90_k100_c2_B | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r13_t10_k010_c1_A | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r13_t10_k010_c1_B | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r13_t10_k010_c2_A | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r13_t10_k010_c2_B | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r13_t10_k100_c1_A | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r13_t10_k100_c1_B | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r13_t10_k100_c2_A | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r13_t10_k100_c2_B | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r13_t50_k010_c1_A | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r13_t50_k010_c1_B | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r13_t50_k010_c2_A | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r13_t50_k010_c2_B | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r13_t50_k100_c1_A | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r13_t50_k100_c1_B | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r13_t50_k100_c2_A | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r13_t50_k100_c2_B | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r13_t90_k010_c1_A | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r13_t90_k010_c1_B | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r13_t90_k010_c2_A | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r13_t90_k010_c2_B | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r13_t90_k100_c1_A | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r13_t90_k100_c1_B | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r13_t90_k100_c2_A | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r13_t90_k100_c2_B | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r14_t10_k010_c1_A | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r14_t10_k010_c1_B | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r14_t10_k010_c2_A | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r14_t10_k010_c2_B | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r14_t10_k100_c1_A | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r14_t10_k100_c1_B | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r14_t10_k100_c2_A | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r14_t10_k100_c2_B | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r14_t50_k010_c1_A | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r14_t50_k010_c1_B | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r14_t50_k010_c2_A | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r14_t50_k010_c2_B | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r14_t50_k100_c1_A | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r14_t50_k100_c1_B | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r14_t50_k100_c2_A | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r14_t50_k100_c2_B | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r14_t90_k010_c1_A | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r14_t90_k010_c1_B | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r14_t90_k010_c2_A | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r14_t90_k010_c2_B | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r14_t90_k100_c1_A | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r14_t90_k100_c1_B | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r14_t90_k100_c2_A | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r14_t90_k100_c2_B | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r15_t10_k010_c1_A | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r15_t10_k010_c1_B | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r15_t10_k010_c2_A | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r15_t10_k010_c2_B | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r15_t10_k100_c1_A | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r15_t10_k100_c1_B | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r15_t10_k100_c2_A | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r15_t10_k100_c2_B | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r15_t50_k010_c1_A | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r15_t50_k010_c1_B | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r15_t50_k010_c2_A | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r15_t50_k010_c2_B | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r15_t50_k100_c1_A | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r15_t50_k100_c1_B | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r15_t50_k100_c2_A | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r15_t50_k100_c2_B | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r15_t90_k010_c1_A | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r15_t90_k010_c1_B | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r15_t90_k010_c2_A | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r15_t90_k010_c2_B | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r15_t90_k100_c1_A | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r15_t90_k100_c1_B | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r15_t90_k100_c2_A | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r15_t90_k100_c2_B | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r16_t10_k010_c1_A | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r16_t10_k010_c1_B | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r16_t10_k010_c2_A | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r16_t10_k010_c2_B | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r16_t10_k100_c1_A | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r16_t10_k100_c1_B | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r16_t10_k100_c2_A | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r16_t10_k100_c2_B | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r16_t50_k010_c1_A | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r16_t50_k010_c1_B | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r16_t50_k010_c2_A | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r16_t50_k010_c2_B | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r16_t50_k100_c1_A | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r16_t50_k100_c1_B | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r16_t50_k100_c2_A | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r16_t50_k100_c2_B | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r16_t90_k010_c1_A | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r16_t90_k010_c1_B | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r16_t90_k010_c2_A | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r16_t90_k010_c2_B | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r16_t90_k100_c1_A | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r16_t90_k100_c1_B | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r16_t90_k100_c2_A | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r16_t90_k100_c2_B | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r17_t10_k010_c1_A | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r17_t10_k010_c1_B | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r17_t10_k010_c2_A | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r17_t10_k010_c2_B | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r17_t10_k100_c1_A | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r17_t10_k100_c1_B | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r17_t10_k100_c2_A | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r17_t10_k100_c2_B | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r17_t50_k010_c1_A | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r17_t50_k010_c1_B | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r17_t50_k010_c2_A | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r17_t50_k010_c2_B | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r17_t50_k100_c1_A | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r17_t50_k100_c1_B | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r17_t50_k100_c2_A | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r17_t50_k100_c2_B | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r17_t90_k010_c1_A | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r17_t90_k010_c1_B | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r17_t90_k010_c2_A | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r17_t90_k010_c2_B | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r17_t90_k100_c1_A | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r17_t90_k100_c1_B | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r17_t90_k100_c2_A | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r17_t90_k100_c2_B | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r18_t10_k010_c1_A | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r18_t10_k010_c1_B | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r18_t10_k010_c2_A | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r18_t10_k010_c2_B | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r18_t10_k100_c1_A | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r18_t10_k100_c1_B | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r18_t10_k100_c2_A | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r18_t10_k100_c2_B | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r18_t50_k010_c1_A | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r18_t50_k010_c1_B | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r18_t50_k010_c2_A | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r18_t50_k010_c2_B | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r18_t50_k100_c1_A | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r18_t50_k100_c1_B | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r18_t50_k100_c2_A | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r18_t50_k100_c2_B | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r18_t90_k010_c1_A | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r18_t90_k010_c1_B | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r18_t90_k010_c2_A | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r18_t90_k010_c2_B | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r18_t90_k100_c1_A | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r18_t90_k100_c1_B | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r18_t90_k100_c2_A | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r18_t90_k100_c2_B | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r19_t10_k010_c1_A | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r19_t10_k010_c1_B | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r19_t10_k010_c2_A | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r19_t10_k010_c2_B | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r19_t10_k100_c1_A | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r19_t10_k100_c1_B | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r19_t10_k100_c2_A | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r19_t10_k100_c2_B | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r19_t50_k010_c1_A | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r19_t50_k010_c1_B | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r19_t50_k010_c2_A | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r19_t50_k010_c2_B | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r19_t50_k100_c1_A | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r19_t50_k100_c1_B | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r19_t50_k100_c2_A | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r19_t50_k100_c2_B | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r19_t90_k010_c1_A | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r19_t90_k010_c1_B | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r19_t90_k010_c2_A | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r19_t90_k010_c2_B | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r19_t90_k100_c1_A | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r19_t90_k100_c1_B | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r19_t90_k100_c2_A | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r19_t90_k100_c2_B | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r20_t10_k010_c1_A | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r20_t10_k010_c1_B | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r20_t10_k010_c2_A | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r20_t10_k010_c2_B | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r20_t10_k100_c1_A | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r20_t10_k100_c1_B | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r20_t10_k100_c2_A | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r20_t10_k100_c2_B | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r20_t50_k010_c1_A | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r20_t50_k010_c1_B | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r20_t50_k010_c2_A | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r20_t50_k010_c2_B | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r20_t50_k100_c1_A | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r20_t50_k100_c1_B | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r20_t50_k100_c2_A | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r20_t50_k100_c2_B | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r20_t90_k010_c1_A | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r20_t90_k010_c1_B | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r20_t90_k010_c2_A | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r20_t90_k010_c2_B | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r20_t90_k100_c1_A | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r20_t90_k100_c1_B | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r20_t90_k100_c2_A | 1 | 279 |
| journal_validation/stage2h/pilot/runs/paired_20261102T112532Z/results/resume_v2/n1000_r20_t90_k100_c2_B | 1 | 279 |
| journal_article/qa/batch4/runtime/config/miktex/config | 2 | 257 |
| thesis_extension/environment/legacy_R343_library/stringr/htmlwidgets/lib | 1 | 184 |
| journal_article/qa/batch4/runtime/data/fonts/map/dvipdfmx | 1 | 180 |
| journal_article/qa/batch4/runtime/inc/lib/auto/share/dist/File-ShareDir/subdir | 1 | 166 |
| journal_article/qa/batch4/runtime/inc/lib/auto/share/dist/File-ShareDir | 1 | 159 |
| thesis_extension/environment/legacy_R343_library/ggplot2/help/macros | 1 | 94 |
| thesis_extension/environment/legacy_R343_library/Rcpp/unitTests/testRcppPackage/R | 1 | 94 |
| journal_article/qa/batch4/runtime/inc/lib/auto/Data/Uniqid | 1 | 93 |
| .vscode | 1 | 40 |
| journal_article/qa/batch4/runtime/inc/lib/auto/share/module/File-ShareDir | 1 | 18 |

### Disposition counts

| Classification | Rows |
|---|---|
| DUPLICATE | 326 |
| EXCLUDE_GENERATED | 120 |
| KEEP_PRIVATE_ARCHIVE | 122647 |
| KEEP_PUBLIC | 195 |
| NEEDS_AUTHOR_DECISION | 11533 |
| SENSITIVE_REVIEW | 25 |
| THIRD_PARTY_REVIEW | 2900 |

## Existing evidence manifest cross-check

| Manifest | Rows checked | Observed status counts |
|---|---|---|
| thesis_extension/reporting/EMPIRICAL_RESULTS_MANIFEST.csv | 2999 | {'SHA256_MATCH': 2998, 'HASH_DIFF_REVIEW': 1} |
| thesis_extension/reporting/REPORTING_OUTPUT_MANIFEST.csv | 33 | {'SHA256_MATCH': 32, 'HASH_DIFF_REVIEW': 1} |
| thesis_extension/diagnostics/grid_sensitivity/GRID_RESULTS_MANIFEST.csv | 124 | {'SHA256_MATCH': 124} |

Byte-hash comparisons are audit inventory checks, not numerical research validation. Historical hashes can differ because Git checkout line endings changed. LF_NORMALIZATION_MATCH_ONLY explicitly distinguishes that case; remaining HASH_DIFF_REVIEW records need content/provenance review and are not presumed corrupted. Missing records were not recreated.

| Manifest | Referenced path | Finding |
|---|---|---|
| thesis_extension/reporting/EMPIRICAL_RESULTS_MANIFEST.csv | thesis_extension/environment/AUTHOR_R343_ENVIRONMENT_REPORT.md | HASH_DIFF_REVIEW |
| thesis_extension/reporting/REPORTING_OUTPUT_MANIFEST.csv | thesis_extension/reporting/build_thesis_results.R | HASH_DIFF_REVIEW |


## Read-only remote verification

On 12 November 2026, the connected GitHub fetch tool returned public repository metadata (private=false; visibility=public) and both branch tips matching the local audited journal-validation and main refs. No git fetch/push or remote mutation occurred.

The four reports R020–R023 were readable through GitHub contents reads at journal-validation. They are therefore not missing/local-only as reports; their companion dynamic dependency gaps remain material. Connected read access plus public metadata supports repository availability, not a verified anonymous-review transfer or full public reproducibility bundle.

Sources: [repository metadata](https://api.github.com/repos/U-Olim/DML-IVQR_Master_Thesis), [branch tips](https://api.github.com/repos/U-Olim/DML-IVQR_Master_Thesis/branches), [R020](https://github.com/U-Olim/DML-IVQR_Master_Thesis/blob/journal-validation/journal_validation/stage2c/stability/STABILITY_REPORT.md), [R021](https://github.com/U-Olim/DML-IVQR_Master_Thesis/blob/journal-validation/journal_validation/stage2g/deterministic_implementation/DETERMINISTIC_IMPLEMENTATION_REPORT.md), [R022](https://github.com/U-Olim/DML-IVQR_Master_Thesis/blob/journal-validation/journal_validation/stage2g/deterministic_implementation/IMPLEMENTATION_CONTRACT_v1.md), [R023](https://github.com/U-Olim/DML-IVQR_Master_Thesis/blob/journal-validation/journal_validation/stage2g/full_path_validation/FULL_PATH_REPORT.md).

## Final audit-output verification

Canonical static dependency closure: 32 files; no missing local inputs. Corrected-build source snapshot/current source comparisons: 39 pairs, 0 differences. This compares available bytes, not the PDF build process or research correctness.

| Snapshot source mismatch | Current source |
|---|---|

The upstream [FieldTien/DML-IVQR repository metadata](https://api.github.com/repos/FieldTien/DML-IVQR) returned license=null on 12 November 2026. That means no license recognized by this metadata endpoint, not a determination that every file lacks a license; upstream permissions remain THIRD_PARTY_REVIEW.

| Deliverable | Data rows |
|---|---|
| MANUSCRIPT_VERSION_MAP.csv | 346 |
| PUBLIC_PACKAGE_DISPOSITION.csv | 137746 |
| REPOSITORY_FILE_INVENTORY.csv | 83566 |
| RESEARCH_DEPENDENCY_MAP.csv | 3398 |

All four CSVs parsed successfully. Current and staged tracked diffs are empty. Exactly the requested report and four CSVs are new; no other new files were produced. No research file was edited, no result reconstructed, and no simulation/estimator/numerical validation was executed. Final classification: **PARTIAL**, with the explicit historical-content/privacy and dynamic-dependency limits stated above.
