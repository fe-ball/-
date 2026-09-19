#!/usr/bin/env python3
import os,sys,json,hashlib,re,subprocess,tempfile,pathlib
args=sys.argv[1:]; preflight='--preflight' in args; args=[x for x in args if x!='--preflight']; root=pathlib.Path(args[0] if args else pathlib.Path(__file__).resolve().parents[1]).resolve(); errs=[]; warns=[]
def err(x):errs.append(x)
def warn(x):warns.append(x)
def load(rel):
    try:return json.loads((root/rel).read_text(encoding='utf-8'))
    except Exception as e:err(f'cannot load {rel}: {e}');return {}
def exists(rel):return (root/rel).exists()
def family_path(fam,current):
    if fam.startswith(('README_refactor','NEXT_SESSION_HANDOFF')):return pathlib.Path('00_README')/current
    if fam.startswith(('CHECKPOINT_','RULE_DEPENDENCY_MAP')):return pathlib.Path('05_WARTIME')/current
    if fam.startswith('TECH_INDEX'):return pathlib.Path('02_TECH')/current
    if fam.startswith('PREWAR_INDEX'):return pathlib.Path('03_PREWAR')/current
    if fam.startswith('WARSTART_'):return pathlib.Path('04_WARSTART')/current
    if fam.startswith(('current_branch_overrides','DOMAIN_STATE_MAP','rule_override_protocol')):return pathlib.Path('00_CONFIG')/current
    if fam.startswith(('TECH_COVERAGE_AUDIT','COMBAT_CAPABILITY_COVERAGE_AUDIT','WEAPON_PLATFORM_COVERAGE_AUDIT','PACKAGE_MANIFEST','VALIDATION_RESULT')):return pathlib.Path('95_AUDIT')/current
    if fam.startswith(('EVENT_RELEVANCE_PROFILES','EVENT_HANDOUT_SCHEMA','RUNTIME_CONTRACT','COMBAT_','WEAPON_PLATFORM_','NOVEL_WEAPON_')):return pathlib.Path('06_RUNTIME')/current
    if fam.startswith(('build_event_handout','build_combat_context','validate_refactor')):return pathlib.Path('98_TOOLS')/current
    return pathlib.Path(current)
# All JSON parse.
for p in root.rglob('*.json'):
    try:json.loads(p.read_text(encoding='utf-8'))
    except Exception as e:err(f'json parse {p.relative_to(root)}: {e}')
reg=load('95_AUDIT/current_version_families_v008.json'); fmap={x.get('family'):x.get('current') for x in reg.get('families',[])}
required=['README_refactor_vX.md','NEXT_SESSION_HANDOFF_REFACTOR_vX.md','CHECKPOINT_INDEX_vX.json','CHECKPOINT_GRAPH_vX.json','TECH_INDEX_vX.json','PREWAR_INDEX_vX.json','WARSTART_CHECKPOINT_vX.json','WARSTART_STATE_LEDGER_vX.json','WARSTART_DOMAIN_AUDIT_vX.json','current_branch_overrides_vX.json','DOMAIN_STATE_MAP_vX.json','rule_override_protocol_vX.json','RULE_DEPENDENCY_MAP_vX.json','EVENT_RELEVANCE_PROFILES_vX.json','EVENT_HANDOUT_SCHEMA_vX.json','RUNTIME_CONTRACT_vX.json','build_event_handout_vX.py','build_combat_context_vX.py','validate_refactor_vX.py','TECH_COVERAGE_AUDIT_vX.json','COMBAT_CAPABILITY_FACTOR_INDEX_vX.json','COMBAT_EVENT_FACTOR_MATRIX_vX.json','COMBAT_EVENT_INPUT_SCHEMA_vX.json','COMBAT_ADJUDICATION_CONTEXT_vX.md','COMBAT_CAPABILITY_COVERAGE_AUDIT_vX.json','WEAPON_PLATFORM_CAPABILITY_INDEX_vX.json','COMBAT_PLATFORM_MATRIX_vX.json','NOVEL_WEAPON_ADJUDICATION_POLICY_vX.json','WEAPON_PLATFORM_COVERAGE_AUDIT_vX.json','PACKAGE_MANIFEST_vX.json','VALIDATION_RESULT_vX.json']
for fam in required:
    if fam not in fmap:err(f'current family missing: {fam}')
    elif preflight and fam in ('PACKAGE_MANIFEST_vX.json','VALIDATION_RESULT_vX.json'):pass
    elif not exists(family_path(fam,fmap[fam])):err(f'current family target missing: {fam} -> {family_path(fam,fmap[fam])}')
# TECH source validity.
tech=load('02_TECH/TECH_INDEX_v006.json'); tids={e.get('id') for e in tech.get('entries',[])}
for e in tech.get('entries',[]):
    for s in e.get('sources',[]):
        if not exists(s.get('path','')):err(f"missing TECH source {e.get('id')}: {s.get('path')}")
# Current checkpoint chain.
idx=load('05_WARTIME/CHECKPOINT_INDEX_v010.json'); current=idx.get('current_restart'); cp=load('05_WARTIME/'+current+'.json')
if current!='CHECKPOINT_1944-04-30T24_v004':err('current restart is not v004 platform/novel revalidation')
if cp.get('technical_baseline')!='TECH_INDEX_v006':err('current TECH baseline mismatch')
if not cp.get('execution_valid'):err('current checkpoint execution_valid false')
sup=cp.get('combat_resolution_support') or {}
for k in ['factor_index','event_factor_matrix','event_input_schema','adjudication_context','weapon_platform_index','platform_matrix','novel_weapon_policy']:
    if not sup.get(k):err(f'current checkpoint combat_resolution_support missing {k}')
    elif not exists(sup[k]):err(f'combat support target missing {k}: {sup[k]}')
graph=load('05_WARTIME/CHECKPOINT_GRAPH_v009.json'); cn=next((n for n in graph.get('nodes',[]) if n.get('id')==current),None)
if not cn or not cn.get('execution_valid'):err('current v004 node missing/execution-invalid')
v3=next((n for n in graph.get('nodes',[]) if n.get('id')=='CHECKPOINT_1944-04-30T24_v003'),None)
if not v3 or v3.get('execution_valid') or v3.get('superseded_by')!=current:err('v003 supersession not represented')
# Combat factor layer.
fi=load('06_RUNTIME/COMBAT_CAPABILITY_FACTOR_INDEX_v001.json'); mx=load('06_RUNTIME/COMBAT_EVENT_FACTOR_MATRIX_v001.json'); profiles=load('06_RUNTIME/EVENT_RELEVANCE_PROFILES_v003.json')
factors=fi.get('factors',[]); fids=[f.get('id') for f in factors]; fset=set(fids)
if len(fids)!=len(fset):err('duplicate combat factor ids')
if len(fids)<20:err('combat factor index unexpectedly small')
for pname in profiles.get('profiles',{}):
    if pname not in mx.get('profiles',{}):err(f'combat factor matrix missing profile: {pname}');continue
    s=mx['profiles'][pname]
    for fid in s.get('mandatory_factors',[])+s.get('conditional_factors',[])+s.get('runtime_required_factors',[]):
        if fid not in fset:err(f'profile {pname} references missing combat factor {fid}')
    if not set(s.get('runtime_required_factors',[])).issubset(set(s.get('mandatory_factors',[]))):err(f'profile {pname} runtime-required factor is not mandatory')
ca=load('95_AUDIT/COMBAT_CAPABILITY_COVERAGE_AUDIT_v001.json')
if ca.get('result')!='PASS' or ca.get('profile_count')!=len(profiles.get('profiles',{})):err('combat capability coverage audit not current PASS')
# Platform/novel layer.
wp=load('06_RUNTIME/WEAPON_PLATFORM_CAPABILITY_INDEX_v001.json'); pm=load('06_RUNTIME/COMBAT_PLATFORM_MATRIX_v001.json'); np=load('06_RUNTIME/NOVEL_WEAPON_ADJUDICATION_POLICY_v001.json')
classes=wp.get('platform_classes',[]); cids=[x.get('id') for x in classes]; cset=set(cids)
if len(cids)!=len(cset):err('duplicate platform class ids')
for need in ['SUBMARINE','SURFACE_COMBATANT','AIRCRAFT','CARRIER','SPECIAL_NOVEL_SYSTEM']:
    if need not in cset:err(f'platform class missing: {need}')
for c in classes:
    for k in ['id','label','tech_domains','capability_dimensions','anti_underestimate_rules','source_paths']:
        if k not in c:err(f"platform class {c.get('id')} missing {k}")
    for rel in c.get('source_paths',[]):
        if rel and not exists(rel):err(f"platform class source missing {c.get('id')}: {rel}")
sids=[]
for s in wp.get('systems',[]):
    if not s.get('id') or s.get('id') in sids:err(f"duplicate/missing weapon system id {s.get('id')}")
    sids.append(s.get('id'))
    if s.get('historical_relation') not in wp.get('historical_relation_values',[]):err(f"bad historical relation {s.get('id')}: {s.get('historical_relation')}")
    for tid in s.get('linked_tech_ids',[]):
        if tid not in tids:err(f"weapon system {s.get('id')} references missing TECH {tid}")
    for so in s.get('sources',[]):
        if not exists(so.get('path','')):err(f"weapon system source missing {s.get('id')}: {so.get('path')}")
for pname in profiles.get('profiles',{}):
    if pname not in pm.get('profiles',{}):err(f'platform matrix missing profile: {pname}');continue
    spec=pm['profiles'][pname]
    for cid in spec.get('mandatory_classes',[])+spec.get('conditional_classes',[]):
        if cid not in cset:err(f'platform matrix {pname} references missing class {cid}')
if 'SUBMARINE' not in pm.get('profiles',{}).get('SUBMARINE',{}).get('mandatory_classes',[]):err('SUBMARINE profile does not force submarine capability review')
if 'SURFACE_COMBATANT' not in pm.get('profiles',{}).get('SURFACE_NIGHT',{}).get('mandatory_classes',[]):err('SURFACE_NIGHT profile does not force surface capability review')
fg=set(pm.get('profiles',{}).get('FORAGER_GATE',{}).get('mandatory_classes',[]))
if not {'SUBMARINE','SURFACE_COMBATANT'}.issubset(fg):err('FORAGER_GATE does not force both submarine and surface combatant review')
wa=load('95_AUDIT/WEAPON_PLATFORM_COVERAGE_AUDIT_v001.json')
if wa.get('result')!='PASS' or wa.get('profile_count')!=len(profiles.get('profiles',{})):err('weapon platform coverage audit not current PASS')
if not np.get('minimum_runtime_fields_for_unindexed_novel_system'):err('novel weapon policy missing minimum fields')
# Generator behavior.
gen='98_TOOLS/build_event_handout_v007.py'; gent=(root/gen).read_text(encoding='utf-8') if exists(gen) else ''
for token in ['platform_capability_resolution','novel_weapon_review','weapon_capability_ready','WEAPON_PLATFORM_CAPABILITY_INDEX_vX.json','--combat-input']:
    if token not in gent:err(f'generator missing platform/novel implementation token: {token}')
def run_hand(argv):
    fd,tmp=tempfile.mkstemp(suffix='.json');os.close(fd)
    try:
        p=subprocess.run([sys.executable,str(root/gen),*argv,'--out',tmp],capture_output=True,text=True,timeout=30)
        if p.returncode:err('generator failed '+' '.join(argv)+': '+p.stderr.strip());return {}
        return json.loads(pathlib.Path(tmp).read_text(encoding='utf-8'))
    finally:
        try:os.unlink(tmp)
        except OSError:pass
h=run_hand(['FORAGER_GATE','--date','1944-05-01'])
if h:
    if h.get('checkpoint')!=current:err('generator default not current v004')
    if h.get('schema')!='EVENT_HANDOUT_SCHEMA_v004':err('generator schema not v004')
    if h.get('execution_blocked'):err(f"FORAGER structural execution blocked: {h.get('block_reasons')}")
    if h.get('weapon_capability_ready') is not True:err(f"FORAGER weapon/platform layer unexpectedly unready: {h.get('weapon_ready_block_reasons')}")
    pcls={x.get('platform_class') for x in h.get('platform_capability_resolution',[]) if x.get('mandatory')}
    if not {'SUBMARINE','SURFACE_COMBATANT'}.issubset(pcls):err('FORAGER output omitted mandatory submarine/surface platform review')
    sub=next((x for x in h.get('platform_capability_resolution',[]) if x.get('platform_class')=='SUBMARINE'),{})
    surf=next((x for x in h.get('platform_capability_resolution',[]) if x.get('platform_class')=='SURFACE_COMBATANT'),{})
    if 'TECH-SUB-KOU-FIRSTGEN-001' not in sub.get('active_tech_entry_ids',[]):err('FORAGER platform review failed to surface 潜高 TECH')
    if 'TECH-TORPEDO-SECOND-SALVO-001' not in surf.get('active_tech_entry_ids',[]):err('FORAGER platform review failed to surface second-salvo TECH')
    novel_ids={x.get('id') for x in h.get('novel_weapon_review',[]) if x.get('source')=='INDEX'}
    for sid in ['SYS-JP-KOU-FIRSTGEN','SYS-JP-SURFACE-SECOND-SALVO','SYS-JP-I400-SEIRAN-INTEGRATED']:
        if sid not in novel_ids:err(f'FORAGER novel review omitted {sid}')
# All factor runtime values -> ready, because indexed platform layer itself should not require invented local new weapon records.
if h:
    data={'factors':{fid:{'value':'validator event-local value'} for fid in mx['profiles']['FORAGER_GATE']['runtime_required_factors']}}
    fd,inp=tempfile.mkstemp(suffix='.json');os.close(fd);pathlib.Path(inp).write_text(json.dumps(data),encoding='utf-8')
    try:h2=run_hand(['FORAGER_GATE','--date','1944-05-01','--combat-input',inp])
    finally:os.unlink(inp)
    if h2 and not h2.get('combat_resolution_ready'):err(f"FORAGER not ready after factor inputs: {h2.get('combat_ready_block_reasons')}")
# Unindexed novel system must block until capability/readiness/provenance supplied.
if h:
    factors={fid:{'value':'validator event-local value'} for fid in mx['profiles']['FORAGER_GATE']['runtime_required_factors']}
    bad={'factors':factors,'weapon_systems':[{'designation':'Validator ahistorical weapon','platform_class':'SURFACE_COMBATANT','historical_relation':'AHISTORICAL_NEW'}]}
    fd,inp=tempfile.mkstemp(suffix='.json');os.close(fd);pathlib.Path(inp).write_text(json.dumps(bad),encoding='utf-8')
    try:hb=run_hand(['FORAGER_GATE','--date','1944-05-01','--combat-input',inp])
    finally:os.unlink(inp)
    if hb and (hb.get('weapon_capability_ready') or hb.get('combat_resolution_ready')):err('incomplete unindexed ahistorical weapon did not block readiness')
    good={'factors':factors,'weapon_systems':[{'designation':'Validator ahistorical weapon','platform_class':'SURFACE_COMBATANT','historical_relation':'AHISTORICAL_NEW','capability_record':{'speed':'test band','weapons':'test band'},'availability_or_readiness':{'ready':1},'source':'validator synthetic'}]}
    fd,inp=tempfile.mkstemp(suffix='.json');os.close(fd);pathlib.Path(inp).write_text(json.dumps(good),encoding='utf-8')
    try:hg=run_hand(['FORAGER_GATE','--date','1944-05-01','--combat-input',inp])
    finally:os.unlink(inp)
    if hg and not hg.get('combat_resolution_ready'):err(f"complete unindexed ahistorical weapon remains blocked: {hg.get('combat_ready_block_reasons')}")
# Every profile emits all mandatory factor and platform classes.
for pname in profiles.get('profiles',{}):
    hh=run_hand([pname,'--date','1944-05-01'])
    if hh:
        got={x.get('factor_id') for x in hh.get('combat_factor_resolution',[]) if x.get('mandatory')}; exp=set(mx['profiles'][pname]['mandatory_factors'])
        if got!=exp:err(f'{pname} mandatory factor emission mismatch')
        gotc={x.get('platform_class') for x in hh.get('platform_capability_resolution',[]) if x.get('mandatory')}; expc=set(pm['profiles'][pname]['mandatory_classes'])
        if gotc!=expc:err(f'{pname} mandatory platform emission mismatch missing={sorted(expc-gotc)} extra={sorted(gotc-expc)}')
# Entrypoint docs.
readme=(root/'00_README/README_refactor_v011.md').read_text(encoding='utf-8') if exists('00_README/README_refactor_v011.md') else ''
handoff=(root/'00_README/NEXT_SESSION_HANDOFF_REFACTOR_v011.md').read_text(encoding='utf-8') if exists('00_README/NEXT_SESSION_HANDOFF_REFACTOR_v011.md') else ''
for token in ['CHECKPOINT_1944-04-30T24_v004','WEAPON_PLATFORM_CAPABILITY_INDEX_v001','build_event_handout_v007.py','潜水艦','水上戦闘艦']:
    if token not in readme:err(f'README missing {token}')
for token in ['CHECKPOINT_1944-04-30T24_v004','weapon_systems','潜水艦','水上艦']:
    if token not in handoff:err(f'handoff missing {token}')
if not (root/'99_LEGACY_UNTOUCHED').is_dir():err('legacy subtree missing')
# Final package checks.
if not preflight:
    manifest=load('95_AUDIT/PACKAGE_MANIFEST_v011.json'); checksum_rel=pathlib.Path('95_AUDIT/SHA256SUMS_REFACTOR_v011.txt')
    if manifest:
        actual=sum(1 for p in root.rglob('*') if p.is_file())
        if manifest.get('package_root')!=root.name:err('manifest package_root mismatch')
        if manifest.get('file_count')!=actual:err(f"manifest file_count {manifest.get('file_count')} != {actual}")
        if manifest.get('current_restart')!=current:err('manifest current restart mismatch')
        for rel in manifest.get('new_revision_entrypoints',[]):
            if not exists(rel):err(f'manifest entrypoint missing: {rel}')
    if not exists(checksum_rel):err('v011 checksum missing')
    else:
        listed={}
        for line in (root/checksum_rel).read_text(encoding='utf-8').splitlines():
            if not line.strip():continue
            m=re.match(r'^([0-9a-f]{64})  (.+)$',line)
            if not m:err('bad checksum line: '+line[:80]);continue
            listed[m.group(2)]=m.group(1)
        allrels={str(p.relative_to(root)) for p in root.rglob('*') if p.is_file() and p.relative_to(root)!=checksum_rel}
        if set(listed)!=allrels:err(f'checksum coverage mismatch missing={sorted(allrels-set(listed))[:8]} extra={sorted(set(listed)-allrels)[:8]}')
        for rel,hv in listed.items():
            if exists(rel) and hashlib.sha256((root/rel).read_bytes()).hexdigest()!=hv:err('checksum mismatch: '+rel)
print(f'ERRORS={len(errs)} WARNINGS={len(warns)}')
for x in errs:print('ERROR',x)
for x in warns:print('WARN',x)
sys.exit(1 if errs else 0)
