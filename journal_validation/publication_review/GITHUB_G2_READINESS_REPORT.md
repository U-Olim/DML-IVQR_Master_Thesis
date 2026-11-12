# G2 — Publication repository migration readiness

12 November 2026. Branch journal-validation; source HEAD dc2a6bb33df15f8c01b1282332273b2944f2ad9f.
Target repository: IVQR-Instrument-Relevance-Monte-Carlo.
**Final decision: CONDITIONAL.** Proposed selection is complete at file level for the defined base package; upload clearance and complete numerical replay are not established. No migration or publication occurred.

## Executive assessment

The corrected canonical source/PDF and frozen main evidence can be selected by exact hash. Remaining conditions are unresolved historical manifest provenance, missing Stage 2F saved outputs, derivative-code redistribution rights, manuscript/asset permissions, privacy review and historical replay guards. Complete selected-case replay remains blocked until its prerequisite bundles are verified; this does not mean the existing reports or main CSVs are missing or scientifically disproven.

Read G1 report and all four inventories (83566 file rows; 137746 disposition rows; 346 manuscript rows; 3398 dependency rows). All G1 KEEP_PUBLIC candidates are reviewed in the new allowlist. Existing G1 historical-body/privacy scan limits remain; G2 is not an exhaustive historical secret scan.

## 1. Manifest discrepancies

MANIFEST_DISCREPANCY_REPORT.md records exact expected/actual digests, inspected commits, line-ending alternatives, significance and corrective actions. Both actual files match HEAD. Their accessible path history starts with e864dd273da6718751c2d5ac5ce6921fd330cd7e; expected-byte versions were not located there. Stale pre-import hashes are plausible, not proven. Never silently change an archived manifest or claim an exact content diff against missing bytes.

The environment report mismatch affects provenance; the reporting generator mismatch affects authentication/replay. Neither is a numerical result mismatch. G1 found 3,154 matching manifest entries, two differences and no missing entries; all 124 grid entries matched. Preserve that distinction.

## 2. Stage 2F dependency review at 50412fe7

| Historical path | Git blob | SHA256 |
|---|---|---|
| journal_validation/stage2f/.gitignore | fd6aad7fa7789c8d23a86afd469f09f91ee60277 | 7e2f65c80bddb76631f05a448b09378247e7f14af4ade18127925c07a6538dbf |
| journal_validation/stage2f/README.md | ced8db33edbe50105a0f4d4ab675451974713ec5 | ec7e7c98ea1398b457f941dc1c9310641b7234b4d9af3619871219e3f4160a32 |
| journal_validation/stage2f/STAGE2F_REPORT.md | c479e0b246ad3c1612f647a13601e23712f86cae | 23e9fa65e8d0748bfcf2d237a08823a8b1ed446729bec646f535d334c757bed1 |
| journal_validation/stage2f/analyze.py | 9575b167d6f6dae17dd3b1bb4ccce57d52310d05 | 4f7de74916b8d0b5ac1182482e6f6b3340b644e44ba8dfdf66e9f20489305608 |
| journal_validation/stage2f/finalize.py | 4ae6b8f110e3d07201156867d4a3a921785a7f82 | cda2ea6bcefb29168a73ed9274285478dfe18e59081b5e752da31bb9f9086596 |
| journal_validation/stage2f/near_optimal.py | 6b1c5a23478090e7d88acae00d0a1bb60a6f1417 | 2c094add78ed4a5c753ae87a60a5eb033be8802f0bc3875806cf2b9c3190c742 |
| journal_validation/stage2f/representation.R | 466dea690a463ae8c9f73603410fe2f985ce761a | e5d8a0bf50e975ca25cb24a7949a4f64e6c226f741b3c08ecf858692a52193dc |
| journal_validation/stage2f/representation_split.py | eb66be4b13414b397b3cf3c0d6ed72fa00eb7bb8 | f13e88ae87b795c5c962b0b4b14614a1551fc85a3029361374a93cf7fb6d1e76 |
| journal_validation/stage2f/verify.py | d61b058dde20672e3ed2712448819ae25f1f57d8 | 532761829af26658dba24b28e936d509e6fba16df5422871fef56c53177a313e |
| journal_validation/stage2f/verify_near_optimal.py | bef7e51f773bf70a4c604256f9c2bc8174da41f2 | 2405c047648212ec4959b2d5ae50b0e31ab3022736ba5de24b50555339c55729 |


Exact source chains inspected:
- stage2g/validate.py and verify.py import Stage 2F analyze helpers. Validation also checks output/exact_face_20261029T102755Z.
- deterministic_implementation/common_v1.py imports analyze helpers; verify_v1.py loads Stage 2F verify.py.
- full_path_validation/common.py imports analyze helpers; prepare.py reads the saved exact-face output directory.
- Stage 2F analyze.py imports dyadic, bareiss_solve and record from stage2c/certification/exact_bounds.py, and uses NumPy plus Python integers/Fractions. verify.py provides separate rational/statistic functions.
- near_optimal.py imports analyze helpers; representation_split.py imports verify. These, representation.R, verify_near_optimal.py and finalize.py belong to the separate two-case F replay, not automatically the cited G path. Preserve historically, include only if that additional scope is chosen.

analyze.py and verify.py are recoverable historical source, held with exact commit/blob/SHA256. They are necessary for the cited downstream implementation's code inspection/replay, but not for simply reading R020–R023. README/STAGE2F_REPORT document their scope. Nothing was restored.

Missing saved-output references recorded in existing input manifests:
| Manifest | Missing dependency | Recorded digest |
|---|---|---|
| journal_validation/stage2g/deterministic_implementation/INPUT_SHA256_MANIFEST.json | journal_validation/stage2f/analyze.py | 4f7de74916b8d0b5ac1182482e6f6b3340b644e44ba8dfdf66e9f20489305608 |
| journal_validation/stage2g/deterministic_implementation/INPUT_SHA256_MANIFEST.json | journal_validation/stage2f/verify.py | 532761829af26658dba24b28e936d509e6fba16df5422871fef56c53177a313e |
| journal_validation/stage2h/readiness/INPUT_SHA256_MANIFEST.json | journal_validation/stage2f/analyze.py | 4f7de74916b8d0b5ac1182482e6f6b3340b644e44ba8dfdf66e9f20489305608 |
| journal_validation/stage2h/readiness/INPUT_SHA256_MANIFEST.json | journal_validation/stage2f/verify.py | 532761829af26658dba24b28e936d509e6fba16df5422871fef56c53177a313e |


output/exact_face_20261029T102755Z and its saved arrays/certificates/manifest are absent. Historical source availability does not prove those saved outputs are recoverable. Do not rebuild them. Complete F/G replay requires the saved Stage 2E inputs and all downstream prerequisite bundles, not just analyze.py. The base allowlist explicitly includes selected reports/contracts, not a falsely complete wholesale numerical replay archive. Enumerating/verifying a separate full replay supplement remains a staging condition.

## 3. Definitive proposed base allowlist

PUBLIC_RELEASE_ALLOWLIST.csv has 210 reviewed file/version rows. Filter decision=PROPOSED_INCLUDE for current-file base candidates. Historical source holds and optional archive rows are not present files or automatic copy instructions. Every selected current file was rehashed against G1; any mismatch would have stopped report generation. Git blob identity and source commit distinguish historical bytes from current ones.

The selection covers the exact recursive article closure (32 files), corrected 34-page PDF, both sample sizes' six frozen main files, DGP/estimator/metrics/runner code, main configuration, primary calibration, enumerated tracked domain diagnostic outputs/config/provenance, coverage audit, manifest-enumerated reporting tables and generators, R020–R023, selected policies/configuration, environment metadata and upstream implementation audits.

Corrected PDF SHA256: 4e9800270d35afd6332abe109bae7eb6fce4a0d8bdb24cbebef30370fc088e7b.
Only this corrected PDF is proposed; older 34-page and cancelled 29-page versions remain archival. No entire directory is included merely by prefix.

Ignored domain profiles/primitives remain essential privately preserved supporting evidence; existing manifests and local-only limitations must travel with the package. They are not disposable. Stage 2H pilot, unrelated empirical examples, university templates, old thesis/submission PDFs, build caches and bundled software are excluded from the base package.

README is a source candidate requiring a later journal-focused rewrite, truthful thesis provenance and upstream credit; do not ship it unchanged. Existing manifests remain historical records; a new release manifest is a separate later artifact.

## 4. Rights, privacy and notices

THIRD_PARTY_RIGHTS_REGISTER.csv separates original contributions, modified external code, manuscript/figure assets, simulated results, environment descriptions and excluded archives/templates. Root MIT licensing is limited; it is not a blanket grant for the manuscript, third-party software or copied implementations.

The implementation audit records Oracle/Full wrappers copied from upstream Table 2 and DML lineage from Table 3. These need actual upstream license/permission evidence. G1's upstream GitHub metadata recognized no license; that is not permission and does not prove every upstream file lacks terms. Preserve FieldTien/DML-IVQR, cited-paper and recorded source-commit attribution. A later THIRD_PARTY_NOTICES.md and PROVENANCE.md must document this; neither is created in this reports-only stage.

No third-party package source archives or installed Windows libraries are proposed for automatic inclusion. Publish reviewed environment version descriptions instead, and verify redistribution rights before reconsidering any archive.

Manuscript emails/ORCIDs/affiliation are intentional scholarly metadata but need author confirmation. Environment/session/setup files have machine paths; public reviewed copies require path cleanup later while originals remain unchanged. The environment report links absent PROJECT_STATUS.md. University title/examination/supervisor/declaration information and Bonn templates are unnecessary for the journal package and remain historical. No secret values are reproduced here; CSV privacy columns contain types only.

## 5. Exact migration feasibility

MIGRATION_PATH_MAP.csv maps every proposed current file and held historical source to an exact destination. Retain thesis_extension/, thesis/tools/ and journal_validation/ paths initially. Move the article tree together to manuscript/; internal TeX references remain relative. Research-path mentions remain compatible with retained research paths. Printed journal_article/ paths in supplementary/D_evidence_map.tex must be updated to manuscript/ in a separately authorized source revision; until then moving the tree alone leaves those manuscript-asset references stale. Retaining journal_article/ temporarily is safer if zero source changes are required. The corrected PDF has one explicit manuscript destination.

Retaining thesis names temporarily is safer than a cosmetic restructuring that breaks root discovery/source/config/input/output relationships. A later src/config/results restructuring requires reviewing every caller, not a prefix rename.

Concrete affected source/path/LaTeX/reporting locations:
| File | Line | Dependency kind |
|---|---|---|
| journal_article/main.tex | 1 | configuration_root_paths |
| journal_article/main.tex | 2 | LaTeX_dependency |
| journal_article/main.tex | 25 | LaTeX_dependency |
| journal_article/main.tex | 26 | LaTeX_dependency |
| journal_article/main.tex | 27 | LaTeX_dependency |
| journal_article/main.tex | 28 | LaTeX_dependency |
| journal_article/main.tex | 29 | LaTeX_dependency |
| journal_article/main.tex | 30 | LaTeX_dependency |
| journal_article/main.tex | 31 | LaTeX_dependency |
| journal_article/main.tex | 32 | LaTeX_dependency |
| journal_article/main.tex | 45 | LaTeX_dependency |
| journal_article/main.tex | 46 | LaTeX_dependency |
| journal_article/main.tex | 47 | LaTeX_dependency |
| journal_article/main.tex | 48 | LaTeX_dependency |
| journal_article/preamble.tex | 15 | LaTeX_dependency |
| journal_article/sections/04_results.tex | 9 | LaTeX_dependency |
| journal_article/sections/04_results.tex | 20 | LaTeX_dependency |
| journal_article/sections/04_results.tex | 37 | LaTeX_dependency |
| journal_article/sections/04_results.tex | 58 | LaTeX_dependency |
| journal_article/sections/04_results.tex | 75 | LaTeX_dependency |
| journal_article/sections/data_availability.tex | 2 | freeze_guard |
| journal_article/sections/data_availability.tex | 4 | configuration_root_paths |
| journal_article/supplementary/A_numerical_domain.tex | 24 | LaTeX_dependency |
| journal_article/supplementary/A_numerical_domain.tex | 25 | LaTeX_dependency |
| journal_article/supplementary/B_kappa_derivation.tex | 59 | LaTeX_dependency |
| journal_article/supplementary/C_coverage_audit.tex | 17 | LaTeX_dependency |
| journal_article/supplementary/C_coverage_audit.tex | 26 | LaTeX_dependency |
| journal_article/supplementary/D_evidence_map.tex | 21 | configuration_root_paths |
| journal_article/supplementary/D_evidence_map.tex | 23 | configuration_root_paths |
| journal_article/supplementary/D_evidence_map.tex | 25 | configuration_root_paths |
| journal_article/supplementary/D_evidence_map.tex | 27 | configuration_root_paths |
| journal_article/supplementary/D_evidence_map.tex | 29 | configuration_root_paths |
| journal_article/supplementary/D_evidence_map.tex | 34 | configuration_root_paths |
| journal_article/supplementary/D_implementation.tex | 6 | configuration_root_paths,freeze_guard |
| journal_article/supplementary/D_implementation.tex | 8 | configuration_root_paths |
| journal_article/supplementary/D_implementation.tex | 10 | configuration_root_paths |
| journal_article/supplementary/D_implementation.tex | 14 | LaTeX_dependency |
| journal_article/supplementary/D_implementation.tex | 18 | configuration_root_paths |
| journal_article/supplementary/D_implementation.tex | 180 | configuration_root_paths |
| journal_article/tables/figure_accepted_measure_main.tex | 3 | LaTeX_dependency |
| journal_article/tables/figure_accepted_measure_main.tex | 5 | LaTeX_dependency |
| journal_article/tables/figure_coverage_main.tex | 3 | LaTeX_dependency |
| journal_article/tables/figure_full_domain_acceptance.tex | 3 | LaTeX_dependency |
| journal_article/tables/figure_power_main.tex | 3 | LaTeX_dependency |
| journal_article/tables/generated/figure_grid_domain.tex | 3 | LaTeX_dependency |
| thesis/tools/build_appendix_tables.py | 6 | configuration_root_paths |
| thesis/tools/build_appendix_tables.py | 7 | configuration_root_paths |
| thesis/tools/build_appendix_tables.py | 8 | configuration_root_paths |
| thesis/tools/build_appendix_tables.py | 10 | configuration_root_paths |
| thesis/tools/build_appendix_tables.py | 11 | configuration_root_paths |
| thesis/tools/build_appendix_tables.py | 12 | configuration_root_paths |
| thesis/tools/build_appendix_tables.py | 13 | configuration_root_paths |
| thesis/tools/build_appendix_tables.py | 14 | configuration_root_paths |
| thesis/tools/build_appendix_tables.py | 15 | configuration_root_paths |
| thesis/tools/build_appendix_tables.py | 17 | configuration_root_paths |
| thesis/tools/build_appendix_tables.py | 18 | configuration_root_paths |
| thesis/tools/build_appendix_tables.py | 27 | configuration_root_paths |
| thesis/tools/build_appendix_tables.py | 30 | configuration_root_paths |
| thesis/tools/build_appendix_tables.py | 62 | reporting_IO |
| thesis/tools/build_appendix_tables.py | 65 | reporting_IO |
| thesis/tools/build_appendix_tables.py | 66 | reporting_IO |
| thesis/tools/build_appendix_tables.py | 79 | reporting_IO |
| thesis/tools/build_appendix_tables.py | 88 | configuration_root_paths |
| thesis/tools/build_selected_figures.R | 6 | R_source,configuration_root_paths |
| thesis/tools/build_selected_figures.R | 15 | configuration_root_paths |
| thesis/tools/build_selected_figures.R | 16 | configuration_root_paths,reporting_IO |
| thesis/tools/build_selected_figures.R | 17 | configuration_root_paths,reporting_IO |
| thesis/tools/build_selected_figures.R | 23 | configuration_root_paths,reporting_IO |
| thesis/tools/build_selected_figures.R | 25 | configuration_root_paths,reporting_IO |
| thesis/tools/build_selected_figures.R | 45 | configuration_root_paths |
| thesis/tools/build_thesis_figures.R | 18 | configuration_root_paths |
| thesis/tools/build_thesis_figures.R | 19 | configuration_root_paths |
| thesis/tools/build_thesis_figures.R | 20 | configuration_root_paths,reporting_IO |
| thesis/tools/build_thesis_figures.R | 22 | reporting_IO |
| thesis/tools/build_thesis_figures.R | 23 | reporting_IO |
| thesis/tools/build_thesis_figures.R | 24 | reporting_IO |
| thesis/tools/build_thesis_figures.R | 29 | configuration_root_paths |
| thesis/tools/build_thesis_figures.R | 30 | configuration_root_paths |
| thesis/tools/build_thesis_figures.R | 35 | reporting_IO |
| thesis/tools/build_thesis_figures.R | 148 | configuration_root_paths |
| thesis/tools/build_thesis_figures.R | 149 | configuration_root_paths |
| thesis/tools/build_thesis_figures.R | 177 | configuration_root_paths,reporting_IO |
| thesis_extension/calibration/instrument_strength_100rep/run_strength_calibration.R | 9 | configuration_root_paths |
| thesis_extension/calibration/instrument_strength_100rep/run_strength_calibration.R | 12 | R_source,configuration_root_paths |
| thesis_extension/calibration/instrument_strength_100rep/run_strength_calibration.R | 13 | configuration_root_paths |
| thesis_extension/calibration/instrument_strength_100rep/run_strength_calibration.R | 14 | R_source,configuration_root_paths |
| thesis_extension/calibration/instrument_strength_100rep/run_strength_calibration.R | 15 | R_source,configuration_root_paths |
| thesis_extension/calibration/instrument_strength_100rep/run_strength_calibration.R | 206 | configuration_root_paths,reporting_IO |
| thesis_extension/calibration/instrument_strength_100rep/run_strength_calibration.R | 207 | reporting_IO |
| thesis_extension/calibration/instrument_strength_100rep/run_strength_calibration.R | 209 | reporting_IO |
| thesis_extension/calibration/instrument_strength_100rep/run_strength_calibration.R | 211 | reporting_IO |
| thesis_extension/calibration/instrument_strength_100rep/run_strength_calibration.R | 212 | configuration_root_paths,reporting_IO |
| thesis_extension/calibration/instrument_strength_100rep/run_strength_calibration.R | 214 | reporting_IO |
| thesis_extension/calibration/instrument_strength_100rep/run_strength_calibration.R | 215 | configuration_root_paths,reporting_IO |
| thesis_extension/calibration/instrument_strength_100rep/run_strength_calibration.R | 249 | configuration_root_paths,reporting_IO |
| thesis_extension/diagnostics/coverage_audit/coverage_audit_functions.R | 298 | configuration_root_paths |
| thesis_extension/diagnostics/coverage_audit/coverage_audit_functions.R | 307 | configuration_root_paths |
| thesis_extension/diagnostics/coverage_audit/coverage_audit_functions.R | 316 | configuration_root_paths |
| thesis_extension/diagnostics/coverage_audit/coverage_audit_functions.R | 337 | configuration_root_paths |
| thesis_extension/diagnostics/coverage_audit/run_coverage_audit.R | 6 | configuration_root_paths |
| thesis_extension/diagnostics/coverage_audit/run_coverage_audit.R | 8 | configuration_root_paths |
| thesis_extension/diagnostics/coverage_audit/run_coverage_audit.R | 15 | R_source,configuration_root_paths |
| thesis_extension/diagnostics/coverage_audit/run_coverage_audit.R | 16 | configuration_root_paths |
| thesis_extension/diagnostics/coverage_audit/run_coverage_audit.R | 20 | R_source,configuration_root_paths |
| thesis_extension/diagnostics/coverage_audit/run_coverage_audit.R | 21 | R_source,configuration_root_paths |
| thesis_extension/diagnostics/coverage_audit/run_coverage_audit.R | 35 | configuration_root_paths |
| thesis_extension/diagnostics/coverage_audit/run_coverage_audit.R | 37 | configuration_root_paths |
| thesis_extension/diagnostics/coverage_audit/run_coverage_audit.R | 39 | configuration_root_paths |
| thesis_extension/diagnostics/coverage_audit/run_coverage_audit.R | 54 | configuration_root_paths,reporting_IO |
| thesis_extension/diagnostics/coverage_audit/run_coverage_audit.R | 55 | configuration_root_paths |
| thesis_extension/diagnostics/coverage_audit/run_coverage_audit.R | 57 | reporting_IO |
| thesis_extension/diagnostics/coverage_audit/run_coverage_audit.R | 66 | configuration_root_paths |
| thesis_extension/diagnostics/coverage_audit/run_coverage_audit.R | 67 | configuration_root_paths |
| thesis_extension/diagnostics/coverage_audit/run_coverage_audit.R | 68 | configuration_root_paths |
| thesis_extension/diagnostics/coverage_audit/run_coverage_audit.R | 69 | configuration_root_paths |
| thesis_extension/diagnostics/coverage_audit/run_coverage_audit.R | 86 | reporting_IO |
| thesis_extension/diagnostics/coverage_audit/run_coverage_audit.R | 100 | reporting_IO |
| thesis_extension/diagnostics/coverage_audit/run_coverage_audit.R | 137 | reporting_IO |
| thesis_extension/diagnostics/coverage_audit/run_coverage_audit.R | 138 | configuration_root_paths,reporting_IO |
| thesis_extension/diagnostics/coverage_audit/run_coverage_audit.R | 177 | configuration_root_paths,reporting_IO |
| thesis_extension/diagnostics/coverage_audit/run_coverage_audit.R | 179 | configuration_root_paths,reporting_IO |
| thesis_extension/diagnostics/coverage_audit/run_coverage_audit.R | 181 | reporting_IO |
| thesis_extension/diagnostics/coverage_audit/run_coverage_audit.R | 182 | configuration_root_paths,reporting_IO |
| thesis_extension/diagnostics/coverage_audit/run_coverage_audit.R | 184 | reporting_IO |
| thesis_extension/diagnostics/coverage_audit/run_coverage_audit.R | 185 | configuration_root_paths,reporting_IO |
| thesis_extension/diagnostics/coverage_audit/run_coverage_audit.R | 187 | configuration_root_paths,reporting_IO |
| thesis_extension/diagnostics/coverage_audit/run_coverage_audit.R | 189 | reporting_IO |
| thesis_extension/diagnostics/coverage_audit/run_coverage_audit.R | 190 | configuration_root_paths,reporting_IO |
| thesis_extension/diagnostics/coverage_audit/run_coverage_audit.R | 192 | reporting_IO |
| thesis_extension/diagnostics/coverage_audit/run_coverage_audit.R | 193 | configuration_root_paths,reporting_IO |
| thesis_extension/diagnostics/coverage_audit/run_coverage_audit.R | 214 | configuration_root_paths,reporting_IO |
| thesis_extension/diagnostics/coverage_audit/run_coverage_audit.R | 370 | configuration_root_paths |
| thesis_extension/diagnostics/coverage_audit/run_coverage_audit.R | 373 | reporting_IO |
| thesis_extension/diagnostics/coverage_audit/run_coverage_audit.R | 376 | configuration_root_paths |
| thesis_extension/diagnostics/coverage_audit/run_coverage_audit.R | 377 | configuration_root_paths |
| thesis_extension/diagnostics/coverage_audit/run_coverage_audit.R | 414 | configuration_root_paths,reporting_IO |
| thesis_extension/diagnostics/grid_sensitivity/grid_sensitivity_functions.R | 16 | configuration_root_paths |
| thesis_extension/diagnostics/grid_sensitivity/grid_sensitivity_functions.R | 18 | reporting_IO |
| thesis_extension/diagnostics/grid_sensitivity/grid_sensitivity_functions.R | 36 | configuration_root_paths |
| thesis_extension/diagnostics/grid_sensitivity/grid_sensitivity_functions.R | 317 | configuration_root_paths,reporting_IO |
| thesis_extension/diagnostics/grid_sensitivity/run_grid_sensitivity.R | 4 | configuration_root_paths |
| thesis_extension/diagnostics/grid_sensitivity/run_grid_sensitivity.R | 5 | configuration_root_paths |
| thesis_extension/diagnostics/grid_sensitivity/run_grid_sensitivity.R | 18 | R_source,configuration_root_paths |
| thesis_extension/diagnostics/grid_sensitivity/run_grid_sensitivity.R | 19 | configuration_root_paths |
| thesis_extension/diagnostics/grid_sensitivity/run_grid_sensitivity.R | 22 | configuration_root_paths |
| thesis_extension/diagnostics/grid_sensitivity/run_grid_sensitivity.R | 30 | configuration_root_paths |
| thesis_extension/diagnostics/grid_sensitivity/run_grid_sensitivity.R | 37 | configuration_root_paths |
| thesis_extension/diagnostics/grid_sensitivity/run_grid_sensitivity.R | 49 | R_source,configuration_root_paths |
| thesis_extension/diagnostics/grid_sensitivity/run_grid_sensitivity.R | 50 | R_source,configuration_root_paths |
| thesis_extension/diagnostics/grid_sensitivity/run_grid_sensitivity.R | 51 | R_source,configuration_root_paths |
| thesis_extension/diagnostics/grid_sensitivity/run_grid_sensitivity.R | 52 | R_source,configuration_root_paths |
| thesis_extension/diagnostics/grid_sensitivity/run_grid_sensitivity.R | 53 | R_source,configuration_root_paths |
| thesis_extension/diagnostics/grid_sensitivity/run_grid_sensitivity.R | 54 | R_source,configuration_root_paths |
| thesis_extension/diagnostics/grid_sensitivity/run_grid_sensitivity.R | 57 | configuration_root_paths |
| thesis_extension/diagnostics/grid_sensitivity/run_grid_sensitivity.R | 58 | configuration_root_paths |
| thesis_extension/diagnostics/grid_sensitivity/run_grid_sensitivity.R | 59 | configuration_root_paths |
| thesis_extension/diagnostics/grid_sensitivity/run_grid_sensitivity.R | 60 | configuration_root_paths |
| thesis_extension/diagnostics/grid_sensitivity/run_grid_sensitivity.R | 93 | configuration_root_paths |
| thesis_extension/diagnostics/grid_sensitivity/run_grid_sensitivity.R | 94 | configuration_root_paths |
| thesis_extension/diagnostics/grid_sensitivity/run_grid_sensitivity.R | 116 | configuration_root_paths |
| thesis_extension/diagnostics/grid_sensitivity/run_grid_sensitivity.R | 131 | configuration_root_paths,reporting_IO |
| thesis_extension/diagnostics/grid_sensitivity/run_grid_sensitivity.R | 140 | configuration_root_paths,reporting_IO |
| thesis_extension/diagnostics/grid_sensitivity/run_grid_sensitivity.R | 190 | configuration_root_paths |
| thesis_extension/diagnostics/grid_sensitivity/run_grid_sensitivity.R | 198 | configuration_root_paths |
| thesis_extension/diagnostics/grid_sensitivity/run_grid_sensitivity.R | 220 | configuration_root_paths,reporting_IO |
| thesis_extension/diagnostics/grid_sensitivity/run_grid_sensitivity.R | 225 | configuration_root_paths |
| thesis_extension/diagnostics/grid_sensitivity/run_grid_sensitivity.R | 226 | configuration_root_paths |
| thesis_extension/diagnostics/grid_sensitivity/run_grid_sensitivity.R | 227 | configuration_root_paths |
| thesis_extension/diagnostics/grid_sensitivity/run_grid_sensitivity.R | 229 | configuration_root_paths |
| thesis_extension/diagnostics/grid_sensitivity/run_grid_sensitivity.R | 238 | configuration_root_paths |
| thesis_extension/diagnostics/grid_sensitivity/run_grid_sensitivity.R | 243 | configuration_root_paths |
| thesis_extension/diagnostics/grid_sensitivity/run_grid_sensitivity.R | 251 | configuration_root_paths |
| thesis_extension/diagnostics/grid_sensitivity/run_grid_sensitivity.R | 255 | configuration_root_paths,reporting_IO |
| thesis_extension/diagnostics/grid_sensitivity/run_grid_sensitivity.R | 273 | configuration_root_paths |
| thesis_extension/diagnostics/grid_sensitivity/run_grid_sensitivity.R | 277 | configuration_root_paths,reporting_IO |
| thesis_extension/diagnostics/grid_sensitivity/run_grid_sensitivity.R | 279 | configuration_root_paths |
| thesis_extension/diagnostics/grid_sensitivity/run_grid_sensitivity.R | 283 | configuration_root_paths,reporting_IO |
| thesis_extension/diagnostics/grid_sensitivity/run_grid_sensitivity.R | 311 | configuration_root_paths,reporting_IO |
| thesis_extension/diagnostics/grid_sensitivity/run_grid_sensitivity.R | 312 | configuration_root_paths |
| thesis_extension/diagnostics/grid_sensitivity/run_grid_sensitivity.R | 313 | configuration_root_paths |
| thesis_extension/diagnostics/grid_sensitivity/run_grid_sensitivity.R | 315 | configuration_root_paths |
| thesis_extension/diagnostics/grid_sensitivity/run_grid_sensitivity.R | 324 | configuration_root_paths |
| thesis_extension/environment/check_author_environment.R | 1 | configuration_root_paths |
| thesis_extension/environment/check_author_environment.R | 3 | configuration_root_paths |
| thesis_extension/environment/check_author_environment.R | 5 | configuration_root_paths |
| thesis_extension/environment/check_author_environment.R | 10 | configuration_root_paths |
| thesis_extension/environment/check_author_environment.R | 11 | configuration_root_paths |
| thesis_extension/environment/check_author_environment.R | 65 | configuration_root_paths |
| thesis_extension/environment/check_author_environment.R | 68 | configuration_root_paths,reporting_IO |
| thesis_extension/environment/check_author_environment.R | 69 | configuration_root_paths |
| thesis_extension/environment/check_author_environment.R | 83 | configuration_root_paths |
| thesis_extension/environment/check_author_environment.R | 91 | configuration_root_paths |
| thesis_extension/environment/check_author_environment.R | 92 | configuration_root_paths |
| thesis_extension/final/run_final.R | 3 | configuration_root_paths |
| thesis_extension/final/run_final.R | 4 | R_source,configuration_root_paths |
| thesis_extension/final/run_final.R | 8 | R_source,configuration_root_paths |
| thesis_extension/final/run_final.R | 10 | R_source,configuration_root_paths |
| thesis_extension/final/run_final.R | 22 | configuration_root_paths,reporting_IO |
| thesis_extension/final/run_final.R | 24 | reporting_IO |
| thesis_extension/reporting/build_thesis_results.R | 16 | configuration_root_paths |
| thesis_extension/reporting/build_thesis_results.R | 18 | configuration_root_paths |
| thesis_extension/reporting/build_thesis_results.R | 23 | configuration_root_paths |
| thesis_extension/reporting/build_thesis_results.R | 24 | R_source,configuration_root_paths |
| thesis_extension/reporting/build_thesis_results.R | 25 | configuration_root_paths |
| thesis_extension/reporting/build_thesis_results.R | 30 | freeze_guard |
| thesis_extension/reporting/build_thesis_results.R | 32 | freeze_guard |
| thesis_extension/reporting/build_thesis_results.R | 33 | freeze_guard |
| thesis_extension/reporting/build_thesis_results.R | 36 | configuration_root_paths,reporting_IO |
| thesis_extension/reporting/build_thesis_results.R | 37 | configuration_root_paths,reporting_IO |
| thesis_extension/reporting/build_thesis_results.R | 38 | configuration_root_paths |
| thesis_extension/reporting/build_thesis_results.R | 39 | configuration_root_paths |
| thesis_extension/reporting/build_thesis_results.R | 41 | reporting_IO |
| thesis_extension/reporting/build_thesis_results.R | 49 | reporting_IO |
| thesis_extension/reporting/build_thesis_results.R | 50 | reporting_IO |
| thesis_extension/reporting/build_thesis_results.R | 55 | configuration_root_paths |
| thesis_extension/reporting/build_thesis_results.R | 72 | reporting_IO |
| thesis_extension/reporting/build_thesis_results.R | 74 | reporting_IO |
| thesis_extension/reporting/build_thesis_results.R | 78 | reporting_IO |
| thesis_extension/reporting/build_thesis_results.R | 79 | configuration_root_paths,reporting_IO |
| thesis_extension/reporting/build_thesis_results.R | 80 | reporting_IO |
| thesis_extension/reporting/build_thesis_results.R | 105 | configuration_root_paths |
| thesis_extension/reporting/build_thesis_results.R | 106 | configuration_root_paths |
| thesis_extension/reporting/build_thesis_results.R | 107 | configuration_root_paths |
| thesis_extension/reporting/build_thesis_results.R | 108 | configuration_root_paths |
| thesis_extension/reporting/build_thesis_results.R | 109 | configuration_root_paths |
| thesis_extension/reporting/build_thesis_results.R | 110 | configuration_root_paths |
| thesis_extension/reporting/build_thesis_results.R | 111 | configuration_root_paths |
| thesis_extension/reporting/build_thesis_results.R | 112 | configuration_root_paths |
| thesis_extension/reporting/build_thesis_results.R | 119 | configuration_root_paths |
| thesis_extension/reporting/build_thesis_results.R | 121 | configuration_root_paths |
| thesis_extension/reporting/build_thesis_results.R | 127 | configuration_root_paths |
| thesis_extension/reporting/build_thesis_results.R | 128 | configuration_root_paths |
| thesis_extension/reporting/build_thesis_results.R | 129 | configuration_root_paths |
| thesis_extension/reporting/build_thesis_results.R | 130 | configuration_root_paths |
| thesis_extension/reporting/build_thesis_results.R | 131 | configuration_root_paths |
| thesis_extension/reporting/build_thesis_results.R | 132 | configuration_root_paths |
| thesis_extension/reporting/build_thesis_results.R | 156 | reporting_IO |
| thesis_extension/reporting/build_thesis_results.R | 166 | configuration_root_paths,reporting_IO |
| thesis_extension/reporting/build_thesis_results.R | 167 | configuration_root_paths,reporting_IO |
| thesis_extension/reporting/build_thesis_results.R | 173 | configuration_root_paths,reporting_IO |
| thesis_extension/reporting/build_thesis_results.R | 174 | configuration_root_paths,reporting_IO |
| thesis_extension/reporting/build_thesis_results.R | 176 | configuration_root_paths,reporting_IO |
| thesis_extension/reporting/build_thesis_results.R | 177 | configuration_root_paths |
| thesis_extension/reporting/build_thesis_results.R | 180 | configuration_root_paths,reporting_IO |
| thesis_extension/reporting/build_thesis_results.R | 181 | configuration_root_paths |
| thesis_extension/reporting/build_thesis_results.R | 187 | configuration_root_paths,reporting_IO |
| thesis_extension/reporting/build_thesis_results.R | 188 | configuration_root_paths |
| thesis_extension/reporting/build_thesis_results.R | 192 | configuration_root_paths,reporting_IO |
| thesis_extension/reporting/build_thesis_results.R | 193 | configuration_root_paths |
| thesis_extension/reporting/build_thesis_results.R | 196 | configuration_root_paths |
| thesis_extension/reporting/build_thesis_results.R | 197 | configuration_root_paths,reporting_IO |
| thesis_extension/reporting/build_thesis_results.R | 202 | configuration_root_paths,reporting_IO |
| thesis_extension/reporting/build_thesis_results.R | 209 | configuration_root_paths,reporting_IO |
| thesis_extension/reporting/build_thesis_results.R | 211 | configuration_root_paths,reporting_IO |
| thesis_extension/reporting/build_thesis_results.R | 214 | configuration_root_paths,reporting_IO |
| thesis_extension/reporting/build_thesis_results.R | 216 | configuration_root_paths,reporting_IO |
| thesis_extension/reporting/build_thesis_results.R | 261 | reporting_IO |
| thesis_extension/reporting/build_thesis_results.R | 266 | reporting_IO |
| thesis_extension/reporting/build_thesis_results.R | 268 | reporting_IO |
| thesis_extension/reporting/build_thesis_results.R | 282 | reporting_IO |
| thesis_extension/reporting/build_thesis_results.R | 284 | reporting_IO |
| thesis_extension/reporting/build_thesis_results.R | 343 | reporting_IO |
| thesis_extension/reporting/build_thesis_results.R | 350 | reporting_IO |
| thesis_extension/reporting/build_thesis_results.R | 355 | reporting_IO |
| thesis_extension/reporting/build_thesis_results.R | 365 | reporting_IO |
| thesis_extension/reporting/build_thesis_results.R | 375 | reporting_IO |
| thesis_extension/reporting/build_thesis_results.R | 378 | reporting_IO |
| thesis_extension/reporting/build_thesis_results.R | 379 | reporting_IO |
| thesis_extension/reporting/build_thesis_results.R | 380 | reporting_IO |
| thesis_extension/reporting/build_thesis_results.R | 381 | reporting_IO |
| thesis_extension/reporting/build_thesis_results.R | 382 | reporting_IO |
| thesis_extension/reporting/build_thesis_results.R | 428 | configuration_root_paths,reporting_IO |
| thesis_extension/reporting/build_thesis_results.R | 431 | configuration_root_paths,reporting_IO |
| thesis_extension/reporting/build_thesis_results.R | 433 | configuration_root_paths,reporting_IO |
| thesis_extension/reporting/build_thesis_results.R | 435 | configuration_root_paths,reporting_IO |
| thesis_extension/reporting/build_thesis_results.R | 438 | configuration_root_paths,reporting_IO |
| thesis_extension/reporting/build_thesis_results.R | 445 | configuration_root_paths,reporting_IO |
| thesis_extension/reporting/build_thesis_results.R | 531 | reporting_IO |
| thesis_extension/reporting/build_thesis_results.R | 547 | reporting_IO |
| thesis_extension/reporting/build_thesis_results.R | 575 | reporting_IO |
| thesis_extension/reporting/build_thesis_results.R | 587 | reporting_IO |
| thesis_extension/reporting/build_thesis_results.R | 588 | reporting_IO |
| thesis_extension/src/run_extension.R | 3 | reporting_IO |
| thesis_extension/src/run_extension.R | 119 | reporting_IO |
| thesis_extension/src/run_extension.R | 120 | reporting_IO |
| thesis_extension/src/run_extension.R | 121 | configuration_root_paths,reporting_IO |


Retaining paths does NOT resolve build_thesis_results.R's hard-coded ac9a9cca expected_commit guard or nonempty-output prohibition. New repository HEAD cannot equal that commit. R 3.4.3/library precedence, Windows paths and worker penalty RNG limitations also remain. Any future portable reporting adapter must be separately versioned, reviewed and write elsewhere; do not bypass guards in the archived generator. No research code was changed.

## 6. Conditions before staging

1. Confirm the proposed base package's evidence-inspection scope; refrain from full replay claims unless every missing numerical prerequisite is verified and separately enumerated.
2. Accept explicit mismatch disclosure or locate authentic expected-byte backups with provenance. Never replace historical manifests silently.
3. Resolve upstream wrapper redistribution rights, manuscript/coauthor and asset permissions, result-data licensing and intended public contacts.
4. Prepare later reviewed README, availability, provenance/notices and environment publication copies; current rows are source candidates, not cleared uploads.
5. If historical Stage 2F source is later recovered, verify listed blob/SHA256 and the exact_bounds import; do not reconstruct saved outputs.
6. Stage only approved rows in a future authorized step, retaining exact source-hash/path mapping. Holds and exclusions do not travel automatically.

## Verification and restrictions

Only the five requested G2 outputs were created. No simulation, estimator, diagnostic, statistical validation, manuscript build, scientific-result change, migration, deletion, history rewrite, repository creation, commit, push, release or submission occurred. Hashing and static inspection are file-integrity work only.

Final decision: **CONDITIONAL**.

## Final path-reference and selection check

All existing journal_article file paths explicitly cited in D_evidence_map.tex are proposed, including presentation tables/images outside the 32-file build closure. Additional cited assets selected: journal_article/figures/generated/rmse_n1000.png, journal_article/figures/generated/rmse_n500.png, journal_article/tables/generated/appendix_coverage.tex, journal_article/tables/generated/appendix_cr_informativeness.tex, journal_article/tables/generated/appendix_point_performance.tex, journal_article/tables/generated/appendix_power.tex.

Moving journal_article/ requires changing printed manuscript paths as well as future build instructions. The retained research paths are deliberate; no referenced file is renamed in G2. If no source adaptation is authorized for initial staging, retain journal_article/ as well and defer the manuscript/ mapping. The CSV mapping is a proposed later destination, not a claim that all printed paths already match it.

| Decision | Rows |
|---|---|
| EXCLUDE_FROM_BASE_PACKAGE | 63 |
| HISTORICAL_SOURCE_HOLD | 4 |
| OPTIONAL_HISTORICAL_ARCHIVE | 6 |
| PROPOSED_INCLUDE | 137 |
