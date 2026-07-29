param(
    [Parameter(Mandatory = $true)][ValidateRange(1, 8)][int]$Lab,
    [string]$WorkRoot = "C436-work/HB-001"
)

function Assert-True([bool]$Condition, [string]$Message) {
    if (-not $Condition) { throw $Message }
}
function Assert-File([string]$Path) {
    Assert-True (Test-Path -LiteralPath $Path -PathType Leaf) "Missing file: $Path"
}
function Read-Json([string]$Path) {
    Assert-File $Path
    return Get-Content -Raw -LiteralPath $Path | ConvertFrom-Json
}
function File-Hash([string]$Path) {
    Assert-File $Path
    return (Get-FileHash -Algorithm SHA256 -LiteralPath $Path).Hash.ToLowerInvariant()
}
function Assert-TextContains([string]$Path, [string[]]$Required) {
    Assert-File $Path
    $text = Get-Content -Raw -LiteralPath $Path
    foreach ($item in $Required) {
        Assert-True ($text -match [regex]::Escape($item)) "Missing required text '$item' in $Path"
    }
}
function Test-Vtt([string]$Path, [int]$ExpectedCues, [double]$ExpectedEnd) {
    Assert-File $Path
    $lines = Get-Content -LiteralPath $Path
    Assert-True ($lines[0] -eq "WEBVTT") "Caption file must begin with WEBVTT."
    $cueLines = @($lines | Where-Object { $_ -match " --> " })
    Assert-True ($cueLines.Count -eq $ExpectedCues) "Caption cue count is invalid."
    $previousEnd = 0.0
    foreach ($line in $cueLines) {
        $parts = $line -split " --> "
        Assert-True ($parts.Count -eq 2) "Invalid VTT cue line: $line"
        $start = [timespan]::ParseExact($parts[0], "hh\:mm\:ss\.fff", $null).TotalSeconds
        $end = [timespan]::ParseExact($parts[1], "hh\:mm\:ss\.fff", $null).TotalSeconds
        Assert-True ($end -gt $start) "VTT cue end must be after start."
        Assert-True ([math]::Abs($start - $previousEnd) -le 0.001) "VTT cues must be ordered and contiguous."
        $previousEnd = $end
    }
    Assert-True ([math]::Abs($previousEnd - $ExpectedEnd) -le 0.25) "VTT final cue does not match the expected duration."
}

$design = Join-Path $WorkRoot "01-design"
$create = Join-Path $WorkRoot "02-create"
$edit = Join-Path $WorkRoot "03-edit"
$release = Join-Path $WorkRoot "04-release"
$learn = Join-Path $WorkRoot "05-learn"

switch ($Lab) {
    1 {
        $c = Read-Json (Join-Path $design "production-contract.json")
        Assert-True ($c.run_id -eq "HB-001" -and $c.contract_version -eq "contract-v1") "Contract identity/version is invalid."
        Assert-True (($c.duration_seconds -is [long] -or $c.duration_seconds -is [int]) -and $c.duration_seconds -eq 30) "duration_seconds must be integer 30."
        Assert-True ($c.max_generation_attempts_per_scene -eq 2) "Retry limit must be 2."
        Assert-True (($c.cost_budget_sgd -is [double] -or $c.cost_budget_sgd -is [decimal] -or $c.cost_budget_sgd -is [long] -or $c.cost_budget_sgd -is [int]) -and $c.cost_budget_sgd -gt 0) "cost_budget_sgd must be a positive number."
        $rows = Import-Csv (Join-Path $design "autonomy-matrix.csv")
        Assert-True ($rows.Count -eq 9) "Autonomy matrix must contain all 9 tasks."
        Assert-True (-not ($rows | Where-Object { @("deterministic","model_assisted","human_approved","prohibited") -notcontains $_.autonomy_level })) "Every autonomy level must be allowed."
        Assert-True (($rows | Where-Object task -eq "publish_publicly").autonomy_level -eq "prohibited") "Public publishing must remain prohibited."
        Assert-True (($rows | Where-Object task -eq "expose_secret").autonomy_level -eq "prohibited") "Secret exposure must be prohibited."
    }
    2 {
        $ready = Read-Json (Join-Path $design "ready-run.json")
        $blocked = Read-Json (Join-Path $design "blocked-run.json")
        $restored = Read-Json (Join-Path $design "ready-restored-run.json")
        foreach ($result in @($ready, $restored)) {
            Assert-True ($result.status -eq "plan_ready" -and $result.next_stage -eq "research_and_script" -and $result.publish_allowed -eq $false) "Ready plan contract failed."
            Assert-True ($result.contract_version -eq "contract-v1" -and -not [string]::IsNullOrWhiteSpace($result.source_fingerprint)) "Ready plan lacks version/fingerprint."
        }
        Assert-True ($ready.source_fingerprint -eq $restored.source_fingerprint) "Restored plan fingerprint changed."
        Assert-True ($blocked.status -eq "blocked" -and $blocked.blockers -contains "missing_approved_facts" -and $blocked.publish_allowed -eq $false) "Blocked run did not fail closed."
    }
    3 {
        $plan = Read-Json (Join-Path $design "ready-restored-run.json")
        Assert-True ($plan.status -eq "plan_ready" -and $plan.next_stage -eq "research_and_script" -and -not [string]::IsNullOrWhiteSpace($plan.source_fingerprint)) "Lab 2 plan hand-off is invalid."
        Assert-TextContains (Join-Path $create "research-script-prompt.txt") @($plan.source_fingerprint)
        $story = Read-Json (Join-Path $create "script-storyboard.json")
        Assert-True ($story.run_id -eq "HB-001" -and $story.status -eq "script_ready" -and $story.script_version -eq "script-v1") "Storyboard identity/status/version is invalid."
        Assert-True ($story.plan_source_fingerprint -eq $plan.source_fingerprint) "Storyboard is not bound to the exact Lab 2 plan fingerprint."
        Assert-True ($story.concepts.Count -ge 3 -and $story.beats.Count -gt 0) "At least three concepts and one beat are required."
        $previousEnd = 0
        foreach ($beat in $story.beats) {
            Assert-True ($beat.beat_id -and $beat.narration -and $beat.visual_request -and $beat.source_ids.Count -gt 0) "A beat is missing required fields."
            Assert-True ([double]$beat.start_seconds -eq [double]$previousEnd -and [double]$beat.end_seconds -gt [double]$beat.start_seconds) "Beat timing is not ordered and contiguous."
            $previousEnd = [double]$beat.end_seconds
        }
        Assert-True ($previousEnd -eq [double]$story.total_duration_seconds -and $previousEnd -le 30) "Storyboard duration is invalid."
        Test-Vtt (Join-Path $create "captions-script-v1.vtt") $story.beats.Count $story.total_duration_seconds
        Assert-TextContains (Join-Path $create "storyboard-approval.md") @("APPROVED_FOR_ASSET_REQUESTS","script_version=script-v1","approved_by=")
    }
    4 {
        $manifest = @(Import-Csv (Join-Path $create "asset-manifest.csv"))
        $expectedIds = @("S01","S02","S03","S04","S05","A01","A02")
        Assert-True ($manifest.Count -eq $expectedIds.Count) "Manifest must contain exactly five scenes, narration, and music."
        foreach ($field in @("run_id","asset_id","beat_id","type","prompt_version","tool","source_path","provenance","rights_status","status")) {
            Assert-True (-not ($manifest | Where-Object { [string]::IsNullOrWhiteSpace($_.$field) })) "Manifest field '$field' contains a blank."
        }
        Assert-True ((($manifest.asset_id | Sort-Object) -join ",") -eq (($expectedIds | Sort-Object) -join ",")) "Manifest asset IDs do not match the required set."
        Assert-True (($manifest | Where-Object { $_.asset_id -like "S*" -and $_.type -ne "video" }).Count -eq 0) "Scene asset types must be video."
        Assert-True (($manifest | Where-Object asset_id -eq "A01").type -eq "narration") "A01 must be narration."
        Assert-True (($manifest | Where-Object asset_id -eq "A02").type -eq "music") "A02 must be music."
        Assert-True (-not ($manifest | Where-Object { $_.run_id -ne "HB-001" -or $_.rights_status -ne "approved_for_course_use" -or $_.status -ne "accepted" })) "Every required asset must be accepted with approved course-use rights."
        Assert-True (($manifest.asset_id | Sort-Object -Unique).Count -eq $manifest.Count) "asset_id values must be unique."
        foreach ($row in $manifest) { Assert-File (Join-Path $create $row.source_path) }
        Assert-TextContains (Join-Path $create "music-brief.md") @("approved_for_course_use","APPROVED_FOR_COURSE_USE")
        Assert-TextContains (Join-Path $create "asset-pack-approval.md") @("APPROVED_FOR_ASSEMBLY","manifest_version=asset-manifest-v1","approved_by=")
    }
    5 {
        $videoPath = Join-Path $edit "output/vertical-draft-v1.mp4"
        $probePath = Join-Path $edit "output/ffprobe-v1.json"
        $captionPath = Join-Path $edit "captions-v1.vtt"
        $logPath = Join-Path $edit "output/render-log-v1.txt"
        $evidence = Read-Json (Join-Path $edit "output/render-evidence-v1.json")
        Assert-True ($evidence.video_sha256 -eq (File-Hash $videoPath)) "Render evidence does not match the actual MP4."
        Assert-True ($evidence.probe_sha256 -eq (File-Hash $probePath)) "Render evidence does not match the probe JSON."
        Assert-True ($evidence.captions_sha256 -eq (File-Hash $captionPath)) "Render evidence does not match captions."
        Assert-True ($evidence.render_log_sha256 -eq (File-Hash $logPath)) "Render evidence does not match the render log."
        $probe = Read-Json $probePath
        $video = $probe.streams | Where-Object codec_type -eq "video" | Select-Object -First 1
        $audio = $probe.streams | Where-Object codec_type -eq "audio" | Select-Object -First 1
        $sub = $probe.streams | Where-Object codec_type -eq "subtitle" | Select-Object -First 1
        Assert-True ($video.width -eq 1080 -and $video.height -eq 1920 -and $video.codec_name -eq "h264" -and $video.pix_fmt -eq "yuv420p" -and $video.r_frame_rate -eq "30/1") "Video technical properties are invalid."
        Assert-True ($null -ne $audio -and $null -ne $sub) "Draft must contain narration audio and a muxed caption track."
        Assert-True ([math]::Abs([double]$probe.format.duration - 30) -le 0.25) "Draft duration must be within 0.25 seconds of 30."
        Test-Vtt $captionPath 5 ([double]$probe.format.duration)
        if (Get-Command ffprobe -ErrorAction SilentlyContinue) {
            $live = (& ffprobe -v quiet -print_format json -show_format -show_streams $videoPath | Out-String) | ConvertFrom-Json
            Assert-True ([math]::Abs([double]$live.format.duration - [double]$probe.format.duration) -le 0.01) "Stored probe duration does not match the actual MP4."
            Assert-True (($live.streams | Where-Object codec_type -eq "video" | Select-Object -First 1).codec_name -eq $video.codec_name) "Stored probe codec does not match the actual MP4."
        }
        Assert-TextContains (Join-Path $edit "assembly-approval.md") @("READY_FOR_QUALITY_REVIEW","render-evidence-v1")
    }
    6 {
        $blocked = Read-Json (Join-Path $edit "issue-register-v1.json")
        $clear = Read-Json (Join-Path $edit "issue-register-v2.json")
        Assert-True ($blocked.review_status -eq "blocked" -and ($blocked.findings.issue_id -contains "RV-RIGHTS")) "Controlled rights blocker is missing."
        Assert-True ($clear.review_status -eq "review_clear" -and $clear.release_allowed -eq $false -and $clear.requires_human_preview -eq $true -and $clear.caption_timeline_valid -eq $true) "Clear automated review must retain human control."
        Assert-True ($clear.duration_seconds -ge 28 -and $clear.duration_seconds -le 32) "Clear review duration is outside 28-32 seconds."
        $approval = Read-Json (Join-Path $edit "final-review-approval.json")
        Assert-True ($approval.run_id -eq "HB-001" -and $approval.approval_version -eq "final-review-v1") "Final review approval identity/version is invalid."
        Assert-True ($approval.decision -eq "APPROVED_FOR_PRIVATE_RELEASE_PACKAGE" -and $approval.scope -eq "private release package only; no public posting") "Final review decision/scope is invalid."
        Assert-True ($approval.reviewed_video_sha256 -eq (File-Hash (Join-Path $edit "output/vertical-draft-v1.mp4"))) "Final review approval is not bound to the actual video."
        Assert-True ($approval.unresolved_blockers.Count -eq 0 -and -not [string]::IsNullOrWhiteSpace($approval.reviewer) -and -not [string]::IsNullOrWhiteSpace($approval.reviewed_at)) "Final review record is incomplete."
    }
    7 {
        $meta = Read-Json (Join-Path $release "release-metadata.json")
        $manifestPath = Join-Path $WorkRoot $meta.package_manifest_path
        $manifest = Read-Json $manifestPath
        $manifestHash = File-Hash $manifestPath
        Assert-True ($meta.package_sha256 -eq $manifestHash -and $meta.approval_package_sha256 -eq $manifestHash) "Approval is not bound to the canonical package manifest."
        Assert-True ([datetimeoffset]::Parse($meta.approval_expires_at) -gt [datetimeoffset]::UtcNow) "Approval has expired."
        Assert-True ($manifest.title -eq $meta.title -and $manifest.description -eq $meta.description -and $manifest.privacy_status -eq "private" -and $manifest.contains_synthetic_media -eq $true) "Metadata differs from the canonical package."
        Assert-True ($manifest.video.sha256 -eq (File-Hash (Join-Path $WorkRoot $manifest.video.path))) "Package video hash mismatch."
        Assert-True ($manifest.captions.sha256 -eq (File-Hash (Join-Path $WorkRoot $manifest.captions.path))) "Package caption hash mismatch."
        Assert-True ($manifest.rights_manifest.sha256 -eq (File-Hash (Join-Path $WorkRoot $manifest.rights_manifest.path))) "Package rights hash mismatch."
        Assert-True ($manifest.final_review_approval.sha256 -eq (File-Hash (Join-Path $WorkRoot $manifest.final_review_approval.path)) -and $meta.final_review_approval_sha256 -eq $manifest.final_review_approval.sha256) "Package final-review approval hash mismatch."
        Assert-True ($manifest.final_review_approval.decision -eq "APPROVED_FOR_PRIVATE_RELEASE_PACKAGE" -and $manifest.final_review_approval.reviewed_video_sha256 -eq $manifest.video.sha256) "Package does not contain a valid Lab 6 approval."
        Assert-True ($manifest.platform_previews.youtube.privacyStatus -eq "private" -and $manifest.platform_previews.youtube.containsSyntheticMedia -eq $true -and $manifest.platform_previews.youtube.execute -eq $false) "YouTube preview schema is invalid."
        Assert-True ($manifest.platform_previews.tiktok.method -eq "POST /v2/post/publish/video/init/" -and $manifest.platform_previews.tiktok.privacy_level -eq "SELF_ONLY" -and $manifest.platform_previews.tiktok.is_aigc -eq $true -and $manifest.platform_previews.tiktok.video_size -gt 0 -and $manifest.platform_previews.tiktok.chunk_size -eq $manifest.platform_previews.tiktok.video_size -and $manifest.platform_previews.tiktok.total_chunk_count -eq 1 -and $manifest.platform_previews.tiktok.execute -eq $false) "TikTok preview schema is invalid."
        $denied = Read-Json (Join-Path $release "denied-approval.json")
        $approved = Read-Json (Join-Path $release "private-release-approval.json")
        Assert-True ($denied.external_action_count -eq 0 -and $denied.publish_allowed -eq $false) "Denial path must have zero actions."
        Assert-True ($approved.status -eq "dry_run_ready" -and $approved.external_action_count -eq 0 -and $approved.publish_allowed -eq $false) "Private dry run must not execute externally."
    }
    8 {
        $result = Read-Json (Join-Path $learn "analytics-result.json")
        Assert-True ($result.summary_by_hook.Count -gt 0 -and $result.low_volume_video_ids -contains "HB-V05") "Analytics result lacks grouped/low-volume evidence."
        $question = $result.summary_by_hook | Where-Object hook_family -eq "question"
        Assert-True ($question.video_count -eq 2 -and $question.total_views -eq 7000) "Low-volume question row was included in the aggregate."
        $ops = @(Import-Csv (Join-Path $learn "synthetic-pipeline-operations.csv"))
        Assert-True ((($ops.phase | Sort-Object -Unique) -join ",") -eq "baseline,pilot") "Operational evidence must contain baseline and pilot rows."
        Assert-True (-not ($ops | Where-Object { [string]::IsNullOrWhiteSpace($_.human_review_capacity_slots) -or [string]::IsNullOrWhiteSpace($_.human_reviews_required) })) "Human-review capacity evidence is missing."
        $accepted = @($ops | Where-Object accepted_status -eq "accepted")
        Assert-True ($accepted.Count -gt 0) "No accepted jobs exist for cost calculation."
        $costPerAccepted = [math]::Round((($ops | Measure-Object cost_sgd -Sum).Sum / $accepted.Count), 2)
        $summary = Read-Json (Join-Path $learn "operational-summary.json")
        Assert-True ([math]::Abs([double]$summary.cost_per_accepted_video_sgd - $costPerAccepted) -le 0.01) "Operational cost calculation is invalid."
        Assert-True ($summary.baseline_job_count -gt 0 -and $summary.pilot_job_count -gt 0 -and $summary.human_review_capacity_sufficient -eq $true) "Operational phase/capacity summary is incomplete."
        Assert-True ($summary.rollback_all_tested -eq $true -and [int]$summary.duplicate_release_actions -eq 0) "Rollback readiness or duplicate-release evidence failed."
        $score = @(Import-Csv (Join-Path $learn "scaling-scorecard.csv"))
        $expectedControls = @("accepted_video_cycle_time","estimated_cost_per_accepted_video","rework_rate","unresolved_rights_items","blocking_review_findings","duplicate_release_actions","rollback_readiness","human_review_capacity")
        Assert-True ($score.Count -eq $expectedControls.Count -and ((($score.control | Sort-Object) -join ",") -eq (($expectedControls | Sort-Object) -join ","))) "Scaling scorecard controls do not match the required set."
        foreach ($field in @("baseline","pilot_evidence","threshold","owner","status","action")) {
            Assert-True (-not ($score | Where-Object { [string]::IsNullOrWhiteSpace($_.$field) -or $_.$field -match "<COMPLETE_ME>" })) "Scorecard field '$field' is incomplete."
        }
        Assert-TextContains (Join-Path $learn "next-test.md") @("Decision","Observation","Caveat","Hypothesis","Single change","Held constant","Primary metric","Guardrails","Minimum sample","Review date","Stop rule")
        $decision = Read-Json (Join-Path $learn "scale-decision.json")
        Assert-True (@("HOLD","PILOT_3_PER_WEEK","SCALE_WITH_LIMITS") -contains $decision.scale_decision) "Scale decision is invalid."
        $hasBlockers = @($ops | Where-Object {
            [int]$_.unresolved_rights_items -gt 0 -or
            [int]$_.blocking_review_findings -gt 0 -or
            [int]$_.duplicate_release_actions -gt 0 -or
            $_.rollback_tested -ne "true" -or
            [int]$_.human_review_capacity_slots -lt [int]$_.human_reviews_required
        }).Count -gt 0
        if ($hasBlockers) { Assert-True ($decision.scale_decision -eq "HOLD" -and $score.status -contains "HOLD") "Blocking evidence must force HOLD." }
        Assert-True ($decision.canary_limit -eq 3 -and $decision.visibility -eq "private" -and [double]$decision.human_review_rate -eq 1.0 -and -not [string]::IsNullOrWhiteSpace($decision.next_owner)) "Canary/human-review decision controls are incomplete."
        $handoverPath = Join-Path $learn "integrated-handover.md"
        $handover = Get-Content -Raw -LiteralPath $handoverPath
        foreach ($n in 1..8) { Assert-True ($handover -match ("LAB-CHECKPOINT-{0:00}" -f $n)) "Integrated handover is missing Lab checkpoint $n." }
        Assert-TextContains $handoverPath @("artifact versions","unresolved issues","enabled tools","disabled tools","approval scope","metric decision","scale decision","rollback path","next owner")
    }
}

Write-Host "LAB-$('{0:00}' -f $Lab) PASS | $((Get-Date).ToString('o'))"
