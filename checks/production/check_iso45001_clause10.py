# ISO 45001 Clause 10 – Improvement
# Evidence: incidents.json, docs.json
# Covers CAPA, nonconformities, continual improvement.

import os, json

def run():
    inc_path = "evidence/incidents.json"
    docs_path = "evidence/docs.json"

    if not os.path.exists(inc_path) or not os.path.exists(docs_path):
        return {
            "id": "OHS-10",
            "coverage": 0.0,
            "category": "MAJOR_NC",
            "details": "Missing OH&S CAPA or improvement evidence.",
            "evidence_used": ["incidents.json", "docs.json"]
        }

    return {
        "id": "OHS-10",
        "coverage": 0.0,
        "category": "MAJOR_NC",
        "details": "Placeholder – implement NCR/CAPA/CI verification.",
        "evidence_used": ["incidents.json", "docs.json"]
    }
