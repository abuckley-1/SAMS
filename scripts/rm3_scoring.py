
import json
from typing import Dict, Any

CATEGORIES = {
    'MAJOR_NC': {'label':'Major Non-Conformance','score':0},
    'MINOR_NC': {'label':'Minor Non-Conformance','score':50},
    'OFI': {'label':'Opportunity for Improvement','score':75},
    'CONFORMING': {'label':'Conforming','score':90},
    'EXCELLENCE': {'label':'Conforming with Excellence','score':100}
}

# RM3 maturity input (1..5) -> category mapping heuristic
MATURITY_TO_CATEGORY = {
    1: 'MAJOR_NC',
    2: 'MINOR_NC',
    3: 'CONFORMING',
    4: 'CONFORMING',
    5: 'EXCELLENCE'
}

def score_rm3_area(area_code: str, maturity_level: int) -> Dict[str, Any]:
    ml = max(1, min(5, int(maturity_level)))
    cat_key = MATURITY_TO_CATEGORY.get(ml, 'OFI')
    cat = CATEGORIES[cat_key]
    return {
        'area': area_code,
        'maturity': ml,
        'category': cat_key,
        'label': cat['label'],
        'score': cat['score']
    }

