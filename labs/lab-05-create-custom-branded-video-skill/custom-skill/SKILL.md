---
name: harbour-bean-video
description: Create a Harbour Bean vertical video from the approved brand profile and supplied assets.
version: 1.0.0
metadata:
  hermes:
    category: video
    tags: [video, governed-production]
---

# harbour-bean-video

## When to use

Use this skill only when the requested video task matches the description and all source assets are authorized.

## Procedure

1. Read `${HERMES_SKILL_DIR}/references/brand-profile.yaml`.
2. Validate the shot plan and authorized assets.
3. Run `${HERMES_SKILL_DIR}/scripts/render_brand_video.py`.
4. Probe the MP4 and return the hash plus brand-review result.

## Safety and verification

- Preview commands and paid or external side effects before execution.
- Never store credentials in `SKILL.md`, scripts, prompts or render logs.
- Write versioned outputs and verify the final media with `ffprobe`.
- Return BLOCKED when a required service, asset, right or approval is unavailable.
