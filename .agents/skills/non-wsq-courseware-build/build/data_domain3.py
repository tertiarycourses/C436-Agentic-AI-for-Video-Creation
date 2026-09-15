"""Topic 3 labs: multi-agent Kanban, YouTube release and scheduled publishing.

Lab bodies live in labs/lab-NN-<slug>/. These entries are the single source for
the deck, Lesson Plan and Learner Guide and must stay aligned with them.
"""

DOMAIN3 = [
    dict(
        num=6,
        topic=3,
        title="Build the Multi-Agent Video Workflow",
        objective="LO3: define four bounded specialist roles and prove that upload stays blocked until every gate passes",
        duration=70,
        goal="Give each stage one owner, one deliverable and one measurable completion rule.",
        desc=(
            "You will define and simulate four isolated Hermes roles for research, "
            "video creation, independent review and approved YouTube upload. Each "
            "role receives a bounded tool list and a named deliverable, the reviewer "
            "runs in an independent context without approval authority, and the "
            "uploader stays blocked until all parent evidence and the current "
            "approval hash pass."
        ),
        build=(
            "A multi-agent-plan.json with four verified handoff records."
        ),
        services="Hermes delegation, agent contracts, handoff schema",
        prerequisites=[
            "Complete Lab 5 so an approved branded master and its hash exist.",
            "Open labs/lab-06-build-multi-agent-video-workflow/ as the current Hermes project.",
            "Review data/agent-contracts.yaml and data/handoff-schema.json.",
        ],
        workflow=[
            "Define the role contracts",
            "Package the context",
            "Delegate research",
            "Delegate production",
            "Request review",
            "Gate the uploader",
        ],
        steps=[
            (
                "Define each role's goal, allowed tools, named deliverable and completion rule",
                "",
            ),
            (
                "Package the delegation context with the exact goal, paths, inputs, constraints and acceptance tests",
                "",
            ),
            (
                "Delegate research and require retrievable URLs, bounded excerpts and explicit limitations",
                "",
            ),
            (
                "Delegate production with immutable research input and require the custom brand-video skill",
                "",
            ),
            (
                "Request review in an independent context and withhold approval authority from the reviewer",
                "",
            ),
            (
                "Gate the uploader on every parent deliverable and the current approval hash",
                "",
            ),
            (
                "Run the verifier and retain the PASS output with the four handoff records",
                "python3 verify.py",
            ),
        ],
        test=(
            "verify.py must print PASS Lab 06. All roles have bounded tools and "
            "outputs, the reviewer is independent, and upload is blocked until all "
            "parent evidence and the current approval hash pass."
        ),
        checkpoint=(
            "The four validated role contracts are the agents the Kanban board "
            "dispatches in the next lab."
        ),
        troubleshooting=[
            (
                "Two agents rewrite the same artifact.",
                "Give each deliverable one owning role and one immutable version identifier.",
            ),
            (
                "A child agent returns something plausible that does not fit the pipeline.",
                "Add the exact paths, inputs and acceptance tests to the delegation context and redispatch.",
            ),
            (
                "The reviewer clears its own findings.",
                "Run the reviewer in an independent context; a reviewer with approval authority provides no independent check.",
            ),
        ],
        challenge=(
            "Change the master after approval and prove the uploader blocks on the "
            "hash mismatch rather than uploading the newer file."
        ),
        reflection=(
            "Where did splitting a stage into its own agent genuinely improve control, "
            "and where did it only add a handoff?"
        ),
    ),
    dict(
        num=7,
        topic=3,
        title="Orchestrate Kanban Review and YouTube Upload",
        objective="LO3: run a durable dependency chain and bind a named approval to the exact release hash",
        duration=60,
        goal="Make the release decision durable, independent and reconcilable.",
        desc=(
            "You will create a Hermes Kanban dependency chain, assign profiles, link "
            "every parent, require review, approve the exact package hash and then "
            "prepare or execute a private YouTube upload under explicit human "
            "authorisation with an idempotency key."
        ),
        build=(
            "A kanban-export.json, approval-ledger.json and a private-upload receipt "
            "or dry-run preview."
        ),
        services="Hermes Kanban, approval ledger, YouTube Data API videos.insert",
        prerequisites=[
            "Complete Lab 6 so the four role contracts are validated.",
            "Open labs/lab-07-orchestrate-kanban-review-and-youtube-upload/ as the current Hermes project.",
            "A Google account with a YouTube channel; uploads remain private throughout.",
        ],
        workflow=[
            "Create the board tasks",
            "Assign the profiles",
            "Link the dependencies",
            "Request review",
            "Approve the exact hash",
            "Upload private",
        ],
        steps=[
            (
                "Create the board tasks and assign a profile to each one",
                "",
            ),
            (
                "Link every dependency so no task can start before its parents are complete",
                "",
            ),
            (
                "Run the dispatcher and confirm the board survives a restart and a deliberate pause",
                "",
            ),
            (
                "Request review and collect timecoded findings from the independent reviewer",
                "",
            ),
            (
                "Freeze the release package, compute its hash and approve that exact hash by name",
                "",
            ),
            (
                "Recheck the current master hash immediately before upload and block on any mismatch",
                "",
            ),
            (
                "Create the idempotency key, upload with privacy set to private, then run the verifier",
                "python3 verify.py",
            ),
        ],
        test=(
            "verify.py must print PASS Lab 07. The Kanban graph has no missing "
            "dependency, review is required, the request points to the approved "
            "master, privacy is private, and no credential is present in any artifact."
        ),
        checkpoint=(
            "approval-ledger.json and the private upload receipt are the release "
            "evidence the scheduled-publishing lab operates against."
        ),
        troubleshooting=[
            (
                "Review or upload is blocked.",
                "Inspect the exact dependency status and compare the approved payload hash with the current master hash.",
            ),
            (
                "A retry after a timeout produces a second video.",
                "Reconcile the prior idempotency key and its committed video identifier before retrying.",
            ),
            (
                "A task fails repeatedly.",
                "Cap the attempts, classify the failure and block it for human intervention rather than retrying indefinitely.",
            ),
        ],
        challenge=(
            "Remove one dependency link and prove the board lets a task start early, "
            "then restore it and show the join waiting on verified artifacts."
        ),
        reflection=(
            "Why does approving a hash rather than a filename close a gap that "
            "filename-based approval leaves open?"
        ),
    ),
    dict(
        num=8,
        topic=3,
        title="Schedule Controlled Video Publishing with Hermes Cron",
        objective="LO3: create a paused, self-contained scheduled job and enable a cadence only after evidence review",
        duration=50,
        goal="Make scheduled release safe by default and observable before it runs unattended.",
        desc=(
            "You will write a self-contained cron prompt containing every required "
            "path, gate and stop rule, attach the custom video skill explicitly, "
            "create the schedule paused with an explicit timezone, trigger a dry run, "
            "inspect the next run time and approve enablement only after reviewing "
            "the evidence."
        ),
        build="A cron-preview.json with an operations-ledger.csv.",
        services="Hermes cron, attached skills, operations ledger",
        prerequisites=[
            "Complete Lab 7 so an approved release package and its ledger exist.",
            "Open labs/lab-08-schedule-controlled-video-publishing/ as the current Hermes project.",
            "Review starter/release-job-prompt.md and starter/cron-commands.md.",
        ],
        workflow=[
            "Write the self-contained job",
            "Attach the video skill",
            "Create the paused cron",
            "Trigger the dry run",
            "Inspect the next run",
            "Approve enablement",
        ],
        steps=[
            (
                "Write the job prompt so it is fully self-contained, assuming no session context",
                "",
            ),
            (
                "Include every required path, gate and stop rule directly in the job prompt",
                "",
            ),
            (
                "Attach the custom video skill and any other required skills explicitly",
                "",
            ),
            (
                "Create the schedule with an explicit timezone and leave the job paused",
                "",
            ),
            (
                "Trigger a dry run and confirm it cannot publish an unapproved or duplicate video",
                "",
            ),
            (
                "Inspect the output and the next scheduled run time, then record the run in the ledger",
                "",
            ),
            (
                "Approve enablement only after the evidence review, then run the verifier",
                "python3 verify.py",
            ),
        ],
        test=(
            "verify.py must print PASS Lab 08. The schedule and timezone are "
            "explicit, the prompt is self-contained, the custom skill is attached, "
            "the job begins paused, and the dry run cannot publish an unapproved or "
            "duplicate video."
        ),
        checkpoint=(
            "cron-preview.json and operations-ledger.csv complete the handover "
            "package for the whole C436 pipeline."
        ),
        troubleshooting=[
            (
                "A job that passed interactively behaves differently on its first scheduled run.",
                "Move every implicit path, gate and stop rule into the job prompt; a cron job inherits no session context.",
            ),
            (
                "The attached skill is not found at run time.",
                "Attach the skill explicitly to the job rather than relying on discovery from the creating session.",
            ),
            (
                "The dry run attempts a real publish.",
                "Keep the job paused and confirm the release gate requires a separate approval for public visibility.",
            ),
        ],
        challenge=(
            "Remove one path from the job prompt and show the scheduled run failing in "
            "a way the interactive run did not, then restore it."
        ),
        reflection=(
            "What is the worst outcome a defect in your schedule could now cause, and "
            "which control bounds it to that?"
        ),
    ),
]
