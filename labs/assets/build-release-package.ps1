param(
    [Parameter(Mandatory = $true)][string]$WorkRoot
)

$root = (Resolve-Path -LiteralPath $WorkRoot).Path
$metadataPath = Join-Path $root "04-release/release-metadata.json"
if (-not (Test-Path -LiteralPath $metadataPath -PathType Leaf)) { throw "Missing release metadata: $metadataPath" }
$metadata = Get-Content -Raw -LiteralPath $metadataPath | ConvertFrom-Json

function Resolve-RequiredFile([string]$RelativePath) {
    if ([string]::IsNullOrWhiteSpace($RelativePath)) { throw "A required package path is blank." }
    $path = Join-Path $root $RelativePath
    if (-not (Test-Path -LiteralPath $path -PathType Leaf)) { throw "Missing package file: $path" }
    return (Resolve-Path -LiteralPath $path).Path
}
function File-Record([string]$RelativePath) {
    $path = Resolve-RequiredFile $RelativePath
    return [ordered]@{
        path = $RelativePath
        sha256 = (Get-FileHash -Algorithm SHA256 -LiteralPath $path).Hash.ToLowerInvariant()
        size_bytes = (Get-Item -LiteralPath $path).Length
    }
}

$video = File-Record $metadata.video_path
$captions = File-Record $metadata.caption_path
$rights = File-Record $metadata.rights_evidence_path
$approvalPath = Resolve-RequiredFile $metadata.final_review_approval_path
$approval = Get-Content -Raw -LiteralPath $approvalPath | ConvertFrom-Json
$approvalHash = (Get-FileHash -Algorithm SHA256 -LiteralPath $approvalPath).Hash.ToLowerInvariant()

if ($approval.decision -ne "APPROVED_FOR_PRIVATE_RELEASE_PACKAGE") { throw "Final review approval decision is not valid." }
if ($approval.scope -ne "private release package only; no public posting") { throw "Final review approval scope is invalid." }
if ($approval.reviewed_video_sha256 -ne $video.sha256) { throw "Final review approval does not bind to the current video." }

$manifest = [ordered]@{
    run_id = $metadata.run_id
    package_version = $metadata.package_version
    platform = $metadata.platform
    title = $metadata.title
    description = $metadata.description
    privacy_status = $metadata.privacy_status
    scheduled_time = $metadata.scheduled_time
    contains_synthetic_media = [bool]$metadata.contains_synthetic_media
    package_owner = $metadata.package_owner
    video = $video
    captions = $captions
    rights_manifest = $rights
    final_review_approval = [ordered]@{
        path = $metadata.final_review_approval_path
        sha256 = $approvalHash
        approval_version = $approval.approval_version
        decision = $approval.decision
        scope = $approval.scope
        reviewed_video_sha256 = $approval.reviewed_video_sha256
    }
    platform_previews = [ordered]@{
        youtube = [ordered]@{
            method = "videos.insert"
            privacyStatus = "private"
            containsSyntheticMedia = $true
            execute = $false
        }
        tiktok = [ordered]@{
            method = "POST /v2/post/publish/video/init/"
            privacy_level = "SELF_ONLY"
            is_aigc = $true
            source = "FILE_UPLOAD"
            video_size = [long]$video.size_bytes
            chunk_size = [long]$video.size_bytes
            total_chunk_count = 1
            execute = $false
        }
    }
}

$manifestPath = Join-Path $root $metadata.package_manifest_path
New-Item -ItemType Directory -Force -Path (Split-Path -Parent $manifestPath) | Out-Null
$manifestJson = $manifest | ConvertTo-Json -Depth 15
[System.IO.File]::WriteAllText($manifestPath, $manifestJson, (New-Object System.Text.UTF8Encoding($false)))

$metadata.package_manifest = $manifest
$metadata.package_sha256 = (Get-FileHash -Algorithm SHA256 -LiteralPath $manifestPath).Hash.ToLowerInvariant()
$metadata.final_review_approval_sha256 = $approvalHash
[System.IO.File]::WriteAllText(
    $metadataPath,
    ($metadata | ConvertTo-Json -Depth 20),
    (New-Object System.Text.UTF8Encoding($false))
)

Write-Host "Created canonical package manifest: $manifestPath"
Write-Host "Updated release metadata with package and approval hashes."
