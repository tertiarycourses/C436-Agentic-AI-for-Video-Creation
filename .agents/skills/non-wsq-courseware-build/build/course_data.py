"""Single source of truth for Agentic AI for Video Creation (C436)."""

TITLE = "Agentic AI for Video Creation"
SHORT_TITLE = "Agentic AI for Video Creation"
COURSE_CODE = "C436"
COURSE_URL = "https://www.tertiarycourses.com.sg/agentic-ai-for-video-creation.html"
VERSION = "v1.0"
VERSION_DATE = "29 July 2026"
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
    "LO1: Explain agentic AI, select suitable video-production tools, write bounded prompts, and design a controlled end-to-end workflow.",
    "LO2: Build AI-assisted research, scripting, storyboard, visual, voiceover, and music hand-offs from an approved creative brief.",
    "LO3: Assemble and refine a short-form video through automated editing, captioning, branding, and evidence-based quality checks.",
    "LO4: Orchestrate multi-step video agents with human approval, prepare safe publishing actions, analyse performance, and plan responsible scale.",
]

LO_TITLES = [
    "Design the Agent",
    "Generate the Assets",
    "Edit and Review",
    "Publish and Scale",
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
        title="Getting Started with Agentic AI for Video",
        subtitle="Agentic AI foundations | Video, voice, and agent tools | Effective prompts | End-to-end workflow design",
        weighting="Day 1 morning | 2 labs",
        concepts=[
            ("Agent loop", "A bounded cycle of observe, plan, act with tools, inspect evidence, and stop or escalate."),
            ("Production contract", "A structured brief that fixes the audience, goal, source facts, constraints, deliverables, and approval gates."),
            ("Tool boundary", "A named capability with explicit inputs, outputs, permissions, cost limits, and failure behavior."),
            ("Human control", "People approve high-impact creative, rights, privacy, brand, and publishing decisions."),
        ],
        sections=[
            _section(
                "Introduction to Agentic AI for Video Creation",
                "Agentic AI combines a model with instructions, tools, state, and a control loop so that the system can decide which bounded action to take next. In video production, an agent may inspect a brief, request missing facts, call research or generation tools, record outputs, check quality, and route an item for human approval. It is different from a one-shot chatbot because the workflow carries state and can take several tool-mediated steps toward a defined completion condition.",
                "Video work contains creative uncertainty as well as operational dependencies. A reliable agent must know what it may decide, what evidence it must retain, and when it must stop. Treating every step as autonomous creates rights, privacy, cost, and brand risk; treating every step as fixed automation misses the value of reasoning. The practical design is bounded autonomy: deterministic rules for known operations, model judgment for well-framed choices, and human review for consequential actions.",
                [
                    "Observe the approved brief and current production state.",
                    "Plan the next smallest useful action against a completion checklist.",
                    "Call only an allowed tool with structured inputs and a budget.",
                    "Inspect the returned artifact, provenance, and quality evidence.",
                    "Continue, retry within limits, or escalate to a named human owner.",
                ],
                [
                    "Harbour Bean needs a 30-second vertical video about three ways to reduce bitter office coffee.",
                    "A coordinator agent checks the brief, delegates research and scripting, then prepares scene requests.",
                    "Every generator result is written to an asset register; publishing remains disabled until a person approves the final package.",
                ],
                [
                    "The task has several dependent steps and the next action depends on intermediate evidence.",
                    "Inputs, tool permissions, completion rules, and escalation paths can be stated clearly.",
                ],
                [
                    "The goal is vague, the source facts are unapproved, or there is no accountable owner.",
                    "The proposed action would publish, spend, or use a person's likeness without explicit review.",
                ],
                [
                    ("Failure signal", "The system keeps generating options without reaching a defined finish state."),
                    ("Repair move", "Add a completion checklist, iteration cap, and escalation rule."),
                    ("Quality evidence", "The run log shows why each tool was called and who approved the release."),
                ],
                [
                    "https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/",
                    "https://openai.github.io/openai-agents-python/agents/",
                ],
            ),
            _section(
                "Popular AI Video, Voice, and Agent Tools",
                "A production stack usually separates orchestration from specialist tools. The orchestrator holds the workflow state and routes tasks. Language models research and write. Image or video generators create candidate shots. Speech services produce narration. Editors and command-line media tools assemble, caption, mix, and export. Publishing and analytics APIs act only after credentials and permissions are configured.",
                "Product names and features change, but the jobs remain stable. A portable architecture defines each tool by capability, contract, and fallback instead of hiding the project inside one vendor. Structured outputs reduce broken hand-offs: a script agent should return timed beats, a visual tool should return a file plus provenance, and an editor should receive a validated manifest rather than free-form prose.",
                [
                    "List each production job and the data it consumes or creates.",
                    "Assign one primary tool and one manual or alternate fallback to each job.",
                    "Define structured fields, file names, size limits, and accepted formats.",
                    "Restrict credentials to the smallest permissions the tool needs.",
                    "Record cost, latency, rights terms, and failure behavior before use.",
                ],
                [
                    "n8n coordinates eight stages without storing secret values in prompts.",
                    "ChatGPT or Claude creates structured research and script outputs from approved source material.",
                    "A chosen video generator supplies clips, ElevenLabs or an equivalent supplies narration, and FFmpeg or an editor assembles the vertical master.",
                ],
                [
                    "A specialist capability materially improves a defined stage and produces a portable output.",
                    "The team has an approved account, a fallback, and a clear rights and privacy position.",
                ],
                [
                    "A tool requires confidential material that is not approved for that service.",
                    "The workflow cannot export files, preserve provenance, or cap cost and retries.",
                ],
                [
                    ("Failure signal", "A downstream stage cannot understand the previous tool's free-form response."),
                    ("Repair move", "Define a JSON or file manifest contract with required fields."),
                    ("Quality evidence", "Each stage can be swapped without redesigning the complete workflow."),
                ],
                [
                    "https://github.com/n8n-io/n8n-docs/blob/main/docs/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/tools-agent.md",
                    "https://platform.claude.com/docs/en/agents-and-tools/tool-use/how-tool-use-works",
                    "https://elevenlabs.io/docs/overview/capabilities/text-to-speech",
                ],
            ),
            _section(
                "Writing Effective Prompts for Video",
                "An effective agent prompt is an operating contract, not a slogan. This course uses B-R-I-E-F: Background, Role and responsibility, Inputs and evidence, Execution constraints, and Format plus finish condition. The prompt states which facts are authoritative, which tools may be used, what must never happen, and exactly what valid output looks like.",
                "A creative request such as 'make a viral video' leaves the system to invent the audience, claims, style, and success rule. A structured prompt produces comparable alternatives, exposes missing evidence, and makes hand-offs machine-readable. Separate stable system instructions from per-run input, and validate important fields before a later tool acts on them.",
                [
                    "Set the audience, business purpose, channel, duration, and desired viewer action.",
                    "Provide approved source facts and mark unknown information explicitly.",
                    "Name the agent's role, allowed tools, cost and iteration limits, and prohibited actions.",
                    "Require a schema for scripts, scenes, claims, assets, risks, and open questions.",
                    "Define a finish condition and conditions that require human clarification.",
                ],
                [
                    "Background: a Singapore cafe campaign for busy office workers.",
                    "Inputs: only the supplied brand brief and audience signals may support claims.",
                    "Execution: return three 25-35 second concepts; do not publish or imitate a living creator.",
                    "Format: valid JSON with hook, timed beats, scene list, evidence, risks, and status.",
                ],
                [
                    "Inputs and desired outputs can be bounded and checked.",
                    "Several tools or agents need a common production contract.",
                ],
                [
                    "The instruction hides a policy decision that an accountable person must make.",
                    "The output cannot be validated before a costly or external action follows.",
                ],
                [
                    ("Failure signal", "The output looks plausible but omits required fields or invents a source."),
                    ("Repair move", "Add a schema, evidence citations, explicit unknown handling, and a validator."),
                    ("Quality evidence", "A second run can use the same prompt contract and produce structurally valid output."),
                ],
                [
                    "https://platform.claude.com/docs/en/agents-and-tools/tool-use/how-tool-use-works",
                    "https://openai.github.io/openai-agents-js/guides/guardrails/",
                ],
            ),
            _section(
                "Designing an End-to-End Video Agent Workflow",
                "A workflow turns the production contract into observable stages: intake, research, concept selection, script and storyboard, asset generation, assembly, quality review, approval, publishing preparation, and learning. Each stage receives a defined input, writes a durable output, and returns a status such as ready, needs-revision, blocked, or approved.",
                "Large all-in-one agents are difficult to debug and may repeat expensive work. Stage boundaries create checkpoints, allow deterministic validation, and let a learner restart from the last accepted artifact. Idempotency keys prevent a retry from duplicating external actions; run identifiers connect every artifact and log entry to the same job.",
                [
                    "Draw the stages and mark every external system or generated artifact.",
                    "Define one input/output contract and owner for each stage.",
                    "Place validation before expensive generation and approval before publishing.",
                    "Add retry limits, timeouts, idempotency keys, and a dead-letter or rework route.",
                    "Log run ID, prompt version, tool, cost, result, evidence, and approval decision.",
                ],
                [
                    "Run HB-001 advances only when brief_status=approved and script_status=approved.",
                    "Scene generation retries once for a technical failure but routes a rights concern to human review.",
                    "The publishing node receives a release package only; it cannot see raw research or use an unapproved file.",
                ],
                [
                    "The work has repeatable stages and accepted artifacts can be reused.",
                    "The system can save state and resume safely after a failure.",
                ],
                [
                    "The process is a one-off creative conversation with no reusable structure.",
                    "A retry might duplicate an external action and no idempotency or approval control exists.",
                ],
                [
                    ("Failure signal", "A failed final step forces the whole production to regenerate."),
                    ("Repair move", "Persist accepted stage outputs and resume from a checkpoint."),
                    ("Quality evidence", "A run can stop, rejoin, and explain its complete state without guesswork."),
                ],
                [
                    "https://docs.n8n.io/flow-logic/error-handling/",
                    "https://docs.n8n.io/advanced-ai/examples/human-fallback/",
                ],
            ),
        ],
    ),
    dict(
        num=2,
        code="02",
        title="Scripting and Generating Content with AI",
        subtitle="Trend and idea research | Scripts and storyboards | Visuals and B-roll | Voiceovers and music",
        weighting="Day 1 afternoon | 2 labs",
        concepts=[
            ("Source register", "A dated record of evidence, relevance, permissions, and claims that may be used."),
            ("Timed beat sheet", "A sequence linking narration, visual, on-screen text, sound, and duration."),
            ("Asset manifest", "The authoritative list of scene files, prompts, versions, rights notes, and status."),
            ("Continuity bible", "Stable character, product, lighting, palette, camera, and negative constraints across generations."),
        ],
        sections=[
            _section(
                "Researching Trends and Ideas",
                "Agentic research is a bounded evidence-gathering workflow. It starts with a question and approved source types, retrieves observations, records provenance, separates evidence from inference, and produces candidate ideas that are traceable to audience need. Trend signals are clues for timing and format, not permission to copy another creator.",
                "A research agent can gather many examples quickly, but search results may be stale, duplicated, promotional, or detached from the target audience. A source register and evidence threshold prevent a script agent from treating popularity as truth. The output should include open questions and rejected ideas, not only a polished recommendation.",
                [
                    "State the audience problem, research window, market, and allowed sources.",
                    "Collect dated signals and record source, observation, and confidence separately.",
                    "Cluster repeated needs, questions, formats, and language patterns.",
                    "Generate original angles from the brand's own proof and feasible assets.",
                    "Human-review the shortlist for relevance, truth, rights, and production effort.",
                ],
                [
                    "Audience signals mention bitter office coffee, inconsistent scoops, and limited time.",
                    "The agent groups these into three teachable variables instead of copying a trending cafe video.",
                    "Each candidate idea cites the supplied observation and the brand fact that supports it.",
                ],
                [
                    "The question, time window, source types, and evidence threshold are explicit.",
                    "A person can inspect the source register before ideas move to scripting.",
                ],
                [
                    "The workflow would scrape personal data or bypass platform access controls.",
                    "Trend volume is being used as proof for a product or health claim.",
                ],
                [
                    ("Failure signal", "The idea bank contains unsourced claims and near-copies of examples."),
                    ("Repair move", "Require provenance, originality notes, and a reason for every retained idea."),
                    ("Quality evidence", "The chosen idea can be traced to audience evidence and approved brand facts."),
                ],
                [
                    "https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/",
                    "https://platform.claude.com/docs/en/agents-and-tools/tool-use/how-tool-use-works",
                ],
            ),
            _section(
                "Generating Scripts and Storyboards",
                "A script translates the selected promise into spoken words and on-screen text; a storyboard translates the same promise into timed visual evidence. The agent should work in beats rather than a single paragraph. Every beat states time, narration, picture, overlay, sound, claim source, and transition so production and review share one model.",
                "Short-form videos fail when words, visuals, and captions compete or when the final edit exceeds the target duration. Time budgeting before generation constrains scope and avoids unnecessary media cost. A storyboard also exposes scenes that cannot be produced safely or consistently before the system requests them.",
                [
                    "Lock one hook, promise, evidence set, and viewer action.",
                    "Allocate seconds to hook, proof beats, synthesis, and close.",
                    "Write concise narration and a shorter complementary text overlay.",
                    "Specify a feasible shot, motion, composition, and transition for each beat.",
                    "Run claim, duration, continuity, accessibility, and rights checks before approval.",
                ],
                [
                    "A 30-second script allocates 3 seconds to the hook, 21 seconds to three fixes, and 6 seconds to recap and close.",
                    "The spoken line explains the fix while on-screen text labels only the variable.",
                    "Every claim points back to an approved source row; the storyboard marks one synthetic scene for disclosure.",
                ],
                [
                    "The message and source facts are approved and a duration can be fixed.",
                    "The next stage needs structured scene requests and voice text.",
                ],
                [
                    "The script requires unsupported before-and-after proof or an unapproved likeness.",
                    "The storyboard depends on complex continuity the chosen generator cannot maintain.",
                ],
                [
                    ("Failure signal", "Narration, captions, and visuals repeat the same sentence."),
                    ("Repair move", "Assign a distinct job to each channel: explain, label, or demonstrate."),
                    ("Quality evidence", "A cold reader can produce the intended cut from the timed beat sheet."),
                ],
                [
                    "https://www.w3.org/TR/webvtt1/",
                    "https://elevenlabs.io/docs/eleven-creative/playground/text-to-speech",
                ],
            ),
            _section(
                "Creating Visuals and B-Roll with AI",
                "Visual generation converts storyboard beats into candidate images or clips. A strong scene request defines subject, action, environment, composition, camera, lighting, palette, duration, and negative constraints. The asset manifest records the prompt, model or tool, date, version, rights note, and accepted use for every file.",
                "One attractive clip does not create a coherent video. Continuity, editability, and factual fit matter more than isolated novelty. Generate short modular shots, preserve safe areas for vertical overlays, and review anatomy, text, logos, product details, and motion before a clip is accepted.",
                [
                    "Create a continuity bible from the approved brand and storyboard.",
                    "Generate low-cost candidates or still frames before expensive motion.",
                    "Inspect each result against scene purpose, composition, continuity, and rights.",
                    "Record accepted and rejected versions in the asset manifest.",
                    "Use approved stock or a supplied fallback if generation fails.",
                ],
                [
                    "Scene 02 shows a measured scoop and timer on a clean office pantry counter.",
                    "The prompt fixes the Harbour Bean palette and leaves the lower third clear for captions.",
                    "A clip with a malformed product label is rejected even if its motion is appealing.",
                ],
                [
                    "The scene is synthetic, clearly bounded, and does not require a real person's identity.",
                    "The team can retain provenance and has a fallback for failed generation.",
                ],
                [
                    "The scene impersonates a person, fabricates a real event, or uses protected material without permission.",
                    "The required text or exact product geometry should be produced deterministically in the editor.",
                ],
                [
                    ("Failure signal", "Accepted scenes vary in lighting, product form, and screen direction."),
                    ("Repair move", "Reuse a continuity bible and generate by shot family with reference frames where allowed."),
                    ("Quality evidence", "Every accepted file has provenance and supports a named storyboard beat."),
                ],
                [
                    "https://platform.openai.com/docs/api-reference/videos",
                    "https://developers.openai.com/api/docs/models/sora-2",
                ],
            ),
            _section(
                "Generating Voiceovers and Music",
                "Voice generation turns approved narration into timed audio. Music supports pace and emotion without masking speech. The workflow selects a permitted voice, normalises written text for speech, produces an audio file, checks pronunciation and duration, and records the service, settings, consent, and usage terms.",
                "Audio can make a visually strong video inaccessible or untrustworthy. Unauthorised voice cloning, poor pronunciation, excessive loudness, and unclear licensing create avoidable risk. Voice and music are therefore separate reviewed assets with explicit owners and fallback options.",
                [
                    "Use an approved synthetic or licensed voice; obtain consent for any personal voice clone.",
                    "Rewrite symbols, dates, acronyms, and names for the intended spoken form.",
                    "Generate a test line, review pronunciation and pace, then render the full narration.",
                    "Choose licensed music or a platform-approved library and retain the rights note.",
                    "Mix for intelligible speech, inspect peaks, and preview on speakers and headphones.",
                ],
                [
                    "The agent converts '3 fixes in 30 sec' to natural spoken wording before synthesis.",
                    "The narrator file is saved with the script version and chosen settings.",
                    "Background music is ducked under speech and the no-music export remains available as a fallback.",
                ],
                [
                    "The voice identity and music rights are explicit and suitable for the intended channel.",
                    "A person can listen to and approve the complete audio before assembly.",
                ],
                [
                    "The workflow clones a voice without documented permission.",
                    "Licensing, commercial use, or territorial rights cannot be established.",
                ],
                [
                    ("Failure signal", "The narration sounds natural but mispronounces the brand or exceeds the scene timing."),
                    ("Repair move", "Add a pronunciation dictionary, rewrite for speech, and regenerate only the affected line."),
                    ("Quality evidence", "The approved audio matches the timed script and has a recorded rights basis."),
                ],
                [
                    "https://elevenlabs.io/docs/overview/capabilities/text-to-speech",
                    "https://elevenlabs.io/docs/api-reference/authentication",
                    "https://elevenlabs.io/docs/api-reference/text-to-speech/convert",
                ],
            ),
        ],
    ),
    dict(
        num=3,
        code="03",
        title="Editing and Assembling Videos with AI",
        subtitle="Automated editing | Captions, effects, and branding | Short-form assembly | AI-supported review and refinement",
        weighting="Day 2 morning | 2 labs",
        concepts=[
            ("Edit decision list", "A deterministic map from source assets to timeline order, in/out points, overlays, and transitions."),
            ("Media probe", "Machine-readable evidence about codec, resolution, frame rate, duration, audio, and streams."),
            ("Caption track", "Time-aligned text stored as a portable file and optionally burned into the picture."),
            ("Quality gate", "A documented set of technical, editorial, accessibility, rights, and brand checks."),
        ],
        sections=[
            _section(
                "Automating Video Editing",
                "Automated editing turns an approved manifest and edit decision list into a repeatable render. Deterministic operations such as trim, scale, crop, concatenate, overlay, caption, and audio mix are best handled by an editor or media pipeline. A model may propose the sequence or repair plan, but the render command should be explicit and logged.",
                "Regenerating a full timeline for a small change wastes time and can introduce new errors. Manifest-driven assembly makes each input and transformation visible, supports selective reruns, and produces the same output from the same accepted files. A media probe before and after the render catches mismatched dimensions, missing audio, and duration drift.",
                [
                    "Validate that every required scene and audio file exists and is approved.",
                    "Normalise aspect ratio, frame rate, codec, and naming before assembly.",
                    "Build the timeline from a versioned edit decision list.",
                    "Render to a draft path, then probe technical properties and duration.",
                    "Promote only the accepted draft to the release folder.",
                ],
                [
                    "The manifest lists five vertical scenes, one narration track, music, and a caption file.",
                    "The assembly script scales to 1080x1920, applies bounded trims, mixes audio, and exports a draft.",
                    "A duration check routes a 33.8-second result back because the contract requires no more than 32 seconds.",
                ],
                [
                    "The repeated edit can be expressed through a stable manifest or template.",
                    "The team needs reproducible renders and traceable revisions.",
                ],
                [
                    "The creative decision depends on subtle performance judgment that is not encoded in the plan.",
                    "The source media cannot be legally or technically processed by the chosen tool.",
                ],
                [
                    ("Failure signal", "A rerun changes unrelated parts of the video."),
                    ("Repair move", "Pin inputs, settings, and the edit decision list to a run version."),
                    ("Quality evidence", "The render log and media probe match the declared release specification."),
                ],
                [
                    "https://ffmpeg.org/ffmpeg.html",
                    "https://ffmpeg.org/ffmpeg-filters.html",
                    "https://ffmpeg.org/ffprobe.html",
                ],
            ),
            _section(
                "Adding Captions, Effects, and Branding",
                "Captions represent speech and essential audio in time-aligned text. Branding uses controlled typography, colour, logo placement, and tone. Effects should guide attention or clarify change; they are not a substitute for a coherent story. Separate caption text from styling so the same approved content can be exported as WebVTT, platform captions, or burned-in text.",
                "Most short-form video is watched in varied sound and attention conditions. Accurate captions improve access and comprehension, while a consistent safe-area layout prevents text and controls from colliding. Automated transcription is a draft: names, numbers, timing, line breaks, and speaker meaning still require human review.",
                [
                    "Create captions from the approved script or a reviewed transcript.",
                    "Check wording, timing, reading order, line length, and meaningful sound labels.",
                    "Apply brand typography and colours within channel-safe areas.",
                    "Use effects only when they support a story beat or viewer orientation.",
                    "Export a portable caption file and preview the full vertical frame at phone size.",
                ],
                [
                    "The WebVTT file begins with the required header and contains ordered cue timings.",
                    "On-screen keywords complement rather than duplicate the complete caption line.",
                    "The logo and lower-third remain clear of common interface overlays.",
                ],
                [
                    "The transcript can be reviewed against the final audio.",
                    "Brand assets and usage rules are approved and available.",
                ],
                [
                    "The system guesses inaudible speech or decorative text hides the subject.",
                    "A generated logo, typeface, or sound effect has uncertain rights.",
                ],
                [
                    ("Failure signal", "Captions are accurate but unreadable on a phone or out of sync after an edit."),
                    ("Repair move", "Regenerate timings from the final audio and recheck safe area, contrast, and line breaks."),
                    ("Quality evidence", "The final file passes text, timing, contrast, and mobile-preview checks."),
                ],
                [
                    "https://www.w3.org/TR/webvtt1/",
                    "https://developers.google.com/youtube/v3/docs/captions",
                ],
            ),
            _section(
                "Assembling Short-Form Videos",
                "Assembly is the editorial act of making every visual, spoken line, caption, and sound serve one promise. The hook establishes relevance, the body delivers proof through a clear sequence, and the close completes the promise with a proportionate next action. Rhythm comes from information change, not from arbitrary rapid cuts.",
                "An agent can detect missing files, long gaps, repeated shots, or timing mismatches, but it cannot own the final communication judgment. The creator must watch the complete video as a viewer, with sound on and off, and confirm that the story remains understandable, truthful, and appropriately paced.",
                [
                    "Start with the target promise and remove any beat that does not support it.",
                    "Align narration, picture, captions, and sound by function rather than repetition.",
                    "Use visual continuity and clear transitions to preserve orientation.",
                    "Preview from start to finish without stopping, then record only observable issues.",
                    "Apply the smallest revision that fixes the stated issue and rerender.",
                ],
                [
                    "The opening shows the bitter-cup problem while narration names the viewer situation.",
                    "Three proof beats demonstrate variables in the same order as the spoken explanation.",
                    "The close summarises the checklist and invites the viewer to save it.",
                ],
                [
                    "The script, storyboard, media, and audio are approved enough for a complete draft.",
                    "The team can preview on the intended aspect ratio and device.",
                ],
                [
                    "Essential evidence is missing and the edit would disguise that gap.",
                    "The workflow optimises only for cut frequency or novelty.",
                ],
                [
                    ("Failure signal", "The edit is energetic but the viewer cannot restate the three fixes."),
                    ("Repair move", "Restore causal order and remove decorative elements that compete with proof."),
                    ("Quality evidence", "A cold viewer identifies the promise, proof, and next action without explanation."),
                ],
                [
                    "https://ffmpeg.org/ffmpeg.html",
                    "https://www.w3.org/TR/webvtt1/",
                ],
            ),
            _section(
                "Reviewing and Refining with AI",
                "A review agent inspects the draft against a declared rubric and returns evidence, severity, location, and a bounded repair suggestion. It may compare the script to captions, probe the file, detect missing manifest entries, or flag brand and rights questions. It does not give itself permission to approve or publish its own work.",
                "Unstructured feedback such as 'make it more engaging' causes uncontrolled rewrites. An issue register turns observations into reproducible decisions: issue ID, category, evidence, severity, owner, fix, and recheck result. Independent checks reduce the risk that the same assumptions survive from generation into review.",
                [
                    "Run deterministic technical and manifest checks first.",
                    "Review story, claims, captions, rights, privacy, branding, and disclosure separately.",
                    "Record each issue with timecode or asset reference and supporting evidence.",
                    "Assign an owner and apply the smallest controlled change.",
                    "Rerun affected checks and obtain human approval on the complete final preview.",
                ],
                [
                    "The agent flags a caption mismatch at 00:12, a missing rights note for asset S03, and a 1.8-second duration overrun.",
                    "The editor fixes only those items and links the new render to the same run.",
                    "A person confirms the whole video after the automated checks return clear.",
                ],
                [
                    "The rubric, evidence sources, and severity thresholds are explicit.",
                    "A human remains accountable for ambiguous creative and release decisions.",
                ],
                [
                    "The reviewer shares the same hidden context and merely confirms its own output.",
                    "A score is used without evidence, location, or a repair path.",
                ],
                [
                    ("Failure signal", "The system gives a high quality score while required release evidence is missing."),
                    ("Repair move", "Use blocking gates for mandatory fields and evidence-linked findings for judgment."),
                    ("Quality evidence", "Every cleared issue has a recorded recheck and the final approval names a person."),
                ],
                [
                    "https://openai.github.io/openai-agents-js/guides/guardrails/",
                    "https://docs.n8n.io/advanced-ai/examples/human-fallback/",
                ],
            ),
        ],
    ),
    dict(
        num=4,
        code="04",
        title="Automating and Scaling Video Production",
        subtitle="Multi-step video agents | Publishing and scheduling | Performance analysis | Scalable content pipelines",
        weighting="Day 2 afternoon | 2 labs",
        concepts=[
            ("Orchestrator", "The workflow component that routes state between specialist stages and enforces gates."),
            ("Approval token", "A recorded, scoped decision that authorises one release action for one approved package."),
            ("Metric contract", "A definition of the decision, grain, window, numerator, denominator, and exclusions for each KPI."),
            ("Scaling guardrail", "A limit on volume, spend, retries, permissions, or variance that grows with automation."),
        ],
        sections=[
            _section(
                "Building Multi-Step Video Agents",
                "A multi-step video system may use a coordinator plus specialist research, script, asset, edit, review, and release stages. Specialisation is valuable when each role has a distinct tool set and output contract. The coordinator should route state and enforce policies, not rewrite every artifact.",
                "Adding agents increases hand-offs, cost, latency, and opportunities for inconsistent assumptions. Start with one workflow and split a stage only when the separation improves control, parallel work, specialist tooling, or evaluation. Shared run state must distinguish approved artifacts from drafts.",
                [
                    "Define a state machine with permitted transitions and blocking conditions.",
                    "Give each specialist the minimum context and tools required for its stage.",
                    "Validate every hand-off against the shared schema and artifact version.",
                    "Cap iterations and route unresolved work to a rework queue or human owner.",
                    "Trace tool calls, costs, decisions, errors, and approvals under one run ID.",
                ],
                [
                    "HB-001 moves brief_approved -> script_ready -> assets_ready -> draft_ready -> release_ready.",
                    "A rights flag prevents the release stage from running even when all media files exist.",
                    "The coordinator sends the issue back to the asset owner rather than regenerating the script.",
                ],
                [
                    "Specialist roles have distinct contracts, tools, or review criteria.",
                    "The orchestrator can persist state and enforce permitted transitions.",
                ],
                [
                    "One prompt and one tool would solve the bounded task more reliably.",
                    "Agents share unrestricted credentials or can silently overwrite accepted artifacts.",
                ],
                [
                    ("Failure signal", "Agents loop or disagree about which artifact is current."),
                    ("Repair move", "Use a state machine, immutable versions, and one authoritative manifest."),
                    ("Quality evidence", "The complete run can be reconstructed from state transitions and logs."),
                ],
                [
                    "https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/",
                    "https://openai.github.io/openai-agents-js/guides/handoffs/",
                    "https://github.com/n8n-io/n8n-docs/blob/main/docs/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/tools-agent.md",
                ],
            ),
            _section(
                "Publishing and Scheduling Across Platforms",
                "Publishing is an external, high-impact action. The release stage should receive only an approved video, captions, metadata, disclosure decision, rights record, target account, privacy setting, and schedule. The default learning path produces a dry-run request and keeps visibility private until an authorised person reviews platform-specific fields and consents.",
                "Platforms have different permissions, quotas, disclosure fields, and audit requirements. Automating the final click without checking creator information, audience settings, privacy, and synthetic-media disclosure can cause irreversible mistakes. A scoped approval token and idempotency key ensure one approved package produces at most one intended post.",
                [
                    "Validate the release package and platform-specific required fields.",
                    "Query the authorised account or creator settings where the API requires it.",
                    "Show the exact title, description, captions, disclosure, privacy, and schedule to a person.",
                    "Record approval, then initialise one private or scheduled upload with an idempotency key.",
                    "Poll processing status, record the returned post ID, and route errors without duplicate posts.",
                ],
                [
                    "The C436 lab creates a private dry-run package for YouTube and a TikTok request preview.",
                    "The release remains blocked until disclosure, rights, and owner_approval fields are complete.",
                    "The workflow records the intended target and package checksum before any live integration is enabled.",
                ],
                [
                    "The account owner has authorised the app and can preview every required field.",
                    "Private or draft mode, error handling, and duplicate prevention are available.",
                ],
                [
                    "The workflow would post publicly without explicit consent and a complete preview.",
                    "Credentials, disclosure, rights, or platform audit requirements are unresolved.",
                ],
                [
                    ("Failure signal", "A retry produces two uploads or exposes an unreviewed caption."),
                    ("Repair move", "Gate the action with approval plus an idempotency key and reconcile the returned post ID."),
                    ("Quality evidence", "The release log links one approved package to one intended platform action."),
                ],
                [
                    "https://developers.google.com/youtube/v3/docs/videos/insert",
                    "https://developers.google.com/youtube/v3/docs/captions/insert",
                    "https://developers.tiktok.com/doc/content-posting-api-reference-direct-post",
                ],
            ),
            _section(
                "Analysing Performance",
                "Performance analysis starts with a decision and a metric contract. Reach, starts, watch time, average view duration, completion, saves, shares, comments, and downstream actions describe different parts of audience response. The agent should calculate defined metrics at a consistent grain, compare appropriate windows, and separate observation from explanation.",
                "A large view count does not prove that a creative choice caused success. Platform metric definitions and counting rules can change, and small samples are unstable. A useful analysis agent preserves denominators, dates, segment, content version, and data source, then proposes a limited next test instead of declaring a universal rule.",
                [
                    "State the decision and choose one primary metric plus guardrails.",
                    "Validate dates, video IDs, denominators, missing values, and metric definitions.",
                    "Compare like with like and calculate rates at the intended grain.",
                    "Describe observed differences before proposing possible drivers.",
                    "Recommend one controlled creative or workflow change with a measurement window.",
                ],
                [
                    "The Harbour Bean synthetic dataset compares eight posts by hook family and duration.",
                    "The agent calculates completion and save rates from the supplied counts, then flags low-impression rows.",
                    "It recommends testing the strongest clear-promise hook while holding topic and duration band stable.",
                ],
                [
                    "The data source, metric definitions, window, and comparison grain are known.",
                    "A proposed action can be tested and reviewed against guardrails.",
                ],
                [
                    "Denominators are missing or metrics from different platforms are treated as identical.",
                    "A single high-performing post is being treated as causal proof.",
                ],
                [
                    ("Failure signal", "The dashboard ranks videos by a rate calculated from incompatible denominators."),
                    ("Repair move", "Write the metric contract and validate each row before analysis."),
                    ("Quality evidence", "Every recommendation cites a defined metric, segment, window, caveat, and next test."),
                ],
                [
                    "https://developers.google.com/youtube/analytics/reference/reports/query",
                    "https://developers.google.com/youtube/v3/docs/videos",
                ],
            ),
            _section(
                "Scaling Your Video Content Pipeline",
                "Scaling means increasing useful throughput without losing evidence, control, or quality. The team standardises production contracts, templates, reusable agent tools, asset naming, review rubrics, and telemetry. Work is queued and prioritised; capacity and cost budgets are visible; exceptions are handled explicitly.",
                "Volume magnifies small defects. A weak prompt creates many weak scripts, a permissive credential multiplies risk, and a missing rights record blocks an entire catalogue. Scale should follow demonstrated reliability at lower volume. Versioned templates, sampling, canary releases, and stop conditions keep growth reversible.",
                [
                    "Measure baseline lead time, rework, cost, quality findings, and release errors.",
                    "Standardise only stages with stable inputs, outputs, and owner acceptance.",
                    "Introduce queues, concurrency limits, budgets, and priority rules.",
                    "Use canary batches and sample-based human review before increasing volume.",
                    "Monitor drift, rights expiry, tool changes, and incidents; pause when thresholds fail.",
                ],
                [
                    "The team moves from one video to a three-video weekly batch using the same approved production contract.",
                    "Generation is capped per run, every fifth draft receives an additional cold review, and public release stays human-approved.",
                    "A scorecard tracks cycle time, cost per accepted video, rework rate, blocked rights items, and post-release learning.",
                ],
                [
                    "The pilot is reliable, measurable, and recoverable.",
                    "Owners, limits, incident response, and manual fallback are in place.",
                ],
                [
                    "Quality evidence is incomplete or rework already consumes more time than the workflow saves.",
                    "The plan increases permissions or public actions faster than monitoring and review capacity.",
                ],
                [
                    ("Failure signal", "Output volume rises while accepted-video cost and rework also rise."),
                    ("Repair move", "Throttle the queue and fix the earliest stage producing repeated defects."),
                    ("Quality evidence", "Throughput improves while guardrail metrics remain within agreed limits."),
                ],
                [
                    "https://openai.github.io/openai-agents-js/guides/guardrails/",
                    "https://docs.n8n.io/flow-logic/error-handling/",
                ],
            ),
        ],
    ),
]

DAY_THEMES = {
    1: "Design the agent and generate an approved production pack",
    2: "Assemble, review, orchestrate, and plan responsible scale",
}


def SCHEDULE(lab_titles):
    return {
        1: (
            DAY_THEMES[1],
            [
                ("9:30", "9:50", 20, "admin", "Welcome, course introduction, setup, and learning approach"),
                ("9:50", "10:40", 50, "topic", "Topic 1 - Getting Started with Agentic AI for Video (concepts and demonstration)"),
                ("10:40", "10:55", 15, "break", "Tea break"),
                ("10:55", "11:40", 45, "lab", "Hands-on: " + lab_titles([1])),
                ("11:40", "12:30", 50, "lab", "Hands-on: " + lab_titles([2])),
                ("12:30", "13:00", 30, "topic", "Topic 2 - Research and structured production hand-offs"),
                ("13:00", "14:00", 60, "lunch", "Lunch break"),
                ("14:00", "15:00", 60, "topic", "Topic 2 - Scripts, storyboards, visuals, voice, and audio"),
                ("15:00", "15:15", 15, "break", "Tea break"),
                ("15:15", "16:20", 65, "lab", "Hands-on: " + lab_titles([3])),
                ("16:20", "17:40", 80, "lab", "Hands-on: " + lab_titles([4])),
                ("17:40", "18:30", 50, "recap", "Day 1 production-pack review, troubleshooting, and recap"),
            ],
        ),
        2: (
            DAY_THEMES[2],
            [
                ("9:30", "9:45", 15, "admin", "Day 1 checkpoint restore and Day 2 briefing"),
                ("9:45", "10:35", 50, "topic", "Topic 3 - Automated editing, captions, assembly, and quality gates"),
                ("10:35", "10:50", 15, "break", "Tea break"),
                ("10:50", "11:50", 60, "lab", "Hands-on: " + lab_titles([5])),
                ("11:50", "13:00", 70, "lab", "Hands-on: " + lab_titles([6])),
                ("13:00", "14:00", 60, "lunch", "Lunch break"),
                ("14:00", "15:10", 70, "topic", "Topic 4 - Orchestration, publishing controls, analytics, and scale"),
                ("15:10", "15:25", 15, "break", "Tea break"),
                ("15:25", "16:15", 50, "lab", "Hands-on: " + lab_titles([7])),
                ("16:15", "17:45", 90, "lab", "Hands-on: " + lab_titles([8])),
                ("17:45", "18:30", 45, "recap", "Integrated workflow demonstration, next steps, and course recap"),
            ],
        ),
    }


COURSE_OVERVIEW = dict(
    section_title="Agentic Video Production Foundations",
    concepts_title="What Makes a Workflow Agentic",
    concepts=[
        ("Goal and state", "The system knows the desired outcome, accepted artifacts, current stage, and unresolved work."),
        ("Reasoning and routing", "A model chooses among bounded next actions while deterministic rules enforce known constraints."),
        ("Tools and contracts", "Every capability has typed inputs, portable outputs, permissions, budgets, and failure behavior."),
        ("Evidence and control", "Logs, provenance, validators, approvals, and stop conditions keep the work reviewable."),
    ],
    framework_title="The C436 Agent Loop",
    framework=[
        ("1 | Observe", "Read the approved brief, state, manifest, and current evidence."),
        ("2 | Plan", "Choose the next smallest action that advances a completion condition."),
        ("3 | Act", "Call one allowed tool with structured inputs and bounded retries."),
        ("4 | Inspect", "Validate the artifact, provenance, cost, and quality evidence."),
        ("5 | Decide", "Accept, revise, retry within limits, or escalate to a named owner."),
        ("6 | Record", "Persist the new state and an auditable event before continuing."),
    ],
    statement=dict(
        headline="Autonomy is a design variable, not the goal.",
        body="Use deterministic automation for known operations, model judgment for bounded choices, and human approval for consequential actions.",
        kicker="CORE PRINCIPLE",
    ),
    pillars_title="The Connected Harbour Bean Build",
    pillars=[
        ("Design", ["Production contract", "Autonomy matrix", "Workflow map"]),
        ("Create", ["Research register", "Timed script", "Asset manifest"]),
        ("Assemble", ["Edit decision list", "Captions", "Vertical draft"]),
        ("Control", ["Issue register", "Release package", "Approval record"]),
        ("Learn", ["Metric contract", "Synthetic analysis", "Scaling scorecard"]),
    ],
    arc_title="How Every Lab Progresses",
    arc=[
        "Start from an approved checkpoint and a named output contract.",
        "Execute bounded steps using supplied synthetic data and placeholder secrets.",
        "Run an observable 'Test It' check and record evidence.",
        "Save the checkpoint so the next lab can continue without regeneration.",
        "Reflect on which choices should remain deterministic, model-led, or human-approved.",
    ],
    deep_dives=[
        dict(
            title="Autonomy Matrix",
            kicker="CONTROL DESIGN",
            items=[
                ("Deterministic", "Validation, naming, file movement, media probing, arithmetic, and schema checks."),
                ("Model-assisted", "Idea clustering, script alternatives, shot suggestions, and evidence-linked issue drafts."),
                ("Human-approved", "Claims, rights, likeness, brand exceptions, final edit, and release actions."),
                ("Prohibited by default", "Unreviewed public posts, secret exposure, identity imitation, and unsupported claims."),
            ],
        ),
        dict(
            title="The Production Contract",
            kicker="STRUCTURED INPUT",
            items=[
                ("Purpose", "Audience, channel, message, desired viewer action, and success decision."),
                ("Evidence", "Approved facts, source register, unknowns, and permitted inference."),
                ("Creative constraints", "Duration, aspect ratio, tone, brand, continuity, and prohibited content."),
                ("Operational limits", "Tools, permissions, budgets, retries, owner, and finish condition."),
            ],
        ),
        dict(
            title="Run Evidence",
            kicker="OBSERVABILITY",
            items=[
                ("Identity", "Run ID, job ID, artifact version, prompt version, and manifest checksum."),
                ("Actions", "Tool name, input reference, output reference, time, status, and error."),
                ("Controls", "Validation result, issue ID, approval scope, and decision owner."),
                ("Resources", "Latency, generation count, cost estimate, and retry count."),
            ],
        ),
    ],
)

LG_INTRO = (
    "This Learner Guide accompanies Agentic AI for Video Creation (C436). It is a "
    "self-contained study text and practical reference for designing, generating, "
    "assembling, reviewing, and scaling a controlled short-form video workflow."
)
LG_INTRO2 = (
    "The four topics and eight connected labs follow one synthetic Harbour Bean "
    "campaign. Work in order and retain each checkpoint: later labs consume the "
    "production contracts, manifests, decisions, and evidence created earlier."
)

LG_SETUP = dict(
    needs=[
        "A Windows or macOS laptop with a modern browser and permission to create local folders.",
        "Access to an approved AI assistant such as ChatGPT or Claude; do not paste confidential data into an unapproved service.",
        "An n8n Cloud workspace or trainer-provided n8n instance for importing the supplied workflow templates.",
        "FFmpeg and FFprobe on PATH. On Windows, install with 'winget install --id Gyan.FFmpeg -e'; on macOS, use 'brew install ffmpeg'. Reopen the terminal and verify both commands.",
        "Optional approved accounts for a video generator and voice service; supplied placeholder assets keep every lab completable without paid generation.",
        "The repository's labs/assets folder, which contains the synthetic brief, templates, sample analytics, manifests, and workflow JSON.",
    ],
    verify_text=(
        "Confirm that the course files are readable, n8n opens, and the media tools "
        "return a version. Never place real secret values in a prompt, lab file, "
        "screenshot, or public repository."
    ),
    verify_code=(
        "ffmpeg -version\n"
        "ffprobe -version\n"
        "# In n8n, open Workflows > Create Workflow and confirm Import from File is available."
    ),
    conventions=[
        "Replace placeholders such as <RUN_ID> or <API_KEY> only in an approved credential store or local environment.",
        "Use the supplied synthetic Harbour Bean data. Do not add real customer, employee, creator, or account data.",
        "Keep public publishing disabled. The labs produce private or dry-run release packages for review.",
        "Save accepted artifacts under the named checkpoint path before starting the next lab.",
        "If an optional generation service is unavailable, use the supplied placeholder media and continue the full control workflow.",
        "For platform request design, use the current official YouTube Data API documentation at https://developers.google.com/youtube/v3/docs/videos and TikTok Content Posting API documentation at https://developers.tiktok.com/doc/content-posting-api-get-started; the labs keep every request non-executing.",
    ],
)

LAB_NOTE = (
    "Use only the supplied synthetic campaign data and approved accounts. Store "
    "secrets in managed credentials, keep public publishing disabled, and obtain "
    "human approval before any external release action."
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
                "Approved production contract, autonomy matrix, and workflow map.",
                "Source register, script, storyboard, asset manifest, and provenance notes.",
                "Edit decision list, caption file, technical probe, draft, and issue register.",
                "Release package, approval record, metric contract, analysis, and scaling scorecard.",
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
    "Rerun the eight labs from the saved checkpoints and explain every state transition.",
    "Replace one mock tool with an approved live integration while preserving the same contract, limits, and evidence.",
    "Add three representative test jobs, including one missing-input case and one tool-failure case.",
    "Pilot with private outputs, review rework and cost evidence, and scale only after the guardrails remain stable.",
    "Review official tool and platform documentation before adapting any live API or interface shown in this guide.",
    "Recheck YouTube upload/privacy requirements at https://developers.google.com/youtube/v3/guides/uploading_a_video and TikTok Direct Post requirements at https://developers.tiktok.com/doc/content-posting-api-reference-direct-post before any authorised implementation.",
]

LG_GLOSSARY = [
    ("Agent", "A model-led system that pursues a bounded goal through instructions, tools, state, and a control loop."),
    ("Agent loop", "The repeated observe, plan, act, inspect, decide, and record cycle."),
    ("Approval token", "A recorded decision authorising one scoped action for one named artifact or package."),
    ("Asset manifest", "The authoritative inventory of media files, prompts, versions, provenance, rights notes, and status."),
    ("Autonomy matrix", "A table classifying tasks as deterministic, model-assisted, human-approved, or prohibited."),
    ("Checkpoint", "A saved accepted state from which the workflow can safely resume."),
    ("Continuity bible", "Stable visual and audio constraints reused across generated scenes."),
    ("Edit decision list", "A structured description of timeline order, trims, overlays, transitions, and audio."),
    ("Guardrail", "A rule or check that constrains inputs, tool calls, outputs, permissions, or actions."),
    ("Human-in-the-loop", "A workflow point where a person reviews evidence and approves, edits, rejects, or stops an action."),
    ("Idempotency key", "A stable identifier used to prevent a retry from creating a duplicate external action."),
    ("Metric contract", "A precise definition of a measure, including grain, period, numerator, denominator, and exclusions."),
    ("Orchestrator", "The component that routes work between stages and enforces state transitions and gates."),
    ("Production contract", "A structured brief containing purpose, evidence, constraints, deliverables, tools, limits, and finish conditions."),
    ("Provenance", "Recorded information about where an artifact came from and how it was created or changed."),
    ("Run ID", "A unique identifier linking the events and artifacts of one workflow execution."),
    ("Schema", "A definition of required fields, data types, allowed values, and relationships."),
    ("Tool boundary", "The documented inputs, outputs, permissions, limits, and failure behavior of a capability."),
    ("WebVTT", "A UTF-8 time-aligned text format commonly used for web video captions and subtitles."),
]

NEXT_STEPS = dict(
    title="Continue Building Safely",
    items=[
        "Replace one mock stage at a time and retain its contract and fallback.",
        "Create test jobs for missing inputs, malformed output, tool failure, and denied approval.",
        "Keep publishing private until platform permissions and an accountable release owner are confirmed.",
        "Measure accepted output, rework, cost, latency, and incidents before increasing volume.",
    ],
)

THANK_YOU = dict(
    body=(
        "You can now design and operate a bounded video-production agent from "
        "approved brief to evidence-led scaling plan."
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
    ("1.0", VERSION_DATE, "Initial aligned release of the C436 deck, Learner Guide, Lesson Plan, and eight connected labs.", TRAINER),
]
