#!/usr/bin/env python3
"""Re-apply path rewrites across all markdown and config files."""
import os
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent

PATH_REWRITES = [
    ("core/hwre/hydraulics/",           "core/hwre/hydraulics/"),
    ("core/hwre/open_channel_flow/",    "core/hwre/open_channel_flow/"),
    ("core/hwre/hydrology/",            "core/hwre/hydrology/"),
    ("core/hwre/water_resources/",      "core/hwre/water_resources/"),
    ("core/hwre/exam_notes/",            "core/hwre/exam_notes/"),
    ("core/hwre/flood_control/",         "core/hwre/flood_control/"),
    ("core/hwre/hydraulics_notes/",      "core/hwre/hydraulics_notes/"),
    ("core/hwre/irrigation/",            "core/hwre/irrigation/"),
    ("core/hwre/wastewater/",            "core/hwre/wastewater/"),
    ("core/hwre/water_supply/",          "core/hwre/water_supply/"),
    ("core/structures/",           "core/structures/"),
    ("core/geotechnical/",         "core/geotechnical/"),
    ("core/environmental/",        "core/environmental/"),
    ("core/transportation/",       "core/transportation/"),
    ("core/geoinformatics/",       "core/geoinformatics/"),
    ("core/infrastructure/",       "core/infrastructure/"),
    ("core/fundamentals/",         "core/fundamentals/"),
    ("core/gate/",                       "core/gate/"),
    ("non-core/aptitude/",                   "non-core/aptitude/"),
    ("non-core/analytics/technical-stack.md","non-core/analytics/technical-stack.md"),
    ("non-core/analytics/non-core-prep.md",  "non-core/analytics/non-core-prep.md"),
    ("prep/behavioral/",                 "prep/behavioral/"),
    ("prep/company-profiles/","prep/company-profiles/"),
    ("prep/mock-tests/",  "prep/mock-tests/"),
    ("prep/hr/",              "prep/hr/"),
    ("prep/technical/",       "prep/technical/"),
    ("prep/templates/",                  "prep/templates/"),
    ("docs/roadmap.md",        "docs/roadmap.md"),
    ("docs/setup.md",                    "docs/setup.md"),
    ("docs/fable-mode-setup.md",         "docs/docs/fable-mode-setup.md"),
]

SKIP_DIRS = {".git", "__pycache__", "node_modules", ".vscode", ".idea", ".roo"}

def update_file(filepath):
    try:
        content = filepath.read_text(encoding="utf-8")
    except Exception:
        return False
    original = content
    for old, new in sorted(PATH_REWRITES, key=lambda x: -len(x[0])):
        content = content.replace(old, new)
    if content != original:
        filepath.write_text(content, encoding="utf-8")
        return True
    return False

def main():
    updated = 0
    for root, dirs, files in os.walk(REPO):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for f in files:
            if f.endswith((".md", ".py", ".yml", ".yaml")):
                fp = Path(root) / f
                if update_file(fp):
                    updated += 1
                    print(f"  Updated: {fp.relative_to(REPO)}")
    print(f"\nTotal: {updated} files updated")

if __name__ == "__main__":
    main()
