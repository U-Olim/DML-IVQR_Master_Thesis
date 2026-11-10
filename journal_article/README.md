# Journal article ? submission preparation

`main.tex` is the named manuscript master. Its approved title is **Controlled Instrument-Relevance Sensitivity in High-Dimensional IVQR: A Monte Carlo Study**. Main sections are in `sections/`; `sections/submission_declarations.tex` contains the author-approved funding, conflict, equal-contribution, AI-assistance and simulated-data ethics declarations, and `sections/data_availability.tex` distinguishes the checked evidence archive from local-only files and the unresolved historical freeze identifier.

The review document includes the article, references and supplementary **Appendices A?D**:

- A: numerical-domain diagnostics, including the recorded candidate failure and finite-domain limits.
- B: controlled-relevance construction and distributional invariances.
- C: direct-at-truth coverage audit and its limits.
- D: reproducibility/environment notes, the complete frozen-evidence map (`supplementary/D_evidence_map.tex`), historical evaluation sequence, penalty/proxy/residualization definitions, finite-solver limitations, retained mixed-density divergence and conditional ideal-score algebra.

Existing figures, tables and bibliography are used directly. No simulation or statistical-result generation is part of the document build. Complete numerical table assets remain under `tables/generated/`; not all are input into the PDF. The evidence map identifies their frozen CSV sources.

## Current document and build evidence

The historical root `main.pdf` and `EDIT_REPORT.md` describe earlier revisions. Do not assume they match the current source. The Batch 4 document-only build and inspection artifacts are under `qa/batch4/`; consult [BATCH4_CHANGE_REPORT.md](../journal_validation/publication_review/BATCH4_CHANGE_REPORT.md) for actual results and remaining blockers. Those records describe the earlier named draft. Final package outputs are `submission/named/manuscript_named.pdf` and `submission/review/manuscript_review.pdf`; the current package report is [FINAL_PACKAGE_REPORT.md](../journal_validation/publication_review/FINAL_PACKAGE_REPORT.md).

For an ordinarily configured TeX installation, run from this directory:

```powershell
.\build.ps1
```

That script runs pdfLaTeX, Biber and two further pdfLaTeX passes. It writes root document outputs, so preserve any historical PDF that is needed before rebuilding there. It does not run research code. A working installation with the packages in `preamble.tex`, including `xurl` for long repository paths, is required.

Batch 4 uses `python qa/batch4/build_document.py` to keep document outputs and a job-local MiKTeX configuration under `qa/batch4/`, with package installation and TeX shell escape disabled. The helper is specific to this Windows MiKTeX installation, reads only selected existing configuration fields, and invokes the installed Biber binary directly. It neither repairs the global installation nor promises a portable runtime. Job-local runtime caches and intermediate files are Git-ignored.

`verify_article.py` and the scripts in `qa/` are version-specific document checks. They can write QA outputs; they are not strictly read-only commands. Earlier `validation.json`, `revision_validation.json`, `revision_build.log`, `revision_pdfinfo.txt`, `revision_title.png`, contact sheets and `qa/article_text.txt` remain historical evidence for their recorded source state. No old pass certifies a later source revision. Do not rerun old scripts as a substitute for inspecting their assumptions.

## Submission blockers

This named master is **not a submission-ready anonymous file**. The publisher's indexed journal information specifies double-anonymous review. Names, contact details, PDF author metadata and the identifying repository link need a separate review-file treatment and a usable anonymous evidence-access route; the complete named master/evidence map should be preserved. The exact current instructions/portal requirements are not fully accessible.

The authors have confirmed the order Umurzokov Olimjon Umidjon ugli, then Kostaev Umidjon Umirzakovich, a shared Tashkent State University of Economics affiliation, the first author as corresponding author, and the declarations now in source. PDF author metadata matches that order. DSc is not printed because the journal convention remains unverified. Tool/model versions and the publisher-specific AI/translation responsibility confirmations remain to be resolved. The separately built review copy masks explicit identities and searchable provenance, but full external anonymous evidence access and remaining journal requirements are not established. Older checklists and QA records retain their historical status; consult the final package report for current results.

The checked accessible evidence revision is `15b8b4dc95e3658f3b858a6f792ea2983299aaa6`; it includes earlier editorial batches, not the current uncommitted manuscript. The freeze record's identifier `ac9a9ccad027cde05488abb633e66cc02f87cc46` remains unresolved locally and returned 404 remotely during Batch 3. Main frozen summaries are tracked; Git-ignored grid profiles/primitives and Stage 2H pilot raw outputs are not promised as public. No commit or push is part of these revisions.


Final local package build: `python submission/prepare_and_build.py`; inspection: `python submission/audit_packages.py`. These document-only helpers reuse the initialized Batch 4 local MiKTeX runtime. Appendices A-D remain inline. The existing-table PDF is an optional supplement, while the compact CSV ZIP is a local data-access candidate, not an approved publication supplement. No upload, public deposit or submission has been made.
