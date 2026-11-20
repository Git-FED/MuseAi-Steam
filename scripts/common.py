from pathlib import Path
import csv, datetime as dt, json, re
ROOT = Path(__file__).resolve().parents[1]

def today(): return dt.date.today().isoformat()
def read_log():
    p = ROOT / 'data/library/playtime-log.csv'
    with p.open(newline='', encoding='utf-8') as f: return list(csv.DictReader(f))
def parse_simple_yaml(path):
    # Small dependency-free reader for the scalar/list structures in this package.
    out = {}; current = None
    for raw in Path(path).read_text(encoding='utf-8').splitlines():
        line = raw.split('#',1)[0].rstrip()
        if not line.strip(): continue
        if line.startswith('  ') and ':' in line and current == 'per_game':
            k,v = line.strip().split(':',1); nums = dict(re.findall(r'(daily|weekly):\s*([0-9.]+)', v)); out[current][k] = {a:float(b) for a,b in nums.items()}; continue
        if ':' not in line: continue
        k,v = line.split(':',1); k=k.strip(); v=v.strip()
        if v == '': out[k] = {}
        elif v.startswith('['): out[k] = [float(x.strip()) if x.strip().replace('.','',1).isdigit() else x.strip() for x in v[1:-1].split(',') if x.strip()]
        elif v.startswith('{'): out.setdefault(current or k, {})
        elif v in ('true','false'): out[k] = v == 'true'
        elif v == 'null': out[k] = None
        elif v.startswith('"'): out[k] = v.strip('"')
        else:
            try: out[k] = float(v) if '.' in v else int(v)
            except ValueError: out[k] = v
        current = k if v == '' else current
    return out
