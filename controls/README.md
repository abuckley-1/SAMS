
# Controls Library (Batch 1)

**Generated:** 2026-02-10T12:52:50.575630Z

This folder contains YAML-only control manifests for:
- ISO 9001:2015 (clauses 4–10)
- ISO 14001:2015 (clauses 4–10)
- ISO 45001:2018 (clauses 4–10)
- RM3 (2019): SP, OC, OP, PI, RCS, MRA

> These manifests are paraphrased to avoid reproducing copyrighted text from the standards. They are designed for automation, mapping to checks, evidence collectors, and dashboards.

Structure of each YAML control entry:
```yaml
- id: "QMS-9.2"
  title: "Internal audit"
  intent: "Plan, establish and conduct internal audits."
  criteria:
    - "Audit programme approved"
    - "Findings tracked to closure"
  evidence:
    - "audit_programme.xlsx"
  frequency: "semiannual"
  owner: "Process Owner"
  tags: ["SHEQ", "ISO 9001", "GitHub-Actions"]
```
