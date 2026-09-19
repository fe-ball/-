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
front=load('00_README/CURRENT_DISCUSSION_FRONTIER_v006.json'); reg=load('95_AUDIT/current_version_families_v025.json'); tech=load('02_TECH/TECH_INDEX_v009.json')
syn=load('06_RUNTIME/TECHNOLOGY_LINEAGE_SYNTHESIS_1944-01-28_WORKING_v003.json'); raid=load('06_RUNTIME/RAIDEN_INTERCEPTOR_SYSTEM_1943Q4_1944Q1_WORKING_v001.json'); exch=load('06_RUNTIME/AIR_DEFENSE_EXCHANGE_TRANSITION_POST_GALVANIC_1943-11_1944-01_WORKING_v001.json')
m1=load('06_RUNTIME/MARSHALL_AIR_OOB_1944-01-28_WORKING_v001.json'); m2=load('06_RUNTIME/MARSHALL_AIR_OOB_1944-01-28_WORKING_v002.json')
yan=load('06_RUNTIME/YANAGI_ROUTE_TECH_GATE_STATE_1944-01-28_WORKING_v001.json'); jet=load('06_RUNTIME/JAPAN_JET_DEVELOPMENT_REAUDIT_1944_1945_WORKING_v001.json')
# authority invariants
if state.get('active_restart',{}).get('checkpoint')!='CHECKPOINT_1943-12-31T24_BRANCH_B_v004':err('authority restart changed')
if idx.get('current_restart')!='CHECKPOINT_1943-12-31T24_BRANCH_B_v004':err('checkpoint index changed')
if cp.get('current_branch_overrides')!='00_CONFIG/current_branch_overrides_v012.json':err('override changed')
if front.get('authority_frontier',{}).get('changed_by_v037') is not False:err('v037 must not promote authority')
if front.get('discussion_frontier',{}).get('discussion_clock_center')!='1944-01-28':err('discussion clock advanced unexpectedly')
if tech.get('revision')!='v009':err('TECH_INDEX authority changed')
# v036 jet/Yanagi guards retained
if 'OUTBOUND_MISSION_ALIVE_AS_OF_1944-01-28' not in json.dumps(yan,ensure_ascii=False):err('I-34 Jan28 outbound-alive adjudication missing')
if 'NO 1944 operational jet' not in json.dumps(jet,ensure_ascii=False) and 'No 1944 operational jet' not in json.dumps(jet,ensure_ascii=False):err('1944 combat-jet guard missing')
# Raiden system shape
if raid.get('status')!='WORKING_BRANCH_ADJUDICATED_NOT_CURRENT':err('Raiden overlay status wrong')
std=raid.get('variants',{}).get('standard_production_raiden',{})
if std.get('climb_to_6000m_production_median')!='5:35-5:55':err('Raiden production-median climb not revised')
if '5:20' not in std.get('climb_to_6000m_good_aircraft_or_prototype_tail',''):err('Raiden old optimistic tail not preserved as tail')
hi=raid.get('variants',{}).get('high_altitude_mechanical_supercharge_subset',{})
if hi.get('serviceable_subset_band')!=[14,22]:err('high-alt Raiden subset missing/changed')
if raid.get('variants',{}).get('exhaust_turbo_experimental',{}).get('status_on_1944_01_28')!='TEST_ONLY_COMBAT_READY_0':err('turbo Raiden improperly combat-ready')
if raid.get('marshall_1944_01_28_composition_overlay',{}).get('serviceable_raiden_center')!=16:err('Marshall Raiden center not 16')
# Marshall v002 must preserve totals
for k in ['physical_center','combat_serviceable_center']:
 if m1.get('theatre_total',{}).get(k)!=m2.get('theatre_total',{}).get(k):err('Marshall total changed '+k)
if m2.get('raiden_composition_overlay',{}).get('serviceable_center')!=16:err('Marshall v002 Raiden overlay missing')
# fighter slots center = 72, no addition
fighters=0
for b in m2.get('base_layers',[]):
 r=b.get('serviceable_role_center',{})
 fighters += r.get('fighters',0)+r.get('fighter_or_local_cover',0)
if fighters!=72:err(f'Marshall serviceable fighter/local-cover total changed: {fighters}')
if m2.get('theatre_total',{}).get('combat_serviceable_center')!=136:err('Marshall serviceable theater center changed')
# Exchange transition
if exch.get('past_event_application',{}).get('GALVANIC_1943_11_26')!='LOCKED_NO_REWRITE':err('GALVANIC retro-rewrite guard missing')
blobex=json.dumps(exch,ensure_ascii=False)
for tok in ['+12% to +22%','percentage-point kill probability bonus','radar_suppressed_base']:
 if tok not in blobex:err('exchange transition guard missing '+tok)
# tech synthesis retains broad all-band and Raiden overlay
keys={b.get('key'):b for b in syn.get('bands',[])}
if len(keys)<15:err('all-band synthesis too narrow')
if 'raiden_1944Q1_overlay' not in keys.get('piston_fighters_engines',{}):err('Raiden lineage overlay missing')
# future summer guard
summer=(ROOT/'06_RUNTIME/1944SUMMER_JAPAN_US_FORCE_REGENERATION_WORKING_LEDGER_v002.md').read_text(encoding='utf-8')
if 'Do not convert this whole number into B-29-effective interceptors' not in summer:err('future Raiden B-29 inventory guard missing')
# refs/frontier
for rel in front.get('mandatory_load_order',[])+front.get('discussion_frontier',{}).get('working_not_promoted',[]):
 if not (ROOT/rel).exists():err('missing frontier ref '+rel)
# registry expected
fams={x['family']:x for x in reg.get('families',[])}
exp={
 'README_refactor_vX.md':'README_refactor_v037.md','NEXT_SESSION_HANDOFF_REFACTOR_vX.md':'NEXT_SESSION_HANDOFF_REFACTOR_v037.md','PACKAGE_MANIFEST_vX.json':'PACKAGE_MANIFEST_v037.json','VALIDATION_RESULT_vX.json':'VALIDATION_RESULT_v037.json','validate_refactor_vX.py':'validate_refactor_v024.py','CURRENT_DISCUSSION_FRONTIER_vX.json':'CURRENT_DISCUSSION_FRONTIER_v006.json','current_version_families_vX.json':'current_version_families_v025.json',
 'MARSHALL_AIR_OOB_1944-01-28_WORKING_vX.json':'MARSHALL_AIR_OOB_1944-01-28_WORKING_v002.json','TECHNOLOGY_LINEAGE_SYNTHESIS_1944-01-28_WORKING_vX.json':'TECHNOLOGY_LINEAGE_SYNTHESIS_1944-01-28_WORKING_v003.json','RAIDEN_INTERCEPTOR_SYSTEM_1943Q4_1944Q1_WORKING_vX.json':'RAIDEN_INTERCEPTOR_SYSTEM_1943Q4_1944Q1_WORKING_v001.json','AIR_DEFENSE_EXCHANGE_TRANSITION_POST_GALVANIC_1943-11_1944-01_WORKING_vX.json':'AIR_DEFENSE_EXCHANGE_TRANSITION_POST_GALVANIC_1943-11_1944-01_WORKING_v001.json','1944SUMMER_JAPAN_US_FORCE_REGENERATION_WORKING_LEDGER_vX.md':'1944SUMMER_JAPAN_US_FORCE_REGENERATION_WORKING_LEDGER_v002.md','RAIDEN_HEAVY_BOMBER_INTERCEPT_REAUDIT_2026-08-29_vX.md':'RAIDEN_HEAVY_BOMBER_INTERCEPT_REAUDIT_2026-08-29_v001.md'}
for k,v in exp.items():
 if fams.get(k,{}).get('current')!=v:err('registry mismatch '+k)
def vn(n):
 m=re.search(r'_v(\d+)(?:\.|$)',n);return int(m.group(1)) if m else -1
for fam,x in fams.items():
 ms=[p for p in ROOT.rglob(fam.replace('vX','v*')) if '99_LEGACY_UNTOUCHED' not in p.parts]
 if ms:
  latest=max(ms,key=lambda p:vn(p.name)).name
  if x.get('latest_present')!=latest:err(f'latest_present mismatch {fam}: {x.get("latest_present")} != {latest}')
# current runtime generator unchanged
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
