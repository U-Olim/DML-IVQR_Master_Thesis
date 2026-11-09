# Stage 2I ? Publication Revision Batch 1: Change Report

**Branch:** `journal-validation`  
**Baseline:** `2ceec58a`  
**Date:** 9 November 2026 (Asia/Tashkent)  
**Scope:** R1-001, R1-004, R1-005 and R1-006 only. No commit or push.

## Summary

This batch adds a selected-case numerical sensitivity disclosure; attributes performance comparisons to the preserved implementations; separates ideal score motivation from nominal implemented inference; and distinguishes direct-at-truth acceptance, stored finite-grid accepted sets and conceptual unrestricted test inversion. The historical Coverage label and its computed formula are retained and explained. No table, plot, reported statistic, estimator, cutoff, research code or authorship detail was changed.

## Evidence for the numerical disclosure

- `journal_validation/stage2g/full_path_validation/FULL_PATH_REPORT.md:25?27,129?131`: complete 24-problem comparison and documented five Policy A/Policy C decision differences. Policy A is historical; Policy C uses certified exact outcome ranks with the retained density/projection pathway.
- `journal_validation/stage2g/full_path_validation/FULL_PATH_REPORT.md:7,19?23,74?80`: bounds have specified conditional scope; no general historical-decision invariance follows.
- `journal_validation/stage2g/deterministic_implementation/DETERMINISTIC_IMPLEMENTATION_REPORT.md:61?97`: fixed-objective/input equivalence is distinguished from adaptive-path and bitwise historical-output equivalence.
- The new paragraph reports only 5 of 24 selected candidate problems; it does not convert this to a Monte Carlo error probability, replace archived results, or claim restored calibration. No new numerical calculation was used.

## Modification log

Original line references are relative to HEAD; revised references are relative to this working tree. Each entry records the exact replaced text, including additions within the replacement.

### B1-01 ? R1-004

- **File:** `journal_article/main.tex`.
- **Original lines:** 18?18; **revised lines:** 18?18.
- **Scientific justification:** Attribute the documented RMSE comparison to complete implementations; retain exceptions and the existing 35/40 count.

**Original wording**

```latex
DML-IVQR often improves point accuracy relative to Full-GMM, with exceptions.
```

**Revised wording**

```latex
The preserved DML-IVQR implementation has lower RMSE than the preserved Full-GMM implementation in 35 of the 40 matched designs, with exceptions.
```

### B1-02 ? R1-004, R1-005

- **File:** `journal_article/main.tex`.
- **Original lines:** 18?18; **revised lines:** 18?18.
- **Scientific justification:** Remove an apparent attribution of observed benefits to orthogonalization/regularization and state the inference boundary.

**Original wording**

```latex
Orthogonalization and regularized nuisance estimation can mitigate high-dimensional estimation difficulties, but cannot replace identifying information lost as instrument relevance deteriorates.
```

**Revised wording**

```latex
These implementation-level comparisons do not isolate the effect of regularization or establish validity of the nominal chi-square cutoff.
```

### B1-03 ? R1-004

- **File:** `journal_article/sections/01_introduction.tex`.
- **Original lines:** 10?10; **revised lines:** 10?10.
- **Scientific justification:** Describe observed performance of the actual bundled procedures rather than a regularization mechanism.

**Original wording**

```latex
DML-IVQR usually improves point accuracy relative to Full-GMM, with exceptions.
```

**Revised wording**

```latex
The preserved DML-IVQR implementation usually has lower RMSE than the preserved Full-GMM implementation, with exceptions.
```

### B1-04 ? R1-004

- **File:** `journal_article/sections/01_introduction.tex`.
- **Original lines:** 10?10; **revised lines:** 10?10.
- **Scientific justification:** Replace an unsupported separation of mechanisms with the supported oracle comparison and explicit confounding.

**Original wording**

```latex
These results separate the benefits of nuisance estimation from the information required to distinguish competing structural effects.
```

**Revised wording**

```latex
Deterioration of Oracle-GMM shows that high-dimensional nuisance estimation is not the sole explanation for the loss of accuracy. Differences in nuisance dimension, residualization and other computational details prevent attributing the DML--Full comparison to regularization alone.
```

### B1-05 ? R1-005

- **File:** `journal_article/sections/02_framework.tex`.
- **Original lines:** 83?83; **revised lines:** 83?83.
- **Scientific justification:** Identify the displayed orthogonal construction as reference theory rather than a property established for executable fits.

**Original wording**

```latex
The theoretical score is
```

**Revised wording**

```latex
The ideal score below is a theoretical reference:
```

### B1-06 ? R1-005

- **File:** `journal_article/sections/02_framework.tex`.
- **Original lines:** 133?133; **revised lines:** 133?135.
- **Scientific justification:** State the missing theory-to-implementation transfer explicitly without treating absence of cross-fitting as a proof of invalidity.

**Original wording**

```latex
The estimator comparison encompasses these implementation differences as well as regularization and nuisance dimension; it cannot isolate the effect of regularization alone.
```

**Revised wording**

```latex
The estimator comparison encompasses these implementation differences as well as regularization and nuisance dimension; it cannot isolate the effect of regularization alone.

The executed procedures use implementation-specific density proxies, residualization and nuisance estimation, so the ideal orthogonality calculation does not establish orthogonality or an inference theorem for these implementations. The absence of cross-fitting alone is not proof of invalidity; the required same-sample nuisance and generated-score conditions have not been established here.
```

### B1-07 ? R1-005, R1-006

- **File:** `journal_article/sections/02_framework.tex`.
- **Original lines:** 168?168; **revised lines:** 170?170.
- **Scientific justification:** State the nominal cutoff and identify the displayed inversion as the computed finite-grid object.

**Original wording**

```latex
The procedures apply the asymptotic $\chi^2_{d_z}$ reference cutoff to each candidate statistic. At significance level $\gamma$, inversion gives
```

**Revised wording**

```latex
The procedures use the asymptotic $\chi^2_{d_z}$ reference cutoff nominally. For the stored candidate evaluations on the finite grid $\mathcal A=G_0$ specified below, inversion at nominal significance level $\gamma$ gives the grid accepted set
```

### B1-08 ? R1-006

- **File:** `journal_article/sections/02_framework.tex`.
- **Original lines:** 170?170; **revised lines:** 172?172.
- **Scientific justification:** Relabel the finite-grid set without changing its candidate decisions, cutoff or defining inequality.

**Original wording**

```latex
\mathcal C_{e,1-\gamma}(\tau)
```

**Revised wording**

```latex
\mathcal C^{\mathrm{grid}}_{e,1-\gamma}(\tau)
```

### B1-09 ? R1-005, R1-006

- **File:** `journal_article/sections/02_framework.tex`.
- **Original lines:** 178?178; **revised lines:** 180?182.
- **Scientific justification:** Separate conceptual unrestricted inversion, stored-grid acceptance and the direct-test diagnostic; explicitly withhold validity and automatic weak-identification transfer.

**Original wording**

```latex
Here $c_{1-\gamma,d_z}$ is the chi-square quantile, with $d_z=2$. The corresponding theoretical candidate tests can accommodate weak identification under their regularity conditions \parencite{chernozhukov_hansen_2008}; finite-sample calibration of these preserved implementations remains an empirical question.
```

**Revised wording**

```latex
This set is defined by the stored grid evaluations, not by separately rerun direct tests. Conceptually, unrestricted test inversion would retain all real candidate values accepted by a fully specified candidate-test rule, including its randomization. That unrestricted set is not computed here. Direct-at-truth test acceptance, defined in Section~\ref{sec:performance-measures}, is a third object; its reported frequency is not literal membership coverage of the stored finite-grid set.

Here $c_{1-\gamma,d_z}$ is the chi-square quantile, with $d_z=2$. Its validity for the preserved implementations under the studied DGP has not been established. The cited theoretical candidate tests can accommodate weak identification under their regularity conditions \parencite{chernozhukov_hansen_2008}, but that robustness does not automatically transfer to the implemented density proxies, residualization and nuisance fits.
```

### B1-10 ? R1-006

- **File:** `journal_article/sections/03_design.tex`.
- **Original lines:** 132?132; **revised lines:** 132?132.
- **Scientific justification:** Explain the retained Coverage label before its unchanged indicator/average formula.

**Original wording**

```latex
Coverage and power are evaluated directly at the unrounded true value and specified false candidates, independently of grid membership:
```

**Revised wording**

```latex
The quantity historically labeled coverage is direct-at-truth candidate-test acceptance, used here as a test-inversion coverage diagnostic. Power is evaluated at specified false candidates. Both use direct evaluations, independently of grid membership; the computed quantities retain their original definitions:
```

### B1-11 ? R1-006

- **File:** `journal_article/sections/03_design.tex`.
- **Original lines:** 163?163; **revised lines:** 163?163.
- **Scientific justification:** Make off-grid truth and independent candidate-penalty calls explicit while retaining all statistics and avoiding a new stochastic process definition.

**Original wording**

```latex
For DML, direct truth and stored-profile evaluations can use different pivotal draws even at the same candidate. Reported coverage is the repeated-sample acceptance frequency of the direct test, rather than membership reconstructed from a stored grid profile. Raw power uses the common nominal cutoff without size adjustment.
```

**Revised wording**

```latex
For DML, fresh pivotal draws are generated for each penalty call, so a direct-truth evaluation and a stored-profile evaluation can use different draws even at the same candidate. Reported coverage is the repeated-sample acceptance frequency of the direct test, not literal membership coverage of the stored finite-grid set $\mathcal C^{\mathrm{grid}}_{e,0.95}(\tau)$. Except at the median, the unrounded structural truths do not belong to $G_0$; even at an on-grid truth, the separate DML computations need not give the same acceptance decision. Conceptual unrestricted inversion requires a fully specified candidate-test rule, including its randomization, and is not reconstructed from these separately recorded evaluations. Raw power uses the common nominal cutoff without size adjustment.
```

### B1-12 ? R1-004

- **File:** `journal_article/sections/04_results.tex`.
- **Original lines:** 25?25; **revised lines:** 25?25.
- **Scientific justification:** Preserve both documented counts and every subsequent numerical exception, while assigning the comparison to implementations.

**Original wording**

```latex
Across the 40 matched $(n,\tau,\kappa)$ designs, DML has lower RMSE than Full-GMM in 35 and lower RMSE than Oracle-GMM in 11.
```

**Revised wording**

```latex
Across the 40 matched $(n,\tau,\kappa)$ designs, the preserved DML-IVQR implementation has lower RMSE than the preserved Full-GMM implementation in 35 and lower RMSE than the preserved Oracle-GMM implementation in 11.
```

### B1-13 ? R1-001

- **File:** `journal_article/sections/04_results.tex`.
- **Original lines:** 50?50; **revised lines:** 50?50.
- **Scientific justification:** Keep the valid bookkeeping-audit conclusions but prevent interpreting them as general numerical invariance.

**Original wording**

```latex
The audit rules out missing-value handling, nonfinite truth statistics, and reconstruction from rounded grid confidence sets as explanations for the observed undercoverage.
```

**Revised wording**

```latex
The audit rules out missing-value handling, nonfinite truth statistics, and reconstruction from rounded grid confidence sets as explanations for the observed undercoverage. It does not establish invariance to residual-rank arithmetic or numerical solution details; later selected-case audits document such sensitivity, as summarized in Appendix~\ref{app:reproducibility}.
```

### B1-14 ? R1-004

- **File:** `journal_article/sections/05_discussion.tex`.
- **Original lines:** 7?7; **revised lines:** 7?7.
- **Scientific justification:** Keep the existing exceptions and no-uniform-superiority qualification at the implementation level.

**Original wording**

```latex
DML-IVQR usually has lower RMSE than Full-GMM, but the documented exceptions and the separate coverage and power results rule out uniform superiority.
```

**Revised wording**

```latex
The preserved DML-IVQR implementation usually has lower RMSE than the preserved Full-GMM implementation, but the documented exceptions and the separate coverage and power results rule out uniform superiority.
```

### B1-15 ? R1-004

- **File:** `journal_article/sections/06_conclusion.tex`.
- **Original lines:** 4?4; **revised lines:** 4?4.
- **Scientific justification:** Remove the causal attribution in the conclusion while retaining the existing count, bundled differences and exceptions.

**Original wording**

```latex
Regularized nuisance estimation often improves point accuracy relative to Full-GMM, with exceptions.
```

**Revised wording**

```latex
The preserved DML-IVQR implementation has lower RMSE than the preserved Full-GMM implementation in 35 of the 40 matched designs. This comparison includes differences in nuisance dimension, residualization and other computational details; it does not isolate the effect of regularization, and the documented exceptions remain material.
```

### B1-16 ? R1-004, R1-005

- **File:** `journal_article/sections/06_conclusion.tex`.
- **Original lines:** 4?4; **revised lines:** 4?4.
- **Scientific justification:** End the interpretation with the supported theory/implementation boundary rather than an untested benefit attributed to orthogonalization.

**Original wording**

```latex
Orthogonalization and regularization can mitigate high-dimensional estimation difficulties, but cannot replace identifying information lost when instrument relevance deteriorates.
```

**Revised wording**

```latex
The ideal orthogonal score motivates the procedure, but the simulations establish neither orthogonality of the implemented score nor validity of its nominal chi-square reference law.
```

### B1-17 ? R1-006

- **File:** `journal_article/supplementary/C_coverage_audit.tex`.
- **Original lines:** 7?7; **revised lines:** 7?7.
- **Scientific justification:** Align the coverage-audit appendix with the clarified framework/design terminology without altering any audit count or interval.

**Original wording**

```latex
Coverage is evaluated directly at the exact true structural effect $\alpha_0(\tau)$, independently of whether that value lies on the finite candidate grid.
```

**Revised wording**

```latex
The reported coverage diagnostic is direct candidate-test acceptance at the exact true structural effect $\alpha_0(\tau)$, independently of whether that value lies on the finite candidate grid. It is not literal membership coverage of the stored grid accepted set defined in Section~\ref{sec:implementation}; fresh pivotal draws can also distinguish the DML direct and stored-grid evaluations at the same candidate.
```

### B1-18 ? R1-001

- **File:** `journal_article/supplementary/D_implementation.tex`.
- **Original lines:** 10?10; **revised lines:** 10?12.
- **Scientific justification:** Disclose the documented 5/24 selected-candidate comparison with exact report references and certificate scope; explicitly reject a full-experiment error-rate interpretation.

**Original wording**

```latex
This editorial conversion does not rerun those historical validations or simulations.
```

**Revised wording**

```latex
This editorial conversion does not rerun those historical validations or simulations.

The original Monte Carlo results remain outputs of the preserved historical executable implementation. Later selected-case Stage 2G audits identified sensitivity of residual ranks and test decisions to computational details: historical Policy A and the certified-outcome Policy C path differed in 5 of the 24 saved candidate problems examined. Policy C uses exact outcome residual ranks with the retained density/projection pathway; these panel results do not replace the historical Monte Carlo results. Numerical certificates establish properties of specified fixed objectives and input values, with decision bounds conditional on the stated exported quantities; they do not establish invariance of every historical Monte Carlo decision or certify all adaptive calibration trajectories. The selected panels do not establish an error frequency for the full Monte Carlo experiment.\footnote{See \path{journal_validation/stage2g/full_path_validation/FULL_PATH_REPORT.md}, ``Complete 24-problem decision comparison'' and ``Required conclusions''; and \path{journal_validation/stage2g/deterministic_implementation/DETERMINISTIC_IMPLEMENTATION_REPORT.md}, ``Mathematical equivalence: established scope''.}
```

### B1-19 ? R1-005

- **File:** `journal_article/supplementary/D_implementation.tex`.
- **Original lines:** 156?156; **revised lines:** 158?158.
- **Scientific justification:** Make the implementation notes explicitly withhold automatic orthogonality/inference transfer without diagnosing invalidity from missing cross-fitting alone.

**Original wording**

```latex
They are not implementation-level assertions.
```

**Revised wording**

```latex
They are not implementation-level assertions. The executed proxy, residualization and nuisance fits do not inherit these properties automatically, and the chi-square cutoff is used nominally without an established validity result for the preserved implementations under this DGP. Same-sample fitting requires its own nuisance and generated-score justification; absence of cross-fitting alone does not prove invalidity.
```

## Preservation and checks

- A source comparison against HEAD confirmed that every displayed equation block is unchanged except the grid-set symbol relabeling. All Bias/MAE/RMSE, direct-truth acceptance, empirical-size, false-candidate rejection, cutoff, primary-grid and accepted-measure equations retain their computed definitions. The finite-grid inversion equation is relabeled with a `grid` superscript; its defining inequality and finite candidate domain are unchanged.
- Result counts and numerical exceptions were retained. The existing 35/40 RMSE count is repeated in the abstract and conclusion as an implementation-level comparison; it was not recomputed.
- The title, author block, author order, affiliations and PDF metadata were intentionally left byte-for-byte unchanged. In particular, R1-003 is outside this batch.
- Research code, data, table sources, plot files, bibliography and the existing PDF were not edited. The Round 1 audit report was preserved.
- No simulations, estimators, statistical tests or result-generation scripts were run. The checks for this batch concern source changes and document consistency only.

## Remaining scientific vulnerabilities

- Orthogonality and valid chi-square inference for the preserved implementation under this DGP remain unestablished. Reference-theory weak-identification robustness does not automatically transfer.
- The infinite-density regularity problem, implementation-specific proxy/intercept, nuisance convergence requirements and same-sample generated-score justification remain unresolved by editing.
- Selected-case numerical sensitivity is documented, but its frequency or effect on aggregate historical Monte Carlo results cannot be inferred from these panels.
- Exact historical RNG regeneration and decision invariance are not established. Separate DML penalty calls can differ even at the same candidate.
- The direct-at-truth acceptance diagnostic does not establish membership coverage of the stored finite-grid sets or geometry of an unrestricted confidence set.
- The design compares bundled implementations; the causal contribution of regularization is not identified.
- Other Round 1 issues, including title-source/revision inconsistency, declarations, broader novelty framing, evidence navigation and journal-specific requirements, remain outside scope.

## Temporary document compilation

**Outcome: compilation did not complete. No successful build is claimed.**

The installed pdfLaTeX was invoked from `journal_article/` with automatic package installation disabled and all document outputs directed to:

`C:\Users\User\AppData\Local\Temp\dml-ivqr-batch1-1ca5db0ddb3446f788fadd9b42bb0b1e`

Command:

```powershell
& 'C:/Users/User/AppData/Local/Programs/MiKTeX/miktex/bin/x64/pdflatex.exe' -disable-installer -interaction=nonstopmode -halt-on-error '-output-directory=C:\Users\User\AppData\Local\Temp\dml-ivqr-batch1-1ca5db0ddb3446f788fadd9b42bb0b1e' main.tex
```

MiKTeX stopped during initialization: ?It seems that this is a fresh TeX installation. Please finish the setup before proceeding.? It then reported access denied while attempting to create `C:\Users\User\AppData\Roaming\MiKTeX\2.9`. Its diagnostic log states exit code 1; PowerShell exposed process exit code `-1073740791`. The document was not successfully compiled, Biber and subsequent passes were not run, and no package installation, setup repair, permission escalation or manuscript workaround was attempted. The existing `journal_article/main.pdf` is unchanged and does not contain these revisions.

The pre-existing author-source issue R1-003 was intentionally left outside scope. Because this attempt stopped at tool initialization, it does not diagnose the current manuscript's TeX compatibility or prove that the author markup is the cause of a build failure.

## Complete manuscript Git diff

The following is the complete Git diff of the revised manuscript files against HEAD (not a summary). The untracked audit/change reports are not manuscript changes.

```diff
diff --git a/journal_article/main.tex b/journal_article/main.tex
index 7ade49b7..6cb95451 100644
--- a/journal_article/main.tex
+++ b/journal_article/main.tex
@@ -15,7 +15,7 @@ Email: \href{mailto:umidjonkostaev2025@gmail.com}{umidjonkostaev2025@gmail.com}\
 \begin{document}
 \maketitle
 \begin{abstract}
-We examine how weakening instrument relevance affects high-dimensional instrumental variable quantile regression (IVQR). A controlled extension of the Monte Carlo design of Chen, Huang, and Tien (2021) reduces the excluded signal while adding independent noise to preserve the marginal treatment distribution and the relationship generating endogeneity. Oracle-GMM, Full-GMM, and double/debiased machine learning IVQR (DML-IVQR) are compared across four relevance settings, five quantiles, and sample sizes of 500 and 1000, using 500 replications per design. As relevance declines, point-estimation errors increase, finite-domain accepted sets expand, and power generally falls, including for the oracle benchmark. Coverage can approach its nominal level while inference becomes uninformative; substantial undercoverage also occurs in several strong-relevance cells. DML-IVQR often improves point accuracy relative to Full-GMM, with exceptions. The evidence concerns a preserved executable implementation with an asymptotic chi-square cutoff, implementation-specific residualization and density proxies, and no cross-fitting. Orthogonalization and regularized nuisance estimation can mitigate high-dimensional estimation difficulties, but cannot replace identifying information lost as instrument relevance deteriorates.
+We examine how weakening instrument relevance affects high-dimensional instrumental variable quantile regression (IVQR). A controlled extension of the Monte Carlo design of Chen, Huang, and Tien (2021) reduces the excluded signal while adding independent noise to preserve the marginal treatment distribution and the relationship generating endogeneity. Oracle-GMM, Full-GMM, and double/debiased machine learning IVQR (DML-IVQR) are compared across four relevance settings, five quantiles, and sample sizes of 500 and 1000, using 500 replications per design. As relevance declines, point-estimation errors increase, finite-domain accepted sets expand, and power generally falls, including for the oracle benchmark. Coverage can approach its nominal level while inference becomes uninformative; substantial undercoverage also occurs in several strong-relevance cells. The preserved DML-IVQR implementation has lower RMSE than the preserved Full-GMM implementation in 35 of the 40 matched designs, with exceptions. The evidence concerns a preserved executable implementation with an asymptotic chi-square cutoff, implementation-specific residualization and density proxies, and no cross-fitting. These implementation-level comparisons do not isolate the effect of regularization or establish validity of the nominal chi-square cutoff.
 \end{abstract}
 \noindent\textbf{Keywords:} instrumental variable quantile regression; double machine learning; weak instruments; Monte Carlo simulation; confidence-set informativeness
 \input{sections/01_introduction}
diff --git a/journal_article/sections/01_introduction.tex b/journal_article/sections/01_introduction.tex
index 392d913b..c58a4ddc 100644
--- a/journal_article/sections/01_introduction.tex
+++ b/journal_article/sections/01_introduction.tex
@@ -7,4 +7,4 @@ High-dimensional regularization addresses a different source of difficulty. \tex
 
 The high-dimensional simulation in \textcite{chen_huang_tien_2021} holds instrument relevance fixed. We ask how progressively weakening that relevance changes point accuracy, coverage, power, and confidence-set informativeness across quantiles. Our contribution is a controlled Monte Carlo extension of their design and preserved executable procedures. A relevance parameter scales the excluded signal, while compensating independent noise preserves the treatment distribution and its joint distribution with the outcome disturbance. The extension introduces neither a new estimator nor a new inference theory.
 
-The experiment compares three complete implementations on common samples. Oracle-GMM knows the designated relevant controls; Full-GMM uses all controls without regularization; DML-IVQR regularizes nuisance estimation. As relevance falls, all three lose point accuracy and numerical localization, while power generally declines. DML-IVQR usually improves point accuracy relative to Full-GMM, with exceptions. Coverage can approach 95\% as tests lose discrimination, and several strong-relevance cells exhibit substantial undercoverage. The implementation differences, non-finite population density weight, and asymptotic reference distribution qualify interpretation throughout. These results separate the benefits of nuisance estimation from the information required to distinguish competing structural effects.
+The experiment compares three complete implementations on common samples. Oracle-GMM knows the designated relevant controls; Full-GMM uses all controls without regularization; DML-IVQR regularizes nuisance estimation. As relevance falls, all three lose point accuracy and numerical localization, while power generally declines. The preserved DML-IVQR implementation usually has lower RMSE than the preserved Full-GMM implementation, with exceptions. Coverage can approach 95\% as tests lose discrimination, and several strong-relevance cells exhibit substantial undercoverage. The implementation differences, non-finite population density weight, and asymptotic reference distribution qualify interpretation throughout. Deterioration of Oracle-GMM shows that high-dimensional nuisance estimation is not the sole explanation for the loss of accuracy. Differences in nuisance dimension, residualization and other computational details prevent attributing the DML--Full comparison to regularization alone.
diff --git a/journal_article/sections/02_framework.tex b/journal_article/sections/02_framework.tex
index 684ea848..ee765f2d 100644
--- a/journal_article/sections/02_framework.tex
+++ b/journal_article/sections/02_framework.tex
@@ -80,7 +80,7 @@ For candidate $a$, define $\widetilde X_i=(1,X_i')'$, $\rho_\tau(v)=v[\tau-\math
     =Z_i-d_0(a)-\Gamma(a)X_i.
     \label{eq:profile-residualized-instrument}
 \end{equation}
-Here $f_{\epsilon(a)}(0\mid X_i,Z_i)$ is the conditional residual density at zero. With $\eta=(c,\beta',\operatorname{vec}(\delta)')'$, let $\eta(a)$ collect the candidate-specific profile and $\eta_0=\eta(\alpha_0(\tau))$. The theoretical score is
+Here $f_{\epsilon(a)}(0\mid X_i,Z_i)$ is the conditional residual density at zero. With $\eta=(c,\beta',\operatorname{vec}(\delta)')'$, let $\eta(a)$ collect the candidate-specific profile and $\eta_0=\eta(\alpha_0(\tau))$. The ideal score below is a theoretical reference:
 \begin{equation}
     \begin{aligned}
         g_{\tau}(W_i;a,\eta)
@@ -132,6 +132,8 @@ The quantile-Lasso objective is an unscaled sum of check losses plus one half of
 
 Nuisances and scores use the same observations, with no sample splitting or cross-fitting. Fresh pivotal draws are generated at each penalty call, introducing algorithmic randomness across candidate evaluations. Appendix~\ref{app:reproducibility} records the penalty formulas, residualization rules, and environment details. The estimator comparison encompasses these implementation differences as well as regularization and nuisance dimension; it cannot isolate the effect of regularization alone.
 
+The executed procedures use implementation-specific density proxies, residualization and nuisance estimation, so the ideal orthogonality calculation does not establish orthogonality or an inference theorem for these implementations. The absence of cross-fitting alone is not proof of invalidity; the required same-sample nuisance and generated-score conditions have not been established here.
+
 For estimator $e$, let $\widehat g_{e,i}(a)$ be its score. The common criterion uses the uncentered score second moment:
 \begin{equation}
     \widehat g_{e,n}(a)
@@ -165,9 +167,9 @@ For estimator $e$, let $\widehat g_{e,i}(a)$ be its score. The common criterion
 \end{equation}
 The Monte Carlo candidate set $\mathcal A$ is the fixed grid specified below; the first exact minimizer is retained, and an incomplete profile receives no point estimate. Direct inversions use neither a generalized inverse nor additional matrix regularization. Failures or non-finite statistics are recorded as numerical failures.
 
-The procedures apply the asymptotic $\chi^2_{d_z}$ reference cutoff to each candidate statistic. At significance level $\gamma$, inversion gives
+The procedures use the asymptotic $\chi^2_{d_z}$ reference cutoff nominally. For the stored candidate evaluations on the finite grid $\mathcal A=G_0$ specified below, inversion at nominal significance level $\gamma$ gives the grid accepted set
 \begin{equation}
-    \mathcal C_{e,1-\gamma}(\tau)
+    \mathcal C^{\mathrm{grid}}_{e,1-\gamma}(\tau)
     =
     \left\{
         a\in\mathcal A:
@@ -175,4 +177,6 @@ The procedures apply the asymptotic $\chi^2_{d_z}$ reference cutoff to each cand
     \right\}.
     \label{eq:robust-confidence-region}
 \end{equation}
-Here $c_{1-\gamma,d_z}$ is the chi-square quantile, with $d_z=2$. The corresponding theoretical candidate tests can accommodate weak identification under their regularity conditions \parencite{chernozhukov_hansen_2008}; finite-sample calibration of these preserved implementations remains an empirical question. This construction differs from exact conditional finite-sample inference \parencite{chernozhukov_hansen_jansson_2009}. Weak-identification robustness does not ensure narrow sets or high power, and a finite numerical domain cannot establish global boundedness.
+This set is defined by the stored grid evaluations, not by separately rerun direct tests. Conceptually, unrestricted test inversion would retain all real candidate values accepted by a fully specified candidate-test rule, including its randomization. That unrestricted set is not computed here. Direct-at-truth test acceptance, defined in Section~\ref{sec:performance-measures}, is a third object; its reported frequency is not literal membership coverage of the stored finite-grid set.
+
+Here $c_{1-\gamma,d_z}$ is the chi-square quantile, with $d_z=2$. Its validity for the preserved implementations under the studied DGP has not been established. The cited theoretical candidate tests can accommodate weak identification under their regularity conditions \parencite{chernozhukov_hansen_2008}, but that robustness does not automatically transfer to the implemented density proxies, residualization and nuisance fits. This construction differs from exact conditional finite-sample inference \parencite{chernozhukov_hansen_jansson_2009}. Weak-identification robustness does not ensure narrow sets or high power, and a finite numerical domain cannot establish global boundedness.
diff --git a/journal_article/sections/03_design.tex b/journal_article/sections/03_design.tex
index a01ef992..03d0fdc3 100644
--- a/journal_article/sections/03_design.tex
+++ b/journal_article/sections/03_design.tex
@@ -129,7 +129,7 @@ For replication $r$, point accuracy is summarized by
   \end{aligned}
   \label{eq:performance-point}
 \end{equation}
-MAE and RMSE denote mean absolute error and root mean squared error. The preserved bias convention is truth minus estimate: positive bias indicates underestimation. Coverage and power are evaluated directly at the unrounded true value and specified false candidates, independently of grid membership:
+MAE and RMSE denote mean absolute error and root mean squared error. The preserved bias convention is truth minus estimate: positive bias indicates underestimation. The quantity historically labeled coverage is direct-at-truth candidate-test acceptance, used here as a test-inversion coverage diagnostic. Power is evaluated at specified false candidates. Both use direct evaluations, independently of grid membership; the computed quantities retain their original definitions:
 \begin{equation}
   C_r(\tau)
     =\mathbf{1}\!\left\{W_{n,r}\!\left(\alpha_0(\tau)\right)\leq c_{0.95}\right\},
@@ -160,7 +160,7 @@ MAE and RMSE denote mean absolute error and root mean squared error. The preserv
       \mathbf{1}\!\left\{W_{n,r}\!\left(a_{\Delta}(\tau)\right)>c_{0.95}\right\}.
   \label{eq:performance-power}
 \end{equation}
-For DML, direct truth and stored-profile evaluations can use different pivotal draws even at the same candidate. Reported coverage is the repeated-sample acceptance frequency of the direct test, rather than membership reconstructed from a stored grid profile. Raw power uses the common nominal cutoff without size adjustment.
+For DML, fresh pivotal draws are generated for each penalty call, so a direct-truth evaluation and a stored-profile evaluation can use different draws even at the same candidate. Reported coverage is the repeated-sample acceptance frequency of the direct test, not literal membership coverage of the stored finite-grid set $\mathcal C^{\mathrm{grid}}_{e,0.95}(\tau)$. Except at the median, the unrounded structural truths do not belong to $G_0$; even at an on-grid truth, the separate DML computations need not give the same acceptance decision. Conceptual unrestricted inversion requires a fully specified candidate-test rule, including its randomization, and is not reconstructed from these separately recorded evaluations. Raw power uses the common nominal cutoff without size adjustment.
 
 The cutoff and common primary grid are
 \begin{equation}
diff --git a/journal_article/sections/04_results.tex b/journal_article/sections/04_results.tex
index 9fc5de1b..f34a2e11 100644
--- a/journal_article/sections/04_results.tex
+++ b/journal_article/sections/04_results.tex
@@ -22,7 +22,7 @@ Point accuracy deteriorates systematically as relevance weakens. Across the comp
 
 Increasing the sample size improves RMSE in every one of the 60 matched estimator--quantile--$\kappa$ comparisons. At $\tau=0.50$, Oracle RMSE falls from $0.102$ to $0.072$ when $n$ rises from 500 to 1000 at $\kappa=1$, and from $1.027$ to $0.945$ at $\kappa=0.10$. At $\tau=0.90$ and $\kappa=0.50$, DML RMSE falls from $0.539$ to $0.396$. These reductions establish better point accuracy in the larger simulated sample, but the remaining errors can still be substantial under weak relevance. Two sample sizes do not establish an asymptotic rate or imply that inference is well calibrated or informative in every design.
 
-Estimator rankings are systematic but not uniform. Across the 40 matched $(n,\tau,\kappa)$ designs, DML has lower RMSE than Full-GMM in 35 and lower RMSE than Oracle-GMM in 11. A sizeable DML advantage occurs at $n=500$, $\tau=0.90$, and $\kappa=0.50$, where RMSE is $0.539$ for DML, $1.362$ for Full, and $0.822$ for Oracle. One clear exception is $n=500$, $\tau=0.10$, and $\kappa=0.50$, where DML RMSE is $1.335$ compared with $1.219$ for Full. Other reversals are small: at $n=1000$, $\tau=0.50$, and $\kappa=1$, the values are $0.104$ and $0.100$. These counts are descriptive, and such small differences do not establish statistically meaningful superiority. Oracle is a benchmark with knowledge of the relevant controls, not a guaranteed finite-sample winner; moreover, the estimators differ in residualisation and other implementation details as well as regularisation.
+Estimator rankings are systematic but not uniform. Across the 40 matched $(n,\tau,\kappa)$ designs, the preserved DML-IVQR implementation has lower RMSE than the preserved Full-GMM implementation in 35 and lower RMSE than the preserved Oracle-GMM implementation in 11. A sizeable DML advantage occurs at $n=500$, $\tau=0.90$, and $\kappa=0.50$, where RMSE is $0.539$ for DML, $1.362$ for Full, and $0.822$ for Oracle. One clear exception is $n=500$, $\tau=0.10$, and $\kappa=0.50$, where DML RMSE is $1.335$ compared with $1.219$ for Full. Other reversals are small: at $n=1000$, $\tau=0.50$, and $\kappa=1$, the values are $0.104$ and $0.100$. These counts are descriptive, and such small differences do not establish statistically meaningful superiority. Oracle is a benchmark with knowledge of the relevant controls, not a guaranteed finite-sample winner; moreover, the estimators differ in residualisation and other implementation details as well as regularisation.
 
 Quantile patterns also distinguish directional bias from overall error. Under the convention $\mathrm{Bias}=\alpha_0-\widehat\alpha$, negative bias means overestimation and positive bias means underestimation. Across both sample sizes, all estimators, and all four $\kappa$ values, the 24 biases at $\tau=0.10$ are negative, whereas the 24 biases at $\tau=0.90$ are positive. The estimates therefore move inward on average at the two tail quantiles. No equally uniform sign statement holds for the three interior quantiles. Using unrounded values, the median has lower MAE and lower RMSE than each tail in every fixed-estimator, fixed-$n$, fixed-$\kappa$ comparison. This uniform centre-versus-tail ordering in point accuracy does not extend to coverage, which varies differently across quantiles and designs. Mean bias can also conceal large replication errors: for Oracle at $n=1000$, $\tau=0.50$, and $\kappa=0.10$, Bias is only $-0.044$ while RMSE is $0.945$. Positive and negative errors partly cancel in the mean, so small Bias is not evidence of small MAE or RMSE.
 
@@ -47,7 +47,7 @@ Each rate is based on $R=500$ replications. Its Monte Carlo standard error is
 \]
 The maximum MCSE is approximately $0.022$ and the MCSE at $0.95$ is approximately $0.010$. Appendix~\ref{app:coverage-forensic-audit} strengthens this cell-by-cell uncertainty check. Across 60,000 valid direct-at-truth evaluations, 53 pointwise two-sided 95\% Wilson intervals lie wholly below $0.95$, one lies wholly above it, and 66 contain it. No truth statistic is missing or nonfinite. The intervals use integer acceptance counts without a continuity correction; they are pointwise Monte Carlo intervals, not simultaneous or multiplicity-adjusted tests. An individual rate's MCSE is not used as the standard error of a difference between correlated simulation results.
 
-The audit rules out missing-value handling, nonfinite truth statistics, and reconstruction from rounded grid confidence sets as explanations for the observed undercoverage. It does not isolate a cause among finite-sample approximation error, features of the preserved implementation, or failure of the idealised regularity conditions for the asymptotic chi-square reference law in this DGP. Strong-relevance undercoverage also shows that weak relevance alone cannot explain the distortions. Coverage records retention of the truth; it does not record how readily false candidates are excluded. The next two sections therefore examine power and accepted-set informativeness before interpreting near-nominal coverage under weak relevance.
+The audit rules out missing-value handling, nonfinite truth statistics, and reconstruction from rounded grid confidence sets as explanations for the observed undercoverage. It does not establish invariance to residual-rank arithmetic or numerical solution details; later selected-case audits document such sensitivity, as summarized in Appendix~\ref{app:reproducibility}. It does not isolate a cause among finite-sample approximation error, features of the preserved implementation, or failure of the idealised regularity conditions for the asymptotic chi-square reference law in this DGP. Strong-relevance undercoverage also shows that weak relevance alone cannot explain the distortions. Coverage records retention of the truth; it does not record how readily false candidates are excluded. The next two sections therefore examine power and accepted-set informativeness before interpreting near-nominal coverage under weak relevance.
 
 \subsection{Power Against False Candidate Values}
 \label{sec:results-power}
diff --git a/journal_article/sections/05_discussion.tex b/journal_article/sections/05_discussion.tex
index a49278aa..941d68b9 100644
--- a/journal_article/sections/05_discussion.tex
+++ b/journal_article/sections/05_discussion.tex
@@ -4,7 +4,7 @@
 
 Taken together, the results show that weakening instrument relevance changes each dimension of finite-sample performance, but not in the same way. Point accuracy deteriorates systematically, accepted sets expand, and power against false candidate values generally declines, subject to the documented small reversals. Coverage is less systematic and can move toward its nominal level precisely when the procedure rejects few candidates. Near-nominal coverage can therefore coexist with low power and acceptance of most or all of the numerical domain. Accuracy, calibration, power, and informativeness measure different features of the procedure, and no one of them is sufficient to assess inference.
 
-The estimator comparison reinforces this interpretation. Oracle-GMM knows the designated relevant controls, yet its point accuracy, power, and accepted-set localisation still deteriorate as relevance declines. High-dimensional nuisance estimation therefore cannot be the sole explanation for the common relevance pattern. DML-IVQR usually has lower RMSE than Full-GMM, but the documented exceptions and the separate coverage and power results rule out uniform superiority. Oracle is likewise an infeasible benchmark rather than a guaranteed finite-sample winner. Because the implementations differ in nuisance dimension, regularisation, and residualisation details, these are comparisons among complete estimator implementations; they do not isolate the causal effect of regularisation.
+The estimator comparison reinforces this interpretation. Oracle-GMM knows the designated relevant controls, yet its point accuracy, power, and accepted-set localisation still deteriorate as relevance declines. High-dimensional nuisance estimation therefore cannot be the sole explanation for the common relevance pattern. The preserved DML-IVQR implementation usually has lower RMSE than the preserved Full-GMM implementation, but the documented exceptions and the separate coverage and power results rule out uniform superiority. Oracle is likewise an infeasible benchmark rather than a guaranteed finite-sample winner. Because the implementations differ in nuisance dimension, regularisation, and residualisation details, these are comparisons among complete estimator implementations; they do not isolate the causal effect of regularisation.
 
 Sample size and quantile comparisons require similar qualifications. Increasing $n$ from 500 to 1000 lowers RMSE in all 60 matched comparisons and typically narrows accepted sets and raises power where usable signal remains. It does not improve every inferential dimension: several strong-relevance DML coverage rates deteriorate substantially, and power has documented exceptions. Across quantiles, the lower-tail biases are uniformly negative and the upper-tail biases uniformly positive under the convention $\mathrm{Bias}=\alpha_0-\widehat\alpha$. At fixed estimator, $n$, and $\kappa$, both MAE and RMSE are lower at the median than at either tail throughout the final results, whereas coverage has no corresponding universal centre-versus-tail ordering. Results at two sample sizes establish finite-sample contrasts, not an asymptotic rate or limit.
 
diff --git a/journal_article/sections/06_conclusion.tex b/journal_article/sections/06_conclusion.tex
index 79bfa79c..1ae20289 100644
--- a/journal_article/sections/06_conclusion.tex
+++ b/journal_article/sections/06_conclusion.tex
@@ -1,6 +1,6 @@
 \section{Conclusion}
 This controlled extension of \textcite{chen_huang_tien_2021} documents the loss of estimation accuracy and inferential informativeness as excluded-instrument relevance weakens in a high-dimensional IVQR design. Independent compensating noise keeps the marginal treatment distribution and the relationship generating endogeneity fixed. The deterioration affects Oracle-GMM as well as Full-GMM and DML-IVQR, so high-dimensional nuisance estimation cannot be its sole explanation.
 
-Regularized nuisance estimation often improves point accuracy relative to Full-GMM, with exceptions. Coverage, however, is distinct from accuracy and informativeness: near-nominal truth retention can coexist with acceptance of most of the computational domain and little power against false effects. Strong-relevance undercoverage further prevents reading the nominal confidence level as a finite-sample guarantee. Orthogonalization and regularization can mitigate high-dimensional estimation difficulties, but cannot replace identifying information lost when instrument relevance deteriorates.
+The preserved DML-IVQR implementation has lower RMSE than the preserved Full-GMM implementation in 35 of the 40 matched designs. This comparison includes differences in nuisance dimension, residualization and other computational details; it does not isolate the effect of regularization, and the documented exceptions remain material. Coverage, however, is distinct from accuracy and informativeness: near-nominal truth retention can coexist with acceptance of most of the computational domain and little power against false effects. Strong-relevance undercoverage further prevents reading the nominal confidence level as a finite-sample guarantee. The ideal orthogonal score motivates the procedure, but the simulations establish neither orthogonality of the implemented score nor validity of its nominal chi-square reference law.
 
 The findings concern one DGP family, two sample sizes, five quantiles, and three preserved implementations. Density-weight regularity, residualization differences, same-sample estimation, penalty randomness, asymptotic critical values, and finite domains qualify the link to theoretical DML-IVQR. Future controlled comparisons could vary these features individually, examine a DGP satisfying the density conditions, and add sample sizes with systematic domain checks. Such experiments would assess mechanisms without presuming that a particular change restores calibration; no finite-grid diagnostic alone can establish global boundedness.
diff --git a/journal_article/supplementary/C_coverage_audit.tex b/journal_article/supplementary/C_coverage_audit.tex
index f69be440..e1f26171 100644
--- a/journal_article/supplementary/C_coverage_audit.tex
+++ b/journal_article/supplementary/C_coverage_audit.tex
@@ -4,7 +4,7 @@
 
 \subsection{Direct-at-Truth Coverage Audit}
 
-Coverage is evaluated directly at the exact true structural effect $\alpha_0(\tau)$, independently of whether that value lies on the finite candidate grid. The forensic audit checked 60,000 direct truth evaluations: 500 replications for each of 120 sample-size, quantile, instrument-strength, and estimator cells.
+The reported coverage diagnostic is direct candidate-test acceptance at the exact true structural effect $\alpha_0(\tau)$, independently of whether that value lies on the finite candidate grid. It is not literal membership coverage of the stored grid accepted set defined in Section~\ref{sec:implementation}; fresh pivotal draws can also distinguish the DML direct and stored-grid evaluations at the same candidate. The forensic audit checked 60,000 direct truth evaluations: 500 replications for each of 120 sample-size, quantile, instrument-strength, and estimator cells.
 
 Wilson 95\% Monte Carlo intervals exclude nominal $0.95$ coverage in 54 of the 120 cells. The audit finds no missing or nonfinite true-parameter $W$ statistics. The large coverage distortions reported in the main text are therefore neither plotting-grid artifacts nor consequences of missing-value handling. The frozen audit report and supporting diagnostics remain preserved in the repository. Wilson intervals are pointwise Monte Carlo uncertainty intervals, without simultaneous or multiplicity-adjusted significance claims. An individual rate's Monte Carlo standard error is not a standard error for a difference between correlated simulation results.
 
diff --git a/journal_article/supplementary/D_implementation.tex b/journal_article/supplementary/D_implementation.tex
index 7dc6405c..fc834ff6 100644
--- a/journal_article/supplementary/D_implementation.tex
+++ b/journal_article/supplementary/D_implementation.tex
@@ -9,6 +9,8 @@ The canonical environment is R~3.4.3 (30 November 2017) on 64-bit Windows, using
 
 Frozen CSVs permit deterministic reporting without re-estimation. Input/output manifests in \path{thesis_extension/reporting/}, diagnostic provenance records, reporting consistency checks, and figure validation records connect the reported numbers to archived outputs. Historical manifests describe their archived presentation state and can retain former asset paths. The original figure check covered 480 plotted values; selected-figure validation separately covered 120 coverage values, 120 full-grid frequencies, and 168 median rejection probabilities. The coverage summary is reconstructed from integer direct-at-truth counts; the variance illustration is analytical. This editorial conversion does not rerun those historical validations or simulations.
 
+The original Monte Carlo results remain outputs of the preserved historical executable implementation. Later selected-case Stage 2G audits identified sensitivity of residual ranks and test decisions to computational details: historical Policy A and the certified-outcome Policy C path differed in 5 of the 24 saved candidate problems examined. Policy C uses exact outcome residual ranks with the retained density/projection pathway; these panel results do not replace the historical Monte Carlo results. Numerical certificates establish properties of specified fixed objectives and input values, with decision bounds conditional on the stated exported quantities; they do not establish invariance of every historical Monte Carlo decision or certify all adaptive calibration trajectories. The selected panels do not establish an error frequency for the full Monte Carlo experiment.\footnote{See \path{journal_validation/stage2g/full_path_validation/FULL_PATH_REPORT.md}, ``Complete 24-problem decision comparison'' and ``Required conclusions''; and \path{journal_validation/stage2g/deterministic_implementation/DETERMINISTIC_IMPLEMENTATION_REPORT.md}, ``Mathematical equivalence: established scope''.}
+
 \subsection{Penalty, density proxy, and residualization}
 For each candidate, $b_0$ is the fitted outcome intercept and $b$ the slopes. In the preserved \texttt{rq.fit.lasso} augmented-observation implementation, the unscaled check-loss sum receives a penalty with factor $1/2$. The vector $\lambda^{rq}(a)$ is the supplied routine argument, including an intercept penalty. There is no post-Lasso refit. Let $s_k=(n^{-1}\sum_iX_{ik}^2)^{1/2}$; $U_{ir}$ are independent artificial Uniform$(0,1)$ draws, with $r=1,\ldots,1000$, and $\widehat Q_{0.9}$ is their empirical pivotal-statistic 90th percentile. Fresh draws are made on every penalty call. This is algorithmic randomness, not sample splitting.
 
@@ -153,7 +155,7 @@ The first five equations describe DML-IVQR. The last three describe Oracle-GMM a
 
 \subsection{Score algebra and its conditions}
 \label{app:score-algebra}
-The ideal nuisance vector and derivative identities are retained below. They presume finite density-weighted moments and permissible differentiation, conditions not established for the simulation DGP's non-finite true residual density. They are not implementation-level assertions.
+The ideal nuisance vector and derivative identities are retained below. They presume finite density-weighted moments and permissible differentiation, conditions not established for the simulation DGP's non-finite true residual density. They are not implementation-level assertions. The executed proxy, residualization and nuisance fits do not inherit these properties automatically, and the chi-square cutoff is used nominally without an established validity result for the preserved implementations under this DGP. Same-sample fitting requires its own nuisance and generated-score justification; absence of cross-fitting alone does not prove invalidity.
 \begin{equation}
     \eta(a)
     =
```
