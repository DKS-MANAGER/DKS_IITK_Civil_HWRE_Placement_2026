"""Verify software-and-tech/ rebuild: file existence + link integrity + content checks."""
import os
import re

ROOT = r"DKS_IITK_Civil_HWRE_Placement_2026/software-and-tech"
OUT = r"DKS_IITK_Civil_HWRE_Placement_2026/_SYSTEM/SOFTWARE_VERIFY.txt"

lines = []
errors = []

# 1. Required new files
required = [
    "_SYSTEM/SOFTWARE_AUDIT_STATE.md",
    "_SYSTEM/SOFTWARE_REPO_MAP.md",
    "_SYSTEM/SOFTWARE_CONTENT_REGISTRY.md",
    "_SYSTEM/SOFTWARE_REQUIRED_FILES.md",
    "SOFTWARE_ROLE_MATRIX.md",
    "SOFTWARE_ROADMAP.md",
    "TOOLS_INDEX.md",
    "SOFTWARE_COMPLETENESS_MATRIX.md",
    "SOFTWARE_RESUME_STRATEGY.md",
    "SOFTWARE_COMPANY_LINKAGE.md",
    "SOFTWARE_THEORY_LINKAGE.md",
    "tools/AutoCAD.md",
    "tools/Excel.md",
    "tools/ETABS.md",
    "tools/STAAD.md",
    "tools/QGIS.md",
    "tools/Primavera.md",
    "tools/Revit.md",
    "tools/SAP2000.md",
    "practice/README.md",
    "tests/README.md",
]

lines.append("=== 1. REQUIRED FILE EXISTENCE ===")
for f in required:
    p = os.path.join(ROOT, f)
    ok = os.path.isfile(p)
    lines.append(f"{'OK ' if ok else 'MISSING'} {f}")
    if not ok:
        errors.append(f"Missing required file: {f}")

# 2. Link integrity: check all relative .md links in new files
lines.append("\n=== 2. LINK INTEGRITY ===")
link_files = required + ["README.md"]
for f in link_files:
    p = os.path.join(ROOT, f)
    if not os.path.isfile(p):
        continue
    with open(p, encoding="utf-8", errors="ignore") as fh:
        text = fh.read()
    # find markdown links (relative, .md)
    for m in re.finditer(r"\]\(([^)]+\.md)(?:#[^)]*)?\)", text):
        target = m.group(1)
        if target.startswith("http") or target.startswith("#"):
            continue
        # resolve relative to file's dir
        base = os.path.dirname(p)
        resolved = os.path.normpath(os.path.join(base, target))
        if not os.path.isfile(resolved):
            errors.append(f"BROKEN LINK in {f}: {target}")
            lines.append(f"BROKEN {f} -> {target}")

lines.append(f"Link check complete. Broken links: {len([e for e in errors if 'BROKEN' in e])}")

# 3. Content completeness: each tool page should have key sections
lines.append("\n=== 3. CONTENT COMPLETENESS (tool pages) ===")
sections_required = [
    "What It Is", "Where It Is Used", "Why Your Target Role Needs It",
    "Installation", "Core Interface", "Essential Features", "Typical Engineering Workflow",
    "Worked Example", "Practice Exercises", "Mini-Project", "Common Mistakes",
    "Interview Questions", "Rapid Revision", "Theory Linkage", "Company Linkage",
]
for f in ["tools/AutoCAD.md", "tools/Excel.md", "tools/ETABS.md", "tools/STAAD.md",
          "tools/QGIS.md", "tools/Primavera.md", "tools/Revit.md", "tools/SAP2000.md"]:
    p = os.path.join(ROOT, f)
    with open(p, encoding="utf-8", errors="ignore") as fh:
        text = fh.read()
    missing = [s for s in sections_required if s.lower() not in text.lower()]
    score = len(sections_required) - len(missing)
    lines.append(f"{f}: {score}/{len(sections_required)} sections")
    if missing:
        lines.append(f"    MISSING: {', '.join(missing)}")

# 4. Word count summary of new files
lines.append("\n=== 4. NEW FILE WORD COUNTS ===")
total = 0
for f in sorted(required + ["README.md"]):
    p = os.path.join(ROOT, f)
    if os.path.isfile(p):
        with open(p, encoding="utf-8", errors="ignore") as fh:
            w = len(fh.read().split())
        total += w
        lines.append(f"{f}: {w} words")
lines.append(f"TOTAL new/updated words: {total}")

with open(OUT, "w", encoding="utf-8") as fh:
    fh.write("\n".join(lines))

print(f"WROTE {len(lines)} lines to {OUT}")
print(f"ERRORS: {len(errors)}")
for e in errors:
    print("  -", e)