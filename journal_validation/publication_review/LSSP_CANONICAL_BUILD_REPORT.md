# Corrected canonical journal manuscript: document build

Date: 11 November 2026 (Asia/Tashkent). Branch: `journal-validation`.

## Scope and preserved master

The master is the complete current canonical `journal_article/main.tex` dependency tree, including the previously approved M1–M3 and E1–E3 prose corrections. The cancelled optimization is not adopted. Sections 1–6 and Appendices A–D remain complete and inline; the full Appendix A tables and E1–E6 evidence inventory are included. No content is shortened or relocated, and the approved title, author details and abstract are preserved.

A byte-identical source snapshot is staged under `journal_validation/publication_review/lssp_canonical_build/source/`. Build intermediates and QA remain in that separate directory. The new PDF is `journal_validation/publication_review/lssp_canonical_build/manuscript_canonical_corrected.pdf`. No canonical source or historical PDF is overwritten.

## Document-only method

The helper `lssp_canonical_build/build_canonical.py` runs pdfLaTeX, Biber, pdfLaTeX and pdfLaTeX, with automatic installation and TeX shell escape disabled. The recorder captures actual input dependencies. It uses the already initialized local MiKTeX runtime; PDF text extraction and page rendering are document-inspection steps. No simulation, estimator, statistical test or numerical research validation is run. Research scripts, datasets, statistical results and figure assets are not edited.

Commands, exit codes and durations are recorded in `lssp_canonical_build/qa/build_results.json`; final source and PDF checks are in `qa/verification.json`. Source hashes, existing PDF hashes, original tracked-file diff, final logs, extracted text and rendered contact sheets are retained in the same QA directory. Reproduce from the repository root using `python -B journal_validation/publication_review/lssp_canonical_build/build_canonical.py build`, then `audit`, then `render` in place of `build` as the final argument. This is a local document workflow, not a portable research runtime guarantee.

## Final results

**PASS ? complete corrected canonical manuscript compiled successfully, 34 pages.**

| Artifact | Result |
|---|---|
| Rebuilt PDF | `lssp_canonical_build/manuscript_canonical_corrected.pdf` |
| Page count | **34** |
| Bytes | **1,014,572** |
| SHA-256 | `4e9800270d35afd6332abe109bae7eb6fce4a0d8bdb24cbebef30370fc088e7b` |
| Build sequence | pdfLaTeX ? Biber ? pdfLaTeX ? pdfLaTeX; all four exit codes 0 |
| Scientific label consistency | **72 unchanged labels/numbers: 58 equation labels, 9 numbered tables, 5 numbered figures** |
| Citations | All **9 distinct cited keys** resolve in the compiled bibliography |
| Dependency verification | **25 recursive TeX inputs** and **6 graphic files** recorded as actual build inputs |
| Canonical preservation | **39 staged dependencies** byte-identical to canonical files before/after build |
| Historical PDF preservation | All **18 pre-existing PDFs** under `journal_article/` retain their pre-build SHA-256 |
| Abstract | Verbatim against historical canonical source; no abstract edit |
| Final warnings affecting references/layout | None: no undefined/multiply-defined references, unresolved citations, stale rerun requests, overfull/underfull boxes or literal `??` placeholders |
| Visual review | All **34 pages** reviewed in rendered grayscale contact sheets; no evident cropped/missing displays or blank pages |

Displayed mathematics and scientific table bodies match the historical source. All scientific label numbers match the original named build; the full inline diagnostic tables are present. The compact claim-to-evidence table and complete inventory remain inline as well. Recorder evidence confirms that no cancelled optimization sources or split-table dependencies were used.

The original named historical PDF remains at `journal_article/submission/named/manuscript_named.pdf`, unchanged at **34 pages**, SHA-256 `4fecad9e125211689910104b8b533cb5e03f1d96e24752dc58bb62b5e77e3388`. The newly rebuilt PDF is a separate artifact representing the corrected canonical sources.

The only final LaTeX package warning is `Package epstopdf Warning: Shell escape feature is not enabled.` Shell escape was intentionally disabled; all required PDF/PNG graphics were read successfully, so no EPS conversion was needed. MiKTeX also emits its existing update-maintenance notice. Neither prevented compilation; no installer, package update or global repair was run.

The initial QA helper needed a narrower error-message pattern (to avoid treating package descriptions as errors) and decoding for localized `pdfinfo` metadata. Those document-inspection issues were corrected; final QA passed without changing or recompiling manuscript content. Contact-sheet inspection is not a new full-resolution typographic or statistical certification.

## Verification scope

- Every staged canonical dependency must match its source hash before and after compilation; the existing tracked working-tree diff must remain unchanged.
- The abstract must match the historical canonical source verbatim, allowing only Git newline normalization when comparing source representations.
- All displayed equations and scientific table bodies must match the historical canonical source. Scientific equation/table/figure labels and their numbering must match the historical named build.
- Every recursively referenced TeX input and graphic must appear in the recorder; no cancelled optimization source is used.
- Citation keys must resolve to bibliography entries; final logs must have no unresolved citations, references, duplicate definitions or stale rerun requests. Rendered PDF text must contain no unresolved `??` placeholders.
- Existing historical PDFs must preserve their pre-build SHA-256 hashes.

These are preservation, typesetting and reference-resolution checks. They do not independently establish mathematical truth, the correctness of cited literature or reported statistics, or statistical inference validity.

## Remaining issues and limits

The manuscript's scientific qualifications remain intact: the mixed-density regularity limitation, unestablished nominal chi-square validity, implementation/residualization differences, same-sample nuisance fitting, penalty-stream reproducibility limits and selected-case numerical decision sensitivity are not repaired by document compilation. No missing historical freeze identifier or public-data access mechanism is resolved here. Current journal portal requirements, any abstract/page-limit interpretation and author disclosure confirmations remain outside this build task.

No commit, push, publication or submission is performed. The previous 29-page proposal and separate 5-page supplement remain archival records only.


## Final working-tree status

The tracked diff is exactly the pre-build diff: the seven previously approved M1?M3 / E1?E3 LaTeX corrections remain uncommitted. This build adds only a separate document-build directory and this report; earlier review/archival files remain untracked. No staged changes.

```text
 M journal_article/sections/02_framework.tex
 M journal_article/sections/04_results.tex
 M journal_article/sections/data_availability.tex
 M journal_article/supplementary/A_numerical_domain.tex
 M journal_article/supplementary/D_evidence_map.tex
 M journal_article/supplementary/D_implementation.tex
 M journal_article/tables/table_main_performance.tex
?? journal_validation/publication_review/LSSP_CANONICAL_BUILD_REPORT.md
?? journal_validation/publication_review/LSSP_CANONICAL_CORRECTIONS_REPORT.md
?? journal_validation/publication_review/LSSP_CONTENT_AUDIT.md
?? journal_validation/publication_review/LSSP_OPTIMIZATION_REPORT.md
?? journal_validation/publication_review/lssp_canonical_build/
?? journal_validation/publication_review/lssp_optimization/
```
