#!/usr/bin/env python3
import json,argparse,pathlib,datetime
ROOT=pathlib.Path(__file__).resolve().parents[1]
TECH=json.load(open(ROOT/'02_TECH/TECH_INDEX_v003.json',encoding='utf-8'))
PROF=json.load(open(ROOT/'06_RUNTIME/EVENT_RELEVANCE_PROFILES_v002.json',encoding='utf-8'))
WAR=json.load(open(ROOT/'04_WARSTART/WARSTART_DOMAIN_AUDIT_v003.json',encoding='utf-8'))
STATE=json.load(open(ROOT/'04_WARSTART/WARSTART_STATE_LEDGER_v002.json',encoding='utf-8'))
MAP=json.load(open(ROOT/'00_CONFIG/DOMAIN_STATE_MAP_v001.json',encoding='utf-8'))['map']

def iso_date(s): return datetime.date.fromisoformat(s[:10]) if s else None

def gate_state(e,date):
    g=e.get('runtime_gate')
    if not g or not date: return 'ACTIVE_OR_CONDITIONAL'
    if g.get('available_from') and date < iso_date(g['available_from']): return g.get('pre_available_state','NOT_YET_MATURE')
    if g.get('available_to') and date > iso_date(g['available_to']): return 'EXPIRED_OR_REPLACED'
    return 'ACTIVE_OR_CONDITIONAL'

def state_lookup(name):
    for d in STATE['domains']:
        if d['domain']==name:return d
    return None

def state_for_tech_domain(domain):
    return [state_lookup(x) for x in MAP.get(domain,[]) if state_lookup(x)]

def select(profile):
    p=PROF['profiles'][profile]; tags=set(p.get('include_tags',[])); mids=set(p.get('mandatory_entry_ids',[])); out=[]
    for e in TECH['entries']:
        et=set(e.get('event_tags',[])); exact=(profile in et); tagged=bool(et & (tags-{'ALL'})); generic=('ALL' in et and (e['id'] in mids or e['domain']=='CROSS_DOMAIN')); domain_required=e['domain'] in p.get('mandatory_domains',[])
        if e['id'] in mids or exact or tagged or domain_required or generic: out.append(e)
    seen=set(); ans=[]
    for e in sorted(out,key=lambda x:(x['domain'],x['id'])):
        if e['id'] not in seen: ans.append(e); seen.add(e['id'])
    return p,ans

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('profile',choices=sorted(PROF['profiles'])); ap.add_argument('--date'); ap.add_argument('--checkpoint',default='WARSTART_1941-12-07_08_v004'); ap.add_argument('--out'); a=ap.parse_args()
    date=iso_date(a.date); p,sel=select(a.profile); coverage={x['domain']:x['coverage'] for x in WAR['domains']}
    domains=[]
    for d in p.get('mandatory_domains',[]):
        cv=coverage.get(d,'UNKNOWN'); ss=state_for_tech_domain(d)
        domains.append({'domain':d,'resolution':'UNKNOWN' if cv=='UNKNOWN' else 'ACTIVE_OR_BOUNDED','warstart_coverage':cv,'mapped_opening_states':[{'domain':x['domain'],'state':x['state'],'values':x.get('values')} for x in ss]})
    mandatory_states=[]
    for s in p.get('mandatory_state_domains',[]):
        x=state_lookup(s); mandatory_states.append({'domain':s,'resolution':'UNKNOWN' if not x else x['state'],'values':None if not x else x.get('values')})
    entries=[]
    for e in sel:
        gs=gate_state(e,date); rec={'id':e['id'],'domain':e['domain'],'status':e['status'],'date_gate_state':gs,'valid_from':e['valid_from'],'causal_stage':e.get('causal_stage',[]),'what_changed':e['what_changed']}
        if gs in ('ACTIVE_OR_CONDITIONAL','PRECURSOR_TRIAL','PRODUCTION_TRANSITION','PREWAR_COMSEC_PRESENT_OUTCOME_NOT_THIS_1942_CARD'):
            rec.update({'magnitude':e['magnitude'],'combat_meaning':e['combat_meaning'],'nonlinear_effect':e.get('nonlinear_effect',[]),'do_not_simplify_as':e.get('do_not_simplify_as',[])})
        else: rec['warning']='Indexed but not mature for this event date; do not back-port.'
        entries.append(rec)
    hand={'profile':a.profile,'date':a.date,'checkpoint':a.checkpoint,'technical_baseline':'TECH_INDEX_v003','warstart_state':'WARSTART_STATE_LEDGER_v002','domain_resolution':domains,'mandatory_state_resolution':mandatory_states,'entries':entries,'integration_rules':['same intermediate state: integrate once','distinct causal stages may compound','check thresholds/reallocation/bottlenecks','carry provisional bands visibly','technical cards never substitute for OOB/readiness/personnel state']}
    txt=json.dumps(hand,ensure_ascii=False,indent=2)
    if a.out:pathlib.Path(a.out).write_text(txt+'\n',encoding='utf-8')
    else:print(txt)
if __name__=='__main__':main()
