# AI Prompts for Lab 07

## Primary Hermes prompt

```text
Create Kanban tasks for research, video, review and upload. Link upload to completed review and a human approval task. Keep the upload task blocked unless approval_hash equals master_hash. Build a YouTube videos.insert request with privacyStatus private and containsSyntheticMedia when applicable. Do not publish publicly.
```

## Planning checkpoint

```text
Before acting, return a concise plan with inputs, files to create or change, tools or skills to invoke, side effects, approval points, acceptance tests and stop conditions. Mark unavailable paid or authenticated services as BLOCKED, not complete.
```

## Independent review prompt

```text
Review the produced artifacts against this criterion: The Kanban graph has no missing dependency; review is required; the request points to the approved master; privacy is private; no credential is present in artifacts.
Return JSON with observed_values, passed_checks, failed_checks, evidence_paths, security_findings, decision and required_repairs. Do not accept an assertion without opening the named evidence.
```

## Repair prompt

```text
Repair only the failed checks in the review record. Preserve approved inputs and create a new output version rather than overwriting reviewed evidence. Re-run python3 verify.py and stop if any check still fails.
```
