"""Windows working-set measurement without third-party dependencies.

OS process high-water marks and 50 ms sampled sum of live descendant RSS
are different measures; neither is described as an exact continuous tree peak.
"""
import ctypes as C,ctypes.wintypes as W,threading,os,time
K=C.WinDLL('kernel32',use_last_error=True);P=C.WinDLL('psapi',use_last_error=True)
SIZE=C.c_size_t
class PMC(C.Structure):
 _fields_=[('cb',W.DWORD),('PageFaultCount',W.DWORD)]+[(n,SIZE) for n in ['PeakWorkingSetSize','WorkingSetSize','QuotaPeakPagedPoolUsage','QuotaPagedPoolUsage','QuotaPeakNonPagedPoolUsage','QuotaNonPagedPoolUsage','PagefileUsage','PeakPagefileUsage','PrivateUsage']]
class PE(C.Structure):
 _fields_=[('dwSize',W.DWORD),('cntUsage',W.DWORD),('th32ProcessID',W.DWORD),('th32DefaultHeapID',SIZE),('th32ModuleID',W.DWORD),('cntThreads',W.DWORD),('th32ParentProcessID',W.DWORD),('pcPriClassBase',W.LONG),('dwFlags',W.DWORD),('szExeFile',W.WCHAR*260)]
K.OpenProcess.argtypes=[W.DWORD,W.BOOL,W.DWORD];K.OpenProcess.restype=W.HANDLE
K.CloseHandle.argtypes=[W.HANDLE];K.CloseHandle.restype=W.BOOL
K.CreateToolhelp32Snapshot.argtypes=[W.DWORD,W.DWORD];K.CreateToolhelp32Snapshot.restype=W.HANDLE
K.Process32FirstW.argtypes=[W.HANDLE,C.POINTER(PE)];K.Process32FirstW.restype=W.BOOL
K.Process32NextW.argtypes=[W.HANDLE,C.POINTER(PE)];K.Process32NextW.restype=W.BOOL
P.GetProcessMemoryInfo.argtypes=[W.HANDLE,C.POINTER(PMC),W.DWORD];P.GetProcessMemoryInfo.restype=W.BOOL
def memory(pid):
 h=K.OpenProcess(0x410,False,pid)
 if not h:return None
 try:
  info=PMC();info.cb=C.sizeof(info)
  if not P.GetProcessMemoryInfo(h,C.byref(info),info.cb):return None
  return {'rss':int(info.WorkingSetSize),'OS_peak_working_set':int(info.PeakWorkingSetSize),'private_commit':int(info.PrivateUsage)}
 finally:K.CloseHandle(h)
def descendants(root):
 h=K.CreateToolhelp32Snapshot(2,0)
 if h in (None,C.c_void_p(-1).value):return [root]
 parents={};e=PE();e.dwSize=C.sizeof(e)
 try:
  ok=K.Process32FirstW(h,C.byref(e))
  while ok:
   parents[int(e.th32ProcessID)]=int(e.th32ParentProcessID);ok=K.Process32NextW(h,C.byref(e))
 finally:K.CloseHandle(h)
 result={root};changed=True
 while changed:
  add={pid for pid,parent in parents.items() if parent in result};changed=not add<=result;result|=add
 return result
class Monitor:
 def __init__(self,root=None):self.root=root or os.getpid();self.stop_event=threading.Event();self.peak=0;self.samples=0;self.process_peaks={};self.thread=None
 def sample(self):
  values=[]
  for pid in descendants(self.root):
   m=memory(pid)
   if m:
    values.append(m['rss']);self.process_peaks[str(pid)]=max(self.process_peaks.get(str(pid),0),m['OS_peak_working_set'])
  self.peak=max(self.peak,sum(values));self.samples+=1
 def start(self):
  def loop():
   self.sample()
   while not self.stop_event.wait(.05):self.sample()
  self.thread=threading.Thread(target=loop,daemon=True);self.thread.start();return self
 def finish(self):
  self.stop_event.set();self.thread.join();self.sample()
  return {'sampled_tree_peak_RSS_bytes':self.peak,'sampling_seconds':.05,'samples':self.samples,
   'observed_OS_peak_working_set_by_PID':self.process_peaks,
   'scope':'sum of sampled live-process RSS, shared pages counted per process; OS process peaks are separate high-water measures'}
