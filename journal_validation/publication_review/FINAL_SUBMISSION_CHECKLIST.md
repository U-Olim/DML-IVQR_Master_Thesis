# Final submission checklist and package plan

**Repository / branch:** `DML-IVQR_Master_Thesis` / `journal-validation`
**Prepared:** 10 November 2026 (Asia/Tashkent)
**Status:** submission readiness is **not established**. Author confirmation, anonymous evidence access and some live journal requirements remain unresolved.
**Scope of this pass:** this checklist only. No manuscript, numerical results, theory, code, figures or previous reports were changed. No new PDF, submission archive or anonymous repository was created; no commit or push.

This file contains identifying author information and repository provenance. It belongs with internal/editor-facing preparation records, not an anonymous reviewer upload.

## 1. Single author-information checklist

Both authors should return one jointly agreed response to the fields below. Confirmed facts must then be applied consistently to the named title page, PDF metadata and portal. No role, affiliation or absence declaration is inferred from author order or earlier records.

### Existing identities to verify

| Current source position (not approval of final order) | Retained name | Retained ORCID | Retained email |
|---|---|---|---|
| 1 | OLIMJON UMIDJON UGLI UMURZOKOV | 0009-0008-0090-7100 | olimumurzokov022@gmail.com |
| 2 | UMIDJON UMIRZAKOVICH KOSTAEV | 0009-0000-0205-5142 | umidjonkostaev2025@gmail.com |

The visible source lists UMURZOKOV first, while `main.tex:14`, the current PDF author metadata and the October edit records list KOSTAEV first. The older report records a shared **Tashkent State University of Economics, Tashkent, Uzbekistan** affiliation. This is historical evidence, not confirmation that it should be restored or assigned to either author now.

| Confirm | Exact information needed from the authors | Exact current LaTeX location |
|---|---|---|
| [ ] Publication identities and final order | Confirm spelling/publication form, ORCID and contact email for each person above; return one numbered final author list agreed by both authors. | `journal_article/main.tex:5?12` (visible block, individual details at 6?11); `journal_article/main.tex:14` (`pdfauthor` must match confirmed order). |
| [ ] Affiliations and author links | For each author: institution during the work, department if applicable, city, country, required postal address, and any present-address note. Confirm whether the older shared university affiliation remains correct and which author superscripts link to which affiliation. | Insert confirmed affiliation text and author markers inside the existing block **before** `journal_article/main.tex:12` (`\end{minipage}}`); no affiliation block is currently printed. Reconcile the placeholder in `journal_article/sections/submission_declarations.tex:10`. |
| [ ] Corresponding author | Full name of the designated person, correspondence email, institution and postal address; confirm both authors agree to the designation. | Add the confirmed correspondence designation/contact in the title block before `journal_article/main.tex:12`; replace the corresponding-author placeholder at `journal_article/sections/submission_declarations.tex:10`; match portal fields. |
| [ ] Funding | Actual funder names, grant identifiers, grant recipients and funder roles; if there was no relevant funding, provide an expressly approved truthful statement instead of leaving an inference from silence. | `journal_article/sections/submission_declarations.tex:4`. |
| [ ] Competing interests | Each author's relevant financial and non-financial interests, or that author's explicit confirmation of the truthful absence statement to use. | `journal_article/sections/submission_declarations.tex:6`. |
| [ ] Contributions | Agreed actual contributions of each author. Supply descriptions first; map to CRediT only if the journal/portal requests it. Do not assign contributions from author position. | `journal_article/sections/submission_declarations.tex:8`. |
| [ ] AI assistance | Full tool names and versions/model identifiers where available, dates/scope, how and why each tool was used, including any earlier research/analysis/code use if applicable. Codex manuscript/documentation assistance is known in this session; earlier use is not established. Authors must confirm the publisher's requested accuracy, responsibility and applicable terms statements after their own review. Do not invent a model version or assert that AI was absent. | `journal_article/sections/submission_declarations.tex:12`. |
| [ ] Institutional applicability / acknowledgements | Confirm whether any institutional/ethics statement is applicable and provide its actual wording/reference if required; do not invent approval, exemption or non-applicability. Identify any acknowledgements and obtain consent where needed. | `journal_article/sections/submission_declarations.tex:14`; any acknowledgements location should be added only after facts/placement are confirmed. |
| [ ] Final approval and access decision | Both authors approve the manuscript and declarations; nominate responsibility for upload; decide with the journal how reviewers will actually receive evidence anonymously. Confirm which existing local-only artifacts, if any, can be provided. This does not authorize publication or creation of a repository in this pass. | Existing access statement: `journal_article/sections/data_availability.tex:2,4`; declaration/access inputs: `journal_article/main.tex:28?29`. |

The declaration heading and warning at `submission_declarations.tex:1?2` are visibly draft. Remove the draft status only after factual text is supplied and approved. A declaration paragraph does not replace the required title-page author/affiliation details. All line references describe the current source and will shift after insertions.

The approved title is already correct at `main.tex:3` and in `pdftitle` at `main.tex:14`. Retain it. The braced technique statement immediately before the abstract is at `main.tex:17`.

## 2. Two-output package plan ? proposed files, not created

Use separate build/output directories so the named and review versions cannot share author-bearing auxiliaries or metadata. Preserve the current named master and historical QA. Do not submit a ZIP of the whole working tree.

| Proposed output | Contents and audience | Preparation still needed |
|---|---|---|
| `manuscript_named.pdf` | Approved title, confirmed title-page identities/affiliations/correspondence, scientific article, confirmed declarations, truthful public availability statement, references and Appendices A?D. Named/editor-facing category, with category confirmed in the live portal. | Apply the author checklist; synchronize PDF author metadata; build and inspect the exact source revision. The current Batch 4 PDF remains a draft with unresolved facts. |
| `title_page_named.pdf` (only if requested) | Confirmed title, complete author order/affiliation links and correspondence; any declarations the journal assigns to its title-page file. Editor-facing, not the anonymous manuscript. | Confirm whether JSCS requests this separately; create from the same confirmed facts as the named manuscript. Do not assume this replaces the full named-file requirement. |
| `manuscript_review.pdf` | Same approved title, abstract, keywords, scientific text, equations, numbers, citations, tables/figures and Appendices A?D, with identifying presentation/provenance handled as below. Reviewer-facing anonymous category. | Prepare a separate review build. Omit author block/contact details, clear identifying metadata, treat identity-bearing declarations according to journal instructions and provide a real reviewer evidence route. No anonymous review PDF exists from this pass. |
| `results_supplement_review.pdf` (optional) | Existing full point-performance, coverage, power and grid-informativeness tables, if useful and permitted; no regenerated statistics. Reviewer-facing. | Assemble existing assets without changing entries, inspect metadata/headers, and use distinct supplement labels if a new wrapper is later authorized. Do not imply it already exists. |
| `frozen_summaries_review.zip` (conditional) | Compact existing CSV summaries plus an anonymous, truthful inventory for reviewer inspection. Reviewer-facing only after access/metadata arrangements are agreed. | Check portal size/type rules and every included file; preserve numerical bytes. Do not include raw runs or a complete repository by default. |
| Confidential provenance / cover material | Full public repository URL and revision information, original-to-review artifact mapping, historical freeze access gap, local-only exclusions, author facts and any disclosure of prior public circulation. Editor-facing only **if the portal provides an appropriate confidential route**. | Confirm actual visibility with the journal. No confidential/anonymous route is assumed to exist. Do not use an editor-only attachment as a substitute for evidence reviewers need. |

Preserve the scientific meaning and all material qualifications in both manuscript versions: unestablished inference validity, non-finite mixed residual density, selected-case numerical sensitivity, direct-truth versus stored-grid distinctions and implementation-level comparisons. Anonymization must not remove inconvenient evidence, alter numerical values, eliminate essential citations or convert an access limitation into a false availability claim.

## 3. Authorship-leak inventory and treatment

**Confirmed** means visible in current source or the recorded Batch 4 PDF metadata. Other rows identify linked/source-bundle exposure or checks still required; this is not a claim that every possible hidden object has already been cleared.

| Leak / exposure | Exact source or artifact | Planned treatment in review material |
|---|---|---|
| Names and author order | `journal_article/main.tex:5?12`; current title-page PDF | Omit the author block in a separate review build. Preserve named source. |
| ORCID IDs and ORCID hyperlink targets | `main.tex:7,10` | Remove both visible IDs and active targets from review output; hiding text alone is insufficient. |
| Emails and mailto links | `main.tex:8,11` | Omit both visible contacts and link annotations from the review file. |
| PDF author metadata | `main.tex:14`; `journal_article/qa/batch4/pdfinfo.txt` records KOSTAEV then UMURZOKOV | Explicitly clear identifying Author/subject/keyword/XMP/custom fields in the review build and inspect the resulting PDF. Retain approved title; tool producer/version alone is not an author identity. |
| Future affiliations, correspondence, named contributions, funding/acknowledgement identities | Named title block and `sections/submission_declarations.tex:4?14` | Route identifying details according to confirmed journal instructions. Keep required scientific/conflict/assistance disclosures truthful; do not assume every declaration may simply be omitted. |
| Public GitHub URL and username | `sections/data_availability.tex:2`; `supplementary/D_implementation.tex:6` | Review presentation needs an agreed anonymous evidence route or journal-approved handling. Merely deleting the URL gives reviewers no replacement access. No anonymous repository/link has been created or verified. |
| Full and shortened commit identifiers | `data_availability.tex:2`; `D_implementation.tex:6`; `supplementary/D_evidence_map.tex:3` | Commit searches can identify the project even without its URL. Use agreed non-identifying review locators only when a real mapping/access mechanism exists; retain full original provenance privately/named. Do not label a new submission revision with an old evidence hash. |
| Supplementary file paths and distinctive provenance | `D_implementation.tex:6,8,12,18,180,182,186`; `D_evidence_map.tex:3,21?34`; linked manifests, reports, contracts and environment records | Paths are not necessarily personal by themselves, but they can identify a searchable public repository. Inspect linked records for author names, machine paths, Git metadata, institutional references and external URLs. Preserve the evidence contents and scientific limits in review copies; do not supply unchecked linked originals as anonymous files. |
| Linked manifests and selected-case numerical reports | `thesis_extension/reporting/EMPIRICAL_RESULTS_MANIFEST.csv`, `REPORTING_OUTPUT_MANIFEST.csv`; `thesis_extension/diagnostics/grid_sensitivity/GRID_RESULTS_MANIFEST.csv`; Stage 2G reports/contracts named in E6 | Original path/hash linkage belongs in the retained full evidence map. Any reviewer copy needs a consistent attachment locator and access to the relevant evidence, with the original mapping retained. Hashes/unique filenames can be searchable fingerprints; a filename change is not a complete anonymity audit. |
| Historical author and QA records | `journal_article/EDIT_REPORT.md`, `qa/revision_title.png`, `qa/revision_pdfinfo.txt`, `qa/revision_validation.json`, root `main.pdf`; Batch 1?4 reports and this checklist | Keep as internal/named historical evidence. Exclude from reviewer uploads. The current `qa/batch4/main.pdf`, text extracts, logs and contact sheets also reveal the named draft. |
| Source/build paths and comments | `qa/batch4/build_document.py`, build logs/results, `.aux`, `.bcf`, `.bbl`, `.out`, `.fls`, editor history and source comments | Do not send build directories or auxiliaries as supplementary evidence. If source is required, prepare a whitelisted source bundle and inspect its text/metadata; retain necessary bibliography and scientific dependencies. |
| Git/package/environment metadata | `.git` history and authorship, repository descriptions/README, environment/session files, copied library metadata and package archives | Do not upload the repository wholesale. Distinguish project identity from legitimate third-party attribution; do not strip required licences or third-party references to manufacture anonymity. Exact source-bundle requirements remain unverified. |
| Embedded figure/attachment metadata | Existing PDF and PNG assets and any future supplement PDF/ZIP | Read-only PNG inspection found DPI fields only. Literal-field inspection of the three generated figure PDFs found Cairo creator/producer fields, not a literal Author field; encoded/XMP/other hidden metadata is **not fully audited**. Inspect standalone uploads and PDF link/attachment/bookmark layers before claiming an anonymous package. No figure was changed. |
| Public matching of title, wording and numerical examples | This approved title and distinctive existing findings can be matched to already public material | Residual re-identification risk cannot be eliminated by removing explicit identifiers. Do not change scientific content to disguise it. Authors should disclose prior public circulation to the editor and follow the journal's guidance; do not promise guaranteed anonymity. |

No author-identifying self-reference by the two manuscript authors was found in the inspected manuscript bibliography/source scan. Names of cited third-party researchers are ordinary scholarly references and should not be removed indiscriminately. Final review-file inspection must include extracted text, visible pages, PDF metadata/XMP, hyperlinks, bookmarks, embedded files and separate uploaded files?not just a text search of the title page.

## 4. Current requirements: verified scope versus unresolved rules

Checked 10 November 2026. Direct IFA/about-page/home-page fetches returned **HTTP 403**. A fresh publisher-indexed [JSCS journal page](https://www.tandfonline.com/journals/GSCS) supplied current journal-specific policy text; it is search-retrieved publisher content, not successful live IFA access.

| Topic | Status | Consequence |
|---|---|---|
| Review model and submission system | **Verified in current publisher-indexed journal content:** double-anonymous review and online Submission Portal. | Plan named and anonymous outputs; confirm actual live file categories and visibility before uploading. |
| Technique/contribution-area cue before abstract | **Verified in the same publisher-indexed journal content:** a braced indication before the abstract is requested. | Already present at `main.tex:17`; retain the existing restrained wording. |
| Scope | **Verified in the same publisher-indexed journal content:** significant computation/simulation contributions are sought; a controlled simulation contribution still requires editorial assessment. | No claim of sufficient novelty or acceptance follows from meeting package requirements. |
| Named/anonymous files and anonymized supplements | **Verified general publisher guidance**, not inspection of this manuscript's portal: [Submission Portal guide](https://authorservices.taylorandfrancis.com/publishing-your-research/making-your-submission/using-taylor-francis-submission-portal/). | Its named/anonymous categories inform the plan; actual JSCS portal requirements must be checked. |
| Authorship agreement and AI disclosure | **Verified publisher-wide policy:** [Authorship guidance](https://authorservices.taylorandfrancis.com/editorial-policies/defining-authorship-research-paper/). It calls for author agreement and transparent tool/version/use disclosure. | Authors must supply and approve facts; the existing placeholders are not completed declarations. |
| Access statement and identity protection | **Verified general publisher guidance:** [Data availability statements](https://authorservices.taylorandfrancis.com/data-sharing/share-your-data/data-availability-statements/) explains access conditions and identity risks under anonymous review. | Keep statements truthful. The exact JSCS data-policy tier and acceptable reviewer route are **unverified**. |
| Format-free submission; required class/template; citation style; abstract/word/page limits; figure resolution/alt text; permitted supplement formats/size; title-page and source-file requirements; declaration placement/CRediT fields; mandatory cover-letter content | **Unverified** because [detailed instructions](https://www.tandfonline.com/action/authorSubmission?show=instructions&journalCode=gscs20) remain inaccessible and the live submission form was not inspected. | Obtain current instructions through the authors' access or editorial office. Do not convert the class/style, impose guessed limits or claim compliance. |

General publisher guidance does not prove that a particular template, data policy tier or file layout is mandatory for JSCS. No submission fee/APC, institutional approval exemption or funding/conflict absence is inferred here.

## 5. Supplement placement and cross-reference protection

**Recommendation for the initial review package, unless confirmed journal rules require otherwise: retain all existing Appendices A?D in the main review PDF.** The Batch 4 document is 34 pages, with A/B/C/D beginning on pages 18/25/26/29. This is historical build evidence for that source state, not a journal page-limit approval or a rebuilt anonymous file.

| Existing section | Recommended placement | Reason / exact dependency |
|---|---|---|
| A: numerical-domain diagnostics and existing tables/figure | Keep in review PDF. | `sections/03_design.tex:191` and `04_results.tex:83` refer to A; A and C cross-reference one another (`A_numerical_domain.tex:28`, `C_coverage_audit.tex:22`). Failure/domain limitations must remain accessible. |
| B: controlled-relevance derivation | Keep in review PDF. | `sections/03_design.tex:105` points to `app:kappa-derivation`; the controlled design is central to the contribution. |
| C: direct-at-truth coverage audit | Keep in review PDF. | `sections/04_results.tex:49` points to C; it qualifies the interpretation of coverage diagnostics. |
| D.1, D.3?D.7: environment/RNG limits, sequence, formulas, finite solvers, density argument and conditional score algebra | Keep in review PDF, with identifying provenance handled in the separate review build. | Framework references D at lines 123/125/133; results at 51; discussion at 8. Removing D.6 would detach the density qualification from its proof sketch; removing numerical/RNG scope would weaken approved corrections. |
| D.2: complete evidence map | Keep in review PDF, with truthful agreed attachment/access locators for review material. | Referenced by results at line 3 and discussion at line 6. Retain the full original named map, including all paths and limitations. A private mapping alone is not evidence access for reviewers. |
| Existing full-result table assets not currently input | Suitable for an optional separate results supplement. | `journal_article/tables/generated/appendix_point_performance.tex`, `appendix_coverage.tex`, `appendix_power.tex`, `appendix_cr_informativeness.tex`. Assemble existing material only; do not regenerate results or insert new duplicated A?D labels into a separate wrapper. |
| Compact machine-readable evidence | Suitable for a separate permitted attachment, after anonymity/access checks. | `thesis_extension/final/output/n500/summary.csv`, `n500/power_summary.csv`, `n1000/summary.csv`, `n1000/power_summary.csv`; `thesis_extension/reporting/output/table_cr_informativeness_full.csv`, `table_grid_domain_diagnostic.csv`; `thesis_extension/calibration/instrument_strength_100rep/kappa_strength_summary.csv`. Retain exact numerical bytes and include an accurate inventory. No attachment was created here. |
| Full numerical-audit reports / provenance | Optional additional reviewer attachments only after inspection and agreed handling; retain full originals in named provenance. | Existing Stage 2G reports/contracts are referenced by D/E6. Their scientific content must not be hidden merely because the original provenance identifies the project. |

The current inclusion points are `journal_article/main.tex:42?45`; D's evidence-map input is `supplementary/D_implementation.tex:14`. **Do not simply comment these inputs out.** Keeping them inline preserves current A?D numbering and cross-references without a new split-build mechanism.

If the journal requires a separate technical supplement, plan a whole A?D supplement with its original labels/numbering and an explicit main-to-supplement locator scheme. External `.aux`/hyperlink handling or textual supplement locators would need a separate authorized document-layout implementation and fresh builds of both files; merely copying sections to another PDF does not preserve working references. Until that is implemented and inspected, retain the inline layout. Do not move individual D subsections or drop labels as a shortcut. No split or cross-reference edit is made in this pass.

## 6. Evidence-access decisions that remain open

- The checked accessible evidence checkpoint is `15b8b4dc95e3658f3b858a6f792ea2983299aaa6`. It contains earlier editorial work and frozen evidence; it is not the present uncommitted submission manuscript. Do not claim that it reproduces a later named or review PDF.
- The freeze record's historical identifier `ac9a9ccad027cde05488abb633e66cc02f87cc46` was unresolved locally and returned 404 during Batch 3. Retain that limitation; do not invent a replacement historical identifier.
- Large grid-diagnostic profiles and saved primitives are local/Git-ignored. Stage 2H pilot outputs under `journal_validation/stage2h/pilot/runs/` and `journal_validation/stage2h/pilot/SHA256_MANIFEST.json` are also local/Git-ignored. They are not promised as public or reviewer attachments.
- Main frozen summaries can be inspected without re-estimation. Exact historical penalty replay and worker-stream independence remain unestablished; a new package inventory does not repair missing RNG records.
- Authors must agree with the journal on actual anonymous access: permitted supplemental attachments, an approved existing service/process, or another genuine route. No anonymous repository/access exists by virtue of this plan. If evidence cannot be provided without identification under the journal's process, raise that problem confidentially with the editor before submission rather than supply a false anonymous-access statement.

## 7. Ordered package-release gates ? future work only

1. Receive the single completed author checklist and both authors' approval; resolve the author-order conflict before editing metadata or portal records.
2. Obtain the inaccessible JSCS instructions/live upload requirements and agree the evidence/anonymity arrangement. No messages to the journal are sent by this pass.
3. Apply confirmed author facts in the named master at the listed locations, preserving all scientific content. Prepare a separate review build and any permitted supplements; keep a confidential original-to-review provenance mapping.
4. Whitelist only required PDFs/source dependencies/assets for each upload category. Exclude this checklist, change reports, old PDFs/QA, `.git`, runtime caches and unchecked provenance bundles from reviewer files.
5. Build named/review documents separately using document tools only. Inspect visible pages, metadata/annotations, all references, equations, table/figure labels, appendices and standalone supplements. Confirm scientific text and numerical assets agree across versions. The Batch 4 named draft's successful build is not evidence for an as-yet-unbuilt review package.
6. Check every `\ref` against the actual package, including any external supplement references, and verify that reviewers can actually open the cited evidence without exposing author details through the agreed route.
7. Record exact final source/output identities and inventories after approval. Any later version-control/release action requires separate authorization; do not call an uncommitted draft a released revision.
8. Have both authors review the portal-generated proof and file visibility before anyone asserts readiness or submits. No submission readiness is claimed in this checklist.

## 8. What the authors should send back

Return the completed table in Section 1, with the jointly agreed numbered author order and per-author affiliations/IDs/contacts; the designated corresponding author; approved funding and per-author conflict statements; agreed contributions; complete tool/version/use/reason and author-confirmation information for AI assistance; applicable institutional/acknowledgement details; both authors' approval; and the current journal instructions/access decision. Those are the factual and procedural inputs still needed. The package names above are proposals, not evidence that files or anonymous access have already been created.
