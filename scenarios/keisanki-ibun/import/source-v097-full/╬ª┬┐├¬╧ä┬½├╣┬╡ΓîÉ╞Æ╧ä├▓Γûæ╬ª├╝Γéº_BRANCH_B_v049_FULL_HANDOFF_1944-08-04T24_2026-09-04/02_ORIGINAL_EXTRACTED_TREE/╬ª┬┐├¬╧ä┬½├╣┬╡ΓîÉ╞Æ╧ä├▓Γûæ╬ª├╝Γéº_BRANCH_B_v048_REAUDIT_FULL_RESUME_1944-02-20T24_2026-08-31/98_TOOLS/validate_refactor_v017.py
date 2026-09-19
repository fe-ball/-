#!/usr/bin/env python3
import json, pathlib, sys, subprocess, tempfile, os, hashlib
ROOT=pathlib.Path(__file__).resolve().parents[1]
errs=[]; warns=[]
def err(x): errs.append(x)
def warn(x): warns.append(x)
def load(rel):
    try: return json.loads((ROOT/rel).read_text(encoding='utf-8'))
    except Exception as e: err(f'load failed {rel}: {e}'); return {}
json_files=list(ROOT.rglob('*.json'))
for p in json_files:
    try: json.loads(p.read_text(encoding='utf-8'))
    except Exception as e: err(f'invalid json {p.relative_to(ROOT)}: {e}')
state=load('06_RUNTIME/CURRENT_BRANCH_STATE_v011.json')
ov=load('00_CONFIG/current_branch_overrides_v011.json')
idx=load('05_WARTIME/CHECKPOINT_INDEX_v017.json')
graph=load('05_WARTIME/CHECKPOINT_GRAPH_v016.json')
cp=load('05_WARTIME/CHECKPOINT_1943-12-31T24_BRANCH_B_v003.json')
guard=load('06_RUNTIME/BRANCH_B_YEAR_END_GUARD_1944-01-01_v002.json')
reg=load('95_AUDIT/current_version_families_v018.json')
air=load('06_RUNTIME/AIRCRAFT_FIELDING_LEDGER_1943-10-01_v002.json')
kin=load('06_RUNTIME/GALVANIC_KINSEI_ZERO_FIELDING_GATE_1943-11_v001.json')
out=load('06_RUNTIME/GALVANIC_FINAL_OUTCOME_LEDGER_1943-11_12_v001.json')
repair=load('06_RUNTIME/GALVANIC_DAMAGE_REPAIR_REGEN_LEDGER_1943-11_1944Q1_v001.json')
if state.get('active_restart',{}).get('checkpoint')!='CHECKPOINT_1943-12-31T24_BRANCH_B_v003': err('current state restart mismatch')
if state.get('reopened_analysis_frontier'): err('GALVANIC reopened frontier still present')
if idx.get('current_restart')!='CHECKPOINT_1943-12-31T24_BRANCH_B_v003': err('index restart mismatch')
if cp.get('current_branch_overrides')!='00_CONFIG/current_branch_overrides_v011.json': err('checkpoint override mismatch')
if cp.get('rollback_guard')!='06_RUNTIME/BRANCH_B_YEAR_END_GUARD_1944-01-01_v002.json': err('checkpoint guard mismatch')
if cp.get('closed_dependency',{}).get('GALVANIC_1943_11')!='Closed and propagated': err('GALVANIC dependency not closed in checkpoint')
nodes={n.get('id'):n for n in graph.get('nodes',[])}
if nodes.get('CHECKPOINT_1943-12-31T24_BRANCH_B_v003',{}).get('execution_valid') is not True: err('v003 year-end not execution-valid')
if nodes.get('CHECKPOINT_1943-12-31T24_BRANCH_B_v002',{}).get('execution_valid') is not False: err('v002 year-end still execution-valid')
# Final fact checks
us=out.get('US_naval',{}); jp=out.get('Japan_naval',{})
if 'survives' not in us.get('Liscome_Bay_CVE56','').lower(): err('Liscome Bay survival missing')
if 'operational' not in us.get('Cowpens_CVL25','').lower(): err('Cowpens operational result missing')
if 'campaign mission-kill' not in us.get('Lexington_CV16','').lower(): err('Lexington major damage result missing')
if 'mission-kill' not in jp.get('Soryu','').lower(): err('Soryu mission-kill missing')
if 'Franks_DD554' not in us: err('Franks named loss missing')
if 'Pierce_APA50' not in us: err('Pierce named damage missing')
if kin.get('event_ready_and_allocatable',{}).get('center')!=20: err('Kinsei centered event allocation mismatch')
if air.get('post_cutoff_gates',{}).get('GALVANIC_1943_11')!='06_RUNTIME/GALVANIC_KINSEI_ZERO_FIELDING_GATE_1943-11_v001.json': err('aircraft ledger post-cutoff gate missing')
# Year-end state checks
jcp=cp.get('carrier_ledger',{}).get('Japan',{}); ucp=cp.get('carrier_ledger',{}).get('United_States',{})
if jcp.get('first_line_operational')!=['Shokaku','Zuikaku','Hiryu']: err('year-end Japanese operational core mismatch')
if jcp.get('first_line_repair')!=['Soryu']: err('year-end Soryu repair state mismatch')
if 'Independence (torpedo 11/23; unavailable)' not in ucp.get('GALVANIC_major_repair',[]): err('Independence year-end repair missing')
if 'Lexington CV-16 (torpedo+bombs 11/26; unavailable)' not in ucp.get('GALVANIC_major_repair',[]): err('Lexington year-end repair missing')
# Guard blocks old facts
rules='\n'.join(guard.get('rules',[]))
for s in ['Liscome Bay sinking','Cowpens campaign-out','undamaged Soryu','historical 12/4 mass Kwajalein/Roi raid']:
    if s not in rules: err('old-result block missing: '+s)
# Override closure
ovs={x.get('override_id'):x for x in ov.get('overrides',[])}
if 'OVR-BRANCH-B-GALVANIC-FINAL-CLOSEOUT-002' not in ovs: err('GALVANIC closeout override missing')
if 'OVR-BRANCH-B-KINSEI-ZERO-DATE-GATE-001' not in ovs: err('Kinsei date gate override missing')
# Registry
fm={f['family']:f['current'] for f in reg.get('families',[])}
expected={'CURRENT_BRANCH_STATE_vX.json':'CURRENT_BRANCH_STATE_v011.json','current_branch_overrides_vX.json':'current_branch_overrides_v011.json','CHECKPOINT_INDEX_vX.json':'CHECKPOINT_INDEX_v017.json','CHECKPOINT_GRAPH_vX.json':'CHECKPOINT_GRAPH_v016.json','AIRCRAFT_FIELDING_LEDGER_1943-10-01_vX.json':'AIRCRAFT_FIELDING_LEDGER_1943-10-01_v002.json','BRANCH_B_YEAR_END_GUARD_1944-01-01_vX.json':'BRANCH_B_YEAR_END_GUARD_1944-01-01_v002.json'}
for fam,cur in expected.items():
    if fm.get(fam)!=cur: err(f'registry mismatch {fam}: {fm.get(fam)}')
# Required files
for rel in ['06_RUNTIME/GALVANIC_BRANCH_B_1943-11_SETTLEMENT_v002.md','06_RUNTIME/GALVANIC_FINAL_OUTCOME_LEDGER_1943-11_12_v001.json','06_RUNTIME/GALVANIC_DAMAGE_REPAIR_REGEN_LEDGER_1943-11_1944Q1_v001.json','06_RUNTIME/GALVANIC_AIRCRAFT_AFTER_ACTION_LESSONS_1943-12_v001.md','06_RUNTIME/GALVANIC_KINSEI_ZERO_FIELDING_GATE_1943-11_v001.json','06_RUNTIME/BRANCH_B_1943H2_YEAR_END_SETTLEMENT_v002.md']:
    if not (ROOT/rel).exists(): err('required final authority missing '+rel)
# Runtime generator must resolve current checkpoint using latest registry
def run_handout():
    fd,tmp=tempfile.mkstemp(suffix='.json'); os.close(fd)
    try:
      p=subprocess.run([sys.executable,str(ROOT/'98_TOOLS/build_event_handout_v012.py'),'CARRIER_BATTLE','--date','1944-01-01','--out',tmp],capture_output=True,text=True,timeout=30)
      if p.returncode: err('generator failed: '+p.stderr.strip()); return {}
      return json.loads(pathlib.Path(tmp).read_text(encoding='utf-8'))
    finally:
      try: os.unlink(tmp)
      except OSError: pass
h=run_handout()
if h:
    if h.get('checkpoint')!='CHECKPOINT_1943-12-31T24_BRANCH_B_v003': err('generator current checkpoint mismatch')
    if h.get('current_branch_overrides')!='00_CONFIG/current_branch_overrides_v011.json': err('generator override mismatch')
    if h.get('rollback_guard')!='06_RUNTIME/BRANCH_B_YEAR_END_GUARD_1944-01-01_v002.json': err('generator guard mismatch')
# Repair schedule minimal consistency
ys=repair.get('year_end_repair_state',{})
for k in ['Independence','Lexington','Soryu']:
    if 'unavailable' not in ys.get(k,'').lower(): err(k+' should be unavailable at year end')
print(f'ERRORS={len(errs)} WARNINGS={len(warns)} JSON_FILES={len(json_files)}')
for x in errs: print('ERROR',x)
for x in warns: print('WARN',x)
sys.exit(1 if errs else 0)
