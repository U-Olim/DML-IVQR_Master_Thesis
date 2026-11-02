"""Independent initialization and adaptive penalty trace cross-checks."""
from common import *
from scipy.stats import norm

def main():
 rows=[]
 for task in csv.DictReader((OUT/'tasks.csv').open()):
  folder=OUT/task['id']/task['variant']
  for j in [1,2]:
   prefix=f'instrument_{j}_';X=readbin(folder/(prefix+'centered_X.bin'),(1000,100));y=readbin(folder/(prefix+'centered_y.bin'))
   parameters=readbin(folder/(prefix+'adaptive_parameters.bin'));lambda0,c,gamma,tol,maxiter=parameters
   coefficients=readbin(folder/(prefix+'trace_coefficients.bin')).reshape(-1,100);penalties=readbin(folder/(prefix+'trace_penalties.bin')).reshape(-1,100)
   assert c==.5 and abs(gamma-.1/np.log(1000))<1e-15
   lambda_expected=2*c*np.sqrt(1000)*norm.ppf(1-gamma/200)
   assert abs(lambda_expected-lambda0)<1e-11
   corr=np.corrcoef(np.column_stack([y,X]),rowvar=False)[0,1:];idx=np.argsort(-corr)[:5]
   design=np.column_stack([np.ones(1000),X[:,idx]]);beta=np.linalg.lstsq(design,y,rcond=None)[0];initial=y-design@beta
   original_initial=readbin(folder/(prefix+'initial_residual.bin'));initial_error=float(np.max(abs(initial-original_initial)))
   assert initial_error<1e-11
   residual=initial;last_scale=np.std(y,ddof=1);errors=[];margins=[]
   for step,b in enumerate(coefficients):
    expected=lambda0*np.sqrt(np.sum((residual[:,None]*X)**2,axis=0)/1000)
    err=float(np.max(abs(expected-penalties[step])));errors.append(err);assert err<1e-10
    residual=y-X@b;current_scale=np.std(residual,ddof=1);difference=abs(last_scale-current_scale)
    margins.append(abs(difference-tol))
    if step<len(coefficients)-1:assert difference>=tol-1e-12
    else:assert difference<tol+1e-12 or len(coefficients)==int(maxiter)
    last_scale=current_scale
   following=lambda0*np.sqrt(np.sum((residual[:,None]*X)**2,axis=0)/1000)
   next_penalty=readbin(folder/(prefix+'next_penalty.bin'));assert np.max(abs(following-next_penalty))<1e-10
   assert np.array_equal(penalties[-1],readbin(folder/(prefix+'last_penalty.bin')))
   row={'id':task['id'],'variant':task['variant'],'instrument':j,'status':'PASS','steps':len(coefficients),
    'initial_OLS_residual_max_error':initial_error,'initial_OLS_condition':float(np.linalg.cond(design)),
    'fifth_sixth_signed_correlation_gap':float(np.sort(corr)[-5]-np.sort(corr)[-6]),
    'lambda0_error':abs(lambda_expected-lambda0),'penalty_trace_max_error':max(errors),
    'outer_stopping_margin_min':min(margins),'last_vs_reported_next_penalty_max':float(np.max(abs(penalties[-1]-next_penalty)))}
   rows.append(row)
 table(OUT/'adaptive_verification.csv',rows);dump(OUT/'adaptive_verification.json',{'status':'PASS','fits':len(rows),'scope':'Independent floating initialization/penalty/update/stopping cross-check; not an interval proof over perturbed weights'})
 print('ADAPTIVE_PASS',len(rows),'fits',flush=True)
if __name__=='__main__':main()
