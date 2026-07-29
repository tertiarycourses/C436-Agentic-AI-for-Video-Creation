# Lab 1 — Design the Video Agent Production Contract and Autonomy Matrix

**Course:** Agentic AI for Video Creation  
**Course Code:** C436  
**Version:** v1.0 (29 July 2026)  
**Topic 1:** Getting Started with Agentic AI for Video  
**Maps to:** LO1: explain agentic AI and design a controlled video workflow with explicit human decision points  
**Duration:** 45 minutes  
**Tools:** Text editor, supplied synthetic brief, JSON validator

---

## Goal

Create the authoritative contract that every later C436 lab will consume.

## What You Will Do

You will turn the synthetic Harbour Bean campaign brief into a structured production contract, classify each task by autonomy level, and mark the evidence, approval, retry, and stop rules for the workflow.

## What You Will Build

A completed production-contract.json and autonomy-matrix.csv for run HB-001, saved in the connected project checkpoint.

## Prerequisites

- Download or clone the C436 repository and open labs/assets.
- Confirm that harbour-bean-brand-brief.md and production-contract-template.json are present.
- Know the local path to the C436 repository; do not use real customer or account data.

> **Data note.** Use only the supplied synthetic campaign data and approved accounts. Store secrets in managed credentials, keep public publishing disabled, and obtain human approval before any external release action.

## Steps

### 1. Set the repository root and fail fast if the course assets are absent

```text
Set-Location '<PATH_TO_C436_REPOSITORY>'
if (-not (Test-Path -LiteralPath labs/assets/harbour-bean-brand-brief.md -PathType Leaf)) { throw 'Run this lab from the C436 repository root.' }
```

### 2. Create the connected project folders

```text
New-Item -ItemType Directory -Force -Path C436-work/HB-001/01-design,C436-work/HB-001/02-create,C436-work/HB-001/03-edit,C436-work/HB-001/04-release,C436-work/HB-001/05-learn | Out-Null
```

### 3. Read the synthetic brief and identify only approved facts

```text
Get-Content -LiteralPath labs/assets/harbour-bean-brand-brief.md
```

### 4. Copy the contract and autonomy templates into stage folder 01-design

```text
Copy-Item -LiteralPath labs/assets/production-contract-template.json -Destination C436-work/HB-001/01-design/production-contract.json
Copy-Item -LiteralPath labs/assets/autonomy-matrix-template.csv -Destination C436-work/HB-001/01-design/autonomy-matrix.csv
```

### 5. Open production-contract.json and replace every text placeholder using only the supplied brief

```text
notepad C436-work/HB-001/01-design/production-contract.json
```

### 6. Set the required contract controls

```text
Set run_id to HB-001; retain contract_version contract-v1; duration_seconds 30; aspect_ratio 9:16; publishing_mode dry_run_private; max_generation_attempts_per_scene 2; cost_budget_sgd 25.0; finish_condition to release package approved or routed to named owner. Keep numbers unquoted.
```

### 7. Complete the autonomy matrix for all listed tasks

```text
Use deterministic for schema validation, file naming, media probing, arithmetic, and packaging; model_assisted for research clustering, script alternatives, and review suggestions; human_approved for claims, rights, final edit, and release; prohibited for secret exposure, unreviewed public posting, and unapproved likeness use.
```

### 8. Run the fail-closed Lab 1 validator and retain the evidence

```text
PowerShell -ExecutionPolicy Bypass -File labs/assets/validate-lab-checkpoint.ps1 -Lab 1 2>&1 | Tee-Object C436-work/HB-001/01-design/lab-01-test-output.txt
```

### 9. Check that no template placeholder remains

```text
Select-String -Path C436-work/HB-001/01-design/production-contract.json,C436-work/HB-001/01-design/autonomy-matrix.csv -Pattern '<COMPLETE_ME>'
```

### 10. Write the Lab checkpoint 01 marker

```text
Set-Content -LiteralPath C436-work/HB-001/01-design/LAB-CHECKPOINT-01.txt -Value 'Lab 1 passed; stage folder 01-design is ready.'
```

## Test It

The validator must print LAB-01 PASS. It enforces JSON types, positive budget, all nine autonomy rows, prohibition of public publishing, and prohibition of secret exposure. The placeholder search must return no matches.

## Checkpoint and Rejoin Point

Lab checkpoint 01 is stored in stage folder C436-work/HB-001/01-design. If you fall behind, copy labs/assets/production-contract-approved.json and labs/assets/autonomy-matrix-approved.csv into this folder, then rerun the tests before continuing.

## Troubleshooting

| If this happens | Fix |
|---|---|
| ConvertFrom-Json reports an invalid object. | Open the file, check the line named in the error, remove trailing commas, and ensure every key and text value is in double quotes. |
| The brief does not contain a value requested by the template. | Write null or add it to open_questions; do not invent a fact. |
| A task seems both model-assisted and human-approved. | Classify the model's draft as model_assisted and the consequential decision or action as human_approved. |

## Challenge

Add a budget warning threshold at 80% of the required cost_budget_sgd and prove the rule returns a named owner rather than another generation attempt.

## Reflection

Which video-production decision was most tempting to automate fully, and what evidence convinced you to keep a human approval point?

---

[← Labs index](README.md) · [Lab 2 →](lab-02-build-and-run-the-bounded-video-planning-agent-in-n8n.md)
