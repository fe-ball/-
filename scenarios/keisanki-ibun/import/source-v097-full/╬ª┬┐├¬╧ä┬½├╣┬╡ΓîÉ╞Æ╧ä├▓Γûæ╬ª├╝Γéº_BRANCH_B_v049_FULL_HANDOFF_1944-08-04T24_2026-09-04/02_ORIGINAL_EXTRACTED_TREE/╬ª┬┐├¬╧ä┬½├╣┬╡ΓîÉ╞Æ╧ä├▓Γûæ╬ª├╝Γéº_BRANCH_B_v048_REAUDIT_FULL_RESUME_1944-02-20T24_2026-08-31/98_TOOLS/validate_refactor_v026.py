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
front=load('00_README/CURRENT_DISCUSSION_FRONTIER_v012.json'); reg=load('95_AUDIT/current_version_families_v030.json'); tech=load('02_TECH/TECH_INDEX_v009.json')
if state.get('active_restart',{}).get('checkpoint')!='CHECKPOINT_1943-12-31T24_BRANCH_B_v004':err('authority restart changed')
if idx.get('current_restart')!='CHECKPOINT_1943-12-31T24_BRANCH_B_v004':err('checkpoint index changed')
if cp.get('current_branch_overrides')!='00_CONFIG/current_branch_overrides_v012.json':err('override changed')
if front.get('authority_frontier',{}).get('changed_by_v043') is not False:err('v043 must not promote authority')
if front.get('discussion_frontier',{}).get('discussion_clock_center')!='1944-02-06T18:00:00+12:00':err('discussion clock mismatch')
if tech.get('revision')!='v009':err('TECH_INDEX authority changed')
for rel in front.get('mandatory_load_order',[]):
 if not (ROOT/rel).exists():err('missing frontier ref '+rel)
rep=load('06_RUNTIME/CARRIER_DAMAGE_REPAIR_CLOCK_1944-02-03_WORKING_v001.json')
if '1944-04-28..1944-05-20' not in json.dumps(rep,ensure_ascii=False):err('Cabot return band missing')
if rep.get('ships',{}).get('USS_Intrepid_CV11',{}).get('near_normal_cycle_band')!='1944-02-04T04:00..1944-02-04T10:00':err('Intrepid clock changed')
if rep.get('ships',{}).get('IJN_Hiryu',{}).get('carrier_team_combat_readiness_band')!='1944-02-23..1944-03-02':err('Hiryu team gate changed')
sub=load('06_RUNTIME/FLINTLOCK_ASSAULT_APPROACH_SUBMARINE_INTERDICTION_1944-02-03_06_WORKING_v001.json')
bs=json.dumps(sub,ensure_ascii=False)
for tok in ['LST-224','constructive total loss','One Japanese conventional submarine sunk centered','Do not separately add']:
 if tok not in bs:err('sub interdiction guard/result missing '+tok)
dd=load('06_RUNTIME/FLINTLOCK_DDAY_DECISION_AND_LANDING_1944-02-06_WORKING_v001.json')
if dd.get('decision',{}).get('main_assault_D_day')!='1944-02-06':err('D-Day mismatch')
if 'secure enough to sustain unloading' not in json.dumps(dd.get('state_at_1800',{}),ensure_ascii=False):err('beachhead state missing')
air=load('06_RUNTIME/MARSHALL_AIR_OOB_1944-02-06T1800_WORKING_v001.json')
if air.get('theatre_1800',{}).get('combat_serviceable_center')!=21:err('Feb6 Marshall air center changed')
# preserve 3-Feb carrier battle centers
cs=load('06_RUNTIME/US_COUNTERSTRIKE_JAPAN_CARRIER_FORCE_1944-02-03_WORKING_v001.json')
if cs.get('carrier_battle_cumulative_3Feb',{}).get('Japan_irrecoverable_aircraft_center')!=73:err('3Feb Japan carrier-air center changed')
if cs.get('carrier_battle_cumulative_3Feb',{}).get('US_irrecoverable_aircraft_center')!=46:err('3Feb US carrier-air center changed')
# registry
fams={x['family']:x for x in reg.get('families',[])}
exp={'README_refactor_vX.md':'README_refactor_v043.md','NEXT_SESSION_HANDOFF_REFACTOR_vX.md':'NEXT_SESSION_HANDOFF_REFACTOR_v043.md','PACKAGE_MANIFEST_vX.json':'PACKAGE_MANIFEST_v043.json','VALIDATION_RESULT_vX.json':'VALIDATION_RESULT_v043.json','validate_refactor_vX.py':'validate_refactor_v026.py','CURRENT_DISCUSSION_FRONTIER_vX.json':'CURRENT_DISCUSSION_FRONTIER_v012.json','current_version_families_vX.json':'current_version_families_v030.json'}
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
