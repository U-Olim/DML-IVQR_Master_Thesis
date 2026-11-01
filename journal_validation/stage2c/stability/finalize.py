"""Finalize stability tables, exact objective records and integrity evidence."""
from pathlib import Path
from fractions import Fraction as F
from collections import Counter
import json,sys
import numpy as np
from analyze import HERE,PRIOR,dump,read,table,sha,snapshot,unpack
sys.path.insert(0,str(HERE.parent/'certification'))
from exact_bounds import record


def main():
 run=Path(sys.argv[1]).resolve();assert HERE in run.parents
 initial=json.loads((run/'initial_state.json').read_text())
 assert sha(HERE/'PROTOCOL.md')==initial['protocol_sha256_before_comparisons']
 assert sha(HERE/'analyze.py')==initial['source_sha256_before_execution']['analyze.py']
 assert sha(HERE/'scores.R')==initial['source_sha256_before_execution']['scores.R']
 validation=json.loads((run/'independent_validation.json').read_text());assert validation['status']=='PASS'
 assert json.loads((run/'run_status.json').read_text())['status']=='COMPLETE'
 comparisons=read(run/'all_probe_inference.csv');baselines=read(run/'baseline_R.csv')
 classifications=read(run/'arm_stability_classification.csv')
 objective_records=[];extended=[];observed=[]
 for r in classifications:
  name,arm=r['dataset'],r['arm'];folder=run/name/arm
  cert=json.loads((PRIOR/name/arm/'exact_certificate.json').read_text());D=unpack(cert['dual'])
  p=json.loads((PRIOR/name/arm/'stability_probes.json').read_text());base=np.fromfile(folder/'baseline_residual.bin',dtype='<f8')<=0
  union=np.zeros(1000,dtype=bool);qualified=0
  for candidate in p:
   id='exp'+str(candidate['exponent'])+'_sign'+str(candidate['sign'])
   row=next(z for z in comparisons if z['dataset']==name and z['arm']==arm and z['id']==id)
   G=unpack(candidate['exact_objective_gap_upper_bound'])
   objective_records.append({'dataset':name,'arm':arm,'id':id,
    'alternative_primal_objective':record(D+G),'exact_dual_feasible_lower_bound':record(D),
    'certified_suboptimality_upper_bound':record(G),'within_frozen_budget':row['within_frozen_budget']=='True',
    'source_primal_dual_certificate_sha256':sha(PRIOR/name/arm/'exact_certificate.json')})
   if row['within_frozen_budget']=='True':
    q=np.fromfile(folder/(id+'_residual.bin'),dtype='<f8')<=0;union|=q!=base;qualified+=1
   if row['within_frozen_budget']=='True' and row['decision_change']=='True':observed.append(row)
  extended.append(dict(r,observed_rank_indicators_changing_in_qualifying_set=int(sum(union)),
   qualifying_original_and_alternatives=qualified+1,
   scope='Finite fixed probe set; not uniform over full near-optimal solution set.'))
 dump(run/'alternative_optimization_certificates.json',objective_records)
 table(run/'arm_stability_classification_extended.csv',extended)
 table(run/'observed_certified_decision_changes.csv',observed)
 proximity=[]
 for epsilon in [1e-6,.01,.1,.5,1]:
  proximity.append({'descriptive_distance':epsilon,'baseline_count':sum(abs(float(r['cutoff_distance']))<=epsilon for r in baselines),
    'denominator':92,'changes_no_indicator_or_cutoff':True})
 table(run/'baseline_cutoff_proximity.csv',proximity)
 before=json.loads((run/'protected_before.json').read_text());after=snapshot()
 preservation={'files_checked':len(before),'changed':[p for p in before if p in after and before[p]!=after[p]],
  'missing':sorted(before.keys()-after.keys()),'added_outside_stability':sorted(after.keys()-before.keys())}
 assert not any(preservation[k] for k in ['changed','missing','added_outside_stability'])
 dump(run/'final_preservation.json',preservation)
 assert (HERE/'STABILITY_REPORT.md').is_file()
 dump(run/'source_sha256.json',{p.name:sha(p) for p in sorted(HERE.iterdir()) if p.is_file()})
 summary=json.loads((run/'summary.json').read_text())
 final={'status':'COMPLETE','recommendation':'C - Remain stopped because numerical inference is insufficiently reliable',
  'classification_counts':summary['classification_counts'],'arms':92,
  'qualifying_certified_alternatives':summary['qualifying_probes'],
  'qualifying_changes_from_original_decision':summary['qualifying_probes_changing_original_decision'],
  'independently_verified_W_evaluations':validation['exact_W_values_verified'],
  'protocol_and_generators_unchanged_since_execution_start':True,
  'no_refits':True,'no_Monte_Carlo':True,'no_continuation':True,'preservation':preservation}
 dump(run/'final_status.json',final)
 files=sorted(p for p in run.rglob('*') if p.is_file() and p.name!='SHA256_MANIFEST.json')
 manifest={p.relative_to(run).as_posix():{'sha256':sha(p),'bytes':p.stat().st_size} for p in files}
 dump(run/'SHA256_MANIFEST.json',manifest)
 for name,r in manifest.items():assert sha(run/name)==r['sha256']
 print(json.dumps(dict(final,verified_artifacts=len(manifest)),indent=2))


if __name__=='__main__':main()
