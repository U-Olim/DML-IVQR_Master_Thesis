"""Pre-fit report adapter: preserve unresolved replay comparisons explicitly."""
from pathlib import Path
P=Path(__file__).resolve().parent
s=(P/'finalize_pilot.py').read_text(encoding='utf-8')
old="identical=a.get('fingerprints')==b.get('fingerprints') if a['status']==b['status']=='PASS' else None"
new="identical=a.get('fingerprints')==b.get('fingerprints') if a['status']==b['status']=='PASS' else (a['status']==b['status'] and a.get('failure_component')==b.get('failure_component') and {x.name:sha(x) for x in (run/'results/pilot'/id).glob('*.bin')}=={x.name:sha(x) for x in f.glob('*.bin')})"
assert old in s;s=s.replace(old,new)
old="dump(run/'preservation.json',preservation);assert preservation['status']=='PASS'"
s=s.replace(old,old+"\n for name,h in load(run/'PREFIT_FINAL_SOURCE_LOCK.json').items():assert sha(P/name)==h,name")
s=s.replace("'## Numerical status and validation',''", "'## Numerical status and validation','', 'The original input verifier rejected the prescribed floating expression at an original Phi value rounded to one. Version 2 checks the unchanged literal transformation against its representable endpoints. Maximum upper-end rounding excess is 1.11e-16. The failed log and both verifier versions are preserved. This changes validation only; no DGP, numerical policy, penalty, stream or sample was changed. See VALIDATOR_FIX_v2.json and treatment_rounding.csv.', ''")
(P/'finalize_pilot_v2.py').write_text('# Version 2 frozen before fitting: retain unresolved replay evidence and document endpoint validation correction.\n'+s,encoding='utf-8')
