#!/usr/bin/env python3
import json, numpy as np, pandas as pd
from pathlib import Path
ROOT=Path(__file__).parent
rows=json.load(open(ROOT/'pairwise_geometry_matrix.json'))
# exact 5km, equal IAS, altitude delta kernels
K={}
for jp in ['JP01','JP02']:
  for d in [-1000,0,1000]:
    x=next(r for r in rows if r['jp']==jp and r['base_alt_m']==5000 and r['jp_alt_delta_m']==d and r['jp_ias_delta_kmh']==0)
    K[(jp,d)]={k:x[k] for k in ['JP_kill','US_kill','JP_diseng','US_diseng','JP_first','US_first']}
# crew center is deliberately small: derived from z0 +0.08 neutral sensitivity
CREW={'JP_kill_mult':1.03,'US_kill_mult':0.96}
DISTS={
 'no_CIC_random': [(-1000,.33),(0,.34),(1000,.33)],
 'US_CIC_GALVANIC': [(-1000,.55),(0,.35),(1000,.10)],
 'US_CIC_strong': [(-1000,.70),(0,.25),(1000,.05)],
 'JP_fleet_CAP_warning': [(-1000,.30),(0,.40),(1000,.30)]
}
def draw_kernel(jp,dist,rng,crew=True):
    u=rng.random(); c=0
    for d,p in DISTS[dist]:
        c+=p
        if u<=c: break
    k=K[(jp,d)].copy()
    if crew:
        k['JP_kill']*=CREW['JP_kill_mult']; k['US_kill']*=CREW['US_kill_mult']
    return k,d

def sim(kinsei=13,zuisei=35,us=60,passes=4,trials=30000,dist='US_CIC_GALVANIC',crew=True,seed=1):
    rng=np.random.default_rng(seed)
    out=[]
    for t in range(trials):
      J=['JP02']*kinsei+['JP01']*zuisei; U=list(range(us))
      jloss=uloss=jdis=udis=0; leaks=0; us_first=jp_first=pairings=0
      for ps in range(passes):
        rng.shuffle(J); rng.shuffle(U); m=min(len(J),len(U)); leaks += max(0,len(U)-m)
        nJ=[]; nU=[]
        for i in range(m):
          typ=J[i]; k,d=draw_kernel(typ,dist,rng,crew)
          pairings+=1; us_first+=k['US_first']; jp_first+=k['JP_first']
          probs=np.array([k['JP_kill'],k['US_kill'],k['JP_diseng'],k['US_diseng']],float)
          # prevent tiny overlap if crew multiplier raises sum; leftover = no decisive event
          probs=np.maximum(0,probs); s=probs.sum();
          if s>.95: probs*=.95/s
          u=rng.random(); c=np.cumsum(probs)
          if u<c[0]: uloss+=1; nJ.append(typ)
          elif u<c[1]: jloss+=1; nU.append(U[i])
          elif u<c[2]: jdis+=1; nU.append(U[i])
          elif u<c[3]: udis+=1; nJ.append(typ)
          else: nJ.append(typ); nU.append(U[i])
        nJ.extend(J[m:]); nU.extend(U[m:]); J,U=nJ,nU
      out.append((jloss,uloss,jdis,udis,leaks,us_first/max(pairings,1),jp_first/max(pairings,1)))
    a=np.array(out,float)
    return {'trials':trials,'kinsei':kinsei,'zuisei':zuisei,'us_CAP':us,'passes':passes,'vectoring':dist,'crew_center':crew,
      'JP_fighter_loss_mean':float(a[:,0].mean()),'US_fighter_loss_mean':float(a[:,1].mean()),
      'JP_diseng_mean':float(a[:,2].mean()),'US_diseng_mean':float(a[:,3].mean()),
      'CAP_bomber_attack_opportunities_mean':float(a[:,4].mean()),
      'mean_US_firstshot_prob_per_pairing':float(a[:,5].mean()),'mean_JP_firstshot_prob_per_pairing':float(a[:,6].mean())}
R=[]; seed=13000
for dist,tr in [('no_CIC_random',400),('US_CIC_GALVANIC',2500),('US_CIC_strong',400)]:
 for comp,(k,z) in {'all_Zuisei':(0,48),'GALVANIC_mix':(13,35),'all_Kinsei':(48,0)}.items():
  seed+=1; r=sim(k,z,60,4,tr,dist,True,seed); r['composition']=comp; R.append(r)
json.dump({'method':'Repeated-pair escort/CAP window. CIC is external initial-altitude distribution; crew edge is small sensitivity multiplier derived from positional-prior runs. Leakage counts CAP bomber-attack opportunities, not bomber kills.','rows':R},open(ROOT/'escort_cap_results.json','w'),ensure_ascii=False,indent=2)
for r in R:
 if r['vectoring']=='US_CIC_GALVANIC':
  print(r['composition'],'JP loss',round(r['JP_fighter_loss_mean'],2),'US loss',round(r['US_fighter_loss_mean'],2),'leak opp',round(r['CAP_bomber_attack_opportunities_mean'],1),'US first',round(r['mean_US_firstshot_prob_per_pairing'],3))
