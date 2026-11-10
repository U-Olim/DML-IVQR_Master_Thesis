# AI-use provenance audit

**Date:** 10 November 2026 (Asia/Tashkent)
**Repository / branch:** `DML-IVQR_Master_Thesis` / `journal-validation`
**HEAD inspected:** `0f4188ca98a45ba03e1c889ac705ec936369862a` plus the existing uncommitted final-package changes.
**Conclusion:** AI-assisted revision and new documentation drafting are documented. Human-only origin of the earliest drafts, complete historical AI scope, exact tool versions and publisher-required author attestations remain UNVERIFIED. No misconduct or compliance verdict is inferred from a human Git author name, substantial editing, or an incomplete record.

This audit creates this report and the accompanying `SUBMISSION_GATE_REPORT.md` only. It does not change the disclosure in the manuscript, execute research/diagnostic programs, rebuild a document or create a deposit. This report itself is new AI-assisted documentation, not a contemporaneous human attestation about earlier work.

## 1. Evidence classes and limits

1. **Git objects inspected directly:** establish the existence and content of files at recorded commits. Commit dates need not be composition dates; the committer is not proof of who drafted each sentence or whether AI was used.
2. **Retained change reports:** show exact earlier/revised passages and described scope. Their dates and preservation statements are documentary records, not independent transcripts of every action.
3. **Visible Codex conversation/tool history for this work:** establishes actual AI assistance in the observed editorial/document-production passes, including full paragraph rewrites and document helper creation. The full chat/application export is not retained as a versioned repository artifact.
4. **Author declarations:** establish what the authors have stated about grammar, translation and research-code scope. They are not independent verification of those historical facts.

No private ChatGPT history, pre-AI author draft archive, original-language/translated version pair, complete historical tool log or reliable tool/model-version ledger was found in the inspected records. Their absence here does not establish that authors cannot supply them.

## 2. What existed before the documented Stage 2I editorial work

| Evidence checkpoint | Existing material | Defensible inference |
|---|---|---|
| `e864dd27`, 17 September 2026, `Initial commit.` | `thesis/main.tex`; `thesis/sections/01_introduction.tex`, `02_background_literature.tex`, `03_methodology.tex`, `04_simulation_design.tex`, `05_results.tex`, `07_conclusion.tex`; extension wrappers/design/metrics under `thesis_extension/src/`. | Substantial thesis prose and executable research material predate the visible Stage 2I revisions. Their initial composition and AI provenance are not established by this commit. |
| `90509cbd`, 22 October 2026, `First check.` | `journal_article/main.tex` with an abstract; all six journal section files; supplementary A?D. Direct inspection of the introduction/conclusion shows a pre-existing controlled relevance study narrative and limitations. | All principal journal sections existed before the November Stage 2I edits. It is incorrect to describe those edits as starting from an empty manuscript. It is also incorrect to certify these earlier texts as human-only. |
| `journal_article/EDIT_REPORT.md`, first tracked in `90509cbd`, internally dated 15 October 2026 | Records an earlier 58-to-28-page conversion/revision, author presentation and appendix truncation. | Evidence of an earlier document state; its internal date precedes first tracking. The conversion's prompts, tool and original drafter are not established. |
| `15b8b4dc`, 9 November 2026, `Stage 2` | Round 1 audit and Batch 1/2 reports and manuscript revisions. | Earlier/revised paragraph pairs are available. This is not a tool-version or human-review certificate. |
| `0f4188ca`, 10 November 2026, `final simulations.` | Retains later Stage 2I manuscript/report/checklist work. | The broad commit subject does not prove a simulation was run in this session or establish AI authorship of research code. |
| Current uncommitted final package, 10 November 2026 | Confirmed author/declaration updates, named/review PDF builds, provenance masking, source/data ZIPs and document QA. | Directly observed Codex document preparation; no research computation was executed in these final editorial/package passes. |

First tracked journal section paths, all added in `90509cbd`:

- Abstract: `journal_article/main.tex`.
- Introduction: `journal_article/sections/01_introduction.tex`.
- Framework: `journal_article/sections/02_framework.tex`.
- Design: `journal_article/sections/03_design.tex`.
- Results: `journal_article/sections/04_results.tex`.
- Discussion: `journal_article/sections/05_discussion.tex`.
- Conclusion: `journal_article/sections/06_conclusion.tex`.
- Appendices: `journal_article/supplementary/A_numerical_domain.tex`, `B_kappa_derivation.tex`, `C_coverage_audit.tex`, `D_implementation.tex`.

**Meaning of ?before AI-assisted editing?:** these files predate the *documented/observed November editorial passes*. There is no proven ?before all AI use? checkpoint in the inspected history. Human authorship of the source material requires the authors' original drafts/records, not an inference from file age.

## 3. Revision activity and drafting classification

| Phase / retained evidence | Documented activity | Classification and uncertainty |
|---|---|---|
| Early thesis and thesis-to-journal conversion; September/October checkpoints and `EDIT_REPORT.md` | Existing thesis sections and complete journal article; earlier conversion/layout reduction. | Original drafting/conversion attribution UNVERIFIED. No categorical claim of AI first-draft generation or human-only drafting. |
| Batch 1, report dated 9 November: `BATCH1_CHANGE_REPORT.md` | Narrows inference/regularization claims, separates direct-truth/grid objects and adds numerical sensitivity disclosure. | Revision of existing material and new explanatory wording. Git/report alone do not identify every editing tool; do not retroactively assign all Batch 1 text to a model. |
| Batch 2, 9 November state and 10 November follow-up: `BATCH2_CHANGE_REPORT.md`, exact original/revised blocks | Abstract, introduction and conclusion rewritten around existing design/results; title alternatives; visible follow-up adds the Gaussian qualification. The conversation records Codex involvement in the revision workflow. | Substantial redrafting of existing prose, not evidence that AI created the original paper. Exact model/version and a complete earlier-session transcript are missing. |
| Batch 3, 10 November: `BATCH3_CHANGE_REPORT.md`, exact changed spans/diff | Operational availability statement, evidence map, evaluation sequence, finite-solver description and retained density-divergence exposition; sample/draw distinction. | Observed Codex drafting of **new documentation passages** from retained scientific/evidence records, as well as revision. These new passages had no identical prior prose; calling all activity grammar-only would understate it. This does not establish AI authorship of the original manuscript, new results or a new theorem. |
| Batch 4, 10 November: `BATCH4_CHANGE_REPORT.md` | Redrafts discussion/conclusion, tightens abstract/introduction/framework, clarifies notation/grid language, prepares declaration placeholders and README; document build/inspection helper. | Observed editing/redrafting of existing article and new document-production material. Explicit author facts were left for confirmation. |
| Final checklist and final packaging, 10 November: `FINAL_SUBMISSION_CHECKLIST.md`, `FINAL_PACKAGE_REPORT.md`, visible tool history | Consolidates author/access checklist; applies user-confirmed facts and declarations; creates review presentation, packaging/audit helpers, CSV inventory and table-only wrapper. | New AI-assisted administrative/documentation drafts and document utilities; existing science/assets preserved. These are not ?no AI-generated code of any kind? activities, but are distinct from research estimator/simulation code. |
| Grammar and translation in ChatGPT/OpenAI Codex | Authors expressly declare those uses. | Author-reported scope. Specific translations, language pairs, dates, versions and responsible human translation checker are not independently documented here. |
| Current gate reports | AI-assisted audit and report drafting from existing records. | New report first drafts; not manuscript-result generation or retrospective author attestations. |

Evidence anchors: `BATCH2_CHANGE_REPORT.md`, ?Exact modification log?; `BATCH3_CHANGE_REPORT.md`, ?Analytical and implementation sources? and exact wording/diff; `BATCH4_CHANGE_REPORT.md`, editorial/build sections and complete diff; `FINAL_PACKAGE_REPORT.md`, Sections 1, 3, 7?10. These preserve before/after content rather than merely asserting language polishing.

**First-draft finding:** new availability/reproducibility/evidence-map and administrative prose was drafted with Codex from existing records. Whether AI drafted the original thesis/journal article, or particular earlier core passages, remains UNVERIFIED. The volume of revision is not used as a test for original first-draft generation. Authors must classify the earlier history using original drafts and interaction records.

## 4. Research-code declaration versus repository history

Current declaration: `journal_article/sections/submission_declarations.tex:8` attributes grammar/translation/editing/documentation assistance and states, **according to the authors**, no AI development/modification of research code, simulations or statistical analysis.

**No proven contradiction is established in the visible final editorial/package work.** The observed AI-created Python files `journal_article/qa/batch4/build_document.py` and `journal_article/submission/{prepare_and_build.py,audit_packages.py}` perform document assembly, builds, source/byte checks and PDF inspection. They are AI-written code, but not research estimators or simulation/statistical-analysis programs. A broader claim that AI wrote *no code at all* would be false; the actual limited research-code claim must not be silently expanded to that claim.

**The historical blanket exclusion is not verified.** Concrete research/diagnostic additions that need attribution include:

| Repository evidence | Why author confirmation is necessary |
|---|---|
| `e864dd27`: `thesis_extension/src/{author_bc_dml_wrapper.R,author_oracle_wrapper.R,dgp_kappa.R,metrics.R,run_extension.R}` | Research/DGP/evaluation/summary code existed at first tracking, with no pre-AI authoring ledger. |
| `d4897232`, 29 October 2026: `journal_validation/stage2a/diagnostic_functions.R`, `run_diagnostics.R`, `summarize.R`; Stage 2B diagnostic/summary programs | Existing reports describe changed diagnostic variants and actual evaluations. Preservation of frozen canonical wrappers is not proof that AI was absent from *new diagnostic code*. |
| Later Stage 2C?G numerical/certification tools | Their new code and record generation are separate from preserving historical estimator outputs. Scope/AI authorship must be checked if the authors' declaration is intended to cover the entire research program. |
| `2ceec58a`, 9 November: `journal_validation/stage2h/pilot/{calibrate_original.R,candidate_h0.py,prepare_pilot.R,run_pilot.py,...}` and retained pilot reports | Pilot/adaptor/analysis code exists; creation and AI role cannot be inferred from the human committer or a statement that manuscript results were unchanged. |

Stage 2A's report mentions an `AGENTS` search at line 295; Stage 2C does so near line 32. These are leads suggesting a coding-agent workflow, **not sufficient proof of a particular tool, AI-written algorithm, or a contradiction**. Git author metadata and report-writing style cannot resolve the issue.

Required scope check: authors must explicitly include or exclude, with accurate reasons, canonical simulation code, extension wrappers, diagnostic variants, numerical validation/certification, Stage 2H pilot/adaptor code and statistical/reporting scripts. If AI assisted any of those research activities, the research-code/analysis exclusion needs correction before submission, even if frozen published numbers were unchanged. This audit does not make that correction or claim it is necessary as a proven fact.

## 5. Known tools, dates and missing versions

| Tool / information | Status |
|---|---|
| OpenAI Codex, documented November editorial/document work | Known from visible activity and retained reports; observed client date 10 November 2026, with Batch 1/2 records also dated 9 November. Exact historical application build/model/deployment versions are not recorded in Git/reports. |
| ChatGPT | Named in the authors' declaration. Exact model/version, account-session dates, prompts, scope and translation pairs are not supplied. |
| Earlier conversion and research/diagnostic tool use | Tool, version and dates UNVERIFIED; commit timestamps bound file tracking, not AI-use events. |
| Runtime versions such as R 3.4.3, Biber 2.22 and pdfTeX 1.40.29 | Document/research software versions, **not AI tool versions**. Do not substitute these for ChatGPT/Codex identifiers. |

No tool/model version is invented from a current product name, a generic model-family label or the fact that this assistant is Codex. Obtain contemporaneous chat exports/app information where available; if versions cannot be recovered, ask the journal what truthful unavailable-version wording it accepts.

## 6. Current policy comparison ? checked 10 November 2026

The official [Taylor & Francis AI policy](https://taylorandfrancis.com/our-policies/ai-policy/) permits responsible language/translation and coding assistance, requires tool/version/use/reason disclosure, human oversight and accuracy, and warns against unreviewed generation replacing core author responsibilities. It notes that journals may impose stricter limits. The observed editorial/document activity is not automatically prohibited, but compliance requires the missing scope and review evidence. The retrieved general policy supplies no quantitative ?amount of editing = first draft? test; this audit invents none.

The official [authorship/AI guidance](https://authorservices.taylorandfrancis.com/editorial-policies/defining-authorship-research-paper/) additionally calls for retained original/revised or translated versions, exact tool information, author accuracy/responsibility and terms confirmations, and identification of the human translation checker. Names must not be added for an AI tool. These attestations are not established by a successful PDF build or by equal human contributions. JSCS-specific AI limits remain UNVERIFIED because its detailed instructions were inaccessible.

## 7. Proposed disclosure ? for author review, not inserted

> AI tools, including ChatGPT and OpenAI Codex, assisted with grammar checking, translation, revision of existing manuscript text and repository documentation, to improve language clarity and the organization of the manuscript and its supporting documentation. Documented Codex assistance included redrafting existing passages and drafting reproducibility, evidence-map and data-availability documentation from existing project material, together with document-build, packaging and inspection utilities. According to the authors' declaration, AI was not used to develop or modify research code, simulations or statistical analysis.

This wording is intentionally broader than grammar-only assistance and does not assert that AI generated the original first draft. The final sentence remains an author assertion requiring the historical scope check above. The proposal has **not** been inserted into either PDF/source.

Before adopting a final version, authors must supply:

- Exact ChatGPT/model and Codex/application/model identifiers for the actual sessions, dates and tasks; an honest unrecoverable-version explanation if necessary, accepted by the publisher.
- Source-language originals, translated/revised versions and the name of the author who checked translation accuracy; clarify whether translation concerned the authors' own work and any prior publication/permissions issue.
- Confirmation of human review of all AI-assisted material, references and methodological descriptions, and responsibility for accuracy/integrity; do not infer that checking a PDF constitutes this review.
- Confirmation that the relevant tool terms were actually examined and are suitable for publication, and any assistance acknowledgements/consents the policy calls for. None is asserted here.
- A scope ledger for the research/diagnostic code listed above, reconciling any AI involvement with the current exclusion, and original-draft evidence sufficient to distinguish revision from earlier first drafting.

A factual final disclosure cannot be completed by filling invented versions or by assuming the authors have reviewed terms. This is an unresolved provenance/disclosure gate, not a finding that the paper was AI-first-drafted or that the authors' research-code assertion has been disproved.
