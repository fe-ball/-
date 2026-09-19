#!/usr/bin/env python3
import json,pathlib,sys,re,subprocess,tempfile,os
ROOT=pathlib.Path(__file__).resolve().parents[1]; errs=[]; warns=[]
def err(x): errs.append(x)
def warn(x): warns.append(x)
def load(rel):
    try:return json.loads((ROOT/rel).read_text(encoding='utf-8'))
    except Exception as e: err(f'JSON load failed {rel}: {e}'); return {}
# Parse every JSON in package.
json_files=list(ROOT.rglob('*.json')); bad=[]
for p in json_files:
    try: json.loads(p.read_text(encoding='utf-8'))
    except Exception as e: bad.append((str(p.relative_to(ROOT)),str(e)))
if bad: err('bad JSON: '+repr(bad[:10]))
reg=load('95_AUDIT/current_version_families_v015.json'); fm={x.get('family'):x.get('current') for x in reg.get('families',[])}
required=['README_refactor_vX.md','NEXT_SESSION_HANDOFF_REFACTOR_vX.md','current_branch_overrides_vX.json','CURRENT_BRANCH_STATE_vX.json','CHECKPOINT_INDEX_vX.json','CHECKPOINT_GRAPH_vX.json','TECH_INDEX_vX.json','build_event_handout_vX.py','build_combat_context_vX.py','validate_refactor_vX.py','PACKAGE_MANIFEST_vX.json','VALIDATION_RESULT_vX.json','BRANCH_B_ROLLBACK_GUARD_1943-08-01_vX.json']
for f in required:
    if f not in fm: err('registry family missing: '+f)
for fam,cur in fm.items():
    if cur and not [p for p in ROOT.rglob(cur) if '99_LEGACY_UNTOUCHED' not in p.parts]: err(f'registry target missing {fam}: {cur}')
state=load('06_RUNTIME/CURRENT_BRANCH_STATE_v008.json'); idx=load('05_WARTIME/CHECKPOINT_INDEX_v014.json'); graph=load('05_WARTIME/CHECKPOINT_GRAPH_v013.json'); cp=load('05_WARTIME/CHECKPOINT_1943-07-31T24_BRANCH_B_v001.json'); guard=load('06_RUNTIME/BRANCH_B_ROLLBACK_GUARD_1943-08-01_v001.json'); ov=load('00_CONFIG/current_branch_overrides_v008.json'); tech=load('02_TECH/TECH_INDEX_v008.json')
if state.get('branch_id')!='BRANCH_B_1943SUMMER_EXPLORATION': err('current branch id mismatch')
if state.get('current_analysis_time')!='1943-08-01T00:00': err('current analysis time mismatch')
if idx.get('current_restart')!='CHECKPOINT_1943-07-31T24_BRANCH_B_v001': err('checkpoint index current restart mismatch')
if idx.get('graph')!='CHECKPOINT_GRAPH_v013.json': err('checkpoint index graph mismatch')
if state.get('active_restart',{}).get('checkpoint')!='CHECKPOINT_1943-07-31T24_BRANCH_B_v001': err('state restart mismatch')
if cp.get('as_of')!='1943-08-01T00:00:00': err('Branch B checkpoint as_of mismatch')
if cp.get('technical_baseline')!='TECH_INDEX_v008': err('checkpoint TECH baseline mismatch')
if cp.get('current_branch_overrides')!='00_CONFIG/current_branch_overrides_v008.json': err('Branch B override binding missing')
if cp.get('rollback_guard')!='06_RUNTIME/BRANCH_B_ROLLBACK_GUARD_1943-08-01_v001.json': err('Branch B rollback guard binding missing')
if guard.get('status')!='ACTIVE_CURRENT_BRANCH_B': err('rollback guard not active')
if guard.get('restart')!='1943-08-01T00:00': err('rollback guard restart mismatch')
if not any('Do not import any realized event after 1943-07-31' in x for x in guard.get('rules',[])): err('rollback future-history exclusion rule missing')
if not any('date-gated' in x for x in guard.get('rules',[])): err('rollback date-gate rule missing')
active={o.get('override_id') for o in ov.get('overrides',[]) if o.get('status')=='ACTIVE_CURRENT_BRANCH'}
for oid in ['OVR-BRANCH-B-RESTART-1943-08-01-001','OVR-BRANCH-B-ROLLBACK-GUARD-001','OVR-BRANCH-B-GALVANIC-FORECAST-ONLY-001','OVR-BRANCH-B-INDIA-NOT-CURRENT-PROGRAM-001']:
    if oid not in active: err('active Branch B override missing '+oid)
nodes={n.get('id'):n for n in graph.get('nodes',[])}
if not nodes.get('CHECKPOINT_1943-07-31T24_BRANCH_B_v001',{}).get('execution_valid'): err('Branch B current node not execution-valid')
if nodes.get('CHECKPOINT_1943-09-30T24_v003',{}).get('execution_valid') is not False: err('former Oct restart still execution-valid')
if cp.get('territory',{}).get('Midway')!='Japanese-held': err('Midway branch state lost')
if cp.get('territory',{}).get('New_Caledonia')!='Japanese military control under Vichy nominal sovereignty': err('New Caledonia branch nuance lost')
if cp.get('territory',{}).get('Kiska')!='evacuated by Japan late July; no Japanese garrison remains': err('Kiska evacuation state lost')
if cp.get('carrier_ledger',{}).get('Japan',{}).get('first_line_core_alive')!=['Shokaku','Zuikaku','Hiryu','Soryu']: err('Japanese first-line carrier core mismatch')
if cp.get('carrier_ledger',{}).get('United_States',{}).get('branch_losses')!=['Lexington','Yorktown','Enterprise','Hornet','Saratoga']: err('US carrier losses mismatch')
tids={e.get('id') for e in tech.get('entries',[])}
for tid in ['TECH-AIR-D4Y-FIELDING-1942-43-001','TECH-AIR-B6N-FIELDING-1942-43-001','TECH-AIR-US-F6F-CARRIER-FIELDING-1943-001','TECH-CARRIER-TACTICAL-MATURATION-1942-43-001','TECH-SURFACE-TACTICAL-MATURATION-1942-43-001']:
    if tid not in tids: err('required TECH entry missing '+tid)
# Current registry resolution checks.
expected={'CURRENT_BRANCH_STATE_vX.json':'CURRENT_BRANCH_STATE_v008.json','current_branch_overrides_vX.json':'current_branch_overrides_v008.json','CHECKPOINT_INDEX_vX.json':'CHECKPOINT_INDEX_v014.json','CHECKPOINT_GRAPH_vX.json':'CHECKPOINT_GRAPH_v013.json','build_event_handout_vX.py':'build_event_handout_v011.py','build_combat_context_vX.py':'build_combat_context_v006.py'}
for fam,cur in expected.items():
    if fm.get(fam)!=cur: err(f'registry current mismatch {fam}: {fm.get(fam)}')
# Smoke generator at Branch B frontier.
def run_handout(profile,date,checkpoint=None):
    fd,tmp=tempfile.mkstemp(suffix='.json'); os.close(fd)
    try:
      cmd=[sys.executable,str(ROOT/'98_TOOLS/build_event_handout_v011.py'),profile,'--date',date,'--out',tmp]
      if checkpoint: cmd += ['--checkpoint',checkpoint]
      p=subprocess.run(cmd,capture_output=True,text=True,timeout=30)
      if p.returncode: err('generator failed '+p.stderr.strip()); return {}
      return json.loads(pathlib.Path(tmp).read_text(encoding='utf-8'))
    finally:
      try: os.unlink(tmp)
      except OSError: pass
h=run_handout('CARRIER_BATTLE','1943-08-01')
if h:
    if h.get('checkpoint')!='CHECKPOINT_1943-07-31T24_BRANCH_B_v001': err('generator default checkpoint mismatch')
    if h.get('checkpoint_execution_valid') is not True: err('generator current checkpoint not execution-valid')
    if h.get('technical_baseline')!='TECH_INDEX_v008': err('generator TECH mismatch')
    if h.get('current_branch_overrides')!='00_CONFIG/current_branch_overrides_v008.json': err('generator Branch B override missing')
    if h.get('rollback_guard')!='06_RUNTIME/BRANCH_B_ROLLBACK_GUARD_1943-08-01_v001.json': err('generator rollback guard path missing')
    if (h.get('rollback_guard_state') or {}).get('id')!='BRANCH_B_ROLLBACK_GUARD_1943-08-01_v001': err('generator rollback guard state not injected')
    if h.get('execution_blocked'): err('generator structurally blocked at current Branch B frontier: '+repr(h.get('block_reasons')))
    e={x.get('id'):x for x in h.get('entries',[])}
    if e.get('TECH-AIR-E16A-ZUIUN-FIELDING-1943-001',{}).get('date_gate_state')=='ACTIVE_OR_CONDITIONAL': err('Zuiun future fielding improperly back-ported to Aug 1')
    for tid in ['TECH-AIR-D4Y-FIELDING-1942-43-001','TECH-AIR-B6N-FIELDING-1942-43-001','TECH-AIR-US-F6F-CARRIER-FIELDING-1943-001','TECH-CARRIER-TACTICAL-MATURATION-1942-43-001','TECH-SURFACE-TACTICAL-MATURATION-1942-43-001']:
        if tid not in e: err('Branch B carrier handout did not surface '+tid)
# Explicit former Oct checkpoint must be structurally blocked in current graph.
old=run_handout('CARRIER_BATTLE','1943-10-01','CHECKPOINT_1943-09-30T24_v003')
if old and old.get('execution_blocked') is not True: err('former Oct checkpoint not structurally blocked when explicitly selected')
print(f'ERRORS={len(errs)} WARNINGS={len(warns)} JSON_FILES={len(json_files)}')
for x in errs: print('ERROR',x)
for x in warns: print('WARN',x)
sys.exit(1 if errs else 0)
