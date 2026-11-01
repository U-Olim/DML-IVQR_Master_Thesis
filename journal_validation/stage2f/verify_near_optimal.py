"""Independent exact verification of tangent-direction/rank-pattern proof."""
from pathlib import Path
from fractions import Fraction as F
import json,sys
import numpy as np
from verify import statistic,val,rec,SOURCE


def main():
 run=Path(sys.argv[1]);results=[]
 cutoff=F(float(np.fromfile(SOURCE/'cutoff.bin',dtype='<f8')[0]))
 for id in ['pilot_002_minus','pilot_006_truth']:
  folder=run/id;x=np.load(folder/'saved_inputs.npz')
  X=[[F(float(v)) for v in row] for row in x['X']];y=[F(float(v)) for v in x['y']];lam=[F(float(v)) for v in x['lambda_vector']]
  optimum=json.loads((folder/'exact_decimal_optimum.json').read_text())
  b=[F(int(z),int(optimum['beta_denominator'])) for z in optimum['beta_numerators']]
  e=[F(int(z),int(optimum['residual_denominator'])) for z in optimum['residual_numerators']]
  S=optimum['active_coefficients_zero_based'];T=[i-1 for i in optimum['tied_observations_one_based']];TS=set(T)
  decisions=[];proofs=[]
  for side in ['historical','independent']:
   c=json.loads((folder/('near_optimal_'+side+'_pattern.json')).read_text())
   d=[val(z) for z in c['direction']];delta=val(c['step']);epsilon=val(c['epsilon']);delta0=val(c['delta0_preserving_nontie_and_active_signs'])
   prediction=[sum((a*bb for a,bb in zip(row,d)),F(0)) for row in X]
   target=x[side+'_residual']<=0
   assert all(prediction[i]==(1 if target[i] else -1) for i in T)
   assert all(d[j]==0 for j in range(101) if j not in S)
   assert all(abs(delta0*d[j])<=abs(b[j])/2 for j in S)
   assert all(abs(delta0*prediction[i])<=abs(e[i])/2 for i in range(1000) if i not in TS)
   assert all((e[i]<=0)==bool(target[i]) for i in range(1000) if i not in TS)
   L=sum(map(abs,prediction))+sum(l*abs(t)/2 for l,t in zip(lam,d))
   assert L==val(c['objective_Lipschitz_direction_bound']) and L>0 and delta>0
   assert delta<=delta0 and delta<=epsilon/(2*L)
   beta=[F(int(z),int(c['beta_denominator'])) for z in c['beta_numerators']]
   assert beta==[a+delta*t for a,t in zip(b,d)]
   residual=[a-sum((xx*bb for xx,bb in zip(row,beta)),F(0)) for a,row in zip(y,X)]
   assert all((r<=0)==bool(t) for r,t in zip(residual,target))
   P=sum(((F(9,10) if r>=0 else F(-1,10))*r for r in residual),F(0))+sum(l*abs(t)/2 for l,t in zip(lam,beta))
   gap=P-val(optimum['primal']);assert gap>0 and gap<=epsilon/2 and gap==val(c['exact_positive_suboptimality'])
   scores=.9-np.array([r<=0 for r in residual]).astype(float)
   _,W=statistic(x['historical_psi'],scores);assert W==val(c['inference_fixed_historical_psi']['W'])
   assert W-cutoff==val(c['inference_fixed_historical_psi']['margin'])
   decisions.append(W<=cutoff);proofs.append({'pattern':side,'status':'PASS','gap':rec(gap),'W':rec(W)})
  assert decisions[0]!=decisions[1]
  results.append({'id':id,'status':'EXACT_GENERAL_DIRECTION_PROOF_VERIFIED','near_optimal_noninvariance_for_every_epsilon_positive':True,'witnesses':proofs})
 final={'status':'PASS','problems':2,'general_noninvariance_proofs':2,'specific_rational_witnesses':4,'cases':results}
 (run/'independent_near_optimal_validation.json').write_text(json.dumps(final,indent=2))
 print(json.dumps({k:v for k,v in final.items() if k!='cases'},indent=2))


if __name__=='__main__':main()
