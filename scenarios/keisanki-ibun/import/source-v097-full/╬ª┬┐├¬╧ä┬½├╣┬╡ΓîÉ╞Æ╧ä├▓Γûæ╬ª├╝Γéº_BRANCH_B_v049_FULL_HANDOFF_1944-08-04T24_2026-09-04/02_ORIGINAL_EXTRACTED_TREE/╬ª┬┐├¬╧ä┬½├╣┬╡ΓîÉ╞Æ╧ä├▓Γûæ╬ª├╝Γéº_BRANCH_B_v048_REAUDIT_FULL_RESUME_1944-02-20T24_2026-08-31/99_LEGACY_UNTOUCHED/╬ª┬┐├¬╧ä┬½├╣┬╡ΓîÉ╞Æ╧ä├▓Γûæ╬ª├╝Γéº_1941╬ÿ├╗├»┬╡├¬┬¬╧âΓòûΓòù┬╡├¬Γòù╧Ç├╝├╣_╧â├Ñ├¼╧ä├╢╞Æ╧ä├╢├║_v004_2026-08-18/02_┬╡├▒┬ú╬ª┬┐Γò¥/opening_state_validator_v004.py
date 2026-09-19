#!/usr/bin/env python3
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / '01_現行正本'

def load(name):
    return json.loads((ROOT / name).read_text(encoding='utf-8'))

def validate():
    errors=[]; warnings=[]; notes=[]
    oob=load('malaya_opening_oob_baseline_v001.json')
    acc=load('prewar_concentration_accounting_v001.json')
    lb=load('malaya_dec8_lower_bound_constraints_v001.json')
    pkt=load('MALAYA_PHASE0_OPENING_PACKET_v003.json')
    reg=load('switch_registry_v010.json')
    state=load('opening_state_1941-12-07_v006.json')
    exe=load('opening_execution_state_v001.json')
    tech=load('opening_technical_clock_guard_v001.json')

    forb=set(oob.get('semantics',{}).get('forbidden',[]))
    if 'subtract_46_concentration_losses_directly_from_dec8_nominal_table' not in forb:
        errors.append('missing semantic ban on direct 46-aircraft subtraction')

    if pkt['pools']['historical_precombat_concentration_loss_unallocated'] != 46:
        errors.append('precombat loss pool must remain 46 unallocated at Phase0')
    if pkt['pools']['southern_army_replacement_shipment_1_unallocated'] != 148:
        errors.append('first replacement shipment must remain 148 unallocated at Phase0')

    hc=acc['historical_constraints']
    expected={
      'concentration_aircraft_losses_bad_weather':46,
      'campaign_post_outbreak_aircraft_losses_to_singapore_fall':331,
      'campaign_replacement_aircraft_total':270,
      'southern_army_replacement_first_shipment_from_mid_november':148,
      'campaign_personnel_losses':582,
      'campaign_officer_losses':73,
    }
    for k,v in expected.items():
        if hc.get(k)!=v: errors.append(f'accounting constraint drift {k}: {hc.get(k)} != {v}')

    cons={c['id']:c for c in lb['constraints']}
    if cons['LB-3AB-597590']['serviceable_at_sortie_min'] != 53:
        errors.append('3AB lower bound not 53')
    if cons['LB-7AB-64126098']['serviceable_at_sortie_min'] != 93:
        errors.append('7AB lower bound not 93')

    units={u['unit']:u for u in oob['units']}
    s3=sum(units[x]['primary']['total'] for x in ['59th Sentai','75th Sentai','90th Sentai'])
    s7=units['64th Sentai']['primary']['total'] + units['12th Sentai']['primary']['total'] + units['98th Sentai']['primary']['total'] + units['60th Sentai']['secondary']['total']
    if s3 != 72: errors.append(f'3AB nominal sum drift: {s3} != 72')
    if s7 != 149: errors.append(f'7AB nominal helper sum drift: {s7} != 149')
    if 53 > s3 or 93 > s7: errors.append('observed launch lower bound exceeds working nominal ceiling')

    intervals={x['id']:x for x in exe['malaya']['participant_serviceable_intervals']}
    if (intervals['3AB-59-75-90']['serviceable_eve_min'], intervals['3AB-59-75-90']['serviceable_eve_max_working']) != (53,72):
        errors.append('3AB execution interval drift')
    if (intervals['7AB-64-12-60-98']['serviceable_eve_min'], intervals['7AB-64-12-60-98']['serviceable_eve_max_working']) != (93,149):
        errors.append('7AB execution interval drift')
    for x in intervals.values():
        if x.get('point_estimate') is not None:
            errors.append(f"{x['id']}: point estimate must remain null until evidence closes it")

    ids={s['id']:s for s in reg['switches']}
    for sid,st in pkt['opening_switches'].items():
        if sid not in ids: errors.append(f'packet switch missing from registry: {sid}')
        elif ids[sid].get('state_at_start') != st:
            errors.append(f'switch state mismatch {sid}: packet={st}, registry={ids[sid].get("state_at_start")}')
    for sid,st in state['switches_opening'].items():
        if sid in ids and ids[sid].get('state_at_start') != st:
            errors.append(f'opening state / registry mismatch {sid}: state={st}, registry={ids[sid].get("state_at_start")}')

    required={
      'A-SKILL-LEVELING':'LATENT',
      'A-DELIBERATE-VETERAN-NUCLEUS-REALLOCATION':'LATENT',
      'A-NATURAL-RETURN':'ON',
      'TECH-THRUST-EXHAUST':'TEST'
    }
    for sid,st in required.items():
        if ids.get(sid,{}).get('state_at_start') != st:
            errors.append(f'{sid} opening state must be {st}')

    guard=next((g for g in tech['guards'] if g['id']=='TECH-THRUST-EXHAUST'),None)
    if not guard: errors.append('missing TECH-THRUST-EXHAUST guard')
    else:
        if guard['opening_state_required']!='TEST': errors.append('thrust-exhaust guard opening state not TEST')
        if guard['opening_mass_standardization_allowed'] is not False: errors.append('thrust-exhaust mass standardization must be banned at opening')

    alt=sum((u.get('primary') or {}).get('type1',0) or 0 for u in oob['units'])
    if alt != 56: errors.append(f'Type1 candidate slots drift: {alt} != 56')
    if pkt['alternate_mapping_working']['historical_Type1_slots_59th_64th'] != alt:
        errors.append('packet Type100 substitution slots mismatch OOB')

    for e in pkt['known_dec7_inner_events']:
        if e.get('membership_in_46') not in {'possible','not_loss'}:
            warnings.append(f'Dec7 event membership not normalized: {e}')

    notes.append(f'3AB executable serviceable interval = [53,{s3}]')
    notes.append(f'7AB executable serviceable interval = [93,{s7}]')
    notes.append('unknown pools remain unallocated; opening can execute as interval state')
    notes.append('TECH-THRUST-EXHAUST opening state = TEST; no 1941 mass-standardization bonus')
    return errors,warnings,notes

if __name__=='__main__':
    e,w,n=validate()
    print(f'errors={len(e)} warnings={len(w)}')
    for x in e: print('ERROR:',x)
    for x in w: print('WARN:',x)
    for x in n: print('NOTE:',x)
    raise SystemExit(1 if e else 0)
