#!/usr/bin/env python3
from __future__ import annotations
import json, math
from pathlib import Path
import numpy as np
import air_microcombat_v03 as base

g=9.80665

# Action codes
MANEUVER=0; ATTACK=1; DEFEND=2; ZOOM=3; EXTEND=4
ACTION_NAMES=np.array(['maneuver','attack','defend','zoom','extend'])

def vinterp(anchors,x):
    a=np.asarray(sorted(anchors),float)
    return np.interp(x,a[:,0],a[:,1])

def rho_vec(h):
    h=np.asarray(h,float)
    T0=288.15; L=.0065; R=287.05
    T=np.maximum(216.65,T0-L*h)
    return 1.225*(T/T0)**(g/(R*L)-1)

def sigma_vec(h): return rho_vec(h)/1.225

def stall_ias(p):
    return math.sqrt(2*p.mass*g/(1.225*p.wing*p.clmax))*3.6

def dyn_metrics(p,h,tas_kmh):
    h=np.asarray(h,float); tas_kmh=np.asarray(tas_kmh,float)
    sig=np.maximum(.20,sigma_vec(h)); ias=tas_kmh*np.sqrt(sig)
    veas=ias/3.6; vtas=np.maximum(35,tas_kmh/3.6)
    q=.5*1.225*veas*veas
    n_aero=q*p.wing*p.clmax/(p.mass*g)
    n_ctrl=vinterp(p.control_g_anchors,ias)
    nmax=np.clip(np.minimum(n_aero,n_ctrl),1.02,5.5)
    roll=vinterp(p.roll_anchors,ias)
    roc=vinterp(p.roc_anchors,h)
    vmax=vinterp(p.vmax_anchors,h)
    wingload=p.mass/p.wing
    sustain=np.clip(.58+.018*roc-.0009*(wingload-150),.50,.94)*p.sustain_mod
    n_sust=1+(nmax-1)*np.clip(.44+.30*sustain,.55,.78)
    turn_max=g*np.sqrt(np.maximum(nmax*nmax-1,0))/vtas*180/math.pi
    turn_eff=turn_max*(.64+.36*sustain)
    return dict(ias=ias,tas=tas_kmh,nmax=nmax,nsust=n_sust,roll=roll,roc=roc,vmax=vmax,
                turn=turn_eff,sustain=sustain,sigma=sig,wingload=wingload)

def excess_specific_power(p,m,pf):
    """Approximate propulsive excess specific power [J/kg/s = m^2/s^3].
    roc anchors give best-climb excess power. The speed shape makes excess power
    tend to zero at local level-flight vmax; this is a deliberately compact
    energy model, not a propeller/drag polar reconstruction.
    """
    r=np.clip(m['tas']/np.maximum(m['vmax'],1),.20,1.20)
    shape=np.where(r<.55,.72+.28*(r/.55),np.clip((1-r)/.45,0,1))
    return g*m['roc']*shape*np.clip(pf,.35,1.0)

def maneuver_loss(m,n_cmd):
    n=np.minimum(n_cmd,m['nmax'])
    excess=np.maximum(0,n-m['nsust'])
    # Cost only the part above estimated sustained load. Scale increases mildly
    # with TAS because induced/trim work at high kinetic state is expensive.
    return 30.0*np.power(excess,1.55)*(0.80+0.20*np.clip(m['tas']/500,0.6,1.5))

def _action_commands(action,z,eadv,turn_ratio,roc_ratio,dive_ratio):
    n=len(z); ncmd=np.full(n,3.15); gamma=np.zeros(n)
    # Generic maneuver: a small climbing component if climb advantage exists.
    mm=action==MANEUVER
    gamma[mm]=np.where(roc_ratio[mm]>1.08,3.5,0.0)
    ncmd[mm]=3.25
    mm=action==ATTACK
    # Convert some height/energy to speed on the attack, especially with a positive reserve.
    gamma[mm]=np.where(eadv[mm]>.15,-8.0,-3.5); ncmd[mm]=3.0
    mm=action==DEFEND
    gamma[mm]=np.where(dive_ratio[mm]>1.03,-5.0,0.0); ncmd[mm]=4.55
    mm=action==ZOOM
    gamma[mm]=np.where(eadv[mm]>-.25,13.0,8.0); ncmd[mm]=1.75
    mm=action==EXTEND
    gamma[mm]=np.where(dive_ratio[mm]>=.98,-4.0,0.0); ncmd[mm]=1.25
    return ncmd,gamma

def choose_actions(z,eA,eB,mA,mB,policyA,policyB,timerA,timerB,postA,postB):
    n=len(z); a=np.full(n,MANEUVER,np.int8); b=np.full(n,MANEUVER,np.int8)
    dnorm=(eA-eB)/10000.0
    tr=np.clip(mA['turn']/np.maximum(mB['turn'],1e-6),.3,3)
    rr=np.clip(mA['roc']/np.maximum(mB['roc'],1e-6),.3,3)
    dr=np.full(n,1.0) # dive scalar handled outside with profile constants in caller if needed

    # Explicit post-shot policies override auto behavior for a few cycles.
    ta=timerA>0; tb=timerB>0
    if policyA=='press': a[ta]=ATTACK
    elif policyA=='zoom': a[ta]=ZOOM
    elif policyA=='extend': a[ta]=EXTEND
    elif policyA=='auto':
        a[ta]=np.where((dnorm[ta]>.10)|(rr[ta]>1.08),ZOOM,np.where(dnorm[ta]<-.45,EXTEND,ATTACK))
    if policyB=='press': b[tb]=ATTACK
    elif policyB=='zoom': b[tb]=ZOOM
    elif policyB=='extend': b[tb]=EXTEND
    elif policyB=='auto':
        invrr=1/rr
        b[tb]=np.where((dnorm[tb]<-.10)|(invrr[tb]>1.08),ZOOM,np.where(dnorm[tb]>.45,EXTEND,ATTACK))

    freeA=~ta; freeB=~tb
    # Aircraft with a positional advantage attacks; the other breaks.
    ma=freeA & (z>.58); mb=freeB & (z<-.58)
    a[ma]=ATTACK; b[ma & freeB]=DEFEND
    b[mb]=ATTACK; a[mb & freeA]=DEFEND
    # In neutral geometry, use energy and turn/climb character rather than a permanent speed bonus.
    neutral=(np.abs(z)<=.58)
    x=neutral & freeA
    a[x & (dnorm>.38)]=ATTACK
    a[x & (dnorm<-.38)]=DEFEND
    x=neutral & freeB
    b[x & (dnorm<-.38)]=ATTACK
    b[x & (dnorm>.38)]=DEFEND
    return a,b

def update_energy(p,h,tas,action,z,eopp,pf,dt,dive_ratio):
    m=dyn_metrics(p,h,tas)
    e=g*h+.5*(tas/3.6)**2
    eadv=(e-eopp)/10000.0
    # Ratios used only to select command shape.
    turn_ratio=np.ones(len(h)); roc_ratio=np.ones(len(h)); dive_r=np.full(len(h),dive_ratio)
    ncmd,gamma=_action_commands(action,z,eadv,turn_ratio,roc_ratio,dive_r)
    ncmd=np.minimum(ncmd,m['nmax'])
    ps=excess_specific_power(p,m,pf)-maneuver_loss(m,ncmd)
    # Defending/attacking high-g flight adds non-sustained transient drag.
    ps-=np.where(action==DEFEND,12.0,0.0)
    ps-=np.where(action==ATTACK,5.0,0.0)
    enew=np.maximum(g*80+.5*(45.0**2),e+ps*dt)
    # Redistribute energy vertically. gamma is a flight-path command, not an energy source.
    dh=(tas/3.6)*np.sin(np.deg2rad(gamma))*dt
    hnew=np.clip(h+dh,80,12000)
    v2=2*np.maximum(0,enew-g*hnew)
    vnew=np.sqrt(v2)*3.6
    # Stall floor: if the commanded zoom/turn asks for too much height, give height back.
    vstall=stall_ias(p)/np.sqrt(np.maximum(.20,sigma_vec(hnew)))
    floor=1.10*vstall
    low=vnew<floor
    if np.any(low):
        vnew[low]=floor[low]
        hnew[low]=(enew[low]-.5*(vnew[low]/3.6)**2)/g
        hnew[low]=np.maximum(80,hnew[low])
    # Structural/practical dive envelope. Excess energy beyond this is shed as drag.
    vmax=vinterp(p.vmax_anchors,hnew)
    vcap=vmax*(1.15+.12*np.clip(p.dive,.70,1.25))
    vnew=np.minimum(vnew,vcap)
    return hnew,vnew,ncmd,gamma,m

def simulate_dynamic(pa,pb,da,db,weapons,effects,hA0,hB0,iasA0,iasB0,ntr=4000,seed=1,
                     max_cycles=34,dt=2.6,policyA='auto',policyB='auto',z0=0.0,noise=.54,initial_attack_A=False):
    rng=np.random.default_rng(seed)
    hA=np.full(ntr,float(hA0)); hB=np.full(ntr,float(hB0))
    tasA=np.full(ntr,float(iasA0)/math.sqrt(base.sigma_at(hA0)))
    tasB=np.full(ntr,float(iasB0)/math.sqrt(base.sigma_at(hB0)))
    eA0=g*hA+.5*(tasA/3.6)**2; eB0=g*hB+.5*(tasB/3.6)**2
    z=rng.normal(float(z0),.09,ntr); alive=np.ones(ntr,bool); outcome=np.zeros(ntr,np.int8); first=np.zeros(ntr,np.int8)
    stA=base._state(ntr); stB=base._state(ntr)
    burstsA=np.zeros(ntr,int); burstsB=np.zeros(ntr,int); roundsA=np.zeros(ntr,int); roundsB=np.zeros(ntr,int); hitsA=np.zeros(ntr,int); hitsB=np.zeros(ntr,int)
    ammoA=[np.full(ntr,int(count*apg),int) for wid,count,apg,mount,conv,sync in da.armament]
    ammoB=[np.full(ntr,int(count*apg),int) for wid,count,apg,mount,conv,sync in db.armament]
    timerA=np.zeros(ntr,int); timerB=np.zeros(ntr,int); postA=np.zeros(ntr,int); postB=np.zeros(ntr,int)
    action_counts_A=np.zeros((5,),float); action_counts_B=np.zeros((5,),float)
    # Fixed tactical emphasis per trial; speed regime updates weights only mildly through metrics.
    W=rng.dirichlet(base.base_weights(.5*(iasA0+iasB0))*65,ntr)
    first_cycle=np.full(ntr,-1,int); second_burst_A=np.zeros(ntr,bool); second_burst_B=np.zeros(ntr,bool)
    # Optional rear-quarter attack-pass setup. This is deliberately distinct from a neutral merge:
    # initial excess speed is useful for closure but can create an overshoot after the burst.
    if initial_attack_A:
        closure=float(iasA0-iasB0)
        psol=float(np.clip(.80-.0012*max(0,closure-120)-.0007*max(0,-closure),.48,.84))
        fire_idx=np.where(rng.random(ntr)<psol)[0]
        if len(fire_idx):
            first[fire_idx]=1; first_cycle[fire_idx]=0; burstsA[fire_idx]+=1
            q=np.full(len(fire_idx),1.60)
            base.firing_burst(da,db,weapons,effects,stB,fire_idx,q,rng,ammoA,roundsA,hitsA)
            base.evolve_damage(stB,db,fire_idx,rng)
            killed=fire_idx[stB['mission'][fire_idx]]
            if len(killed): outcome[killed]=1; alive[killed]=False
            surv=fire_idx[alive[fire_idx]]
            if len(surv):
                timerA[surv]=3; postA[surv]=1
                # Fast closure buys the pass but tends to reduce post-pass positional advantage.
                z[surv]=np.clip(.28-.0035*closure,-.25,.42)+rng.normal(0,.06,len(surv))
        miss=np.where((first==0)&alive)[0]
        if len(miss): z[miss]=.50+rng.normal(0,.07,len(miss))
    for cyc in range(max_cycles):
        idx=np.where(alive)[0]
        if not len(idx): break
        base.evolve_damage(stA,da,idx,rng); base.evolve_damage(stB,db,idx,rng)
        deadA=idx[stA['mission'][idx]]; deadB=idx[stB['mission'][idx]]
        both=np.intersect1d(deadA,deadB)
        if len(both):
            pfa=base.perf_factor(stA,da)[both]; pfb=base.perf_factor(stB,db)[both]
            outcome[both[pfa<pfb]]=-1; outcome[both[pfb<pfa]]=1; outcome[both[pfa==pfb]]=3; alive[both]=False
        deadA=deadA[alive[deadA]]; outcome[deadA]=-1; alive[deadA]=False
        deadB=deadB[alive[deadB]]; outcome[deadB]=1; alive[deadB]=False
        idx=np.where(alive)[0]
        if not len(idx): break
        mA=dyn_metrics(pa,hA[idx],tasA[idx]); mB=dyn_metrics(pb,hB[idx],tasB[idx])
        eA=g*hA[idx]+.5*(tasA[idx]/3.6)**2; eB=g*hB[idx]+.5*(tasB[idx]/3.6)**2
        # Position drift from instantaneous handling + a bounded, consumable energy reserve.
        comps=np.stack([
            np.log(np.maximum(mA['turn'],1e-4)/np.maximum(mB['turn'],1e-4)),
            np.log(np.maximum(mA['roll'],1e-4)/np.maximum(mB['roll'],1e-4)),
            np.log(np.maximum(mA['roc'],.5)/np.maximum(mB['roc'],.5)),
            np.log(np.maximum((mA['vmax']-mA['tas'])+.18*mA['vmax'],15)/np.maximum((mB['vmax']-mB['tas'])+.18*mB['vmax'],15)),
            np.full(len(idx),math.log(pa.dive/pb.dive)),
            np.full(len(idx),math.log(pa.visibility/pb.visibility))
        ],axis=1)
        pfA=base.perf_factor(stA,da)[idx]; pfB=base.perf_factor(stB,db)[idx]
        dr=(W[idx]*comps).sum(1)*1.75 + np.log(np.clip(pfA/pfB,.5,2))*1.35
        eres=np.tanh((eA-eB)/9000.0)*.26
        a,b=choose_actions(z[idx],eA,eB,mA,mB,policyA,policyB,timerA[idx],timerB[idx],postA[idx],postB[idx])
        for ac in range(5):
            action_counts_A[ac]+=np.sum(a==ac); action_counts_B[ac]+=np.sum(b==ac)
        # Attack/defense interaction: reserve helps an attacker, roll/turn help the defender.
        interact=np.zeros(len(idx))
        aa=(a==ATTACK)&(b==DEFEND); bb=(b==ATTACK)&(a==DEFEND)
        interact[aa]+=.08+.10*np.maximum(0,(eA[aa]-eB[aa])/10000)
        interact[bb]-=.08+.10*np.maximum(0,(eB[bb]-eA[bb])/10000)
        interact[a==ZOOM]-=.055; interact[b==ZOOM]+=.055
        interact[a==EXTEND]-=.035; interact[b==EXTEND]+=.035
        z[idx]=.67*z[idx]+.27*dr+.20*eres+interact+rng.normal(0,noise,len(idx))
        # Update energy after position choice. Damage degrades recoverable power.
        full_eA=g*hA+.5*(tasA/3.6)**2; full_eB=g*hB+.5*(tasB/3.6)**2
        hAn,vAn,_,_,_=update_energy(pa,hA[idx],tasA[idx],a,z[idx],full_eB[idx],pfA,dt,pa.dive/pb.dive)
        hBn,vBn,_,_,_=update_energy(pb,hB[idx],tasB[idx],b,-z[idx],full_eA[idx],pfB,dt,pb.dive/pa.dive)
        hA[idx]=hAn; tasA[idx]=vAn; hB[idx]=hBn; tasB[idx]=vBn
        # Timers count down after the commanded post-shot maneuver.
        timerA[idx]=np.maximum(0,timerA[idx]-1); timerB[idx]=np.maximum(0,timerB[idx]-1)
        # Firing solutions. A shot is harder if the shooter is near stall or far above practical vmax.
        ia=dyn_metrics(pa,hA[idx],tasA[idx])['ias']; ib=dyn_metrics(pb,hB[idx],tasB[idx])['ias']
        stallA=stall_ias(pa); stallB=stall_ias(pb)
        eligibleA=(ia>1.12*stallA); eligibleB=(ib>1.12*stallB)
        fa=idx[(z[idx]>1.02)&eligibleA]
        if len(fa):
            burstsA[fa]+=1; second_burst_A[fa]|=burstsA[fa]>=2
            new=fa[first[fa]==0]; first[new]=1; first_cycle[new]=cyc
            base.firing_burst(da,db,weapons,effects,stB,fa,z[fa],rng,ammoA,roundsA,hitsA); z[fa]*=.28
            # Post-shot policy persists for ~8 seconds.
            timerA[fa]=3; postA[fa]+=1
        base.evolve_damage(stB,db,fa,rng)
        newly=fa[stB['mission'][fa]&alive[fa]] if len(fa) else np.array([],int)
        if len(newly): outcome[newly]=1; alive[newly]=False
        idx2=np.where(alive)[0]
        # Re-index z conditions directly in global arrays.
        if len(idx2):
            ib2=dyn_metrics(pb,hB[idx2],tasB[idx2])['ias']; eligibleB2=ib2>1.12*stallB
            fb=idx2[(z[idx2]<-1.02)&eligibleB2]
        else: fb=np.array([],int)
        if len(fb):
            burstsB[fb]+=1; second_burst_B[fb]|=burstsB[fb]>=2
            new=fb[first[fb]==0]; first[new]=-1; first_cycle[new]=cyc
            base.firing_burst(db,da,weapons,effects,stA,fb,-z[fb],rng,ammoB,roundsB,hitsB); z[fb]*=.28
            timerB[fb]=3; postB[fb]+=1
        base.evolve_damage(stA,da,fb,rng)
        newly=fb[stA['mission'][fb]&alive[fb]] if len(fb) else np.array([],int)
        if len(newly): outcome[newly]=-1; alive[newly]=False
        # Dynamic disengagement. Extending after a shot is now a real use of residual energy.
        if cyc>=7:
            ix=np.where(alive)[0]
            if len(ix):
                eAg=g*hA[ix]+.5*(tasA[ix]/3.6)**2; eBg=g*hB[ix]+.5*(tasB[ix]/3.6)**2
                relv=(tasA[ix]-tasB[ix])/100.0
                escA=.65*relv+.65*np.tanh((eAg-eBg)/9000)+.55*math.log(pa.dive/pb.dive)
                desireA=(timerA[ix]>0)&((policyA=='extend')|((policyA=='auto')&(postA[ix]>0)&(z[ix]<.35)))
                pA=np.clip((escA-.10)*.07,0,.16)
                take=desireA&(rng.random(len(ix))<pA); ai=ix[take]; outcome[ai]=2; alive[ai]=False
                ix=np.where(alive)[0]
                if len(ix):
                    eAg=g*hA[ix]+.5*(tasA[ix]/3.6)**2; eBg=g*hB[ix]+.5*(tasB[ix]/3.6)**2
                    relv=(tasB[ix]-tasA[ix])/100.0
                    escB=.65*relv+.65*np.tanh((eBg-eAg)/9000)+.55*math.log(pb.dive/pa.dive)
                    desireB=(timerB[ix]>0)&((policyB=='extend')|((policyB=='auto')&(postB[ix]>0)&(z[ix]>-.35)))
                    pB=np.clip((escB-.10)*.07,0,.16)
                    take=desireB&(rng.random(len(ix))<pB); bi=ix[take]; outcome[bi]=-2; alive[bi]=False
    dA=base.damage_summary(stA); dB=base.damage_summary(stB)
    eAf=g*hA+.5*(tasA/3.6)**2; eBf=g*hB+.5*(tasB/3.6)**2
    denom=max(1,((outcome==1)|(outcome==-1)).sum())
    active_cycles=max(1,action_counts_A.sum())
    return dict(
      A_kill=float((outcome==1).mean()),B_kill=float((outcome==-1).mean()),double_terminal=float((outcome==3).mean()),
      A_diseng=float((outcome==2).mean()),B_diseng=float((outcome==-2).mean()),timeout=float((outcome==0).mean()),
      A_missionloss_share=float((outcome==1).sum()/denom),
      A_firstshot=float((first==1).mean()),B_firstshot=float((first==-1).mean()),no_firstshot=float((first==0).mean()),
      A_second_burst=float(second_burst_A.mean()),B_second_burst=float(second_burst_B.mean()),
      burstsA=float(burstsA.mean()),burstsB=float(burstsB.mean()),roundsA=float(roundsA.mean()),roundsB=float(roundsB.mean()),hitsA=float(hitsA.mean()),hitsB=float(hitsB.mean()),
      A_any_hit=float(stA['ever_hit'].mean()),B_any_hit=float(stB['ever_hit'].mean()),
      A_damaged_returnable=float(((dA>.08)&(~stA['mission'])&(outcome!=1)).mean()),B_damaged_returnable=float(((dB>.08)&(~stB['mission'])&(outcome!=-1)).mean()),
      A_mean_damage=float(dA.mean()),B_mean_damage=float(dB.mean()),
      A_energy_initial=float(np.mean(eA0)),B_energy_initial=float(np.mean(eB0)),A_energy_final=float(np.mean(eAf)),B_energy_final=float(np.mean(eBf)),
      A_final_alt_m=float(np.mean(hA)),B_final_alt_m=float(np.mean(hB)),A_final_tas_kmh=float(np.mean(tasA)),B_final_tas_kmh=float(np.mean(tasB)),
      mean_firstshot_time_s=float(np.mean(first_cycle[first_cycle>=0])*dt if np.any(first_cycle>=0) else math.nan),
      action_share_A={ACTION_NAMES[i]:float(action_counts_A[i]/active_cycles) for i in range(5)},
      action_share_B={ACTION_NAMES[i]:float(action_counts_B[i]/max(1,action_counts_B.sum())) for i in range(5)},
      policyA=policyA,policyB=policyB,initial_attack_A=bool(initial_attack_A),dt_s=dt,max_time_s=dt*max_cycles
    )

def load_all(root='.'):
    root=Path(root)
    return base.load_all(root/'profiles_v03.json',root/'weapons_v02.json',root/'aircraft_damage_v02.json')

if __name__=='__main__':
    p,w,e,d=load_all(Path(__file__).parent)
    r=simulate_dynamic(p['JP05'],p['US02'],d['JP05'],d['US02'],w,e,3000,3000,400,400,ntr=2000,seed=44)
    print(json.dumps(r,ensure_ascii=False,indent=2))
