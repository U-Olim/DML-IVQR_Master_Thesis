"""Separate coefficient rounding from same-coefficient residual arithmetic."""
from pathlib import Path
from fractions import Fraction as F
import json,sys
import numpy as np
from verify import statistic,rec,val


def main():
 run=Path(sys.argv[1]);results=[]
 for id in ['pilot_002_minus','pilot_006_truth']:
  folder=run/id;x=np.load(folder/'saved_inputs.npz');c=json.loads((folder/'exact_decimal_optimum.json').read_text())
  beta=np.fromfile(folder/'exact_optimum_nearest_binary64_beta.bin',dtype='<f8')
  exact_rounded=[F(float(y))-sum((F(float(a))*F(float(b)) for a,b in zip(row,beta)),F(0)) for y,row in zip(x['y'],x['X'])]
  R=np.fromfile(folder/'rounded_optimum_R_residual.bin',dtype='<f8')
  optimum=np.array([int(v)<=0 for v in c['residual_numerators']]);rounded=np.array([v<=0 for v in exact_rounded]);ranksR=R<=0
  definitions=[('rational_optimum_exact_residuals',optimum),('rounded_coefficients_exact_residuals',rounded),('rounded_coefficients_R_residuals',ranksR)]
  inferred={}
  for name,ranks in definitions:
   score=.9-ranks.astype(float);_,W=statistic(x['historical_psi'],score)
   inferred[name]={'frozen_historical_psi_W':rec(W)}
  result={'id':id,'coefficient_rounding_rank_changes':int(sum(rounded!=optimum)),
   'same_rounded_coefficients_R_vs_exact_algebra_rank_changes':int(sum(ranksR!=rounded)),
   'combined_representation_rank_changes':int(sum(ranksR!=optimum)),
   'R_exact_zero_residual_count':int(sum(R==0)),
   'exact_zero_residual_count_at_mathematical_optimum':sum(int(v)==0 for v in c['residual_numerators']),
   'inference':inferred,
   'scope':'Three diagnostic representations of one unique exact optimum, not a new fitted problem or implemented estimator policy.'}
  results.append(result)
 (run/'representation_split.json').write_text(json.dumps({'status':'COMPLETE','cases':results},indent=2))
 print(json.dumps([{'id':r['id'],'coefficient_rounding_rank_changes':r['coefficient_rounding_rank_changes'],
  'pure_arithmetic_rank_changes':r['same_rounded_coefficients_R_vs_exact_algebra_rank_changes']} for r in results],indent=2))


if __name__=='__main__':main()
