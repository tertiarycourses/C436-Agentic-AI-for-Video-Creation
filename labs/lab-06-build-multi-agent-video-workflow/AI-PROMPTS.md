# AI Prompts for Lab 06

## Primary Hermes prompt

```text
Create four specialist roles: researcher, video-producer, independent-reviewer and youtube-uploader. Each role receives exact paths, allowed tools, output schema and done_when. Research and visual preparation may run in parallel; upload depends on verified production, independent review and matching human approval_hash. Return a dependency graph and delegation prompts.
```

## Planning checkpoint

```text
Before acting, return a concise plan with inputs, files to create or change, tools or skills to invoke, side effects, approval points, acceptance tests and stop conditions. Mark unavailable paid or authenticated services as BLOCKED, not complete.
```

## Independent review prompt

```text
Review the produced artifacts against this criterion: All roles have bounded tools and outputs; the reviewer is independent; upload is blocked until all parent evidence and the current approval hash pass.
Return JSON with observed_values, passed_checks, failed_checks, evidence_paths, security_findings, decision and required_repairs. Do not accept an assertion without opening the named evidence.
```

## Repair prompt

```text
Repair only the failed checks in the review record. Preserve approved inputs and create a new output version rather than overwriting reviewed evidence. Re-run python3 verify.py and stop if any check still fails.
```
