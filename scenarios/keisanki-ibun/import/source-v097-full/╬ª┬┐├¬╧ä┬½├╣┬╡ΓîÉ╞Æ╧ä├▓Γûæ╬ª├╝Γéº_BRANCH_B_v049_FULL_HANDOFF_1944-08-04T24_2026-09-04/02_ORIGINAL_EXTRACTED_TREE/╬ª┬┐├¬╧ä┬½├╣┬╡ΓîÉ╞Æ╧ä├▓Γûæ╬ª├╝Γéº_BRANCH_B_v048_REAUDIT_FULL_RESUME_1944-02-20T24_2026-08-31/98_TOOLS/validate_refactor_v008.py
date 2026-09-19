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
    if fam.startswith(('TECH_COVERAGE_AUDIT','COMBAT_CAPABILITY_COVERAGE_AUDIT','PACKAGE_MANIFEST','VALIDATION_RESULT')):return pathlib.Path('95_AUDIT')/current
    if fam.startswith(('EVENT_RELEVANCE_PROFILES','EVENT_HANDOUT_SCHEMA','RUNTIME_CONTRACT','COMBAT_')):return pathlib.Path('06_RUNTIME')/current
    if fam.startswith(('build_event_handout','build_combat_context','validate_refactor')):return pathlib.Path('98_TOOLS')/current
    return pathlib.Path(current)
for p in root.rglob('*.json'):
    try:json.loads(p.read_text(encoding='utf-8'))
    except Exception as e:err(f'json parse {p.relative_to(root)}: {e}')
reg=load('95_AUDIT/current_version_families_v007.json'); fmap={x.get('family'):x.get('current') for x in reg.get('families',[])}
required=['README_refactor_vX.md','NEXT_SESSION_HANDOFF_REFACTOR_vX.md','CHECKPOINT_INDEX_vX.json','CHECKPOINT_GRAPH_vX.json','TECH_INDEX_vX.json','PREWAR_INDEX_vX.json','WARSTART_CHECKPOINT_vX.json','WARSTART_STATE_LEDGER_vX.json','WARSTART_DOMAIN_AUDIT_vX.json','current_branch_overrides_vX.json','DOMAIN_STATE_MAP_vX.json','rule_override_protocol_vX.json','RULE_DEPENDENCY_MAP_vX.json','EVENT_RELEVANCE_PROFILES_vX.json','EVENT_HANDOUT_SCHEMA_vX.json','RUNTIME_CONTRACT_vX.json','build_event_handout_vX.py','build_combat_context_vX.py','validate_refactor_vX.py','TECH_COVERAGE_AUDIT_vX.json','COMBAT_CAPABILITY_FACTOR_INDEX_vX.json','COMBAT_EVENT_FACTOR_MATRIX_vX.json','COMBAT_EVENT_INPUT_SCHEMA_vX.json','COMBAT_ADJUDICATION_CONTEXT_vX.md','COMBAT_CAPABILITY_COVERAGE_AUDIT_vX.json','PACKAGE_MANIFEST_vX.json','VALIDATION_RESULT_vX.json']
for fam in required:
    if fam not in fmap:err(f'current family missing: {fam}')
    elif preflight and fam in ('PACKAGE_MANIFEST_vX.json','VALIDATION_RESULT_vX.json'):pass
    elif not exists(family_path(fam,fmap[fam])):err(f'current family target missing: {fam} -> {family_path(fam,fmap[fam])}')
tech=load('02_TECH/TECH_INDEX_v006.json'); tids={e.get('id') for e in tech.get('entries',[])}
for e in tech.get('entries',[]):
    for s in e.get('sources',[]):
        if not exists(s.get('path','')):err(f"missing TECH source {e.get('id')}: {s.get('path')}")
idx=load('05_WARTIME/CHECKPOINT_INDEX_v009.json'); current=idx.get('current_restart'); cp=load('05_WARTIME/'+current+'.json')
if current!='CHECKPOINT_1944-04-30T24_v003':err('current restart is not v003 combat revalidation')
if cp.get('technical_baseline')!='TECH_INDEX_v006':err('current TECH baseline mismatch')
if not cp.get('execution_valid'):err('current checkpoint execution_valid false')
sup=cp.get('combat_resolution_support') or {}
for k in ['factor_index','event_factor_matrix','event_input_schema','adjudication_context']:
    if not sup.get(k):err(f'current checkpoint combat_resolution_support missing {k}')
    elif not exists(sup[k]):err(f'combat support target missing {k}: {sup[k]}')
graph=load('05_WARTIME/CHECKPOINT_GRAPH_v008.json'); cn=next((n for n in graph.get('nodes',[]) if n.get('id')==current),None)
if not cn or not cn.get('execution_valid'):err('current v003 node missing/execution-invalid')
v2=next((n for n in graph.get('nodes',[]) if n.get('id')=='CHECKPOINT_1944-04-30T24_v002'),None)
if not v2 or v2.get('execution_valid') or v2.get('superseded_by')!=current:err('v002 supersession not represented')
fi=load('06_RUNTIME/COMBAT_CAPABILITY_FACTOR_INDEX_v001.json'); mx=load('06_RUNTIME/COMBAT_EVENT_FACTOR_MATRIX_v001.json'); profiles=load('06_RUNTIME/EVENT_RELEVANCE_PROFILES_v003.json')
factors=fi.get('factors',[]); fids=[f.get('id') for f in factors]; fset=set(fids)
if len(fids)!=len(fset):err('duplicate combat factor ids')
if len(fids)<20:err('combat factor index unexpectedly small')
for f in factors:
    for k in ['id','label','group','question','checkpoint_paths','tech_domains','runtime_keys','source_candidates','unresolved_rule']:
        if k not in f:err(f"combat factor {f.get('id')} missing {k}")
    if not f.get('source_candidates'):err(f"combat factor {f.get('id')} has no discovery source candidates")
for pname in profiles.get('profiles',{}):
    if pname not in mx.get('profiles',{}):err(f'combat factor matrix missing profile: {pname}');continue
    s=mx['profiles'][pname]
    for fid in s.get('mandatory_factors',[])+s.get('conditional_factors',[])+s.get('runtime_required_factors',[]):
        if fid not in fset:err(f'profile {pname} references missing combat factor {fid}')
    if not s.get('mandatory_factors'):err(f'profile {pname} has no mandatory combat factors')
    if not set(s.get('runtime_required_factors',[])).issubset(set(s.get('mandatory_factors',[]))):err(f'profile {pname} runtime-required factor is not mandatory')
ca=load('95_AUDIT/COMBAT_CAPABILITY_COVERAGE_AUDIT_v001.json')
if ca.get('result')!='PASS' or ca.get('profile_count')!=len(profiles.get('profiles',{})):err('combat capability coverage audit not current PASS')
gen='98_TOOLS/build_event_handout_v006.py'; gent=(root/gen).read_text(encoding='utf-8') if exists(gen) else ''
for token in ['combat_resolution_support','combat_factor_resolution','combat_resolution_ready','--combat-input']:
    if token not in gent:err(f'generator missing combat completeness implementation token: {token}')
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
    if h.get('checkpoint')!=current:err('generator default not current v003')
    if h.get('schema')!='EVENT_HANDOUT_SCHEMA_v003':err('generator schema not v003')
    if h.get('execution_blocked'):err(f"FORAGER structural execution blocked: {h.get('block_reasons')}")
    if h.get('combat_resolution_ready'):err('FORAGER without event-local input should not be combat-ready')
    rr={x.get('factor_id'):x for x in h.get('combat_factor_resolution',[])}
    for fid in mx['profiles']['FORAGER_GATE']['mandatory_factors']:
        if fid not in rr:err(f'FORAGER omitted mandatory factor {fid}')
    for fid in mx['profiles']['FORAGER_GATE']['runtime_required_factors']:
        if rr.get(fid,{}).get('resolution')!='RUNTIME_INPUT_REQUIRED':err(f'FORAGER runtime factor not explicitly required without input: {fid}')
# Supply synthetic event-local values for every FORAGER runtime-required factor and require readiness.
if h:
    data={'factors':{fid:{'value':'validator supplied event-local value'} for fid in mx['profiles']['FORAGER_GATE']['runtime_required_factors']}}
    fd,inp=tempfile.mkstemp(suffix='.json');os.close(fd);pathlib.Path(inp).write_text(json.dumps(data),encoding='utf-8')
    try: h2=run_hand(['FORAGER_GATE','--date','1944-05-01','--combat-input',inp])
    finally: os.unlink(inp)
    if h2 and not h2.get('combat_resolution_ready'):err(f"FORAGER remains not combat-ready after all runtime-required inputs supplied: {h2.get('combat_ready_block_reasons')}")
# Every profile must emit every mandatory factor.
for pname in profiles.get('profiles',{}):
    hh=run_hand([pname,'--date','1944-05-01'])
    if hh:
        got={x.get('factor_id') for x in hh.get('combat_factor_resolution',[]) if x.get('mandatory')}
        exp=set(mx['profiles'][pname]['mandatory_factors'])
        if got!=exp:err(f'{pname} mandatory factor emission mismatch missing={sorted(exp-got)} extra={sorted(got-exp)}')
readme=(root/'00_README/README_refactor_v010.md').read_text(encoding='utf-8') if exists('00_README/README_refactor_v010.md') else ''
handoff=(root/'00_README/NEXT_SESSION_HANDOFF_REFACTOR_v010.md').read_text(encoding='utf-8') if exists('00_README/NEXT_SESSION_HANDOFF_REFACTOR_v010.md') else ''
for token in ['CHECKPOINT_1944-04-30T24_v003','COMBAT_CAPABILITY_FACTOR_INDEX_v001','build_event_handout_v006.py']:
    if token not in readme:err(f'README missing {token}')
for token in ['CHECKPOINT_1944-04-30T24_v003','combat_resolution_support','combat_resolution_ready']:
    if token not in handoff:err(f'handoff missing {token}')
# Legacy preservation presence.
if not (root/'99_LEGACY_UNTOUCHED').is_dir():err('legacy subtree missing')
# Final packaging checks skipped during preflight.
if not preflight:
    manifest=load('95_AUDIT/PACKAGE_MANIFEST_v010.json'); checksum_rel=pathlib.Path('95_AUDIT/SHA256SUMS_REFACTOR_v010.txt')
    if manifest:
        actual=sum(1 for p in root.rglob('*') if p.is_file())
        if manifest.get('package_root')!=root.name:err('manifest package_root mismatch')
        if manifest.get('file_count')!=actual:err(f"manifest file_count {manifest.get('file_count')} != {actual}")
        if manifest.get('current_restart')!=current:err('manifest current restart mismatch')
        for rel in manifest.get('new_revision_entrypoints',[]):
            if not exists(rel):err(f'manifest entrypoint missing: {rel}')
    if not exists(checksum_rel):err('v010 checksum missing')
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
