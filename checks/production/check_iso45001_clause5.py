# ISO 45001 Clause 5 – Leadership & worker participation

import json, os

def run():
    docs_path = "evidence/docs.json"
    if not os.path.exists(docs_path):
        return {
            "id": "OHS-5",
            "coverage": 0.0,
            "category": "MAJOR_NC",
            "details": "Missing OH&S policy or leadership evidence.",
            "evidence_used": ["docs.json"]
        }

    return {
        "id": "OHS-5",
        "coverage": 0.0,
        "category": "MAJOR_NC",
        "details": "Placeholder – implement OH&S leadership & consultation evidence checks.",
        "evidence_used": ["docs.json"]
    }
