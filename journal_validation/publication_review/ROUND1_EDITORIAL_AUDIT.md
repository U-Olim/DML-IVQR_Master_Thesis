# Stage 2I — Publication Readiness Audit, Round 1

**Target:** Journal of Statistical Computation and Simulation (JSCS)  
**Repository / branch:** `DML-IVQR_Master_Thesis` / `journal-validation`  
**Inspected research/manuscript commit:** `2ceec58a`  
**Review date:** 9 November 2026 (Asia/Tashkent)  
**Overall recommendation:** **MAJOR REVISION**

## 1. Decision and scope

The existing empirical contribution is potentially defensible as a controlled simulation study of a specified historical executable procedure. It is not evidence that this implementation satisfies an orthogonal-score inference theorem, and it is not an experiment isolating the effect of regularization. The paper should be submitted only after the material numerical limitations, contribution framing, evidence navigation and source/package inconsistencies below are addressed. Acceptance at JSCS remains uncertain: the main editorial risk is that weakening instruments and losing power will appear predictable unless the controlled design and the accuracy–calibration–informativeness disagreement are made the central contribution.

The review covers the abstract, all six main sections, bibliography, Appendices A–D, included table/figure sources, the empirical freeze, implementation wrappers and relevant closed numerical-validation reports. It does not reopen the research program. No simulations, hypothesis tests, estimation, result regeneration, manuscript edits or research-code edits were performed. The only authorized project-file change is this report.

Line numbers refer to the inspected working-tree sources. Quotations preserve manuscript wording or TeX fragments; omissions are marked where needed. Categories are A (contribution), B (methodology), C (results), D (writing), and E (journal/package readiness). Issues are ordered by estimated impact on acceptance; IDs are stable within this round. CRITICAL means submission-blocking disclosure or document-integrity risk, not a claim that the empirical study is worthless.

### Verification limits

- All current main-section and Appendix A–D LaTeX sources were read. Included numerical table entries and captions were inspected, alongside existing validation records. Existing QA records report consistency of the copied assets, but are historical records, not fresh validation of the current source state.
- A fresh PDF text extraction was attempted without writing an output file, but the installed MiKTeX utilities failed because they wanted to initialize an external configuration directory. No setup changes or installation were made. The stored `journal_article/qa/article_text.txt`, `revision_pdfinfo.txt` and `revision_title.png` were inspected instead. The latter records a 28-page revision. Older `final-contact-*.png` sheets depict the superseded 58-page version and were not treated as the current submission. A current PDF/source match is **unverified**.
- The current source author block visibly differs from the stored revision evidence; issue R1-003 does not depend on assuming that an old QA pass remains valid.
- Numerical values below are quotations or lookups of existing manuscript/report values. Aggregate comparisons such as 35/40 and 305/360 were not recomputed. No new uncertainty intervals or statistical tests were generated.
- Journal-specific instructions and scope pages returned HTTP 403. Their exact current requirements are **not verified**. Section 5 separates accessible publisher guidance from journal-specific matters requiring confirmation.

## 2. Ranked issue register

| Rank / ID | Severity | Categories | Main issue | Editing alone? |
|---|---|---|---|---|
| 1 / R1-001 | CRITICAL | B, C, E | Known rank/decision sensitivity is absent from manuscript disclosure | Disclosure yes; numerical invariance no |
| 2 / R1-002 | MAJOR | A, E | Incremental contribution needs a sharper scientific reason to publish | Yes; broad novelty cannot be guaranteed |
| 3 / R1-003 | CRITICAL | D, E | Current author source, metadata and stored revision evidence disagree | Requires author confirmation and document rebuild |
| 4 / R1-004 | MAJOR | A, B, C | Abstract/conclusion attribute benefits to regularization despite confounded comparisons | Yes, by narrowing attribution |
| 5 / R1-005 | MAJOR | B | No explicit boundary between cited reference theory and implementation-level validity | Yes for claim boundaries; no for validity proof |
| 6 / R1-006 | MAJOR | B, C | Finite-grid confidence-set definition and direct-test “coverage” are different objects | Yes, through precise definitions |
| 7 / R1-007 | MAJOR | C, E | Full-result claims lack a direct reader-facing evidence route | Yes, using existing tables and paths |
| 8 / R1-008 | MAJOR | E | Repository description is not a complete data/code availability statement | Wording yes; access/deposit verification also needed |
| 9 / R1-009 | MAJOR | B, C, E | Randomized test/profile and replication scope are not fully specified | Partly; lost RNG states cannot be recreated by prose |
| 10 / R1-010 | MAJOR | B | Important infinite-density assertion is stated without its short derivation | Yes, reuse the retained derivation |
| 11 / R1-011 | MAJOR | B, E | Mathematical instrument argmin is stronger than native adaptive finite computation | Yes, as an operational description |
| 12 / R1-012 | MAJOR | E | Submission declarations and corresponding-author designation are incomplete | Requires factual author input; no research |
| 13 / R1-013 | MINOR | E | Anonymity risk is real but the journal’s review model is unverified | Conditional package edit after confirmation |
| 14 / R1-014 | MINOR | C, D | Abstract omits the strongest quantitative result | Yes |
| 15 / R1-015 | MINOR | A, D | Broad weak-IV literature list crowds out the specific gap | Yes |
| 16 / R1-016 | MINOR | C, D | Results become an inventory of numbers and sequence counts | Yes |
| 17 / R1-017 | MINOR | D | Discussion and conclusion repeat results and caveats | Yes |
| 18 / R1-018 | MINOR | B, D | Ideal score algebra is duplicated across main text and appendix | Yes |
| 19 / R1-019 | MINOR | C | Average coverage across heterogeneous cells can look like overall calibration | Yes |
| 20 / R1-020 | MINOR | B, C, D | Grid quadrature language overstates accepted-component geometry | Yes |
| 21 / R1-021 | MINOR | E | Citation support is uneven; some claims need source-level confirmation | Yes for narrowing; verification may be needed |
| 22 / R1-022 | MINOR | D, E | README and QA claims describe superseded document states | Documentation edit; verification outside manuscript |
| 23 / R1-023 | MINOR | D, E | Presentation has not been checked at actual submission size/style | Presentation verification needed; no new evidence |
| 24 / R1-024 | MINOR | B, D | A few nuisance/statistic symbols are incompletely defined | Yes |

### R1-001 — Material numerical sensitivity is not disclosed

- **Severity / category:** CRITICAL / B, C, E.
- **Manuscript location:** `journal_article/sections/04_results.tex:48–50`; `journal_article/supplementary/C_coverage_audit.tex:9–11`; `journal_article/supplementary/D_implementation.tex:8–10`; `journal_article/sections/05_discussion.tex:13`.
- **Quotation:** “The audit rules out missing-value handling, nonfinite truth statistics, and reconstruction from rounded grid confidence sets as explanations for the observed undercoverage.” Also: “These checks rule out those numerical explanations for the reported coverage patterns.”
- **Weakness:** These statements are carefully limited to specific bookkeeping checks, but the manuscript omits later, material evidence that approximate residual signs and resulting decisions can change even when objective errors are small. `journal_validation/stage2g/full_path_validation/FULL_PATH_REPORT.md:129–131` records five A/C decision differences on a fixed 24-candidate panel and opposite full-path decisions for 12 selected near-optimal cases at both examined budgets. `journal_validation/stage2g/deterministic_implementation/DETERMINISTIC_IMPLEMENTATION_REPORT.md:61–97` explicitly distinguishes exact-objective equivalence from bitwise historical output. The article’s generic “implementation features” caveat does not communicate this finding.
- **Consequence:** A reader could reasonably mistake finite, nonmissing archived statistics for numerically invariant evaluations of the ideal optimization-defined statistic. A referee discovering the closed audit independently could regard the omission as selective disclosure.
- **Correction without new evidence:** Add a compact numerical-limitations paragraph and an appendix pointer: archived results are retained as outputs of a specified historical finite computation; later saved-panel audits show rank/decision sensitivity; certificates apply to stated objectives/inputs, not all historical outputs. Quote the existing panel counts only with their selected-panel denominator and policy definitions. Do not convert them into a failure probability, coverage correction, or mechanism estimate. Do not replace the frozen Monte Carlo results.
- **Editing alone?** **Yes for transparent disclosure and a narrower empirical claim. No for establishing solver invariance or correcting historical coverage.**

### R1-002 — The contribution is explicit but not yet compelling enough

- **Severity / category:** MAJOR / A, E.
- **Location:** `journal_article/sections/01_introduction.tex:8–10`; `journal_article/main.tex:3,18`; `journal_article/sections/06_conclusion.tex:2–4`.
- **Quotation:** “Our contribution is a controlled Monte Carlo extension of their design and preserved executable procedures.” “The extension introduces neither a new estimator nor a new inference theory.”
- **Weakness:** Honest positioning is a strength, but the main takeaway can still read as the familiar observation that weaker instruments reduce power. The paper does not sharply distinguish its more useful result: preserving the treatment/endogeneity distribution while showing that improved point accuracy, nominal-looking truth acceptance and useful exclusion of alternatives can disagree sharply. The generic title does not signal that distinction or the historical-implementation scope.
- **Consequence:** Desk-rejection risk on significance and incremental novelty, even if the reported patterns are correct.
- **Correction:** End the introduction with a short contribution paragraph that separates (i) the controlled relevance construction, (ii) joint assessment of accuracy, calibration and grid informativeness, and (iii) the limits of the executable-procedure interpretation. Contrast these with the predecessor’s fixed-design point-performance/profile comparisons. Consider a title emphasizing controlled relevance sensitivity of a preserved high-dimensional IVQR procedure. Do not claim to be the first weak-IV simulation study generally.
- **External support / limit:** The authors’ February 2021 preprint, Sections 3.1–3.2, reports baseline point-performance and illustrative profiles; its Section 2.3 also discusses same-sample sparsity-based estimation. This supports a specific comparison, not an exhaustive novelty claim. [Chen–Huang–Tien preprint](https://arxiv.org/html/1909.12592).
- **Editing alone?** **Yes for presenting the existing contribution; no edit can guarantee journal-level novelty or replace a comprehensive literature verification.**

### R1-003 — Current source is not a coherent submission master

- **Severity / category:** CRITICAL / D, E.
- **Location:** `journal_article/main.tex:4–14`; supporting `journal_article/EDIT_REPORT.md:13–18,30–34` and `journal_article/qa/revision_validation.json:2–6`.
- **Quotation:** Source line 9 ends `KOSTAEV\textsuperscript\\`; source line 6 places UMURZOKOV first, while line 14’s `pdfauthor` starts with KOSTAEV. The source comment says “Shared affiliation,” but lines 5–12 print no affiliation.
- **Weakness:** The second superscript lacks its intended braced affiliation argument; author order in visible source and PDF metadata differs; the shared affiliation is absent from the current block. The stored title image/text and edit report show a different order and a shared affiliation. Historical “all_author_details_present” and “clean_latex_log” records do not validate this current source. Fresh PDF/source matching remains unverified.
- **Consequence:** Authorship/version confusion and malformed output are submission blockers, independent of scientific merit. The malformed command may consume following markup; this review did not compile it and does not assert a tested build failure.
- **Correction:** Obtain the intended author order, affiliations and corresponding author from the authors; make one consistent title block and metadata; rebuild only the document and inspect the resulting title/PDF against source. Do not infer that an old order is authoritative or silently change authorship.
- **Editing alone?** **Source edits can repair markup, but author confirmation and document compilation/inspection are also required.** No new research is needed.

### R1-004 — Residual causal attribution to regularization is inconsistent with the comparison

- **Severity / category:** MAJOR / A, B, C.
- **Location:** `journal_article/main.tex:18`; `journal_article/sections/01_introduction.tex:10`; `journal_article/sections/06_conclusion.tex:4`; contrast `journal_article/sections/02_framework.tex:133` and `journal_article/sections/05_discussion.tex:7`.
- **Quotation:** “These results separate the benefits of nuisance estimation from the information required to distinguish competing structural effects.” “Regularized nuisance estimation often improves point accuracy relative to Full-GMM, with exceptions.”
- **Weakness:** Oracle/DML/Full differ in more than regularization. The body recognizes that residualization and nuisance dimensions also differ, yet the summary language assigns observed gains to regularized nuisance estimation and suggests a separation the design cannot identify. The last sentence of the abstract similarly shifts from implementation-specific evidence to an unqualified benefit of orthogonalization.
- **Consequence:** Readers can interpret a comparison of bundled procedures as a causal mechanism result or validation of the implemented orthogonality.
- **Correction:** Use “The preserved DML-IVQR implementation often has lower RMSE than the preserved Full-GMM implementation.” Replace “separate the benefits” with the narrower result that the oracle’s deterioration shows high-dimensional nuisance estimation is not the sole explanation. Retain orthogonality’s theoretical motivation with an explicit reference-theory qualifier.
- **Editing alone?** **Yes.** Identifying the separate effect of regularization would require evidence outside this closed study and should not be claimed.

### R1-005 — Cite reference theory without suggesting an implementation-level theorem

- **Severity / category:** MAJOR / B.
- **Location:** `journal_article/sections/02_framework.tex:123–125,168–178`; `journal_article/supplementary/D_implementation.tex:152–156,244`.
- **Quotation:** “The corresponding theoretical candidate tests can accommodate weak identification under their regularity conditions.” “These are properties of the ideal construction under its conditions, rather than guarantees for every executable implementation.”
- **Weakness:** These qualifications are good, but the manuscript still presents a substantial ideal construction immediately before the executable statistic without one concise statement that no theorem is established for the implemented proxy, transformed ordinary intercept and same-sample generated score. “Corresponding” can suggest a demonstrated transfer. There is no complete assumption mapping, nuisance-rate argument, generated-score limit or covariance-consistency result for this implementation.
- **Consequence:** A referee may require a theorem the paper neither proves nor intends to prove; the reader can overread the chi-square cutoff as validated robustness.
- **Correction:** Add a clear boundary statement: the ideal score supplies motivation; the archived procedures use a nominal reference cutoff whose validity under this DGP and implementation is not established here. Distinguish finite density-weighted moments, nuisance adaptivity, score limit/covariance and weak-identification uniformity as unverified requirements. Do not write a new theorem or characterize absence of cross-fitting alone as proof of invalidity. The predecessor itself discusses same-sample sparsity-based adaptivity; applicable rate conditions still require verification. [Chen–Huang–Tien, Section 2.3](https://arxiv.org/html/1909.12592).
- **Editing alone?** **Yes for framing and removing implied guarantees; no for establishing the missing theory.**

### R1-006 — Formal confidence-set coverage and reported direct-test acceptance are different

- **Severity / category:** MAJOR / B, C.
- **Location:** `journal_article/sections/02_framework.tex:159–178`; `journal_article/sections/03_design.tex:132–163,170–180`; `journal_article/supplementary/C_coverage_audit.tex:7,24`.
- **Quotation:** `\mathcal C_{e,1-\gamma}(\tau)=\{a\in\mathcal A:W_{e,n}(a)\leq c_{1-\gamma,d_z}\}` and “Reported coverage is the repeated-sample acceptance frequency of the direct test, rather than membership reconstructed from a stored grid profile.”
- **Weakness:** The framework identifies the Monte Carlo candidate set with a finite grid. Most true quantile effects do not belong to that grid; literal membership coverage of that finite set is therefore not the direct-test rate. For DML, separate pivotal draws make even an on-grid direct evaluation a different randomized computation. The prose discloses this, but the formal set definition and the label “coverage” remain insufficiently reconciled.
- **Consequence:** A mathematical referee can identify an estimand mismatch between the formally defined confidence set and the plotted coverage.
- **Correction:** Define the direct candidate-test acceptance probability separately and label it “direct-at-truth acceptance (test-inversion coverage diagnostic).” Define the stored finite-grid accepted set separately. Explain that unrestricted inversion motivates the terminology but was not computed, and do not claim that direct testing measures coverage of the stored randomized grid set. No new profile or random-number convention is needed.
- **Editing alone?** **Yes.** Actual coverage/geometry of a newly specified continuous randomized procedure cannot be established by renaming existing results.

### R1-007 — Full-result claims need explicit evidence navigation

- **Severity / category:** MAJOR / C, E.
- **Location:** `journal_article/sections/04_results.tex:17,21–27,61,65,76`; `journal_article/main.tex:32,39–42`; `journal_article/supplementary/D_implementation.tex:10`.
- **Quotation:** “The comparisons in this subsection also use the complete saved results for both sample sizes and all five quantiles.” “Across the 40 matched ... designs, DML has lower RMSE than Full-GMM in 35”.
- **Weakness:** The article prints a representative 36-row main table, but makes many all-design counts. The full tables remain as assets, yet are not included in the current manuscript; the October edit report explicitly removed Appendix E. The reader is not directed to exact archived files/tables supporting those counts. Their absence from the PDF is not evidence that the counts are wrong.
- **Consequence:** Reduced inspectability and concern about selective emphasis, especially for unplotted quantiles and estimator exceptions.
- **Correction:** Provide a compact evidence map in Appendix D or a separate existing-results supplement. Point to `thesis_extension/final/output/n500/summary.csv`, `.../n1000/summary.csv`, the corresponding `power_summary.csv` files, and the already existing full-table assets under `journal_article/tables/generated/`. The map should identify which claim uses which frozen output. Include existing tables selectively or supply them separately; do not regenerate statistics or restore 29 pages by default.
- **Editing alone?** **Yes, using existing artifacts and precise references.** Fresh recomputation of all counts is outside this round and has not been implied.

### R1-008 — Data/code availability is descriptive rather than operational

- **Severity / category:** MAJOR / E.
- **Location:** `journal_article/supplementary/D_implementation.tex:6–10`; `journal_article/main.tex:26–28`.
- **Quotation:** “The computational archive is the project repository ... This reference identifies the archived workflow”.
- **Weakness:** A repository root and historical commit do not tell readers exactly which frozen data produce each table, what can be reproduced without old software, what is unavailable, or whether archived package/environment dependencies are accessible. There is no separately headed data availability statement before references. Main historical summaries/results and the coverage-audit table are Git-tracked; this review does not allege they are missing. Stage 2H raw runs are local/Git-ignored and must not be promised as publicly available without checking access.
- **Consequence:** Reproducibility and submission-transparency concerns; references to later audit evidence become hard to follow.
- **Correction:** Write a factual data-and-code statement that separates frozen result inspection from historical stochastic rerunning and later numerical audit reproduction, with commit/path identifiers and actual access conditions. Verify any public release link before claiming availability. A repository DOI is useful if one already exists; do not invent one or assert that JSCS requires a DOI.
- **Publisher guidance:** Accessible Taylor & Francis guidance describes a headed data availability statement before references for journals with a data-sharing policy. The exact JSCS policy tier was not verified. [Publisher guidance](https://authorservices.taylorandfrancis.com/data-sharing/share-your-data/data-availability-statements/).
- **Editing alone?** **Partly.** Statement wording is editorial; verifying access or depositing existing files is packaging work, not new research, and was not performed here.

### R1-009 — Specify the randomized computational object and reproducibility limits

- **Severity / category:** MAJOR / B, C, E.
- **Location:** `journal_article/sections/02_framework.tex:133`; `journal_article/sections/03_design.tex:118,163`; `journal_article/supplementary/D_implementation.tex:8,13`.
- **Quotation:** “Fresh pivotal draws are generated at each penalty call” and “Worker-specific RNG streams are not explicitly initialized ... the parent seed alone does not establish exact regeneration of every penalty draw.”
- **Weakness:** The disclosure is candid, but a reader still needs to know that the reported estimator includes algorithmic randomness, that nuisance fits/penalties are candidate-specific, and that common primitive samples do not make pivotal draws common across procedures/evaluations. Exact historical penalty replay and independence of worker draws should not be presumed from seed 675. The manuscript’s MCSE formula is a conventional descriptive calculation, not a verification of worker-stream independence.
- **Consequence:** Ambiguous interpretation of “same sample,” repeatability and grid-profile comparisons. Removing the RNG caveat would worsen the problem.
- **Correction:** Add an operational sequence for one replication and distinguish observed-data reuse, fresh candidate penalty draws and direct-truth reruns. State explicitly what archived files permit deterministic inspection and what cannot be reconstructed exactly from a parent seed. Do not retroactively invent stream assignments or claim bitwise replay of historical main results.
- **Editing alone?** **Yes for specification; no for recovering unrecorded RNG states or proving historical stream independence.**

### R1-010 — The density pathology deserves a self-contained proof sketch

- **Severity / category:** MAJOR / B.
- **Location:** `journal_article/sections/02_framework.tex:125`; `journal_article/sections/05_discussion.tex:13`; supporting `journal_validation/stage2h/readiness/BOUNDED_DGP_DERIVATION.md:105–114`.
- **Quotation:** “The density at zero contains a term proportional to ... which is not finite.”
- **Weakness:** This is a major reason the reference theory is not being validated, but the journal article gives neither the short divergence argument nor a precise source pointer. The phrase “contains a term proportional” also leaves the conditioning and integration step less explicit than a referee is likely to accept for a result this consequential.
- **Consequence:** The paper’s central theoretical qualification may look asserted rather than demonstrated, or be mistaken for a conjecture.
- **Correction:** Reuse the already retained argument: state the mixed residual-density identity, conditioning set, conditional normal variance and inverse-Phi tail comparison. The existing derivation establishes the relevant variance greater than one and the divergent negative-tail integral. Put the short existing calculation in Appendix D and cite it from the framework. This is presentation of retained analytical evidence, not authorization for new theorem development. Keep the distinction from a density conditional on realized treatment.
- **Editing alone?** **Yes, by incorporating the existing derivation accurately.** This does not make the original DGP regular or validate the proxy.

### R1-011 — Native finite instrument fitting is not fully characterized by an argmin

- **Severity / category:** MAJOR / B, E.
- **Location:** `journal_article/supplementary/D_implementation.tex:15,78–95`; `journal_article/sections/02_framework.tex:131`.
- **Quotation:** “using default iterative heteroskedastic loadings”; the display defines the instrument coefficients by `\operatorname*{arg\,min}`.
- **Weakness:** The mathematical objective is useful, but historical adaptive penalties, shooting termination and finite returned coefficients are collapsed into an exact argmin. Closed numerical reports explicitly distinguish the last-used penalty, reported next penalty and refined final-objective solution. “Default” is only meaningful with the pinned package version and routine pathway. Numerical precision is particularly material because ranks and penalties feed the final score.
- **Consequence:** The executable estimator is underspecified and can be mistaken for the certified final-objective algorithm developed later.
- **Correction:** Label displays as objective definitions and separately describe the historical finite algorithm that approximates them. Identify `quantreg::rq(..., method="lasso")`, `hdm::rlasso(..., post=FALSE)`, package versions, the retained rank rule and where archived settings/termination details reside. Summarize the final-used/adaptive-trajectory distinction from the existing contract. Do not silently replace historical fits with certified optima.
- **Editing alone?** **Yes for disclosure and operational specification; no for proving exact attainment by historical outputs.**

### R1-012 — Complete factual submission declarations

- **Severity / category:** MAJOR / E.
- **Location:** `journal_article/main.tex:4–14,26–28`.
- **Quotation:** “no corresponding author” (source comment); the main file goes from the conclusion input to `\printbibliography` with no declaration inputs.
- **Weakness:** The current document has no explicit funding, competing-interest or contribution declarations, and no designated corresponding author. The authors’ actual circumstances cannot be inferred from missing text. This is distinct from the malformed author block in R1-003.
- **Consequence:** Avoidable submission queries and incomplete publication metadata. Whether each declaration must appear in the manuscript or submission form is journal-specific and unverified.
- **Correction:** Obtain accurate statements and the corresponding-author designation; place them as required by confirmed journal instructions. Do not automatically write “no funding” or “no conflicts.” Confirm any applicable assistance/disclosure policy and report actual use, without inventing a requirement.
- **Editing alone?** **Factual author input and editorial packaging suffice; no research evidence is needed.**

### R1-013 — Conditional anonymity risks need a submission-version decision

- **Severity / category:** MINOR / E; potentially submission-blocking if double-anonymous review is confirmed.
- **Location:** `journal_article/main.tex:5–14`; `journal_article/supplementary/D_implementation.tex:6`.
- **Quotation:** The named author block and repository URL `https://github.com/U-Olim/DML-IVQR_Master_Thesis`.
- **Weakness:** Names, emails, ORCIDs, PDF metadata and the repository identify the authors. That is normal for a named manuscript, but incompatible with a blind review file if such a file is required. The journal’s current anonymity model was not verified.
- **Consequence:** Possible administrative return; no present basis to assert a journal-rule violation.
- **Correction:** Confirm the review model. If a blind file is required, prepare separate title-page and anonymized review materials, including metadata and a suitable anonymous evidence-access route. Preserve the named master and data provenance.
- **Publisher guidance:** Taylor & Francis explicitly notes identity risks from data links under double-anonymous review. [Data-sharing FAQ](https://authorservices.taylorandfrancis.com/frequently-asked-questions/data-sharing-faq/).
- **Editing alone?** **Conditional document/package preparation; no research.**

### R1-014 — Abstract lacks a quantitative anchor

- **Severity / category:** MINOR / C, D.
- **Location:** `journal_article/main.tex:18`; supporting `journal_article/sections/04_results.tex:34,78`.
- **Quotation:** “substantial undercoverage also occurs in several strong-relevance cells.”
- **Weakness:** The abstract devotes substantial space to setup and general qualifications, but none to a concrete magnitude. Its most arresting result is weakened by generic wording.
- **Consequence:** The study can sound like a predictable weak-IV exercise rather than an informative computational assessment.
- **Correction:** Replace one setup/detail sentence with an existing quantitative contrast. For example, identify the reported DML upper-tail coverage of 0.498 at n=1000 and strongest relevance, or the median weak-relevance combination of coverage 0.942, accepted measure 3.900 and power 0.094 at the stated false candidate. Include the design labels needed to prevent generalization; do not add all examples. Keep a concise implementation-scope qualification.
- **Editing alone?** **Yes.**

### R1-015 — Focus the introduction’s literature review

- **Severity / category:** MINOR / A, D.
- **Location:** `journal_article/sections/01_introduction.tex:4–8`.
- **Quotation:** “Related developments in the broader IV literature include the direct structural tests ... weak-IV approximations ... weak-identification-robust GMM ... pivotal and conditional likelihood-ratio procedures”.
- **Weakness:** The citation catalogue is broader than the design comparison and delays the precise empirical gap. It does not explain which of those distinctions the simulation actually evaluates.
- **Consequence:** A generic literature-survey tone weakens contribution visibility and econometrics-specific detail can obscure the simulation question for a statistical-computation readership.
- **Correction:** Retain the few references needed to distinguish moment validity, identification and candidate testing; compress the historical list into a short contextual sentence. Move the controlled-design gap and the existing quantitative motivation earlier. Do not remove citations merely because findings are inconvenient.
- **Editing alone?** **Yes.**

### R1-016 — Reduce numerical inventory while preserving exceptions

- **Severity / category:** MINOR / C, D.
- **Location:** `journal_article/sections/04_results.tex:21–29,38–40,59–65,76–84`.
- **Quotation:** “Across all five quantiles and six nonzero deviations, n=1000 has higher rejection probability in 305 of 360 matched cells, the same probability in 25, and a lower probability in 30.”
- **Weakness:** Several paragraphs combine sequence counts, multiple examples, exceptions and repeated qualifications. The claims are generally cautious, but their density makes the main findings harder to retain and puts weight on counts whose detailed evidence is outside the PDF (R1-007).
- **Consequence:** Reviewer fatigue and weak results-to-discussion transitions; small descriptive reversals can receive disproportionate space.
- **Correction:** Give each subsection one leading finding, one representative magnitude and the scientifically relevant exception. Move secondary exact sequence counts into an existing-results evidence map or compact supplement. Preserve strong-relevance undercoverage, DML reversals, sample-size coverage deterioration and signed power asymmetry.
- **Editing alone?** **Yes.**

### R1-017 — Discussion and conclusion repeat rather than sharpen

- **Severity / category:** MINOR / D.
- **Location:** `journal_article/sections/05_discussion.tex:5–17`; `journal_article/sections/06_conclusion.tex:2–6`.
- **Quotation:** “Accuracy, calibration, power, and informativeness measure different features of the procedure” and “Coverage, however, is distinct from accuracy and informativeness”.
- **Weakness:** The discussion repeats counts, estimator rankings, tail signs and limitations already stated in the results/framework. The conclusion repeats the same conceptual distinctions and another future-experiment list.
- **Consequence:** Important qualifications become boilerplate and the final scientific message loses force.
- **Correction:** Organize the discussion around interpretation, what remains unexplained, and what a practitioner should report. Consolidate limitations in one explicit scope paragraph, including the numerical issue. Let the conclusion contain the controlled-design contribution, the key empirical disagreement, and the bounded implication. Describe future research as unresolved scope, not a requirement to reopen the closed project.
- **Editing alone?** **Yes.** A meaningful shortening is possible without deleting scientific information.

### R1-018 — Ideal algebra occupies space disproportionate to its role

- **Severity / category:** MINOR / B, D.
- **Location:** `journal_article/sections/02_framework.tex:35–123`; `journal_article/supplementary/D_implementation.tex:154–244`.
- **Quotation:** “Appendix ... gives the algebra.” The appendix then restates the nuisance vector, M/J definitions and derivative cancellation.
- **Weakness:** Main text and appendix duplicate much of an ideal construction whose regularity is explicitly not established for this DGP. The operational estimator remains more important to interpreting the simulation.
- **Consequence:** The paper can appear to present a theoretical contribution while its actual empirical contribution is less prominent; unnecessary equation count increases length.
- **Correction:** Keep a compact ideal-score definition and the condition/implementation boundary in the main text. Retain derivative algebra once in the appendix, alongside the short retained density calculation. Prioritize a concise operational algorithm in the framework. Preserve all differences between ideal and implemented residualization.
- **Editing alone?** **Yes.**

### R1-019 — Cross-cell average coverage needs a descriptive label

- **Severity / category:** MINOR / C.
- **Location:** `journal_article/sections/04_results.tex:40`.
- **Quotation:** “Averaged over estimators, quantiles, and sample sizes, coverage rises from 0.798 ... to ... 0.944”.
- **Weakness:** The average combines different tests and designs. It can mask opposite calibration errors and be read as an aggregate validity measure, although subsequent cell examples and caveats are appropriate.
- **Consequence:** An otherwise careful size discussion acquires an unnecessary pooled-calibration impression.
- **Correction:** Call it an equally weighted descriptive average of cell rates, explicitly not pooled observations or overall test calibration; or omit it and lead with the existing cell-level patterns. Preserve the nonmonotonicity and undercoverage examples. No new averaging is requested.
- **Editing alone?** **Yes.**

### R1-020 — Quadrature does not identify accepted components

- **Severity / category:** MINOR / B, C, D.
- **Location:** `journal_article/sections/03_design.tex:182–189`; `journal_article/supplementary/A_numerical_domain.tex:16–18`.
- **Quotation:** “the calculation totals separated accepted components without solving for exact critical-value crossings.”
- **Weakness:** The defined trapezoidal sum is a quadrature summary of binary grid decisions. It neither identifies continuous components nor measures their exact lengths. On a finite set, ordinary Lebesgue length is zero; nonzero quadrature requires an interpolation convention. Other manuscript sentences properly qualify the finite grid, but this phrase implies more geometry than was computed.
- **Consequence:** Terminological ambiguity in a central informativeness measure.
- **Correction:** Say “a trapezoidal summary of grid acceptance, allowing multiple accepted grid runs, without locating continuous boundaries.” Keep the exact formula and current values. Avoid describing disconnected continuous components as established. Do not rename the measure an unrestricted confidence-interval length.
- **Editing alone?** **Yes.**

### R1-021 — Narrow unsupported citation glosses and verify bibliographic relevance

- **Severity / category:** MINOR / E, B.
- **Location:** `journal_article/sections/01_introduction.tex:2,6`; `journal_article/references.bib:89–97,175–206`.
- **Quotation:** “orthogonal moments for nonparametric IVQR with high-dimensional covariates” (Jin–Sun citation); the first IVQR sentence jointly cites Koenker–Bassett and Chernozhukov–Hansen.
- **Weakness:** The Jin–Sun metadata/title was corroborated by publisher search results, but its full text was inaccessible; the specific “nonparametric” characterization remains unverified. The joint early citation can blur foundational ordinary quantile regression and instrumental quantile identification. Numerical versions of QR results and historical penalty conventions also need clearly separated attribution.
- **Consequence:** A specialist reviewer may question precision of literature positioning. No fabricated or definitely erroneous reference was established in this review.
- **Correction:** Verify the particular characterization from full text or use wording supported by the recorded title. Attribute ordinary quantile regression and IVQR separately where useful. Check cited versions/pages for the theoretical-versus-code distinction. Do not add references based on title similarity or pretend to have checked inaccessible proofs.
- **Source:** [Jin–Sun publisher record](https://www.sciencedirect.com/science/article/pii/S016517652500206X); full-text claims were not verified.
- **Editing alone?** **Yes for narrowing prose; full-source verification is also needed for stronger claims.**

### R1-022 — Superseded README and QA records invite reliance on stale evidence

- **Severity / category:** MINOR / D, E.
- **Location:** `journal_article/README.md:3,11–13`; relevant manuscript anchor `journal_article/main.tex:32,39–42`.
- **Quotation:** README: “online supplementary Appendices A–E” and “The author field is intentionally empty.” Manuscript: “Appendices A--D”.
- **Weakness:** The README conflicts with the current source and October edit report. `verify_article.py` writes a QA file despite being described as “read-only”; historical QA assertions concern particular revisions. The report’s current source inconsistency confirms the danger of treating them as timeless passes.
- **Consequence:** Reviewers or authors can open the wrong version, seek removed tables, or assume the source has been freshly checked.
- **Correction:** In a later authorized documentation pass, align the README with the actual submission master, label historical QA clearly, and distinguish non-research validation outputs from strictly no-write commands. No such documentation change was made in this round.
- **Editing alone?** **Documentation editing and current document verification; not a manuscript-only fix.**

### R1-023 — Confirm readability and style without inventing journal rules

- **Severity / category:** MINOR / D, E.
- **Location:** `journal_article/preamble.tex:1–15`; `journal_article/tables/table_main_performance.tex:2,6–12`; `journal_article/tables/figure_coverage_main.tex:3–7`; `journal_article/tables/figure_accepted_measure_main.tex:3–10`.
- **Quotation:** `\documentclass[11pt,a4paper]{article}`, `style=authoryear`; the main table uses `\small` and dense 36-row content; heatmap width is `0.72\textwidth`.
- **Weakness:** Standard article class and author-year references are not demonstrated journal violations. Nevertheless, dense tables, heatmap annotations and two stacked multi-panel plots need inspection at the actual submitted size. The stored accepted-measure graphic uses distinguishable markers/dashes, a presentation strength. Current PDF rendering and exact JSCS style compatibility remain unverified.
- **Consequence:** Possible readability or submission-style queries; premature template conversion could create avoidable errors.
- **Correction:** Confirm whether JSCS accepts format-free initial submissions, then inspect the current compiled PDF at ordinary reading size and in grayscale. Check figure notes, labels and table breaks; apply only confirmed style requirements. Do not regenerate statistical graphics or change data. Any later caption/layout edits must preserve the plotted values.
- **Editing alone?** **Presentation edits plus document inspection can address this; journal rules still need confirmation.**

### R1-024 — Complete local symbol definitions

- **Severity / category:** MINOR / B, D.
- **Location:** `journal_article/sections/02_framework.tex:35–45,83–102`; `journal_article/supplementary/D_implementation.tex:15,59–75`.
- **Quotation:** `g_\tau(W_i;a,\eta)` and `\widehat{\sigma}_{\epsilon}^{2}(a)`.
- **Weakness:** The observation vector W is not explicitly collected when the score first appears; W is also used for the scalar test statistic later. The residual variance supplied as a normal scale is described verbally and by the R call but lacks its exact n−1 sample formula. The population argmin is written as single-valued without an explicit uniqueness/selection qualification.
- **Consequence:** Avoidable ambiguity for readers auditing implementation equivalence, especially around the already unusual density convention.
- **Correction:** Define the observation vector once, distinguish its notation from the test statistic, give the existing sample-variance convention explicitly, and qualify the ideal nuisance selection under the stated reference conditions. Do not “correct” variance to standard deviation in code or equations describing the historical estimator.
- **Editing alone?** **Yes.**

## 3. Findings that should be preserved

The adversarial review does not support hiding or smoothing the inconvenient results. In particular:

- Preserve severe strong-relevance undercoverage, including the reported n=1000 upper-tail DML rate of 0.498; preserve deterioration of coverage with larger n even when RMSE improves.
- Preserve the distinction between empirical size at the true candidate and raw rejection at false candidates. The paper already says power is not size-adjusted and explicitly rejects interpreting it as an efficiency ranking.
- Preserve DML/Full ranking exceptions and the fact that Oracle is an infeasible benchmark, not a guaranteed winner.
- Preserve the ordinary transformed-intercept convention, variance-as-normal-scale proxy, absence of cross-fitting and fresh pivotal draws as descriptions of the actual archived implementation.
- Preserve the fixed-grid/domain limitations, the 99-profile expanded-domain exception, and the separation of the 100-replication diagnostic from the 500-replication main study.
- Preserve the explicit warning that first-stage F and partial R-squared are descriptive, not universal IVQR identification thresholds.
- Preserve the existing pointwise Monte Carlo qualification: the 53-below/1-above Wilson counts are descriptive and not simultaneous discoveries. The included coverage-audit table and prose agree on that total; no fresh interval calculation was performed.

### Consistency assessment

No direct numerical contradiction was found in the inspected main-table examples, calibration sequences, coverage-audit summary and quoted domain-expansion examples. The main text’s 53 below plus one above matches the appendix’s 54 exclusions. The power caption identifies the null point as size and the nonzero points as power; accepted-measure captions identify the finite-domain ceiling. These are substantive strengths.

That assessment is limited: no statistical assets were regenerated; existing QA passes describe prior states; not every all-design count was independently recomputed. The confirmed contradictions concern author/source/revision state and README scope, while R1-006 is a formal-object mismatch. Numerical sensitivity omitted from the manuscript is a disclosure gap, not proof that all printed aggregate results are false.

## 4. Claims That Cannot Be Repaired Through Editing Alone

These are boundaries on admissible claims, not a request to run new research. The closed study can remain publishable by declining to make them.

| Claim that cannot be established by prose | Why current evidence is insufficient | Permissible editorial treatment |
|---|---|---|
| The implemented score is Neyman-orthogonal and has valid nuisance-robust chi-square inference under this DGP | Ideal algebra does not transfer automatically to the proxy/intercept procedure; relevant rates, regularity and generated-score conditions are unestablished | Present ideal motivation and nominal-cutoff empirical behavior; expressly withhold a validity claim |
| This procedure is uniformly weak-identification robust | Finite positive relevance settings, descriptive first-stage diagnostics and acceptance frequencies do not prove uniform asymptotic validity | Describe sensitivity to designed relevance without claiming a weak-IV theorem |
| Regularization caused the DML/Full performance difference | Compared implementations bundle different nuisance dimensions, residualization and other choices | Attribute results to the whole preserved implementations |
| Historical main-study decisions are invariant to solver accuracy or residual-sign arithmetic | Closed saved-panel audits exhibit contrary examples; main Monte Carlo outputs were not replaced by a certified rerun | Disclose numerical-policy sensitivity; retain historical outputs and their narrower empirical interpretation |
| The original DGP satisfies finite mixed-density conditions, or bounded treatment validates the estimator’s theorem | Original density pathology remains; the partial bounded-treatment pilot does not prove remaining assumptions | Keep the pathology and explicitly separate numerical qualification, density calculations and statistical validity |
| Stage 2H is a completed repeatable validation study | Its report records incomplete evaluations and four unexecuted result replays | If mentioned, report it only as a partial diagnostic with its existing missing-decision limitations; do not silently substitute it for the main study |
| An exact historical main-study penalty trajectory can be regenerated from seed 675 | Worker-specific historical streams were not explicitly initialized; missing states cannot be recovered by prose | Explain deterministic inspection of frozen outputs separately from bitwise stochastic regeneration |
| Grid measures establish continuous interval length, global boundedness or non-identification | Three investigated domains and discrete candidates do not determine unrestricted geometry | Report finite-grid quadrature, boundary acceptance and numerical localization only |
| A single variance-scale, intercept, cross-fitting or solver change would restore calibration | Those mechanisms were not separately isolated by the reported main experiment; later numerical diagnostics have narrower scope | State unresolved mechanisms and avoid repair promises |
| DML’s RMSE or raw-power advantage is statistically significant across designs | Descriptive counts and single-rate MCSEs do not supply the required paired comparison evidence | Preserve numerical rankings as descriptive; do not add significance language |

Neither supplying missing author declarations nor resolving source/PDF consistency is a research problem. They require factual confirmation and document/package work. Likewise, checking journal instructions and making existing artifacts accessible do not require new statistical experiments.

## 5. Journal readiness: verified guidance versus unknown requirements

### Verified publisher-level guidance

1. Taylor & Francis directs authors to the particular journal’s Instructions for Authors for submission details. This does not establish the JSCS template or reference style. [Submission FAQ](https://authorservices.taylorandfrancis.com/frequently-asked-questions/making-your-submission-faq/).
2. Its accessible data-availability guidance describes a statement within the manuscript before references for journals with a data-sharing policy. The specific JSCS policy tier was not established. [Data availability statements](https://authorservices.taylorandfrancis.com/data-sharing/share-your-data/data-availability-statements/).
3. Its data-sharing FAQ explains the anonymity implications of repository links when a journal uses double-anonymous review. Whether JSCS currently uses that model remains unverified here. [Data-sharing FAQ](https://authorservices.taylorandfrancis.com/frequently-asked-questions/data-sharing-faq/).

These are paraphrases of publisher guidance, not quotations of accessible JSCS-specific rules.

### Journal-specific matters requiring confirmation

The official [JSCS instructions page](https://www.tandfonline.com/action/authorSubmission?show=instructions&journalCode=gscs20) and [journal scope page](https://www.tandfonline.com/journals/gscs20/about-this-journal) returned HTTP 403 during this review. Historical mirrors and third-party journal descriptions were not treated as current requirements. Confirm:

- Current aims/scope and the expected significance of simulation-only methodological assessments.
- Article category; any word/page limits; abstract/keyword limits; whether supplement pages count.
- Initial format-free policy, accepted LaTeX class and bibliography/reference conventions.
- Review anonymity, separate title page and treatment of repository links/metadata.
- Data/code-sharing policy, required declarations and supplementary-file organization.
- Figure resolution, file format, accessibility and submission-system upload requirements.
- Corresponding-author and contribution disclosures and any applicable assistance policies.

**Editorial scope judgment, not a verified journal rule:** A controlled assessment of numerical statistical procedures is a plausible subject for JSCS. The fit would be strengthened by making the simulation design and computational implementation the focus, rather than presenting the paper as a new econometric estimator or theorem. The absence of a new estimator is not, by itself, evidence of being out of scope. Conversely, topical fit alone does not establish sufficient originality.

## 6. Editing sequence under the closed-research constraint

1. Resolve R1-003’s submission-master and authorship facts before relying on any regenerated PDF. This audit does not authorize changing author order.
2. Address R1-001 and R1-004–R1-006 together: one consistent statement of the historical executable procedure, numerical sensitivity, reference-theory limits and direct-test versus grid-set objects.
3. Reframe the abstract/introduction around R1-002 and R1-014, using only already reported quantitative examples.
4. Add the evidence map, exact availability language and operational specification (R1-007–R1-011). Make later numerical evidence accessible if it is cited; do not imply local-only runs are in GitHub.
5. Consolidate repetition and reduce secondary numeric inventory while retaining reversals, undercoverage and uncertainty qualifications.
6. Obtain declarations and verify journal-specific instructions. Inspect a consistently built document and its submission package without rerunning research.

Do not silently change the estimator, cutoff, density proxy, ranks, penalties, Monte Carlo denominators, archived results or scientific conclusions. Do not replace the main historical simulations with the partial Stage 2H pilot. Do not infer restored calibration from numerical certificates. Any later packaging or source changes need their own authorized task; they were not made here.

## 7. Final recommendation

**MAJOR REVISION.** The controlled empirical comparison and its negative calibration/informativeness findings are worth preserving. The current submission is not ready because it omits material numerical limitations and has document-integrity and reproducibility-navigation problems. Those issues can largely be addressed by candid disclosure, precise definitions, stronger contribution framing and publication packaging using existing evidence. This recommendation does not promise acceptance or theoretical validation. If the intended claim remains a validated orthogonal, weak-instrument-robust implementation rather than an assessment of a historical executable procedure, that stronger claim is **not defensible with current evidence** and cannot be rescued by editing.
