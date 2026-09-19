#!/usr/bin/env python3
import os,json,sys,glob,hashlib
root=os.path.abspath(sys.argv[1] if len(sys.argv)>1 else os.path.join(os.path.dirname(__file__),'..'))
errs=[]; warns=[]
def load(rel):
    try:
        with open(os.path.join(root,rel),encoding='utf-8') as f:return json.load(f)
    except Exception as e: errs.append(f"cannot load {rel}: {e}"); return {}
def exists(rel): return os.path.exists(os.path.join(root,rel))
for p in glob.glob(os.path.join(root,'**','*.json'),recursive=True):
    try:
        with open(p,encoding='utf-8') as f: json.load(f)
    except Exception as e: errs.append(f"json parse {os.path.relpath(p,root)}: {e}")
tech=load('02_TECH/TECH_INDEX_v005.json'); tids={e['id'] for e in tech.get('entries',[])}
idx=load('05_WARTIME/CHECKPOINT_INDEX_v007.json'); current=idx.get('current_restart')
cp_rel=f'05_WARTIME/{current}.json'
if not exists(cp_rel): errs.append(f'current restart missing: {cp_rel}')
else:
    cp=load(cp_rel)
    if cp.get('technical_baseline')!='TECH_INDEX_v005': errs.append('current restart wrong TECH baseline')
    if cp.get('prewar_baseline')!='PREWAR_INDEX_v004': errs.append('current restart wrong PREWAR baseline')
    for t in cp.get('technical_entries',[]):
        if t not in tids: errs.append(f'current restart missing tech entry {t}')
if not exists('05_WARTIME/'+idx.get('graph','')): errs.append('checkpoint graph missing')
g=load('05_WARTIME/CHECKPOINT_GRAPH_v006.json')
if not any(n.get('id')==current and n.get('execution_valid') for n in g.get('nodes',[])): errs.append('current restart not execution-valid in graph')
for n in g.get('nodes',[]):
    if n.get('execution_valid') and n.get('checkpoint_file') and not exists(n['checkpoint_file']): errs.append(f"graph node file missing {n['id']}: {n['checkpoint_file']}")
required=[
'00_README/README_refactor_v008.md','00_README/NEXT_SESSION_HANDOFF_REFACTOR_v008.md',
'06_RUNTIME/1943_1944Q1_STRATEGIC_SETTLEMENT_v001.md','06_RUNTIME/WEAPONS_AUDIT_1944-04-30_v001.md',
'06_RUNTIME/AIR_COMBAT_RESEARCH_1944SPRING_v001.md','06_RUNTIME/MATERIALS_NICKEL_TURBO_JET_1944SPRING_v001.md',
'06_RUNTIME/ASW_TOKAI_MAD_SUBWAR_1944SPRING_v001.md','06_RUNTIME/I400_SEIRAN_READINESS_GATE_1944_v001.md',
'06_RUNTIME/EASTERN_FRONT_1941_1944Q1_DIFFERENTIAL_LEDGER_v001.md','06_RUNTIME/EUROPE_ITALY_OVERLORD_ANVIL_REAUDIT_1943_1944Q1_v001.md',
'06_RUNTIME/CHINA_BURMA_CBI_1943_1944Q1_SETTLEMENT_v001.md','06_RUNTIME/PACIFIC_CENTRAL_1943_1944Q1_SETTLEMENT_v001.md',
'06_RUNTIME/DECISION_RATIONALE_VARIABLE_LEDGER_v001.md']
for rel in required:
    if not exists(rel): errs.append(f'missing v008 settlement: {rel}')
if not os.path.isdir(os.path.join(root,'99_LEGACY_UNTOUCHED')): errs.append('legacy subtree missing')
print(f"ERRORS={len(errs)} WARNINGS={len(warns)}")
for x in errs: print('ERROR',x)
for x in warns: print('WARN',x)
sys.exit(1 if errs else 0)
