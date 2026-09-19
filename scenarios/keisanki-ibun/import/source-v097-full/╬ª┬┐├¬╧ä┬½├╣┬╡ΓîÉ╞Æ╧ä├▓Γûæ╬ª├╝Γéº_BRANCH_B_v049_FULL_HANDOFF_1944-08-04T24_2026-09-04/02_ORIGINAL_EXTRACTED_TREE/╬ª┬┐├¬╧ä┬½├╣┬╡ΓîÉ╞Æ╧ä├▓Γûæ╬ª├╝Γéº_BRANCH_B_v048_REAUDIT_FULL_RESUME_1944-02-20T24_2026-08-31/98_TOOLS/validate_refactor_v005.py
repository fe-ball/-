#!/usr/bin/env python3
import os,json,sys,glob,hashlib
root=os.path.abspath(sys.argv[1] if len(sys.argv)>1 else os.path.join(os.path.dirname(__file__),'..'))
errs=[]; warns=[]
def load(rel):
    try:
        with open(os.path.join(root,rel),encoding='utf-8') as f:return json.load(f)
    except Exception as e:
        errs.append(f"cannot load {rel}: {e}"); return {}
def exists(rel): return os.path.exists(os.path.join(root,rel))
for p in glob.glob(os.path.join(root,'**','*.json'),recursive=True):
    try:
        with open(p,encoding='utf-8') as f: json.load(f)
    except Exception as e: errs.append(f"json parse {os.path.relpath(p,root)}: {e}")
tech=load('02_TECH/TECH_INDEX_v004.json'); tids={e['id'] for e in tech.get('entries',[])}
pre=load('03_PREWAR/PREWAR_INDEX_v004.json')
idx=load('05_WARTIME/CHECKPOINT_INDEX_v006.json'); current=idx.get('current_restart')
cp_rel=f'05_WARTIME/{current}.json'
if not exists(cp_rel): errs.append(f'current restart missing: {cp_rel}')
else:
    cp=load(cp_rel)
    if cp.get('technical_baseline')!='TECH_INDEX_v004': errs.append('current restart wrong TECH baseline')
    if cp.get('prewar_baseline')!='PREWAR_INDEX_v004': errs.append('current restart wrong PREWAR baseline')
    for t in cp.get('technical_entries',[]):
        if t not in tids: errs.append(f'current restart missing tech entry {t}')
if not exists('05_WARTIME/'+idx.get('graph','')): errs.append('checkpoint graph missing')
g=load('05_WARTIME/CHECKPOINT_GRAPH_v005.json')
valid=[n for n in g.get('nodes',[]) if n.get('execution_valid')]
if not any(n.get('id')==current for n in valid): errs.append('current restart not execution-valid in graph')
for n in g.get('nodes',[]):
    if n.get('execution_valid') and n.get('checkpoint_file') and not exists(n['checkpoint_file']):
        errs.append(f"graph node file missing {n['id']}: {n['checkpoint_file']}")
for rel in ['06_RUNTIME/1942H2_STRATEGIC_SETTLEMENT_v001.md','06_RUNTIME/SANTO_1942-08_TECH_STACK_REAUDIT_v001.md','06_RUNTIME/NEW_CALEDONIA_1942-10_SETTLEMENT_v001.md','06_RUNTIME/ALLIED_LOGISTICS_FLEET_AXIS_EFFECTS_1942H2_v001.md','06_RUNTIME/CHINA_FIVEGO_POLITICAL_IMPLEMENTATION_1942Q4_v001.md']:
    if not exists(rel): errs.append(f'missing H2 settlement: {rel}')
if not os.path.isdir(os.path.join(root,'99_LEGACY_UNTOUCHED')): errs.append('legacy subtree missing')
# Quarantine guard
for rel in ['00_README/README_refactor_v007.md','00_README/NEXT_SESSION_HANDOFF_REFACTOR_v007.md','06_RUNTIME/1942H2_STRATEGIC_SETTLEMENT_v001.md']:
    if exists(rel):
        s=open(os.path.join(root,rel),encoding='utf-8').read()
        if '6.30--6.38m GRT' in s and '非canonical' not in s and 'noncanonical' not in s:
            errs.append(f'mixed-scope GRT appears without quarantine: {rel}')
print(f"ERRORS={len(errs)} WARNINGS={len(warns)}")
for x in errs: print('ERROR',x)
for x in warns: print('WARN',x)
sys.exit(1 if errs else 0)
