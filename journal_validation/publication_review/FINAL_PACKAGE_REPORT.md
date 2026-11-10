# Final manuscript and submission package report

**Date:** 10 November 2026 (Asia/Tashkent)
**Branch:** `journal-validation`
**Starting HEAD:** `0f4188ca98a45ba03e1c889ac705ec936369862a` (`0f4188ca`, subject `final simulations.`; parent `15b8b4dc`). The supplied working tree was clean. This session did not create that commit and did not run simulations.
**Final assessment: NOT READY TO SUBMIT.** Named/review documents are built and inspected, but full anonymous evidence access, detailed journal rules and remaining AI-disclosure information are unresolved. Nothing was uploaded, deposited, committed, pushed or submitted.

## 1. Applied author information and declarations

The named title page and PDF Author metadata now use the user-confirmed order and publication forms:

1. **Umurzokov Olimjon Umidjon ugli**, ORCID `0009-0008-0090-7100`, `olimumurzokov022@gmail.com`.
2. **Kostaev Umidjon Umirzakovich**, ORCID `0009-0000-0205-5142`, `umidjonkostaev2025@gmail.com`.

Both authors are linked to **Tashkent State University of Economics, Tashkent, Uzbekistan**. The first author is marked as corresponding author with the approved email. The old reversed PDF-author order is resolved. Existing ORCID/email values were retained; no new identity or affiliation fact was invented. The supplied second-author qualification **DSc in Economics** is recorded here but not printed: no accessible JSCS instruction established that degree suffixes belong in the author line. This is a conservative omission under the user's conditional instruction, not a claim that the journal prohibits degrees.

`journal_article/sections/submission_declarations.tex` contains the approved text, without the former draft heading, funding/conflict/contribution/affiliation/ethics placeholders or unassigned CRediT roles:

- Funding: **This research received no external funding.**
- Competing interests: **The authors declare no financial or non-financial conflicts of interest.**
- Contributions: **Both authors contributed equally.**
- AI assistance: **AI tools, including ChatGPT and OpenAI Codex, assisted with grammar checking, translation, manuscript editing and documentation. The authors state that AI was not used to develop or modify research code, simulations or statistical analysis.**
- Ethics and informed consent: **The study uses simulated data without human participants or personal data. Ethics approval and informed consent were not required.**

These are author-supplied declarations, not independent retrospective verification of every prior activity. No tool version was invented. Exact ChatGPT/model and Codex/tool versions remain to be supplied or addressed with publisher-approved wording if unavailable. The publisher's translation/assistance policy also calls for author accuracy/responsibility and applicable terms confirmations; those attestations were not silently added beyond the approved text.

## 2. Concrete package outputs

All paths are repository-relative. Outputs are local/Git-ignored, not a public release or verified portal upload. The canonical complete named LaTeX source remains in `journal_article/`.

| Artifact | Location | Purpose/status |
|---|---|---|
| Named manuscript PDF | `journal_article/submission/named/manuscript_named.pdf` | Confirmed title-page authors/affiliation/correspondence and approved declarations; includes Appendices A?D. |
| Separate review PDF | `journal_article/submission/review/manuscript_review.pdf` | Explicit identities and searchable repository/revision provenance removed from inspected surfaces; same scientific content, with neutral evidence-record IDs. Full external anonymous access remains unresolved. |
| Optional full-table supplement | `journal_article/submission/review/supplementary_tables_review.pdf` | Existing full point-performance, coverage, power and grid-informativeness table assets, with separate S.1?S.6 numbering; no calculations/regenerated entries. Same PDF also at `journal_article/submission/named/supplementary_tables.pdf`. Not established as mandatory. |
| Complete named document source archive | `journal_article/submission/named/source_named.zip` | Whitelisted main/preamble/bibliography, sections, Appendices A?D, original table/figure dependencies and optional table-wrapper sources. No entire-repository export or research runtime is implied. |
| Review document source archive | `journal_article/submission/review/source_review.zip` | Corresponding review presentation and dependencies, with explicit identity/provenance masking. Source-upload requirement remains unverified; do not assume it must be uploaded. |
| Local compact data-access candidate | `journal_article/submission/review/frozen_summaries_review.zip` | Seven unchanged existing CSV summaries, anonymous record inventory and truthful README. **Not an approved publication supplement or verified journal reviewer-access mechanism.** |
| Identifying original-to-review mapping | `journal_article/submission/named/provenance_mapping.csv`, `named/package_manifest.json` | Complete record ID ? original path mapping retained with the named package. Do not upload in an anonymous category. |
| Document-only helpers / instructions | `journal_article/submission/prepare_and_build.py`, `audit_packages.py`, `README.md` | Rebuild/inspection logic; no research invocation. Outputs/work/QA are intentionally ignored. |

Both manuscripts retain all Appendices A?D inline, avoiding broken main-to-appendix references or loss of the density argument, coverage/numerical qualifications and complete evidence associations. The separate 28-page table supplement does not restore those full tables to the main manuscript. The named PDF's first page supplies title-page material; no separate title-page PDF was asserted necessary because that live journal requirement remains unverified.

### Final PDF identities

| PDF | Pages / bytes | SHA-256 |
|---|---|---|
| Named manuscript | 34 / 1,013,853 | `4fecad9e125211689910104b8b533cb5e03f1d96e24752dc58bb62b5e77e3388` |
| Review manuscript | 33 / 997,536 | `bc8ef361d7d46546412735d40ba2b4203876569c041fe24081fd8cee42ea7645` |
| Optional table supplement | 28 / 187,961 | `c277db1a4c1c2ca6d8b1a826dacdaeb30c56e93c526c97273674a68d39715277` |

Source/archive/CSV package hashes and sizes are retained in `journal_article/submission/qa/package_hashes.json`. The PDF copies under named/review are final outputs of this pass; the historical root `journal_article/main.pdf` and Batch 4 outputs were not overwritten.

## 3. Exact scope and scientific consistency

Canonical edits are limited to `main.tex` (author block and matching PDF author metadata), approved declaration text, README status and local-output ignore rules. The approved title and abstract are unchanged. Six scientific sections, original tables/figures, bibliography, Appendices A?C, and the canonical named Appendix D/evidence map/availability statement are unchanged from the supplied baseline. No numerical result, research code, density/score theory or research figure was modified.

Review copies are derived in `submission/work/review_source/`: the author block is omitted, PDF Author is empty, identifying availability/provenance paragraphs are replaced with truthful access-limit statements, and original repository paths are represented by neutral R001-style identifiers. The full original map is preserved in the named package. No evidence finding or limitation is redacted merely because it is inconvenient. Displayed Appendix D mathematics is identical. A derived-copy diff is provided below so these presentation changes are reviewable.

Document integrity checks confirmed:

- The abstract and Sections 1?6 are identical between named and review sources; table/figure/bibliography bytes, Appendices A?C and approved declarations match exactly.
- All displayed Appendix D equations/identities match; differences concern identifying provenance presentation and access wording.
- All scientific assets used by the optional table PDF are the pre-existing TeX assets, copied unchanged. Its wrapper only supplies a separate document and numbering.
- Each of the seven compact CSV payloads equals its existing source byte-for-byte. No descriptive count, statistic or uncertainty measure was recomputed.
- Named/review source archives contain the staged dependencies, no absolute member paths/parent traversal, and no unchecked entire repository or Git history.
- Every pre-existing file outside the four authorized canonical/documentation edits matches its captured baseline SHA-256. This includes research R/Python files, frozen datasets, table/figure sources, older PDFs, QA and earlier editorial reports.

These are document/byte-integrity checks, not statistical validation or a validation of inference theory.

## 4. Anonymity inspection and limits

| Surface | Actual result |
|---|---|
| Review title page / extracted text | No supplied author names, ORCIDs, emails or institution. Same approved title/abstract and scientific narrative remain. |
| PDF Author/other printed metadata | Named metadata matches confirmed order; review and table supplement have no author identity. Parsed metadata scans find no listed author/institution/repository/revision token. |
| XMP | Metadata extraction returned no XMP author payload for review or supplement. |
| Active URL annotations | Named PDF retains approved ORCID/mailto and public repository links. Review/supplement URL lists have no supplied author/ORCID/mailto/GitHub/project/revision identifiers; legitimate scholarly references are retained. |
| Embedded files | PDF utilities report zero embedded files in the manuscripts/supplement. |
| Repository URLs and revision tokens | Explicit GitHub username/project URLs, `15b8b4dc?`, `ac9a9cca?` and the current starting revision token are absent from review source/text/metadata/URLs. Full named provenance remains unchanged. |
| Appendix D supplementary provenance | Original paths are replaced by neutral record IDs, consistently mapped in the private named record table and review bundle inventory. The inventory explicitly distinguishes seven CSVs included in that bundle from records not in it; some document dependencies are available in the separate source archive. |
| Source/data ZIP inspection | Text members pass the supplied-name/ORCID/email/institution/repository/revision scans. Inventories and ZIP member names were checked; original numerical CSV bytes are preserved. Named mapping/manifest files are identifying and stay out of the review directory. |
| Bookmarks / destinations | Decoded compiled bookmark-source entries (29 in each manuscript) have no listed identity token. A direct `pdfinfo -dests` enumeration stalled and was stopped; no exhaustive PDF-object/JavaScript audit is claimed. Clean LaTeX builds have no destination-reference warnings. |
| Residual re-identification | Distinctive title, wording, numerical examples and generic source-asset filenames may be matched to existing public material. Removing explicit identifiers does not guarantee non-identifiability. No claim of guaranteed anonymity is made. |

The review PDF is a separately built review candidate with explicit identity masking, **not** evidence that an anonymous repository or a full reviewer-access mechanism exists. Native inspection utilities sometimes printed non-fatal MiKTeX package-database-lock/update messages while returning success and producing usable outputs; raw logs are retained. The direct destination-enumeration limitation is explicitly reported rather than treated as a pass.

## 5. Journal requirements: verified versus inaccessible

Checked 10 November 2026. Direct JSCS instructions/about-page fetches returned HTTP 403. Search-retrieved publisher page text supplied the limited journal-specific confirmations below; this is not a complete live portal/IFA verification. Third-party instructions were not treated as authority.

| Topic | Source / verification | Application / remaining issue |
|---|---|---|
| Review model and submission route | Publisher-indexed [JSCS journal information](https://www.tandfonline.com/action/journalInformation?journalCode=gscs20&show=instructions) confirms double-anonymous review and Submission Portal. | Separate named/review documents prepared. Exact live file categories and who can see each uploaded source/supplement remain unverified. |
| Technique/novelty cue before abstract | Same publisher-indexed journal information requests a braced technique/contribution-area cue. | Existing restrained Monte Carlo/instrument-relevance cue retained. No new novelty/theorem claim. |
| Manuscript formatting, class, citation style, length/abstract limits, degrees, separate title-page requirement, figure specifications and exact supplementary-file rules | Detailed [official instructions endpoint](https://www.tandfonline.com/action/authorSubmission?show=instructions&journalCode=gscs20) inaccessible (403). | Existing layout retained. DSc not printed under the user's conditional instruction. No format-free/template/length compliance claim. |
| Named/anonymous upload categories | Accessible general [publisher Submission Portal guidance](https://authorservices.taylorandfrancis.com/publishing-your-research/making-your-submission/using-taylor-francis-submission-portal/) describes named and anonymous manuscripts and supplementary categorization. | Proposed categories follow that distinction; actual JSCS form/visibility must be confirmed. A generic supplementary upload must not be assumed editor-confidential. |
| Supplemental versus research-data routing | Accessible general [supplementary-material guidance](https://authorservices.taylorandfrancis.com/publishing-your-research/writing-your-paper/enhancing-your-article-with-supplementary-material/) distinguishes research data from ordinary supplemental material and directs data to its sharing policy. | Optional existing-table PDF is a supplemental candidate. The CSV ZIP is a local data-access candidate only; its acceptable route is unresolved, not a claimed approved supplement upload. |
| Data availability / anonymity | Accessible general [data-availability guidance](https://authorservices.taylorandfrancis.com/data-sharing/share-your-data/data-availability-statements/) discusses truthful access conditions and identity risks. | Review statement explicitly says full anonymous access is not arranged/verified. Exact JSCS policy tier and acceptable anonymous data route remain unverified. |
| AI assistance and translation | Accessible publisher-wide [authorship/AI policy](https://authorservices.taylorandfrancis.com/editorial-policies/defining-authorship-research-paper/) requests tool/version/use disclosure and author confirmations for translation/copyediting. | Approved disclosure inserted; no versions invented. Exact ChatGPT/model/Codex versions (or accepted unavailable-version wording), responsible author review and applicable terms confirmations remain to be resolved. |

General publisher guidance does not establish every JSCS-specific upload, data or formatting requirement. This report makes no journal-acceptance claim.

## 6. Remaining evidence-access and submission issues

1. **Anonymous reviewer access remains unresolved.** Seven existing summaries are packaged locally and their payloads inspected, but no journal-approved data upload/visibility route has been arranged or tested. Full selected-case numerical reports/contracts and other external provenance are not supplied through a verified anonymous mechanism. The reviewer copy states this plainly.
2. **Original provenance remains complete in the named package.** The checked `15b8b4dc?` checkpoint is evidence provenance, not the current submission master. Current source changes are uncommitted. The historical `ac9a9cca?` freeze checkout remains unresolved as recorded in Batch 3; no replacement identifier or accessible release is invented.
3. **Local-only artifacts remain local-only.** Grid-diagnostic profiles/primitives and Stage 2H pilot raw outputs/seal are not promised public or attached. Exact main-run worker penalty replay remains unestablished.
4. **Detailed journal instructions/portal visibility need confirmation.** Particularly research-data routing, supplement/source acceptance, format/length/style/degree conventions and title-page/declaration placement. No upload, anonymous repository or deposit was created.
5. **AI-disclosure version/attestation details need confirmation.** Author-approved substantive wording is applied, but missing versions and publisher-requested responsibility/translation/terms statements cannot be invented.
6. **Anonymity has bounded inspection scope.** Explicit identifiers pass inspected text/metadata/URI/archive channels, but direct destination enumeration stalled and public matching/fingerprinting remains possible. The final portal-generated proof and file access must be inspected before submission.

**Final recommendation: NOT READY TO SUBMIT.** The factual author/declaration work and local document preparation are complete within the supplied information. Readiness is withheld until the journal requirements, reviewer access and remaining disclosure/anonymity checks are resolved. Do not upload named provenance in an anonymous category or describe the current local data bundle as a verified anonymous repository.

## 7. Actual build and visual inspection

Separate named/review working directories were used, with clean auxiliaries, installed pdfLaTeX/Biber, the initialized job-local MiKTeX runtime, package installation disabled and TeX shell escape disabled. Each manuscript completed pdfLaTeX ? Biber ? pdfLaTeX ? pdfLaTeX with zero exit codes. The optional table document uses no citations/bibliography and completed two pdfLaTeX passes with zero exit codes. No global MiKTeX repair or new package installation was needed.

Final logs contain no undefined references/citations, multiply defined labels, overfull boxes, unresolved destinations or rerun requests. Non-fatal shell-escape-disabled/updates-not-checked messages remain. Main equation labels are 1?40 and appendix labels B.1?B.4/D.1?D.14, 58 unique labels in each manuscript. Both main bibliographies contain nine cited entries from the unchanged bibliography. All A?D cross-references resolve. The optional tables use S.1?S.6 and retain existing continuation captions/entries.

Every page of all three PDFs was rendered in grayscale and visually inspected in contact sheets. Named/review title pages and the review declarations/evidence map were also opened at reading size. Confirmed author details and shared affiliation/correspondence render in the named file and are absent from review. Tables, figures, appendix continuations, equations and references are present, with no observed clipped content or blank pages; extracted text has no `??`. Dense full-result tables remain dense and may require zoom. This is not a printed-proof or full journal-template compliance claim.

Actual commands/exit codes/timings are in `submission/qa/build_results.json`. Per-PDF metadata, XMP/URL/attachment outputs, text, raster pages, contact sheets and audit summaries are under `submission/qa/{named,review,supplement}/`. Byte/source/ZIP consistency and bookmark-source checks are in `consistency_checks.json` and `source_anonymity_checks.json`. These generated QA artifacts are local/Git-ignored; no statistical inference has been validated by these checks.

## 8. Exact changes and complete source Git diff

The following diff compares canonical changes with the captured clean starting tree. New document-only helpers/documentation are compared with `/dev/null`. Generated ignored PDFs, ZIPs and QA are identified by location/hash above; they are reproducible package outputs, not silently omitted tracked edits. This report is not recursively embedded in its own diff. Earlier editorial reports and scientific source/data assets were not rewritten.

```diff
diff --git a/journal_article/main.tex b/journal_article/main.tex
index a0362869..071bd799 100644
--- a/journal_article/main.tex
+++ b/journal_article/main.tex
@@ -1,17 +1,20 @@
 % Compile from journal_article/: pdflatex main; biber main; pdflatex main; pdflatex main
 \input{preamble}
 \title{Controlled Instrument-Relevance Sensitivity in High-Dimensional IVQR: A Monte Carlo Study}
-% Named master; author order, affiliations and corresponding author require confirmation.
+% Confirmed author order, shared affiliation and corresponding author.
 \author{\begin{minipage}{\dimexpr\textwidth-2\tabcolsep\relax}\centering
-\normalsize OLIMJON UMIDJON UGLI UMURZOKOV\\
+\normalsize Umurzokov Olimjon Umidjon ugli\textsuperscript{a,*}\\
 \small ORCID: \href{https://orcid.org/0009-0008-0090-7100}{0009-0008-0090-7100}\\
 Email: \href{mailto:olimumurzokov022@gmail.com}{olimumurzokov022@gmail.com}\\[0.7em]
-\normalsize UMIDJON UMIRZAKOVICH KOSTAEV\\
+\normalsize Kostaev Umidjon Umirzakovich\textsuperscript{a}\\
 \small ORCID: \href{https://orcid.org/0009-0000-0205-5142}{0009-0000-0205-5142}\\
 Email: \href{mailto:umidjonkostaev2025@gmail.com}{umidjonkostaev2025@gmail.com}\\[0.7em]
+\textsuperscript{a}Tashkent State University of Economics, Tashkent, Uzbekistan.\\[0.4em]
+\textsuperscript{*}Corresponding author: Umurzokov Olimjon Umidjon ugli;\\
+\href{mailto:olimumurzokov022@gmail.com}{olimumurzokov022@gmail.com}.
 \end{minipage}}
 \date{}
-\hypersetup{pdftitle={Controlled Instrument-Relevance Sensitivity in High-Dimensional IVQR: A Monte Carlo Study},pdfauthor={UMIDJON UMIRZAKOVICH KOSTAEV; OLIMJON UMIDJON UGLI UMURZOKOV}}
+\hypersetup{pdftitle={Controlled Instrument-Relevance Sensitivity in High-Dimensional IVQR: A Monte Carlo Study},pdfauthor={Umurzokov Olimjon Umidjon ugli; Kostaev Umidjon Umirzakovich}}
 \begin{document}
 \maketitle
 \noindent\textit{\{Monte Carlo simulation assesses instrument-relevance sensitivity in high-dimensional IVQR.\}}\par\medskip
diff --git a/journal_article/sections/submission_declarations.tex b/journal_article/sections/submission_declarations.tex
index 7aeccca9..c1d10d49 100644
--- a/journal_article/sections/submission_declarations.tex
+++ b/journal_article/sections/submission_declarations.tex
@@ -1,14 +1,10 @@
-\section*{Declarations: author confirmation required}
-\noindent\textit{Draft placeholders below must be completed and approved before submission.}
+\section*{Declarations}
+\paragraph{Funding.} This research received no external funding.
 
-\paragraph{Funding.} Pending author confirmation of funding sources, grant identifiers, recipients and any funder role. No absence of funding is asserted.
+\paragraph{Competing interests.} The authors declare no financial or non-financial conflicts of interest.
 
-\paragraph{Competing interests.} Pending each author's declaration of relevant financial and non-financial interests. No absence of competing interests is asserted.
+\paragraph{Author contributions.} Both authors contributed equally.
 
-\paragraph{Author contributions.} Pending agreement on each author's actual contributions and the journal's requested contribution format. No roles are assigned by this draft.
+\paragraph{AI assistance.} AI tools, including ChatGPT and OpenAI Codex, assisted with grammar checking, translation, manuscript editing and documentation. The authors state that AI was not used to develop or modify research code, simulations or statistical analysis.
 
-\paragraph{Affiliations and corresponding author.} Pending confirmation of institutional affiliations and their author links, the corresponding author's name, postal address and email, and a single agreed author order for the title page, PDF metadata and submission system.
-
-\paragraph{Generative AI assistance.} Draft for author review: OpenAI Codex assisted manuscript revision and repository documentation. The authors must confirm the tool/model version, full scope and reason for use, and the accuracy, responsibility and applicable terms-of-use statements required by the publisher before submission.
-
-\paragraph{Ethics and institutional requirements.} Pending author confirmation of applicability and any required statement; this draft makes no claim that approvals were obtained, waived or unnecessary.
+\paragraph{Ethics and informed consent.} The study uses simulated data without human participants or personal data. Ethics approval and informed consent were not required.
diff --git a/journal_article/.gitignore b/journal_article/.gitignore
index 0cd0a7ee..04070e87 100644
--- a/journal_article/.gitignore
+++ b/journal_article/.gitignore
@@ -30,3 +30,9 @@
 /qa/batch4/*.png
 /qa/batch4/*.ppm
 /qa/batch4/*.xml
+
+# Final package: reproducible local sources are staged by the document-only helper.
+/submission/work/
+/submission/qa/
+/submission/named/
+/submission/review/
diff --git a/journal_article/README.md b/journal_article/README.md
index cd5ae4a9..72f61a95 100644
--- a/journal_article/README.md
+++ b/journal_article/README.md
@@ -1,6 +1,6 @@
 # Journal article ? submission preparation
 
-`main.tex` is the named manuscript master. Its approved title is **Controlled Instrument-Relevance Sensitivity in High-Dimensional IVQR: A Monte Carlo Study**. Main sections are in `sections/`; `sections/submission_declarations.tex` contains visible author-confirmation placeholders, and `sections/data_availability.tex` distinguishes the checked evidence archive from local-only files and the unresolved historical freeze identifier.
+`main.tex` is the named manuscript master. Its approved title is **Controlled Instrument-Relevance Sensitivity in High-Dimensional IVQR: A Monte Carlo Study**. Main sections are in `sections/`; `sections/submission_declarations.tex` contains the author-approved funding, conflict, equal-contribution, AI-assistance and simulated-data ethics declarations, and `sections/data_availability.tex` distinguishes the checked evidence archive from local-only files and the unresolved historical freeze identifier.
 
 The review document includes the article, references and supplementary **Appendices A?D**:
 
@@ -13,7 +13,7 @@ Existing figures, tables and bibliography are used directly. No simulation or st
 
 ## Current document and build evidence
 
-The historical root `main.pdf` and `EDIT_REPORT.md` describe earlier revisions. Do not assume they match the current source. The Batch 4 document-only build and inspection artifacts are under `qa/batch4/`; consult [BATCH4_CHANGE_REPORT.md](../journal_validation/publication_review/BATCH4_CHANGE_REPORT.md) for actual results and remaining blockers. The current build target is `qa/batch4/main.pdf`; only a completed build and inspection establish its status.
+The historical root `main.pdf` and `EDIT_REPORT.md` describe earlier revisions. Do not assume they match the current source. The Batch 4 document-only build and inspection artifacts are under `qa/batch4/`; consult [BATCH4_CHANGE_REPORT.md](../journal_validation/publication_review/BATCH4_CHANGE_REPORT.md) for actual results and remaining blockers. Those records describe the earlier named draft. Final package outputs are `submission/named/manuscript_named.pdf` and `submission/review/manuscript_review.pdf`; the current package report is [FINAL_PACKAGE_REPORT.md](../journal_validation/publication_review/FINAL_PACKAGE_REPORT.md).
 
 For an ordinarily configured TeX installation, run from this directory:
 
@@ -31,6 +31,9 @@ Batch 4 uses `python qa/batch4/build_document.py` to keep document outputs and a
 
 This named master is **not a submission-ready anonymous file**. The publisher's indexed journal information specifies double-anonymous review. Names, contact details, PDF author metadata and the identifying repository link need a separate review-file treatment and a usable anonymous evidence-access route; the complete named master/evidence map should be preserved. The exact current instructions/portal requirements are not fully accessible.
 
-Authors must confirm one author order, affiliations and author links, corresponding-author details, funding, competing interests, contributions, applicable institutional requirements and the assistance disclosure. The existing PDF author metadata order is deliberately retained pending that confirmation, although it conflicts with the visible source order. The previous shared university affiliation in `EDIT_REPORT.md` is historical evidence, not confirmation of present facts. See the Batch 4 checklist before replacing any draft placeholder.
+The authors have confirmed the order Umurzokov Olimjon Umidjon ugli, then Kostaev Umidjon Umirzakovich, a shared Tashkent State University of Economics affiliation, the first author as corresponding author, and the declarations now in source. PDF author metadata matches that order. DSc is not printed because the journal convention remains unverified. Tool/model versions and the publisher-specific AI/translation responsibility confirmations remain to be resolved. The separately built review copy masks explicit identities and searchable provenance, but full external anonymous evidence access and remaining journal requirements are not established. Older checklists and QA records retain their historical status; consult the final package report for current results.
 
 The checked accessible evidence revision is `15b8b4dc95e3658f3b858a6f792ea2983299aaa6`; it includes earlier editorial batches, not the current uncommitted manuscript. The freeze record's identifier `ac9a9ccad027cde05488abb633e66cc02f87cc46` remains unresolved locally and returned 404 remotely during Batch 3. Main frozen summaries are tracked; Git-ignored grid profiles/primitives and Stage 2H pilot raw outputs are not promised as public. No commit or push is part of these revisions.
+
+
+Final local package build: `python submission/prepare_and_build.py`; inspection: `python submission/audit_packages.py`. These document-only helpers reuse the initialized Batch 4 local MiKTeX runtime. Appendices A-D remain inline. The existing-table PDF is an optional supplement, while the compact CSV ZIP is a local data-access candidate, not an approved publication supplement. No upload, public deposit or submission has been made.
diff --git a/journal_article/submission/prepare_and_build.py b/journal_article/submission/prepare_and_build.py
new file mode 100644
index 00000000..36045046
--- /dev/null
+++ b/journal_article/submission/prepare_and_build.py
@@ -0,0 +1,195 @@
+"""Build documents and copy frozen evidence only; never run research or install packages."""
+from pathlib import Path
+import csv, io, json, os, re, shutil, subprocess, sys, time, zipfile
+
+ARTICLE = Path(__file__).resolve().parents[1]
+REPO = ARTICLE.parent
+ROOT = Path(__file__).resolve().parent
+WORK, QA = ROOT / 'work', ROOT / 'qa'
+INSTALL = Path(os.environ['LOCALAPPDATA']) / 'Programs/MiKTeX'
+RUNTIME = ARTICLE / 'qa/batch4/runtime'
+for folder in [WORK, QA, ROOT / 'named', ROOT / 'review']:
+    folder.mkdir(parents=True, exist_ok=True)
+
+relative = ['main.tex', 'preamble.tex', 'references.bib']
+for directory in ['sections', 'supplementary', 'tables', 'figures']:
+    relative.extend(p.relative_to(ARTICLE).as_posix() for p in sorted((ARTICLE / directory).rglob('*'))
+                    if p.is_file() and p.suffix.lower() in ['.tex', '.bib', '.png', '.pdf', '.jpg', '.jpeg'])
+for variant in ['named', 'review']:
+    for rel in relative:
+        target = WORK / (variant + '_source') / rel
+        target.parent.mkdir(parents=True, exist_ok=True)
+        shutil.copyfile(ARTICLE / rel, target)
+
+paths = sorted({value for rel in relative if rel.endswith('.tex')
+                for value in re.findall(r'\\path\{([^}]+)\}', (ARTICLE / rel).read_text(encoding='utf-8'))
+                if not re.fullmatch('[0-9a-f]{40}', value)})
+ids = {value: 'R%03d' % (i + 1) for i, value in enumerate(paths)}
+selected = {
+    'thesis_extension/final/output/n500/summary.csv': 'Full performance and grid summaries, n=500',
+    'thesis_extension/final/output/n500/power_summary.csv': 'False-candidate rejection summaries, n=500',
+    'thesis_extension/final/output/n1000/summary.csv': 'Full performance and grid summaries, n=1000',
+    'thesis_extension/final/output/n1000/power_summary.csv': 'False-candidate rejection summaries, n=1000',
+    'thesis_extension/reporting/output/table_cr_informativeness_full.csv': 'Grid informativeness, all main design cells',
+    'thesis_extension/reporting/output/table_grid_domain_diagnostic.csv': 'Domain-expansion summaries',
+    'thesis_extension/calibration/instrument_strength_100rep/kappa_strength_summary.csv': 'Instrument-relevance calibration summaries'
+}
+assert set(selected) <= set(ids)
+review = WORK / 'review_source'
+main = (review / 'main.tex').read_text(encoding='utf-8')
+a, b = main.index('% Confirmed author order,'), main.index('\\date{}')
+main = main[:a] + '% Review copy: no identities or affiliation/contact block.\n\\author{}\n' + main[b:]
+main = re.sub(r'pdfauthor=\{[^}]*\}', 'pdfauthor={}', main)
+(review / 'main.tex').write_text(main, encoding='utf-8', newline='\n')
+
+availability = r'''\section*{Data and code availability}
+This study uses simulated data and archived computational outputs. A local optional evidence bundle, \texttt{frozen\_summaries\_review.zip}, contains seven existing compact CSV summaries and a record inventory. These files have been copied without numerical changes; they support inspection without re-estimation. Their inclusion in this local package is not verification of reviewer access through the journal. Anonymous access to the full external archive and remaining provenance records has not been arranged or verified.
+
+Appendix~\ref{app:evidence-map} retains the claim-to-evidence map with neutral record identifiers. The bundle inventory distinguishes included summaries from records that are not attached. The full original path/revision mapping is retained in the named package. The historical freeze checkout remains unresolved; its identifying token is withheld in this review copy, not replaced by a verified release claim. A checked evidence checkpoint does not identify the current manuscript revision.
+
+Historical rerunning requires the recorded R~3.4.3 environment and pinned dependencies. Their presence in the original archive does not establish portability or exact replay. Main-run worker-specific penalty states are not recoverable from the parent seed alone. Large grid-diagnostic profiles/primitives and Stage 2H pilot raw outputs and their seal are local, Git-ignored artifacts, not promised public or attached data. No public deposit of those artifacts or portable historical runtime is established. Historical estimator results have not been replaced by later certified solutions.
+'''
+(review / 'sections/data_availability.tex').write_text(availability, encoding='utf-8', newline='\n')
+p = review / 'supplementary/D_implementation.tex'
+s = p.read_text(encoding='utf-8')
+s = s.replace(s.splitlines()[5], 'The full archive location, revision identifiers and original paths are withheld in this review copy to limit direct identification. Neutral record identifiers below preserve the evidence associations; the full mapping is retained with the named package. Only the compact CSV summaries identified in the optional bundle inventory are attached locally. Full external anonymous access is not arranged or verified, and the historical freeze checkout remains unresolved. These access limits do not imply bit-for-bit regeneration from a seed on arbitrary systems.', 1)
+p.write_text(s, encoding='utf-8', newline='\n')
+p = review / 'supplementary/D_evidence_map.tex'
+s = p.read_text(encoding='utf-8')
+s = s.replace(s.splitlines()[2], 'Repository locations and revision identifiers are withheld in this review copy. Neutral record identifiers below correspond to the retained named evidence map; the optional CSV bundle inventory states which records are included and which are not attached. Full external anonymous access remains unresolved. Keys E1--E6 retain their original claim/evidence associations; no comparison count or statistic is recomputed.')
+p.write_text(s, encoding='utf-8', newline='\n')
+for rel in relative:
+    if rel.endswith('.tex'):
+        p = review / rel
+        original = p.read_text(encoding='utf-8')
+        s = re.sub(r'\\path\{([^}]+)\}', lambda m: r'\texttt{' + ids[m.group(1)] + '}'
+                   if m.group(1) in ids else r'\texttt{revision identifier withheld}', original)
+        if s != original:
+            p.write_text(s, encoding='utf-8', newline='\n')
+
+for rel in relative:
+    if rel.startswith(('figures/', 'tables/')) or rel == 'references.bib' or re.match(r'sections/0[1-6]_', rel):
+        assert (review / rel).read_bytes() == (WORK / 'named_source' / rel).read_bytes(), rel
+abstract = lambda s: s.split('\\begin{abstract}\n', 1)[1].split('\n\\end{abstract}', 1)[0]
+assert abstract((review / 'main.tex').read_text()) == abstract((WORK / 'named_source/main.tex').read_text())
+
+inventory, private_map = [], []
+for original, record_id in ids.items():
+    attached = original in selected
+    entry = {'record_id': record_id, 'description': selected.get(original, 'Original evidence/source/provenance locator; not included in this CSV bundle'),
+             'attachment': ('data/' + record_id + '.csv') if attached else '',
+             'status': 'Included unchanged CSV' if attached else 'Not included in this CSV bundle; document dependencies may be in the source archive; external record access unresolved'}
+    inventory.append(entry)
+    private_map.append(dict(entry, original_path=original))
+with (ROOT / 'named/provenance_mapping.csv').open('w', encoding='utf-8', newline='') as h:
+    writer = csv.DictWriter(h, fieldnames=list(private_map[0])); writer.writeheader(); writer.writerows(private_map)
+with zipfile.ZipFile(ROOT / 'review/frozen_summaries_review.zip', 'w', zipfile.ZIP_DEFLATED) as z:
+    temp = io.StringIO(newline='')
+    writer = csv.DictWriter(temp, fieldnames=list(inventory[0])); writer.writeheader(); writer.writerows(inventory)
+    z.writestr('record_inventory.csv', temp.getvalue())
+    z.writestr('README.txt', 'Optional local review evidence bundle: seven archived compact CSV summaries, unchanged.\nRecord IDs match the review manuscript. Other records are not included in this CSV bundle; some document dependencies are in the separate source archive.\nJournal acceptance of ZIP uploads, reviewer visibility and full external anonymous access are unverified.\nNo simulations, estimation or statistical validation were performed to create this attachment.\n')
+    for original in selected:
+        z.write(REPO / original, 'data/' + ids[original] + '.csv')
+with zipfile.ZipFile(ROOT / 'review/frozen_summaries_review.zip') as z:
+    for original in selected:
+        assert z.read('data/' + ids[original] + '.csv') == (REPO / original).read_bytes()
+for variant in ['named', 'review']:
+    with zipfile.ZipFile(ROOT / variant / ('source_' + variant + '.zip'), 'w', zipfile.ZIP_DEFLATED) as z:
+        for rel in relative:
+            z.write(WORK / (variant + '_source') / rel, rel)
+terms = ['umurzokov', 'kostaev', 'olimumurzokov022', 'umidjonkostaev2025', 'orcid.org/0009',
+         '0009-0008-0090-7100', '0009-0000-0205-5142', 'Tashkent State University',
+         'github.com/U-Olim', 'DML-IVQR_Master_Thesis', '15b8b4dc', 'ac9a9cca', '0f4188ca']
+for rel in relative:
+    if rel.endswith(('.tex', '.bib')):
+        s = (review / rel).read_text(encoding='utf-8')
+        assert not any(t.lower() in s.lower() for t in terms), rel
+
+assert (RUNTIME / 'miktexstartup.ini').exists()
+records = []
+if '--review-only' in sys.argv and (QA / 'build_results.json').exists():
+    records = [x for x in json.loads((QA / 'build_results.json').read_text()) if x['variant'] == 'named']
+for variant in (['review'] if '--review-only' in sys.argv else ['named', 'review']):
+    out = WORK / (variant + '_build'); out.mkdir(parents=True, exist_ok=True)
+    source = WORK / (variant + '_source')
+    env = os.environ.copy()
+    env.update({'MIKTEX_USERCONFIG': str(RUNTIME / 'config'), 'MIKTEX_USERDATA': str(RUNTIME / 'data'),
+                'MIKTEX_USERINSTALL': str(INSTALL), 'MIKTEX_USERSTARTUPFILE': str(RUNTIME / 'miktexstartup.ini'),
+                'LANG': 'C', 'LC_ALL': 'C', 'PAR_GLOBAL_TEMP': str(RUNTIME),
+                'TEXINPUTS': str(out) + ';' + str(source) + ';', 'BIBINPUTS': str(source) + ';'})
+    for name in ['main.aux', 'main.bcf', 'main.bbl', 'main.out', 'main.run.xml']:
+        target = out / name
+        assert target.parent == out and out.is_relative_to(ROOT)
+        if target.exists():
+            target.unlink()
+    latex = [str(INSTALL / 'miktex/bin/x64/pdflatex.exe'), '--disable-installer', '-no-shell-escape',
+             '-interaction=nonstopmode', '-halt-on-error', '-file-line-error', '-output-directory=' + str(out), 'main.tex']
+    biber = [str(INSTALL / 'executables/windows-x64/biber/biber.exe'), '--input-directory', str(out), '--output-directory', str(out), 'main']
+    for step, cmd in [('latex1', latex), ('biber', biber), ('latex2', latex), ('latex3', latex)]:
+        print('Starting', variant, step, flush=True)
+        start = time.monotonic()
+        with (QA / (variant + '_' + step + '.txt')).open('w', encoding='utf-8') as log:
+            process = subprocess.Popen(cmd, cwd=out, env=env, stdout=log, stderr=subprocess.STDOUT)
+            try:
+                code = process.wait(timeout=240)
+            except subprocess.TimeoutExpired:
+                process.kill(); code = 'TIMEOUT'
+        records.append({'variant': variant, 'step': step, 'exit_code': code,
+                        'seconds': round(time.monotonic() - start, 2), 'command': cmd})
+        (QA / 'build_results.json').write_text(json.dumps(records, indent=2), encoding='utf-8')
+        print(variant, step, code, flush=True)
+        if code != 0:
+            raise SystemExit(1)
+    shutil.copyfile(out / 'main.pdf', ROOT / variant / ('manuscript_' + variant + '.pdf'))
+(ROOT / 'named/package_manifest.json').write_text(json.dumps({'records': private_map,
+    'scientific_inputs_identical': True, 'source_files': relative,
+    'reviewer_access': 'Local attachment assembled only; portal visibility and full external access unverified'}, indent=2), encoding='utf-8')
+print('Both document builds completed; no submission or anonymous repository created.', flush=True)
+
+# Optional separate full-table supplement: use existing entries, no numerical regeneration.
+source = WORK / 'review_source'
+out = WORK / 'tables_build'; out.mkdir(parents=True, exist_ok=True)
+pre = (source / 'preamble.tex').read_text(encoding='utf-8')
+pre = '\n'.join(line for line in pre.splitlines() if '{biblatex}' not in line and '\\addbibresource' not in line) + '\n'
+(out / 'supplement_preamble.tex').write_text(pre, encoding='utf-8')
+wrapper = r"""\input{supplement_preamble}
+\hypersetup{pdftitle={Supplementary Tables: Full Frozen Results},pdfauthor={}}
+\renewcommand{\thetable}{S.\arabic{table}}
+\begin{document}
+\section*{Supplementary Tables: Full Frozen Results}
+These optional tables reproduce existing frozen presentation assets without new calculations. They retain all sample sizes, quantiles and relevance settings in those assets. Direct-at-truth acceptance, false-candidate rejection and finite-grid informativeness are distinct summaries. The historical Coverage label is not independently validated coverage of the stored finite-grid accepted set. Interpretation remains subject to the implementation and numerical limitations in the manuscript.
+\input{tables/generated/appendix_point_performance}
+\input{tables/generated/appendix_coverage}
+\input{tables/generated/appendix_power}
+\input{tables/generated/appendix_cr_informativeness}
+\end{document}
+"""
+(out / 'supplementary_tables.tex').write_text(wrapper, encoding='utf-8')
+env = os.environ.copy()
+env.update({'MIKTEX_USERCONFIG': str(RUNTIME / 'config'), 'MIKTEX_USERDATA': str(RUNTIME / 'data'),
+            'MIKTEX_USERINSTALL': str(INSTALL), 'MIKTEX_USERSTARTUPFILE': str(RUNTIME / 'miktexstartup.ini'),
+            'TEXINPUTS': str(out) + ';' + str(source) + ';', 'LANG': 'C', 'LC_ALL': 'C'})
+cmd = [str(INSTALL / 'miktex/bin/x64/pdflatex.exe'), '--disable-installer', '-no-shell-escape',
+       '-interaction=nonstopmode', '-halt-on-error', '-file-line-error', 'supplementary_tables.tex']
+for step in ['tables_latex1', 'tables_latex2']:
+    print('Starting', step, flush=True)
+    start = time.monotonic()
+    with (QA / (step + '.txt')).open('w', encoding='utf-8') as log:
+        process = subprocess.Popen(cmd, cwd=out, env=env, stdout=log, stderr=subprocess.STDOUT)
+        try:
+            code = process.wait(timeout=240)
+        except subprocess.TimeoutExpired:
+            process.kill(); code = 'TIMEOUT'
+    records.append({'variant': 'supplement', 'step': step, 'exit_code': code,
+                    'seconds': round(time.monotonic() - start, 2), 'command': cmd})
+    (QA / 'build_results.json').write_text(json.dumps(records, indent=2), encoding='utf-8')
+    print(step, code, flush=True)
+    if code != 0:
+        raise SystemExit(1)
+shutil.copyfile(out / 'supplementary_tables.pdf', ROOT / 'review/supplementary_tables_review.pdf')
+shutil.copyfile(out / 'supplementary_tables.pdf', ROOT / 'named/supplementary_tables.pdf')
+for variant in ['named', 'review']:
+    with zipfile.ZipFile(ROOT / variant / ('source_' + variant + '.zip'), 'a', zipfile.ZIP_DEFLATED) as z:
+        for rel in ['supplementary_tables.tex', 'supplement_preamble.tex']:
+            z.write(out / rel, rel)
+print('Optional existing-table PDF completed; no portal requirement or reviewer access is asserted.', flush=True)
diff --git a/journal_article/submission/audit_packages.py b/journal_article/submission/audit_packages.py
new file mode 100644
index 00000000..5760e619
--- /dev/null
+++ b/journal_article/submission/audit_packages.py
@@ -0,0 +1,48 @@
+"""Read-only document/ZIP integrity inspection and PDF rendering; not statistical validation."""
+from pathlib import Path
+import csv, hashlib, io, json, os, re, subprocess, sys, zipfile
+from PIL import Image, ImageDraw
+ROOT = Path(__file__).resolve().parent
+ARTICLE = ROOT.parent
+RUNTIME = ARTICLE / 'qa/batch4/runtime'
+env = os.environ.copy()
+env.update({'MIKTEX_USERCONFIG': str(RUNTIME / 'config'), 'MIKTEX_USERDATA': str(RUNTIME / 'data'),
+            'MIKTEX_USERINSTALL': str(Path(os.environ['LOCALAPPDATA']) / 'Programs/MiKTeX'),
+            'MIKTEX_USERSTARTUPFILE': str(RUNTIME / 'miktexstartup.ini')})
+terms = ['umurzokov', 'kostaev', 'olimumurzokov022', 'umidjonkostaev2025', 'orcid.org/0009',
+         '0009-0008-0090-7100', '0009-0000-0205-5142', 'Tashkent State University',
+         'github.com', 'U-Olim', 'DML-IVQR_Master_Thesis', '15b8b4dc', 'ac9a9cca', '0f4188ca']
+for variant in (sys.argv[1:] or ['named', 'review', 'supplement']):
+    pdf = ROOT / ('review/supplementary_tables_review.pdf' if variant == 'supplement' else variant + '/manuscript_' + variant + '.pdf')
+    out = ROOT / 'qa' / variant
+    out.mkdir(parents=True, exist_ok=True)
+    jobs = [('info', ['pdfinfo', '-enc', 'UTF-8', str(pdf)]), ('xmp', ['pdfinfo', '-meta', str(pdf)]),
+            ('urls', ['pdfinfo', '-url', str(pdf)]), ('attachments', ['pdfdetach', '-list', str(pdf)]),
+            ('text_console', ['pdftotext', '-enc', 'UTF-8', '-layout', str(pdf), str(out / 'text.txt')]),
+            ('render_console', ['pdftoppm', '-r', '75', '-gray', '-png', str(pdf), str(out / 'page')])]
+    for label, cmd in jobs:
+        with (out / (label + '.txt')).open('w', encoding='utf-8') as h:
+            result = subprocess.run(cmd, env=env, stdout=h, stderr=subprocess.STDOUT, timeout=180)
+        assert result.returncode == 0, (variant, label, result.returncode)
+        print(variant, label, 'done', flush=True)
+    text = (out / 'text.txt').read_text(encoding='utf-8')
+    pages = [p for p in text.split('\f') if p.strip()]
+    scans = ['text', 'info', 'xmp', 'urls', 'attachments']
+    leaks = {label: [t for t in terms if t.lower() in (out / (label + '.txt')).read_text(encoding='utf-8', errors='replace').lower()] for label in scans}
+    # Utilities can log local installation paths on initialization. Metadata/URI output is still reviewed explicitly.
+    if variant != 'named':
+        assert not any(leaks.values()), leaks
+    pngs = sorted(out.glob('page-*.png'))
+    for start in range(0, len(pngs), 12):
+        canvas = Image.new('RGB', (1000, 1110), '#d0d0d0'); draw = ImageDraw.Draw(canvas)
+        for j, path in enumerate(pngs[start:start+12]):
+            im = Image.open(path).convert('RGB'); im.thumbnail((236, 337))
+            x, y = (j % 4) * 250 + 7, (j // 4) * 370 + 23
+            canvas.paste(im, (x, y)); draw.text((x, y-17), path.stem, fill='black')
+        canvas.save(out / ('contact-%s.png' % (start // 12 + 1)))
+    result = {'variant': variant, 'pdf': str(pdf.relative_to(ROOT)), 'sha256': hashlib.sha256(pdf.read_bytes()).hexdigest(),
+              'bytes': pdf.stat().st_size, 'pages': len(pages), 'rendered_pages': len(pngs),
+              'question_pairs': text.count('??'), 'blank_pages': [i+1 for i,p in enumerate(text.split('\f')[:-1]) if not p.strip()],
+              'identity_scan': leaks, 'destination_audit': 'Direct utility enumeration stalled; compiled bookmark sources inspected separately. No exhaustive object/JavaScript audit claimed.'}
+    (out / 'audit.json').write_text(json.dumps(result, indent=2), encoding='utf-8')
+    print(json.dumps(result), flush=True)
diff --git a/journal_article/submission/README.md b/journal_article/submission/README.md
new file mode 100644
index 00000000..64095dbb
--- /dev/null
+++ b/journal_article/submission/README.md
@@ -0,0 +1,11 @@
+# Local named and review document packages
+
+Canonical named source: `../main.tex` and its original dependencies. Author details and declarations reflect the latest user confirmation. The named PDF is in `named/manuscript_named.pdf`; the separately built review PDF is in `review/manuscript_review.pdf`. Both include Appendices A-D. An optional existing-table supplement is in `review/supplementary_tables_review.pdf` (also copied under `named/`). Whitelisted complete document sources are `named/source_named.zip` and `review/source_review.zip`.
+
+`review/frozen_summaries_review.zip` is a LOCAL data-access candidate containing seven unchanged archived CSVs and a neutral record inventory. It is not an approved publication supplement or a verified journal reviewer-access route. General publisher guidance distinguishes research data from ordinary supplemental material. Confirm the journal's applicable data policy and upload/visibility mechanism before using it. Remaining external provenance records, historical RNG replay, local-only raw outputs and the unresolved freeze checkout are not supplied or repaired by this bundle.
+
+The review manuscript/source masks names, affiliation/contact details, PDF author metadata, explicit public repository URLs and identifying revision tokens. Original repository paths are replaced by neutral record IDs; the full original-to-review map is `named/provenance_mapping.csv`. That mapping and all named files are identifying. Do not put them in anonymous upload categories. Distinctive scientific text and title can still be matched to public material; no guarantee of non-identifiability is made.
+
+Build helpers invoke only installed pdfLaTeX/Biber and PDF utilities. `prepare_and_build.py` copies sources/evidence, runs separate builds with package installation and shell escape disabled, and assembles packages. It reuses `../qa/batch4/runtime/`, initialized in Batch 4. `audit_packages.py` extracts text, metadata/links/destinations/embedded-file information and grayscale renders for document inspection. They do not run research code or compute statistical results. Outputs/work/QA are deliberately Git-ignored; the scripts and this note remain reviewable.
+
+See `../../journal_validation/publication_review/FINAL_PACKAGE_REPORT.md` for exact changes, hashes, actual build/inspection outcomes and unresolved requirements. No commit, push, public deposit, anonymous repository or journal submission is performed. These local artifacts are not a READY submission claim.
```

## 9. Complete named-to-review derived-source diff

These are presentation/access differences inside the source archives, not changes to canonical science. All unchanged scientific files/assets are excluded because they have no diff.

```diff
diff --git a/named_source/main.tex b/review_source/main.tex
index 071bd799..ad3e606b 100644
--- a/named_source/main.tex
+++ b/review_source/main.tex
@@ -1,20 +1,10 @@
 % Compile from journal_article/: pdflatex main; biber main; pdflatex main; pdflatex main
 \input{preamble}
 \title{Controlled Instrument-Relevance Sensitivity in High-Dimensional IVQR: A Monte Carlo Study}
-% Confirmed author order, shared affiliation and corresponding author.
-\author{\begin{minipage}{\dimexpr\textwidth-2\tabcolsep\relax}\centering
-\normalsize Umurzokov Olimjon Umidjon ugli\textsuperscript{a,*}\\
-\small ORCID: \href{https://orcid.org/0009-0008-0090-7100}{0009-0008-0090-7100}\\
-Email: \href{mailto:olimumurzokov022@gmail.com}{olimumurzokov022@gmail.com}\\[0.7em]
-\normalsize Kostaev Umidjon Umirzakovich\textsuperscript{a}\\
-\small ORCID: \href{https://orcid.org/0009-0000-0205-5142}{0009-0000-0205-5142}\\
-Email: \href{mailto:umidjonkostaev2025@gmail.com}{umidjonkostaev2025@gmail.com}\\[0.7em]
-\textsuperscript{a}Tashkent State University of Economics, Tashkent, Uzbekistan.\\[0.4em]
-\textsuperscript{*}Corresponding author: Umurzokov Olimjon Umidjon ugli;\\
-\href{mailto:olimumurzokov022@gmail.com}{olimumurzokov022@gmail.com}.
-\end{minipage}}
+% Review copy: no identities or affiliation/contact block.
+\author{}
 \date{}
-\hypersetup{pdftitle={Controlled Instrument-Relevance Sensitivity in High-Dimensional IVQR: A Monte Carlo Study},pdfauthor={Umurzokov Olimjon Umidjon ugli; Kostaev Umidjon Umirzakovich}}
+\hypersetup{pdftitle={Controlled Instrument-Relevance Sensitivity in High-Dimensional IVQR: A Monte Carlo Study},pdfauthor={}}
 \begin{document}
 \maketitle
 \noindent\textit{\{Monte Carlo simulation assesses instrument-relevance sensitivity in high-dimensional IVQR.\}}\par\medskip
diff --git a/named_source/sections/data_availability.tex b/review_source/sections/data_availability.tex
index 3c5b3fc3..49480a4a 100644
--- a/named_source/sections/data_availability.tex
+++ b/review_source/sections/data_availability.tex
@@ -1,4 +1,6 @@
 \section*{Data and code availability}
-The public repository is \url{https://github.com/U-Olim/DML-IVQR_Master_Thesis}. Repository visibility, commit \path{15b8b4dc95e3658f3b858a6f792ea2983299aaa6}, and directory listings for the main frozen CSVs, reporting summaries and package archives were checked through the GitHub API on 10 November 2026. That commit supplies the accessible evidence archive, not the current uncommitted manuscript revision. Readers can select it and follow the exact paths in Appendix~\ref{app:evidence-map} to inspect both sample sizes, all quantiles and relevance settings without running an estimator. These are simulated data and archived computational outputs, not an external observational dataset. The freeze record names \path{ac9a9ccad027cde05488abb633e66cc02f87cc46}; that identifier was not resolvable in the present local object store and returned HTTP 404 from the repository API. It is retained as recorded provenance, not offered as a verified release checkout.
+This study uses simulated data and archived computational outputs. A local optional evidence bundle, \texttt{frozen\_summaries\_review.zip}, contains seven existing compact CSV summaries and a record inventory. These files have been copied without numerical changes; they support inspection without re-estimation. Their inclusion in this local package is not verification of reviewer access through the journal. Anonymous access to the full external archive and remaining provenance records has not been arranged or verified.
 
-Historical rerunning is a different task. Source and configuration are under \path{thesis_extension/src/} and \path{thesis_extension/config/}; environment records, package archives and the captured Windows library are under \path{thesis_extension/environment/}. The recorded environment uses R~3.4.3 and pinned historical packages (Appendix~\ref{app:reproducibility}); their presence does not establish installation portability or exact random-number replay. Main-run worker-specific penalty states are not recoverable from the parent seed alone. Large grid-diagnostic profiles and saved primitives are local, Git-ignored artifacts identified in \path{thesis_extension/diagnostics/grid_sensitivity/GRID_RESULTS_MANIFEST.csv}; tracked diagnostic summaries remain available. Stage 2H pilot outputs under \path{journal_validation/stage2h/pilot/runs/} and its \path{journal_validation/stage2h/pilot/SHA256_MANIFEST.json} are also Git-ignored and are not part of the public tracked archive. No public deposit of these local artifacts or portable historical runtime is established here. This revision does not publish new results or replace historical fits with later certified numerical solutions.
+Appendix~\ref{app:evidence-map} retains the claim-to-evidence map with neutral record identifiers. The bundle inventory distinguishes included summaries from records that are not attached. The full original path/revision mapping is retained in the named package. The historical freeze checkout remains unresolved; its identifying token is withheld in this review copy, not replaced by a verified release claim. A checked evidence checkpoint does not identify the current manuscript revision.
+
+Historical rerunning requires the recorded R~3.4.3 environment and pinned dependencies. Their presence in the original archive does not establish portability or exact replay. Main-run worker-specific penalty states are not recoverable from the parent seed alone. Large grid-diagnostic profiles/primitives and Stage 2H pilot raw outputs and their seal are local, Git-ignored artifacts, not promised public or attached data. No public deposit of those artifacts or portable historical runtime is established. Historical estimator results have not been replaced by later certified solutions.
diff --git a/named_source/supplementary/D_implementation.tex b/review_source/supplementary/D_implementation.tex
index 9539039e..e85c92fd 100644
--- a/named_source/supplementary/D_implementation.tex
+++ b/review_source/supplementary/D_implementation.tex
@@ -3,19 +3,19 @@
 \label{app:reproducibility}
 \setcounter{equation}{0}\setcounter{table}{0}\setcounter{figure}{0}
 \subsection{Environment, records, and reproducibility limits}
-The computational archive is the project repository \url{https://github.com/U-Olim/DML-IVQR_Master_Thesis}. This reference identifies the archived workflow; it is not a claim of bit-for-bit regeneration from a seed on arbitrary systems. Preserved source is in \path{simulation/}, \path{Empirical_work/}, and \path{example/}; extension wrappers and configuration are in \path{thesis_extension/src/} and \path{thesis_extension/config/extension_config.R}. The checked accessible evidence archive is commit \texttt{15b8b4dc}; it contains the earlier editorial batches. Current manuscript revisions are local and uncommitted. The freeze record's historical identifier \texttt{ac9a9cca} (2 September 2026) remains unresolved; full identifiers and access limits appear in the data and code availability statement.
+The full archive location, revision identifiers and original paths are withheld in this review copy to limit direct identification. Neutral record identifiers below preserve the evidence associations; the full mapping is retained with the named package. Only the compact CSV summaries identified in the optional bundle inventory are attached locally. Full external anonymous access is not arranged or verified, and the historical freeze checkout remains unresolved. These access limits do not imply bit-for-bit regeneration from a seed on arbitrary systems.
 
-The canonical environment is R~3.4.3 (30 November 2017) on 64-bit Windows, using five workers. The captured attached packages are \texttt{doSNOW} 1.0.16, \texttt{snow} 0.4-2, \texttt{iterators} 1.0.8, \texttt{foreach} 1.4.3, \texttt{mvtnorm} 1.0-6, \texttt{hqreg} 1.4, \texttt{hdm} 0.2.0, \texttt{quantreg} 5.34, and \texttt{SparseM} 1.77. Environment session and library manifests are under \path{thesis_extension/environment/}. The main simulation uses seed 675; the grid diagnostic also uses seed 675, with saved primitives reloaded in Stage 2; calibration uses seed 20260813. Worker-specific RNG streams are not explicitly initialized in the preserved parallel DML procedure, so the parent seed alone does not establish exact regeneration of every penalty draw.
+The canonical environment is R~3.4.3 (30 November 2017) on 64-bit Windows, using five workers. The captured attached packages are \texttt{doSNOW} 1.0.16, \texttt{snow} 0.4-2, \texttt{iterators} 1.0.8, \texttt{foreach} 1.4.3, \texttt{mvtnorm} 1.0-6, \texttt{hqreg} 1.4, \texttt{hdm} 0.2.0, \texttt{quantreg} 5.34, and \texttt{SparseM} 1.77. Environment session and library manifests are under \texttt{R037}. The main simulation uses seed 675; the grid diagnostic also uses seed 675, with saved primitives reloaded in Stage 2; calibration uses seed 20260813. Worker-specific RNG streams are not explicitly initialized in the preserved parallel DML procedure, so the parent seed alone does not establish exact regeneration of every penalty draw.
 
-Frozen CSVs permit deterministic reporting without re-estimation. Input/output manifests in \path{thesis_extension/reporting/}, diagnostic provenance records, reporting consistency checks, and figure validation records connect the reported numbers to archived outputs. Historical manifests describe their archived presentation state and can retain former asset paths. The original figure check covered 480 plotted values; selected-figure validation separately covered 120 coverage values, 120 full-grid frequencies, and 168 median rejection probabilities. The coverage summary is reconstructed from integer direct-at-truth counts; the variance illustration is analytical. This editorial conversion does not rerun those historical validations or simulations.
+Frozen CSVs permit deterministic reporting without re-estimation. Input/output manifests in \texttt{R049}, diagnostic provenance records, reporting consistency checks, and figure validation records connect the reported numbers to archived outputs. Historical manifests describe their archived presentation state and can retain former asset paths. The original figure check covered 480 plotted values; selected-figure validation separately covered 120 coverage values, 120 full-grid frequencies, and 168 median rejection probabilities. The coverage summary is reconstructed from integer direct-at-truth counts; the variance illustration is analytical. This editorial conversion does not rerun those historical validations or simulations.
 
-The original Monte Carlo results remain outputs of the preserved historical executable implementation. Later selected-case Stage 2G audits identified sensitivity of residual ranks and test decisions to computational details: historical Policy A and the certified-outcome Policy C path differed in 5 of the 24 saved candidate problems examined. Policy C uses exact outcome residual ranks with the retained density/projection pathway; these panel results do not replace the historical Monte Carlo results. Numerical certificates establish properties of specified fixed objectives and input values, with decision bounds conditional on the stated exported quantities; they do not establish invariance of every historical Monte Carlo decision or certify all adaptive calibration trajectories. The selected panels do not establish an error frequency for the full Monte Carlo experiment.\footnote{See \path{journal_validation/stage2g/full_path_validation/FULL_PATH_REPORT.md}, ``Complete 24-problem decision comparison'' and ``Required conclusions''; and \path{journal_validation/stage2g/deterministic_implementation/DETERMINISTIC_IMPLEMENTATION_REPORT.md}, ``Mathematical equivalence: established scope''.}
+The original Monte Carlo results remain outputs of the preserved historical executable implementation. Later selected-case Stage 2G audits identified sensitivity of residual ranks and test decisions to computational details: historical Policy A and the certified-outcome Policy C path differed in 5 of the 24 saved candidate problems examined. Policy C uses exact outcome residual ranks with the retained density/projection pathway; these panel results do not replace the historical Monte Carlo results. Numerical certificates establish properties of specified fixed objectives and input values, with decision bounds conditional on the stated exported quantities; they do not establish invariance of every historical Monte Carlo decision or certify all adaptive calibration trajectories. The selected panels do not establish an error frequency for the full Monte Carlo experiment.\footnote{See \texttt{R023}, ``Complete 24-problem decision comparison'' and ``Required conclusions''; and \texttt{R021}, ``Mathematical equivalence: established scope''.}
 
 \input{supplementary/D_evidence_map}
 
 \subsection{Historical evaluation sequence}
 \label{app:evaluation-sequence}
-The operational source is \path{thesis_extension/src/run_extension.R}, with candidate routines in \path{thesis_extension/src/author_bc_dml_wrapper.R} and \path{thesis_extension/src/author_oracle_wrapper.R}. One replication proceeds as follows.
+The operational source is \texttt{R057}, with candidate routines in \texttt{R055} and \texttt{R056}. One replication proceeds as follows.
 \begin{enumerate}
 \item Generate one set of primitives; construct a sample at each relevance setting. Within that setting all three estimators share $(Y,D,X,Z)$. Reusing primitives across settings does not hold realized $(Y,D)$ fixed.
 \item For each quantile and estimator, profile the ordered 41-point primary grid. At each DML candidate $a$, call \texttt{lambda\_BC\_author} afresh (1000 artificial uniform columns), then fit \texttt{quantreg::rq(y-a*D\string~X, method="lasso")} with the resulting penalty and an intercept. Refit nuisances at each candidate; there is no post-Lasso refit. Oracle and Full instead call unpenalized \texttt{quantreg::rq} with their designated controls.
@@ -177,13 +177,13 @@ The first five equations describe DML-IVQR. The last three describe Oracle-GMM a
 \label{app:finite-solvers}
 The argmin displays above specify optimization objectives; the archived coefficients are finite routine outputs, not certified exact minimizers. The DML outcome route is \texttt{quantreg::rq(..., method="lasso")} / \texttt{rq.fit.lasso} in \texttt{quantreg}~5.34. It uses augmented observations and the penalized intercept described above. Oracle and Full use the package's default unpenalized \texttt{rq} route. Computed residual signs, including exact floating-point zeros, feed the literal $\leq0$ rule; small objective errors alone do not establish rank or decision invariance.
 
-Instrument fitting uses \texttt{hdm}~0.2.0 \texttt{rlasso} with \texttt{post=FALSE}, the default heteroskedastic, X-independent loading calculation and an ordinary unpenalized intercept. In the retained source, outer calibration has \texttt{numIter=15} and \texttt{tol=1e-5}; it stops when the absolute change in the estimated residual standard deviation is below the tolerance or the iteration budget is exhausted. A zero-selected-coefficient branch can return early. Inner \texttt{LassoShooting.fit} uses \texttt{maxIter=1000}, \texttt{optTol=1e-5} and \texttt{zeroThreshold=1e-6}; its loop starts at one and runs while the counter is below the maximum, stopping early when the sum of absolute coefficient changes falls below \texttt{optTol}. The returned small coefficients are thresholded. These are finite algorithmic conventions, not accuracy certificates. The pinned source is in \path{thesis_extension/environment/package_archives_R343/hdm_0.2.0.tar.gz} (\path{hdm/R/rlasso.R} and \path{hdm/R/LassoShooting.fit.R} inside that archive).
+Instrument fitting uses \texttt{hdm}~0.2.0 \texttt{rlasso} with \texttt{post=FALSE}, the default heteroskedastic, X-independent loading calculation and an ordinary unpenalized intercept. In the retained source, outer calibration has \texttt{numIter=15} and \texttt{tol=1e-5}; it stops when the absolute change in the estimated residual standard deviation is below the tolerance or the iteration budget is exhausted. A zero-selected-coefficient branch can return early. Inner \texttt{LassoShooting.fit} uses \texttt{maxIter=1000}, \texttt{optTol=1e-5} and \texttt{zeroThreshold=1e-6}; its loop starts at one and runs while the counter is below the maximum, stopping early when the sum of absolute coefficient changes falls below \texttt{optTol}. The returned small coefficients are thresholded. These are finite algorithmic conventions, not accuracy certificates. The pinned source is in \texttt{R038} (\texttt{R004} and \texttt{R003} inside that archive).
 
-The outer routine updates loadings after a finite shooting fit. Its reported next penalty need not be the last penalty actually used to produce those coefficients. The later contract \path{journal_validation/stage2g/deterministic_implementation/IMPLEMENTATION_CONTRACT_v1.md} distinguishes preservation of the adaptive trajectory from refinement of the final centered objective at the last-used penalty. Refined final coefficients are not fed back into that trajectory under its Policy B contract; recalibration is a different pathway. Those selected-case numerical investigations do not establish exact attainment by historical fits. No certified solution, altered residual threshold or revised penalty path replaces any archived estimator result here. The selected-panel decision-sensitivity disclosure above remains applicable.
+The outer routine updates loadings after a finite shooting fit. Its reported next penalty need not be the last penalty actually used to produce those coefficients. The later contract \texttt{R022} distinguishes preservation of the adaptive trajectory from refinement of the final centered objective at the last-used penalty. Refined final coefficients are not fed back into that trajectory under its Policy B contract; recalibration is a different pathway. Those selected-case numerical investigations do not establish exact attainment by historical fits. No certified solution, altered residual threshold or revised penalty path replaces any archived estimator result here. The selected-panel decision-sensitivity disclosure above remains applicable.
 
 \subsection{Retained density-divergence argument for the original DGP}
 \label{app:density-divergence}
-This argument is reproduced from Section 3 of \path{journal_validation/stage2h/readiness/BOUNDED_DGP_DERIVATION.md}, specifically its analysis of the original $D=\Phi(T)$ construction; no bounded-treatment results are substituted. Put $\rho=0.3$, $q_\tau=\Phi^{-1}(\tau)$, $Q_j=Z_j-h_j(X)=z_j+v_j$, and $\mu_Q=\kappa(Q_1+Q_2)/2$. The observed instrument shifts $h_j(X)$ are given in the DGP. Since $Q\sim\mathcal N(0,2I_2)$, Gaussian conditioning in the retained derivation gives
+This argument is reproduced from Section 3 of \texttt{R026}, specifically its analysis of the original $D=\Phi(T)$ construction; no bounded-treatment results are substituted. Put $\rho=0.3$, $q_\tau=\Phi^{-1}(\tau)$, $Q_j=Z_j-h_j(X)=z_j+v_j$, and $\mu_Q=\kappa(Q_1+Q_2)/2$. The observed instrument shifts $h_j(X)$ are given in the DGP. Since $Q\sim\mathcal N(0,2I_2)$, Gaussian conditioning in the retained derivation gives
 \[
  T\mid Q\sim\mathcal N(\mu_Q,v_\kappa),\qquad v_\kappa=3-\kappa^2,
  \qquad
diff --git a/named_source/supplementary/D_evidence_map.tex b/review_source/supplementary/D_evidence_map.tex
index e63aec65..97ef1eb6 100644
--- a/named_source/supplementary/D_evidence_map.tex
+++ b/review_source/supplementary/D_evidence_map.tex
@@ -1,6 +1,6 @@
 \subsection{Frozen-evidence map}
 \label{app:evidence-map}
-All paths below are repository-relative. The checked accessible evidence revision is \texttt{15b8b4dc}; it is distinct from both the unresolved historical freeze identifier and the current uncommitted manuscript revision. Full identifiers and access limitations appear in the data and code availability statement. Keys E1--E6 connect the principal findings to saved evidence, including cells omitted from compact main-text displays. This map identifies sources; it does not recompute descriptive comparison counts or rerun historical checks.
+Repository locations and revision identifiers are withheld in this review copy. Neutral record identifiers below correspond to the retained named evidence map; the optional CSV bundle inventory states which records are included and which are not attached. Full external anonymous access remains unresolved. Keys E1--E6 retain their original claim/evidence associations; no comparison count or statistic is recomputed.
 
 \begin{center}
 \small
@@ -18,17 +18,17 @@ Selected-case rank and decision sensitivity & Appendix~\ref{app:reproducibility}
 \begingroup\small\raggedright
 \Urlmuskip=0mu plus 1mu\relax
 \begin{description}
-\item[E1: Relevance.] \path{thesis_extension/calibration/instrument_strength_100rep/kappa_strength_summary.csv}; presentation: \path{journal_article/tables/table_strength_calibration.tex}.
+\item[E1: Relevance.] \texttt{R028}; presentation: \texttt{R019}.
 
-\item[E2: Full performance.] \path{thesis_extension/final/output/n500/summary.csv} and \path{thesis_extension/final/output/n1000/summary.csv} contain Bias, MAE, RMSE, historical \texttt{Coverage}/\texttt{Size}, accepted-measure and boundary/full-grid summaries. Replication-level sources are \path{thesis_extension/final/output/n500/results.csv} and \path{thesis_extension/final/output/n1000/results.csv}; stored candidate statistics are \path{thesis_extension/final/output/n500/profiles.csv} and \path{thesis_extension/final/output/n1000/profiles.csv}. Full presentation assets: \path{journal_article/tables/generated/appendix_point_performance.tex}, \path{journal_article/tables/generated/appendix_coverage.tex}, and \path{journal_article/tables/generated/appendix_cr_informativeness.tex}; compact table: \path{journal_article/tables/table_main_performance.tex}. Existing RMSE images are \path{journal_article/figures/generated/rmse_n500.png} and \path{journal_article/figures/generated/rmse_n1000.png}.
+\item[E2: Full performance.] \texttt{R048} and \texttt{R043} contain Bias, MAE, RMSE, historical \texttt{Coverage}/\texttt{Size}, accepted-measure and boundary/full-grid summaries. Replication-level sources are \texttt{R047} and \texttt{R042}; stored candidate statistics are \texttt{R046} and \texttt{R041}. Full presentation assets: \texttt{R016}, \texttt{R013}, and \texttt{R014}; compact table: \texttt{R018}. Existing RMSE images are \texttt{R011} and \texttt{R010}.
 
-\item[E3: Truth testing and power.] Use E2's \texttt{Coverage}, \texttt{Size} and replication \texttt{W\_true} fields for direct-at-truth evaluations. False-candidate summaries are \path{thesis_extension/final/output/n500/power_summary.csv} and \path{thesis_extension/final/output/n1000/power_summary.csv}; replication records are \path{thesis_extension/final/output/n500/power.csv} and \path{thesis_extension/final/output/n1000/power.csv}. Full presentation: \path{journal_article/tables/generated/appendix_power.tex}; figures: \path{journal_article/figures/generated/coverage_heatmap.pdf} and \path{journal_article/figures/generated/power_median_combined.pdf}. The abstract's $0.942/3.900/0.094$ contrast selects E2's \texttt{Coverage}/\texttt{median\_grid\_accepted\_set\_measure} and this power summary's \texttt{power}, respectively, at $n=1000$, $\tau=0.50$, $\kappa=0.10$, estimator \texttt{DML-IVQR-BC}, with $\Delta=0.50$ for power only. These are different summaries, not a joint event or validated grid-set coverage.
+\item[E3: Truth testing and power.] Use E2's \texttt{Coverage}, \texttt{Size} and replication \texttt{W\_true} fields for direct-at-truth evaluations. False-candidate summaries are \texttt{R045} and \texttt{R040}; replication records are \texttt{R044} and \texttt{R039}. Full presentation: \texttt{R017}; figures: \texttt{R007} and \texttt{R009}. The abstract's $0.942/3.900/0.094$ contrast selects E2's \texttt{Coverage}/\texttt{median\_grid\_accepted\_set\_measure} and this power summary's \texttt{power}, respectively, at $n=1000$, $\tau=0.50$, $\kappa=0.10$, estimator \texttt{DML-IVQR-BC}, with $\Delta=0.50$ for power only. These are different summaries, not a joint event or validated grid-set coverage.
 
-\item[E4: Grid informativeness.] In addition to E2's summaries/profiles, \path{thesis_extension/reporting/output/table_cr_informativeness_full.csv} contains all design cells. Existing images are \path{journal_article/figures/generated/accepted_measure_n500.png}, \path{journal_article/figures/generated/accepted_measure_n1000.png}, and \path{journal_article/figures/generated/full_domain_acceptance_heatmap.pdf}. Grid quadrature and all-grid acceptance are distinct diagnostics on the maintained domain.
+\item[E4: Grid informativeness.] In addition to E2's summaries/profiles, \texttt{R052} contains all design cells. Existing images are \texttt{R006}, \texttt{R005}, and \texttt{R008}. Grid quadrature and all-grid acceptance are distinct diagnostics on the maintained domain.
 
-\item[E5: Domain expansion.] Tracked sources: \path{thesis_extension/diagnostics/grid_sensitivity/output/stage1/stage1_summary.csv}, \path{thesis_extension/diagnostics/grid_sensitivity/output/stage1/stage1_expansion_summary.csv}, \path{thesis_extension/diagnostics/grid_sensitivity/output/stage2/stage2_summary.csv}, and \path{thesis_extension/diagnostics/grid_sensitivity/output/stage2/stage2_expansion_summary.csv}. Combined reporting view: \path{thesis_extension/reporting/output/table_grid_domain_diagnostic.csv}; table and figure: \path{journal_article/tables/generated/appendix_grid_diagnostic.tex} and \path{journal_article/figures/grid_domain_expansion.png}. Design, failure and local-only artifact scope are in \path{thesis_extension/diagnostics/grid_sensitivity/GRID_RESULTS_PROVENANCE.md} and \path{thesis_extension/diagnostics/grid_sensitivity/GRID_RESULTS_MANIFEST.csv}. This separate diagnostic uses 100 intended replications; the recorded Stage 1 failure remains excluded from complete-profile summaries, not counted as acceptance. Large profiles and saved primitives are Git-ignored; tracked summaries do not supply full stochastic replay.
+\item[E5: Domain expansion.] Tracked sources: \texttt{R034}, \texttt{R033}, \texttt{R036}, and \texttt{R035}. Combined reporting view: \texttt{R053}; table and figure: \texttt{R015} and \texttt{R012}. Design, failure and local-only artifact scope are in \texttt{R032} and \texttt{R031}. This separate diagnostic uses 100 intended replications; the recorded Stage 1 failure remains excluded from complete-profile summaries, not counted as acceptance. Large profiles and saved primitives are Git-ignored; tracked summaries do not supply full stochastic replay.
 
-\item[E6: Numerical sensitivity.] \path{journal_validation/stage2g/full_path_validation/FULL_PATH_REPORT.md} records the selected 24-problem comparison and five Policy A/C decision differences. \path{journal_validation/stage2g/deterministic_implementation/DETERMINISTIC_IMPLEMENTATION_REPORT.md} and \path{journal_validation/stage2g/deterministic_implementation/IMPLEMENTATION_CONTRACT_v1.md} specify the fixed-objective and input scope of later certificates. Earlier rank-stability evidence is in \path{journal_validation/stage2c/stability/STABILITY_REPORT.md}. These reports are not population error rates or replacements for E2--E5.
+\item[E6: Numerical sensitivity.] \texttt{R023} records the selected 24-problem comparison and five Policy A/C decision differences. \texttt{R021} and \texttt{R022} specify the fixed-objective and input scope of later certificates. Earlier rank-stability evidence is in \texttt{R020}. These reports are not population error rates or replacements for E2--E5.
 \end{description}
 \endgroup
-The inventories \path{thesis_extension/reporting/EMPIRICAL_RESULTS_MANIFEST.csv} and \path{thesis_extension/reporting/REPORTING_OUTPUT_MANIFEST.csv} retain historical input/output hashes and provenance. An entry in a manifest alone does not establish public availability: local-only exclusions are stated in the data and code availability statement.
+The inventories \texttt{R050} and \texttt{R051} retain historical input/output hashes and provenance. An entry in a manifest alone does not establish public availability: local-only exclusions are stated in the data and code availability statement.
```

## 10. Exact optional table-wrapper sources

Existing table assets are included unchanged; only the standalone wrapper/preamble below are generated.

### `supplementary_tables.tex`

```latex
\input{supplement_preamble}
\hypersetup{pdftitle={Supplementary Tables: Full Frozen Results},pdfauthor={}}
\renewcommand{\thetable}{S.\arabic{table}}
\begin{document}
\section*{Supplementary Tables: Full Frozen Results}
These optional tables reproduce existing frozen presentation assets without new calculations. They retain all sample sizes, quantiles and relevance settings in those assets. Direct-at-truth acceptance, false-candidate rejection and finite-grid informativeness are distinct summaries. The historical Coverage label is not independently validated coverage of the stored finite-grid accepted set. Interpretation remains subject to the implementation and numerical limitations in the manuscript.
\input{tables/generated/appendix_point_performance}
\input{tables/generated/appendix_coverage}
\input{tables/generated/appendix_power}
\input{tables/generated/appendix_cr_informativeness}
\end{document}
```

### `supplement_preamble.tex`

```latex
\documentclass[11pt,a4paper]{article}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage[english]{babel}
\usepackage[margin=25mm]{geometry}
\usepackage{newtxtext,newtxmath}
\renewcommand{\ttdefault}{lmtt}
\usepackage{amsmath,mathtools}
\usepackage{graphicx,booktabs,ragged2e,etoolbox,placeins,needspace}
\usepackage{tabularray}
\UseTblrLibrary{booktabs,siunitx}
\usepackage[font=small,labelfont=bf,labelsep=period]{caption}
\usepackage{csquotes}
\usepackage{xurl}
\usepackage[hidelinks]{hyperref}
\usepackage{microtype}
\SetTblrInner[booktabs]{width=\textwidth,row{1}={font=\bfseries},hline{1,Z}={0.8pt},hline{2}={0.4pt}}
\SetTblrStyle{remark-text}{font=\footnotesize}
\SetTblrStyle{remark-tag}{font=\footnotesize\itshape}
\newenvironment{tablenotes}[1][Note]{\par\medskip\begingroup\footnotesize\noindent\textit{#1:} }{\par\endgroup}
\newenvironment{figurenotes}[1][Note]{\par\medskip\begingroup\footnotesize\noindent\textit{#1:} }{\par\endgroup}
\newlength{\baselinedist}\setlength{\baselinedist}{\baselineskip}
\setlength{\emergencystretch}{2em}
\setcounter{topnumber}{3}\setcounter{totalnumber}{4}
\renewcommand{\topfraction}{.95}\renewcommand{\textfraction}{.05}
\renewcommand{\floatpagefraction}{.75}
\raggedbottom
```

## Final working-tree status

```text
 M journal_article/.gitignore
 M journal_article/README.md
 M journal_article/main.tex
 M journal_article/sections/submission_declarations.tex
?? journal_article/submission/
?? journal_validation/publication_review/FINAL_PACKAGE_REPORT.md
```
