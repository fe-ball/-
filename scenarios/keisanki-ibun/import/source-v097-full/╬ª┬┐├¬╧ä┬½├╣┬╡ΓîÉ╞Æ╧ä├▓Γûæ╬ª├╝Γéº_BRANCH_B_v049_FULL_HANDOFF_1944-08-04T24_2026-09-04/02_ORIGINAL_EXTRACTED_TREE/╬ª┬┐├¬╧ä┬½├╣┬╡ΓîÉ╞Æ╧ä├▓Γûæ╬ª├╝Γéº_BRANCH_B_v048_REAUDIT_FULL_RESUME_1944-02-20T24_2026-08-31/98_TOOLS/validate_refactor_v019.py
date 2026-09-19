#!/usr/bin/env python3
import json, pathlib, sys, subprocess, tempfile, os, re
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
state=load('06_RUNTIME/CURRENT_BRANCH_STATE_v012.json')
ov=load('00_CONFIG/current_branch_overrides_v012.json')
idx=load('05_WARTIME/CHECKPOINT_INDEX_v018.json')
graph=load('05_WARTIME/CHECKPOINT_GRAPH_v017.json')
cp=load('05_WARTIME/CHECKPOINT_1943-12-31T24_BRANCH_B_v004.json')
reg=load('95_AUDIT/current_version_families_v020.json')
front=load('00_README/CURRENT_DISCUSSION_FRONTIER_v001.json')
hull=load('06_RUNTIME/JAPAN_HULL_RECONCILIATION_1944-01-01_WORKING_v004.json')
cand=load('06_RUNTIME/JAPAN_INDIAN_OCEAN_REINFORCEMENT_CANDIDATES_1944-01_WORKING_v005.json')
tl=load('06_RUNTIME/EASTERN_FLEET_INDICATION_TIMELINE_1943-12_1944-01_WORKING_v001.json')
obs=load('06_RUNTIME/ANDAMAN_ARAKAN_OBSERVATION_NETWORK_1944-01-01_WORKING_v001.json')
# authority invariants
if state.get('active_restart',{}).get('checkpoint')!='CHECKPOINT_1943-12-31T24_BRANCH_B_v004': err('current state restart mismatch')
if state.get('reopened_analysis_frontier'): err('authoritative state unexpectedly reopened')
if idx.get('current_restart')!='CHECKPOINT_1943-12-31T24_BRANCH_B_v004': err('checkpoint index restart mismatch')
if cp.get('current_branch_overrides')!='00_CONFIG/current_branch_overrides_v012.json': err('checkpoint override mismatch')
if front.get('authority_frontier',{}).get('changed_by_v032') is not False: err('v032 must not promote authority')
if front.get('authority_frontier',{}).get('state')!='06_RUNTIME/CURRENT_BRANCH_STATE_v012.json': err('frontier authority state mismatch')
# registry current vs latest semantics
families={x.get('family'):x for x in reg.get('families',[])}
expected_current={
 'README_refactor_vX.md':'README_refactor_v032.md',
 'NEXT_SESSION_HANDOFF_REFACTOR_vX.md':'NEXT_SESSION_HANDOFF_REFACTOR_v032.md',
 'PACKAGE_MANIFEST_vX.json':'PACKAGE_MANIFEST_v032.json',
 'VALIDATION_RESULT_vX.json':'VALIDATION_RESULT_v032.json',
 'validate_refactor_vX.py':'validate_refactor_v019.py',
 'CURRENT_BRANCH_STATE_vX.json':'CURRENT_BRANCH_STATE_v012.json',
 'current_branch_overrides_vX.json':'current_branch_overrides_v012.json',
 'CHECKPOINT_INDEX_vX.json':'CHECKPOINT_INDEX_v018.json',
 'CHECKPOINT_GRAPH_vX.json':'CHECKPOINT_GRAPH_v017.json',
 'JAPAN_HULL_RECONCILIATION_1944-01-01_WORKING_vX.json':'JAPAN_HULL_RECONCILIATION_1944-01-01_WORKING_v004.json',
 'JAPAN_INDIAN_OCEAN_REINFORCEMENT_CANDIDATES_1944-01_WORKING_vX.json':'JAPAN_INDIAN_OCEAN_REINFORCEMENT_CANDIDATES_1944-01_WORKING_v005.json'
}
for fam,cur in expected_current.items():
    if families.get(fam,{}).get('current')!=cur: err(f'registry current mismatch {fam}: {families.get(fam,{}).get("current")}')
def vn(name):
    m=re.search(r'_v(\d+)(?:\.|$)',name); return int(m.group(1)) if m else -1
for fam,x in families.items():
    pat=fam.replace('vX','v*')
    ms=[p for p in ROOT.rglob(pat) if '99_LEGACY_UNTOUCHED' not in p.parts]
    if ms:
        latest=max(ms,key=lambda p:vn(p.name)).name
        if x.get('latest_present')!=latest: err(f'latest_present mismatch {fam}: {x.get("latest_present")} != {latest}')
# frontier refs exist
for rel in front.get('mandatory_load_order',[])+front.get('discussion_frontier',{}).get('working_not_promoted',[]):
    if not (ROOT/rel).exists(): err('frontier missing ref '+rel)
# stale-open item repaired
remain='\n'.join(hull.get('remaining_hard_close_items',[])).lower()
if 'assign exact jan-1944 origin/route' in remain: err('stale origin/route open item survived into hull v004')
if not hull.get('closed_since_v003'): err('hull v004 missing closure note')
# timeline/source-data gates
if tl.get('branch_realization',{}).get('any_1944_Japanese_movement_order_realized') is not False: err('timeline incorrectly realizes Japanese 1944 movement')
events=tl.get('historical_events',[])
if not any(e.get('date')=='1944-01-11T16:40' and 'German aircraft' in e.get('event','') for e in events): err('11 Jan German visual gate missing')
if not any('boiler cleaning' in e.get('event','').lower() for e in events): err('post-arrival boiler-cleaning readiness gate missing')
if cand.get('dated_trigger_center',{}).get('actual_GO_realized') is not False: err('candidate screen incorrectly realizes GO')
# observation accounting: no fabricated exact radar count
pr=obs.get('accounting_decision',{}).get('physical_radar_station_count',{})
if pr.get('value') is not None or 'UNKNOWN' not in pr.get('status',''): err('observation model must keep Jan radar-site count unknown')
if obs.get('countable_summary',{}).get('forward_functional_reporting_nodes')!=4: err('forward functional node count mismatch')
if obs.get('data_gate_result')!='CLOSED_FOR_WORKING_SIMULATION_WITH_BOUNDED_NODE_MODEL': err('observation data gate not closed')
# runtime generator still resolves authoritative checkpoint from latest registry
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
    if h.get('checkpoint')!='CHECKPOINT_1943-12-31T24_BRANCH_B_v004': err('generator current checkpoint mismatch')
    if h.get('current_branch_overrides')!='00_CONFIG/current_branch_overrides_v012.json': err('generator override mismatch')
print(f'ERRORS={len(errs)} WARNINGS={len(warns)} JSON_FILES={len(json_files)}')
for x in errs: print('ERROR',x)
for x in warns: print('WARN',x)
sys.exit(1 if errs else 0)
