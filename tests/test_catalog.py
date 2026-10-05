#!/usr/bin/env python3
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[1]
projects=json.loads((ROOT/'projects/project_catalog.json').read_text())
assert len(projects)==16
assert len({p['id'] for p in projects})==16
assert sum(p['core_runs'] for p in projects)==620
assert {p['tier'] for p in projects}=={'Standard','Intermediate','Advanced'}
for p in projects:
    m=json.loads((ROOT/'projects'/p['id']/'matrix.json').read_text())
    assert m['project_id']==p['id']
    assert len(m['cases'])*len(m['runs'])==p['core_runs'], (p['id'],len(m['cases'])*len(m['runs']),p['core_runs'])
    if m.get('runner')=='common': assert m.get('source')=='btu-calibrated-wifi.cc'
    else:
        assert p['id'] in {'P03','P12','P14','P15'}
        assert m.get('source') is None
print('catalog integrity: PASS')
