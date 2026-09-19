#!/usr/bin/env python3
"""AIRPOWER6 E5-J / E5-JF local installed audit.

Uses the accepted v40 E5 cooling/pressure/mechanical ledger and the v46
jet/nozzle/free-turbine accounting pattern. This is a local product audit,
not a new generic cheat multiplier and not a historical-calendar correction.
"""
from __future__ import annotations
import csv, math
from pathlib import Path

T0=288.0; P0=101.325; R=.287
CP_A=1.005; GAMMA_A=1.4; CP_G=1.10; GAMMA_G=1.33
PR_C=6.0; ETA_C=.83; INLET_RECOVERY=.99; COMBUSTOR_DP=.035
ETA_COMB=.985; LHV=43000.0; ETA_MAIN_T=.83; ETA_MAIN_MECH=.992
ACCESSORY=1.0; ETA_NOZZLE=.94; FLOW=8.4

def bleedset(vane,rotor,root,seal):
    return [
        {'b':vane,'tap_frac':1.0}, {'b':rotor,'tap_frac':1.0},
        {'b':root,'tap_frac':.75}, {'b':seal,'tap_frac':.55},
    ]
B765=bleedset(.010,.017,.008,.005)     # v40 non-Ni 765 C quantity
B800N=bleedset(.014,.030,.010,.006)    # v40 non-Ni 800 C full
B800NI=bleedset(.010,.018,.008,.004)   # v40 Ni 800 C

def tcomp(Tin,pr=PR_C,eta=ETA_C):
    a=(GAMMA_A-1)/GAMMA_A
    return Tin*(1+(pr**a-1)/eta)

def staged_wc(Tin, bleeds):
    def work(pr): return CP_A*(tcomp(Tin,pr)-Tin)
    btot=sum(x['b'] for x in bleeds)
    wc=(1-btot)*work(PR_C)
    for x in bleeds:
        wc += x['b']*work(PR_C**x['tap_frac'])
    return wc

def nozzle(mdot,Tt,Pt,cp,gamma,Pamb=P0):
    crit=(2/(gamma+1))**(gamma/(gamma-1))
    if Pamb/Pt <= crit:
        pe=Pt*crit
        Ts=Tt*2/(gamma+1)
        v=math.sqrt(ETA_NOZZLE*2*cp*1000*(Tt-Ts))
        Tstat=Tt-v*v/(2*cp*1000)
        rho=pe/(R*Tstat)
        area=mdot/(rho*v)
        F=mdot*v+(pe-Pamb)*1000*area
        return F,v,pe,area,True
    Ts=Tt*(Pamb/Pt)**((gamma-1)/gamma)
    v=math.sqrt(ETA_NOZZLE*2*cp*1000*(Tt-Ts))
    return mdot*v,v,Pamb,0.0,False

def gasgen(tit_c,bleeds,flow=FLOW):
    T2=tcomp(T0); T3=tit_c+273.15
    btot=sum(x['b'] for x in bleeds)
    q=(1-btot)*CP_A*(T3-T2)/ETA_COMB
    f=q/LHV; fuel=flow*f; mg=flow+fuel
    P2=P0*INLET_RECOVERY*PR_C; P3=P2*(1-COMBUSTOR_DP)
    wc=staged_wc(T0,bleeds)
    need=(wc+ACCESSORY)/ETA_MAIN_MECH
    dT=need*flow/(mg*CP_G)
    T4=T3-dT; T4s=T3-dT/ETA_MAIN_T
    P4=P3*(T4s/T3)**(GAMMA_G/(GAMMA_G-1))
    return dict(T2=T2,T3=T3,T4=T4,P4=P4,fuel=fuel,mg=mg,wc=wc,bleed=btot)

def pure_jet(tit_c,bleeds,flow=FLOW):
    g=gasgen(tit_c,bleeds,flow)
    F,v,pe,area,ch=nozzle(g['mg'],g['T4'],g['P4'],CP_G,GAMMA_G)
    kgf=F/9.80665
    return {**g,'thrust_kgf':kgf,'tsfc':g['fuel']*3600/kgf,
            'fuel_kg_h':g['fuel']*3600,'nozzle_v_m_s':v,'nozzle_area_m2':area,
            'nozzle_choked':ch}

def aft_fan(tit_c,bleeds,flow=FLOW,bpr=.9,fpr=1.30,eta_f=.80,eta_ft=.82,
            drive=.97,duct=.96):
    g=gasgen(tit_c,bleeds,flow)
    mb=flow*bpr
    Tfs=T0*fpr**((GAMMA_A-1)/GAMMA_A)
    Tf=T0+(Tfs-T0)/eta_f
    dh=CP_A*(Tf-T0)
    fanp=mb*dh; ftp=fanp/drive
    dT=ftp/(g['mg']*CP_G)
    T5=g['T4']-dT; T5s=g['T4']-dT/eta_ft
    P5=g['P4']*(T5s/g['T4'])**(GAMMA_G/(GAMMA_G-1))
    Fc,*_=nozzle(g['mg'],T5,P5,CP_G,GAMMA_G)
    Pb=P0*INLET_RECOVERY*fpr*duct
    Fb,*_=nozzle(mb,Tf,Pb,CP_A,GAMMA_A)
    kgf=(Fc+Fb)/9.80665
    return {**g,'bpr':bpr,'fpr':fpr,'thrust_kgf':kgf,
            'tsfc':g['fuel']*3600/kgf,'fuel_kg_h':g['fuel']*3600,
            'fan_power_kW':fanp,'free_turbine_power_kW':ftp,
            'core_thrust_kgf':Fc/9.80665,'fan_thrust_kgf':Fb/9.80665}

def fan_geometry(mb, axial_v=110.0, htr=.72, fpr=1.30, eta=.80, psi=.46):
    rho=1.225
    area=mb/(rho*axial_v)
    dtip=math.sqrt(4*area/(math.pi*(1-htr*htr)))
    dhub=htr*dtip
    Tfs=T0*fpr**((GAMMA_A-1)/GAMMA_A)
    Tf=T0+(Tfs-T0)/eta
    dh=CP_A*1000*(Tf-T0)
    U=math.sqrt(dh/psi)
    rpm=60*U/(math.pi*dtip)
    mach=math.sqrt(U*U+axial_v*axial_v)/math.sqrt(GAMMA_A*287*T0)
    return dict(bypass_kg_s=mb,annulus_area_m2=area,tip_diameter_m=dtip,
                hub_diameter_m=dhub,tip_speed_m_s=U,rpm=rpm,tip_relative_mach=mach)

def main():
    out=Path(__file__).parent
    rows=[]
    ratings=[
        ('E5-J-Q-nonNi-765',765,B765),
        ('E5-J-N-nonNi-800',800,B800N),
        ('E5-J-Ni-800-life-hot-high',800,B800NI),
        ('E5-J-M-selected-Ni-830-short-shadow',830,B800NI),
    ]
    for name,t,b in ratings:
        r=pure_jet(t,b)
        rows.append(dict(case=name,kind='pure-J',TIT_C=t,bleed_pct=100*r['bleed'],
                         flow_kg_s=FLOW,bpr='',fpr='',thrust_kgf=r['thrust_kgf'],
                         tsfc_kg_kgfh=r['tsfc'],fuel_kg_h=r['fuel_kg_h'],
                         fan_power_kW='',free_turbine_power_kW=''))
    for tag,t,b in [('E5-JF-Q',765,B765),('E5-JF-N',800,B800N)]:
        for bpr in (.8,.9,1.0):
            r=aft_fan(t,b,bpr=bpr)
            rows.append(dict(case=f'{tag}-BPR-{bpr:.1f}',kind='aft-fan',TIT_C=t,
                             bleed_pct=100*r['bleed'],flow_kg_s=FLOW,bpr=bpr,fpr=1.30,
                             thrust_kgf=r['thrust_kgf'],tsfc_kg_kgfh=r['tsfc'],
                             fuel_kg_h=r['fuel_kg_h'],fan_power_kW=r['fan_power_kW'],
                             free_turbine_power_kW=r['free_turbine_power_kW']))
    with (out/'E5-J-JF-INSTALLED-V8.tsv').open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t'); w.writeheader(); w.writerows(rows)
    grows=[]
    for bpr in (.8,.9,1.0): grows.append({'bpr':bpr,**fan_geometry(FLOW*bpr)})
    with (out/'E5-JF-FAN-GEOMETRY-V8.tsv').open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=list(grows[0]),delimiter='\t'); w.writeheader(); w.writerows(grows)
    for r in rows: print(r)
    for r in grows: print(r)
if __name__=='__main__': main()
