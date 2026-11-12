#!/usr/bin/env python3
"""Render REPORT.md (a small Markdown subset) into a submission-ready .docx.

Supports: headings, paragraphs with **bold** / `code`, bullet and numbered
lists, blockquotes, fenced code blocks, and pipe tables.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

from docx import Document
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Inches, Pt, RGBColor

INLINE = re.compile(r"(\*\*.+?\*\*|`[^`]+`)")


def add_runs(par, text: str) -> None:
    for chunk in INLINE.split(text):
        if not chunk:
            continue
        if chunk.startswith("**") and chunk.endswith("**"):
            run = par.add_run(chunk[2:-2])
            run.bold = True
        elif chunk.startswith("`") and chunk.endswith("`"):
            run = par.add_run(chunk[1:-1])
            run.font.name = "Menlo"
            run.font.size = Pt(9)
        else:
            par.add_run(chunk)


def add_table(doc: Document, rows: list[list[str]]) -> None:
    header, body = rows[0], rows[1:]
    table = doc.add_table(rows=1, cols=len(header))
    table.style = "Light Grid Accent 1"
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    for i, cell in enumerate(header):
        par = table.rows[0].cells[i].paragraphs[0]
        run = par.add_run(cell.strip())
        run.bold = True
        run.font.size = Pt(9)
    for row in body:
        cells = table.add_row().cells
        for i, cell in enumerate(row[: len(header)]):
            par = cells[i].paragraphs[0]
            add_runs(par, cell.strip())
            for run in par.runs:
                run.font.size = Pt(9)
    doc.add_paragraph()


def main() -> int:
    src = Path(sys.argv[1] if len(sys.argv) > 1 else "REPORT.md")
    dst = Path(sys.argv[2] if len(sys.argv) > 2 else "REPORT.docx")

    doc = Document()
    style = doc.styles["Normal"]
    style.font.name = "Calibri"
    style.font.size = Pt(10.5)
    for section in doc.sections:
        section.top_margin = section.bottom_margin = Inches(0.8)
        section.left_margin = section.right_margin = Inches(0.85)

    lines = src.read_text().splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        if stripped.startswith("```"):
            block = []
            i += 1
            while i < len(lines) and not lines[i].strip().startswith("```"):
                block.append(lines[i])
                i += 1
            i += 1
            par = doc.add_paragraph()
            par.paragraph_format.left_indent = Inches(0.25)
            run = par.add_run("\n".join(block))
            run.font.name = "Menlo"
            run.font.size = Pt(8.5)
            run.font.color.rgb = RGBColor(0x33, 0x33, 0x33)
            continue

        if stripped.startswith("|") and i + 1 < len(lines) and set(lines[i + 1].strip()) <= set("|-: "):
            rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                cells = [c for c in lines[i].strip().strip("|").split("|")]
                if not set("".join(cells).strip()) <= set("-: "):
                    rows.append(cells)
                i += 1
            if rows:
                add_table(doc, rows)
            continue

        if stripped.startswith("#"):
            level = len(stripped) - len(stripped.lstrip("#"))
            text = stripped[level:].strip()
            if level == 1:
                par = doc.add_paragraph()
                par.alignment = WD_ALIGN_PARAGRAPH.LEFT
                run = par.add_run(text)
                run.bold = True
                run.font.size = Pt(19)
                par.paragraph_format.space_after = Pt(6)
            else:
                doc.add_heading(text, level=min(level, 3))
            i += 1
            continue

        if stripped == "---":
            i += 1
            continue

        if stripped.startswith("> "):
            par = doc.add_paragraph()
            par.paragraph_format.left_indent = Inches(0.3)
            run = par.add_run(stripped[2:])
            run.italic = True
            run.font.color.rgb = RGBColor(0x44, 0x44, 0x44)
            i += 1
            continue

        if re.match(r"^[-*] ", stripped):
            par = doc.add_paragraph(style="List Bullet")
            add_runs(par, stripped[2:])
            i += 1
            continue

        if re.match(r"^\d+\. ", stripped):
            par = doc.add_paragraph(style="List Number")
            add_runs(par, re.sub(r"^\d+\. ", "", stripped))
            i += 1
            continue

        if not stripped:
            i += 1
            continue

        par = doc.add_paragraph()
        par.paragraph_format.space_after = Pt(4)
        add_runs(par, stripped)
        i += 1

    doc.save(dst)
    print(f"wrote {dst}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
