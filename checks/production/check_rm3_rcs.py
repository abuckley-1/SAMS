# RM3 – RCS (Risk Control Systems)
# Evidence: docs.json, incidents.json

import os, json

def run():
    docs_path = "evidence/docs.json"
    inc_path = "evidence/incidents.json"

    if not os.path.exists(docs_path) or not os.path.exists(inc_path):
        return {
            "id": "RM3-RCS",
            "coverage": 0.0,
            "category": "MAJOR_NC",
            "details": "Missing RM3 RCS evidence (risk controls, maintenance, inspections).",
            "evidence_used": ["docs.json", "incidents.json"]
        }

    return {
        "id": "RM3-RCS",
        "coverage": 0.0,
        "category": "MAJOR_NC",
        "details": "Placeholder – implement verification of risk control systems and maintenance controls.",
        "evidence_used": ["docs.json", "incidents.json"]
    }
