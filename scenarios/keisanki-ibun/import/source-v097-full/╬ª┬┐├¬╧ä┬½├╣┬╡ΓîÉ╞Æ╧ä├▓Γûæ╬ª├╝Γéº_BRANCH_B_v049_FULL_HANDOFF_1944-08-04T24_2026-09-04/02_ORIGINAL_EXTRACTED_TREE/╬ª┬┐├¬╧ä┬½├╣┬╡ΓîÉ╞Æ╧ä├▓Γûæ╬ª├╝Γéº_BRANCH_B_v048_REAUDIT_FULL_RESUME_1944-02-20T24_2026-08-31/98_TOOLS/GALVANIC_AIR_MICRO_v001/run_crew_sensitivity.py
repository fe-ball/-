import sys,json
from pathlib import Path
ROOT=Path(__file__).parent; sys.path.insert(0,str(ROOT))
import air_microcombat_v03 as base, air_microcombat_v04 as sim
p,w,e,d=base.load_all(ROOT/'profiles_v04_GALVANIC_1943-11.json',ROOT/'weapons_v02.json',ROOT/'aircraft_damage_v02.json')
rows=[]; seed=11000
for jp in ['JP01','JP02']:
 for z0,label in [(0,'equal_crew_proxy'),(.08,'JP_experience_edge_center'),(.15,'JP_experience_edge_high'),(-.08,'US_individual_edge')]:
  seed+=1
  r=sim.simulate_dynamic(p[jp],p['US01'],d[jp],d['US01'],w,e,5000,5000,400,400,ntr=24000,seed=seed,z0=z0,noise=.54)
  rows.append({'jp':jp,'crew_proxy':label,'z0':z0,**{k:r[k] for k in ['A_kill','B_kill','A_firstshot','B_firstshot','A_diseng','B_diseng','timeout']}})
json.dump({'note':'Crew proxy uses small initial positional prior only; no blanket kill-rate multiplier. Center +0.08 reflects higher surviving IJN carrier-fighter leader density, while US has strong standardized training.','rows':rows},open(ROOT/'crew_sensitivity.json','w'),ensure_ascii=False,indent=2)
for x in rows: print(x['jp'],x['crew_proxy'],round(x['A_kill'],4),round(x['B_kill'],4),round(x['A_firstshot'],3),round(x['B_firstshot'],3))
