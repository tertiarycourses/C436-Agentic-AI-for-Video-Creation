"""Topic 2 labs: video tools, Hermes skills and custom brand production.

Lab bodies live in labs/lab-NN-<slug>/. These entries are the single source for
the deck, Lesson Plan and Learner Guide and must stay aligned with them.
"""

DOMAIN2 = [
    dict(
        num=4,
        topic=2,
        title="Install Video Tools and Hermes Skills",
        objective="LO2: build a governed tool registry and install learner-safe skills with recorded permissions and fallbacks",
        duration=60,
        goal="Establish which capability is a tool, which is a skill, and what each is permitted to do.",
        desc=(
            "You will inventory the local media tools, search the Hermes skill "
            "catalogue, install or create skills for Remotion, Manim, Higgsfield "
            "request preparation and FFmpeg verification, run a smoke test on each, "
            "and record the authentication mode, side effects and fallback for every "
            "entry in the registry."
        ),
        build="A tool-routing.json registry with skill-smoke-test.json evidence.",
        services="Hermes skills, Remotion, Manim, Higgsfield request preview, FFmpeg",
        prerequisites=[
            "Complete Lab 3 so a validated prompt pack exists to route.",
            "Open labs/lab-04-install-video-tools-and-skills/ as the current Hermes project.",
            "Confirm FFmpeg and FFprobe return a version on PATH.",
        ],
        workflow=[
            "Inventory the local tools",
            "Search the Hermes skills",
            "Install or create the skills",
            "Run the smoke tests",
            "Record the permissions",
            "Choose the fallbacks",
        ],
        steps=[
            (
                "Inventory the locally available media tools and record which are installed",
                "ffmpeg -version",
            ),
            (
                "Search the Hermes skill catalogue before loading anything, then view only the selected skill",
                "",
            ),
            (
                "Install or create the supplied skills and check each SKILL.md frontmatter and paths",
                "",
            ),
            (
                "Run a smoke test per skill and confirm the expected artifacts are produced",
                "",
            ),
            (
                "Record capability, installation state, authentication mode and side effects in the registry",
                "",
            ),
            (
                "Prepare the Higgsfield request as a preview only, with no account or quota consumed",
                "",
            ),
            (
                "Choose a documented fallback per capability, then run the verifier and retain the PASS output",
                "python3 verify.py",
            ),
        ],
        test=(
            "verify.py must print PASS Lab 04. The registry records capability, "
            "installation state, auth mode, side effects and fallback, and every "
            "supplied SKILL.md passes its frontmatter and path checks."
        ),
        checkpoint=(
            "tool-routing.json governs which tool or skill each later production task "
            "is permitted to call."
        ),
        troubleshooting=[
            (
                "A skill is not discovered when its trigger is used.",
                "Check the YAML frontmatter, the directory name and the SKILL.md filename, then restart skill discovery.",
            ),
            (
                "A smoke test loads far more context than the task needs.",
                "Search first and load only the resources the selected skill actually references.",
            ),
            (
                "A tool is unavailable on this machine.",
                "Record the limitation and route the task to the documented deterministic fallback.",
            ),
        ],
        challenge=(
            "Add one capability to the registry that you deliberately implement as a "
            "tool rather than a skill, and record the reasoning in the decision record."
        ),
        reflection=(
            "Which capability was genuinely ambiguous between tool and skill, and "
            "which requirement finally decided it?"
        ),
    ),
    dict(
        num=5,
        topic=2,
        title="Create a Custom Branded Video Skill",
        objective="LO2: package brand, tone and style rules into a reusable skill and verify the rendered output",
        duration=70,
        goal="Make brand compliance repeatable and demonstrable rather than asserted.",
        desc=(
            "You will approve a brand profile, write SKILL.md for a custom "
            "brand-video skill, bind its templates using relative or Hermes template "
            "paths, render a custom video through the skill, review the frame samples "
            "against the brand checklist and version the resulting evidence."
        ),
        build=(
            "A custom-video.mp4 with brand-review.json and render-evidence.json."
        ),
        services="Hermes skills, brand token profile, Remotion or FFmpeg renderer, FFprobe",
        prerequisites=[
            "Complete Lab 4 so the tool registry and skills are installed.",
            "Open labs/lab-05-create-custom-branded-video-skill/ as the current Hermes project.",
            "Review data/brand-profile.yaml before editing any token.",
        ],
        workflow=[
            "Approve the brand profile",
            "Create SKILL.md",
            "Bind the templates",
            "Render the video",
            "Review the frames",
            "Version the evidence",
        ],
        steps=[
            (
                "Approve the brand profile and store the logo, palette, typography and motion rules as editable tokens",
                "",
            ),
            (
                "Define the audience, voice and pacing, and write the style exclusions explicitly",
                "",
            ),
            (
                "Create SKILL.md with frontmatter describing the exact trigger, inputs, outputs and verification",
                "",
            ),
            (
                "Bind the bundled scripts and templates using relative or Hermes template paths",
                "",
            ),
            (
                "Render the custom video through the skill rather than by calling the renderer directly",
                "",
            ),
            (
                "Probe the output and review the frame samples against the brand checklist",
                "ffprobe -v error -show_streams -show_format custom-video.mp4",
            ),
            (
                "Run the acceptance test from a clean start, then run the verifier and retain the PASS output",
                "python3 verify.py",
            ),
        ],
        test=(
            "verify.py must print PASS Lab 05. The custom skill is discoverable, uses "
            "relative or Hermes template paths, creates an MP4, passes the technical "
            "probe and meets every required brand token."
        ),
        checkpoint=(
            "The custom brand-video skill and its approved master are the production "
            "inputs for the multi-agent and release labs."
        ),
        troubleshooting=[
            (
                "Two runs produce visibly different brand treatment.",
                "Move the varying value into a stored token and reference it from the skill.",
            ),
            (
                "The skill works interactively but fails from a clean start.",
                "Replace any absolute or session-dependent path with a relative or Hermes template path.",
            ),
            (
                "The render looks correct but the probe fails.",
                "Fix the delivery properties; a master that fails the gate is not a candidate for release.",
            ),
        ],
        challenge=(
            "Change one palette token and prove that the rendered frames and the brand "
            "review both reflect the change without any edit to the skill's procedure."
        ),
        reflection=(
            "Which brand rule was hardest to express as a checkable token rather than "
            "as prose, and how did you make it measurable?"
        ),
    ),
]
