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
front=load('00_README/CURRENT_DISCUSSION_FRONTIER_v013.json'); reg=load('95_AUDIT/current_version_families_v031.json'); tech=load('02_TECH/TECH_INDEX_v009.json')
if state.get('active_restart',{}).get('checkpoint')!='CHECKPOINT_1943-12-31T24_BRANCH_B_v004':err('authority restart changed')
if idx.get('current_restart')!='CHECKPOINT_1943-12-31T24_BRANCH_B_v004':err('checkpoint index changed')
if cp.get('current_branch_overrides')!='00_CONFIG/current_branch_overrides_v012.json':err('override changed')
if front.get('authority_frontier',{}).get('changed_by_v046') is not False:err('v046 must not promote authority')
if front.get('discussion_frontier',{}).get('discussion_clock_center')!='1944-02-06T18:00:00+12:00':err('discussion clock changed')
if tech.get('revision')!='v009':err('TECH_INDEX authority changed')
for rel in front.get('mandatory_load_order',[]):
 if not (ROOT/rel).exists():err('missing frontier ref '+rel)
land=load('06_RUNTIME/JAPANESE_LAND_COMBAT_HARDWARE_LINEAGE_1932_1944_WORKING_v001.json')
if len(land.get('bands',[]))<9:err('land hardware bands incomplete')
if len(land.get('maturity_by_period',[]))<4:err('land maturity clock incomplete')
if 'No global Army-artillery hit-rate scalar.' not in json.dumps(land,ensure_ascii=False):err('artillery scalar guard missing')
retro=load('06_RUNTIME/ALLIED_DEATH_TALLY_RETROACTIVE_LAND_HARDWARE_RESERVATION_1941_1944_WORKING_v001.json')
if retro.get('status')!='WORKING_ACCOUNTING_RESERVATION_NOT_YET_APPLIED':err('retro reservation applied too early')
if retro.get('ledger_label_ja')!='連合死者出納表':err('Japanese tally label missing')
if retro.get('method',{}).get('no_blanket_multiplier') is not True:err('retro no-multiplier guard missing')
if retro.get('method',{}).get('no_1944_backport_to_1941') is not True:err('maturity backport guard missing')
dd1=load('06_RUNTIME/FLINTLOCK_DDAY_DECISION_AND_LANDING_1944-02-06_WORKING_v001.json'); dd2=load('06_RUNTIME/FLINTLOCK_DDAY_DECISION_AND_LANDING_1944-02-06_WORKING_v002.json')
if dd2.get('decision')!=dd1.get('decision'):err('D-Day decision changed in v046')
if dd2.get('landing_execution')!=dd1.get('landing_execution'):err('D-Day geography/execution changed in v046')
if dd2.get('centered_first_day_costs')!=dd1.get('centered_first_day_costs'):err('D-Day casualty numbers changed despite deferred retro rule')
if dd2.get('land_hardware_accounting_status',{}).get('no_reroll_in_v046') is not True:err('D-Day no-reroll guard missing')
syn=load('06_RUNTIME/TECHNOLOGY_LINEAGE_SYNTHESIS_1944-01-28_WORKING_v004.json')
if not any(x.get('key')=='land_combat_hardware_engineering' for x in syn.get('bands',[])):err('all-band synthesis missing land hardware')
# preserve v043 carrier/sub/D-day states
rep=load('06_RUNTIME/CARRIER_DAMAGE_REPAIR_CLOCK_1944-02-03_WORKING_v001.json')
if '1944-04-28..1944-05-20' not in json.dumps(rep,ensure_ascii=False):err('Cabot return band missing')
sub=load('06_RUNTIME/FLINTLOCK_ASSAULT_APPROACH_SUBMARINE_INTERDICTION_1944-02-03_06_WORKING_v001.json')
if 'LST-224' not in json.dumps(sub,ensure_ascii=False):err('LST-224 result lost')
air=load('06_RUNTIME/MARSHALL_AIR_OOB_1944-02-06T1800_WORKING_v001.json')
if air.get('theatre_1800',{}).get('combat_serviceable_center')!=21:err('Feb6 Marshall air center changed')
# registry latest/current
fams={x['family']:x for x in reg.get('families',[])}
exp={'README_refactor_vX.md':'README_refactor_v046.md','NEXT_SESSION_HANDOFF_REFACTOR_vX.md':'NEXT_SESSION_HANDOFF_REFACTOR_v046.md','PACKAGE_MANIFEST_vX.json':'PACKAGE_MANIFEST_v046.json','VALIDATION_RESULT_vX.json':'VALIDATION_RESULT_v046.json','validate_refactor_vX.py':'validate_refactor_v027.py','CURRENT_DISCUSSION_FRONTIER_vX.json':'CURRENT_DISCUSSION_FRONTIER_v013.json','current_version_families_vX.json':'current_version_families_v031.json','FLINTLOCK_DDAY_DECISION_AND_LANDING_1944-02-06_WORKING_vX.json':'FLINTLOCK_DDAY_DECISION_AND_LANDING_1944-02-06_WORKING_v002.json'}
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
  if h.get('checkpoint')!='CHECKPOINT_1943-12-31T24_BRANCH_B_v004':err('generator checkpoint changed')
finally:
 try:os.unlink(tmp)
 except:pass
print(f'ERRORS={len(errs)} WARNINGS={len(warns)} JSON_FILES={len(json_files)}')
for x in errs:print('ERROR',x)
for x in warns:print('WARN',x)
sys.exit(1 if errs else 0)
