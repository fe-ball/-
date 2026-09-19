#!/usr/bin/env python3
import csv, json, subprocess, sys
from pathlib import Path

BASE=Path(__file__).resolve().parents[1]
ROOT=BASE/'01_現行正本'
V=BASE/'02_検証'
errors=[]; warnings=[]

def err(x): errors.append(x)
def warn(x): warnings.append(x)

# All JSON parses.
for f in sorted(ROOT.glob('*.json')):
    try: json.loads(f.read_text(encoding='utf-8'))
    except Exception as e: err(f'JSON parse {f.name}: {e}')

# Authoritative manifest v002 completeness.
m=json.loads((ROOT/'AUTHORITATIVE_MANIFEST_v002.json').read_text(encoding='utf-8'))
for name in m['authoritative_files']:
    if not (ROOT/name).exists() and not (V/name).exists(): err(f'manifest missing: {name}')

# Phase0 source dependencies.
pkt=json.loads((ROOT/'MALAYA_PHASE0_OPENING_PACKET_v003.json').read_text(encoding='utf-8'))
for name in pkt.get('source_files',[]):
    if not (ROOT/name).exists(): err(f'Phase0 source missing: {name}')

# Registry / audit CSV identity and opening states.
reg=json.loads((ROOT/'switch_registry_v010.json').read_text(encoding='utf-8'))
rg={s['id']:s for s in reg['switches']}
if len(rg)!=len(reg['switches']): err('duplicate switch ID in registry')
rows=list(csv.DictReader((ROOT/'MASTER_SWITCH_AUDIT_v010.csv').open(encoding='utf-8-sig')))
rd={r['id']:r for r in rows}
if set(rg)!=set(rd): err(f'switch ID set mismatch registry/csv missing_csv={sorted(set(rg)-set(rd))} extra_csv={sorted(set(rd)-set(rg))}')
for i in set(rg)&set(rd):
    if rg[i]['state_at_start']!=rd[i]['opening_state']: err(f'switch opening-state mismatch {i}')
if len(rg)!=46: err(f'switch count {len(rg)} != 46')

# Run focused validators.
cmds=[
    [sys.executable, str(V/'opening_state_validator_v004.py')],
    [sys.executable, str(ROOT/'state_transition_validator_v001.py'), str(ROOT/'malaya_phase1_events_v001.json')]
]
for c in cmds:
    p=subprocess.run(c,text=True,capture_output=True)
    print(p.stdout,end='')
    if p.stderr: print(p.stderr,end='',file=sys.stderr)
    if p.returncode: err('validator failed: '+' '.join(c))

print(f'PACKAGE_VALIDATION errors={len(errors)} warnings={len(warnings)}')
for x in warnings: print('WARN:',x)
for x in errors: print('ERROR:',x)
if not errors:
    print('OPENING_GATE=PASS')
    print('START=1941-11-15 southern concentration; synchronize global combat at 1941-12-07/08')
    print('STATE_POLICY=bounded/UNKNOWN permitted; no invented point estimates')
raise SystemExit(1 if errors else 0)
