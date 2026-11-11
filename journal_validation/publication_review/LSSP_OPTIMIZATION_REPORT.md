# LSSP manuscript and appendix optimization proposal

11 November 2026, Asia/Tashkent. Repository: DML-IVQR_Master_Thesis. Target: Communications in Statistics – Simulation and Computation.

## Decision and scope

This is a separate, reviewable proposal. **Do not replace the canonical manuscript until the authors approve it.** No canonical source, abstract, author identity, research script, dataset or archived result is intentionally changed. No simulation, estimator, statistical test or numerical research validation is run. All calculations in the helper scripts concern document integrity, source comparison or PDF layout, not research results.

The contribution remains a descriptive, controlled instrument-relevance sensitivity experiment for three preserved implementations. It is not recast as a new estimator, an inference theorem, a causal isolation of regularization, or validation of nominal chi-square inference. No arbitrary page target guided the changes.

## Deliverables and reading order

All proposed files are under `journal_validation/publication_review/lssp_optimization/`.

| Deliverable | Location | Purpose |
|---|---|---|
| Complete pre-edit necessity plan | `CONTENT_OPTIMIZATION_PLAN.md` | Item-level original locations, classifications, justifications, destinations and impact; exact proposed original/replacement passages. Produced before revised sources. |
| Complete machine-readable item inventory | `CONTENT_ITEM_MAP.json` | Full original text and line spans of every inventoried paragraph, mathematical block, display and structural item, including existing non-input assets. |
| Proposed named main PDF | `manuscript_optimized.pdf` | Main manuscript with optimized Appendices A–D still inline. |
| Accompanying technical PDF | `technical_supplement.pdf` | Original detailed domain-diagnostic Tables A.2–A.5, unchanged scientific entries and original numbering. Must accompany the proposed main PDF. |
| Complete proposed LaTeX/dependency tree | `source/` | Independent copies of source, bibliography, tables and figures; new `technical_supplement.tex` supplies the separate technical document. |
| Full before/after source diff | `BEFORE_AFTER_SOURCE.diff` | Every canonical-to-proposal textual change, including newly split table dependencies. |
| Complete combined text diff | `BEFORE_AFTER_COMPLETE_TEXT.diff` | Original PDF against proposed main PDF, technical PDF and relocated inventory; line-wrap noise remains visible. |
| Rendered text diff | `BEFORE_AFTER_PDF_TEXT.diff` | Original 34-page PDF against optimized main PDF; pagination/line-wrap changes also appear. Relocated tables are available in the separate technical PDF. |
| Retention/deletion map | `CONTENT_RETENTION_MAP.md` | Change-by-change destination and impact; full unchanged-item coverage is in the necessity plan/JSON. |
| Full relocated evidence inventory | `EVIDENCE_INVENTORY.md` | E1–E6 locators and administrative provenance, supplied with the proposal rather than silently assumed publicly available. |
| Verbatim original inventory | `EVIDENCE_INVENTORY_ORIGINAL.tex` | Original full E1–E6 source preserved for exact inspection. |
| Scientific integrity audit | `SCIENTIFIC_INTEGRITY_AUDIT.md`, `qa/scientific_integrity.json` | Actual preservation and document-build evidence, with limits. |
| Reproducible document-only helper | `optimize_documents.py` | Separate plan, prepare, build and verify stages; no research invocation. |

## Necessity audit and editorial decisions

The plan inventories **340 source items**: prose blocks, mathematical displays, tables/figures including captions/notes, algorithm steps and structural elements. Display-separated prose is split at the display; the mathematical argument is evaluated as an ordered whole. Existing unused table/figure wrappers are inventoried and preserved as available assets, not inserted into the new manuscript. Exact original passages remain in JSON and the edit register.

Thirty-three exact changes are proposed. No scientific item is classified REMOVE: all substantively useful content is retained, condensed or relocated. The braced pre-abstract summary is classified DUPLICATE and removed; its information is already in the protected title and abstract. The classifications are necessity judgments, not quotas requiring a deletion in each category.

### Sections 1–6

- **Introduction:** retain the research question, distribution-preserving relevance construction, comparison design and inferential scope. Replace the early exact ranking count and repeated Oracle finding with a short preview; full counts, examples and interpretation remain in Results and Discussion. Replace an early detailed randomization explanation with a pointer to the full definitions in §3.2.
- **Framework:** retain every mathematical display, the ideal-versus-executable distinction, non-finite-density finding and all implementation details. Clarify that the selected grid candidate minimizes stored statistics; this is not an assertion of exact nuisance optimization. Condense a repeated inference-theory qualification while retaining the cross-fitting caveat explicitly.
- **Design:** preserve its full specification and all original equations. The kappa settings, sample sizes, quantiles, replications, bias convention, direct truth/false-candidate tests, grid, trapezoidal measure, failure policy and separate diagnostic scope remain unchanged.
- **Results:** preserve all numerical findings, comparison counts, counterexamples and supporting displays. Remove the repeated OLS regression specification from §4.1 because §3.2 already specifies it. Remove one redundant closing summary in §4.2. Qualify the larger-sample statement as an observed Monte Carlo RMSE comparison. Clarify coverage terminology locally and place the independence assumption next to the conventional Monte Carlo standard error and pointwise interval discussion. Describe accepted-measure changes without continuous-domain or isolated-mechanism implications.
- **Discussion:** retain the central synthesis, Oracle interpretation, implementation-comparison limits, numerical sensitivity, practical implications and DGP scope. Remove a repeated RMSE/calibration sentence and replace another full ranking/differences inventory with a short statement; its following no-mechanism/no-superiority sentence remains.
- **Conclusion:** retain the construction and central acceptance-versus-discrimination conclusion. Remove another Oracle sentence and replace the full repeated limitation inventory with a Discussion pointer. Explicit disclaimers about implemented orthogonality, chi-square validity, theoretical robustness, numerical certificates, historical decisions, unrestricted geometry and absence of a demonstrated correction remain.

### Appendix A

Keep the common-domain justification, all-domain interpretation, key full domain-measure table A.1, expansion figure and **exact failed-evaluation disclosure** inline. Retain the failure identifiers, missing aggregate policy, 99-versus-100 usable profiles, Stage 2 error statement and boundary/global-geometry qualifications. Correct the continuous-domain acceptance overstatement.

Move Tables A.2–A.5 to the accompanying Technical Supplement. These contain incremental measures, endpoint/full-grid frequencies, profile/error counts and stabilization diagnostics. They provide detailed verification across the same cells rather than a new main contribution. Their table blocks, captions, numerical entries and notes are unchanged; their numbers remain A.2–A.5. The main PDF names the separate document explicitly instead of leaving unresolved cross-document references. The technical PDF repeats the failure and interpretation conventions so it can be inspected independently.

This relocation reduces immediate inline detail but **does not reduce the available evidence if the technical PDF is supplied**. Omitting that PDF from author review or eventual submission would weaken inspectability and is not the proposed delivery.

### Appendix B

Preserved **byte-for-byte**. The complete compensating-noise derivation, normality-dependent distributional invariance, covariance relations, structural-quantile argument, conceptual endpoint and variance-allocation table remain inline. No mathematical conclusion or explanatory step is shortened.

### Appendix C

Retain the direct-at-truth definition, all existing audit counts, pointwise Wilson interpretation, absence of missing/nonfinite statistics, summary table and full-grid heatmap. Remove only a generic repository-preservation sentence, a repeated sentence excluding already-specified numerical explanations and a repeated central interpretation of truth retention versus false-candidate exclusion. Preserve the separate-evaluation/fresh-draw distinction and the fact that full-grid acceptance concerns 41 evaluated values, not the real line. No interval or audit statistic is recalculated.

### Appendix D

Retain the environment/package versions, seeds and worker-stream limits; full evaluation sequence; penalties/objectives; fitted-normal variance-as-scale proxy; residualization/intercept differences; finite solver and last-used penalty definitions; five-of-24 selected-case decision discrepancy; fixed-objective certificate limits; mixed-density argument and conditional score algebra. These are scientifically necessary and remain inline.

Relocate the long E1–E6 path inventory and duplicated administrative archive/check descriptions to `EVIDENCE_INVENTORY.md`. Preserve the original inventory verbatim as an additional `.tex` file. Keep the compact claim/key table, a description of every key and an explicit inventory location in the PDF. Retain public-versus-local exclusions, the unresolved freeze record and lack of portable/exact replay in the main availability statement. Historical check counts survive in the inventory as archival context, not claims that this revision reran them. This is a real evidence-access dependency: supply the inventory with both PDFs; its new repository path is not asserted to be a verified public deposit.

## Previously identified corrections

| Audit item | Proposal implementation |
|---|---|
| M1 | Appendix A now describes a near-maximum trapezoidal grid summary, not acceptance of almost the entire continuous interval. |
| M2 | Availability and compact evidence map no longer claim the present manuscript is uncommitted. D.1 points to the availability record instead of repeating stale Git-status wording. The verbatim historical inventory remains clearly identified as historical. |
| M3 | Results describes observed Monte Carlo RMSE. The standard-error statement and uncertainty discussion explicitly condition on independent replications and acknowledge unverified DML worker-stream independence. Formulas and existing intervals are unchanged. |
| E1 | §4.3 heading/opening and Table 2's prose note identify direct-at-truth acceptance. Historical column names, equations and figure artwork remain intact. |
| E2 | §4.5 describes observed median grid-acceptance changes and the investigated larger-sample comparison, without a claim about a separately identified mechanism. |
| E3 | §2.2 says the first candidate attaining the minimum stored grid statistic is selected. |

The starting canonical files still contained these issues; each is applied once to the proposed copy. No wholesale terminology substitution is made. Detailed exact replacements and original locations are in the pre-edit plan.

## Page counts and verification

Build and inspection results are recorded in `qa/build_results.json` and `qa/scientific_integrity.json`. Both documents built successfully. The final counts are **29 pages in the optimized main PDF (including A–D), plus 5 pages in the Technical Supplement**, versus 34 pages in the original named PDF. The combined PDF page count is therefore still 34; this is principally better placement of verification material, with modest prose compression, not a claim of five pages of deleted science. The full Markdown evidence inventory is additional supplied material. All 34 proposed pages were inspected in contact sheets; no evident cropped or missing displays were found. A reduction in the main PDF must be read together with the separate technical PDF and repository inventory; it is not all deletion of content.

## Remaining unresolved issues

1. **Author approval:** this is a proposed copy. Canonical replacement is not authorized until the authors review and approve the concrete artifacts.
2. **Current LSSP format rules:** the preceding content audit documents indexed official single-anonymous review, an accessible but apparently historical publisher instructions PDF, and an inaccessible live instructions endpoint. This workflow does not newly verify the portal. Do not retain the old JSCS double-anonymity gate as an LSSP requirement. Confirm abstract limits, page-count basis, supplement treatment, source upload and current title-page/reference requirements. The protected abstract is unchanged even if a journal-rule conflict requires a later author decision.
3. **Evidence delivery:** the technical PDF and full inventory must accompany the proposal and remain available to reviewers. No new public repository deposit or journal reviewer-access mechanism is created. The previously checked public evidence revision is not a claim that this new proposal is publicly accessible.
4. **Historical reproducibility:** missing main-run worker penalty states, local-only profiles/primitives and Stage 2H outputs, unresolved historical freeze identifier and runtime portability limits remain. The proposal does not repair them or promise full replay.
5. **Inference validity:** the true mixed density is non-finite and ideal regularity is not established for the executable implementation. The nominal chi-square rule remains unvalidated. Lack of cross-fitting alone is not proof of invalidity. No correction is demonstrated to restore calibration.
6. **Numerical sensitivity:** the five-of-24 policy discrepancy remains a selected-panel finding, not a full-experiment error rate. Historical numerical decisions are not universally certified or replaced.
7. **AI declarations:** existing author attestations remain unchanged. Accurate disclosure and current publisher compliance require author confirmation of the actual assistance history; document integrity checks cannot retrospectively establish it.

## Scientific assessment

The proposed manuscript retains the complete defensible contribution **when read with its supplied technical supplement and evidence inventory**. Its design, estimator definitions, mathematical arguments, empirical findings and material limitations are preserved. The local acceptance/geometry wording and uncertainty language are more precise. Removing repeated previews and limitation inventories does not strengthen the claims or hide inconvenient evidence.

It remains potentially suitable for consideration as a descriptive Monte Carlo sensitivity study, with a narrow scope tied to the specified DGP and historical implementations. This is not certification of statistical validity, reproducibility on another system, universal method rankings or journal acceptance. Final submission readiness remains conditional on author review, actual delivery of relocated materials and resolution of journal-specific requirements. No commit, push, release, publication or submission is performed.


## Completed verification

All seven document-build steps exited zero. Final logs contain no undefined/multiply-defined scientific references or citations and no overfull boxes; PDF text has no unresolved `??` placeholders. SHA-256 checks found no changes to 192 protected document dependencies/research scripts; Git confirms all tracked canonical files and datasets remain unchanged. The abstract and title/author/metadata text match; Appendix B is byte-identical; every original displayed mathematical block, scientific table body and relocated table block is unchanged. Figures and bibliography remain byte-identical. All original scientific label numbers remain the same across the two PDFs, and citation keys are preserved. These checks establish document preservation, not statistical validity. See `lssp_optimization/SCIENTIFIC_INTEGRITY_AUDIT.md` for exact scope and limitations.
