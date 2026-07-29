param(
    [Parameter(Mandatory = $true)][string]$StoryboardPath,
    [Parameter(Mandatory = $true)][string]$OutputPath
)

function Convert-ToVttTime([double]$Seconds) {
    $span = [TimeSpan]::FromSeconds($Seconds)
    return "{0:00}:{1:00}:{2:00}.{3:000}" -f [math]::Floor($span.TotalHours), $span.Minutes, $span.Seconds, $span.Milliseconds
}

$story = Get-Content -Raw -LiteralPath $StoryboardPath | ConvertFrom-Json
if ($story.status -ne "script_ready" -or -not $story.beats) {
    throw "Storyboard must have status=script_ready and at least one beat."
}

$lines = @("WEBVTT", "", "NOTE run_id=$($story.run_id); script_version=script-v1", "")
$previousEnd = 0
foreach ($beat in $story.beats) {
    if ([double]$beat.start_seconds -ne [double]$previousEnd -or [double]$beat.end_seconds -le [double]$beat.start_seconds) {
        throw "Beat timing is not contiguous at $($beat.beat_id)."
    }
    $lines += $beat.beat_id
    $lines += "$(Convert-ToVttTime $beat.start_seconds) --> $(Convert-ToVttTime $beat.end_seconds)"
    $lines += [string]$beat.narration
    $lines += ""
    $previousEnd = [double]$beat.end_seconds
}
if ($previousEnd -ne [double]$story.total_duration_seconds) {
    throw "Last cue does not end at total_duration_seconds."
}

[System.IO.File]::WriteAllLines($OutputPath, $lines, (New-Object System.Text.UTF8Encoding($false)))
Write-Host "Created $OutputPath with $($story.beats.Count) cues."
