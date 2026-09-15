# Lab 08 Schedule Controlled Video Publishing with Hermes Cron

**Course:** Agentic AI for Video Creation (`C436`)  
**Version:** v2.0  
**Primary deliverable:** cron-preview.json and operations-ledger.csv

## Objective

Create a paused Hermes cron job that prepares a release from a self-contained prompt, dry-run it, and enable a cadence only after evidence review.

## Files

- `data/cron-job.json`
- `starter/cron-commands.md`
- `starter/release-job-prompt.md`
- `verify.py`
- `AI-PROMPTS.md` and `AI-PROMPTS.pdf` - identical copy-ready learner prompt resources.
- `evidence/checklist.md` and `evidence/checklist.pdf` - evidence gate.
- `verify.py` - deterministic acceptance verifier.

## Detailed procedure

1. Write self-contained job
2. Attach video skill
3. Create paused cron
4. Trigger dry run
5. Inspect next run
6. Approve enablement

1. Open this lab folder as the current project in Hermes Desktop.
2. Read `AI-PROMPTS.md`; replace only the named placeholders with supplied synthetic values.
3. Ask Hermes to inspect the local files before it proposes a plan.
4. Require a preview before any network, paid-generation, upload or scheduling side effect.
5. Run `python3 verify.py` and retain the PASS output with the requested evidence.

## Acceptance check

The schedule and timezone are explicit, the prompt is self-contained, the custom skill is attached, the job begins paused, and the dry run cannot publish an unapproved or duplicate video.

## Troubleshooting

- If Hermes reports the wrong model, start a new session after selecting `MiniMax-M3`; an existing session may retain its original model.
- If a tool is missing, use the documented deterministic fallback and record the limitation instead of inventing a successful call.
- If a skill is not discovered, check its YAML frontmatter, directory name and `SKILL.md` filename, then restart skill discovery.
- If review or upload is blocked, inspect the exact dependency status and compare the approved payload hash with the current master hash.
- If a trial or quota differs from the course note, record the current live account terms and use the fallback path.

## Safety boundary

Use only supplied or authorized assets. Never paste a MiniMax key, OAuth token or YouTube credential into a prompt, lab file, screenshot or repository. YouTube examples default to `private`; public visibility requires an explicit trainer-supervised decision.
