"""Supplementary exact-residual diagnostics; original R inference is unchanged."""
from fractions import Fraction as F
from pathlib import Path
import csv,json,sys
import numpy as np
from run_stage2e import methods,dyadic,dump,table,read
from verify import exactW


def main():
 out=Path(sys.argv[1]);rows=[];cutoff=F(float(np.fromfile(out/'cutoff.bin',dtype='<f8')[0]))
 for task in read(out/'task_manifest.csv'):
  folder=out/task['id'];X=np.fromfile(folder/'X_row_major.bin',dtype='<f8').reshape(1000,101)
  xx,EX=dyadic(X);Xi=xx.tolist();y=np.fromfile(folder/'response.bin',dtype='<f8');lam=np.fromfile(folder/'lambda.bin',dtype='<f8')
  record={'id':task['id']};signs={};scores={}
  for side in ['historical','independent']:
   b=np.fromfile(folder/(side+'_beta.bin'),dtype='<f8');e=np.fromfile(folder/(side+'_residual.bin'),dtype='<f8')
   rational,E,_,_,_=methods.primal_parts(Xi,EX,y,b,lam);truth=np.array([r<=0 for r in rational]);signs[side]=truth
   scores[side]=.9-truth.astype(float)
   differences=truth!=(e<=0)
   record[side+'_R_exact_zero']=int(sum(e==0));record[side+'_exact_arithmetic_zero']=sum(r==0 for r in rational)
   record[side+'_R_vs_exact_sign_differences']=int(sum(differences))
   record[side+'_maximum_R_residual_abs_at_sign_disagreement']=float(max(abs(e[differences]))) if differences.any() else 0.
   record[side+'_minimum_R_residual_magnitude']=float(min(abs(e)))
   for t in [1e-12,1e-10,1e-8,1e-7,1e-6]:record[side+'_abs_residual_le_'+str(t)]=int(sum(abs(e)<=t))
  record['paired_exact_arithmetic_rank_changes']=int(sum(signs['historical']!=signs['independent']))
  he=np.fromfile(folder/'historical_residual.bin',dtype='<f8');ie=np.fromfile(folder/'independent_residual.bin',dtype='<f8');changed=(he<=0)!=(ie<=0)
  record['paired_R_rank_changes']=int(sum(changed))
  record['maximum_H_R_residual_abs_at_paired_sign_change']=float(max(abs(he[changed]))) if changed.any() else 0.
  record['maximum_I_R_residual_abs_at_paired_sign_change']=float(max(abs(ie[changed]))) if changed.any() else 0.
  hp=np.fromfile(folder/'historical_psi.bin',dtype='<f8').reshape(1000,2);ip=np.fromfile(folder/'independent_psi.bin',dtype='<f8').reshape(1000,2)
  W=[exactW(hp,scores['historical']),exactW(hp,scores['independent']),exactW(ip,scores['independent'])]
  for w,label in zip(W,['H','A_independent','B_independent']):
   record['exact_residual_diagnostic_'+label+'_W']=float(w);record['exact_residual_diagnostic_'+label+'_accepted']=w<=cutoff
  rows.append(record)
 table(out/'residual_arithmetic_diagnostics.csv',rows)
 dump(out/'residual_arithmetic_scope.json',{'status':'COMPLETE','problems':24,
  'note':'Diagnostic re-evaluation of the same stored coefficients, using exact residual algebra and unchanged <=0. Not the primary preserved R arithmetic; does not replace any classification or result.'})
 print('Residual arithmetic diagnostics saved for 24 pairs; no refits or reclassification.')


if __name__=='__main__':main()
