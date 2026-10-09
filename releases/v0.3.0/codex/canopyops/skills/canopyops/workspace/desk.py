#!/usr/bin/env python3
"""Native local record desk. Python standard library only."""
import argparse, base64, binascii, csv, hashlib, io, json, math, mimetypes, os, re, secrets, subprocess, sys, tempfile, threading, time, urllib.parse, urllib.request, webbrowser, zipfile
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

PRODUCT = 'canopyops'
TITLE = 'CanopyOps'
ENV = 'CANOPYOPS_DATA_HOME'
PORT = 8751
HERE = Path(__file__).resolve().parent
ASSETS = HERE.parent / 'assets'
ROOT = Path(os.environ.get(ENV, str(Path.home() / 'Documents' / TITLE))).expanduser().resolve()
TOKEN = secrets.token_urlsafe(24)
BUILD = hashlib.sha256(b''.join(p.name.encode()+p.read_bytes() for p in sorted(HERE.iterdir()) if p.is_file())).hexdigest()
LOCK = threading.Lock()
KINDS = {'rooms': 'room-runbook.md', 'batches': 'crop-plan.md', 'incidents': 'incident-report.md', 'handoffs': 'shift-handoff.md'}
HEADERS = 'timestamp,facility,room,zone,crop_id,stage,observer,observation_type,plant_or_sample,observed_condition,severity,distribution,measurement_value,unit,method,sensor_or_tool,photo_or_record,action_taken,incident_id,notes'.split(',')

def digest(data): return hashlib.sha256(data).hexdigest()
def safe(name):
    if not isinstance(name, str) or not re.fullmatch(r'[A-Za-z0-9_. /-]{1,180}', name): raise ValueError('Use a simple record filename')
    p = (ROOT / name).resolve()
    if ROOT not in p.parents or any(x.startswith('.') for x in Path(name).parts): raise ValueError('Record path outside store')
    return p
def atomic(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, name = tempfile.mkstemp(dir=path.parent, prefix='.write-')
    try:
        with os.fdopen(fd, 'wb') as f: f.write(data); f.flush(); os.fsync(f.fileno())
        os.replace(name, path)
    finally:
        if os.path.exists(name): os.unlink(name)
def health(port):
    try:
        with urllib.request.urlopen(f'http://127.0.0.1:{port}/health', timeout=.3) as r: return json.load(r)
    except Exception: return None

class Handler(BaseHTTPRequestHandler):
    def log_message(self, *args): pass
    def answer(self, value, status=200, kind='application/json'):
        data = json.dumps(value).encode() if kind == 'application/json' else value
        self.send_response(status); self.send_header('Content-Type', kind); self.send_header('Content-Length', str(len(data)))
        self.send_header('Cache-Control', 'no-store'); self.send_header('X-Content-Type-Options', 'nosniff'); self.end_headers(); self.wfile.write(data)
    def do_GET(self):
        try:
            expected=f'http://127.0.0.1:{self.server.server_port}'
            if self.headers.get('Host') != f'127.0.0.1:{self.server.server_port}' or self.headers.get('Origin',expected) != expected: return self.answer({'error':'Use the workspace loopback address'},403)
            u = urllib.parse.urlsplit(self.path); q = urllib.parse.parse_qs(u.query)
            if u.path == '/health': return self.answer({'product': PRODUCT, 'root': str(ROOT), 'ui': str(HERE), 'build': BUILD, 'port': self.server.server_port})
            if u.path == '/api/state':
                files = []
                if ROOT.exists():
                    for p in sorted(ROOT.rglob('*')):
                        if p.is_file() and p.suffix.lower() in ('.md', '.csv', '.json', '.txt') and not any(x.startswith('.') for x in p.relative_to(ROOT).parts): files.append({'name': p.relative_to(ROOT).as_posix(), 'bytes': p.stat().st_size})
                return self.answer({'files': files, 'root': str(ROOT), 'token': TOKEN, 'templates': {k: (ASSETS/v).read_text(encoding='utf-8') for k,v in KINDS.items()}, 'headers': HEADERS})
            if u.path == '/api/file':
                p = safe(q.get('name', [''])[0]); data = p.read_bytes()
                if len(data)>8000000: raise ValueError('Record is too large for the editor')
                return self.answer({'name': p.relative_to(ROOT).as_posix(), 'text': data.decode('utf-8-sig'), 'etag': digest(data)})
            if u.path == '/api/export':
                p=safe(q.get('name',[''])[0]); self.send_response(200); self.send_header('Content-Type','application/octet-stream'); self.send_header('Content-Disposition',f'attachment; filename="{p.name}"'); self.end_headers(); return self.wfile.write(p.read_bytes())
            if u.path.startswith('/photos/'):
                p=safe(u.path.lstrip('/')); return self.answer(p.read_bytes(),kind=mimetypes.guess_type(p.name)[0] or 'application/octet-stream')
            name = 'index.html' if u.path == '/' else u.path.lstrip('/')
            if name not in ('index.html','app.js','model.js','style.css','skins.css','canopy-atmosphere.png'): return self.answer({'error':'Not found'},404)
            p=HERE/name; return self.answer(p.read_bytes(),kind=mimetypes.guess_type(p.name)[0] or 'text/plain')
        except (ValueError, UnicodeError) as e: self.answer({'error':str(e)},400)
        except FileNotFoundError: self.answer({'error':'Record not found'},404)
    def do_POST(self):
        try:
            origin=self.headers.get('Origin'); expected=f'http://127.0.0.1:{self.server.server_port}'
            if self.headers.get('Host') != f'127.0.0.1:{self.server.server_port}' or self.headers.get('X-Desk-Token') != TOKEN or origin != expected: return self.answer({'error':'Reopen the workspace to refresh authorization'},403)
            size=int(self.headers.get('Content-Length','0'))
            if not 0<size<=12000000: raise ValueError('Request size limit is 12 MB')
            obj=json.loads(self.rfile.read(size))
            with LOCK:
                if self.path == '/api/save':
                    p=safe(obj['name'])
                    if p.suffix.lower() not in ('.md','.csv','.json','.txt'): raise ValueError('Choose a native text record extension')
                    old=p.read_bytes() if p.exists() else None
                    if obj.get('etag') != (digest(old) if old is not None else None): return self.answer({'error':'Record changed since you opened it. Export your draft, then reopen.'},409)
                    text=obj['text']
                    if not isinstance(text,str) or len(text.encode())>8000000: raise ValueError('Invalid text record')
                    if p.suffix.lower()=='.json': json.loads(text)
                    if p.suffix.lower()=='.csv': list(csv.reader(io.StringIO(text),strict=True))
                    if old is not None: atomic(ROOT/'history'/f'{time.time_ns()}-{p.name}',old)
                    if obj.get('import'): atomic(ROOT/'imports'/f'{time.time_ns()}-{p.name}', base64.b64decode(obj['original'],validate=True))
                    atomic(p,text.encode()); return self.answer({'etag':digest(text.encode()),'name':obj['name']})
                if self.path == '/api/walk':
                    row=obj.get('row',{}); p=safe('crop-walk.csv'); old=p.read_bytes() if p.exists() else None
                    if obj.get('etag') != (digest(old) if old is not None else None): return self.answer({'error':'Crop walk changed. Reload before adding this observation.'},409)
                    if not isinstance(row,dict) or not all(isinstance(row.get(k),str) and row[k].strip() for k in ('room','observer','observed_condition')): raise ValueError('Room, observer and observation are required')
                    if str(row.get('measurement_value','')).strip():
                        if not math.isfinite(float(row['measurement_value'])): raise ValueError('Measurement must be a finite number')
                        if not all(isinstance(row.get(k),str) and row[k].strip() for k in ('unit','method','sensor_or_tool')): raise ValueError('Measurements require unit, method and sensor/tool')
                    current=list(csv.DictReader(io.StringIO(old.decode('utf-8-sig')),strict=True)) if old else []
                    if old and (csv.DictReader(io.StringIO(old.decode('utf-8-sig'))).fieldnames or [])!=HEADERS: raise ValueError('CSV columns differ from crop-walk template. Use the native editor to preserve your format.')
                    photo=obj.get('photo'); photo_name=None; photo_data=None
                    if photo is not None:
                        if not isinstance(photo,dict): raise ValueError('Invalid photo')
                        ext=Path(photo.get('filename','')).suffix.lower()
                        if ext not in ('.png','.jpg','.jpeg','.webp'): raise ValueError('Use PNG, JPEG or WebP photos')
                        photo_data=base64.b64decode(photo['data'],validate=True)
                        if len(photo_data)>8000000: raise ValueError('Photo limit is 8 MB')
                        signatures={'.png':photo_data.startswith(b'\x89PNG\r\n\x1a\n'),'.jpg':photo_data.startswith(b'\xff\xd8\xff'),'.jpeg':photo_data.startswith(b'\xff\xd8\xff'),'.webp':photo_data.startswith(b'RIFF') and photo_data[8:12]==b'WEBP'}
                        if not signatures[ext]: raise ValueError('Image signature does not match its file type')
                        photo_name=f'photos/{time.time_ns()}-{secrets.token_hex(4)}{ext}'
                        row={**row,'photo_or_record':photo_name}
                    out=io.StringIO(newline=''); writer=csv.DictWriter(out,fieldnames=HEADERS); writer.writeheader(); writer.writerows(current); writer.writerow({k:str(row.get(k,'')) for k in HEADERS})
                    written=False
                    try:
                        if photo_name:
                            atomic(safe(photo_name),photo_data); written=True
                        if old: atomic(ROOT/'history'/f'{time.time_ns()}-crop-walk.csv',old)
                        atomic(p,out.getvalue().encode())
                    except OSError:
                        if written: safe(photo_name).unlink(missing_ok=True)
                        raise
                    return self.answer({'etag':digest(out.getvalue().encode()),'photo_or_record':photo_name})
                raise ValueError('Unknown action')
        except (ValueError, KeyError, UnicodeError, TypeError, binascii.Error, csv.Error) as e: self.answer({'error':str(e)},400)
        except OSError as e: self.answer({'error':str(e)},500)

def main():
    parser=argparse.ArgumentParser(); parser.add_argument('--serve',action='store_true'); parser.add_argument('--port',type=int,default=PORT); parser.add_argument('--no-browser',action='store_true'); parser.add_argument('--data-root'); args=parser.parse_args()
    global ROOT
    if args.data_root: ROOT=Path(args.data_root).expanduser().resolve()
    if ROOT==HERE.parent or HERE.parent in ROOT.parents: raise SystemExit('Choose a data root outside the product installation; runtime records must remain portable.')
    if args.serve:
        server=ThreadingHTTPServer(('127.0.0.1',args.port),Handler); server.serve_forever(); return
    for port in range(args.port,args.port+20):
        found=health(port)
        if found and found.get('product')==PRODUCT and found.get('root')==str(ROOT) and found.get('ui')==str(HERE) and found.get('build')==BUILD:
            if not args.no_browser: webbrowser.open(f'http://127.0.0.1:{port}')
            print(f'http://127.0.0.1:{port}'); return
        if found: continue
        command=[sys.executable,str(Path(__file__).resolve()),'--serve','--port',str(port),'--data-root',str(ROOT)]
        kwargs={'stdout':subprocess.DEVNULL,'stderr':subprocess.DEVNULL,'stdin':subprocess.DEVNULL}
        if os.name=='nt': kwargs['creationflags']=subprocess.CREATE_NO_WINDOW | subprocess.DETACHED_PROCESS
        else: kwargs['start_new_session']=True
        child=subprocess.Popen(command,**kwargs)
        for _ in range(40):
            time.sleep(.1); found=health(port)
            if found and found.get('product')==PRODUCT and found.get('root')==str(ROOT) and found.get('ui')==str(HERE) and found.get('build')==BUILD:
                if not args.no_browser: webbrowser.open(f'http://127.0.0.1:{port}')
                print(f'http://127.0.0.1:{port}'); return
            if child.poll() is not None: break
    raise SystemExit('No available local port. Close an old desk or choose --port NUMBER.')
if __name__=='__main__': main()
