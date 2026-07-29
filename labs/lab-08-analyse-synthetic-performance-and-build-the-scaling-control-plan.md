# Lab 8 — Analyse Synthetic Performance and Build the Scaling Control Plan

**Course:** Agentic AI for Video Creation  
**Course Code:** C436  
**Version:** v1.0 (29 July 2026)  
**Topic 4:** Automating and Scaling Video Production  
**Maps to:** LO4: analyse performance with metric contracts and scale the pipeline through measurable guardrails  
**Duration:** 90 minutes  
**Tools:** n8n, supplied synthetic analytics CSV, spreadsheet or text editor

---

## Goal

Turn synthetic post data into a bounded next test and a scaling decision supported by operational evidence.

## What You Will Do

You will import a deterministic analytics workflow, validate metric definitions and denominators, calculate completion and save rates, inspect low-volume caveats, and produce one creative experiment. You will then complete a scaling scorecard covering throughput, cost, rework, quality, rights, incidents, and rollback.

## What You Will Build

A metric-contract.json, analytics-result.json, next-test.md, scaling-scorecard.csv, and integrated-handover.md in stage folder 05-learn.

## Prerequisites

- Complete Lab 7 or restore Lab checkpoint 07.
- Confirm labs/assets/synthetic-video-analytics.csv, analytics-scale-workflow.json, and scaling-scorecard-template.csv are present.
- Treat all analytics as synthetic; do not infer facts about real people or accounts.

> **Data note.** Use only the supplied synthetic campaign data and approved accounts. Store secrets in managed credentials, keep public publishing disabled, and obtain human approval before any external release action.

## Steps

### 1. Create the learning checkpoint and copy the supplied data

```text
New-Item -ItemType Directory -Force C436-work/HB-001/05-learn | Out-Null
Copy-Item labs/assets/synthetic-video-analytics.csv C436-work/HB-001/05-learn/synthetic-video-analytics.csv
Copy-Item labs/assets/synthetic-pipeline-operations.csv C436-work/HB-001/05-learn/synthetic-pipeline-operations.csv
Copy-Item labs/assets/metric-contract-approved.json C436-work/HB-001/05-learn/metric-contract.json
Copy-Item labs/assets/scaling-scorecard-template.csv C436-work/HB-001/05-learn/scaling-scorecard.csv
Copy-Item labs/assets/scale-decision-template.json C436-work/HB-001/05-learn/scale-decision.json
```

### 2. Inspect data grain and required denominators

```text
Import-Csv C436-work/HB-001/05-learn/synthetic-video-analytics.csv | Format-Table video_id,hook_family,duration_seconds,views,completed_views,saves,shares
```

### 3. Review the metric contract before calculation

```text
Get-Content -Raw C436-work/HB-001/05-learn/metric-contract.json | ConvertFrom-Json | Select-Object decision,primary_metric,minimum_views,comparison_grain,window | Format-List
```

### 4. Import the analytics workflow

```text
In n8n, create a workflow from labs/assets/analytics-scale-workflow.json, rename it C436-HB-001-Analytics-and-Scale, save it, and keep it inactive.
```

### 5. Inspect deterministic calculations

```text
Confirm completion_rate=completed_views/views and save_rate=saves/views after excluding rows below minimum_views. Confirm cost_per_accepted_video=sum(cost_sgd)/accepted_count and any rights, review, duplicate-release, rollback, or capacity blocker forces HOLD.
```

### 6. Paste the exact source artifacts into the workflow

```text
Open Load Exact Analytics Operations and Contract. Paste the complete synthetic-video-analytics.csv, synthetic-pipeline-operations.csv, and metric-contract.json into their named constants. Do not retype or use a subset.
```

### 7. Run the analytics workflow and save the result

```text
Select Test Workflow. Open Emit Analysis and save its complete JSON output as C436-work/HB-001/05-learn/analytics-result.json.
```

### 8. Verify rates and caveats

```text
$result = Get-Content -Raw C436-work/HB-001/05-learn/analytics-result.json | ConvertFrom-Json
$result.summary_by_hook | Format-Table hook_family,video_count,total_views,completion_rate,save_rate
$result.caveats
if (-not $result.low_volume_video_ids) { Write-Host 'No low-volume rows in this supplied dataset' }
```

### 9. Calculate baseline, pilot, cost, rework, blocker, rollback, and capacity evidence

```text
$ops=@(Import-Csv C436-work/HB-001/05-learn/synthetic-pipeline-operations.csv); $base=@($ops|Where-Object phase -eq 'baseline'); $pilot=@($ops|Where-Object phase -eq 'pilot'); $accepted=@($ops|Where-Object accepted_status -eq 'accepted'); $rework=@($ops|Where-Object rework_required -eq 'true'); $blockers=@($ops|Where-Object {[int]$_.unresolved_rights_items -gt 0 -or [int]$_.blocking_review_findings -gt 0}); $summary=[ordered]@{baseline_job_count=$base.Count;pilot_job_count=$pilot.Count;baseline_average_cycle_minutes=[math]::Round((($base|Measure-Object cycle_minutes -Average).Average),2);pilot_average_cycle_minutes=[math]::Round((($pilot|Measure-Object cycle_minutes -Average).Average),2);cost_per_accepted_video_sgd=[math]::Round((($ops|Measure-Object cost_sgd -Sum).Sum/$accepted.Count),2);rework_rate=[math]::Round(($rework.Count/$ops.Count),4);blocking_job_ids=@($blockers.job_id);duplicate_release_actions=[int](($ops|Measure-Object duplicate_release_actions -Sum).Sum);rollback_all_tested=(-not ($ops|Where-Object rollback_tested -ne 'true'));human_review_capacity_sufficient=(-not ($ops|Where-Object {[int]$_.human_review_capacity_slots -lt [int]$_.human_reviews_required}))}; $summary|ConvertTo-Json -Depth 8|Set-Content C436-work/HB-001/05-learn/operational-summary.json
$summary
```

### 10. Write one bounded next test

```text
Create next-test.md with Decision, Observation, Caveat, Hypothesis, Single change, Held constant, Primary metric, Guardrails, Minimum sample, Review date, and Stop rule. Change only hook family; hold topic and duration band constant.
```

### 11. Complete the scaling scorecard

```text
Use operational-summary.json and the phase/capacity columns to complete all eight rows. Set baseline, pilot_evidence, threshold, owner, status, and action with no placeholders. At least the rights/review rows must be HOLD while the supplied pilot blocker remains.
```

### 12. Make the scale decision

```text
Open scale-decision.json. Set scale_decision to HOLD for the supplied blocker, add reason and next_owner, and retain canary_limit=3, visibility=private, human_review_rate=1.0, and rollback path. Only a later clean pilot may use PILOT_3_PER_WEEK or SCALE_WITH_LIMITS.
```

### 13. Create the integrated handover

```text
Write integrated-handover.md with literal LAB-CHECKPOINT-01 through LAB-CHECKPOINT-08 paths plus headings: artifact versions, unresolved issues, enabled tools, disabled tools, approval scope, metric decision, scale decision, rollback path, and next owner.
```

### 14. Export the reviewed analytics workflow

```text
Use n8n Download and save C436-work/HB-001/05-learn/analytics-scale-reviewed.json. Run labs/assets/validate-lab-checkpoint.ps1 -Lab 8 and retain lab-08-test-output.txt.
```

## Test It

The validator must print LAB-08 PASS. It proves low-volume exclusion, baseline/pilot, duplicate-release, rollback, and capacity gates, exact scorecard controls, the complete next test/handover, and a structured HOLD/canary decision.

## Checkpoint and Rejoin Point

Lab checkpoint 08 is the full stage folder C436-work/HB-001/05-learn plus the integrated handover. A rejoining learner may use the approved metric contract and supplied synthetic data, but must still make and explain their own bounded next-test and scaling decisions.

## Troubleshooting

| If this happens | Fix |
|---|---|
| A calculated rate is greater than 1 or below 0. | Check numeric conversion and confirm the numerator cannot exceed the declared denominator; flag the row instead of repairing it silently. |
| The workflow recommends a winner from a low-volume row. | Apply the minimum_views rule before ranking and retain the caveat in the result. |
| The scale scorecard is green while rights or release evidence is missing. | Set the affected control to blocked and choose HOLD until the owner resolves and rechecks it. |

## Challenge

Use the supplied cost and accepted-status fields to calculate cost per accepted video, then add a canary rule limiting the first pilot to three private drafts with 100% human review.

## Reflection

Which scaling metric would reveal that the workflow is producing more output but less useful accepted work?

---

[← Lab 7](lab-07-orchestrate-the-private-release-package-with-human-approval.md) · [Labs index →](README.md)
