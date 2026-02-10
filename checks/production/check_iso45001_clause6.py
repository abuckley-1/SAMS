# ISO 45001 Clause 6 – Planning (hazards, risks, legal requirements)

import os, json

def run():
    docs_path = "evidence/docs.json"
    inc_path = "evidence/incidents.json"

    if not os.path.exists(docs_path) or not os.path.exists(inc_path):
        return {
            "id": "OHS-6",
            "coverage": 0.0,
            "category": "MAJOR_NC",
            "details": "Missing hazard/risk/legal requirement evidence.",
            "evidence_used": ["docs.json", "incidents.json"]
        }

    return {
        "id": "OHS-6",
        "coverage": 0.0,
        "category": "MAJOR_NC",
        "details": "Placeholder – implement hazard ID, risk assessment and legal compliance checks.",
        "evidence_used": ["docs.json", "incidents.json"]
    }
