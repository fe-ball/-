#!/usr/bin/env python3
"""Reproduce Stage3A arithmetic. Historical aggregates and conditional examples are separate.
Usage: python BRANCH_B_SUBMARINE_STAGE3A_CALCULATE_v001.py --output result.json
Python3.10+; standard library only. No random draws and no campaign outcome override.
"""
from __future__ import annotations
import argparse, json, math
from pathlib import Path

def probability(x: float) -> float:
    if not 0 <= x <= 1: raise ValueError('probability must be in [0,1]')
    return x

def technical_reliability(q_run: float, q_fuze_given_valid_hit: float, reduction: float) -> dict:
    """Factorization is conditional: not a claim that all weapon failures are independent."""
    q_run=probability(q_run); q_fuze_given_valid_hit=probability(q_fuze_given_valid_hit)
    reduction=probability(reduction)
    before=(1-q_run)*(1-q_fuze_given_valid_hit)
    after=(1-q_run*(1-reduction))*(1-q_fuze_given_valid_hit*(1-reduction))
    return dict(before=before,after=after,relative_change=after/before-1)

def common_solution_salvo(n: int, probability_good_solution: float, conditional_success_per_torpedo: float) -> float:
    """Illustrative two-state shared-error model; bad-solution state assumed to miss all.
    Conditional independence inside good state is an illustration, not calibratedIJNphysics.
    Output is chance>=1damaginghit, NOT chance of sinking.
    """
    if n < 1: raise ValueError('positive salvo size required')
    g=probability(probability_good_solution); p=probability(conditional_success_per_torpedo)
    return g*(1-(1-p)**n)

def main() -> None:
    ap=argparse.ArgumentParser(); ap.add_argument('--output',type=Path); args=ap.parse_args()
    here=Path(__file__).resolve().parent
    patrols=json.loads((here/'BRANCH_B_SUBMARINE_STAGE3A_PATROLS_v001.json').read_text(encoding='utf8'))
    events=json.loads((here/'BRANCH_B_SUBMARINE_STAGE3A_EVENTS_v001.json').read_text(encoding='utf8'))
    a=[p for p in patrols if p['cohort']=='A']; b=[p for p in patrols if p['cohort']=='B']
    eb=[e for e in events if e['boat'] in {'I-11','I-175'}]
    obs={'A_reported_patrol_days':sum(p['reported_patrol_days'] for p in a),
         'B_reported_patrol_days':sum(p['reported_patrol_days'] for p in b),
         'B_recorded_attack_events':len(eb),
         'B_ship_total_losses':sum(e['outcome_normalized'] in {'sunk','total_loss_after_damage'} for e in eb),
         'B_damaged_not_lost':sum(e['outcome_normalized']=='damaged' for e in eb),
         'B_missed_attacks':sum(e['outcome_normalized']=='miss' for e in eb),
         'B_claimed_sinkings':sum(e.get('claimed_outcome')=='sunk' for e in eb),
         'on_station_days':None,'torpedoes_fired_complete':None,'absolute_torpedo_failure_rate':None}
    assert obs['A_reported_patrol_days']==232 and obs['B_reported_patrol_days']==99
    assert obs['B_recorded_attack_events']==9
    assert obs['B_ship_total_losses']==5 and obs['B_damaged_not_lost']==1 and obs['B_missed_attacks']==3
    assert obs['B_claimed_sinkings']==8
    b1={'range_delta':15100/14000-1,'same_fuel_burn_per_nm_reduction':1-14000/15100,
        'submerged_endurance_hours_before':99/3,'submerged_endurance_hours_after':107/3,
        'submerged_endurance_added_hours':8/3,
        'surface_speed_cubic_power_change_if_coefficient_fixed':(22.4/22)**3-1,
        'dive_time_change':44/50-1,
        'status':'arithmetical_implications_of_legacy_hypotheses_NOT_new_measured_capabilities'}
    residual=[]
    for transit in [5000,8000,10000]:
        before=14000-transit; after=15100-transit
        residual.append({'roundtrip_transit_nm_at_same_test_condition':transit,
                         'remaining_equivalent_nm_before':before,'remaining_equivalent_nm_after':after,
                         'remaining_range_budget_increase':after/before-1,
                         'assumptions':'samefuel,16kt-equivalent budget,noadditionalreserve; remainingrangeNOTliters; NOTpatrol-durationprediction'})
    # Conditional availability example. May not be substituted for historical rates.
    abort=.2; lost=15.; preventable=.5; reduction=.3
    abort_gain=abort*lost*preventable*reduction
    # Conditional average long-run cycle utilization. Finite campaign must schedule individual boats.
    cycles=[]
    for station,other in [(40,40),(45,40),(45,36)]:
        cycles.append({'station_days':station,'nonstation_cycle_days':other,
                       'station_days_per_100_calendar_days_longrun':100*station/(station+other),
                       'status':'CONDITIONAL_EXAMPLE_NOT_CALIBRATION'})
    rel=technical_reliability(.15,.10,.20)
    salvos=[]
    good=.65; conditional_hit=.45*rel['before']
    for n in [1,2,3]:
        p=common_solution_salvo(n,good,conditional_hit)
        salvos.append({'torpedoes_per_attack':n,'p_at_least_one_damaging_hit':p,
                       'max_engagements_with_20_torpedoes':20//n,
                       'expected_damaging_hit_engagements_if_4_available':min(4,20//n)*p,
                       'expected_damaging_hit_engagements_if_12_available':min(12,20//n)*p,
                       'status':'CONDITIONAL_EXAMPLE; not historicalsalvodoctrine; not shipkills'})
    shipping={'loss_tons_per23daycycle':404619-373967,
              'relative_output_reduction':1-373967/404619,
              'identical_capacity_increase_to_restore_output':404619/373967-1,
              'approx_tons_perday_gap':(404619-373967)/23,
              'status':'calculation from reported estimate; not pure causal attribution orBranchincrement'}
    out={'schema':'Stage3A_v001','historical_observations':obs,'B1_legacy_consistency':b1,
         'conditional_residual_range_budget':residual,'conditional_machinery_station_days_saved_per_sortie':abort_gain,
         'conditional_cycle_examples':cycles,'conditional_torpedo_technical_reliability':rel,
         'conditional_common_error_salvos':salvos,'historical_report_shipping_arithmetic':shipping,
         'campaign_clock_advanced':False,'legacy_final_kill_band_revalidated':False}
    encoded=json.dumps(out,ensure_ascii=False,indent=2)+'\n'
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True); args.output.write_text(encoded,encoding='utf8')
    else: print(encoded,end='')
if __name__=='__main__': main()
