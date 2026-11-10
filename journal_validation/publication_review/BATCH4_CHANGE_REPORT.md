# Stage 2I ? Publication Revision Batch 4

**Date:** 10 November 2026 (Asia/Tashkent)
**Branch:** `journal-validation`
**Supplied HEAD:** `15b8b4dc95e3658f3b858a6f792ea2983299aaa6` (`Stage 2`, 9 November 2026; parent `2ceec58a`).
**Final recommendation: NOT READY for submission.** A current document was built and inspected, but author facts, declarations, anonymous-review packaging and essential journal instructions remain unresolved.

## Outcome and scope

Applied **Controlled Instrument-Relevance Sensitivity in High-Dimensional IVQR: A Monte Carlo Study** to the LaTeX title and PDF title metadata. Repaired malformed author markup without choosing an author order or affiliation. Added explicit draft declaration locations, reduced repeated result/caveat inventories, completed notation, corrected finite-grid geometry language, improved Appendix D path presentation and updated the README. All scientific qualifications from Batches 1?3 remain in the manuscript.

A clean document-only build generated and was inspected as `journal_article/qa/batch4/main.pdf`: **34 A4 pages; 1,014,922 bytes**. The historical root `journal_article/main.pdf` and historical QA evidence are unchanged. Compilation does not resolve the factual/publication blockers below. No research code, statistical data, original table/figure assets, bibliography records or numerical results were changed. No simulations, estimation, statistical tests, scientific numerical validation or figure regeneration were run. No commit or push.

## Author and metadata audit ? R1-003

The pre-batch source had `KOSTAEV\textsuperscript\\` without an argument. The first author also carried an affiliation marker `a` with no printed affiliation. The malformed command and orphan marker were removed; no affiliation letter or institutional fact was assigned. Existing names, ORCIDs, emails and visible order were retained exactly. The comment claiming a shared affiliation was replaced with a confirmation-needed comment.

| Record | Author order | Affiliation / correspondence |
|---|---|---|
| Current named source and newly rendered title page | OLIMJON UMIDJON UGLI UMURZOKOV; then UMIDJON UMIRZAKOVICH KOSTAEV | No confirmed affiliation printed; no corresponding author designated |
| Current PDF author metadata (retained) | KOSTAEV; then UMURZOKOV | No affiliation/correspondence metadata added |
| `journal_article/EDIT_REPORT.md` (15 October 2026), `qa/revision_pdfinfo.txt`, `qa/revision_validation.json` and historical title image | KOSTAEV; then UMURZOKOV | The edit report records a shared Tashkent State University of Economics, Tashkent, Uzbekistan affiliation; no corresponding author |

The older report/title evidence is version-specific, not authority to reverse the present visible order or restore an affiliation without confirmation. The PDF author-order discrepancy is **identified and deliberately unresolved**, rather than silently normalized. Only PDF **title** metadata was updated. The new PDF confirms both existing names/ORCIDs/emails render, and confirms the missing affiliation/correspondence problem remains.

## Author-confirmation checklist ? R1-003 / R1-012

- [ ] Both authors agree on the final order; apply that single order to the title page, PDF author metadata and submission system. The current source order and older records conflict.
- [ ] Confirm spelling/publication form of both retained names, ORCIDs and email addresses. No identity change was inferred.
- [ ] Confirm each author's institutional affiliation at the time of the work, department/address if required, and any present-address note. Confirm whether the historical shared university affiliation remains applicable and which author links belong to it.
- [ ] Designate the corresponding author and confirm postal address/email and authority to correspond for all authors.
- [ ] Supply actual funding sources, grant numbers/recipients and any funder role, or approve the appropriate truthful absence statement. No absence is presently asserted.
- [ ] Each author confirms relevant financial/non-financial competing interests and approves the declaration. No absence is presently asserted.
- [ ] Agree actual author contributions; confirm the required journal/portal format before assigning CRediT or other roles. No contributions were invented.
- [ ] Confirm applicable institutional/ethics requirements and any necessary statement. No approval, exemption or non-applicability is inferred from silence.
- [ ] Review the assistance disclosure: this session used OpenAI Codex for manuscript/documentation work. Confirm exact tool/model version, full scope/reason for use, and the publisher's accuracy/responsibility/terms confirmations; no author attestation is invented.
- [ ] Approve the final manuscript, declarations, corresponding-author designation and submission package before upload.

The visible draft placeholders are in `journal_article/sections/submission_declarations.tex`, before the existing headed data/code availability statement and references. They are preparation locations, not completed declarations. The title-page affiliation/correspondence details must be filled from confirmed facts; the draft declaration paragraph does not substitute for them.

## Verified versus unverified submission requirements ? R1-012 / R1-013 / R1-023

Checks were made on 10 November 2026. Source retrieval was mixed: publisher search indexing exposed the journal information text, but direct current instructions requests returned HTTP 403. Indexed publisher text and general publisher guidance are distinguished below; third-party journal guides were not treated as current authority.

| Requirement / issue | Verification and action |
|---|---|
| Double-anonymous review | **Verified in publisher-indexed journal information**, not a successful direct live IFA fetch: [JSCS journal information](https://www.tandfonline.com/action/journalInformation?journalCode=gscs20&show=instructions) states the review model is double anonymized. Treat the current named master as unsuitable for anonymous review upload; confirm the live portal categories before submission. |
| Technique/novelty cue just before the abstract | **Verified in the same publisher-indexed journal page**: it requests a braced indication of the primary technique and contribution area. Added a restrained Monte Carlo / instrument-relevance sensitivity line before the abstract; no estimator/theorem or improvement claim was added. |
| Named and anonymous file separation | **Verified general publisher portal guidance**, conditionally applicable to a double-anonymous journal: [Submission Portal guidance](https://authorservices.taylorandfrancis.com/publishing-your-research/making-your-submission/using-taylor-francis-submission-portal/) calls for an anonymous manuscript without identifying details in addition to the named file. Exact JSCS upload categories/files remain to be checked. |
| Data/code availability and identifying links | **Verified general publisher guidance**: [Data availability statements](https://authorservices.taylorandfrancis.com/data-sharing/share-your-data/data-availability-statements/) explains access-condition statements and identity risks under double-anonymous review. The named master retains its full evidence route. The exact JSCS data-policy tier, repository/deposit conditions and anonymous access route remain unverified. |
| Authorship, contributions and AI assistance | **Verified publisher-wide guidance**, not a verified JSCS-specific contribution taxonomy: [Authorship policy](https://authorservices.taylorandfrancis.com/editorial-policies/defining-authorship-research-paper/) requires agreement on author details and transparency about AI use, including tool/version and use. Added factual-confirmation placeholders; no authorship decisions or attestations were made. |
| Funding and competing interests | **Verified publisher-wide guidance**: [Editorial policies](https://authorservices.taylorandfrancis.com/editorial-policies/) and [competing-interest guidance](https://authorservices.taylorandfrancis.com/editorial-policies/competing-interest/) support truthful disclosure of funding/interests. Added locations awaiting authors' facts. Exact JSCS wording/portal fields remain unverified. |
| Article class, reference style, abstract/word/page limits, format-free initial submission, separate title-page/supplement requirements and artwork specifications | **Unverified**: [direct instructions endpoint](https://www.tandfonline.com/action/authorSubmission?show=instructions&journalCode=gscs20) returned 403. The existing article class, author?year style and numerical assets were retained; no compliance or mandatory Interact-template claim is made. |

### Anonymity disposition

The named master, its author metadata and the identifying GitHub URL are preserved. No anonymous PDF is claimed or supplied: masking the title page alone would leave identifying repository/commit provenance and potentially identifying supplements. A separate review copy must remove names/contact details/author metadata and handle repository access, revision identifiers, declaration identities and supplementary-file metadata without severing reviewer access to evidence. An anonymous repository/deposit route was not created, and no files were published. The exact named master and complete evidence map must remain preserved. R1-013 is therefore **diagnosed with an actionable blocker**, not declared fully resolved.

## Editorial and presentation changes ? R1-017 / R1-020 / R1-024

The abstract and conclusion retain the controlled Gaussian design, the existing three-measure contrast, oracle deterioration, strong-relevance undercoverage, ranking exceptions and implementation-level scope. Discussion now interprets the disagreement between truth retention and false-effect exclusion instead of repeating the Section 4 numerical inventory. Repeated caveats were shortened with direct Appendix D pointers; non-finite mixed density, unestablished inference validity, same-sample fitting/penalty randomness, selected-panel rank/decision sensitivity, and direct-truth/stored-grid distinctions remain explicit. No correction is promised to restore calibration.

The observation vector W is defined separately from the scalar candidate statistic; the reference population nuisance profile is qualified by uniqueness or a fixed measurable selection. The already-used n?1 sample-variance convention is written explicitly while retaining the historical use of variance as a normal scale. These are notation/description changes, not altered statistical definitions. Finite-grid wording now describes a trapezoidal summary of binary decisions and accepted grid runs, not exact continuous component lengths or unrestricted confidence-region geometry. Appendix A's localization wording is narrowed accordingly.

Appendix D preserves every complete evidence-map path, the full historical evaluation sequence, penalty/proxy/residualization formulas, finite-solver limitations, density argument and ideal-score algebra. The detailed finite termination description is retained once; the operational sequence points to it. `xurl` wraps long paths, with a small/ragged-right path inventory and a normal readable evidence table. D remains six pages (29?34); the map heading begins on page 29, its table/inventory continues on pages 30?31. No evidence map or solver qualification was removed merely to shorten the document.

The accessible **evidence** revision `15b8b4dc?` is explicitly separated from the unresolved historical freeze identifier `ac9a9cca?` and from the current **uncommitted manuscript**. The README now describes actual Appendices A?D, the current source/build target and historical QA's version-specific scope; it no longer calls the author field empty or treats the old root PDF as current. All historical records remain.

## Actual build and PDF inspection ? R1-023

1. Normal `pdflatex --version` / `biber --version` failed before TeX processing, reporting a fresh installation and access-denied attempts involving `C:/Users/User/AppData/Roaming/MiKTeX/2.9` and `Software/MiKTeX.org/MiKTeX/2.9/Setup` initialization. This diagnosed a configuration/permission issue, not a manuscript syntax result.
2. Job-local `MIKTEX_USERCONFIG`, `MIKTEX_USERDATA`, `MIKTEX_USERINSTALL` and `MIKTEX_USERSTARTUPFILE` settings reuse the installed binaries and selected existing non-sensitive maintenance/NoRegistry settings. Writable caches stay under `journal_article/qa/batch4/runtime/`. No global configuration/registry repair, software installation or updates were performed. `AutoInstall=0`, `--disable-installer` and `-no-shell-escape` prevent package installation and TeX shell commands in the build. The installed Biber executable is invoked directly.
3. First build: all command exits were zero and a 35-page PDF appeared, but root historical auxiliaries supplied stale references. Its logs are retained as `attempt1_*`. A second build fixed search precedence but retained a stale Biber rerun marker; its diagnostics are `attempt2_*`. Neither was declared a clean final document. Only this job's rebuildable auxiliaries were cleared, after preserving diagnostics; the historical root auxiliaries/PDF and older QA were untouched.
4. Final clean sequence: pdfLaTeX ? Biber ? pdfLaTeX ? pdfLaTeX, **all exit 0**. Working directory and auxiliary precedence are the job's output directory, with source/bibliography paths pointing to the article. The PDF is **34 A4 pages, 1,014,922 bytes**; SHA-256 `d3f3ef20d0cc75212bc03326963140db6413f369aeaac3055a926376da05e214`. Final commands, times and exit codes are in `journal_article/qa/batch4/build_results.json`; Biber identifies itself as 2.22, pdfLaTeX as MiKTeX 26.5 / pdfTeX 1.40.29.
5. Final LaTeX log: **no undefined references/citations, multiply defined labels, overfull boxes, unresolved destinations or remaining rerun requests**. Biber reports no warnings/errors. Non-fatal diagnostics remain: epstopdf notes disabled shell escape, and MiKTeX notes updates have not been checked. Some metadata/text/render utility calls printed package-database-lock warnings despite exit 0 and valid outputs; these logs are retained. No EPS conversion, update or package repair was needed to produce and inspect the document.
6. PDF title matches the approved title. The title page displays both retained names, ORCIDs and emails in source order; PDF author metadata still has the conflicting older order. Affiliation/corresponding-author facts are absent pending confirmation, and declarations remain visible draft placeholders.
7. All **34 pages were rendered in grayscale**, with three contact sheets visually inspected. Title page (1), main table (9), coverage figure (10), reference list (17) and evidence map (30) were additionally viewed at reading size. No clipped content, missing assets or overflowing paths were observed. The main table and heatmap annotations are readable in the inspected rendering; dense appendix tables remain dense. This is not a printed-proof or verified journal-template compliance claim.
8. Text extraction contains **no `??`** and no blank pages. Main equation labels run **1?40**; appendix equation labels use **B.1?B.4** and **D.1?D.14**, without duplicate numbering in the document checks. References contain nine cited entries from the unchanged bibliography. Appendices A, B, C and D start on pages **18, 25, 26 and 29**. Appendix table continuations, figure notes and pagination were visually checked; no historical result assets were regenerated.

### Document evidence retained locally

- `journal_article/qa/batch4/main.pdf`, `pdfinfo.txt`, `article_text_utf8.txt`, `inspection_checks.json` (including source/PDF hashes), `build_results.json`.
- `journal_article/qa/batch4/latex1.txt`, `biber.txt`, `latex2.txt`, `latex3.txt`, `main.log`, and preserved `attempt1_*` / `attempt2_*` diagnostics.
- `journal_article/qa/batch4/page-01.png` through `page-34.png`, `contact-1.png` through `contact-3.png`, and utility/version logs.
- Reviewable helper and inspection note: `journal_article/qa/batch4/build_document.py` and `journal_article/qa/batch4/BUILD_INSPECTION.md`.

Generated PDFs, renders, intermediates, logs and runtime caches are intentionally Git-ignored local artifacts; this report does not present them as a public release. The helper and inspection note are included in the complete source/document diff below. No historical QA evidence was deleted.

## Remaining submission blockers and recommendation

**NOT READY.** The document now compiles and has been inspected, but the following must be resolved before a readiness claim:

1. Confirm author order/affiliations/correspondence, then reconcile title page, metadata and submission-system facts.
2. Complete and obtain approval for factual funding, competing-interest, contribution, institutional-applicability and assistance declarations; remove all draft placeholders only after confirmation.
3. Prepare and inspect the anonymous manuscript/supplements with an actual anonymous evidence-access route; preserve the named master. The present named PDF is not suitable for anonymous upload.
4. Confirm the current live JSCS instructions/portal requirements not retrievable here, including format-free/template policy, length/style/artwork requirements and exact declaration/data-policy/file-category rules.
5. Designate the final accessible manuscript/evidence revision after author review; `15b8b4dc` is an evidence checkpoint, not this uncommitted submission master. The historical freeze checkout and full RNG replay/local-only artifact limitations remain transparently disclosed, not repaired by prose.

The empirical/theoretical qualifications from earlier batches remain limitations of the study, not failures that a document build can validate away. No inference theorem, calibration repair, exhaustive novelty or journal acceptance is claimed.

## Exact modification inventory

Original lines refer to the captured pre-Batch-4 working tree, including all earlier uncommitted work. Revised lines refer to current source. The complete diff below supplies the exact wording for every change; earlier Batch 2/3 changes are excluded from this batch's diff.

| File | Exact changed spans (original ? revised lines) | Change |
|---|---|---|
| `journal_article/main.tex` | 3?4 ? 3?4; 6?6 ? 6?6; 9?9 ? 9?9; 14?14 ? 14?14; after 16 ? 17?17; 18?18 ? 19?19; after 26 ? 28?28 | Apply approved title/PDF title; remove unbound affiliation superscript and malformed command; retain visible and metadata author orders pending confirmation; add the indexed journal scope line and declaration input; tighten abstract. |
| `journal_article/preamble.tex` | after 15 ? 16?16 | Load the already installed xurl package to wrap repository paths; no journal class/template assumption. |
| `journal_article/sections/01_introduction.tex` | 14?14 ? 14?14 | Condense the limitations paragraph while retaining all material qualifications and the Batch 3 sample/draw distinction. |
| `journal_article/sections/02_framework.tex` | 35?35 ? 35?35; 83?83 ? 83?83; 135?135 ? 135?135 | Define observation-vector W separately from scalar W statistic; qualify ideal nuisance selection; reduce repeated inference-boundary prose. |
| `journal_article/sections/03_design.tex` | 189?189 ? 189?189 | Replace continuous-component language with binary-grid quadrature terminology; preserve the formula and values. |
| `journal_article/sections/05_discussion.tex` | 2?2 ? after 1; 5?5 ? 4?4; 7?7 ? 6?6; 9?9 ? 8?8; 11?17 ? 10?10 | Replace repeated result inventory with interpretation, confounding, limitations and reporting implications; keep exceptions and evidence pointers. |
| `journal_article/sections/06_conclusion.tex` | 2?2 ? 2?2; 4?4 ? 4?4; 6?6 ? 6?6 | Emphasize controlled contribution and truth-acceptance/exclusion disagreement, with oracle deterioration and bounded implementation/numerical inference. |
| `journal_article/sections/data_availability.tex` | 2?2 ? 2?2 | Make long full identifiers breakable; explicitly distinguish accessible evidence commit from uncommitted manuscript; retain local-only/accessibility limitations. |
| `journal_article/supplementary/A_numerical_domain.tex` | 16?16 ? 16?16 | Describe localization of accepted grid values without asserting continuous accepted components. |
| `journal_article/supplementary/D_evidence_map.tex` | 3?3 ? 3?3; after 17 ? 18?19; 21?21 ? 23?23; after 30 ? 33?33 | Retain every evidence path; distinguish evidence revision from uncommitted source; wrap paths with xurl and use a readable small/ragged-right inventory. |
| `journal_article/supplementary/D_implementation.tex` | 6?6 ? 6?6; 22?22 ? 22?22; 32?32 ? 32?37 | Separate accessible evidence commit from unresolved freeze identifier/current source; give the n?1 sample-variance convention; remove redundant solver wording from the operational sequence, retaining full formulas and finite-solver section. |
| `journal_article/README.md` | 1?1 ? 1?1; 3?3 ? 3?3; 5?5 ? 5?18; 11?11 ? 24?24; 13?13 ? 26?36 | Replace superseded A?E/empty-author/current-PDF claims with actual A?D contents, source/build locations, version-specific QA and submission blockers. |
| `journal_article/.gitignore` | after 11 ? 12?32 | Keep job-local TeX/Biber runtime, intermediates and generated PDF/render/log evidence local; preserve all historical tracked evidence. |
| `journal_article/sections/submission_declarations.tex` | after 0 ? 1?14 | Add visible, explicitly unconfirmed funding, competing-interest, contribution, affiliation/correspondence, AI-assistance and institutional-applicability placeholders. |
| `journal_article/qa/batch4/build_document.py` | after 0 ? 1?41 | Add a document-only local MiKTeX/Biber build helper; no installer, shell escape or research invocation. |
| `journal_article/qa/batch4/BUILD_INSPECTION.md` | after 0 ? 1?17 | Record actual final PDF/build/render inspection, caveats, provenance of unsuccessful attempts and NOT READY recommendation. |

## Preservation and Git status

Supplied HEAD remains `15b8b4dc?`, which combined the Round 1 audit and Batches 1/2. The pre-batch working tree already contained the Batch 2 follow-up and Batch 3 source/report additions. Their change reports were not rewritten in Batch 4. `sections/04_results.tex` still shows a Git modification from Batch 3; it is byte-identical to the Batch 4 baseline. All tracked files outside the explicitly listed Batch 4 sources/documents match pre-batch SHA-256 identities, including research code, frozen CSVs, figure/table assets, bibliography, old PDF and historical QA. Pre-existing untracked Batch 3 report content also matches. The exact source author identities/ORCIDs/emails and visible order are preserved; PDF author metadata is unchanged. No index/history mutations were made.

Current working tree (cumulative; includes earlier batches):

```text
 M journal_article/.gitignore
 M journal_article/README.md
 M journal_article/main.tex
 M journal_article/preamble.tex
 M journal_article/sections/01_introduction.tex
 M journal_article/sections/02_framework.tex
 M journal_article/sections/03_design.tex
 M journal_article/sections/04_results.tex
 M journal_article/sections/05_discussion.tex
 M journal_article/sections/06_conclusion.tex
 M journal_article/supplementary/A_numerical_domain.tex
 M journal_article/supplementary/D_implementation.tex
 M journal_validation/publication_review/BATCH2_CHANGE_REPORT.md
?? journal_article/qa/batch4/
?? journal_article/sections/data_availability.tex
?? journal_article/sections/submission_declarations.tex
?? journal_article/supplementary/D_evidence_map.tex
?? journal_validation/publication_review/BATCH3_CHANGE_REPORT.md
?? journal_validation/publication_review/BATCH4_CHANGE_REPORT.md
```

## Complete Batch 4 source/document Git diff

Actual `git diff --no-index` output against captured pre-batch copies, with temporary prefixes normalized to repository-relative paths. New files are compared to `/dev/null`. It includes every modified/new reviewable source/document file for Batch 4; generated ignored build/render artifacts are inventoried above rather than recursively embedded. This report is not embedded in its own diff.

```diff
diff --git a/journal_article/main.tex b/journal_article/main.tex
index 8fdde7ba..a0362869 100644
--- a/journal_article/main.tex
+++ b/journal_article/main.tex
@@ -1,21 +1,22 @@
 % Compile from journal_article/: pdflatex main; biber main; pdflatex main; pdflatex main
 \input{preamble}
-\title{High-Dimensional Instrumental Variable Quantile Regression under Weak Instruments: A Monte Carlo Study}
-% Shared affiliation and individual contact details; no corresponding author.
+\title{Controlled Instrument-Relevance Sensitivity in High-Dimensional IVQR: A Monte Carlo Study}
+% Named master; author order, affiliations and corresponding author require confirmation.
 \author{\begin{minipage}{\dimexpr\textwidth-2\tabcolsep\relax}\centering
-\normalsize OLIMJON UMIDJON UGLI UMURZOKOV\textsuperscript{a}\\
+\normalsize OLIMJON UMIDJON UGLI UMURZOKOV\\
 \small ORCID: \href{https://orcid.org/0009-0008-0090-7100}{0009-0008-0090-7100}\\
 Email: \href{mailto:olimumurzokov022@gmail.com}{olimumurzokov022@gmail.com}\\[0.7em]
-\normalsize UMIDJON UMIRZAKOVICH KOSTAEV\textsuperscript\\
+\normalsize UMIDJON UMIRZAKOVICH KOSTAEV\\
 \small ORCID: \href{https://orcid.org/0009-0000-0205-5142}{0009-0000-0205-5142}\\
 Email: \href{mailto:umidjonkostaev2025@gmail.com}{umidjonkostaev2025@gmail.com}\\[0.7em]
 \end{minipage}}
 \date{}
-\hypersetup{pdftitle={High-Dimensional IVQR under Weak Instruments},pdfauthor={UMIDJON UMIRZAKOVICH KOSTAEV; OLIMJON UMIDJON UGLI UMURZOKOV}}
+\hypersetup{pdftitle={Controlled Instrument-Relevance Sensitivity in High-Dimensional IVQR: A Monte Carlo Study},pdfauthor={UMIDJON UMIRZAKOVICH KOSTAEV; OLIMJON UMIDJON UGLI UMURZOKOV}}
 \begin{document}
 \maketitle
+\noindent\textit{\{Monte Carlo simulation assesses instrument-relevance sensitivity in high-dimensional IVQR.\}}\par\medskip
 \begin{abstract}
-We study how weakening instrument relevance changes point accuracy, test calibration and inferential informativeness in high-dimensional instrumental variable quantile regression (IVQR). Extending the fixed-relevance Monte Carlo design of Chen, Huang, and Tien (2021), we scale the excluded signal and add independent compensating noise, preserving the joint distribution of treatment and the outcome disturbance under the stated Gaussian construction. We compare preserved Oracle-GMM, Full-GMM and double/debiased machine learning IVQR (DML-IVQR) implementations across four relevance settings, five quantiles and sample sizes of 500 and 1000, with 500 replications per design; no new estimator or theorem is proposed. At $n=1000$, $\tau=0.50$ and $\kappa=0.10$, DML-IVQR has direct-at-truth acceptance $0.942$, a median grid-based accepted measure of $3.900$ out of $4$, and rejection probability $0.094$ at the false candidate $\alpha_0(\tau)+0.50$. These distinct measures show that nominal-looking truth acceptance can coexist with little exclusion of false effects; the acceptance frequency is not membership coverage of the stored finite-grid set. Oracle-GMM also deteriorates as relevance weakens. DML--Full RMSE rankings have exceptions, and substantial undercoverage occurs in several strong-relevance cells. Findings concern historical implementations with density proxies, differing residualization, no cross-fitting and numerical sensitivity documented in selected-case audits. Their nominal chi-square inference is not validated, and the comparisons do not isolate the effect of regularization.
+We study how weakening instrument relevance changes point accuracy, test calibration and inferential informativeness in high-dimensional instrumental variable quantile regression (IVQR). Extending the fixed-relevance Monte Carlo design of Chen, Huang, and Tien (2021), we scale the excluded signal and add independent compensating noise, preserving the joint treatment/outcome-disturbance distribution under the stated Gaussian construction. We compare preserved Oracle-GMM, Full-GMM and double/debiased machine learning IVQR (DML-IVQR) implementations across four relevance settings, five quantiles and sample sizes of 500 and 1000, with 500 replications per design. The contribution is a controlled sensitivity experiment, with no new estimator or theorem. At $n=1000$, $\tau=0.50$ and $\kappa=0.10$, DML-IVQR has direct-at-truth acceptance $0.942$, median grid-based accepted measure $3.900$ out of $4$, and rejection probability $0.094$ at the false candidate $\alpha_0(\tau)+0.50$. These different measures show that nominal-looking truth acceptance can coexist with little exclusion of false effects; direct acceptance is not membership coverage of the stored finite-grid set. Oracle-GMM also deteriorates under weaker relevance. DML--Full RMSE rankings have exceptions, and several strong-relevance cells exhibit substantial undercoverage. The comparisons do not isolate regularization. Non-finite mixed-density regularity, density proxies, differing residualization, same-sample fitting without cross-fitting, penalty randomness and selected-case numerical sensitivity limit interpretation; validity of the implemented nominal chi-square inference remains unestablished.
 \end{abstract}
 \noindent\textbf{Keywords:} instrumental variable quantile regression; double machine learning; weak instruments; Monte Carlo simulation; confidence-set informativeness
 \input{sections/01_introduction}
@@ -24,6 +25,7 @@ We study how weakening instrument relevance changes point accuracy, test calibra
 \input{sections/04_results}
 \input{sections/05_discussion}
 \input{sections/06_conclusion}
+\input{sections/submission_declarations}
 \input{sections/data_availability}
 \FloatBarrier
 \printbibliography[title={References}]
diff --git a/journal_article/preamble.tex b/journal_article/preamble.tex
index ef5c47ab..de646de3 100644
--- a/journal_article/preamble.tex
+++ b/journal_article/preamble.tex
@@ -13,6 +13,7 @@
 \usepackage{csquotes}
 \usepackage[backend=biber,style=authoryear,maxcitenames=2,maxbibnames=99,doi=true,isbn=false,url=false]{biblatex}
 \addbibresource{references.bib}
+\usepackage{xurl}
 \usepackage[hidelinks]{hyperref}
 \usepackage{microtype}
 \SetTblrInner[booktabs]{width=\textwidth,row{1}={font=\bfseries},hline{1,Z}={0.8pt},hline{2}={0.4pt}}
diff --git a/journal_article/sections/01_introduction.tex b/journal_article/sections/01_introduction.tex
index 5d82637e..a7d3105d 100644
--- a/journal_article/sections/01_introduction.tex
+++ b/journal_article/sections/01_introduction.tex
@@ -11,4 +11,4 @@ The paper makes three empirical contributions. First, it specifies a controlled
 
 The preserved DML-IVQR implementation has lower RMSE than the preserved Full-GMM implementation in 35 of the 40 matched designs, with documented exceptions. Differences in nuisance dimension, residualization and computational details prevent attributing this comparison to regularization alone. Oracle-GMM also deteriorates under weaker relevance, so high-dimensional nuisance estimation is not the sole explanation. Strong-relevance undercoverage limits any reading of nominal-looking acceptance as validated inference.
 
-The findings concern one DGP family and historical implementations using density proxies, differing residualization, same-sample nuisance fits and fresh penalty draws. The original DGP has a non-finite population density weight. Implemented orthogonality, validity of the nominal chi-square cutoff and transfer of theoretical weak-identification robustness remain unestablished; absence of cross-fitting alone does not prove invalidity. Selected-case audits document residual-rank and decision sensitivity, not a full-experiment error frequency (Appendix~\ref{app:reproducibility}). Historical results are retained, and finite-grid diagnostics establish no unrestricted confidence-set geometry.
+The findings concern one DGP family and historical implementations with a non-finite mixed residual density, density proxies, differing residualization, same-sample fits and fresh penalty draws. Implemented orthogonality, nominal chi-square validity and transfer of theoretical weak-identification robustness remain unestablished; missing cross-fitting alone does not prove invalidity. Appendix~\ref{app:reproducibility} documents selected-case rank/decision sensitivity, not a full-experiment error frequency. Historical results are retained, and finite grids establish no unrestricted confidence-set geometry.
diff --git a/journal_article/sections/02_framework.tex b/journal_article/sections/02_framework.tex
index efe704fa..a15e9a42 100644
--- a/journal_article/sections/02_framework.tex
+++ b/journal_article/sections/02_framework.tex
@@ -32,7 +32,7 @@ The treatment coefficient $\alpha_0(\tau)$ is the target. The intercept and cont
 \end{equation}
 Instrument validity supports this restriction; identification additionally requires variation that distinguishes alternative treatment coefficients.
 
-For candidate $a$, define $\widetilde X_i=(1,X_i')'$, $\rho_\tau(v)=v[\tau-\mathbf1\{v<0\}]$, and the population nuisance profile
+For candidate $a$, define $\widetilde X_i=(1,X_i')'$, $\rho_\tau(v)=v[\tau-\mathbf1\{v<0\}]$, and a population nuisance profile (under the reference conditions, assume uniqueness or a fixed measurable selection from the minimizers)
 \begin{equation}
     \begin{pmatrix}
         c(a)\\
@@ -80,7 +80,7 @@ For candidate $a$, define $\widetilde X_i=(1,X_i')'$, $\rho_\tau(v)=v[\tau-\math
     =Z_i-d_0(a)-\Gamma(a)X_i.
     \label{eq:profile-residualized-instrument}
 \end{equation}
-Here $f_{\epsilon(a)}(0\mid X_i,Z_i)$ is the conditional residual density at zero. With $\eta=(c,\beta',\operatorname{vec}(\delta)')'$, let $\eta(a)$ collect the candidate-specific profile and $\eta_0=\eta(\alpha_0(\tau))$. The ideal score below is a theoretical reference:
+Here $f_{\epsilon(a)}(0\mid X_i,Z_i)$ is the conditional residual density at zero. With $\eta=(c,\beta',\operatorname{vec}(\delta)')'$, let $\eta(a)$ collect the candidate-specific profile and $\eta_0=\eta(\alpha_0(\tau))$. Let $W_i=(Y_i,D_i^{\prime},X_i^{\prime},Z_i^{\prime})^{\prime}$ collect an observation; it is distinct from the scalar candidate statistic $W_{e,n}(a)$ below. The ideal score is a theoretical reference:
 \begin{equation}
     \begin{aligned}
         g_{\tau}(W_i;a,\eta)
@@ -132,7 +132,7 @@ The quantile-Lasso objective is an unscaled sum of check losses plus one half of
 
 Nuisances and scores use the same observations, with no sample splitting or cross-fitting. Fresh pivotal draws are generated at each penalty call, introducing algorithmic randomness across candidate evaluations. Appendix~\ref{app:reproducibility} records the penalty formulas, residualization rules, and environment details. The estimator comparison encompasses these implementation differences as well as regularization and nuisance dimension; it cannot isolate the effect of regularization alone.
 
-The executed procedures use implementation-specific density proxies, residualization and nuisance estimation, so the ideal orthogonality calculation does not establish orthogonality or an inference theorem for these implementations. The absence of cross-fitting alone is not proof of invalidity; the required same-sample nuisance and generated-score conditions have not been established here.
+These implementation differences prevent automatic transfer of the ideal orthogonality calculation or its inference theory. Absence of cross-fitting alone does not prove invalidity; the same-sample nuisance and generated-score conditions remain unestablished.
 
 For estimator $e$, let $\widehat g_{e,i}(a)$ be its score. The common criterion uses the uncentered score second moment:
 \begin{equation}
diff --git a/journal_article/sections/03_design.tex b/journal_article/sections/03_design.tex
index 03d0fdc3..ca7fc079 100644
--- a/journal_article/sections/03_design.tex
+++ b/journal_article/sections/03_design.tex
@@ -186,6 +186,6 @@ Let $I_r(a_j)=\mathbf1\{W_{n,r}(a_j)\le c_{0.95}\}$. The accepted-set measure is
     \left[I_r(a_j)+I_r(a_{j+1})\right].
   \label{eq:accepted-measure}
 \end{equation}
-This trapezoidal sum of binary acceptance indicators ranges from zero to four. Adjacent intervals contribute 0, 0.05, or 0.10; the calculation totals separated accepted components without solving for exact critical-value crossings. It is neither the span between extreme accepted values nor unrestricted confidence-region length. Full-grid acceptance requires acceptance at all 41 points; either-boundary acceptance requires acceptance at at least one endpoint. Neither event establishes acceptance between all points or outside the domain.
+This trapezoidal sum of binary acceptance indicators ranges from zero to four. Adjacent intervals contribute 0, 0.05, or 0.10; the calculation summarizes grid acceptance, allowing multiple accepted grid runs, without locating continuous boundaries. It is a quadrature summary, not the Lebesgue length of the finite accepted set, the span between extreme accepted values, or unrestricted confidence-region length. Full-grid acceptance requires acceptance at all 41 points; either-boundary acceptance requires acceptance at at least one endpoint. Neither event establishes acceptance between all points or outside the domain.
 
 Appendix~\ref{app:numerical-domain-diagnostics} examines $A_1=[-3,5]$ and $A_2=[-5,7]$ at spacing 0.1 in a separate 100-replication diagnostic with $n=1000$, all quantiles and estimators, and $\kappa\in\{1,0.25,0.10\}$. It reuses saved samples and interior profiles while adding candidates. Coverage and power remain separate direct evaluations. This bounded diagnostic assesses numerical localization over investigated ranges only.
diff --git a/journal_article/sections/05_discussion.tex b/journal_article/sections/05_discussion.tex
index 941d68b9..3e02df00 100644
--- a/journal_article/sections/05_discussion.tex
+++ b/journal_article/sections/05_discussion.tex
@@ -1,17 +1,10 @@
 \section{Discussion}
-
 \label{sec:results-overall-interpretation}
 
-Taken together, the results show that weakening instrument relevance changes each dimension of finite-sample performance, but not in the same way. Point accuracy deteriorates systematically, accepted sets expand, and power against false candidate values generally declines, subject to the documented small reversals. Coverage is less systematic and can move toward its nominal level precisely when the procedure rejects few candidates. Near-nominal coverage can therefore coexist with low power and acceptance of most or all of the numerical domain. Accuracy, calibration, power, and informativeness measure different features of the procedure, and no one of them is sufficient to assess inference.
-
-The estimator comparison reinforces this interpretation. Oracle-GMM knows the designated relevant controls, yet its point accuracy, power, and accepted-set localisation still deteriorate as relevance declines. High-dimensional nuisance estimation therefore cannot be the sole explanation for the common relevance pattern. The preserved DML-IVQR implementation usually has lower RMSE than the preserved Full-GMM implementation, but the documented exceptions and the separate coverage and power results rule out uniform superiority. Oracle is likewise an infeasible benchmark rather than a guaranteed finite-sample winner. Because the implementations differ in nuisance dimension, regularisation, and residualisation details, these are comparisons among complete estimator implementations; they do not isolate the causal effect of regularisation.
-
-Sample size and quantile comparisons require similar qualifications. Increasing $n$ from 500 to 1000 lowers RMSE in all 60 matched comparisons and typically narrows accepted sets and raises power where usable signal remains. It does not improve every inferential dimension: several strong-relevance DML coverage rates deteriorate substantially, and power has documented exceptions. Across quantiles, the lower-tail biases are uniformly negative and the upper-tail biases uniformly positive under the convention $\mathrm{Bias}=\alpha_0-\widehat\alpha$. At fixed estimator, $n$, and $\kappa$, both MAE and RMSE are lower at the median than at either tail throughout the final results, whereas coverage has no corresponding universal centre-versus-tail ordering. Results at two sample sizes establish finite-sample contrasts, not an asymptotic rate or limit.
-
-Neyman orthogonality is designed to reduce first-order sensitivity to small nuisance-estimation errors \parencite{chernozhukov_et_al_2018}, while candidate-specific test inversion is designed to avoid relying on a precisely estimated structural coefficient under weak identification \parencite{chernozhukov_hansen_2008}. Neither property creates identifying variation. Subject to its assumptions and regularity conditions, weak-identification-robust construction concerns validity of testing a candidate; it does not promise a narrow confidence region or high power when many false candidates are observationally difficult to distinguish. The DML-IVQR framework of \textcite{chen_huang_tien_2021} combines high-dimensional nuisance estimation with this style of candidate-specific inference, but the present simulations evaluate the preserved executable procedure. They do not validate the ideal asymptotic theory.
+The experiment distinguishes retaining a true candidate from excluding false effects. As relevance weakens, direct-at-truth acceptance can approach the nominal level while false-candidate rejection falls and most of the grid remains accepted. A lower RMSE likewise need not imply better test calibration. The strong-relevance undercoverage and documented power reversals in Section~\ref{chap:results} remain material: neither nominal-looking acceptance nor a favourable point-estimation ranking establishes reliable and informative inference.
 
-The population density weight at the true parameter encounters the non-finite regularity problem derived in Section~\ref{sec:framework}. The executable estimators instead use the fitted-normal density proxy and implementation-specific residualisation rules in Section~\ref{sec:implementation}; Appendix~\ref{app:reproducibility} further records that the preserved \texttt{dnorm} call supplies the residual variance in the argument position interpreted by R as a standard deviation. DML uses the same sample for nuisances and scores rather than cross-fitting, and its pivotal penalty generates fresh draws across evaluations. All three estimators use an asymptotic chi-square reference cutoff, while their empirical sizes differ. These features qualify the relationship between the experiment and the theoretical procedures, but the design does not vary them separately. None can therefore be identified as the cause of a particular distortion, and the results do not establish that changing one feature would remove it.
+Oracle-GMM also loses accuracy and numerical localization despite knowing the designated relevant controls. High-dimensional nuisance estimation is therefore not the sole explanation for deterioration. The preserved DML-IVQR implementation often has lower RMSE than preserved Full-GMM, with exceptions, but the procedures differ in nuisance dimension, regularization and residualization. Their comparison does not identify a regularization mechanism or establish uniform superiority. The larger sample improves point accuracy without improving every inferential measure; quantile patterns in bias and point error do not imply a corresponding calibration ordering. The complete cell evidence is mapped in Appendix~\ref{app:evidence-map}.
 
-The numerical and design scope imposes further limits. Point estimates minimize a 41-point profile and hence reflect its resolution, endpoints, and first-tie rule. The accepted-set measure is restricted to $A_0=[-1,3]$ and cannot describe acceptance outside that domain; Appendix~\ref{app:numerical-domain-diagnostics} shows that accepted measure and boundary acceptance can continue to grow on wider investigated domains under weak relevance. Those diagnostics establish limited numerical localisation over the ranges examined, not global unboundedness or non-identification. More broadly, the evidence comes from one DGP family, five quantiles, two sample sizes, four relevance settings, and three preserved estimator implementations. It cannot establish how every alternative DGP, implementation, or larger sample would behave.
+The ideal theory supplies motivation rather than a validated description of the executed tests. Orthogonality concerns nuisance sensitivity under its conditions \parencite{chernozhukov_et_al_2018}; weak-identification-robust candidate testing concerns validity under its own conditions, not guaranteed power \parencite{chernozhukov_hansen_2008}. Here the mixed residual density is non-finite (Appendix~\ref{app:density-divergence}), while the implementations use density proxies, differing residualization, same-sample nuisance fits and fresh pivotal penalties. Their nominal chi-square validity remains unestablished. Absence of cross-fitting alone does not prove invalidity, and these features were not varied separately to identify a cause of the observed distortions. Selected-case audits also document residual-rank and decision sensitivity; they neither provide a full-experiment error frequency nor replace historical results (Appendix~\ref{app:reproducibility}).
 
-The bounded implication is therefore to distinguish what can be assessed in a simulation from what can be established in an empirical application. A procedure can produce a more accurate point estimate while remaining poorly calibrated, attain coverage near the nominal level while excluding few false candidates, or show a finite-domain measure near its ceiling without establishing the shape of an unrestricted confidence region. Simulation evaluations should report accuracy, calibration, power, and informativeness jointly. In empirical applications, researchers should disclose numerical-domain sensitivity and the assumptions underlying inference; nominal confidence levels alone do not establish finite-sample reliability. Within the scope of this experiment, that distinction gives the clearest account of what is lost as instrument relevance weakens.
+The practical implication is joint reporting of point accuracy, direct-test calibration diagnostics, false-candidate rejection and finite-grid informativeness. The trapezoidal accepted measure summarizes binary grid decisions; it does not locate continuous boundaries. Wider-domain diagnostics reveal limited localization over the examined ranges, not global unboundedness or non-identification. One DGP family, five quantiles, two sample sizes and three preserved implementations delimit the evidence. No particular numerical or statistical correction is shown to restore calibration, and two sample sizes establish no asymptotic rate. In applications, domain sensitivity and the maintained inference assumptions should accompany the nominal confidence level.
diff --git a/journal_article/sections/06_conclusion.tex b/journal_article/sections/06_conclusion.tex
index b6a49147..af65abb3 100644
--- a/journal_article/sections/06_conclusion.tex
+++ b/journal_article/sections/06_conclusion.tex
@@ -1,6 +1,6 @@
 \section{Conclusion}
-This study extends the fixed-relevance design of \textcite{chen_huang_tien_2021} by reducing excluded-instrument signal while independent compensating noise preserves the joint treatment/outcome-disturbance distribution under the stated Gaussian construction. Joint assessment of three preserved high-dimensional IVQR implementations distinguishes point accuracy, direct-test acceptance, false-candidate rejection and finite-grid informativeness. Oracle-GMM also deteriorates under weaker relevance, so high-dimensional nuisance estimation cannot be the sole explanation.
+This controlled extension of the fixed-relevance design of \textcite{chen_huang_tien_2021} reduces excluded-instrument signal while independent compensating noise preserves the joint treatment/outcome-disturbance distribution under the stated Gaussian construction. Comparing three preserved high-dimensional IVQR implementations shows why point accuracy, direct-test acceptance, false-candidate rejection and finite-grid informativeness must be assessed together. Oracle-GMM also deteriorates under weaker relevance, so high-dimensional nuisance estimation cannot be the sole explanation.
 
-Nominal-looking truth acceptance can coexist with retention of most of the grid and little rejection of false effects. It is not membership coverage of the stored finite-grid set; separate DML penalty draws can distinguish the two computations. Strong-relevance undercoverage also precludes a finite-sample guarantee. The preserved DML-IVQR implementation often has lower RMSE than preserved Full-GMM, with documented exceptions, but nuisance dimensions, residualization and computational details also differ. This comparison does not isolate regularization.
+The central empirical disagreement is between nominal-looking truth acceptance and useful exclusion of false effects. Retaining most of a grid while rejecting few false candidates offers little discrimination. Direct-at-truth acceptance is not membership coverage of the stored randomized grid set, and strong-relevance undercoverage remains a counterpoint to near-nominal rates elsewhere. Implementation-level RMSE advantages have documented exceptions and do not isolate regularization.
 
-The historical results establish neither implemented orthogonality nor validity of nominal chi-square inference or automatic transfer of theoretical weak-identification robustness. Density-weight regularity, the implemented proxies/residualization, same-sample fits and penalty randomness remain limitations; missing cross-fitting alone does not prove invalidity. Selected numerical audits document rank and decision sensitivity: certificates concern specified objectives and inputs, not invariance of every historical decision or a full-experiment error frequency. Historical results remain unchanged; finite grids establish no unrestricted confidence-set geometry, and no particular correction is shown to restore calibration.
+These findings establish neither implemented orthogonality nor validity of the nominal chi-square cutoff or automatic transfer of theoretical weak-identification robustness. The non-finite mixed density, proxy/residualization choices, same-sample fitting and penalty randomness limit that link; selected numerical audits additionally show rank and decision sensitivity within a specified panel. Their certificates do not establish invariance of historical decisions or a full-experiment error frequency. Historical results are retained, finite grids establish no unrestricted confidence-set geometry, and no particular correction is shown to restore calibration.
diff --git a/journal_article/sections/data_availability.tex b/journal_article/sections/data_availability.tex
index c49b21eb..3c5b3fc3 100644
--- a/journal_article/sections/data_availability.tex
+++ b/journal_article/sections/data_availability.tex
@@ -1,4 +1,4 @@
 \section*{Data and code availability}
-The public repository is \url{https://github.com/U-Olim/DML-IVQR_Master_Thesis}. Repository visibility, commit \texttt{15b8b4dc95e3658f3b858a6f792ea2983299aaa6}, and directory listings for the main frozen CSVs, reporting summaries and package archives were checked through the GitHub API on 10 November 2026. Readers can select that commit and follow the exact paths in Appendix~\ref{app:evidence-map} to inspect both sample sizes, all quantiles and relevance settings without running an estimator. These are simulated data and archived computational outputs, not an external observational dataset. The freeze record names \texttt{ac9a9ccad027cde05488abb633e66cc02f87cc46}; that identifier was not resolvable in the present local object store and returned HTTP 404 from the repository API. It is retained as recorded provenance, not offered as a verified release checkout.
+The public repository is \url{https://github.com/U-Olim/DML-IVQR_Master_Thesis}. Repository visibility, commit \path{15b8b4dc95e3658f3b858a6f792ea2983299aaa6}, and directory listings for the main frozen CSVs, reporting summaries and package archives were checked through the GitHub API on 10 November 2026. That commit supplies the accessible evidence archive, not the current uncommitted manuscript revision. Readers can select it and follow the exact paths in Appendix~\ref{app:evidence-map} to inspect both sample sizes, all quantiles and relevance settings without running an estimator. These are simulated data and archived computational outputs, not an external observational dataset. The freeze record names \path{ac9a9ccad027cde05488abb633e66cc02f87cc46}; that identifier was not resolvable in the present local object store and returned HTTP 404 from the repository API. It is retained as recorded provenance, not offered as a verified release checkout.
 
 Historical rerunning is a different task. Source and configuration are under \path{thesis_extension/src/} and \path{thesis_extension/config/}; environment records, package archives and the captured Windows library are under \path{thesis_extension/environment/}. The recorded environment uses R~3.4.3 and pinned historical packages (Appendix~\ref{app:reproducibility}); their presence does not establish installation portability or exact random-number replay. Main-run worker-specific penalty states are not recoverable from the parent seed alone. Large grid-diagnostic profiles and saved primitives are local, Git-ignored artifacts identified in \path{thesis_extension/diagnostics/grid_sensitivity/GRID_RESULTS_MANIFEST.csv}; tracked diagnostic summaries remain available. Stage 2H pilot outputs under \path{journal_validation/stage2h/pilot/runs/} and its \path{journal_validation/stage2h/pilot/SHA256_MANIFEST.json} are also Git-ignored and are not part of the public tracked archive. No public deposit of these local artifacts or portable historical runtime is established here. This revision does not publish new results or replace historical fits with later certified numerical solutions.
diff --git a/journal_article/supplementary/A_numerical_domain.tex b/journal_article/supplementary/A_numerical_domain.tex
index 9b48a65c..2922421d 100644
--- a/journal_article/supplementary/A_numerical_domain.tex
+++ b/journal_article/supplementary/A_numerical_domain.tex
@@ -13,7 +13,7 @@ The interval also contains the true structural quantile effects for all five inv
 \]
 so the true effects are approximately \(-0.282\), \(0.326\), \(1.000\), \(1.674\), and \(2.282\) for \(\tau=0.10,0.25,0.50,0.75,\) and \(0.90\), respectively. All five structural truths lie strictly inside \(A_0\); using their unrounded values, the minimum distance to either endpoint is approximately \(0.718\). The interval should therefore be understood as a common numerical search domain, not as an assumed theoretical parameter space.
 
-A finite search domain can nevertheless become restrictive when instruments are weak and many candidate values are accepted. For this reason, a separate sensitivity diagnostic expands the search range from \(A_0=[-1,3]\) to \(A_1=[-3,5]\) and then to \(A_2=[-5,7]\). Under strong instrument relevance, expanding the domain adds little accepted measure, indicating that the observed accepted components are well localized within the investigated ranges. At intermediate relevance, the wider domains contain additional accepted values in some profiles. Under the weakest relevance setting, the accepted measure continues to increase as the domain is expanded and does not stabilize within \(A_2\).
+A finite search domain can nevertheless become restrictive when instruments are weak and many candidate values are accepted. For this reason, a separate sensitivity diagnostic expands the search range from \(A_0=[-1,3]\) to \(A_1=[-3,5]\) and then to \(A_2=[-5,7]\). Under strong instrument relevance, expanding the domain adds little accepted measure, indicating that accepted grid values are well localized within the investigated ranges, without establishing continuous accepted components. At intermediate relevance, the wider domains contain additional accepted values in some profiles. Under the weakest relevance setting, the accepted measure continues to increase as the domain is expanded and does not stabilize within \(A_2\).
 
 These results clarify the interpretation of the main accepted-set measure. A value close to four in \(A_0\) means that almost the entire four-unit primary domain is accepted; it does not mean that the unrestricted confidence region has length four. Similarly, continued acceptance in the wider domains indicates poor numerical localization over the ranges examined, but it does not by itself establish that the theoretical confidence region is globally unbounded or that identification completely fails.
 
diff --git a/journal_article/supplementary/D_evidence_map.tex b/journal_article/supplementary/D_evidence_map.tex
index 6ee1edac..e63aec65 100644
--- a/journal_article/supplementary/D_evidence_map.tex
+++ b/journal_article/supplementary/D_evidence_map.tex
@@ -1,6 +1,6 @@
 \subsection{Frozen-evidence map}
 \label{app:evidence-map}
-All paths below are repository-relative. Select commit \texttt{15b8b4dc95e3658f3b858a6f792ea2983299aaa6} for the tracked archive. The keys connect the principal findings to complete saved evidence, including cells omitted from compact main-text displays. This map identifies sources; it does not recompute descriptive comparison counts or rerun historical checks.
+All paths below are repository-relative. The checked accessible evidence revision is \texttt{15b8b4dc}; it is distinct from both the unresolved historical freeze identifier and the current uncommitted manuscript revision. Full identifiers and access limitations appear in the data and code availability statement. Keys E1--E6 connect the principal findings to saved evidence, including cells omitted from compact main-text displays. This map identifies sources; it does not recompute descriptive comparison counts or rerun historical checks.
 
 \begin{center}
 \small
@@ -15,10 +15,12 @@ Selected-case rank and decision sensitivity & Appendix~\ref{app:reproducibility}
 \end{tblr}
 \end{center}
 
+\begingroup\small\raggedright
+\Urlmuskip=0mu plus 1mu\relax
 \begin{description}
 \item[E1: Relevance.] \path{thesis_extension/calibration/instrument_strength_100rep/kappa_strength_summary.csv}; presentation: \path{journal_article/tables/table_strength_calibration.tex}.
 
-\item[E2: Full performance, both sample sizes.] \path{thesis_extension/final/output/n500/summary.csv} and \path{thesis_extension/final/output/n1000/summary.csv} contain Bias, MAE, RMSE, historical \texttt{Coverage}/\texttt{Size}, accepted-measure and boundary/full-grid summaries. Replication-level sources are \path{thesis_extension/final/output/n500/results.csv} and \path{thesis_extension/final/output/n1000/results.csv}; stored candidate statistics are \path{thesis_extension/final/output/n500/profiles.csv} and \path{thesis_extension/final/output/n1000/profiles.csv}. Full presentation assets: \path{journal_article/tables/generated/appendix_point_performance.tex}, \path{journal_article/tables/generated/appendix_coverage.tex}, and \path{journal_article/tables/generated/appendix_cr_informativeness.tex}; compact table: \path{journal_article/tables/table_main_performance.tex}. Existing RMSE images are \path{journal_article/figures/generated/rmse_n500.png} and \path{journal_article/figures/generated/rmse_n1000.png}.
+\item[E2: Full performance.] \path{thesis_extension/final/output/n500/summary.csv} and \path{thesis_extension/final/output/n1000/summary.csv} contain Bias, MAE, RMSE, historical \texttt{Coverage}/\texttt{Size}, accepted-measure and boundary/full-grid summaries. Replication-level sources are \path{thesis_extension/final/output/n500/results.csv} and \path{thesis_extension/final/output/n1000/results.csv}; stored candidate statistics are \path{thesis_extension/final/output/n500/profiles.csv} and \path{thesis_extension/final/output/n1000/profiles.csv}. Full presentation assets: \path{journal_article/tables/generated/appendix_point_performance.tex}, \path{journal_article/tables/generated/appendix_coverage.tex}, and \path{journal_article/tables/generated/appendix_cr_informativeness.tex}; compact table: \path{journal_article/tables/table_main_performance.tex}. Existing RMSE images are \path{journal_article/figures/generated/rmse_n500.png} and \path{journal_article/figures/generated/rmse_n1000.png}.
 
 \item[E3: Truth testing and power.] Use E2's \texttt{Coverage}, \texttt{Size} and replication \texttt{W\_true} fields for direct-at-truth evaluations. False-candidate summaries are \path{thesis_extension/final/output/n500/power_summary.csv} and \path{thesis_extension/final/output/n1000/power_summary.csv}; replication records are \path{thesis_extension/final/output/n500/power.csv} and \path{thesis_extension/final/output/n1000/power.csv}. Full presentation: \path{journal_article/tables/generated/appendix_power.tex}; figures: \path{journal_article/figures/generated/coverage_heatmap.pdf} and \path{journal_article/figures/generated/power_median_combined.pdf}. The abstract's $0.942/3.900/0.094$ contrast selects E2's \texttt{Coverage}/\texttt{median\_grid\_accepted\_set\_measure} and this power summary's \texttt{power}, respectively, at $n=1000$, $\tau=0.50$, $\kappa=0.10$, estimator \texttt{DML-IVQR-BC}, with $\Delta=0.50$ for power only. These are different summaries, not a joint event or validated grid-set coverage.
 
@@ -28,4 +30,5 @@ Selected-case rank and decision sensitivity & Appendix~\ref{app:reproducibility}
 
 \item[E6: Numerical sensitivity.] \path{journal_validation/stage2g/full_path_validation/FULL_PATH_REPORT.md} records the selected 24-problem comparison and five Policy A/C decision differences. \path{journal_validation/stage2g/deterministic_implementation/DETERMINISTIC_IMPLEMENTATION_REPORT.md} and \path{journal_validation/stage2g/deterministic_implementation/IMPLEMENTATION_CONTRACT_v1.md} specify the fixed-objective and input scope of later certificates. Earlier rank-stability evidence is in \path{journal_validation/stage2c/stability/STABILITY_REPORT.md}. These reports are not population error rates or replacements for E2--E5.
 \end{description}
+\endgroup
 The inventories \path{thesis_extension/reporting/EMPIRICAL_RESULTS_MANIFEST.csv} and \path{thesis_extension/reporting/REPORTING_OUTPUT_MANIFEST.csv} retain historical input/output hashes and provenance. An entry in a manifest alone does not establish public availability: local-only exclusions are stated in the data and code availability statement.
diff --git a/journal_article/supplementary/D_implementation.tex b/journal_article/supplementary/D_implementation.tex
index 499a1aba..9539039e 100644
--- a/journal_article/supplementary/D_implementation.tex
+++ b/journal_article/supplementary/D_implementation.tex
@@ -3,7 +3,7 @@
 \label{app:reproducibility}
 \setcounter{equation}{0}\setcounter{table}{0}\setcounter{figure}{0}
 \subsection{Environment, records, and reproducibility limits}
-The computational archive is the project repository \url{https://github.com/U-Olim/DML-IVQR_Master_Thesis}. This reference identifies the archived workflow; it is not a claim of bit-for-bit regeneration from a seed on arbitrary systems. Preserved source is in \path{simulation/}, \path{Empirical_work/}, and \path{example/}; extension wrappers and configuration are in \path{thesis_extension/src/} and \path{thesis_extension/config/extension_config.R}. The empirical freeze records identifier \texttt{ac9a9ccad027cde05488abb633e66cc02f87cc46} (2 September 2026), whose checkout accessibility is unverified as explained in the data and code availability statement; the checked tracked archive is commit \texttt{15b8b4dc95e3658f3b858a6f792ea2983299aaa6}.
+The computational archive is the project repository \url{https://github.com/U-Olim/DML-IVQR_Master_Thesis}. This reference identifies the archived workflow; it is not a claim of bit-for-bit regeneration from a seed on arbitrary systems. Preserved source is in \path{simulation/}, \path{Empirical_work/}, and \path{example/}; extension wrappers and configuration are in \path{thesis_extension/src/} and \path{thesis_extension/config/extension_config.R}. The checked accessible evidence archive is commit \texttt{15b8b4dc}; it contains the earlier editorial batches. Current manuscript revisions are local and uncommitted. The freeze record's historical identifier \texttt{ac9a9cca} (2 September 2026) remains unresolved; full identifiers and access limits appear in the data and code availability statement.
 
 The canonical environment is R~3.4.3 (30 November 2017) on 64-bit Windows, using five workers. The captured attached packages are \texttt{doSNOW} 1.0.16, \texttt{snow} 0.4-2, \texttt{iterators} 1.0.8, \texttt{foreach} 1.4.3, \texttt{mvtnorm} 1.0-6, \texttt{hqreg} 1.4, \texttt{hdm} 0.2.0, \texttt{quantreg} 5.34, and \texttt{SparseM} 1.77. Environment session and library manifests are under \path{thesis_extension/environment/}. The main simulation uses seed 675; the grid diagnostic also uses seed 675, with saved primitives reloaded in Stage 2; calibration uses seed 20260813. Worker-specific RNG streams are not explicitly initialized in the preserved parallel DML procedure, so the parent seed alone does not establish exact regeneration of every penalty draw.
 
@@ -19,7 +19,7 @@ The operational source is \path{thesis_extension/src/run_extension.R}, with cand
 \begin{enumerate}
 \item Generate one set of primitives; construct a sample at each relevance setting. Within that setting all three estimators share $(Y,D,X,Z)$. Reusing primitives across settings does not hold realized $(Y,D)$ fixed.
 \item For each quantile and estimator, profile the ordered 41-point primary grid. At each DML candidate $a$, call \texttt{lambda\_BC\_author} afresh (1000 artificial uniform columns), then fit \texttt{quantreg::rq(y-a*D\string~X, method="lasso")} with the resulting penalty and an intercept. Refit nuisances at each candidate; there is no post-Lasso refit. Oracle and Full instead call unpenalized \texttt{quantreg::rq} with their designated controls.
-\item Form candidate outcome residuals and the proxy \texttt{dnorm(e, mean(e), var(e))}. For each DML instrument, call \texttt{hdm::rlasso(..., post=FALSE)} on square-root-proxy-transformed instruments and controls with an ordinary unpenalized intercept. Subtract the returned intercept and original-control slopes from the original instrument. Oracle and Full use the direct matrix residualization described below.
+\item Form candidate outcome residuals and the proxy \texttt{dnorm(e, mean(e), var(e))}. Residualize instruments using the DML transformed regressions or benchmark matrix rule below; numerical termination and last-used penalty conventions are specified once in Appendix~\ref{app:finite-solvers}.
 \item Apply the literal computed-residual rule $r_i=\mathbf1\{\widehat e_i\leq0\}$, with no residual tolerance. Set $s_i=\tau-r_i$, $g=\sum_i\widehat\Psi_i s_i$ and $S=\sum_i\widehat\Psi_i\widehat\Psi_i' s_i^2$. The statistic is $g'S^{-1}g$, equivalent to the normalized definition in Section~\ref{sec:framework}. Use direct \texttt{solve} and the retained nominal chi-square cutoff; singular or non-finite evaluations are failures, not acceptances.
 \item Retain the first grid minimum for the point estimate and the stored grid decisions for informativeness summaries. After profiling, separately evaluate the true effect and six specified false candidates. DML again invokes its candidate routine, with fresh pivotal draws, in a separate five-worker evaluation. Direct-at-truth acceptance and false-candidate rejection therefore do not reuse stored grid statistics, even when candidates coincide. Failed profiles receive no point estimate; the documented failure conventions remain in force.
 \end{enumerate}
@@ -29,7 +29,12 @@ The archived estimator includes both sample randomness and algorithmic penalty r
 \label{app:penalty-implementation}
 For each candidate, $b_0$ is the fitted outcome intercept and $b$ the slopes. In the preserved \texttt{rq.fit.lasso} augmented-observation implementation, the unscaled check-loss sum receives a penalty with factor $1/2$. The vector $\lambda^{rq}(a)$ is the supplied routine argument, including an intercept penalty. There is no post-Lasso refit. Let $s_k=(n^{-1}\sum_iX_{ik}^2)^{1/2}$; $U_{ir}$ are independent artificial Uniform$(0,1)$ draws, with $r=1,\ldots,1000$, and $\widehat Q_{0.9}$ is their empirical pivotal-statistic 90th percentile. Fresh draws are made on every penalty call. This is algorithmic randomness, not sample splitting.
 
-In the following formulas, $\phi(e;\mu,\sigma)$ denotes a normal density parameterized by standard deviation. The proxy supplies $\widehat\sigma_\epsilon^2$ in that argument: the preserved R call is \texttt{dnorm(e, mean(e), var(e))}. It evaluates a fitted-normal density at residuals rather than estimating the theoretical conditional density at zero. The instrument penalty is $\mathcal P_{j,a}(\gamma_j)=\sum_k\lambda^\Gamma_{jk}(a)|\gamma_{jk}|$, using default iterative heteroskedastic loadings. Its ordinary intercept is unpenalized; no post-Lasso refit is performed.
+In the following formulas, $\phi(e;\mu,\sigma)$ denotes a normal density parameterized by standard deviation. The proxy supplies $\widehat\sigma_\epsilon^2$ in that argument: the preserved R call is \texttt{dnorm(e, mean(e), var(e))}. It evaluates a fitted-normal density at residuals rather than estimating the theoretical conditional density at zero. The sample-variance convention is
+\[
+ \widehat\sigma_\epsilon^2(a)=\frac{1}{n-1}\sum_{i=1}^n
+ \left[\widehat\epsilon_i(a)-\widehat\mu_\epsilon(a)\right]^2.
+\]
+This variance, not its square root, is supplied as the normal scale; the historical convention is described, not corrected. The instrument penalty is $\mathcal P_{j,a}(\gamma_j)=\sum_k\lambda^\Gamma_{jk}(a)|\gamma_{jk}|$, using default iterative heteroskedastic loadings. Its ordinary intercept is unpenalized; no post-Lasso refit is performed.
 \begin{equation}
     \begin{pmatrix}
         \widehat b_0(a)\\
diff --git a/journal_article/README.md b/journal_article/README.md
index fb178a95..cd5ae4a9 100644
--- a/journal_article/README.md
+++ b/journal_article/README.md
@@ -1,13 +1,36 @@
-# Journal article
+# Journal article ? submission preparation
 
-Start with `main.pdf`. The review PDF contains the article, references, and online supplementary Appendices A–E. Supplement sources are under `supplementary/`; this keeps cross-references local and resolved. All figures, tables, and the bibliography needed for compilation are included. Simulation datasets are linked through the repository documentation, not copied here.
+`main.tex` is the named manuscript master. Its approved title is **Controlled Instrument-Relevance Sensitivity in High-Dimensional IVQR: A Monte Carlo Study**. Main sections are in `sections/`; `sections/submission_declarations.tex` contains visible author-confirmation placeholders, and `sections/data_availability.tex` distinguishes the checked evidence archive from local-only files and the unresolved historical freeze identifier.
 
-From this directory, run:
+The review document includes the article, references and supplementary **Appendices A?D**:
+
+- A: numerical-domain diagnostics, including the recorded candidate failure and finite-domain limits.
+- B: controlled-relevance construction and distributional invariances.
+- C: direct-at-truth coverage audit and its limits.
+- D: reproducibility/environment notes, the complete frozen-evidence map (`supplementary/D_evidence_map.tex`), historical evaluation sequence, penalty/proxy/residualization definitions, finite-solver limitations, retained mixed-density divergence and conditional ideal-score algebra.
+
+Existing figures, tables and bibliography are used directly. No simulation or statistical-result generation is part of the document build. Complete numerical table assets remain under `tables/generated/`; not all are input into the PDF. The evidence map identifies their frozen CSV sources.
+
+## Current document and build evidence
+
+The historical root `main.pdf` and `EDIT_REPORT.md` describe earlier revisions. Do not assume they match the current source. The Batch 4 document-only build and inspection artifacts are under `qa/batch4/`; consult [BATCH4_CHANGE_REPORT.md](../journal_validation/publication_review/BATCH4_CHANGE_REPORT.md) for actual results and remaining blockers. The current build target is `qa/batch4/main.pdf`; only a completed build and inspection establish its status.
+
+For an ordinarily configured TeX installation, run from this directory:
 
 ```powershell
 .\build.ps1
 ```
 
-Alternatively: `pdflatex main`, `biber main`, `pdflatex main`, `pdflatex main`. A working TeX installation with the packages in `preamble.tex` is required. `python verify_article.py` performs read-only integrity checks against the original project and writes `qa/validation.json`. It does not run simulations.
+That script runs pdfLaTeX, Biber and two further pdfLaTeX passes. It writes root document outputs, so preserve any historical PDF that is needed before rebuilding there. It does not run research code. A working installation with the packages in `preamble.tex`, including `xurl` for long repository paths, is required.
+
+Batch 4 uses `python qa/batch4/build_document.py` to keep document outputs and a job-local MiKTeX configuration under `qa/batch4/`, with package installation and TeX shell escape disabled. The helper is specific to this Windows MiKTeX installation, reads only selected existing configuration fields, and invokes the installed Biber binary directly. It neither repairs the global installation nor promises a portable runtime. Job-local runtime caches and intermediate files are Git-ignored.
+
+`verify_article.py` and the scripts in `qa/` are version-specific document checks. They can write QA outputs; they are not strictly read-only commands. Earlier `validation.json`, `revision_validation.json`, `revision_build.log`, `revision_pdfinfo.txt`, `revision_title.png`, contact sheets and `qa/article_text.txt` remain historical evidence for their recorded source state. No old pass certifies a later source revision. Do not rerun old scripts as a substitute for inspecting their assumptions.
+
+## Submission blockers
+
+This named master is **not a submission-ready anonymous file**. The publisher's indexed journal information specifies double-anonymous review. Names, contact details, PDF author metadata and the identifying repository link need a separate review-file treatment and a usable anonymous evidence-access route; the complete named master/evidence map should be preserved. The exact current instructions/portal requirements are not fully accessible.
+
+Authors must confirm one author order, affiliations and author links, corresponding-author details, funding, competing interests, contributions, applicable institutional requirements and the assistance disclosure. The existing PDF author metadata order is deliberately retained pending that confirmation, although it conflicts with the visible source order. The previous shared university affiliation in `EDIT_REPORT.md` is historical evidence, not confirmation of present facts. See the Batch 4 checklist before replacing any draft placeholder.
 
-Read `EDIT_REPORT.md` before preparing submission. Author metadata and declarations need confirmation, and the journal's detailed instructions/template could not be verified. The author field is intentionally empty. The repository URL in Appendix D identifies the project and must be reviewed for double-anonymized submission.
+The checked accessible evidence revision is `15b8b4dc95e3658f3b858a6f792ea2983299aaa6`; it includes earlier editorial batches, not the current uncommitted manuscript. The freeze record's identifier `ac9a9ccad027cde05488abb633e66cc02f87cc46` remains unresolved locally and returned 404 remotely during Batch 3. Main frozen summaries are tracked; Git-ignored grid profiles/primitives and Stage 2H pilot raw outputs are not promised as public. No commit or push is part of these revisions.
diff --git a/journal_article/.gitignore b/journal_article/.gitignore
index a1e1fa9d..0cd0a7ee 100644
--- a/journal_article/.gitignore
+++ b/journal_article/.gitignore
@@ -9,3 +9,24 @@
 /main.synctex.gz
 /main.fdb_latexmk
 /main.fls
+
+# Batch 4 job-local TeX runtime and rebuildable document intermediates.
+/qa/batch4/runtime/
+/qa/batch4/*.aux
+/qa/batch4/*.bcf
+/qa/batch4/*.blg
+/qa/batch4/*.bbl
+/qa/batch4/*.out
+/qa/batch4/*.run.xml
+/qa/batch4/*.toc
+/qa/batch4/*.fls
+/qa/batch4/*.fdb_latexmk
+
+# Rebuildable Batch 4 PDF/render/log evidence stays local; retain helper and inspection note.
+/qa/batch4/*.txt
+/qa/batch4/*.log
+/qa/batch4/*.json
+/qa/batch4/*.pdf
+/qa/batch4/*.png
+/qa/batch4/*.ppm
+/qa/batch4/*.xml
diff --git a/journal_article/sections/submission_declarations.tex b/journal_article/sections/submission_declarations.tex
new file mode 100644
index 00000000..7aeccca9
--- /dev/null
+++ b/journal_article/sections/submission_declarations.tex
@@ -0,0 +1,14 @@
+\section*{Declarations: author confirmation required}
+\noindent\textit{Draft placeholders below must be completed and approved before submission.}
+
+\paragraph{Funding.} Pending author confirmation of funding sources, grant identifiers, recipients and any funder role. No absence of funding is asserted.
+
+\paragraph{Competing interests.} Pending each author's declaration of relevant financial and non-financial interests. No absence of competing interests is asserted.
+
+\paragraph{Author contributions.} Pending agreement on each author's actual contributions and the journal's requested contribution format. No roles are assigned by this draft.
+
+\paragraph{Affiliations and corresponding author.} Pending confirmation of institutional affiliations and their author links, the corresponding author's name, postal address and email, and a single agreed author order for the title page, PDF metadata and submission system.
+
+\paragraph{Generative AI assistance.} Draft for author review: OpenAI Codex assisted manuscript revision and repository documentation. The authors must confirm the tool/model version, full scope and reason for use, and the accuracy, responsibility and applicable terms-of-use statements required by the publisher before submission.
+
+\paragraph{Ethics and institutional requirements.} Pending author confirmation of applicability and any required statement; this draft makes no claim that approvals were obtained, waived or unnecessary.
diff --git a/journal_article/qa/batch4/build_document.py b/journal_article/qa/batch4/build_document.py
new file mode 100644
index 00000000..e398c496
--- /dev/null
+++ b/journal_article/qa/batch4/build_document.py
@@ -0,0 +1,41 @@
+"""Document-only Batch 4 build; never invokes research scripts or package installers."""
+from pathlib import Path
+import configparser, json, os, subprocess, time
+ARTICLE = Path(__file__).resolve().parents[2]
+OUT = Path(__file__).resolve().parent
+RUNTIME = OUT / 'runtime'
+INSTALL = Path(os.environ['LOCALAPPDATA']) / 'Programs' / 'MiKTeX'
+ORIGINAL_CONFIG = Path(os.environ['APPDATA']) / 'MiKTeX' / 'miktex' / 'config' / 'miktex.ini'
+for folder in [OUT, RUNTIME / 'config' / 'miktex' / 'config', RUNTIME / 'data']:
+    folder.mkdir(parents=True, exist_ok=True)
+original = configparser.ConfigParser()
+original.read(ORIGINAL_CONFIG)
+config = configparser.ConfigParser()
+config.optionxform = str
+config['Core'] = {key: original.get('Core', key) for key in ['LastUserMaintenance', 'NoRegistry', 'SharedSetup'] if original.has_option('Core', key)}
+config['MPM'] = {'AutoInstall': '0'}
+with (RUNTIME / 'config' / 'miktex' / 'config' / 'miktex.ini').open('w') as handle:
+    config.write(handle)
+startup = RUNTIME / 'miktexstartup.ini'
+startup.write_text('[Paths]\nUserConfig=' + str(RUNTIME / 'config') + '\nUserData=' + str(RUNTIME / 'data') + '\nUserInstall=' + str(INSTALL) + '\n[Setup]\nVersion=25.12\n')
+env = os.environ.copy()
+env.update({'MIKTEX_USERCONFIG': str(RUNTIME / 'config'), 'MIKTEX_USERDATA': str(RUNTIME / 'data'), 'MIKTEX_USERINSTALL': str(INSTALL), 'MIKTEX_USERSTARTUPFILE': str(startup), 'LANG': 'C', 'LC_ALL': 'C', 'PAR_GLOBAL_TEMP': str(RUNTIME), 'TEXINPUTS': str(OUT) + ';' + str(ARTICLE) + ';', 'BIBINPUTS': str(ARTICLE) + ';'})
+latex = [str(INSTALL / 'miktex/bin/x64/pdflatex.exe'), '--disable-installer', '-no-shell-escape', '-interaction=nonstopmode', '-halt-on-error', '-file-line-error', '-output-directory=' + str(OUT), 'main.tex']
+biber = [str(INSTALL / 'executables/windows-x64/biber/biber.exe'), '--input-directory', str(OUT), '--output-directory', str(OUT), 'main']
+records = []
+for name, command in [('latex1', latex), ('biber', biber), ('latex2', latex), ('latex3', latex)]:
+    print('Starting', name, flush=True)
+    started = time.monotonic()
+    with (OUT / (name + '.txt')).open('w', encoding='utf-8') as log:
+        process = subprocess.Popen(command, cwd=OUT, env=env, stdout=log, stderr=subprocess.STDOUT)
+        try:
+            code = process.wait(timeout=240)
+        except subprocess.TimeoutExpired:
+            process.kill()
+            code = 'TIMEOUT'
+    records.append({'step': name, 'command': command, 'exit_code': code, 'seconds': round(time.monotonic() - started, 2)})
+    (OUT / 'build_results.json').write_text(json.dumps(records, indent=2), encoding='utf-8')
+    print(name, 'exit:', code, flush=True)
+    if code != 0:
+        raise SystemExit(1)
+print('Document-only build sequence finished.', flush=True)
diff --git a/journal_article/qa/batch4/BUILD_INSPECTION.md b/journal_article/qa/batch4/BUILD_INSPECTION.md
new file mode 100644
index 00000000..59660758
--- /dev/null
+++ b/journal_article/qa/batch4/BUILD_INSPECTION.md
@@ -0,0 +1,17 @@
+# Batch 4 document build and inspection
+
+Date: 10 November 2026 (Asia/Tashkent). This is document QA, not statistical validation.
+
+The final clean pdfLaTeX ? Biber ? pdfLaTeX ? pdfLaTeX sequence completed with exit code 0 at every step, producing `main.pdf` in this directory: **34 A4 pages, 1,014,922 bytes**. SHA-256: `d3f3ef20d0cc75212bc03326963140db6413f369aeaac3055a926376da05e214`.
+
+The PDF title matches the approved title. The visible title-page order is UMURZOKOV then KOSTAEV; the retained PDF author metadata has the reverse order. Both existing names, ORCIDs and emails render. Affiliation facts and the corresponding author remain unconfirmed; no historical affiliation was silently restored. The declarations are visibly draft placeholders. This named PDF is not the anonymous review file.
+
+The final LaTeX log reports no undefined references/citations, duplicate labels, overfull boxes or rerun requests. Biber 2.22 reports no warnings/errors. Main equations are numbered 1?40; appendix equations use B.1?B.4 and D.1?D.14. Reference links resolve; text extraction contains no `??`. References contain nine cited entries from the unchanged bibliography. Appendices A, B, C and D begin on pages 18, 25, 26 and 29. All 34 pages were rendered in grayscale, with no blank pages. Three contact sheets were inspected; pages 1, 9, 10, 17 and 30 were also viewed at reading size. The main table, coverage annotations and wrapped evidence-map paths are readable in those renderings, with no clipped content observed. Dense appendix tables still require ordinary zoom. No printed-proof or verified journal-template compliance is asserted.
+
+Non-fatal diagnostics remain: epstopdf warns that shell escape is disabled (no EPS conversion was required); MiKTeX reports that updates have not been checked. Some utility invocations also printed package-database-lock warnings despite returning 0 and producing valid metadata/text/render outputs. Global MiKTeX was not repaired or updated. Package installation and TeX shell escape were disabled for the build.
+
+The initial normal invocation failed during configuration-directory/registry initialization. A job-local configuration reuses the installed binaries and selected non-sensitive maintenance/NoRegistry settings, with writable caches under `runtime/`. Biber is invoked directly from the installed executable location. The first output-directory build read historical root auxiliary files; the second retained a stale Biber rerun marker. Their logs are preserved with `attempt1_` and `attempt2_` prefixes. Clearing only this job's generated auxiliaries and rebuilding from its output directory resolved those warnings. The historical root PDF, bibliography output and QA records were not overwritten or deleted.
+
+Rebuild helper: `build_document.py`. Machine-readable final commands/exit codes/timings: `build_results.json`; PDF metadata: `pdfinfo.txt`; current extracted text: `article_text_utf8.txt`; rendering: `page-01.png` through `page-34.png`, and `contact-1.png` through `contact-3.png`; source/PDF hashes and document checks: `inspection_checks.json`. Generated binaries, logs, renders and runtime caches are intentionally local/Git-ignored; this note and the document-only helper are reviewable source artifacts. No research code, datasets, statistical results or original figures/tables were regenerated.
+
+**Submission recommendation: NOT READY.** Author-order/affiliation/correspondence confirmation, factual declarations, the anonymous review package and evidence-access route, and remaining live journal instructions must be resolved. Successful document compilation supplies none of those confirmations.
```
