#!/usr/bin/env python3
"""Rewrite the page numbers of a tab-style TOC ("Label<TAB>N") from the rendered PDF."""
import sys, re, fitz
from docx import Document

def run(docx, pdf):
    doc = Document(docx); pd = fitz.open(pdf)
    toc = [p for p in doc.paragraphs[:80] if "\t" in p.text and re.search(r"\t\d+$", p.text)]
    pages = [[ln.strip() for ln in pg.get_text().splitlines()] for pg in pd]
    toc_pg = next(i for i, ls in enumerate(pages) if "TABLE OF CONTENTS" in ls)
    start, changed = toc_pg + 1, 0
    for p in toc:
        label = p.text.split("\t")[0].strip()
        hit = next((i for i in range(start, len(pages)) if label in pages[i]), None)
        if hit is None:   # long headings wrap: match the joined page text
            norm = lambda t: re.sub(r"\s+", "", t)
            hit = next((i for i in range(start, len(pages))
                        if norm(label) in norm(" ".join(pages[i]))), None)
        if hit is None:
            print("  not found:", label); continue
        start = hit
        new = str(hit + 1)
        r = [r for r in p.runs if re.search(r"\d+$", r.text)][-1]
        old = re.search(r"\d+$", r.text).group()
        if old != new:
            r.text = re.sub(r"\d+$", new, r.text); changed += 1
    doc.save(docx)
    print(f"{docx}: {changed} TOC page numbers updated")

if __name__ == "__main__":
    run(sys.argv[1], sys.argv[2])
