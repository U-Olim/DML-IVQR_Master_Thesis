import os,sys
sys.dont_write_bytecode=True
for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS']:os.environ[k]='1'
os.environ['PYTHONDONTWRITEBYTECODE']='1'
from pathlib import Path
from fractions import Fraction as F
import json,csv,hashlib,time
import numpy as np
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[2];RUN=Path(os.environ['STAGE2H_RUN']);OUT=RUN/'results';INPUT=RUN/'inputs'
V1=ROOT/'journal_validation/stage2g/deterministic_implementation'
sys.path.insert(0,str(V1))
from common_v1 import dump,load,sha,read,put,rows,table,val,record,dyadic,exact_W
from outcome_v1 import solve
from outcome_exact_v1 import certify
from instrument_v1 import optimize,certificate,bound_W,rational_stat
def snapshot():
 result={}
 for base,dirs,files in os.walk(ROOT):
  base=Path(base);dirs[:]=[s for s in dirs if base/s!=HERE and not(base==ROOT and s=='.git')]
  for name in files:
   p=base/name;result[p.relative_to(ROOT).as_posix()]=sha(p)
 return result
def tasks():return rows(HERE/'DESIGN.csv')
