
import hashlib, time, json
from typing import Any

def sign_payload(payload: Any) -> dict:
    raw = json.dumps(payload, sort_keys=True).encode('utf-8')
    digest = hashlib.sha256(raw).hexdigest()
    return {'signed_at_utc': int(time.time()), 'sha256': digest}

if __name__=='__main__':
    print(sign_payload({'example':True}))
