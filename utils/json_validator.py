
import json

def is_valid_json(path: str) -> bool:
    try:
        with open(path,'r',encoding='utf-8') as f:
            json.load(f)
        return True
    except Exception:
        return False
