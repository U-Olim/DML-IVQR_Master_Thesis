"""Independent exact LP/objective/inference audit; no fitting or optimization."""
from pathlib import Path
from fractions import Fraction as F
import csv,json,sys,subprocess
import numpy as np
from scipy.sparse import load_npz,eye,csr_matrix

HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[1]


def read(p):
 with p.open(newline='',encoding='utf-8-sig') as f:return list(csv.DictReader(f))


def rat(r):return F(int(r['numerator']),int(r['denominator']))


def ints(a):
 p=[float(x).as_integer_ratio() for x in np.asarray(a).flat];E=max(d.bit_length()-1 for _,d in p)
 return [n*(2**E//d) for n,d in p],E


def exactW(psi,s):
 # Independent direct Fraction arithmetic.
 obs=[(F(float(a))*F(float(v)),F(float(b))*F(float(v))) for (a,b),v in zip(psi,s)]
 g=[sum((r[j] for r in obs),F(0)) for j in [0,1]]
 a=sum((r[0]**2 for r in obs),F(0));b=sum((r[0]*r[1] for r in obs),F(0));c=sum((r[1]**2 for r in obs),F(0))
 det=a*c-b*b;assert det>0
 return (c*g[0]**2-2*b*g[0]*g[1]+a*g[1]**2)/det


def objective_audit(folder):
 X=np.fromfile(folder/'X_row_major.bin',dtype='<f8').reshape(1000,101)
 y=np.fromfile(folder/'response.bin',dtype='<f8');lam=np.fromfile(folder/'lambda.bin',dtype='<f8')
 Aeq=load_npz(folder/'LP_Aeq.npz');Aub=load_npz(folder/'LP_Aub.npz');vec=np.load(folder/'LP_vectors.npz')
 assert Aeq.shape==(1000,2202) and Aub.shape==(202,2202)
 assert np.array_equal(Aeq[:,:101].toarray(),X)
 assert (Aeq[:,101:1101]-eye(1000)).nnz==0 and (Aeq[:,1101:2101]+eye(1000)).nnz==0
 assert Aeq[:,2101:].nnz==0
 assert (Aub[:101,:101]-eye(101)).nnz==0 and (Aub[101:,:101]+eye(101)).nnz==0
 assert (Aub[:101,2101:]+eye(101)).nnz==0 and (Aub[101:,2101:]+eye(101)).nnz==0
 assert Aub[:,101:2101].nnz==0
 expected=np.r_[np.zeros(101),np.full(1000,.9),np.full(1000,1-.9),lam/2]
 assert np.array_equal(expected,vec['objective']) and np.array_equal(y,vec['b_eq'])
 cert=json.loads((folder/'dual_certificate.json').read_text())
 v=list(map(int,cert['dual_numerators']));L=int(cert['dual_common_denominator'])
 assert all(-L<=10*t<=9*L for t in v)
 xx,EX=ints(X);Xi=[xx[i*101:(i+1)*101] for i in range(1000)]
 yi,EY=ints(y);gradient=[sum(row[j]*t for row,t in zip(Xi,v)) for j in range(101)]
 assert all(abs(F(g,2**EX*L))<=F(float(lam[j]))/2 for j,g in enumerate(gradient))
 D=F(sum(a*b for a,b in zip(yi,v)),2**EY*L);assert D==rat(cert['dual_objective'])
 result={}
 for side in ['historical','independent']:
  beta=np.fromfile(folder/(side+'_beta.bin'),dtype='<f8');bi,EB=ints(beta);E=max(EY,EX+EB)
  e=[yi[i]*2**(E-EY)-sum(a*b for a,b in zip(Xi[i],bi))*2**(E-EX-EB) for i in range(1000)]
  loss=F(sum(9*r if r>=0 else -r for r in e),10*2**E)
  penalty=sum((F(float(l))*abs(F(float(b)))/2 for l,b in zip(lam,beta)),F(0));P=loss+penalty
  C=json.loads((folder/(side+'_objective_certificate.json')).read_text())
  assert P==rat(C['primal_objective']) and D==rat(C['dual_objective']) and P-D==rat(C['certified_gap'])
  assert P-D>=0
  losscomp=sum((F(9*r if r>=0 else -r,10*2**E)-F(r*t,2**E*L) for r,t in zip(e,v)),F(0))
  pencomp=penalty-sum((F(b*g,2**(EB+EX)*L) for b,g in zip(bi,gradient)),F(0))
  assert losscomp>=0 and pencomp>=0 and losscomp+pencomp==P-D
  assert losscomp==rat(C['loss_complementarity']) and pencomp==rat(C['penalty_complementarity'])
  assert C['within_frozen_accuracy_envelope']==(P-D<=rat(cert['accuracy_budget']))
  result[side]={'primal':float(P),'dual':float(D),'certified_gap':float(P-D),'status':'PASS'}
 result['historical_suboptimality_lower_bound_from_independent_primal']=float(max(F(0),rat(json.loads((folder/'historical_objective_certificate.json').read_text())['primal_objective'])-rat(json.loads((folder/'independent_objective_certificate.json').read_text())['primal_objective'])))
 return result


def main():
 out=Path(sys.argv[1]).resolve();assert HERE in out.parents
 assert json.loads((out/'run_status.json').read_text())['status']=='COMPLETE'
 argv=[r'C:\Program Files\R\R-3.4.3\bin\x64\Rscript.exe','--vanilla',str(HERE/'verify_R.R'),str(out)]
 with (out/'saved_downstream_audit.log').open('w') as log:p=subprocess.run(argv,cwd=ROOT,stdout=log,stderr=subprocess.STDOUT)
 (out/'downstream_audit_command.json').write_text(json.dumps({'argv':argv,'exit_status':p.returncode},indent=2));assert p.returncode==0
 rows=read(out/'paired_summary.csv');assert len(rows)==24
 cutoff=F(float(np.fromfile(out/'cutoff.bin',dtype='<f8')[0]));checks=[]
 for row in rows:
  folder=out/row['id']
  if row['numerical_status']!='SUCCESS':
   checks.append({'id':row['id'],'status':'NOT_ASSESSABLE'});continue
  proof=objective_audit(folder)
  hpsi=np.fromfile(folder/'historical_psi.bin',dtype='<f8').reshape(1000,2)
  ipsi=np.fromfile(folder/'independent_psi.bin',dtype='<f8').reshape(1000,2)
  hs=np.fromfile(folder/'historical_score.bin',dtype='<f8');ss=np.fromfile(folder/'independent_score.bin',dtype='<f8')
  he=np.fromfile(folder/'historical_residual.bin',dtype='<f8');ie=np.fromfile(folder/'independent_residual.bin',dtype='<f8')
  assert np.array_equal(hs,.9-(he<=0).astype(float)) and np.array_equal(ss,.9-(ie<=0).astype(float))
  W=[exactW(hpsi,hs),exactW(hpsi,ss),exactW(ipsi,ss)]
  for value,label,decision in zip(W,['historical_W','A_independent_W','B_independent_W'],['historical_accepted','A_independent_accepted','B_independent_accepted']):
   assert abs(float(value)-float(row[label]))<1e-9
   assert (value<=cutoff)==(row[decision]=='TRUE')
  assert int(row['rank_changes'])==int(sum((he<=0)!=(ie<=0)))
  # Exact cutoff-side certificates for the original binary64 score/instrument inputs.
  def frac(q):return {'numerator':str(q.numerator),'denominator':str(q.denominator),'float':float(q)}
  inference={'cutoff':frac(cutoff),'historical_W':frac(W[0]),'layer_A_W':frac(W[1]),'layer_B_W':frac(W[2]),
   'accepted':[v<=cutoff for v in W],'scope':'Exact rational W conditional on stored historical R score and psi values.'}
  (folder/'exact_inference_verification.json').write_text(json.dumps(inference,indent=2))
  checks.append({'id':row['id'],'status':'PASS','objective_audit':proof,'exact_W_values':3})
  print('INDEPENDENT_AUDIT',row['id'],flush=True)
 result={'status':'PASS' if all(c['status']=='PASS' for c in checks) else 'PARTIAL',
  'problems':len(checks),'objective_certificates_verified':sum(c['status']=='PASS' for c in checks)*2,
  'exact_W_values_verified':sum(c.get('exact_W_values',0) for c in checks),'cases':checks}
 (out/'independent_validation.json').write_text(json.dumps(result,indent=2))
 print(json.dumps({k:v for k,v in result.items() if k!='cases'},indent=2))


if __name__=='__main__':main()
