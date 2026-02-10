# ISO 45001 Clause 7 – Support (competence, awareness, communication)

import os, json

def run():
    training_path = "evidence/training.json"
    docs_path = "evidence/docs.json"

    if not os.path.exists(training_path) or not os.path.exists(docs_path):
        return {
            "id": "OHS-7",
            "coverage": 0.0,
            "category": "MAJOR_NC",
            "details": "Missing OH&S training or communication evidence.",
            "evidence_used": ["training.json", "docs.json"]
        }

    return {
        "id": "OHS-7",
        "coverage": 0.0,
        "category": "MAJOR_NC",
        "details": "Placeholder – implement competence & awareness evaluation.",
        "evidence_used": ["training.json", "docs.json"]
    }
