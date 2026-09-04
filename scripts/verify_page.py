#!/usr/bin/env python3
"""Generic page verification (cp1252-safe). Usage: python verify_page.py <relpath>"""
import os, re, sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "verify_page_report.txt")

def main():
    rel = sys.argv[1] if len(sys.argv) > 1 else "core/steel/steel-design.md"
    FILE = os.path.join(BASE, rel)
    with open(FILE, "r", encoding="utf-8") as f:
        content = f.read()
    lines = content.split("\n")

    out = []
    out.append(f"=== PAGE VERIFICATION: {rel} ===")
    out.append(f"Lines: {len(lines)}")
    out.append(f"Bytes: {len(content.encode('utf-8'))}")
    out.append(f"H1: {lines[0]}")
    out.append(f"H2 sections: {sum(1 for l in lines if l.startswith('## '))}")
    out.append(f"H3 subsections: {sum(1 for l in lines if l.startswith('### '))}")
    out.append(f"Tables: {sum(1 for l in lines if l.startswith('|'))}")
    out.append(f"Formula delimiters: {content.count(chr(36))}")

    # Interview question categories
    out.append("")
    out.append("Interview question categories:")
    for cat in ["### A. Basic", "### B. WHY", "### C. WHAT-IF", "### D. Comparison",
                "### E. Numerical", "### F. Rapid-Fire", "### G. Deep"]:
        found = cat in content
        out.append(f"  [{'OK' if found else 'MISSING'}] {cat}")

    # Cross-links resolve (handle ../ prefix correctly)
    out.append("")
    out.append("Cross-link targets:")
    broken = 0
    for m in re.finditer(r'\]\(\.\./([^)]+\.md)\)', content):
        target = m.group(1)
        # resolve relative to the file's directory
        filedir = os.path.dirname(FILE)
        tpath = os.path.normpath(os.path.join(filedir, "..", target))
        exists = os.path.exists(tpath)
        if not exists:
            broken += 1
        out.append(f"  [{'OK' if exists else 'BROKEN'}] {target}")

    out.append("")
    out.append(f"Broken cross-links: {broken}")
    out.append("VERIFICATION COMPLETE")

    with open(OUT, "w", encoding="utf-8") as f:
        f.write("\n".join(out))
    print(f"Report written to {OUT}")
    print(f"Lines: {len(lines)} | Bytes: {len(content.encode('utf-8'))} | Broken links: {broken}")

if __name__ == "__main__":
    main()
