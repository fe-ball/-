#!/usr/bin/env python3
import os,json,sys,glob
root=os.path.abspath(sys.argv[1] if len(sys.argv)>1 else os.path.join(os.path.dirname(__file__),'..'))
errs=[]; warns=[]
def load(rel):
    try:
        with open(os.path.join(root,rel),encoding='utf-8') as f:return json.load(f)
    except Exception as e:
        errs.append(f"cannot load {rel}: {e}"); return {}
def exists(rel): return os.path.exists(os.path.join(root,rel))
# parse every json
for p in glob.glob(os.path.join(root,'**','*.json'),recursive=True):
    try:
        with open(p,encoding='utf-8') as f: json.load(f)
    except Exception as e: errs.append(f"json parse {os.path.relpath(p,root)}: {e}")
tech=load('02_TECH/TECH_INDEX_v004.json'); tids={e['id'] for e in tech.get('entries',[])}
if tech.get('entry_count')!=len(tech.get('entries',[])): errs.append('TECH entry_count mismatch')
pre=load('03_PREWAR/PREWAR_INDEX_v004.json')
if pre.get('entry_count')!=len(pre.get('entries',[])): errs.append('PREWAR entry_count mismatch')
for e in tech.get('entries',[]):
    for s in e.get('sources',[]):
        if not exists(s['path']): errs.append(f"missing TECH source {e['id']}: {s['path']}")
for e in pre.get('entries',[]):
    for t in e.get('tech_links',[]):
        if t not in tids: errs.append(f"PREWAR {e['id']} missing tech {t}")
    for s in e.get('sources',[]):
        if not exists(s['path']): errs.append(f"missing PREWAR source {e['id']}: {s['path']}")
ledger=load('04_WARSTART/WARSTART_STATE_LEDGER_v003.json')
for d in ledger.get('domains',[]):
    for t in d.get('tech_links',[]):
        if t not in tids: errs.append(f"WARSTART ledger {d['domain']} missing tech {t}")
ws=load('04_WARSTART/WARSTART_CHECKPOINT_v004.json')
if ws.get('technical_baseline')!='TECH_INDEX_v004': errs.append('WARSTART v004 wrong TECH baseline')
if ws.get('prewar_baseline')!='PREWAR_INDEX_v004': errs.append('WARSTART v004 wrong PREWAR baseline')
for s in ws.get('state_sources',[]):
    if not exists(s): errs.append(f"WARSTART missing state source: {s}")
idx=load('05_WARTIME/CHECKPOINT_INDEX_v005.json')
current=idx.get('current_restart')
cp_rel=f'05_WARTIME/{current}.json'
if not exists(cp_rel): errs.append(f"current restart missing: {cp_rel}")
else:
    cp=load(cp_rel)
    if cp.get('technical_baseline')!='TECH_INDEX_v004': errs.append('current restart wrong TECH baseline')
    if cp.get('prewar_baseline')!='PREWAR_INDEX_v004': errs.append('current restart wrong PREWAR baseline')
    for t in cp.get('technical_entries',[]):
        if t not in tids: errs.append(f"current restart missing tech entry {t}")
opening=idx.get('opening_baseline')
if opening=='WARSTART_1941-12-07_08_v004' and not exists('04_WARSTART/WARSTART_CHECKPOINT_v004.json'):
    errs.append('opening baseline pointer lacks actual WARSTART_CHECKPOINT_v004.json')
if not exists('05_WARTIME/'+idx.get('graph','')): errs.append('checkpoint graph missing')
g=load('05_WARTIME/CHECKPOINT_GRAPH_v004.json')
valid=[n for n in g.get('nodes',[]) if n.get('execution_valid')]
if not any(n.get('id')==current for n in valid): errs.append('current restart not execution-valid in graph')
# ensure current WARSTART node points to actual file when field supplied
for n in g.get('nodes',[]):
    if n.get('execution_valid') and n.get('checkpoint_file') and not exists(n['checkpoint_file']):
        errs.append(f"graph node file missing {n['id']}: {n['checkpoint_file']}")
# Legacy preservation presence
if not os.path.isdir(os.path.join(root,'99_LEGACY_UNTOUCHED')): errs.append('legacy subtree missing')
# Quarantined conversational GRT should not be in authoritative new supplement as accepted value
supp=open(os.path.join(root,'02_TECH/INDUSTRIAL_LOGISTICS_BASELINE_1932_1942_v001.md'),encoding='utf-8').read()
if 'canonical value としない' not in supp: warns.append('quarantine statement for mixed-scope GRT estimate not found')
print(f"ERRORS={len(errs)} WARNINGS={len(warns)}")
for x in errs: print('ERROR',x)
for x in warns: print('WARN',x)
sys.exit(1 if errs else 0)
