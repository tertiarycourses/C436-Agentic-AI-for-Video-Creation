# AI Prompts for Lab 04

## Primary Hermes prompt

```text
Inspect the supplied tool registry. Recommend Remotion for code-driven branded motion graphics, Manim for explanatory diagrams, Higgsfield for approved generative shots, and FFmpeg for deterministic assembly and probing. Use skill_view before invocation. Return a routing table and do not install or call a paid service without approval.
```

## Planning checkpoint

```text
Before acting, return a concise plan with inputs, files to create or change, tools or skills to invoke, side effects, approval points, acceptance tests and stop conditions. Mark unavailable paid or authenticated services as BLOCKED, not complete.
```

## Independent review prompt

```text
Review the produced artifacts against this criterion: The registry records capability, installation state, auth mode, side effects and fallback; every supplied SKILL.md passes frontmatter and path checks.
Return JSON with observed_values, passed_checks, failed_checks, evidence_paths, security_findings, decision and required_repairs. Do not accept an assertion without opening the named evidence.
```

## Repair prompt

```text
Repair only the failed checks in the review record. Preserve approved inputs and create a new output version rather than overwriting reviewed evidence. Re-run python3 verify.py and stop if any check still fails.
```
