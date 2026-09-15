# AI Prompts for Lab 02

## Primary Hermes prompt

```text
Create a 15-second 1080x1920 MP4 for Harbour Bean using only the supplied brief and assets. First return shot-plan.json with three non-overlapping five-second shots. Then run starter/render_preview.py. Do not use network tools. Stop when verify.py reports PASS and return the output path plus observed ffprobe values.
```

## Planning checkpoint

```text
Before acting, return a concise plan with inputs, files to create or change, tools or skills to invoke, side effects, approval points, acceptance tests and stop conditions. Mark unavailable paid or authenticated services as BLOCKED, not complete.
```

## Independent review prompt

```text
Review the produced artifacts against this criterion: The shot plan is valid JSON, totals 15 seconds, uses only supplied assets, and the generated MP4 passes dimensions, codec and duration checks.
Return JSON with observed_values, passed_checks, failed_checks, evidence_paths, security_findings, decision and required_repairs. Do not accept an assertion without opening the named evidence.
```

## Repair prompt

```text
Repair only the failed checks in the review record. Preserve approved inputs and create a new output version rather than overwriting reviewed evidence. Re-run python3 verify.py and stop if any check still fails.
```
