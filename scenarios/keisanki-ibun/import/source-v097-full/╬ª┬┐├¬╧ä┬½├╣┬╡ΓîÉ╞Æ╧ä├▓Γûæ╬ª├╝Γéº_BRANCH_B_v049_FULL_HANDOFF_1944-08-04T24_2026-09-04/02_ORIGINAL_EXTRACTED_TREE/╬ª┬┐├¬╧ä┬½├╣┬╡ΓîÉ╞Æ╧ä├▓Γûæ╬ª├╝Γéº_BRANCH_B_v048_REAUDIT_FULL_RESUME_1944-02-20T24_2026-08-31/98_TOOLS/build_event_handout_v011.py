#!/usr/bin/env python3
import argparse, datetime, json, pathlib, re, sys
ROOT=pathlib.Path(__file__).resolve().parents[1]
def load(rel): return json.loads((ROOT/rel).read_text(encoding='utf-8'))
def latest_family_registry():
    files=list((ROOT/'95_AUDIT').glob('current_version_families_v*.json'))
    def n(p):
        m=re.search(r'_v(\d+)\.json$',p.name); return int(m.group(1)) if m else -1
    return json.loads(max(files,key=n).read_text(encoding='utf-8'))
def family(reg,name):
    for x in reg.get('families',[]):
        if x.get('family')==name:return x['current']
    raise KeyError(f'current-version family missing: {name}')
def iso_date(s): return datetime.date.fromisoformat(s[:10]) if s else None
def inferred_valid_from(text):
    if not text:return None
    low=text.lower()
    if any(k in low for k in ['all dates','prewar','opening','all wartime']):return None
    m=re.search(r'(?<!\d)(19\d{2})(?:-(\d{2})(?:-(\d{2}))?)?',text)
    if not m:return None
    y=int(m.group(1)); mo=int(m.group(2) or 1); day=int(m.group(3) or 1)
    try:return datetime.date(y,mo,day)
    except ValueError:return datetime.date(y,1,1)
def gate_state(e,date):
    if not date:return ('ACTIVE_OR_CONDITIONAL','no_event_date')
    g=e.get('runtime_gate') or {}
    if g.get('available_from'):
        af=iso_date(g['available_from'])
        if date<af:return (g.get('pre_available_state','NOT_YET_MATURE'),f"runtime_gate.available_from={g['available_from']}")
    if g.get('available_to'):
        at=iso_date(g['available_to'])
        if date>at:return ('EXPIRED_OR_REPLACED',f"runtime_gate.available_to={g['available_to']}")
    if g:return ('ACTIVE_OR_CONDITIONAL','runtime_gate')
    inf=inferred_valid_from(e.get('valid_from',''))
    if inf and date<inf:return ('NOT_YET_MATURE',f"inferred_from_valid_from={inf.isoformat()}")
    return ('ACTIVE_OR_CONDITIONAL','valid_from_or_ungated')
def resolve_checkpoint(spec,idx,graph):
    if not spec:spec=idx['current_restart']
    p=pathlib.Path(spec)
    if p.is_absolute() and p.exists():return p,json.loads(p.read_text(encoding='utf-8'))
    rp=ROOT/spec
    if rp.exists():return rp,json.loads(rp.read_text(encoding='utf-8'))
    p=ROOT/'05_WARTIME'/f'{spec}.json'
    if p.exists():return p,json.loads(p.read_text(encoding='utf-8'))
    for n in graph.get('nodes',[]):
        if n.get('id')==spec and n.get('checkpoint_file'):
            p=ROOT/n['checkpoint_file']
            if p.exists():return p,json.loads(p.read_text(encoding='utf-8'))
    raise FileNotFoundError(f'checkpoint not found: {spec}')
def get_path(obj,path):
    cur=obj
    for part in path.split('.'):
        if isinstance(cur,dict) and part in cur:cur=cur[part]
        else:return None
    return cur
def opening_ledger(reg):return load('04_WARSTART/'+family(reg,'WARSTART_STATE_LEDGER_vX.json'))
def state_lookup(ledger,name):
    for d in ledger.get('domains',[]):
        if d.get('domain')==name:return d
    return None
def resolve_state_binding(cp,paths,war_domains,ledger):
    bindings=[]
    for path in paths:
        v=get_path(cp,path)
        if v is not None:bindings.append({'source':'CHECKPOINT_LOCAL','path':path,'value':v})
    if bindings:return ('CHECKPOINT_LOCAL',bindings)
    for d in war_domains:
        x=state_lookup(ledger,d)
        if x:bindings.append({'source':'WARSTART_BASELINE_FALLBACK','domain':d,'state':x.get('state'),'value':x.get('values')})
    return (('WARSTART_BASELINE_FALLBACK' if bindings else 'UNKNOWN'),bindings)
def select(profile,tech):
    tags=set(profile.get('include_tags',[])); mids=set(profile.get('mandatory_entry_ids',[])); mand=set(profile.get('mandatory_domains',[])); also=set(profile.get('also_check',[])); out=[]
    for e in tech.get('entries',[]):
        et=set(e.get('event_tags',[])); exact=bool(et & tags); generic=('ALL' in et and (e['id'] in mids or e['domain']=='CROSS_DOMAIN')); domain_relevant=e['domain'] in mand or e['domain'] in also
        if e['id'] in mids or exact or generic or domain_relevant:out.append(e)
    seen=set(); ans=[]
    for e in sorted(out,key=lambda x:(x['domain'],x['id'])):
        if e['id'] not in seen:ans.append(e); seen.add(e['id'])
    return ans
def load_combat_support(cp,reg):
    sup=cp.get('combat_resolution_support') or {}
    fi=sup.get('factor_index') or ('06_RUNTIME/'+family(reg,'COMBAT_CAPABILITY_FACTOR_INDEX_vX.json'))
    mx=sup.get('event_factor_matrix') or ('06_RUNTIME/'+family(reg,'COMBAT_EVENT_FACTOR_MATRIX_vX.json'))
    ctx=sup.get('adjudication_context') or ('06_RUNTIME/'+family(reg,'COMBAT_ADJUDICATION_CONTEXT_vX.md'))
    inp=sup.get('event_input_schema') or ('06_RUNTIME/'+family(reg,'COMBAT_EVENT_INPUT_SCHEMA_vX.json'))
    wi=sup.get('weapon_platform_index') or ('06_RUNTIME/'+family(reg,'WEAPON_PLATFORM_CAPABILITY_INDEX_vX.json'))
    pm=sup.get('platform_matrix') or ('06_RUNTIME/'+family(reg,'COMBAT_PLATFORM_MATRIX_vX.json'))
    np=sup.get('novel_weapon_policy') or ('06_RUNTIME/'+family(reg,'NOVEL_WEAPON_ADJUDICATION_POLICY_vX.json'))
    return sup,fi,load(fi),mx,load(mx),ctx,inp,wi,load(wi),pm,load(pm),np
def resolve_combat_factors(profile_name,cp,selected,gate_by_id,fi,matrix,event_input):
    fby={f['id']:f for f in fi.get('factors',[])}; spec=matrix.get('profiles',{}).get(profile_name)
    if spec is None:return [],False,[f'combat factor matrix profile missing: {profile_name}']
    mandatory=set(spec.get('mandatory_factors',[])); conditional=set(spec.get('conditional_factors',[])); runtime_req=set(spec.get('runtime_required_factors',[])); wanted=list(spec.get('mandatory_factors',[]))+[x for x in spec.get('conditional_factors',[]) if x not in mandatory]
    evf=(event_input or {}).get('factors',{}) if isinstance(event_input,dict) else {}
    results=[]; blockers=[]
    for fid in wanted:
        f=fby.get(fid)
        if not f:
            results.append({'factor_id':fid,'mandatory':fid in mandatory,'resolution':'UNKNOWN','reason':'factor definition missing'}); blockers.append(f'mandatory factor definition missing: {fid}'); continue
        evidence=[]
        for path in f.get('checkpoint_paths',[]):
            v=get_path(cp,path)
            if v is not None:evidence.append({'source':'CHECKPOINT_LOCAL','path':path,'value':v})
        te=[e['id'] for e in selected if e.get('domain') in set(f.get('tech_domains',[])) and gate_by_id.get(e['id'])=='ACTIVE_OR_CONDITIONAL']
        if te:evidence.append({'source':'TECH_ENTRIES','entry_ids':te})
        cpsrc=set(cp.get('state_sources',[]))
        sc=[x for x in f.get('source_candidates',[]) if x.get('path') in cpsrc]
        if sc:evidence.append({'source':'CHECKPOINT_STATE_SOURCE_POINTERS','paths':[x['path'] for x in sc[:6]]})
        rin=evf.get(fid)
        has_runtime=rin is not None
        if has_runtime and evidence:resolution='RUNTIME_AND_ARCHIVE_EVIDENCE'
        elif has_runtime:resolution='RUNTIME_INPUT'
        elif fid in runtime_req:resolution='RUNTIME_INPUT_REQUIRED'
        elif evidence:
            kinds={x['source'] for x in evidence}; resolution='MIXED_EVIDENCE' if len(kinds)>1 else ('TECH_EVIDENCE' if 'TECH_ENTRIES' in kinds else 'CHECKPOINT_EVIDENCE')
        else:resolution='UNKNOWN'
        rec={'factor_id':fid,'label':f.get('label'),'group':f.get('group'),'mandatory':fid in mandatory,'runtime_required':fid in runtime_req,'assessment':f.get('assessment'),'question':f.get('question'),'resolution':resolution,'runtime_input_keys':f.get('runtime_keys',[]),'evidence':evidence}
        if has_runtime:rec['runtime_input']=rin
        results.append(rec)
        if fid in mandatory and resolution in ('UNKNOWN','RUNTIME_INPUT_REQUIRED'):
            blockers.append(f'{fid} {resolution}: {f.get("label")}')
    return results,(len(blockers)==0),blockers

def resolve_platform_capabilities(profile_name,cp,tech,date,wp,pm,event_input):
    classes={x.get('id'):x for x in wp.get('platform_classes',[])}
    spec=pm.get('profiles',{}).get(profile_name)
    if spec is None:return [],[],False,[f'combat platform matrix profile missing: {profile_name}']
    mandatory=set(spec.get('mandatory_classes',[])); wanted=list(spec.get('mandatory_classes',[]))+[x for x in spec.get('conditional_classes',[]) if x not in mandatory]
    tech_by_id={e.get('id'):e for e in tech.get('entries',[])}
    active_by_domain={}
    for e in tech.get('entries',[]):
        gs,_=gate_state(e,date)
        if gs=='ACTIVE_OR_CONDITIONAL':active_by_domain.setdefault(e.get('domain'),[]).append(e.get('id'))
    results=[]; blockers=[]
    for cid in wanted:
        c=classes.get(cid)
        if not c:
            results.append({'platform_class':cid,'mandatory':cid in mandatory,'resolution':'UNKNOWN','reason':'platform class definition missing'})
            if cid in mandatory:blockers.append(f'mandatory platform class definition missing: {cid}')
            continue
        tids=[]
        for d in c.get('tech_domains',[]):tids.extend(active_by_domain.get(d,[]))
        tids=sorted(set(x for x in tids if x))
        systems=[]
        for sysrec in wp.get('systems',[]):
            if cid not in sysrec.get('platform_classes',[]):continue
            if profile_name not in sysrec.get('event_profiles',[]) and 'ALL' not in sysrec.get('event_profiles',[]):continue
            linked=sysrec.get('linked_tech_ids',[])
            linked_active=[tid for tid in linked if tid in tech_by_id and gate_state(tech_by_id[tid],date)[0]=='ACTIVE_OR_CONDITIONAL']
            if linked and not linked_active:continue
            state='TECH_ACTIVE_CANDIDATE' if linked_active else 'DISCOVERY_ONLY_REQUIRES_PRESENCE_CONFIRMATION'
            systems.append({'id':sysrec.get('id'),'designation':sysrec.get('designation'),'historical_relation':sysrec.get('historical_relation'),'state':state,'linked_active_tech_ids':linked_active,'rule':sysrec.get('rule')})
        results.append({'platform_class':cid,'label':c.get('label'),'mandatory':cid in mandatory,'resolution':'CAPABILITY_INDEXED','capability_dimensions':c.get('capability_dimensions',[]),'anti_underestimate_rules':c.get('anti_underestimate_rules',[]),'strength_anchors':c.get('strength_anchors',[]),'active_tech_entry_ids':tids,'indexed_system_candidates':systems,'presence_rule':'Candidate capability only; match to actual participants/configuration before application.'})
    # Known branch-specific systems are surfaced even if the normal TECH event tag path would omit them.
    novel=[]
    for sysrec in wp.get('systems',[]):
        if sysrec.get('historical_relation')=='HISTORICAL_BASELINE':continue
        if profile_name not in sysrec.get('event_profiles',[]) and 'ALL' not in sysrec.get('event_profiles',[]):continue
        linked=sysrec.get('linked_tech_ids',[])
        linked_active=[tid for tid in linked if tid in tech_by_id and gate_state(tech_by_id[tid],date)[0]=='ACTIVE_OR_CONDITIONAL']
        if linked and not linked_active:continue
        novel.append({'source':'INDEX','id':sysrec.get('id'),'designation':sysrec.get('designation'),'historical_relation':sysrec.get('historical_relation'),'review_state':('ACTIVE_CAPABILITY_CANDIDATE' if linked_active else 'DISCOVERY_ONLY_REQUIRES_PRESENCE_CONFIRMATION'),'linked_active_tech_ids':linked_active,'rule':sysrec.get('rule'),'historical_baseline_substitution_forbidden':True})
    known={x.get('id'):x for x in wp.get('systems',[])}
    known_name={x.get('designation'):x for x in wp.get('systems',[])}
    runtime=(event_input or {}).get('weapon_systems',[]) if isinstance(event_input,dict) else []
    if runtime is None:runtime=[]
    if not isinstance(runtime,list):
        blockers.append('weapon_systems must be a list');runtime=[]
    special={'AHISTORICAL_NEW','AHISTORICAL_TIMING','DIVERGENT_VARIANT','UNKNOWN'}
    for i,r in enumerate(runtime):
        if not isinstance(r,dict):blockers.append(f'weapon_systems[{i}] is not an object');continue
        idxrec=known.get(r.get('index_id')) or known_name.get(r.get('designation'))
        rel=r.get('historical_relation') or (idxrec or {}).get('historical_relation') or 'UNKNOWN'
        cid=r.get('platform_class')
        if cid and cid not in classes:blockers.append(f'weapon_systems[{i}] unknown platform_class: {cid}')
        missing=[]
        if rel in special:
            if idxrec:
                if not r.get('availability_or_readiness'):missing.append('availability_or_readiness')
            else:
                for k in ['designation','platform_class','capability_record','availability_or_readiness','source']:
                    if not r.get(k):missing.append(k)
        rec={'source':'RUNTIME','index_id':(idxrec or {}).get('id'),'designation':r.get('designation') or (idxrec or {}).get('designation'),'platform_class':cid,'historical_relation':rel,'indexed':bool(idxrec),'capability_record':r.get('capability_record'),'availability_or_readiness':r.get('availability_or_readiness'),'provenance':r.get('source'),'historical_baseline_substitution_forbidden':rel in special,'resolution':('RUNTIME_CAPABILITY_RESOLVED' if not missing else 'RUNTIME_CAPABILITY_INCOMPLETE')}
        novel.append(rec)
        if missing:blockers.append(f"novel/divergent weapon incomplete {rec.get('designation') or i}: missing {', '.join(missing)}")
    return results,novel,(len(blockers)==0),blockers

def main():
    reg=latest_family_registry(); idx=load('05_WARTIME/'+family(reg,'CHECKPOINT_INDEX_vX.json')); graph=load('05_WARTIME/'+family(reg,'CHECKPOINT_GRAPH_vX.json')); prof=load('06_RUNTIME/'+family(reg,'EVENT_RELEVANCE_PROFILES_vX.json')); dmap=load('00_CONFIG/'+family(reg,'DOMAIN_STATE_MAP_vX.json')); contract='06_RUNTIME/'+family(reg,'RUNTIME_CONTRACT_vX.json')
    ap=argparse.ArgumentParser(); ap.add_argument('profile',choices=sorted(prof['profiles'])); ap.add_argument('--date'); ap.add_argument('--checkpoint'); ap.add_argument('--combat-input'); ap.add_argument('--out'); a=ap.parse_args()
    cp_path,cp=resolve_checkpoint(a.checkpoint,idx,graph)
    if not a.checkpoint and (cp.get('checkpoint_id') or cp.get('id'))!=idx.get('current_restart'): raise SystemExit('current registry/index did not resolve to indexed current restart')
    cp_id=cp.get('checkpoint_id') or cp.get('id') or (a.checkpoint or idx['current_restart']); graph_node=next((n for n in graph.get('nodes',[]) if n.get('id')==cp_id),None); graph_execution_valid=(graph_node.get('execution_valid') if graph_node is not None else cp.get('execution_valid',True))
    baseline=cp.get('technical_baseline');
    if not baseline:raise SystemExit('selected checkpoint has no technical_baseline')
    tech=load('02_TECH/'+baseline+'.json'); profile=prof['profiles'][a.profile]; date=iso_date(a.date or cp.get('as_of')); ledger=opening_ledger(reg); selected=select(profile,tech); cp_declared=set(cp.get('technical_entries',[])); entries=[]; gate_by_id={}
    for e in selected:
        gs,basis=gate_state(e,date); gate_by_id[e['id']]=gs; rec={'id':e['id'],'domain':e['domain'],'status':e.get('status'),'date_gate_state':gs,'date_gate_basis':basis,'valid_from':e.get('valid_from'),'checkpoint_declared':e['id'] in cp_declared,'causal_stage':e.get('causal_stage',[]),'what_changed':e.get('what_changed'),'sources':e.get('sources',[])}
        if gs=='ACTIVE_OR_CONDITIONAL':
            for k in ['magnitude','combat_meaning','nonlinear_effect','do_not_simplify_as']:
                if k in e:rec[k]=e[k]
        else:rec['warning']='Indexed for relevance but not mature/active on this event date; do not back-port.'
        entries.append(rec)
    domain_results=[]; block=[]
    if graph_execution_valid is False:block.append(f'selected checkpoint is not execution-valid in current graph: {cp_id}')
    cp_date=iso_date(cp.get('as_of'))
    if date and cp_date and date<cp_date:block.append(f'event date {date.isoformat()} precedes checkpoint state date {cp_date.isoformat()}')
    for dom in profile.get('mandatory_domains',[]):
        des=[e for e in selected if e['domain']==dom]; gates=[gate_by_id[e['id']] for e in des]
        if not des:resolution='UNKNOWN'
        elif any(g=='ACTIVE_OR_CONDITIONAL' for g in gates):resolution='ACTIVE'
        elif all(g in ('NOT_YET_MATURE','PRECURSOR_TRIAL','PRODUCTION_TRANSITION','UNDER_CONSTRUCTION_OR_WORKUP','PREWAR_COMSEC_PRESENT_OUTCOME_NOT_THIS_1942_CARD') for g in gates):resolution='NOT_YET_MATURE'
        else:resolution='NO_RELEVANT_DELTA'
        state_source,bindings=resolve_state_binding(cp,dmap.get('checkpoint_state_paths',{}).get(dom,[]),dmap.get('warstart_map',{}).get(dom,[]),ledger); domain_results.append({'domain':dom,'resolution':resolution,'entry_ids':[e['id'] for e in des],'state_source':state_source,'state_bindings':bindings})
        if resolution=='UNKNOWN':block.append(f'mandatory technical domain UNKNOWN: {dom}')
    state_results=[]
    for req in profile.get('state_requirements',[]):
        spec=dmap.get('state_requirements',{}).get(req)
        if not spec:state_results.append({'requirement':req,'resolution':'UNKNOWN','bindings':[]}); block.append(f'state requirement definition missing: {req}'); continue
        source,bindings=resolve_state_binding(cp,spec.get('checkpoint_paths',[]),spec.get('warstart_domains',[]),ledger); state_results.append({'requirement':req,'resolution':source,'bindings':bindings})
        if source=='UNKNOWN':block.append(f'mandatory state requirement UNKNOWN: {req}')
    ov_path=cp.get('current_branch_overrides'); active=[]
    if ov_path and (ROOT/ov_path).exists():
        od=load(ov_path); active=[o.get('override_id') or o.get('rule_id') for o in od.get('overrides',[]) if o.get('status') in ('ACTIVE_CURRENT_BRANCH','active')]
    event_input={}
    if a.combat_input:event_input=json.loads(pathlib.Path(a.combat_input).read_text(encoding='utf-8'))
    sup,fi_path,fi,mx_path,mx,ctx_path,input_schema,wi_path,wp,pm_path,pm,np_path=load_combat_support(cp,reg)
    factor_results,factor_ready,combat_block=resolve_combat_factors(a.profile,cp,selected,gate_by_id,fi,mx,event_input)
    platform_results,novel_review,weapon_ready,weapon_block=resolve_platform_capabilities(a.profile,cp,tech,date,wp,pm,event_input)
    combat_ready=factor_ready and weapon_ready
    inv_path=cp.get('branch_invariants'); branch_inv=(load(inv_path) if inv_path and (ROOT/inv_path).exists() else None)
    air_path=cp.get('aircraft_fielding_ledger'); aircraft_fielding=(load(air_path) if air_path and (ROOT/air_path).exists() else None)
    sea_path=cp.get('seaplane_tactics_ledger'); seaplane_tactics=(load(sea_path) if sea_path and (ROOT/sea_path).exists() else None)
    surface_path=cp.get('surface_combatant_capability_ledger'); surface_capability=(load(surface_path) if surface_path and (ROOT/surface_path).exists() else None)
    carrier_path=cp.get('carrier_capability_ledger'); carrier_capability=(load(carrier_path) if carrier_path and (ROOT/carrier_path).exists() else None)
    rollback_path=cp.get('rollback_guard'); rollback_guard=(load(rollback_path) if rollback_path and (ROOT/rollback_path).exists() else None)
    hand={'schema':'EVENT_HANDOUT_SCHEMA_v004','profile':a.profile,'date':(date.isoformat() if date else a.date),'checkpoint':cp_id,'checkpoint_file':str(cp_path.relative_to(ROOT)),'checkpoint_as_of':cp.get('as_of'),'checkpoint_status':cp.get('status'),'checkpoint_execution_valid':graph_execution_valid,'technical_baseline':baseline,'prewar_baseline':cp.get('prewar_baseline'),'current_branch_overrides':ov_path,'active_override_ids':active,'event_profile_revision':prof.get('revision'),'domain_map_revision':dmap.get('revision'),'runtime_contract':contract,'state_sources':cp.get('state_sources',[]),'branch_invariant_guard':inv_path,'branch_invariants':branch_inv,'aircraft_fielding_ledger':air_path,'aircraft_fielding':aircraft_fielding,'seaplane_tactics_ledger':sea_path,'seaplane_tactics':seaplane_tactics,'surface_combatant_capability_ledger':surface_path,'surface_combatant_capability':surface_capability,'carrier_capability_ledger':carrier_path,'carrier_capability':carrier_capability,'rollback_guard':rollback_path,'rollback_guard_state':rollback_guard,'future_boundary':cp.get('future_boundary'),'maturation_deltas':cp.get('maturation_deltas',[]),'domain_resolution':domain_results,'state_requirement_resolution':state_results,'entries':entries,'combat_resolution_support':sup,'combat_factor_index':fi_path,'combat_factor_index_revision':fi.get('revision'),'combat_factor_matrix':mx_path,'combat_factor_matrix_revision':mx.get('revision'),'combat_adjudication_context':ctx_path,'combat_event_input_schema':input_schema,'combat_factor_resolution':factor_results,'weapon_platform_index':wi_path,'weapon_platform_index_revision':wp.get('revision'),'combat_platform_matrix':pm_path,'combat_platform_matrix_revision':pm.get('revision'),'novel_weapon_policy':np_path,'platform_capability_resolution':platform_results,'novel_weapon_review':novel_review,'weapon_capability_ready':weapon_ready,'weapon_ready_block_reasons':weapon_block,'combat_resolution_ready':combat_ready,'combat_ready_block_reasons':combat_block+weapon_block,'execution_blocked':bool(block),'block_reasons':block,'integration_rules':['same intermediate state: integrate once','distinct causal stages may compound','check thresholds/reallocation/bottlenecks','carry provisional bands visibly','checkpoint-local state wins over opening baseline fallback','technical cards never substitute for OOB/readiness/personnel state','mandatory combat factors are explicit; omission is not a zero modifier','mandatory platform classes are reviewed independently of normal event tags','branch-specific/new weapons use capability+maturity evidence, never historical reputation substitution','branch invariant guard and checkpoint-local ownership/OOB override historical defaults and retained-provisional descendants','aircraft existence/production/delivery/readiness/allocation are separate clocks','seaplane search/observation/local-defense effects require local base/tender/sea-state/comms support and are not flat bonuses','surface combatant class capability must be combined with actual hull readiness, formation, fuel, sensor fit and mission geometry','carrier combat power uses ready air group + deck cycle + crew + information/geometry; nominal aircraft capacity is never the runtime combat value']}
    txt=json.dumps(hand,ensure_ascii=False,indent=2)
    if a.out:pathlib.Path(a.out).write_text(txt+'\n',encoding='utf-8')
    else:print(txt)
if __name__=='__main__':main()
