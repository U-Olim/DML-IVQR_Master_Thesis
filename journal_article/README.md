# Journal article

Start with `main.pdf`. The review PDF contains the article, references, and online supplementary Appendices A–E. Supplement sources are under `supplementary/`; this keeps cross-references local and resolved. All figures, tables, and the bibliography needed for compilation are included. Simulation datasets are linked through the repository documentation, not copied here.

From this directory, run:

```powershell
.\build.ps1
```

Alternatively: `pdflatex main`, `biber main`, `pdflatex main`, `pdflatex main`. A working TeX installation with the packages in `preamble.tex` is required. `python verify_article.py` performs read-only integrity checks against the original project and writes `qa/validation.json`. It does not run simulations.

Read `EDIT_REPORT.md` before preparing submission. Author metadata and declarations need confirmation, and the journal's detailed instructions/template could not be verified. The author field is intentionally empty. The repository URL in Appendix D identifies the project and must be reviewed for double-anonymized submission.
