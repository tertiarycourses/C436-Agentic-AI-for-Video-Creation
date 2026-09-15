"""Single source of truth for Agentic AI for Video Creation (C436)."""

TITLE = "Agentic AI for Video Creation"
SHORT_TITLE = "Agentic AI for Video Creation"
COURSE_CODE = "C436"
COURSE_URL = "https://www.tertiarycourses.com.sg/agentic-ai-for-video-creation.html"
VERSION = "v2.0"
VERSION_DATE = "16 September 2026"
ORG = "Tertiary Infotech Academy Pte Ltd"
UEN = "UEN: 201200696W"
TRAINER = "Assigned Course Trainer"
DAYS = 2
DAY_MINUTES = 480
INSTRUCTIONAL_MINUTES = 450
MODE = "Instructor-led, hands-on practical labs"
DAILY_TIMING = (
    "9:30 am - 6:30 pm (1-hour lunch; two 15-minute tea breaks; "
    "7.5 instructional hours)"
)
DARK_THEME = False

LEARNING_OUTCOMES = [
    "LO1: Develop an editing strategy and work plan in Hermes Agent using MiniMax M3, structured video prompts and governed tool selection.",
    "LO2: Create and customise an evidence-backed video with Hermes skills, Remotion, Manim, Higgsfield-compatible requests and deterministic media checks.",
    "LO3: Orchestrate research, production, review and YouTube release agents through a durable Kanban board and controlled scheduled publishing.",
]

LO_TITLES = [
    "Plan the Video",
    "Build the Video",
    "Orchestrate and Release",
]


def _section(
    title,
    definition,
    why,
    how,
    example,
    use_when,
    avoid_when,
    quality,
    sources,
):
    return dict(
        title=title,
        definition=definition,
        why=why,
        how=how,
        example=example,
        use_when=use_when,
        avoid_when=avoid_when,
        quality=quality,
        sources=sources,
    )


TOPICS = [
    dict(
        num=1,
        code="01",
        title="Hermes Agent Setup, MiniMax M3 and Video Prompt Engineering",
        subtitle="Hermes Desktop runtime | MiniMax M3 provider contract | FRAME-CUT prompting | Structured shot plans",
        weighting="Day 1 morning and early afternoon | 3 labs",
        concepts=[
            ("Runtime boundary", "The installed Hermes surface, its profile, configuration path and skill root that every run depends on."),
            ("Provider contract", "The named provider, base URL, model identifier and credential reference used for reasoning."),
            ("FRAME-CUT", "A prompt contract covering Format, Role, Action, Motion, Environment plus Continuity, Unwanted and Technical output."),
            ("Shot plan", "Strict JSON of timed shots whose durations total the approved target with no gaps or overlaps."),
        ],
        sections=[
            _section(
                "Hermes Desktop Runtime and Shared CLI State",
                "Hermes Agent runs as a desktop application with a matching command-line surface. Both read the same profile, configuration path and skill directory, so a change made in one surface is visible to the other. Installation is completed from the official desktop page, after which a diagnostic command reports the health of each required dependency. The runtime boundary is the set of facts that define where the agent executes: platform, installer source, version, active profile, configuration path and skill root.",
                "An agent that cannot describe its own runtime cannot produce reproducible work. If the desktop and the terminal disagree about the active provider or skill directory, a lab that passes in one surface fails in the other for reasons that look like model behaviour. Recording the runtime boundary before any production work converts a class of confusing failures into a single observable check, and a failed dependency becomes a reason to stop rather than a problem to discover halfway through a render.",
                [
                    "Download the installer from the official Hermes desktop page and confirm the platform build.",
                    "Complete setup, then run the diagnostic command and read every reported dependency.",
                    "Open the desktop profile and note the configuration path and skill root.",
                    "Open the terminal and compare provider, model and skill directory against the desktop.",
                    "Stop and repair when a required diagnostic fails; do not continue into production work.",
                ],
                [
                    "hermes doctor reports all required dependencies healthy on a supported platform.",
                    "The desktop profile and the CLI session report the same provider, model and skill root.",
                    "setup-evidence.json records the official source, version and diagnostic status with no credential value.",
                ],
                [
                    "A new machine, a new learner account or a fresh profile is being prepared for production work.",
                    "Results differ between the desktop and the terminal and the cause is not yet known.",
                ],
                [
                    "A required diagnostic fails and the failure has not been repaired or recorded.",
                    "The installer came from an unofficial mirror or the platform build is unverified.",
                ],
                [
                    ("Failure signal", "The same prompt behaves differently in the desktop and the terminal."),
                    ("Repair move", "Name the active profile and compare provider, model and skill directory across both surfaces."),
                    ("Quality evidence", "profile-check.json shows matching settings and the diagnostic reports no blocking failure."),
                ],
                [
                    "https://hermes-agent.nousresearch.com/desktop",
                    "https://hermes-agent.nousresearch.com/docs/getting-started/installation",
                ],
            ),
            _section(
                "MiniMax M3 Provider, Trial Terms and Credential Isolation",
                "The provider contract names the service, base URL, model identifier and a reference to a stored credential. This course configures provider minimax with model MiniMax-M3 and verifies a tool-capable response before any production run. Trial availability, duration, quota and region terms are time-sensitive commercial terms rather than fixed course facts, so they are observed live at sign-up and recorded with a date. Credentials live in Hermes credential or configuration storage and are referenced by name; published evidence carries placeholders only.",
                "A model handshake that is assumed rather than verified is the most common cause of a lab that fails much later, at the point of an expensive call. Verifying the returned model identifier proves that the configured model is the model actually answering. Separating the credential from the evidence keeps the lab package publishable: a secret that never enters a prompt, file, screenshot or repository cannot be leaked by one of them. Recording trial terms with a date and a fallback model means a changed offer becomes a planned decision rather than a blocked class.",
                [
                    "Create the account and an API key, then store the key in credential storage and reference it by name.",
                    "Configure provider minimax with model MiniMax-M3 and confirm the returned model identifier.",
                    "Open the live offer, read the current terms and record what was seen, the date and the expiry.",
                    "Reserve a quota budget and nominate a fallback model before production work begins.",
                    "Scan the lab package and confirm zero live tokens before publishing any evidence.",
                ],
                [
                    "model-check.json records MiniMax-M3 and a successful tool-capable response without recording the key.",
                    "trial-checklist.md contains the observed terms, the date seen and the learner's fallback decision.",
                    "A secret scan over the lab package reports no live token pattern.",
                ],
                [
                    "A provider or model is being configured for the first time, or a key has been rotated.",
                    "Quota, billing or region terms materially affect how much generation the run can afford.",
                ],
                [
                    "The returned model identifier does not match the configured model.",
                    "A key would have to be pasted into a prompt, lab file, screenshot or repository to proceed.",
                ],
                [
                    ("Failure signal", "The session answers but reports a different model than the one configured."),
                    ("Repair move", "Start a new session after selecting the model; an existing session can retain its original model."),
                    ("Quality evidence", "budget-ledger.csv reconciles attempts, latency and cost against the approved ceiling."),
                ],
                [
                    "https://www.minimax.io/models/text/m3",
                    "https://hermes-agent.nousresearch.com/docs/user-guide/configuring-models",
                ],
            ),
            _section(
                "The FRAME-CUT Video Prompt Contract",
                "FRAME-CUT is the prompt contract used throughout this course. FRAME fixes Format and finish, Role and references, Action, Motion and Environment. CUT fixes Continuity tokens, Unwanted elements as explicit negative constraints, and the Technical output schema. A compliant prompt names one dominant subject action and one camera move per timed shot, states the palette and identity tokens that must persist, lists what must never appear, and requires strict JSON that can be validated before anything is generated.",
                "A vague creative request such as 'make it cinematic' leaves the model to invent the channel, duration, subject, camera language and acceptance rule, and every regeneration invents them differently. A field-complete contract makes shots comparable across attempts, makes drift observable against named invariants, and makes the output checkable by a validator rather than by opinion. Because the contract is validated before generation, a defective plan costs a schema error instead of a paid render.",
                [
                    "Choose the channel, then freeze duration, aspect ratio and delivery codec before any shot work.",
                    "Assign the role, attach the brief and register the source and asset identifiers that reasoning may use.",
                    "Write one dominant action and one camera move for each timed shot.",
                    "Lock continuity tokens and palette values, then list the must-avoid elements explicitly.",
                    "Require strict JSON and fail the plan on gaps, overlaps, unknown fields or a duration mismatch.",
                ],
                [
                    "A 15-second brief becomes a shot plan whose shot durations total exactly 15 seconds with no overlap.",
                    "Each shot carries one action-motion pair, a continuity token and an explicit must-avoid list.",
                    "prompt-contract.json passes the schema and duration checks before a renderer is called.",
                ],
                [
                    "A creative intent must survive several regenerations or be handed to another agent or tool.",
                    "The output will feed a deterministic renderer that requires named, typed fields.",
                ],
                [
                    "The request asks for imitation of a living artist or a named creator's identity.",
                    "The delivery format is still unsettled, so shot work would be rebuilt after the format changes.",
                ],
                [
                    ("Failure signal", "Shots look plausible individually but identity, palette or screen direction drifts between them."),
                    ("Repair move", "Reuse the continuity token and compare keyframes against the explicit invariant list."),
                    ("Quality evidence", "continuity-review.json records each deviation and the acceptance decision."),
                ],
                [
                    "https://hermes-agent.nousresearch.com/docs/user-guide/configuring-models",
                    "https://www.remotion.dev/docs",
                ],
            ),
            _section(
                "The Simple Video Agent Loop with Cost and Stop Rules",
                "The agent loop receives a brief, plans shots, calls one tool, inspects the returned artifact and then stops or escalates. Its controls are numeric: an estimated cost, a maximum number of attempts, a timeout and a recorded stop reason. A run ledger links the run identifier, the plan hash, each tool call and each result so that the run can be reconstructed after the fact. The default posture is one render attempt, one review pass and an explicit repair decision rather than open-ended retrying.",
                "Generation costs money and time, and an unbounded loop spends both without converging. Capping attempts converts a runaway loop into a decision that reaches a named person with the evidence already assembled. Recording the stop reason matters as much as recording success: a run that stopped because a dependency failed is a different operational fact from one that stopped because the budget ceiling was reached, and the two require different repairs.",
                [
                    "Estimate the number of calls and the cost before the first paid action.",
                    "Set the maximum attempts, the timeout and the budget ceiling as explicit numbers.",
                    "Run the loop: receive the brief, plan the shots, call one tool, inspect the result.",
                    "Stop at the cap and record the stop reason rather than attempting another generation.",
                    "Require a human decision before any additional paid generation is authorised.",
                ],
                [
                    "run-ledger.json contains the plan, the tool call, the result reference and the stop reason.",
                    "A 15-second preview is produced in one render attempt and probed before it is accepted.",
                    "A second paid attempt is not started automatically; it is escalated with the evidence attached.",
                ],
                [
                    "Work involves paid generation, external calls or any action with a real cost.",
                    "A run must be explainable later to a reviewer who was not present when it executed.",
                ],
                [
                    "Attempts, timeouts and budget have not been given numeric limits.",
                    "The loop can start another paid generation without a recorded human decision.",
                ],
                [
                    ("Failure signal", "The loop keeps regenerating without reaching a defined finish state."),
                    ("Repair move", "Cap attempts, add an explicit finish condition and route the remainder to a named owner."),
                    ("Quality evidence", "The ledger shows one committed result per run identifier and a recorded stop reason."),
                ],
                [
                    "https://hermes-agent.nousresearch.com/docs/guides/delegation-patterns",
                    "https://ffmpeg.org/ffprobe.html",
                ],
            ),
        ],
    ),
    dict(
        num=2,
        code="02",
        title="Video Tools, Hermes Skills and Custom Brand Production",
        subtitle="Tool versus skill | Remotion, Manim and FFmpeg | Brand tokens | Technical quality gate",
        weighting="Day 1 late afternoon and Day 2 morning | 2 labs",
        concepts=[
            ("Tool versus skill", "A tool performs precise integrated execution; a skill packages repeatable instructions plus scripts."),
            ("Skill anatomy", "A directory holding SKILL.md with frontmatter, a procedure, bundled scripts and verification commands."),
            ("Brand token", "A stored, editable value for logo, palette, typography or motion referenced by the video skill."),
            ("Quality gate", "A fail-closed technical check on container, streams, dimensions, frame rate, duration and captions."),
        ],
        sections=[
            _section(
                "Choosing Between a Tool and a Hermes Skill",
                "A tool is the right choice when a capability needs precise, integrated execution with its own authentication and error handling. A skill is the right choice when a procedure must be repeated reliably: it bundles instructions, scripts and templates in a directory containing SKILL.md, whose frontmatter declares the name, description and version. Hermes discovers skills by searching the catalogue, then loads the selected skill and only the resources it references, so context stays proportionate to the task.",
                "Wrapping everything as a skill produces brittle prose where an integration was needed; wrapping everything as a tool produces unrepeatable one-off calls where a documented procedure was needed. Deciding explicitly, and recording why, keeps the production stack legible to the next person. Progressive loading matters for the same reason: a skill that pulls its entire reference tree into context on every invocation crowds out the working material the task actually needs.",
                [
                    "Identify the capability and its authentication mode, then decide tool or skill and name an owner.",
                    "Create the skill directory and write frontmatter that describes the exact trigger.",
                    "Add the procedure, bundle the scripts and include deterministic verification commands.",
                    "Search the catalogue first, then view the selected skill and load only referenced resources.",
                    "Test invocation and confirm the expected artifacts are produced.",
                ],
                [
                    "decision-record.md states why each capability was implemented as a tool or as a skill.",
                    "SKILL.md and a test transcript together show correct activation from the intended trigger.",
                    "skill-usage.json records the selected skill and the resources that were loaded.",
                ],
                [
                    "A procedure will be repeated across runs, learners or courses and must behave the same way each time.",
                    "The capability needs bundled scripts and templates alongside its instructions.",
                ],
                [
                    "A single ad-hoc call would do and no repetition is expected.",
                    "The capability requires integrated authentication and precise error handling better served by a tool.",
                ],
                [
                    ("Failure signal", "A skill is not discovered when its trigger phrase is used."),
                    ("Repair move", "Check the YAML frontmatter, the directory name and the SKILL.md filename, then restart discovery."),
                    ("Quality evidence", "Repeated runs of the skill produce matching outputs from a clean start."),
                ],
                [
                    "https://hermes-agent.nousresearch.com/docs/guides/work-with-skills",
                    "https://hermes-agent.nousresearch.com/docs/user-guide/configuring-models",
                ],
            ),
            _section(
                "Routing Remotion, Manim, Higgsfield and FFmpeg",
                "Each media tool has a distinct contract. Remotion renders code-driven compositions where duration in frames divided by frames per second gives the duration in seconds. Manim renders programmatic explanatory scenes whose labels and values are bound to an approved evidence model. A Higgsfield-compatible request selects a model, attaches references and writes a motion prompt, and is prepared as a preview before any account or quota is consumed. FFmpeg performs deterministic assembly: normalise every source, build the timeline, mix audio and encode the master.",
                "Routing a task to a tool that cannot satisfy its contract is the most expensive category of error in a video pipeline, because the cost is usually discovered after generation. Deriving frames from duration rather than guessing prevents a composition that is silently the wrong length. Normalising sources before concatenation prevents the class of failures where clips join but the container reports inconsistent streams. Preparing a generation request as a preview keeps an unapproved asset or an exhausted quota from becoming a failed paid call.",
                [
                    "Classify the task, check the required modality and route it to a capable tool.",
                    "For Remotion, derive duration frames from the approved duration and validate width, height, fps and codec after render.",
                    "For Manim, bind labels and values to the approved evidence model and review the rendered frames.",
                    "For a Higgsfield request, build a request preview first and call the service only with approved assets and quota.",
                    "For FFmpeg, normalise every source before concatenation and probe the final container.",
                ],
                [
                    "tool-routing.csv links every task to a capable model or tool with a recorded fallback.",
                    "remotion-render.json and ffprobe.json agree with the composition contract.",
                    "ffprobe.json confirms H.264 video, AAC audio, the expected dimensions, frame rate and duration.",
                ],
                [
                    "A media task has a clear modality and an approved tool exists for it.",
                    "The output must be verified deterministically rather than accepted on appearance.",
                ],
                [
                    "The required assets are unapproved or the account quota has not been confirmed.",
                    "A deterministic renderer would produce the result more reliably than a generative call.",
                ],
                [
                    ("Failure signal", "Clips concatenate but the final container reports inconsistent streams or the wrong duration."),
                    ("Repair move", "Normalise every source to the same codec, dimensions and frame rate before rebuilding the timeline."),
                    ("Quality evidence", "The probe of the final master matches the approved delivery specification field for field."),
                ],
                [
                    "https://www.remotion.dev/docs",
                    "https://docs.manim.community/",
                    "https://ffmpeg.org/ffmpeg.html",
                ],
            ),
            _section(
                "Brand Tokens, Tone and the Custom Video Skill",
                "A brand token system stores the logo reference, palette values, font stack and motion rules as editable values that the video skill references rather than hard-codes. Tone and style controls describe the audience, the voice, the pacing in words per minute and an explicit list of stylistic exclusions. The custom brand-video skill combines these: it bundles scripts and templates, declares its inputs and outputs, and ships an acceptance test so that repeated runs can be compared rather than merely rerun.",
                "Brand rules written into prose drift as soon as two people apply them. Stored as tokens and referenced from a skill, they become checkable: a frame either uses the approved palette value or it does not. Describing tone through attributes and exclusions, rather than by naming a living artist to imitate, keeps the output original and defensible. An acceptance test converts 'the skill works' into a repeatable comparison between a clean run and the expected artifacts.",
                [
                    "Extract the identity, then set the palette, typography and motion rules as stored tokens.",
                    "Define the audience, voice and pacing, and write the style exclusions explicitly.",
                    "Write the skill, bundle its scripts and bind its templates using relative or Hermes template paths.",
                    "Render the video through the skill and review the frame samples against the checklist.",
                    "Run the acceptance test from a clean start and version the resulting evidence.",
                ],
                [
                    "brand-profile.yaml holds editable tokens and the frame samples pass the brand checklist.",
                    "The custom skill is discoverable, produces an MP4 and passes the technical probe.",
                    "A repeat run from a clean state produces matching outputs and the same evidence artifacts.",
                ],
                [
                    "The same brand treatment must be applied across many videos or by several people.",
                    "Brand compliance needs to be demonstrated rather than asserted.",
                ],
                [
                    "The style brief asks for imitation of a living artist or a specific creator's identity.",
                    "Brand values are still changing, so tokens would be rewritten immediately after use.",
                ],
                [
                    ("Failure signal", "Two runs of the same skill produce visibly different brand treatment."),
                    ("Repair move", "Move the varying value into a stored token and reference it from the skill."),
                    ("Quality evidence", "brand-review.json records the passed checks against the applicable brand tokens."),
                ],
                [
                    "https://hermes-agent.nousresearch.com/docs/guides/work-with-skills",
                    "https://www.remotion.dev/docs",
                ],
            ),
            _section(
                "The Technical Quality Gate, Provenance and Repair",
                "The quality gate probes the container, inspects representative frames, checks that captions are readable and then either passes or fails the master. It fails closed: a missing stream, an out-of-bounds dimension or an unreadable caption blocks the master rather than producing a warning. Provenance runs alongside it — every asset is registered with its source, licence and a SHA-256 hash, so approval binds to an immutable version. A finding opens a repair, the repair renders a new version, and every affected check is rerun against that new version.",
                "A video that looks correct in a player can still be technically invalid for the destination platform, and the failure surfaces at upload rather than in review. Deterministic probing catches that class of defect while it is still cheap to fix. Binding approval to a hash prevents the most damaging version-control error in a release pipeline: approving one master and shipping another. Re-testing the affected scope after a repair is what stops a fix in one place from silently breaking another.",
                [
                    "Probe the container and record the observed width, height, average frame rate and duration.",
                    "Inspect frames and confirm captions are present and readable.",
                    "Register each asset with its source, rights status and SHA-256 hash.",
                    "Open a finding with its severity, assign the repair and render a new immutable version.",
                    "Rerun every affected check against the new version and record the outcome.",
                ],
                [
                    "technical-qc.json and the contact sheet show the observed values against the required bounds.",
                    "asset-manifest.csv verifies rights status and hashes for every manifest row.",
                    "repair-log.json links the finding, the change, the new hash and the re-test result.",
                ],
                [
                    "A master is a candidate for release and must meet a declared delivery specification.",
                    "Approval will be given now and acted on later, so the approved artifact must be identifiable.",
                ],
                [
                    "The delivery specification has not been agreed, so there is nothing to check against.",
                    "A finding would be closed without re-testing the checks it affects.",
                ],
                [
                    ("Failure signal", "A repair closes one finding and reopens another that was previously passing."),
                    ("Repair move", "Write a new immutable version and rerun the full affected scope rather than the single check."),
                    ("Quality evidence", "Closed findings outnumber reopened findings and each closure names its re-test."),
                ],
                [
                    "https://ffmpeg.org/ffprobe.html",
                    "https://developers.google.com/youtube/v3/docs/captions",
                ],
            ),
        ],
    ),
    dict(
        num=3,
        code="03",
        title="Multi-Agent Kanban, YouTube Release and Scheduled Publishing",
        subtitle="Agent role contracts | Delegation and parallel work | Durable Kanban | Approval hash and cron release",
        weighting="Day 2 afternoon | 3 labs",
        concepts=[
            ("Role contract", "One agent, one owned deliverable, a bounded tool list and one measurable completion rule."),
            ("Delegation context", "The exact goal, paths, inputs, constraints and acceptance tests handed to a child agent."),
            ("Durable Kanban", "Task state and dependencies that survive restarts and deliberate human pauses."),
            ("Approval hash", "A named decision bound to the immutable hash of the release package it authorises."),
        ],
        sections=[
            _section(
                "Agent Role Contracts and the Four Specialist Roles",
                "Each agent receives a contract: a goal, a bounded list of allowed tools, one named deliverable and an explicit completion rule. This course uses four roles. The research agent reads the brief, retrieves sources, scores evidence and hands off claims with retrievable URLs and stated limitations. The video production agent consumes approved claims, creates the shot plan, invokes the brand skill and returns a master with its hash. The independent review agent inspects evidence against a rubric and creates timecoded findings. The upload agent verifies approval, builds metadata and uploads privately.",
                "Roles without contracts drift into each other until no agent owns the outcome and two agents rewrite the same artifact. One deliverable per agent makes ownership unambiguous and makes a stalled pipeline diagnosable — the incomplete deliverable identifies the responsible role. The reviewer is deliberately denied approval authority: a reviewer that can approve its own findings provides no independent check, because the same assumptions that produced the work would clear it.",
                [
                    "Define the goal, limit the tools, name the deliverable and set the completion rule for each role.",
                    "Require the research agent to produce retrievable URLs, bounded excerpts and explicit limitations.",
                    "Give the production agent immutable research input and require the custom brand-video skill.",
                    "Run the reviewer in an independent context and withhold approval authority from that role.",
                    "Block the upload agent until every parent deliverable and the current approval hash pass.",
                ],
                [
                    "agent-contracts.yaml validates all four specialist roles against the required fields.",
                    "research-handoff.json contains approved sources and claim identifiers.",
                    "review-handoff.json contains timecoded findings and a QA status but no approval decision.",
                ],
                [
                    "Distinct roles have genuinely different tools, inputs or review criteria.",
                    "An independent check is needed before a consequential external action.",
                ],
                [
                    "One bounded prompt and one tool would complete the task more reliably.",
                    "Agents would share unrestricted credentials or be able to overwrite accepted artifacts.",
                ],
                [
                    ("Failure signal", "Two agents disagree about which artifact is current."),
                    ("Repair move", "Give each deliverable one owning role and one immutable version identifier."),
                    ("Quality evidence", "Every factual claim in the output traces to a sourced claim identifier."),
                ],
                [
                    "https://hermes-agent.nousresearch.com/docs/guides/delegation-patterns",
                    "https://hermes-agent.nousresearch.com/docs/user-guide/features/kanban",
                ],
            ),
            _section(
                "Delegation Context, Parallel Work and the Durable Kanban",
                "A delegation context packages the goal, the required context, the exact paths and the acceptance tests before a child agent is dispatched. Independent tasks may run in parallel, but the join happens only on explicit verified artifacts rather than on elapsed time. The Hermes Kanban makes this durable: tasks carry an assignee, a status and parent identifiers, and the board survives restarts and deliberate human pauses, which is what allows a production run to span a break, a review or an overnight wait.",
                "A child agent that receives a goal without paths, inputs and tests will produce something plausible that does not fit the pipeline, and the mismatch is usually discovered at the join. Parallelising dependent work is worse: it appears faster while silently skipping a dependency. A durable board is what separates a multi-agent workflow from a long single conversation — work that must survive a restart cannot live only in a session, and a paused human review is a normal state rather than a failure.",
                [
                    "Package the goal, context, exact paths and acceptance criteria into the delegation context.",
                    "Dispatch the child agent, receive its summary and verify the artifact it claims to have produced.",
                    "Identify genuinely independent tasks and dispatch those as a batch.",
                    "Create the board tasks, assign profiles and link every dependency before running the dispatcher.",
                    "Join only after all required parents are complete and verified.",
                ],
                [
                    "delegation-log.json records the prompt, the agent and the verified result.",
                    "join-ledger.json shows every required parent complete before the join proceeded.",
                    "kanban-export.json shows the full dependency chain with no missing dependency.",
                ],
                [
                    "Work crosses several agents and must survive restarts or a human pause.",
                    "Independent tasks exist and the join can be defined on verified artifacts.",
                ],
                [
                    "The tasks are dependent, so parallel dispatch would skip a dependency.",
                    "The work fits one session and gains nothing from durable state.",
                ],
                [
                    ("Failure signal", "A task repeats the same failure and the pipeline retries it indefinitely."),
                    ("Repair move", "Cap attempts, classify the failure and block repeated failures for human intervention."),
                    ("Quality evidence", "Task history shows checkpoints, the review and the final evidence for each task."),
                ],
                [
                    "https://hermes-agent.nousresearch.com/docs/guides/delegation-patterns",
                    "https://hermes-agent.nousresearch.com/docs/user-guide/features/kanban",
                ],
            ),
            _section(
                "Human Approval, the YouTube Contract and Publishing Idempotency",
                "Before release the package is frozen and hashed, and a named reviewer approves that specific hash. Immediately before upload the current master hash is compared against the approved hash; a mismatch blocks the upload. The YouTube videos.insert contract requires OAuth authorisation, a snippet, a status block carrying the privacy setting and, where applicable, the synthetic-media disclosure. Uploads default to private. An idempotency key is created before the attempt and reconciled after it, so one approved package yields at most one committed video identifier.",
                "Publishing is irreversible in a way that almost nothing earlier in the pipeline is. Approving a hash rather than a filename closes the gap where an artifact changes between approval and upload. Defaulting to private means a mistake is recoverable by deleting a private video rather than by retracting a public one. Reconciling an idempotency key before a retry prevents the specific failure where a network timeout on a successful upload produces a second copy on the channel.",
                [
                    "Freeze the release package, compute its hash and request approval against that hash.",
                    "Recheck the current master hash immediately before upload and block on any mismatch.",
                    "Authorise OAuth, confirm the channel identity, then set the snippet and the status block.",
                    "Default privacy to private and include the synthetic-media disclosure where applicable.",
                    "Create the publish key, check any prior result, then upload and commit the returned identifier.",
                ],
                [
                    "approval-ledger.json proves the reviewer, the time, the decision and the approved hash.",
                    "request-preview.json and the private upload receipt match the approved package.",
                    "publication-ledger.csv contains exactly one committed video identifier per idempotency key.",
                ],
                [
                    "An external, irreversible action is about to be taken on an approved artifact.",
                    "Retries are possible and duplicate posts would be damaging.",
                ],
                [
                    "The approved hash does not match the current master hash.",
                    "Channel identity, disclosure or rights are unresolved, or public visibility is proposed without supervision.",
                ],
                [
                    ("Failure signal", "A retry after a timeout produces a second video on the channel."),
                    ("Repair move", "Reconcile the prior idempotency key and its committed video identifier before retrying."),
                    ("Quality evidence", "The duplicate publish rate is zero across all recorded attempts."),
                ],
                [
                    "https://developers.google.com/youtube/v3/docs/videos/insert",
                    "https://developers.google.com/youtube/v3/docs/captions",
                ],
            ),
            _section(
                "Hermes Cron and Controlled Scheduled Release Operations",
                "A cron job runs in a fresh session, so its prompt must be self-contained: every required path, gate and stop rule is written into the job, and the skills it needs are attached explicitly. The job is created paused. It is exercised with a dry run whose output is inspected, and the next scheduled run is confirmed before any cadence is enabled. Scheduled work in this course prepares the release and performs the private upload; public visibility remains a separate, explicitly approved decision.",
                "A scheduled job inherits nothing from the session that created it, so a prompt that relies on conversational context will behave differently at three in the morning than it did during testing. Creating the job paused makes that difference observable before it matters. Restricting the schedule to preparation and private upload means the worst outcome of a scheduling defect is an unwanted private draft rather than an unapproved public post.",
                [
                    "Write a self-contained job prompt containing every required path, gate and stop rule.",
                    "Attach the custom video skill and any other required skills explicitly.",
                    "Create the schedule with an explicit timezone and leave the job paused.",
                    "Trigger a dry run, inspect the output and confirm the next run time.",
                    "Enable the cadence only after the evidence has been reviewed and the enablement approved.",
                ],
                [
                    "cron-preview.json records the schedule, the next run and the paused state.",
                    "operations-ledger.csv records each run, its outcome and the owner's decision.",
                    "The dry run cannot publish an unapproved or duplicate video.",
                ],
                [
                    "A release cadence is required and the preparation steps are already reliable.",
                    "The job can be made fully self-contained and exercised with a dry run first.",
                ],
                [
                    "The job prompt still depends on context from the session that created it.",
                    "Enabling the cadence would allow a public post without a separate approval.",
                ],
                [
                    ("Failure signal", "A job that passed interactively behaves differently on its first scheduled run."),
                    ("Repair move", "Move every implicit path, gate and stop rule into the job prompt and re-run the dry run."),
                    ("Quality evidence", "The on-time success rate holds with zero unauthorised posts."),
                ],
                [
                    "https://hermes-agent.nousresearch.com/docs/user-guide/features/cron",
                    "https://developers.google.com/youtube/v3/docs/videos/insert",
                ],
            ),
        ],
    ),
]

DAY_THEMES = {
    1: "Configure Hermes, engineer video prompts and route the media tools",
    2: "Build the branded video, then orchestrate review and controlled release",
}


def SCHEDULE(lab_titles):
    return {
        1: (
            DAY_THEMES[1],
            [
                ("9:30", "9:50", 20, "admin", "Welcome, course introduction, setup, and learning approach"),
                ("9:50", "10:40", 50, "topic", "Topic 1 - Hermes Desktop runtime, MiniMax M3 provider contract, and credential isolation"),
                ("10:40", "10:55", 15, "break", "Tea break"),
                ("10:55", "11:45", 50, "lab", "Hands-on: " + lab_titles([1])),
                ("11:45", "12:35", 50, "lab", "Hands-on: " + lab_titles([2])),
                ("12:35", "13:00", 25, "topic", "Topic 1 - FRAME-CUT prompt contract and structured shot plans"),
                ("13:00", "14:00", 60, "lunch", "Lunch break"),
                ("14:00", "14:40", 40, "topic", "Topic 1 - Agent loop, cost ceilings, and stop rules"),
                ("14:40", "15:40", 60, "lab", "Hands-on: " + lab_titles([3])),
                ("15:40", "15:55", 15, "break", "Tea break"),
                ("15:55", "16:45", 50, "topic", "Topic 2 - Tool versus skill, Remotion, Manim, Higgsfield, and FFmpeg routing"),
                ("16:45", "17:45", 60, "lab", "Hands-on: " + lab_titles([4])),
                ("17:45", "18:30", 45, "recap", "Day 1 runtime and prompt-contract review, troubleshooting, and recap"),
            ],
        ),
        2: (
            DAY_THEMES[2],
            [
                ("9:30", "9:45", 15, "admin", "Day 1 checkpoint restore and Day 2 briefing"),
                ("9:45", "10:35", 50, "topic", "Topic 2 - Brand tokens, tone controls, quality gate, and versioned repair evidence"),
                ("10:35", "10:50", 15, "break", "Tea break"),
                ("10:50", "12:00", 70, "lab", "Hands-on: " + lab_titles([5])),
                ("12:00", "13:00", 60, "topic", "Topic 3 - Agent role contracts, delegation context, and parallel work"),
                ("13:00", "14:00", 60, "lunch", "Lunch break"),
                ("14:00", "15:10", 70, "lab", "Hands-on: " + lab_titles([6])),
                ("15:10", "15:25", 15, "break", "Tea break"),
                ("15:25", "15:55", 30, "topic", "Topic 3 - Durable Kanban, approval hash, YouTube contract, and idempotency"),
                ("15:55", "16:55", 60, "lab", "Hands-on: " + lab_titles([7])),
                ("16:55", "17:45", 50, "lab", "Hands-on: " + lab_titles([8])),
                ("17:45", "18:30", 45, "recap", "Integrated workflow demonstration, next steps, and course recap"),
            ],
        ),
    }


COURSE_OVERVIEW = dict(
    section_title="Agentic Video Production Foundations",
    concepts_title="What Makes a Video Workflow Agentic",
    concepts=[
        ("Goal and state", "The system knows the approved brief, the accepted artifacts, the current stage, and the unresolved work."),
        ("Reasoning and routing", "MiniMax M3 chooses among bounded next actions while deterministic rules enforce known constraints."),
        ("Tools and skills", "Every capability has typed inputs, portable outputs, permissions, budgets, and failure behaviour."),
        ("Evidence and control", "Ledgers, hashes, probes, approvals, and stop rules keep the work reviewable."),
    ],
    framework_title="The C436 Agent Loop",
    framework=[
        ("1 | Observe", "Read the approved brief, the current state, and the asset manifest."),
        ("2 | Plan", "Produce a validated shot plan that totals the approved duration."),
        ("3 | Act", "Call one allowed tool or skill with structured inputs and a capped attempt count."),
        ("4 | Inspect", "Probe the artifact and check it against the declared delivery specification."),
        ("5 | Decide", "Accept, repair within limits, or stop and record the stop reason."),
        ("6 | Record", "Persist the ledger entry, the hash, and the approval decision before continuing."),
    ],
    statement=dict(
        headline="Autonomy is a design variable, not the goal.",
        body="Use deterministic tools for known operations, model judgment for bounded choices, and human approval for consequential actions.",
        kicker="CORE PRINCIPLE",
    ),
    pillars_title="The Connected Hermes Build",
    pillars=[
        ("Configure", ["Hermes runtime", "MiniMax M3", "Credential isolation"]),
        ("Prompt", ["FRAME-CUT contract", "Shot plan JSON", "Preview render"]),
        ("Produce", ["Tool routing", "Brand tokens", "Custom video skill"]),
        ("Review", ["Role contracts", "Durable Kanban", "Independent findings"]),
        ("Release", ["Approval hash", "Private upload", "Paused cron"]),
    ],
    arc_title="How Every Lab Progresses",
    arc=[
        "Open the lab folder as the current Hermes project and read its copy-ready prompts.",
        "Ask Hermes to inspect the supplied local files before it proposes a plan.",
        "Require a preview before any network, paid-generation, upload, or scheduling side effect.",
        "Run the lab's verify.py and retain the PASS output with the requested evidence.",
        "Reflect on which choices should remain deterministic, model-led, or human-approved.",
    ],
    deep_dives=[
        dict(
            title="Autonomy Matrix",
            kicker="CONTROL DESIGN",
            items=[
                ("Deterministic", "Schema validation, duration arithmetic, media probing, hashing, and file naming."),
                ("Model-assisted", "Shot planning, prompt repair, review findings, and research clustering."),
                ("Human-approved", "Claims, rights, brand exceptions, the final master, and every release action."),
                ("Prohibited by default", "Unreviewed public posts, credential exposure, and living-artist imitation."),
            ],
        ),
        dict(
            title="The FRAME-CUT Contract",
            kicker="STRUCTURED PROMPT",
            items=[
                ("Format and finish", "Channel, duration, aspect ratio, and delivery codec frozen before shot work."),
                ("Role and references", "Assigned role, attached brief, registered sources, and authorised assets."),
                ("Action and motion", "One dominant subject action and one camera move per timed shot."),
                ("Continuity and unwanted", "Identity and palette tokens to keep, plus explicit must-avoid elements."),
            ],
        ),
        dict(
            title="Release Evidence",
            kicker="OBSERVABILITY",
            items=[
                ("Identity", "Run ID, plan hash, master hash, asset version, and idempotency key."),
                ("Actions", "Tool or skill name, input reference, output reference, status, and error."),
                ("Controls", "Probe result, finding ID, approval hash, reviewer, and decision."),
                ("Resources", "Attempts, latency, estimated cost, and budget variance."),
            ],
        ),
    ],
)

LG_INTRO = (
    "This Learner Guide accompanies Agentic AI for Video Creation (C436). It is a "
    "self-contained study text and practical reference for building an evidence-led "
    "video production system in Hermes Agent, from runtime setup and prompt "
    "engineering to custom video skills, multi-agent review, and controlled release."
)
LG_INTRO2 = (
    "The three topics and eight connected labs follow one Hermes-native journey. "
    "Work in order and retain each lab's evidence: later labs consume the runtime "
    "configuration, prompt contracts, skills, and approved masters created earlier."
)

LG_SETUP = dict(
    needs=[
        "A Windows or macOS laptop with a modern browser, administrator rights to install desktop software, and permission to create local folders.",
        "Hermes Desktop installed from the official page at https://hermes-agent.nousresearch.com/desktop.",
        "A MiniMax account and API key for the MiniMax-M3 model; trial, quota, and region terms are time-sensitive and must be confirmed live at sign-up.",
        "Python 3 on PATH for the supplied verify.py scripts and preview renderers.",
        "FFmpeg and FFprobe on PATH. On Windows, install with 'winget install --id Gyan.FFmpeg -e'; on macOS, use 'brew install ffmpeg'. Reopen the terminal and verify both commands.",
        "A Google account with a YouTube channel for the release labs; uploads stay private and public visibility is never required to complete a lab.",
        "The repository's labs folder, which contains eight lab packages with copy-ready prompts, synthetic data, starter files, evidence checklists, and verifiers.",
    ],
    verify_text=(
        "Confirm that Hermes launches, the configured provider is minimax, the model "
        "is MiniMax-M3, and the media tools return a version. Never place a real "
        "secret value in a prompt, lab file, screenshot, or public repository."
    ),
    verify_code=(
        "hermes doctor\n"
        "ffmpeg -version\n"
        "ffprobe -version\n"
        "python3 --version"
    ),
    conventions=[
        "Replace placeholders such as <RUN_ID> or <API_KEY> only in Hermes credential or configuration storage, never in a prompt or lab file.",
        "Use the supplied synthetic lab data. Do not add real customer, employee, creator, or account data.",
        "Keep YouTube visibility private. Public release requires an explicit trainer-supervised decision.",
        "Require a preview before any network call, paid generation, upload, or scheduling side effect.",
        "Run the lab's verify.py and retain the PASS output before starting the next lab.",
        "If a tool is unavailable, use the documented deterministic fallback and record the limitation rather than inventing a successful call.",
        "Confirm live trial, quota, and pricing terms in your own account at sign-up; treat any figure in this guide as an example, not a current offer.",
    ],
)

LAB_NOTE = (
    "Use only supplied or authorised assets. Never paste a MiniMax key, OAuth token, "
    "or YouTube credential into a prompt, lab file, screenshot, or repository. "
    "YouTube examples default to private and scheduled publishing starts paused."
)

LG_WRAPUP = dict(
    title="Integrated Workflow Wrap-Up",
    intro=(
        "The completed C436 project is not merely a generated video. It is a "
        "controlled production system whose artifacts, decisions, and evidence can "
        "be reviewed, resumed, and improved."
    ),
    sections=[
        dict(
            title="Minimum handover package",
            bullets=[
                "Setup evidence, profile check, and model check with no credential value recorded.",
                "FRAME-CUT prompt pack, validated shot plan, and the preview probe.",
                "Tool routing registry, installed skills, brand profile, and the custom video skill.",
                "Agent contracts, Kanban export, review findings, approval ledger, and the cron preview.",
            ],
        ),
        dict(
            title="Operational rule",
            text=(
                "When a stage cannot prove that its required input is approved, it "
                "must stop or escalate. It must not silently invent the missing "
                "fact, permission, file, or decision."
            ),
        ),
    ],
)

LG_NEXT_STEPS = [
    "Rerun the eight labs from a clean profile and explain every recorded state transition.",
    "Replace one deterministic fallback with an approved live integration while preserving the same contract, limits, and evidence.",
    "Add three representative test jobs, including one missing-input case and one tool-failure case.",
    "Pilot with private outputs, review the repair and cost evidence, and enable a cadence only after the guardrails remain stable.",
    "Review the official Hermes, MiniMax, Remotion, Manim, and YouTube documentation before adapting any live API or interface shown in this guide.",
    "Recheck YouTube upload and privacy requirements at https://developers.google.com/youtube/v3/guides/uploading_a_video before any authorised public release.",
]

LG_GLOSSARY = [
    ("Agent loop", "The repeated observe, plan, act, inspect, decide, and record cycle."),
    ("Approval hash", "A named decision bound to the immutable hash of the package it authorises."),
    ("Asset manifest", "The authoritative inventory of assets with source, rights status, version, and checksum."),
    ("Brand token", "A stored, editable value for logo, palette, typography, or motion referenced by a skill."),
    ("Circuit breaker", "A cap on attempts that blocks a repeatedly failing task for human intervention."),
    ("Continuity token", "A reusable identifier that holds subject identity and palette stable across shots."),
    ("Cron job", "A scheduled Hermes task that runs in a fresh session from a self-contained prompt."),
    ("Delegation context", "The goal, context, exact paths, and acceptance tests handed to a child agent."),
    ("FRAME-CUT", "The prompt contract covering Format, Role, Action, Motion, Environment, Continuity, Unwanted, and Technical output."),
    ("Hermes Desktop", "The desktop application surface of Hermes Agent, sharing profile and configuration with the CLI."),
    ("Idempotency key", "A stable identifier used to prevent a retry from creating a duplicate external action."),
    ("Kanban", "A durable board of tasks with assignees, statuses, and parent dependencies that survives restarts."),
    ("MiniMax M3", "The reasoning and tool-orchestration model configured through the minimax provider."),
    ("Progressive loading", "Searching the skill catalogue first and loading only the resources a selected skill references."),
    ("Provenance", "Recorded information about an asset's source, licence, version, and checksum."),
    ("Quality gate", "A fail-closed technical check on container, streams, dimensions, frame rate, duration, and captions."),
    ("Shot plan", "Strict JSON of timed shots whose durations total the approved target with no gaps or overlaps."),
    ("Skill", "A directory containing SKILL.md, scripts, and templates that package a repeatable procedure."),
    ("Synthetic media disclosure", "The platform status field declaring that content was generated or materially altered."),
]

NEXT_STEPS = dict(
    title="Continue Building Safely",
    items=[
        "Replace one deterministic fallback at a time and retain its contract and evidence.",
        "Create test jobs for a missing input, a malformed shot plan, a tool failure, and a denied approval.",
        "Keep uploads private until channel permissions and an accountable release owner are confirmed.",
        "Measure accepted masters, repair rate, cost, and latency before enabling any cadence.",
    ],
)

THANK_YOU = dict(
    body=(
        "You can now configure Hermes Agent, engineer video prompts, build a custom "
        "branded video skill, and operate a reviewed, evidence-led release pipeline."
    ),
    kicker="C436 | AGENTIC AI FOR VIDEO CREATION",
)

TRAINER_TEAM = [
    ("Surendra Batukdeo", "Emerging-technology, automation, data-intelligence, project, and technical-training experience."),
    ("Agus Salim", "IT solutions, systems integration, cloud infrastructure, project, and cybersecurity experience."),
    ("Quah Chee Yong", "Data science, Python, natural-language processing, machine-learning, and AI-training experience."),
]

ICE_BREAKER = [
    "Introduce yourself and name one short-form video workflow you would like to improve.",
    "Identify the stage that consumes the most time or creates the most rework.",
    "State one video action you would never allow an agent to take without your approval.",
]

LAB_SHOTS = {}

VERSION_HISTORY = [
    ("1.0", "29 July 2026", "Initial aligned release of the C436 deck, Learner Guide, Lesson Plan, and eight connected labs.", TRAINER),
    ("2.0", VERSION_DATE, "Rebuilt on Hermes Agent and MiniMax M3: three topics, FRAME-CUT prompt engineering, Remotion/Manim/Higgsfield/FFmpeg tool routing, custom brand-video skill, multi-agent Kanban review, private YouTube release, and paused cron publishing. Replaces the previous n8n-based labs.", TRAINER),
]
