# Lab 3 — Run the Research-to-Script Agent and Approve a Timed Storyboard

**Course:** Agentic AI for Video Creation  
**Course Code:** C436  
**Version:** v1.0 (29 July 2026)  
**Topic 2:** Scripting and Generating Content with AI  
**Maps to:** LO2: create evidence-linked research, script, caption, and storyboard hand-offs from an approved brief  
**Duration:** 65 minutes  
**Tools:** Approved AI assistant or offline fallback, text editor, supplied synthetic data

---

## Goal

Produce one approved 30-second concept whose claims and scenes are traceable to the supplied evidence.

## What You Will Do

You will use an approved AI assistant with a structured B-R-I-E-F prompt, or the supplied offline result, to cluster synthetic audience signals, propose distinct concepts, and return a timed script and storyboard. You will validate the schema and manually approve only evidence-linked content.

## What You Will Build

A source-register.csv, research-script-prompt.txt, script-storyboard.json, captions-script-v1.vtt, and storyboard-approval.md in stage folder 02-create.

## Prerequisites

- Complete Labs 1 and 2 or restore Lab checkpoint 02, including ready-restored-run.json, from stage folder 01-design.
- Confirm labs/assets/audience-signals.csv, harbour-bean-brand-brief.md, and research-script-prompt-template.txt are present.
- Use only the supplied synthetic inputs; do not search for or add personal audience data.

> **Data note.** Use only the supplied synthetic campaign data and approved accounts. Store secrets in managed credentials, keep public publishing disabled, and obtain human approval before any external release action.

## Steps

### 1. Validate and consume the Lab 2 planning hand-off

```text
$plan=Get-Content -Raw C436-work/HB-001/01-design/ready-restored-run.json | ConvertFrom-Json
if($plan.status -ne 'plan_ready' -or $plan.next_stage -ne 'research_and_script' -or [string]::IsNullOrWhiteSpace($plan.source_fingerprint)){throw 'Lab 2 planning hand-off is invalid.'}
$plan | Select-Object run_id,contract_version,source_fingerprint,status,next_stage
```

### 2. Create the topic 2 checkpoint folder

```text
New-Item -ItemType Directory -Force -Path C436-work/HB-001/02-create | Out-Null
```

### 3. Copy the synthetic evidence and prompt template

```text
Copy-Item -LiteralPath labs/assets/audience-signals.csv -Destination C436-work/HB-001/02-create/source-register.csv
Copy-Item -LiteralPath labs/assets/research-script-prompt-template.txt -Destination C436-work/HB-001/02-create/research-script-prompt.txt
```

### 4. Inspect the source register before prompting

```text
Import-Csv C436-work/HB-001/02-create/source-register.csv | Format-Table source_id,observation,evidence_type,allowed_use
```

### 5. Complete the prompt placeholders from the approved production contract

```text
Open research-script-prompt.txt. Set run ID HB-001 and paste the exact source_fingerprint from ready-restored-run.json. Set the audience, 30-second duration, 9:16 aspect ratio, three concepts, and required JSON schema. Paste the approved facts and source rows.
```

### 6. Run the prompt in an approved AI assistant

```text
Start a new chat, paste the completed prompt, and do not enable external actions. If unavailable, run: Copy-Item labs/assets/script-storyboard-approved.json C436-work/HB-001/02-create/script-storyboard.json, then continue at validation.
```

### 7. Save only the JSON response

```text
Copy the assistant's JSON object into C436-work/HB-001/02-create/script-storyboard.json. Remove text outside the outer braces and ensure the root contains script_version='script-v1' and plan_source_fingerprint copied exactly from ready-restored-run.json.
```

### 8. Validate the JSON and inspect the selected concept

```text
Get-Content -Raw C436-work/HB-001/02-create/script-storyboard.json | ConvertFrom-Json | Select-Object run_id,plan_source_fingerprint,status,selected_concept_id,total_duration_seconds | Format-List
```

### 9. Generate a versioned caption hand-off from the exact storyboard

```text
PowerShell -ExecutionPolicy Bypass -File labs/assets/captions-from-storyboard.ps1 -StoryboardPath C436-work/HB-001/02-create/script-storyboard.json -OutputPath C436-work/HB-001/02-create/captions-script-v1.vtt
```

### 10. Review every claim and mark the human decision

```text
Create storyboard-approval.md with four headings: Approved concept, Evidence checked, Required revisions, Decision. Set Decision to APPROVED_FOR_ASSET_REQUESTS only after each factual statement maps to an allowed source ID and no scene uses a real person's likeness.
```

### 11. Record the approved script version

```text
Add script_version=script-v1 and approved_by=<YOUR_NAME> to storyboard-approval.md. Do not write credentials or personal account identifiers.
```

### 12. Run the fail-closed Lab 3 validator and retain the evidence

```text
PowerShell -ExecutionPolicy Bypass -File labs/assets/validate-lab-checkpoint.ps1 -Lab 3 2>&1 | Tee-Object C436-work/HB-001/02-create/lab-03-test-output.txt
Set-Content C436-work/HB-001/02-create/LAB-CHECKPOINT-03.txt 'Lab 3 passed; script and caption hand-offs accepted.'
```

## Test It

The validator must print LAB-03 PASS. It enforces run ID, script_ready status, exact Lab 2 fingerprint hand-off, human approval token, three concepts, required beat fields/source IDs, contiguous timing, and captions.

## Checkpoint and Rejoin Point

Lab checkpoint 03 is stored in stage folder C436-work/HB-001/02-create. The complete rejoin block below restores the approved storyboard, binds it to the exact Lab 2 plan fingerprint, regenerates captions, restores the human approval, and runs the same fail-closed validator.

```text
Set-Location '<PATH_TO_C436_REPOSITORY>'
$planPath='C436-work/HB-001/01-design/ready-restored-run.json'
$createPath='C436-work/HB-001/02-create'
$plan=Get-Content -Raw -LiteralPath $planPath | ConvertFrom-Json
if($plan.status -ne 'plan_ready' -or $plan.next_stage -ne 'research_and_script'){throw 'Restore Lab checkpoint 02 first.'}
New-Item -ItemType Directory -Force -Path $createPath | Out-Null
Copy-Item -LiteralPath labs/assets/script-storyboard-approved.json -Destination "$createPath/script-storyboard.json" -Force
$story=Get-Content -Raw -LiteralPath "$createPath/script-storyboard.json" | ConvertFrom-Json
if($story.plan_source_fingerprint -ne $plan.source_fingerprint){throw 'Approved storyboard does not match the restored Lab 2 plan.'}
$prompt=Get-Content -Raw -LiteralPath labs/assets/research-script-prompt-template.txt
$prompt=$prompt.Replace('<RUN_ID>','HB-001').Replace('<PLAN_SOURCE_FINGERPRINT>',[string]$plan.source_fingerprint)
$prompt | Set-Content -LiteralPath "$createPath/research-script-prompt.txt" -Encoding utf8
PowerShell -ExecutionPolicy Bypass -File labs/assets/captions-from-storyboard.ps1 -StoryboardPath "$createPath/script-storyboard.json" -OutputPath "$createPath/captions-script-v1.vtt"
Copy-Item -LiteralPath labs/assets/storyboard-approval-approved.md -Destination "$createPath/storyboard-approval.md" -Force
PowerShell -ExecutionPolicy Bypass -File labs/assets/validate-lab-checkpoint.ps1 -Lab 3 -WorkRoot C436-work/HB-001
```

## Troubleshooting

| If this happens | Fix |
|---|---|
| The assistant returns Markdown around the JSON. | Copy only the content from the first opening brace to the final closing brace, then rerun ConvertFrom-Json. |
| The beats total more than 30 seconds. | Ask for a repair that preserves the approved claim order and reduces narration; do not silently speed up the voice. |
| A claim has no source ID. | Remove the claim or route it to open_questions. Do not approve it for asset generation. |

## Challenge

Generate a second concept that uses the same evidence but a different angle family, then compare relevance, proof, feasibility, and estimated generation cost before choosing.

## Reflection

Which part of the script required human judgment even after the schema and source checks passed?

---

[← Lab 2](lab-02-build-and-run-the-bounded-video-planning-agent-in-n8n.md) · [Lab 4 →](lab-04-build-the-visual-voiceover-and-music-asset-request-pack.md)
