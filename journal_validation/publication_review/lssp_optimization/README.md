# Proposed LSSP optimization — author review only

Read ../LSSP_OPTIMIZATION_REPORT.md, then CONTENT_OPTIMIZATION_PLAN.md. Review manuscript_optimized.pdf together with technical_supplement.pdf and EVIDENCE_INVENTORY.md. Appendices A–D remain inline in the main PDF. Tables A.2–A.5 are in the technical PDF. Do not replace canonical journal_article/ without author approval.

The complete proposed LaTeX tree is source/. Source and rendered-text diffs, the item inventory, retention map and scientific integrity audit describe all changes. review_package.zip contains the two PDFs, complete proposed sources and review documents without build/runtime caches.

Document-only reproduction: from the repository root run `python -B journal_validation/publication_review/lssp_optimization/optimize_documents.py plan`, then `prepare`, `build`, `verify`, `finalize`. This uses the previously initialized local MiKTeX runtime; installers and shell escape are disabled. It never invokes research scripts. Plan recreates the baseline only when tracked canonical files are clean. Visual inspection remains a manual review step; finalization records the review performed in this session.
