<div align="center">

# Agentic AI for Video Creation

[![Course](https://img.shields.io/badge/Course-C436-1f6feb?style=for-the-badge)](https://www.tertiarycourses.com.sg/agentic-ai-for-video-creation.html)
[![Duration](https://img.shields.io/badge/Duration-2_days_15_instructional_hours-5E5E5E?style=for-the-badge)](#course-toolkit)
[![Labs](https://img.shields.io/badge/Labs-8-34d399?style=for-the-badge)](labs/README.md)
[![License](https://img.shields.io/badge/License-Educational-fbbf24?style=for-the-badge)](#license)

**A connected, hands-on course in Agentic AI for Video Creation — build an evidence-led video production system in Hermes Agent, from MiniMax M3 setup and FRAME-CUT prompt engineering to custom video skills, multi-agent Kanban review, private YouTube upload and controlled scheduling.**

[📘 Course Page](https://www.tertiarycourses.com.sg/agentic-ai-for-video-creation.html) · [🧪 Hands-On Labs](labs/README.md) · [📖 Learner Guide](<LG-Agentic AI for Video Creation.md>) · [🐛 Report Bug](https://github.com/tertiarycourses/C436-Agentic-AI-for-Video-Creation/issues) · [💡 Request Feature](https://github.com/tertiarycourses/C436-Agentic-AI-for-Video-Creation/issues)

</div>

> [!NOTE]
> **These are the official hands-on lab materials for the commercial course:**
> ### 🎓 Agentic AI for Video Creation
> **Course Code:** `C436` · by Tertiary Courses / Tertiary Infotech<br>
> **Duration:** 2 days · 15 instructional hours<br>
> **Course page:** https://www.tertiarycourses.com.sg/agentic-ai-for-video-creation.html

---

## Lab Activities

The 8 labs form one connected practical journey. Complete them in order so each verified output can support the activities that follow.

### Topic 1 — Hermes Agent Setup, MiniMax M3 and Video Prompt Engineering

| # | Activity | Outcome |
|---:|----------|---------|
| **1** | [Set Up Hermes Desktop and Connect MiniMax M3](labs/lab-01-setup-hermes-and-connect-minimax-m3/README.md) | A `setup-evidence.json` and redacted diagnostic screenshot proving a tool-capable model handshake with no exposed credential. |
| **2** | [Prompt Hermes to Create a Simple Video](labs/lab-02-prompt-hermes-to-create-a-simple-video/README.md) | A `simple-video.mp4` with its `shot-plan.json` and `ffprobe.json` evidence. |
| **3** | [Engineer Video Prompts with FRAME-CUT](labs/lab-03-engineer-video-prompts-with-frame-cut/README.md) | A `prompt-pack.json` with its `prompt-score.csv` rubric evidence. |

### Topic 2 — Video Tools, Hermes Skills and Custom Brand Production

| # | Activity | Outcome |
|---:|----------|---------|
| **4** | [Install Video Tools and Hermes Skills](labs/lab-04-install-video-tools-and-skills/README.md) | A `tool-routing.json` registry with `skill-smoke-test.json` evidence. |
| **5** | [Create a Custom Branded Video Skill](labs/lab-05-create-custom-branded-video-skill/README.md) | A `custom-video.mp4` with `brand-review.json` and `render-evidence.json`. |

### Topic 3 — Multi-Agent Kanban, YouTube Release and Scheduled Publishing

| # | Activity | Outcome |
|---:|----------|---------|
| **6** | [Build the Multi-Agent Video Workflow](labs/lab-06-build-multi-agent-video-workflow/README.md) | A `multi-agent-plan.json` with four verified handoff records. |
| **7** | [Orchestrate Kanban Review and YouTube Upload](labs/lab-07-orchestrate-kanban-review-and-youtube-upload/README.md) | A `kanban-export.json`, `approval-ledger.json` and private-upload receipt or dry-run preview. |
| **8** | [Schedule Controlled Video Publishing with Hermes Cron](labs/lab-08-schedule-controlled-video-publishing/README.md) | A `cron-preview.json` with an `operations-ledger.csv`. |

Each lab package ships copy-ready prompts in Markdown and PDF, synthetic inputs, starter scripts or configuration, an evidence checklist and a deterministic `verify.py`. The sample YouTube request defaults to `private` and scheduled publishing starts paused.

---

## About

This repository contains the complete lab and courseware package for **Agentic AI for Video Creation** (**C436**) by Tertiary Courses / Tertiary Infotech. Learners configure the Hermes runtime, turn a creative brief into structured prompts, route specialist video tools, build a reusable branded video skill, coordinate research/production/review/upload roles, and prepare a governed publishing schedule — verifying each result before moving on.

### What you'll learn

- Complete **8 connected hands-on activities** and carry their outputs through one coherent learning journey.
- Practise with **Hermes Agent · MiniMax M3 · Remotion · Manim · FFmpeg · YouTube Data API** and the supporting resources supplied in the repository.
- Begin with **Set Up Hermes Desktop and Connect MiniMax M3** and finish with **Schedule Controlled Video Publishing with Hermes Cron**.
- Apply safe data handling, deterministic evidence checks and named human review before any release action.

> 📖 **Full walkthrough:** see the [Learner Guide](<LG-Agentic AI for Video Creation.md>) for the complete course narrative, and [labs/README.md](labs/README.md) for the lab index. Slides, the Learner Guide and the Lesson Plan are in [courseware/](courseware/).

---

## Course Toolkit

| Category | Details |
|----------|---------|
| **Duration** | 2 days · 15 instructional hours |
| **Delivery** | Instructor-led, hands-on practical labs |
| **Core tools** | Hermes Agent (Desktop + CLI) · MiniMax M3 · Remotion · Manim · FFmpeg · YouTube Data API |
| **Practical work** | 8 connected labs, each with a deterministic `verify.py` |
| **Courseware** | PowerPoint and PDF slides, Word and PDF guides, Markdown lab instructions |

---

## Learning Journey

```text
START
  Lab 1    Set Up Hermes Desktop and Connect MiniMax M3
     │
     ▼
  Topic 1 — Hermes Agent Setup, MiniMax M3 and Video Prompt Engineering
  Labs 1–3
     │
     ▼
  Topic 2 — Video Tools, Hermes Skills and Custom Brand Production
  Labs 4–5
     │
     ▼
  Topic 3 — Multi-Agent Kanban, YouTube Release and Scheduled Publishing
  Labs 6–8
     │
     ▼
FINISH
  Lab 8   Schedule Controlled Video Publishing with Hermes Cron
```

Connected workflow: `Hermes setup → MiniMax M3 → FRAME-CUT prompt → tool and skill routing → custom branded video → specialist agents → Kanban review and private upload → paused cron release`

---

## Project Structure

```text
C436-Agentic-AI-for-Video-Creation/
├── README.md
├── LG-Agentic AI for Video Creation.md
│
├── labs/
│   ├── README.md                 # Start here: complete lab index
│   └── lab-NN-<slug>/            # 8 connected lab packages
│       ├── README.md             #   activity instructions
│       ├── AI-PROMPTS.md/.pdf    #   copy-ready learner prompts
│       ├── data/                 #   synthetic inputs
│       ├── starter/              #   starter scripts and templates
│       ├── evidence/checklist.md #   evidence gate
│       └── verify.py             #   deterministic acceptance verifier
│
└── courseware/
    ├── *.pptx / *.pdf            # Trainer and learner slides
    ├── LG-*.docx / LG-*.pdf      # Learner Guide
    ├── LP-*.docx / LP-*.pdf      # Lesson Plan
    └── archive/                  # Superseded versions
```

---

## Getting Started

### Prerequisites

- **Hermes Desktop** installed from the official page at https://hermes-agent.nousresearch.com/desktop, with administrator rights to install desktop software.
- A **MiniMax account and API key** for the `MiniMax-M3` model. Trial, quota and region terms are time-sensitive — confirm the live offer in your own account at sign-up.
- **Python 3**, **FFmpeg** and **FFprobe** on `PATH` for the supplied verifiers and preview renderers.
- A Google account with a YouTube channel for the release labs. Uploads stay `private`; public visibility is never required to complete a lab.
- Synthetic or authorised data only. Never paste a MiniMax key, OAuth token or YouTube credential into a prompt, lab file, screenshot or repository.

### 1. Clone the repository

```bash
git clone https://github.com/tertiarycourses/C436-Agentic-AI-for-Video-Creation.git
cd C436-Agentic-AI-for-Video-Creation
```

### 2. Open the lab index

Start with [labs/README.md](labs/README.md), then complete Labs 1–8 in order. Open each lab folder as the current project in Hermes Desktop and read its `AI-PROMPTS.md` before prompting.

### 3. Verify and keep your connected outputs

Run `python3 verify.py` inside each lab folder and retain the `PASS` output with the requested evidence. Later activities depend on these approved outputs.

---

## Contributing

Contributions, corrections and improvements are welcome:

1. **Fork** the repository.
2. Create a feature branch: `git checkout -b feature/my-improvement`.
3. Commit your changes: `git commit -m "Add my improvement"`.
4. Push the branch: `git push origin feature/my-improvement`.
5. Open a **Pull Request**.

Found a bug or have an idea? Open an [issue](https://github.com/tertiarycourses/C436-Agentic-AI-for-Video-Creation/issues).

---

## License

This material is provided for **educational use** as part of the commercial course **Agentic AI for Video Creation (C436)**. © Tertiary Infotech Pte. Ltd. All rights reserved.

---

## Developed By

**Tertiary Infotech Pte. Ltd.** — [Tertiary Courses](https://www.tertiarycourses.com.sg)<br>
Course: [Agentic AI for Video Creation (C436)](https://www.tertiarycourses.com.sg/agentic-ai-for-video-creation.html)

## Acknowledgements

- The teams behind Hermes Agent, MiniMax, Remotion, Manim and FFmpeg.
- Course trainers and learners of C436.

---

<div align="center">

⭐ **If these materials helped you learn Agentic AI for Video Creation, star the repository!**

Powered by [Tertiary Infotech Academy Pte Ltd](https://www.tertiaryinfotech.com/)

[📘 Course Page](https://www.tertiarycourses.com.sg/agentic-ai-for-video-creation.html) · [🧪 Hands-On Labs](labs/README.md) · [📖 Learner Guide](<LG-Agentic AI for Video Creation.md>)

</div>
