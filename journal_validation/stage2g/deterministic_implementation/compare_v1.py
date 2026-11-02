"""Three-path comparison and observed-runtime planning, without new samples."""
from common_v1 import *
def main():
 comparisons=rows(OUT/'candidate_comparison.csv');outcomes={r['id']:r for r in rows(OUT/'outcome_validation.csv')}
 calibration={r['id']:r for r in rows(OUT/'calibration_validation.csv')};times=[];metrics=[]
 for row in comparisons:
  id=row['id'];f=OUT/id
  if row['status']!='PASS':metrics.append({'id':id,'status':row['status']});continue
  coef=read(f/'instrument_coefficients.bin',(101,2));psi=read(f/'psi.bin',(1000,2));s=read(f/'score.bin');obs=psi*s[:,None]
  rank=read(f/'rank.bin');Apsi=read(E/id/'historical_psi.bin',(1000,2));As=read(E/id/'historical_score.bin')
  Acoef=read(f/'historical_instrument_coefficients.bin',(101,2));Ccoef=read(OLD/id/'C/instrument_coefficients.bin',(101,2))
  A_beta=read(E/id/'historical_beta.bin');A_e=read(E/id/'historical_residual.bin')
  B_beta=read(f/'outcome_beta_rounded.bin');C_beta=read(OLD/id/'C/outcome_beta_rounded.bin')
  accuracy=load(G/'results'/id/'accuracy.json')['historical']
  metrics.append(dict(row)|{'historical_outcome_true_gap':accuracy['true_gap']['float'],
   'proposed_LP_true_gap':float(outcomes[id]['LP_true_gap']),
   'historical_rank_disagreements_from_certified':int(np.sum((A_e<=0)!=rank)),
   'proposed_certified_rank_disagreements_from_C':int(np.sum(rank!=read(OLD/id/'C/rank.bin'))),
   'outcome_coefficient_max_change_from_historical':float(np.max(abs(B_beta-A_beta))),
   'rounded_outcome_coefficient_max_change_from_C':float(np.max(abs(B_beta-C_beta))),
   'instrument_coefficient_max_change_from_historical':float(np.max(abs(coef-Acoef))),
   'density_max_change_from_historical':float(np.max(abs(read(f/'density.bin')-read(E/id/'historical_density.bin')))),
   'density_max_change_from_C':float(np.max(abs(read(f/'density.bin')-read(OLD/id/'C/density.bin')))),
   'rank_score_changes_from_historical':int(np.sum(s!=As)),
   'observation_score_max_change_from_historical':float(np.max(abs(obs-Apsi*As[:,None]))),
   'score_sum_max_change_from_historical':float(np.max(abs(obs.sum(axis=0)-(Apsi*As[:,None]).sum(axis=0))))})
  o=outcomes[id];r=calibration[id]
  # Single production-like evaluation, excluding repeat/audit/development I/O.
  point=float(o['LP_seconds'])+float(r['density_seconds'])+float(r['native_calibration_seconds'])+float(row['instrument_solver_seconds'])
  qualified=point+float(o['outcome_exact_seconds'])+float(row['instrument_exact_seconds'])
  # Exact W and interval assembly is included in observed instrument-phase total;
  # isolate its residual overhead conservatively (includes validation I/O/repeats).
  inst=rows(OUT/'instrument_validation.csv');repeats=sum(float(v['repeat_seconds']) for v in inst if v['id']==id)
  remainder=max(0,float(row['instrument_phase_total_seconds'])-float(row['instrument_solver_seconds'])-float(row['instrument_exact_seconds'])-repeats)
  qualified+=remainder
  times.append({'id':id,'n':1000,'controls':100,'outcome_LP_seconds':float(o['LP_seconds']),
   'outcome_exact_seconds':float(o['outcome_exact_seconds']),'native_calibration_seconds':float(r['native_calibration_seconds']),
   'final_instrument_solver_seconds':float(row['instrument_solver_seconds']),'final_instrument_certificate_seconds':float(row['instrument_exact_seconds']),
   'inference_and_validation_overhead_seconds':remainder,'point_pipeline_seconds':point,
   'qualified_pipeline_proxy_seconds':qualified,'scope':'Observed component sum; excludes pivotal penalty simulation, data generation and separate independent audit'})
 table(OUT/'three_path_comparison.csv',metrics);table(OUT/'runtime_benchmarks.csv',times)
 storage=[{'id':id,'candidate_payload_bytes':sum(p.stat().st_size for p in (OUT/id).rglob('*') if p.is_file()),
  'scope':'Current retained per-candidate inputs/certificates/results, including retained development notes; shared manifests/logs excluded'} for id in cases()]
 table(OUT/'storage_benchmarks.csv',storage);payload=float(np.mean([r['candidate_payload_bytes'] for r in storage]))
 qualified=[r['qualified_pipeline_proxy_seconds'] for r in times];point=[r['point_pipeline_seconds'] for r in times]
 independent=load(OUT/'independent_verification.json');mean=float(np.mean(qualified));p95=float(np.quantile(qualified,.95));plans=[]
 audit_mean=independent['seconds']/24
 for name,N in [('40 samples, one tau/kappa, 41-candidate DML profiles',40*41),
                 ('500 samples, 5 tau, 4 kappa, 41 candidates; ONE sample size',500*5*4*41),
                 ('Same design across BOTH n=500 and n=1000',2*500*5*4*41)]:
  plans.append({'scenario':name,'candidate_evaluations':N,'mean_seconds_per_candidate_proxy':mean,
    'serial_hours_proxy':N*mean/3600,'ideal_5_worker_hours_proxy':N*mean/3600/5,
    'serial_hours_using_panel_p95':N*p95/3600,
    'serial_hours_if_independent_audit_every_candidate':N*(mean+audit_mean)/3600,
    'retained_candidate_storage_GiB_proxy':N*payload/1024**3,
    'limitations':'DML candidate component only; n500 unmeasured, assumes n1000 cost; no parallel scaling benchmark, penalty simulation, other estimators or new-DGP costs'})
 table(OUT/'runtime_projections.csv',plans)
 dump(OUT/'summary.json',{'cases':24,'passed':sum(r['status']=='PASS' for r in comparisons),
  'unresolved':sum(r['status']!='PASS' for r in comparisons),
  'Policy_C_decision_disagreements':sum(r.get('decision_agrees_Policy_C')=='False' for r in comparisons),
  'historical_decision_disagreements':sum(r.get('decision_agrees_historical')=='False' for r in comparisons),
  'certified_rank_disagreements_from_C':sum(int(r['proposed_certified_rank_disagreements_from_C']) for r in metrics if r['status']=='PASS'),
  'raw_LP_sign_disagreements':sum(int(r['LP_raw_sign_disagreements']) for r in outcomes.values() if r['status']=='PASS'),
  'max_LP_true_gap':max(float(r['LP_true_gap']) for r in outcomes.values() if r['status']=='PASS'),
  'max_LP_fitted_error':max(float(r['LP_fitted_max_error']) for r in outcomes.values() if r['status']=='PASS'),
  'max_abs_W_change_from_C':max(abs(float(r['W_change_from_C'])) for r in comparisons if r['status']=='PASS'),
  'max_W_interval_width':max(float(r['W_upper'])-float(r['W_lower']) for r in comparisons if r['status']=='PASS'),
  'mean_point_pipeline_seconds':float(np.mean(point)),'mean_qualified_pipeline_proxy_seconds':mean,
  'p95_qualified_pipeline_proxy_seconds':p95,'independent_audit_seconds':independent['seconds'],
  'independent_audit_mean_seconds':audit_mean,'mean_retained_candidate_payload_bytes':payload,
  'n500_directly_benchmarked':False,'readiness':'CONDITIONAL'})
if __name__=='__main__':main()
