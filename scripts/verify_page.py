#!/usr/bin/env python3
"""
verify_page.py — Generic single-page structural and quality verification tool.
Usage:
    python scripts/verify_page.py <path_to_markdown_file> [--profile rcc|general]

Checks:
- Line and byte count against recommended thresholds
- Heading hierarchy (H1, H2, H3)
- Table formatting and mathematical delimiters ($)
- Interview section categories (A-G taxonomy)
- Relative cross-link resolution
"""

import sys
import re
from pathlib import Path

# Add parent directory to sys.path to import config
sys.path.insert(0, str(Path(__file__).resolve().parent))
from config import REPO_ROOT, MAX_RECOMMENDED_LINES

def verify_file(filepath: Path, profile: str = "general"):
    if not filepath.exists():
        print(f"[ERROR] File not found: {filepath}")
        return False

    try:
        content = filepath.read_text(encoding="utf-8")
    except Exception as e:
        print(f"[ERROR] Could not read file: {e}")
        return False

    lines = content.splitlines()
    rel_path = filepath.relative_to(REPO_ROOT) if filepath.is_relative_to(REPO_ROOT) else filepath

    print(f"\n{'='*60}")
    print(f"PAGE VERIFICATION: {rel_path}")
    print(f"{'='*60}")
    print(f"Lines: {len(lines)} (Max recommended: {MAX_RECOMMENDED_LINES})")
    print(f"Bytes: {len(content.encode('utf-8')):,}")

    h1_lines = [l for l in lines if l.startswith("# ")]
    h2_count = sum(1 for l in lines if l.startswith("## "))
    h3_count = sum(1 for l in lines if l.startswith("### "))
    table_lines = sum(1 for l in lines if l.startswith("|"))
    formula_count = content.count("$")

    print(f"H1 Heading: {h1_lines[0] if h1_lines else '[MISSING]'}")
    if len(h1_lines) > 1:
        print(f"  [WARNING] Multiple H1 headings found ({len(h1_lines)})")
    print(f"H2 Sections: {h2_count}")
    print(f"H3 Subsections: {h3_count}")
    print(f"Table Lines: {table_lines}")
    print(f"Formula Delimiters ($): {formula_count}")

    # Check interview categories if technical/interview page
    print("\nInterview Question Categories (A-G Taxonomy):")
    categories = [
        "### A. Basic", "### B. WHY", "### C. WHAT-IF", "### D. Comparison",
        "### E. Numerical", "### F. Rapid-Fire", "### G. Deep"
    ]
    present_cats = 0
    for cat in categories:
        found = cat in content
        if found:
            present_cats += 1
        print(f"  [{'OK' if found else '—'}] {cat}")
    print(f"Categories matched: {present_cats}/{len(categories)}")

    # Specific Profile Checks
    if profile.lower() == "rcc":
        print("\nRCC Specific Core Sections:")
        rcc_required = [
            "## 1. Concrete Properties", "## 2. Working Stress",
            "## 3. Flexural Design", "## 4. Doubly Reinforced",
            "## 6. Shear Design", "## 7. Bond & Development",
            "## 12. IS 456", "## 13. Worked Numerical", "## References"
        ]
        rcc_missing = [s for s in rcc_required if s not in content]
        if rcc_missing:
            print(f"  [WARNING] Missing expected RCC sections: {rcc_missing}")
        else:
            print("  [OK] All core RCC sections present.")

    # Cross-link validation
    print("\nRelative Cross-link Verification:")
    link_pattern = r'\[([^\]]*)\]\(([^)]+)\)'
    broken_links = []
    total_links = 0

    # Strip code blocks to avoid false positives in code snippets
    code_stripped = re.sub(r'^```.*?^```', '', content, flags=re.MULTILINE | re.DOTALL)
    for m in re.finditer(link_pattern, code_stripped):
        target = m.group(2).split("#")[0].strip()
        if not target or target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        total_links += 1
        resolved = (filepath.parent / target).resolve()
        if resolved.is_dir():
            resolved = resolved / "README.md"
        elif not resolved.suffix and not resolved.exists():
            resolved = resolved.with_suffix(".md")

        if not resolved.exists():
            broken_links.append((target, str(resolved)))

    print(f"Total internal links checked: {total_links}")
    if broken_links:
        print(f"  [FAIL] Broken links ({len(broken_links)}):")
        for tgt, res in broken_links:
            print(f"    - {tgt} (resolved to {res})")
    else:
        print("  [OK] All internal cross-links resolved cleanly.")

    print(f"{'='*60}")
    print(f"RESULT: {'PASS' if not broken_links and h1_lines else 'ISSUES DETECTED'}\n")
    return len(broken_links) == 0

def main():
    if len(sys.argv) < 2:
        target = REPO_ROOT / "core" / "rcc" / "rcc-design.md"
        profile = "rcc"
    else:
        target = Path(sys.argv[1])
        if not target.is_absolute():
            target = REPO_ROOT / target
        profile = "general"
        if "--profile" in sys.argv:
            idx = sys.argv.index("--profile")
            if idx + 1 < len(sys.argv):
                profile = sys.argv[idx + 1]
        elif "rcc" in target.name.lower():
            profile = "rcc"

    success = verify_file(target, profile)
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
