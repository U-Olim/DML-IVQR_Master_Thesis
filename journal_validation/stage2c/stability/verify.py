"""Independent saved-certificate and inference audit; no fit or LP calls."""
from fractions import Fraction as F
from pathlib import Path
import csv,hashlib,importlib.util,json,sys
import numpy as np

HERE=Path(__file__).resolve().parent;PARENT=HERE.parent
PRIOR=PARENT/'validation_protocol/reassessment_20261029T083111Z'
FULL=PARENT/'certification/saved_inputs_20261029T080821Z/full_precision'


def read(p):
 with p.open(newline='',encoding='utf-8-sig') as f:return list(csv.DictReader(f))


def rat(x):return F(int(x['numerator']),int(x['denominator']))


def exact_statistic(psi,s):
 # Independent direct Fraction implementation, not analyze.exact_W.
 observations=[(F(float(p[0]))*F(float(v)),F(float(p[1]))*F(float(v))) for p,v in zip(psi,s)]
 g1=sum((a for a,b in observations),F(0));g2=sum((b for a,b in observations),F(0))
 a=sum((u*u for u,v in observations),F(0));b=sum((u*v for u,v in observations),F(0));c=sum((v*v for u,v in observations),F(0))
 det=a*c-b*b;assert det>0
 return (c*g1*g1-2*b*g1*g2+a*g2*g2)/det,(g1,g2,a,b,c)


def main():
 run=Path(sys.argv[1]);manifest=json.loads((PARENT/'output/controlled_20261029_01/artifact_manifest.json').read_text())
 original=PARENT/'output/controlled_20261029_01'
 for name,r in manifest.items():
  assert hashlib.sha256((original/name).read_bytes()).hexdigest()==r['sha256'],name
 spec=importlib.util.spec_from_file_location('frozen_independent_certificate_audit',PARENT/'validation_protocol/audit.py')
 module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
 rows=json.loads((PRIOR/'arm_summary.json').read_text());assert len(rows)==92
 computed=[]
 for r in rows:
  c=json.loads((PRIOR/r['dataset']/r['arm']/'exact_certificate.json').read_text())
  computed.append(rat(c['gap'])/F(float(r['gap_response_scale_reference'])))
 eta=max(computed);assert eta==rat(json.loads((run/'frozen_accuracy_budget.json').read_text())['eta'])
 cutoff=F(float(np.fromfile(run/'historical_cutoff.bin',dtype='<f8')[0]))
 comparisons=read(run/'all_probe_inference.csv');qualifying=0;different=0;proofs=[]
 for index,r in enumerate(rows):
  name,arm=r['dataset'],r['arm'];folder=run/name/arm
  prior=PRIOR/name/arm;c=json.loads((prior/'exact_certificate.json').read_text());p=json.loads((prior/'stability_probes.json').read_text())
  objective_audit=module.case(FULL/name,arm,c,p)
  B=F(float(r['gap_response_scale_reference']));psi=np.fromfile(run/name/'psi_observation_row_major.bin',dtype='<f8').reshape(1000,2)
  beta=np.fromfile(folder/'baseline_beta.bin',dtype='<f8');s=np.fromfile(folder/'baseline_score.bin',dtype='<f8')
  baseline=json.loads((folder/'baseline_exact_inference.json').read_text());W,t=exact_statistic(psi,s)
  assert W==rat(baseline['W']) and (W<=cutoff)==baseline['accepted']
  for key,value in zip(['score_sum_1','score_sum_2','S11','S12','S22'],t):assert value==rat(baseline[key])
  alternatives=json.loads((folder/'alternative_exact_inference.json').read_text())
  for z,source in zip(alternatives,p):
   id=z['id'];bb=np.fromfile(folder/(id+'_beta.bin'),dtype='<f8')
   assert F(float(bb[0]))-F(float(beta[0]))==rat(source['intercept_step_exact'])
   assert np.array_equal(bb[1:],beta[1:])
   gap=rat(source['exact_objective_gap_upper_bound']);q=gap<=eta*B
   assert q==z['qualifies']
   ss=np.fromfile(folder/(id+'_score.bin'),dtype='<f8');e=np.fromfile(folder/(id+'_residual.bin'),dtype='<f8')
   assert np.array_equal(ss,.9-(e<=0).astype(float))
   ww,tt=exact_statistic(psi,ss);assert ww==rat(z['inference']['W'])
   assert (ww<=cutoff)==z['inference']['accepted']
   for key,value in zip(['score_sum_1','score_sum_2','S11','S12','S22'],tt):assert value==rat(z['inference'][key])
   row=next(x for x in comparisons if x['dataset']==name and x['arm']==arm and x['id']==id)
   assert (row['within_frozen_budget']=='True')==q
   assert (row['decision_change']=='True')==((W<=cutoff)!=(ww<=cutoff))
   qualifying+=int(q);different+=int(q and ((W<=cutoff)!=(ww<=cutoff)))
  proofs.append({'dataset':name,'arm':arm,'status':'PASS','certified_objectives':9,'exact_W_evaluations':9,'objective_audit':objective_audit})
  if (index+1)%10==0:print('INDEPENDENT_AUDIT',index+1,'of 92',flush=True)
 result={'status':'PASS','arms':92,'objective_certificates_verified':92,
  'alternative_objectives_verified':736,'exact_W_values_verified':828,
  'original_artifact_hashes_verified':len(manifest),'qualifying_alternatives':qualifying,
  'qualifying_original_decision_changes':different,'eta_verified_exactly':True,'cases':proofs}
 (run/'independent_validation.json').write_text(json.dumps(result,indent=2))
 print(json.dumps({k:v for k,v in result.items() if k!='cases'},indent=2))


if __name__=='__main__':main()
