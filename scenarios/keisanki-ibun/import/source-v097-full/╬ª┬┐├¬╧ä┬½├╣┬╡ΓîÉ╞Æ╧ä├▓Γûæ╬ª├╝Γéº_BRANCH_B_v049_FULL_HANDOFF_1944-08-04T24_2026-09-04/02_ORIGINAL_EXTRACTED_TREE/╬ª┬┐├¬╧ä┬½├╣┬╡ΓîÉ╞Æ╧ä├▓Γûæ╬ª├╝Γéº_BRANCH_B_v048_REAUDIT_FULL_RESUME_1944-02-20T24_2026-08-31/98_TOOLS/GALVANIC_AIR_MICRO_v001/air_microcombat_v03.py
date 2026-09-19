#!/usr/bin/env python3
from __future__ import annotations
import argparse, gzip, json, math
from dataclasses import dataclass
from pathlib import Path
import numpy as np

g=9.80665

@dataclass
class Profile:
    id:str; name:str; side:str; mass:float; wing:float
    vmax_anchors:list; roc_anchors:list; clmax:float; roll_anchors:list; control_g_anchors:list
    dive:float; fire:float; protect:float; visibility:float
    sustain_mod:float=1.0; perf_sigma:float=0.025; source_grade:str="A"

@dataclass
class Weapon:
    id:str; name:str; caliber_mm:float; projectile_g:float; muzzle_mps:float; rpm:float; rpm_sigma:float
    base_pen_mm_250:float; blast:float; incendiary:float; ammo_mix:dict; source_grade:str
    @property
    def energy_kj(self): return 0.5*(self.projectile_g/1000.0)*self.muzzle_mps**2/1000.0

@dataclass
class Defense:
    id:str; armament:list; engine:str; rear_armor_mm:float; front_armor_mm:float; self_seal:float
    fire_supp:float; structure:float; controls:float; cooling_vuln:float; engine_tough:float; redundancy:float; source_grade:str

def interp(anchors,x):
    a=sorted(anchors)
    if x<=a[0][0]: return a[0][1]
    if x>=a[-1][0]: return a[-1][1]
    for (x0,y0),(x1,y1) in zip(a,a[1:]):
        if x0<=x<=x1:
            t=(x-x0)/(x1-x0); return y0+t*(y1-y0)
    raise RuntimeError

def rho_at(h):
    T0=288.15; L=.0065; R=287.05; T=T0-L*h
    return 1.225*(T/T0)**(g/(R*L)-1)

def sigma_at(h):
    return rho_at(h)/1.225

def metrics(p,h,ias_kmh):
    """Maneuver metrics with an explicit speed convention.

    Inputs to the combat experiment are IAS/EAS-like km/h. Dynamic pressure and
    control/roll tables therefore use sea-level-equivalent airspeed. Kinematic
    turn rate uses the corresponding TAS at altitude. vmax_anchors remain TAS.
    Compressibility corrections are intentionally deferred beyond v0.3.
    """
    sigma=max(.25,sigma_at(h))
    tas_kmh=ias_kmh/math.sqrt(sigma)
    vtas=tas_kmh/3.6
    veas=ias_kmh/3.6
    q=.5*1.225*veas*veas
    n_aero=q*p.wing*p.clmax/(p.mass*g)
    n_ctrl=interp(p.control_g_anchors,ias_kmh)
    n=max(1.01,min(n_aero,n_ctrl,5.5))
    turn=g*math.sqrt(max(n*n-1,0))/vtas*180/math.pi
    roc=interp(p.roc_anchors,h); wingload=p.mass/p.wing
    sustain=np.clip(.58+.018*roc-.0009*(wingload-150),.50,.94)*p.sustain_mod
    turn_eff=turn*(.64+.36*sustain)
    vmax_tas=interp(p.vmax_anchors,h)
    speed_margin=max(.05,(vmax_tas-tas_kmh)/max(vmax_tas,1.0)+1.0)
    return dict(vmax=vmax_tas,roc=roc,roll=interp(p.roll_anchors,ias_kmh),turn=turn_eff,n=n,
                dive=p.dive,vis=p.visibility,wingload=wingload,ias=ias_kmh,tas=tas_kmh,
                speed_margin=speed_margin,sigma=sigma)

def base_weights(ias_kmh):
    spd=ias_kmh
    if spd<=340: return np.array([.50,.14,.18,.05,.07,.06])
    if spd<=430:
        t=(spd-340)/90; a=np.array([.50,.14,.18,.05,.07,.06]); b=np.array([.30,.23,.19,.12,.10,.06]); return a*(1-t)+b*t
    t=min(1,(spd-430)/120); a=np.array([.30,.23,.19,.12,.10,.06]); b=np.array([.18,.28,.17,.18,.13,.06]); return a*(1-t)+b*t

# aspect-specific zone probabilities: pilot, engine, cooling, fuel, controls, wing, tail
ZONE_NAMES=np.array(["pilot","engine","cooling","fuel","controls","wing","tail"])
ZONE_P={
    "rear": np.array([.09,.10,.08,.19,.15,.22,.17]),
    "beam": np.array([.07,.18,.08,.20,.12,.27,.08]),
    "front":np.array([.07,.35,.05,.10,.07,.30,.06])
}
AMMO_KEYS=["AP","API","I","HEI","T","BALL"]

def load_all(ppath,wpath,dpath):
    pr=json.loads(Path(ppath).read_text(encoding="utf-8"))["profiles"]
    pkeys=set(Profile.__dataclass_fields__); profiles={k:Profile(**{kk:vv for kk,vv in v.items() if kk in pkeys}) for k,v in pr.items()}
    wr=json.loads(Path(wpath).read_text(encoding="utf-8"))
    weapons={k:Weapon(id=k,**v) for k,v in wr["weapons"].items()}
    effects=wr["ammo_effects"]
    dr=json.loads(Path(dpath).read_text(encoding="utf-8"))["aircraft"]
    defenses={k:Defense(id=k,**v) for k,v in dr.items()}
    return profiles,weapons,effects,defenses

def _state(n):
    return {
      "pilot":np.ones(n), "engine":np.ones(n), "cooling":np.ones(n), "fuel":np.ones(n),
      "controls":np.ones(n), "structure":np.ones(n), "fire":np.zeros(n),
      "ever_hit":np.zeros(n,bool), "mission":np.zeros(n,bool), "immediate":np.zeros(n,bool)
    }

def perf_factor(st,df):
    # Short-duel performance degradation: engine/cooling cost energy, controls/structure cost positioning.
    eng=.58+.42*np.clip(st["engine"],0,1)
    cool=.72+.28*np.clip(st["cooling"],0,1)
    ctl=.55+.45*np.clip(st["controls"],0,1)
    stru=.72+.28*np.clip(st["structure"],0,1)
    fire=1-.25*np.clip(st["fire"],0,1)
    return np.clip(eng*cool*ctl*stru*fire,.35,1.0)

def _sample_aspect(rng,n):
    r=rng.random(n); out=np.empty(n,np.int8); out[r<.65]=0; out[(r>=.65)&(r<.90)]=1; out[r>=.90]=2
    return out  # 0 rear,1 beam,2 front

def _armor_for(df:Defense,aspect):
    if aspect==0: return df.rear_armor_mm
    if aspect==2: return df.front_armor_mm
    return .35*max(df.rear_armor_mm,df.front_armor_mm)

def apply_hits(st, df:Defense, weapon:Weapon, effects, idx, nhits, aspect_code, range_m, rng):
    """Apply each projectile hit. idx/nhits/aspect_code/range_m are equal-length arrays for firing trials."""
    total_hit=0
    maxh=int(nhits.max(initial=0))
    if maxh==0: return 0
    mix_keys=list(weapon.ammo_mix.keys()); mix_p=np.array([weapon.ammo_mix[k] for k in mix_keys],float); mix_p/=mix_p.sum()
    ke=weapon.energy_kj
    for k in range(1,maxh+1):
        mask=nhits>=k
        if not mask.any(): continue
        ii=idx[mask]; aa=aspect_code[mask]; rr=range_m[mask]; total_hit+=len(ii); st["ever_hit"][ii]=True
        # zone sample conditional on aspect
        zones=np.empty(len(ii),np.int8)
        for ac,name in [(0,"rear"),(1,"beam"),(2,"front")]:
            m=aa==ac
            if m.any(): zones[m]=rng.choice(7,size=m.sum(),p=ZONE_P[name])
        ammo=np.array(rng.choice(mix_keys,size=len(ii),p=mix_p),dtype=object)
        pen_scale=np.array([effects[x]["pen_scale"] for x in ammo]); blast_scale=np.array([effects[x]["blast_scale"] for x in ammo]); inc_scale=np.array([effects[x]["inc_scale"] for x in ammo])
        vfac=np.exp(-(rr-250)/1800); pen=weapon.base_pen_mm_250*vfac*pen_scale
        blast=weapon.blast*blast_scale; inc=weapon.incendiary*inc_scale
        kin=np.sqrt(max(ke,0.5)/18.0)*np.sqrt(vfac)
        # PILOT
        m=zones==0
        if m.any():
            jj=ii[m]; aaa=aa[m]; ppen=np.zeros(m.sum())
            for ac in (0,1,2):
                mm=aaa==ac
                if mm.any():
                    armor=_armor_for(df,ac); ppen[mm]=1/(1+np.exp(-(pen[m][mm]-armor)/2.5))
            lethal=np.clip(.18+.42*kin[m]+.18*blast[m],.20,.95)*ppen + .04*blast[m]*(1-ppen)
            dead=rng.random(m.sum())<np.clip(lethal,0,.98); dj=jj[dead]
            st["pilot"][dj]=0; st["immediate"][dj]=True; st["mission"][dj]=True
        # ENGINE
        m=zones==1
        if m.any():
            jj=ii[m]; sev=(.15+.18*kin[m]+.12*blast[m])/(df.engine_tough*df.redundancy)
            sev*=rng.uniform(.72,1.28,m.sum()); st["engine"][jj]-=sev
            catastrophic=(rng.random(m.sum())<np.clip(.015+.035*blast[m]+.018*kin[m],0,.18)/df.redundancy)
            cj=jj[catastrophic]; st["engine"][cj]=0; st["mission"][cj]=True
        # COOLING / OIL
        m=zones==2
        if m.any():
            jj=ii[m]; sev=(.12+.16*kin[m]+.12*blast[m])*df.cooling_vuln*rng.uniform(.75,1.30,m.sum())
            st["cooling"][jj]-=sev
        # FUEL
        m=zones==3
        if m.any():
            jj=ii[m]; raw=(.12+.12*kin[m]+.18*blast[m])*rng.uniform(.7,1.3,m.sum())
            leak=raw*(1-.72*df.self_seal); st["fuel"][jj]-=leak
            pfire=np.clip((.055+.18*inc[m]+.08*blast[m])*(1-.62*df.self_seal),0,.55)
            ignite=rng.random(m.sum())<pfire
            ij=jj[ignite]; st["fire"][ij]=np.maximum(st["fire"][ij],rng.uniform(.28,.55,len(ij)))
        # CONTROLS
        m=zones==4
        if m.any():
            jj=ii[m]; sev=(.10+.15*kin[m]+.22*blast[m])/df.controls*rng.uniform(.7,1.3,m.sum()); st["controls"][jj]-=sev
        # WING STRUCTURE
        m=zones==5
        if m.any():
            jj=ii[m]; sev=(.08+.14*kin[m]+.26*blast[m])/df.structure*rng.uniform(.7,1.3,m.sum()); st["structure"][jj]-=sev
            brk=rng.random(m.sum())<np.clip((blast[m]-.55)*.06+(kin[m]-1.0)*.015,0,.10)/df.structure
            bj=jj[brk]; st["structure"][bj]=0; st["immediate"][bj]=True; st["mission"][bj]=True
        # TAIL / REAR FUSELAGE
        m=zones==6
        if m.any():
            jj=ii[m]; sev=(.07+.11*kin[m]+.18*blast[m])*rng.uniform(.7,1.3,m.sum())
            st["controls"][jj]-=.55*sev/df.controls; st["structure"][jj]-=.45*sev/df.structure
    return total_hit

def evolve_damage(st,df:Defense,idx,rng):
    if not len(idx): return
    # Fire can self-extinguish; otherwise it grows. Self-sealing and dedicated suppression both help.
    active=idx[st["fire"][idx]>.02]
    if len(active):
        pext=np.clip(.06+.42*df.fire_supp+.18*df.self_seal,0,.80)
        extinguish=rng.random(len(active))<pext
        st["fire"][active[extinguish]]*=rng.uniform(.05,.25,extinguish.sum())
        grow=active[~extinguish]
        if len(grow):
            st["fire"][grow]=np.clip(st["fire"][grow]+rng.uniform(.05,.16,len(grow))*(1-.45*df.fire_supp),0,1.2)
            st["structure"][grow]-=.035*st["fire"][grow]/df.structure
            st["engine"][grow]-=.025*st["fire"][grow]/df.engine_tough
    # Continuing coolant loss is especially punishing to liquid engines.
    damaged=idx[st["cooling"][idx]<.70]
    if len(damaged):
        rate=.012 if df.engine=="radial" else (.035 if df.engine=="liquid" else .025)
        st["engine"][damaged]-=rate*(.70-st["cooling"][damaged]+.25)*df.cooling_vuln
    # Mission-kill thresholds mean the aircraft can no longer continue the fight safely, not necessarily instant destruction.
    # A liquid-cooled single-engine fighter is forced out by a major coolant loss earlier than a radial; twins retain more engine redundancy.
    eng_thr=.34 if df.engine=="twin_liquid" else .52
    cool_thr=.52 if df.engine=="liquid" else (.40 if df.engine=="twin_liquid" else .28)
    m=(st["engine"][idx]<=eng_thr)|(st["cooling"][idx]<=cool_thr)|(st["controls"][idx]<=.52)|(st["structure"][idx]<=.44)|(st["fire"][idx]>=.65)|(st["pilot"][idx]<=0)
    st["mission"][idx[m]]=True
    for key in ("engine","cooling","fuel","controls","structure"):
        st[key][idx]=np.clip(st[key][idx],0,1)

def firing_burst(shooter:Defense,target:Defense,weapons,effects,st_t,fire_idx,zabs,rng,ammo_left,shot_rounds,hit_count):
    if not len(fire_idx): return
    # Range/trigger time from solution quality. No explicit aspect geometry yet: rear-quarter dominates as a v0.2 approximation.
    q=np.clip(zabs-1.05,0,1.5)
    ranges=np.clip(415-120*q+rng.normal(0,32,len(fire_idx)),140,460)
    dur=np.clip(.42+.11*q+rng.normal(0,.055,len(fire_idx)),.28,.78)
    aspect=_sample_aspect(rng,len(fire_idx))
    for gi,(wid,count,ammo_per_gun,mount,conv,sync) in enumerate(shooter.armament):
        w=weapons[wid]
        rpm=np.clip(rng.normal(w.rpm,w.rpm_sigma,len(fire_idx)),.65*w.rpm,1.25*w.rpm)
        nominal=count*rpm/60*dur*sync
        rounds=np.maximum(0,np.rint(nominal).astype(int))
        # total remaining group ammunition, not per gun, is tracked per trial
        left=ammo_left[gi][fire_idx]; rounds=np.minimum(rounds,left); ammo_left[gi][fire_idx]-=rounds; shot_rounds[fire_idx]+=rounds
        if mount=="nose": mountfac=1.08*np.ones(len(fire_idx))
        else:
            convfac=np.exp(-0.5*((ranges-conv)/260.0)**2); mountfac=.90+.14*convfac
        rangefac=np.exp(-(ranges-220)/700)
        # Baseline calibrated so a marginal 0.4–0.6 s fighter burst yields roughly the same order of any-hit probability as v0.1, while allowing multiple-projectile effects to emerge.
        ppr=np.clip(.0092*(1+.30*q)*rangefac*mountfac,.0028,.024)
        lam=rounds*ppr
        hits=rng.poisson(lam); hit_count[fire_idx]+=hits
        apply_hits(st_t,target,w,effects,fire_idx,hits,aspect,ranges,rng)

def damage_summary(st):
    dmg=1-np.minimum.reduce([st["engine"],st["cooling"],st["fuel"],st["controls"],st["structure"]])
    return dmg

def _adv_components(pa,pb,ma,mb,rng,ntr):
    keys=["turn","roll","roc","speed_margin","dive","vis"]; comps=[]
    for k in keys:
        # Operational dispersion, not epistemic uncertainty. Japanese source uncertainty is handled in sensitivity profiles.
        sa=pa.perf_sigma if k in ("turn","roll","roc","speed_margin") else pa.perf_sigma*.5
        sb=pb.perf_sigma if k in ("turn","roll","roc","speed_margin") else pb.perf_sigma*.5
        comps.append(np.log((ma[k]*np.exp(rng.normal(0,sa,ntr)))/(mb[k]*np.exp(rng.normal(0,sb,ntr)))))
    return np.stack(comps,1)

def simulate_pair_geometry(pa,pb,da,db,weapons,effects,hA,hB,iasA,iasB,ntr=10000,seed=1,max_cycles=26,adv_scale=2.0,noise=.62,z0=0.0):
    """One-on-one duel with potentially asymmetric altitude, IAS and initial position.

    A is normally Japanese in experiment runners. h/IAS are frozen reference
    conditions for the short position-fight model; energy exchange inside each
    cycle remains abstract. Height/speed differences enter through both aircraft
    metrics and a conservative initial specific-energy bias. z0 is a separate
    geometry/detection bias and is zero in altitude/speed sweeps.
    """
    rng=np.random.default_rng(seed); ma=metrics(pa,hA,iasA); mb=metrics(pb,hB,iasB)
    comps=_adv_components(pa,pb,ma,mb,rng,ntr)
    ias_ref=.5*(iasA+iasB); W=rng.dirichlet(base_weights(ias_ref)*60,ntr)
    adv=(W*comps).sum(1)*adv_scale
    # Specific-energy difference: 1 km height ~= 98% of this normalization.
    va=ma["tas"]/3.6; vb=mb["tas"]/3.6
    dE=g*(hA-hB)+.5*(va*va-vb*vb)
    energy_bias=np.clip(dE/10000.0,-2.0,2.0)*.16
    adv=adv+energy_bias
    z=rng.normal(float(z0),.1,ntr); alive=np.ones(ntr,bool); outcome=np.zeros(ntr,np.int8); first=np.zeros(ntr,np.int8)
    stA=_state(ntr); stB=_state(ntr); burstsA=np.zeros(ntr,int); burstsB=np.zeros(ntr,int); roundsA=np.zeros(ntr,int); roundsB=np.zeros(ntr,int); hitsA=np.zeros(ntr,int); hitsB=np.zeros(ntr,int)
    ammoA=[np.full(ntr,int(count*apg),int) for wid,count,apg,mount,conv,sync in da.armament]
    ammoB=[np.full(ntr,int(count*apg),int) for wid,count,apg,mount,conv,sync in db.armament]
    for cyc in range(max_cycles):
        idx=np.where(alive)[0]
        if not len(idx): break
        evolve_damage(stA,da,idx,rng); evolve_damage(stB,db,idx,rng)
        deadA=idx[stA["mission"][idx]]; deadB=idx[stB["mission"][idx]]
        both=np.intersect1d(deadA,deadB,assume_unique=False)
        if len(both):
            pA=perf_factor(stA,da)[both]; pB=perf_factor(stB,db)[both]; a_worse=pA<pB; b_worse=pB<pA
            outcome[both[a_worse]]=-1; outcome[both[b_worse]]=1; outcome[both[~(a_worse|b_worse)]]=3; alive[both]=False
        deadA=deadA[alive[deadA]]; outcome[deadA]=-1; alive[deadA]=False
        deadB=deadB[alive[deadB]]; outcome[deadB]=1; alive[deadB]=False
        idx=np.where(alive)[0]
        if not len(idx): break
        pfA=perf_factor(stA,da)[idx]; pfB=perf_factor(stB,db)[idx]
        dr=adv[idx]+np.log(np.clip(pfA/pfB,.5,2.0))*1.55
        z[idx]=.62*z[idx]+.30*dr+rng.normal(0,noise,len(idx))
        fa=idx[z[idx]>1.05]
        if len(fa):
            burstsA[fa]+=1; first[fa[first[fa]==0]]=1
            firing_burst(da,db,weapons,effects,stB,fa,z[fa],rng,ammoA,roundsA,hitsA); z[fa]*=.3
        evolve_damage(stB,db,fa,rng)
        newly=fa[stB["mission"][fa]&alive[fa]] if len(fa) else np.array([],int)
        if len(newly): outcome[newly]=1; alive[newly]=False
        fb=idx[(z[idx]<-1.05)&alive[idx]]
        if len(fb):
            burstsB[fb]+=1; first[fb[first[fb]==0]]=-1
            firing_burst(db,da,weapons,effects,stA,fb,-z[fb],rng,ammoB,roundsB,hitsB); z[fb]*=.3
        evolve_damage(stA,da,fb,rng)
        newly=fb[stA["mission"][fb]&alive[fb]] if len(fb) else np.array([],int)
        if len(newly): outcome[newly]=-1; alive[newly]=False
        if cyc>=10:
            idx=np.where(alive)[0]
            if len(idx):
                dA=damage_summary(stA)[idx]; dB=damage_summary(stB)[idx]
                # Escape uses current TAS headroom plus dive characteristics rather than vmax alone.
                escA=(ma["speed_margin"]/mb["speed_margin"])**1.1*(ma["dive"]/mb["dive"])
                escB=1/escA
                paesc=np.clip((escA-1.03)*.12+dA*.045,0,.065)
                take=(z[idx]<-.5)&(rng.random(len(idx))<paesc); ai=idx[take]; outcome[ai]=2; alive[ai]=False
                idx2=idx[~take & alive[idx]]
                if len(idx2):
                    dB2=damage_summary(stB)[idx2]
                    pbesc=np.clip((escB-1.03)*.12+dB2*.045,0,.065)
                    take2=(z[idx2]>.5)&(rng.random(len(idx2))<pbesc); bi=idx2[take2]; outcome[bi]=-2; alive[bi]=False
    dA=damage_summary(stA); dB=damage_summary(stB)
    return dict(
      A_kill=float((outcome==1).mean()),B_kill=float((outcome==-1).mean()),double_terminal=float((outcome==3).mean()),
      A_diseng=float((outcome==2).mean()),B_diseng=float((outcome==-2).mean()),timeout=float((outcome==0).mean()),
      A_kill_share_cond=float((outcome==1).sum()/max(1,((outcome==1)|(outcome==-1)).sum())),
      A_firstshot=float((first==1).mean()),B_firstshot=float((first==-1).mean()),no_firstshot=float((first==0).mean()),adv_mean=float(adv.mean()),
      burstsA=float(burstsA.mean()),burstsB=float(burstsB.mean()),roundsA=float(roundsA.mean()),roundsB=float(roundsB.mean()),hitsA=float(hitsA.mean()),hitsB=float(hitsB.mean()),
      A_any_hit=float(stA["ever_hit"].mean()),B_any_hit=float(stB["ever_hit"].mean()),
      A_damaged_returnable=float(((dA>.08)&(~stA["mission"])&(outcome!=1)).mean()),
      B_damaged_returnable=float(((dB>.08)&(~stB["mission"])&(outcome!=-1)).mean()),
      A_mean_damage=float(dA.mean()),B_mean_damage=float(dB.mean()),
      A_immediate_loss=float(((outcome==-1)&stA["immediate"]).mean()),B_immediate_loss=float(((outcome==1)&stB["immediate"]).mean()),
      A_forced_loss=float(((outcome==-1)&(~stA["immediate"])).mean()),B_forced_loss=float(((outcome==1)&(~stB["immediate"])).mean()),
      A_fire_incidence=float((stA["fire"]>.05).mean()),B_fire_incidence=float((stB["fire"]>.05).mean()),
      A_tas_kmh=float(ma["tas"]),B_tas_kmh=float(mb["tas"]),energy_bias=float(energy_bias)
    )

def simulate_pair(pa,pb,da,db,weapons,effects,h,ias_kmh,ntr=10000,seed=1,max_cycles=26,adv_scale=2.0,noise=.62):
    return simulate_pair_geometry(pa,pb,da,db,weapons,effects,h,h,ias_kmh,ias_kmh,ntr=ntr,seed=seed,max_cycles=max_cycles,adv_scale=adv_scale,noise=noise,z0=0.0)

def run_grid(profs,weapons,effects,defs,ntr=3000):
    us=[f"US{i:02d}" for i in range(1,15)]; jp=[f"JP{i:02d}" for i in range(1,7)]
    conds=[(h,s) for h in [1000,3000,5000,7000] for s in [320,400,480]]; rows=[]
    for ci,(h,s) in enumerate(conds):
      for ui,u in enumerate(us):
        for ji,j in enumerate(jp):
          seed=3300000+ci*1000+ui*20+ji
          r=simulate_pair(profs[j],profs[u],defs[j],defs[u],weapons,effects,h,s,ntr=ntr,seed=seed)
          rows.append(dict(alt_m=h,entry_ias_kmh=s,jp=j,us=u,**r))
    return rows

def run_key_geometry(profs,weapons,effects,defs,ntr=2500):
    us=["US02","US04","US07","US09","US13","US14"]
    jp=["JP01","JP02","JP03","JP04","JP05","JP06"]
    rows=[]
    # Separate altitude and speed sweeps keep interpretation clean.
    for mid in [3000,5000]:
      for dh in [-1500,-1000,-500,0,500,1000,1500]:
        hA=mid+dh/2; hB=mid-dh/2
        for j in jp:
          for u in us:
            seed=3400000+mid*10+dh+int(j[-2:])*100+int(u[-2:])
            r=simulate_pair_geometry(profs[j],profs[u],defs[j],defs[u],weapons,effects,hA,hB,400,400,ntr=ntr,seed=seed)
            rows.append(dict(sweep="altitude",mid_alt_m=mid,dh_JP_m=dh,h_JP_m=hA,h_US_m=hB,ias_JP=400,ias_US=400,jp=j,us=u,**r))
      for ds in [-100,-50,0,50,100]:
        for j in jp:
          for u in us:
            seed=3500000+mid*10+ds+int(j[-2:])*100+int(u[-2:])
            r=simulate_pair_geometry(profs[j],profs[u],defs[j],defs[u],weapons,effects,mid,mid,400+ds,400,ntr=ntr,seed=seed)
            rows.append(dict(sweep="speed",mid_alt_m=mid,dh_JP_m=0,h_JP_m=mid,h_US_m=mid,ias_JP=400+ds,ias_US=400,jp=j,us=u,**r))
    return rows

def run_detection_geometry(profs,weapons,effects,defs,ntr=3000):
    us=["US02","US04","US07","US09","US13","US14"]
    jp=["JP01","JP02","JP03","JP04","JP05","JP06"]
    rows=[]
    for z0,label in [(-.65,"US_prior"),(-.35,"US_slight"),(0,"mutual"),(.35,"JP_slight"),(.65,"JP_prior")]:
      for j in jp:
        for u in us:
          seed=3600000+int((z0+1)*1000)+int(j[-2:])*100+int(u[-2:])
          r=simulate_pair_geometry(profs[j],profs[u],defs[j],defs[u],weapons,effects,3000,3000,400,400,ntr=ntr,seed=seed,z0=z0)
          rows.append(dict(sweep="initial_position",alt_m=3000,ias_JP=400,ias_US=400,z0=z0,label=label,jp=j,us=u,**r))
    return rows

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--profiles",default="profiles_v03.json"); ap.add_argument("--weapons",default="weapons_v02.json"); ap.add_argument("--damage",default="aircraft_damage_v02.json"); ap.add_argument("--trials",type=int,default=3000); ap.add_argument("--out",default="results_grid_v03.json.gz"); ap.add_argument("--mode",choices=["grid","geometry","detection"],default="grid")
    a=ap.parse_args(); profs,weapons,effects,defs=load_all(a.profiles,a.weapons,a.damage)
    if a.mode=="grid": rows=run_grid(profs,weapons,effects,defs,a.trials)
    elif a.mode=="geometry": rows=run_key_geometry(profs,weapons,effects,defs,a.trials)
    else: rows=run_detection_geometry(profs,weapons,effects,defs,a.trials)
    payload={"model_version":"air-microcombat-v0.3-IAS-geometry","speed_convention":"entry IAS/EAS-like; TAS derived from density; vmax anchors TAS","mode":a.mode,"trials_per_condition":a.trials,"total_duels":a.trials*len(rows),"rows":rows}
    with gzip.open(a.out,"wt",encoding="utf-8") as f: json.dump(payload,f,ensure_ascii=False,separators=(",",":"))
    print(f"wrote {a.out}: {len(rows)} conditions, {a.trials*len(rows):,} duels")
if __name__=="__main__": main()
