# RM3 – Organisational Capability (OC)
# Evidence: training.json, docs.json

import os, json

def run():
    training_path = "evidence/training.json"
    docs_path = "evidence/docs.json"

    if not os.path.exists(training_path) or not os.path.exists(docs_path):
        return {
            "id": "RM3-OC",
            "coverage": 0.0,
            "category": "MAJOR_NC",
            "details": "Missing OC evidence (competence, staffing, assurance).",
            "evidence_used": ["training.json", "docs.json"]
        }

    return {
        "id": "RM3-OC",
        "coverage": 0.0,
        "category": "MAJOR_NC",
        "details": "Placeholder – implement organisational capability evaluation.",
        "evidence_used": ["training.json", "docs.json"]
    }
