# Lab 2 — Build and Run the Bounded Video Planning Agent in n8n

**Course:** Agentic AI for Video Creation  
**Course Code:** C436  
**Version:** v1.0 (29 July 2026)  
**Topic 1:** Getting Started with Agentic AI for Video  
**Maps to:** LO1: use structured prompts and tool boundaries to implement a resumable planning workflow  
**Duration:** 50 minutes  
**Tools:** n8n, supplied workflow JSON, production contract

---

## Goal

Import, inspect, and run a planning workflow that stops on missing evidence and emits a valid production plan.

## What You Will Do

You will import a supplied n8n workflow, trace its trigger, validation, planning, guardrail, and output stages, then run one ready case and one blocked case. The agent uses deterministic mock planning so everyone can verify the control pattern without a paid API.

## What You Will Build

An n8n workflow named C436-HB-001-Planning-Agent plus exported ready and blocked execution evidence.

## Prerequisites

- Complete Lab 1 or restore Lab checkpoint 01 in stage folder 01-design.
- Access an n8n Cloud workspace or trainer-provided n8n instance.
- Keep live credentials disconnected; this lab uses deterministic Code nodes.

> **Data note.** Use only the supplied synthetic campaign data and approved accounts. Store secrets in managed credentials, keep public publishing disabled, and obtain human approval before any external release action.

## Steps

### 1. Open n8n and import the supplied workflow

```text
In n8n, select Workflows > Create Workflow. Open the top-right three-dot menu, select Import from File, and choose labs/assets/video-planning-agent-workflow.json.
```

### 2. Rename and save the imported workflow

```text
Set the workflow name to C436-HB-001-Planning-Agent and select Save. Keep the workflow inactive.
```

### 3. Inspect the five-node control path

```text
Confirm the main path is Manual Trigger > Load Exact Production Contract > Validate Contract and Version > Plan or Block > Emit Run State. Confirm a blocked result calls no external tool.
```

### 4. Paste the exact Lab 1 artifact into the input node

```text
Open Load Exact Production Contract. Copy the entire contents of C436-work/HB-001/01-design/production-contract.json between the contractText backticks. Do not retype or use the supplied approved fixture. Run once and verify contract_version=contract-v1 plus a non-empty source_fingerprint.
```

### 5. Execute the complete ready workflow

```text
Select Test Workflow. After execution, select Emit Run State and open the JSON output.
```

### 6. Verify the ready-state schema

```text
The output must contain run_id=HB-001, status=plan_ready, current_stage=planning, next_stage=research_and_script, a non-empty actions array, iteration=1, and publish_allowed=false.
```

### 7. Create a controlled missing-evidence case

```text
Copy the complete Emit Run State output to C436-work/HB-001/01-design/ready-run.json. Then open Load Exact Production Contract, set approved_facts to an empty array inside the pasted JSON, save, and select Test Workflow again.
```

### 8. Verify the workflow stops safely

```text
Open Emit Run State. Confirm status=blocked, next_stage=human_clarification, publish_allowed=false, and blockers includes missing_approved_facts. Save the complete output as C436-work/HB-001/01-design/blocked-run.json.
```

### 9. Restore the ready case and export the workflow

```text
Restore the exact approved_facts array from the Lab 1 file, rerun from Manual Trigger, and save the complete output as C436-work/HB-001/01-design/ready-restored-run.json. Download the workflow as planning-agent-reviewed.json.
```

### 10. Save a short execution evidence note

```text
PowerShell -ExecutionPolicy Bypass -File labs/assets/validate-lab-checkpoint.ps1 -Lab 2 2>&1 | Tee-Object C436-work/HB-001/01-design/lab-02-test-output.txt
Set-Content C436-work/HB-001/01-design/LAB-CHECKPOINT-02.txt 'Lab 2 passed; planning evidence retained in stage folder 01-design.'
```

## Test It

The Lab 2 validator must print LAB-02 PASS after reading ready-run.json, blocked-run.json, and ready-restored-run.json. Both ready results must remain non-publishing; the controlled missing-evidence result must fail closed.

## Checkpoint and Rejoin Point

Lab checkpoint 02 adds three execution JSON files, test evidence, and planning-agent-reviewed.json to stage folder C436-work/HB-001/01-design. The template remains available at labs/assets/video-planning-agent-workflow.json.

## Troubleshooting

| If this happens | Fix |
|---|---|
| n8n rejects the imported JSON. | Confirm that you selected the workflow file rather than a course data file, then ask the trainer for the current n8n import fallback. |
| The path after Validate Contract does not reach Emit Run State. | Open the validation output and confirm required fields use the exact supplied names and approved_facts is an array. |
| The blocked run still shows plan_ready. | Execute from Manual Trigger after saving the edited contract node; running only the final node may reuse pinned data. |

## Challenge

Add a deterministic budget check that returns blocker generation_budget_missing when cost_budget_sgd is absent.

## Reflection

Why is the blocked result a successful agent behavior rather than a workflow failure?

---

[← Lab 1](lab-01-design-the-video-agent-production-contract-and-autonomy-matrix.md) · [Lab 3 →](lab-03-run-the-research-to-script-agent-and-approve-a-timed-storyboard.md)
