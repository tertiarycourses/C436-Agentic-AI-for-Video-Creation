# AI Prompts for Lab 03

## Primary Hermes prompt

```text
Apply FRAME-CUT. FRAME = Format and finish; Role and references; Assets and action; Motion; Environment and exposure. CUT = Continuity; Unwanted changes; Technical output. Return one JSON object per shot with every field, duration, seed_policy and acceptance_check. Do not imitate a living artist or invent brand facts.
```

## Planning checkpoint

```text
Before acting, return a concise plan with inputs, files to create or change, tools or skills to invoke, side effects, approval points, acceptance tests and stop conditions. Mark unavailable paid or authenticated services as BLOCKED, not complete.
```

## Independent review prompt

```text
Review the produced artifacts against this criterion: Every shot has all FRAME-CUT fields, one dominant action, one camera move, explicit continuity and negative constraints, and a measurable output check.
Return JSON with observed_values, passed_checks, failed_checks, evidence_paths, security_findings, decision and required_repairs. Do not accept an assertion without opening the named evidence.
```

## Repair prompt

```text
Repair only the failed checks in the review record. Preserve approved inputs and create a new output version rather than overwriting reviewed evidence. Re-run python3 verify.py and stop if any check still fails.
```
