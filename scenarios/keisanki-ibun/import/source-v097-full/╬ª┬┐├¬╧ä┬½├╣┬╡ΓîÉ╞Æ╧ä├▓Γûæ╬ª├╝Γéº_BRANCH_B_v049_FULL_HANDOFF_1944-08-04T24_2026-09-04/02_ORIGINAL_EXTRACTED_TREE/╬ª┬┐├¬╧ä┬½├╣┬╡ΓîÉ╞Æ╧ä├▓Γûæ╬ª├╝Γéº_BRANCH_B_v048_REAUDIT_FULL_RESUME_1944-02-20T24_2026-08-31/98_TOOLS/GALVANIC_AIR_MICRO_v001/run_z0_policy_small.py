import sys,json
from pathlib import Path
ROOT=Path(__file__).parent; sys.path.insert(0,str(ROOT))
import air_microcombat_v03 as base, air_microcombat_v04 as sim
p,w,e,d=base.load_all(ROOT/'profiles_v04_GALVANIC_1943-11.json',ROOT/'weapons_v02.json',ROOT/'aircraft_damage_v02.json')
out=[]; seed=7000
for jp in ['JP01','JP02']:
  for z0 in [-0.5,-0.25,0,0.10,0.25,0.5]:
    seed+=1
    r=sim.simulate_dynamic(p[jp],p['US01'],d[jp],d['US01'],w,e,5000,5000,400,400,ntr=8000,seed=seed,policyA='auto',policyB='auto',z0=z0,noise=.54)
    out.append({'jp':jp,'alt':5000,'z0':z0,'policy':'duel',**{k:r[k] for k in ['A_kill','B_kill','A_diseng','B_diseng','A_firstshot','B_firstshot','timeout','A_damaged_returnable','B_damaged_returnable']}})
  for polA,polB,label in [('press','auto','escort_press'),('auto','press','cap_press')]:
    seed+=1
    r=sim.simulate_dynamic(p[jp],p['US01'],d[jp],d['US01'],w,e,5000,5000,400,400,ntr=8000,seed=seed,policyA=polA,policyB=polB,z0=0,noise=.54)
    out.append({'jp':jp,'alt':5000,'z0':0,'policy':label,**{k:r[k] for k in ['A_kill','B_kill','A_diseng','B_diseng','A_firstshot','B_firstshot','timeout','A_damaged_returnable','B_damaged_returnable']}})
json.dump(out,open(ROOT/'z0_policy_matrix.json','w'),ensure_ascii=False,indent=2)
for jp in ['JP01','JP02']:
 print('\n',jp)
 for x in out:
  if x['jp']==jp:
   print(x['policy'],x['z0'], {k:round(x[k],3) for k in ['A_kill','B_kill','A_firstshot','B_firstshot','A_diseng','B_diseng']})
