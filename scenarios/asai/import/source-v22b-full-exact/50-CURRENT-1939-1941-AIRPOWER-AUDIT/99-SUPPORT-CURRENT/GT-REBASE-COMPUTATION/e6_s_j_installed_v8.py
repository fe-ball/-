#!/usr/bin/env python3
"""AIRPOWER7 E6-S-J local installed-package audit.

Uses the accepted v44 E6 PR7/cooling/mechanical ledger and the v46 pure-jet
nozzle accounting pattern. It closes the S-core pure-jet product package;
it does not re-rate E6-M and does not apply a second cheat multiplier.
"""
from __future__ import annotations
import csv, math
from pathlib import Path
T0=288.0; P0=101.325; R=.287
CP_A=1.005; GA=1.4; CP_G=1.10; GG=1.33
PR=7.0; ETA_C=.84; INLET=.99; DP=.03; ETA_COMB=.985; LHV=43000.0
ETA_T=.84; ETA_MECH=.992; ACCESSORY=1.0; ETA_NOZZLE=.94

def calc(flow,tit_c,bleed):
    T2=T0*(1+(PR**((GA-1)/GA)-1)/ETA_C)
    T3=tit_c+273.15
    # v46-compatible surrogate: staged taps recover enough compressor work
    # that total-bleed sensitivity is slightly below a full-discharge bleed.
    wc=CP_A*(T2-T0)*(1-0.15*bleed)
    q=(1-bleed)*CP_A*(T3-T2)/ETA_COMB
    fuel=flow*q/LHV; mg=flow+fuel
    P3=P0*INLET*PR*(1-DP)
    need=(wc+ACCESSORY)/ETA_MECH
    dT=need*flow/(mg*CP_G)
    T4=T3-dT; T4s=T3-dT/ETA_T
    P4=P3*(T4s/T3)**(GG/(GG-1))
    crit=(2/(GG+1))**(GG/(GG-1))
    pe=P4*crit
    Ts=T4*2/(GG+1)
    v=math.sqrt(ETA_NOZZLE*2*CP_G*1000*(T4-Ts))
    Tstat=T4-v*v/(2*CP_G*1000)
    rho=pe/(R*Tstat)
    area=mg/(rho*v)
    F=mg*v+(pe-P0)*1000*area
    kgf=F/9.80665
    return dict(flow_kg_s=flow,TIT_C=tit_c,bleed_pct=100*bleed,
                thrust_kgf=kgf,TSFC_kg_per_kgfh=fuel*3600/kgf,
                fuel_kg_h=fuel*3600,turbine_exit_Tt_K=T4,
                turbine_exit_Pt_kPa=P4,nozzle_throat_m2=area,
                nozzle_equiv_d_m=math.sqrt(4*area/math.pi),
                nozzle_velocity_m_s=v)

def main():
    out=Path(__file__).parent
    cases=[
      ('C-long-duration',7.8,820,.055),
      ('C-plus-long-life',7.8,835,.0525),
      ('N-intermediate',7.8,850,.051),
      ('N-nonNi-standard',7.8,870,.050),
      ('M-Ni-selected',7.8,890,.0475),
      ('M-Ni-upper',7.8,920,.045),
      ('HF-nonNi-short',8.2,870,.050),
      ('HF-Ni-upper-short',8.2,920,.045),
    ]
    rows=[]
    for name,flow,t,b in cases:
        r=calc(flow,t,b); rows.append({'case':name,**r})
    with (out/'E6-S-J-INSTALLED-V8.tsv').open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t'); w.writeheader(); w.writerows(rows)
    # Physical package ledger. Mass deltas are engineering closure from E5-J baseline
    # plus two axial stages/VIGV/hot-section update; OD remains centrifugal-case driven.
    phys=[
      {'coordinate':'complete_dry_mass_kg','low':400,'center':420,'high':445,'basis':'E5-J 380-415 + 2 axial stages/VIGV/PR7 hot-section and case; newer design partly offsets added hardware'},
      {'coordinate':'maximum_engine_OD_m','low':0.70,'center':0.735,'high':0.77,'basis':'~0.500 m centrifugal impeller at 18 krpm/471 m/s remains diameter driver'},
      {'coordinate':'complete_length_m','low':1.95,'center':2.08,'high':2.22,'basis':'E5-J 1.80-2.05 plus two axial rows, VIGV and PR7 compressor spacing'},
      {'coordinate':'870C_standard_nozzle_throat_m2','low':0.0280,'center':rows[3]['nozzle_throat_m2'],'high':0.0292,'basis':'v46-compatible choked static nozzle calculation'},
      {'coordinate':'920C_standard_nozzle_throat_m2','low':0.0273,'center':rows[5]['nozzle_throat_m2'],'high':0.0285,'basis':'v46-compatible choked static nozzle calculation'},
    ]
    with (out/'E6-S-J-PACKAGE-ENVELOPE-V8.tsv').open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=list(phys[0]),delimiter='\t'); w.writeheader(); w.writerows(phys)
    for r in rows: print(r)
    for r in phys: print(r)
if __name__=='__main__': main()
