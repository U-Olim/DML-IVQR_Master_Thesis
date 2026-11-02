from common_h0 import *
def main():
 design=tasks();validation=[];bench=[];relevance=[]
 phases=load(OUT/'phases.json');phase={r['mode']:r for r in phases}
 prep={r['id']:r for r in rows(INPUT/'preparation.csv')}
 seq=[]
 for d in design:
  id=d['id'];runs={mode:load(OUT/mode/id/'result.json') for mode in ['sequential','repeat','parallel']}
  r=runs['sequential'];seq.append(r);passed=all(v['status']=='PASS' for v in runs.values())
  identical=bool(passed and all(runs[m]['fingerprints']==r['fingerprints'] for m in ['repeat','parallel']))
  validation.append({'id':id,'n':d['n'],'tau':d['tau'],'kappa':d['kappa'],
   'sequential_status':r['status'],'repeat_status':runs['repeat']['status'],'parallel_status':runs['parallel']['status'],
   'all_numerical_fingerprints_identical':identical,'certified_signs':r.get('certified_residual_signs',0),
   'raw_LP_sign_disagreements':r.get('raw_LP_sign_disagreements',''),
   'W':r.get('W',''),'native_C_W':r.get('native_C_W',''),'W_lower':r.get('W_lower',''),'W_upper':r.get('W_upper',''),
   'accepted':r.get('accepted',''),'decision_matches_exact_reference':r.get('W_consistent_with_exact_reference',False),
   'decision_matches_native_C':bool(passed and ((r['native_C_W']<=r['cutoff'])==r['accepted'])),
   'W_reconstruction_error':r.get('W_reconstruction_error',''),'S_condition':r.get('S_condition',''),
   'error':r.get('error','')})
  for mode,x in runs.items():
   folder=OUT/mode/id
   cert=sum(x.get(k,0) for k in ['outcome_certificate_seconds','instrument_certificate_seconds','inference_certificate_seconds'])
   bench.append({'id':id,'mode':mode,'n':d['n'],'tau':d['tau'],'kappa':d['kappa'],'status':x['status'],
    'outcome_solve_seconds':x.get('outcome_solve_seconds',''),'native_calibration_R_process_seconds':x.get('calibration_process_seconds',''),
    'instrument_solve_seconds':x.get('instrument_solve_seconds',''),'certificate_seconds':cert,
    'independent_audit_seconds':x.get('independent_audit_seconds',''),'total_worker_candidate_seconds':x['total_candidate_seconds'],
    'sampled_candidate_tree_peak_RSS_MiB':x['memory']['sampled_tree_peak_RSS_bytes']/2**20,
    'worker_OS_peak_working_set_MiB':x['own_OS_memory']['OS_peak_working_set']/2**20,
    'observed_max_process_OS_peak_MiB':max(x['memory']['observed_OS_peak_working_set_by_PID'].values())/2**20,
    'output_payload_bytes':sum(p.stat().st_size for p in folder.rglob('*') if p.is_file()),
    'original_input_payload_bytes':sum(p.stat().st_size for p in (INPUT/id).rglob('*') if p.is_file())})
  X=read(INPUT/id/'X_row_major.bin',(int(d['n']),101));D=read(INPUT/id/'D.bin');Z=read(INPUT/id/'Z_row_major.bin',(int(d['n']),2))
  Q=Z-np.column_stack([X[:,[2,3,4]].sum(axis=1),X[:,[7,8,9,10]].sum(axis=1)])
  r0=D-X@np.linalg.lstsq(X,D,rcond=None)[0];A=np.column_stack([X,Z]);r1=D-A@np.linalg.lstsq(A,D,rcond=None)[0]
  rss0=float(r0@r0);rss1=float(r1@r1);partial=(rss0-rss1)/rss0
  relevance.append({'id':id,'n':d['n'],'tau':d['tau'],'kappa':d['kappa'],
   'sample_cov_D_Q1':float(np.cov(D,Q[:,0],ddof=1)[0,1]),'sample_cov_D_Q2':float(np.cov(D,Q[:,1],ddof=1)[0,1]),
   'partial_first_stage_R2':partial,'conventional_first_stage_F':((rss0-rss1)/2)/(rss1/(int(d['n'])-103)),
   'residual_df':int(d['n'])-103,'interpretation':'original DGP one diagnostic sample per n; diagnostic only, no weak-IV or population-rate proof'})
 table(OUT/'numerical_validation.csv',validation);table(OUT/'runtime_storage_memory.csv',bench);table(OUT/'instrument_relevance.csv',relevance)
 parallel=phase['parallel'];sequential=phase['sequential'];speed=sequential['wall_seconds']/parallel['wall_seconds']
 cohorts=[{'mode':m,'workers':phase[m]['workers'],'cases':12,'wall_seconds':phase[m]['wall_seconds'],
  'sampled_tree_peak_RSS_MiB':phase[m]['memory']['sampled_tree_peak_RSS_bytes']/2**20,
  'sample_interval_seconds':phase[m]['memory']['sampling_seconds']} for m in ['sequential','repeat','parallel']]
 table(OUT/'cohort_benchmarks.csv',cohorts)
 # Include measured process-launch/monitor overhead, not just inner solver time.
 overhead=max(0,sequential['wall_seconds']-sum(r['total_candidate_seconds'] for r in seq))/12
 prep_allowance=phase['prepare']['wall_seconds']/12
 budgets=[]
 for factor in [1.,2.]:
  serial=0;payload=0
  for d in design:
   id=d['id'];r=load(OUT/'sequential'/id/'result.json');ncase=r['total_candidate_seconds']+overhead
   pairs=20*3
   # Shared original penalty draw per A/B pair, candidate cost for both arms.
   prep_cost=max(prep_allowance,float(prep[id]['penalty_seconds']))
   serial+=pairs*(2*ncase+prep_cost)
   bb=next(v for v in bench if v['mode']=='sequential' and v['id']==id)
   payload+=pairs*2*(bb['output_payload_bytes']+bb['original_input_payload_bytes'])
  budgets.append({'planning_factor':factor,'replications_per_cell':20,'cells':12,'arms':2,'candidates_per_profile':3,
   'total_candidate_evaluations':1440,'serial_hours':factor*serial/3600,
   'two_worker_hours_using_observed_speedup':factor*serial/3600/speed,
   'retained_storage_GiB':factor*payload/2**30,
   'provisioned_memory_GiB':max(2.,factor*parallel['memory']['sampled_tree_peak_RSS_bytes']/2**30),
   'limitations':'Bounded arm and off-truth costs not measured; original-input duplication charged conservatively; planning factor is not a mathematical bound'})
 table(OUT/'pilot_budget.csv',budgets)
 allpass=all(v['sequential_status']==v['repeat_status']==v['parallel_status']=='PASS' and v['all_numerical_fingerprints_identical'] for v in validation)
 summary={'diagnostic_cells':12,'primitive_samples':2,'candidate_executions_in_measured_cohorts':36,'additional_same_input_smoke_execution':1,'passed_executions':sum(r['status']=='PASS' for r in bench),
  'all_12_cells_pass_and_repeat_bitwise':allpass,'certified_signs_per_execution_panel':sum(int(v['certified_signs']) for v in validation),
  'raw_LP_sign_disagreements_in_sequential_panel':sum(int(v['raw_LP_sign_disagreements']) for v in validation if v['sequential_status']=='PASS'),
  'native_C_decision_disagreements':sum(not v['decision_matches_native_C'] for v in validation),
  'max_W_reconstruction_error':max(float(v['W_reconstruction_error']) for v in validation if v['sequential_status']=='PASS'),
  'max_W_interval_width':max(float(v['W_upper'])-float(v['W_lower']) for v in validation if v['sequential_status']=='PASS'),
  'mean_candidate_seconds_n500':float(np.mean([r['total_candidate_seconds'] for r in seq if r['n']==500])),
  'mean_candidate_seconds_n1000':float(np.mean([r['total_candidate_seconds'] for r in seq if r['n']==1000])),
  'mean_certification_seconds':float(np.mean([r['certificate_seconds'] for r in bench if r['mode']=='sequential'])),
  'mean_independent_audit_seconds':float(np.mean([r['independent_audit_seconds'] for r in bench if r['mode']=='sequential'])),
  'sequential_cohort_seconds':sequential['wall_seconds'],'two_worker_cohort_seconds':parallel['wall_seconds'],'observed_two_worker_speedup':speed,
  'sequential_peak_tree_RSS_MiB':sequential['memory']['sampled_tree_peak_RSS_bytes']/2**20,
  'two_worker_peak_tree_RSS_MiB':parallel['memory']['sampled_tree_peak_RSS_bytes']/2**20,
  'mean_output_MiB_per_candidate':float(np.mean([r['output_payload_bytes']/2**20 for r in bench if r['mode']=='sequential'])),
  'analytical_verification_status':load(OUT/'analytical_verification.json')['status'],
  'readiness':'READY_FOR_LIMITED_DIAGNOSTIC_PILOT' if allpass else 'CONDITIONAL_NUMERICAL_FAILURES_RETAINED',
  'scope':'No bounded-DGP implementation or Monte Carlo pilot executed; theoretical inference assumptions remain explicitly open'}
 dump(OUT/'summary.json',summary)
 print(json.dumps(summary,indent=2),flush=True)
if __name__=='__main__':main()
