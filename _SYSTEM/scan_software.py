"""Scan software-and-tech/ for word counts and heading structure."""
import os
import re

ROOT = r"DKS_IITK_Civil_HWRE_Placement_2026/software-and-tech"
OUT = r"DKS_IITK_Civil_HWRE_Placement_2026/_SYSTEM/SOFTWARE_SCAN.txt"

rows = []
for dirpath, _, files in os.walk(ROOT):
    for f in sorted(files):
        if f.endswith(".md"):
            p = os.path.join(dirpath, f)
            with open(p, encoding="utf-8", errors="ignore") as fh:
                t = fh.read()
            words = len(t.split())
            h1 = len(re.findall(r"^# ", t, re.M))
            h2 = len(re.findall(r"^## ", t, re.M))
            h3 = len(re.findall(r"^### ", t, re.M))
            rows.append((p, words, h1, h2, h3))

lines = [f"{p}\t{words}\t{h1}\t{h2}\t{h3}" for p, words, h1, h2, h3 in sorted(rows)]
with open(OUT, "w", encoding="utf-8") as fh:
    fh.write("\n".join(lines))
print(f"WROTE {len(lines)} rows to {OUT}")