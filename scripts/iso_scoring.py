
import json
from typing import Dict, Any

CATEGORIES = {
    'MAJOR_NC': {'label':'Major Non-Conformance','score':0},
    'MINOR_NC': {'label':'Minor Non-Conformance','score':50},
    'OFI': {'label':'Opportunity for Improvement','score':75},
    'CONFORMING': {'label':'Conforming','score':90},
    'EXCELLENCE': {'label':'Conforming with Excellence','score':100}
}

# Map boolean/percentage compliance to category
# expected input example: {'id':'QMS-9.2','evidence_ok': True, 'coverage': 0.92, 'excellence': False}

def score_iso_clause(item: Dict[str, Any]) -> Dict[str, Any]:
    coverage = float(item.get('coverage', 0))
    excellence = bool(item.get('excellence', False))
    if not item.get('evidence_ok', False):
        cat = 'MAJOR_NC'
    elif coverage < 0.6:
        cat = 'MINOR_NC'
    elif coverage < 0.85:
        cat = 'OFI'
    elif excellence or coverage >= 0.98:
        cat = 'EXCELLENCE'
    else:
        cat = 'CONFORMING'
    out = {
        'id': item.get('id'),
        'category': cat,
        'label': CATEGORIES[cat]['label'],
        'score': CATEGORIES[cat]['score'],
        'coverage': round(coverage,3),
        'excellence': excellence
    }
    return out
