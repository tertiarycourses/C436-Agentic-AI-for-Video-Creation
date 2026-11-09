#!/usr/bin/env python3
"""C436 v4.0: convert the WSQ TGS-2023036088 Higgsfield v6.2 deck to its non-WSQ twin.

Edits text at RUN level so the house design survives. Reuses drop_slides and
renumber_footers from the wsq-to-non-wsq skill.
"""
import json, re, sys
from pathlib import Path
sys.path.insert(0, str(Path.home() / ".claude/skills/wsq-to-non-wsq/scripts"))
from convert_deck import drop_slides, renumber_footers  # noqa: E402
from pptx import Presentation

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "source-wsq/courseware/PPT-Agentic AI for Video Creation-v6.2.pptx"
OUT = ROOT / "courseware/Agentic AI for Video Creation-v4.0.pptx"

# 0-based source indexes of WSQ-only slides (6: the LMS-TMS login screenshot,
# whose portal is labelled "For WSQ courses")
DROP = [1, 6, 7, 8, 9, 10, 18, 19, 20, 21, 23, 104, 146, 177, 179, 180, 181]
FEEDBACK = 178

GLOBAL = [  # (regex, replacement) applied per paragraph, deck-wide
    (r"WSQ COURSE CODE\s*•\s*TGS-2023036088", "NON-WSQ COURSE  •  C436"),
    (r"TGS-2023036088", "C436"),
    (r"Version 6\.2", "Version 4.0"),
    (r"75% attendance", "Full attendance"),
    (r"Required for funding eligibility\.", "Attend every session to get the most from the course."),
    (r" — one per Learning Unit\.", "."),
    (r"\s*\(the video PP Task 3 asks you to upload\)", ""),
    # K/A competency tags
    (r"\s*·\s*[KA]\d(?:\s*\([a-z]+\))?(?:,\s*[KA]\d(?:\s*\([a-z]+\))?)*\s*$", ""),
    (r"\s*\((?:ability )?[KA]\d\)", ""),
]

NOTES = [
    (r"(Lab \d \(\d+ min)(?:,\s*[KA]\d(?:\s*\((?:preview|preparation)\))?)+\)", r"\1)"),
    (r"\b(is|are) the [KA]\d (skill|ability|knowledge)", r"\1 the \2 at work here"),
    (r"\s*\((?:ability )?[KA]\d\)", ""),
    (r"\s*\(the video PP Task 3 asks you to upload\)", ""),
    (r"TGS-2023036088", "C436"),
    (r"Your film is the evidence for PP Task 3: export it as", "Export your film as"),
]

# lab timings rescaled onto the 450-min Day 2 (proportional, see LP)
LAB_MIN = {"LAB 05": ("~60 MIN", "~80 MIN"), "LAB 06": ("~60 MIN", "~80 MIN"),
           "LAB 07": ("~55 MIN", "~70 MIN")}
NOTE_MIN = [("Lab 5 (60 min)", "Lab 5 (80 min)"), ("Lab 6 (60 min)", "Lab 6 (80 min)"),
            ("Lab 7 (55 min)", "Lab 7 (70 min)")]

SCHEDULE = {  # source slide 17
    "Lesson Plan (9:30 AM – 6:30 PM)": "Lesson Plan (9:30 AM – 5:30 PM)",
    "Tea breaks 15 min, lunch 1 hour (Day 1 at 12:45). Full timings and slide numbers are in the Lesson Plan.":
        "One 30-minute lunch (Day 1 at 12:30, Day 2 at 12:25). Full timings and slide numbers are in the Lesson Plan.",
    "9:30–11:00  Welcome · AI video today · Higgsfield basics": "9:30–11:00  Welcome · AI video today · Higgsfield basics",
    "9:30–10:30  Recap · Topic 2 (parameters, editor)": "9:30–10:50  Recap · Topic 2 (parameters, editor)",
    "11:15–12:45  Story principles · Lab 1 · Ah Ma demo": "11:00–12:30  Story principles · Lab 1 · Ah Ma demo",
    "10:30–1:00  Lab 5 · Topic 3 (skills, standards)": "10:50–12:25  Lab 5 · Topic 2 recap",
    "1:45–4:05  Lab 2 · standards, work plans · Lab 3": "1:00–3:20  Lab 2 · standards, work plans · Lab 3",
    "2:00–4:10  Lab 6 · publishing · Lab 7 capstone": "12:55–3:35  Topic 3 (skills, standards) · Lab 6",
    "4:20–6:30  Topic 2 (production run) · Lab 4 · case study": "3:20–5:30  Topic 2 (production run) · Lab 4 · case study",
    "4:10 Ethics, summary · 4:30–6:30 Assessment": "3:35–5:30  Publishing · Lab 7 capstone · ethics, summary",
    "TIP   Day 2 assessment: Written Assessment 4:30–5:30 PM, Practical Performance 5:30–6:30 PM.":
        "TIP   Refreshments are available through the day; take them during lab time.",
}

LABTABLE = {  # source slide 14: the K & A column becomes what each lab makes
    "K & A": "YOU MAKE", "K5 (preview)": "Your Claude studio", "K1, A1": "Brief, script, review",
    "A2, A3": "Storyboard, standards, plan", "K2, A4 (preparation)": "Episode 1 clips",
    "K2, K3, A4, A5": "Episode 1 v1 → v2", "K4, A6": "Compliance skill, fixes",
    "K5, A7": "Your own short film",
}

WRAPUP = {  # source slide 176
    "Each ability statement in the TSC, and where you demonstrated it.":
        "Seven abilities you practised, and the lab where you did each one.",
    **{f"A{i}": str(i) for i in range(1, 8)},
}

FEEDBACK_TEXT = {
    "Certification & TRAQOM Survey": "Course Feedback",
    "TRAQOM Survey (Mandatory)": "Share Your Feedback",
    "Complete the certification & TRAQOM survey to receive your certificate.":
        "Please complete the course feedback form before you leave — it helps us improve this course.",
    "https://lms-tms.tertiaryinfotech.com/": "Your trainer shares the link at the end of the course.",
    "Digital Attendance": "Certificate of Completion",
    "Remember to take AM, PM and Assessment digital attendance — required for your funding.":
        "Your certificate of completion is emailed to you after the course.",
}


def set_para(p, new):
    """Write new text into a paragraph, keeping the first run's formatting."""
    runs = p.runs
    if not runs:
        return
    runs[0].text = new
    for r in runs[1:]:
        r.text = ""


def sub_para(p, rules):
    old = p.text
    new = old
    for rx, rep in rules:
        new = re.sub(rx, rep, new)
    if new == old:
        return False
    # try a run-local edit first so mixed formatting survives
    for r in p.runs:
        t = r.text
        nt = t
        for rx, rep in rules:
            nt = re.sub(rx, rep, nt)
        if nt != t:
            r.text = nt
    if p.text != new:
        set_para(p, new)
    return True


def exact(p, table):
    t = p.text.strip()
    if t in table:
        set_para(p, table[t])
        return True
    return False


def shapes(container):
    for sh in container:
        if sh.shape_type == 6:
            yield from shapes(sh.shapes)
        else:
            yield sh


def paragraphs(slide):
    for sh in shapes(slide.shapes):
        if sh.has_text_frame:
            yield from sh.text_frame.paragraphs
        elif getattr(sh, "has_table", False) and sh.has_table:
            for row in sh.table.rows:
                for c in row.cells:
                    yield from c.text_frame.paragraphs


def main():
    prs = Presentation(str(SRC))
    slides = list(prs.slides)
    assert len(slides) == 183, len(slides)
    # guard: the drop list must match the inspected titles
    must = {1: "Digital Attendance", 6: "Login to LMS", 7: "Learning Outcomes", 8: "Knowledge Statements",
            9: "Ability Statements", 10: "Learning Outcomes, K & A", 18: "Briefing for Assessment",
            19: "Assessment & Funding", 20: "Courseware & Assessment", 21: "TRAQOM",
            23: "LEARNING OUTCOME, KNOWLEDGE", 104: "LEARNING OUTCOME, KNOWLEDGE",
            146: "LEARNING OUTCOME, KNOWLEDGE", 177: "Courseware & Assessment",
            178: "TRAQOM", 179: "Assessment & Funding", 180: "Assessment Flow", 181: "Digital Attendance"}
    for i, needle in must.items():
        txt = " ".join(sh.text_frame.text for sh in slides[i].shapes if sh.has_text_frame)
        assert needle in txt, (i, needle)

    # per-slide exact rewrites (source indexes)
    for i, table in ((17, SCHEDULE), (14, LABTABLE), (176, WRAPUP), (FEEDBACK, FEEDBACK_TEXT)):
        for p in paragraphs(slides[i]):
            exact(p, table)
    for p in paragraphs(slides[176]):
        if re.match(r"T[123] · ", p.text):
            sub_para(p, [(r"^T([123]) · ", r"Topic \1 · ")])

    # lab-slide durations
    for s in slides:
        txt = " ".join(p.text for p in paragraphs(s))
        for lab, (a, b) in LAB_MIN.items():
            if txt.startswith(lab) or f"{lab} · HANDS-ON" in txt:
                for p in paragraphs(s):
                    if a in p.text:
                        sub_para(p, [(re.escape(a), b)])

    # cover: remove the WSQ logo, shrink the white badge to the Tertiary logo
    cover = slides[0]
    pics = [sh for sh in cover.shapes if sh.shape_type == 13]
    wsq = [sh for sh in pics if sh.image.size == (300, 137)]
    assert len(wsq) == 1
    wsq[0]._element.getparent().remove(wsq[0]._element)
    badge = [sh for sh in cover.shapes if sh.name == "Rounded Rectangle 9"][0]
    tlogo = [sh for sh in cover.shapes if sh.shape_type == 13][0]
    pad = tlogo.left - badge.left
    right = badge.left + badge.width
    badge.width = tlogo.width + 2 * pad
    badge.left = right - badge.width
    tlogo.left = badge.left + pad

    # screenshots of the lab pages carry the course code and K & A tags in the
    # pixels: swap in fresh captures of the converted C436 labs
    # (build/screens/, taken with headless Chrome from labs/)
    for idx, title, png in ((15, "The Labs Home Page", "labs-index.png"),
                            (16, "Every Lab Has a Prompt Page", "lab-prompt-page.png")):
        s = slides[idx]
        assert any(title in p.text for p in paragraphs(s)), (idx, title)
        pic = [sh for sh in s.shapes if sh.shape_type == 13]
        assert len(pic) == 1
        part = pic[0].part.related_part(pic[0]._element.blip_rId)
        part._blob = (ROOT / "build/screens" / png).read_bytes()

    # deck-wide rules, notes
    for s in slides:
        for p in paragraphs(s):
            sub_para(p, GLOBAL)
        if s.has_notes_slide:
            for p in s.notes_slide.notes_text_frame.paragraphs:
                sub_para(p, NOTES)
                sub_para(p, [(re.escape(a), b) for a, b in NOTE_MIN])

    drop_slides(prs, DROP)
    renumber_footers(prs)

    # kept-slide map: source 1-based -> new 1-based
    kept = [i for i in range(183) if i not in DROP]
    smap = {i + 1: n + 1 for n, i in enumerate(kept)}
    (ROOT / "build/slide_map_c436.json").write_text(json.dumps(smap, indent=0))
    OUT.parent.mkdir(exist_ok=True)
    prs.save(str(OUT))
    print("wrote", OUT, len(prs.slides), "slides")


if __name__ == "__main__":
    main()
