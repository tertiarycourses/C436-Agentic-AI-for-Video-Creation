"""Topic 1 labs: agent foundations and end-to-end workflow design."""

DOMAIN1 = [
    dict(
        num=1,
        topic=1,
        title="Design the Video Agent Production Contract and Autonomy Matrix",
        objective="LO1: explain agentic AI and design a controlled video workflow with explicit human decision points",
        duration=45,
        goal="Create the authoritative contract that every later C436 lab will consume.",
        desc=(
            "You will turn the synthetic Harbour Bean campaign brief into a "
            "structured production contract, classify each task by autonomy level, "
            "and mark the evidence, approval, retry, and stop rules for the workflow."
        ),
        build=(
            "A completed production-contract.json and autonomy-matrix.csv for run "
            "HB-001, saved in the connected project checkpoint."
        ),
        services="Text editor, supplied synthetic brief, JSON validator",
        prerequisites=[
            "Download or clone the C436 repository and open labs/assets.",
            "Confirm that harbour-bean-brand-brief.md and production-contract-template.json are present.",
            "Know the local path to the C436 repository; do not use real customer or account data.",
        ],
        workflow=[
            "Inspect the synthetic brief",
            "Define the production contract",
            "Classify task autonomy",
            "Validate the files",
            "Save Lab checkpoint 01 in stage folder 01-design",
        ],
        steps=[
            (
                "Set the repository root and fail fast if the course assets are absent",
                "Set-Location '<PATH_TO_C436_REPOSITORY>'\nif (-not (Test-Path -LiteralPath labs/assets/harbour-bean-brand-brief.md -PathType Leaf)) { throw 'Run this lab from the C436 repository root.' }",
            ),
            (
                "Create the connected project folders",
                "New-Item -ItemType Directory -Force -Path C436-work/HB-001/01-design,C436-work/HB-001/02-create,C436-work/HB-001/03-edit,C436-work/HB-001/04-release,C436-work/HB-001/05-learn | Out-Null",
            ),
            (
                "Read the synthetic brief and identify only approved facts",
                "Get-Content -LiteralPath labs/assets/harbour-bean-brand-brief.md",
            ),
            (
                "Copy the contract and autonomy templates into stage folder 01-design",
                "Copy-Item -LiteralPath labs/assets/production-contract-template.json -Destination C436-work/HB-001/01-design/production-contract.json\nCopy-Item -LiteralPath labs/assets/autonomy-matrix-template.csv -Destination C436-work/HB-001/01-design/autonomy-matrix.csv",
            ),
            (
                "Open production-contract.json and replace every text placeholder using only the supplied brief",
                "notepad C436-work/HB-001/01-design/production-contract.json",
            ),
            (
                "Set the required contract controls",
                "Set run_id to HB-001; retain contract_version contract-v1; duration_seconds 30; aspect_ratio 9:16; publishing_mode dry_run_private; max_generation_attempts_per_scene 2; cost_budget_sgd 25.0; finish_condition to release package approved or routed to named owner. Keep numbers unquoted.",
            ),
            (
                "Complete the autonomy matrix for all listed tasks",
                "Use deterministic for schema validation, file naming, media probing, arithmetic, and packaging; model_assisted for research clustering, script alternatives, and review suggestions; human_approved for claims, rights, final edit, and release; prohibited for secret exposure, unreviewed public posting, and unapproved likeness use.",
            ),
            (
                "Run the fail-closed Lab 1 validator and retain the evidence",
                "PowerShell -ExecutionPolicy Bypass -File labs/assets/validate-lab-checkpoint.ps1 -Lab 1 2>&1 | Tee-Object C436-work/HB-001/01-design/lab-01-test-output.txt",
            ),
            (
                "Check that no template placeholder remains",
                "Select-String -Path C436-work/HB-001/01-design/production-contract.json,C436-work/HB-001/01-design/autonomy-matrix.csv -Pattern '<COMPLETE_ME>'",
            ),
            (
                "Write the Lab checkpoint 01 marker",
                "Set-Content -LiteralPath C436-work/HB-001/01-design/LAB-CHECKPOINT-01.txt -Value 'Lab 1 passed; stage folder 01-design is ready.'",
            ),
        ],
        test=(
            "The validator must print LAB-01 PASS. It enforces JSON types, positive "
            "budget, all nine autonomy rows, prohibition of public publishing, "
            "and prohibition of secret exposure. The placeholder search must return "
            "no matches."
        ),
        checkpoint=(
            "Lab checkpoint 01 is stored in stage folder C436-work/HB-001/01-design. If you fall behind, copy "
            "labs/assets/production-contract-approved.json and "
            "labs/assets/autonomy-matrix-approved.csv into this folder, then rerun "
            "the tests before continuing."
        ),
        troubleshooting=[
            (
                "ConvertFrom-Json reports an invalid object.",
                "Open the file, check the line named in the error, remove trailing commas, and ensure every key and text value is in double quotes.",
            ),
            (
                "The brief does not contain a value requested by the template.",
                "Write null or add it to open_questions; do not invent a fact.",
            ),
            (
                "A task seems both model-assisted and human-approved.",
                "Classify the model's draft as model_assisted and the consequential decision or action as human_approved.",
            ),
        ],
        challenge=(
            "Add a budget warning threshold at 80% of the required cost_budget_sgd "
            "and prove the rule returns a named owner rather than another generation attempt."
        ),
        reflection=(
            "Which video-production decision was most tempting to automate fully, "
            "and what evidence convinced you to keep a human approval point?"
        ),
    ),
    dict(
        num=2,
        topic=1,
        title="Build and Run the Bounded Video Planning Agent in n8n",
        objective="LO1: use structured prompts and tool boundaries to implement a resumable planning workflow",
        duration=50,
        goal="Import, inspect, and run a planning workflow that stops on missing evidence and emits a valid production plan.",
        desc=(
            "You will import a supplied n8n workflow, trace its trigger, validation, "
            "planning, guardrail, and output stages, then run one ready case and one "
            "blocked case. The agent uses deterministic mock planning so everyone "
            "can verify the control pattern without a paid API."
        ),
        build=(
            "An n8n workflow named C436-HB-001-Planning-Agent plus exported ready "
            "and blocked execution evidence."
        ),
        services="n8n, supplied workflow JSON, production contract",
        prerequisites=[
            "Complete Lab 1 or restore Lab checkpoint 01 in stage folder 01-design.",
            "Access an n8n Cloud workspace or trainer-provided n8n instance.",
            "Keep live credentials disconnected; this lab uses deterministic Code nodes.",
        ],
        workflow=[
            "Import the workflow",
            "Inspect contracts and gates",
            "Run the ready job",
            "Force a blocked job",
            "Export evidence",
        ],
        steps=[
            (
                "Open n8n and import the supplied workflow",
                "In n8n, select Workflows > Create Workflow. Open the top-right three-dot menu, select Import from File, and choose labs/assets/video-planning-agent-workflow.json.",
            ),
            (
                "Rename and save the imported workflow",
                "Set the workflow name to C436-HB-001-Planning-Agent and select Save. Keep the workflow inactive.",
            ),
            (
                "Inspect the five-node control path",
                "Confirm the main path is Manual Trigger > Load Exact Production Contract > Validate Contract and Version > Plan or Block > Emit Run State. Confirm a blocked result calls no external tool.",
            ),
            (
                "Paste the exact Lab 1 artifact into the input node",
                "Open Load Exact Production Contract. Copy the entire contents of C436-work/HB-001/01-design/production-contract.json between the contractText backticks. Do not retype or use the supplied approved fixture. Run once and verify contract_version=contract-v1 plus a non-empty source_fingerprint.",
            ),
            (
                "Execute the complete ready workflow",
                "Select Test Workflow. After execution, select Emit Run State and open the JSON output.",
            ),
            (
                "Verify the ready-state schema",
                "The output must contain run_id=HB-001, status=plan_ready, current_stage=planning, next_stage=research_and_script, a non-empty actions array, iteration=1, and publish_allowed=false.",
            ),
            (
                "Create a controlled missing-evidence case",
                "Copy the complete Emit Run State output to C436-work/HB-001/01-design/ready-run.json. Then open Load Exact Production Contract, set approved_facts to an empty array inside the pasted JSON, save, and select Test Workflow again.",
            ),
            (
                "Verify the workflow stops safely",
                "Open Emit Run State. Confirm status=blocked, next_stage=human_clarification, publish_allowed=false, and blockers includes missing_approved_facts. Save the complete output as C436-work/HB-001/01-design/blocked-run.json.",
            ),
            (
                "Restore the ready case and export the workflow",
                "Restore the exact approved_facts array from the Lab 1 file, rerun from Manual Trigger, and save the complete output as C436-work/HB-001/01-design/ready-restored-run.json. Download the workflow as planning-agent-reviewed.json.",
            ),
            (
                "Save a short execution evidence note",
                "PowerShell -ExecutionPolicy Bypass -File labs/assets/validate-lab-checkpoint.ps1 -Lab 2 2>&1 | Tee-Object C436-work/HB-001/01-design/lab-02-test-output.txt\nSet-Content C436-work/HB-001/01-design/LAB-CHECKPOINT-02.txt 'Lab 2 passed; planning evidence retained in stage folder 01-design.'",
            ),
        ],
        test=(
            "The Lab 2 validator must print LAB-02 PASS after reading ready-run.json, "
            "blocked-run.json, and ready-restored-run.json. Both ready results must "
            "remain non-publishing; the controlled missing-evidence result must fail closed."
        ),
        checkpoint=(
            "Lab checkpoint 02 adds three execution JSON files, test evidence, and "
            "planning-agent-reviewed.json to stage folder C436-work/HB-001/01-design. The template remains "
            "available at labs/assets/video-planning-agent-workflow.json."
        ),
        troubleshooting=[
            (
                "n8n rejects the imported JSON.",
                "Confirm that you selected the workflow file rather than a course data file, then ask the trainer for the current n8n import fallback.",
            ),
            (
                "The path after Validate Contract does not reach Emit Run State.",
                "Open the validation output and confirm required fields use the exact supplied names and approved_facts is an array.",
            ),
            (
                "The blocked run still shows plan_ready.",
                "Execute from Manual Trigger after saving the edited contract node; running only the final node may reuse pinned data.",
            ),
        ],
        challenge=(
            "Add a deterministic budget check that returns blocker "
            "generation_budget_missing when cost_budget_sgd is absent."
        ),
        reflection=(
            "Why is the blocked result a successful agent behavior rather than a "
            "workflow failure?"
        ),
    ),
]
