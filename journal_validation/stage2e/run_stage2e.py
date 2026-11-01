"""Fixed 24-pair primal LP experiment. No new datasets or historical writes."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import csv,hashlib,importlib.util,json,os,subprocess,sys,warnings
from collections import Counter
import numpy as np
import scipy
from scipy.optimize import linprog
from scipy.sparse import bmat,csr_matrix,eye

HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[1]
HIST=ROOT/'journal_validation/stage2c/output/controlled_20261029_01'
sys.path.insert(0,str(ROOT/'journal_validation/stage2c/certification'))
from exact_bounds import dyadic,record
spec=importlib.util.spec_from_file_location('stage2cp_certificate_methods',ROOT/'journal_validation/stage2c/validation_protocol/reassess.py')
methods=importlib.util.module_from_spec(spec);spec.loader.exec_module(methods)


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


def read(p):
 with p.open(newline='',encoding='utf-8-sig') as f:return list(csv.DictReader(f))


def snapshot():
 result={}
 for directory,subdirs,files in os.walk(ROOT):
  base=Path(directory);subdirs[:]=[d for d in subdirs if base/d!=HERE and not(base==ROOT and d=='.git')]
  for name in files:
   p=base/name;result[p.relative_to(ROOT).as_posix()]=sha(p)
 return result


def table(p,rows):
 fields=list(dict.fromkeys(k for r in rows for k in r))
 with p.open('w',newline='',encoding='utf-8') as f:
  w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)


def certify(folder,X,y,betas,lam,v,eta):
 Xi,EX=dyadic(X);Xi=Xi.tolist()
 nums,L,gradient,scale,free=methods.exact_dual(X,Xi,EX,lam,v)
 Yi,EY=dyadic(y);dual=F(sum(int(a)*b for a,b in zip(Yi.tolist(),nums)),(1 << EY)*L)
 robust=max(float(np.quantile(y,.75)-np.quantile(y,.25)),float(np.median(abs(y-np.median(y)))),1.)
 B=F(float(len(y)*robust));budget=eta*B
 common={'tau':'9/10','scope':'Saved binary64 X, candidate-adjusted y, beta and lambda treated as exact rationals.',
  'dual_numerators':[str(t) for t in nums],'dual_common_denominator':str(L),
  'dual_objective':record(dual),'exact_scale':record(scale),
  'scale_B':record(B),'accuracy_budget':record(budget),
  'score_box_verified_exactly':True,'penalty_inequalities_verified_exactly':True}
 dump(folder/'dual_certificate.json',common);results={}
 for name,beta in betas.items():
  residual,ER,loss,penalty,parts=methods.primal_parts(Xi,EX,y,beta,lam)
  _,_,Bi,EB,_,_=parts;P=loss+penalty;gap=P-dual;assert gap>=0
  losscomp=F(0)
  for e,t in zip(residual,nums):
   z=F(9*e if e>=0 else -e,10 << ER)-F(e*t,(1 << ER)*L);assert z>=0;losscomp+=z
  pencomp=penalty-sum(F(b*g,(1 << (EB+EX))*L) for b,g in zip(Bi,gradient))
  assert pencomp>=0 and losscomp+pencomp==gap
  exacte=np.array([float(F(e,1 << ER)) for e in residual])
  active=abs(beta)>1e-7;ties=abs(exacte)<=1e-7
  M=np.vstack([X[ties],np.eye(101)[~active]])
  result={'status':'EXACT_OBJECTIVE_AND_DUAL_BOUND','solver':name,'primal_objective':record(P),
   'dual_objective':record(dual),'certified_gap':record(gap),'within_frozen_accuracy_envelope':gap<=budget,
   'loss_complementarity':record(losscomp),'penalty_complementarity':record(pencomp),
   'primal_feasibility':'Canonical r_plus=max(e,0),r_minus=max(-e,0),t=abs(beta), evaluated exactly; beta unchanged.',
   'near_zero_residuals_1e7':int(sum(ties)),'selected_coefficients_1e7':int(sum(active)),
   'numerical_active_constraint_rank':int(np.linalg.matrix_rank(M)),
   'nonuniqueness_status':'Not established: numerical active-set rank and nonzero gap do not prove unique exact optimal coefficients.'}
  dump(folder/(name+'_objective_certificate.json'),result);results[name]=result
 return results,common


def independent(folder,eta,config):
 X=np.fromfile(folder/'X_row_major.bin',dtype='<f8').reshape(1000,101)
 y=np.fromfile(folder/'response.bin',dtype='<f8');lam=np.fromfile(folder/'lambda.bin',dtype='<f8')
 historical=np.fromfile(folder/'historical_beta.bin',dtype='<f8')
 n,p=X.shape;I=eye(n,format='csr');J=eye(p,format='csr');Xm=csr_matrix(X)
 # Variable blocks beta (free), r_plus, r_minus, t (nonnegative).
 # Explicit zero t block keeps the exact requested variable dimensions.
 from scipy.sparse import hstack
 Aeq=hstack([Xm,I,-I,csr_matrix((n,p))],format='csr')
 Aub=bmat([[J,csr_matrix((p,n)),csr_matrix((p,n)),-J],
           [-J,csr_matrix((p,n)),csr_matrix((p,n)),-J]],format='csr')
 c=np.concatenate([np.zeros(p),np.full(n,.9),np.full(n,1-.9),lam/2])
 solver_warnings=[]
 with warnings.catch_warnings(record=True) as caught:
  result=linprog(c,A_ub=Aub,b_ub=np.zeros(2*p),A_eq=Aeq,b_eq=y,
    bounds=[(None,None)]*p+[(0,None)]*(2*n+p),method='highs-ds',
    options={'primal_feasibility_tolerance':config['LP_primal_feasibility_tolerance'],
             'dual_feasibility_tolerance':config['LP_dual_feasibility_tolerance']})
  solver_warnings=[str(w.message) for w in caught]
 dump(folder/'independent_solver.json',dict(result));dump(folder/'independent_solver_warnings.json',solver_warnings)
 from scipy.sparse import save_npz
 save_npz(folder/'LP_Aeq.npz',Aeq);save_npz(folder/'LP_Aub.npz',Aub)
 np.savez(folder/'LP_vectors.npz',objective=c,b_eq=y,b_ub=np.zeros(2*p),lambda_vector=lam)
 if not result.success:
  (folder/'independent_status.txt').write_text('FAILED\n')
  return {'status':'SOLVER_FAILURE','message':result.message,'warnings':solver_warnings}
 beta=result.x[:p];beta.astype('<f8').tofile(folder/'independent_beta.bin')
 cert,dual=certify(folder,X,y,{'historical':historical,'independent':beta},lam,result.eqlin.marginals,eta)
 status={'status':'SUCCESS','warnings':solver_warnings,
  'LP_method':'highs-ds','LP_iterations':int(result.nit),'reported_LP_objective':float(result.fun),
  'original_LP_equality_max_violation':float(max(abs(Aeq@result.x-y))),
  'original_LP_inequality_max_violation':float(max(0,max(Aub@result.x))),
  'original_LP_nonnegative_block_violation':float(max(0,-min(result.x[p:]))),
  'independent_primal_minus_LP_fun_float_diagnostic':cert['independent']['primal_objective']['float']-float(result.fun),
  'design_condition_float':float(np.linalg.cond(X)),
  'historical_certified_gap':cert['historical']['certified_gap']['outward_upper'],
  'independent_certified_gap':cert['independent']['certified_gap']['outward_upper'],
  'accuracy_budget':dual['accuracy_budget']['outward_upper'],
  'both_qualified':all(z['within_frozen_accuracy_envelope'] for z in cert.values())}
 dump(folder/'numerical_status.json',status);(folder/'independent_status.txt').write_text('SUCCESS\n')
 return status


def main():
 config=json.loads((HERE/'config.json').read_text())
 assert subprocess.check_output(['git','branch','--show-current'],cwd=ROOT,text=True).strip()=='journal-validation'
 for name in config['datasets']:
  for f in ['details.rds','sample.rds','rng_states.rds','coefficients.csv','observations.csv']:
   assert (HIST/name/f).is_file(),'Missing required saved input: '+str(HIST/name/f)
 eta_source=ROOT/config['prior_eta_source'];assert eta_source.is_file()
 eta_record=json.loads(eta_source.read_text())['eta'];eta=F(int(eta_record['numerator']),int(eta_record['denominator']))
 out=HERE/'output'/('paired_'+datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ'));out.mkdir(parents=True,exist_ok=False)
 print('RUN',out,flush=True)
 dump(out/'config.json',config);dump(out/'frozen_eta.json',eta_record)
 dump(out/'initial_state.json',{'branch':'journal-validation',
  'commit':subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),
  'git_status':subprocess.check_output(['git','status','--short'],cwd=ROOT,text=True),
  'source_hashes_before_execution':{p.name:sha(p) for p in HERE.iterdir() if p.is_file()},
  'python':sys.version,'numpy':np.__version__,'scipy':scipy.__version__})
 print('Hashing protected files',flush=True);before=snapshot();dump(out/'protected_before.json',before)
 status='FAILED';commands=[]
 def run_R(phase):
  argv=[r'C:\Program Files\R\R-3.4.3\bin\x64\Rscript.exe','--vanilla',str(HERE/'experiment.R'),str(out),phase]
  print('R_PHASE',phase,flush=True)
  started=datetime.now(timezone.utc).isoformat()
  with (out/(phase+'.log')).open('w') as log:p=subprocess.run(argv,cwd=ROOT,stdout=log,stderr=subprocess.STDOUT)
  commands.append({'argv':argv,'exit_status':p.returncode,'started_utc':started,'finished_utc':datetime.now(timezone.utc).isoformat()})
  dump(out/'commands.json',commands);assert p.returncode==0,'Historical R phase failed; see '+phase+'.log'
 try:
  oldmanifest=json.loads((HIST/'artifact_manifest.json').read_text())
  for name,r in oldmanifest.items():assert sha(HIST/name)==r['sha256'],name
  dump(out/'historical_manifest_verification.json',{'status':'PASS','artifacts':len(oldmanifest)})
  run_R('prepare');tasks=read(out/'task_manifest.csv');assert len(tasks)==24
  results=[]
  for task in tasks:
   print('INDEPENDENT_LP',task['id'],flush=True)
   try:result=independent(out/task['id'],eta,config)
   except Exception as exc:
    dump(out/task['id']/'CERTIFICATION_FAILURE.json',{'error':repr(exc)})
    (out/task['id']/'independent_status.txt').write_text('FAILED\n')
    result={'status':'NUMERICALLY_UNRESOLVED','error':repr(exc)}
   results.append(dict(id=task['id'],**result));dump(out/'numerical_statuses.json',results)
  run_R('evaluate');paths=read(out/'paired_paths_R.csv');assert len(paths)==24
  rows=[]
  for task in tasks:
   path=next(r for r in paths if r['id']==task['id']);cert=next(r for r in results if r['id']==task['id'])
   good=path['status']=='SUCCESS' and cert['status']=='SUCCESS'
   qualified=good and cert['both_qualified']
   Achange=good and path['historical_accepted']!=path['A_independent_accepted']
   Bchange=good and path['historical_accepted']!=path['B_independent_accepted']
   classification='C' if not qualified else 'B' if Achange or Bchange else 'A'
   rows.append(dict(task,**{k:v for k,v in path.items() if k not in task},
    classification=classification,both_objective_bounds_within_frozen_envelope=qualified,
    layer_A_decision_change=Achange,layer_B_decision_change=Bchange,
    historical_certified_gap=cert.get('historical_certified_gap'),independent_certified_gap=cert.get('independent_certified_gap'),
    accuracy_budget=cert.get('accuracy_budget'),numerical_status=cert['status']))
  table(out/'paired_summary.csv',rows)
  dump(out/'summary.json',{'paired_problems':24,'classification_counts':dict(Counter(r['classification'] for r in rows)),
   'layer_A_raw_decision_changes':sum(r['layer_A_decision_change'] for r in rows),
   'layer_B_raw_decision_changes':sum(r['layer_B_decision_change'] for r in rows),
   'layer_A_qualified_decision_changes':sum(r['both_objective_bounds_within_frozen_envelope'] and r['layer_A_decision_change'] for r in rows),
   'layer_B_qualified_decision_changes':sum(r['both_objective_bounds_within_frozen_envelope'] and r['layer_B_decision_change'] for r in rows)})
  status='COMPLETE';print((out/'summary.json').read_text(),flush=True)
 finally:
  after=snapshot();dump(out/'protected_after.json',after)
  preservation={'status':status,'files_checked':len(before),'changed':[p for p in before if p in after and before[p]!=after[p]],
   'missing':sorted(before.keys()-after.keys()),'added_outside_stage2e':sorted(after.keys()-before.keys())}
  dump(out/'preservation.json',preservation);assert not any(preservation[k] for k in ['changed','missing','added_outside_stage2e'])
  dump(out/'run_status.json',{'status':status});print('PRESERVATION',preservation,flush=True)


if __name__=='__main__':main()
