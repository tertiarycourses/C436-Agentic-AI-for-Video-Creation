# AI Prompts for Lab 01

## Primary Hermes prompt

```text
Act as my Hermes setup verifier. Inspect only the redacted configuration and diagnostic output I provide. Return JSON with provider, model, doctor_status, missing_requirements, security_findings and next_action. Require model MiniMax-M3. Never ask me to paste an API key.
```

## Planning checkpoint

```text
Before acting, return a concise plan with inputs, files to create or change, tools or skills to invoke, side effects, approval points, acceptance tests and stop conditions. Mark unavailable paid or authenticated services as BLOCKED, not complete.
```

## Independent review prompt

```text
Review the produced artifacts against this criterion: Hermes launches; the configured provider is minimax; the model is MiniMax-M3; hermes doctor has no blocking failure; published evidence contains placeholders only.
Return JSON with observed_values, passed_checks, failed_checks, evidence_paths, security_findings, decision and required_repairs. Do not accept an assertion without opening the named evidence.
```

## Repair prompt

```text
Repair only the failed checks in the review record. Preserve approved inputs and create a new output version rather than overwriting reviewed evidence. Re-run python3 verify.py and stop if any check still fails.
```
