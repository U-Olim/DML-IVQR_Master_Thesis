"""Analytic near-optimal rank-pattern witnesses, only the two fixed objectives."""
from pathlib import Path
from fractions import Fraction as F
import json,sys
import numpy as np
from analyze import integer_solve_rational_rhs,exact_objective,dyadic,record,dump,exact_W,SOURCE


def unpack(r):return F(int(r['numerator']),int(r['denominator']))


def main():
 run=Path(sys.argv[1]);summaries=json.loads((run/'case_summaries.json').read_text());results=[]
 for summary in summaries:
  if summary['status']!='EXACT_OPTIMUM_RECONSTRUCTED':continue
  id=summary['id'];folder=run/id;x=np.load(folder/'saved_inputs.npz')
  X=x['X'];y=x['y'];lam=[F(float(t)) for t in x['lambda_vector']]
  c=json.loads((folder/'exact_decimal_optimum.json').read_text());assert c['unique_beta_and_fitted_values']
  S=c['active_coefficients_zero_based'];T=[i-1 for i in c['tied_observations_one_based']];Tset=set(T)
  beta=[F(int(z),int(c['beta_denominator'])) for z in c['beta_numerators']]
  residual=[F(int(z),int(c['residual_denominator'])) for z in c['residual_numerators']]
  xx,EX=dyadic(X);yy,EY=dyadic(y);Xi=xx.tolist();yi=yy.tolist();A=[[Xi[i][j] for j in S] for i in T]
  proofs=[]
  for side in ['historical','independent']:
   target=x[side+'_residual']<=0
   assert all((residual[i]<=0)==target[i] for i in range(1000) if i not in Tset)
   z=[-1 if target[i] else 1 for i in T]
   direction=[F(0)]*101
   solution=integer_solve_rational_rhs(A,[F(-v*(1 << EX)) for v in z])
   for j,d in zip(S,solution):direction[j]=d
   predictions=[sum((F(a,1 << EX)*d for a,d in zip(row,direction)),F(0)) for row in Xi]
   assert [predictions[i] for i in T]==[F(-v) for v in z]
   delta0=F(1)
   for j in S:
    if direction[j]:delta0=min(delta0,abs(beta[j])/(2*abs(direction[j])))
   for i in range(1000):
    if i not in Tset and predictions[i]:delta0=min(delta0,abs(residual[i])/(2*abs(predictions[i])))
   lipschitz=sum(map(abs,predictions))+sum(l*abs(d)/2 for l,d in zip(lam,direction))
   assert delta0>0 and lipschitz>0
   epsilon=F(1,10**20);step=min(delta0,epsilon/(2*lipschitz))
   candidate=[b+step*d for b,d in zip(beta,direction)]
   P,e,D,_,_,bn,L=exact_objective(Xi,EX,yi,EY,candidate,lam,F(9,10))
   optimum=unpack(c['primal']);gap=P-optimum
   assert gap>0 and gap<=epsilon/2 and all((r<=0)==bool(t) for r,t in zip(e,target))
   scores=.9-np.array([v<=0 for v in e]).astype(float)
   # Fixed historical psi only: this is a proved near-optimal outcome-direction result.
   cutoff=F(float(np.fromfile(SOURCE/'cutoff.bin',dtype='<f8')[0]));inf=exact_W(x['historical_psi'],scores,cutoff)
   expected=json.loads((folder/'inference.json').read_text())['historical' if side=='historical' else 'independent_layer_A']
   assert unpack(inf['W'])==unpack(expected['W'])
   proof={'target_rank_pattern':side,'status':'EXACT_NEAR_OPTIMAL_WITNESS','epsilon':record(epsilon),
    'step':record(step),'delta0_preserving_nontie_and_active_signs':record(delta0),
    'objective_Lipschitz_direction_bound':record(lipschitz),
    'direction':[record(d) for d in direction],
    'beta_numerators':[str(v) for v in bn],'beta_denominator':str(L),
    'primal':record(P),'exact_positive_suboptimality':record(gap),
    'all_1000_target_ranks_verified':True,'inference_fixed_historical_psi':inf,
    'general_proof':'For every epsilon>0 choose 0<step<=min(delta0,epsilon/(2*L)). Nontie and active signs stay fixed, tied residual signs equal target, and 0<Q-Q*<=epsilon/2. Therefore both opposite W patterns occur arbitrarily near the unique optimum in objective value.',
    'scope':'Mathematical rational witnesses; not new fitted estimates, representable-double claims, full-path limits, or production solution-selection rules.'}
   dump(folder/('near_optimal_'+side+'_pattern.json'),proof);proofs.append(proof)
  assert proofs[0]['inference_fixed_historical_psi']['accepted']!=proofs[1]['inference_fixed_historical_psi']['accepted']
  results.append({'id':id,'status':'PROVED','frozen_inference_noninvariant_for_every_positive_objective_budget':True,
   'epsilon_demonstrated':'1e-20','witness_gaps':[p['exact_positive_suboptimality']['float'] for p in proofs]})
 dump(run/'near_optimal_set_summary.json',{'status':'COMPLETE','cases':results})
 print(json.dumps(results,indent=2))


if __name__=='__main__':main()
