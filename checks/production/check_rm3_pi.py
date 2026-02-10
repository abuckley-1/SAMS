# RM3 – PI (Monitoring, measuring, reviewing performance)
# Evidence: incidents.json, docs.json

import os, json

def run():
    inc_path = "evidence/incidents.json"
    docs_path = "evidence/docs.json"

    if not os.path.exists(inc_path) or not os.path.exists(docs_path):
        return {
            "id": "RM3-PI",
            "coverage": 0.0,
            "category": "MAJOR_NC",
            "details": "Missing RM3 PI evidence (KPIs, monitoring, incident learning).",
            "evidence_used": ["incidents.json", "docs.json"]
        }

    return {
        "id": "RM3-PI",
        "coverage": 0.0,
        "category": "MAJOR_NC",
        "details": "Placeholder – implement KPI trend analysis, audit cycles, incident learning checks.",
        "evidence_used": ["incidents.json", "docs.json"]
    }
``
