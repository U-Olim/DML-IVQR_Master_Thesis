"""Independent split-variable LP; exact basis checks authorize ranks."""
from common_v1 import *
from outcome_exact_v1 import certify
from scipy.optimize import linprog
from scipy.sparse import csr_matrix,eye,hstack,save_npz
import warnings
def solve(X,y,lam,cfg,tau=.9):
 n,p=X.shape;I=eye(n,format='csr');A=hstack([csr_matrix(X),-csr_matrix(X),I,-I],format='csr')
 c=np.r_[lam/2,lam/2,np.full(n,tau),np.full(n,1-tau)]
 options={k:v for k,v in cfg.items() if k!='method'}
 with warnings.catch_warnings(record=True) as caught:
  warnings.simplefilter('always');result=linprog(c,A_eq=A,b_eq=y,bounds=(0,None),method=cfg['method'],options=options)
 return result,A,c,[str(v.message) for v in caught]
def main():
 cfg=load(HERE/'CONFIG_v1.json');results=[]
 for id in cases():
  f=OUT/id;f.mkdir(exist_ok=True);start=time.perf_counter()
  try:
   X=read(E/id/'X_row_major.bin',(1000,101));y=read(E/id/'response.bin');lam=read(E/id/'lambda.bin');n,p=X.shape
   t=time.perf_counter();lp,A,c,warnings_=solve(X,y,lam,cfg['outcome_LP']);solver_seconds=time.perf_counter()-t
   assert lp.success,lp.message
   beta=lp.x[:p]-lp.x[p:2*p];e=y-X@beta;dual=lp.eqlin.marginals
   save_npz(f/'LP_Aeq.npz',A);np.savez(f/'LP_vectors.npz',objective=c,rhs=y,lambda_vector=lam)
   np.savez(f/'LP_solution.npz',x=lp.x,equality_dual=dual,lower_marginals=lp.lower.marginals)
   put(f/'outcome_beta_LP.bin',beta)
   numerical={'solver_seconds':solver_seconds,'success':lp.success,'message':lp.message,'nit':lp.nit,
    'crossover_nit':lp.crossover_nit,'reported_objective':lp.fun,'warnings':warnings_,
    'primal_equality_max':float(np.max(abs(A@lp.x-y))), 'nonnegative_violation':float(max(0,-np.min(lp.x))),
    'dual_score_box_violation':float(max(0,np.max(dual-.9),np.max((.9-1)-dual))),
    'dual_penalty_violation':float(max(0,np.max(abs(X.T@dual)-lam/2))),
    'split_KKT_stationarity_max':float(np.max(abs(c-A.T@dual-lp.lower.marginals))),
    'split_KKT_complementarity_max':float(np.max(abs(lp.x*lp.lower.marginals)))}
   t=time.perf_counter();cert=certify(X,y,lam,beta,e,F(float(.9)),cfg['basis_proposal_threshold'])
   assert cert['unique_beta_and_fitted_values'],'No uniqueness certificate'
   exact_seconds=time.perf_counter()-t;dump(f/'outcome_certificate.json',cert)
   ref=load(G/'results'/id/'exact_optimum.json')
   b=[F(int(v),int(cert['beta_denominator'])) for v in cert['beta_numerators']]
   br=[F(int(v),int(ref['beta_denominator'])) for v in ref['beta_numerators']]
   assert b==br,'Independent optimum disagrees with reference'
   er=[F(int(v),int(cert['residual_denominator'])) for v in cert['residual_numerators']]
   put(f/'outcome_residual.bin',[float(v) for v in er]);put(f/'rank.bin',[v<=0 for v in er]);put(f/'outcome_beta_rounded.bin',[float(v) for v in b])
   xx,EX=dyadic(X);yy,EY=dyadic(y)
   P,ee,den,*_=exact_objective(xx.tolist(),EX,yy.tolist(),EY,[F(float(z)) for z in beta],[F(float(z)) for z in lam],F(float(.9)))
   gap=P-val(cert['dual']);assert gap>=0
   numerical.update({'exact_certification_seconds':exact_seconds,'LP_true_objective_gap':record(gap),
    'LP_coefficient_max_error':float(max(abs(F(float(v))-r) for v,r in zip(beta,b))),
    'LP_fitted_value_max_error':float(max(abs(F(a,den)-r) for a,r in zip(ee,er))),
    'LP_raw_float_sign_disagreements':int(sum((v<=0)!=(r<=0) for v,r in zip(e,er))),
    'exact_ranks_agree_Policy_C':True,'exact_zero_residuals':sum(v==0 for v in er)})
   t=time.perf_counter();lp2,_,_,_=solve(X,y,lam,cfg['outcome_LP']);repeat_seconds=time.perf_counter()-t
   same=bool(lp2.success and np.array_equal(lp.x,lp2.x));assert same,'LP not bitwise reproducible'
   numerical.update({'repeat_solver_seconds':repeat_seconds,'repeat_bitwise_identical':same,'status':'CERTIFIED_UNIQUE_OPTIMUM'})
   dump(f/'outcome_numerics.json',numerical)
   results.append({'id':id,'status':'PASS','LP_seconds':solver_seconds,'outcome_exact_seconds':exact_seconds,
    'LP_true_gap':float(gap),'LP_raw_sign_disagreements':numerical['LP_raw_float_sign_disagreements'],
    'certified_sign_disagreements':0,'ties':numerical['exact_zero_residuals'],
    'LP_fitted_max_error':numerical['LP_fitted_value_max_error'],'repeat_identical':same,'total_outcome_seconds':time.perf_counter()-start})
   print('OUTCOME',id,'PASS','LP seconds',solver_seconds,flush=True)
  except Exception as exc:
   dump(f/'OUTCOME_UNRESOLVED.json',{'error':repr(exc)});results.append({'id':id,'status':'OUTCOME_UNRESOLVED','error':repr(exc)})
   print('OUTCOME',id,'UNRESOLVED',repr(exc),flush=True)
 table(OUT/'outcome_validation.csv',results)
if __name__=='__main__':main()
