#!/usr/bin/env python3
import os,sys,json,glob,hashlib,re,subprocess,tempfile,pathlib
root=pathlib.Path(sys.argv[1] if len(sys.argv)>1 else pathlib.Path(__file__).resolve().parents[1]).resolve()
errs=[]; warns=[]

def err(msg): errs.append(msg)
def warn(msg): warns.append(msg)
def load(rel):
    try:return json.loads((root/rel).read_text(encoding='utf-8'))
    except Exception as e: err(f'cannot load {rel}: {e}'); return {}
def exists(rel): return (root/rel).exists()

def family_path(fam,current):
    if fam.startswith(('README_refactor','NEXT_SESSION_HANDOFF')): return pathlib.Path('00_README')/current
    if fam.startswith(('CHECKPOINT_','RULE_DEPENDENCY_MAP')): return pathlib.Path('05_WARTIME')/current
    if fam.startswith('TECH_INDEX'): return pathlib.Path('02_TECH')/current
    if fam.startswith('PREWAR_INDEX'): return pathlib.Path('03_PREWAR')/current
    if fam.startswith(('WARSTART_')): return pathlib.Path('04_WARSTART')/current
    if fam.startswith(('current_branch_overrides','DOMAIN_STATE_MAP','rule_override_protocol')): return pathlib.Path('00_CONFIG')/current
    if fam.startswith(('EVENT_RELEVANCE_PROFILES','EVENT_HANDOUT_SCHEMA','RUNTIME_CONTRACT')): return pathlib.Path('06_RUNTIME')/current
    if fam.startswith(('build_event_handout','validate_refactor')): return pathlib.Path('98_TOOLS')/current
    if fam.startswith(('TECH_COVERAGE_AUDIT','PACKAGE_MANIFEST','VALIDATION_RESULT')): return pathlib.Path('95_AUDIT')/current
    return pathlib.Path(current)

# Parse every JSON.
for p in root.rglob('*.json'):
    try: json.loads(p.read_text(encoding='utf-8'))
    except Exception as e: err(f'json parse {p.relative_to(root)}: {e}')

# Current family registry and required machinery coverage.
reg=load('95_AUDIT/current_version_families_v006.json')
fmap={x.get('family'):x.get('current') for x in reg.get('families',[])}
required_families=[
 'README_refactor_vX.md','NEXT_SESSION_HANDOFF_REFACTOR_vX.md','CHECKPOINT_INDEX_vX.json','CHECKPOINT_GRAPH_vX.json','TECH_INDEX_vX.json','PREWAR_INDEX_vX.json',
 'WARSTART_CHECKPOINT_vX.json','WARSTART_STATE_LEDGER_vX.json','WARSTART_DOMAIN_AUDIT_vX.json','current_branch_overrides_vX.json','DOMAIN_STATE_MAP_vX.json',
 'rule_override_protocol_vX.json','RULE_DEPENDENCY_MAP_vX.json','EVENT_RELEVANCE_PROFILES_vX.json','EVENT_HANDOUT_SCHEMA_vX.json','RUNTIME_CONTRACT_vX.json',
 'build_event_handout_vX.py','validate_refactor_vX.py','TECH_COVERAGE_AUDIT_vX.json','PACKAGE_MANIFEST_vX.json','VALIDATION_RESULT_vX.json']
for fam in required_families:
    if fam not in fmap: err(f'current family missing: {fam}')
    else:
        rel=family_path(fam,fmap[fam])
        if not exists(rel): err(f'current family target missing: {fam} -> {rel}')

# TECH / PREWAR / source integrity.
tech_rel=family_path('TECH_INDEX_vX.json',fmap.get('TECH_INDEX_vX.json','TECH_INDEX_v006.json'))
tech=load(str(tech_rel)); entries=tech.get('entries',[]); tids=[e.get('id') for e in entries]; tidset=set(tids)
if tech.get('entry_count')!=len(entries): err('TECH entry_count mismatch')
if len(tids)!=len(tidset): err('TECH duplicate ids')
for e in entries:
    for s in e.get('sources',[]):
        if not exists(s.get('path','')): err(f"missing TECH source {e.get('id')}: {s.get('path')}")
pre_rel=family_path('PREWAR_INDEX_vX.json',fmap.get('PREWAR_INDEX_vX.json','PREWAR_INDEX_v004.json'))
pre=load(str(pre_rel)); pentries=pre.get('entries',[])
if pre.get('entry_count')!=len(pentries): err('PREWAR entry_count mismatch')
for e in pentries:
    for t in e.get('tech_links',[]):
        if t not in tidset: err(f"PREWAR {e.get('id')} missing tech {t}")
    for s in e.get('sources',[]):
        if not exists(s.get('path','')): err(f"missing PREWAR source {e.get('id')}: {s.get('path')}")
# New v005 additions must have explicit gates in v006.
expected_gates={
 'TECH-AIR-COMBAT-MISSION-MATRIX-1944-001':'1944-03-01',
 'TECH-NICKEL-SELECTIVE-HOTTEMP-1943-44-001':'1943-01-01',
 'TECH-ASW-MAD-DATUM-LOCALIZATION-1943-44-001':'1943-10-01',
 'TECH-I400-SEIRAN-INTEGRATED-READINESS-1944-001':'1944-03-01'}
byid={e.get('id'):e for e in entries}
for eid,date in expected_gates.items():
    if eid not in byid: err(f'missing v008 TECH addition: {eid}')
    elif byid[eid].get('runtime_gate',{}).get('available_from')!=date: err(f'wrong/missing runtime gate {eid}')

# Current checkpoint / graph / sources / baselines.
idx_rel=family_path('CHECKPOINT_INDEX_vX.json',fmap.get('CHECKPOINT_INDEX_vX.json','CHECKPOINT_INDEX_v008.json'))
idx=load(str(idx_rel)); current=idx.get('current_restart')
cp_rel=pathlib.Path('05_WARTIME')/f'{current}.json'
if not exists(cp_rel): err(f'current restart missing: {cp_rel}')
cp=load(str(cp_rel)) if exists(cp_rel) else {}
if cp.get('technical_baseline')!=pathlib.Path(str(tech_rel)).stem: err(f"current restart TECH baseline {cp.get('technical_baseline')} != {pathlib.Path(str(tech_rel)).stem}")
if cp.get('prewar_baseline')!=pathlib.Path(str(pre_rel)).stem: err('current restart PREWAR baseline mismatch')
if cp.get('current_branch_overrides')!='00_CONFIG/current_branch_overrides_v003.json': err('current restart branch override pointer is not v003')
for s in cp.get('state_sources',[]):
    if not exists(s): err(f'current checkpoint missing state source: {s}')
if '06_RUNTIME/MATERIALS_NICKEL_TURBO_JET_1944SPRING_v001.md' not in cp.get('state_sources',[]): err('materials/nickel settlement absent from current checkpoint state_sources')
for t in cp.get('technical_entries',[]):
    if t not in tidset: err(f'current checkpoint technical entry missing from TECH: {t}')
if not cp.get('execution_valid'): err('current restart execution_valid is false')
graph_rel=pathlib.Path('05_WARTIME')/idx.get('graph','')
if not exists(graph_rel): err('checkpoint graph missing')
graph=load(str(graph_rel)) if exists(graph_rel) else {}
cn=next((n for n in graph.get('nodes',[]) if n.get('id')==current),None)
if not cn or not cn.get('execution_valid'): err('current restart not execution-valid in graph')
for n in graph.get('nodes',[]):
    if n.get('execution_valid') and n.get('checkpoint_file') and not exists(n['checkpoint_file']): err(f"graph node file missing {n.get('id')}: {n.get('checkpoint_file')}")
oldnode=next((n for n in graph.get('nodes',[]) if n.get('id')=='CHECKPOINT_1944-04-30T24_v001'),None)
if not oldnode or oldnode.get('execution_valid') or oldnode.get('superseded_by')!=current: err('v001 current checkpoint supersession not represented correctly')

# WARSTART links against current superset TECH.
ledger_rel=family_path('WARSTART_STATE_LEDGER_vX.json',fmap.get('WARSTART_STATE_LEDGER_vX.json','WARSTART_STATE_LEDGER_v003.json'))
ledger=load(str(ledger_rel))
for d in ledger.get('domains',[]):
    for t in d.get('tech_links',[]):
        if t not in tidset: err(f"WARSTART ledger {d.get('domain')} missing tech {t}")

# Profiles / domain map coverage.
prof_rel=family_path('EVENT_RELEVANCE_PROFILES_vX.json',fmap.get('EVENT_RELEVANCE_PROFILES_vX.json','EVENT_RELEVANCE_PROFILES_v003.json'))
profiles=load(str(prof_rel)); dmap_rel=family_path('DOMAIN_STATE_MAP_vX.json',fmap.get('DOMAIN_STATE_MAP_vX.json','DOMAIN_STATE_MAP_v002.json')); dmap=load(str(dmap_rel))
domains={e.get('domain') for e in entries}
for pname,p in profiles.get('profiles',{}).items():
    for dom in p.get('mandatory_domains',[]):
        if dom not in domains: err(f'profile {pname} mandatory domain absent from current TECH: {dom}')
        if dom not in dmap.get('checkpoint_state_paths',{}): err(f'profile {pname} mandatory domain missing checkpoint state map: {dom}')
    for req in p.get('state_requirements',[]):
        if req not in dmap.get('state_requirements',{}): err(f'profile {pname} state requirement undefined: {req}')
for needed in ['AIR_COMBAT','MATERIALS_PROPULSION','SUBMARINE_AVIATION']:
    if needed not in dmap.get('checkpoint_state_paths',{}): err(f'new TECH domain absent from checkpoint state map: {needed}')
for pname in ['BASE_DEFENSE','FORAGER_GATE','SPECIAL_STRIKE','INDUSTRIAL_AIRCRAFT']:
    if pname not in profiles.get('profiles',{}): err(f'new profile missing: {pname}')

# Override schema and dependency completeness.
proto_rel=family_path('rule_override_protocol_vX.json',fmap.get('rule_override_protocol_vX.json','rule_override_protocol_v002.json')); proto=load(str(proto_rel))
ov_rel=family_path('current_branch_overrides_vX.json',fmap.get('current_branch_overrides_vX.json','current_branch_overrides_v003.json')); ovs=load(str(ov_rel))
rules=load('00_CONFIG/rule_registry_v001.json'); rids={r.get('id') for r in rules.get('rules',[])}
actions=set(proto.get('override_schema',{}).get('action',[])); active_ov=[]
for o in ovs.get('overrides',[]):
    oid=o.get('override_id')
    for k in ['override_id','target_rule_ids','action','status','effective_from','impact_scope','effective_rule']:
        if k not in o: err(f'override {oid} missing schema field {k}')
    if not str(oid).startswith('OVR-'): err(f'bad override id: {oid}')
    if o.get('action') not in actions: err(f'override {oid} action not allowed by protocol')
    for rid in o.get('target_rule_ids',[]):
        if rid not in rids: err(f'override {oid} targets unknown base rule {rid}')
    if o.get('status')=='ACTIVE_CURRENT_BRANCH': active_ov.append(oid)
dep_rel=family_path('RULE_DEPENDENCY_MAP_vX.json',fmap.get('RULE_DEPENDENCY_MAP_vX.json','RULE_DEPENDENCY_MAP_v002.json')); dep=load(str(dep_rel))
dep_rules={d.get('rule_id') for d in dep.get('dependencies',[])}
for rid in rids:
    if rid not in dep_rules: err(f'base rule missing dependency map: {rid}')
dep_ov={d.get('override_id') for d in dep.get('override_dependencies',[])}
for oid in active_ov:
    if oid not in dep_ov: err(f'active override missing dependency map: {oid}')

# Generator behavior tests: current checkpoint is consumed; old checkpoint changes baseline; invalid checkpoint is blocked.
gen_rel=family_path('build_event_handout_vX.py',fmap.get('build_event_handout_vX.py','build_event_handout_v005.py'))
gentext=(root/gen_rel).read_text(encoding='utf-8') if exists(gen_rel) else ''
for stale in ['TECH_INDEX_v003.json','WARSTART_STATE_LEDGER_v002.json','WARSTART_DOMAIN_AUDIT_v003.json']:
    if stale in gentext: err(f'current generator contains stale hard-coded baseline: {stale}')
def run_hand(args):
    fd,tmp=tempfile.mkstemp(suffix='.json'); os.close(fd)
    try:
        cp2=subprocess.run([sys.executable,str(root/gen_rel),*args,'--out',tmp],capture_output=True,text=True,timeout=30)
        if cp2.returncode!=0: err(f"generator failed {' '.join(args)}: {cp2.stderr.strip()}"); return {}
        return json.loads(pathlib.Path(tmp).read_text(encoding='utf-8'))
    finally:
        try: os.unlink(tmp)
        except OSError: pass
cur=run_hand(['FORAGER_GATE','--date','1944-05-01'])
if cur:
    if cur.get('checkpoint')!=current: err('generator default did not use current restart')
    if cur.get('technical_baseline')!=cp.get('technical_baseline'): err('generator did not consume checkpoint TECH baseline')
    if cur.get('event_profile_revision')!='v003' or cur.get('domain_map_revision')!='v002': err('generator did not consume current profile/domain-map revisions')
    if cur.get('execution_blocked'): err(f"current FORAGER_GATE is blocked: {cur.get('block_reasons')}")
    for eid in ['TECH-AIR-COMBAT-MISSION-MATRIX-1944-001','TECH-ASW-MAD-DATUM-LOCALIZATION-1943-44-001','TECH-I400-SEIRAN-INTEGRATED-READINESS-1944-001']:
        rec=next((e for e in cur.get('entries',[]) if e.get('id')==eid),None)
        if not rec or rec.get('date_gate_state')!='ACTIVE_OR_CONDITIONAL': err(f'current FORAGER handout missing/incorrect gated tech: {eid}')
old=run_hand(['CARRIER_BATTLE','--date','1942-05-12','--checkpoint','CHECKPOINT_1942-05-11T24_v001'])
if old:
    if old.get('checkpoint')!='CHECKPOINT_1942-05-11T24_v001' or old.get('technical_baseline')!='TECH_INDEX_v003': err('generator checkpoint override did not materially change consumed baseline')
    if old.get('technical_baseline')==cur.get('technical_baseline') and old.get('state_sources')==cur.get('state_sources'): err('generator checkpoint override appears label-only')
invalid=run_hand(['CARRIER_BATTLE','--date','1942-05-07','--checkpoint','CHECKPOINT_1942-05-06T24_v001'])
if invalid and not invalid.get('execution_blocked'): err('generator failed to block graph-invalid checkpoint')
industrial=run_hand(['INDUSTRIAL_AIRCRAFT','--date','1944-05-01'])
if industrial:
    rec=next((e for e in industrial.get('entries',[]) if e.get('id')=='TECH-NICKEL-SELECTIVE-HOTTEMP-1943-44-001'),None)
    if not rec or rec.get('date_gate_state')!='ACTIVE_OR_CONDITIONAL': err('industrial profile does not surface current nickel/materials TECH')

# Coverage audit.
cov_rel=family_path('TECH_COVERAGE_AUDIT_vX.json',fmap.get('TECH_COVERAGE_AUDIT_vX.json','TECH_COVERAGE_AUDIT_v003.json')); cov=load(str(cov_rel))
if cov.get('result')!='PASS': err('current TECH coverage audit not PASS')
if cov.get('tech_index')!='TECH_INDEX_v006' or cov.get('profiles')!='EVENT_RELEVANCE_PROFILES_v003': err('coverage audit is stale')
if cov.get('test_count',0)<11: err('coverage audit does not include repaired/current profiles')

# Closeout and current docs.
close=load('95_AUDIT/1943_1944Q1_ADVANCE_CLOSEOUT_v002.json')
if close.get('status')!='PASS_VALIDATED_EXECUTION_REPAIRED': err('1943-44Q1 closeout not updated to validated repaired status')
readme=(root/'00_README/README_refactor_v009.md').read_text(encoding='utf-8') if exists('00_README/README_refactor_v009.md') else ''
for token in ['CHECKPOINT_1944-04-30T24_v002','TECH_INDEX_v006','MATERIALS_NICKEL_TURBO_JET_1944SPRING_v001.md','build_event_handout_v005.py']:
    if token not in readme: err(f'current README missing entrypoint/reference: {token}')
handoff=(root/'00_README/NEXT_SESSION_HANDOFF_REFACTOR_v009.md').read_text(encoding='utf-8') if exists('00_README/NEXT_SESSION_HANDOFF_REFACTOR_v009.md') else ''
for token in ['CHECKPOINT_1944-04-30T24_v002','FORAGER_GATE','TECH_INDEX_v006']:
    if token not in handoff: err(f'current handoff missing execution reference: {token}')

# Current manifest and checksum, if present (mandatory current-family targets above will report missing).
manifest_path=family_path('PACKAGE_MANIFEST_vX.json',fmap.get('PACKAGE_MANIFEST_vX.json','PACKAGE_MANIFEST_v009.json'))
manifest=load(str(manifest_path)) if exists(manifest_path) else {}
if manifest:
    if manifest.get('package_root')!=root.name: err(f"manifest package_root mismatch: {manifest.get('package_root')} != {root.name}")
    actual_count=sum(1 for p in root.rglob('*') if p.is_file())
    if manifest.get('file_count')!=actual_count: err(f"manifest file_count {manifest.get('file_count')} != actual {actual_count}")
    for rel in manifest.get('new_revision_entrypoints',[]):
        if not exists(rel): err(f'manifest entrypoint missing: {rel}')
    if manifest.get('current_restart')!=current: err('manifest current_restart mismatch')
    if manifest.get('validation')!='95_AUDIT/VALIDATION_RESULT_v009.json': err('manifest validation pointer mismatch')
    if manifest.get('checksum')!='95_AUDIT/SHA256SUMS_REFACTOR_v009.txt': err('manifest checksum pointer mismatch')
checksum_rel=pathlib.Path('95_AUDIT/SHA256SUMS_REFACTOR_v009.txt')
if exists(checksum_rel):
    listed={}
    for line in (root/checksum_rel).read_text(encoding='utf-8').splitlines():
        if not line.strip(): continue
        m=re.match(r'^([0-9a-f]{64})  (.+)$',line)
        if not m: err(f'bad checksum line: {line[:80]}'); continue
        listed[m.group(2)]=m.group(1)
    allrels={str(p.relative_to(root)) for p in root.rglob('*') if p.is_file() and p.relative_to(root)!=checksum_rel}
    if set(listed)!=allrels:
        miss=sorted(allrels-set(listed)); extra=sorted(set(listed)-allrels)
        if miss: err(f'checksum missing files: {miss[:10]}')
        if extra: err(f'checksum extra files: {extra[:10]}')
    for rel,h in listed.items():
        p=root/rel
        if p.exists():
            got=hashlib.sha256(p.read_bytes()).hexdigest()
            if got!=h: err(f'checksum mismatch: {rel}')

if not (root/'99_LEGACY_UNTOUCHED').is_dir(): err('legacy subtree missing')
print(f'ERRORS={len(errs)} WARNINGS={len(warns)}')
for x in errs: print('ERROR',x)
for x in warns: print('WARN',x)
sys.exit(1 if errs else 0)
