"""Compare previously saved P00/ordinary-QR fits; no outcome optimization."""
import json,sys,subprocess
from pathlib import Path
from fractions import Fraction as F
import numpy as np

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'certification'))
from exact_bounds import dyadic,record
from reassess import primal_parts,dump,CERT,ORIGINAL,ROOT


def main():
 run=Path(sys.argv[1]);folder=run/'ordinary_references';folder.mkdir(exist_ok=False)
 argv=[r'C:\Program Files\R\R-3.4.3\bin\x64\Rscript.exe','--vanilla',str(HERE/'export_references.R'),str(ORIGINAL),str(folder)]
 with (folder/'export.log').open('w') as log:p=subprocess.run(argv,stdout=log,stderr=subprocess.STDOUT,cwd=ROOT)
 dump(folder/'command.json',{'argv':argv,'exit_status':p.returncode});assert p.returncode==0
 results=[]
 for bfile in sorted(folder.glob('*_ordinary_beta.bin')):
  name=bfile.name.removesuffix('_ordinary_beta.bin');raw=CERT/'full_precision'/name
  X=np.fromfile(raw/'X_row_major.bin',dtype='<f8').reshape(1000,101);y=np.fromfile(raw/'y_candidate.bin',dtype='<f8')
  b0=np.fromfile(raw/'P00_beta.bin',dtype='<f8');b1=np.fromfile(bfile,dtype='<f8');lam=np.zeros(101)
  xx,EX=dyadic(X);Xi=xx.tolist()
  e0,E0,l0,p0,_=primal_parts(Xi,EX,y,b0,lam)
  e1,E1,l1,p1,_=primal_parts(Xi,EX,y,b1,lam)
  pred_delta=X@(b1-b0)
  c=json.loads((run/name/'P00/exact_certificate.json').read_text());dual=F(int(c['dual']['numerator']),int(c['dual']['denominator']))
  assert l0+p0>=dual and l1+p1>=dual
  row={'dataset':name,'P00_objective':record(l0+p0),'saved_reference_objective':record(l1+p1),
       'objective_difference_reference_minus_P00':record(l1+p1-l0-p0),
       'P00_gap_upper':record(l0+p0-dual),'reference_gap_upper':record(l1+p1-dual),
       'prediction_RMS_difference_float_diagnostic':float(np.sqrt(np.mean(pred_delta**2))),
       'prediction_max_difference_float_diagnostic':float(max(abs(pred_delta))),
       'coefficient_l2_difference_float_diagnostic':float(np.linalg.norm(b1-b0)),
       'exact_rank_sign_differences':sum((a<=0)!=(b<=0) for a,b in zip(e0,e1))}
  results.append(row)
 dump(run/'saved_reference_comparison.json',{'status':'COMPLETE','no_refits':True,'comparisons':results})
 print('Saved-reference comparisons',len(results),'max fitted discrepancy',max(r['prediction_max_difference_float_diagnostic'] for r in results))


if __name__=='__main__':main()
