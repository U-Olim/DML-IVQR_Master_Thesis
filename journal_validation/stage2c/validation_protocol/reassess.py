"""Dual-certificate reconstruction and saved-coefficient probes; NEVER fits outcomes."""
from fractions import Fraction as F
from pathlib import Path
from datetime import datetime,timezone
import csv,hashlib,json,math,os,subprocess,sys
import numpy as np
import scipy
from scipy.optimize import linprog
from scipy.linalg import qr

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
CERT=HERE.parent/'certification/saved_inputs_20261029T080821Z'
ORIGINAL=HERE.parent/'output/controlled_20261029_01'
sys.path.insert(0,str(HERE.parent/'certification'))
from exact_bounds import bareiss_solve,dyadic,record


def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for block in iter(lambda:f.read(1024*1024),b''):h.update(block)
 return h.hexdigest()


def dump(p,x):
 def convert(v):
  if isinstance(v,np.ndarray):return v.tolist()
  if isinstance(v,np.generic):return v.item()
  raise TypeError(str(type(v)))
 p.write_text(json.dumps(x,indent=2,default=convert),encoding='utf-8')


def snapshot():
 result={}
 for directory,subdirs,files in os.walk(ROOT):
  base=Path(directory);subdirs[:]=[d for d in subdirs if base/d!=HERE and not(base==ROOT and d=='.git')]
  for name in files:
   p=base/name;result[p.relative_to(ROOT).as_posix()]=sha(p)
 return result


def primal_parts(Xi,EX,y,beta,lam):
 Yi,EY=dyadic(y);Bi,EB=dyadic(beta);Li,EL=dyadic(lam)
 Yi=Yi.tolist();Bi=Bi.tolist();Li=Li.tolist();ER=max(EY,EX+EB)
 residual=[(Yi[i] << (ER-EY))-(sum(a*b for a,b in zip(Xi[i],Bi)) << (ER-EX-EB)) for i in range(len(y))]
 loss=F(sum(9*r if r>=0 else -r for r in residual),10 << ER)
 penalty=F(sum(abs(a)*b for a,b in zip(Bi,Li)),2 << (EB+EL))
 return residual,ER,loss,penalty,(Yi,EY,Bi,EB,Li,EL)


def exact_dual(X,Xi,EX,lam,vfloat):
 zero=np.flatnonzero(lam==0);k=len(zero)
 # Choose a basis for certificate equalities, not new outcome coefficients.
 if k:
  interior=np.flatnonzero((vfloat>-.1+1e-7)&(vfloat<.9-1e-7))
  candidates=interior if len(interior)>=k else np.arange(len(vfloat))
  _,_,pivot=qr(X[candidates][:,zero].T,pivoting=True,mode='economic')
  free=candidates[pivot[:k]]
 else:free=np.array([],dtype=int)
 free_set=set(map(int,free));fixed=[i for i in range(len(vfloat)) if i not in free_set]
 vals={}
 for i in fixed:
  t=float(vfloat[i])
  vals[i]=F(9,10) if t>.9-1e-7 else F(-1,10) if t<-.1+1e-7 else F(t)
 L=math.lcm(*(v.denominator for v in vals.values())) if vals else 1
 fixed_nums={i:t.numerator*(L//t.denominator) for i,t in vals.items()}
 if k:
  A=[[Xi[int(i)][int(j)] for i in free] for j in zero]
  rhs=[-sum(Xi[i][int(j)]*t for i,t in fixed_nums.items()) for j in zero]
  solution=bareiss_solve(A,rhs)
  for i,t in zip(free,solution):vals[int(i)]=t/L
 v=[vals[i] for i in range(len(vfloat))]
 L=math.lcm(*(t.denominator for t in v));nums=[t.numerator*(L//t.denominator) for t in v]
 grad=[sum(row[j]*t for row,t in zip(Xi,nums)) for j in range(101)]
 assert all(grad[int(j)]==0 for j in zero)
 # Exact scaling toward the feasible zero witness preserves all equalities.
 scale=F(1)
 for t in nums:
  if t>0:scale=min(scale,F(9*L,10*t))
  elif t<0:scale=min(scale,F(-L,10*t))
 for j,g in enumerate(grad):
  if lam[j]>0 and g:
   scale=min(scale,F(float(lam[j]))/2/abs(F(g,(1 << EX)*L)))
 assert scale>0
 nums=[t*scale.numerator for t in nums];L*=scale.denominator
 grad=[g*scale.numerator for g in grad]
 assert all(-L<=10*t<=9*L for t in nums)
 assert all(abs(F(g,(1 << EX)*L))<=F(float(lam[j]))/2 for j,g in enumerate(grad))
 return nums,L,grad,scale,free.tolist()


def evaluate(folder,X,Xi,EX,y,beta,lam,saved_e,arm):
 n=len(y);zero=lam==0;other=~zero
 result=linprog(-y,A_ub=np.vstack([X[:,other].T,-X[:,other].T]) if other.any() else None,
   b_ub=np.concatenate([lam[other]/2,lam[other]/2]) if other.any() else None,
   A_eq=X[:,zero].T if zero.any() else None,b_eq=np.zeros(int(zero.sum())) if zero.any() else None,
   bounds=[(-.1,.9)]*n,method='highs-ds',
   options={'primal_feasibility_tolerance':1e-10,'dual_feasibility_tolerance':1e-10})
 dump(folder/'dual_solver.json',dict(result))
 if not result.success:raise RuntimeError('Certificate dual LP unavailable: '+result.message)
 nums,L,grad,scale,free=exact_dual(X,Xi,EX,lam,result.x)
 residual,ER,loss,penalty,parts=primal_parts(Xi,EX,y,beta,lam)
 Yi,EY,Bi,EB,Li,EL=parts
 primal=loss+penalty;dual=F(sum(a*b for a,b in zip(Yi,nums)),(1 << EY)*L);gap=primal-dual
 assert gap>=0
 losscomp=F(0)
 for r,t in zip(residual,nums):
  c=F(9*r if r>=0 else -r,10 << ER)-F(r*t,(1 << ER)*L)
  assert c>=0;losscomp+=c
 penaltycomp=penalty-sum(F(b*g,(1 << (EB+EX))*L) for b,g in zip(Bi,grad))
 assert penaltycomp>=0 and losscomp+penaltycomp==gap
 classification='Numerically acceptable under the new protocol' if gap==0 else 'Indeterminate'
 # Exact certified objective bounds, separate from application accuracy.
 cert={'status':'EXACT_DUAL_FEASIBLE','tau':'9/10','classification':classification,
  'dual_numerators':[str(t) for t in nums],'dual_common_denominator':str(L),
  'free_certificate_observations_zero_based':free,'exact_scale_toward_zero':record(scale),
  'primal':record(primal),'dual':record(dual),'gap':record(gap),
  'gap_per_observation':record(gap/n),'loss_complementarity':record(losscomp),
  'penalty_complementarity':record(penaltycomp),'zero_penalty_equalities_exact':int(zero.sum())}
 dump(folder/'exact_certificate.json',cert)
 # Fixed, predeclared local probes: only evaluate stored-coefficient perturbations.
 probes=[];base_rank=[r<=0 for r in residual]
 for exponent in [-40,-30,-20,-10]:
  for sign in [-1,1]:
   perturbed=float(beta[0]+sign*2.**exponent);delta=F(perturbed)-F(float(beta[0]));DE=delta.denominator.bit_length()-1
   E=max(ER,DE);new_res=[(r << (E-ER))-delta.numerator*(1 << (E-DE)) for r in residual]
   new_loss=F(sum(9*r if r>=0 else -r for r in new_res),10 << E)
   new_penalty=penalty-F(float(lam[0]))*abs(F(float(beta[0])))/2+F(float(lam[0]))*abs(F(perturbed))/2
   upper=new_loss+new_penalty-dual;assert upper>=0
   flips=sum((r<=0)!=b for r,b in zip(new_res,base_rank))
   probes.append({'exponent':exponent,'sign':sign,'intercept_step_exact':record(delta),
    'prediction_RMS_change':float(abs(delta)), 'rank_sign_changes':flips,
    'exact_objective_gap_upper_bound':record(upper),'is_refit':False})
 dump(folder/'stability_probes.json',probes)
 exact_sign=np.array(base_rank);saved_sign=saved_e<=0
 col_rms=np.sqrt(np.mean(X*X,axis=0));sv=np.linalg.svd(X,compute_uv=False)
 robust=max(float(np.quantile(y,.75)-np.quantile(y,.25)),float(np.median(abs(y-np.median(y)))),1.)
 e_float=np.array([float(F(r,1 << ER)) for r in residual]);vn=np.array([float(F(t,L)) for t in nums])
 stationarity=X.T@vn
 active=abs(beta)>1e-7;target=.5*lam*np.sign(beta)
 kkt=np.where(active,abs(stationarity-target),np.maximum(abs(stationarity)-lam/2,0))
 diagnostics={'column_RMS_min':float(min(col_rms)),'column_RMS_max':float(max(col_rms)),
  'outcome_design_singular_value_condition':float(sv[0]/sv[-1]),
  'residual_abs_min':float(min(abs(e_float))),'residual_abs_median':float(np.median(abs(e_float))),
  'coefficient_abs_max':float(max(abs(beta))),'saved_vs_exact_residual_sign_changes':int(sum(saved_sign!=exact_sign)),
  'saved_vs_exact_residual_max_difference':float(max(abs(saved_e-e_float))),
  'max_certificate_slope_equality_float_diagnostic':float(max(abs(stationarity[zero]))) if zero.any() else 0,
  'numerical_coefficient_KKT_max_over_n_diagnostic':float(max(kkt)/n),
  'gap_response_scale_reference':n*robust,'gap_over_response_scale':float(gap)/(n*robust),
  'objective_units':'unscaled check loss plus half-L1; gap/n also reported',
  'note':'Response scale is descriptive, not an acceptance threshold; exact dual feasibility is verified algebraically.'}
 dump(folder/'scaling_diagnostics.json',diagnostics)
 return cert,diagnostics,probes


def main():
 assert subprocess.check_output(['git','branch','--show-current'],cwd=ROOT,text=True).strip()=='journal-validation'
 run=HERE/('reassessment_'+datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ'));run.mkdir(exist_ok=False)
 print('RUN',run,flush=True)
 dump(run/'initial_state.json',{'git_status':subprocess.check_output(['git','status','--short','--branch'],cwd=ROOT,text=True),
  'python':sys.version,'numpy':np.__version__,'scipy':scipy.__version__,
  'protocol_sha256_before_execution':sha(HERE/'PROTOCOL.md'),
  'source_sha256_before_execution':{p.name:sha(p) for p in HERE.iterdir() if p.is_file()}})
 print('Hashing protected files',flush=True);before=snapshot();dump(run/'protected_before.json',before)
 summary=[];status='FAILED'
 try:
  manifest=json.loads((CERT/'SHA256_MANIFEST.json').read_text())
  for name,r in manifest.items():assert sha(CERT/name)==r['sha256'],name
  dump(run/'certification_manifest_check.json',{'status':'PASS','artifacts_verified':len(manifest)})
  cases=json.loads((CERT/'all_case_summary.json').read_text());assert len(cases)==92
  cases.sort(key=lambda r:(r['dataset'],r['arm']))
  cached={}
  for old in cases:
   name=old['dataset'];arm=old['arm'];raw=CERT/'full_precision'/name
   if name not in cached:
    X=np.fromfile(raw/'X_row_major.bin',dtype='<f8').reshape(1000,101);xx,EX=dyadic(X)
    cached[name]=(X,xx.tolist(),EX,np.fromfile(raw/'y_candidate.bin',dtype='<f8'))
   X,Xi,EX,y=cached[name]
   beta=np.fromfile(raw/(arm+'_beta.bin'),dtype='<f8');lam=np.fromfile(raw/(arm+'_penalty.bin'),dtype='<f8');e=np.fromfile(raw/(arm+'_residual.bin'),dtype='<f8')
   folder=run/name/arm;folder.mkdir(parents=True)
   try:
    cert,diag,probes=evaluate(folder,X,Xi,EX,y,beta,lam,e,arm)
    row={'dataset':name,'arm':arm,'historical_record':old['historical_record'],
     'certified_historical_LP_result':old['historical_csv']['classification'],
     'certified_historical_LP_lower':old['historical_csv']['lower'],'certified_historical_LP_upper':old['historical_csv']['upper'],
     'primal':cert['primal']['float'],'dual':cert['dual']['float'],'certified_gap_upper':cert['gap']['outward_upper'],
     'certified_gap_per_observation':cert['gap_per_observation']['outward_upper'],
     'dual_feasibility':'exact rational','classification':cert['classification'],**diag}
   except Exception as exc:
    dump(folder/'certificate_unavailable.json',{'error':repr(exc)})
    row={'dataset':name,'arm':arm,'historical_record':old['historical_record'],
     'certified_historical_LP_result':old['historical_csv']['classification'],
     'classification':'Insufficient evidence','reason':repr(exc)}
   summary.append(row);dump(run/'arm_summary.json',summary)
   print(name,arm,row['classification'],row.get('certified_gap_upper'),flush=True)
  status='COMPLETE'
 finally:
  after=snapshot();dump(run/'protected_after.json',after)
  preservation={'status':status,'files_checked':len(before),'changed':[p for p in before if p in after and before[p]!=after[p]],
   'missing':sorted(before.keys()-after.keys()),'added_outside_validation_protocol':sorted(after.keys()-before.keys())}
  dump(run/'preservation.json',preservation)
  assert not any(preservation[k] for k in ['changed','missing','added_outside_validation_protocol'])
  dump(run/'run_status.json',{'status':status,'arms':len(summary)})
  print('PRESERVATION',preservation,flush=True)


if __name__=='__main__':main()
