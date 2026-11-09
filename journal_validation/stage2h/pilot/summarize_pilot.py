"""Denominator-preserving summaries and independent saved-score validation."""
import os,sys
sys.dont_write_bytecode=True
for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS']:os.environ[k]='1'
from pathlib import Path
import json,csv,math,hashlib
import numpy as np
from scipy.stats import beta,norm
P=Path(__file__).resolve().parent;ROOT=P.parents[2]
run=Path(sys.argv[1] if len(sys.argv)>1 else (P/'LATEST_RUN.txt').read_text().strip());os.environ['STAGE2H_RUN']=str(run)
from common_h0 import read,load,dump,table,sha,F,exact_W
def cp(k,n):return [0. if k==0 else float(beta.ppf(.025,k,n-k+1)),1. if k==n else float(beta.ppf(.975,k+1,n-k))]
def meanstats(x,prefix):
 x=np.asarray(x,dtype=float);n=len(x)
 return {prefix+'N':n,prefix+'mean':float(x.mean()) if n else None,prefix+'SD':float(x.std(ddof=1)) if n>1 else None,prefix+'MCSE':float(x.std(ddof=1)/math.sqrt(n)) if n>1 else None}
def main():
 design=list(csv.DictReader((run/'DESIGN.csv').open()));obs=[];checks=[];diagnostics=[];relevance=[]
 cutoff=read(run/'inputs/cutoff.bin')[0];assert cutoff==5.99146454710798
 assert sha(run/'inputs/cutoff.bin')==sha(P.parent/'readiness/inputs/cutoff.bin')
 for d in design:
  id=d['id'];n=int(d['n']);tau=float(d['tau']);f=run/'results/pilot'/id;src=run/'inputs'/id
  r=load(f/'result.json') if (f/'result.json').exists() else {'status':'NOT_EXECUTED','attempted':False}
  ok=r['status']=='PASS';row=dict(d,status=r['status'],component=r.get('failure_component',''),attempted=r.get('attempted',True),qualified=ok,accepted=r.get('accepted') if ok else None,W=r.get('W') if ok else None,error=r.get('error',''))
  obs.append(row)
  if ok:
   X=read(src/'X_row_major.bin',(n,101));Z=read(src/'Z_row_major.bin',(n,2));ranks=read(f/'rank.bin');s=read(f/'score.bin');psi=read(f/'psi.bin',(n,2));z=read(f/'observation_scores.bin',(n,2));S=read(f/'second_moment.bin',(2,2));g=read(f/'score_sum.bin')
   assert np.array_equal(s,tau-ranks) and np.array_equal(z,psi*s[:,None])
   assert np.array_equal(S,z.T@z) and np.array_equal(g,z.sum(axis=0))
   W=float(g@np.linalg.solve(S,g));assert W==r['W']
   assert load(f/'independent_verification.json')['status']=='PASS'
   assert F(float(r['cutoff']))==F(float(cutoff))
   assert all(sha(f/name)==h for name,h in load(f/'calibration_hashes.json').items())
   checks.append({'id':id,'status':'PASS','W_reconstruction_error':abs(W-load(f/'exact_returned_score_inference.json')['W']['float'])})
   density=read(f/'density.bin');diagnostics.append(dict(d,density_min=float(density.min()),density_max=float(density.max()),S_eigen_min=float(np.linalg.eigvalsh(S/n)[0]),S_eigen_max=float(np.linalg.eigvalsh(S/n)[1]),S_condition=r['S_condition'],instrument_residual_variance_1=float(np.var(psi[:,0],ddof=1)),instrument_residual_variance_2=float(np.var(psi[:,1],ddof=1)),W_width=r['W_upper']-r['W_lower'],max_KKT=r['max_instrument_KKT'],max_objective_gap=r['max_instrument_objective_gap'],outcome_gap=r['outcome_exact_gap'],execution_seconds=r['total_candidate_seconds'],certification_seconds=sum(r.get(k,0) for k in ['outcome_certificate_seconds','instrument_certificate_seconds','inference_certificate_seconds']),audit_seconds=r['independent_audit_seconds']))
  else:checks.append({'id':id,'status':'UNRESOLVED_RETAINED','error':row['error']})
  if float(d['offset'])==0 and tau==.1:
   X=read(src/'X_row_major.bin',(n,101));Z=read(src/'Z_row_major.bin',(n,2));D=read(src/'D.bin');Q=read(run/'inputs'/d['sample_id']/'Q.bin',(n,2))
   e0=D-X@np.linalg.lstsq(X,D,rcond=None)[0];A=np.column_stack([X,Z]);e1=D-A@np.linalg.lstsq(A,D,rcond=None)[0];rss0=e0@e0;rss1=e1@e1
   relevance.append(dict(d,cov_D_Q1=float(np.cov(D,Q[:,0],ddof=1)[0,1]),cov_D_Q2=float(np.cov(D,Q[:,1],ddof=1)[0,1]),partial_R2=float((rss0-rss1)/rss0),first_stage_F=float(((rss0-rss1)/2)/(rss1/(n-103))),D_min=float(D.min()),D_max=float(D.max()),D_mean=float(D.mean()),D_variance=float(D.var(ddof=1))))
 table(run/'raw_evaluations.csv',obs);table(run/'numerical_validation.csv',checks)
 if diagnostics:table(run/'numerical_diagnostics.csv',diagnostics)
 table(run/'instrument_relevance.csv',relevance)
 summaries=[];paired=[]
 for n in [500,1000]:
  for tau in [.1,.5,.9]:
   for k in [1.,.1]:
    for off in [-.5,0.,.5]:
     selected=[r for r in obs if int(r['n'])==n and float(r['tau'])==tau and float(r['kappa'])==k and float(r['offset'])==off]
     for arm in ['A','B']:
      rr=[r for r in selected if r['arm']==arm];assert len(rr)==20
      good=[r for r in rr if r['qualified']];acc=sum(r['accepted'] for r in good);rej=len(good)-acc;u=20-len(good);ws=[r['W'] for r in good]
      row={'n':n,'tau':tau,'kappa':k,'offset':off,'arm':arm,'planned':20,'attempted':sum(r['attempted'] for r in rr),'qualified':len(good),'accepted':acc,'rejected':rej,'unresolved_or_not_executed':u,'not_executed':sum(not r['attempted'] for r in rr),'acceptance_lower':acc/20,'acceptance_upper':(acc+u)/20,'rejection_lower':rej/20,'rejection_upper':(rej+u)/20,'qualified_acceptance':acc/len(good) if good else None,'acceptance_lower_completion_MCSE':math.sqrt((acc/20)*(1-acc/20)/20),'acceptance_upper_completion_MCSE':math.sqrt(((acc+u)/20)*(1-(acc+u)/20)/20),'rejection_lower_completion_MCSE':math.sqrt((rej/20)*(1-rej/20)/20),'rejection_upper_completion_MCSE':math.sqrt(((rej+u)/20)*(1-(rej+u)/20)/20),'acceptance_lower_completion_CP95':json.dumps(cp(acc,20)),'acceptance_upper_completion_CP95':json.dumps(cp(acc+u,20)),'rejection_lower_completion_CP95':json.dumps(cp(rej,20)),'rejection_upper_completion_CP95':json.dumps(cp(rej+u,20)),**meanstats(ws,'qualified_W_')}
      if ws:row.update(dict(zip(['W_q05','W_q25','W_median','W_q75','W_q95'],map(float,np.quantile(ws,[.05,.25,.5,.75,.95])))))
      summaries.append(row)
     AA={r['replication']:r for r in selected if r['arm']=='A'};BB={r['replication']:r for r in selected if r['arm']=='B'}
     lower=[];upper=[];diff=[];wdiff=[];ab=ba=0
     for rep in AA:
      a,b=AA[rep],BB[rep];la=int(a['accepted']) if a['qualified'] else 0;ua=la if a['qualified'] else 1;lb=int(b['accepted']) if b['qualified'] else 0;ub=lb if b['qualified'] else 1
      lower.append(lb-ua);upper.append(ub-la)
      if a['qualified'] and b['qualified']:
       diff.append(lb-la);wdiff.append(b['W']-a['W']);ab+=int(la==1 and lb==0);ba+=int(la==0 and lb==1)
     discord=ab+ba;N=len(diff)
     paired.append({'n':n,'tau':tau,'kappa':k,'offset':off,'planned_pairs':20,'complete_pairs':N,'acceptance_B_minus_A_lower':float(np.mean(lower)),'acceptance_B_minus_A_upper':float(np.mean(upper)),'rejection_B_minus_A_lower':-float(np.mean(upper)),'rejection_B_minus_A_upper':-float(np.mean(lower)),'A_accept_B_reject':ab,'A_reject_B_accept':ba,'discordant_pairs':discord,'discordance_CP95_complete_pairs':json.dumps(cp(discord,N)) if N else None,'B_improvement_given_discordance_CP95':json.dumps(cp(ba,discord)) if discord else None,'zero_discordance_two_sided95_upper':cp(0,N)[1] if N and discord==0 else None,**meanstats(diff,'complete_acceptance_difference_'),**meanstats([-x for x in diff],'complete_rejection_difference_'),**meanstats(wdiff,'complete_W_difference_')})
 table(run/'coverage_rejection_summary.csv',summaries);table(run/'paired_comparisons.csv',paired)
 # Verify exactly 0.90 relevance scaling and invariant partial R2/F within each sample.
 rmap={(r['sample_id'],r['kappa'],r['arm']):r for r in relevance};maxerr=0.
 for (sid,k,arm),a in rmap.items():
  if arm!='A':continue
  b=rmap[sid,k,'B'];maxerr=max(maxerr,abs(b['cov_D_Q1']-.9*a['cov_D_Q1']),abs(b['cov_D_Q2']-.9*a['cov_D_Q2']),abs(b['D_variance']-.81*a['D_variance']),abs(b['partial_R2']-a['partial_R2']),abs(b['first_stage_F']-a['first_stage_F']))
 assert maxerr<1e-8
 dump(run/'SUMMARY.json',{'planned':1440,'attempted':sum(r['attempted'] for r in obs),'qualified':sum(r['qualified'] for r in obs),'unresolved_or_not_executed':sum(not r['qualified'] for r in obs),'truth_planned':480,'truth_qualified':sum(r['qualified'] and float(r['offset'])==0 for r in obs),'relevance_affine_identity_max_error':maxerr,'statistical_scope':'pointwise per-cell; no pooling dependent cells; qualified-only W and complete-pair summaries explicitly selected'})
 print(json.dumps(load(run/'SUMMARY.json')),flush=True)
if __name__=='__main__':main()
