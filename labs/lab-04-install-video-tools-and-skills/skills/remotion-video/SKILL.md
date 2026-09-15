---
name: remotion-video
description: Render a governed code-driven video with Remotion.
version: 1.0.0
metadata:
  hermes:
    category: video
    tags: [video, governed-production]
---

# remotion-video

## When to use

Use this skill only when the requested video task matches the description and all source assets are authorized.

## Procedure

1. Read the approved video specification and input props.
2. Preview the composition and compare durationFrames divided by fps to duration_s.
3. Render a versioned MP4.
4. Run ffprobe and write render-evidence.json.

## Safety and verification

- Preview commands and paid or external side effects before execution.
- Never store credentials in `SKILL.md`, scripts, prompts or render logs.
- Write versioned outputs and verify the final media with `ffprobe`.
- Return BLOCKED when a required service, asset, right or approval is unavailable.
