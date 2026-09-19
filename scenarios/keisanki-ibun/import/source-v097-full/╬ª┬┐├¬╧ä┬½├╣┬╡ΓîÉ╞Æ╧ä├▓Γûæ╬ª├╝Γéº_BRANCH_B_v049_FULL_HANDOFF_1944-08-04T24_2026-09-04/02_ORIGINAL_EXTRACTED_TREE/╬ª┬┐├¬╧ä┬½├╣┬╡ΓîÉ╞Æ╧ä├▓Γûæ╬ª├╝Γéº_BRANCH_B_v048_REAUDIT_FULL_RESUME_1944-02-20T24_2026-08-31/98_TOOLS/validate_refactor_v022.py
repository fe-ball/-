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
front=load('00_README/CURRENT_DISCUSSION_FRONTIER_v004.json'); reg=load('95_AUDIT/current_version_families_v023.json'); tech=load('02_TECH/TECH_INDEX_v009.json'); syn=load('06_RUNTIME/TECHNOLOGY_LINEAGE_SYNTHESIS_1944-01-28_WORKING_v001.json')
# authority invariants
if state.get('active_restart',{}).get('checkpoint')!='CHECKPOINT_1943-12-31T24_BRANCH_B_v004':err('authority restart changed')
if idx.get('current_restart')!='CHECKPOINT_1943-12-31T24_BRANCH_B_v004':err('checkpoint index changed')
if cp.get('current_branch_overrides')!='00_CONFIG/current_branch_overrides_v012.json':err('override changed')
if front.get('authority_frontier',{}).get('changed_by_v035') is not False:err('v035 must not promote authority')
if front.get('discussion_frontier',{}).get('discussion_clock_center')!='1944-01-28':err('discussion clock advanced unexpectedly')
if tech.get('revision')!='v009':err('TECH_INDEX authority changed')
# synthesis shape
bands=syn.get('bands',[])
if len(bands)<15:err('all-band synthesis too narrow')
keys={b.get('key'):b for b in bands}
for k in ['submarine_conventional_and_sentaka','radar_esm_ew_c2','piston_fighters_engines','capital_ships_yamato_refits','carrier_platform_deck_doctrine','crypto_comint_command','asw','jet_rocket_future','logistics_shipping_industry']:
 if k not in keys:err('missing synthesis band '+k)
if 'DOMESTIC' not in keys.get('submarine_conventional_and_sentaka',{}).get('dominant_origin',''):err('SenTaka provenance not domestic')
if 'GERMAN_CARD_COMPLETION' not in keys.get('radar_esm_ew_c2',{}).get('dominant_origin',''):err('radar/EW mixed provenance missing')
if 'DOMESTIC' not in keys.get('piston_fighters_engines',{}).get('dominant_origin',''):err('piston-fighter provenance not domestic')
# future/backport guards
blob=json.dumps(syn,ensure_ascii=False)
for token in ['BMW003','Jumo004','HWK509','Type XXI','schnorchel','future unresolved']:
 if token.lower() not in blob.lower():err('future guard missing '+token)
if 'Ko-1..6' not in blob:err('RO-500 anti-retrofit guard missing')
if 'weapon-quality' not in blob.lower():err('contact quality anti-magic guard missing')
# tech refs exist
techids={e.get('id') for e in tech.get('entries',[])}
for b in bands:
 for t in b.get('tech_index_refs',[]):
  if t not in techids:err('unknown tech ref '+str(t))
# refs/registry
for rel in front.get('mandatory_load_order',[])+front.get('discussion_frontier',{}).get('working_not_promoted',[]):
 if not (ROOT/rel).exists():err('missing frontier ref '+rel)
fams={x['family']:x for x in reg.get('families',[])}
exp={'README_refactor_vX.md':'README_refactor_v035.md','NEXT_SESSION_HANDOFF_REFACTOR_vX.md':'NEXT_SESSION_HANDOFF_REFACTOR_v035.md','PACKAGE_MANIFEST_vX.json':'PACKAGE_MANIFEST_v035.json','VALIDATION_RESULT_vX.json':'VALIDATION_RESULT_v035.json','validate_refactor_vX.py':'validate_refactor_v022.py','CURRENT_DISCUSSION_FRONTIER_vX.json':'CURRENT_DISCUSSION_FRONTIER_v004.json','TECHNOLOGY_LINEAGE_SYNTHESIS_1944-01-28_WORKING_vX.json':'TECHNOLOGY_LINEAGE_SYNTHESIS_1944-01-28_WORKING_v001.json','TECHNOLOGY_LINEAGE_ALL_BANDS_AUDIT_2026-08-29_vX.md':'TECHNOLOGY_LINEAGE_ALL_BANDS_AUDIT_2026-08-29_v001.md'}
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
