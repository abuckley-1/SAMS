
import json
from typing import Dict, Any, List

"""Fuses policy results + check outputs + evidence into a single model for scoring."""

def fuse(policy_results: Dict[str, Any], check_results: List[Dict[str,Any]], evidence: Dict[str,Any]) -> Dict[str, Any]:
    return {
        'policy': policy_results,
        'checks': check_results,
        'evidence': evidence
    }

if __name__=='__main__':
    # demo
    print(json.dumps(fuse({'demo':True}, [{'id':'QMS-9.2','ok':True}], {'incidents':[]}), indent=2))
