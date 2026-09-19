from pathlib import Path
import json, subprocess, sys
HERE=Path(__file__).resolve().parent
ROOT=HERE.parent/'01_現行正本'
errors=[]; warnings=[]
def load(n): return json.loads((ROOT/n).read_text(encoding='utf-8'))
required=['AUTHORITATIVE_MANIFEST_v003.json','opening_sync_state_1941-12-07_08_v001.json','pearl_state_transition_v002.json','philippines_opening_events_v001.json','opening_execution_state_v001.json','opening_technical_clock_guard_v001.json','malaya_phase1_events_v001.json']
for n in required:
    if not (ROOT/n).exists(): errors.append(f'missing {n}')
if not errors:
    s=load('opening_sync_state_1941-12-07_08_v001.json')
    p=load('pearl_state_transition_v002.json')
    ph=load('philippines_opening_events_v001.json')
    ex=load('opening_execution_state_v001.json')
    tech=load('opening_technical_clock_guard_v001.json')
    if p['executable_scenario_state']['attacking_aircraft']!=350: errors.append('Pearl executable attack count must remain 350 until event-level recovery is identified')
    if p['executable_scenario_state']['irrecoverable_aircraft_loss']!=29: errors.append('Pearl executable loss must remain 29 until event-level recovery is identified')
    if p['executable_scenario_state']['loss_reduction_credit']!=0: errors.append('Pearl uncalibrated loss credit forbidden')
    if s['theaters']['Malaya']['3AB_59_75_90_serviceable_eve'] != [53,72]: errors.append('Malaya 3AB interval drift')
    if s['theaters']['Malaya']['7AB_64_12_60_98_serviceable_eve'] != [93,149]: errors.append('Malaya 7AB interval drift')
    main=ph['events'][0]['japanese']
    if main['naval_twin_engine_bombers_departed']+main['zeros_escort_departed'] != 192: errors.append('Philippines main strike arithmetic')
    end=ph['events'][2]
    if end['japanese_state']['fighters_lost']!=7 or end['japanese_state']['loss_credit_scenario']!=0: errors.append('Philippines historical shell loss accounting drift')
    if tech['guards'][0]['opening_state_required']!='TEST': errors.append('thrust exhaust opening clock drift')
# run existing validators
for script,args in [('opening_state_validator_v004.py',[]),]:
    cp=subprocess.run([sys.executable,str(HERE/script),*args],capture_output=True,text=True)
    if cp.returncode!=0: errors.append(f'{script} failed: {cp.stdout} {cp.stderr}')
cp=subprocess.run([sys.executable,str(ROOT/'state_transition_validator_v001.py'),str(ROOT/'malaya_phase1_events_v001.json')],capture_output=True,text=True)
if cp.returncode!=0: errors.append(f'state_transition_validator failed: {cp.stdout} {cp.stderr}')
print(f'OPENING_SYNC_VALIDATION errors={len(errors)} warnings={len(warnings)}')
for e in errors: print('ERROR:',e)
for w in warnings: print('WARNING:',w)
if not errors:
    print('OPENING_SYNC_GATE=PASS')
    print('NEXT=1941-12-08..15 Malaya daily; Pearl ship-level and Philippines return/serviceability parallel ledgers')
sys.exit(1 if errors else 0)
