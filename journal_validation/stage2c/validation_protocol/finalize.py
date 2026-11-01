"""Finalize saved-input reassessment evidence and integrity. No numerical fits."""
import csv,json,sys
from pathlib import Path
from collections import Counter
from reassess import HERE,ORIGINAL,dump,sha,snapshot


def read(p):
 with p.open(newline='',encoding='utf-8-sig') as f:return list(csv.DictReader(f))


def table(p,rows):
 fields=list(dict.fromkeys(k for r in rows for k in r))
 with p.open('w',newline='',encoding='utf-8') as f:
  w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)


def main():
 run=Path(sys.argv[1]).resolve();assert HERE in run.parents
 initial=json.loads((run/'initial_state.json').read_text())
 assert sha(HERE/'PROTOCOL.md')==initial['protocol_sha256_before_execution']
 assert sha(HERE/'reassess.py')==initial['source_sha256_before_execution']['reassess.py']
 assert json.loads((run/'run_status.json').read_text())['status']=='COMPLETE'
 validation=json.loads((run/'independent_validation.json').read_text());assert validation['status']=='PASS'
 rows=json.loads((run/'arm_summary.json').read_text());assert len(rows)==92
 csvrows=[];probes=[]
 for r in rows:
  orig=next(x for x in read(ORIGINAL/r['dataset']/'evaluations.csv') if x['arm']==r['arm'])
  z=dict(r,recorded_primal_objective=float(orig['objective']),
   exact_minus_recorded_primal_float_diagnostic=r['primal']-float(orig['objective']),
   interpretation='Objective error certified; application-level accuracy budget/transfer not established.')
  csvrows.append(z)
  for p in json.loads((run/r['dataset']/r['arm']/'stability_probes.json').read_text()):
   probes.append({'dataset':r['dataset'],'arm':r['arm'],'exponent':p['exponent'],'sign':p['sign'],
    'prediction_RMS_change':p['prediction_RMS_change'],'rank_sign_changes':p['rank_sign_changes'],
    'certified_objective_gap_upper':p['exact_objective_gap_upper_bound']['outward_upper'],'is_refit':False})
 table(run/'arm_classification_table.csv',csvrows)
 table(run/'stability_probe_table.csv',probes)
 refs=json.loads((run/'saved_reference_comparison.json').read_text())['comparisons']
 table(run/'saved_reference_comparison.csv',[{'dataset':r['dataset'],
  'P00_objective':r['P00_objective']['float'],'saved_reference_objective':r['saved_reference_objective']['float'],
  'exact_objective_difference_reference_minus_P00':r['objective_difference_reference_minus_P00']['float'],
  'certified_P00_gap_upper':r['P00_gap_upper']['outward_upper'],'certified_reference_gap_upper':r['reference_gap_upper']['outward_upper'],
  'prediction_RMS_difference_float_diagnostic':r['prediction_RMS_difference_float_diagnostic'],
  'prediction_max_difference_float_diagnostic':r['prediction_max_difference_float_diagnostic'],
  'coefficient_l2_difference_float_diagnostic':r['coefficient_l2_difference_float_diagnostic'],
  'exact_rank_sign_differences':r['exact_rank_sign_differences']} for r in refs])
 crossing=Counter((r['certified_historical_LP_result'],r['classification']) for r in rows)
 table(run/'historical_vs_new_classification.csv',[{'certified_historical_gate':a,'new_protocol':b,'count':n} for (a,b),n in sorted(crossing.items())])
 before=json.loads((run/'protected_before.json').read_text());after=snapshot()
 preservation={'files_checked':len(before),'changed':[p for p in before if p in after and before[p]!=after[p]],
  'missing':sorted(before.keys()-after.keys()),'added_outside_validation_protocol':sorted(after.keys()-before.keys())}
 assert not any(preservation[k] for k in ['changed','missing','added_outside_validation_protocol'])
 dump(run/'final_preservation.json',preservation)
 assert (HERE/'VALIDATION_PROTOCOL_REPORT.md').is_file()
 dump(run/'source_sha256.json',{p.name:sha(p) for p in sorted(HERE.iterdir()) if p.is_file()})
 status={'status':'COMPLETE','recommendation':'B - Further numerical validation is required',
  'fitted_arms':len(rows),'known_anchors_not_fitted':23,'classification_counts':dict(Counter(r['classification'] for r in rows)),
  'exact_dual_certificates_independently_verified':validation['exact_certificates_passed'],
  'exact_probe_objectives_independently_verified':validation['probe_objectives_audited'],
  'minimum_certified_gap_upper':min(r['certified_gap_upper'] for r in rows),
  'maximum_certified_gap_upper':max(r['certified_gap_upper'] for r in rows),
  'protocol_and_generator_unchanged_since_execution_start':True,
  'no_samples':True,'no_refits':True,'no_continuation':True,'preservation':preservation}
 dump(run/'final_status.json',status)
 files=sorted(p for p in run.rglob('*') if p.is_file() and p.name!='SHA256_MANIFEST.json')
 manifest={p.relative_to(run).as_posix():{'sha256':sha(p),'bytes':p.stat().st_size} for p in files}
 dump(run/'SHA256_MANIFEST.json',manifest)
 for name,r in manifest.items():assert sha(run/name)==r['sha256']
 print(json.dumps(dict(status,verified_artifacts=len(manifest)),indent=2))


if __name__=='__main__':main()
