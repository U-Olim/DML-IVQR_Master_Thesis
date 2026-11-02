"""Version 2G-D.1; all writes must remain below HERE."""
from pathlib import Path
from fractions import Fraction as F
import json,csv,hashlib,os,sys,time
import numpy as np
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[2];OUT=HERE/'results'
OLD=HERE.parent/'full_path_validation/results'
E=ROOT/'journal_validation/stage2e/output/paired_20261029T093009Z'
G=HERE.parent
sys.path.insert(0,str(ROOT/'journal_validation/stage2f'))
from analyze import exact_objective,dyadic,integer_solve_rational_rhs,record,exact_W
def dump(p,x):
 p.parent.mkdir(parents=True,exist_ok=True)
 def default(z):
  if isinstance(z,np.ndarray):return z.tolist()
  if isinstance(z,np.generic):return z.item()
  raise TypeError(str(type(z)))
 p.write_text(json.dumps(x,indent=2,default=default,allow_nan=False),encoding='utf-8')
def load(p):return json.loads(p.read_text(encoding='utf-8'))
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(1048576),b''):h.update(b)
 return h.hexdigest()
def read(p,shape=None):
 a=np.fromfile(p,dtype='<f8');return a.reshape(shape) if shape else a
def put(p,x):np.asarray(x,dtype='<f8').tofile(p)
def rows(p):
 with p.open(newline='',encoding='utf-8-sig') as f:return list(csv.DictReader(f))
def table(p,r):
 keys=list(dict.fromkeys(k for v in r for k in v))
 with p.open('w',newline='',encoding='utf-8') as f:
  w=csv.DictWriter(f,fieldnames=keys);w.writeheader();w.writerows(r)
def cases():return [r['id'] for r in rows(OLD/'tasks.csv') if r['variant']=='C']
def val(r):return F(int(r['numerator']),int(r['denominator']))
def snapshot():
 d={}
 for base,dirs,files in os.walk(ROOT):
  base=Path(base);dirs[:]=[s for s in dirs if base/s!=HERE and not(base==ROOT and s=='.git')]
  for name in files:
   p=base/name;d[p.relative_to(ROOT).as_posix()]=sha(p)
 return d
