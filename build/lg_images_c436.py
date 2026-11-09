#!/usr/bin/env python3
"""Refresh the LG pictures that carry WSQ pixels, in courseware/assets/lg and inside the LG DOCX.

- lab-0N-workflow.png: re-rendered from the C436 deck PDF (the WSQ ones show TGS-… and old page numbers)
- labs-index.png, lab-prompt-page.png: the fresh C436 captures in build/screens/
Pictures are matched in the DOCX by the MD5 of the WSQ original, never by position.
"""
import hashlib, json, shutil, subprocess, tempfile
from pathlib import Path
from docx import Document
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "source-wsq/courseware/assets"
DST = ROOT / "courseware/assets"
DECK_PDF = ROOT / "courseware/Agentic AI for Video Creation-v4.0.pdf"
LG = ROOT / "courseware/LG-Agentic AI for Video Creation.docx"
SMAP = {int(k): v for k, v in json.loads((ROOT / "build/slide_map_c436.json").read_text()).items()}
STEPS_SRC = {1: 69, 2: 83, 3: 96, 4: 117, 5: 139, 6: 157, 7: 167}   # WSQ 1-based "LAB 0N · STEPS"

md5 = lambda b: hashlib.md5(b).hexdigest()

if DST.exists():
    shutil.rmtree(DST)
shutil.copytree(SRC, DST, ignore=shutil.ignore_patterns("wsq-logo.png", "lms-tms-login.png"))

swap = {}
with tempfile.TemporaryDirectory() as td:
    for n, src_page in STEPS_SRC.items():
        f = DST / "lg" / f"lab-{n:02d}-workflow.png"
        w, h = Image.open(f).size
        page = SMAP[src_page]
        subprocess.run(["pdftoppm", "-png", "-singlefile", "-f", str(page), "-l", str(page),
                        "-scale-to-x", str(w), "-scale-to-y", str(h), str(DECK_PDF), f"{td}/p"], check=True)
        old = f.read_bytes()
        shutil.copyfile(f"{td}/p.png", f)
        swap[md5(old)] = f.read_bytes()
for name in ("labs-index.png", "lab-prompt-page.png"):
    f = DST / "lg" / name
    w, h = Image.open(f).size
    old = f.read_bytes()
    Image.open(ROOT / "build/screens" / name).convert("RGB").resize((w, h), Image.LANCZOS).save(f)
    swap[md5(old)] = f.read_bytes()

doc = Document(LG)
done = 0
for rel in doc.part.rels.values():
    if "image" in rel.reltype and not rel.is_external:
        h = md5(rel.target_part.blob)
        if h in swap:
            rel.target_part._blob = swap[h]
            done += 1
doc.save(LG)
print(f"assets refreshed; {done} pictures swapped in the LG (expected {len(swap)})")
