#!/usr/bin/env python3
import argparse, json
from pathlib import Path
p=argparse.ArgumentParser()
p.add_argument('--tech-index', default='../02_TECH/TECH_INDEX_v001.json')
p.add_argument('--domains', required=True, help='comma-separated domains, e.g. AIR,SENSOR_SEARCH,SIGINT_COMINT')
p.add_argument('--out', required=True)
a=p.parse_args()
idx=json.loads(Path(a.tech_index).read_text(encoding='utf-8'))
domains={x.strip() for x in a.domains.split(',') if x.strip()}
selected=[e for e in idx['entries'] if e['domain'] in domains or e['domain']=='CROSS_DOMAIN']
Path(a.out).write_text(json.dumps({'selected_domains':sorted(domains),'entries':selected},ensure_ascii=False,indent=2),encoding='utf-8')
