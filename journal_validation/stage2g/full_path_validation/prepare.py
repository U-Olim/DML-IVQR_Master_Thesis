"""Preserve inputs; exact residual export and predeclared near-optimal witnesses."""
from common import *
import subprocess,time,platform

def export(folder,beta,e,den,certificate):
 folder.mkdir(parents=True,exist_ok=False)
 np.array([float(b) for b in beta],dtype='<f8').tofile(folder/'outcome_beta_rounded.bin')
 np.array([float(F(v,den)) for v in e],dtype='<f8').tofile(folder/'outcome_residual.bin')
 np.array([v<=0 for v in e],dtype='<f8').tofile(folder/'rank.bin')
 dump(folder/'outcome_certificate.json',certificate)

def main():
 OUT.mkdir(exist_ok=False);start=time.perf_counter()
 print('Snapshot protected files',flush=True);dump(OUT/'protected_before.json',snapshot())
 dump(OUT/'initial_state.json',{'branch':subprocess.check_output(['git','branch','--show-current'],cwd=ROOT,text=True).strip(),'HEAD':subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),'git_status':subprocess.check_output(['git','status','--short'],cwd=ROOT,text=True),'python':sys.version,'numpy':np.__version__,'platform':platform.platform()})
 manifests=[]
 for parent in [G,E,ROOT/'journal_validation/stage2f/output/exact_face_20261029T102755Z']:
  m=json.loads((parent/'SHA256_MANIFEST.json').read_text())
  for name,r in m.items():assert sha(parent/name)==r['sha256'],(parent,name)
  manifests.append({'root':str(parent.relative_to(ROOT)),'files':len(m)})
 dump(OUT/'input_integrity.json',manifests)
 cases=json.loads((G/'results/cases.json').read_text());tasks=[]
 tau=F(float(.9))
 for case in cases:
  id=case['id'];src=E/id;cert=json.loads((G/'results'/id/'exact_optimum.json').read_text())
  beta=[F(int(z),int(cert['beta_denominator'])) for z in cert['beta_numerators']]
  X=readbin(src/'X_row_major.bin',(1000,101));y=readbin(src/'response.bin');lam=[F(float(z)) for z in readbin(src/'lambda.bin')]
  xx,EX=dyadic(X);yy,EY=dyadic(y);Xi=xx.tolist();yi=yy.tolist()
  P,e,D,_,_,bn,LB=exact_objective(Xi,EX,yi,EY,beta,lam,tau)
  assert P==val(cert['primal']) and [F(a,D) for a in e]==[F(int(z),int(cert['residual_denominator'])) for z in cert['residual_numerators']]
  export(OUT/id/'C',beta,e,D,{'type':'exact_optimum','source_sha256':sha(G/'results'/id/'exact_optimum.json'),'primal':record(P),'gap':record(F(0)),'residual_numerators':[str(v) for v in e],'residual_denominator':str(D)})
  tasks.append({'id':id,'variant':'C','epsilon':'0'})
  if case['positive_budget_noninvariance_witness']:
   sensitivity=json.loads((G/'results'/id/'sensitivity.json').read_text());S=cert['active_coefficients_zero_based'];T=[i-1 for i in cert['tied_observations_one_based']];Tset=set(T)
   A=[[Xi[i][j] for j in S] for i in T];res=[F(v,D) for v in e]
   for side in ['minimum','maximum']:
    target=sensitivity[side+'_rank'];z=[-1 if target[i] else 1 for i in T]
    direction=[F(0)]*101
    for j,v in zip(S,integer_solve_rational_rhs(A,[F(-v*(1<<EX)) for v in z])):direction[j]=v
    pred=[sum((F(a,1<<EX)*d for a,d in zip(row,direction)),F(0)) for row in Xi]
    delta=F(1)
    for j in S:
     if direction[j]:delta=min(delta,abs(beta[j])/(2*abs(direction[j])))
    for i in range(1000):
     if i not in Tset and pred[i]:delta=min(delta,abs(res[i])/(2*abs(pred[i])))
    lip=sum(map(abs,pred))+sum(l*abs(v)/2 for l,v in zip(lam,direction))
    for power in [8,20]:
     epsilon=F(1,10**power);step=min(delta,epsilon/(2*lip));b=[v+step*d for v,d in zip(beta,direction)]
     q,ee,dd,_,_,nn,ll=exact_objective(Xi,EX,yi,EY,b,lam,tau)
     assert 0<q-P<=epsilon and all((v<=0)==t for v,t in zip(ee,target))
     name=f'{side}_e{power}'
     export(OUT/id/name,b,ee,dd,{'type':'near_optimal_rational_witness','epsilon':record(epsilon),'step':record(step),'direction':[record(d) for d in direction],'beta_numerators':[str(v) for v in nn],'beta_denominator':str(ll),'primal':record(q),'gap':record(q-P),'residual_numerators':[str(v) for v in ee],'residual_denominator':str(dd),'target_rank_pattern':side,'source_sensitivity_sha256':sha(G/'results'/id/'sensitivity.json')})
     tasks.append({'id':id,'variant':name,'epsilon':f'1e-{power}'})
  print('PREPARED',id,flush=True)
 table(OUT/'tasks.csv',tasks);dump(OUT/'preparation.json',{'cases':24,'paths':len(tasks),'seconds':time.perf_counter()-start})
if __name__=='__main__':main()
