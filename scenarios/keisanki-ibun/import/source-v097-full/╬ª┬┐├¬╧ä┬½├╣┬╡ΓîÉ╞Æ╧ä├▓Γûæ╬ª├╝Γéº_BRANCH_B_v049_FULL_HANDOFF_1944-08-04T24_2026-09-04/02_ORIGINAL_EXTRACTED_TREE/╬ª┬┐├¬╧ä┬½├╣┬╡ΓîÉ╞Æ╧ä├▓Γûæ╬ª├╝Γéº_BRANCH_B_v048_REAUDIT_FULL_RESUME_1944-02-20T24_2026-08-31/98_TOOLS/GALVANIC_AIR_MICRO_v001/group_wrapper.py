#!/usr/bin/env python3
import json, numpy as np
from pathlib import Path
ROOT=Path(__file__).parent
zmat=json.load(open(ROOT/'z0_policy_matrix.json'))
# representative 5km neutral duel kernels
def kern(jp):
    x=next(r for r in zmat if r['jp']==jp and r['policy']=='duel' and r['z0']==0)
    return {k:x[k] for k in ['A_kill','B_kill','A_diseng','B_diseng']}
K={j:kern(j) for j in ['JP01','JP02']}

def run(comp,n_us,passes=3,trials=30000,seed=1):
    rng=np.random.default_rng(seed)
    stats=[]
    for t in range(trials):
        jp=list(comp); us=list(range(n_us)); jp_left=[]; us_left=[]
        jp_lost=us_lost=jp_dis=us_dis=0
        for ps in range(passes):
            if not jp or not us: break
            rng.shuffle(jp); rng.shuffle(us)
            m=min(len(jp),len(us))
            surv_j=[]; surv_u=[]
            for i in range(m):
                typ=jp[i]; k=K[typ]
                probs=np.array([k['A_kill'],k['B_kill'],k['A_diseng'],k['B_diseng']],float)
                # pairwise outcomes are mutually exclusive in kernel; remaining probability = no decisive event
                u=rng.random(); c=np.cumsum(probs)
                if u<c[0]:
                    # Japan kills US
                    us_lost+=1; surv_j.append(typ)
                elif u<c[1]:
                    jp_lost+=1; surv_u.append(us[i])
                elif u<c[2]:
                    jp_dis+=1; surv_u.append(us[i])
                elif u<c[3]:
                    us_dis+=1; surv_j.append(typ)
                else:
                    surv_j.append(typ); surv_u.append(us[i])
            surv_j.extend(jp[m:]); surv_u.extend(us[m:])
            jp,us=surv_j,surv_u
        stats.append((jp_lost,us_lost,jp_dis,us_dis,len(jp),len(us)))
    a=np.array(stats)
    return {
      'trials':trials,'passes':passes,'JP_start':len(comp),'US_start':n_us,
      'JP_loss_mean':float(a[:,0].mean()),'US_loss_mean':float(a[:,1].mean()),
      'JP_diseng_mean':float(a[:,2].mean()),'US_diseng_mean':float(a[:,3].mean()),
      'JP_no_loss_prob':float((a[:,0]==0).mean()),'US_no_loss_prob':float((a[:,1]==0).mean()),
      'JP_2plus_loss_prob':float((a[:,0]>=2).mean()),'US_2plus_loss_prob':float((a[:,1]>=2).mean()),
    }
rows=[]; seed=9000
for n in [4,8]:
  comps={
   'all_Zuisei':['JP01']*n,
   'all_Kinsei':['JP02']*n,
   'GALVANIC_mix': (['JP02']*max(1,round(n*13/48)) + ['JP01']*(n-max(1,round(n*13/48))))
  }
  for name,c in comps.items():
    seed+=1; r=run(c,n,passes=3 if n==4 else 4,trials=25000,seed=seed); r.update({'size':n,'composition':name}); rows.append(r)
json.dump({'method':'Repeated neutral 5km pairwise-kernel mesoscopic wrapper; no extra nationality/cohesion bonus. Diagnostic scaling only.','rows':rows},open(ROOT/'group_4v4_8v8.json','w'),ensure_ascii=False,indent=2)
for r in rows:
 print(r['size'],r['composition'],'JP loss',round(r['JP_loss_mean'],3),'US loss',round(r['US_loss_mean'],3),'JP2+',round(r['JP_2plus_loss_prob'],3),'US2+',round(r['US_2plus_loss_prob'],3))
