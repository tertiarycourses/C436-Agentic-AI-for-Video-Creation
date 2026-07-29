"""Topic 2 labs: research, scripting, storyboards, and media requests."""

DOMAIN2 = [
    dict(
        num=3,
        topic=2,
        title="Run the Research-to-Script Agent and Approve a Timed Storyboard",
        objective="LO2: create evidence-linked research, script, caption, and storyboard hand-offs from an approved brief",
        duration=65,
        goal="Produce one approved 30-second concept whose claims and scenes are traceable to the supplied evidence.",
        desc=(
            "You will use an approved AI assistant with a structured B-R-I-E-F "
            "prompt, or the supplied offline result, to cluster synthetic audience "
            "signals, propose distinct concepts, and return a timed script and "
            "storyboard. You will validate the schema and manually approve only "
            "evidence-linked content."
        ),
        build=(
            "A source-register.csv, research-script-prompt.txt, "
            "script-storyboard.json, captions-script-v1.vtt, and storyboard-approval.md in stage folder 02-create."
        ),
        services="Approved AI assistant or offline fallback, text editor, supplied synthetic data",
        prerequisites=[
            "Complete Labs 1 and 2 or restore Lab checkpoint 02, including ready-restored-run.json, from stage folder 01-design.",
            "Confirm labs/assets/audience-signals.csv, harbour-bean-brand-brief.md, and research-script-prompt-template.txt are present.",
            "Use only the supplied synthetic inputs; do not search for or add personal audience data.",
        ],
        workflow=[
            "Register evidence",
            "Run a structured prompt",
            "Validate timed output",
            "Review claims and scenes",
            "Save Lab checkpoint 03 in stage folder 02-create",
        ],
        steps=[
            (
                "Validate and consume the Lab 2 planning hand-off",
                "$plan=Get-Content -Raw C436-work/HB-001/01-design/ready-restored-run.json | ConvertFrom-Json\nif($plan.status -ne 'plan_ready' -or $plan.next_stage -ne 'research_and_script' -or [string]::IsNullOrWhiteSpace($plan.source_fingerprint)){throw 'Lab 2 planning hand-off is invalid.'}\n$plan | Select-Object run_id,contract_version,source_fingerprint,status,next_stage",
            ),
            (
                "Create the topic 2 checkpoint folder",
                "New-Item -ItemType Directory -Force -Path C436-work/HB-001/02-create | Out-Null",
            ),
            (
                "Copy the synthetic evidence and prompt template",
                "Copy-Item -LiteralPath labs/assets/audience-signals.csv -Destination C436-work/HB-001/02-create/source-register.csv\nCopy-Item -LiteralPath labs/assets/research-script-prompt-template.txt -Destination C436-work/HB-001/02-create/research-script-prompt.txt",
            ),
            (
                "Inspect the source register before prompting",
                "Import-Csv C436-work/HB-001/02-create/source-register.csv | Format-Table source_id,observation,evidence_type,allowed_use",
            ),
            (
                "Complete the prompt placeholders from the approved production contract",
                "Open research-script-prompt.txt. Set run ID HB-001 and paste the exact source_fingerprint from ready-restored-run.json. Set the audience, 30-second duration, 9:16 aspect ratio, three concepts, and required JSON schema. Paste the approved facts and source rows.",
            ),
            (
                "Run the prompt in an approved AI assistant",
                "Start a new chat, paste the completed prompt, and do not enable external actions. If unavailable, run: Copy-Item labs/assets/script-storyboard-approved.json C436-work/HB-001/02-create/script-storyboard.json, then continue at validation.",
            ),
            (
                "Save only the JSON response",
                "Copy the assistant's JSON object into C436-work/HB-001/02-create/script-storyboard.json. Remove text outside the outer braces and ensure the root contains script_version='script-v1' and plan_source_fingerprint copied exactly from ready-restored-run.json.",
            ),
            (
                "Validate the JSON and inspect the selected concept",
                "Get-Content -Raw C436-work/HB-001/02-create/script-storyboard.json | ConvertFrom-Json | Select-Object run_id,plan_source_fingerprint,status,selected_concept_id,total_duration_seconds | Format-List",
            ),
            (
                "Generate a versioned caption hand-off from the exact storyboard",
                "PowerShell -ExecutionPolicy Bypass -File labs/assets/captions-from-storyboard.ps1 -StoryboardPath C436-work/HB-001/02-create/script-storyboard.json -OutputPath C436-work/HB-001/02-create/captions-script-v1.vtt",
            ),
            (
                "Review every claim and mark the human decision",
                "Create storyboard-approval.md with four headings: Approved concept, Evidence checked, Required revisions, Decision. Set Decision to APPROVED_FOR_ASSET_REQUESTS only after each factual statement maps to an allowed source ID and no scene uses a real person's likeness.",
            ),
            (
                "Record the approved script version",
                "Add script_version=script-v1 and approved_by=<YOUR_NAME> to storyboard-approval.md. Do not write credentials or personal account identifiers.",
            ),
            (
                "Run the fail-closed Lab 3 validator and retain the evidence",
                "PowerShell -ExecutionPolicy Bypass -File labs/assets/validate-lab-checkpoint.ps1 -Lab 3 2>&1 | Tee-Object C436-work/HB-001/02-create/lab-03-test-output.txt\nSet-Content C436-work/HB-001/02-create/LAB-CHECKPOINT-03.txt 'Lab 3 passed; script and caption hand-offs accepted.'",
            ),
        ],
        test=(
            "The validator must print LAB-03 PASS. It enforces run ID, script_ready "
            "status, exact Lab 2 fingerprint hand-off, human approval token, three "
            "concepts, required beat fields/source IDs, contiguous timing, and captions."
        ),
        checkpoint=(
            "Lab checkpoint 03 is stored in stage folder C436-work/HB-001/02-create. "
            "The complete rejoin block below restores the approved storyboard, binds it "
            "to the exact Lab 2 plan fingerprint, regenerates captions, restores the "
            "human approval, and runs the same fail-closed validator."
        ),
        rejoin_commands=(
            "Set-Location '<PATH_TO_C436_REPOSITORY>'\n"
            "$planPath='C436-work/HB-001/01-design/ready-restored-run.json'\n"
            "$createPath='C436-work/HB-001/02-create'\n"
            "$plan=Get-Content -Raw -LiteralPath $planPath | ConvertFrom-Json\n"
            "if($plan.status -ne 'plan_ready' -or $plan.next_stage -ne 'research_and_script'){throw 'Restore Lab checkpoint 02 first.'}\n"
            "New-Item -ItemType Directory -Force -Path $createPath | Out-Null\n"
            "Copy-Item -LiteralPath labs/assets/script-storyboard-approved.json -Destination \"$createPath/script-storyboard.json\" -Force\n"
            "$story=Get-Content -Raw -LiteralPath \"$createPath/script-storyboard.json\" | ConvertFrom-Json\n"
            "if($story.plan_source_fingerprint -ne $plan.source_fingerprint){throw 'Approved storyboard does not match the restored Lab 2 plan.'}\n"
            "$prompt=Get-Content -Raw -LiteralPath labs/assets/research-script-prompt-template.txt\n"
            "$prompt=$prompt.Replace('<RUN_ID>','HB-001').Replace('<PLAN_SOURCE_FINGERPRINT>',[string]$plan.source_fingerprint)\n"
            "$prompt | Set-Content -LiteralPath \"$createPath/research-script-prompt.txt\" -Encoding utf8\n"
            "PowerShell -ExecutionPolicy Bypass -File labs/assets/captions-from-storyboard.ps1 -StoryboardPath \"$createPath/script-storyboard.json\" -OutputPath \"$createPath/captions-script-v1.vtt\"\n"
            "Copy-Item -LiteralPath labs/assets/storyboard-approval-approved.md -Destination \"$createPath/storyboard-approval.md\" -Force\n"
            "PowerShell -ExecutionPolicy Bypass -File labs/assets/validate-lab-checkpoint.ps1 -Lab 3 -WorkRoot C436-work/HB-001"
        ),
        troubleshooting=[
            (
                "The assistant returns Markdown around the JSON.",
                "Copy only the content from the first opening brace to the final closing brace, then rerun ConvertFrom-Json.",
            ),
            (
                "The beats total more than 30 seconds.",
                "Ask for a repair that preserves the approved claim order and reduces narration; do not silently speed up the voice.",
            ),
            (
                "A claim has no source ID.",
                "Remove the claim or route it to open_questions. Do not approve it for asset generation.",
            ),
        ],
        challenge=(
            "Generate a second concept that uses the same evidence but a different "
            "angle family, then compare relevance, proof, feasibility, and estimated "
            "generation cost before choosing."
        ),
        reflection=(
            "Which part of the script required human judgment even after the schema "
            "and source checks passed?"
        ),
    ),
    dict(
        num=4,
        topic=2,
        title="Build the Visual, Voiceover, and Music Asset Request Pack",
        objective="LO2: create structured media-generation requests with continuity, provenance, rights, and fallback controls",
        duration=80,
        goal="Transform the approved storyboard into generator-ready requests without making paid or external actions mandatory.",
        desc=(
            "You will import a deterministic asset-request workflow, generate a "
            "continuity bible and one request per storyboard beat, prepare narration "
            "and music briefs, and review the resulting asset manifest. Optional "
            "live generation is kept outside the required path; supplied placeholder "
            "media lets everyone continue."
        ),
        build=(
            "A continuity-bible.json, asset-requests.json, narration.txt, "
            "music-brief.md, and asset-manifest.csv with approved placeholders or "
            "authorised generated files."
        ),
        services="n8n, optional approved video/voice tools, supplied placeholder media",
        prerequisites=[
            "Complete Lab 3 or restore its exact script-storyboard.json, captions-script-v1.vtt, and approval note.",
            "Confirm labs/assets/asset-request-agent-workflow.json and asset-manifest-template.csv are present.",
            "If using a live service, store its secret in managed credentials and confirm usage rights and budget with the trainer.",
        ],
        workflow=[
            "Import the request agent",
            "Generate continuity and requests",
            "Prepare voice and music briefs",
            "Register files and provenance",
            "Save Lab checkpoint 04 in stage folder 02-create",
        ],
        steps=[
            (
                "Import the asset-request workflow into n8n",
                "In n8n, select Workflows > Create Workflow, open the top-right three-dot menu, choose Import from File, and select labs/assets/asset-request-agent-workflow.json. Rename it C436-HB-001-Asset-Request-Agent and keep it inactive.",
            ),
            (
                "Inspect the workflow controls",
                "Confirm the path loads the exact storyboard, validates run_id HB-001 and script_version script-v1, creates one bounded request per beat, caps attempts at 2, and makes zero external actions.",
            ),
            (
                "Paste the exact Lab 3 storyboard into the workflow",
                "Open Load Exact Approved Storyboard. Copy the entire contents of C436-work/HB-001/02-create/script-storyboard.json between the storyboardText backticks. Run from Manual Trigger and verify source_fingerprint is non-empty.",
            ),
            (
                "Run the workflow and copy the output",
                "Select Test Workflow. Open Emit Asset Pack and copy the complete JSON output to C436-work/HB-001/02-create/asset-requests.json.",
            ),
            (
                "Extract the continuity bible",
                "$pack = Get-Content -Raw C436-work/HB-001/02-create/asset-requests.json | ConvertFrom-Json\n$pack.continuity_bible | ConvertTo-Json -Depth 8 | Set-Content C436-work/HB-001/02-create/continuity-bible.json",
            ),
            (
                "Create the narration file from approved beat text",
                "$story = Get-Content -Raw C436-work/HB-001/02-create/script-storyboard.json | ConvertFrom-Json\n($story.beats.narration -join ' ') | Set-Content C436-work/HB-001/02-create/narration.txt",
            ),
            (
                "Prepare the music brief",
                "Copy labs/assets/music-brief-template.md C436-work/HB-001/02-create/music-brief.md. Set mood to warm and practical, duration 30 seconds, dialogue priority high, and permitted source to the supplied course-use placeholder or an approved library. Resolve rights_status to approved_for_course_use before acceptance.",
            ),
            (
                "Create the asset manifest and register every requested scene",
                "Copy labs/assets/asset-manifest-template.csv C436-work/HB-001/02-create/asset-manifest.csv. Add exactly S01-S05, A01 narration, and A02 music. Every row must be accepted with approved_for_course_use rights. For rejoin, copy asset-manifest-approved.csv.",
            ),
            (
                "Use supplied placeholder media for the required path",
                "New-Item -ItemType Directory -Force C436-work/HB-001/02-create/media | Out-Null\nCopy-Item -Recurse -Force labs/assets/placeholder-media/* C436-work/HB-001/02-create/media/",
            ),
            (
                "Optionally replace one placeholder through an approved service",
                "Before a live call, confirm the provider, prompt, estimated cost, rights basis, and credential are approved. Generate only one bounded candidate, save it in media, and update its manifest row. Never paste a secret into the prompt or file.",
            ),
            (
                "Review the complete pack and record the decision",
                "Create asset-pack-approval.md with checks for storyboard coverage, continuity, narration, music rights, provenance, cost, and fallback. Set Decision to APPROVED_FOR_ASSEMBLY, manifest_version=asset-manifest-v1, and approved_by=<YOUR_NAME> only when every required asset is accepted.",
            ),
            (
                "Run the fail-closed Lab 4 validator and retain the evidence",
                "PowerShell -ExecutionPolicy Bypass -File labs/assets/validate-lab-checkpoint.ps1 -Lab 4 2>&1 | Tee-Object C436-work/HB-001/02-create/lab-04-test-output.txt\nSet-Content C436-work/HB-001/02-create/LAB-CHECKPOINT-04.txt 'Lab 4 passed; asset pack accepted for assembly.'",
            ),
        ],
        test=(
            "The validator must print LAB-04 PASS. It requires the exact S01-S05, "
            "A01, and A02 set, correct types, accepted approved-rights status, files, "
            "unique IDs, and the human APPROVED_FOR_ASSEMBLY token."
        ),
        checkpoint=(
            "Lab checkpoint 04 is the complete 02-create stage folder. The rejoin block "
            "below restores every required accepted asset, narration, approved music "
            "brief, and human assembly decision before validating the checkpoint."
        ),
        rejoin_commands=(
            "Set-Location '<PATH_TO_C436_REPOSITORY>'\n"
            "$createPath='C436-work/HB-001/02-create'\n"
            "if(-not (Test-Path -LiteralPath \"$createPath/script-storyboard.json\")){throw 'Restore Lab checkpoint 03 first.'}\n"
            "New-Item -ItemType Directory -Force -Path \"$createPath/media\" | Out-Null\n"
            "Copy-Item -LiteralPath labs/assets/asset-manifest-approved.csv -Destination \"$createPath/asset-manifest.csv\" -Force\n"
            "Copy-Item -Path labs/assets/placeholder-media/* -Destination \"$createPath/media/\" -Force\n"
            "Copy-Item -LiteralPath labs/assets/asset-pack-approval-approved.md -Destination \"$createPath/asset-pack-approval.md\" -Force\n"
            "Copy-Item -LiteralPath labs/assets/music-brief-approved.md -Destination \"$createPath/music-brief.md\" -Force\n"
            "$story=Get-Content -Raw -LiteralPath \"$createPath/script-storyboard.json\" | ConvertFrom-Json\n"
            "($story.beats.narration -join ' ') | Set-Content -LiteralPath \"$createPath/narration.txt\" -Encoding utf8\n"
            "PowerShell -ExecutionPolicy Bypass -File labs/assets/validate-lab-checkpoint.ps1 -Lab 4 -WorkRoot C436-work/HB-001"
        ),
        troubleshooting=[
            (
                "The number of asset requests differs from the number of beats.",
                "Check that every beat has a visual_request object and rerun from the workflow trigger without pinned output.",
            ),
            (
                "A generated file has no usable provenance or rights information.",
                "Mark it rejected, restore the placeholder, and route the rights question to the owner.",
            ),
            (
                "Narration duration is likely too long.",
                "Read it aloud at a natural pace, shorten the approved script, update script_version, and regenerate only the narration request.",
            ),
        ],
        challenge=(
            "Add estimated_cost_sgd per request and a deterministic guard that "
            "compares the sum with the required cost_budget_sgd from the exact Lab 1 contract."
        ),
        reflection=(
            "Why is an accepted placeholder with complete provenance preferable to "
            "an impressive generated clip with unresolved rights?"
        ),
    ),
]
