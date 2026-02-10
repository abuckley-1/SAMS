
import json, os
from evidence_normaliser import normalise
from iso_scoring import score_iso_clause
from rm3_scoring import score_rm3_area
from timestamp_signer import sign_payload

OUTPUT_DIR = os.path.join('dashboard','output')
os.makedirs(OUTPUT_DIR, exist_ok=True)

# --- SAMPLE INPUTS (EXAMPLES ONLY) ---
# In production, these would be built from real checks and policy outputs.
iso_inputs = [
    {'id':'QMS-9.2','evidence_ok': True, 'coverage': 0.92, 'excellence': False},
    {'id':'EMS-6.1.2','evidence_ok': True, 'coverage': 0.70, 'excellence': False},
    {'id':'OHS-6.1.2.1','evidence_ok': False, 'coverage': 0.40, 'excellence': False}
]

rm3_inputs = [
    ('SP','5'), # excellence
    ('OP','3'), # conforming
    ('PI','2')  # minor NC
]

# --- SCORING ---
iso_scored = [score_iso_clause(i) for i in iso_inputs]
rm3_scored = [score_rm3_area(code, int(level)) for code, level in rm3_inputs]

# --- EVIDENCE ---
evidence = normalise()

# --- SUMMARY SCORES ---
def avg(xs):
    return round(sum(xs)/len(xs),2) if xs else 0

iso_score = avg([i['score'] for i in iso_scored])
rm3_score = avg([i['score'] for i in rm3_scored])
overall = round((iso_score*0.6 + rm3_score*0.4),2)

model = {
    'meta': {'note':'EXAMPLE DATA ONLY — replace with production inputs'},
    'scores': {
        'iso_average': iso_score,
        'rm3_average': rm3_score,
        'overall': overall
    },
    'iso': iso_scored,
    'rm3': rm3_scored,
    'evidence': {
        'counts': {k: len(v) for k,v in evidence.items()}
    },
}

sig = sign_payload(model)
model['signature'] = sig

with open(os.path.join(OUTPUT_DIR,'compliance.json'),'w',encoding='utf-8') as f:
    json.dump(model, f, indent=2)

print('Dashboard JSON generated at dashboard/output/compliance.json')
