# Lab 6 — Run the Independent Video Review Gate and Repair One Finding

**Course:** Agentic AI for Video Creation  
**Course Code:** C436  
**Version:** v1.0 (29 July 2026)  
**Topic 3:** Editing and Assembling Videos with AI  
**Maps to:** LO3: review and refine a video through technical, editorial, accessibility, brand, rights, and release gates  
**Duration:** 70 minutes  
**Tools:** n8n, FFprobe evidence, text editor, local media player

---

## Goal

Produce an evidence-linked issue register, repair a controlled defect, and obtain a human release-readiness decision.

## What You Will Do

You will import an n8n review workflow that reads exact technical, caption, and manifest evidence, validates 28–32 seconds plus ordered contiguous cues, creates blocking and advisory findings, and never self-approves. You will inject a controlled defect, verify that the gate blocks, repair the data, rerun, and record the final human decision after watching the complete draft.

## What You Will Build

A review-agent workflow export, issue-register-v1.json, issue-register-v2.json, repair-log.md, and final-review-approval.json.

## Prerequisites

- Complete Lab 5 or restore Lab checkpoint 05 from stage folder 03-edit with a valid draft and probe.
- Confirm labs/assets/video-review-agent-workflow.json and review-rubric.csv are present.
- Keep the review workflow inactive and do not connect publishing tools.

> **Data note.** Use only the supplied synthetic campaign data and approved accounts. Store secrets in managed credentials, keep public publishing disabled, and obtain human approval before any external release action.

## Steps

### 1. Import and rename the review workflow

```text
In n8n, select Workflows > Create Workflow, import labs/assets/video-review-agent-workflow.json, rename it C436-HB-001-Video-Review-Gate, save it, and keep it inactive.
```

### 2. Inspect the gate structure

```text
Confirm it consumes exact FFprobe, WebVTT, and manifest evidence; enforces 28–32 seconds plus five ordered, positive, contiguous cues; keeps approval pending; and never emits release_approved.
```

### 3. Paste exact prior evidence and create a controlled missing-rights case

```text
Open Load Exact Review Evidence. Paste the complete Lab 5 ffprobe-v1.json, Lab 3 captions-script-v1.vtt, and Lab 4 asset-manifest.csv into the three named constants. In only the pasted manifest copy, change S01 rights_status to review_required and save.
```

### 4. Run the blocked review and save its output

```text
Select Test Workflow. Open Emit Issue Register, copy the complete JSON output, and save it to C436-work/HB-001/03-edit/issue-register-v1.json.
```

### 5. Verify the blocking finding

```text
$issues = Get-Content -Raw C436-work/HB-001/03-edit/issue-register-v1.json | ConvertFrom-Json
$issues | Select-Object run_id,review_status,release_allowed
$issues.findings | Format-Table issue_id,category,severity,evidence,required_action
```

### 6. Repair the controlled defect

```text
Return to Load Exact Review Evidence and repaste the unchanged exact Lab 4 asset-manifest.csv. Record the repair in C436-work/HB-001/03-edit/repair-log.md under issue RV-RIGHTS.
```

### 7. Rerun the review and save the clear result

```text
Select Test Workflow again. Save the Emit Issue Register JSON output as C436-work/HB-001/03-edit/issue-register-v2.json.
```

### 8. Verify that automation stops at review clear

```text
$clear = Get-Content -Raw C436-work/HB-001/03-edit/issue-register-v2.json | ConvertFrom-Json
if ($clear.review_status -ne 'review_clear' -or $clear.release_allowed -ne $false -or $clear.owner_approval_status -ne 'pending') { throw 'Automated review did not stop before human approval.' }
```

### 9. Conduct the human full-length review

```text
Watch vertical-draft-v1.mp4 once with sound and once muted. Review the supplied rubric for story, claims, captions, mobile readability, brand, privacy, rights, disclosure, and technical output. Record timecoded observations.
```

### 10. Record the scoped decision

```text
$path='C436-work/HB-001/03-edit/final-review-approval.json'
Copy-Item labs/assets/final-review-approval-template.json $path
$a=Get-Content -Raw $path | ConvertFrom-Json
$a.reviewer='<YOUR_NAME>'; $a.reviewed_at=[datetimeoffset]::UtcNow.ToString('o'); $a.decision='APPROVED_FOR_PRIVATE_RELEASE_PACKAGE'; $a.scope='private release package only; no public posting'; $a.reviewed_video_sha256=(Get-FileHash -Algorithm SHA256 C436-work/HB-001/03-edit/output/vertical-draft-v1.mp4).Hash.ToLowerInvariant(); $a.unresolved_blockers=@()
$a | ConvertTo-Json -Depth 10 | Set-Content $path
```

### 11. Export the reviewed workflow

```text
Use n8n Download and save C436-work/HB-001/03-edit/video-review-agent-reviewed.json. Then run labs/assets/validate-lab-checkpoint.ps1 -Lab 6 and retain lab-06-test-output.txt.
```

## Test It

The validator must print LAB-06 PASS: rights, invalid duration, or bad caption timing must block; repaired evidence stays non-releasing; the human JSON approval must bind the actual video hash and private-only scope.

## Checkpoint and Rejoin Point

Lab checkpoint 06 adds both issue registers, the repair log, structured human final review, and exported workflow to C436-work/HB-001/03-edit. Keep v1 evidence to prove the defect. The trainer-approved rejoin block below restores exact review artifacts and verifies that the final approval names the SHA-256 of the supplied Lab 5 MP4.

```text
Set-Location '<PATH_TO_C436_REPOSITORY>'
$editPath='C436-work/HB-001/03-edit'
if(-not (Test-Path -LiteralPath "$editPath/output/vertical-draft-v1.mp4")){throw 'Run the complete Lab 5 rejoin block first.'}
Copy-Item -LiteralPath labs/assets/issue-register-blocked-example.json -Destination "$editPath/issue-register-v1.json" -Force
Copy-Item -LiteralPath labs/assets/issue-register-clear-example.json -Destination "$editPath/issue-register-v2.json" -Force
Copy-Item -LiteralPath labs/assets/repair-log-approved.md -Destination "$editPath/repair-log.md" -Force
Copy-Item -LiteralPath labs/assets/final-review-approval-approved.json -Destination "$editPath/final-review-approval.json" -Force
$approval=Get-Content -Raw -LiteralPath "$editPath/final-review-approval.json" | ConvertFrom-Json
$videoHash=(Get-FileHash -Algorithm SHA256 -LiteralPath "$editPath/output/vertical-draft-v1.mp4").Hash.ToLowerInvariant()
if($approval.reviewed_video_sha256 -ne $videoHash){throw 'Final approval does not match the restored video.'}
PowerShell -ExecutionPolicy Bypass -File labs/assets/validate-lab-checkpoint.ps1 -Lab 6 -WorkRoot C436-work/HB-001
```

## Troubleshooting

| If this happens | Fix |
|---|---|
| The clear run still contains the rights blocker. | Confirm the edited evidence node was saved and run from the workflow trigger rather than a downstream node with pinned data. |
| The review result sets release_allowed=true. | Stop. Restore the supplied workflow and confirm the final deterministic gate always sets release_allowed=false pending a separate approval token. |
| The video preview reveals a new issue not in the automated output. | Record it with evidence and severity, repair it, and rerun only the affected technical checks plus the complete human preview. |

## Challenge

Add a blocking rule for duplicate WebVTT cue identifiers, prove it with a controlled duplicate cue ID, then restore the approved caption file and confirm the full review returns review_clear.

## Reflection

What important quality judgment remained invisible to the automated review evidence?

---

[← Lab 5](lab-05-assemble-and-probe-the-captioned-vertical-video.md) · [Lab 7 →](lab-07-orchestrate-the-private-release-package-with-human-approval.md)
