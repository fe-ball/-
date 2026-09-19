#!/usr/bin/env python3
import json,pathlib,sys,re,subprocess,tempfile,os
ROOT=pathlib.Path(__file__).resolve().parents[1]; errs=[]; warns=[]
def err(x): errs.append(x)
def load(rel):
    try:return json.loads((ROOT/rel).read_text(encoding='utf-8'))
    except Exception as e: err(f'JSON load failed {rel}: {e}'); return {}
json_files=list(ROOT.rglob('*.json')); bad=[]
for p in json_files:
    try: json.loads(p.read_text(encoding='utf-8'))
    except Exception as e: bad.append((str(p.relative_to(ROOT)),str(e)))
if bad: err('bad JSON: '+repr(bad[:10]))
reg=load('95_AUDIT/current_version_families_v013.json'); fm={x.get('family'):x.get('current') for x in reg.get('families',[])}
required=['README_refactor_vX.md','NEXT_SESSION_HANDOFF_REFACTOR_vX.md','CURRENT_BRANCH_STATE_vX.json','CHECKPOINT_INDEX_vX.json','CHECKPOINT_GRAPH_vX.json','TECH_INDEX_vX.json','build_event_handout_vX.py','build_combat_context_vX.py','validate_refactor_vX.py','PACKAGE_MANIFEST_vX.json','VALIDATION_RESULT_vX.json','BRANCH_INVARIANT_GUARD_1943-10-01_vX.json','AIRCRAFT_FIELDING_LEDGER_1943-10-01_vX.json','SEAPLANE_TACTICS_LEDGER_1943-10-01_vX.json']
for f in required:
    if f not in fm: err('registry family missing: '+f)
for fam,cur in fm.items():
    if cur and not [p for p in ROOT.rglob(cur) if '99_LEGACY_UNTOUCHED' not in p.parts]: err(f'registry target missing {fam}: {cur}')
state=load('06_RUNTIME/CURRENT_BRANCH_STATE_v006.json'); idx=load('05_WARTIME/CHECKPOINT_INDEX_v012.json'); graph=load('05_WARTIME/CHECKPOINT_GRAPH_v011.json'); cp=load('05_WARTIME/CHECKPOINT_1943-09-30T24_v002.json'); inv=load('06_RUNTIME/BRANCH_INVARIANT_GUARD_1943-10-01_v002.json'); air=load('06_RUNTIME/AIRCRAFT_FIELDING_LEDGER_1943-10-01_v001.json'); sea=load('06_RUNTIME/SEAPLANE_TACTICS_LEDGER_1943-10-01_v001.json'); tech=load('02_TECH/TECH_INDEX_v007.json')
if state.get('current_analysis_time')!='1943-10-01T00:00': err('current analysis time mismatch')
if idx.get('current_restart')!='CHECKPOINT_1943-09-30T24_v002': err('checkpoint index current restart mismatch')
if state.get('active_restart',{}).get('checkpoint')!='CHECKPOINT_1943-09-30T24_v002': err('state restart mismatch')
if cp.get('technical_baseline')!='TECH_INDEX_v007': err('checkpoint TECH baseline not v007')
if cp.get('branch_invariants')!='06_RUNTIME/BRANCH_INVARIANT_GUARD_1943-10-01_v002.json': err('checkpoint invariant not v002')
if cp.get('aircraft_fielding_ledger')!='06_RUNTIME/AIRCRAFT_FIELDING_LEDGER_1943-10-01_v001.json': err('aircraft ledger not checkpoint-bound')
if cp.get('seaplane_tactics_ledger')!='06_RUNTIME/SEAPLANE_TACTICS_LEDGER_1943-10-01_v001.json': err('seaplane ledger not checkpoint-bound')
nodes={n.get('id'):n for n in graph.get('nodes',[])}
if not nodes.get('CHECKPOINT_1943-09-30T24_v002',{}).get('execution_valid'): err('v002 current node not valid')
if nodes.get('CHECKPOINT_1943-09-30T24_v001',{}).get('execution_valid') is not False: err('v001 restart still valid')
if inv.get('territorial_control',{}).get('Midway',{}).get('state')!='JAPANESE_HELD': err('Midway guard lost')
if inv.get('territorial_control',{}).get('New_Caledonia',{}).get('state')!='JAPANESE_MILITARY_CONTROL_VICHY_NOMINAL_SOVEREIGNTY': err('New Caledonia nuance lost')
required_air=['TECH-AIR-D4Y-FIELDING-1942-43-001','TECH-AIR-B6N-FIELDING-1942-43-001','TECH-AIR-J2M-FIELDING-1942-43-001','TECH-AIR-N1K1-KYOFU-FIELDING-1943-001','TECH-AIR-E16A-ZUIUN-FIELDING-1943-001','TECH-AIR-SEAPLANE-DOCTRINE-1942-43-001','TECH-AIR-US-F6F-CARRIER-FIELDING-1943-001','TECH-AIR-SEAPLANE-OPENING-001','TECH-SEARCH-MULTILAYER-001']
tids={e.get('id') for e in tech.get('entries',[])}
for t in required_air:
    if t not in tids: err('required aviation TECH missing '+t)
    if t not in cp.get('technical_entries',[]): err('checkpoint does not declare '+t)
if air.get('japan',{}).get('N1K1_Kyofu',{}).get('october_1943')!='70-90 completed; 50-65 frontline center': err('Kyofu October clock missing')
if 'combat-ready local detachment' not in air.get('japan',{}).get('E16A_Zuiun',{}).get('restart_rule',''): err('Zuiun restart gate missing')
if air.get('united_states',{}).get('june_efate',{}).get('F6F')!='NOT_PRESENT_IN_THIS_BATTLE': err('June Efate F6F exclusion missing')
if sea.get('night_operations',{}).get('state')!='EVENT_SPECIFIC_NOT_GENERIC_BONUS': err('seaplane night rule missing')
if 'broad sector search' not in sea.get('search_contact_cycle',[]): err('multilayer water search cycle missing')
# smoke generator
def run(profile,date):
    fd,tmp=tempfile.mkstemp(suffix='.json'); os.close(fd)
    try:
      p=subprocess.run([sys.executable,str(ROOT/'98_TOOLS/build_event_handout_v009.py'),profile,'--date',date,'--out',tmp],capture_output=True,text=True,timeout=30)
      if p.returncode: err('generator failed '+p.stderr.strip()); return {}
      return json.loads(pathlib.Path(tmp).read_text(encoding='utf-8'))
    finally:
      try: os.unlink(tmp)
      except OSError: pass
h=run('CARRIER_BATTLE','1943-10-01')
if h:
    if h.get('checkpoint')!='CHECKPOINT_1943-09-30T24_v002': err('generator default checkpoint mismatch')
    if h.get('technical_baseline')!='TECH_INDEX_v007': err('generator TECH mismatch')
    if h.get('aircraft_fielding_ledger')!='06_RUNTIME/AIRCRAFT_FIELDING_LEDGER_1943-10-01_v001.json': err('generator aircraft ledger injection failed')
    if h.get('seaplane_tactics_ledger')!='06_RUNTIME/SEAPLANE_TACTICS_LEDGER_1943-10-01_v001.json': err('generator seaplane ledger injection failed')
    selected={x.get('id') for x in h.get('entries',[])}
    for t in ['TECH-AIR-D4Y-FIELDING-1942-43-001','TECH-AIR-B6N-FIELDING-1942-43-001','TECH-AIR-J2M-FIELDING-1942-43-001','TECH-AIR-N1K1-KYOFU-FIELDING-1943-001','TECH-AIR-E16A-ZUIUN-FIELDING-1943-001','TECH-AIR-SEAPLANE-DOCTRINE-1942-43-001','TECH-AIR-US-F6F-CARRIER-FIELDING-1943-001']:
        if t not in selected: err('carrier handout did not surface '+t)
print(f'ERRORS={len(errs)} WARNINGS={len(warns)} JSON_FILES={len(json_files)}')
for x in errs: print('ERROR',x)
for x in warns: print('WARN',x)
sys.exit(1 if errs else 0)
