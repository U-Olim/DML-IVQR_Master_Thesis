# G2 — Manifest discrepancy investigation

12 November 2026. Preserve historical manifests and current files unchanged.

## thesis_extension/environment/AUTHOR_R343_ENVIRONMENT_REPORT.md

| Field | Value |
|---|---|
| Manifest | thesis_extension/reporting/EMPIRICAL_RESULTS_MANIFEST.csv |
| Expected SHA256 | 113ab0bfb90b3aa1433baed735113924d9849534aa7543d4fb4b899c9cb9d5d9 |
| Actual SHA256 | e003cb055ea472e8a3d08a572ec65a3dd5238fcf400763e203b63e6f23385b5e |
| HEAD blob SHA256 | e003cb055ea472e8a3d08a572ec65a3dd5238fcf400763e203b63e6f23385b5e |
| LF SHA256 | e003cb055ea472e8a3d08a572ec65a3dd5238fcf400763e203b63e6f23385b5e |
| CRLF SHA256 | 6f1e59935216a44aa1e6c1d101b841e3c1b7838932787b7f9b5d134da96e95ff |

Source history:

| Commit | Blob SHA256 |
|---|---|
| e864dd273da6718751c2d5ac5ce6921fd330cd7e | e003cb055ea472e8a3d08a572ec65a3dd5238fcf400763e203b63e6f23385b5e |

Current bytes match HEAD; neither LF nor CRLF explains the expected hash. All accessible path revisions listed above were inspected; none supplies the expected bytes. A stale pre-import manifest is plausible but its timing and original contents are not established. No exact textual diff against an unavailable expected version can be claimed.

Environment-description provenance is affected, not a numerical result. It includes historical machine paths and an absent PROJECT_STATUS.md link; no altered runtime or scientific statistic is established.

Safest correction: retain both original manifest and current file. Seek a provenance-backed backup of expected bytes; otherwise disclose the unresolved entry. A later release manifest must record actual current hashes and source commit separately, never silently replace historical hashes. Any portable reporting adapter must be separately versioned, reviewed and write elsewhere; do not bypass original guards or regenerate results here.

## thesis_extension/reporting/build_thesis_results.R

| Field | Value |
|---|---|
| Manifest | thesis_extension/reporting/REPORTING_OUTPUT_MANIFEST.csv |
| Expected SHA256 | 8a5ccd4df30401aea8c2bd7e4d3bd795f55f230453441367b208ff81bbea1faf |
| Actual SHA256 | be51eb22fb69a62e7dc1e4dc280af85112243d94e8592085ed8ab93fcd8b056a |
| HEAD blob SHA256 | be51eb22fb69a62e7dc1e4dc280af85112243d94e8592085ed8ab93fcd8b056a |
| LF SHA256 | be51eb22fb69a62e7dc1e4dc280af85112243d94e8592085ed8ab93fcd8b056a |
| CRLF SHA256 | 4c8ee84c10f9263cd60b8d7bf9b52d2363b40a2f1dc15506786ffe9472d6097f |

Source history:

| Commit | Blob SHA256 |
|---|---|
| e864dd273da6718751c2d5ac5ce6921fd330cd7e | be51eb22fb69a62e7dc1e4dc280af85112243d94e8592085ed8ab93fcd8b056a |

Current bytes match HEAD; neither LF nor CRLF explains the expected hash. All accessible path revisions listed above were inspected; none supplies the expected bytes. A stale pre-import manifest is plausible but its timing and original contents are not established. No exact textual diff against an unavailable expected version can be claimed.

The reporting generator cannot be authenticated against its historical manifest. Current source additionally requires unresolved freeze commit ac9a9ccad027cde05488abb633e66cc02f87cc46 and refuses nonempty existing outputs. A new repository HEAD will fail this guard even if paths are retained. This does not establish that frozen statistics changed.

Safest correction: retain both original manifest and current file. Seek a provenance-backed backup of expected bytes; otherwise disclose the unresolved entry. A later release manifest must record actual current hashes and source commit separately, never silently replace historical hashes. Any portable reporting adapter must be separately versioned, reviewed and write elsewhere; do not bypass original guards or regenerate results here.

