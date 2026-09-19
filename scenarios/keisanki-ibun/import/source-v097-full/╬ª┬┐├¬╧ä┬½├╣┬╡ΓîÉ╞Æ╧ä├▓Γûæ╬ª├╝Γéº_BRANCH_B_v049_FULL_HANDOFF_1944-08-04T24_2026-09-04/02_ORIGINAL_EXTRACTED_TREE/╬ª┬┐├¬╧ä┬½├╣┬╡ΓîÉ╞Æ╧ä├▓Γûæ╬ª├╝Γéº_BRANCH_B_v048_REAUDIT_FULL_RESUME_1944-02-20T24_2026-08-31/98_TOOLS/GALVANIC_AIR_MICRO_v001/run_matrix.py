#!/usr/bin/env python3
import json, math, sys
from pathlib import Path
import numpy as np
ROOT=Path(__file__).parent
sys.path.insert(0,str(ROOT))
import air_microcombat_v03 as base
import air_microcombat_v04 as sim
# load current profiles explicitly
profiles,weapons,effects,defenses=base.load_all(ROOT/'profiles_v04_GALVANIC_1943-11.json',ROOT/'weapons_v02.json',ROOT/'aircraft_damage_v02.json')
rows=[]
seed=1000
for jp in ['JP01','JP02']:
  for base_alt in [3000,5000,7000]:
    for alt_delta in [-1000,0,1000]:
      for spd_delta in [-40,0,40]:
        seed += 1
        hJ=max(500,base_alt+alt_delta); hU=base_alt
        iJ=400+spd_delta; iU=400
        r=sim.simulate_dynamic(profiles[jp],profiles['US01'],defenses[jp],defenses['US01'],weapons,effects,
          hJ,hU,iJ,iU,ntr=12000,seed=seed,max_cycles=34,dt=2.6,policyA='auto',policyB='auto',z0=0.0,noise=.54)
        rows.append({'jp':jp,'base_alt_m':base_alt,'jp_alt_delta_m':alt_delta,'jp_ias_delta_kmh':spd_delta,
          'JP_kill':r['A_kill'],'US_kill':r['B_kill'],'JP_first':r['A_firstshot'],'US_first':r['B_firstshot'],
          'JP_diseng':r['A_diseng'],'US_diseng':r['B_diseng'],'timeout':r['timeout'],
          'JP_damaged_returnable':r['A_damaged_returnable'],'US_damaged_returnable':r['B_damaged_returnable']})
json.dump(rows,open(ROOT/'pairwise_geometry_matrix.json','w'),ensure_ascii=False,indent=2)
# aggregate equal geometry and by altitude advantage
from collections import defaultdict
agg=defaultdict(list)
for x in rows:
  agg[(x['jp'],x['base_alt_m'],x['jp_alt_delta_m'],x['jp_ias_delta_kmh'])].append(x)
# print equal
for jp in ['JP01','JP02']:
 print('\n',jp,profiles[jp].name)
 for alt in [3000,5000,7000]:
  x=next(y for y in rows if y['jp']==jp and y['base_alt_m']==alt and y['jp_alt_delta_m']==0 and y['jp_ias_delta_kmh']==0)
  print(alt, {k:round(x[k],4) for k in ['JP_kill','US_kill','JP_first','US_first','JP_diseng','US_diseng','timeout']})
