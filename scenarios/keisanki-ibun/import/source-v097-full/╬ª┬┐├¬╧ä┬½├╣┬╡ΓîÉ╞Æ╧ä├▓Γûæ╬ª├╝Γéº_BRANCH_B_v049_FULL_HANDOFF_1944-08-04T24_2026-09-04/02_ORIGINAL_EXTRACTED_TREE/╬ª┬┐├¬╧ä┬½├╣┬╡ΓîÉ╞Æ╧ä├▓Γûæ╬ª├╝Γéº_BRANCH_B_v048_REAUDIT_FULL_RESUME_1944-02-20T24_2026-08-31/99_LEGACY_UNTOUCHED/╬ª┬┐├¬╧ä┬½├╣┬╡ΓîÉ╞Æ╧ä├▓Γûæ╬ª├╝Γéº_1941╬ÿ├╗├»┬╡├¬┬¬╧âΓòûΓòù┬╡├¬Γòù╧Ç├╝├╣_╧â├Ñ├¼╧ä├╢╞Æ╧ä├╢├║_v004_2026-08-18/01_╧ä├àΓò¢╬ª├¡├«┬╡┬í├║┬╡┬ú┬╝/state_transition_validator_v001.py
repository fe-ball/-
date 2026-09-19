#!/usr/bin/env python3
"""Minimal conservation validator for campaign event/state ledgers.
Unknown values are allowed. The validator only rejects contradictions in known fields.
"""
import json, sys
from pathlib import Path


def load(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def validate_events(data):
    errors=[]; warnings=[]
    for e in data.get("events",[]):
        o=e.get("observed",{})
        launched=o.get("launched")
        reached=o.get("mission_reached")
        effective=o.get("mission_effective")
        if isinstance(launched,(int,float)):
            if isinstance(reached,(int,float)) and reached>launched:
                errors.append(f"{e['id']}: mission_reached > launched")
            if isinstance(effective,(int,float)) and effective>launched:
                errors.append(f"{e['id']}: mission_effective > launched")
            closed_sum=0; have=False
            for k in ("returned_serviceable","returned_damaged_short","returned_damaged_long","forced_landing","lost","combat_lost"):
                v=o.get(k)
                if isinstance(v,(int,float)):
                    closed_sum += v; have=True
            if have and closed_sum>launched:
                errors.append(f"{e['id']}: known terminal states ({closed_sum}) > launched ({launched})")
        wa=o.get("weather_abort")
        if isinstance(wa,(int,float)) and isinstance(effective,(int,float)) and wa>0 and effective>0 and launched==wa:
            warnings.append(f"{e['id']}: all launched marked weather_abort but mission_effective > 0")
    return errors,warnings


def main():
    if len(sys.argv)!=2:
        print("usage: state_transition_validator_v001.py events.json"); return 2
    data=load(sys.argv[1])
    errors,warnings=validate_events(data)
    for w in warnings: print("WARN",w)
    for e in errors: print("ERROR",e)
    print(f"validated events={len(data.get('events',[]))} errors={len(errors)} warnings={len(warnings)}")
    return 1 if errors else 0

if __name__=='__main__': raise SystemExit(main())
