# Optimization cancelled; canonical corrections verified

11 November 2026 (Asia/Tashkent). Branch: `journal-validation`.

## Master version and archives

The full original `journal_article/main.tex` dependency tree remains the master. All original Sections 1?6 and Appendices A?D remain inline and in their original order. No shortening, inventory relocation, split-table dependency or separate technical-supplement delivery is adopted. The 29-page optimized manuscript and 5-page technical supplement are archival experiments only. This status supersedes any adoption recommendation in the optimization report.

All pre-existing optimization artifacts, the optimization report and content audit were hash-checked and remain unchanged. The cancellation does not delete or merge those records.

The original named 34-page PDF is unchanged: `journal_article/submission/named/manuscript_named.pdf`, SHA-256 `4fecad9e125211689910104b8b533cb5e03f1d96e24752dc58bb62b5e77e3388`. Only approved canonical LaTeX corrections are applied in this task; no PDF is rebuilt. That preserved PDF is the pre-correction build, not a freshly compiled representation of the corrected source.

## Approved corrections applied

Thirteen literal replacements implement exactly M1?M3 and E1?E3; no other optimization edit is applied.

| Issue | Canonical file / line | Approved replacement |
|---|---|---|
| E3 | journal_article/sections/02_framework.tex:168 | the first candidate attaining the minimum stored grid statistic is retained |
| M3 | journal_article/sections/04_results.tex:24 | These reductions show lower observed Monte Carlo RMSE at the larger sample size |
| E1 | journal_article/sections/04_results.tex:32 | \subsection{Direct-at-Truth Acceptance and Finite-Sample Calibration} |
| E1 | journal_article/sections/04_results.tex:35 | shows that direct-at-truth acceptance (historically labelled coverage) differs considerably |
| M3 | journal_article/sections/04_results.tex:43 | Under independent replications, its conventional plug-in Monte Carlo standard error is |
| M3 | journal_article/sections/04_results.tex:49 | An individual rate's MCSE is not used as the standard error of a difference between correlated simulation results. These uncertainty summaries assume independent replications; the historical DML worker-stream independence is not verified (Appendix~\ref{app:evaluation-sequence}). |
| E2 | journal_article/sections/04_results.tex:73 | Thus lower designed relevance is accompanied by a progressively larger median grid-acceptance measure, even when direct-at-truth acceptance moves closer to $0.95$. |
| E2 | journal_article/sections/04_results.tex:77 | The larger sample has a smaller or unchanged observed median accepted measure in these comparisons, with little localization under the weakest relevance setting. |
| M1 | journal_article/supplementary/A_numerical_domain.tex:18 | A value close to four in \(A_0\) means that the trapezoidal grid-acceptance summary is close to its maximum on the four-unit primary domain; it does not establish acceptance between evaluated points or unrestricted confidence-region length. |
| E1 | journal_article/tables/table_main_performance.tex:51 | Coverage denotes direct-at-truth test acceptance, not membership coverage of the stored grid set. |
| M2 | journal_article/sections/data_availability.tex:2 | That commit supplies the checked evidence archive, rather than identifying the present manuscript version. |
| M2 | journal_article/supplementary/D_implementation.tex:6 | The present manuscript version is distinct from that checked evidence revision. |
| M2 | journal_article/supplementary/D_evidence_map.tex:3 | it is distinct from both the unresolved historical freeze identifier and the present manuscript version. |

## Verification

- Each of the seven modified files exactly matches its pre-edit working-tree bytes plus the approved replacements. All initial files matched HEAD after Git newline normalization; existing CRLF/LF bytes were preserved during editing.
- The earlier 192-file SHA-256 baseline identifies exactly these seven changes and no others. `main.tex` remains byte-identical, preserving the abstract, title, authors and inclusion structure.
- Introduction, Design, Discussion, Conclusion, Appendices B and C, figures, other table assets and bibliography remain unchanged. The full E1?E6 inventory and all original Appendix A tables remain inline.
- Displayed mathematics and the numerical main-table body are unchanged. Only a prose table note is corrected.
- Git reports no changes to any other tracked file, including research scripts and datasets. No research code, dataset, statistical result or figure was targeted for writing.
- All pre-existing archival optimization files and review reports are hash-identical to the start of this task.
- No simulations, estimators, research validations, commits, pushes or submissions were performed.

## Current Git status

No staged changes. Seven modified tracked LaTeX files; four untracked review entries including this report.

```text
 M journal_article/sections/02_framework.tex
 M journal_article/sections/04_results.tex
 M journal_article/sections/data_availability.tex
 M journal_article/supplementary/A_numerical_domain.tex
 M journal_article/supplementary/D_evidence_map.tex
 M journal_article/supplementary/D_implementation.tex
 M journal_article/tables/table_main_performance.tex
?? journal_validation/publication_review/LSSP_CANONICAL_CORRECTIONS_REPORT.md
?? journal_validation/publication_review/LSSP_CONTENT_AUDIT.md
?? journal_validation/publication_review/LSSP_OPTIMIZATION_REPORT.md
?? journal_validation/publication_review/lssp_optimization/
```
