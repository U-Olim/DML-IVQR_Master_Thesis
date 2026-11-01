"""Fixed certified saved-vector inference comparisons; no data generation or fitting."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from collections import Counter
import csv,hashlib,itertools,json,os,subprocess,sys
import numpy as np

HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[2]
ORIGINAL=HERE.parent/'output/controlled_20261029_01'
PRIOR=HERE.parent/'validation_protocol/reassessment_20261029T083111Z'
FULL=HERE.parent/'certification/saved_inputs_20261029T080821Z/full_precision'
sys.path.insert(0,str(HERE.parent/'certification'))
from exact_bounds import dyadic,record


def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for block in iter(lambda:f.read(1024*1024),b''):h.update(block)
 return h.hexdigest()


def dump(p,x):
 def convert(v):
  if isinstance(v,np.generic):return v.item()
  if isinstance(v,np.ndarray):return v.tolist()
  raise TypeError(str(type(v)))
 p.write_text(json.dumps(x,indent=2,default=convert),encoding='utf-8')


def read(p):
 with p.open(newline='',encoding='utf-8-sig') as f:return list(csv.DictReader(f))


def table(p,rows):
 fields=list(dict.fromkeys(k for r in rows for k in r))
 with p.open('w',newline='',encoding='utf-8') as f:
  w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)


def snapshot():
 result={}
 for directory,subdirs,files in os.walk(ROOT):
  base=Path(directory);subdirs[:]=[d for d in subdirs if base/d!=HERE and not(base==ROOT and d=='.git')]
  for name in files:
   p=base/name;result[p.relative_to(ROOT).as_posix()]=sha(p)
 return result


def unpack(x):return F(int(x['numerator']),int(x['denominator']))


def exact_W(psi,score,cutoff):
 P,EP=dyadic(psi);S,ES=dyadic(score)
 obs=[[int(a)*int(s) for a in row] for row,s in zip(P.tolist(),S.tolist())]
 g=[sum(r[j] for r in obs) for j in [0,1]]
 Q=[sum(r[0]*r[0] for r in obs),sum(r[0]*r[1] for r in obs),sum(r[1]*r[1] for r in obs)]
 det=Q[0]*Q[2]-Q[1]**2;assert det>0
 W=F(g[0]**2*Q[2]-2*g[0]*g[1]*Q[1]+g[1]**2*Q[0],det)
 return {'W':record(W),'accepted':W<=F(float(cutoff)),
  'cutoff_margin':record(W-F(float(cutoff))),
  'score_sum_1':record(F(g[0],1 << (EP+ES))),
  'score_sum_2':record(F(g[1],1 << (EP+ES))),
  'S11':record(F(Q[0],1 << (2*(EP+ES)))),'S12':record(F(Q[1],1 << (2*(EP+ES)))),
  'S22':record(F(Q[2],1 << (2*(EP+ES)))),
  'scope':'Exact rational W for stored binary64 psi and historical floating score values; historical R ranks kept fixed.'}


def main():
 assert subprocess.check_output(['git','branch','--show-current'],cwd=ROOT,text=True).strip()=='journal-validation'
 run=HERE/('saved_stability_'+datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ'));run.mkdir(exist_ok=False)
 print('RUN',run,flush=True)
 dump(run/'initial_state.json',{'git_status':subprocess.check_output(['git','status','--short','--branch'],cwd=ROOT,text=True),
  'protocol_sha256_before_comparisons':sha(HERE/'PROTOCOL.md'),
  'source_sha256_before_execution':{p.name:sha(p) for p in HERE.iterdir() if p.is_file()}})
 print('Hashing protected inputs',flush=True);before=snapshot();dump(run/'protected_before.json',before)
 status='FAILED'
 try:
  m=json.loads((PRIOR/'SHA256_MANIFEST.json').read_text())
  for name,r in m.items():assert sha(PRIOR/name)==r['sha256'],name
  dump(run/'prior_manifest_verification.json',{'status':'PASS','artifacts':len(m)})
  arms=json.loads((PRIOR/'arm_summary.json').read_text());assert len(arms)==92
  budgets=[]
  for arm in arms:
   c=json.loads((PRIOR/arm['dataset']/arm['arm']/'exact_certificate.json').read_text())
   G=unpack(c['gap']);B=F(float(arm['gap_response_scale_reference']))
   budgets.append((G/B,arm,G,B))
  eta=max(t[0] for t in budgets)
  dump(run/'frozen_accuracy_budget.json',{'eta':record(eta),
   'definition':'max of all 92 certified G/B, no multiplier; frozen before baseline/probe inference',
   'interpretation':'Common observed-accuracy envelope for this sensitivity study, not an approved future optimization tolerance.',
   'arms':[{'dataset':a['dataset'],'arm':a['arm'],'scale_B':record(B),'original_gap':record(G),'allowed_gap':record(eta*B)} for _,a,G,B in budgets]})
  def phase(which):
   argv=[r'C:\Program Files\R\R-3.4.3\bin\x64\Rscript.exe','--vanilla',str(HERE/'scores.R'),str(ORIGINAL),str(run),which]
   with (run/(which+'.log')).open('w') as log:p=subprocess.run(argv,cwd=ROOT,stdout=log,stderr=subprocess.STDOUT)
   dump(run/(which+'_command.json'),{'argv':argv,'exit_status':p.returncode});assert p.returncode==0,which+' failed'
  phase('baseline');assert (run/'BASELINE_PASS.txt').is_file()
  baselines=read(run/'baseline_R.csv');assert len(baselines)==92
  # All baselines must pass before any probe or comparison is evaluated.
  cutoff=np.fromfile(run/'historical_cutoff.bin',dtype='<f8')[0]
  for b in baselines:
   assert float(b['residual_max_difference'])==0 and int(b['rank_differences'])==0
   assert float(b['W_difference'])<=1e-9 and b['accepted']==b['saved_accepted']
  print('BASELINE PASS: all 92 fits',flush=True)
  phase('probes');probe_rows=read(run/'probes_R.csv');assert len(probe_rows)==736
  classifications=[];comparisons=[];diagnostics=[];pairrows=[]
  for _,arm,G,B in budgets:
   name,a=arm['dataset'],arm['arm'];folder=run/name/a
   base=next(z for z in baselines if z['dataset']==name and z['arm']==a)
   psi=np.fromfile(run/name/'psi_observation_row_major.bin',dtype='<f8').reshape(1000,2)
   e=np.fromfile(folder/'baseline_residual.bin',dtype='<f8');score=np.fromfile(folder/'baseline_score.bin',dtype='<f8')
   beta=np.fromfile(folder/'baseline_beta.bin',dtype='<f8')
   assert np.array_equal(e,np.fromfile(FULL/name/(a+'_residual.bin'),dtype='<f8'))
   assert np.array_equal(beta,np.fromfile(FULL/name/(a+'_beta.bin'),dtype='<f8'))
   assert np.array_equal(np.fromfile(run/name/'y_candidate.bin',dtype='<f8'),np.fromfile(FULL/name/'y_candidate.bin',dtype='<f8'))
   exact=exact_W(psi,score,cutoff);assert exact['accepted']==(base['accepted']=='TRUE')
   assert abs(exact['W']['float']-float(base['W']))<1e-9
   dump(folder/'baseline_exact_inference.json',exact)
   diag={'dataset':name,'arm':a,'exact_zero_residuals':int(sum(e==0)),
    'min_absolute_residual':float(min(abs(e))),'median_absolute_residual':float(np.median(abs(e))),
    'W':float(base['W']),'cutoff':float(cutoff),'W_minus_cutoff':float(base['cutoff_distance']),
    'score_matrix_condition':float(base['condition'])}
   for threshold in [1e-12,1e-10,1e-8,1e-7,1e-6]:diag['abs_residual_le_'+str(threshold)]=int(sum(abs(e)<=threshold))
   diagnostics.append(diag)
   prior_probes=json.loads((PRIOR/name/a/'stability_probes.json').read_text())
   qualified=[{'id':'original','accepted':exact['accepted'],'W':exact['W']['float'],'gap_bound':float(G)}]
   per=[]
   for p in prior_probes:
    exponent,sign=p['exponent'],p['sign'];id='exp'+str(exponent)+'_sign'+str(sign)
    r=next(z for z in probe_rows if z['dataset']==name and z['arm']==a and z['id']==id)
    eb=np.fromfile(folder/(id+'_residual.bin'),dtype='<f8');sb=np.fromfile(folder/(id+'_score.bin'),dtype='<f8');bb=np.fromfile(folder/(id+'_beta.bin'),dtype='<f8')
    delta=unpack(p['intercept_step_exact']);assert F(float(bb[0]))-F(float(beta[0]))==delta
    assert np.array_equal(bb[1:],beta[1:])
    gap=unpack(p['exact_objective_gap_upper_bound']);qualifies=gap<=eta*B
    inf=exact_W(psi,sb,cutoff);assert abs(inf['W']['float']-float(r['W']))<1e-9
    assert inf['accepted']==(r['accepted']=='TRUE')
    flips=int(sum((eb<=0)!=(e<=0)));assert flips==int(r['rank_changes'])
    row={'dataset':name,'arm':a,'id':id,'exponent':exponent,'sign':sign,
     'prediction_RMS_change':float(abs(delta)),'rank_changes_R':flips,
     'rank_changes_exact_objective_arithmetic_prior':p['rank_sign_changes'],
     'certified_objective_gap_upper':float(gap),'budget':float(eta*B),'within_frozen_budget':qualifies,
     'original_W':float(base['W']),'alternative_W':inf['W']['float'],
     'delta_W':inf['W']['float']-exact['W']['float'],
     'original_accepted':exact['accepted'],'alternative_accepted':inf['accepted'],
     'decision_change':exact['accepted']!=inf['accepted'],
     'delta_mean_rank_score':float(r['mean_rank_score'])-float(base['mean_rank_score']),
     'delta_score_sum_1':float(r['score_sum_1'])-float(base['score_sum_1']),
     'delta_score_sum_2':float(r['score_sum_2'])-float(base['score_sum_2']),
     'delta_S11':float(r['S11'])-float(base['S11']),'delta_S12':float(r['S12'])-float(base['S12']),
     'delta_S22':float(r['S22'])-float(base['S22']),'condition':float(r['condition'])}
    comparisons.append(row);per.append(dict(id=id,qualifies=qualifies,exact_gap_bound=record(gap),inference=inf))
    if qualifies:qualified.append({'id':id,'accepted':inf['accepted'],'W':inf['W']['float'],'gap_bound':float(gap)})
   dump(folder/'alternative_exact_inference.json',per)
   opposite=len({z['accepted'] for z in qualified})>1
   classification=('Observed decision instability between certified near-optimal alternatives' if opposite else
     'Stable under the tested certified near-optimal alternatives' if len(qualified)>1 else 'Numerically indeterminate')
   classifications.append({'dataset':name,'arm':a,'classification':classification,
    'qualifying_alternatives_excluding_original':len(qualified)-1,'original_W':float(base['W']),
    'minimum_qualifying_W':min(z['W'] for z in qualified),'maximum_qualifying_W':max(z['W'] for z in qualified),
    'original_accepted':exact['accepted'],'historical_KKT':arm['certified_historical_LP_result']})
   for u,v in itertools.combinations(qualified,2):
    pairrows.append({'dataset':name,'arm':a,'first':u['id'],'second':v['id'],
     'first_W':u['W'],'second_W':v['W'],'different_decisions':u['accepted']!=v['accepted']})
  table(run/'near_zero_diagnostics.csv',diagnostics);table(run/'all_probe_inference.csv',comparisons)
  table(run/'arm_stability_classification.csv',classifications);table(run/'qualified_pairwise_inference.csv',pairrows)
  dump(run/'summary.json',{'arms':92,'classification_counts':dict(Counter(r['classification'] for r in classifications)),
   'all_probes':len(comparisons),'qualifying_probes':sum(r['within_frozen_budget'] for r in comparisons),
   'qualifying_probes_changing_original_decision':sum(r['within_frozen_budget'] and r['decision_change'] for r in comparisons),
   'historical_cutoff':float(cutoff),'eta':record(eta)})
  print(json.dumps(json.loads((run/'summary.json').read_text()),indent=2),flush=True)
  status='COMPLETE'
 finally:
  after=snapshot();dump(run/'protected_after.json',after)
  preservation={'status':status,'files_checked':len(before),'changed':[p for p in before if p in after and before[p]!=after[p]],
   'missing':sorted(before.keys()-after.keys()),'added_outside_stability':sorted(after.keys()-before.keys())}
  dump(run/'preservation.json',preservation);assert not any(preservation[k] for k in ['changed','missing','added_outside_stability'])
  dump(run/'run_status.json',{'status':status});print('PRESERVATION',preservation,flush=True)


if __name__=='__main__':main()
