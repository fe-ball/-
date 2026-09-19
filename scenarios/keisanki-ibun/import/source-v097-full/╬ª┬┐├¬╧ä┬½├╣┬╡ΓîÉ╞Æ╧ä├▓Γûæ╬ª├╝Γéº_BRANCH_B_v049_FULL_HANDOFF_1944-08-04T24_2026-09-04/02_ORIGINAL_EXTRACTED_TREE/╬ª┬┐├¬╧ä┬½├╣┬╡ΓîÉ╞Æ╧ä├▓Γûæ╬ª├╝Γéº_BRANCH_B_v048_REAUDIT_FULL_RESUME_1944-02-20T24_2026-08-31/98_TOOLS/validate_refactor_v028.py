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
state=load('06_RUNTIME/CURRENT_BRANCH_STATE_v013.json'); cp=load('05_WARTIME/CHECKPOINT_1943-12-31T24_BRANCH_B_v005.json'); idx=load('05_WARTIME/CHECKPOINT_INDEX_v019.json')
front=load('00_README/CURRENT_DISCUSSION_FRONTIER_v014.json'); reg=load('95_AUDIT/current_version_families_v032.json'); tech=load('02_TECH/TECH_INDEX_v009.json')
if state.get('active_restart',{}).get('checkpoint')!='CHECKPOINT_1943-12-31T24_BRANCH_B_v005':err('authority restart mismatch')
if idx.get('current_restart')!='CHECKPOINT_1943-12-31T24_BRANCH_B_v005':err('checkpoint index mismatch')
if cp.get('current_branch_overrides')!='00_CONFIG/current_branch_overrides_v013.json':err('override mismatch')
if front.get('authority_frontier',{}).get('changed_by_v047') is not True:err('v047 ground rollback authority promotion missing')
if front.get('discussion_frontier',{}).get('discussion_clock_center')!='1944-02-06T18:00:00+12:00':err('discussion clock changed')
if tech.get('revision')!='v009':err('TECH_INDEX authority changed')
for rel in front.get('mandatory_load_order',[]):
 if not (ROOT/rel).exists():err('missing frontier ref '+rel)
land=load('06_RUNTIME/JAPANESE_LAND_COMBAT_HARDWARE_LINEAGE_1932_1944_WORKING_v001.json')
if len(land.get('bands',[]))<9:err('land hardware bands incomplete')
if len(land.get('maturity_by_period',[]))<4:err('land maturity clock incomplete')
if 'No global Army-artillery hit-rate scalar.' not in json.dumps(land,ensure_ascii=False):err('artillery scalar guard missing')
veh=load('06_RUNTIME/JAPANESE_LAND_VEHICLE_ARMOR_LINEAGE_1932_1944_WORKING_v001.json')
if len(veh.get('platform_families',[]))<6:err('vehicle families incomplete')
if '1.1-1.3x' not in json.dumps(veh,ensure_ascii=False):err('atoll vehicle reappearance guard missing')
integ=load('06_RUNTIME/JAPANESE_LAND_COMBAT_INTEGRATED_SYNTHESIS_1932_1944_WORKING_v001.json')
if len(integ.get('land_system_layers',[]))<7:err('integrated land layers incomplete')
retro=load('06_RUNTIME/ALLIED_DEATH_TALLY_RETROACTIVE_LAND_HARDWARE_RESERVATION_1941_1944_WORKING_v002.json')
if retro.get('status')!='WORKING_ACCOUNTING_RESERVATION_PARTIALLY_APPLIED_GALVANIC_ONLY':err('retro reservation state wrong')
if retro.get('ledger_label_ja')!='連合死者出納表':err('Japanese tally label missing')
if retro.get('method',{}).get('no_blanket_multiplier') is not True:err('retro no-multiplier guard missing')
if retro.get('method',{}).get('no_1944_backport_to_1941') is not True:err('maturity backport guard missing')
dd2=load('06_RUNTIME/FLINTLOCK_DDAY_DECISION_AND_LANDING_1944-02-06_WORKING_v002.json'); dd3=load('06_RUNTIME/FLINTLOCK_DDAY_DECISION_AND_LANDING_1944-02-06_WORKING_v003.json')
if dd3.get('decision')!=dd2.get('decision'):err('D-Day decision changed in v047')
if dd3.get('landing_execution')!=dd2.get('landing_execution'):err('D-Day geography/execution changed in v047')
if dd3.get('centered_first_day_costs')!=dd2.get('centered_first_day_costs'):err('D-Day casualty numbers changed despite remaining reservation')
if dd3.get('land_hardware_accounting_status',{}).get('no_reroll_in_v047') is not True:err('D-Day v047 no-reroll guard missing')
syn=load('06_RUNTIME/TECHNOLOGY_LINEAGE_SYNTHESIS_1944-01-28_WORKING_v005.json')
if not any(x.get('key')=='land_combat_hardware_engineering' for x in syn.get('bands',[])):err('all-band synthesis missing land hardware')
gal=load('06_RUNTIME/GALVANIC_FINAL_OUTCOME_LEDGER_1943-11_12_v003.json')
tg=gal.get('Tarawa_ground',{}); vc=tg.get('vehicle_OOB_and_serviceability',{}); cas=tg.get('US_final_casualties',{})
if vc.get('Japan_Type95_physical')!=14 or vc.get('Japan_post_suppression_contact_capable_band')!=[6,9]:err('GALVANIC Japanese vehicle OOB wrong')
if vc.get('US_M4A2_operational_first_night_band')!=[6,8]:err('GALVANIC M4 first-night band wrong')
if cas.get('total_band')!=[2150,2550] or cas.get('working_center_delta')!=250:err('GALVANIC casualty correction wrong')
if '1943-11-29' not in tg.get('organized_resistance_end',''):err('GALVANIC end-time correction missing')
# preserve v043 carrier/sub/D-day states
rep=load('06_RUNTIME/CARRIER_DAMAGE_REPAIR_CLOCK_1944-02-03_WORKING_v001.json')
if '1944-04-28..1944-05-20' not in json.dumps(rep,ensure_ascii=False):err('Cabot return band missing')
sub=load('06_RUNTIME/FLINTLOCK_ASSAULT_APPROACH_SUBMARINE_INTERDICTION_1944-02-03_06_WORKING_v001.json')
if 'LST-224' not in json.dumps(sub,ensure_ascii=False):err('LST-224 result lost')
air=load('06_RUNTIME/MARSHALL_AIR_OOB_1944-02-06T1800_WORKING_v001.json')
if air.get('theatre_1800',{}).get('combat_serviceable_center')!=21:err('Feb6 Marshall air center changed')
# registry latest/current
fams={x['family']:x for x in reg.get('families',[])}
exp={'README_refactor_vX.md':'README_refactor_v047.md','NEXT_SESSION_HANDOFF_REFACTOR_vX.md':'NEXT_SESSION_HANDOFF_REFACTOR_v047.md','PACKAGE_MANIFEST_vX.json':'PACKAGE_MANIFEST_v047.json','VALIDATION_RESULT_vX.json':'VALIDATION_RESULT_v047.json','validate_refactor_vX.py':'validate_refactor_v028.py','CURRENT_DISCUSSION_FRONTIER_vX.json':'CURRENT_DISCUSSION_FRONTIER_v014.json','current_version_families_vX.json':'current_version_families_v032.json','FLINTLOCK_DDAY_DECISION_AND_LANDING_1944-02-06_WORKING_vX.json':'FLINTLOCK_DDAY_DECISION_AND_LANDING_1944-02-06_WORKING_v003.json','CHECKPOINT_INDEX_vX.json':'CHECKPOINT_INDEX_v019.json','CHECKPOINT_GRAPH_vX.json':'CHECKPOINT_GRAPH_v018.json','CURRENT_BRANCH_STATE_vX.json':'CURRENT_BRANCH_STATE_v013.json','current_branch_overrides_vX.json':'current_branch_overrides_v013.json','BRANCH_B_YEAR_END_GUARD_1944-01-01_vX.json':'BRANCH_B_YEAR_END_GUARD_1944-01-01_v004.json'}
for k,v in exp.items():
 if fams.get(k,{}).get('current')!=v:err('registry mismatch '+k)
def vn(n):
 m=re.search(r'_v(\d+)(?:\.|$)',n);return int(m.group(1)) if m else -1
for fam,x in fams.items():
 ms=[p for p in ROOT.rglob(fam.replace('vX','v*')) if '99_LEGACY_UNTOUCHED' not in p.parts]
 if ms:
  latest=max(ms,key=lambda p:vn(p.name)).name
  if x.get('latest_present')!=latest:err(f'latest_present mismatch {fam}: {x.get("latest_present")} != {latest}')
# authority generator still resolves same checkpoint
fd,tmp=tempfile.mkstemp(suffix='.json');os.close(fd)
try:
 p=subprocess.run([sys.executable,str(ROOT/'98_TOOLS/build_event_handout_v012.py'),'CARRIER_BATTLE','--date','1944-01-01','--out',tmp],capture_output=True,text=True,timeout=30)
 if p.returncode:err('generator failed '+p.stderr.strip())
 else:
  h=json.loads(pathlib.Path(tmp).read_text(encoding='utf-8'))
  if h.get('checkpoint')!='CHECKPOINT_1943-12-31T24_BRANCH_B_v005':err('generator checkpoint mismatch')
finally:
 try:os.unlink(tmp)
 except:pass
print(f'ERRORS={len(errs)} WARNINGS={len(warns)} JSON_FILES={len(json_files)}')
for x in errs:print('ERROR',x)
for x in warns:print('WARN',x)
sys.exit(1 if errs else 0)
