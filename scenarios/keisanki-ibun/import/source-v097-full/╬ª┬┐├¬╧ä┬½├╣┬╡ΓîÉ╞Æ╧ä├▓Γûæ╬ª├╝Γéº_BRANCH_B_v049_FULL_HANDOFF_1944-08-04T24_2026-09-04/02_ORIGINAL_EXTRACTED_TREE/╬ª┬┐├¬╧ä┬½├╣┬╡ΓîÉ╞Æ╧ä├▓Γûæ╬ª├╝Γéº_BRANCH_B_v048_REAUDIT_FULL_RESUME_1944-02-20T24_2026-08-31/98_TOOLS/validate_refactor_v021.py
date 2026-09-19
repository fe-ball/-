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
front=load('00_README/CURRENT_DISCUSSION_FRONTIER_v003.json'); reg=load('95_AUDIT/current_version_families_v022.json')
air=load('06_RUNTIME/MARSHALL_AIR_OOB_1944-01-28_WORKING_v001.json'); tf=load('06_RUNTIME/US_TF58_BRANCH_OOB_1944-01-28_WORKING_v001.json'); sub=load('06_RUNTIME/MARSHALL_SUBMARINE_CONTACT_LIAISON_1944-01-28_WORKING_v001.json'); par=load('06_RUNTIME/PARALLEL_THEATER_STATE_1944-01-28_WORKING_v001.json')
# authority invariants
if state.get('active_restart',{}).get('checkpoint')!='CHECKPOINT_1943-12-31T24_BRANCH_B_v004':err('authority restart changed')
if idx.get('current_restart')!='CHECKPOINT_1943-12-31T24_BRANCH_B_v004':err('checkpoint index changed')
if cp.get('current_branch_overrides')!='00_CONFIG/current_branch_overrides_v012.json':err('override changed')
if front.get('authority_frontier',{}).get('changed_by_v034') is not False:err('v034 must not promote authority')
if front.get('discussion_frontier',{}).get('discussion_clock_center')!='1944-01-28':err('discussion clock mismatch')
# TF58
if tf.get('fast_deck_total',{}).get('total')!=11:err('TF58 fast deck total must be 11')
if tf.get('fast_deck_total',{}).get('CV')!=5 or tf.get('fast_deck_total',{}).get('CVL')!=6:err('TF58 CV/CVL split mismatch')
groups=tf.get('task_groups',[])
if len(groups)!=3:err('TF58 must be 3 TG working organization')
carriers=[c for g in groups for c in g.get('carriers',[])]
for forbidden in ['Enterprise CV-6','Saratoga CV-3','Lexington CV-16','Independence CVL-22']:
 if forbidden in carriers:err('forbidden unavailable carrier reinserted '+forbidden)
for needed in ['Wasp CV-7','Yorktown CV-10','Essex CV-9','Intrepid CV-11','Bunker Hill CV-17','Princeton CVL-23','Belleau Wood CVL-24','Cowpens CVL-25','Monterey CVL-26','Langley CVL-27','Cabot CVL-28']:
 if needed not in carriers:err('missing fast deck '+needed)
# Marshall air layer
if air.get('theatre_total',{}).get('combat_serviceable_center')!=136:err('Marshall serviceable center mismatch')
if sum(x.get('serviceable_center',0) for x in air.get('base_layers',[]))!=136:err('Marshall base serviceable centers do not sum to 136')
if not str(air.get('kinsei_zero',{}).get('dedicated_Marshall_combat_detachment_on_28Jan','')).startswith('0 centered'):err('Kinsei anti-spawn guard missing')
# submarine liaison
if sub.get('jan28_assignment',{}).get('assigned_center')!=16:err('sub assigned center mismatch')
if sub.get('jan28_assignment',{}).get('on_station_center')!=12:err('sub on-station center mismatch')
rules=' '.join(x.get('content','') for x in sub.get('authoritative_internal_rules',[]))
for token in ['time/position/enemy type/course/speed/confidence/own state','continuous data link','preserve/shadow/report','silent-node']:
 if token.lower() not in rules.lower():err('sub liaison rule missing '+token)
if 'weapon-quality' not in ' '.join(sub.get('anti_double_count',[])).lower()+json.dumps(sub,ensure_ascii=False).lower():err('weapon-quality anti-magic guard missing')
# parallel state
if par.get('theaters',{}).get('Central_Pacific',{}).get('warning','').startswith('HIGH') is False:err('parallel Pacific warning not HIGH')
# refs/registry
for rel in front.get('mandatory_load_order',[])+front.get('discussion_frontier',{}).get('working_not_promoted',[]):
 if not (ROOT/rel).exists():err('missing frontier ref '+rel)
fams={x['family']:x for x in reg.get('families',[])}
exp={'README_refactor_vX.md':'README_refactor_v034.md','NEXT_SESSION_HANDOFF_REFACTOR_vX.md':'NEXT_SESSION_HANDOFF_REFACTOR_v034.md','PACKAGE_MANIFEST_vX.json':'PACKAGE_MANIFEST_v034.json','VALIDATION_RESULT_vX.json':'VALIDATION_RESULT_v034.json','validate_refactor_vX.py':'validate_refactor_v021.py','CURRENT_DISCUSSION_FRONTIER_vX.json':'CURRENT_DISCUSSION_FRONTIER_v003.json','MARSHALL_AIR_OOB_1944-01-28_WORKING_vX.json':'MARSHALL_AIR_OOB_1944-01-28_WORKING_v001.json','US_TF58_BRANCH_OOB_1944-01-28_WORKING_vX.json':'US_TF58_BRANCH_OOB_1944-01-28_WORKING_v001.json','MARSHALL_SUBMARINE_CONTACT_LIAISON_1944-01-28_WORKING_vX.json':'MARSHALL_SUBMARINE_CONTACT_LIAISON_1944-01-28_WORKING_v001.json','PARALLEL_THEATER_STATE_1944-01-28_WORKING_vX.json':'PARALLEL_THEATER_STATE_1944-01-28_WORKING_v001.json'}
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
