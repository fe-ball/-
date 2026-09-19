#!/usr/bin/env python3
import json, argparse, pathlib, datetime
ROOT=pathlib.Path(__file__).resolve().parents[1]
TECH=json.load(open(ROOT/'02_TECH/TECH_INDEX_v002.json',encoding='utf-8'))
PROF=json.load(open(ROOT/'06_RUNTIME/EVENT_RELEVANCE_PROFILES_v001.json',encoding='utf-8'))
WAR=json.load(open(ROOT/'04_WARSTART/WARSTART_DOMAIN_AUDIT_v001.json',encoding='utf-8'))

def iso_date(s):
 if not s: return None
 return datetime.date.fromisoformat(s[:10])

def gate_state(e,date):
 g=e.get('runtime_gate')
 if not g or not date: return 'ACTIVE_OR_CONDITIONAL'
 if g.get('available_from') and date < iso_date(g['available_from']):
  return g.get('pre_available_state','NOT_YET_MATURE')
 if g.get('available_to') and date > iso_date(g['available_to']): return 'EXPIRED_OR_REPLACED'
 return 'ACTIVE_OR_CONDITIONAL'

def relevant(profile,date):
 p=PROF['profiles'][profile]
 tags=set(p.get('include_tags',[profile,'ALL']))
 ids=set(p.get('mandatory_entry_ids',[]))
 selected=[]
 for e in TECH['entries']:
  et=set(e.get('event_tags',[]))
  if e['id'] in ids or (et & tags):
   selected.append(e)
 selected.sort(key=lambda e:(e['domain'],e['id']))
 return p,selected

def main():
 ap=argparse.ArgumentParser()
 ap.add_argument('profile',choices=sorted(PROF['profiles']))
 ap.add_argument('--date',default=None)
 ap.add_argument('--checkpoint',default='WARSTART_1941-12-07_08_v002')
 ap.add_argument('--out',default=None)
 a=ap.parse_args(); date=iso_date(a.date)
 p,sel=relevant(a.profile,date)
 coverage={x['domain']:x['coverage'] for x in WAR['domains']}
 domain_state=[]
 for d in p.get('mandatory_domains',[]):
  cv=coverage.get(d,'UNKNOWN')
  if cv=='UNKNOWN': state='UNKNOWN'
  elif 'NOT_YET' in cv: state='NOT_YET_MATURE'
  else: state='ACTIVE_OR_BOUNDED'
  domain_state.append({'domain':d,'resolution':state,'warstart_coverage':cv})
 out_entries=[]
 for e in sel:
  gs=gate_state(e,date)
  rec={'id':e['id'],'domain':e['domain'],'status':e['status'],'date_gate_state':gs,'valid_from':e['valid_from'],'what_changed':e['what_changed']}
  if gs in ('ACTIVE_OR_CONDITIONAL','PRECURSOR_TRIAL','PRODUCTION_TRANSITION'):
   rec.update({'magnitude':e['magnitude'],'combat_meaning':e['combat_meaning'],'do_not_simplify_as':e.get('do_not_simplify_as',[])})
  else:
   rec['warning']='Relevant capability exists in the index but is not yet mature for this event date; do not back-port it.'
  out_entries.append(rec)
 hand={'profile':a.profile,'date':a.date,'checkpoint':a.checkpoint,'technical_baseline':'TECH_INDEX_v002','domain_resolution':domain_state,'entries':out_entries}
 text=json.dumps(hand,ensure_ascii=False,indent=2)
 if a.out: pathlib.Path(a.out).write_text(text+'\n',encoding='utf-8')
 else: print(text)
if __name__=='__main__': main()
