param(
    [Parameter(Mandatory = $true)][string]$ProjectRoot,
    [string]$Version = "v1"
)

$root = (Resolve-Path -LiteralPath $ProjectRoot).Path
$videoPath = Join-Path $root "output/vertical-draft-$Version.mp4"
$probePath = Join-Path $root "output/ffprobe-$Version.json"
$captionPath = Join-Path $root "captions-$Version.vtt"
$logPath = Join-Path $root "output/render-log-$Version.txt"
$evidencePath = Join-Path $root "output/render-evidence-$Version.json"

foreach ($path in @($videoPath, $probePath, $captionPath, $logPath)) {
    if (-not (Test-Path -LiteralPath $path -PathType Leaf)) { throw "Missing render evidence input: $path" }
}

$probe = Get-Content -Raw -LiteralPath $probePath | ConvertFrom-Json
$video = $probe.streams | Where-Object codec_type -eq "video" | Select-Object -First 1
$audio = $probe.streams | Where-Object codec_type -eq "audio" | Select-Object -First 1
$subtitle = $probe.streams | Where-Object codec_type -eq "subtitle" | Select-Object -First 1
if (-not $video -or -not $audio -or -not $subtitle) { throw "Probe must contain video, audio, and subtitle streams." }

$evidence = [ordered]@{
    run_id = "HB-001"
    evidence_version = "render-evidence-$Version"
    video_path = "output/vertical-draft-$Version.mp4"
    video_sha256 = (Get-FileHash -Algorithm SHA256 -LiteralPath $videoPath).Hash.ToLowerInvariant()
    video_size_bytes = (Get-Item -LiteralPath $videoPath).Length
    probe_path = "output/ffprobe-$Version.json"
    probe_sha256 = (Get-FileHash -Algorithm SHA256 -LiteralPath $probePath).Hash.ToLowerInvariant()
    captions_path = "captions-$Version.vtt"
    captions_sha256 = (Get-FileHash -Algorithm SHA256 -LiteralPath $captionPath).Hash.ToLowerInvariant()
    render_log_path = "output/render-log-$Version.txt"
    render_log_sha256 = (Get-FileHash -Algorithm SHA256 -LiteralPath $logPath).Hash.ToLowerInvariant()
    technical = [ordered]@{
        codec_name = $video.codec_name
        width = [int]$video.width
        height = [int]$video.height
        frame_rate = $video.r_frame_rate
        pixel_format = $video.pix_fmt
        duration_seconds = [double]$probe.format.duration
        audio_codec = $audio.codec_name
        subtitle_codec = $subtitle.codec_name
    }
}

[System.IO.File]::WriteAllText(
    $evidencePath,
    ($evidence | ConvertTo-Json -Depth 10),
    (New-Object System.Text.UTF8Encoding($false))
)
Write-Host "Created $evidencePath"
