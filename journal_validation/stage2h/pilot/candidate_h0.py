from common_h0 import *
import subprocess,shutil,traceback,os
from win_memory import Monitor,memory
def audit(id,mode):
 ns={'__name__':'readiness_independent_auditor','__file__':str(HERE/'independent_auditor_source.py.txt')}
 code=(HERE/'independent_auditor_source.py.txt').read_text(encoding='utf-8');exec(compile(code,ns['__file__'],'exec'),ns)
 ns['OUT']=OUT/mode;ns['E']=INPUT
 X=ns['verify_outcome'](id);width=ns['verify_instruments'](id,X)
 return {'status':'PASS','direct_rational_outcome_and_sign_checks':True,'exact_instrument_checks':2,'W_interval_width':width}
def main():
 id,mode=sys.argv[1:];src=INPUT/id;f=OUT/mode/id;f.mkdir(parents=True,exist_ok=True)
 meta=load(src/'metadata.json');n=int(meta['n']);tau,kappa,alpha=read(src/'parameters.bin');cfg=load(V1/'CONFIG_v1.json')
 start=time.perf_counter();monitor=Monitor().start();result={'id':id,'mode':mode,'n':n,'tau':float(tau),'kappa':float(kappa),'candidate_alpha':float(alpha),'status':'UNRESOLVED'}
 try:
  X=read(src/'X_row_major.bin',(n,101));y=read(src/'response.bin');lam=read(src/'lambda.bin');Z=read(src/'Z_row_major.bin',(n,2))
  t=time.perf_counter();lp,A,c,warnings_=solve(X,y,lam,cfg['outcome_LP'],tau=float(tau));result['outcome_solve_seconds']=time.perf_counter()-t
  if not lp.success:raise ArithmeticError('OUTCOME_UNRESOLVED: '+lp.message)
  beta=lp.x[:101]-lp.x[101:202];put(f/'LP_beta.bin',beta);np.savez_compressed(f/'LP_diagnostics.npz',x=lp.x,dual=lp.eqlin.marginals)
  t=time.perf_counter();cert=certify(X,y,lam,beta,y-X@beta,F(float(tau)),cfg['basis_proposal_threshold']);result['outcome_certificate_seconds']=time.perf_counter()-t
  dump(f/'outcome_certificate.json',cert);er=[F(int(v),int(cert['residual_denominator'])) for v in cert['residual_numerators']]
  rank=np.array([v<=0 for v in er]);put(f/'outcome_residual.bin',[float(v) for v in er]);put(f/'rank.bin',rank)
  result.update({'certified_residual_signs':n,'exact_zero_residuals':sum(v==0 for v in er),
   'raw_LP_sign_disagreements':int(np.sum((y-X@beta<=0)!=rank)),
   'LP_equality_max_error':float(np.max(abs(A@lp.x-y))),'outcome_exact_gap':0,
   'LP_warnings':warnings_})
  t=time.perf_counter()
  with (f/'calibration.log').open('w',encoding='utf-8') as log:
   p=subprocess.run([r'C:/Program Files/R/R-3.4.3/bin/x64/Rscript.exe','--vanilla',str(HERE/'calibrate_original.R'),id,str(f)],cwd=ROOT,env=os.environ.copy(),stdout=log,stderr=subprocess.STDOUT)
  result['calibration_process_seconds']=time.perf_counter()-t
  if p.returncode:raise ArithmeticError('INSTRUMENT_UNRESOLVED: native calibration process failed')
  hashes={f'instrument_{j}_last_penalty.bin':sha(f/f'instrument_{j}_last_penalty.bin') for j in (1,2)};dump(f/'calibration_hashes.json',hashes)
  coeff=np.zeros((101,2));solver_seconds=0;diagnostics=[]
  for j in (1,2):
   prefix=f'instrument_{j}_';xc=read(f/(prefix+'centered_X.bin'),(n,100));yc=read(f/(prefix+'centered_y.bin'));l=read(f/(prefix+'last_penalty.bin'));cent=read(f/(prefix+'centering.bin'))
   t=time.perf_counter();b,diag=optimize(xc,yc,l,cfg['instrument']);solver_seconds+=time.perf_counter()-t
   coeff[1:,j-1]=b;coeff[0,j-1]=cent[0]-cent[1:]@b;diagnostics.append(diag)
  result['instrument_solve_seconds']=solver_seconds
  psi=Z-X@coeff;score=tau-rank;obs=psi*score[:,None];g=obs.sum(axis=0);S=obs.T@obs;W=float(g@np.linalg.solve(S,g))
  for name,z in [('instrument_coefficients',coeff),('psi',psi),('score',score),('observation_scores',obs),('score_sum',g),('second_moment',S),('W',[W])]:put(f/(name+'.bin'),z)
  t=time.perf_counter();refs=[];radii=[];ics=[]
  for j in (1,2):
   ic,ref,rad=certificate(f,j,coeff[1:,j-1],X[:,1:],Z[:,j-1],read(f/f'instrument_{j}_centering.bin'))
   refs.append(ref);radii.append(rad);ics.append(ic)
  result['instrument_certificate_seconds']=time.perf_counter()-t
  t=time.perf_counter();cut=F(float(read(INPUT/'cutoff.bin')[0]));sr=[F(float(v)) for v in score]
  reference=rational_stat(list(zip(*refs)),sr,cut);bound=bound_W(list(zip(*refs)),radii,sr,cut);inf=exact_W(psi,score,cut)
  if bound['status'] not in ['ACCEPT_CERTIFIED','REJECT_CERTIFIED']:raise ArithmeticError('INFERENCE_UNRESOLVED: '+bound['status'])
  assert val(bound['lower'])<=F(W)<=val(bound['upper'])
  assert inf['accepted']==reference['accepted']==(W<=float(cut))
  dump(f/'decision_bounds.json',bound);dump(f/'exact_returned_score_inference.json',inf);dump(f/'exact_reference_inference.json',reference)
  result.update({'inference_certificate_seconds':time.perf_counter()-t,'W':W,'accepted':W<=float(cut),'cutoff':float(cut),
   'native_C_W':float(read(f/'native_W.bin')[0]),'W_lower':bound['lower']['float'],'W_upper':bound['upper']['float'],
   'W_reconstruction_error':abs(W-inf['W']['float']),'W_consistent_with_exact_reference':True,
   'max_instrument_objective_gap':max(v['returned_true_gap']['float'] for v in ics),
   'max_instrument_KKT':max(v['KKT_max'] for v in diagnostics),'S_condition':float(np.linalg.cond(S))})
  result['candidate_with_certificates_before_independent_audit_seconds']=time.perf_counter()-start
  t=time.perf_counter();independent=audit(id,mode);result['independent_audit_seconds']=time.perf_counter()-t
  dump(f/'independent_verification.json',independent)
  fingerprints={}
  for name in ['LP_beta.bin','outcome_certificate.json','outcome_residual.bin','rank.bin','density.bin','instrument_coefficients.bin','psi.bin','score.bin','second_moment.bin','W.bin','decision_bounds.json']+list(hashes):fingerprints[name]=sha(f/name)
  result['fingerprints']=fingerprints;result['status']='PASS'
 except Exception as exc:
  result['failure_component']=('OUTCOME_UNRESOLVED' if not (f/'outcome_certificate.json').exists() else 'INSTRUMENT_UNRESOLVED' if not (f/'instrument_2_certificate.json').exists() else 'INFERENCE_UNRESOLVED'); result['error']=repr(exc);result['traceback']=traceback.format_exc();dump(f/'UNRESOLVED.json',{'error':repr(exc),'traceback':result['traceback']})
 finally:
  if result['status']!='PASS':
   t=time.perf_counter()
   try: independent=audit(id,mode)
   except Exception as exc: independent={'status':'UNRESOLVED','error':repr(exc),'scope':'independent audit of retained attempted certificates; missing artifacts explicit'}
   dump(f/'independent_verification.json',independent);result['independent_audit_seconds']=time.perf_counter()-t
  result['total_candidate_seconds']=time.perf_counter()-start;result['memory']=monitor.finish();result['own_OS_memory']=memory(os.getpid())
  result['payload_bytes_before_result_json']=sum(p.stat().st_size for p in f.rglob('*') if p.is_file());dump(f/'result.json',result)
  print(id,mode,result['status'],result.get('W'),result.get('error',''),flush=True)
if __name__=='__main__':main()
