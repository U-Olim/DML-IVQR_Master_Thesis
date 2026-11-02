"""Capture R return codes directly, avoiding PowerShell stderr-redirection status."""
from common import *
import subprocess,time
def main():
 mode=sys.argv[1];assert mode in ['native','verify']
 script=HERE/('native_paths.R' if mode=='native' else 'verify_native.R')
 command=[r'C:\Program Files\R\R-3.4.3\bin\x64\Rscript.exe','--vanilla',str(script)]
 start=time.perf_counter()
 with (OUT/(mode+'_direct.log')).open('w',encoding='utf-8') as log:
  result=subprocess.run(command,cwd=ROOT,stdout=log,stderr=subprocess.STDOUT,text=True)
 dump(OUT/(mode+'_process.json'),{'command':command,'returncode':result.returncode,'seconds':time.perf_counter()-start})
 print(mode,'returncode',result.returncode,flush=True)
 assert result.returncode==0
if __name__=='__main__':main()
