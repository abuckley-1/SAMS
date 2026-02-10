# ISO 45001 Clause 4 – Context of OH&S system

import json, os

def run():
    docs_path = "evidence/docs.json"
    if not os.path.exists(docs_path):
        return {
            "id": "OHS-4",
            "coverage": 0.0,
            "category": "MAJOR_NC",
            "details": "Missing OH&S context documentation.",
            "evidence_used": ["docs.json"]
        }

    return {
        "id": "OHS-4",
        "coverage": 0.0,
        "category": "MAJOR_NC",
        "details": "Placeholder – implement OH&S context verification.",
        "evidence_used": ["docs.json"]
    }
