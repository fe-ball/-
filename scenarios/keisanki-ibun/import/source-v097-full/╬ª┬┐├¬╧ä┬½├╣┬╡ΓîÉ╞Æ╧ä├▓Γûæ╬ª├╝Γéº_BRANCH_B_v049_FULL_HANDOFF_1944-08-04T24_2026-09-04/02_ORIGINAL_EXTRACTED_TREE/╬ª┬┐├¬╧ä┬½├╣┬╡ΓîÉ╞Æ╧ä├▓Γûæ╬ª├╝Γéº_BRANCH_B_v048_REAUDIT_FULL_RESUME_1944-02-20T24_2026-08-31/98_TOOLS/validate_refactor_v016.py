#!/usr/bin/env python3
import json,pathlib,sys,re,subprocess,tempfile,os
ROOT=pathlib.Path(__file__).resolve().parents[1]; errs=[]; warns=[]
def err(x): errs.append(x)
def warn(x): warns.append(x)
def load(rel):
    try:return json.loads((ROOT/rel).read_text(encoding='utf-8'))
    except Exception as e: err(f'JSON load failed {rel}: {e}'); return {}
json_files=list(ROOT.rglob('*.json')); bad=[]
for p in json_files:
    try: json.loads(p.read_text(encoding='utf-8'))
    except Exception as e: bad.append((str(p.relative_to(ROOT)),str(e)))
if bad: err('bad JSON: '+repr(bad[:10]))
reg=load('95_AUDIT/current_version_families_v017.json'); fm={x.get('family'):x.get('current') for x in reg.get('families',[])}
required=['README_refactor_vX.md','NEXT_SESSION_HANDOFF_REFACTOR_vX.md','current_branch_overrides_vX.json','CURRENT_BRANCH_STATE_vX.json','CHECKPOINT_INDEX_vX.json','CHECKPOINT_GRAPH_vX.json','TECH_INDEX_vX.json','build_event_handout_vX.py','build_combat_context_vX.py','validate_refactor_vX.py','PACKAGE_MANIFEST_vX.json','VALIDATION_RESULT_vX.json','BRANCH_B_YEAR_END_GUARD_1944-01-01_vX.json']
for f in required:
    if f not in fm: err('registry family missing: '+f)
for fam,cur in fm.items():
    if cur and not [p for p in ROOT.rglob(cur) if '99_LEGACY_UNTOUCHED' not in p.parts]: err(f'registry target missing {fam}: {cur}')
state=load('06_RUNTIME/CURRENT_BRANCH_STATE_v010.json'); idx=load('05_WARTIME/CHECKPOINT_INDEX_v016.json'); graph=load('05_WARTIME/CHECKPOINT_GRAPH_v015.json'); cp=load('05_WARTIME/CHECKPOINT_1943-12-31T24_BRANCH_B_v002.json'); guard=load('06_RUNTIME/BRANCH_B_YEAR_END_GUARD_1944-01-01_v001.json'); ov=load('00_CONFIG/current_branch_overrides_v010.json'); tech=load('02_TECH/TECH_INDEX_v009.json')
if state.get('branch_id')!='BRANCH_B_1943SUMMER_EXPLORATION': err('current branch id mismatch')
if state.get('current_analysis_time')!='1944-01-01T00:00': err('current analysis time mismatch')
if idx.get('current_restart')!='CHECKPOINT_1943-12-31T24_BRANCH_B_v002': err('checkpoint index current restart mismatch')
if idx.get('graph')!='CHECKPOINT_GRAPH_v015.json': err('checkpoint index graph mismatch')
if state.get('active_restart',{}).get('checkpoint')!='CHECKPOINT_1943-12-31T24_BRANCH_B_v002': err('state restart mismatch')
if cp.get('as_of')!='1944-01-01T00:00:00': err('year-end checkpoint as_of mismatch')
if cp.get('technical_baseline')!='TECH_INDEX_v009': err('checkpoint TECH baseline mismatch')
if cp.get('current_branch_overrides')!='00_CONFIG/current_branch_overrides_v010.json': err('override binding missing')
if cp.get('rollback_guard')!='06_RUNTIME/BRANCH_B_YEAR_END_GUARD_1944-01-01_v001.json': err('year-end guard binding missing')
if guard.get('status')!='ACTIVE_CURRENT_BRANCH_B_YEAR_END': err('year-end guard not active')
if guard.get('restart')!='1944-01-01T00:00': err('year-end guard restart mismatch')
if not any('Do not import any realized combat event after 1943-12-31' in x for x in guard.get('rules',[])): err('future-history exclusion rule missing')
active={o.get('override_id') for o in ov.get('overrides',[]) if o.get('status')=='ACTIVE_CURRENT_BRANCH'}
for oid in ['OVR-BRANCH-B-RESTART-1944-01-01-001','OVR-BRANCH-B-1943H2-REALIZED-001','OVR-BRANCH-B-RN-AUDIT-001','OVR-BRANCH-B-1944-YEAREND-GUARD-001','OVR-BRANCH-B-JAPAN-NAVAL-WALLET-FIRST-001','OVR-BRANCH-B-I30-SURVIVAL-TECH-CHAIN-001','OVR-BRANCH-B-EW-1943-STAGED-001','OVR-BRANCH-B-GALVANIC-REAUDIT-001','OVR-BRANCH-B-CARRIER-ALL-CLASSES-001','OVR-BRANCH-B-GERMAN-FUTURE-TECH-GATES-001']:
    if oid not in active: err('active Branch B override missing '+oid)
nodes={n.get('id'):n for n in graph.get('nodes',[])}
if not nodes.get('CHECKPOINT_1943-12-31T24_BRANCH_B_v002',{}).get('execution_valid'): err('year-end current node not execution-valid')
if nodes.get('CHECKPOINT_1943-09-30T24_v003',{}).get('execution_valid') is not False: err('former Oct restart execution-valid')
if nodes.get('CHECKPOINT_1944-04-30T24_v004',{}).get('execution_valid') is not False: err('retained 1944 checkpoint execution-valid')
if cp.get('territory',{}).get('Chittagong') is None: err('Chittagong year-end state missing')
if cp.get('territory',{}).get('Tarawa') is None or cp.get('territory',{}).get('Makin') is None: err('GALVANIC territorial settlement missing')
if cp.get('carrier_ledger',{}).get('Japan',{}).get('first_line_core_alive')!=['Shokaku','Zuikaku','Hiryu','Soryu']: err('Japanese first-line carrier core mismatch')
if cp.get('carrier_ledger',{}).get('United_States',{}).get('branch_losses')!=['Lexington','Yorktown','Enterprise','Hornet','Saratoga']: err('US carrier losses mismatch')
if cp.get('carrier_ledger',{}).get('Britain',{}).get('branch_losses')!=['Indomitable','Formidable']: err('British carrier losses mismatch')
for rel in ['06_RUNTIME/BRANCH_B_1943H2_YEAR_END_SETTLEMENT_v001.md','06_RUNTIME/BENGAL_ARAKAN_CHITTAGONG_1943-10_12_SETTLEMENT_v001.md','06_RUNTIME/GALVANIC_BRANCH_B_1943-11_SETTLEMENT_v001.md','06_RUNTIME/DODECANESE_WITHDRAWAL_BRANCH_B_1943-11_SETTLEMENT_v001.md','06_RUNTIME/ROYAL_NAVY_DIVERGENCE_AUDIT_1942-1943_v001.md','06_RUNTIME/EASTERN_FLEET_1944Q1_POTENTIAL_GATE_v001.md','06_RUNTIME/JAPAN_NAVAL_FORCE_REOPEN_GATE_1944_v002.md']:
    if not (ROOT/rel).exists(): err('required settlement/gate missing '+rel)
expected={'CURRENT_BRANCH_STATE_vX.json':'CURRENT_BRANCH_STATE_v010.json','current_branch_overrides_vX.json':'current_branch_overrides_v010.json','CHECKPOINT_INDEX_vX.json':'CHECKPOINT_INDEX_v016.json','CHECKPOINT_GRAPH_vX.json':'CHECKPOINT_GRAPH_v015.json','build_event_handout_vX.py':'build_event_handout_v012.py','build_combat_context_vX.py':'build_combat_context_v007.py'}
for fam,cur in expected.items():
    if fm.get(fam)!=cur: err(f'registry current mismatch {fam}: {fm.get(fam)}')
def run_handout(profile,date,checkpoint=None):
    fd,tmp=tempfile.mkstemp(suffix='.json'); os.close(fd)
    try:
      cmd=[sys.executable,str(ROOT/'98_TOOLS/build_event_handout_v012.py'),profile,'--date',date,'--out',tmp]
      if checkpoint: cmd += ['--checkpoint',checkpoint]
      p=subprocess.run(cmd,capture_output=True,text=True,timeout=30)
      if p.returncode: err('generator failed '+p.stderr.strip()); return {}
      return json.loads(pathlib.Path(tmp).read_text(encoding='utf-8'))
    finally:
      try: os.unlink(tmp)
      except OSError: pass
h=run_handout('CARRIER_BATTLE','1944-01-01')
if h:
    if h.get('checkpoint')!='CHECKPOINT_1943-12-31T24_BRANCH_B_v002': err('generator default checkpoint mismatch')
    if h.get('checkpoint_execution_valid') is not True: err('generator current checkpoint not execution-valid')
    if h.get('technical_baseline')!='TECH_INDEX_v009': err('generator TECH mismatch')
    if h.get('current_branch_overrides')!='00_CONFIG/current_branch_overrides_v010.json': err('generator override missing')
    if h.get('rollback_guard')!='06_RUNTIME/BRANCH_B_YEAR_END_GUARD_1944-01-01_v001.json': err('generator year-end guard missing')
    if h.get('execution_blocked'): warn('event handout has unresolved mandatory runtime state at frontier: '+repr(h.get('block_reasons')))
old=run_handout('CARRIER_BATTLE','1944-05-01','CHECKPOINT_1944-04-30T24_v004')
if old and old.get('execution_blocked') is not True: err('retained 1944 checkpoint not structurally blocked when explicitly selected')

# v028 dependency-reopen checks
if not (ROOT/'05_WARTIME/CHECKPOINT_1943-11-23T00_BRANCH_B_GALVANIC_REAUDIT_v001.json').exists(): err('GALVANIC analysis checkpoint missing')
if not (ROOT/'06_RUNTIME/GALVANIC_BRANCH_B_1943-11_REAUDIT_GATE_v001.md').exists(): err('GALVANIC reaudit gate missing')
if state.get('reopened_analysis_frontier',{}).get('checkpoint')!='CHECKPOINT_1943-11-23T00_BRANCH_B_GALVANIC_REAUDIT_v001': err('reopened GALVANIC analysis frontier missing')
ids={e.get('id') for e in tech.get('entries',[])}
for tid in ['TECH-CONTACT-QUALITY-LADDER-001','TECH-ESM-METRIC-RWR-1943-001','TECH-SURFACE-NIGHT-ESM-TORPEDO-PREP-1943-001','TECH-SUB-ACOUSTIC-DECOY-BOLD-1943-001','TECH-SUB-GERMAN-COMPARATIVE-1943-001','TECH-JET-DOMESTIC-BENCH-1943-001']:
    if tid not in ids: err('TECH v009 audit card missing '+tid)
analysis_cp=load('05_WARTIME/CHECKPOINT_1943-11-23T00_BRANCH_B_GALVANIC_REAUDIT_v001.json')
if analysis_cp.get('technical_baseline')!='TECH_INDEX_v009': err('GALVANIC analysis checkpoint TECH mismatch')
if 'Ryujo' not in analysis_cp.get('carrier_ledger',{}).get('Japan',{}).get('secondary_carrier_candidates_requiring_trace',[]): err('secondary/light carrier audit guard missing')

print(f'ERRORS={len(errs)} WARNINGS={len(warns)} JSON_FILES={len(json_files)}')
for x in errs: print('ERROR',x)
for x in warns: print('WARN',x)
sys.exit(1 if errs else 0)
