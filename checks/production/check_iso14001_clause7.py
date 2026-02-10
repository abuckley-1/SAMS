# ISO 14001 Clause 7 (Support) – production logic stub
# Evidence: training.json, docs.json
# Strict scoring thresholds and graceful fail behaviour.

import json, os

def run():
    training_path = "evidence/training.json"
    docs_path = "evidence/docs.json"

    training_ok = os.path.exists(training_path)
    docs_ok = os.path.exists(docs_path)

    if not training_ok or not docs_ok:
        return {
            "id": "EMS-7",
            "coverage": 0.0,
            "category": "MAJOR_NC",
            "details": "Missing EMS training or documentation evidence.",
            "evidence_used": ["training.json", "docs.json"]
        }

    return {
        "id": "EMS-7",
        "coverage": 0.0,
        "category": "MAJOR_NC",
        "details": "Placeholder logic – implement EMS support verification.",
        "evidence_used": ["training.json", "docs.json"]
    }
