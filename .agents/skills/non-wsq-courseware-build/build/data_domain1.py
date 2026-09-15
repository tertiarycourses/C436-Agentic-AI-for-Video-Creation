"""Topic 1 labs: Hermes runtime, MiniMax M3 and video prompt engineering.

Lab bodies live in labs/lab-NN-<slug>/ (README.md, AI-PROMPTS.md, data/,
starter/, solution/, evidence/, verify.py). These entries are the single source
for the deck, Lesson Plan and Learner Guide and must stay aligned with them.
"""

DOMAIN1 = [
    dict(
        num=1,
        topic=1,
        title="Set Up Hermes Desktop and Connect MiniMax M3",
        objective="LO1: configure the Hermes runtime and prove a tool-capable MiniMax M3 handshake without exposing a credential",
        duration=50,
        goal="Establish the verified runtime boundary that every later C436 lab depends on.",
        desc=(
            "You will install Hermes Desktop from the official source, configure the "
            "MiniMax provider for MiniMax-M3, run the diagnostic command, compare the "
            "desktop and CLI state, and record the live trial terms you actually see. "
            "Every piece of published evidence carries placeholders instead of secrets."
        ),
        build=(
            "A setup-evidence.json recording the official source, version and "
            "diagnostic status, plus a redacted diagnostic screenshot."
        ),
        services="Hermes Desktop, Hermes CLI, MiniMax M3, credential storage",
        prerequisites=[
            "A laptop with administrator rights to install desktop software.",
            "A MiniMax account able to create an API key.",
            "Open labs/lab-01-setup-hermes-and-connect-minimax-m3/ as the current Hermes project.",
        ],
        workflow=[
            "Download the official installer",
            "Complete Hermes setup",
            "Configure MiniMax-M3",
            "Run hermes doctor",
            "Verify the model response",
            "Redact the evidence",
        ],
        steps=[
            (
                "Download the installer from the official Hermes desktop page and confirm the platform build",
                "",
            ),
            (
                "Complete setup, then run the diagnostic and read every reported dependency",
                "hermes doctor",
            ),
            (
                "Create the MiniMax API key and store it in credential storage, referenced by name",
                "",
            ),
            (
                "Configure provider minimax with model MiniMax-M3, then verify the returned model identifier",
                "",
            ),
            (
                "Compare the desktop profile and the CLI session for provider, model and skill root",
                "",
            ),
            (
                "Open the live trial offer, record the observed terms with today's date, and nominate a fallback model",
                "",
            ),
            (
                "Run the lab verifier and retain the PASS output with redacted evidence",
                "python3 verify.py",
            ),
        ],
        test=(
            "verify.py must print PASS Lab 01. Hermes launches, the configured "
            "provider is minimax, the model is MiniMax-M3, hermes doctor reports no "
            "blocking failure, and the published evidence contains placeholders only."
        ),
        checkpoint=(
            "The verified runtime boundary is recorded in setup-evidence.json. Every "
            "later lab assumes this provider, model and skill root."
        ),
        troubleshooting=[
            (
                "Hermes reports a different model than the one configured.",
                "Start a new session after selecting MiniMax-M3; an existing session can retain its original model.",
            ),
            (
                "hermes doctor reports a failed dependency.",
                "Repair the dependency before continuing; a failed diagnostic is a reason to stop, not a warning to pass.",
            ),
            (
                "The live trial terms differ from the course note.",
                "Record the current live account terms with the date and use the fallback path; the offer is time-sensitive.",
            ),
        ],
        challenge=(
            "Write the runtime boundary as a single JSON object and prove the desktop "
            "and CLI both report the same values for every field in it."
        ),
        reflection=(
            "Which runtime fact, if it silently changed between sessions, would be "
            "hardest to diagnose from the model's behaviour alone?"
        ),
    ),
    dict(
        num=2,
        topic=1,
        title="Prompt Hermes to Create a Simple Video",
        objective="LO1: convert a bounded brief into a validated shot plan and a deterministically rendered preview",
        duration=50,
        goal="Produce a first end-to-end video whose plan and output are both machine-checked.",
        desc=(
            "You will use a copy-ready Hermes prompt to turn a supplied 15-second "
            "brief into a strict-JSON shot plan, validate that the plan totals the "
            "target duration with no gaps or overlaps, run the deterministic preview "
            "renderer and probe the resulting MP4."
        ),
        build="A simple-video.mp4 with its shot-plan.json and ffprobe.json evidence.",
        services="Hermes Desktop, MiniMax M3, Python preview renderer, FFprobe",
        prerequisites=[
            "Complete Lab 1 so the provider and model are verified.",
            "Open labs/lab-02-prompt-hermes-to-create-a-simple-video/ as the current Hermes project.",
            "Confirm data/video-brief.json and starter/render_preview.py are present.",
        ],
        workflow=[
            "Open the project folder",
            "Submit the bounded prompt",
            "Validate the shot plan",
            "Run the preview renderer",
            "Probe the MP4",
            "Record the evidence",
        ],
        steps=[
            (
                "Open the lab folder as the current project and ask Hermes to inspect the local files before planning",
                "",
            ),
            (
                "Read AI-PROMPTS.md and replace only the named placeholders with the supplied synthetic values",
                "",
            ),
            (
                "Submit the bounded prompt and require strict JSON for the shot plan",
                "",
            ),
            (
                "Validate that the plan is valid JSON, totals 15 seconds, and uses only supplied assets",
                "",
            ),
            (
                "Run the deterministic preview renderer, requiring a preview before any paid or network side effect",
                "python3 starter/render_preview.py",
            ),
            (
                "Probe the rendered MP4 and compare dimensions, codec and duration against the contract",
                "ffprobe -v error -show_streams -show_format simple-video.mp4",
            ),
            (
                "Run the lab verifier and retain the PASS output",
                "python3 verify.py",
            ),
        ],
        test=(
            "verify.py must print PASS Lab 02. The shot plan is valid JSON, totals 15 "
            "seconds, uses only supplied assets, and the generated MP4 passes the "
            "dimensions, codec and duration checks."
        ),
        checkpoint=(
            "shot-plan.json and ffprobe.json establish the plan-then-probe pattern "
            "reused by every later production lab."
        ),
        troubleshooting=[
            (
                "The shot durations do not total the target.",
                "Fix the plan before rendering; a duration mismatch is a schema failure, not a rendering problem.",
            ),
            (
                "The renderer cannot find an asset.",
                "Check that the plan references only the supplied assets by their exact names.",
            ),
            (
                "A tool is missing.",
                "Use the documented deterministic fallback and record the limitation instead of inventing a successful call.",
            ),
        ],
        challenge=(
            "Introduce a deliberate one-second overlap between two shots and prove the "
            "validator rejects the plan before any render is attempted."
        ),
        reflection=(
            "Why is it cheaper to fail on the shot plan than on the rendered output, "
            "and what does that imply about where checks belong?"
        ),
    ),
    dict(
        num=3,
        topic=1,
        title="Engineer Video Prompts with FRAME-CUT",
        objective="LO1: apply the FRAME-CUT contract to make creative intent portable, comparable and checkable",
        duration=60,
        goal="Turn a vague creative request into field-complete, scorable shot prompts.",
        desc=(
            "You will diagnose a deliberately vague prompt, complete every FRAME field "
            "and every CUT field, generate strict shot JSON, score the result against a "
            "deterministic rubric and repair the single highest-severity defect."
        ),
        build="A prompt-pack.json with its prompt-score.csv rubric evidence.",
        services="Hermes Desktop, MiniMax M3, FRAME-CUT template, scoring rubric",
        prerequisites=[
            "Complete Lab 2 so the plan-and-probe pattern is familiar.",
            "Open labs/lab-03-engineer-video-prompts-with-frame-cut/ as the current Hermes project.",
            "Review starter/frame-cut-template.md and data/prompt-cases.csv.",
        ],
        workflow=[
            "Diagnose the vague prompt",
            "Complete the FRAME fields",
            "Complete the CUT fields",
            "Generate the shot JSON",
            "Score against the rubric",
            "Repair one defect",
        ],
        steps=[
            (
                "Read the supplied vague prompt and name each decision it leaves to the model",
                "",
            ),
            (
                "Complete the FRAME fields: format and finish, role and references, action, motion and environment",
                "",
            ),
            (
                "Complete the CUT fields: continuity tokens, unwanted elements and the technical output schema",
                "",
            ),
            (
                "Require one dominant subject action and one camera move per timed shot",
                "",
            ),
            (
                "Generate the shot JSON and confirm every FRAME-CUT field is present",
                "",
            ),
            (
                "Score the pack against the rubric and identify the highest-severity defect",
                "",
            ),
            (
                "Repair that one defect, rescore, then run the verifier and retain the PASS output",
                "python3 verify.py",
            ),
        ],
        test=(
            "verify.py must print PASS Lab 03. Every shot carries all FRAME-CUT "
            "fields, one dominant action, one camera move, explicit continuity and "
            "negative constraints, and a measurable output check."
        ),
        checkpoint=(
            "prompt-pack.json is the reusable prompt contract that the tool-routing "
            "and brand-skill labs consume."
        ),
        troubleshooting=[
            (
                "A shot contains two competing camera moves.",
                "Split it into two timed shots; one action-motion pair per shot keeps the result comparable.",
            ),
            (
                "Identity or palette drifts between shots.",
                "Reuse the continuity token and compare keyframes against the explicit invariant list.",
            ),
            (
                "The rubric score is high but the output still looks wrong.",
                "Check that the rubric measures the defect you observed; add the missing check rather than overriding the score.",
            ),
        ],
        challenge=(
            "Hand your prompt pack to another learner and have them generate from it "
            "without discussion; every difference reveals a field still left implicit."
        ),
        reflection=(
            "Which FRAME-CUT field did you most want to leave blank, and what would "
            "the model have invented in its place?"
        ),
    ),
]
