"""Reconstruct every primary outer update; numerical diagnostics, not B bounds."""
from support import *
def main():
 records=[];initial=[]
 for id in cases():
  f=OLD/id/'C'
  for j in (1,2):
   p=f'instrument_{j}_';X=read(f/(p+'centered_X.bin'),(1000,100));y=read(f/(p+'centered_y.bin'))
   B=read(f/(p+'trace_coefficients.bin')).reshape(-1,100);L=read(f/(p+'trace_penalties.bin')).reshape(-1,100)
   params=read(f/(p+'adaptive_parameters.bin'));lambda0,c,gamma,tol,maxit=params
   corr=np.corrcoef(np.column_stack([y,X]),rowvar=False)[0,1:];order=np.argsort(-corr,kind='stable')
   design=np.column_stack([np.ones(1000),X[:,order[:5]]]);beta=np.linalg.lstsq(design,y,rcond=None)[0]
   r=y-design@beta;actual_initial=read(f/(p+'initial_residual.bin'))
   initial.append({'id':id,'instrument':j,'selected_signed_correlation_indices':json.dumps((order[:5]+1).tolist()),
    'fifth_sixth_correlation_gap':float(corr[order[4]]-corr[order[5]]),'OLS_condition':float(np.linalg.cond(design)),
    'independent_OLS_max_residual_difference':float(np.max(abs(r-actual_initial))),
    'selection_and_QR_interval_status':'UNRESOLVED'})
   r=actual_initial;s0=np.std(y,ddof=1)
   for k,b in enumerate(B):
    expected=lambda0*np.sqrt(np.sum((r[:,None]*X)**2,axis=0)/1000)
    r=y-X@b;s1=np.std(r,ddof=1);difference=abs(s0-s1)
    records.append({'id':id,'instrument':j,'adaptive_step':k+1,'active_slopes':int(np.sum(b!=0)),
     'coefficient_change_L1_from_previous_outer_step':float(np.sum(abs(b-B[k-1]))) if k else 'NOT_APPLICABLE',
     'penalty_recalibration_max_error':float(np.max(abs(expected-L[k]))),'previous_scale':float(s0),'new_scale':float(s1),
     'absolute_scale_change':float(difference),'outer_tolerance':float(tol),'distance_to_stopping_threshold':float(abs(difference-tol)),
     'native_stops_here':k==len(B)-1,'outer_branch_interval_status':'UNRESOLVED_NOT_PROPAGATED_FROM_INITIALIZATION'})
    s0=s1
 table(OUT/'outer_adaptive_updates.csv',records);table(OUT/'initialization_analysis.csv',initial)
 inner=[];coordinate_rows=[]
 for call in rows(OUT/'shooting_calls.csv'):
  d=OUT/call['id'];p=call['prefix'];n=int(call['sweeps'])
  H=read(d/(p+'iterates.bin'),(100,n+1));G=2*read(d/(p+'XX.bin'),(100,100)).astype(np.longdouble)
  h=2*read(d/(p+'Xy.bin')).astype(np.longdouble);L=read(d/(p+'lambda.bin')).astype(np.longdouble)
  minmargin=np.longdouble(np.inf);max_update_difference=np.longdouble(0)
  for t in range(n):
   b=H[:,t].astype(np.longdouble).copy()
   for k in range(100):
    s=np.sum(G[k]*b)-G[k,k]*b[k]-h[k]
    minmargin=min(minmargin,abs(s-L[k]),abs(s+L[k]))
    expected=(L[k]-s)/G[k,k] if s>L[k] else (-L[k]-s)/G[k,k] if s<-L[k] else 0
    max_update_difference=max(max_update_difference,abs(expected-H[k,t+1]));b[k]=H[k,t+1]
   change=np.sum(np.abs(H[:,t+1].astype(np.longdouble)-H[:,t].astype(np.longdouble)))
   inner.append({'id':call['id'],'instrument':call['instrument'],'call':call['call'],'sweep':t+1,
    'L1_coefficient_change':float(change),'optTol':1e-5,'distance_to_threshold':float(abs(change-1e-5)),
    'native_last_sweep':t==n-1,'scope':'NATIVE_TRACE_DIAGNOSTIC_NOT_PROPAGATED_BOUND'})
  coordinate_rows.append({'id':call['id'],'instrument':call['instrument'],'call':call['call'],
   'coordinates_reconstructed':n*100,'minimum_soft_threshold_distance':float(minmargin),
   'max_longdouble_update_difference':float(max_update_difference),
   'minimum_final_zero_threshold_distance':float(np.min(abs(abs(H[:,-1])-1e-6))),
   'scope':'NATIVE_TRACE_DIAGNOSTIC_NOT_PROPAGATED_BOUND'})
 table(OUT/'inner_stopping_trace.csv',inner);table(OUT/'coordinate_branch_diagnostics.csv',coordinate_rows)
 dump(OUT/'adaptive_analysis_summary.json',{'primary_instrument_fits':48,'outer_updates':len(records),
  'minimum_outer_stopping_margin':min(r['distance_to_stopping_threshold'] for r in records),
  'minimum_signed_selection_gap':min(r['fifth_sixth_correlation_gap'] for r in initial),
  'max_penalty_reconstruction_error':max(r['penalty_recalibration_max_error'] for r in records),
  'max_initializer_condition':max(r['OLS_condition'] for r in initial),
  'inner_sweeps_recorded':len(inner),'coordinate_updates_reconstructed':sum(r['coordinates_reconstructed'] for r in coordinate_rows),
  'minimum_native_soft_threshold_distance':min(r['minimum_soft_threshold_distance'] for r in coordinate_rows),
  'max_longdouble_coordinate_update_difference':max(r['max_longdouble_update_difference'] for r in coordinate_rows),
  'scope':'Numerical trace reconstruction only; not a full adaptive branch certificate'})
if __name__=='__main__':main()
