# ISO 45001 Clause 8 – Operation
# Evidence: incidents.json, docs.json
# Covers operational controls, contractor management, emergency preparedness.

import os, json

def run():
    inc_path = "evidence/incidents.json"
    docs_path = "evidence/docs.json"

    if not os.path.exists(inc_path) or not os.path.exists(docs_path):
        return {
            "id": "OHS-8",
            "coverage": 0.0,
            "category": "MAJOR_NC",
            "details": "Missing operational control or incident evidence.",
            "evidence_used": ["incidents.json", "docs.json"]
        }

    return {
        "id": "OHS-8",
        "coverage": 0.0,
        "category": "MAJOR_NC",
        "details": "Placeholder – implement operational control, contractor mgmt, and EPR verification.",
        "evidence_used": ["incidents.json", "docs.json"]
    }
