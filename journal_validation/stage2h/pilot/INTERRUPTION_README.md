# Operational version 2: host interruption and immutable resume

The monitoring tool host became stale after a long interruption. The original
supervisor continued and recorded three numerical PASS results with external
elapsed times above the 180-second limit (750.547, 10663.062 and 9944.5 seconds).
These numerical records remain immutable. They are **TIME_LIMIT_UNRESOLVED** for
inference through `status_overrides.json`, even though their numerical audits
passed. They are not rerun or replaced by favorable results. Coverage/rejection
bounds retain them in denominator 20.

The original supervisor and its active children were stopped. Incomplete original
attempts remain in place and undergo independent attempted-certificate audits.
They resume with the identical frozen candidate IDs, numerical code, inputs and
recorded streams, saving into `results/resume_v2`. Already completed IDs are
skipped, including the three late/unresolved records. No source, data, penalty or
certificate from the original attempt is overwritten.

The versioned driver repairs operational wall-limit enforcement using repeated
short waits and a post-completion check of elapsed wall time. The total 12-hour
deadline is conservatively anchored to original run creation, including input
preparation and the interruption. The two-worker, one-thread policy and all
statistical/numerical definitions remain unchanged. This implements the existing
failure and resume rules; it introduces no estimator or protocol deviation.

The original supervisor's aggregate RSS peak was not saved when it was stopped.
Per-candidate RSS and OS working-set records survive. Resumed aggregate memory
is measured separately; the full-run aggregate maximum must be reported unknown.
`all_process_attempts.csv` distinguishes unique planned evaluations, completed
process attempts and preserved incomplete attempts. Extra same-ID process
attempts are not independent statistical replications.

After the original interruption, use:

```powershell
$pilotPython = 'C:/Users/User/AppData/Local/Programs/Python/Python311/python.exe'
& $pilotPython -B journal_validation/stage2h/pilot/resume_pilot_v2.py
& $pilotPython -B journal_validation/stage2h/pilot/merge_execution_v2.py
& $pilotPython -B journal_validation/stage2h/pilot/summarize_pilot_v2.py
& $pilotPython -B journal_validation/stage2h/pilot/finalize_pilot_v3.py
```

These commands extend the original run; do not initialize a new design or RNG
map. Original source locks stay intact. `RESUME_SOURCE_LOCK.json` additionally
freezes new operational/report adapters before resumed fitting. Numerical
worker/certificate/auditor sources are unchanged and are verified against their
original locks. The analysis adapters change result lookup and operational
qualification only; binomial intervals, paired MCSEs and missing-decision bounds
retain their original definitions.
