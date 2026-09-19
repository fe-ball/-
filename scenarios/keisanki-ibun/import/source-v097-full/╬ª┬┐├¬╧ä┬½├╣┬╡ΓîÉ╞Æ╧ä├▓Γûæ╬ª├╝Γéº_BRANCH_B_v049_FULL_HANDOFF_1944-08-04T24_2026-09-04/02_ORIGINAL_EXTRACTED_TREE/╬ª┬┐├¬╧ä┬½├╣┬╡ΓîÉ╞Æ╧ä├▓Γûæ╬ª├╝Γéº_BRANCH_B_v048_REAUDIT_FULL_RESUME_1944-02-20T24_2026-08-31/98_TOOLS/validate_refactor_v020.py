#!/usr/bin/env python3
import json,pathlib,sys,subprocess,tempfile,os,re
ROOT=pathlib.Path(__file__).resolve().parents[1]; errs=[]; warns=[]
def err(x): errs.append(x)
def load(r):
 try:return json.loads((ROOT/r).read_text(encoding='utf-8'))
 except Exception as e:err(f'load failed {r}: {e}');return {}
json_files=list(ROOT.rglob('*.json'))
for p in json_files:
 try:json.loads(p.read_text(encoding='utf-8'))
 except Exception as e:err(f'invalid json {p.relative_to(ROOT)}: {e}')
state=load('06_RUNTIME/CURRENT_BRANCH_STATE_v012.json'); cp=load('05_WARTIME/CHECKPOINT_1943-12-31T24_BRANCH_B_v004.json'); idx=load('05_WARTIME/CHECKPOINT_INDEX_v018.json')
front=load('00_README/CURRENT_DISCUSSION_FRONTIER_v002.json'); reg=load('95_AUDIT/current_version_families_v021.json'); cand=load('06_RUNTIME/JAPAN_INDIAN_OCEAN_REINFORCEMENT_CANDIDATES_1944-01_WORKING_v006.json'); tl=load('06_RUNTIME/EASTERN_FLEET_INDICATION_TIMELINE_1943-12_1944-01_WORKING_v002.json'); oob=load('06_RUNTIME/EASTERN_FLEET_MEDIUM_LIGHT_OOB_1944-01_WORKING_v001.json')
# authority invariants
if state.get('active_restart',{}).get('checkpoint')!='CHECKPOINT_1943-12-31T24_BRANCH_B_v004':err('authority restart changed')
if idx.get('current_restart')!='CHECKPOINT_1943-12-31T24_BRANCH_B_v004':err('checkpoint index changed')
if cp.get('current_branch_overrides')!='00_CONFIG/current_branch_overrides_v012.json':err('override changed')
if front.get('authority_frontier',{}).get('changed_by_v033') is not False:err('v033 must not promote authority')
# discussion realization
if cand.get('dated_trigger_center',{}).get('actual_GO_realized') is not True:err('working GO not encoded')
if tl.get('branch_realization',{}).get('Axis_report_delivery_to_Japan_realized_working') is not True:err('Axis report delivery not encoded')
if tl.get('branch_realization',{}).get('authority_promotion') is not False:err('timeline promotes authority')
if cand.get('Pacific_opportunity_cost_debit',{}).get('modern_DD_screen_debit')!=4:err('Pacific DD allocation debit missing')
# OOB distinctions
new=set(oob.get('net_January_medium_light_new_arrival_set',[])); expected={'HNMS Tromp','HMS Petard','HMS Paladin','HMS Pathfinder','HMS Rocket','HMS Stonehenge','HMS Truculent'}
if new!=expected:err('Jan true-new set mismatch '+repr(new))
locals_={x.get('ship') for x in oob.get('not_true_new_arrivals_but_local_escort_joiners',[])}
if not {'HMS Rotherham','HMS Roebuck','HMS Racehorse','HMS Rapid','HMAS Norman','HMAS Napier','HMAS Nizam'}.issubset(locals_):err('local joiner set incomplete')
initial={x.get('ship') for x in oob.get('initial_UK_to_Port_Said_screen_not_retained_east_of_Suez',[])}
if initial!={'HMS Termagant','HMS Tenacious','HMS Kempenfelt'}:err('Port Said recalled screen distinction broken')
late={x.get('ship') for x in oob.get('February_or_later_reinforcements_explicitly_excluded_from_January',[])}
for name in ['HMS Gambia','HMS Maidstone','HMS Surf','HMS Sea Rover']:
 if name not in late:err(name+' must be excluded from Jan')
saved={x.get('ship') for x in oob.get('branch_saved_hulls_not_auto_counted',[])}
if not {'HMS Hermes','HMAS Vampire','HMS Hollyhock'}.issubset(saved):err('saved-hull anti-spawn guard missing')
if oob.get('submarine_late_Jan_physical_named_total',{}).get('count')!=7:err('sub physical named count mismatch')
if set(oob.get('late_Jan_near_Ceylon_cruiser_core',{}).get('center',[]))!={'HMS Emerald','HNMS Tromp'}:err('late Jan cruiser core mismatch')
# refs / registry
for rel in front.get('mandatory_load_order',[])+front.get('discussion_frontier',{}).get('working_not_promoted',[]):
 if not (ROOT/rel).exists():err('missing frontier ref '+rel)
fams={x['family']:x for x in reg.get('families',[])}
exp={'README_refactor_vX.md':'README_refactor_v033.md','NEXT_SESSION_HANDOFF_REFACTOR_vX.md':'NEXT_SESSION_HANDOFF_REFACTOR_v033.md','PACKAGE_MANIFEST_vX.json':'PACKAGE_MANIFEST_v033.json','VALIDATION_RESULT_vX.json':'VALIDATION_RESULT_v033.json','validate_refactor_vX.py':'validate_refactor_v020.py','CURRENT_DISCUSSION_FRONTIER_vX.json':'CURRENT_DISCUSSION_FRONTIER_v002.json','JAPAN_INDIAN_OCEAN_REINFORCEMENT_CANDIDATES_1944-01_WORKING_vX.json':'JAPAN_INDIAN_OCEAN_REINFORCEMENT_CANDIDATES_1944-01_WORKING_v006.json','EASTERN_FLEET_INDICATION_TIMELINE_1943-12_1944-01_WORKING_vX.json':'EASTERN_FLEET_INDICATION_TIMELINE_1943-12_1944-01_WORKING_v002.json','EASTERN_FLEET_MEDIUM_LIGHT_OOB_1944-01_WORKING_vX.json':'EASTERN_FLEET_MEDIUM_LIGHT_OOB_1944-01_WORKING_v001.json'}
for k,v in exp.items():
 if fams.get(k,{}).get('current')!=v:err('registry mismatch '+k)
def vn(n):
 m=re.search(r'_v(\d+)(?:\.|$)',n);return int(m.group(1)) if m else -1
for fam,x in fams.items():
 ms=[p for p in ROOT.rglob(fam.replace('vX','v*')) if '99_LEGACY_UNTOUCHED' not in p.parts]
 if ms:
  latest=max(ms,key=lambda p:vn(p.name)).name
  if x.get('latest_present')!=latest:err(f'latest_present mismatch {fam}: {x.get("latest_present")} != {latest}')
# runtime generator still authoritative
fd,tmp=tempfile.mkstemp(suffix='.json');os.close(fd)
try:
 p=subprocess.run([sys.executable,str(ROOT/'98_TOOLS/build_event_handout_v012.py'),'CARRIER_BATTLE','--date','1944-01-01','--out',tmp],capture_output=True,text=True,timeout=30)
 if p.returncode:err('generator failed '+p.stderr.strip())
 else:
  h=json.loads(pathlib.Path(tmp).read_text(encoding='utf-8'))
  if h.get('checkpoint')!='CHECKPOINT_1943-12-31T24_BRANCH_B_v004':err('generator checkpoint changed')
finally:
 try:os.unlink(tmp)
 except:pass
print(f'ERRORS={len(errs)} WARNINGS={len(warns)} JSON_FILES={len(json_files)}')
for x in errs:print('ERROR',x)
for x in warns:print('WARN',x)
sys.exit(1 if errs else 0)
