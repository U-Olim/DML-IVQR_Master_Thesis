# Stage 2I ? Publication Revision Batch 3

**Date:** 10 November 2026 (Asia/Tashkent)
**Branch:** `journal-validation`
**Scope:** R1-007, R1-008, R1-009, R1-010, R1-011 and the requested introduction consistency correction.
**Baseline:** working tree at the start of this batch, including the prior Batch 2 follow-up. No commit or push.

## Implemented changes

Added a headed data-and-code availability statement before references; a claim-to-evidence map included in Appendix D and linked from Section 4; a candidate-evaluation sequence; an explicit distinction between optimization objectives and finite historical routine outputs; and the retained Gaussian mixed-density divergence argument. The introduction now distinguishes common observed data within a relevance setting from reused primitive draws across settings. No numerical result or research procedure was changed.

The title and author block are unchanged. The prior abstract qualification and Batch 2 report changes remain intact. No changes were made to the conclusion, design section, discussion, Appendices A?C, bibliography, research code, tables, figures or frozen evidence. The additions preserve direct-truth/grid distinctions, RMSE exceptions, confounding of implementation comparisons, nominal-cutoff limitations, non-finite density regularity and selected-panel numerical sensitivity.

## Git history and status

- Supplied HEAD: `15b8b4dc95e3658f3b858a6f792ea2983299aaa6`, subject `Stage 2`, dated 9 November 2026, with parent `2ceec58a`.
- Its file list includes the Round 1 audit, both BATCH1/BATCH2 reports and their manuscript changes. Thus Batches 1 and 2 are already combined in the supplied commit; they are not separate uncommitted changes against `2ceec58a` in this checkout. This session did not create that commit.
- At Batch 3 start, `journal_article/main.tex` and `journal_validation/publication_review/BATCH2_CHANGE_REPORT.md` were already modified by the prior follow-up. The former contains the Gaussian qualification in the abstract. Both pre-existing changes are preserved; the Batch 2 report is byte-identical to its Batch 3 baseline.
- Batch 3 modifies five existing LaTeX files and adds two LaTeX files plus this report. `main.tex` changes only by the availability input; results change only by an evidence-navigation sentence. The complete diff below is against the captured working-tree baseline, so it excludes prior Batch 2 work. A plain `git diff` against HEAD includes that earlier follow-up and omits untracked additions unless explicitly compared.
- The historical freeze identifier `ac9a9ccad027cde05488abb633e66cc02f87cc46` is recorded in `thesis_extension/reporting/EMPIRICAL_RESULTS_FREEZE.md`. `git cat-file -t` could not resolve it locally; the repository Git-commit API returned HTTP 404. It is not presented as a usable verified checkout. The checked accessible archive is `15b8b4dc?`.

## Public-access checks and limits

Read-only GitHub connector checks on 10 November 2026 returned `private=false`/`visibility=public` for [the repository API](https://api.github.com/repos/U-Olim/DML-IVQR_Master_Thesis), and resolved [commit 15b8b4dc](https://github.com/U-Olim/DML-IVQR_Master_Thesis/commit/15b8b4dc95e3658f3b858a6f792ea2983299aaa6). Contents API listings at that ref returned the six main files for each sample size, reporting CSVs, tracked Stage 1/2 grid summaries, package archives and full-table assets. The two principal Stage 2G report URLs also returned success. The corresponding [historical freeze commit API](https://api.github.com/repos/U-Olim/DML-IVQR_Master_Thesis/git/commits/ac9a9ccad027cde05488abb633e66cc02f87cc46) returned 404. These checks establish repository metadata/listing access through the connector; they do not establish byte-for-byte identity of every remote download, anonymous download testing, long-term preservation, package installation portability or historical random-number replay. No deposit, DOI or public release of local artifacts is inferred.

## Claim-to-evidence traceability table

All paths are repository-relative and were checked for local existence. Public listings were checked only as described above. Existing descriptive comparison counts are traced, not recomputed.

| Principal manuscript claim | Frozen inputs and fields / selection | Existing tables, figures or reports |
|---|---|---|
| Designed relevance ordering, Section 4.1 | `thesis_extension/calibration/instrument_strength_100rep/kappa_strength_summary.csv` | `journal_article/tables/table_strength_calibration.tex` |
| Point-error deterioration, sample-size comparisons and qualified 35/40 DML?Full RMSE ranking, Section 4.2 | `thesis_extension/final/output/n500/summary.csv`; `thesis_extension/final/output/n1000/summary.csv`; Bias/MAE/RMSE by n, tau, kappa, estimator; replication files `thesis_extension/final/output/n500/results.csv` and `thesis_extension/final/output/n1000/results.csv` | `journal_article/tables/table_main_performance.tex`; `journal_article/tables/generated/appendix_point_performance.tex`; `journal_article/figures/generated/rmse_n500.png`; `journal_article/figures/generated/rmse_n1000.png` |
| Direct-at-truth acceptance and strong-relevance undercoverage, Section 4.3 | Same two `summary.csv` files: historical Coverage/Size; same two `results.csv` files: W_true/covered/rejected_true | `journal_article/tables/generated/appendix_coverage.tex`; `journal_article/figures/generated/coverage_heatmap.pdf`; `thesis_extension/diagnostics/coverage_audit/COVERAGE_AUDIT_REPORT.md` |
| False-candidate rejection, including the existing 305/360 matched-cell comparison, Section 4.4 | `thesis_extension/final/output/n500/power_summary.csv`; `thesis_extension/final/output/n1000/power_summary.csv`; power by n, tau, kappa, estimator, Delta; replication records `thesis_extension/final/output/n500/power.csv` and `thesis_extension/final/output/n1000/power.csv` | `journal_article/tables/generated/appendix_power.tex`; `journal_article/figures/generated/power_median_combined.pdf` |
| Finite-grid informativeness and accepted-measure comparisons, Section 4.5 | Both main `summary.csv` files; `thesis_extension/reporting/output/table_cr_informativeness_full.csv`; saved profiles `thesis_extension/final/output/n500/profiles.csv` and `thesis_extension/final/output/n1000/profiles.csv` | `journal_article/tables/generated/appendix_cr_informativeness.tex`; `journal_article/figures/generated/accepted_measure_n500.png`; `journal_article/figures/generated/accepted_measure_n1000.png`; `journal_article/figures/generated/full_domain_acceptance_heatmap.pdf` |
| Abstract's 0.942 / 3.900 / 0.094 contrast | `thesis_extension/final/output/n1000/summary.csv`: Coverage and median_grid_accepted_set_measure; `thesis_extension/final/output/n1000/power_summary.csv`: power. Select n=1000, tau=.50, kappa=.10, estimator DML-IVQR-BC; Delta=.50 applies only to power. These are separate summaries. | Existing narrative in `journal_article/sections/04_results.tex`, paragraph beginning ?The DML sequence?; figures in the preceding three rows. No independent coverage validation is claimed. |
| Domain expansion and one Stage 1 candidate failure, Appendix A | `thesis_extension/diagnostics/grid_sensitivity/output/stage1/stage1_summary.csv`; `thesis_extension/diagnostics/grid_sensitivity/output/stage1/stage1_expansion_summary.csv`; `thesis_extension/diagnostics/grid_sensitivity/output/stage2/stage2_summary.csv`; `thesis_extension/diagnostics/grid_sensitivity/output/stage2/stage2_expansion_summary.csv`; `thesis_extension/reporting/output/table_grid_domain_diagnostic.csv` | `journal_article/tables/generated/appendix_grid_diagnostic.tex`; `journal_article/figures/grid_domain_expansion.png`; `thesis_extension/diagnostics/grid_sensitivity/GRID_RESULTS_PROVENANCE.md` |
| Selected-case numerical sensitivity, not a full-experiment error rate | `journal_validation/stage2g/full_path_validation/FULL_PATH_REPORT.md`; `journal_validation/stage2g/deterministic_implementation/DETERMINISTIC_IMPLEMENTATION_REPORT.md`; `journal_validation/stage2c/stability/STABILITY_REPORT.md` | `journal_validation/stage2g/deterministic_implementation/IMPLEMENTATION_CONTRACT_v1.md`; retained Batch 1 selected-panel disclosure in Appendix D |

The corresponding manuscript map is `journal_article/supplementary/D_evidence_map.tex`, included by Appendix D. Full-table assets named above already exist; they were neither regenerated nor all inserted into the article. Historical manifests retain former presentation paths and identify provenance rather than proving accessibility.

## Analytical and implementation sources

- Density argument: `journal_validation/stage2h/readiness/BOUNDED_DGP_DERIVATION.md`, Section 3 and ?What the transformation repairs in the original DGP.? Only its original-DGP argument is incorporated. Conditioning on X,Z fixes Q; conditional on u=q_tau,Q, T has mean mu_Q+rho*q_tau and variance 2.91-kappa^2. The retained inverse-Phi negative-tail comparison establishes the infinite mixed density. This is not density conditional on realized treatment and does not diagnose a cause of observed undercoverage.
- Historical evaluation order and literal rank/solve conventions: `thesis_extension/src/run_extension.R`, `thesis_extension/src/author_bc_dml_wrapper.R`, `thesis_extension/src/author_oracle_wrapper.R`; read only, not executed.
- Pinned instrument defaults and finite termination: inspected `hdm/R/rlasso.R` and `hdm/R/LassoShooting.fit.R` inside `thesis_extension/environment/package_archives_R343/hdm_0.2.0.tar.gz`, without extraction or execution. Outer numIter=15/tol=1e-5; inner maxIter=1000/optTol=1e-5/zeroThreshold=1e-6, with the actual while-counter and early-return qualifications stated. Outcome route and factor-1/2/intercept convention remain the retained quantreg 5.34 description.
- Last-used versus reported-next penalty and fixed-final-objective versus adaptive-trajectory scope: the existing Stage 2G implementation contract and report. Nothing substitutes their certified outputs for historical results.

## Unavailable or unverified reproduction artifacts

| Artifact / requirement | Status and consequence |
|---|---|
| Historical freeze checkout `ac9a9cca?` | Missing from local object store; remote API 404. Identifier retained as documentary provenance only. |
| Main-run worker stream assignments and per-candidate historical pivotal RNG states | Not supplied as an archived complete replay specification. Seed 675 alone cannot reconstruct exact penalty draws or prove worker-stream independence. Saved Stage 2G cases have narrower scope. |
| Main-run primitive sample files | The tracked final-output directories contain results/profiles/power/summaries/failure records, not a saved primitive/RNG replay archive. No exact sample-and-penalty replay is promised from those CSVs. |
| Large grid-diagnostic per-candidate files | Present locally but Git-ignored: `thesis_extension/diagnostics/grid_sensitivity/output/stage1/stage1_profiles.csv`, `thesis_extension/diagnostics/grid_sensitivity/output/stage1/stage1_range_metrics.csv`, `thesis_extension/diagnostics/grid_sensitivity/output/stage1/stage1_expansion_metrics.csv`, `thesis_extension/diagnostics/grid_sensitivity/output/stage2/stage2_tail_profiles.csv`, `thesis_extension/diagnostics/grid_sensitivity/output/stage2/combined_profiles_-5_7.csv`, `thesis_extension/diagnostics/grid_sensitivity/output/stage2/stage2_range_metrics.csv`, `thesis_extension/diagnostics/grid_sensitivity/output/stage2/stage2_expansion_metrics.csv`. Tracked summary counterparts exist. Ordinary clones omit these large files. |
| Saved grid primitives | `thesis_extension/diagnostics/grid_sensitivity/output/stage1/primitives/` is local/Git-ignored. Paths/hashes are documented in `thesis_extension/diagnostics/grid_sensitivity/GRID_RESULTS_MANIFEST.csv`; no verified external public deposit is established. |
| Stage 2H raw pilot outputs and seal | `journal_validation/stage2h/pilot/runs/` and `journal_validation/stage2h/pilot/SHA256_MANIFEST.json` are Git-ignored local artifacts. Tracked scripts/reports do not make them publicly available. |
| Historical runtime portability | Environment manifests, captured library and package archives are tracked; package-archive listing was checked remotely. No installation/rebuild, R executable distribution, operating-system compatibility or exact historical replay was tested. |
| Remote artifact byte identity and durable release | Metadata/listing checks only; no exhaustive remote hash/download comparison or new public deposit. Historical manifests were not re-certified. |
| Current PDF/source match | Unverified; no MiKTeX repair, compilation or PDF regeneration attempted. |
| Statistical inference validity and global set geometry | Remain unestablished; document edits supply neither an inference theorem nor numerical validation. |

No missing required evidence-map CSV/table/figure/report path was found locally. The missing checkout and excluded replay artifacts above are disclosed rather than assigned invented public locations.

## Claim strength and preservation

The evidence route is more operational and the existing density statement more explicit, but no new statistical finding or theorem is claimed. Public availability is now asserted only for the checked public repository/tracked archive; the unresolved freeze checkout and local-only files narrow the previous broad archive description. Exact historical replay is explicitly separated from deterministic inspection. Argmin notation no longer implies certified attainment by historical routine outputs. Common-sample wording is narrowed to within-setting comparisons. These changes do not attribute estimator differences to regularization, validate nominal chi-square inference, estimate a full-experiment numerical error frequency, change historical results, promise a calibration correction or assure journal acceptance.

## Verification performed

Document-only checks confirmed that referenced repository paths exist locally (internal hdm source-member paths were checked inside the pinned archive), new cross-references resolve, new labels are unique, and main.tex matches its pre-batch text except the new input. Tracked files outside authorized LaTeX/report scope are byte-identical to the captured baseline, including the prior Batch 2 report, all research code and result assets. Exact wording and diff below are generated from captured baseline/current source; no research scripts were invoked. Git whitespace checks were also run. No simulations, estimators, statistical tests, result regeneration, new numerical validation, dependency installation, MiKTeX repair or PDF build was performed. No commit or push.

## Exact original and revised wording

Line references below use the pre-Batch-3 baseline and revised source, respectively. Each changed span is recorded verbatim; an insertion has no original text. Unchanged context is retained in the complete Git diff that follows.

### `journal_article/main.tex`

R1-008: include the headed availability statement before references.

**Original lines:** insertion after line 26; **revised lines:** 27?27.

**Original text**

```latex
```

**Revised text**

```latex
\input{sections/data_availability}
```

### `journal_article/sections/01_introduction.tex`

Task 6 / R1-009: distinguish common samples within a setting, common primitives across settings and fresh algorithmic draws.

**Original lines:** 10?10; **revised lines:** 10?10.

**Original text**

```latex
The paper makes three empirical contributions. First, it specifies a controlled Monte Carlo relevance modification preserving the stated treatment/endogeneity distribution. Second, it compares preserved Oracle-GMM, Full-GMM and DML-IVQR implementations across relevance settings and quantiles on common observed samples. Third, it jointly evaluates point accuracy, direct-at-truth acceptance, false-candidate rejection and finite-grid informativeness. No new estimator or inference theorem is proposed.
```

**Revised text**

```latex
The paper makes three empirical contributions. First, it specifies a controlled Monte Carlo relevance modification preserving the stated treatment/endogeneity distribution. Second, it compares preserved Oracle-GMM, Full-GMM and DML-IVQR implementations across relevance settings and quantiles: estimators share the observed sample within each setting, while relevance settings reuse primitive draws but generally have different realized treatment and outcome values. This reuse does not make the DML pivotal penalty draws common across evaluations. Third, it jointly evaluates point accuracy, direct-at-truth acceptance, false-candidate rejection and finite-grid informativeness. No new estimator or inference theorem is proposed.
```

### `journal_article/sections/02_framework.tex`

R1-010: give the precise mixed-density identity and point to the retained derivation.

**Original lines:** 125?125; **revised lines:** 125?125.

**Original text**

```latex
This distinction is material for the present DGP. At truth, the outcome residual is $e_\tau=D(u-q_\tau)$, with $q_\tau=\Phi^{-1}(\tau)$ and $D=\Phi(T)$, $T=d^*(\kappa)$. Conditional on $u=q_\tau$, $X$, and observed $Z$, the variance of the normal index is $2.91-\kappa^2>1$ for every investigated setting. The density at zero contains a term proportional to $\operatorname E[1/\Phi(T)\mid u=q_\tau,X,Z]$, which is not finite. The experiment therefore does not establish the ideal density-weight regularity conditions or validate the associated asymptotic theory.
```

**Revised text**

```latex
This distinction is material for the present DGP. At truth, the outcome residual is $e_\tau=D(u-q_\tau)$, with $q_\tau=\Phi^{-1}(\tau)$ and $D=\Phi(T)$, $T=d^*(\kappa)$. Its density conditional on $(X,Z)$ mixes over treatment and equals $\phi(q_\tau)\operatorname E[1/\Phi(T)\mid u=q_\tau,X,Z]$. The conditional normal variance $2.91-\kappa^2>1$ makes this expectation infinite at every investigated setting. Appendix~\ref{app:density-divergence} gives the retained Gaussian conditioning and negative-tail argument; this is not the density conditional on realized treatment. The experiment therefore does not establish the ideal density-weight regularity conditions or validate the associated asymptotic theory.
```

### `journal_article/supplementary/D_implementation.tex`

R1-008/R1-009/R1-010/R1-011: distinguish provenance from accessible checkout, specify evaluation order and solver conventions, and reproduce the retained density argument.

**Original lines:** 6?6; **revised lines:** 6?6.

**Original text**

```latex
The computational archive is the project repository \url{https://github.com/U-Olim/DML-IVQR_Master_Thesis}. This reference identifies the archived workflow; it is not a claim of bit-for-bit regeneration from a seed on arbitrary systems. Preserved source is in \path{simulation/}, \path{Empirical_work/}, and \path{example/}; extension wrappers and configuration are in \path{thesis_extension/src/} and \path{thesis_extension/config/extension_config.R}. The empirical freeze identifies commit \texttt{ac9a9ccad027cde05488abb633e66cc02f87cc46} (2 September 2026).
```

**Revised text**

```latex
The computational archive is the project repository \url{https://github.com/U-Olim/DML-IVQR_Master_Thesis}. This reference identifies the archived workflow; it is not a claim of bit-for-bit regeneration from a seed on arbitrary systems. Preserved source is in \path{simulation/}, \path{Empirical_work/}, and \path{example/}; extension wrappers and configuration are in \path{thesis_extension/src/} and \path{thesis_extension/config/extension_config.R}. The empirical freeze records identifier \texttt{ac9a9ccad027cde05488abb633e66cc02f87cc46} (2 September 2026), whose checkout accessibility is unverified as explained in the data and code availability statement; the checked tracked archive is commit \texttt{15b8b4dc95e3658f3b858a6f792ea2983299aaa6}.
```

**Original lines:** insertion after line 13; **revised lines:** 14?27.

**Original text**

```latex
```

**Revised text**

```latex
\input{supplementary/D_evidence_map}

\subsection{Historical evaluation sequence}
\label{app:evaluation-sequence}
The operational source is \path{thesis_extension/src/run_extension.R}, with candidate routines in \path{thesis_extension/src/author_bc_dml_wrapper.R} and \path{thesis_extension/src/author_oracle_wrapper.R}. One replication proceeds as follows.
\begin{enumerate}
\item Generate one set of primitives; construct a sample at each relevance setting. Within that setting all three estimators share $(Y,D,X,Z)$. Reusing primitives across settings does not hold realized $(Y,D)$ fixed.
\item For each quantile and estimator, profile the ordered 41-point primary grid. At each DML candidate $a$, call \texttt{lambda\_BC\_author} afresh (1000 artificial uniform columns), then fit \texttt{quantreg::rq(y-a*D\string~X, method="lasso")} with the resulting penalty and an intercept. Refit nuisances at each candidate; there is no post-Lasso refit. Oracle and Full instead call unpenalized \texttt{quantreg::rq} with their designated controls.
\item Form candidate outcome residuals and the proxy \texttt{dnorm(e, mean(e), var(e))}. For each DML instrument, call \texttt{hdm::rlasso(..., post=FALSE)} on square-root-proxy-transformed instruments and controls with an ordinary unpenalized intercept. Subtract the returned intercept and original-control slopes from the original instrument. Oracle and Full use the direct matrix residualization described below.
\item Apply the literal computed-residual rule $r_i=\mathbf1\{\widehat e_i\leq0\}$, with no residual tolerance. Set $s_i=\tau-r_i$, $g=\sum_i\widehat\Psi_i s_i$ and $S=\sum_i\widehat\Psi_i\widehat\Psi_i' s_i^2$. The statistic is $g'S^{-1}g$, equivalent to the normalized definition in Section~\ref{sec:framework}. Use direct \texttt{solve} and the retained nominal chi-square cutoff; singular or non-finite evaluations are failures, not acceptances.
\item Retain the first grid minimum for the point estimate and the stored grid decisions for informativeness summaries. After profiling, separately evaluate the true effect and six specified false candidates. DML again invokes its candidate routine, with fresh pivotal draws, in a separate five-worker evaluation. Direct-at-truth acceptance and false-candidate rejection therefore do not reuse stored grid statistics, even when candidates coincide. Failed profiles receive no point estimate; the documented failure conventions remain in force.
\end{enumerate}
The archived estimator includes both sample randomness and algorithmic penalty randomness. Common observed data do not imply common pivotal draws across estimators, candidates, or repeated calls. Worker-specific RNG stream assignments and the full main-run candidate penalty states were not archived as a replay specification; seed 675 alone neither reproduces every historical penalty nor establishes independence of worker streams. Saved Stage 2G cases with exported states have a narrower replay scope. The conventional Monte Carlo standard-error summaries do not verify historical stream independence. Frozen CSV inspection and selection of existing table/figure assets require no stochastic rerun; they do not recover missing RNG states.

```

**Original lines:** insertion after line 14; **revised lines:** 29?29.

**Original text**

```latex
```

**Revised text**

```latex
\label{app:penalty-implementation}
```

**Original lines:** insertion after line 155; **revised lines:** 171?199.

**Original text**

```latex
```

**Revised text**

```latex
\subsection{Objectives and finite historical solver outputs}
\label{app:finite-solvers}
The argmin displays above specify optimization objectives; the archived coefficients are finite routine outputs, not certified exact minimizers. The DML outcome route is \texttt{quantreg::rq(..., method="lasso")} / \texttt{rq.fit.lasso} in \texttt{quantreg}~5.34. It uses augmented observations and the penalized intercept described above. Oracle and Full use the package's default unpenalized \texttt{rq} route. Computed residual signs, including exact floating-point zeros, feed the literal $\leq0$ rule; small objective errors alone do not establish rank or decision invariance.

Instrument fitting uses \texttt{hdm}~0.2.0 \texttt{rlasso} with \texttt{post=FALSE}, the default heteroskedastic, X-independent loading calculation and an ordinary unpenalized intercept. In the retained source, outer calibration has \texttt{numIter=15} and \texttt{tol=1e-5}; it stops when the absolute change in the estimated residual standard deviation is below the tolerance or the iteration budget is exhausted. A zero-selected-coefficient branch can return early. Inner \texttt{LassoShooting.fit} uses \texttt{maxIter=1000}, \texttt{optTol=1e-5} and \texttt{zeroThreshold=1e-6}; its loop starts at one and runs while the counter is below the maximum, stopping early when the sum of absolute coefficient changes falls below \texttt{optTol}. The returned small coefficients are thresholded. These are finite algorithmic conventions, not accuracy certificates. The pinned source is in \path{thesis_extension/environment/package_archives_R343/hdm_0.2.0.tar.gz} (\path{hdm/R/rlasso.R} and \path{hdm/R/LassoShooting.fit.R} inside that archive).

The outer routine updates loadings after a finite shooting fit. Its reported next penalty need not be the last penalty actually used to produce those coefficients. The later contract \path{journal_validation/stage2g/deterministic_implementation/IMPLEMENTATION_CONTRACT_v1.md} distinguishes preservation of the adaptive trajectory from refinement of the final centered objective at the last-used penalty. Refined final coefficients are not fed back into that trajectory under its Policy B contract; recalibration is a different pathway. Those selected-case numerical investigations do not establish exact attainment by historical fits. No certified solution, altered residual threshold or revised penalty path replaces any archived estimator result here. The selected-panel decision-sensitivity disclosure above remains applicable.

\subsection{Retained density-divergence argument for the original DGP}
\label{app:density-divergence}
This argument is reproduced from Section 3 of \path{journal_validation/stage2h/readiness/BOUNDED_DGP_DERIVATION.md}, specifically its analysis of the original $D=\Phi(T)$ construction; no bounded-treatment results are substituted. Put $\rho=0.3$, $q_\tau=\Phi^{-1}(\tau)$, $Q_j=Z_j-h_j(X)=z_j+v_j$, and $\mu_Q=\kappa(Q_1+Q_2)/2$. The observed instrument shifts $h_j(X)$ are given in the DGP. Since $Q\sim\mathcal N(0,2I_2)$, Gaussian conditioning in the retained derivation gives
\[
 T\mid Q\sim\mathcal N(\mu_Q,v_\kappa),\qquad v_\kappa=3-\kappa^2,
 \qquad
 T\mid u=q_\tau,Q\sim\mathcal N(\mu_Q+\rho q_\tau,s_\kappa^2),\quad
 s_\kappa^2=v_\kappa-\rho^2=2.91-\kappa^2.
\]
Controls are independent of $(T,u,Q)$, and conditioning on $(X,Z)$ identifies $Q$. For the structural residual $e_\tau=\Phi(T)(u-q_\tau)$, Bayes' formula and $u\perp(X,Z)$ yield the mixed-density identity
\begin{equation}
 f_{e_\tau\mid X,Z}(0)
 =\phi(q_\tau)\operatorname E\!\left[\frac{1}{\Phi(T)}\,\middle|\,u=q_\tau,Q\right].
 \label{eq:mixed-density-divergence}
\end{equation}
Here $s_\kappa^2>1$ at every investigated relevance setting (1.91 at $\kappa=1$ and 2.90 at $\kappa=0.10$). As $t\to-\infty$, $1/\Phi(t)\sim |t|/\phi(t)$. Against the conditional normal density, the integrand is proportional in its tail to
\[
 |t|\exp\!\left\{\frac{1-1/s_\kappa^2}{2}t^2+O(t)\right\},
\]
whose negative-tail integral diverges. Thus the original $f_{e_\tau\mid X,Z}(0)$ is infinite. Mixing conditional only on $X$ instead gives Gaussian variance $3-\rho^2=2.91>1$ and the same divergence. These are densities that integrate over treatment, not $f_{e_\tau\mid D,X,Z}(0)$ at a realized positive treatment value. Nor are they the historical fitted-normal proxy. This retained regularity limitation does not establish which feature causes any particular Monte Carlo rejection pattern and does not validate or repair nominal inference.

```

### `journal_article/sections/04_results.tex`

R1-007: provide a direct reader-facing route from full-result claims to the evidence map.

**Original lines:** insertion after line 2; **revised lines:** 3?3.

**Original text**

```latex
```

**Revised text**

```latex
Appendix~\ref{app:evidence-map} maps the principal numerical findings, including comparisons using all design cells, to the exact frozen CSVs and existing full-table and figure assets. These sources permit inspection without re-estimation.
```

### `journal_article/sections/data_availability.tex`

R1-008: operational public/tracked/local-only/dependency statement, with checked and unresolved commit identifiers.

**Original lines:** insertion after line 0; **revised lines:** 1?4.

**Original text**

```latex
```

**Revised text**

```latex
\section*{Data and code availability}
The public repository is \url{https://github.com/U-Olim/DML-IVQR_Master_Thesis}. Repository visibility, commit \texttt{15b8b4dc95e3658f3b858a6f792ea2983299aaa6}, and directory listings for the main frozen CSVs, reporting summaries and package archives were checked through the GitHub API on 10 November 2026. Readers can select that commit and follow the exact paths in Appendix~\ref{app:evidence-map} to inspect both sample sizes, all quantiles and relevance settings without running an estimator. These are simulated data and archived computational outputs, not an external observational dataset. The freeze record names \texttt{ac9a9ccad027cde05488abb633e66cc02f87cc46}; that identifier was not resolvable in the present local object store and returned HTTP 404 from the repository API. It is retained as recorded provenance, not offered as a verified release checkout.

Historical rerunning is a different task. Source and configuration are under \path{thesis_extension/src/} and \path{thesis_extension/config/}; environment records, package archives and the captured Windows library are under \path{thesis_extension/environment/}. The recorded environment uses R~3.4.3 and pinned historical packages (Appendix~\ref{app:reproducibility}); their presence does not establish installation portability or exact random-number replay. Main-run worker-specific penalty states are not recoverable from the parent seed alone. Large grid-diagnostic profiles and saved primitives are local, Git-ignored artifacts identified in \path{thesis_extension/diagnostics/grid_sensitivity/GRID_RESULTS_MANIFEST.csv}; tracked diagnostic summaries remain available. Stage 2H pilot outputs under \path{journal_validation/stage2h/pilot/runs/} and its \path{journal_validation/stage2h/pilot/SHA256_MANIFEST.json} are also Git-ignored and are not part of the public tracked archive. No public deposit of these local artifacts or portable historical runtime is established here. This revision does not publish new results or replace historical fits with later certified numerical solutions.
```

### `journal_article/supplementary/D_evidence_map.tex`

R1-007: map claims to exact frozen inputs, existing presentation assets and selected numerical reports.

**Original lines:** insertion after line 0; **revised lines:** 1?31.

**Original text**

```latex
```

**Revised text**

```latex
\subsection{Frozen-evidence map}
\label{app:evidence-map}
All paths below are repository-relative. Select commit \texttt{15b8b4dc95e3658f3b858a6f792ea2983299aaa6} for the tracked archive. The keys connect the principal findings to complete saved evidence, including cells omitted from compact main-text displays. This map identifies sources; it does not recompute descriptive comparison counts or rerun historical checks.

\begin{center}
\small
\begin{tblr}{colspec={X[3,l] X[2,l] X[1,l]},row{1}={font=\bfseries},hline{1,2,Z}={0.4pt}}
Finding & Manuscript location & Evidence key \\
Designed relevance ordering & Section~\ref{sec:results-relevance-calibration} & E1 \\
Point-error deterioration and qualified estimator rankings & Section~\ref{sec:results-point-accuracy} & E2 \\
Truth acceptance and false-candidate rejection & Sections~\ref{sec:results-coverage}--\ref{sec:results-power} & E3 \\
Nominal-looking acceptance with little grid exclusion & Abstract; Section~\ref{chap:results} & E2--E4 \\
Domain sensitivity and finite numerical scope & Appendix~\ref{app:numerical-domain-diagnostics} & E5 \\
Selected-case rank and decision sensitivity & Appendix~\ref{app:reproducibility} & E6 \\
\end{tblr}
\end{center}

\begin{description}
\item[E1: Relevance.] \path{thesis_extension/calibration/instrument_strength_100rep/kappa_strength_summary.csv}; presentation: \path{journal_article/tables/table_strength_calibration.tex}.

\item[E2: Full performance, both sample sizes.] \path{thesis_extension/final/output/n500/summary.csv} and \path{thesis_extension/final/output/n1000/summary.csv} contain Bias, MAE, RMSE, historical \texttt{Coverage}/\texttt{Size}, accepted-measure and boundary/full-grid summaries. Replication-level sources are \path{thesis_extension/final/output/n500/results.csv} and \path{thesis_extension/final/output/n1000/results.csv}; stored candidate statistics are \path{thesis_extension/final/output/n500/profiles.csv} and \path{thesis_extension/final/output/n1000/profiles.csv}. Full presentation assets: \path{journal_article/tables/generated/appendix_point_performance.tex}, \path{journal_article/tables/generated/appendix_coverage.tex}, and \path{journal_article/tables/generated/appendix_cr_informativeness.tex}; compact table: \path{journal_article/tables/table_main_performance.tex}. Existing RMSE images are \path{journal_article/figures/generated/rmse_n500.png} and \path{journal_article/figures/generated/rmse_n1000.png}.

\item[E3: Truth testing and power.] Use E2's \texttt{Coverage}, \texttt{Size} and replication \texttt{W\_true} fields for direct-at-truth evaluations. False-candidate summaries are \path{thesis_extension/final/output/n500/power_summary.csv} and \path{thesis_extension/final/output/n1000/power_summary.csv}; replication records are \path{thesis_extension/final/output/n500/power.csv} and \path{thesis_extension/final/output/n1000/power.csv}. Full presentation: \path{journal_article/tables/generated/appendix_power.tex}; figures: \path{journal_article/figures/generated/coverage_heatmap.pdf} and \path{journal_article/figures/generated/power_median_combined.pdf}. The abstract's $0.942/3.900/0.094$ contrast selects E2's \texttt{Coverage}/\texttt{median\_grid\_accepted\_set\_measure} and this power summary's \texttt{power}, respectively, at $n=1000$, $\tau=0.50$, $\kappa=0.10$, estimator \texttt{DML-IVQR-BC}, with $\Delta=0.50$ for power only. These are different summaries, not a joint event or validated grid-set coverage.

\item[E4: Grid informativeness.] In addition to E2's summaries/profiles, \path{thesis_extension/reporting/output/table_cr_informativeness_full.csv} contains all design cells. Existing images are \path{journal_article/figures/generated/accepted_measure_n500.png}, \path{journal_article/figures/generated/accepted_measure_n1000.png}, and \path{journal_article/figures/generated/full_domain_acceptance_heatmap.pdf}. Grid quadrature and all-grid acceptance are distinct diagnostics on the maintained domain.

\item[E5: Domain expansion.] Tracked sources: \path{thesis_extension/diagnostics/grid_sensitivity/output/stage1/stage1_summary.csv}, \path{thesis_extension/diagnostics/grid_sensitivity/output/stage1/stage1_expansion_summary.csv}, \path{thesis_extension/diagnostics/grid_sensitivity/output/stage2/stage2_summary.csv}, and \path{thesis_extension/diagnostics/grid_sensitivity/output/stage2/stage2_expansion_summary.csv}. Combined reporting view: \path{thesis_extension/reporting/output/table_grid_domain_diagnostic.csv}; table and figure: \path{journal_article/tables/generated/appendix_grid_diagnostic.tex} and \path{journal_article/figures/grid_domain_expansion.png}. Design, failure and local-only artifact scope are in \path{thesis_extension/diagnostics/grid_sensitivity/GRID_RESULTS_PROVENANCE.md} and \path{thesis_extension/diagnostics/grid_sensitivity/GRID_RESULTS_MANIFEST.csv}. This separate diagnostic uses 100 intended replications; the recorded Stage 1 failure remains excluded from complete-profile summaries, not counted as acceptance. Large profiles and saved primitives are Git-ignored; tracked summaries do not supply full stochastic replay.

\item[E6: Numerical sensitivity.] \path{journal_validation/stage2g/full_path_validation/FULL_PATH_REPORT.md} records the selected 24-problem comparison and five Policy A/C decision differences. \path{journal_validation/stage2g/deterministic_implementation/DETERMINISTIC_IMPLEMENTATION_REPORT.md} and \path{journal_validation/stage2g/deterministic_implementation/IMPLEMENTATION_CONTRACT_v1.md} specify the fixed-objective and input scope of later certificates. Earlier rank-stability evidence is in \path{journal_validation/stage2c/stability/STABILITY_REPORT.md}. These reports are not population error rates or replacements for E2--E5.
\end{description}
The inventories \path{thesis_extension/reporting/EMPIRICAL_RESULTS_MANIFEST.csv} and \path{thesis_extension/reporting/REPORTING_OUTPUT_MANIFEST.csv} retain historical input/output hashes and provenance. An entry in a manifest alone does not establish public availability: local-only exclusions are stated in the data and code availability statement.
```

## Complete Batch 3 manuscript Git diff

Actual `git diff --no-index` output comparing captured baseline/current source copies; temporary prefixes are normalized to repository-relative paths. New files are compared against `/dev/null`. This report is the documentation artifact and is not recursively embedded in its own diff. Prior Batch 2 follow-up changes are excluded.

```diff
diff --git a/journal_article/main.tex b/journal_article/main.tex
index e3e7a1b0..8fdde7ba 100644
--- a/journal_article/main.tex
+++ b/journal_article/main.tex
@@ -24,6 +24,7 @@ We study how weakening instrument relevance changes point accuracy, test calibra
 \input{sections/04_results}
 \input{sections/05_discussion}
 \input{sections/06_conclusion}
+\input{sections/data_availability}
 \FloatBarrier
 \printbibliography[title={References}]
 \clearpage
diff --git a/journal_article/sections/01_introduction.tex b/journal_article/sections/01_introduction.tex
index 5a6860b4..5d82637e 100644
--- a/journal_article/sections/01_introduction.tex
+++ b/journal_article/sections/01_introduction.tex
@@ -7,7 +7,7 @@ The high-dimensional simulation of \textcite{chen_huang_tien_2021} holds instrum
 
 The scientific question extends beyond point accuracy. Direct-at-truth acceptance can approach the nominal confidence level while most of the grid is retained and few false candidates are rejected; a more accurate point estimate also need not imply better calibration. Reported coverage is a direct-test acceptance diagnostic, not literal membership coverage of stored grid sets. Fresh pivotal draws can distinguish separate DML evaluations even at the same candidate; unrestricted inversion remains conceptual.
 
-The paper makes three empirical contributions. First, it specifies a controlled Monte Carlo relevance modification preserving the stated treatment/endogeneity distribution. Second, it compares preserved Oracle-GMM, Full-GMM and DML-IVQR implementations across relevance settings and quantiles on common observed samples. Third, it jointly evaluates point accuracy, direct-at-truth acceptance, false-candidate rejection and finite-grid informativeness. No new estimator or inference theorem is proposed.
+The paper makes three empirical contributions. First, it specifies a controlled Monte Carlo relevance modification preserving the stated treatment/endogeneity distribution. Second, it compares preserved Oracle-GMM, Full-GMM and DML-IVQR implementations across relevance settings and quantiles: estimators share the observed sample within each setting, while relevance settings reuse primitive draws but generally have different realized treatment and outcome values. This reuse does not make the DML pivotal penalty draws common across evaluations. Third, it jointly evaluates point accuracy, direct-at-truth acceptance, false-candidate rejection and finite-grid informativeness. No new estimator or inference theorem is proposed.
 
 The preserved DML-IVQR implementation has lower RMSE than the preserved Full-GMM implementation in 35 of the 40 matched designs, with documented exceptions. Differences in nuisance dimension, residualization and computational details prevent attributing this comparison to regularization alone. Oracle-GMM also deteriorates under weaker relevance, so high-dimensional nuisance estimation is not the sole explanation. Strong-relevance undercoverage limits any reading of nominal-looking acceptance as validated inference.
 
diff --git a/journal_article/sections/02_framework.tex b/journal_article/sections/02_framework.tex
index ee765f2d..efe704fa 100644
--- a/journal_article/sections/02_framework.tex
+++ b/journal_article/sections/02_framework.tex
@@ -122,7 +122,7 @@ Here $f_{\epsilon(a)}(0\mid X_i,Z_i)$ is the conditional residual density at zer
 \end{equation}
 Under finite density-weighted moments, a nonsingular $J$, and the requisite differentiation conditions, the derivative in the intercept and slopes is $-[M_0-\delta_0J_0]=0$. The residualization derivative vanishes by the quantile moment. Appendix~\ref{app:score-algebra} gives the algebra. These are properties of the ideal construction under its conditions, rather than guarantees for every executable implementation.
 
-This distinction is material for the present DGP. At truth, the outcome residual is $e_\tau=D(u-q_\tau)$, with $q_\tau=\Phi^{-1}(\tau)$ and $D=\Phi(T)$, $T=d^*(\kappa)$. Conditional on $u=q_\tau$, $X$, and observed $Z$, the variance of the normal index is $2.91-\kappa^2>1$ for every investigated setting. The density at zero contains a term proportional to $\operatorname E[1/\Phi(T)\mid u=q_\tau,X,Z]$, which is not finite. The experiment therefore does not establish the ideal density-weight regularity conditions or validate the associated asymptotic theory.
+This distinction is material for the present DGP. At truth, the outcome residual is $e_\tau=D(u-q_\tau)$, with $q_\tau=\Phi^{-1}(\tau)$ and $D=\Phi(T)$, $T=d^*(\kappa)$. Its density conditional on $(X,Z)$ mixes over treatment and equals $\phi(q_\tau)\operatorname E[1/\Phi(T)\mid u=q_\tau,X,Z]$. The conditional normal variance $2.91-\kappa^2>1$ makes this expectation infinite at every investigated setting. Appendix~\ref{app:density-divergence} gives the retained Gaussian conditioning and negative-tail argument; this is not the density conditional on realized treatment. The experiment therefore does not establish the ideal density-weight regularity conditions or validate the associated asymptotic theory.
 
 \subsection{Preserved estimators and inference}
 \label{sec:implementation}
diff --git a/journal_article/supplementary/D_implementation.tex b/journal_article/supplementary/D_implementation.tex
index fc834ff6..499a1aba 100644
--- a/journal_article/supplementary/D_implementation.tex
+++ b/journal_article/supplementary/D_implementation.tex
@@ -3,7 +3,7 @@
 \label{app:reproducibility}
 \setcounter{equation}{0}\setcounter{table}{0}\setcounter{figure}{0}
 \subsection{Environment, records, and reproducibility limits}
-The computational archive is the project repository \url{https://github.com/U-Olim/DML-IVQR_Master_Thesis}. This reference identifies the archived workflow; it is not a claim of bit-for-bit regeneration from a seed on arbitrary systems. Preserved source is in \path{simulation/}, \path{Empirical_work/}, and \path{example/}; extension wrappers and configuration are in \path{thesis_extension/src/} and \path{thesis_extension/config/extension_config.R}. The empirical freeze identifies commit \texttt{ac9a9ccad027cde05488abb633e66cc02f87cc46} (2 September 2026).
+The computational archive is the project repository \url{https://github.com/U-Olim/DML-IVQR_Master_Thesis}. This reference identifies the archived workflow; it is not a claim of bit-for-bit regeneration from a seed on arbitrary systems. Preserved source is in \path{simulation/}, \path{Empirical_work/}, and \path{example/}; extension wrappers and configuration are in \path{thesis_extension/src/} and \path{thesis_extension/config/extension_config.R}. The empirical freeze records identifier \texttt{ac9a9ccad027cde05488abb633e66cc02f87cc46} (2 September 2026), whose checkout accessibility is unverified as explained in the data and code availability statement; the checked tracked archive is commit \texttt{15b8b4dc95e3658f3b858a6f792ea2983299aaa6}.
 
 The canonical environment is R~3.4.3 (30 November 2017) on 64-bit Windows, using five workers. The captured attached packages are \texttt{doSNOW} 1.0.16, \texttt{snow} 0.4-2, \texttt{iterators} 1.0.8, \texttt{foreach} 1.4.3, \texttt{mvtnorm} 1.0-6, \texttt{hqreg} 1.4, \texttt{hdm} 0.2.0, \texttt{quantreg} 5.34, and \texttt{SparseM} 1.77. Environment session and library manifests are under \path{thesis_extension/environment/}. The main simulation uses seed 675; the grid diagnostic also uses seed 675, with saved primitives reloaded in Stage 2; calibration uses seed 20260813. Worker-specific RNG streams are not explicitly initialized in the preserved parallel DML procedure, so the parent seed alone does not establish exact regeneration of every penalty draw.
 
@@ -11,7 +11,22 @@ Frozen CSVs permit deterministic reporting without re-estimation. Input/output m
 
 The original Monte Carlo results remain outputs of the preserved historical executable implementation. Later selected-case Stage 2G audits identified sensitivity of residual ranks and test decisions to computational details: historical Policy A and the certified-outcome Policy C path differed in 5 of the 24 saved candidate problems examined. Policy C uses exact outcome residual ranks with the retained density/projection pathway; these panel results do not replace the historical Monte Carlo results. Numerical certificates establish properties of specified fixed objectives and input values, with decision bounds conditional on the stated exported quantities; they do not establish invariance of every historical Monte Carlo decision or certify all adaptive calibration trajectories. The selected panels do not establish an error frequency for the full Monte Carlo experiment.\footnote{See \path{journal_validation/stage2g/full_path_validation/FULL_PATH_REPORT.md}, ``Complete 24-problem decision comparison'' and ``Required conclusions''; and \path{journal_validation/stage2g/deterministic_implementation/DETERMINISTIC_IMPLEMENTATION_REPORT.md}, ``Mathematical equivalence: established scope''.}
 
+\input{supplementary/D_evidence_map}
+
+\subsection{Historical evaluation sequence}
+\label{app:evaluation-sequence}
+The operational source is \path{thesis_extension/src/run_extension.R}, with candidate routines in \path{thesis_extension/src/author_bc_dml_wrapper.R} and \path{thesis_extension/src/author_oracle_wrapper.R}. One replication proceeds as follows.
+\begin{enumerate}
+\item Generate one set of primitives; construct a sample at each relevance setting. Within that setting all three estimators share $(Y,D,X,Z)$. Reusing primitives across settings does not hold realized $(Y,D)$ fixed.
+\item For each quantile and estimator, profile the ordered 41-point primary grid. At each DML candidate $a$, call \texttt{lambda\_BC\_author} afresh (1000 artificial uniform columns), then fit \texttt{quantreg::rq(y-a*D\string~X, method="lasso")} with the resulting penalty and an intercept. Refit nuisances at each candidate; there is no post-Lasso refit. Oracle and Full instead call unpenalized \texttt{quantreg::rq} with their designated controls.
+\item Form candidate outcome residuals and the proxy \texttt{dnorm(e, mean(e), var(e))}. For each DML instrument, call \texttt{hdm::rlasso(..., post=FALSE)} on square-root-proxy-transformed instruments and controls with an ordinary unpenalized intercept. Subtract the returned intercept and original-control slopes from the original instrument. Oracle and Full use the direct matrix residualization described below.
+\item Apply the literal computed-residual rule $r_i=\mathbf1\{\widehat e_i\leq0\}$, with no residual tolerance. Set $s_i=\tau-r_i$, $g=\sum_i\widehat\Psi_i s_i$ and $S=\sum_i\widehat\Psi_i\widehat\Psi_i' s_i^2$. The statistic is $g'S^{-1}g$, equivalent to the normalized definition in Section~\ref{sec:framework}. Use direct \texttt{solve} and the retained nominal chi-square cutoff; singular or non-finite evaluations are failures, not acceptances.
+\item Retain the first grid minimum for the point estimate and the stored grid decisions for informativeness summaries. After profiling, separately evaluate the true effect and six specified false candidates. DML again invokes its candidate routine, with fresh pivotal draws, in a separate five-worker evaluation. Direct-at-truth acceptance and false-candidate rejection therefore do not reuse stored grid statistics, even when candidates coincide. Failed profiles receive no point estimate; the documented failure conventions remain in force.
+\end{enumerate}
+The archived estimator includes both sample randomness and algorithmic penalty randomness. Common observed data do not imply common pivotal draws across estimators, candidates, or repeated calls. Worker-specific RNG stream assignments and the full main-run candidate penalty states were not archived as a replay specification; seed 675 alone neither reproduces every historical penalty nor establishes independence of worker streams. Saved Stage 2G cases with exported states have a narrower replay scope. The conventional Monte Carlo standard-error summaries do not verify historical stream independence. Frozen CSV inspection and selection of existing table/figure assets require no stochastic rerun; they do not recover missing RNG states.
+
 \subsection{Penalty, density proxy, and residualization}
+\label{app:penalty-implementation}
 For each candidate, $b_0$ is the fitted outcome intercept and $b$ the slopes. In the preserved \texttt{rq.fit.lasso} augmented-observation implementation, the unscaled check-loss sum receives a penalty with factor $1/2$. The vector $\lambda^{rq}(a)$ is the supplied routine argument, including an intercept penalty. There is no post-Lasso refit. Let $s_k=(n^{-1}\sum_iX_{ik}^2)^{1/2}$; $U_{ir}$ are independent artificial Uniform$(0,1)$ draws, with $r=1,\ldots,1000$, and $\widehat Q_{0.9}$ is their empirical pivotal-statistic 90th percentile. Fresh draws are made on every penalty call. This is algorithmic randomness, not sample splitting.
 
 In the following formulas, $\phi(e;\mu,\sigma)$ denotes a normal density parameterized by standard deviation. The proxy supplies $\widehat\sigma_\epsilon^2$ in that argument: the preserved R call is \texttt{dnorm(e, mean(e), var(e))}. It evaluates a fitted-normal density at residuals rather than estimating the theoretical conditional density at zero. The instrument penalty is $\mathcal P_{j,a}(\gamma_j)=\sum_k\lambda^\Gamma_{jk}(a)|\gamma_{jk}|$, using default iterative heteroskedastic loadings. Its ordinary intercept is unpenalized; no post-Lasso refit is performed.
@@ -153,6 +168,35 @@ In the following formulas, $\phi(e;\mu,\sigma)$ denotes a normal density paramet
 \end{equation}
 The first five equations describe DML-IVQR. The last three describe Oracle-GMM and Full-GMM, with $S_0=\{1,\ldots,10\}$, $X_{\mathrm{orc},i}=X_{S_0,i}$, and $X_{\mathrm{full},i}=X_i$. Their quantile regressions include an intercept, but their matrix residualization includes no constant regressor. DML retains the ordinary intercept of a transformed regression and subtracts it from the original instrument without dividing by $\sqrt{\widehat f_i(a)}$. It is therefore not the exact sample counterpart of the ideal density-weighted intercept. All procedures use same-sample nuisance fits and scores; cross-fitting is absent. The comparison does not isolate regularization from these residualization differences.
 
+\subsection{Objectives and finite historical solver outputs}
+\label{app:finite-solvers}
+The argmin displays above specify optimization objectives; the archived coefficients are finite routine outputs, not certified exact minimizers. The DML outcome route is \texttt{quantreg::rq(..., method="lasso")} / \texttt{rq.fit.lasso} in \texttt{quantreg}~5.34. It uses augmented observations and the penalized intercept described above. Oracle and Full use the package's default unpenalized \texttt{rq} route. Computed residual signs, including exact floating-point zeros, feed the literal $\leq0$ rule; small objective errors alone do not establish rank or decision invariance.
+
+Instrument fitting uses \texttt{hdm}~0.2.0 \texttt{rlasso} with \texttt{post=FALSE}, the default heteroskedastic, X-independent loading calculation and an ordinary unpenalized intercept. In the retained source, outer calibration has \texttt{numIter=15} and \texttt{tol=1e-5}; it stops when the absolute change in the estimated residual standard deviation is below the tolerance or the iteration budget is exhausted. A zero-selected-coefficient branch can return early. Inner \texttt{LassoShooting.fit} uses \texttt{maxIter=1000}, \texttt{optTol=1e-5} and \texttt{zeroThreshold=1e-6}; its loop starts at one and runs while the counter is below the maximum, stopping early when the sum of absolute coefficient changes falls below \texttt{optTol}. The returned small coefficients are thresholded. These are finite algorithmic conventions, not accuracy certificates. The pinned source is in \path{thesis_extension/environment/package_archives_R343/hdm_0.2.0.tar.gz} (\path{hdm/R/rlasso.R} and \path{hdm/R/LassoShooting.fit.R} inside that archive).
+
+The outer routine updates loadings after a finite shooting fit. Its reported next penalty need not be the last penalty actually used to produce those coefficients. The later contract \path{journal_validation/stage2g/deterministic_implementation/IMPLEMENTATION_CONTRACT_v1.md} distinguishes preservation of the adaptive trajectory from refinement of the final centered objective at the last-used penalty. Refined final coefficients are not fed back into that trajectory under its Policy B contract; recalibration is a different pathway. Those selected-case numerical investigations do not establish exact attainment by historical fits. No certified solution, altered residual threshold or revised penalty path replaces any archived estimator result here. The selected-panel decision-sensitivity disclosure above remains applicable.
+
+\subsection{Retained density-divergence argument for the original DGP}
+\label{app:density-divergence}
+This argument is reproduced from Section 3 of \path{journal_validation/stage2h/readiness/BOUNDED_DGP_DERIVATION.md}, specifically its analysis of the original $D=\Phi(T)$ construction; no bounded-treatment results are substituted. Put $\rho=0.3$, $q_\tau=\Phi^{-1}(\tau)$, $Q_j=Z_j-h_j(X)=z_j+v_j$, and $\mu_Q=\kappa(Q_1+Q_2)/2$. The observed instrument shifts $h_j(X)$ are given in the DGP. Since $Q\sim\mathcal N(0,2I_2)$, Gaussian conditioning in the retained derivation gives
+\[
+ T\mid Q\sim\mathcal N(\mu_Q,v_\kappa),\qquad v_\kappa=3-\kappa^2,
+ \qquad
+ T\mid u=q_\tau,Q\sim\mathcal N(\mu_Q+\rho q_\tau,s_\kappa^2),\quad
+ s_\kappa^2=v_\kappa-\rho^2=2.91-\kappa^2.
+\]
+Controls are independent of $(T,u,Q)$, and conditioning on $(X,Z)$ identifies $Q$. For the structural residual $e_\tau=\Phi(T)(u-q_\tau)$, Bayes' formula and $u\perp(X,Z)$ yield the mixed-density identity
+\begin{equation}
+ f_{e_\tau\mid X,Z}(0)
+ =\phi(q_\tau)\operatorname E\!\left[\frac{1}{\Phi(T)}\,\middle|\,u=q_\tau,Q\right].
+ \label{eq:mixed-density-divergence}
+\end{equation}
+Here $s_\kappa^2>1$ at every investigated relevance setting (1.91 at $\kappa=1$ and 2.90 at $\kappa=0.10$). As $t\to-\infty$, $1/\Phi(t)\sim |t|/\phi(t)$. Against the conditional normal density, the integrand is proportional in its tail to
+\[
+ |t|\exp\!\left\{\frac{1-1/s_\kappa^2}{2}t^2+O(t)\right\},
+\]
+whose negative-tail integral diverges. Thus the original $f_{e_\tau\mid X,Z}(0)$ is infinite. Mixing conditional only on $X$ instead gives Gaussian variance $3-\rho^2=2.91>1$ and the same divergence. These are densities that integrate over treatment, not $f_{e_\tau\mid D,X,Z}(0)$ at a realized positive treatment value. Nor are they the historical fitted-normal proxy. This retained regularity limitation does not establish which feature causes any particular Monte Carlo rejection pattern and does not validate or repair nominal inference.
+
 \subsection{Score algebra and its conditions}
 \label{app:score-algebra}
 The ideal nuisance vector and derivative identities are retained below. They presume finite density-weighted moments and permissible differentiation, conditions not established for the simulation DGP's non-finite true residual density. They are not implementation-level assertions. The executed proxy, residualization and nuisance fits do not inherit these properties automatically, and the chi-square cutoff is used nominally without an established validity result for the preserved implementations under this DGP. Same-sample fitting requires its own nuisance and generated-score justification; absence of cross-fitting alone does not prove invalidity.
diff --git a/journal_article/sections/04_results.tex b/journal_article/sections/04_results.tex
index f34a2e11..2c7d4f8e 100644
--- a/journal_article/sections/04_results.tex
+++ b/journal_article/sections/04_results.tex
@@ -1,5 +1,6 @@
 \section{Simulation Results}
 \label{chap:results}
+Appendix~\ref{app:evidence-map} maps the principal numerical findings, including comparisons using all design cells, to the exact frozen CSVs and existing full-table and figure assets. These sources permit inspection without re-estimation.
 \subsection{Instrument-Relevance Calibration}
 \label{sec:results-relevance-calibration}
 
diff --git a/journal_article/sections/data_availability.tex b/journal_article/sections/data_availability.tex
new file mode 100644
index 00000000..c49b21eb
--- /dev/null
+++ b/journal_article/sections/data_availability.tex
@@ -0,0 +1,4 @@
+\section*{Data and code availability}
+The public repository is \url{https://github.com/U-Olim/DML-IVQR_Master_Thesis}. Repository visibility, commit \texttt{15b8b4dc95e3658f3b858a6f792ea2983299aaa6}, and directory listings for the main frozen CSVs, reporting summaries and package archives were checked through the GitHub API on 10 November 2026. Readers can select that commit and follow the exact paths in Appendix~\ref{app:evidence-map} to inspect both sample sizes, all quantiles and relevance settings without running an estimator. These are simulated data and archived computational outputs, not an external observational dataset. The freeze record names \texttt{ac9a9ccad027cde05488abb633e66cc02f87cc46}; that identifier was not resolvable in the present local object store and returned HTTP 404 from the repository API. It is retained as recorded provenance, not offered as a verified release checkout.
+
+Historical rerunning is a different task. Source and configuration are under \path{thesis_extension/src/} and \path{thesis_extension/config/}; environment records, package archives and the captured Windows library are under \path{thesis_extension/environment/}. The recorded environment uses R~3.4.3 and pinned historical packages (Appendix~\ref{app:reproducibility}); their presence does not establish installation portability or exact random-number replay. Main-run worker-specific penalty states are not recoverable from the parent seed alone. Large grid-diagnostic profiles and saved primitives are local, Git-ignored artifacts identified in \path{thesis_extension/diagnostics/grid_sensitivity/GRID_RESULTS_MANIFEST.csv}; tracked diagnostic summaries remain available. Stage 2H pilot outputs under \path{journal_validation/stage2h/pilot/runs/} and its \path{journal_validation/stage2h/pilot/SHA256_MANIFEST.json} are also Git-ignored and are not part of the public tracked archive. No public deposit of these local artifacts or portable historical runtime is established here. This revision does not publish new results or replace historical fits with later certified numerical solutions.
diff --git a/journal_article/supplementary/D_evidence_map.tex b/journal_article/supplementary/D_evidence_map.tex
new file mode 100644
index 00000000..6ee1edac
--- /dev/null
+++ b/journal_article/supplementary/D_evidence_map.tex
@@ -0,0 +1,31 @@
+\subsection{Frozen-evidence map}
+\label{app:evidence-map}
+All paths below are repository-relative. Select commit \texttt{15b8b4dc95e3658f3b858a6f792ea2983299aaa6} for the tracked archive. The keys connect the principal findings to complete saved evidence, including cells omitted from compact main-text displays. This map identifies sources; it does not recompute descriptive comparison counts or rerun historical checks.
+
+\begin{center}
+\small
+\begin{tblr}{colspec={X[3,l] X[2,l] X[1,l]},row{1}={font=\bfseries},hline{1,2,Z}={0.4pt}}
+Finding & Manuscript location & Evidence key \\
+Designed relevance ordering & Section~\ref{sec:results-relevance-calibration} & E1 \\
+Point-error deterioration and qualified estimator rankings & Section~\ref{sec:results-point-accuracy} & E2 \\
+Truth acceptance and false-candidate rejection & Sections~\ref{sec:results-coverage}--\ref{sec:results-power} & E3 \\
+Nominal-looking acceptance with little grid exclusion & Abstract; Section~\ref{chap:results} & E2--E4 \\
+Domain sensitivity and finite numerical scope & Appendix~\ref{app:numerical-domain-diagnostics} & E5 \\
+Selected-case rank and decision sensitivity & Appendix~\ref{app:reproducibility} & E6 \\
+\end{tblr}
+\end{center}
+
+\begin{description}
+\item[E1: Relevance.] \path{thesis_extension/calibration/instrument_strength_100rep/kappa_strength_summary.csv}; presentation: \path{journal_article/tables/table_strength_calibration.tex}.
+
+\item[E2: Full performance, both sample sizes.] \path{thesis_extension/final/output/n500/summary.csv} and \path{thesis_extension/final/output/n1000/summary.csv} contain Bias, MAE, RMSE, historical \texttt{Coverage}/\texttt{Size}, accepted-measure and boundary/full-grid summaries. Replication-level sources are \path{thesis_extension/final/output/n500/results.csv} and \path{thesis_extension/final/output/n1000/results.csv}; stored candidate statistics are \path{thesis_extension/final/output/n500/profiles.csv} and \path{thesis_extension/final/output/n1000/profiles.csv}. Full presentation assets: \path{journal_article/tables/generated/appendix_point_performance.tex}, \path{journal_article/tables/generated/appendix_coverage.tex}, and \path{journal_article/tables/generated/appendix_cr_informativeness.tex}; compact table: \path{journal_article/tables/table_main_performance.tex}. Existing RMSE images are \path{journal_article/figures/generated/rmse_n500.png} and \path{journal_article/figures/generated/rmse_n1000.png}.
+
+\item[E3: Truth testing and power.] Use E2's \texttt{Coverage}, \texttt{Size} and replication \texttt{W\_true} fields for direct-at-truth evaluations. False-candidate summaries are \path{thesis_extension/final/output/n500/power_summary.csv} and \path{thesis_extension/final/output/n1000/power_summary.csv}; replication records are \path{thesis_extension/final/output/n500/power.csv} and \path{thesis_extension/final/output/n1000/power.csv}. Full presentation: \path{journal_article/tables/generated/appendix_power.tex}; figures: \path{journal_article/figures/generated/coverage_heatmap.pdf} and \path{journal_article/figures/generated/power_median_combined.pdf}. The abstract's $0.942/3.900/0.094$ contrast selects E2's \texttt{Coverage}/\texttt{median\_grid\_accepted\_set\_measure} and this power summary's \texttt{power}, respectively, at $n=1000$, $\tau=0.50$, $\kappa=0.10$, estimator \texttt{DML-IVQR-BC}, with $\Delta=0.50$ for power only. These are different summaries, not a joint event or validated grid-set coverage.
+
+\item[E4: Grid informativeness.] In addition to E2's summaries/profiles, \path{thesis_extension/reporting/output/table_cr_informativeness_full.csv} contains all design cells. Existing images are \path{journal_article/figures/generated/accepted_measure_n500.png}, \path{journal_article/figures/generated/accepted_measure_n1000.png}, and \path{journal_article/figures/generated/full_domain_acceptance_heatmap.pdf}. Grid quadrature and all-grid acceptance are distinct diagnostics on the maintained domain.
+
+\item[E5: Domain expansion.] Tracked sources: \path{thesis_extension/diagnostics/grid_sensitivity/output/stage1/stage1_summary.csv}, \path{thesis_extension/diagnostics/grid_sensitivity/output/stage1/stage1_expansion_summary.csv}, \path{thesis_extension/diagnostics/grid_sensitivity/output/stage2/stage2_summary.csv}, and \path{thesis_extension/diagnostics/grid_sensitivity/output/stage2/stage2_expansion_summary.csv}. Combined reporting view: \path{thesis_extension/reporting/output/table_grid_domain_diagnostic.csv}; table and figure: \path{journal_article/tables/generated/appendix_grid_diagnostic.tex} and \path{journal_article/figures/grid_domain_expansion.png}. Design, failure and local-only artifact scope are in \path{thesis_extension/diagnostics/grid_sensitivity/GRID_RESULTS_PROVENANCE.md} and \path{thesis_extension/diagnostics/grid_sensitivity/GRID_RESULTS_MANIFEST.csv}. This separate diagnostic uses 100 intended replications; the recorded Stage 1 failure remains excluded from complete-profile summaries, not counted as acceptance. Large profiles and saved primitives are Git-ignored; tracked summaries do not supply full stochastic replay.
+
+\item[E6: Numerical sensitivity.] \path{journal_validation/stage2g/full_path_validation/FULL_PATH_REPORT.md} records the selected 24-problem comparison and five Policy A/C decision differences. \path{journal_validation/stage2g/deterministic_implementation/DETERMINISTIC_IMPLEMENTATION_REPORT.md} and \path{journal_validation/stage2g/deterministic_implementation/IMPLEMENTATION_CONTRACT_v1.md} specify the fixed-objective and input scope of later certificates. Earlier rank-stability evidence is in \path{journal_validation/stage2c/stability/STABILITY_REPORT.md}. These reports are not population error rates or replacements for E2--E5.
+\end{description}
+The inventories \path{thesis_extension/reporting/EMPIRICAL_RESULTS_MANIFEST.csv} and \path{thesis_extension/reporting/REPORTING_OUTPUT_MANIFEST.csv} retain historical input/output hashes and provenance. An entry in a manifest alone does not establish public availability: local-only exclusions are stated in the data and code availability statement.
```

## Working-tree status after implementation

```text
 M journal_article/main.tex
 M journal_article/sections/01_introduction.tex
 M journal_article/sections/02_framework.tex
 M journal_article/sections/04_results.tex
 M journal_article/supplementary/D_implementation.tex
 M journal_validation/publication_review/BATCH2_CHANGE_REPORT.md
?? journal_article/sections/data_availability.tex
?? journal_article/supplementary/D_evidence_map.tex
?? journal_validation/publication_review/BATCH3_CHANGE_REPORT.md
```
