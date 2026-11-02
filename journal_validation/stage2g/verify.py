"""Independent Fraction arithmetic audit; no reconstruction routine is imported."""
from pathlib import Path
from fractions import Fraction as F
import json,sys,time
import numpy as np
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[1]
sys.path.insert(0,str(ROOT/'journal_validation/stage2f'))
from verify import det_fraction,statistic

def value(r):return F(int(r['numerator']),int(r['denominator']))
def main():
 start=time.perf_counter();out=HERE/'results';source=ROOT/'journal_validation/stage2e/output/paired_20261029T093009Z'
 cutoff=F(float(np.fromfile(source/'cutoff.bin',dtype='<f8')[0]));results=[]
 for case in json.loads((out/'cases.json').read_text()):
  id=case['id'];folder=out/id;src=source/id
  if not case['exact_unique']:
   results.append({'id':id,'status':'UNCERTIFIED'});continue
  c=json.loads((folder/'exact_optimum.json').read_text());tau=value(c['tau'])
  X=[[F(float(a)) for a in row] for row in np.fromfile(src/'X_row_major.bin',dtype='<f8').reshape(1000,101)]
  y=list(map(lambda a:F(float(a)),np.fromfile(src/'response.bin',dtype='<f8')))
  lam=list(map(lambda a:F(float(a)),np.fromfile(src/'lambda.bin',dtype='<f8')))
  beta=[F(int(a),int(c['beta_denominator'])) for a in c['beta_numerators']]
  dual=[F(int(a),int(c['dual_denominator'])) for a in c['dual_numerators']]
  e=[v-sum((a*b for a,b in zip(row,beta)),F(0)) for row,v in zip(X,y)]
  assert e==[F(int(a),int(c['residual_denominator'])) for a in c['residual_numerators']]
  grad=[sum((row[j]*v for row,v in zip(X,dual)),F(0)) for j in range(101)]
  assert all(tau-1<=v<=tau for v in dual)
  assert all(abs(g)<=l/2 for g,l in zip(grad,lam))
  primal=sum(((tau if r>=0 else tau-1)*r for r in e),F(0))+sum((l*abs(b)/2 for l,b in zip(lam,beta)),F(0))
  assert primal==sum((a*b for a,b in zip(y,dual)),F(0))==value(c['primal'])==value(c['dual'])
  T=[i for i,r in enumerate(e) if not r];S=[j for j,b in enumerate(beta) if b]
  assert all(tau-1<dual[i]<tau for i in T)
  assert all(abs(grad[j])<lam[j]/2 for j in range(101) if j not in S)
  assert len(T)==len(S) and det_fraction([[X[i][j] for j in S] for i in T])!=0
  accuracy=json.loads((folder/'accuracy.json').read_text())
  for side in ['historical','independent']:
   b=[F(float(a)) for a in np.fromfile(src/(side+'_beta.bin'),dtype='<f8')]
   re=[v-sum((a*z for a,z in zip(row,b)),F(0)) for row,v in zip(X,y)]
   P=sum(((tau if r>=0 else tau-1)*r for r in re),F(0))+sum((l*abs(z)/2 for l,z in zip(lam,b)),F(0))
   assert P==value(accuracy[side]['primal']) and P-primal==value(accuracy[side]['true_gap'])>=0
  inference=json.loads((folder/'inference.json').read_text());checks=0
  for policy,record in inference.items():
   if policy=='A':rank=np.fromfile(src/'historical_residual.bin',dtype='<f8')<=0
   elif policy.startswith('B'):rank=np.fromfile(src/'independent_residual.bin',dtype='<f8')<=0
   elif policy.startswith('D'):rank=np.array([r<0 for r in e])
   else:rank=np.array([r<=0 for r in e])
   side='independent' if policy in ['B_float_saved_path','C_exact_saved_independent_psi'] else 'historical'
   psi=np.fromfile(src/(side+'_psi.bin'),dtype='<f8').reshape(1000,2)
   stats,W=statistic(psi,.9-rank.astype(float))
   assert W==value(record['W']) and (W<=cutoff)==record['accepted']
   for key,v in zip(['score_sum_1','score_sum_2','S11','S12','S22'],stats):assert v==value(record[key])
   checks+=1
  sensitivity=json.loads((folder/'sensitivity.json').read_text());hp=np.fromfile(src/'historical_psi.bin',dtype='<f8').reshape(1000,2)
  for label in ['minimum','maximum']:
   rank=sensitivity[label+'_rank'];assert all(rank[i]==(e[i]<=0) for i in range(1000) if i not in T)
   _,W=statistic(hp,.9-np.array(rank).astype(float));assert W==value(sensitivity[label+'_found']['W'])
  # Invertible tied/active basis realizes ANY chosen nonzero tied residual direction.
  # Continuity preserves other signs, and the objective is globally Lipschitz along it.
  results.append({'id':id,'status':'PASS','unique_exact_optimum':True,'inference_records':checks,'local_pattern_realizability_proof':'nonsingular tied/active basis, nonzero nontie residuals, finite Lipschitz loss','positive_budget_noninvariance_witness':sensitivity['opposite_decisions_found']})
  print('AUDIT_PASS',id,flush=True)
 (out/'independent_audit.json').write_text(json.dumps({'cases':results,'seconds':time.perf_counter()-start,'status':'PASS' if all(r['status']=='PASS' for r in results) else 'PARTIAL'},indent=2))
if __name__=='__main__':main()
