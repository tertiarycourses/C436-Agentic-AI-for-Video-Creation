#!/usr/bin/env python3
"""C436 v4.0: the LG Markdown mirror (repo root), converted from the WSQ mirror line by line."""
import re, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from convert_docs_c436 import kept, PAGE, MATERIALS   # same slide map and product page

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "source-wsq/LG-Agentic AI for Video Creation.md"
OUT = ROOT / "LG-Agentic AI for Video Creation.md"

LAB_TIME = {"138": "80 min", "156": "80 min", "166": "70 min"}
RULES = [
    (r"^TGS-2023036088 · Version 6\.2 ·", "C436 · Version 4.0 ·"),
    (r"^\*\*Course:\*\* .*$", "**Course:** Agentic AI for Video Creation (C436) · 2 days, 15 instructional hours (9:30 AM – 5:30 PM)."),
    (r"use as your open-book reference in the assessment", "keep as your reference after the course"),
    (r"https://www\.tertiarycourses\.com\.sg/wsq-agentic-ai-for-video-creation\.html", PAGE),
    (r"^Courseware and the assessment are on the LMS: \S+", MATERIALS),
    (r"\s*\(the video PP Task 3 asks you to upload\)", ""),
    (r"Your film is the evidence for PP Task 3: export it as", "Export your film as"),
    (r"\bLU[123] · ", ""),
    (r"\s+·\s+\*\*K & A:\*\*[^·]*(?=·)", "  "),
    (r"\b(is|are) the [KA]\d (skill|ability|knowledge)", r"\1 the \2 at work here"),
    (r"\s*\((?:ability )?[KA]\d\)", ""),
    (r"\b[KA]\d — ", ""),
    (r"TGS-2023036088", "C436"),
]


def remap(m):
    a, b = m.group(2), m.group(3)
    return f"{m.group(1)}{kept(int(a), 1)}" + (f"–{kept(int(b), -1)}" if b else "")


out, skip = [], False
for line in SRC.read_text(encoding="utf-8").splitlines():
    if re.match(r"^#{2,3} (Knowledge and Abilities|Assessment Flow)\s*$", line):
        skip = True
        continue
    if skip and re.match(r"^#{1,3} ", line):
        skip = False
    if skip:
        continue
    m = re.search(r"\*\*Slides:\*\* (\d+)–", line)
    if m and m.group(1) in LAB_TIME:
        line = re.sub(r"(\*\*Time:\*\* )\d+ min", r"\g<1>" + LAB_TIME[m.group(1)], line)
    for rx, rep in RULES:
        line = re.sub(rx, rep, line)
    line = re.sub(r"(\*\*Slides:\*\* |\bSlides |\(slide )(\d+)(?:–(\d+))?", remap, line)
    out.append(line)
while out and not out[-1].strip():
    out.pop()
OUT.write_text("\n".join(out) + "\n", encoding="utf-8")
bad = [l for l in out if re.search(r"\b[KA][1-7]\b|PP Task|\bWA\b|TRAQOM|Written Assessment|Practical Performance|TGS-|(?<!NON-)WSQ|assessment", l)]
print(f"wrote {OUT.name}; leftovers: {len(bad)}")
for l in bad: print("  ", l[:150])
