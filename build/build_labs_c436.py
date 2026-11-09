#!/usr/bin/env python3
"""C436 v4.0 labs: rebuild the WSQ Higgsfield v6.2 lab pack as non-WSQ.

Runs the WSQ lab builder (read-only import from the WSQ course's build/
folder) with the WSQ layer stripped: course code C436, no K & A tags, no
assessment references, slide ranges remapped to the 167-slide non-WSQ deck,
and Day 2 lab times rescaled onto the 450-minute non-WSQ day.

  python3 build/build_labs_c436.py
"""
import json, re, shutil, sys
from pathlib import Path

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[1]
WSQ_BUILD = Path("/Users/alfredang/Documents/Supporting Document/Tertiary Infotech/"
                 "Tertiary WSQ Projects/TGS-2023036088-Agentic AI for Video Creation/"
                 "courseware_higgsfield/build")
sys.path.insert(0, str(WSQ_BUILD))
import build_labs as BL  # noqa: E402
import vc_labs, vc_lab_assets  # noqa: E402

SMAP = {int(k): v for k, v in json.loads((ROOT / "build/slide_map_c436.json").read_text()).items()}
MINUTES = {5: 80, 6: 80, 7: 70}   # proportional rescale onto 450 min/day (see LP)

TEXT_SUBS = [
    (r"\s*\(the video PP Task 3 asks you to upload\)", ""),
    (r"Your film is the evidence for PP Task 3: export it as", "Export your film as"),
    (r"\s*—\s*the video PP Task 3 asks you to\s+upload to the LMS\.", "."),
    (r": it is the video they upload for PP Task 3\.", ": it is the film they screen at the end."),
    (r"TGS-2023036088", "C436"),
    (r"\s*\((?:ability )?[KA]\d\)", ""),
    (r"\b(is|are) the [KA]\d (skill|ability|knowledge)", r"\1 the \2 at work here"),
]


def clean(v):
    if isinstance(v, str):
        for rx, rep in TEXT_SUBS:
            v = re.sub(rx, rep, v)
        return v
    if isinstance(v, list):
        return [clean(x) for x in v]
    if isinstance(v, tuple):
        return tuple(clean(x) for x in v)
    if isinstance(v, dict):
        return {k: clean(x) for k, x in v.items()}
    return v


def main():
    labs_dir = ROOT / "labs"
    if labs_dir.exists():
        shutil.rmtree(labs_dir)
    # start from the WSQ lab tree so binary assets (mock clips, images) carry over
    shutil.copytree(ROOT / "source-wsq/labs", labs_dir)
    for p in labs_dir.rglob("*.pdf"):
        p.unlink()          # every PDF is regenerated below

    BL.LABS_DIR = labs_dir
    BL.CODE = "C436"
    # remap the WSQ deck's lab slide ranges onto the non-WSQ deck
    m = BL.MAP
    m["labs"] = {k: [SMAP[a], SMAP[b]] for k, (a, b) in m["labs"].items()}
    for i, lab in enumerate(BL.LABS):
        lab = clean(lab)
        lab["ka"] = ""
        if lab["n"] in MINUTES:
            lab["minutes"] = MINUTES[lab["n"]]
        BL.LABS[i] = lab
    for n, files in BL.ASSETS.items():
        BL.ASSETS[n] = {rel: clean(v) for rel, v in files.items()}

    # strip the K & A tag / column and the assessment hand-off from the generators
    rm, pm, im, ih, ph = BL.readme_md, BL.prompts_md, BL.index_md, BL.index_html, BL.prompts_html

    def readme(lab):
        s = rm(lab).replace(" ·  **", "**").replace(" · **  ", "**  ")
        s = s.replace("Bring your evidence to the Practical Performance assessment.",
                      "Keep your evidence: it is your portfolio from the course.")
        return s

    def index():
        s = im()
        s = s.replace("| Lab | Day | Tools | Time | K & A |", "| Lab | Day | Tools | Time |")
        s = s.replace("|---|---|---|---|---|", "|---|---|---|---|")
        return re.sub(r"( min) \|  \|\n", r"\1 |\n", s)

    def prompts_html(lab):
        return ph(lab).replace(" minutes · </p>", " minutes</p>")

    BL.readme_md, BL.index_md, BL.prompts_html = readme, index, prompts_html
    n, jobs = BL.build()
    # the prompt builder is copied verbatim by build(); recode it
    pb = labs_dir / "prompt-builder.html"
    pb.write_text(pb.read_text(encoding="utf-8").replace("TGS-2023036088", "C436"), encoding="utf-8")
    print(f"{n} labs, {jobs} PDFs -> {labs_dir}")


if __name__ == "__main__":
    main()
