param(
    [string]$RepositoryRoot = (Resolve-Path (Join-Path $PSScriptRoot "../..")).Path
)

$ErrorActionPreference = "Stop"
$assetRoot = Join-Path $RepositoryRoot "labs/assets"
$testRoot = Join-Path ([System.IO.Path]::GetTempPath()) ("C436-checkpoints-" + [guid]::NewGuid().ToString("N"))
$workRoot = Join-Path $testRoot "C436-work/HB-001"
$design = Join-Path $workRoot "01-design"
$create = Join-Path $workRoot "02-create"
$edit = Join-Path $workRoot "03-edit"
$release = Join-Path $workRoot "04-release"
$learn = Join-Path $workRoot "05-learn"
New-Item -ItemType Directory -Force -Path $design,$create,(Join-Path $create "media"),(Join-Path $edit "output"),$release,$learn | Out-Null

function Copy-Asset([string]$Name, [string]$Destination) {
    Copy-Item -LiteralPath (Join-Path $assetRoot $Name) -Destination $Destination -Force
}
function Write-Utf8([string]$Path, [string]$Text) {
    [System.IO.File]::WriteAllText($Path, $Text, (New-Object System.Text.UTF8Encoding($false)))
}
function Write-Json([string]$Path, $Value) {
    Write-Utf8 $Path ($Value | ConvertTo-Json -Depth 20)
}
function Get-Fnv31Fingerprint([string]$Text) {
    [uint32]$fingerprint = 0
    foreach ($character in $Text.ToCharArray()) {
        $fingerprint = [uint32](([uint64]$fingerprint * 31 + [uint32][char]$character) % 4294967296)
    }
    return "fnv31-" + $fingerprint.ToString("x")
}

# Labs 1-2: contract, control matrix, and deterministic planning outcomes.
Copy-Asset "production-contract-approved.json" (Join-Path $design "production-contract.json")
Copy-Asset "autonomy-matrix-approved.csv" (Join-Path $design "autonomy-matrix.csv")
$contractText = Get-Content -Raw -LiteralPath (Join-Path $design "production-contract.json")
$sourceFingerprint = Get-Fnv31Fingerprint $contractText
$ready = [ordered]@{
    run_id = "HB-001"
    status = "plan_ready"
    contract_version = "contract-v1"
    source_fingerprint = $sourceFingerprint
    next_stage = "research_and_script"
    publish_allowed = $false
    external_action_count = 0
}
Write-Json (Join-Path $design "ready-run.json") $ready
Write-Json (Join-Path $design "ready-restored-run.json") $ready
Write-Json (Join-Path $design "blocked-run.json") ([ordered]@{
    run_id = "HB-001"
    status = "blocked"
    contract_version = "contract-v1"
    blockers = @("missing_approved_facts")
    publish_allowed = $false
    external_action_count = 0
})

# Labs 3-4: exact plan hand-off, storyboard, captions, approvals, and seven accepted assets.
$prompt = Get-Content -Raw -LiteralPath (Join-Path $assetRoot "research-script-prompt-template.txt")
$prompt = $prompt.Replace("<RUN_ID>","HB-001").Replace("<PLAN_SOURCE_FINGERPRINT>",$sourceFingerprint)
Write-Utf8 (Join-Path $create "research-script-prompt.txt") $prompt
Copy-Asset "script-storyboard-approved.json" (Join-Path $create "script-storyboard.json")
Copy-Asset "captions-approved.vtt" (Join-Path $create "captions-script-v1.vtt")
Copy-Asset "storyboard-approval-approved.md" (Join-Path $create "storyboard-approval.md")
Copy-Asset "asset-manifest-approved.csv" (Join-Path $create "asset-manifest.csv")
Copy-Asset "asset-pack-approval-approved.md" (Join-Path $create "asset-pack-approval.md")
Copy-Asset "music-brief-approved.md" (Join-Path $create "music-brief.md")
$story = Get-Content -Raw -LiteralPath (Join-Path $assetRoot "script-storyboard-approved.json") | ConvertFrom-Json
Write-Utf8 (Join-Path $create "narration.txt") (($story.beats.narration -join " ") + [Environment]::NewLine)
foreach ($scene in 1..5) {
    $sceneName = "scene-{0:00}-placeholder.txt" -f $scene
    Write-Utf8 (Join-Path $create "media/$sceneName") "Course-supplied synthetic placeholder for scene $scene. Rights: approved_for_course_use."
}

# Labs 5-6: verified media package, technical evidence, controlled blocker, repair, and bound approval.
Copy-Asset "rejoin/lab-05/vertical-draft-v1.mp4" (Join-Path $edit "output/vertical-draft-v1.mp4")
Copy-Asset "rejoin/lab-05/ffprobe-v1.json" (Join-Path $edit "output/ffprobe-v1.json")
Copy-Asset "rejoin/lab-05/render-log-v1.txt" (Join-Path $edit "output/render-log-v1.txt")
Copy-Asset "rejoin/lab-05/render-evidence-v1.json" (Join-Path $edit "output/render-evidence-v1.json")
Copy-Asset "rejoin/lab-05/captions-v1.vtt" (Join-Path $edit "captions-v1.vtt")
Copy-Asset "assembly-approval-approved.md" (Join-Path $edit "assembly-approval.md")
Write-Json (Join-Path $edit "issue-register-v1.json") ([ordered]@{
    run_id = "HB-001"
    review_status = "blocked"
    findings = @([ordered]@{
        issue_id = "RV-RIGHTS"
        category = "rights"
        severity = "blocking"
        evidence = "controlled test row was changed to review_required"
        required_action = "restore approved rights evidence"
    })
    release_allowed = $false
    external_action_count = 0
})
Write-Json (Join-Path $edit "issue-register-v2.json") ([ordered]@{
    run_id = "HB-001"
    review_status = "review_clear"
    findings = @()
    duration_seconds = 30
    caption_cue_count = 5
    caption_timeline_valid = $true
    owner_approval_status = "pending"
    requires_human_preview = $true
    release_allowed = $false
    external_action_count = 0
})
Copy-Asset "final-review-approval-approved.json" (Join-Path $edit "final-review-approval.json")

# Lab 7: canonical release package, future-scoped approval, and zero-action outputs.
$metadata = Get-Content -Raw -LiteralPath (Join-Path $assetRoot "release-metadata-template.json") | ConvertFrom-Json
$metadata.title = "Three coffee variables"
$metadata.description = "Synthetic training package for a private, non-executing preview."
$metadata.caption_path = "03-edit/captions-v1.vtt"
$metadata.video_path = "03-edit/output/vertical-draft-v1.mp4"
$metadata.rights_evidence_path = "02-create/asset-manifest.csv"
$metadata.package_owner = "course learner"
$metadata.human_decision = "approve_private_dry_run"
$metadata.decision_reason = "All evidence and human review are complete."
$metadata.approval_scope = "one private non-executing preview"
$metadata.approval_expires_at = [datetimeoffset]::UtcNow.AddHours(2).ToString("o")
Write-Json (Join-Path $release "release-metadata.json") $metadata
& (Join-Path $assetRoot "build-release-package.ps1") -WorkRoot $workRoot
$metadata = Get-Content -Raw -LiteralPath (Join-Path $release "release-metadata.json") | ConvertFrom-Json
$metadata.approval_package_sha256 = $metadata.package_sha256
Write-Json (Join-Path $release "release-metadata.json") $metadata
Write-Json (Join-Path $release "denied-approval.json") ([ordered]@{
    run_id = "HB-001"
    status = "denied"
    publish_allowed = $false
    external_action_count = 0
})
Write-Json (Join-Path $release "private-release-approval.json") ([ordered]@{
    run_id = "HB-001"
    status = "dry_run_ready"
    publish_allowed = $false
    external_action_count = 0
    package_sha256 = $metadata.package_sha256
    approval_scope = $metadata.approval_scope
})

# Lab 8: analytics, operational evidence, complete controls, experiment, and integrated hand-over.
Copy-Asset "synthetic-pipeline-operations.csv" (Join-Path $learn "synthetic-pipeline-operations.csv")
Write-Json (Join-Path $learn "analytics-result.json") ([ordered]@{
    run_id = "HB-001"
    status = "analysis_ready"
    summary_by_hook = @(
        [ordered]@{ hook_family="clear_promise"; video_count=3; total_views=16200; completed_views=9598; saves=1003 },
        [ordered]@{ hook_family="question"; video_count=2; total_views=7000; completed_views=3532; saves=280 },
        [ordered]@{ hook_family="mistake"; video_count=2; total_views=9800; completed_views=5006; saves=443 }
    )
    low_volume_video_ids = @("HB-V05")
    recommended_scale_decision = "HOLD"
    caveats = @("Rows below the minimum-view threshold were excluded.", "Synthetic data cannot prove future causal performance.")
    external_action_count = 0
})
$ops = @(Import-Csv (Join-Path $learn "synthetic-pipeline-operations.csv"))
$accepted = @($ops | Where-Object accepted_status -eq "accepted")
$cost = [math]::Round((($ops | Measure-Object cost_sgd -Sum).Sum / $accepted.Count),2)
Write-Json (Join-Path $learn "operational-summary.json") ([ordered]@{
    baseline_job_count = @($ops | Where-Object phase -eq "baseline").Count
    pilot_job_count = @($ops | Where-Object phase -eq "pilot").Count
    cost_per_accepted_video_sgd = $cost
    human_review_capacity_sufficient = $true
    duplicate_release_actions = [int](($ops | Measure-Object duplicate_release_actions -Sum).Sum)
    rollback_all_tested = (-not ($ops | Where-Object rollback_tested -ne "true"))
    blocking_job_ids = @($ops | Where-Object { [int]$_.unresolved_rights_items -gt 0 -or [int]$_.blocking_review_findings -gt 0 } | ForEach-Object job_id)
})
$scoreRows = @(
    "accepted_video_cycle_time,yes,144 minutes,105.7 minutes,no increase after three-video canary,production owner,PASS,keep canary limit",
    "estimated_cost_per_accepted_video,yes,not separated,$cost SGD,within approved budget,production owner,PASS,monitor every run",
    "rework_rate,yes,100 percent,33 percent,no more than 20 percent,editor,HOLD,repair before scaling",
    "unresolved_rights_items,yes,one,one,zero at release gate,rights owner,HOLD,clear every blocker",
    "blocking_review_findings,yes,one,one,zero before private package,review owner,HOLD,repeat independent review",
    "duplicate_release_actions,yes,zero,zero,zero,release owner,PASS,retain idempotency key",
    "rollback_readiness,yes,tested,tested,tested checkpoint restore,operations owner,PASS,retain restore drill",
    "human_review_capacity,yes,three slots,three slots,covers every canary draft,review owner,PASS,do not exceed three drafts"
)
Write-Utf8 (Join-Path $learn "scaling-scorecard.csv") ("control,mandatory,baseline,pilot_evidence,threshold,owner,status,action`r`n" + ($scoreRows -join "`r`n") + "`r`n")
Write-Utf8 (Join-Path $learn "next-test.md") @"
# Decision
HOLD
# Observation
Pilot cycle time improved but rework and rights blockers remain.
# Caveat
The dataset is synthetic and rows below the minimum-view threshold were excluded.
# Hypothesis
A preflight rights checklist will reduce rework.
# Single change
Add a preflight rights checklist before asset acceptance.
# Held constant
Audience, script, duration, visibility, tools, and reviewer.
# Primary metric
Rework rate.
# Guardrails
Zero unresolved rights items and zero blocking review findings.
# Minimum sample
Three private canary drafts.
# Review date
2026-08-12.
# Stop rule
Stop immediately if a rights or quality blocker is found.
"@
Write-Json (Join-Path $learn "scale-decision.json") ([ordered]@{
    run_id = "HB-001"
    decision_version = "scale-v1"
    scale_decision = "HOLD"
    reason = "Rights and review blockers remain in the pilot evidence."
    canary_limit = 3
    visibility = "private"
    human_review_rate = 1.0
    next_owner = "production owner"
    rollback_path = "restore the last accepted Lab checkpoint and disable downstream tools"
})
$checkpoints = (1..8 | ForEach-Object { "LAB-CHECKPOINT-{0:00}" -f $_ }) -join "`r`n"
Write-Utf8 (Join-Path $learn "integrated-handover.md") @"
# Integrated hand-over
$checkpoints

artifact versions: contract-v1, script-v1, asset-manifest-v1, render-evidence-v1, final-review-v1, release-v1, scale-v1
unresolved issues: rights and independent-review blockers in pilot evidence
enabled tools: local validation and private dry-run preview
disabled tools: public publishing and credential exposure
approval scope: one private non-executing preview
metric decision: exclude low-volume rows from grouped results
scale decision: HOLD
rollback path: restore the last accepted checkpoint and disable downstream tools
next owner: production owner
"@

$validator = Join-Path $assetRoot "validate-lab-checkpoint.ps1"
foreach ($lab in 1..8) {
    & $validator -Lab $lab -WorkRoot $workRoot
}
Write-Host "All eight lab checkpoints PASS. Test fixture: $testRoot"
