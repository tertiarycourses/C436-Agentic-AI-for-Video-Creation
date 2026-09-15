# AI Prompts for Lab 08

## Primary Hermes prompt

```text
Create a Hermes cron job named Weekly approved video release with schedule 0 9 * * 2 in Asia/Singapore. Attach the harbour-bean-video skill. The job must select only APPROVED packages, verify hash and idempotency, upload private, and write a receipt. Create it paused, trigger one dry run, and report next_run_at. Never edit jobs.json directly.
```

## Planning checkpoint

```text
Before acting, return a concise plan with inputs, files to create or change, tools or skills to invoke, side effects, approval points, acceptance tests and stop conditions. Mark unavailable paid or authenticated services as BLOCKED, not complete.
```

## Independent review prompt

```text
Review the produced artifacts against this criterion: The schedule and timezone are explicit, the prompt is self-contained, the custom skill is attached, the job begins paused, and the dry run cannot publish an unapproved or duplicate video.
Return JSON with observed_values, passed_checks, failed_checks, evidence_paths, security_findings, decision and required_repairs. Do not accept an assertion without opening the named evidence.
```

## Repair prompt

```text
Repair only the failed checks in the review record. Preserve approved inputs and create a new output version rather than overwriting reviewed evidence. Re-run python3 verify.py and stop if any check still fails.
```
