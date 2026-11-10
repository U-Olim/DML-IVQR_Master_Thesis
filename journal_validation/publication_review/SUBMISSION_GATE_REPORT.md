# JSCS final submission gate

**Verification date:** 10 November 2026 (Asia/Tashkent)
**Repository / branch:** `DML-IVQR_Master_Thesis` / `journal-validation`
**HEAD:** `0f4188ca98a45ba03e1c889ac705ec936369862a`, plus the existing uncommitted final-package changes.
**Final recommendation: NOT READY.** Essential AI provenance/attestations, anonymous evidence access and live JSCS requirements are not all verified.

Only this report and `AI_USE_PROVENANCE.md` are created by this pass. Existing manuscript/PDF/ZIP/source/QA artifacts are read and hash-checked, not rebuilt or revised. No simulations, estimators, statistical tests, new scientific calculations, data regeneration, upload, repository/deposit creation, commit, push or submission are performed. PASS below means the specified local/policy condition passed, not blanket journal approval. FAIL means an identified requirement or evidence need is demonstrably incomplete; UNVERIFIED means the available record/access cannot establish it. Neither label is an accusation of misconduct.

## 1. AI provenance and proposed disclosure

The companion [AI_USE_PROVENANCE.md](AI_USE_PROVENANCE.md) records the inspected Git objects, report evidence and limits:

- The thesis prose existed at `e864dd27` (17 September 2026). The journal abstract, six main sections and Appendices A?D were all first tracked at `90509cbd` (22 October 2026), before the documented November editorial passes.
- This establishes pre-existing text, not human-only authorship. Initial drafting and the earlier thesis-to-journal conversion lack a full AI-use ledger. The internally dated 15 October edit report was first tracked on 22 October; report/commit dates are not proof of composition or tool use.
- Codex assistance in the observed work includes substantial redrafting of existing manuscript passages, newly drafting reproducibility/availability/evidence-map documentation from retained records, administrative reports and document-production utilities. Calling all this grammar-only would understate the record. Calling it proof that AI wrote the original manuscript's first draft would overstate the record.
- ChatGPT grammar/translation use and the research-code exclusion are author-declared. Exact tool/model versions, earlier sessions, original/translation pairs and human-review/terms attestations are not supplied.
- There is **no proven conflict** between the research-code exclusion and the observed final document-production helpers. Those helpers are AI-written code, so an unqualified ?AI wrote no code? statement would be wrong. Their function is document production, not simulation/estimation.
- The broader exclusion remains **UNVERIFIED** for earlier extension/diagnostic/validation/pilot code. Concrete additions in `e864dd27`, `d4897232` and `2ceec58a`, including Stage 2A/B variants and Stage 2H pilot code, require author attribution. References to AGENTS searches are leads, not proof of AI authorship. Unchanged frozen canonical wrappers do not establish that new diagnostic research code was human-only.

### Proposed disclosure, not applied

> AI tools, including ChatGPT and OpenAI Codex, assisted with grammar checking, translation, revision of existing manuscript text and repository documentation, to improve language clarity and the organization of the manuscript and its supporting documentation. Documented Codex assistance included redrafting existing passages and drafting reproducibility, evidence-map and data-availability documentation from existing project material, together with document-build, packaging and inspection utilities. According to the authors' declaration, AI was not used to develop or modify research code, simulations or statistical analysis.

This is a proposed scope statement, not a completed compliance attestation. Retain the final sentence only if the authors can reconcile it with the entire intended research/diagnostic scope. Do not convert it into a verified audit finding. Before adopting a final disclosure, obtain:

1. Exact ChatGPT/model and Codex/app/model versions and actual use dates/tasks, or publisher-accepted truthful unavailable-version wording.
2. Original/revised/translated material and the responsible human translation checker.
3. Author confirmation of accuracy, reference checking and responsibility for AI-assisted content, and confirmation of actual review of applicable tool terms. None is assumed.
4. A research-code scope ledger covering canonical/extension code, diagnostic variants, certification/validation, pilots and statistical/reporting scripts; reconcile any AI involvement before making a blanket exclusion.

The current manuscript disclosure is at `journal_article/sections/submission_declarations.tex:8`. It names tools and activities but lacks versions and the additional attestations required by the accessible publisher guidance. No source or PDF was changed by this gate.

## 2. Anonymous evidence bundle audit

**Artifact:** `journal_article/submission/review/frozen_summaries_review.zip`

**SHA-256:** `610a752337d6d1d3f61f5ae40c42f417e29cf06d4e99bd64a4fe35d11da3a258`
**Size:** 20615 bytes.

### Exact member inventory

The ZIP was opened read-only; CRC checks passed for every member. It has nine unique members, no encryption, no archive/member comments, no extra-field payloads, no absolute member paths and no parent-directory traversal. Standard ZIP timestamps/attributes remain; these are not proof of non-identifiability.

| Member | Uncompressed bytes | SHA-256 of member content |
|---|---|---|
| `record_inventory.csv` | 10790 | `6bf5eebe3e05871d7aa72d6df59cba010ee1c81e67428a75b3390ea8733c580d` |
| `README.txt` | 443 | `663e463ee0695da0941ae74313abbe998db7d28c6e5a17059c25467b3e51fea7` |
| `data/R048.csv` | 11421 | `5ea9c4368966c39e6b6f874cc7dc9019d1c58b5b56b65ecb9b9b72c823f96f38` |
| `data/R045.csv` | 19314 | `c1168cef8c2a4b1345e01a08386e7c2505c642f61d7211ba9b962d27c5c0bd8e` |
| `data/R043.csv` | 11513 | `da067bc5bf1f86703d5764c0ba4d164fbaea6b06f917c70d44bf027332e61cfd` |
| `data/R040.csv` | 19508 | `fa24ec859a8fd1df9575f4385f7c42113047b3077e514832aa55b080a2019adc` |
| `data/R052.csv` | 25589 | `153f90ddb02dbbc04de1476699d5aba131474a71de8ee945908ee2c106612ffa` |
| `data/R053.csv` | 11262 | `86b99d4cee32fbbca6afc788153e17cc78c990bf13b63ad0be99bcf5c2f3010e` |
| `data/R028.csv` | 2355 | `9a0d511aab9e0eb5d950b8287f846d5e02df65cf34b8f2c09bd3075826126da4` |

`record_inventory.csv` has 57 unique neutral record IDs (R001?R057). It is a **record catalogue**, not 57 attached evidence files. Seven rows identify CSV payloads. Inventory rows match the private original-to-review map, excluding its identifying original-path column. Every ID used by the review Appendix D map exists in the inventory; all seven attached CSV IDs occur in that map. Local proof of correspondence does not establish journal reviewer access.

### CSV correspondence and supported findings

Each payload was compared byte-for-byte with the corresponding existing local frozen source. No CSV was normalized, rewritten or statistically recomputed.

| Neutral ID / member | Existing source | Supported manuscript evidence |
|---|---|---|
| R028: `data/R028.csv` | `thesis_extension/calibration/instrument_strength_100rep/kappa_strength_summary.csv` | E1: designed relevance ordering; calibration F/partial-R2 summaries. |
| R040: `data/R040.csv` | `thesis_extension/final/output/n1000/power_summary.csv` | E3: n=1000 false-candidate rejection rates; power contrasts and cells underlying existing comparison counts. |
| R043: `data/R043.csv` | `thesis_extension/final/output/n1000/summary.csv` | E2/E3/E4: n=1000 Bias/MAE/RMSE, direct-at-truth Coverage/Size, accepted measure, boundary/full-grid summaries. |
| R045: `data/R045.csv` | `thesis_extension/final/output/n500/power_summary.csv` | E3: n=500 false-candidate rejection rates and sample-size comparisons. |
| R048: `data/R048.csv` | `thesis_extension/final/output/n500/summary.csv` | E2/E3/E4: n=500 point accuracy, direct-at-truth and grid summaries. |
| R052: `data/R052.csv` | `thesis_extension/reporting/output/table_cr_informativeness_full.csv` | E4: full main-design grid-informativeness summaries and explicit primary-domain definition. |
| R053: `data/R053.csv` | `thesis_extension/reporting/output/table_grid_domain_diagnostic.csv` | E5: existing domain-expansion measures, boundary/full-grid rates, profile/failure counts and interpretation limits. |

Reading the existing n=1000, tau=.50, kappa=.10, DML-IVQR-BC rows gives stored strings `Coverage=0.942`, `median_grid_accepted_set_measure=3.9`, and `power=0.094` for Delta=.50. The manuscript formats the measure as 3.900. This is a lookup of archived entries, not a new computation or independent coverage validation. Direct-test acceptance, grid quadrature and false-candidate rejection remain different quantities. Existing comparison counts such as 35/40 or 305/360 were **not recomputed** in this audit; these files expose their underlying cells.

### Identification and preservation checks

Names/surnames, both ORCIDs/emails, Tashkent/institution strings, GitHub username/project URLs, known revision tokens and personal absolute paths were searched in inventory/README/CSV text. No listed explicit identifier was found. ZIP comments and extra fields are absent, and members have neutral names. This is a bounded scan: exact numerical content/hashes and timestamps can still be matched to public material, and it does not guarantee anonymity.

All numerical payloads equal their local source files, and the ZIP member digest list above permits exact checking. This does not independently authenticate the historical freeze, verify scientific findings, establish worker-stream independence or prove statistical validity.

### Evidence availability: do not conflate the two ZIPs

The separate `source_review.zip` contains the document dependencies referenced by R005?R019 (existing figures and table TeX assets). Those are not in the CSV bundle, but they are in the local source package and/or rendered manuscripts. It would be incorrect to call all 50 non-CSV inventory records missing merely because they are not members of the data ZIP.

The following external/replay evidence is not supplied through either inspected local ZIP or a verified anonymous external route:

| Record IDs / evidence | Limitation and significance |
|---|---|
| **R020?R023:** existing rank-stability report, deterministic implementation report/contract, full-path report | Essential underlying records for the selected-case rank/decision sensitivity and five-of-24 comparison are not available to anonymous reviewers through a verified mechanism. Appendix D's summary is not access to the reports. |
| R026: retained DGP derivation source | The proof sketch is retained in Appendix D, but its original analytical provenance record is not provided anonymously. No new derivation is requested. |
| R031?R036: grid manifest/provenance and individual Stage 1/2 summary files | R053 supplies the combined reported diagnostic view, not the full original failure/provenance inventory or saved primitives/profiles. |
| R039, R041, R042, R044, R046, R047: replication-level power/results/profile CSVs | Aggregate summaries do not supply individual truth statistics, grid profiles or all forensic distribution/failure checks. They cannot provide exact random-number replay. |
| R029/R030/R037/R038/R054?R057 and original source directories | Candidate implementations, configuration, historical environment/package evidence are not in the manuscript source ZIP. Detailed algorithm prose is present; executable research reproduction access is not. Exact journal data/code requirements remain unverified. |
| R024/R025 and ignored grid primitives/profiles | Stage 2H raw pilot outputs/seal and large grid artifacts are local/Git-ignored; no public/anonymous availability is claimed. The historical main-run RNG replay specification also remains incomplete. |
| R050/R051 | Original empirical/reporting manifests are not included through a verified anonymous route. The unresolved historical freeze identifier remains a provenance gap, not an invented accessible checkout. |

### Minimal evidence-access recommendation

Do not upload or reclassify anything in this audit. First obtain the journal's actual research-data/reviewer-access procedure. The accessible general publisher guidance distinguishes research data from ordinary publication supplements; a generic supplementary upload is not automatically an approved data route, and ?not for review? is not a guarantee of editor confidentiality.

Use an existing journal-approved anonymous reviewer-access channel if available, with the seven verified summaries and their neutral inventory. Supply existing anonymized copies of **R020?R023** so reviewers can inspect the sensitivity evidence; add the existing candidate/configuration/environment and other provenance records the actual data/code policy requires. Preserve the original named mapping separately and do not falsely label all records available. Where direct evidence transfer would reveal identities, obtain editorial instructions rather than invent access. Do not require a new simulation, new certificate, reconstruction of lost RNG states or upload of every local Stage 2H raw file to repair a packaging gap. No new repository or deposit is created or assumed.

## 3. Official requirements and verification scope

All URLs below were checked on 10 November 2026. Direct JSCS IFA/about requests returned **HTTP 403**. Publisher-indexed journal text was accessible in search; it is identified as such, not represented as a successful live IFA/portal inspection. No submission login/process was initiated.

| Official source | What was verifiable | Limits |
|---|---|---|
| [JSCS publisher page](https://www.tandfonline.com/journals/GSCS) and [journal-information endpoint](https://www.tandfonline.com/action/journalInformation?journalCode=gscs20&show=instructions) | Search-retrieved publisher content specifies double-anonymous review, Submission Portal and a braced technique/contribution-area cue before the abstract. | Exact live portal/file categories and detailed IFA not inspected. |
| [JSCS Instructions for Authors](https://www.tandfonline.com/action/authorSubmission?show=instructions&journalCode=gscs20); [about page](https://www.tandfonline.com/journals/gscs20/about-this-journal) | Direct requests returned 403. | Format/template/style, abstract/article limits, degree/title-page conventions, source requirements, exact supplement/data policy and journal-specific AI limits are UNVERIFIED. |
| [Publisher AI policy](https://taylorandfrancis.com/our-policies/ai-policy/) | Accessible current general policy. Its role/scope/oversight comparison is documented in `AI_USE_PROVENANCE.md`. | Does not establish JSCS's potentially stricter AI limits or prove this paper complies. |
| [Publisher authorship/AI guidance](https://authorservices.taylorandfrancis.com/editorial-policies/defining-authorship-research-paper/) | Accessible general disclosure/translation/author-responsibility requirements. | Versions/terms/human-review confirmations are not supplied by an author list or build log. |
| [Submission Portal guide](https://authorservices.taylorandfrancis.com/publishing-your-research/making-your-submission/using-taylor-francis-submission-portal/) | General named and anonymous manuscript distinction; supplements must be appropriately categorized and anonymized. | Exact JSCS upload categories, title-page/source fields and reviewer visibility remain UNVERIFIED. |
| [Data-availability guidance](https://authorservices.taylorandfrancis.com/data-sharing/share-your-data/data-availability-statements/) | General truthful access conditions and anonymity implications. | Exact JSCS policy tier, public-deposit/code requirements and accepted anonymous mechanism remain UNVERIFIED. |
| [Supplementary-material guidance](https://authorservices.taylorandfrancis.com/publishing-your-research/writing-your-paper/enhancing-your-article-with-supplementary-material/) | General distinction between research data and ordinary supplements; review/not-for-review visibility differs. | Does not authorize this CSV ZIP's upload category or identify a confidential editor channel. |
| [Editorial policies](https://authorservices.taylorandfrancis.com/editorial-policies/) | General author declarations/framework. | Precise journal declaration headings, contribution taxonomy, placement and portal fields remain UNVERIFIED. |

No format-free permission, reference-style compliance, word/page/abstract limit, required source format or compulsory separate title-page PDF is inferred from other journals or a third-party template list. The current 11pt article class/author-year style and 34/33-page manuscripts are observed formats, not verified JSCS compliance. The source archives exist; a requirement to upload them has not been established.

## 4. Existing package and QA audit

The final-package artifacts were not regenerated. Fresh file hashes match their existing QA identities:

| Artifact | Pages / bytes | SHA-256 |
|---|---|---|
| Named manuscript | 34 / 1,013,853 | `4fecad9e125211689910104b8b533cb5e03f1d96e24752dc58bb62b5e77e3388` |
| Review manuscript | 33 / 997,536 | `bc8ef361d7d46546412735d40ba2b4203876569c041fe24081fd8cee42ea7645` |
| Optional tables | 28 / 187,961 | `c277db1a4c1c2ca6d8b1a826dacdaeb30c56e93c526c97273674a68d39715277` |

Sources: `submission/qa/build_results.json`, `consistency_checks.json`, `source_anonymity_checks.json`, per-PDF `audit.json`, metadata/text/URI/attachment outputs and raster contact sheets, plus `FINAL_PACKAGE_REPORT.md`. The ten recorded document-build commands exited zero. Final recorded logs have no undefined references/citations, duplicate labels, overfull boxes or rerun requests. Both main files have main equations 1?40, appendix B.1?B.4/D.1?D.14 and nine cited bibliography entries. These are document checks, not inference validation.

The current named/review cover renderings were inspected again. Named author order/affiliation/correspondence matches the supplied confirmation; the review cover omits them. Existing QA records document every page rendered/inspected, no blank pages and no `??`, and unchanged scientific source/assets. Fresh source-archive checks compare document members to staged/current named dependencies; archives/PDFs are not assumed current from filenames alone.

Review text/metadata/XMP/URI/embedded-file records have no listed explicit identity token; the PDF Author field is empty and zero embedded files are reported. The optional tables have the same bounded result. Direct PDF destination enumeration previously stalled; compiled bookmark-source inspection passed but no exhaustive object/JavaScript audit exists. Public matching of distinctive title/text/numbers or generic source filenames remains possible. No guarantee of absolute anonymity is made.

## 5. Requirement-by-requirement gate

| Requirement / condition | Gate | Evidence / exact action if not cleared |
|---|---|---|
| Confirmed names, order, shared affiliation, correspondence, ORCIDs/emails applied consistently | PASS | Named source, source archive, cover rendering and metadata agree. This checks application of user-confirmed facts. |
| Approved funding/conflict/equal-contribution/ethics statements inserted | PASS | Statements match the supplied text; no new CRediT role or version invented. This is not independent legal/ethics verification. |
| AI tools/activities acknowledged in current manuscript | PASS | Declaration names ChatGPT/Codex and assistance scope. |
| Complete tool/version/use disclosure required by accessible general policy | FAIL | Versions are absent; documented redrafting/new documentation/helper scope should be reviewed using the proposed wording. Do not invent identifiers or silently insert attestations. |
| Original-draft and earlier AI-use provenance | UNVERIFIED | Pre-existing Git text is established; original author/tool attribution and translation pairs are missing. Obtain author evidence. |
| Research-code/analysis AI exclusion across the whole intended research program | UNVERIFIED | Document helpers do not disprove it; earlier research/diagnostic/pilot tool authorship remains unresolved. Reconcile scope ledger. |
| Human review, translation responsibility, tool-terms review and retained originals | UNVERIFIED | Obtain actual author confirmations/records; no affirmative attestation is present. |
| Journal double-anonymous policy and technique cue identified | PASS | Publisher-indexed JSCS policy; cue already present. Exact live portal still needs confirmation. |
| Separate named and review PDFs exist and match recorded build identities | PASS | Fresh PDF hashes and source/archive checks; named 34 pages, review 33 pages. |
| Explicit identity masking in inspected review text/metadata/URLs and source/data text | PASS | Bounded scans and empty review Author; scientific citations retained. |
| Exhaustive deep-object anonymity / final portal-generated proof and visibility | UNVERIFIED | Destination-tool limitation, re-identification risk and no portal proof. Complete remaining checks before upload/readiness. |
| Reference/equation/table/figure/appendix consistency in existing package | PASS | Recorded clean builds and preserved source/assets; no rebuild or statistical check in this audit. |
| Optional table supplement built from existing assets, no changed entries | PASS | Existing 28-page standalone table document and source-byte comparison. Whether required/accepted is separate. |
| Data ZIP CRC, exact member inventory, neutral mapping and unchanged CSV payloads | PASS | Read-only CRC/member/source checks in this audit. |
| Claim coverage of included summaries correctly delimited | PASS | E1?E5 summary evidence is present; existing count comparisons not recomputed; selected-case/replay records not claimed present. |
| Essential selected-case numerical sensitivity records accessible anonymously | FAIL | R020?R023 absent from inspected review ZIPs and no verified external route. Arrange approved access to existing records. |
| Journal-approved anonymous research-data/code access and reviewer visibility | UNVERIFIED | Local ZIP presence is not a verified portal data route; full code/environment/replay/provenance not supplied. |
| Public/local-only distinctions and historical replay limits disclosed | PASS | Review availability statement/inventory do not promise ignored raw data or lost RNG replay. |
| Historical freeze checkout accessibility | UNVERIFIED | Prior report records local failure/remote 404 for `ac9a9cca?`; no usable release is invented. Clarify provenance/access under actual policy. |
| Research-data versus publication-supplement routing | UNVERIFIED | General distinction verified; JSCS-specific category/policy and handling of this ZIP not verified. Do not upload as a generic supplement by assumption. |
| Source-file requirements and acceptable anonymous source archive | UNVERIFIED | Whitelisted source ZIPs exist, but exact required formats/contents/metadata rules are inaccessible. |
| Separate title-page file and degree convention | UNVERIFIED | Named PDF contains the confirmed title page; separate file requirement not verified. DSc omitted under conditional instruction. |
| Required declaration headings, placement and contribution schema | UNVERIFIED | Generic approved statements exist; exact JSCS fields/CRediT requirement not established. |
| Abstract/article length, class/template, citation style, artwork and supplement constraints | UNVERIFIED | Detailed IFA inaccessible. No guessed compliance or unsupported numeric limit. |
| Scientific results/code/datasets unchanged by this audit | PASS | Pre/post identities checked; only the two reports are added. |
| Final source identity/release and submission approval | UNVERIFIED | Package is local/uncommitted; no final journal proof or approved access arrangement. No commit/upload is authorized in this gate. |

## 6. Remaining blockers, ranked corrective actions

1. **HIGH ? Anonymous evidence access (FAIL/UNVERIFIED).** Obtain the journal's real review-data procedure; enable access to the verified summary bundle and existing R020?R023 records. Supply implementation/configuration/environment and other provenance as the confirmed policy requires. Keep the identifying map out of reviewer files. Do not create a repository or upload anything in this audit.
2. **HIGH ? AI provenance/scope and attestations (UNVERIFIED).** Authors must supply original/revised/translation records, a responsible human checker and a scope ledger including research/diagnostic code. Resolve any actual conflict before certifying the research-code exclusion; do not assume a contradiction or innocence from Git author metadata.
3. **HIGH ? Incomplete AI disclosure (FAIL).** Obtain actual versions or journal-accepted honest unavailable-version wording, verify role/scope, and obtain real author accuracy/responsibility/terms confirmations. Only a later authorized revision should apply the agreed disclosure to both named/review documents and rebuild them.
4. **HIGH ? Detailed JSCS requirements (UNVERIFIED).** Retrieve the current IFA/live requirements through author access or editorial clarification: anonymity/files, data/code route, title page, declarations, AI limits, formatting/length/source/figure/supplement rules. Do not send a message or initiate submission here.
5. **MEDIUM ? Remaining anonymity/visibility checks (UNVERIFIED).** Resolve or explicitly agree acceptable scope of deep metadata/object inspection; inspect the eventual portal-generated proof and each file's visibility. Disclose existing public circulation appropriately; do not alter scientific values to disguise a public match.
6. **MEDIUM ? Provenance/reproduction gaps.** Clarify the unresolved freeze identifier and what exists only locally. These do not authorize new statistical work or require recovering impossible RNG history; the availability statement must remain accurate and meet the actual journal policy.

**Final recommendation: NOT READY.** Local packaging integrity is largely PASS, but not every essential submission requirement is verified. No compliance assurance, guaranteed anonymity, inference-theorem validation or acceptance prediction is made. Stop with these reports; no corrective manuscript/package action is performed.

## Appendix: exact record disposition across the two existing review ZIPs

This catalogue is identifying internal audit material because it restores original repository paths. Do not upload this report as an anonymous supplement. ?Not in either ZIP? is a local inventory fact, not a claim that no editor-approved access could later be arranged. Directory/member locators such as R003/R004 refer to retained package-source records, not fabricated top-level repository files.

| ID | Local disposition | Original locator |
|---|---|---|
| R001 | Not in either ZIP | `Empirical_work/` |
| R002 | Not in either ZIP | `example/` |
| R003 | Not in either ZIP | `hdm/R/LassoShooting.fit.R` |
| R004 | Not in either ZIP | `hdm/R/rlasso.R` |
| R005 | Review source ZIP / document dependency | `journal_article/figures/generated/accepted_measure_n1000.png` |
| R006 | Review source ZIP / document dependency | `journal_article/figures/generated/accepted_measure_n500.png` |
| R007 | Review source ZIP / document dependency | `journal_article/figures/generated/coverage_heatmap.pdf` |
| R008 | Review source ZIP / document dependency | `journal_article/figures/generated/full_domain_acceptance_heatmap.pdf` |
| R009 | Review source ZIP / document dependency | `journal_article/figures/generated/power_median_combined.pdf` |
| R010 | Review source ZIP / document dependency | `journal_article/figures/generated/rmse_n1000.png` |
| R011 | Review source ZIP / document dependency | `journal_article/figures/generated/rmse_n500.png` |
| R012 | Review source ZIP / document dependency | `journal_article/figures/grid_domain_expansion.png` |
| R013 | Review source ZIP / document dependency | `journal_article/tables/generated/appendix_coverage.tex` |
| R014 | Review source ZIP / document dependency | `journal_article/tables/generated/appendix_cr_informativeness.tex` |
| R015 | Review source ZIP / document dependency | `journal_article/tables/generated/appendix_grid_diagnostic.tex` |
| R016 | Review source ZIP / document dependency | `journal_article/tables/generated/appendix_point_performance.tex` |
| R017 | Review source ZIP / document dependency | `journal_article/tables/generated/appendix_power.tex` |
| R018 | Review source ZIP / document dependency | `journal_article/tables/table_main_performance.tex` |
| R019 | Review source ZIP / document dependency | `journal_article/tables/table_strength_calibration.tex` |
| R020 | Not in either ZIP | `journal_validation/stage2c/stability/STABILITY_REPORT.md` |
| R021 | Not in either ZIP | `journal_validation/stage2g/deterministic_implementation/DETERMINISTIC_IMPLEMENTATION_REPORT.md` |
| R022 | Not in either ZIP | `journal_validation/stage2g/deterministic_implementation/IMPLEMENTATION_CONTRACT_v1.md` |
| R023 | Not in either ZIP | `journal_validation/stage2g/full_path_validation/FULL_PATH_REPORT.md` |
| R024 | Not in either ZIP | `journal_validation/stage2h/pilot/SHA256_MANIFEST.json` |
| R025 | Not in either ZIP | `journal_validation/stage2h/pilot/runs/` |
| R026 | Not in either ZIP | `journal_validation/stage2h/readiness/BOUNDED_DGP_DERIVATION.md` |
| R027 | Not in either ZIP | `simulation/` |
| R028 | CSV bundle | `thesis_extension/calibration/instrument_strength_100rep/kappa_strength_summary.csv` |
| R029 | Not in either ZIP | `thesis_extension/config/` |
| R030 | Not in either ZIP | `thesis_extension/config/extension_config.R` |
| R031 | Not in either ZIP | `thesis_extension/diagnostics/grid_sensitivity/GRID_RESULTS_MANIFEST.csv` |
| R032 | Not in either ZIP | `thesis_extension/diagnostics/grid_sensitivity/GRID_RESULTS_PROVENANCE.md` |
| R033 | Not in either ZIP | `thesis_extension/diagnostics/grid_sensitivity/output/stage1/stage1_expansion_summary.csv` |
| R034 | Not in either ZIP | `thesis_extension/diagnostics/grid_sensitivity/output/stage1/stage1_summary.csv` |
| R035 | Not in either ZIP | `thesis_extension/diagnostics/grid_sensitivity/output/stage2/stage2_expansion_summary.csv` |
| R036 | Not in either ZIP | `thesis_extension/diagnostics/grid_sensitivity/output/stage2/stage2_summary.csv` |
| R037 | Not in either ZIP | `thesis_extension/environment/` |
| R038 | Not in either ZIP | `thesis_extension/environment/package_archives_R343/hdm_0.2.0.tar.gz` |
| R039 | Not in either ZIP | `thesis_extension/final/output/n1000/power.csv` |
| R040 | CSV bundle | `thesis_extension/final/output/n1000/power_summary.csv` |
| R041 | Not in either ZIP | `thesis_extension/final/output/n1000/profiles.csv` |
| R042 | Not in either ZIP | `thesis_extension/final/output/n1000/results.csv` |
| R043 | CSV bundle | `thesis_extension/final/output/n1000/summary.csv` |
| R044 | Not in either ZIP | `thesis_extension/final/output/n500/power.csv` |
| R045 | CSV bundle | `thesis_extension/final/output/n500/power_summary.csv` |
| R046 | Not in either ZIP | `thesis_extension/final/output/n500/profiles.csv` |
| R047 | Not in either ZIP | `thesis_extension/final/output/n500/results.csv` |
| R048 | CSV bundle | `thesis_extension/final/output/n500/summary.csv` |
| R049 | Not in either ZIP | `thesis_extension/reporting/` |
| R050 | Not in either ZIP | `thesis_extension/reporting/EMPIRICAL_RESULTS_MANIFEST.csv` |
| R051 | Not in either ZIP | `thesis_extension/reporting/REPORTING_OUTPUT_MANIFEST.csv` |
| R052 | CSV bundle | `thesis_extension/reporting/output/table_cr_informativeness_full.csv` |
| R053 | CSV bundle | `thesis_extension/reporting/output/table_grid_domain_diagnostic.csv` |
| R054 | Not in either ZIP | `thesis_extension/src/` |
| R055 | Not in either ZIP | `thesis_extension/src/author_bc_dml_wrapper.R` |
| R056 | Not in either ZIP | `thesis_extension/src/author_oracle_wrapper.R` |
| R057 | Not in either ZIP | `thesis_extension/src/run_extension.R` |

## Audit preservation record

HEAD and the pre-existing working-tree changes were preserved. Only `AI_USE_PROVENANCE.md` and `SUBMISSION_GATE_REPORT.md` were added. All pre-existing tracked/non-ignored file bytes and every named/review package artifact were compared with the gate baseline; no manuscript, research code, numerical asset, PDF, ZIP or QA file was rewritten. No document helper or research script was executed. ZIP/byte/header/lookup checks are packaging inspection, not new statistical computations.
