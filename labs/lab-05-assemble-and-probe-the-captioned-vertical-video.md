# Lab 5 — Assemble and Probe the Captioned Vertical Video

**Course:** Agentic AI for Video Creation  
**Course Code:** C436  
**Version:** v1.0 (29 July 2026)  
**Topic 3:** Editing and Assembling Videos with AI  
**Maps to:** LO3: assemble a reproducible short-form video with captions, branding, and technical evidence  
**Duration:** 60 minutes  
**Tools:** PowerShell, FFmpeg, FFprobe, supplied assembly script

---

## Goal

Render a 9:16 draft from approved checkpoint files and prove its technical properties.

## What You Will Do

You will use the supplied PowerShell and FFmpeg assembly path to verify the accepted manifest sources, create deterministic scene clips, add narrated audio and a muxed WebVTT-derived caption track. You will then probe the draft and save machine-readable technical evidence.

## What You Will Build

A vertical-draft-v1.mp4, captions-v1.vtt, edit-decision-list.json, ffprobe-v1.json, render-log-v1.txt, and render-evidence-v1.json in stage folder 03-edit.

## Prerequisites

- Complete Lab 4 or restore the approved placeholder asset pack.
- If FFmpeg is missing on Windows, run winget install --id Gyan.FFmpeg -e; on macOS, run brew install ffmpeg. Reopen the terminal.
- Run ffmpeg -version and ffprobe -version successfully before assembly.
- Confirm labs/assets/assemble-harbour-bean.ps1 and the Lab 3 captions-script-v1.vtt are present. If installation is not possible, use the supplied labs/assets/rejoin/lab-05 draft and probe package.

> **Data note.** Use only the supplied synthetic campaign data and approved accounts. Store secrets in managed credentials, keep public publishing disabled, and obtain human approval before any external release action.

## Steps

### 1. Create the edit checkpoint and copy the controlled inputs

```text
New-Item -ItemType Directory -Force -Path C436-work/HB-001/03-edit/input/media,C436-work/HB-001/03-edit/output | Out-Null
Copy-Item -Recurse -Force C436-work/HB-001/02-create/media/* C436-work/HB-001/03-edit/input/media/
Copy-Item C436-work/HB-001/02-create/asset-manifest.csv C436-work/HB-001/03-edit/input/asset-manifest.csv
Copy-Item C436-work/HB-001/02-create/narration.txt C436-work/HB-001/03-edit/input/narration.txt
Copy-Item labs/assets/narration-fallback.wav C436-work/HB-001/03-edit/input/narration-fallback.wav
Copy-Item C436-work/HB-001/02-create/captions-script-v1.vtt C436-work/HB-001/03-edit/captions-v1.vtt
Copy-Item labs/assets/edit-decision-list-approved.json C436-work/HB-001/03-edit/edit-decision-list.json
```

### 2. Validate the edit decision list

```text
Get-Content -Raw C436-work/HB-001/03-edit/edit-decision-list.json | ConvertFrom-Json | Select-Object run_id,version,target_duration_seconds,width,height,frame_rate | Format-List
```

### 3. Inspect the caption header and cues

```text
Get-Content C436-work/HB-001/03-edit/captions-v1.vtt | Select-Object -First 20
```

### 4. Run the deterministic assembly script

```text
PowerShell -ExecutionPolicy Bypass -File labs/assets/assemble-harbour-bean.ps1 -ProjectRoot C436-work/HB-001/03-edit
```

### 5. Confirm the expected render files exist

```text
Get-Item C436-work/HB-001/03-edit/output/vertical-draft-v1.mp4,C436-work/HB-001/03-edit/output/render-log-v1.txt | Select-Object Name,Length,LastWriteTime
```

### 6. Probe the rendered video to JSON

```text
ffprobe -v quiet -print_format json -show_format -show_streams C436-work/HB-001/03-edit/output/vertical-draft-v1.mp4 | Set-Content C436-work/HB-001/03-edit/output/ffprobe-v1.json
```

### 7. Bind the actual MP4, probe, captions, and log into render evidence

```text
PowerShell -ExecutionPolicy Bypass -File labs/assets/write-render-evidence.ps1 -ProjectRoot C436-work/HB-001/03-edit -Version v1
```

### 8. Run the fail-closed Lab 5 validator and retain technical evidence

```text
PowerShell -ExecutionPolicy Bypass -File labs/assets/validate-lab-checkpoint.ps1 -Lab 5 2>&1 | Tee-Object C436-work/HB-001/03-edit/lab-05-test-output.txt
```

### 9. Preview the complete draft with sound on and off

```text
Open C436-work/HB-001/03-edit/output/vertical-draft-v1.mp4 in a local media player. Confirm every scene appears in edit-decision-list order and the visual treatment does not obscure the subject.
```

### 10. Record the assembly decision

```text
Create assembly-approval.md with asset-manifest-v1, edl-v1, script-v1, render-evidence-v1, technical/editorial findings, and Decision=READY_FOR_QUALITY_REVIEW. Then write LAB-CHECKPOINT-05.txt.
```

## Test It

The validator must print LAB-05 PASS. It hashes and inspects the actual MP4, probe, captions, and log; asserts H.264, 1080x1920, 30 fps, yuv420p, 30-second duration, audio/subtitles, ordered VTT, and approval.

## Checkpoint and Rejoin Point

Lab checkpoint 05 is the complete 03-edit stage folder. The block below restores the mutually hashed video, probe, caption, log, and evidence files plus the human assembly decision before running the validator.

```text
Set-Location '<PATH_TO_C436_REPOSITORY>'
$editPath='C436-work/HB-001/03-edit'
$outputPath="$editPath/output"
New-Item -ItemType Directory -Force -Path $outputPath | Out-Null
Copy-Item -LiteralPath labs/assets/rejoin/lab-05/vertical-draft-v1.mp4 -Destination "$outputPath/vertical-draft-v1.mp4" -Force
Copy-Item -LiteralPath labs/assets/rejoin/lab-05/ffprobe-v1.json -Destination "$outputPath/ffprobe-v1.json" -Force
Copy-Item -LiteralPath labs/assets/rejoin/lab-05/render-log-v1.txt -Destination "$outputPath/render-log-v1.txt" -Force
Copy-Item -LiteralPath labs/assets/rejoin/lab-05/render-evidence-v1.json -Destination "$outputPath/render-evidence-v1.json" -Force
Copy-Item -LiteralPath labs/assets/rejoin/lab-05/captions-v1.vtt -Destination "$editPath/captions-v1.vtt" -Force
Copy-Item -LiteralPath labs/assets/assembly-approval-approved.md -Destination "$editPath/assembly-approval.md" -Force
PowerShell -ExecutionPolicy Bypass -File labs/assets/validate-lab-checkpoint.ps1 -Lab 5 -WorkRoot C436-work/HB-001
```

## Troubleshooting

| If this happens | Fix |
|---|---|
| PowerShell cannot find ffmpeg or ffprobe. | Run the exact installer command in the prerequisites, reopen PowerShell, and rerun the version checks. If installation is unavailable, run the complete Checkpoint and Rejoin Point block; it restores all five mutually hashed evidence files and the assembly approval before validation. |
| The render is landscape or square. | Confirm the edit decision list width is 1080 and height is 1920, then remove the incomplete output and rerun the supplied script. |
| The caption cues no longer match the edited timing. | Update the cue times against the final narration and scene order, save a new caption version, and record the change before review. |

## Challenge

Copy the EDL to edit-decision-list-v2.json, change adjacent scene/cue boundaries while preserving 30 seconds, copy captions-v1.vtt to captions-v2.vtt and update those boundaries, then run with -Version v2 -EdlPath C436-work/HB-001/03-edit/edit-decision-list-v2.json.

## Reflection

Which editing operations were safer as deterministic commands than as open-ended agent decisions?

---

[← Lab 4](lab-04-build-the-visual-voiceover-and-music-asset-request-pack.md) · [Lab 6 →](lab-06-run-the-independent-video-review-gate-and-repair-one-finding.md)
