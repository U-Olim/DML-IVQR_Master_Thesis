"""Independent rational primal/dual/uniqueness and contribution verification."""
from fractions import Fraction as F
from pathlib import Path
import json,csv,subprocess,sys
import numpy as np

HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[1]
SOURCE=ROOT/'journal_validation/stage2e/output/paired_20261029T093009Z'


def val(r):return F(int(r['numerator']),int(r['denominator']))


def rec(r):return {'numerator':str(r.numerator),'denominator':str(r.denominator),'float':float(r)}


def decode(a,d):return [F(int(t),int(d)) for t in a]


def det_fraction(A):
 a=[r.copy() for r in A];n=len(a);d=F(1)
 for k in range(n):
  pivotrow=next((i for i in range(k,n) if a[i][k]),None)
  assert pivotrow is not None
  if pivotrow!=k:a[k],a[pivotrow]=a[pivotrow],a[k];d=-d
  pivot=a[k][k];d*=pivot
  for i in range(k+1,n):
   ratio=a[i][k]/pivot
   for j in range(k+1,n):a[i][j]-=ratio*a[k][j]
   a[i][k]=F(0)
 return d


def statistic(psi,score):
 obs=[(F(float(a))*F(float(s)),F(float(b))*F(float(s))) for (a,b),s in zip(psi,score)]
 g1=sum((a for a,b in obs),F(0));g2=sum((b for a,b in obs),F(0))
 s11=sum((a*a for a,b in obs),F(0));s12=sum((a*b for a,b in obs),F(0));s22=sum((b*b for a,b in obs),F(0))
 det=s11*s22-s12*s12;assert det>0
 W=(s22*g1*g1-2*s12*g1*g2+s11*g2*g2)/det
 return [g1,g2,s11,s12,s22],W


def main():
 run=Path(sys.argv[1]);summaries=json.loads((run/'case_summaries.json').read_text());records=[]
 cutoff=F(float(np.fromfile(SOURCE/'cutoff.bin',dtype='<f8')[0]))
 for summary in summaries:
  id=summary['id'];folder=run/id
  if summary['status']!='EXACT_OPTIMUM_RECONSTRUCTED':
   records.append({'id':id,'status':'UNRESOLVED'});continue
  x=np.load(folder/'saved_inputs.npz');X=x['X'];y=x['y'];lam=x['lambda_vector']
  XR=[[F(float(v)) for v in row] for row in X];yr=[F(float(v)) for v in y];lr=[F(float(v)) for v in lam]
  beta=None;residual=None;certificates=[]
  for name in ['exact_decimal_optimum.json','exact_binary_optimum.json']:
   c=json.loads((folder/name).read_text());tau=val(c['tau'])
   b=decode(c['beta_numerators'],c['beta_denominator']);v=decode(c['dual_numerators'],c['dual_denominator'])
   e=[a-sum((xx*bb for xx,bb in zip(row,b)),F(0)) for a,row in zip(yr,XR)]
   assert e==decode(c['residual_numerators'],c['residual_denominator'])
   assert all(tau-1<=t<=tau for t in v)
   g=[sum((row[j]*t for row,t in zip(XR,v)),F(0)) for j in range(101)]
   assert all(abs(a)<=l/2 for a,l in zip(g,lr))
   P=sum(((tau if r>=0 else tau-1)*r for r in e),F(0))+sum((l*abs(bb)/2 for l,bb in zip(lr,b)),F(0))
   D=sum((a*t for a,t in zip(yr,v)),F(0));assert P==D==val(c['primal'])==val(c['dual'])
   S=c['active_coefficients_zero_based'];T=[i-1 for i in c['tied_observations_one_based']]
   inactive=[i for i in range(101) if i not in S]
   assert [j for j,t in enumerate(b) if t]==S and [i for i,t in enumerate(e) if t==0]==T
   assert all(tau-1<v[i]<tau for i in T)
   assert all(abs(g[j])<lr[j]/2 for j in inactive)
   A=[[XR[i][j] for j in S] for i in T];det=det_fraction(A)
   assert det!=0 and det==val(c['basis_real_determinant'])
   assert min(min(v[i]-(tau-1),tau-v[i]) for i in T)==val(c['minimum_tied_dual_box_margin'])
   assert min(lr[j]/2-abs(g[j]) for j in inactive)==val(c['minimum_inactive_penalty_margin'])
   if beta is not None:assert beta==b
   beta,residual=b,e
   certificates.append({'scope':name,'status':'EXACT_PRIMAL_DUAL_AND_UNIQUENESS_VERIFIED','P':rec(P),
    'tied_rows':len(T),'active_coefficients':len(S),'exact_gap_zero':True})
  errors=json.loads((folder/'exact_errors_of_saved_solutions.json').read_text());same_vector_signs={}
  for side in ['historical','independent']:
   b=[F(float(z)) for z in x[side+'_beta']]
   e=[a-sum((xx*bb for xx,bb in zip(row,b)),F(0)) for a,row in zip(yr,XR)]
   same_vector_signs[side]=int(sum((r<=0)!=(z<=0) for r,z in zip(e,x[side+'_residual'])))
   for label,tau in [('decimal',F(9,10)),('binary',F(float(.9)))]:
    P=sum(((tau if r>=0 else tau-1)*r for r in e),F(0))+sum((l*abs(bb)/2 for l,bb in zip(lr,b)),F(0))
    assert P==val(errors[side][label]['primal'])
    opt=json.loads((folder/('exact_'+label+'_optimum.json')).read_text())
    assert P-val(opt['primal'])==val(errors[side][label]['exact_suboptimality'])
  hs=.9-(x['historical_residual']<=0).astype(float);Is=.9-(x['independent_residual']<=0).astype(float)
  os=.9-np.array([r<=0 for r in residual]).astype(float)
  hp=x['historical_psi'];ip=x['independent_psi']
  inference=json.loads((folder/'inference.json').read_text())
  stats={}
  for key,p,s in [('historical',hp,hs),('independent_layer_A',hp,Is),('independent_complete_path',ip,Is),
   ('exact_optimum_score_fixed_historical_psi',hp,os),('exact_optimum_score_fixed_independent_psi',ip,os)]:
   values,W=statistic(p,s);assert W==val(inference[key]['W'])
   assert (W<=cutoff)==inference[key]['accepted']
   for label,r in zip(['score_sum_1','score_sum_2','S11','S12','S22'],values):assert r==val(inference[key][label])
   stats[key]=values
  # Exact observation-by-observation split of sign and projection effects.
  sumsA=[F(0)]*5;sumsProjection=[F(0)]*5
  for ph,pi,sh,si in zip(hp,ip,hs,Is):
   a,b=map(lambda z:F(float(z)),ph);c,d=map(lambda z:F(float(z)),pi);sh,si=F(float(sh)),F(float(si))
   da=[a*(si-sh),b*(si-sh),a*a*(si*si-sh*sh),a*b*(si*si-sh*sh),b*b*(si*si-sh*sh)]
   dp=[(c-a)*si,(d-b)*si,(c*c-a*a)*si*si,(c*d-a*b)*si*si,(d*d-b*b)*si*si]
   sumsA=[x+y for x,y in zip(sumsA,da)];sumsProjection=[x+y for x,y in zip(sumsProjection,dp)]
  assert sumsA==[a-b for a,b in zip(stats['independent_layer_A'],stats['historical'])]
  assert sumsProjection==[a-b for a,b in zip(stats['independent_complete_path'],stats['independent_layer_A'])]
  (folder/'exact_score_decomposition.json').write_text(json.dumps({'frozen_differences':[rec(z) for z in sumsA],
   'additional_projection_differences':[rec(z) for z in sumsProjection],'all_equalities_verified_exactly':True},indent=2))
  records.append({'id':id,'status':'PASS','exact_optima':certificates,'unique_beta':True,
   'same_stored_vector_R_vs_exact_residual_sign_differences':same_vector_signs,'exact_inference_evaluations':5,
   'exact_observation_decomposition':True})
  print('EXACT_UNIQUENESS_AUDIT_PASS',id,flush=True)
 # Representation diagnostic is evaluation only, not a solution-selection algorithm.
 if all(r['status']=='PASS' for r in records):
  argv=[r'C:\Program Files\R\R-3.4.3\bin\x64\Rscript.exe','--vanilla',str(HERE/'representation.R'),str(run)]
  if not (run/'rounded_optimum_R_diagnostics.csv').exists():
   with (run/'representation.log').open('w') as log:p=subprocess.run(argv,cwd=ROOT,stdout=log,stderr=subprocess.STDOUT)
   assert p.returncode==0
   (run/'representation_command.json').write_text(json.dumps({'argv':argv,'exit_status':p.returncode},indent=2))
  for r in records:
   folder=run/r['id'];c=json.loads((folder/'exact_decimal_optimum.json').read_text())
   er=[int(z) for z in c['residual_numerators']];e=np.fromfile(folder/'rounded_optimum_R_residual.bin',dtype='<f8')
   r['rounded_exact_beta_R_vs_mathematical_rank_changes']=int(sum((a<=0)!=(b<=0) for a,b in zip(er,e)))
 result={'status':'PASS' if all(r['status']=='PASS' for r in records) else 'PARTIAL',
  'problems':2,'exact_optimum_certificates':sum(len(r.get('exact_optima',[])) for r in records),
  'unique_optimum_proofs':sum(r.get('unique_beta',False) for r in records),'cases':records}
 (run/'independent_validation.json').write_text(json.dumps(result,indent=2))
 print(json.dumps({k:v for k,v in result.items() if k!='cases'},indent=2))


if __name__=='__main__':main()
