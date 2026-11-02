from pathlib import Path
from fractions import Fraction as F
import hashlib,json,csv,os,sys
import numpy as np
HERE=Path(__file__).resolve().parent; ROOT=HERE.parents[2]
G=HERE.parent; E=ROOT/'journal_validation/stage2e/output/paired_20261029T093009Z'
OUT=HERE/'results'
sys.path.insert(0,str(ROOT/'journal_validation/stage2f'))
from analyze import dyadic,integer_solve_rational_rhs,exact_objective,exact_W,record

def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for block in iter(lambda:f.read(1024*1024),b''):h.update(block)
 return h.hexdigest()
def dump(p,obj):
 def convert(v):
  if isinstance(v,np.ndarray):return v.tolist()
  if isinstance(v,np.generic):return v.item()
  raise TypeError(type(v))
 p.write_text(json.dumps(obj,indent=2,default=convert),encoding='utf-8')
def val(r):return F(int(r['numerator']),int(r['denominator']))
def table(p,rows):
 keys=list(dict.fromkeys(k for r in rows for k in r))
 with p.open('w',newline='',encoding='utf-8') as f:
  w=csv.DictWriter(f,fieldnames=keys);w.writeheader();w.writerows(rows)
def readbin(p,shape=None):
 a=np.fromfile(p,dtype='<f8');return a.reshape(shape) if shape else a
def snapshot():
 result={}
 for directory,dirs,files in os.walk(ROOT):
  base=Path(directory);dirs[:]=[d for d in dirs if base/d!=HERE and not(base==ROOT and d=='.git')]
  for name in files:
   p=base/name;result[p.relative_to(ROOT).as_posix()]=sha(p)
 return result
