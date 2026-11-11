# Scientific integrity and document QA audit

Document-only audit; no research validation performed.

| Check | Actual result |
|---|---|
| protected files checked | 192 |
| protected changes | [] |
| all tracked files unchanged | True |
| abstract verbatim | True |
| title author metadata verbatim | True |
| appendix B byte identical | True |
| mathematical displays identical | True |
| figure bibliography bytes identical | True |
| table asset bytes identical except prose note | True |
| main table body identical | True |
| relocated table blocks identical | True |
| full evidence inventory verbatim | True |
| main reference warnings | [] |
| main overfull boxes | [] |
| technical supplement reference warnings | [] |
| technical supplement overfull boxes | [] |
| main sections unique numeric tokens lost | [] |
| numbered scientific labels preserved across two documents | 72 |
| citation key set unchanged | True |
| relocated inventory paths present | 40 |
| visual inspection | All 29 main and 5 technical pages reviewed in rendered contact sheets; no evident missing/cropped displays or blank pages. No full-resolution typographic certification. |

## Page-count comparison

| Document | Original | Proposed |
|---|---:|---:|
| Named main PDF including inline appendices | 34 | 29 |
| Separate detailed technical tables | — | 5 |
| Combined PDF pages | 34 | 34 |

The proposed combined PDFs have the same total page count. The smaller main PDF reflects relocation and modest wording changes, not five pages of scientific deletion. The relocated Markdown inventory is additional supplied material. Main text ends on p.16 in both versions; proposed references begin on p.16 rather than p.17. Inline appendices start on p.18 in both; Appendix A occupies pp.18–20, B starts p.21, C p.22 and D p.25.

No final-build undefined/multiply-defined references, unresolved citation warnings, literal ?? placeholders or overfull boxes were found. Scientific label numbers match across the main and technical PDFs, including moved tables. All seven build steps exited zero. MiKTeX prints an update-maintenance notice; no package installation/update or global runtime repair was attempted.

Rendered contact sheets cover all pages. The technical supplement begins its first long table on p.1 and continues on p.2; the continuation is labelled and not lost content. Other long tables and figure captions remain within page boundaries. Existing small table fonts are retained, not reduced to meet a page target.

## Limits

Byte/text preservation and document consistency do not establish inference validity, reproduce stochastic calculations, verify every reported numerical count, establish public evidence access or certify historical numerical decisions. Original research limitations remain binding. Protected-file hashes cover 192 canonical dependencies/research scripts; Git confirms all tracked files, including tracked datasets, are unchanged. Untracked research artifacts were not enumerated as a full dataset inventory and were not targeted by any write operation. Local MiKTeX runtime logs/configuration can be refreshed by document tools.