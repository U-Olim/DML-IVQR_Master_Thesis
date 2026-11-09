"""Reporting and integrity only after the final resource stop. No fitting."""
import os,sys
sys.dont_write_bytecode=True
for key in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS']:os.environ[key]='1'
from pathlib import Path
import csv,json,collections,math
import numpy as np
P=Path(__file__).resolve().parent;ROOT=P.parents[2]
run=Path((P/'LATEST_RUN.txt').read_text().strip());os.environ['STAGE2H_RUN']=str(run)
from common_h0 import load,dump,sha,read,table
def rows(name):return list(csv.DictReader((run/name).open(encoding='utf-8')))
def main():
 raw=rows('raw_evaluations.csv');counts=dict(collections.Counter(r['status'] for r in raw))
 assert len(raw)==1440 and len({r['id'] for r in raw})==1440
 execution=load(run/'EXECUTION.json');summary=load(run/'SUMMARY.json')
 state={'status':'STOPPED_RESOURCE_ENVELOPE_INCOMPLETE','planned_unique_evaluations':1440,'attempted_unique_evaluations':summary['attempted'],'qualified_unique_evaluations':summary['qualified'],'status_counts':counts,'all_process_attempts_including_two_preserved_interruptions':execution['all_candidate_process_attempts'],'four_prespecified_replays_executed':0,'extra_statistical_samples_or_streams':0,'raw_inputs_complete_before_fitting':True,'calendar_elapsed_candidate_hours_including_interruptions':execution['elapsed_seconds']/3600,'deadline_utc':load(run/'INTERRUPTION_REPAIR_v2.json')['total_deadline_utc'],'numerical_worker_or_solver_policy_changed':False,'overall_aggregate_peak_memory':'unknown: initial supervisor samples lost; resumed PID-tree samples retained','resume_sampled_PID_tree_RSS_GiB':execution['memory']['sampled_tree_peak_RSS_bytes']/2**30,'resume_memory_limitations':'sampled sum, shared pages counted per process; PID parent-chain sampling over long interruptions may include PID-reuse attribution error; not a rigorous full-run maximum'}
 state['retained_run_bytes_before_final_reporting']=sum(f.stat().st_size for f in run.rglob('*') if f.is_file())
 prep=rows('inputs/preparation.csv');state['unique_preparation_penalty_calculations']=sum(r['arm']=='A' for r in prep)
 state['preparation_penalty_internal_seconds_excluding_replay']=sum(float(r['penalty_seconds']) for r in prep if r['arm']=='A')
 dump(run/'FINAL_STATUS.json',state)
 # Operationally unresolved numeric artifacts remain auditable; do not use them
 # as acceptance, rejection, or W observations in the scientific summaries.
 late=[]
 for r in raw:
  if r['status']!='TIME_LIMIT_UNRESOLVED':continue
  id=r['id'];f=run/'results/pilot'/id
  if not (f/'result.json').exists():f=run/'results/resume_v2'/id
  nr=load(f/'result.json');record={'id':id,'operational_status':'TIME_LIMIT_UNRESOLVED','raw_worker_status':nr['status'],'restored_to_scientific_qualification':False}
  if (f/'W.bin').exists() and (f/'score_sum.bin').exists():
   n=int(r['n']);s=read(f/'score.bin');psi=read(f/'psi.bin',(n,2));z=read(f/'observation_scores.bin',(n,2));g=read(f/'score_sum.bin');S=read(f/'second_moment.bin',(2,2))
   assert np.array_equal(s,float(r['tau'])-read(f/'rank.bin')) and np.array_equal(z,psi*s[:,None]) and np.array_equal(g,z.sum(axis=0)) and np.array_equal(S,z.T@z)
   assert float(g@np.linalg.solve(S,g))==float(read(f/'W.bin')[0]);record['saved_score_W_reconstruction']='PASS'
  else:record['saved_score_W_reconstruction']='NOT_AVAILABLE_AFTER_TIMEOUT; partial certificates retained'
  record['independent_audit_artifact']=str(next((p for p in [f/'independent_verification.json',f/'timeout_audit.json'] if p.exists()),'none'))
  late.append(record)
 table(run/'time_limit_numerical_validation.csv',late)
 # Report all three operational components separately.
 stats=rows('coverage_rejection_summary.csv');paired=rows('paired_comparisons.csv')
 truth500=[p for p in paired if p['n']=='500' and float(p['offset'])==0]
 section=['## What the completed n=500 cells show, and what remains missing','',
  'The fixed pilot did not complete. Of 1,440 planned unique evaluations, 1,069 were attempted and 1,064 qualified; five are TIME_LIMIT_UNRESOLVED and 371 RESOURCE_NOT_EXECUTED. There were 1,071 actual process attempts because two interrupted incomplete attempts were retained and resumed on the same input IDs. The four fixed reproducibility replays were not launched after resource exhaustion. No new statistical samples or streams were substituted. All 40 primitive samples and 720 paired input/penalty sets had been prepared and independently replayed before fitting.', '',
  'All six n=500 cells have 20 qualified truth observations per arm and 20 complete pairs. Bounded treatment raises observed truth inclusion in five cells and lowers it in the median/weak-instrument cell (1.00 to .90; paired difference −.10, MCSE .0688). With strong instruments, inclusion changes .85→1.00 at tau=.10 (paired +.15, MCSE .0819), .90→.95 at the median (+.05, MCSE .0500), and .75→.85 at tau=.90 (+.10, MCSE .1000). These are small-sample point estimates with pointwise exact intervals in the tables, not simultaneous evidence or proof of nominal coverage.', '',
  'The upper-tail strong-instrument cell therefore still has observed undercoverage under bounded treatment, while the weak-instrument median changes adversely. The bounded arm is not a universal coverage repair. Mean-W paired changes are also mixed: for example, the completed weak-instrument median has B−A mean W +.715 (MCSE .528), whereas the strong-instrument lower tail has −1.027 (MCSE .485). The direction is not uniform across quantiles/instrument strengths.', '',
  'Weak-instrument off-truth rejection remains low in the completed n=500 cells: original-arm frequencies range 0–.15 and bounded-arm frequencies 0–.10 at the two false candidates. At the strong-instrument median, both arms reject each false candidate in 19/20 samples (.95). Tail asymmetry persists: at tau=.10 with strong instruments, rejection at offsets −.50/+ .50 is .90/.20 in A and .75/.10 in B; at tau=.90 it is .20/.95 in A and .25/.90 in B. These describe the two fixed false candidates only; they do not establish interval geometry or global identification.', '',
  'The n=1000 truth cells have only 8–10 qualified observations per arm out of 20 planned. Their full-planned-design coverage and paired-effect bounds remain wide; all six paired coverage-difference bounds include zero. Qualified-only or complete-pair summaries are additional selected diagnostics and cannot be substituted for the missing full design. No dependent tau/kappa cells are pooled as new independent samples.', '',
  'This pattern survives the DGP change: weak-instrument power remains limited, tail behavior remains asymmetric, and statistical validity remains unsettled despite exact numerical qualification of completed fixed objectives. What changes is cell-dependent coverage, score levels and off-truth rejection. Affine relevance-scale changes (.90 covariance and .81 treatment variance) coexist with unchanged first-stage partial R²/F; the experiment does not isolate density regularity as the sole mechanism.', '',
  'The actual elapsed candidate period was '+f"{execution['elapsed_seconds']/3600:.3f}"+' calendar hours including host interruptions, exceeding the 12-hour envelope while the host was interrupted. The persistent deadline was not extended. At the next execution opportunity the driver stopped further fits and wrote all remaining IDs as not executed. The 2.52-hour base/5.04-hour planning allowance is not validated as the cost of a completed pilot by this interrupted run. Resumed sampled PID-tree RSS peaked at '+f"{state['resume_sampled_PID_tree_RSS_GiB']:.3f}"+' GiB; the full-run aggregate maximum is unknown. The PID-tree method is sampled and can overcount shared pages or misattribute reused process IDs over long interruptions. These are measurement limitations, not proof of a future memory bound.', '',
  'Retained run storage before final reporting is '+f"{state['retained_run_bytes_before_final_reporting']/2**30:.3f}"+' GiB, below the 20-GiB envelope. All 720 unique original 1,000-draw penalty calculations were performed during preparation, with '+f"{state['preparation_penalty_internal_seconds_excluding_replay']:.3f}"+' summed internal R seconds (excludes independent replay, process launch and I/O). Candidate execution/certification/audit component times are retained in raw result JSON and the qualified-only numerical diagnostics table; late/interrupted times are preserved rather than replaced by timing averages.', '',
  'Recommended next scientific task: map the retained score, historical variance-as-scale density proxy and ordinary transformed-intercept residualization to an explicit inference theorem, checking conditioning sets, nuisance orthogonality/rates and weak-instrument conditions. Any future attempt to finish or enlarge simulation after this final resource stop needs a new frozen execution protocol with a stable host and persistent wall-clock enforcement. Do not silently resume the 371 unexecuted IDs under an extended budget. The manuscript remains unchanged.', '']
 report=P/'STAGE2H_REPORT.md';text=report.read_text(encoding='utf-8')
 text=text.replace('# Stage 2H prespecified paired diagnostic pilot', '# Stage 2H paired diagnostic pilot — stopped at the resource guardrail',1)
 marker='## Partial-pilot truth inclusion bounds and paired comparisons'
 text=text.replace(marker,'\n'.join(section)+'\n'+marker,1)
 report.write_text(text,encoding='utf-8')
 versions=load(run/'environment.json');versions['HiGHS']='1.12.0';versions['R']='3.4.3';versions['hdm']='0.2.0';dump(run/'final_versions.json',versions)
 protected=load(run/'preservation.json');assert protected['status']=='PASS'
 backup=Path(load(run/'PREFLIGHT.json')['backup']);assert sha(backup)==load(run/'PREFLIGHT.json')['backup_sha256']
 dump(run/'FINAL_INTEGRITY.json',{'preservation':protected['status'],'external_historical_backup_hash':'PASS','no_candidate_process_launched_by_final_reporting':True,'all_planned_records_retained':len(raw),'versioned_operational_fixes_documented':True,'statistical_definitions_changed':False})
 # The finalizer has just hashed every retained raw artifact. Preserve that
 # complete manifest, then refresh only new files and the reporting files this
 # function changes; no candidate/input artifact is modified after that pass.
 prior_path=P/'SHA256_MANIFEST.json';prior=load(prior_path);prior_hash=sha(prior_path)
 archived=run/'SHA256_MANIFEST_BEFORE_REPORT_INTERPRETATION.json'
 with archived.open('xb') as f:f.write(prior_path.read_bytes())
 changed={str(report.relative_to(P)),Path(__file__).name,'RESOURCE_STOP_README.md'}
 changed.update(str((run/name).relative_to(P)) for name in ['FINAL_STATUS.json','time_limit_numerical_validation.csv','final_versions.json','FINAL_INTEGRITY.json'])
 manifest={};reused=refreshed=0
 for f in P.rglob('*'):
  if not f.is_file() or f.name=='SHA256_MANIFEST.json':continue
  key=str(f.relative_to(P));size=f.stat().st_size
  if key in prior and key not in changed and prior[key]['bytes']==size:manifest[key]=prior[key];reused+=1
  else:manifest[key]={'sha256':sha(f),'bytes':size};refreshed+=1
 update=run/'MANIFEST_UPDATE.json';dump(update,{'full_pass_manifest_sha256':prior_hash,'archived_full_pass_manifest':str(archived.relative_to(P)),'immutable_unchanged_raw_artifact_hashes_reused':reused,'new_or_modified_reporting_artifacts_hashed':refreshed,'candidate_artifacts_modified_after_full_pass':False})
 manifest[str(update.relative_to(P))]={'sha256':sha(update),'bytes':update.stat().st_size}
 dump(P/'SHA256_MANIFEST.json',manifest)
 print(json.dumps(state),flush=True)
if __name__=='__main__':main()
