"""Create an optional crop desk entry; keep records outside the installed product."""
from pathlib import Path
import argparse,json,os,plistlib,shlex,shutil,stat,subprocess,sys,tempfile,uuid
ROOT=Path(__file__).absolute().parent
TITLE='CanopyOps Crop Desk'
def unlinked(value):
 p=Path(os.path.abspath(Path(value).expanduser()))
 for q in (p,*p.parents):
  try:s=q.lstat()
  except FileNotFoundError:continue
  if stat.S_ISLNK(s.st_mode) or getattr(s,'st_file_attributes',0)&getattr(stat,'FILE_ATTRIBUTE_REPARSE_POINT',0x400):raise ValueError('Choose an unlinked runtime/entry/store path')
 return p
def ps(value):return "'"+str(value).replace("'","''")+"'"
def create_entry(directory,platform,data_root,port=8751,headless=False):
 directory=unlinked(directory);data_root=unlinked(data_root);unlinked(ROOT)
 if not directory.is_dir() or not data_root.is_dir():raise ValueError('Choose existing entry and external record-store directories')
 if data_root==ROOT.parent or ROOT.parent in data_root.parents:raise ValueError('Keep records outside the installed product')
 if type(port) is not int or not 1<=port<=65516:raise ValueError('Choose a first candidate port between1 and65516')
 flags=['-B','-X','utf8',str(ROOT/'desk.py'),'--data-root',str(data_root),'--port',str(port)]
 if headless:flags.append('--no-browser')
 if platform=='windows':
  if os.name!='nt':raise ValueError('Windows shortcut creation requires Windows')
  target=unlinked(directory/(TITLE+'.lnk'))
  if target.exists():raise FileExistsError('Existing crop desk entry retained')
  icon=unlinked(ROOT/'canopyops.ico')
  if not icon.is_file() or not (ROOT/'desk.py').is_file():raise ValueError('Keep the complete installed crop desk together')
  stage=directory/('.canopyops-'+uuid.uuid4().hex+'.lnk');arguments=subprocess.list2cmdline(flags)
  code="$w=New-Object -ComObject WScript.Shell;$s=$w.CreateShortcut("+ps(stage)+");$s.TargetPath="+ps(sys.executable)+";$s.Arguments="+ps(arguments)+";$s.WorkingDirectory="+ps(ROOT)+";$s.IconLocation="+ps(str(icon)+',0')+";$s.Description='CanopyOps Crop Desk';$s.WindowStyle=7;$s.Save()"
  try:
   r=subprocess.run(['powershell.exe','-NoProfile','-NonInteractive','-Command',code],capture_output=True,text=True,creationflags=subprocess.CREATE_NO_WINDOW)
   if r.returncode:raise RuntimeError(r.stderr.strip() or 'Shortcut creation failed')
   with target.open('xb') as f:f.write(stage.read_bytes())
  finally:
   if stage.exists():stage.unlink()
  return {'state':'created','platform':'windows','entry':str(target),'python':sys.executable,'arguments':arguments,'data_root':str(data_root),'starts_automatically':False}
 if platform!='mac':raise ValueError('Use windows or mac')
 target=unlinked(directory/(TITLE+'.app'))
 if target.exists():raise FileExistsError('Existing crop desk entry retained')
 icon=unlinked(ROOT/'canopyops.icns')
 if not icon.is_file():raise ValueError('Keep the complete installed crop desk together')
 runtime=os.path.relpath(ROOT,directory).replace(os.sep,'/');store=os.path.relpath(data_root,directory).replace(os.sep,'/');stage=Path(tempfile.mkdtemp(prefix='.canopyops-',dir=directory))
 try:
  content=stage/'Contents';(content/'MacOS').mkdir(parents=True);(content/'Resources').mkdir()
  info={'CFBundleName':TITLE,'CFBundleDisplayName':TITLE,'CFBundleIdentifier':'com.collaborative-dynamics.canopyops','CFBundlePackageType':'APPL','CFBundleExecutable':TITLE,'CFBundleIconFile':'canopyops.icns','CFBundleShortVersionString':'0.3.1','CFBundleVersion':'0.3.1'}
  (content/'Info.plist').write_bytes(plistlib.dumps(info));shutil.copyfile(icon,content/'Resources/canopyops.icns')
  script='#!/bin/sh\nset -eu\nENTRY_DIR=$(CDPATH= cd -- "$(dirname -- "$0")/../../.." && pwd)\nWORKSPACE="$ENTRY_DIR"/'+shlex.quote(runtime)+'\nSTORE="$ENTRY_DIR"/'+shlex.quote(store)+'\ncd "$WORKSPACE"\nexec /usr/bin/env python3 -B -X utf8 desk.py --data-root "$STORE" --port '+str(port)+(' --no-browser' if headless else '')+'\n'
  executable=content/'MacOS'/TITLE;executable.write_bytes(script.encode());executable.chmod(0o755);target.mkdir();shutil.copytree(stage,target,dirs_exist_ok=True)
 finally:
  if not stage.resolve().is_relative_to(directory.resolve()):raise ValueError('Entry staging escaped selected directory')
  shutil.rmtree(stage)
 return {'state':'created','platform':'mac','entry':str(target),'runtime_relative':runtime,'store_relative':store,'starts_automatically':False,'native_mac_launch':'unobserved unless executed on a Mac'}
def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--directory',type=Path,required=True);p.add_argument('--data-root',type=Path,required=True);p.add_argument('--platform',choices=['windows','mac'],default='windows' if os.name=='nt' else 'mac');p.add_argument('--port',type=int,default=8751);p.add_argument('--headless',action='store_true',help=argparse.SUPPRESS);a=p.parse_args()
 try:print(json.dumps(create_entry(a.directory,a.platform,a.data_root,a.port,a.headless)));return 0
 except (OSError,ValueError,RuntimeError) as e:print(json.dumps({'state':'refused','error':str(e)}));return 2
if __name__=='__main__':raise SystemExit(main())
