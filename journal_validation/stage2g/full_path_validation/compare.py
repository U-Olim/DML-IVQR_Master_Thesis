"""Complete panel comparisons and near-optimal full-path summaries."""
from common import *

def main():
 cases=json.loads((G/'results/cases.json').read_text());audit=list(csv.DictReader((OUT/'downstream_audit.csv').open()));table24=[];near=[]
 cutoff=F(float(readbin(E/'cutoff.bin')[0]))
 for case in cases:
  id=case['id'];src=E/id;folder=OUT/id/'C';cert=json.loads((G/'results'/id/'exact_optimum.json').read_text())
  bC=[F(int(z),int(cert['beta_denominator'])) for z in cert['beta_numerators']]
  vectors={}
  for policy,side in [('A','historical'),('B','independent')]:
   residual=readbin(src/(side+'_residual.bin'));s=.9-(residual<=0).astype(float);psi=readbin(src/(side+'_psi.bin'),(1000,2))
   vectors[policy]={'beta':[F(float(v)) for v in readbin(src/(side+'_beta.bin'))],'rank':residual<=0,'density':readbin(src/(side+'_density.bin')),'psi':psi,'score':s,'obs':psi*s[:,None],'inference':exact_W(psi,s,cutoff)}
  psi=readbin(folder/'psi.bin',(1000,2));s=readbin(folder/'score.bin')
  vectors['C']={'beta':bC,'rank':readbin(folder/'rank.bin').astype(bool),'density':readbin(folder/'density.bin'),'psi':psi,'score':s,'obs':psi*s[:,None],'inference':exact_W(psi,s,cutoff)}
  row={'id':id,'candidate':next(r['candidate'] for r in csv.DictReader((E/'complete_24_problem_table.csv').open()) if r['id']==id)}
  for p in ['A','B','C']:
   row[p+'_W']=vectors[p]['inference']['W']['float'];row[p+'_accepted']=vectors[p]['inference']['accepted']
  for left,right in [('A','B'),('A','C'),('B','C')]:
   a=vectors[left];b=vectors[right];prefix=left+'_'+right+'_'
   row[prefix+'outcome_coefficient_max']=float(max(abs(v-w) for v,w in zip(a['beta'],b['beta'])))
   row[prefix+'rank_changes']=int(np.sum(a['rank']!=b['rank']))
   for key in ['density','psi','score','obs']:row[prefix+key+'_max_difference']=float(np.max(abs(a[key]-b[key])))
   row[prefix+'delta_W_right_minus_left']=b['inference']['W']['float']-a['inference']['W']['float'];row[prefix+'decision_changed']=a['inference']['accepted']!=b['inference']['accepted']
  C_audit=next(r for r in audit if r['id']==id and r['variant']=='C')
  row.update(C_fixed_penalty_decision_certificate=C_audit['decision_bound_status'],C_W_lower=float(C_audit['W_lower']),C_W_upper=float(C_audit['W_upper']),C_downstream_status=C_audit['status'],
   A_certification='Saved path reconstructed; exact conditional W and Stage 2G outcome accuracy certificate',B_certification='Saved independent path reconstructed; exact conditional W and Stage 2G outcome accuracy certificate',C_certification='Exact outcome/signs; native full path reproduced; exact final-penalty instrument optima and conditional decision bounds; density/adaptive propagation not interval-certified')
  table24.append(row);dump(OUT/id/'complete_path_inference.json',{p:vectors[p]['inference'] for p in ['A','B','C']})
  if case['positive_budget_noninvariance_witness']:
   frozen=json.loads((G/'results'/id/'sensitivity.json').read_text())
   for power in [8,20]:
    result={'id':id,'objective_budget':f'1e-{power}','exact_optimum_C_W':row['C_W'],'exact_optimum_C_accepted':row['C_accepted']}
    for side in ['minimum','maximum']:
     q=OUT/id/f'{side}_e{power}';rec=next(r for r in audit if r['id']==id and r['variant']==f'{side}_e{power}');oc=json.loads((q/'outcome_certificate.json').read_text())
     result[side+'_fixed_historical_W']=frozen[side+'_found']['W']['float'];result[side+'_full_W']=float(rec['W']);result[side+'_full_accepted']=rec['accepted']=='True'
     result[side+'_true_outcome_gap']=val(oc['gap']).__float__();result[side+'_downstream_bound_status']=rec['decision_bound_status']
     result[side+'_density_change_from_C']=float(np.max(abs(readbin(q/'density.bin')-vectors['C']['density'])))
     result[side+'_psi_change_from_C']=float(np.max(abs(readbin(q/'psi.bin',(1000,2))-vectors['C']['psi'])))
    result['opposite_decisions_persist']=result['minimum_full_accepted']!=result['maximum_full_accepted'];near.append(result)
 table(OUT/'complete_24_problem_comparison.csv',table24);table(OUT/'near_optimal_full_path_comparison.csv',near)
 summary={'cases':24,'paths':len(audit),'native_failures_or_partial_audits':sum(r['status']!='PASS' for r in audit),
  'AB_decision_changes':sum(r['A_B_decision_changed'] for r in table24),'AC_decision_changes':sum(r['A_C_decision_changed'] for r in table24),'BC_decision_changes':sum(r['B_C_decision_changed'] for r in table24),
  'near_pairs':len(near),'opposite_pairs':sum(r['opposite_decisions_persist'] for r in near),'all_fixed_penalty_decision_bounds_conclusive':all(r['decision_bound_status'] in ['ACCEPT_CERTIFIED','REJECT_CERTIFIED'] for r in audit),
  'density_max_relative_error':max(float(r['density_relative_error']) for r in audit),'max_instrument_true_gap':max(float(r['instrument_max_true_gap']) for r in audit),
  'max_instrument_coefficient_error':max(float(r['instrument_max_coefficient_error']) for r in audit),'max_W_reconstruction_error':max(float(r['W_R_error']) for r in audit),
  'max_S_condition':max(float(r['S_condition']) for r in audit),'max_inverse_residual':max(float(r['inverse_residual']) for r in audit),
  'max_reference_W_change':max(abs(float(r['fixed_penalty_reference_W'])-float(r['W'])) for r in audit),
  'reference_decision_changes':sum(r['fixed_penalty_reference_accepted']!=r['accepted'] for r in audit)}
 dump(OUT/'summary.json',summary);print(json.dumps(summary,indent=2))
if __name__=='__main__':main()
