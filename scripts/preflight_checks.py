
import os, sys

REQUIRED = [
    'controls', 'checks', 'policies', 'dashboard', 'evidence', 'scripts'
]

def run():
    missing = [p for p in REQUIRED if not os.path.exists(p)]
    if missing:
        print('Preflight failed; missing:', ', '.join(missing))
        sys.exit(2)
    print('Preflight OK')

if __name__=='__main__':
    run()
