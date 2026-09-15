# Lab 01 Set Up Hermes Desktop and Connect MiniMax M3

**Course:** Agentic AI for Video Creation (`C436`)  
**Version:** v2.0  
**Primary deliverable:** setup-evidence.json and redacted diagnostic screenshot

## Objective

Install Hermes Desktop from the official source, configure the MiniMax provider for MiniMax-M3 and prove a tool-capable model handshake without exposing a credential.

## Files

- `hermes-config.example.yaml`
- `minimax-credential-template.md`
- `verify.py`
- `data/setup-checklist.csv`
- `AI-PROMPTS.md` and `AI-PROMPTS.pdf` - identical copy-ready learner prompt resources.
- `evidence/checklist.md` and `evidence/checklist.pdf` - evidence gate.
- `verify.py` - deterministic acceptance verifier.

## Detailed procedure

1. Download official installer
2. Complete Hermes setup
3. Configure MiniMax-M3
4. Run hermes doctor
5. Verify model response
6. Redact evidence

1. Open this lab folder as the current project in Hermes Desktop.
2. Read `AI-PROMPTS.md`; replace only the named placeholders with supplied synthetic values.
3. Ask Hermes to inspect the local files before it proposes a plan.
4. Require a preview before any network, paid-generation, upload or scheduling side effect.
5. Run `python3 verify.py` and retain the PASS output with the requested evidence.

## Acceptance check

Hermes launches; the configured provider is minimax; the model is MiniMax-M3; hermes doctor has no blocking failure; published evidence contains placeholders only.

## Troubleshooting

- If Hermes reports the wrong model, start a new session after selecting `MiniMax-M3`; an existing session may retain its original model.
- If a tool is missing, use the documented deterministic fallback and record the limitation instead of inventing a successful call.
- If a skill is not discovered, check its YAML frontmatter, directory name and `SKILL.md` filename, then restart skill discovery.
- If review or upload is blocked, inspect the exact dependency status and compare the approved payload hash with the current master hash.
- If a trial or quota differs from the course note, record the current live account terms and use the fallback path.

## Safety boundary

Use only supplied or authorized assets. Never paste a MiniMax key, OAuth token or YouTube credential into a prompt, lab file, screenshot or repository. YouTube examples default to `private`; public visibility requires an explicit trainer-supervised decision.
