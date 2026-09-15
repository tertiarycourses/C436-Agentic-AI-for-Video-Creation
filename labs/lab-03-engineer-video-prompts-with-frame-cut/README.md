# Lab 03 Engineer Video Prompts with FRAME-CUT

**Course:** Agentic AI for Video Creation (`C436`)  
**Version:** v2.0  
**Primary deliverable:** prompt-pack.json and prompt-score.csv

## Objective

Transform a vague creative request into portable shot prompts using the FRAME-CUT framework and evaluate them with a deterministic rubric.

## Files

- `data/prompt-cases.csv`
- `starter/frame-cut-template.md`
- `verify.py`
- `solution/prompt-pack-approved.json`
- `AI-PROMPTS.md` and `AI-PROMPTS.pdf` - identical copy-ready learner prompt resources.
- `evidence/checklist.md` and `evidence/checklist.pdf` - evidence gate.
- `verify.py` - deterministic acceptance verifier.

## Detailed procedure

1. Diagnose vague prompt
2. Complete FRAME fields
3. Complete CUT fields
4. Generate shot JSON
5. Score rubric
6. Repair one defect

1. Open this lab folder as the current project in Hermes Desktop.
2. Read `AI-PROMPTS.md`; replace only the named placeholders with supplied synthetic values.
3. Ask Hermes to inspect the local files before it proposes a plan.
4. Require a preview before any network, paid-generation, upload or scheduling side effect.
5. Run `python3 verify.py` and retain the PASS output with the requested evidence.

## Acceptance check

Every shot has all FRAME-CUT fields, one dominant action, one camera move, explicit continuity and negative constraints, and a measurable output check.

## Troubleshooting

- If Hermes reports the wrong model, start a new session after selecting `MiniMax-M3`; an existing session may retain its original model.
- If a tool is missing, use the documented deterministic fallback and record the limitation instead of inventing a successful call.
- If a skill is not discovered, check its YAML frontmatter, directory name and `SKILL.md` filename, then restart skill discovery.
- If review or upload is blocked, inspect the exact dependency status and compare the approved payload hash with the current master hash.
- If a trial or quota differs from the course note, record the current live account terms and use the fallback path.

## Safety boundary

Use only supplied or authorized assets. Never paste a MiniMax key, OAuth token or YouTube credential into a prompt, lab file, screenshot or repository. YouTube examples default to `private`; public visibility requires an explicit trainer-supervised decision.
