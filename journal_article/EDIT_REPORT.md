# Journal article edit report

Updated 15 October 2026. This report supersedes the earlier 58-page conversion report.

## Page cutoff and deletions

The pre-edit compiled journal article had 58 pages. PDF text extraction established that page 29 began exactly at D.4, "Numerics, failures, and reproduction workflow"; Appendix E, "Complete Frozen Numerical Results", began on page 30 and continued through page 58. The cutoff was identified before editing, using the journal PDF and its LaTeX auxiliary labels, rather than thesis page numbers.

Removed D.4 completely from supplementary/D_implementation.tex. Removed supplementary/E_full_results.tex and its input from main.tex. Removed the main-results cross-reference to E and the supplementary introduction's promise of E. Narrowed the framework's description of D to the details still present. Appendices A-C and D.1-D.3 remain because they preceded the specified cutoff. The revised PDF ends with D.3 on page 28; no empty page or obsolete E heading remains. Copied numerical table assets are not input merely to preserve their former appearance in the thesis.

## Authors

The title page now gives exactly these authors in order:

1. UMIDJON UMIRZAKOVICH KOSTAEV; ORCID 0009-0000-0205-5142; umidjonkostaev2025@gmail.com.
2. OLIMJON UMIDJON UGLI UMURZOKOV; ORCID 0009-0008-0090-7100; olimumurzokov022@gmail.com.

Both use one shared affiliation: Tashkent State University of Economics, Tashkent, Uzbekistan. ORCID identifiers and email addresses are visible and hyperlinked. No corresponding author, degrees, job titles, or additional affiliations were added. PDF author metadata includes both names.

The publisher-authored Taylor & Francis Interact example was consulted at https://www.overleaf.com/latex/templates/taylor-and-francis-latex-template-for-authors-interact-layout-plus-p-reference-style/jcttgbjrwpvq . Its superscript author/affiliation convention is followed. Downloading the official class from https://files.taylorandfrancis.com/interact_latex.zip returned HTTP 403; the Overleaf template ZIP endpoint returned 404. The existing article class and layout therefore remain, with a compatible author block. This is not a claim of compilation with the official Interact class or verified journal-specific submission compliance.

## Scientific preservation

The main article's scientific conclusions, equations, numerical tables, figures, citations, and qualifications are retained. Its result discussion still draws on the complete saved results, without claiming those complete tables are printed in the article. The deleted E tables repeat the archived frozen results; numerical datasets and simulation outputs were not deleted or recomputed. The only changes to scientific section sources are removal of the E cross-reference and narrowing the description of retained D content.

The main article retains the DGP and invariance explanation, estimator definitions, finite-grid and direct-evaluation distinctions, chi-square cutoff, covariance convention, first-minimizer rule, density-regularity caveat, proxy/intercept differences, same-sample fitting, fresh penalty randomness, empirical coverage distortions, and limits of estimator comparisons. A retains diagnostic failures and numerical-domain limits; D.1-D.3 retain environment/RNG qualifications, detailed penalty and residualization formulas, and conditional score algebra. Bibliography records and numerical entries were not modified.

## Build and verification

Recompiled with pdfLaTeX, Biber, and two further pdfLaTeX passes. LC_ALL=C and LANG=C avoid the host Perl locale warning. Final main.pdf: 28 pages. The final LaTeX log has no undefined citations/references, multiply defined labels, overfull boxes, or remaining rerun warnings. Biber reports no warnings or errors. Title-page rendering was visually inspected; PDF text checks verify all author details, order, and a single shared affiliation. All pages contain content, and deleted headings and the E reference are absent.

Checksums of 3,227 files in thesis/, simulation/, Empirical_work/, example/, and thesis_extension/ match the snapshot taken before these revisions: zero changed preserved files. The original Master's thesis, simulation code, and extension data remain unchanged. No simulations were run.

Current evidence: qa/revision_validation.json, qa/revision_preservation_sha256.json, qa/revision_build.log, qa/revision_pdfinfo.txt, qa/revision_title.png, and qa/article_text.txt. qa/original_pages_28_30.txt records the original cutoff. Other pre-existing QA images/logs and validation.json describe the earlier conversion and are historical, not validation of this revision.

## Modified deliverables

main.pdf; main.tex; sections/02_framework.tex; sections/04_results.tex; supplementary/D_implementation.tex; this report. supplementary/E_full_results.tex was deleted. The build also regenerated article-local auxiliary files. Added revision-specific QA scripts and evidence.
