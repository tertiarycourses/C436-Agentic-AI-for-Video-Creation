# Lab 7 — Orchestrate the Private Release Package with Human Approval

**Course:** Agentic AI for Video Creation  
**Course Code:** C436  
**Version:** v1.0 (29 July 2026)  
**Topic 4:** Automating and Scaling Video Production  
**Maps to:** LO4: orchestrate multi-step agents and prepare safe platform-specific publishing actions  
**Duration:** 50 minutes  
**Tools:** n8n, supplied release workflow, reviewed video package

---

## Goal

Build a release-ready package that is blocked until a person approves one scoped private action.

## What You Will Do

You will import a release orchestrator, inspect its state transitions, validate video, caption, metadata, rights, and disclosure fields, then exercise denial and approval paths. The lab creates a dry-run package only; no public account or live posting credential is used.

## What You Will Build

A release-package.json, denied-approval.json, private-release-approval.json, and release-orchestrator-reviewed.json in stage folder 04-release.

## Prerequisites

- Complete Lab 6 or restore Lab checkpoint 06 with final-review-approval.json bound to the reviewed video.
- Confirm labs/assets/release-orchestrator-workflow.json and release-metadata-template.json are present.
- Do not connect a YouTube, TikTok, or other publishing credential during the required lab path.

> **Data note.** Use only the supplied synthetic campaign data and approved accounts. Store secrets in managed credentials, keep public publishing disabled, and obtain human approval before any external release action.

## Steps

### 1. Create the release checkpoint

```text
New-Item -ItemType Directory -Force C436-work/HB-001/04-release | Out-Null
Copy-Item labs/assets/release-metadata-template.json C436-work/HB-001/04-release/release-metadata.json
```

### 2. Complete the release metadata without account secrets

```text
Open release-metadata.json and set title, description, caption_path='02-create/captions-script-v1.vtt', video_path='03-edit/output/vertical-draft-v1.mp4', rights_evidence_path='02-create/asset-manifest.csv', final_review_approval_path='03-edit/final-review-approval.json', and package_owner. Retain typed private/null/true values and public_release_allowed=false.
```

### 3. Build and hash the canonical release package manifest

```text
PowerShell -ExecutionPolicy Bypass -File labs/assets/build-release-package.ps1 -WorkRoot C436-work/HB-001
Get-Content -Raw C436-work/HB-001/04-release/release-package-manifest.json | ConvertFrom-Json | Select-Object run_id,package_version,title,privacy_status,contains_synthetic_media
```

### 4. Import and inspect the release orchestrator

```text
In n8n, create a workflow from labs/assets/release-orchestrator-workflow.json, rename it C436-HB-001-Private-Release-Orchestrator, save it, and keep it inactive. Confirm the states are release_input -> validation -> awaiting_human_approval -> dry_run_ready or denied.
```

### 5. Run the input validation path

```text
Open Load Exact Release Metadata and paste the complete release-metadata.json between the releaseText backticks. Select Test Workflow and inspect Emit Release Package.
```

### 6. Save the awaiting-approval package

```text
Copy the Emit Release Package JSON output to C436-work/HB-001/04-release/release-package.json. Confirm publish_allowed=false and status=awaiting_human_approval.
```

### 7. Exercise the denial path

```text
Edit release-metadata.json to set human_decision='deny' and decision_reason='Controlled lab denial - verify no action'. Repaste the complete file, run, and save the complete output as C436-work/HB-001/04-release/denied-approval.json.
```

### 8. Verify denial causes no external action

```text
$denied = Get-Content -Raw C436-work/HB-001/04-release/denied-approval.json | ConvertFrom-Json
$denied | Select-Object status,publish_allowed,external_action_count
if ($denied.external_action_count -ne 0) { throw 'Denial must cause zero external actions' }
```

### 9. Create a scoped private approval

```text
$path='C436-work/HB-001/04-release/release-metadata.json'
$m=Get-Content -Raw $path | ConvertFrom-Json
$m.human_decision='approve_private_dry_run'; $m.decision_reason='Reviewed exact package for private dry run only'; $m.approval_scope='HB-001; private dry-run request preview; one package; no external execution'; $m.approval_package_sha256=$m.package_sha256; $m.approval_expires_at=[datetimeoffset]::UtcNow.AddHours(8).ToString('o')
$m | ConvertTo-Json -Depth 10 | Set-Content $path
Repaste the complete file into Load Exact Release Metadata and run.
```

### 10. Save and verify the approved dry-run output

```text
Save the final output as C436-work/HB-001/04-release/private-release-approval.json. Confirm dry_run_ready, non-publishing, zero actions, a non-empty idempotency key, and disclosure-complete non-executing platform previews.
```

### 11. Export the reviewed orchestrator

```text
Use n8n Download and save C436-work/HB-001/04-release/release-orchestrator-reviewed.json.
```

### 12. Compare platform requirements

```text
Open labs/assets/platform-release-references.md and inspect the supplied YouTube/TikTok non-executing preview JSON. In release-notes.md, link those official references and distinguish request previews from authorised live calls.
```

### 13. Run the fail-closed Lab 7 validator and retain the evidence

```text
PowerShell -ExecutionPolicy Bypass -File labs/assets/validate-lab-checkpoint.ps1 -Lab 7 2>&1 | Tee-Object C436-work/HB-001/04-release/lab-07-test-output.txt
Set-Content C436-work/HB-001/04-release/LAB-CHECKPOINT-07.txt 'Lab 7 passed; hash-bound private dry-run package retained.'
```

## Test It

The validator must print LAB-07 PASS. It recomputes the canonical package and every video/caption/rights/final-review hash, requires an exact approval hash plus future expiry, and validates zero-action platform previews.

## Checkpoint and Rejoin Point

Lab checkpoint 07 is stored in stage folder C436-work/HB-001/04-release. It contains both decision paths and the private dry-run package. A live integration may be added later only by an authorised owner using current official platform documentation and managed credentials.

## Troubleshooting

| If this happens | Fix |
|---|---|
| The validator reports a missing disclosure decision. | Set contains_synthetic_media explicitly to true or false based on the reviewed content; never leave it implicit. |
| The approved dry run sets publish_allowed=true. | Stop and restore the supplied workflow. This lab never authorises a live public action. |
| The idempotency key changes every time the same package is retried. | Build it from the stable run ID, target, and package checksum rather than the current timestamp. |

## Challenge

Set approval_expires_at to one minute in the past and prove the package is blocked with approval_hash_or_expiry_invalid and zero actions, then restore a future expiry.

## Reflection

Which release fields must a person see together before an approval can be considered informed?

---

[← Lab 6](lab-06-run-the-independent-video-review-gate-and-repair-one-finding.md) · [Lab 8 →](lab-08-analyse-synthetic-performance-and-build-the-scaling-control-plan.md)
