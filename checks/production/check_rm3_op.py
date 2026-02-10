# RM3 – Operational (OP)
# Evidence: incidents.json, docs.json

import os, json

def run():
    inc_path = "evidence/incidents.json"
    docs_path = "evidence/docs.json"

    if not os.path.exists(inc_path) or not os.path.exists(docs_path):
        return {
            "id": "RM3-OP",
            "coverage": 0.0,
            "category": "MAJOR_NC",
            "details": "Missing RM3 OP evidence (risk controls, safe systems of work).",
            "evidence_used": ["incidents.json", "docs.json"]
        }

    return {
        "id": "RM3-OP",
        "coverage": 0.0,
        "category": "MAJOR_NC",
        "details": "Placeholder – implement operational risk control evaluations.",
        "evidence_used": ["incidents.json", "docs.json"]
    }
``
