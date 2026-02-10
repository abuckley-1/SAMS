# ISO 45001 Clause 9 – Performance Evaluation
# Evidence: docs.json, incidents.json
# Covers audits, monitoring, measurement, analysis, evaluations.

import os, json

def run():
    docs_path = "evidence/docs.json"
    inc_path = "evidence/incidents.json"

    if not os.path.exists(docs_path):
        return {
            "id": "OHS-9",
            "coverage": 0.0,
            "category": "MAJOR_NC",
            "details": "Missing OH&S monitoring or audit evidence.",
            "evidence_used": ["docs.json"]
        }

    return {
        "id": "OHS-9",
        "coverage": 0.0,
        "category": "MAJOR_NC",
        "details": "Placeholder – implement audit programme, monitoring KPI checks, and compliance review.",
        "evidence_used": ["docs.json"]
    }
