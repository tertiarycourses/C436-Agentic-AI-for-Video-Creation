# C436 - Agentic AI for Video Creation

Complete non-WSQ courseware package for the two-day beginner course
[Agentic AI for Video Creation](https://www.tertiarycourses.com.sg/agentic-ai-for-video-creation.html).

## Courseware

- `courseware/Agentic AI for Video Creation-v1.0.pptx` - trainer slides
- `courseware/Agentic AI for Video Creation-v1.0.pdf` - learner slides
- `courseware/LG-Agentic AI for Video Creation.docx` and `.pdf` - Learner Guide
- `courseware/LP-Agentic AI for Video Creation.docx` and `.pdf` - Lesson Plan
- `LG-Agentic AI for Video Creation.md` - searchable Learner Guide mirror
- `labs/` - eight connected hands-on labs and synthetic support assets

The single source is in
`.agents/skills/non-wsq-courseware-build/build/course_data.py` and
`data_domain1.py` through `data_domain4.py`. It drives the PPT, Learner Guide,
Lesson Plan, and labs so their topic and lab sequence remains aligned.

## Build

From Git Bash on Windows:

```bash
export COURSE_REPO="$(pwd)"
bash .agents/skills/non-wsq-courseware-build/build/build_courseware.sh
```

## Quality checks

```bash
python .agents/skills/non-wsq-courseware-qa/scan_prohibited.py .
node labs/assets/test-n8n-workflows.js
powershell.exe -NoProfile -ExecutionPolicy Bypass -File labs/assets/test-lab-checkpoints.ps1
```

The package is designed for commercial non-WSQ delivery. It contains no formal
course assessment, funding/compliance material, attendance workflow, or survey
workflow.
