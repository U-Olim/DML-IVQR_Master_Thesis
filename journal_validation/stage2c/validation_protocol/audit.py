"""Independent exact certificate/probe audit. No optimizer or fitting calls."""
from pathlib import Path
from fractions import Fraction as F
import json,sys
import numpy as np

HERE=Path(__file__).resolve().parent
CERT=HERE.parent/'certification/saved_inputs_20261029T080821Z'


def get(r):return F(int(r['numerator']),int(r['denominator']))


def ints(x):
 values=[float(v).as_integer_ratio() for v in np.asarray(x).flat]
 E=max(d.bit_length()-1 for _,d in values)
 return [a*(2**E//b) for a,b in values],E


def case(raw,arm,certificate,probes=None):
 X=np.fromfile(raw/'X_row_major.bin',dtype='<f8').reshape(1000,101)
 y=np.fromfile(raw/'y_candidate.bin',dtype='<f8');b=np.fromfile(raw/(arm+'_beta.bin'),dtype='<f8')
 lam=np.fromfile(raw/(arm+'_penalty.bin'),dtype='<f8')
 xx,EX=ints(X);Xint=[xx[i*101:(i+1)*101] for i in range(1000)]
 yy,EY=ints(y);bb,EB=ints(b)
 # Stage 2C-V certificate uses different field names; both carry exact witnesses.
 v=list(map(int,certificate['dual_numerators']));L=int(certificate['dual_common_denominator'])
 assert len(v)==1000 and L>0
 assert all(-L<=10*t<=9*L for t in v)
 g=[sum(row[j]*t for row,t in zip(Xint,v)) for j in range(101)]
 assert all(abs(F(t,2**EX*L))<=F(float(lam[j]))/2 for j,t in enumerate(g))
 assert all(g[j]==0 for j in range(101) if lam[j]==0)
 E=max(EY,EX+EB)
 e=[yy[i]*2**(E-EY)-sum(a*c for a,c in zip(Xint[i],bb))*2**(E-EX-EB) for i in range(1000)]
 loss=F(sum(9*t if t>=0 else -t for t in e),10*2**E)
 penalty=sum((F(float(l))*abs(F(float(c)))/2 for l,c in zip(lam,b)),F(0))
 primal=loss+penalty;dual=F(sum(a*c for a,c in zip(yy,v)),2**EY*L);gap=primal-dual
 assert gap>=0
 keyp='primal' if 'primal' in certificate else 'primal_objective'
 keyd='dual' if 'dual' in certificate else 'dual_objective'
 assert primal==get(certificate[keyp]) and dual==get(certificate[keyd]) and gap==get(certificate['gap'])
 loss_comp=sum((F(9*t if t>=0 else -t,10*2**E)-F(t*s,2**E*L) for t,s in zip(e,v)),F(0))
 penalty_comp=penalty-sum((F(c*t,2**(EB+EX)*L) for c,t in zip(bb,g)),F(0))
 assert loss_comp>=0 and penalty_comp>=0 and loss_comp+penalty_comp==gap
 if probes:
  signs=[t<=0 for t in e]
  for p in probes:
   delta=get(p['intercept_step_exact']);D=delta.denominator.bit_length()-1;Enew=max(E,D)
   ep=[t*2**(Enew-E)-delta.numerator*2**(Enew-D) for t in e]
   lp=F(sum(9*t if t>=0 else -t for t in ep),10*2**Enew)
   penp=penalty+F(float(lam[0]))*(abs(F(float(b[0]))+delta)-abs(F(float(b[0]))))/2
   assert lp+penp-dual==get(p['exact_objective_gap_upper_bound'])
   assert sum((t<=0)!=s for t,s in zip(ep,signs))==p['rank_sign_changes']
 return {'status':'PASS','primal':float(primal),'dual':float(dual),'gap':float(gap),
  'exact_equalities':int(sum(lam==0)),'probes_checked':len(probes) if probes else 0}


def main():
 run=Path(sys.argv[1]);rows=json.loads((run/'arm_summary.json').read_text());assert len(rows)==92
 result=[]
 for i,row in enumerate(rows):
  name,arm=row['dataset'],row['arm'];folder=run/name/arm
  if not (folder/'exact_certificate.json').is_file():
   result.append({'dataset':name,'arm':arm,'status':'NOT_ASSESSABLE'});continue
  c=json.loads((folder/'exact_certificate.json').read_text());probes=json.loads((folder/'stability_probes.json').read_text())
  r=case(CERT/'full_precision'/name,arm,c,probes)
  result.append(dict(dataset=name,arm=arm,**r))
  if (i+1)%10==0:print('Independent exact audit',i+1,'of 92',flush=True)
 old=json.loads((CERT/'pilot_021/P10/qr_exact_certificate.json').read_text())
 old_result=case(CERT/'full_precision/pilot_021','P10',old)
 summary={'status':'PASS' if all(r['status']=='PASS' for r in result) else 'PARTIAL',
  'arms_audited':len(result),'exact_certificates_passed':sum(r['status']=='PASS' for r in result),
  'probe_objectives_audited':sum(r.get('probes_checked',0) for r in result),
  'Stage2CV_P10_certificate_independently_verified':old_result,'arms':result}
 (run/'independent_validation.json').write_text(json.dumps(summary,indent=2))
 print(json.dumps({k:v for k,v in summary.items() if k!='arms'},indent=2))


if __name__=='__main__':main()
