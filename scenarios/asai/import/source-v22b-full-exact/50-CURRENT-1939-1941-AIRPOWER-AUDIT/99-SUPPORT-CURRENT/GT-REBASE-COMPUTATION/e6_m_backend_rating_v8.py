#!/usr/bin/env python3
from __future__ import annotations
import csv, math
from pathlib import Path
T0=288.;P0=101.325;R=.287;CPA=1.005;GA=1.4;CPG=1.10;GG=1.33
PR=7.;ETA_C=.84;INLET=.99;DP=.03;ETA_COMB=.985;LHV=43000.;ETA_T=.84;ETA_MECH=.992;ACC=1.;ETA_N=.94
FLOW=14.; FAN_PWR=394.3; DRIVE=.97; ETA_FT=.82

def gg(flow,tit,bleed):
    T2=T0*(1+(PR**((GA-1)/GA)-1)/ETA_C); T3=tit+273.15
    wc=CPA*(T2-T0)*(1-.15*bleed)
    q=(1-bleed)*CPA*(T3-T2)/ETA_COMB; fuel=flow*q/LHV; mg=flow+fuel
    P3=P0*INLET*PR*(1-DP); need=(wc+ACC)/ETA_MECH
    dT=need*flow/(mg*CPG); T4=T3-dT; T4s=T3-dT/ETA_T
    P4=P3*(T4s/T3)**(GG/(GG-1))
    return T4,P4,mg,fuel

def nozzle(mdot,Tt,Pt,dp_mult=1.0):
    Pt*=dp_mult
    crit=(2/(GG+1))**(GG/(GG-1)); pe=Pt*crit; Ts=Tt*2/(GG+1)
    v=math.sqrt(ETA_N*2*CPG*1000*(Tt-Ts)); Tstat=Tt-v*v/(2*CPG*1000)
    rho=pe/(R*Tstat); A=mdot/(rho*v); F=mdot*v+(pe-P0)*1000*A
    return F/9.80665,A,v

def jf(tit,bleed,bpr=1.0,fpr=1.30):
    T4,P4,mg,fuel=gg(FLOW,tit,bleed)
    # fixed fan power at accepted FPR/BPR center; governor keeps fan speed/load near design
    ftp=FAN_PWR/DRIVE; dT=ftp/(mg*CPG); T5=T4-dT; T5s=T4-dT/ETA_FT
    P5=P4*(T5s/T4)**(GG/(GG-1))
    # reproduce v46 bypass stream central point as fixed ~267kgf; total trend is dominated by core stream
    # compute bypass nozzle with FPR/duct
    mb=FLOW*bpr; eta_f=.80
    Tfs=T0*fpr**((GA-1)/GA); Tf=T0+(Tfs-T0)/eta_f
    Pb=P0*INLET*fpr*.96
    # generic air nozzle
    crit=(2/(GA+1))**(GA/(GA-1))
    if P0/Pb <= crit:
        pe=Pb*crit; Ts=Tf*2/(GA+1); v=math.sqrt(.94*2*CPA*1000*(Tf-Ts)); Tstat=Tf-v*v/(2*CPA*1000); rho=pe/(R*Tstat); A=mb/(rho*v); Fb=mb*v+(pe-P0)*1000*A
    else:
        Ts=Tf*(P0/Pb)**((GA-1)/GA); v=math.sqrt(.94*2*CPA*1000*(Tf-Ts)); Fb=mb*v
    Fc,Ac,Vc=nozzle(mg,T5,P5)
    total=Fc+Fb/9.80665
    return dict(TIT_C=tit,bleed_pct=100*bleed,thrust_kgf=total,TSFC_kg_per_kgfh=fuel*3600/total,fuel_kg_h=fuel*3600,main_turbine_exit_C=T4-273.15,free_turbine_exit_C=T5-273.15,free_turbine_deltaT_K=dT,free_turbine_power_kW=ftp,fan_power_kW=FAN_PWR)

def reheat(outlet_c,ab_dp=.05,ab_eta=.95):
    T4,P4,mg,fuel=gg(FLOW,870,.05)
    T5=outlet_c+273.15
    add=mg*CPG*(T5-T4)/(ab_eta*LHV)
    mg2=mg+add
    thrust,A,v=nozzle(mg2,T5,P4,dp_mult=1-ab_dp)
    return dict(reheat_outlet_C=outlet_c,thrust_kgf=thrust,thrust_gain_pct=100*(thrust/853.4684456340995-1),total_fuel_kg_h=(fuel+add)*3600,TSFC_kg_per_kgfh=(fuel+add)*3600/thrust,nozzle_throat_m2=A,nozzle_equiv_d_m=math.sqrt(4*A/math.pi),dry_to_wet_throat_area_ratio=A/0.051275175653102974)

def main():
    out=Path(__file__).parent
    jrows=[]
    for name,t,b in [('C-820',820,.054),('C-longlife-835',835,.0525),('N-850',850,.0515),('H-870',870,.05),('Ni-M-890',890,.048),('Ni-E-920',920,.045)]:
        jrows.append({'case':name,**jf(t,b)})
    with (out/'E6-M-JF-RATING-LADDER-V8.tsv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(jrows[0]),delimiter='\t');w.writeheader();w.writerows(jrows)
    rrows=[]
    for t in [900,1000,1050,1100,1150,1200,1300]: rrows.append(reheat(t))
    with (out/'E6-M-J-REHEAT-V8.tsv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rrows[0]),delimiter='\t');w.writeheader();w.writerows(rrows)
    for r in jrows:print(r)
    for r in rrows:print(r)
if __name__=='__main__':main()
