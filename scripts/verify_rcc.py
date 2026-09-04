#!/usr/bin/env python3
"""Verify RCC design page structure and content quality (cp1252-safe)."""
import os, re, sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILE = os.path.join(BASE, "core", "rcc", "rcc-design.md")
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "verify_rcc_report.txt")

def main():
    with open(FILE, "r", encoding="utf-8") as f:
        content = f.read()
    lines = content.split("\n")

    out = []
    out.append("=== RCC DESIGN PAGE VERIFICATION ===")
    out.append(f"File: core/rcc/rcc-design.md")
    out.append(f"Lines: {len(lines)}")
    out.append(f"Bytes: {len(content.encode('utf-8'))}")
    out.append(f"H1: {lines[0]}")
    out.append(f"H2 sections: {sum(1 for l in lines if l.startswith('## '))}")
    out.append(f"H3 subsections: {sum(1 for l in lines if l.startswith('### '))}")
    out.append(f"Tables: {sum(1 for l in lines if l.startswith('|'))}")
    out.append(f"Formula delimiters: {content.count(chr(36))}")

    # Required sections (use plain-text markers to avoid emoji encoding issues)
    required = [
        "## Scope", "## 1. Concrete Properties", "## 2. Working Stress",
        "## 3. Flexural Design", "## 4. Doubly Reinforced", "## 5. Flanged Beams",
        "## 6. Shear Design", "## 7. Bond & Development", "## 8. Slab Design",
        "## 9. Column Design", "## 10. Footing Design", "## 11. Prestressed",
        "## 12. IS 456", "## 13. Worked Numerical", "## 14.",
        "## 15. High-Value", "## 16. Software", "## 17.",
        "## 18.", "## 19.", "## References"
    ]
    out.append("")
    out.append("Section presence check:")
    missing = []
    for sec in required:
        found = sec in content
        status = "OK" if found else "MISSING"
        if not found:
            missing.append(sec)
        out.append(f"  [{status}] {sec}")

    # Interview question categories
    out.append("")
    out.append("Interview question categories:")
    for cat in ["### A. Basic", "### B. WHY", "### C. WHAT-IF", "### D. Comparison",
                "### E. Numerical", "### F. Rapid-Fire", "### G. Deep"]:
        found = cat in content
        out.append(f"  [{'OK' if found else 'MISSING'}] {cat}")

    # Cross-links resolve
    out.append("")
    out.append("Cross-link targets:")
    for m in re.finditer(r'\]\(\.\./([^)]+\.md)\)', content):
        target = m.group(1)
        tpath = os.path.normpath(os.path.join(BASE, "core", "rcc", target))
        exists = os.path.exists(tpath)
        out.append(f"  [{'OK' if exists else 'BROKEN'}] {target}")

    out.append("")
    out.append(f"Missing sections: {len(missing)}")
    if missing:
        out.append("  " + ", ".join(missing))
    out.append("")
    out.append("VERIFICATION COMPLETE")

    with open(OUT, "w", encoding="utf-8") as f:
        f.write("\n".join(out))
    print(f"Report written to {OUT}")
    print(f"Lines: {len(lines)} | Bytes: {len(content.encode('utf-8'))} | Missing: {len(missing)}")

if __name__ == "__main__":
    main()
