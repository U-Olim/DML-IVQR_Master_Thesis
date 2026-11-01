"""Independent Fraction-based witness audit; does not call any LP or fit solver."""
from fractions import Fraction as F
import json
import sys
from pathlib import Path
import numpy as np


def rational(v):return F.from_float(float(v))


def unpack(r):return F(int(r['numerator']),int(r['denominator']))


def audit_minimax(folder):
    data=np.load(folder/'lp_inputs.npz');C=data['C'];r=data['rhs'];lo=data['lo'];hi=data['hi']
    checked=[]
    for algorithm in ['highs','highs-ds']:
        p=folder/(algorithm+'_diagnostics.json')
        if not p.exists():continue
        c=json.loads(p.read_text())['certificate']
        x=list(map(rational,c['witness_x']));q=list(map(rational,c['witness_q']))
        assert all(rational(l)<=v<=rational(u) for v,l,u in zip(x,lo,hi))
        deviations=[sum((rational(a)*b for a,b in zip(row,x)),F(0))-rational(b) for row,b in zip(C,r)]
        upper=max(map(abs,deviations))
        norm=sum(map(abs,q));lower=F(0)
        if norm:
            weights=[sum((q[i]*rational(C[i,j]) for i in range(len(q))),F(0)) for j in range(C.shape[1])]
            support=sum((max(w*rational(l),w*rational(u)) for w,l,u in zip(weights,lo,hi)),F(0))
            lower=max(F(0),(sum((a*rational(b) for a,b in zip(q,r)),F(0))-support)/norm)
        assert upper==unpack(c['upper']) and lower==unpack(c['lower'])
        assert lower<=upper
        checked.append(algorithm)
    return checked


def ints(a):
    pairs=[float(x).as_integer_ratio() for x in np.asarray(a).flat]
    exp=max(d.bit_length()-1 for _,d in pairs)
    values=[v*(2**exp//d) for v,d in pairs]
    return values,exp


def audit_qr(run):
    folder=run/'pilot_021/P10';c=json.loads((folder/'qr_exact_certificate.json').read_text())
    raw=run/'full_precision/pilot_021'
    X=np.fromfile(raw/'X_row_major.bin',dtype='<f8').reshape(1000,101)
    y=np.fromfile(raw/'y_candidate.bin',dtype='<f8');beta=np.fromfile(raw/'P10_beta.bin',dtype='<f8')
    lam=np.fromfile(raw/'P10_penalty.bin',dtype='<f8')
    vi=list(map(int,c['dual_numerators']));L=int(c['dual_common_denominator'])
    assert all(-L<=10*v<=9*L for v in vi)
    xi,E=ints(X);xi=[xi[i*101:(i+1)*101] for i in range(1000)]
    grad=[sum(xi[i][j]*vi[i] for i in range(1000)) for j in range(101)]
    assert all(g==0 for g in grad[1:])
    assert abs(F(grad[0],2**E*L))<=rational(lam[0])/2
    yi,EY=ints(y);bi,EB=ints(beta)
    dual=F(sum(a*b for a,b in zip(yi,vi)),2**EY*L)
    ER=max(EY,E+EB)
    residuals=[yi[i]*2**(ER-EY)-sum(a*b for a,b in zip(xi[i],bi))*2**(ER-E-EB) for i in range(1000)]
    loss=F(sum(9*e if e>=0 else -e for e in residuals),10*2**ER)
    penalty=sum((rational(l)*abs(rational(b))/2 for l,b in zip(lam,beta)),F(0))
    primal=loss+penalty;gap=primal-dual
    assert primal==unpack(c['primal_objective']) and dual==unpack(c['dual_objective']) and gap==unpack(c['gap'])
    assert gap>=0
    return {'status':'PASS','zero_penalty_equalities_exact':100,'primal':float(primal),'dual':float(dual),'gap':float(gap)}


def main():
    run=Path(sys.argv[1]);folders=sorted(p.parent for p in run.rglob('lp_inputs.npz'))
    results=[]
    for i,folder in enumerate(folders):
        results.append({'folder':str(folder.relative_to(run)),'algorithms':audit_minimax(folder)})
        if (i+1)%25==0:print('Independent rational audit',i+1,'of',len(folders),flush=True)
    qr=audit_qr(run)
    result={'status':'PASS','LP_problems':len(results),'LP_witnesses':sum(len(r['algorithms']) for r in results),
            'method':'Independent Fraction dot products and support bounds; no linprog calls',
            'qr_certificate':qr,'cases':results}
    (run/'independent_rational_audit.json').write_text(json.dumps(result,indent=2))
    print(json.dumps({k:v for k,v in result.items() if k!='cases'},indent=2))


if __name__=='__main__':main()
