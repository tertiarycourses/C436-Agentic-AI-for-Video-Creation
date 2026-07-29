param(
    [Parameter(Mandatory = $true)][string]$ProjectRoot,
    [string]$Version = "v1",
    [string]$EdlPath = ""
)

$resolvedProject = (Resolve-Path -LiteralPath $ProjectRoot).Path
if (-not $EdlPath) { $EdlPath = Join-Path $resolvedProject "edit-decision-list.json" }
$resolvedEdl = (Resolve-Path -LiteralPath $EdlPath).Path
$inputDir = Join-Path $resolvedProject "input"
$manifestPath = Join-Path $inputDir "asset-manifest.csv"
$narrationPath = Join-Path $inputDir "narration.txt"
$captionsPath = Join-Path $resolvedProject "captions-$Version.vtt"
$outputDir = Join-Path $resolvedProject "output"
$sceneDir = Join-Path $outputDir "scenes-$Version"
$draftPath = Join-Path $outputDir "vertical-draft-$Version.mp4"
$concatPath = Join-Path $outputDir "concat-$Version.txt"
$narrationWav = Join-Path $outputDir "narration-$Version.wav"
$logPath = Join-Path $outputDir "render-log-$Version.txt"
$fontCandidates = @(
    $(if ($env:WINDIR) { Join-Path $env:WINDIR "Fonts\arial.ttf" }),
    "/System/Library/Fonts/Supplemental/Arial.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
)
$fontPath = $fontCandidates | Where-Object { $_ -and (Test-Path -LiteralPath $_ -PathType Leaf) } | Select-Object -First 1
if (-not $fontPath) { throw "No supported local font was found for deterministic labels." }
$filterFontPath = ($fontPath -replace "\\", "/") -replace ":", "\:"

foreach ($tool in @("ffmpeg", "ffprobe")) {
    if (-not (Get-Command $tool -ErrorAction SilentlyContinue)) { throw "$tool is not available on PATH." }
}
foreach ($path in @($resolvedEdl, $manifestPath, $narrationPath, $captionsPath)) {
    if (-not (Test-Path -LiteralPath $path -PathType Leaf)) { throw "Missing required input: $path" }
}

New-Item -ItemType Directory -Force -Path $outputDir, $sceneDir | Out-Null
$edl = Get-Content -Raw -LiteralPath $resolvedEdl | ConvertFrom-Json
$manifest = Import-Csv -LiteralPath $manifestPath
if ($edl.width -ne 1080 -or $edl.height -ne 1920 -or $edl.frame_rate -ne 30) {
    throw "The supplied lab path requires 1080x1920 at 30 fps."
}

foreach ($scene in $edl.scenes) {
    $row = $manifest | Where-Object { $_.asset_id -eq $scene.asset_id -and $_.status -eq "accepted" } | Select-Object -First 1
    if (-not $row) { throw "No accepted manifest row for $($scene.asset_id)." }
    $source = Join-Path $inputDir $row.source_path
    if (-not (Test-Path -LiteralPath $source -PathType Leaf)) { throw "Missing accepted source: $source" }
}

$spokenText = Get-Content -Raw -LiteralPath $narrationPath
try {
    Add-Type -AssemblyName System.Speech -ErrorAction Stop
    $voice = New-Object System.Speech.Synthesis.SpeechSynthesizer
    $voice.SetOutputToWaveFile($narrationWav)
    $voice.Speak($spokenText)
    $voice.Dispose()
}
catch {
    $fallback = Join-Path $inputDir "narration-fallback.wav"
    if (-not (Test-Path -LiteralPath $fallback -PathType Leaf)) {
        throw "Speech synthesis unavailable and narration-fallback.wav is missing."
    }
    Copy-Item -LiteralPath $fallback -Destination $narrationWav -Force
}

$log = @("Run: $($edl.run_id)", "Edit decision list: $($edl.version)", "Manifest: $(Split-Path $manifestPath -Leaf)", "Started: $(Get-Date -Format o)")
$concatLines = @()
foreach ($scene in $edl.scenes) {
    if ($scene.duration_seconds -le 0) { throw "Invalid duration for $($scene.asset_id)." }
    $row = $manifest | Where-Object asset_id -eq $scene.asset_id | Select-Object -First 1
    $scenePath = Join-Path $sceneDir ("{0}.mp4" -f $scene.asset_id)
    $safeLabel = ($scene.label -replace ":", "\:" -replace "'", "")
    $safeSource = (($row.source_path -replace ":", "\:") -replace "'", "")
    $videoSource = "color=c=$($scene.colour):s=$($edl.width)x$($edl.height):r=$($edl.frame_rate):d=$($scene.duration_seconds)"
    $filter = "drawbox=x=90:y=120:w=900:h=300:color=black@0.38:t=fill,drawtext=fontfile='$filterFontPath':text='$safeLabel':fontcolor=white:fontsize=54:x=(w-text_w)/2:y=175,drawtext=fontfile='$filterFontPath':text='Accepted source\: $safeSource':fontcolor=white:fontsize=28:x=(w-text_w)/2:y=275"
    & ffmpeg -hide_banner -loglevel error -y -f lavfi -i $videoSource -vf $filter -an -c:v libx264 -preset veryfast -pix_fmt yuv420p -r $edl.frame_rate $scenePath
    if ($LASTEXITCODE -ne 0) { throw "Failed to render $($scene.asset_id)." }
    $concatLines += "file '$($scenePath -replace "\\", "/")'"
    $log += "Rendered $($scene.asset_id) from $($row.source_path) for $($scene.duration_seconds) seconds."
}

[System.IO.File]::WriteAllLines($concatPath, $concatLines, (New-Object System.Text.UTF8Encoding($false)))
$silentVideo = Join-Path $outputDir "silent-$Version.mp4"
& ffmpeg -hide_banner -loglevel error -y -f concat -safe 0 -i $concatPath -c copy $silentVideo
if ($LASTEXITCODE -ne 0) { throw "Failed to concatenate scenes." }

& ffmpeg -hide_banner -loglevel error -y -i $silentVideo -i $narrationWav -i $captionsPath `
    -map 0:v:0 -map 1:a:0 -map 2:0 -c:v copy -c:a aac -ar 48000 -ac 2 `
    -af "apad=pad_dur=30" -t 30 -c:s mov_text -metadata:s:s:0 language=eng `
    -movflags +faststart $draftPath
if ($LASTEXITCODE -ne 0 -or -not (Test-Path -LiteralPath $draftPath)) { throw "Failed to mux narration and captions." }

$log += "Narration: $narrationPath"
$log += "Captions: $captionsPath"
$log += "Draft: $draftPath"
$log += "Finished: $(Get-Date -Format o)"
Set-Content -LiteralPath $logPath -Value $log -Encoding utf8
Write-Host "Created $draftPath"
Write-Host "Created $logPath"
