---
name: higgsfield-shot
description: Prepare and optionally execute an approved Higgsfield shot request.
version: 1.0.0
metadata:
  hermes:
    category: video
    tags: [video, governed-production]
---

# higgsfield-shot

## When to use

Use this skill only when the requested video task matches the description and all source assets are authorized.

## Procedure

1. Validate the FRAME-CUT prompt and asset rights.
2. Create a request preview without consuming quota.
3. Ask for approval before a paid generation call.
4. Record generation ID, prompt version and review result.

## Safety and verification

- Preview commands and paid or external side effects before execution.
- Never store credentials in `SKILL.md`, scripts, prompts or render logs.
- Write versioned outputs and verify the final media with `ffprobe`.
- Return BLOCKED when a required service, asset, right or approval is unavailable.
