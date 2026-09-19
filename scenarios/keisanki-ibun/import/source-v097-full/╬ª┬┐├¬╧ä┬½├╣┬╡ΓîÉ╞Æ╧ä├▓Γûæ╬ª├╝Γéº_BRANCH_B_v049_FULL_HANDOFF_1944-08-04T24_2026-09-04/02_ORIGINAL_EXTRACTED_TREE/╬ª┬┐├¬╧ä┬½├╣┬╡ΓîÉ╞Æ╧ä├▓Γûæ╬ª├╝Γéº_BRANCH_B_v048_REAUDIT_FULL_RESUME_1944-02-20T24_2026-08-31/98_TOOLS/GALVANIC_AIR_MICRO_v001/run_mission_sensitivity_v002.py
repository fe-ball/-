#!/usr/bin/env python3
import json, numpy as np
from pathlib import Path
ROOT=Path(__file__).parent
rows=json.load(open(ROOT/'pairwise_geometry_matrix.json'))
K={}
for jp in ['JP01','JP02']:
    for d in [-1000,0,1000]:
        x=next(r for r in rows if r['jp']==jp and r['base_alt_m']==5000 and r['jp_alt_delta_m']==d and r['jp_ias_delta_kmh']==0)
        K[(jp,d)]={k:x[k] for k in ['JP_kill','US_kill','JP_diseng','US_diseng','JP_first','US_first']}
CREW={'JP_kill_mult':1.03,'US_kill_mult':0.96}
DISTS={
 'US_CIC_GALVANIC':[(-1000,.55),(0,.35),(1000,.10)],
 'JP_fleet_CAP_warning':[(-1000,.30),(0,.40),(1000,.30)],
}
def draw_kernel(jp,dist,rng):
    u=rng.random(); c=0
    for d,p in DISTS[dist]:
        c += p
        if u <= c: break
    k=K[(jp,d)].copy()
    k['JP_kill']*=CREW['JP_kill_mult']; k['US_kill']*=CREW['US_kill_mult']
    return k

def sim(kinsei,zuisei,us,passes,trials,dist,seed):
    rng=np.random.default_rng(seed); a=[]
    for _ in range(trials):
        J=['JP02']*kinsei+['JP01']*zuisei; U=list(range(us))
        jl=ul=jd=ud=0; uf=jf=n=0
        for _p in range(passes):
            rng.shuffle(J); rng.shuffle(U); m=min(len(J),len(U)); nJ=[]; nU=[]
            for i in range(m):
                typ=J[i]; k=draw_kernel(typ,dist,rng); n+=1; uf+=k['US_first']; jf+=k['JP_first']
                probs=np.array([k['JP_kill'],k['US_kill'],k['JP_diseng'],k['US_diseng']],float)
                probs=np.maximum(0,probs); s=probs.sum()
                if s>.95: probs*=.95/s
                u=rng.random(); c=np.cumsum(probs)
                if u<c[0]: ul+=1; nJ.append(typ)
                elif u<c[1]: jl+=1; nU.append(U[i])
                elif u<c[2]: jd+=1; nU.append(U[i])
                elif u<c[3]: ud+=1; nJ.append(typ)
                else: nJ.append(typ); nU.append(U[i])
            nJ.extend(J[m:]); nU.extend(U[m:]); J,U=nJ,nU
        a.append((jl,ul,jd,ud,uf/max(n,1),jf/max(n,1),len(J),len(U)))
    a=np.array(a,float)
    return {
      'trials':trials,'kinsei':kinsei,'zuisei':zuisei,'us_fighters':us,'passes':passes,'vectoring':dist,
      'JP_fighter_loss_mean':float(a[:,0].mean()),'US_fighter_loss_mean':float(a[:,1].mean()),
      'JP_diseng_mean':float(a[:,2].mean()),'US_diseng_mean':float(a[:,3].mean()),
      'mean_US_firstshot_prob':float(a[:,4].mean()),'mean_JP_firstshot_prob':float(a[:,5].mean()),
      'JP_fighters_remaining_mean':float(a[:,6].mean()),'US_fighters_remaining_mean':float(a[:,7].mean())}

out={'method':{'kernel':'legacy v04 pairwise event engine with current GALVANIC profiles','crew':'small JP carrier-leadership sensitivity: JP kill x1.03, US kill x0.96; no ace multiplier','CIC':'external initial-altitude distribution; not aircraft stat','warning':'mesoscopic mission-window diagnostic, not a full raid-loss generator'},'scenarios':[]}
seed=26000
for passes,trials in [(4,2500),(6,1800)]:
    for name,k,z,u,dist in [
      ('FIRST_STRIKE_ALL_ZUISEI',0,48,60,'US_CIC_GALVANIC'),
      ('FIRST_STRIKE_ACTUAL_MIX',13,35,60,'US_CIC_GALVANIC'),
      ('FIRST_STRIKE_ALL_KINSEI',48,0,60,'US_CIC_GALVANIC'),
      ('DEF_CAP_ALL_ZUISEI',0,52,42,'JP_fleet_CAP_warning'),
      ('DEF_CAP_ACTUAL_MIX',7,45,42,'JP_fleet_CAP_warning'),
      ('DEF_CAP_ALL_KINSEI',52,0,42,'JP_fleet_CAP_warning')]:
        seed+=1; r=sim(k,z,u,passes,trials,dist,seed); r['scenario']=name; out['scenarios'].append(r)
json.dump(out,open(ROOT/'mission_sensitivity_v002.json','w'),ensure_ascii=False,indent=2)
for r in out['scenarios']:
    if r['passes']==6: print(r['scenario'], round(r['JP_fighter_loss_mean'],2), round(r['US_fighter_loss_mean'],2), round(r['mean_US_firstshot_prob'],3))
