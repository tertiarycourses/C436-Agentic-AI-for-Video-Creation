# Lab 4 — Build the Visual, Voiceover, and Music Asset Request Pack

**Course:** Agentic AI for Video Creation  
**Course Code:** C436  
**Version:** v1.0 (29 July 2026)  
**Topic 2:** Scripting and Generating Content with AI  
**Maps to:** LO2: create structured media-generation requests with continuity, provenance, rights, and fallback controls  
**Duration:** 80 minutes  
**Tools:** n8n, optional approved video/voice tools, supplied placeholder media

---

## Goal

Transform the approved storyboard into generator-ready requests without making paid or external actions mandatory.

## What You Will Do

You will import a deterministic asset-request workflow, generate a continuity bible and one request per storyboard beat, prepare narration and music briefs, and review the resulting asset manifest. Optional live generation is kept outside the required path; supplied placeholder media lets everyone continue.

## What You Will Build

A continuity-bible.json, asset-requests.json, narration.txt, music-brief.md, and asset-manifest.csv with approved placeholders or authorised generated files.

## Prerequisites

- Complete Lab 3 or restore its exact script-storyboard.json, captions-script-v1.vtt, and approval note.
- Confirm labs/assets/asset-request-agent-workflow.json and asset-manifest-template.csv are present.
- If using a live service, store its secret in managed credentials and confirm usage rights and budget with the trainer.

> **Data note.** Use only the supplied synthetic campaign data and approved accounts. Store secrets in managed credentials, keep public publishing disabled, and obtain human approval before any external release action.

## Steps

### 1. Import the asset-request workflow into n8n

```text
In n8n, select Workflows > Create Workflow, open the top-right three-dot menu, choose Import from File, and select labs/assets/asset-request-agent-workflow.json. Rename it C436-HB-001-Asset-Request-Agent and keep it inactive.
```

### 2. Inspect the workflow controls

```text
Confirm the path loads the exact storyboard, validates run_id HB-001 and script_version script-v1, creates one bounded request per beat, caps attempts at 2, and makes zero external actions.
```

### 3. Paste the exact Lab 3 storyboard into the workflow

```text
Open Load Exact Approved Storyboard. Copy the entire contents of C436-work/HB-001/02-create/script-storyboard.json between the storyboardText backticks. Run from Manual Trigger and verify source_fingerprint is non-empty.
```

### 4. Run the workflow and copy the output

```text
Select Test Workflow. Open Emit Asset Pack and copy the complete JSON output to C436-work/HB-001/02-create/asset-requests.json.
```

### 5. Extract the continuity bible

```text
$pack = Get-Content -Raw C436-work/HB-001/02-create/asset-requests.json | ConvertFrom-Json
$pack.continuity_bible | ConvertTo-Json -Depth 8 | Set-Content C436-work/HB-001/02-create/continuity-bible.json
```

### 6. Create the narration file from approved beat text

```text
$story = Get-Content -Raw C436-work/HB-001/02-create/script-storyboard.json | ConvertFrom-Json
($story.beats.narration -join ' ') | Set-Content C436-work/HB-001/02-create/narration.txt
```

### 7. Prepare the music brief

```text
Copy labs/assets/music-brief-template.md C436-work/HB-001/02-create/music-brief.md. Set mood to warm and practical, duration 30 seconds, dialogue priority high, and permitted source to the supplied course-use placeholder or an approved library. Resolve rights_status to approved_for_course_use before acceptance.
```

### 8. Create the asset manifest and register every requested scene

```text
Copy labs/assets/asset-manifest-template.csv C436-work/HB-001/02-create/asset-manifest.csv. Add exactly S01-S05, A01 narration, and A02 music. Every row must be accepted with approved_for_course_use rights. For rejoin, copy asset-manifest-approved.csv.
```

### 9. Use supplied placeholder media for the required path

```text
New-Item -ItemType Directory -Force C436-work/HB-001/02-create/media | Out-Null
Copy-Item -Recurse -Force labs/assets/placeholder-media/* C436-work/HB-001/02-create/media/
```

### 10. Optionally replace one placeholder through an approved service

```text
Before a live call, confirm the provider, prompt, estimated cost, rights basis, and credential are approved. Generate only one bounded candidate, save it in media, and update its manifest row. Never paste a secret into the prompt or file.
```

### 11. Review the complete pack and record the decision

```text
Create asset-pack-approval.md with checks for storyboard coverage, continuity, narration, music rights, provenance, cost, and fallback. Set Decision to APPROVED_FOR_ASSEMBLY, manifest_version=asset-manifest-v1, and approved_by=<YOUR_NAME> only when every required asset is accepted.
```

### 12. Run the fail-closed Lab 4 validator and retain the evidence

```text
PowerShell -ExecutionPolicy Bypass -File labs/assets/validate-lab-checkpoint.ps1 -Lab 4 2>&1 | Tee-Object C436-work/HB-001/02-create/lab-04-test-output.txt
Set-Content C436-work/HB-001/02-create/LAB-CHECKPOINT-04.txt 'Lab 4 passed; asset pack accepted for assembly.'
```

## Test It

The validator must print LAB-04 PASS. It requires the exact S01-S05, A01, and A02 set, correct types, accepted approved-rights status, files, unique IDs, and the human APPROVED_FOR_ASSEMBLY token.

## Checkpoint and Rejoin Point

Lab checkpoint 04 is the complete 02-create stage folder. The rejoin block below restores every required accepted asset, narration, approved music brief, and human assembly decision before validating the checkpoint.

```text
Set-Location '<PATH_TO_C436_REPOSITORY>'
$createPath='C436-work/HB-001/02-create'
if(-not (Test-Path -LiteralPath "$createPath/script-storyboard.json")){throw 'Restore Lab checkpoint 03 first.'}
New-Item -ItemType Directory -Force -Path "$createPath/media" | Out-Null
Copy-Item -LiteralPath labs/assets/asset-manifest-approved.csv -Destination "$createPath/asset-manifest.csv" -Force
Copy-Item -Path labs/assets/placeholder-media/* -Destination "$createPath/media/" -Force
Copy-Item -LiteralPath labs/assets/asset-pack-approval-approved.md -Destination "$createPath/asset-pack-approval.md" -Force
Copy-Item -LiteralPath labs/assets/music-brief-approved.md -Destination "$createPath/music-brief.md" -Force
$story=Get-Content -Raw -LiteralPath "$createPath/script-storyboard.json" | ConvertFrom-Json
($story.beats.narration -join ' ') | Set-Content -LiteralPath "$createPath/narration.txt" -Encoding utf8
PowerShell -ExecutionPolicy Bypass -File labs/assets/validate-lab-checkpoint.ps1 -Lab 4 -WorkRoot C436-work/HB-001
```

## Troubleshooting

| If this happens | Fix |
|---|---|
| The number of asset requests differs from the number of beats. | Check that every beat has a visual_request object and rerun from the workflow trigger without pinned output. |
| A generated file has no usable provenance or rights information. | Mark it rejected, restore the placeholder, and route the rights question to the owner. |
| Narration duration is likely too long. | Read it aloud at a natural pace, shorten the approved script, update script_version, and regenerate only the narration request. |

## Challenge

Add estimated_cost_sgd per request and a deterministic guard that compares the sum with the required cost_budget_sgd from the exact Lab 1 contract.

## Reflection

Why is an accepted placeholder with complete provenance preferable to an impressive generated clip with unresolved rights?

---

[← Lab 3](lab-03-run-the-research-to-script-agent-and-approve-a-timed-storyboard.md) · [Lab 5 →](lab-05-assemble-and-probe-the-captioned-vertical-video.md)
