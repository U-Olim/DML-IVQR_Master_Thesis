"""Mechanical adapters for interrupted execution; preserve original analysis code."""
from pathlib import Path
P=Path(__file__).resolve().parent
s=(P/'summarize_pilot.py').read_text(encoding='utf-8')
old="id=d['id'];n=int(d['n']);tau=float(d['tau']);f=run/'results/pilot'/id;src=run/'inputs'/id"
new="id=d['id'];n=int(d['n']);tau=float(d['tau']);f=run/'results/pilot'/id;src=run/'inputs'/id\n  if not (f/'result.json').exists():f=run/'results/resume_v2'/id"
assert old in s;s=s.replace(old,new)
old="ok=r['status']=='PASS';row="
new="overrides=load(run/'status_overrides.json')\n  if id in overrides:r.update(overrides[id])\n  if (f/'operational_status.json').exists():r.update(load(f/'operational_status.json'))\n  ok=r['status']=='PASS';row="
assert old in s;s=s.replace(old,new)
(P/'summarize_pilot_v2.py').write_text('# Version 2: unchanged statistical definitions; resolve immutable result roots and explicit wall-limit overrides.\n'+s,encoding='utf-8')
s=(P/'finalize_pilot_v2.py').read_text(encoding='utf-8')
s=s.replace("a=load(run/'results/pilot'/id/'result.json');b=load(f/'result.json')", "original=run/'results/pilot'/id\n  if not (original/'result.json').exists():original=run/'results/resume_v2'/id\n  a=load(original/'result.json');b=load(f/'result.json')")
s=s.replace("(run/'results/pilot'/id).glob('*.bin')", "original.glob('*.bin')")
s=s.replace("dump(run/'preservation.json',preservation);assert preservation['status']=='PASS'", "dump(run/'preservation.json',preservation);assert preservation['status']=='PASS'\n for name,h in load(run/'RESUME_SOURCE_LOCK.json').items():assert sha(P/name)==h,name")
s=s.replace("Measured candidate execution wall time:","Measured candidate wall time including host interruption:")
s=s.replace("sampled aggregate peak RSS:","sampled aggregate peak RSS in the resumed phase:")
s=s.replace("This sampled RSS counts shared pages and is not a continuous maximum.","This sampled RSS counts shared pages and is not a continuous maximum. The original supervisor peak was not retained after interruption; candidate-level OS/RSS records remain available, so the full-run aggregate maximum is unknown.")
s=s.replace("'## Numerical status and validation',''", "'## Numerical status and validation','', 'Execution was interrupted by a long host interruption and a stale monitoring host. Three original numerical PASS records exceeded the 180-second elapsed wall limit and are explicitly TIME_LIMIT_UNRESOLVED through immutable sidecar overrides; their decisions are excluded from qualification and remain in missing-decision bounds. Incomplete attempts were retained and audited, then resumed on the exact same frozen input IDs and RNG streams in a separate output directory. The operational v2 driver adds repeated deadline checks and a post-completion elapsed-time check. No estimator, solver tolerance, objective, penalty, numerical certificate, DGP parameter or stream changed. The 12-hour total envelope remains anchored conservatively at original run creation, including preparation and interruption. See INTERRUPTION_REPAIR_v2.json, status_overrides.json, interruption_audits and resume_execution.jsonl.', ''")
(P/'finalize_pilot_v3.py').write_text('# Version 3: interrupted result roots, operational uncertainty and explicit missing original aggregate memory peak.\n'+s,encoding='utf-8')
