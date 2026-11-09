#!/usr/bin/env python3
"""C436 v4.0: convert the WSQ TGS-2023036088 Higgsfield v6.2 LP and LG to non-WSQ.

Edits the built DOCX files in place (run-level), so the house layout survives:
  - cover: course code C436, version 4.0; C436's own version-control history
  - drops the K & A tables, the LU/assessment mapping, the Assessment section
    and the Assessment Flow; strips K/A/LU codes and PP/WA references
  - LP: 9:30 AM - 5:30 PM, 450 min teaching + one 30-min lunch per day; Day 2
    rescaled proportionally (all topics kept, same order)
  - remaps every slide reference onto the 167-slide non-WSQ deck
Run after convert_deck_c436.py (needs build/slide_map_c436.json).
"""
import copy, json, re
from pathlib import Path
from docx import Document

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "source-wsq/courseware"
OUT = ROOT / "courseware"
SMAP = {int(k): v for k, v in json.loads((ROOT / "build/slide_map_c436.json").read_text()).items()}
PAGE = "https://www.tertiarycourses.com.sg/agentic-ai-for-video-creation.html"
DECK_SLIDES = max(SMAP.values())
MATERIALS = "Your trainer shares the slides, the Learner Guide and the lab pack at the start of the course."

VC_ROWS = [
    ("1.0", "29 Jul 2026", "First C436 courseware.", "Dr. Alfred Ang"),
    ("2.0", "16 Sep 2026", "Rebuilt with Hermes Agent and MiniMax M3.", "Dr. Alfred Ang"),
    ("3.0", "16 Sep 2026", "Four creative labs and a micro-drama series.", "Dr. Alfred Ang"),
    ("4.0", "9 Nov 2026", "Claude + Higgsfield edition: Claude Desktop with five video skills, "
     "Higgsfield through MCP and LahLah Video; seven connected Kopi & Coins labs ending in a mini "
     "capstone; GenAI video ethics. 9:30 AM – 5:30 PM, 15 instructional hours.", "Dr. Alfred Ang"),
]


# ------------------------------------------------------------------ helpers
def set_para(p, new):
    runs = p.runs
    if not runs:
        p.add_run(new)
        return
    runs[0].text = new
    for r in runs[1:]:
        r.text = ""


def sub_para(p, rules):
    old = p.text
    new = old
    for rx, rep in rules:
        new = re.sub(rx, rep, new) if not callable(rep) else re.sub(rx, rep, new)
    if new == old:
        return
    for r in p.runs:                       # run-local first, keeps bold/links
        t = r.text
        for rx, rep in rules:
            t = re.sub(rx, rep, t)
        r.text = t
    if p.text != new:
        if len([r for r in p.runs if r.text]) > 1:
            FALLBACK.append(new[:90])
        set_para(p, new)


FALLBACK = []


def drop(el):
    el.getparent().remove(el)


def all_paras(doc):
    yield from doc.paragraphs
    for t in doc.tables:
        for row in t.rows:
            for c in row.cells:
                yield from c.paragraphs


def find(doc, text, start=0, exact=True):
    for i, p in enumerate(doc.paragraphs[start:], start):
        if (p.text.strip() == text) if exact else (text in p.text):
            return i, p
    raise KeyError(text)


def next_table(p):
    el = p._p.getnext()
    while el is not None and not el.tag.endswith("}tbl"):
        el = el.getnext()
    return el


def drop_section(doc, heading, stop_styles=("Heading 1", "Heading 2")):
    """Drop a heading and everything up to the next heading of the given styles."""
    i, p = find(doc, heading)
    lvl = p.style.name
    stops = stop_styles if lvl == "Heading 2" else ("Heading 1",)
    el = p._p
    nxt = el.getnext()
    drop(el)
    while nxt is not None:
        if nxt.tag.endswith("}p"):
            sty = nxt.find(".//{*}pStyle")
            name = sty.get("{http://schemas.openxmlformats.org/wordprocessingml/2006/main}val") if sty is not None else ""
            if name.replace(" ", "") in [s.replace(" ", "") for s in stops]:
                break
        if nxt.tag.endswith("}sectPr"):
            break
        cur, nxt = nxt, nxt.getnext()
        drop(cur)


def kept(n, direction):
    """Map a source slide number onto the new deck (dropped -> nearest kept)."""
    step = 1 if direction > 0 else -1
    while n not in SMAP and 1 <= n <= 183:
        n += step
    return SMAP.get(n, SMAP[183] if direction < 0 else 1)


def remap_range(m):
    a = int(m.group(2))
    b = m.group(3)
    if b is None:
        return f"{m.group(1)}{kept(a, 1)}"
    return f"{m.group(1)}{kept(a, 1)}–{kept(int(b), -1)}"


SLIDE_RX = (r"(\b[Ss]lides?:?\*{0,2} |\(slide )(\d+)(?:–(\d+))?", remap_range)

COMMON = [
    (r"TGS Ref No: TGS-2023036088", "Course Code: C436"),
    (r"^Version 6\.2$", "Version 4.0"),
    (r"TGS-2023036088", "C436"),
    (r"\s*\(the video PP Task 3 asks you to upload\)", ""),
    (r"Your film is the evidence for PP Task 3: export it as", "Export your film as"),
    (r"\bLU[123] · ", ""),
    (r"\s*·\s*K & A: [^·]*?(?=\s*·)", ""),
    (r"\s*·\s*[KA]\d(?:\s*\([a-z]+\))?(?:,\s*[KA]\d(?:\s*\([a-z]+\))?)*\s*$", ""),
    (r"\b(is|are) the [KA]\d (skill|ability|knowledge)", r"\1 the \2 at work here"),
    (r"\s*\((?:ability )?[KA]\d\)", ""),
    (r"(Knowledge|Abilities): ", r"\1: "),
    (r"\b[KA]\d — ", ""),
    (r"(?<=; )[KA]\d (?=[A-Z])", ""),
    (r"(?<=: )[KA]\d (?=[A-Z])", ""),
    (r"^\s[KA]\d (?=[A-Z])", " "),
    (r"(Slides 138–144 · Day 2, )60 min", r"\g<1>80 min"),
    (r"(Slides 156–161 · Day 2, )60 min", r"\g<1>80 min"),
    (r"(Slides 166–172 · Day 2, )55 min", r"\g<1>70 min"),
]


def vc_table(doc):
    t = doc.tables[0]
    assert t.rows[0].cells[0].text.startswith("Version"), t.rows[0].cells[0].text
    rows = list(t.rows)[1:]
    while len(rows) > len(VC_ROWS):
        drop(rows.pop()._tr)
    for row, vals in zip(rows, VC_ROWS):
        for c, v in zip(row.cells, vals):
            set_para(c.paragraphs[0], v)
            for extra in c.paragraphs[1:]:
                drop(extra._p)


def toc_drop(doc, titles):
    for p in list(doc.paragraphs[:60]):
        head = p.text.split("\t")[0].strip()
        if "\t" in p.text and head in titles:
            drop(p._p)


# ------------------------------------------------------------------- LP
DAY1 = [  # (match, time, duration, slides) - teaching rows keep their minutes
    ("Welcome", "9:30 AM–10:00 AM", "30 min", None),
    ("Topic 1 — LO1", "10:00 AM–11:00 AM", "60 min", None),
    ("Topic 1 — principles", "11:00 AM–11:40 AM", "40 min", None),
    ("Lab 1 —", "11:40 AM–12:10 PM", "30 min", None),
    ("Claude instructs Higgsfield", "12:10 PM–12:30 PM", "20 min", None),
    ("Lunch", "12:30 PM–1:00 PM", "30 min", None),
    ("Lab 2 —", "1:00 PM–1:50 PM", "50 min", None),
    ("Editing standards", "1:50 PM–2:20 PM", "30 min", None),
    ("Lab 3 —", "2:20 PM–3:20 PM", "60 min", None),
    ("Topic 1 recap", "3:20 PM–3:30 PM", "10 min", None),
    ("Topic 2 — LO2", "3:30 PM–3:50 PM", "20 min", None),
    ("Lab 4 —", "3:50 PM–5:05 PM", "75 min", None),
    ("Reviewing edited footage", "5:05 PM–5:30 PM", "25 min", None),
]
# Day 2 teaching (345 min in the WSQ day) rescaled x450/345, 5-min grain
DAY2 = [
    ("Day 1 recap", "9:30 AM–9:50 AM", "20 min", None),
    ("Parameters to assess", "9:50 AM–10:50 AM", "60 min", None),
    ("Lab 5 —", "10:50 AM–12:10 PM", "80 min", None),
    ("Topic 2 recap", "12:10 PM–12:25 PM", "15 min", None),
    ("Lunch", "12:25 PM–12:55 PM", "30 min", None),
    ("Topic 3 — LO3", "12:55 PM–2:15 PM", "80 min", None),
    ("Lab 6 —", "2:15 PM–3:35 PM", "80 min", None),
    ("Publishing to TikTok", "3:35 PM–3:55 PM", "20 min", None),
    ("Lab 7 —", "3:55 PM–5:05 PM", "70 min", None),
    ("The core ethical issues", "5:05 PM–5:30 PM", "25 min", None),
]


def minutes(s):
    return int(s.split()[0])


def rebuild_schedule(table, plan):
    rows = list(table.rows)
    header, body = rows[0], rows[1:]
    tbl = header._tr.getparent()
    used = []
    for match, tm, dur, _ in plan:
        hit = [r for r in body if r.cells[2].text.startswith(match)]
        assert len(hit) == 1, (match, [r.cells[2].text[:40] for r in body])
        r = hit[0]
        set_para(r.cells[0].paragraphs[0], tm)
        set_para(r.cells[1].paragraphs[0], dur)
        act = r.cells[2].paragraphs[0]
        sub_para(act, [(r" — LO\d, [KA]\d[^;]*;", " —"), (r"\s*\((?:[KA]\d(?:-[KA]\d)?)\)", ""),
                       (r",? digital attendance", ""), (r" and the [KA]\d skill", ""),
                       (r", TSC knowledge and abilities", ""),
                       (r", assessment briefing and the LMS", " and the LMS"),
                       (r"; course summary, Q&A, LMS, TRAQOM, briefing for assessment and "
                        r"assessment attendance", "; course summary, Q&A, course feedback and the LMS")])
        sl = r.cells[4].paragraphs[0]
        m = re.fullmatch(r"(\d+)(?:–(\d+))?", sl.text.strip())
        if m:
            a, b = int(m.group(1)), m.group(2)
            set_para(sl, f"{kept(a, 1)}–{kept(int(b), -1)}" if b else str(kept(a, 1)))
        used.append(r)
    for r in body:
        if r not in used:
            drop(r._tr)
    for r in used:                  # re-append in plan order (Day 2 lunch moves)
        tbl.remove(r._tr)
        tbl.append(r._tr)
    teach = sum(minutes(d) for m, _, d, _ in plan if m != "Lunch")
    assert teach == 450, teach


def fix_numbering(doc):
    """Give every numbered item its list's numId explicitly.

    The WSQ builder restarts each list by giving only its FIRST item a new numId;
    later items inherit the style's numId. After paragraphs are removed elsewhere
    in the document LibreOffice stops treating them as one list and numbers the
    LG "1., 33., 34. …". Explicit numIds make every list restart at 1 everywhere.
    """
    from docx.oxml import OxmlElement
    from docx.oxml.ns import qn
    cur, prev = None, False
    for p in doc.paragraphs:
        is_list = p.style.name == "List Number"
        if is_list:
            num = p._p.find(".//" + qn("w:numPr"))
            if num is not None:
                cur = num.find(qn("w:numId")).get(qn("w:val"))
            elif prev and cur:
                pPr = p._p.get_or_add_pPr()
                numPr = OxmlElement("w:numPr")
                for tag, val in (("w:ilvl", "0"), ("w:numId", cur)):
                    e = OxmlElement(tag); e.set(qn("w:val"), val); numPr.append(e)
                sty = pPr.find(qn("w:pStyle"))
                sty.addnext(numPr) if sty is not None else pPr.insert(0, numPr)
        prev = is_list


def convert_lp():
    doc = Document(SRC / "LP-Agentic AI for Video Creation.docx")
    for p in all_paras(doc):
        sub_para(p, COMMON)
    vc_table(doc)
    toc_drop(doc, {"Knowledge and Abilities", "Learning Units, Outcomes and Assessment"})
    _, p = find(doc, "Assessment\t", exact=False)
    sub_para(p, [(r"^Assessment\t", "Learning Reinforcement\t")])

    # course facts table
    facts = doc.tables[1]
    for row in list(facts.rows):
        k = row.cells[0].text
        v = row.cells[1].paragraphs[0]
        if k == "TSC":
            drop(row._tr)
        elif k == "Duration":
            set_para(v, "2 days · 15 instructional hours (7.5 hours a day)")
        elif k == "Class time":
            set_para(v, "9:30 AM – 5:30 PM, with one 30-minute lunch")
        elif k == "Deck":
            set_para(v, f"{DECK_SLIDES} slides, version 4.0 · 7 labs, each in its own folder")

    _, p = find(doc, "A two-day, hands-on WSQ course", exact=False)
    sub_para(p, [(r"hands-on WSQ course", "hands-on course")])

    # K & A table and the LU/LO/assessment mapping: not part of a non-WSQ LP
    for head in ("Knowledge and Abilities", "Learning Units, Outcomes and Assessment"):
        _, p = find(doc, head)
        t = next_table(p)
        drop(t)
        drop(p._p)

    _, p = find(doc, "Both days run 9:30 AM", exact=False)
    set_para(p, "Both days run 9:30 AM – 5:30 PM: 7.5 instructional hours a day with one 30-minute "
                "lunch; refreshments are taken during activity time. The Slides column gives the "
                "deck pages for each block.")
    _, p = find(doc, "Total training hours", exact=False)
    set_para(p, "Total instructional hours: 15 (7.5 hours a day over 2 days)")

    rebuild_schedule(doc.tables[2], DAY1)
    rebuild_schedule(doc.tables[3], DAY2)

    # instructional methods: purpose column without K/A/WA/PP
    purposes = {
        "Lecture": "Builds the knowledge each lab needs before learners start it.",
        "Didactic questioning": "Checks understanding before moving on to the next lab.",
        "Demonstration": "Shows the standard of work expected in each lab.",
        "Hands-on practical": "Builds the abilities to plan, make, review and fix a video with agents.",
        "Peer review and discussion": "Develops judgement for reviewing scripts, footage and compliance.",
    }
    for row in doc.tables[4].rows:
        if row.cells[0].text in purposes:
            set_para(row.cells[2].paragraphs[0], purposes[row.cells[0].text])

    _, p = find(doc, "Trainer: the v6.2 slide deck", exact=False)
    set_para(p, "Trainer: the v4.0 slide deck, this Lesson Plan, the Learner Guide and the lab pack "
                "(labs/, seven folders, the labs home page and the Prompt Builder).")

    # Assessment section -> Learning Reinforcement
    i, h = find(doc, "Assessment")
    set_para(h, "Learning Reinforcement")
    items = [doc.paragraphs[j] for j in range(i + 1, len(doc.paragraphs))
             if doc.paragraphs[j].text.strip()]
    new = [
        "Every lab builds on the last: Lab 4 shoots the storyboard approved in Lab 3, and Lab 7 "
        "reuses every skill from Labs 1 and 6.",
        "Each topic ends with a recap and check-your-understanding questions; Day 2 opens with a "
        "Day 1 recap.",
        "Peer review: learners swap storyboards, reviews and plans and critique each other against "
        "the studio's standards.",
        "The mini capstone (Lab 7) applies the whole pipeline to each learner's own short film; two "
        "films are screened and discussed in the last 10 minutes of Lab 7.",
        MATERIALS,
    ]
    assert len(items) >= len(new), len(items)
    for p, txt in zip(items, new):
        set_para(p, txt)
    for p in items[len(new):]:
        drop(p._p)

    for p in all_paras(doc):
        sub_para(p, [SLIDE_RX])
    fix_numbering(doc)
    _check(doc, "LP")
    doc.save(OUT / "LP-Agentic AI for Video Creation.docx")


# ------------------------------------------------------------------- LG
LAB_TIME = {"138": "80 min", "156": "80 min", "166": "70 min"}


def lab_meta(p):
    """LG lab line: bold labels in their own runs. Drop K & A, retime, remap."""
    runs = p.runs
    labels = [r.text.strip() for r in runs]
    if "Slides:" not in labels:
        return
    first = runs[labels.index("Slides:") + 1].text.strip().split("–")[0]
    for i, r in enumerate(runs[:-1]):
        lab, val = r.text.strip(), runs[i + 1]
        if lab == "K & A:":
            r.text = ""
            val.text = ""
        elif lab == "Time:" and first in LAB_TIME:
            val.text = re.sub(r"\d+ min", LAB_TIME[first], val.text)
        elif lab == "Slides:":
            m = re.fullmatch(r" (\d+)–(\d+)", val.text)
            val.text = f" {kept(int(m.group(1)), 1)}–{kept(int(m.group(2)), -1)}"


def convert_lg():
    doc = Document(SRC / "LG-Agentic AI for Video Creation.docx")
    for p in doc.paragraphs:
        if p.text.startswith("Agent:") and "Slides:" in p.text:
            lab_meta(p)
    for p in all_paras(doc):
        sub_para(p, COMMON)
    vc_table(doc)
    toc_drop(doc, {"Knowledge and Abilities", "Assessment Flow"})

    _, p = find(doc, "use as your open-book reference in the assessment", exact=False)
    sub_para(p, [(r"use as your open-book reference in the assessment",
                  "keep as your reference after the course")])
    _, p = find(doc, "Course: Agentic AI for Video Creation (C436)", exact=False)
    set_para(p, "Course: Agentic AI for Video Creation (C436) · 2 days, 15 instructional hours "
                "(9:30 AM – 5:30 PM).")

    _, p = find(doc, "Knowledge and Abilities")
    t = next_table(p)
    drop(t)
    drop(p._p)

    _, p = find(doc, "Course page — https://www.tertiarycourses.com.sg/wsq-", exact=False)
    set_para(p, f"Course page — {PAGE}")
    _, p = find(doc, "Courseware and the assessment are on the LMS", exact=False)
    set_para(p, MATERIALS)
    drop_section(doc, "Assessment Flow")

    for p in all_paras(doc):
        if not (p.text.startswith("Agent:") and "Slides:" in p.text):   # lab_meta did these
            sub_para(p, [SLIDE_RX])
    fix_numbering(doc)
    _check(doc, "LG")
    doc.save(OUT / "LG-Agentic AI for Video Creation.docx")


BAD = re.compile(r"\b[KA][1-7]\b|\bWA\b|\bPP\b|Written Assessment|Practical Performance|TRAQOM|"
                 r"SkillsFuture|\bSSG\b|(?<!non-)\bWSQ\b|TGS-|\bLU\d|Learning Unit|funding|"
                 r"assessment|assessor|6:30|Facilitator Guide|Assessment Plan|competen", re.I)


def _check(doc, name):
    hits = [p.text[:140] for p in all_paras(doc) if BAD.search(p.text)]
    for h in hits:
        print(f"  {name} CHECK: {h}")


if __name__ == "__main__":
    convert_lp()
    convert_lg()
    print("wrote LP + LG")
    for t in FALLBACK:
        print("  formatting flattened:", t)
