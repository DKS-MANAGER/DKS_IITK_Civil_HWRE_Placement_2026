#!/usr/bin/env python3
"""Analyze heading issues: distinguish BOM-caused false positives from true issues."""
import os
import re
from pathlib import Path

root = Path(".").resolve()
md_files = [p for p in root.rglob("*.md") if not any(part.startswith(".") for part in p.relative_to(root).parts)]

no_h1 = []
multi_h1 = []
bom_count = 0
bom_with_h1 = 0
true_no_h1 = []

for p in md_files:
    content = p.read_text(encoding="utf-8", errors="ignore")
    has_bom = content.startswith("\ufeff")
    if has_bom:
        bom_count += 1
    stripped = content.lstrip("\ufeff")
    h1_count = len(re.findall(r"^# [^#]", stripped, re.MULTILINE))
    if h1_count == 0:
        no_h1.append(str(p.relative_to(root)))
        if has_bom:
            bom_with_h1 += 1
        else:
            true_no_h1.append(str(p.relative_to(root)))
    elif h1_count > 1:
        multi_h1.append((str(p.relative_to(root)), h1_count))

print(f"Total md files: {len(md_files)}")
print(f"Files with BOM: {bom_count}")
print(f"Files flagged no-H1: {len(no_h1)}")
print(f"  - of which have BOM: {bom_with_h1}")
print(f"  - TRUE no-H1 (no BOM): {len(true_no_h1)}")
print()
print("TRUE no-H1 files (no BOM):")
for f in true_no_h1:
    print(f"  {f}")
print()
print("Multiple H1 files:")
for f, c in multi_h1:
    print(f"  {f}: {c}")