# ISO 14001 Clause 10 (Improvement) – production logic stub
# Evidence: incidents.json, docs.json

import json, os

def run():
    inc_path = "evidence/incidents.json"
    docs_path = "evidence/docs.json"

    if not os.path.exists(inc_path) or not os.path.exists(docs_path):
        return {
            "id": "EMS-10",
            "coverage": 0.0,
            "category": "MAJOR_NC",
            "details": "Missing environmental NCR/CI evidence.",
            "evidence_used": ["incidents.json", "docs.json"]
        }

    return {
        "id": "EMS-10",
        "coverage": 0.0,
        "category": "MAJOR_NC",
        "details": "Placeholder logic – implement corrective action and CI evaluation.",
        "evidence_used": ["incidents.json", "docs.json"]
    }
