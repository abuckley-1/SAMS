
import json, os
from typing import Dict, Any

"""Normalises raw evidence files into a common JSON structure.
Looks for files in ./evidence such as incidents, training, docs.
Outputs a merged dict to be used by scoring & dashboard builder.
"""

def load_json(path):
    with open(path,'r',encoding='utf-8') as f:
        return json.load(f)


def normalise(evidence_dir='evidence') -> Dict[str, Any]:
    out = {'incidents':[], 'training':[], 'docs':[]}
    # sample loaders with graceful fallbacks
    inc = os.path.join(evidence_dir,'sample_incidents.json')
    if os.path.exists(inc):
        data = load_json(inc)
        out['incidents'] = data if isinstance(data,list) else [data]
    trn = os.path.join(evidence_dir,'sample_training.json')
    if os.path.exists(trn):
        data = load_json(trn)
        out['training'] = data if isinstance(data,list) else [data]
    djs = os.path.join(evidence_dir,'sample_docs.json')
    if os.path.exists(djs):
        data = load_json(djs)
        out['docs'] = data if isinstance(data,list) else [data]
    return out

if __name__=='__main__':
    print(json.dumps(normalise(), indent=2))
