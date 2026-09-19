#!/usr/bin/env python3
import os,json,sys
root=os.path.abspath(sys.argv[1] if len(sys.argv)>1 else os.path.join(os.path.dirname(__file__),'..'))
errs=[]; warns=[]
def load(rel):
    with open(os.path.join(root,rel),encoding='utf-8') as f:return json.load(f)
tech=load('02_TECH/TECH_INDEX_v003.json'); tids={e['id'] for e in tech['entries']}
pre=load('03_PREWAR/PREWAR_INDEX_v003.json')
for e in tech['entries']:
    for s in e.get('sources',[]):
        p=os.path.join(root,s['path'])
        if not os.path.exists(p): errs.append(f"missing source {e['id']}: {s['path']}")
for e in pre['entries']:
    for t in e.get('tech_links',[]):
        if t not in tids: errs.append(f"PREWAR {e['id']} missing tech {t}")
    for s in e.get('sources',[]):
        if not os.path.exists(os.path.join(root,s['path'])): errs.append(f"missing prewar source {e['id']}: {s['path']}")
ledger=load('04_WARSTART/WARSTART_STATE_LEDGER_v001.json')
for d in ledger['domains']:
    for t in d.get('tech_links',[]):
        if t not in tids: errs.append(f"WARSTART {d['domain']} missing tech {t}")
profiles=load('06_RUNTIME/EVENT_RELEVANCE_PROFILES_v001.json')['profiles']
domains={e['domain'] for e in tech['entries']}
for p,v in profiles.items():
    for d in v.get('mandatory_domains',[]):
        if d not in domains: warns.append(f"profile {p}: mandatory domain {d} has no TECH entries")
print(f"ERRORS={len(errs)} WARNINGS={len(warns)}")
for x in errs: print('ERROR',x)
for x in warns: print('WARN',x)
sys.exit(1 if errs else 0)
