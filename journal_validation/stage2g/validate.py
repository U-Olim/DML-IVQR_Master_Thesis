"""Saved-panel policy assessment. Never calls a numerical fit or edits inputs."""
from pathlib import Path
from fractions import Fraction as F
import sys,json,time,subprocess,os
import numpy as np
HERE=Path(__file__).resolve().parent; ROOT=HERE.parents[1]
sys.path.insert(0,str(ROOT/'journal_validation/stage2f'))
from analyze import reconstruct,exact_objective,exact_W,dyadic,record,dump,table,sha,read,SOURCE
TAU=F(float(.9))

def snapshot():
 result={}
 for directory,dirs,files in os.walk(ROOT):
  base=Path(directory)
  dirs[:]=[d for d in dirs if base/d!=HERE and not(base==ROOT and d=='.git')]
  for name in files:
   p=base/name;result[p.relative_to(ROOT).as_posix()]=sha(p)
 return result

def main():
 out=HERE/'results'
 resume='--resume-integrity' in sys.argv
 out.mkdir(exist_ok=resume)
 start=time.perf_counter()
 before=json.loads((out/'protected_before.json').read_text()) if resume else snapshot()
 if not resume:dump(out/'protected_before.json',before)
 dump(out/'initial_state.json',{'branch':subprocess.check_output(['git','branch','--show-current'],text=True).strip(),'HEAD':subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip(),'status':subprocess.check_output(['git','status','--short'],text=True)})
 integrity=[]
 for src in [SOURCE,ROOT/'journal_validation/stage2f/output/exact_face_20261029T102755Z']:
  manifests=[src/'SHA256_MANIFEST.json']
  for mf in manifests:
   data=json.loads(mf.read_text());count=0
   for name,r in data.items():
    p=src/name
    expected=r['sha256'] if isinstance(r,dict) else r
    assert sha(p)==expected,(mf,name);count+=1
   integrity.append({'manifest':str(mf.relative_to(ROOT)),'verified':count})
 dump(out/'source_integrity.json',integrity)
 tasks=read(SOURCE/'complete_24_problem_table.csv')
 tasks.sort(key=lambda r:(r['id'] not in ['pilot_002_minus','pilot_006_truth'],r['id']))
 cutoff=F(float(np.fromfile(SOURCE/'cutoff.bin',dtype='<f8')[0]));rows=[];cases=[]
 for task in tasks:
  case_start=time.perf_counter();id=task['id'];src=SOURCE/id;folder=out/id;folder.mkdir()
  print('ASSESS',id,flush=True)
  X=np.fromfile(src/'X_row_major.bin',dtype='<f8').reshape(1000,101);y=np.fromfile(src/'response.bin',dtype='<f8');lam=np.fromfile(src/'lambda.bin',dtype='<f8')
  hb=np.fromfile(src/'historical_beta.bin',dtype='<f8');ib=np.fromfile(src/'independent_beta.bin',dtype='<f8')
  he=np.fromfile(src/'historical_residual.bin',dtype='<f8');ie=np.fromfile(src/'independent_residual.bin',dtype='<f8')
  hp=np.fromfile(src/'historical_psi.bin',dtype='<f8').reshape(1000,2);ip=np.fromfile(src/'independent_psi.bin',dtype='<f8').reshape(1000,2)
  cert=None;error=None
  try:
   cert=reconstruct(X,y,lam,ib,ie,TAU);assert cert['unique_beta_and_fitted_values']
   dump(folder/'exact_optimum.json',cert)
  except Exception as exc:error=repr(exc)
  XX,EX=dyadic(X);YY,EY=dyadic(y);Xi=XX.tolist();yi=YY.tolist();pen=[F(float(z)) for z in lam]
  beta=([F(int(z),int(cert['beta_denominator'])) for z in cert['beta_numerators']] if cert else None)
  er=([int(z) for z in cert['residual_numerators']] if cert else None)
  observations=[];inferences={};accuracy={}
  for side,b,e in [('historical',hb,he),('independent',ib,ie)]:
   P,ee,D,*_=exact_objective(Xi,EX,yi,EY,[F(float(z)) for z in b],pen,TAU)
   accuracy[side]={'primal':record(P),'floating_vs_exact_same_vector_sign_changes':sum((a<=0)!=(v<=0) for a,v in zip(ee,e))}
   if cert:
    lower=F(int(cert['dual']['numerator']),int(cert['dual']['denominator']))
    accuracy[side].update(dual_lower=record(lower),true_gap=record(P-lower),coefficient_max_error=float(max(abs(F(float(v))-z) for v,z in zip(b,beta))),fitted_max_error=float(max(abs(F(a,D)-F(z,int(cert['residual_denominator']))) for a,z in zip(ee,er))))
  policies=[('A',he<=0,hp),('B_float_frozen',ie<=0,hp),('B_float_saved_path',ie<=0,ip)]
  if cert:
   rank=np.array([z<=0 for z in er]);ties=np.array([z==0 for z in er])
   policies.extend([('C_exact_frozen',rank,hp),('C_exact_saved_independent_psi',rank,ip),('D_strict_frozen',np.array([z<0 for z in er]),hp)])
   # All tie ranks are locally realizable: square nonsingular tied/active basis.
   # Exact optimizer is a singleton; positive objective sublevels are different sets.
   for i in range(1000):observations.append({'observation':i+1,'exact_residual_numerator':str(er[i]),'exact_zero':bool(ties[i]),'A_rank':bool(he[i]<=0),'B_rank':bool(ie[i]<=0),'C_rank':bool(rank[i]),'positive_budget_locally_ambiguous':bool(ties[i])})
   table(folder/'signs.csv',observations)
  for policy,rank,psi in policies:
   inf=exact_W(psi,.9-rank.astype(float),cutoff);inferences[policy]=inf
   row={'id':id,'policy':policy,'W':inf['W']['float'],'accepted':inf['accepted'],'rank_changes_from_A':int(np.sum(rank!=(he<=0))),'certified_optimum_signs':1000 if cert and policy.startswith(('C','D')) else 0,'positive_budget_locally_ambiguous_signs':sum(z==0 for z in er) if cert else '', 'uncertified_optimum_signs':0 if cert and policy.startswith(('C','D')) else 1000,'scope':'fixed saved psi; no new complete-path certificate'}
   for key in ['score_sum_1','score_sum_2','S11','S12','S22']:row[key]=inf[key]['float']
   rows.append(row)
  dump(folder/'inference.json',inferences);dump(folder/'accuracy.json',accuracy)
  # Deterministic finite sensitivity search, only local tie patterns at saved hp.
  # It supplies witnesses, never global bounds. Exact arithmetic verifies extrema.
  sensitivity=None
  if cert:
   base=np.array([z<=0 for z in er]);idx=np.flatnonzero(np.array(er,dtype=object)==0)
   patterns=[base.copy(),he<=0,ie<=0,np.array([z<0 for z in er])]
   # Coordinate descent/ascent initialized at all four fixed patterns.
   def wf(r):
    z=hp*(.9-r.astype(float))[:,None];g=z.sum(axis=0);S=z.T@z
    return float(g@np.linalg.solve(S,g))
   for direction in [-1,1]:
    for initial in patterns[:4]:
     r=initial.copy()
     for sweep in range(10):
      changed=False;w=wf(r)
      for i in idx:
       r[i]=not r[i];v=wf(r)
       if direction*v>direction*w:w=v;changed=True
       else:r[i]=not r[i]
      if not changed:break
     patterns.append(r)
   values=[wf(r) for r in patterns];lo=patterns[int(np.argmin(values))];hi=patterns[int(np.argmax(values))]
   sensitivity={'minimum_found':exact_W(hp,.9-lo.astype(float),cutoff),'maximum_found':exact_W(hp,.9-hi.astype(float),cutoff),'minimum_rank':lo.tolist(),'maximum_rank':hi.tolist(),'global_bounds':False,'scope':'local tied-sign patterns; not full downstream path','all_tie_patterns_locally_realizable':True}
   sensitivity['opposite_decisions_found']=sensitivity['minimum_found']['accepted']!=sensitivity['maximum_found']['accepted']
   dump(folder/'sensitivity.json',sensitivity)
  result={'id':id,'exact_unique':bool(cert),'failure':error,'ties':sum(z==0 for z in er) if cert else None,'seconds':time.perf_counter()-case_start,'positive_budget_noninvariance_witness':sensitivity['opposite_decisions_found'] if sensitivity else None}
  cases.append(result);dump(folder/'status.json',result);print(json.dumps(result),flush=True)
 table(out/'policy_results.csv',rows);dump(out/'cases.json',cases)
 after=snapshot();dump(out/'protected_after.json',after)
 preservation={'checked':len(before),'changed':[p for p in before if p in after and before[p]!=after[p]],'missing':sorted(before.keys()-after.keys()),'added':sorted(after.keys()-before.keys())}
 dump(out/'preservation.json',preservation);assert not any(preservation[k] for k in ['changed','missing','added'])
 dump(out/'run.json',{'seconds':time.perf_counter()-start,'cases':len(cases),'exact_unique':sum(r['exact_unique'] for r in cases),'cutoff':record(cutoff)})

if __name__=='__main__':main()
