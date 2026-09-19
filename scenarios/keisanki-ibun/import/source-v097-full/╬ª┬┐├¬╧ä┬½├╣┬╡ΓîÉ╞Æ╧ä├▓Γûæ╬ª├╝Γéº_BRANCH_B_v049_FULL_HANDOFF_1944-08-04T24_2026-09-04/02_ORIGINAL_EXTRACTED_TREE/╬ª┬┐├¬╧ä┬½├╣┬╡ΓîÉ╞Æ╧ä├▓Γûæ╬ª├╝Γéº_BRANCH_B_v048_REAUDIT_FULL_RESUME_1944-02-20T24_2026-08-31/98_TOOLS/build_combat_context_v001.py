#!/usr/bin/env python3
import argparse,json,pathlib,subprocess,sys,tempfile
ROOT=pathlib.Path(__file__).resolve().parents[1]
ap=argparse.ArgumentParser(); ap.add_argument('profile'); ap.add_argument('--date'); ap.add_argument('--checkpoint'); ap.add_argument('--combat-input'); ap.add_argument('--out'); a=ap.parse_args()
cmd=[sys.executable,str(ROOT/'98_TOOLS/build_event_handout_v006.py'),a.profile]
if a.date:cmd += ['--date',a.date]
if a.checkpoint:cmd += ['--checkpoint',a.checkpoint]
if a.combat_input:cmd += ['--combat-input',a.combat_input]
with tempfile.NamedTemporaryFile(suffix='.json',delete=False) as f: tmp=f.name
cmd += ['--out',tmp]; p=subprocess.run(cmd,capture_output=True,text=True)
if p.returncode: raise SystemExit(p.stderr)
h=json.loads(pathlib.Path(tmp).read_text(encoding='utf-8')); pathlib.Path(tmp).unlink(missing_ok=True)
lines=[f"# Combat context: {h['profile']} {h.get('date')}",f"Checkpoint: {h['checkpoint']} / TECH: {h['technical_baseline']}",f"Structural execution blocked: {h['execution_blocked']}",f"Combat resolution ready: {h['combat_resolution_ready']}","","## Mandatory/conditional capability factors"]
for x in h.get('combat_factor_resolution',[]):
    mark='M' if x.get('mandatory') else 'C'; lines.append(f"- [{mark}] {x['factor_id']} {x['label']}: {x['resolution']}")
    if x['resolution'] in ('RUNTIME_INPUT_REQUIRED','UNKNOWN'): lines.append('  - Need: '+', '.join(x.get('runtime_input_keys',[])))
    for e in x.get('evidence',[])[:3]:
        if e.get('source')=='TECH_ENTRIES': lines.append('  - TECH: '+', '.join(e.get('entry_ids',[])[:6]))
        elif e.get('path'): lines.append('  - checkpoint: '+e['path'])
        elif e.get('paths'): lines.append('  - source: '+', '.join(e['paths'][:3]))
if h.get('combat_ready_block_reasons'): lines += ['', '## Must resolve before final combat result'] + ['- '+x for x in h['combat_ready_block_reasons']]
out='\n'.join(lines)+'\n'
if a.out:pathlib.Path(a.out).write_text(out,encoding='utf-8')
else:print(out,end='')
