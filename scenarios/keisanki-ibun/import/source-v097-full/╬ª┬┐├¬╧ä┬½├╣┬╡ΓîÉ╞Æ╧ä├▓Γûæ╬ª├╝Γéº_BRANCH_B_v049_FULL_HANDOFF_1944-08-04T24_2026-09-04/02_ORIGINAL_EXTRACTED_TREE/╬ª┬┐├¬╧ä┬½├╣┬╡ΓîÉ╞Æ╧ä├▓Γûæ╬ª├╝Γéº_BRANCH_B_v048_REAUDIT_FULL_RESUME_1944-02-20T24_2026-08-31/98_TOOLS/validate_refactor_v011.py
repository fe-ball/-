#!/usr/bin/env python3
import json,pathlib,sys,re,subprocess,tempfile,hashlib,os
ROOT=pathlib.Path(__file__).resolve().parents[1]
errs=[]; warns=[]
def err(x): errs.append(x)
def load(rel):
    try:return json.loads((ROOT/rel).read_text(encoding='utf-8'))
    except Exception as e: err(f'JSON load failed {rel}: {e}'); return {}
def exists(rel): return (ROOT/rel).exists()
# Parse all JSON except legacy is still included because package integrity includes it.
json_files=list(ROOT.rglob('*.json')); bad=[]
for p in json_files:
    try:json.loads(p.read_text(encoding='utf-8'))
    except Exception as e: bad.append((str(p.relative_to(ROOT)),str(e)))
if bad: err('bad JSON: '+repr(bad[:8]))
# Registry full families and targets.
reg=load('95_AUDIT/current_version_families_v012.json'); fm={x.get('family'):x.get('current') for x in reg.get('families',[])}
required=['README_refactor_vX.md','NEXT_SESSION_HANDOFF_REFACTOR_vX.md','current_branch_overrides_vX.json','CURRENT_BRANCH_STATE_vX.json','CHECKPOINT_INDEX_vX.json','CHECKPOINT_GRAPH_vX.json','TECH_INDEX_vX.json','PREWAR_INDEX_vX.json','WARSTART_CHECKPOINT_vX.json','WARSTART_STATE_LEDGER_vX.json','WARSTART_DOMAIN_AUDIT_vX.json','EVENT_RELEVANCE_PROFILES_vX.json','EVENT_HANDOUT_SCHEMA_vX.json','RUNTIME_CONTRACT_vX.json','COMBAT_CAPABILITY_FACTOR_INDEX_vX.json','COMBAT_EVENT_FACTOR_MATRIX_vX.json','COMBAT_EVENT_INPUT_SCHEMA_vX.json','COMBAT_ADJUDICATION_CONTEXT_vX.md','WEAPON_PLATFORM_CAPABILITY_INDEX_vX.json','COMBAT_PLATFORM_MATRIX_vX.json','NOVEL_WEAPON_ADJUDICATION_POLICY_vX.json','build_event_handout_vX.py','build_combat_context_vX.py','validate_refactor_vX.py','PACKAGE_MANIFEST_vX.json','VALIDATION_RESULT_vX.json','BRANCH_INVARIANT_GUARD_1943-10-01_vX.json']
for f in required:
    if f not in fm: err('registry family missing: '+f)
# resolve family targets by expected directories
prefixes={'README_':'00_README/','NEXT_SESSION_':'00_README/','current_branch_':'00_CONFIG/','CURRENT_BRANCH_':'06_RUNTIME/','CHECKPOINT_':'05_WARTIME/','TECH_INDEX':'02_TECH/','PREWAR_INDEX':'03_PREWAR/','WARSTART_':'04_WARSTART/','EVENT_':'06_RUNTIME/','RUNTIME_':'06_RUNTIME/','COMBAT_':'06_RUNTIME/','WEAPON_':'06_RUNTIME/','NOVEL_':'06_RUNTIME/','build_':'98_TOOLS/','validate_':'98_TOOLS/','PACKAGE_':'95_AUDIT/','VALIDATION_':'95_AUDIT/','BRANCH_':'06_RUNTIME/'}
for fam,cur in fm.items():
    if not cur: continue
    matches=[p for p in ROOT.rglob(cur) if '99_LEGACY_UNTOUCHED' not in p.parts]
    if not matches: err(f'registry target missing {fam}: {cur}')
# Current state/index/graph/checkpoint agreement.
state=load('06_RUNTIME/CURRENT_BRANCH_STATE_v005.json'); idx=load('05_WARTIME/CHECKPOINT_INDEX_v011.json'); graph=load('05_WARTIME/CHECKPOINT_GRAPH_v010.json'); cp=load('05_WARTIME/CHECKPOINT_1943-09-30T24_v001.json'); inv=load('06_RUNTIME/BRANCH_INVARIANT_GUARD_1943-10-01_v001.json')
if state.get('current_analysis_time')!='1943-10-01T00:00': err('current analysis time mismatch')
if idx.get('current_restart')!='CHECKPOINT_1943-09-30T24_v001': err('checkpoint index current restart mismatch')
if state.get('active_restart',{}).get('checkpoint')!='CHECKPOINT_1943-09-30T24_v001': err('branch state restart checkpoint mismatch')
if cp.get('as_of')!='1943-10-01T00:00:00' or not cp.get('execution_valid'): err('current checkpoint as_of/execution mismatch')
node={n.get('id'):n for n in graph.get('nodes',[])}
if not node.get('CHECKPOINT_1943-09-30T24_v001',{}).get('execution_valid'): err('graph current 1943 node not execution-valid')
if node.get('CHECKPOINT_1944-04-30T24_v004',{}).get('execution_valid') is not False: err('former 1944 restart still execution-valid')
# Invariant content.
if inv.get('territorial_control',{}).get('Midway',{}).get('state')!='JAPANESE_HELD': err('Midway current ownership guard missing')
if inv.get('territorial_control',{}).get('New_Caledonia',{}).get('state')!='JAPANESE_MILITARY_CONTROL_VICHY_NOMINAL_SOVEREIGNTY': err('New Caledonia control nuance missing')
if inv.get('territorial_control',{}).get('Efate',{}).get('state')!='US_HELD': err('Efate state missing')
us=set(inv.get('carrier_and_hull_state',{}).get('United_States',{}).get('branch_losses_through_MI',[]))
if us!={'Lexington','Yorktown','Enterprise','Hornet','Saratoga'}: err('US branch carrier loss ledger mismatch')
br=set(inv.get('carrier_and_hull_state',{}).get('Britain',{}).get('branch_losses',[]))
if br!={'Indomitable','Formidable'}: err('British carrier loss ledger mismatch')
jp=set(inv.get('carrier_and_hull_state',{}).get('Japan',{}).get('first_line_core_alive',[]))
if jp!={'Shokaku','Zuikaku','Hiryu','Soryu'}: err('Japanese first-line carrier survival mismatch')
if inv.get('china_guard',{}).get('phase_III')!='HOLD toward Sichuan.': err('China Phase III HOLD guard missing')
# TECH and COMINT entries exist in current tech.
tech=load('02_TECH/TECH_INDEX_v006.json'); tids={e.get('id') for e in tech.get('entries',[])}
for tid in inv.get('sigint_comint_guard',{}).get('active_entries',[])+inv.get('japanese_combat_capability_guard',{}).get('active_or_relevant_by_cutoff',[]):
    if tid not in tids: err('guard TECH id missing from TECH v006: '+tid)
# Provisional Midway file may say US-held later; ensure it is not authoritative through current state.
if '06_RUNTIME/PACIFIC_MIDWAY_CONTINUOUS_CAMPAIGN_REAUDIT_1943-07_10_v001.md' not in state.get('retained_provisional',[]): err('Midway downstream file not marked retained provisional')
# Generator smoke: default must resolve current checkpoint and inject invariant guard.
def run(argv):
    fd,tmp=tempfile.mkstemp(suffix='.json');os.close(fd)
    try:
      p=subprocess.run([sys.executable,str(ROOT/'98_TOOLS/build_event_handout_v008.py'),*argv,'--out',tmp],capture_output=True,text=True,timeout=30)
      if p.returncode: err('generator failed: '+p.stderr.strip()); return {}
      return json.loads(pathlib.Path(tmp).read_text(encoding='utf-8'))
    finally:
      try:os.unlink(tmp)
      except OSError:pass
h=run(['CARRIER_BATTLE','--date','1943-10-01'])
if h:
    if h.get('checkpoint')!='CHECKPOINT_1943-09-30T24_v001': err('generator default checkpoint not 1943 restart')
    if h.get('branch_invariant_guard')!='06_RUNTIME/BRANCH_INVARIANT_GUARD_1943-10-01_v001.json': err('generator did not inject branch invariant guard')
    bi=h.get('branch_invariants') or {}
    if bi.get('territorial_control',{}).get('Midway',{}).get('state')!='JAPANESE_HELD': err('generator handout lost Midway invariant')
# Check README/handoff tokens.
for rel,toks in [('00_README/README_refactor_v023.md',['Midway','New Caledonia','Indomitable','Formidable','JN-25','Hanzhong']),('00_README/NEXT_SESSION_HANDOFF_REFACTOR_v023.md',['CHECKPOINT_1943-09-30T24_v001','Midway','Wasp','Sichuan Phase III HOLD'])]:
    txt=(ROOT/rel).read_text(encoding='utf-8') if exists(rel) else ''
    for t in toks:
        if t not in txt: err(f'{rel} missing {t}')
print(f'ERRORS={len(errs)} WARNINGS={len(warns)} JSON_FILES={len(json_files)}')
for x in errs: print('ERROR',x)
for x in warns: print('WARN',x)
sys.exit(1 if errs else 0)
