#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def load(name):
    with open(ROOT / name, encoding='utf-8') as f:
        return json.load(f)


def validate():
    errors=[]; warnings=[]; notes=[]
    oob=load('malaya_opening_oob_baseline_v001.json')
    acc=load('prewar_concentration_accounting_v001.json')
    lb=load('malaya_dec8_lower_bound_constraints_v001.json')
    pkt=load('MALAYA_PHASE0_OPENING_PACKET_v002.json')
    reg=load('switch_registry_v007.json')

    # semantic bans
    forb=set(oob.get('semantics',{}).get('forbidden',[]))
    if 'subtract_46_concentration_losses_directly_from_dec8_nominal_table' not in forb:
        errors.append('missing semantic ban on direct 46-aircraft subtraction')

    # pools must remain unallocated at Phase0
    if pkt['pools']['historical_precombat_concentration_loss_unallocated'] != 46:
        errors.append('precombat loss pool must remain 46 unallocated at Phase0')
    if pkt['pools']['southern_army_replacement_shipment_1_unallocated'] != 148:
        errors.append('first replacement shipment must remain 148 unallocated at Phase0')

    # lower bound consistency
    cons={c['id']:c for c in lb['constraints']}
    if cons['LB-3AB-597590']['serviceable_at_sortie_min'] != 53:
        errors.append('3rd Air Brigade lower bound not 53')
    if cons['LB-7AB-64126098']['serviceable_at_sortie_min'] != 93:
        errors.append('7th Air Brigade lower bound not 93')

    # recompute nominal sums used in constraints
    units={u['unit']:u for u in oob['units']}
    s3=sum(units[x]['primary']['total'] for x in ['59th Sentai','75th Sentai','90th Sentai'])
    if s3 != 72:
        errors.append(f'3AB nominal sum drift: {s3} != 72')
    # 7AB primary known + secondary-only 60th
    s7=units['64th Sentai']['primary']['total'] + units['12th Sentai']['primary']['total'] + units['98th Sentai']['primary']['total'] + units['60th Sentai']['secondary']['total']
    if s7 != 149:
        errors.append(f'7AB nominal helper sum drift: {s7} != 149')

    if 53 > s3:
        errors.append('3AB observed launch exceeds nominal working sum')
    if 93 > s7:
        errors.append('7AB observed launch exceeds nominal helper sum')

    # known events are explicitly inner/possible, never added to 46 in packet
    for e in pkt['known_dec7_inner_events']:
        if e.get('membership_in_46') not in {'possible','not_loss'}:
            warnings.append(f"Dec7 event membership not normalized: {e}")

    # opening switches present
    ids={s['id']:s for s in reg['switches']}
    for sid,state in pkt['opening_switches'].items():
        if sid not in ids:
            errors.append(f'packet switch missing from registry: {sid}')
        elif ids[sid].get('state_at_start') != state:
            errors.append(f'switch state mismatch {sid}: packet={state}, registry={ids[sid].get("state_at_start")}')

    # no early activation of leveling / deliberate redistribution
    if pkt['opening_switches']['A-SKILL-LEVELING'] != 'LATENT':
        errors.append('skill leveling must not be active at opening')
    if pkt['opening_switches']['A-DELIBERATE-VETERAN-NUCLEUS-REALLOCATION'] != 'LATENT':
        errors.append('deliberate veteran redistribution must not be active at opening')
    if pkt['opening_switches']['A-NATURAL-RETURN'] != 'ON':
        errors.append('natural return tracking must be ON from opening')

    # alternate mapping must not exceed existing Type1 slots
    alt=sum(u.get('primary',{}).get('type1',0) or 0 for u in oob['units'])
    if alt != 56:
        errors.append(f'Type1 candidate slots drift: {alt} != 56')
    if pkt['alternate_mapping_working']['historical_Type1_slots_59th_64th'] != alt:
        errors.append('packet Type100 substitution slots mismatch OOB')

    # administrative calibration pools in source accounting
    hc=acc['historical_constraints']
    expected={'concentration_aircraft_losses_bad_weather':46,'campaign_post_outbreak_aircraft_losses_to_singapore_fall':331,'campaign_replacement_aircraft_total':270,'southern_army_replacement_first_shipment_from_mid_november':148}
    for k,v in expected.items():
        if hc.get(k)!=v:
            errors.append(f'accounting constraint drift {k}: {hc.get(k)} != {v}')

    notes.append(f'3AB working observed/nominal floor = {53/s3:.3f}')
    notes.append(f'7AB working observed/nominal floor = {93/s7:.3f}')
    return errors,warnings,notes

if __name__=='__main__':
    e,w,n=validate()
    print(f'errors={len(e)} warnings={len(w)}')
    for x in e: print('ERROR:',x)
    for x in w: print('WARN:',x)
    for x in n: print('NOTE:',x)
    raise SystemExit(1 if e else 0)
