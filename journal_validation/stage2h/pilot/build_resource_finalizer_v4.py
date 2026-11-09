"""Honor the prespecified resource stop: report, never launch further fits."""
from pathlib import Path
P=Path(__file__).resolve().parent
s=(P/'finalize_pilot_v3.py').read_text(encoding='utf-8')
start=s.index(' for id in ids:');end=s.index(" table(run/'reproducibility.csv',replays)",start)
s=s[:start]+" for id in ids:\n  replays.append({'id':id,'status':'NOT_EXECUTED_RESOURCE_STOP','statistical_replications_added':0,'reason':'Prespecified total resource envelope exhausted; no further candidate processes launched'})\n"+s[end:]
s=s.replace(" assert all(r['all_numerical_fingerprints_identical'] for r in replays),'Replay failure retained; investigate before claiming reproducibility'",'')
s=s.replace('Four prespecified same-input replays add no statistical observations.', 'The four prespecified same-input replays were not executed after the resource stop; pilot result repeatability is therefore unverified. Primitive/penalty RNG replay and independent numerical audits remain separately documented.')
s=s.replace('`reproducibility.csv` verifies the frozen four-case replay panel bitwise.', '`reproducibility.csv` records the four-case replay panel as NOT_EXECUTED_RESOURCE_STOP; no pilot bitwise result-repeatability claim is made.')
s=s.replace('## Truth inclusion and paired comparisons', '## Partial-pilot truth inclusion bounds and paired comparisons')
s=s.replace("'## Numerical status and validation',''", "'## Numerical status and validation','', 'A second long host interruption carried the calendar wall time beyond the immutable 12-hour deadline. At the next execution opportunity the operational driver marked both active fits TIME_LIMIT_UNRESOLVED and stopped launching fits, recording every remaining planned ID RESOURCE_NOT_EXECUTED. The pilot is therefore STOPPED AT THE RESOURCE GUARDRAIL and incomplete. The elapsed envelope was exceeded while the host was interrupted; it must not be reported as a completed within-budget experiment. No replication count, grid, seed or deadline was extended. The four result-repeatability fits were also withheld after the stop. Only reporting and integrity checks continued.', ''")
s=s.replace('sampled aggregate peak RSS in the resumed phase:', 'sampled PID-tree aggregate peak RSS in the resumed phase:')
s=s.replace('## Manuscript implications and next scientific task', '## Manuscript implications and next scientific task after the guardrail stop')
s=s.replace('Use these results as a finite prespecified DGP-sensitivity diagnostic,', 'Use these incomplete results as a partial prespecified DGP-sensitivity diagnostic with explicit missing-decision bounds,')
(P/'finalize_pilot_v4.py').write_text('# Version 4: resource stop is final; no fitting or replay after the deadline.\n'+s,encoding='utf-8')
