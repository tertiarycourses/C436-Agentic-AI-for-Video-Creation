"""Topic 4 labs: release orchestration, analytics, and scaling."""

DOMAIN4 = [
    dict(
        num=7,
        topic=4,
        title="Orchestrate the Private Release Package with Human Approval",
        objective="LO4: orchestrate multi-step agents and prepare safe platform-specific publishing actions",
        duration=50,
        goal="Build a release-ready package that is blocked until a person approves one scoped private action.",
        desc=(
            "You will import a release orchestrator, inspect its state transitions, "
            "validate video, caption, metadata, rights, and disclosure fields, then "
            "exercise denial and approval paths. The lab creates a dry-run package "
            "only; no public account or live posting credential is used."
        ),
        build=(
            "A release-package.json, denied-approval.json, "
            "private-release-approval.json, and release-orchestrator-reviewed.json "
            "in stage folder 04-release."
        ),
        services="n8n, supplied release workflow, reviewed video package",
        prerequisites=[
            "Complete Lab 6 or restore Lab checkpoint 06 with final-review-approval.json bound to the reviewed video.",
            "Confirm labs/assets/release-orchestrator-workflow.json and release-metadata-template.json are present.",
            "Do not connect a YouTube, TikTok, or other publishing credential during the required lab path.",
        ],
        workflow=[
            "Import the orchestrator",
            "Validate release inputs",
            "Exercise denial",
            "Issue scoped approval",
            "Export dry-run package",
        ],
        steps=[
            (
                "Create the release checkpoint",
                "New-Item -ItemType Directory -Force C436-work/HB-001/04-release | Out-Null\nCopy-Item labs/assets/release-metadata-template.json C436-work/HB-001/04-release/release-metadata.json",
            ),
            (
                "Complete the release metadata without account secrets",
                "Open release-metadata.json and set title, description, caption_path='02-create/captions-script-v1.vtt', video_path='03-edit/output/vertical-draft-v1.mp4', rights_evidence_path='02-create/asset-manifest.csv', final_review_approval_path='03-edit/final-review-approval.json', and package_owner. Retain typed private/null/true values and public_release_allowed=false.",
            ),
            (
                "Build and hash the canonical release package manifest",
                "PowerShell -ExecutionPolicy Bypass -File labs/assets/build-release-package.ps1 -WorkRoot C436-work/HB-001\nGet-Content -Raw C436-work/HB-001/04-release/release-package-manifest.json | ConvertFrom-Json | Select-Object run_id,package_version,title,privacy_status,contains_synthetic_media",
            ),
            (
                "Import and inspect the release orchestrator",
                "In n8n, create a workflow from labs/assets/release-orchestrator-workflow.json, rename it C436-HB-001-Private-Release-Orchestrator, save it, and keep it inactive. Confirm the states are release_input -> validation -> awaiting_human_approval -> dry_run_ready or denied.",
            ),
            (
                "Run the input validation path",
                "Open Load Exact Release Metadata and paste the complete release-metadata.json between the releaseText backticks. Select Test Workflow and inspect Emit Release Package.",
            ),
            (
                "Save the awaiting-approval package",
                "Copy the Emit Release Package JSON output to C436-work/HB-001/04-release/release-package.json. Confirm publish_allowed=false and status=awaiting_human_approval.",
            ),
            (
                "Exercise the denial path",
                "Edit release-metadata.json to set human_decision='deny' and decision_reason='Controlled lab denial - verify no action'. Repaste the complete file, run, and save the complete output as C436-work/HB-001/04-release/denied-approval.json.",
            ),
            (
                "Verify denial causes no external action",
                "$denied = Get-Content -Raw C436-work/HB-001/04-release/denied-approval.json | ConvertFrom-Json\n$denied | Select-Object status,publish_allowed,external_action_count\nif ($denied.external_action_count -ne 0) { throw 'Denial must cause zero external actions' }",
            ),
            (
                "Create a scoped private approval",
                "$path='C436-work/HB-001/04-release/release-metadata.json'\n$m=Get-Content -Raw $path | ConvertFrom-Json\n$m.human_decision='approve_private_dry_run'; $m.decision_reason='Reviewed exact package for private dry run only'; $m.approval_scope='HB-001; private dry-run request preview; one package; no external execution'; $m.approval_package_sha256=$m.package_sha256; $m.approval_expires_at=[datetimeoffset]::UtcNow.AddHours(8).ToString('o')\n$m | ConvertTo-Json -Depth 10 | Set-Content $path\nRepaste the complete file into Load Exact Release Metadata and run.",
            ),
            (
                "Save and verify the approved dry-run output",
                "Save the final output as C436-work/HB-001/04-release/private-release-approval.json. Confirm dry_run_ready, non-publishing, zero actions, a non-empty idempotency key, and disclosure-complete non-executing platform previews.",
            ),
            (
                "Export the reviewed orchestrator",
                "Use n8n Download and save C436-work/HB-001/04-release/release-orchestrator-reviewed.json.",
            ),
            (
                "Compare platform requirements",
                "Open labs/assets/platform-release-references.md and inspect the supplied YouTube/TikTok non-executing preview JSON. In release-notes.md, link those official references and distinguish request previews from authorised live calls.",
            ),
            (
                "Run the fail-closed Lab 7 validator and retain the evidence",
                "PowerShell -ExecutionPolicy Bypass -File labs/assets/validate-lab-checkpoint.ps1 -Lab 7 2>&1 | Tee-Object C436-work/HB-001/04-release/lab-07-test-output.txt\nSet-Content C436-work/HB-001/04-release/LAB-CHECKPOINT-07.txt 'Lab 7 passed; hash-bound private dry-run package retained.'",
            ),
        ],
        test=(
            "The validator must print LAB-07 PASS. It recomputes the canonical "
            "package and every video/caption/rights/final-review hash, requires an "
            "exact approval hash plus future expiry, and validates zero-action platform previews."
        ),
        checkpoint=(
            "Lab checkpoint 07 is stored in stage folder C436-work/HB-001/04-release. It contains both decision "
            "paths and the private dry-run package. A live integration may be added "
            "later only by an authorised owner using current official platform "
            "documentation and managed credentials."
        ),
        troubleshooting=[
            (
                "The validator reports a missing disclosure decision.",
                "Set contains_synthetic_media explicitly to true or false based on the reviewed content; never leave it implicit.",
            ),
            (
                "The approved dry run sets publish_allowed=true.",
                "Stop and restore the supplied workflow. This lab never authorises a live public action.",
            ),
            (
                "The idempotency key changes every time the same package is retried.",
                "Build it from the stable run ID, target, and package checksum rather than the current timestamp.",
            ),
        ],
        challenge=(
            "Set approval_expires_at to one minute in the past and prove the package "
            "is blocked with approval_hash_or_expiry_invalid and zero actions, then restore a future expiry."
        ),
        reflection=(
            "Which release fields must a person see together before an approval can "
            "be considered informed?"
        ),
    ),
    dict(
        num=8,
        topic=4,
        title="Analyse Synthetic Performance and Build the Scaling Control Plan",
        objective="LO4: analyse performance with metric contracts and scale the pipeline through measurable guardrails",
        duration=90,
        goal="Turn synthetic post data into a bounded next test and a scaling decision supported by operational evidence.",
        desc=(
            "You will import a deterministic analytics workflow, validate metric "
            "definitions and denominators, calculate completion and save rates, "
            "inspect low-volume caveats, and produce one creative experiment. You "
            "will then complete a scaling scorecard covering throughput, cost, "
            "rework, quality, rights, incidents, and rollback."
        ),
        build=(
            "A metric-contract.json, analytics-result.json, next-test.md, "
            "scaling-scorecard.csv, and integrated-handover.md in stage folder 05-learn."
        ),
        services="n8n, supplied synthetic analytics CSV, spreadsheet or text editor",
        prerequisites=[
            "Complete Lab 7 or restore Lab checkpoint 07.",
            "Confirm labs/assets/synthetic-video-analytics.csv, analytics-scale-workflow.json, and scaling-scorecard-template.csv are present.",
            "Treat all analytics as synthetic; do not infer facts about real people or accounts.",
        ],
        workflow=[
            "Define metric contracts",
            "Validate synthetic data",
            "Calculate and compare",
            "Design one next test",
            "Gate the scaling plan",
        ],
        steps=[
            (
                "Create the learning checkpoint and copy the supplied data",
                "New-Item -ItemType Directory -Force C436-work/HB-001/05-learn | Out-Null\nCopy-Item labs/assets/synthetic-video-analytics.csv C436-work/HB-001/05-learn/synthetic-video-analytics.csv\nCopy-Item labs/assets/synthetic-pipeline-operations.csv C436-work/HB-001/05-learn/synthetic-pipeline-operations.csv\nCopy-Item labs/assets/metric-contract-approved.json C436-work/HB-001/05-learn/metric-contract.json\nCopy-Item labs/assets/scaling-scorecard-template.csv C436-work/HB-001/05-learn/scaling-scorecard.csv\nCopy-Item labs/assets/scale-decision-template.json C436-work/HB-001/05-learn/scale-decision.json",
            ),
            (
                "Inspect data grain and required denominators",
                "Import-Csv C436-work/HB-001/05-learn/synthetic-video-analytics.csv | Format-Table video_id,hook_family,duration_seconds,views,completed_views,saves,shares",
            ),
            (
                "Review the metric contract before calculation",
                "Get-Content -Raw C436-work/HB-001/05-learn/metric-contract.json | ConvertFrom-Json | Select-Object decision,primary_metric,minimum_views,comparison_grain,window | Format-List",
            ),
            (
                "Import the analytics workflow",
                "In n8n, create a workflow from labs/assets/analytics-scale-workflow.json, rename it C436-HB-001-Analytics-and-Scale, save it, and keep it inactive.",
            ),
            (
                "Inspect deterministic calculations",
                "Confirm completion_rate=completed_views/views and save_rate=saves/views after excluding rows below minimum_views. Confirm cost_per_accepted_video=sum(cost_sgd)/accepted_count and any rights, review, duplicate-release, rollback, or capacity blocker forces HOLD.",
            ),
            (
                "Paste the exact source artifacts into the workflow",
                "Open Load Exact Analytics Operations and Contract. Paste the complete synthetic-video-analytics.csv, synthetic-pipeline-operations.csv, and metric-contract.json into their named constants. Do not retype or use a subset.",
            ),
            (
                "Run the analytics workflow and save the result",
                "Select Test Workflow. Open Emit Analysis and save its complete JSON output as C436-work/HB-001/05-learn/analytics-result.json.",
            ),
            (
                "Verify rates and caveats",
                "$result = Get-Content -Raw C436-work/HB-001/05-learn/analytics-result.json | ConvertFrom-Json\n$result.summary_by_hook | Format-Table hook_family,video_count,total_views,completion_rate,save_rate\n$result.caveats\nif (-not $result.low_volume_video_ids) { Write-Host 'No low-volume rows in this supplied dataset' }",
            ),
            (
                "Calculate baseline, pilot, cost, rework, blocker, rollback, and capacity evidence",
                "$ops=@(Import-Csv C436-work/HB-001/05-learn/synthetic-pipeline-operations.csv); $base=@($ops|Where-Object phase -eq 'baseline'); $pilot=@($ops|Where-Object phase -eq 'pilot'); $accepted=@($ops|Where-Object accepted_status -eq 'accepted'); $rework=@($ops|Where-Object rework_required -eq 'true'); $blockers=@($ops|Where-Object {[int]$_.unresolved_rights_items -gt 0 -or [int]$_.blocking_review_findings -gt 0}); $summary=[ordered]@{baseline_job_count=$base.Count;pilot_job_count=$pilot.Count;baseline_average_cycle_minutes=[math]::Round((($base|Measure-Object cycle_minutes -Average).Average),2);pilot_average_cycle_minutes=[math]::Round((($pilot|Measure-Object cycle_minutes -Average).Average),2);cost_per_accepted_video_sgd=[math]::Round((($ops|Measure-Object cost_sgd -Sum).Sum/$accepted.Count),2);rework_rate=[math]::Round(($rework.Count/$ops.Count),4);blocking_job_ids=@($blockers.job_id);duplicate_release_actions=[int](($ops|Measure-Object duplicate_release_actions -Sum).Sum);rollback_all_tested=(-not ($ops|Where-Object rollback_tested -ne 'true'));human_review_capacity_sufficient=(-not ($ops|Where-Object {[int]$_.human_review_capacity_slots -lt [int]$_.human_reviews_required}))}; $summary|ConvertTo-Json -Depth 8|Set-Content C436-work/HB-001/05-learn/operational-summary.json\n$summary",
            ),
            (
                "Write one bounded next test",
                "Create next-test.md with Decision, Observation, Caveat, Hypothesis, Single change, Held constant, Primary metric, Guardrails, Minimum sample, Review date, and Stop rule. Change only hook family; hold topic and duration band constant.",
            ),
            (
                "Complete the scaling scorecard",
                "Use operational-summary.json and the phase/capacity columns to complete all eight rows. Set baseline, pilot_evidence, threshold, owner, status, and action with no placeholders. At least the rights/review rows must be HOLD while the supplied pilot blocker remains.",
            ),
            (
                "Make the scale decision",
                "Open scale-decision.json. Set scale_decision to HOLD for the supplied blocker, add reason and next_owner, and retain canary_limit=3, visibility=private, human_review_rate=1.0, and rollback path. Only a later clean pilot may use PILOT_3_PER_WEEK or SCALE_WITH_LIMITS.",
            ),
            (
                "Create the integrated handover",
                "Write integrated-handover.md with literal LAB-CHECKPOINT-01 through LAB-CHECKPOINT-08 paths plus headings: artifact versions, unresolved issues, enabled tools, disabled tools, approval scope, metric decision, scale decision, rollback path, and next owner.",
            ),
            (
                "Export the reviewed analytics workflow",
                "Use n8n Download and save C436-work/HB-001/05-learn/analytics-scale-reviewed.json. Run labs/assets/validate-lab-checkpoint.ps1 -Lab 8 and retain lab-08-test-output.txt.",
            ),
        ],
        test=(
            "The validator must print LAB-08 PASS. It proves low-volume exclusion, "
            "baseline/pilot, duplicate-release, rollback, and capacity gates, exact "
            "scorecard controls, the complete next test/handover, and a structured "
            "HOLD/canary decision."
        ),
        checkpoint=(
            "Lab checkpoint 08 is the full stage folder C436-work/HB-001/05-learn plus the "
            "integrated handover. A rejoining learner may use the approved metric "
            "contract and supplied synthetic data, but must still make and explain "
            "their own bounded next-test and scaling decisions."
        ),
        troubleshooting=[
            (
                "A calculated rate is greater than 1 or below 0.",
                "Check numeric conversion and confirm the numerator cannot exceed the declared denominator; flag the row instead of repairing it silently.",
            ),
            (
                "The workflow recommends a winner from a low-volume row.",
                "Apply the minimum_views rule before ranking and retain the caveat in the result."),
            (
                "The scale scorecard is green while rights or release evidence is missing.",
                "Set the affected control to blocked and choose HOLD until the owner resolves and rechecks it."),
        ],
        challenge=(
            "Use the supplied cost and accepted-status fields to calculate cost per "
            "accepted video, then add a canary rule limiting the first pilot to three private drafts with 100% human review."
        ),
        reflection=(
            "Which scaling metric would reveal that the workflow is producing more "
            "output but less useful accepted work?"
        ),
    ),
]
