# Final state: resource guardrail reached; no further fitting

The run ended incomplete after a second long host interruption. The persistent
12-hour deadline was exceeded during the interruption. At the next execution
opportunity the operational driver recorded both active candidates as time-limit
unresolved and marked every remaining planned ID not executed. It did not extend
the deadline or start replacement samples.

Final unique-evaluation counts: 1,440 planned; 1,069 attempted; 1,064 qualified;
five TIME_LIMIT_UNRESOLVED; 371 RESOURCE_NOT_EXECUTED. There were two additional
preserved incomplete process attempts on the same frozen IDs (1,071 total
process attempts); they add no statistical observations. All n=500 evaluations
completed. The n=1,000 results are incomplete.

Four prespecified result-repeatability fits were withheld after the resource
stop. RNG/input replay and independent numerical audits are documented, but
pilot bitwise result-repeatability is unverified. Do not run old finalizers
v1/v2/v3: they launch the replay panel and would violate the final stop.

Reporting after the stop uses only existing artifacts:

```powershell
$pilotPython = 'C:/Users/User/AppData/Local/Programs/Python/Python311/python.exe'
& $pilotPython -B journal_validation/stage2h/pilot/merge_execution_v2.py
& $pilotPython -B journal_validation/stage2h/pilot/summarize_pilot_v2.py
& $pilotPython -B journal_validation/stage2h/pilot/finalize_pilot_v4.py
& $pilotPython -B journal_validation/stage2h/pilot/finish_reporting.py
```

`merge_execution_v2.py` uses exclusive output creation; it is an archival
one-time merge and must not overwrite its completed outputs. Likewise, do not
rerun `finish_reporting.py` over a final report without preserving the earlier
report, because it inserts the interpretation section. The exact executed source
is retained and covered by the final SHA-256 manifest.

Coverage/rejection and paired tables retain denominator 20 and explicit missing
decision bounds. Means and MCSEs label qualified/complete-pair counts. No failed
decision is acceptance, and no missing W is zero-imputed. The three original
late PASS artifacts remain immutable with sidecar operational overrides. The
two resumed time limits have separate operational/audit artifacts.

No further fits or resumed scientific evaluations are permitted under this
exhausted run. A follow-up requires a separately frozen protocol and budget.
No manuscript edit, historical edit, commit or push was performed.
