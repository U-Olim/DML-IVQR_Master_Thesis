"""Additional exact certificate for literal binary64 tau used by both solvers."""
from fractions import Fraction as F
from pathlib import Path
import json,sys
import numpy as np
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'stage2c/certification'))
from exact_bounds import dyadic,record


def val(r):return F(int(r['numerator']),int(r['denominator']))


def main():
 out=Path(sys.argv[1]);tasks=[]
 import csv
 with (out/'task_manifest.csv').open() as f:tasks=list(csv.DictReader(f))
 tau=F(float(.9));difference=tau-F(9,10);rows=[]
 for task in tasks:
  folder=out/task['id'];old=json.loads((folder/'dual_certificate.json').read_text())
  vi=list(map(int,old['dual_numerators']));L=int(old['dual_common_denominator']);scale=F(1)
  for v in vi:
   if v>0:scale=min(scale,tau/F(v,L))
   elif v<0:scale=min(scale,(1-tau)/F(-v,L))
  nums=[v*scale.numerator for v in vi];den=L*scale.denominator
  assert all(tau-1<=F(v,den)<=tau for v in nums)
  X=np.fromfile(folder/'X_row_major.bin',dtype='<f8').reshape(1000,101);y=np.fromfile(folder/'response.bin',dtype='<f8')
  lam=np.fromfile(folder/'lambda.bin',dtype='<f8');xx,EX=dyadic(X);Xi=xx.tolist();yi,EY=dyadic(y);yi=yi.tolist()
  gradient=[sum(row[j]*v for row,v in zip(Xi,nums)) for j in range(101)]
  assert all(abs(F(g,(1 << EX)*den))<=F(float(lam[j]))/2 for j,g in enumerate(gradient))
  D=F(sum(a*b for a,b in zip(yi,nums)),(1 << EY)*den)
  records={}
  for side in ['historical','independent']:
   beta=np.fromfile(folder/(side+'_beta.bin'),dtype='<f8');bi,EB=dyadic(beta);bi=bi.tolist();E=max(EY,EX+EB)
   e=[(yi[i] << (E-EY))-(sum(a*b for a,b in zip(Xi[i],bi)) << (E-EX-EB)) for i in range(1000)]
   loss=sum((tau if r>=0 else tau-1)*F(r,1 << E) for r in e)
   penalty=sum(F(float(l))*abs(F(float(b)))/2 for l,b in zip(lam,beta));P=loss+penalty;G=P-D;assert G>=0
   C=json.loads((folder/(side+'_objective_certificate.json')).read_text())
   assert P-val(C['primal_objective'])==difference*F(sum(e),1 << E)
   losscomp=sum(((tau if r>=0 else tau-1)*F(r,1 << E)-F(r*v,(1 << E)*den)) for r,v in zip(e,nums))
   pencomp=penalty-sum(F(b*g,(1 << (EB+EX))*den) for b,g in zip(bi,gradient))
   assert losscomp>=0 and pencomp>=0 and losscomp+pencomp==G
   records[side]={'primal':record(P),'dual':record(D),'gap':record(G),
    'within_frozen_envelope':G<=val(old['accuracy_budget']),
    'decimal_tau_objective_difference':record(P-val(C['primal_objective']))}
  proof={'status':'EXACT_BINARY64_TAU_CERTIFIED','tau':record(tau),'lower_score_bound':record(tau-1),
   'dual_numerators':[str(v) for v in nums],'dual_common_denominator':str(den),
   'all_constraints_verified_exactly':True,'fits':records}
  (folder/'binary_tau_certificates.json').write_text(json.dumps(proof,indent=2))
  assert all(records[s]['within_frozen_envelope']==json.loads((folder/(s+'_objective_certificate.json')).read_text())['within_frozen_accuracy_envelope'] for s in records)
  rows.append({'id':task['id'],'status':'PASS','fits':records})
 (out/'binary_tau_verification.json').write_text(json.dumps({'status':'PASS','problems':24,'objective_certificates':48,
  'qualification_changed':False,'cases':rows},indent=2))
 print('Literal binary64 tau: 48 exact certificates verified; all envelope qualifications unchanged.')


if __name__=='__main__':main()
