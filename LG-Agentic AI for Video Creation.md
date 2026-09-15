# Agentic AI for Video Creation
**Course Code:** C436  
**Version:** v2.0  
## Learning outcomes
- LO1: Develop an editing strategy and work plan in Hermes Agent using MiniMax M3, structured video prompts and governed tool selection.
- LO2: Create and customise an evidence-backed video with Hermes skills, Remotion, Manim, Higgsfield-compatible requests and deterministic media checks.
- LO3: Orchestrate research, production, review and YouTube release agents through a durable Kanban board and controlled scheduled publishing.

## End-to-end architecture
1. Hermes Desktop setup and MiniMax-M3 model verification
2. FRAME-CUT prompt and timed shot-plan validation
3. Remotion, Manim, Higgsfield and FFmpeg tool routing
4. Reusable brand, tone and style video skill
5. Research, video, review and upload agent contracts
6. Durable Kanban dependencies and approval hash
7. Private YouTube upload and paused scheduled release

## Topic 1: Hermes Agent Setup, MiniMax M3 and Video Prompt Engineering

LO1 - configure Hermes safely and convert creative intent into a machine-checkable video plan

### Hermes Desktop runtime boundary

**Mechanism:** Download installer → Verify platform → Complete setup → Run diagnostics  
**Fields:** platform, installer_source, hermes_version, doctor_status  
**Measure:** setup pass = required diagnostics passed / required diagnostics  
**Control:** Use the official desktop page and stop when hermes doctor reports a failed dependency.  
**Evidence:** setup-evidence.json records official source, version and diagnostic status.

### Shared desktop and CLI state

**Mechanism:** Open Desktop → Inspect profile → Open terminal → Compare configuration  
**Fields:** profile, config_path, session_id, skill_root  
**Measure:** state consistency = matching settings / checked settings  
**Control:** Name the active profile and compare provider, model and skill directory before production.  
**Evidence:** profile-check.json shows the same provider and model on both surfaces.

### MiniMax M3 provider contract

**Mechanism:** Create account → Create API key → Configure provider → Select model  
**Fields:** provider, base_url, model, credential_ref  
**Measure:** model handshake pass = successful tool-capable response  
**Control:** Use provider minimax with model MiniMax-M3 and verify the returned model identifier.  
**Evidence:** model-check.json records MiniMax-M3 without recording the key.

### Trial and quota verification

**Mechanism:** Open live offer → Read terms → Record expiry → Set budget  
**Fields:** offer_seen_at, trial_end, quota, fallback_model  
**Measure:** budget headroom = available quota - reserved quota  
**Control:** Treat the offer as time-sensitive; record live terms at sign-up and prepare a fallback.  
**Evidence:** trial-checklist.md contains observed terms, date and learner decision.

### Credential isolation

**Mechanism:** Create secret → Store securely → Reference variable → Redact evidence  
**Fields:** secret_name, scope, provider, rotation_due  
**Measure:** secret exposure count = 0  
**Control:** Keep secrets in Hermes credential/config storage and publish placeholders only.  
**Evidence:** secret scan reports zero live tokens in the lab package.

### Model capability routing

**Mechanism:** Classify task → Check modality → Choose M3 → Choose media tool  
**Fields:** task_type, input_modality, model_id, tool_id  
**Measure:** routing yield = accepted outputs / routed calls  
**Control:** Use M3 for reasoning and tool orchestration; use a video renderer or generator for media.  
**Evidence:** tool-routing.csv links every task to a capable model or tool.

### FRAME-CUT prompt contract

**Mechanism:** Define FRAME → Add CUT controls → Require schema → Validate output  
**Fields:** format_role_assets, motion_environment, continuity_unwanted, technical_output  
**Measure:** prompt validity = required fields present / required fields  
**Control:** Use FRAME-CUT and validate the returned shot plan before generation.  
**Evidence:** prompt-contract.json passes schema and duration checks.

### Format and finish

**Mechanism:** Choose channel → Set duration → Set aspect → Set delivery codec  
**Fields:** channel, duration_s, aspect_ratio, codec  
**Measure:** delivery compliance = passed technical fields / required fields  
**Control:** Freeze delivery properties before shot generation and assembly.  
**Evidence:** video-spec.json contains approved format and finish values.

### Role, references and assets

**Mechanism:** Assign role → Attach brief → Register sources → List assets  
**Fields:** role, brief_uri, source_ids, asset_ids  
**Measure:** asset coverage = registered assets / required assets  
**Control:** Limit reasoning to named references and a manifest of authorized assets.  
**Evidence:** asset-manifest.csv resolves every asset and source identifier.

### Action, motion and environment

**Mechanism:** Name subject → Choose action → Choose camera → Lock environment  
**Fields:** subject, action, camera_motion, environment  
**Measure:** usable shot rate = accepted shots / attempts  
**Control:** Use one dominant subject action and one camera move per timed shot.  
**Evidence:** shot-list.json shows one action-motion pair per shot.

### Continuity and negative constraints

**Mechanism:** Lock identity → Lock palette → List invariants → Reject drift  
**Fields:** continuity_token, palette_hex, must_keep, must_avoid  
**Measure:** continuity defects per reviewed shot  
**Control:** Reuse continuity tokens and compare keyframes against explicit invariants.  
**Evidence:** continuity-review.json records deviations and acceptance.

### Structured shot-plan output

**Mechanism:** Request JSON → Parse response → Check timeline → Approve plan  
**Fields:** shot_id, start_s, end_s, prompt  
**Measure:** timeline variance = planned duration - target duration  
**Control:** Require strict JSON and fail on gaps, overlaps or unknown fields.  
**Evidence:** shot-plan.json totals the target duration with no overlap.

### Simple video agent loop

**Mechanism:** Receive brief → Plan shots → Call tool → Inspect result  
**Fields:** run_id, plan_hash, tool_call, result_uri  
**Measure:** first-pass completion rate  
**Control:** Set one render attempt, one review pass and an explicit repair decision.  
**Evidence:** run-ledger.json contains the plan, call, result and stop reason.

### Cost, latency and stop rules

**Mechanism:** Estimate calls → Reserve retries → Set ceiling → Stop or escalate  
**Fields:** estimated_cost, max_attempts, timeout_s, stop_reason  
**Measure:** budget variance = actual cost - approved cost  
**Control:** Cap attempts and require a human decision before additional paid generation.  
**Evidence:** budget-ledger.csv reconciles attempts, latency and cost.

## Topic 2: Video Tools, Hermes Skills and Custom Brand Production

LO2 - create a technically valid branded video by combining agent reasoning with specialist media tools

### Tool versus skill decision

**Mechanism:** Identify capability → Assess auth → Choose tool → Wrap procedure  
**Fields:** capability, auth_mode, tool_or_skill, owner  
**Measure:** integration fit = satisfied requirements / requirements  
**Control:** Use a tool for precise integrated execution and a skill for repeatable instructions plus scripts.  
**Evidence:** decision-record.md states why each capability is a tool or skill.

### Hermes skill anatomy

**Mechanism:** Create directory → Write frontmatter → Add procedure → Test invocation  
**Fields:** name, description, version, skill_dir  
**Measure:** skill test pass = expected artifacts produced  
**Control:** Describe the exact trigger and include deterministic verification commands.  
**Evidence:** SKILL.md and test transcript show correct activation.

### Skill discovery and progressive loading

**Mechanism:** List skills → Search catalog → View selected skill → Invoke task  
**Fields:** skill_name, category, file_path, task  
**Measure:** context efficiency = loaded relevant files / loaded files  
**Control:** Search first, view the selected skill, then load only referenced resources.  
**Evidence:** skill-usage.json records the selected skill and resources.

### Remotion composition contract

**Mechanism:** Define composition → Bind props → Preview frames → Render MP4  
**Fields:** composition_id, fps, duration_frames, input_props  
**Measure:** duration seconds = duration frames / fps  
**Control:** Derive frames from duration and validate width, height, fps and codec after render.  
**Evidence:** remotion-render.json and ffprobe.json agree with the contract.

### Manim explanatory scene

**Mechanism:** Define objects → Stage transforms → Render scene → Composite clip  
**Fields:** scene_class, resolution, frame_rate, output_file  
**Measure:** animation timing variance  
**Control:** Bind labels and values to the approved evidence model and review rendered frames.  
**Evidence:** manim-scene.py and contact sheet prove the intended transformation.

### Higgsfield shot request

**Mechanism:** Select model → Attach reference → Write motion prompt → Review output  
**Fields:** model, reference_uri, motion_prompt, generation_id  
**Measure:** accepted clip yield = approved clips / generated clips  
**Control:** Create a request preview first; call the service only with approved assets and quota.  
**Evidence:** higgsfield-request.json records prompt, references and review status.

### FFmpeg deterministic assembly

**Mechanism:** Normalize media → Build timeline → Mix audio → Encode master  
**Fields:** filter_complex, video_codec, audio_codec, pix_fmt  
**Measure:** render success = valid masters / render attempts  
**Control:** Normalize every source before concat and probe the final container.  
**Evidence:** ffprobe.json confirms H.264, AAC, dimensions, fps and duration.

### Tool permission boundary

**Mechanism:** Declare capability → Set working root → Request approval → Record result  
**Fields:** allowed_paths, network_scope, side_effect, approval_id  
**Measure:** unauthorized side effects = 0  
**Control:** Scope paths and accounts; separate preview from consequential execution.  
**Evidence:** tool-policy.yaml and audit log show bounded operations.

### Asset provenance and checksum

**Mechanism:** Register source → Record license → Compute hash → Freeze version  
**Fields:** asset_id, source_uri, rights_status, sha256  
**Measure:** manifest integrity = verified hashes / manifest rows  
**Control:** Bind approval to cryptographic hashes and immutable versions.  
**Evidence:** asset-manifest.csv verifies rights and hashes.

### Brand token system

**Mechanism:** Extract identity → Set palette → Set typography → Set motion rules  
**Fields:** logo_uri, palette_hex, font_stack, motion_style  
**Measure:** brand compliance = passed checks / applicable checks  
**Control:** Store editable brand tokens and reference them from the video skill.  
**Evidence:** brand-profile.yaml and frame samples pass the checklist.

### Tone and style controls

**Mechanism:** Define audience → Set voice → Set pacing → Define exclusions  
**Fields:** audience, tone, words_per_min, style_avoid  
**Measure:** tone adherence score  
**Control:** Use descriptive attributes and exclusions, not living-artist imitation.  
**Evidence:** review rubric records tone, pacing and originality evidence.

### Custom brand-video skill

**Mechanism:** Write skill → Bundle scripts → Add templates → Run acceptance test  
**Fields:** skill_name, script_path, template_path, output_contract  
**Measure:** repeatability = matching outputs / repeated runs  
**Control:** Use Hermes template variables and explicit inputs, outputs and verification.  
**Evidence:** custom skill produces the expected video and evidence on a clean run.

### Technical video quality gate

**Mechanism:** Probe container → Inspect frames → Check captions → Gate master  
**Fields:** width, height, avg_frame_rate, duration_s  
**Measure:** technical checks passed / technical checks  
**Control:** Fail closed on missing streams, wrong bounds or unreadable captions.  
**Evidence:** technical-qc.json and contact sheet show observed values.

### Repair and versioned evidence

**Mechanism:** Open finding → Assign repair → Render version → Re-test scope  
**Fields:** finding_id, severity, asset_version, resolution  
**Measure:** repair effectiveness = closed findings / reopened findings  
**Control:** Write a new immutable version and rerun every affected check.  
**Evidence:** repair-log.json links finding, change, hash and re-test.

## Topic 3: Multi-Agent Kanban, YouTube Release and Scheduled Publishing

LO3 - operate a durable role-based production system with review, release and scheduling safeguards

### Agent role contract

**Mechanism:** Define goal → Limit tools → Name output → Set finish rule  
**Fields:** agent_name, allowed_tools, deliverable, done_when  
**Measure:** role completeness = required fields / required fields  
**Control:** Give every agent one owned deliverable and one measurable completion rule.  
**Evidence:** agent-contracts.yaml validates all four specialist roles.

### Research agent

**Mechanism:** Read brief → Retrieve sources → Score evidence → Handoff claims  
**Fields:** research_task, source_ids, claim_ids, handoff_status  
**Measure:** claim coverage = sourced claims / factual claims  
**Control:** Require retrievable URLs, bounded excerpts and explicit limitations.  
**Evidence:** research-handoff.json contains approved sources and claim IDs.

### Video production agent

**Mechanism:** Read approved claims → Create shot plan → Invoke skills → Return master  
**Fields:** claim_ids, shot_plan, skill_names, master_hash  
**Measure:** production acceptance = passed render checks / checks  
**Control:** Provide immutable research input and require the custom brand-video skill.  
**Evidence:** video-handoff.json references approved claims and master hash.

### Independent review agent

**Mechanism:** Inspect evidence → Score rubric → Create findings → Request decision  
**Fields:** master_hash, rubric_version, findings, qa_status  
**Measure:** weighted review score and unresolved high count  
**Control:** Use an independent context and forbid approval authority in the reviewer role.  
**Evidence:** review-handoff.json contains timecoded findings and QA status.

### Upload agent

**Mechanism:** Verify approval → Build metadata → Upload private → Record video ID  
**Fields:** approval_hash, privacy_status, synthetic_media, video_id  
**Measure:** upload reconciliation = one video ID per idempotency key  
**Control:** Default to private and verify the current master hash immediately before upload.  
**Evidence:** upload-receipt.json records privacy, disclosure and returned video ID.

### Delegation context contract

**Mechanism:** Package context → Dispatch child → Receive summary → Verify artifact  
**Fields:** goal, context, paths, acceptance  
**Measure:** handoff pass rate = accepted handoffs / handoffs  
**Control:** Include exact paths, inputs, constraints and tests in every delegation context.  
**Evidence:** delegation-log.json records prompt, agent and verified result.

### Parallel work and join

**Mechanism:** Find independent tasks → Dispatch batch → Track results → Join after checks  
**Fields:** task_ids, dependencies, result_refs, join_status  
**Measure:** elapsed reduction with zero skipped dependencies  
**Control:** Parallelize only independent work and join on explicit verified artifacts.  
**Evidence:** join-ledger.json shows all required parents complete.

### Durable Hermes Kanban

**Mechanism:** Create tasks → Assign profiles → Link dependencies → Run dispatcher  
**Fields:** task_id, assignee, status, parent_ids  
**Measure:** flow time = done_at - created_at  
**Control:** Use Kanban for cross-agent work that must survive restarts and human pauses.  
**Evidence:** kanban-export.json shows the full dependency chain and statuses.

### Kanban status and circuit breaker

**Mechanism:** Move to ready → Run worker → Request review → Block or complete  
**Fields:** status, attempt, failure_class, reviewer  
**Measure:** retry recovery and repeated-failure count  
**Control:** Cap attempts, require contract verification and block repeated failures for intervention.  
**Evidence:** task history shows checkpoints, review and final evidence.

### Human approval with payload hash

**Mechanism:** Freeze package → Compute hash → Request approval → Recheck before upload  
**Fields:** approval_id, payload_hash, reviewer, decision  
**Measure:** approval integrity = approved hash equals current hash  
**Control:** Bind the named decision to the immutable release package hash.  
**Evidence:** approval-ledger.json proves reviewer, time, decision and hash.

### YouTube videos.insert contract

**Mechanism:** Authorize OAuth → Set snippet → Set status → Upload media  
**Fields:** snippet.title, status.privacyStatus, status.containsSyntheticMedia, media_path  
**Measure:** metadata completeness and processing success  
**Control:** Confirm channel identity, default private and include applicable synthetic-media disclosure.  
**Evidence:** request-preview.json and private upload receipt match the approved package.

### Publishing idempotency

**Mechanism:** Create publish key → Check prior result → Attempt upload → Commit external ID  
**Fields:** idempotency_key, channel_id, video_id, published_at  
**Measure:** duplicate publish rate = 0  
**Control:** Reconcile the prior key and video ID before any retry.  
**Evidence:** publication-ledger.csv contains one committed ID per key.

### Hermes cron job contract

**Mechanism:** Write self-contained prompt → Attach skills → Create schedule → Inspect next run  
**Fields:** job_name, schedule, skills, delivery  
**Measure:** schedule validity and successful dry run  
**Control:** Put all required paths, gates and stop rules in the job prompt; attach skills explicitly.  
**Evidence:** cron-preview.json records schedule, next run and paused state.

### Scheduled release operations

**Mechanism:** Keep job paused → Trigger dry run → Review output → Enable cadence  
**Fields:** paused, last_run, next_run, owner  
**Measure:** on-time success rate with zero unauthorized posts  
**Control:** Schedule preparation and private upload only; require approval before public visibility.  
**Evidence:** operations-ledger.csv records each run, outcome and owner decision.

## Labs

### Lab 01: Set Up Hermes Desktop and Connect MiniMax M3

Install Hermes Desktop from the official source, configure the MiniMax provider for MiniMax-M3 and prove a tool-capable model handshake without exposing a credential.

- Folder: `labs/lab-01-setup-hermes-and-connect-minimax-m3/`
- Stages: Download official installer, Complete Hermes setup, Configure MiniMax-M3, Run hermes doctor, Verify model response, Redact evidence
- Prompt resources: `AI-PROMPTS.md` and `AI-PROMPTS.pdf`
- Acceptance: Hermes launches; the configured provider is minimax; the model is MiniMax-M3; hermes doctor has no blocking failure; published evidence contains placeholders only.

### Lab 02: Prompt Hermes to Create a Simple Video

Use a copy-ready Hermes prompt to convert a supplied 15-second brief into a validated shot plan and deterministic preview video.

- Folder: `labs/lab-02-prompt-hermes-to-create-a-simple-video/`
- Stages: Open project folder, Submit bounded prompt, Validate shot plan, Run preview renderer, Probe MP4, Record evidence
- Prompt resources: `AI-PROMPTS.md` and `AI-PROMPTS.pdf`
- Acceptance: The shot plan is valid JSON, totals 15 seconds, uses only supplied assets, and the generated MP4 passes dimensions, codec and duration checks.

### Lab 03: Engineer Video Prompts with FRAME-CUT

Transform a vague creative request into portable shot prompts using the FRAME-CUT framework and evaluate them with a deterministic rubric.

- Folder: `labs/lab-03-engineer-video-prompts-with-frame-cut/`
- Stages: Diagnose vague prompt, Complete FRAME fields, Complete CUT fields, Generate shot JSON, Score rubric, Repair one defect
- Prompt resources: `AI-PROMPTS.md` and `AI-PROMPTS.pdf`
- Acceptance: Every shot has all FRAME-CUT fields, one dominant action, one camera move, explicit continuity and negative constraints, and a measurable output check.

### Lab 04: Install Video Tools and Hermes Skills

Create a governed tool registry and install learner-safe Hermes skills for Remotion, Manim, Higgsfield request preparation and FFmpeg verification.

- Folder: `labs/lab-04-install-video-tools-and-skills/`
- Stages: Inventory local tools, Search Hermes skills, Install or create skills, Run smoke tests, Record permissions, Choose fallback
- Prompt resources: `AI-PROMPTS.md` and `AI-PROMPTS.pdf`
- Acceptance: The registry records capability, installation state, auth mode, side effects and fallback; every supplied SKILL.md passes frontmatter and path checks.

### Lab 05: Create a Custom Branded Video Skill

Turn brand, tone and style rules into a reusable Hermes skill, render a custom video and verify the output against brand and technical evidence.

- Folder: `labs/lab-05-create-custom-branded-video-skill/`
- Stages: Approve brand profile, Create SKILL.md, Bind templates, Render video, Review frames, Version evidence
- Prompt resources: `AI-PROMPTS.md` and `AI-PROMPTS.pdf`
- Acceptance: The custom skill is discoverable, uses relative or Hermes template paths, creates an MP4, passes the technical probe and meets every required brand token.

### Lab 06: Build the Multi-Agent Video Workflow

Define and simulate four isolated Hermes roles for research, video creation, independent review and approved YouTube upload.

- Folder: `labs/lab-06-build-multi-agent-video-workflow/`
- Stages: Define role contracts, Package context, Delegate research, Delegate production, Request review, Gate uploader
- Prompt resources: `AI-PROMPTS.md` and `AI-PROMPTS.pdf`
- Acceptance: All roles have bounded tools and outputs; the reviewer is independent; upload is blocked until all parent evidence and the current approval hash pass.

### Lab 07: Orchestrate Kanban Review and YouTube Upload

Create a durable Hermes Kanban dependency chain, review the approved video, and prepare or execute a private YouTube upload with explicit human authorization.

- Folder: `labs/lab-07-orchestrate-kanban-review-and-youtube-upload/`
- Stages: Create board tasks, Assign profiles, Link dependencies, Request review, Approve exact hash, Upload private
- Prompt resources: `AI-PROMPTS.md` and `AI-PROMPTS.pdf`
- Acceptance: The Kanban graph has no missing dependency; review is required; the request points to the approved master; privacy is private; no credential is present in artifacts.

### Lab 08: Schedule Controlled Video Publishing with Hermes Cron

Create a paused Hermes cron job that prepares a release from a self-contained prompt, dry-run it, and enable a cadence only after evidence review.

- Folder: `labs/lab-08-schedule-controlled-video-publishing/`
- Stages: Write self-contained job, Attach video skill, Create paused cron, Trigger dry run, Inspect next run, Approve enablement
- Prompt resources: `AI-PROMPTS.md` and `AI-PROMPTS.pdf`
- Acceptance: The schedule and timezone are explicit, the prompt is self-contained, the custom skill is attached, the job begins paused, and the dry run cannot publish an unapproved or duplicate video.

## References
- [Official course page](https://www.tertiarycourses.com.sg/agentic-ai-for-video-creation.html) — Course identity, duration and outcomes
- [Hermes Desktop](https://hermes-agent.nousresearch.com/desktop) — Official desktop installer and supported operating systems
- [Hermes Agent installation](https://hermes-agent.nousresearch.com/docs/getting-started/installation) — Desktop and CLI installation plus diagnostic commands
- [Hermes model configuration](https://hermes-agent.nousresearch.com/docs/user-guide/configuring-models) — Provider, model and auxiliary-task configuration
- [MiniMax M3](https://www.minimax.io/models/text/m3) — Current MiniMax-M3 model identifier and agentic capabilities
- [Hermes skills](https://hermes-agent.nousresearch.com/docs/guides/work-with-skills) — Skill discovery, invocation and custom SKILL.md structure
- [Hermes delegation](https://hermes-agent.nousresearch.com/docs/guides/delegation-patterns) — Isolated subagents, explicit context and parallel work
- [Hermes Kanban](https://hermes-agent.nousresearch.com/docs/user-guide/features/kanban) — Durable multi-agent task dependencies and review states
- [Hermes scheduled tasks](https://hermes-agent.nousresearch.com/docs/user-guide/features/cron) — Cron jobs, attached skills and fresh-session behavior
- [Remotion documentation](https://www.remotion.dev/docs) — Code-driven video compositions and rendering
- [Manim documentation](https://docs.manim.community/) — Programmatic explanatory animation
- [Higgsfield](https://higgsfield.ai/) — Generative video shot production; verify current account and quota terms
- [YouTube videos.insert](https://developers.google.com/youtube/v3/docs/videos/insert) — OAuth upload, snippet and status fields
- AI Video Prompting: reference/AI Video Prompting.pdf — Shot grammar, camera movement and continuity patterns
- Hermes Agent The Complete Developers: reference/Hermes Agent The Complete Developers.pdf — Supplied reference for agent architecture, tools, memory and orchestration
