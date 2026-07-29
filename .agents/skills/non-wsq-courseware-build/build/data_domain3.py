"""Topic 3 labs: deterministic assembly and evidence-linked review."""

DOMAIN3 = [
    dict(
        num=5,
        topic=3,
        title="Assemble and Probe the Captioned Vertical Video",
        objective="LO3: assemble a reproducible short-form video with captions, branding, and technical evidence",
        duration=60,
        goal="Render a 9:16 draft from approved checkpoint files and prove its technical properties.",
        desc=(
            "You will use the supplied PowerShell and FFmpeg assembly path to "
            "verify the accepted manifest sources, create deterministic scene clips, "
            "add narrated audio and a muxed WebVTT-derived caption track. You will then probe the "
            "draft and save machine-readable technical evidence."
        ),
        build=(
            "A vertical-draft-v1.mp4, captions-v1.vtt, edit-decision-list.json, "
            "ffprobe-v1.json, render-log-v1.txt, and render-evidence-v1.json in stage folder 03-edit."
        ),
        services="PowerShell, FFmpeg, FFprobe, supplied assembly script",
        prerequisites=[
            "Complete Lab 4 or restore the approved placeholder asset pack.",
            "If FFmpeg is missing on Windows, run winget install --id Gyan.FFmpeg -e; on macOS, run brew install ffmpeg. Reopen the terminal.",
            "Run ffmpeg -version and ffprobe -version successfully before assembly.",
            "Confirm labs/assets/assemble-harbour-bean.ps1 and the Lab 3 captions-script-v1.vtt are present. If installation is not possible, use the supplied labs/assets/rejoin/lab-05 draft and probe package.",
        ],
        workflow=[
            "Validate inputs",
            "Build edit decision list",
            "Render vertical draft",
            "Attach caption evidence",
            "Save Lab checkpoint 05 in stage folder 03-edit",
        ],
        steps=[
            (
                "Create the edit checkpoint and copy the controlled inputs",
                "New-Item -ItemType Directory -Force -Path C436-work/HB-001/03-edit/input/media,C436-work/HB-001/03-edit/output | Out-Null\nCopy-Item -Recurse -Force C436-work/HB-001/02-create/media/* C436-work/HB-001/03-edit/input/media/\nCopy-Item C436-work/HB-001/02-create/asset-manifest.csv C436-work/HB-001/03-edit/input/asset-manifest.csv\nCopy-Item C436-work/HB-001/02-create/narration.txt C436-work/HB-001/03-edit/input/narration.txt\nCopy-Item labs/assets/narration-fallback.wav C436-work/HB-001/03-edit/input/narration-fallback.wav\nCopy-Item C436-work/HB-001/02-create/captions-script-v1.vtt C436-work/HB-001/03-edit/captions-v1.vtt\nCopy-Item labs/assets/edit-decision-list-approved.json C436-work/HB-001/03-edit/edit-decision-list.json",
            ),
            (
                "Validate the edit decision list",
                "Get-Content -Raw C436-work/HB-001/03-edit/edit-decision-list.json | ConvertFrom-Json | Select-Object run_id,version,target_duration_seconds,width,height,frame_rate | Format-List",
            ),
            (
                "Inspect the caption header and cues",
                "Get-Content C436-work/HB-001/03-edit/captions-v1.vtt | Select-Object -First 20",
            ),
            (
                "Run the deterministic assembly script",
                "PowerShell -ExecutionPolicy Bypass -File labs/assets/assemble-harbour-bean.ps1 -ProjectRoot C436-work/HB-001/03-edit",
            ),
            (
                "Confirm the expected render files exist",
                "Get-Item C436-work/HB-001/03-edit/output/vertical-draft-v1.mp4,C436-work/HB-001/03-edit/output/render-log-v1.txt | Select-Object Name,Length,LastWriteTime",
            ),
            (
                "Probe the rendered video to JSON",
                "ffprobe -v quiet -print_format json -show_format -show_streams C436-work/HB-001/03-edit/output/vertical-draft-v1.mp4 | Set-Content C436-work/HB-001/03-edit/output/ffprobe-v1.json",
            ),
            (
                "Bind the actual MP4, probe, captions, and log into render evidence",
                "PowerShell -ExecutionPolicy Bypass -File labs/assets/write-render-evidence.ps1 -ProjectRoot C436-work/HB-001/03-edit -Version v1",
            ),
            (
                "Run the fail-closed Lab 5 validator and retain technical evidence",
                "PowerShell -ExecutionPolicy Bypass -File labs/assets/validate-lab-checkpoint.ps1 -Lab 5 2>&1 | Tee-Object C436-work/HB-001/03-edit/lab-05-test-output.txt",
            ),
            (
                "Preview the complete draft with sound on and off",
                "Open C436-work/HB-001/03-edit/output/vertical-draft-v1.mp4 in a local media player. Confirm every scene appears in edit-decision-list order and the visual treatment does not obscure the subject.",
            ),
            (
                "Record the assembly decision",
                "Create assembly-approval.md with asset-manifest-v1, edl-v1, script-v1, render-evidence-v1, technical/editorial findings, and Decision=READY_FOR_QUALITY_REVIEW. Then write LAB-CHECKPOINT-05.txt.",
            ),
        ],
        test=(
            "The validator must print LAB-05 PASS. It hashes and inspects the actual "
            "MP4, probe, captions, and log; asserts H.264, 1080x1920, 30 fps, "
            "yuv420p, 30-second duration, audio/subtitles, ordered VTT, and approval."
        ),
        checkpoint=(
            "Lab checkpoint 05 is the complete 03-edit stage folder. The block below "
            "restores the mutually hashed video, probe, caption, log, and evidence "
            "files plus the human assembly decision before running the validator."
        ),
        rejoin_commands=(
            "Set-Location '<PATH_TO_C436_REPOSITORY>'\n"
            "$editPath='C436-work/HB-001/03-edit'\n"
            "$outputPath=\"$editPath/output\"\n"
            "New-Item -ItemType Directory -Force -Path $outputPath | Out-Null\n"
            "Copy-Item -LiteralPath labs/assets/rejoin/lab-05/vertical-draft-v1.mp4 -Destination \"$outputPath/vertical-draft-v1.mp4\" -Force\n"
            "Copy-Item -LiteralPath labs/assets/rejoin/lab-05/ffprobe-v1.json -Destination \"$outputPath/ffprobe-v1.json\" -Force\n"
            "Copy-Item -LiteralPath labs/assets/rejoin/lab-05/render-log-v1.txt -Destination \"$outputPath/render-log-v1.txt\" -Force\n"
            "Copy-Item -LiteralPath labs/assets/rejoin/lab-05/render-evidence-v1.json -Destination \"$outputPath/render-evidence-v1.json\" -Force\n"
            "Copy-Item -LiteralPath labs/assets/rejoin/lab-05/captions-v1.vtt -Destination \"$editPath/captions-v1.vtt\" -Force\n"
            "Copy-Item -LiteralPath labs/assets/assembly-approval-approved.md -Destination \"$editPath/assembly-approval.md\" -Force\n"
            "PowerShell -ExecutionPolicy Bypass -File labs/assets/validate-lab-checkpoint.ps1 -Lab 5 -WorkRoot C436-work/HB-001"
        ),
        troubleshooting=[
            (
                "PowerShell cannot find ffmpeg or ffprobe.",
                "Run the exact installer command in the prerequisites, reopen PowerShell, and rerun the version checks. If installation is unavailable, run the complete Checkpoint and Rejoin Point block; it restores all five mutually hashed evidence files and the assembly approval before validation.",
            ),
            (
                "The render is landscape or square.",
                "Confirm the edit decision list width is 1080 and height is 1920, then remove the incomplete output and rerun the supplied script.",
            ),
            (
                "The caption cues no longer match the edited timing.",
                "Update the cue times against the final narration and scene order, save a new caption version, and record the change before review.",
            ),
        ],
        challenge=(
            "Copy the EDL to edit-decision-list-v2.json, change adjacent scene/cue "
            "boundaries while preserving 30 seconds, copy captions-v1.vtt to "
            "captions-v2.vtt and update those boundaries, then run with -Version v2 "
            "-EdlPath C436-work/HB-001/03-edit/edit-decision-list-v2.json."
        ),
        reflection=(
            "Which editing operations were safer as deterministic commands than as "
            "open-ended agent decisions?"
        ),
    ),
    dict(
        num=6,
        topic=3,
        title="Run the Independent Video Review Gate and Repair One Finding",
        objective="LO3: review and refine a video through technical, editorial, accessibility, brand, rights, and release gates",
        duration=70,
        goal="Produce an evidence-linked issue register, repair a controlled defect, and obtain a human release-readiness decision.",
        desc=(
            "You will import an n8n review workflow that reads exact technical, "
            "caption, and manifest evidence, validates 28–32 seconds plus ordered "
            "contiguous cues, creates blocking and advisory findings, and "
            "never self-approves. You will inject a controlled defect, verify that "
            "the gate blocks, repair the data, rerun, and record the final human "
            "decision after watching the complete draft."
        ),
        build=(
            "A review-agent workflow export, issue-register-v1.json, "
            "issue-register-v2.json, repair-log.md, and final-review-approval.json."
        ),
        services="n8n, FFprobe evidence, text editor, local media player",
        prerequisites=[
            "Complete Lab 5 or restore Lab checkpoint 05 from stage folder 03-edit with a valid draft and probe.",
            "Confirm labs/assets/video-review-agent-workflow.json and review-rubric.csv are present.",
            "Keep the review workflow inactive and do not connect publishing tools.",
        ],
        workflow=[
            "Import independent review",
            "Inject a controlled defect",
            "Verify the blocking gate",
            "Repair and recheck",
            "Perform human final preview",
        ],
        steps=[
            (
                "Import and rename the review workflow",
                "In n8n, select Workflows > Create Workflow, import labs/assets/video-review-agent-workflow.json, rename it C436-HB-001-Video-Review-Gate, save it, and keep it inactive.",
            ),
            (
                "Inspect the gate structure",
                "Confirm it consumes exact FFprobe, WebVTT, and manifest evidence; enforces 28–32 seconds plus five ordered, positive, contiguous cues; keeps approval pending; and never emits release_approved.",
            ),
            (
                "Paste exact prior evidence and create a controlled missing-rights case",
                "Open Load Exact Review Evidence. Paste the complete Lab 5 ffprobe-v1.json, Lab 3 captions-script-v1.vtt, and Lab 4 asset-manifest.csv into the three named constants. In only the pasted manifest copy, change S01 rights_status to review_required and save.",
            ),
            (
                "Run the blocked review and save its output",
                "Select Test Workflow. Open Emit Issue Register, copy the complete JSON output, and save it to C436-work/HB-001/03-edit/issue-register-v1.json.",
            ),
            (
                "Verify the blocking finding",
                "$issues = Get-Content -Raw C436-work/HB-001/03-edit/issue-register-v1.json | ConvertFrom-Json\n$issues | Select-Object run_id,review_status,release_allowed\n$issues.findings | Format-Table issue_id,category,severity,evidence,required_action",
            ),
            (
                "Repair the controlled defect",
                "Return to Load Exact Review Evidence and repaste the unchanged exact Lab 4 asset-manifest.csv. Record the repair in C436-work/HB-001/03-edit/repair-log.md under issue RV-RIGHTS.",
            ),
            (
                "Rerun the review and save the clear result",
                "Select Test Workflow again. Save the Emit Issue Register JSON output as C436-work/HB-001/03-edit/issue-register-v2.json.",
            ),
            (
                "Verify that automation stops at review clear",
                "$clear = Get-Content -Raw C436-work/HB-001/03-edit/issue-register-v2.json | ConvertFrom-Json\nif ($clear.review_status -ne 'review_clear' -or $clear.release_allowed -ne $false -or $clear.owner_approval_status -ne 'pending') { throw 'Automated review did not stop before human approval.' }",
            ),
            (
                "Conduct the human full-length review",
                "Watch vertical-draft-v1.mp4 once with sound and once muted. Review the supplied rubric for story, claims, captions, mobile readability, brand, privacy, rights, disclosure, and technical output. Record timecoded observations.",
            ),
            (
                "Record the scoped decision",
                "$path='C436-work/HB-001/03-edit/final-review-approval.json'\nCopy-Item labs/assets/final-review-approval-template.json $path\n$a=Get-Content -Raw $path | ConvertFrom-Json\n$a.reviewer='<YOUR_NAME>'; $a.reviewed_at=[datetimeoffset]::UtcNow.ToString('o'); $a.decision='APPROVED_FOR_PRIVATE_RELEASE_PACKAGE'; $a.scope='private release package only; no public posting'; $a.reviewed_video_sha256=(Get-FileHash -Algorithm SHA256 C436-work/HB-001/03-edit/output/vertical-draft-v1.mp4).Hash.ToLowerInvariant(); $a.unresolved_blockers=@()\n$a | ConvertTo-Json -Depth 10 | Set-Content $path",
            ),
            (
                "Export the reviewed workflow",
                "Use n8n Download and save C436-work/HB-001/03-edit/video-review-agent-reviewed.json. Then run labs/assets/validate-lab-checkpoint.ps1 -Lab 6 and retain lab-06-test-output.txt.",
            ),
        ],
        test=(
            "The validator must print LAB-06 PASS: rights, invalid duration, or bad "
            "caption timing must block; repaired evidence stays non-releasing; the "
            "human JSON approval must bind the actual video hash and private-only scope."
        ),
        checkpoint=(
            "Lab checkpoint 06 adds both issue registers, the repair log, structured human final "
            "review, and exported workflow to C436-work/HB-001/03-edit. Keep v1 "
            "evidence to prove the defect. The trainer-approved rejoin block below "
            "restores exact review artifacts and verifies that the final approval "
            "names the SHA-256 of the supplied Lab 5 MP4."
        ),
        rejoin_commands=(
            "Set-Location '<PATH_TO_C436_REPOSITORY>'\n"
            "$editPath='C436-work/HB-001/03-edit'\n"
            "if(-not (Test-Path -LiteralPath \"$editPath/output/vertical-draft-v1.mp4\")){throw 'Run the complete Lab 5 rejoin block first.'}\n"
            "Copy-Item -LiteralPath labs/assets/issue-register-blocked-example.json -Destination \"$editPath/issue-register-v1.json\" -Force\n"
            "Copy-Item -LiteralPath labs/assets/issue-register-clear-example.json -Destination \"$editPath/issue-register-v2.json\" -Force\n"
            "Copy-Item -LiteralPath labs/assets/repair-log-approved.md -Destination \"$editPath/repair-log.md\" -Force\n"
            "Copy-Item -LiteralPath labs/assets/final-review-approval-approved.json -Destination \"$editPath/final-review-approval.json\" -Force\n"
            "$approval=Get-Content -Raw -LiteralPath \"$editPath/final-review-approval.json\" | ConvertFrom-Json\n"
            "$videoHash=(Get-FileHash -Algorithm SHA256 -LiteralPath \"$editPath/output/vertical-draft-v1.mp4\").Hash.ToLowerInvariant()\n"
            "if($approval.reviewed_video_sha256 -ne $videoHash){throw 'Final approval does not match the restored video.'}\n"
            "PowerShell -ExecutionPolicy Bypass -File labs/assets/validate-lab-checkpoint.ps1 -Lab 6 -WorkRoot C436-work/HB-001"
        ),
        troubleshooting=[
            (
                "The clear run still contains the rights blocker.",
                "Confirm the edited evidence node was saved and run from the workflow trigger rather than a downstream node with pinned data.",
            ),
            (
                "The review result sets release_allowed=true.",
                "Stop. Restore the supplied workflow and confirm the final deterministic gate always sets release_allowed=false pending a separate approval token.",
            ),
            (
                "The video preview reveals a new issue not in the automated output.",
                "Record it with evidence and severity, repair it, and rerun only the affected technical checks plus the complete human preview.",
            ),
        ],
        challenge=(
            "Add a blocking rule for duplicate WebVTT cue identifiers, prove it with "
            "a controlled duplicate cue ID, then restore the approved caption file "
            "and confirm the full review returns review_clear."
        ),
        reflection=(
            "What important quality judgment remained invisible to the automated "
            "review evidence?"
        ),
    ),
]
