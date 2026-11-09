"""Preserve interruption/attempt accounting; do not reinterpret late results as qualified."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
import csv,json,time
P=Path(__file__).resolve().parent;run=Path((P/'LATEST_RUN.txt').read_text().strip())
def load(p):return json.loads(p.read_text())
original=[json.loads(s) for s in (run/'execution.jsonl').read_text().splitlines()]
resumed=[json.loads(s) for s in (run/'resume_execution.jsonl').read_text().splitlines()]
repair=load(run/'INTERRUPTION_REPAIR_v2.json');resume=load(run/'EXECUTION_RESUME_v2.json')
start=min(f.stat().st_ctime for f in (run/'results/pilot').glob('*.log'));end=(run/'EXECUTION_RESUME_v2.json').stat().st_mtime
all_events=original+resumed
out={'elapsed_seconds':end-start,'elapsed_scope':'first candidate log creation to resumed execution completion; includes host interruption','memory':resume['memory'],'memory_scope':'aggregate supervisor memory sampled during resume only; original supervisor aggregate peak unavailable after interruption','resource_stop':resume['resource_stop'],'events':len(all_events),'unique_completed_ids':len(set(e['id'] for e in all_events)),'interrupted_process_attempts':len(repair['interrupted_attempts_preserved']),'all_candidate_process_attempts':len(all_events)+len(repair['interrupted_attempts_preserved']),'original_completed':len(original),'resume_completed':len(resumed),'resumed_elapsed_seconds':resume['elapsed_seconds'],'retained_bytes_estimate':resume['retained_bytes_estimate'],'wall_limit_overrides':len(load(run/'status_overrides.json'))}
with (run/'EXECUTION.json').open('x',encoding='utf-8') as f:json.dump(out,f,indent=2)
attempts=[dict(e,attempt_phase='original',process_attempt_completed=True) for e in original]+[dict(e,attempt_phase='resume_v2',process_attempt_completed=True) for e in resumed]+[{'id':id,'attempt_phase':'original_interrupted','status':'INTERRUPTED_UNRESOLVED','process_attempt_completed':False} for id in repair['interrupted_attempts_preserved']]
with (run/'all_process_attempts.csv').open('x',newline='',encoding='utf-8') as f:
 w=csv.DictWriter(f,fieldnames=list(dict.fromkeys(k for r in attempts for k in r)));w.writeheader();w.writerows(attempts)
print(json.dumps(out),flush=True)
