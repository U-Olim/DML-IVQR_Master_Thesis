# LSSP scientific and editorial content audit

Date: 11 November 2026 (Asia/Tashkent). Target: **Communications in Statistics – Simulation and Computation (LSSP)**.

## Scope, identity and limits

Reviewed the complete named manuscript, `journal_article/submission/named/manuscript_named.pdf`, and its canonical LaTeX source: `main.tex`, `preamble.tex`, Sections 1–6, declarations, availability statement, Appendices A–D including the evidence map, included table/figure wrappers and generated domain-diagnostic tables. The bibliography and document dependencies were inspected as supporting material. Locations below are repository-relative, with current source line numbers; quotations retain source LaTeX where relevant.

The PDF has **34 pages**, SHA-256 `4fecad9e125211689910104b8b533cb5e03f1d96e24752dc58bb62b5e77e3388`. Fresh text extraction matches the existing named-package extraction exactly. Staged named `.tex`/`.bib` files have no byte differences from their corresponding canonical files. Existing contact sheets covering all 34 pages were inspected for section/display placement; this is a content audit, not a new full-resolution typography certification. Main text/declarations/availability end on p.16, references occupy p.17, and inline supplementary material occupies pp.18–34.

No manuscript changes are applied. The abstract, length, scientific results, equations, figures, tables and appendices are preserved. No simulations, statistical tests, estimator runs, research-code changes or dataset changes are undertaken. Existing Wilson intervals, comparison counts and numerical-audit findings are assessed as reported evidence, not independently regenerated here. This report does not certify every historical numerical value, original citation or public repository access. It does not reinterpret the incomplete Stage 2H pilot as new article evidence.

Classification: **MUST FIX** means a specific misleading statement or factual inconsistency to resolve before submission; **RECOMMENDED** means a useful local editorial improvement; **OPTIONAL** means a preference without a scientific necessity; **NO CHANGE** means the current passage is appropriate. Journal-rule uncertainties are distinguished from scientific defects.

## Overall assessment

**Scientifically coherent as a descriptive Monte Carlo sensitivity study, conditional on the local corrections below; not ready for submission unchanged.** The manuscript does not need a new estimator or inference theorem to support its stated descriptive purpose. Its central contribution is the distribution-preserving relevance construction and joint reporting of point errors, direct-test acceptance, false-candidate rejection and finite-grid informativeness for preserved executable implementations.

The limitations are substantive, not merely editorial: nominal chi-square validity is unestablished, historical numerical decisions are not universally certified, and exact historical penalty-stream replay is unavailable. Those facts restrict the conclusions to archived implementation behavior. They do not make the archived descriptive summaries meaningless or justify replacing them with theoretical-method claims. Conversely, adding caveats cannot establish validated inference. No new theoretical validation or simulation is requested as a condition of this editorial audit.

The strongest remaining content defect is Appendix A's continuous-domain acceptance wording (M1). Provenance language also became stale after the latest commit (M2). Local uncertainty wording should be qualified where conclusions otherwise sound established beyond the observed Monte Carlo estimates (M3). The repeated limitations are mostly purposeful; only modest optional compression is justified, not a broad shortening of the article.

## Section-by-section review

| Component / PDF pages | Assessment and disposition |
|---|---|
| Title, abstract, keywords / p.1 | **NO CHANGE.** The title accurately identifies a sensitivity study. The abstract explicitly disclaims a new estimator/theorem and distinguishes its three numerical summaries. Its non-finite-density and implementation caveats are scientifically material. Preserve it verbatim as instructed. Possible journal word-limit conflict is recorded under J3, not resolved by editing. |
| Introduction / pp.1–2 | **NO CHANGE** to the gap, controlled-design contribution and scope. Lines 6 and 10 distinguish distributional invariance from fixed realized samples. Lines 12–14 avoid causal regularization claims and validated-inference language. Some findings/limitations repeat Discussion/Conclusion; see R1–R4. |
| Framework §2.1 / pp.2–3 | **NO CHANGE** to equations or conditional orthogonality argument. Structural quantiles are distinguished from observational conditional quantiles. Finite density-weighted moments, invertibility and differentiation conditions are stated before interpreting the derivative identity. Line 125 explicitly says the mixed density diverges in this DGP. Thus the displayed ideal score is a conditional reference, not a score claimed to exist with those finite-moment properties here. |
| Implementations/inference §2.2 / pp.3–4 | **NO CHANGE** to proxy, intercept, same-sample and randomized-penalty disclosures. The cutoff is expressly nominal; theoretical robustness is not transferred automatically. “First exact minimizer” at line 168 refers to selection among stored scalar grid statistics, not exact nuisance optimization; clarify optionally under E3. |
| Design §3.1 / pp.5–6 | **NO CHANGE.** The Gaussian construction preserves the entire joint distribution of treatment and outcome disturbance, not only variance. The appendix derives this. The observed instrument construction differs from the source paper's displayed notation and is disclosed. Positive minimum kappa is not treated as a non-identification experiment. |
| Measures §3.2 / pp.6–7 | **NO CHANGE** to historical definitions, bias sign or equations. The trapezoidal quantity is correctly distinguished from finite-set Lebesgue length and unrestricted region length. Direct truth tests, grid tests and conceptual unrestricted inversion are separate. Conventional Monte Carlo uncertainty needs the nearby qualification proposed in M3; Appendix D already acknowledges the stream limitation. |
| Calibration §4.1 / pp.7–8 | **NO CHANGE.** F and partial R-squared describe the designed first-stage ordering, without a universal IVQR threshold. The 100-replication diagnostic is distinguished from the main experiment. |
| Point accuracy §4.2 / pp.8–10 | Rankings are descriptive, including exceptions and small differences. Oracle deterioration supports the limited statement that high-dimensional nuisance estimation is not the sole explanation. It does not identify a mechanism. **M3** qualifies the sentence claiming the larger-sample advantage is established. Preserve counts and values. |
| Acceptance/calibration §4.3 / pp.10–11 | Substantial below-nominal direct acceptance is documented; lack of grid rounding or missing statistics does not establish numerically invariant decisions. This is correctly acknowledged at line 51. The cross-design mean is a descriptive average, not pooled coverage or an independent sample. **E1** improves terminology; **M3** qualifies MC uncertainty. |
| False-candidate rejection §4.4 / pp.11–13 | **NO CHANGE** to the distinction between empirical size and raw power. The DGP parameter stays fixed while candidate values vary; this is rejection of false hypotheses, not a new alternative DGP. Size distortion is explicitly discussed, so power is not offered as an efficiency ranking. The 305/360 and 162/180 counts describe observed rates, not statistical superiority. |
| Informativeness §4.5 / pp.13–15 | Correct finite-domain interpretation, separate direct truth tests, no unrestricted geometry claim. **E2** softens “causes” and localizes the sample-size interpretation. The 100-replication wider-domain diagnostic and usable-profile qualification are explicit. |
| Discussion / p.15 | **NO CHANGE** to substantive implications. It explains the findings without attributing them to any single implementation feature. Reporting several diagnostics is justified; an application recommendation does not imply that the retained procedure is validated for applications. Optional repetitions are listed below. |
| Conclusion / pp.15–16 | Scientifically consistent. It does not promise restored calibration, global identification, implemented orthogonality or regularization superiority. **OPTIONAL** compression of the repeated inventory of limitations; retain the final inferential boundary. |
| Declarations and availability / p.16 | Funding/contribution/ethics statements are author attestations, not independently verified facts. Do not alter them automatically. AI-use history cannot be validated from this content audit; reconcile exact wording with author-confirmed provenance and applicable publisher policy before submission. **M2** concerns stale revision wording. No new anonymous-access requirement should be inherited from JSCS. |
| References / p.17 | The author–date system is compatible in principle with the available LSSP publisher PDF. No bibliography deletion or expansion is warranted solely by journal change. Exact current style remains a production check, not a demonstrated scientific defect. |
| Appendix A / pp.18–24 | Finite-domain diagnostics and the one incomplete profile are reported transparently; **M1** corrects continuous-acceptance wording. Preserve all five diagnostic tables and figure. |
| Appendix B / pp.25–26 | **NO CHANGE.** Normality, covariance and the compensating coefficient support the distributional invariance. Fixed-treatment structural quantiles are correctly distinguished from endogenous observational quantiles. The conceptual zero-signal endpoint is not claimed as a simulated identification result. |
| Appendix C / pp.26–28 | **NO CHANGE** to the 60,000 evaluations, 54 pointwise Wilson exclusions or separation of full-grid acceptance. These are existing uncertainty diagnostics, not multiplicity-adjusted discoveries. The language about excluding missingness/grid reconstruction is appropriately limited when read with §4.3 and Appendix D. Add M3 qualification near the main uncertainty statement rather than duplicating it everywhere. |
| Appendix D / pp.29–34 | Essential for interpreting the preserved implementation; **NO CHANGE** to equations, density-divergence argument, finite-solver qualifications or five-of-24 selected-panel disclosure. Fixed-objective certification is correctly separated from historical decision invariance. **M2** updates provenance tense. The evidence map identifies inspection sources without claiming portable replay or public availability of every listed artifact. |

## MUST FIX before submission

### M1. Continuous-domain acceptance is asserted from a grid quadrature

Location: `journal_article/supplementary/A_numerical_domain.tex:18` (p.18).

Original:

> A value close to four in \(A_0\) means that almost the entire four-unit primary domain is accepted; it does not mean that the unrestricted confidence region has length four.

Problem: The first clause asserts acceptance throughout almost all of a continuous interval. The second clause only disclaims unrestricted length; it does not cure that first assertion. Section 3 explicitly states that the trapezoidal binary sum does not locate continuous boundaries or establish intermediate-point acceptance. Appendix A should not contradict that definition.

Proposed minimal replacement:

> A value close to four in \(A_0\) means that the trapezoidal grid-acceptance summary is close to its maximum on the four-unit primary domain; it does not establish acceptance between evaluated points or unrestricted confidence-region length.

No equation, statistic, table or figure changes.

### M2. Current manuscript is incorrectly described as uncommitted

Locations and originals:

- `journal_article/sections/data_availability.tex:2`: “That commit supplies the accessible evidence archive, not the current uncommitted manuscript revision.”
- `journal_article/supplementary/D_implementation.tex:6`: “Current manuscript revisions are local and uncommitted.”
- `journal_article/supplementary/D_evidence_map.tex:3`: “it is distinct from both the unresolved historical freeze identifier and the current uncommitted manuscript revision.”

Problem: These were historically accurate build-time statements, but the corresponding canonical sources are now committed at HEAD `04180d551dd4ab04333333f2407bfeed7167c587`; the starting working tree was clean. A present-tense submission statement must not describe their current Git status incorrectly. This audit does not establish that HEAD is publicly accessible and must not replace the previously checked public evidence revision with an unverified public-release claim.

Proposed minimal changes, respectively:

> That commit supplies the checked evidence archive, rather than identifying the present manuscript version.

> The present manuscript version is distinct from that checked evidence revision.

> it is distinct from both the unresolved historical freeze identifier and the present manuscript version.

Retain the exact previously checked evidence identifier, check date, unresolved freeze identifier and local-only exclusions. Do not silently resolve the missing freeze or promise complete replay.

### M3. Qualify uncertainty statements rather than treating descriptive estimates as established population improvements

Location: `journal_article/sections/04_results.tex:24`.

Original:

> These reductions establish better point accuracy in the larger simulated sample, but the remaining errors can still be substantial under weak relevance.

Problem: The preceding “every one of the 60” count is a valid description of the saved estimates. “Establish” can nevertheless imply an underlying performance improvement demonstrated beyond Monte Carlo uncertainty, for which no paired RMSE-difference uncertainty is supplied. The later sentence about asymptotic rates does not address this finite-simulation distinction.

Proposed minimal replacement:

> These reductions show lower observed Monte Carlo RMSE at the larger sample size, but the remaining errors can still be substantial under weak relevance.

Related location: `journal_article/sections/04_results.tex:43`.

Original:

> Each rate is based on $R=500$ replications. Its Monte Carlo standard error is

Proposed minimal replacement before the unchanged displayed formula:

> Each rate is based on $R=500$ replications. Under independent replications, its conventional plug-in Monte Carlo standard error is

Add after the existing pointwise-interval qualification at line 49:

> These uncertainty summaries assume independent replications; the historical DML worker-stream independence is not verified (Appendix~\ref{app:evaluation-sequence}).

Reason: Appendix D already says the parent seed neither establishes worker-stream independence nor reproduces every penalty draw. That does not prove dependence or invalidate all reported MCSEs, but the main text's unconditional uncertainty language is stronger than the archived assurance. This correction preserves the formula and all existing intervals; it does not request new tests or a new RNG audit.

## RECOMMENDED editorial improvements

### E1. Make the coverage shorthand locally explicit

Location: `journal_article/sections/04_results.tex:32`.

Original: `\subsection{Coverage and Finite-Sample Calibration}`

Proposal: `\subsection{Direct-at-Truth Acceptance and Finite-Sample Calibration}`.

At line 35, replace only the opening sentence:

> Figure~\ref{fig:coverage-heatmap} shows that empirical coverage differs considerably from the nominal 95\% level, even under the strongest instrument relevance considered.

with:

> Figure~\ref{fig:coverage-heatmap} shows that direct-at-truth acceptance (historically labelled coverage) differs considerably from the nominal 95\% level, even under the strongest instrument relevance considered.

Rationale: Existing definitions make the shorthand defensible; it is not an undisclosed coverage computation error. A reader entering Results directly can still mistake it for membership coverage. Keep historical labels in preserved equations, figure artwork and tables. No global search-and-replace is appropriate.

The Table 2 note (`journal_article/tables/table_main_performance.tex:51`) says “Coverage is evaluated directly at the true structural quantile effect.” If prose-only caption-note changes are later authorized, the clearer equivalent is “Coverage denotes direct-at-truth test acceptance, not membership coverage of the stored grid set.” Preserve the table itself and numerical cells.

### E2. Describe observed grid effects without implying a separately identified mechanism

Location: `journal_article/sections/04_results.tex:73`.

Original:

> Thus declining relevance causes progressively more of the maintained domain to survive test inversion, even when coverage moves closer to $0.95$.

Proposal:

> Thus lower designed relevance is accompanied by a progressively larger median grid-acceptance measure, even when direct-at-truth acceptance moves closer to $0.95$.

The controlled design supports interpreting changes along the kappa construction. This is not a claim that all causal language is forbidden in simulation. The replacement precisely identifies the observed summary and avoids suggesting a mechanism separated from the compensating-noise construction or continuous interval acceptance.

Related line 77 original: “More observations improve localisation, but do not overcome the weakest relevance setting at these sample sizes.”

Proposal: “The larger sample has a smaller or unchanged observed median accepted measure in these comparisons, with little localization under the weakest relevance setting.”

### E3. Avoid confusing grid selection with exact nuisance optimization

Location: `journal_article/sections/02_framework.tex:168`.

Original: “the first exact minimizer is retained”

Proposal: “the first candidate attaining the minimum stored grid statistic is retained”.

The present statement is compatible with Appendix D's finite routine outputs when read carefully. This clarification prevents a local misunderstanding without changing the equation or tie rule.

## Actual repetition between Introduction, Results, Discussion and Conclusion

These are repeated propositions, not evidence of duplicated paragraphs. Full numerical Results passages generally belong in Results. A brief Introduction preview and Conclusion synthesis serve different functions. The following are alternatives for modest compression, not cumulative mandatory deletions; no reduction in current length is required.

### R1. Truth acceptance versus exclusion of false effects — OPTIONAL

Exact passages:

- `sections/01_introduction.tex:8`: “Direct-at-truth acceptance can approach the nominal confidence level while most of the grid is retained and few false candidates are rejected; a more accurate point estimate also need not imply better calibration.”
- `sections/04_results.tex:79`: “Truth retention, the amount of the grid retained, acceptance of the entire grid, and rejection of a particular false value therefore answer different questions.”
- `sections/05_discussion.tex:4`: “As relevance weakens, direct-at-truth acceptance can approach the nominal level while false-candidate rejection falls and most of the grid remains accepted. A lower RMSE likewise need not imply better test calibration.”
- `sections/06_conclusion.tex:4`: “The central empirical disagreement is between nominal-looking truth acceptance and useful exclusion of false effects. Retaining most of a grid while rejecting few false candidates offers little discrimination.”

Minimal proposal: retain the Introduction question and Results demonstration. If one deletion is desired, delete only the Discussion sentence “A lower RMSE likewise need not imply better test calibration.” It repeats the Introduction and the quantitative §4.3 argument. Retain the Conclusion's central finding. **NO CHANGE is also reasonable** because this is the principal message.

### R2. Oracle deterioration excludes a sole high-dimensional explanation — OPTIONAL

Exact passages:

- `sections/01_introduction.tex:12`: “Oracle-GMM also deteriorates under weaker relevance, so high-dimensional nuisance estimation is not the sole explanation.”
- `sections/04_results.tex:22`: “Deterioration of Oracle-GMM, which knows the designated relevant control set, shows that high-dimensional nuisance estimation is not the sole source of the loss of accuracy.”
- `sections/05_discussion.tex:6`: “Oracle-GMM also loses accuracy and numerical localization despite knowing the designated relevant controls. High-dimensional nuisance estimation is therefore not the sole explanation for deterioration.”
- `sections/06_conclusion.tex:2`: “Oracle-GMM also deteriorates under weaker relevance, so high-dimensional nuisance estimation cannot be the sole explanation.”

Minimal proposal: delete the final quoted Conclusion sentence only, leaving the empirical demonstration and Discussion interpretation. This is optional, not a scientific correction. The inference is already limited; do not replace it with a claim about the causal size of nuisance-estimation effects.

### R3. Implementation comparison does not isolate regularization — NO CHANGE, with optional local compression

Exact passages:

- `sections/01_introduction.tex:12`: “Differences in nuisance dimension, residualization and computational details prevent attributing this comparison to regularization alone.”
- `sections/04_results.tex:26`: “Oracle is a benchmark with knowledge of the relevant controls, not a guaranteed finite-sample winner; moreover, the estimators differ in residualisation and other implementation details as well as regularisation.”
- `sections/05_discussion.tex:6`: “Their comparison does not identify a regularization mechanism or establish uniform superiority.”
- `sections/06_conclusion.tex:4`: “Implementation-level RMSE advantages have documented exceptions and do not isolate regularization.”

Recommendation: retain these local safeguards because ranking statements otherwise invite precisely the interpretation the study cannot support. If compression is specifically wanted, replace the Discussion's preceding sentence “The preserved DML-IVQR implementation often has lower RMSE than preserved Full-GMM, with exceptions, but the procedures differ in nuisance dimension, regularization and residualization.” with “The implementation-level RMSE comparisons have exceptions.” Keep the following mechanism/superiority sentence.

### R4. Repeated full limitation inventory — RECOMMENDED only as optional compression of the Conclusion

Exact passages:

- `sections/01_introduction.tex:14`: “The findings concern one DGP family and historical implementations with a non-finite mixed residual density, density proxies, differing residualization, same-sample fits and fresh penalty draws.”
- `sections/05_discussion.tex:8`: “Here the mixed residual density is non-finite (Appendix~\ref{app:density-divergence}), while the implementations use density proxies, differing residualization, same-sample nuisance fits and fresh pivotal penalties. Their nominal chi-square validity remains unestablished.”
- `sections/06_conclusion.tex:6`: “The non-finite mixed density, proxy/residualization choices, same-sample fitting and penalty randomness limit that link; selected numerical audits additionally show rank and decision sensitivity within a specified panel.”

Minimal proposal: replace only the last quotation with “The implementation and selected-case numerical limitations summarized in the Discussion restrict that link.” Retain the Conclusion's opening sentence disclaiming validated inference and the following sentences limiting numerical certificates and grid geometry. The full inventory remains in the Introduction, Framework, Discussion and Appendix D. Preserving the current version is also defensible; there is no clearly off-topic scientific appendix to remove.

## Key-term consistency and scientific boundaries

| Distinction | Current evidence and conclusion | Disposition |
|---|---|---|
| Coverage / direct-at-truth acceptance | §3.2 and Appendix C explicitly define the historical Coverage field as a direct test at unrounded truth. Off-grid truths and fresh DML draws prevent interpreting it as stored-grid membership. §4 shorthand and the figure caption are understandable with their notes. | E1 recommended; preserve equations and artwork. No newly discovered coverage-definition error. |
| Accepted measure / confidence-set length | §3.2 correctly defines trapezoidal quadrature, not finite-set Lebesgue measure, outer span or unrestricted region length. Figures and Table 2 disclaim unrestricted length. | M1 fixes the actual contradictory local assertion. |
| Nominal chi-square / validated inference | §2.2, Discussion and Conclusion consistently deny established validity for these executable procedures. Near-95% truth acceptance is not evidence of a valid law or useful power. | NO CHANGE to the conditional theory or limitations. Do not call the study a validation of weak-IV-robust inference. |
| Implementation comparison / regularization effect | The procedures differ in dimension, intercept handling, residualization, proxies and computation. Repeated caveats correctly prohibit a pure regularization attribution. | NO CHANGE to rankings/results; E2 concerns local wording only. |
| Weak relevance / non-identification | Kappa orders designed relevance. First-stage F has no universal IVQR threshold; minimum simulated kappa is positive. | NO CHANGE. No claim that all low-F designs are formally unidentified. |
| Numerical certificates / historical decision accuracy | Five of 24 selected candidate problems differ between policies. This selected fraction is not an error rate for the full experiment, and exact fixed-objective work does not certify archived fits. | NO CHANGE. Do not extrapolate the fraction or replace historical results. |
| Non-finite density / cause of distortions | The conditional Gaussian tail argument supports divergence of the treatment-mixed density. It does not imply every conditional-on-treatment density diverges, prove the chi-square law fails by itself, or identify the cause of each rejection. | NO CHANGE: these distinctions are already explicit. |

After considering the existing caveats, M1 remains scientifically misleading; M3 remains too categorical locally. M2 is a factual provenance defect. Other phrases such as “coverage”, “power”, “oracle” and “orthogonal score” are not automatically misleading when used with the manuscript's explicit definitions and reference-versus-implementation distinction. Do not manufacture a need for new theory by ignoring those caveats.

## LSSP fit and inherited JSCS requirements

Sources consulted on 11 November 2026:

1. [Official LSSP journal overview](https://www.tandfonline.com/journals/lssp20), available through indexed publisher text. It explicitly includes comprehensive reproducible simulation comparisons and identifies single-anonymous review. The live about page returned HTTP 403, so this is not a claim of successful full live-page inspection.
2. [Publisher-hosted LSSP instructions PDF](https://files.taylorandfrancis.com/lsspauth.pdf), three pages, successfully read. It lists a normal expectation of at most 25 double-spaced pages, an abstract below 200 words, a short running title, and named title-page information. The document contains visibly dated production directions and no verified current effective date; do not silently treat every historical specification as the live portal rule.
3. [Current LSSP instructions endpoint](https://www.tandfonline.com/action/authorSubmission?show=instructions&journalCode=lssp20), returned HTTP 403. Detailed current requirements therefore remain unverified.

### J1. Review model — MUST FIX in submission planning, NO CHANGE to the named manuscript

`journal_article/README.md`, “Submission blockers”, says: “The publisher's indexed journal information specifies double-anonymous review.” The historical `journal_validation/publication_review/SUBMISSION_GATE_REPORT.md:1` is headed “JSCS final submission gate”. These are JSCS records, not LSSP instructions. The official LSSP overview instead specifies single-anonymous review. Preserve historical reports as history; do not use them as the current submission checklist. The named manuscript and identifying evidence links are not disqualified by the old double-anonymity gate. Evidence accessibility and truthful availability statements still matter independently of anonymity. No need to create or publish an anonymous repository is established by this review.

### J2. Braced pre-abstract summary — OPTIONAL

`journal_article/main.tex:20`:

> `\noindent\textit{\{Monte Carlo simulation assesses instrument-relevance sensitivity in high-dimensional IVQR.\}}\par\medskip`

This appears as a braced italic sentence above the abstract on p.1. It is consistent with prior submission-oriented presentation, but no verified LSSP requirement for this element was found. It also duplicates the title/abstract. Proposed minimal change if desired: remove this line only. Do not label it prohibited or definitively JSCS-mandated without evidence. This is the only clearly dispensable front-matter repetition; it does not justify shortening scientific content.

### J3. Abstract and total length — unresolved journal-compliance gate, NO CHANGE under author instructions

The available publisher PDF's abstract and page expectations may conflict with the protected abstract and present layout. The source abstract has 202 whitespace-delimited tokens including TeX/math tokens; this is a screening count, not the journal's definitive rendered-word count. The current document has 34 pages with 17 pages of inline supplementary material and is not double-spaced. Thus neither “34 exceeds 25, cut nine pages” nor “only 17 main pages, certainly compliant” is justified.

Before submission, establish the applicable current abstract limit, page-count basis and supplement treatment, or obtain an exception if necessary. **Do not edit the abstract or cut appendices to satisfy an unverified historical rule.** Preserve all content in this review. A compliance conflict requires an explicit later author decision; it is not permission to rewrite the protected abstract.

### J4. Named front matter and inline supplement heading — OPTIONAL / verify current requirements

`main.tex:37` prints “Online supplementary material”, followed at line 38 by:

> They are included here to keep all cross-references resolvable in a single review PDF.

This does not remove them from the named document; they are visibly inline on pp.18–34. If their final delivery remains inline, “Supplementary appendices” is a clearer heading. Do not split or delete them during this audit. The current author block supplies names, institution, ORCIDs and correspondence email. The older LSSP PDF also requests a correspondence address and short running title; these are formatting checks to verify against current instructions, not scientific defects. Do not infer that the existing one-sentence summary is a compliant short running title.

### J5. Journal scope — potentially suitable, not an acceptance prediction

LSSP considers substantive simulation comparisons, so a descriptive contribution is not ruled out merely because it lacks a new estimator. The controlled relevance construction and joint diagnostics should be the submission's focus. Preserved implementation peculiarities, one DGP family, limited replay and selected-case decision sensitivity constrain how comprehensive and reproducible the contribution can be claimed to be. The manuscript discloses those constraints; it should not be advertised as a general validation or a definitive ranking of IVQR methods. No invented empirical application, additional simulation or new theorem is needed for this audit.

## Final readiness assessment and next action

**Content verdict: suitable for consideration as a narrowly scoped descriptive sensitivity study after minimal local clarification; not scientifically certified as an inference-validation study.** Preserve the abstract, all results/equations/displays/appendices and substantially the current length. Address M1–M3 through a separately authorized prose-only pass. E1–E3 improve precision; R1–R4 are choices rather than a required shortening programme.

**Submission verdict: not ready unchanged.** In addition to the local content corrections, replace JSCS assumptions in the active submission plan with verified LSSP requirements and resolve the abstract/length uncertainty without overriding author instructions. Keep author AI attestations accurate and the archived/public/local-only distinction explicit. The unresolved historical freeze identifier and unavailable full stochastic replay must remain disclosed; this audit neither repairs nor conceals them.

This audit report is the only added Git-visible deliverable. A before/after SHA-256 inventory of 4,469 existing article/supporting files found changes only in the ignored job-local MiKTeX runtime configuration/logs refreshed by PDF extraction. All inventoried manuscript sources, PDFs, scientific assets, CSVs and research scripts remained byte-identical. Git status shows only this new report. No commit, push, release, upload or submission is performed.
