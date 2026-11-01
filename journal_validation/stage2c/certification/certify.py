"""Saved-input certification only. No outcome estimation or Monte Carlo generation."""
import csv
import hashlib
import json
import os
import subprocess
import sys
from datetime import datetime,timezone
from pathlib import Path

import numpy as np
import scipy
from scipy.optimize import linprog

from exact_bounds import certificate,qr_exact_certificate,record

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
SOURCE=HERE.parent/'output/controlled_20261029_01'


def sha(p):
    h=hashlib.sha256()
    with p.open('rb') as f:
        for block in iter(lambda:f.read(1024*1024),b''):h.update(block)
    return h.hexdigest()


def snapshot():
    result={}
    for directory,subdirs,files in os.walk(ROOT):
        base=Path(directory)
        subdirs[:]=[d for d in subdirs if base/d!=HERE and not(base==ROOT and d=='.git')]
        for name in files:
            p=base/name;result[p.relative_to(ROOT).as_posix()]=sha(p)
    return result


def read(p):
    with p.open(newline='',encoding='utf-8-sig') as f:return list(csv.DictReader(f))


def dump(p,x):
    def convert(v):
        if isinstance(v,np.ndarray):return v.tolist()
        if isinstance(v,np.generic):return v.item()
        raise TypeError(str(type(v)))
    p.write_text(json.dumps(x,indent=2,default=convert),encoding='utf-8')


def problem(X,e,beta,lam,tie=1e-7):
    n=len(e);p=X.shape[1];score=.9-(e<=0).astype(float)
    ties=np.abs(e)<=tie;inactive=(np.abs(beta)<=1e-7)&(lam>0)
    fixed=X[~ties].T@score[~ties];target=.5*lam*np.sign(beta);target[inactive]=0
    C=np.concatenate([X[ties].T,-np.eye(p)[:,inactive]],axis=1)/n
    rhs=(target-fixed)/n
    lo=np.concatenate([np.full(int(ties.sum()),-.1),-lam[inactive]/2])
    hi=np.concatenate([np.full(int(ties.sum()),.9),lam[inactive]/2])
    A=np.vstack([np.column_stack([C,-np.ones(p)]),np.column_stack([-C,-np.ones(p)])])
    b=np.concatenate([rhs,-rhs]);c=np.zeros(C.shape[1]+1);c[-1]=1
    return dict(C=C,rhs=rhs,lo=lo,hi=hi,A=A,b=b,c=c,ties=ties,inactive=inactive,fixed=fixed,target=target,score=score)


def solve(folder,P,method,options):
    result=linprog(P['c'],A_ub=P['A'],b_ub=P['b'],
        bounds=list(zip(P['lo'],P['hi']))+[(0,None)],method=method,options=options)
    raw=dict(result);raw['method']=method;raw['options']=options
    dump(folder/(method+'_solver.json'),raw)
    if not result.success:return {'classification':'Not assessable with saved evidence','solver_message':result.message}
    m=len(P['rhs']);q=result.ineqlin.marginals[:m]-result.ineqlin.marginals[m:]
    cert=certificate(P['C'],P['rhs'],P['lo'],P['hi'],result.x[:-1],q)
    discrepancy=P['C']@result.x[:-1]-P['rhs']
    epigraph=float(result.x[-1]);actual=float(np.max(np.abs(discrepancy)))
    raw_violation=float(max(0,np.max(P['A']@result.x-P['b'])))
    xclamp=np.array(cert['witness_x']);gradient=P['fixed'].copy()
    nt=int(P['ties'].sum());gradient+=1000*P['C'][:,:nt]@xclamp[:nt]
    h=P['target'].copy();h[P['inactive']]=xclamp[nt:]
    diagnostics={'returned_epigraph':epigraph,'float_attained_maximum':actual,
        'epigraph_minus_attained':epigraph-actual,'raw_max_inequality_violation':raw_violation,
        'normalized_stationarity_float':discrepancy.tolist(),
        'clamped_penalty_subgradients':h.tolist(),'clamped_Xt_score':gradient.tolist(),
        'tie_subgradients':xclamp[:nt].tolist(),'tie_observation_indices_zero_based':np.flatnonzero(P['ties']).tolist(),
        'interval_penalty_coordinates':np.flatnonzero(P['inactive']).tolist(),
        'near_active_inequality_indices_diagnostic_1e10':np.flatnonzero(np.abs(P['A']@result.x-P['b'])<=1e-10).tolist(),
        'certificate':cert}
    dump(folder/(method+'_diagnostics.json'),diagnostics)
    return dict(classification=cert['classification'],lower=cert['lower']['outward_lower'],
                upper=cert['upper']['outward_upper'],width=cert['width']['outward_upper'],
                epigraph=epigraph,attained=actual,raw_violation=raw_violation,
                max_coordinates=cert['max_coordinates_zero_based'])


def certify_problem(folder,X,e,beta,lam,tie=1e-7):
    folder.mkdir(parents=True,exist_ok=False);P=problem(X,e,beta,lam,tie)
    np.savez(folder/'lp_inputs.npz',X=X,residual=e,beta=beta,penalty=lam,**P)
    dump(folder/'definition.json',{'tie_tolerance':tie,'coefficient_zero_tolerance':1e-7,
        'historical_gate':1e-7,'n':len(e),'variables':P['C'].shape[1]+1,
        'tie_count':int(P['ties'].sum()),'inactive_penalty_coordinates':np.flatnonzero(P['inactive']).tolist()})
    original=solve(folder,P,'highs',{'primal_feasibility_tolerance':1e-9,'dual_feasibility_tolerance':1e-9})
    refined=solve(folder,P,'highs-ds',{'primal_feasibility_tolerance':1e-10,'dual_feasibility_tolerance':1e-10})
    candidates=[v for v in (original,refined) if 'lower' in v]
    if not candidates:return {'classification':'Not assessable with saved evidence'}
    lower=max(v['lower'] for v in candidates);upper=min(v['upper'] for v in candidates)
    # Outward-rounded bounds are conservative; individual rational decisions remain saved.
    classification='Certified pass' if upper<=1e-7 else 'Certified failure' if lower>1e-7 else 'Numerically indeterminate'
    return {'classification':classification,'lower':lower,'upper':upper,'original':original,'refined':refined,
            'tie_count':int(P['ties'].sum())}


def qr_dual(folder,X,y,beta,lam,exact=False):
    zero=lam==0;other=~zero
    Aeq=X[:,zero].T;beq=np.zeros(int(zero.sum()))
    Aub=np.vstack([X[:,other].T,-X[:,other].T]);bub=np.concatenate([lam[other]/2,lam[other]/2])
    result=linprog(-y,A_ub=Aub if len(bub) else None,b_ub=bub if len(bub) else None,
                  A_eq=Aeq,b_eq=beq,bounds=[(-.1,.9)]*len(y),method='highs-ds',
                  options={'primal_feasibility_tolerance':1e-10,'dual_feasibility_tolerance':1e-10})
    dump(folder/'qr_dual_solver.json',dict(result))
    if not result.success:return {'status':'NUMERICAL_DUAL_SOLVE_FAILED'}
    v=result.x;e=y-X@beta;g=X.T@v
    primal=float(np.sum(e*(.9-(e<0)))+.5*np.sum(lam*np.abs(beta)))
    comp=e*(.9-(e<0))-v*e
    out={'status':'APPROXIMATE_DUAL_ONLY','primal_float':primal,'dual_float':float(y@v),
         'gap_float_not_certified':float(primal-y@v),
         'box_violation':float(max(0,np.max(-.1-v),np.max(v-.9))),
         'zero_penalty_equality_max':float(np.max(abs(g[zero]))) if zero.any() else 0.0,
         'penalty_constraint_violation':float(max(0,np.max(abs(g[other])-lam[other]/2))) if other.any() else 0,
         'loss_complementarity_sum_float':float(comp.sum()),
         'penalty_complementarity_sum_float':float((lam*abs(beta)/2-beta*g).sum()),
         'zero_dual_is_exactly_feasible':True,
         'note':'Approximate equality residuals are not exact feasibility; no floating gap is a certified bound.'}
    if exact:
        try:
            print('Exact rational QR dual basis reconstruction',flush=True)
            cert=qr_exact_certificate(X,y,beta,lam,v);dump(folder/'qr_exact_certificate.json',cert)
            out['exact_certificate_status']=cert['status'];out['exact_gap']=cert['gap']['outward_upper']
        except Exception as ex:
            out['exact_certificate_status']='UNAVAILABLE';out['exact_certificate_reason']=repr(ex)
    dump(folder/'qr_dual_diagnostics.json',out)
    return out


def main():
    assert ROOT.name=='DML-IVQR_Master_Thesis',ROOT
    assert subprocess.check_output(['git','branch','--show-current'],cwd=ROOT,text=True).strip()=='journal-validation'
    backup=json.loads((SOURCE/'backup_verified.json').read_text());assert Path(backup['archive']).is_file()
    assert sha(Path(backup['archive']))==backup['sha256']
    run=HERE/('saved_inputs_'+datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ'))
    run.mkdir(exist_ok=False)
    dump(run/'initial_state.json',{'git_status':subprocess.check_output(['git','status','--short','--branch'],cwd=ROOT,text=True),
         'source':str(SOURCE),'backup_sha256_verified':backup['sha256'],
         'python':sys.version,'numpy':np.__version__,'scipy':scipy.__version__})
    print('RUN_DIRECTORY',run,flush=True)
    print('Hashing protected files (everything except certification and Git metadata)',flush=True)
    before=snapshot();dump(run/'protected_before.json',before)
    status='FAILED';summary=[];sensitivity=[]
    try:
        export=run/'full_precision';export.mkdir()
        argv=[r'C:\Program Files\R\R-3.4.3\bin\x64\Rscript.exe','--vanilla',str(HERE/'export_saved.R'),str(SOURCE),str(export)]
        with (run/'export.log').open('w') as log:proc=subprocess.run(argv,cwd=ROOT,stdout=log,stderr=subprocess.STDOUT)
        dump(run/'export_command.json',{'argv':argv,'exit_status':proc.returncode})
        assert proc.returncode==0,'Saved-RDS export failed'
        folders=sorted(p for p in SOURCE.iterdir() if p.is_dir() and p.name.startswith(('pilot_','validation_')))
        assert len(folders)==23
        # Failure first, then all other stored cases, without fitting.
        folders.sort(key=lambda p:(p.name!='pilot_021',p.name))
        for src in folders:
            print('CERTIFY',src.name,flush=True)
            Xcsv=np.loadtxt(src/'design.csv',delimiter=',',skiprows=1)
            observations=read(src/'observations.csv');coefficients=read(src/'coefficients.csv')
            binfolder=export/src.name
            Xfull=np.fromfile(binfolder/'X_row_major.bin',dtype='<f8').reshape(1000,101)
            yfull=np.fromfile(binfolder/'y_candidate.bin',dtype='<f8')
            case=run/src.name;case.mkdir()
            previous=json.loads((src/'verification.json').read_text()) if (src/'verification.json').exists() else None
            for arm in ['P11','P01','P10','P00']:
                co=[r for r in coefficients if r['arm']==arm];ob=[r for r in observations if r['arm']==arm]
                bc=np.array([float(r['coefficient']) for r in co]);lc=np.array([float(r['penalty']) for r in co]);ec=np.array([float(r['residual']) for r in ob])
                bf=np.fromfile(binfolder/(arm+'_beta.bin'),dtype='<f8');lf=np.fromfile(binfolder/(arm+'_penalty.bin'),dtype='<f8');ef=np.fromfile(binfolder/(arm+'_residual.bin'),dtype='<f8')
                armfolder=case/arm;armfolder.mkdir()
                historical=certify_problem(armfolder/'historical_csv_lp',Xcsv,ec,bc,lc)
                full=certify_problem(armfolder/'full_precision_lp',Xfull,ef,bf,lf)
                row={'dataset':src.name,'arm':arm,'historical_record':'PASS' if previous else ('FAILED_GATE' if arm=='P10' else 'NO_COMPLETE_RECORD'),
                     'historical_recorded_kkt':previous['arms'][arm]['kkt_stationarity_over_n'] if previous else (1.0044854692833311e-7 if arm=='P10' else None),
                     'historical_csv':historical,'full_precision':full,
                     'csv_full_X_max_difference':float(np.max(abs(Xcsv-Xfull))),
                     'csv_full_residual_max_difference':float(np.max(abs(ec-ef))),
                     'tie_classification_changes':int(np.sum((abs(ec)<=1e-7)!=(abs(ef)<=1e-7)))}
                if src.name=='pilot_021':
                    row['qr_dual']=qr_dual(armfolder,Xfull,yfull,bf,lf,exact=arm=='P10')
                    if arm=='P10':
                        for tie in [0,1e-8,5e-8,1e-7,2e-7,5e-7,1e-6]:
                            sf=armfolder/('sensitivity_'+str(tie).replace('.','p'))
                            result=certify_problem(sf,Xfull,ef,bf,lf,tie)
                            sensitivity.append(dict(tie_tolerance=tie,diagnostic_only=True,**result))
                        dump(armfolder/'tie_sensitivity.json',sensitivity)
                        abs_res=sorted((float(abs(v)),i+1,float(v)) for i,v in enumerate(ef))
                        dump(armfolder/'residuals_near_boundary.json',{'residuals_sorted_by_magnitude':abs_res,
                            'exact_zero':int(sum(ef==0)),'coefficient_zero_threshold':1e-7,
                            'intercept':float(bf[0]),'minimum_absolute_slope':float(min(abs(bf[1:])))})
                dump(armfolder/'summary.json',row);summary.append(row)
                dump(run/'all_case_summary.json',summary)
                print(src.name,arm,historical['classification'],historical.get('lower'),historical.get('upper'),flush=True)
        status='COMPLETE'
    finally:
        after=snapshot();dump(run/'protected_after.json',after)
        preservation={'status':status,'files_checked':len(before),
            'changed':[p for p in before if p in after and before[p]!=after[p]],
            'missing':sorted(before.keys()-after.keys()),'added_outside_certification':sorted(after.keys()-before.keys())}
        dump(run/'preservation.json',preservation)
        assert not any(preservation[k] for k in ['changed','missing','added_outside_certification']),preservation
        dump(run/'run_status.json',{'status':status,'cases':len(summary),'run_directory':str(run)})
        print('PRESERVATION',preservation,flush=True)


if __name__=='__main__':main()
