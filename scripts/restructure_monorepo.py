#!/usr/bin/env python3
"""
restructure_monorepo.py

One-shot monorepo restructuring: moves files, creates new directory layout,
and updates all internal markdown links in a single atomic pass.

Target topology:
  core/hwre/           ← civil/{hydraulics,open_channel_flow,hydrology,water_resources} + hwre/*
  core/structures/     ← core/structures/
  core/geotechnical/   ← core/geotechnical/
  core/environmental/  ← core/environmental/
  core/transportation/ ← core/transportation/
  core/geoinformatics/ ← core/geoinformatics/
  core/infrastructure/ ← core/infrastructure/
  core/fundamentals/   ← core/fundamentals/
  core/core/gate/           ← core/gate/*
  non-core/non-core/aptitude/ ← non-core/aptitude/*
  non-core/analytics/ ← resources/{technical-stack,non-core-prep}
  prep/prep/behavioral/ ← prep/behavioral/*
  prep/company-profiles/ ← prep/company-profiles/
  prep/mock-tests/ ← prep/mock-tests/
  prep/prep/templates/  ← prep/templates/*
  prep/hr/         ← prep/hr/
  prep/technical/  ← prep/technical/
  docs/            ← docs/roadmap.md, docs/setup.md, docs/docs/fable-mode-setup.md
  resources/       ← remaining resources (books, links, papers, gis-tools, placement-data)
  index/           ← index (unchanged, paths updated in master_index.md)
  scripts/         ← scripts (unchanged)
"""

import os
import shutil
import re
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent


# ============================================================
# 1. MOVE MAP: (source_relative, target_relative)
# ============================================================
MOVE_MAP = [
    # --- core/hwre (unified fluid mechanics / water resources) ---
    ("civil/hydraulics",           "core/hwre/hydraulics"),
    ("civil/open_channel_flow",    "core/hwre/open_channel_flow"),
    ("civil/hydrology",            "core/hwre/hydrology"),
    ("civil/water_resources",      "core/hwre/water_resources"),
    ("hwre/exam_notes",            "core/hwre/exam_notes"),
    ("hwre/flood_control",         "core/hwre/flood_control"),
    ("hwre/hydraulics_notes",      "core/hwre/hydraulics_notes"),
    ("hwre/irrigation",            "core/hwre/irrigation"),
    ("hwre/wastewater",            "core/hwre/wastewater"),
    ("hwre/water_supply",          "core/hwre/water_supply"),

    # --- core/branches (each civil branch as its own folder) ---
    ("civil/structures",           "core/structures"),
    ("civil/geotechnical",         "core/geotechnical"),
    ("civil/environmental",        "core/environmental"),
    ("civil/transportation",       "core/transportation"),
    ("civil/geoinformatics",       "core/geoinformatics"),
    ("civil/infrastructure",       "core/infrastructure"),
    ("civil/fundamentals",         "core/fundamentals"),

    # --- core/gate ---
    ("gate",                       "core/gate"),

    # --- non-core ---
    ("aptitude",                   "non-core/aptitude"),

    # --- prep ---
    ("behavioral",                 "prep/behavioral"),
    ("interviews/company_specific","prep/company-profiles"),
    ("interviews/mock_questions",  "prep/mock-tests"),
    ("interviews/hr",              "prep/hr"),
    ("interviews/technical",       "prep/technical"),
    ("templates",                  "prep/templates"),

    # --- docs ---
    ("docs/roadmap.md",       "docs/roadmap.md"),
    ("docs/setup.md",                   "docs/setup.md"),
    ("docs/docs/fable-mode-setup.md",        "docs/docs/docs/fable-mode-setup.md"),
]

# Files from resources that move to non-core/analytics
ANALYTICS_FILES = [
    ("non-core/analytics/technical-stack.md",  "non-core/analytics/technical-stack.md"),
    ("non-core/analytics/non-core-prep.md",    "non-core/analytics/non-core-prep.md"),
]

# ============================================================
# 2. PATH REWRITE RULES (old_prefix → new_prefix)
# ============================================================
PATH_REWRITES = [
    # core/hwre
    ("core/hwre/hydraulics/",           "core/hwre/hydraulics/"),
    ("core/hwre/open_channel_flow/",    "core/hwre/open_channel_flow/"),
    ("core/hwre/hydrology/",            "core/hwre/hydrology/"),
    ("core/hwre/water_resources/",      "core/hwre/water_resources/"),
    ("core/hwre/exam_notes/",            "core/core/hwre/exam_notes/"),
    ("core/hwre/flood_control/",         "core/core/hwre/flood_control/"),
    ("core/hwre/hydraulics_notes/",      "core/core/hwre/hydraulics_notes/"),
    ("core/hwre/irrigation/",            "core/core/hwre/irrigation/"),
    ("core/hwre/wastewater/",            "core/core/hwre/wastewater/"),
    ("core/hwre/water_supply/",          "core/core/hwre/water_supply/"),
    # core/branches
    ("core/structures/",           "core/structures/"),
    ("core/geotechnical/",         "core/geotechnical/"),
    ("core/environmental/",        "core/environmental/"),
    ("core/transportation/",       "core/transportation/"),
    ("core/geoinformatics/",       "core/geoinformatics/"),
    ("core/infrastructure/",       "core/infrastructure/"),
    ("core/fundamentals/",         "core/fundamentals/"),
    # core/gate
    ("core/gate/",                       "core/core/gate/"),
    # non-core
    ("non-core/aptitude/",                   "non-core/non-core/aptitude/"),
    # analytics from resources
    ("non-core/analytics/technical-stack.md","non-core/analytics/technical-stack.md"),
    ("non-core/analytics/non-core-prep.md",  "non-core/analytics/non-core-prep.md"),
    # prep
    ("prep/behavioral/",                 "prep/prep/behavioral/"),
    ("prep/company-profiles/","prep/company-profiles/"),
    ("prep/mock-tests/",  "prep/mock-tests/"),
    ("prep/hr/",              "prep/hr/"),
    ("prep/technical/",       "prep/technical/"),
    ("prep/templates/",                  "prep/prep/templates/"),
    # docs
    ("docs/roadmap.md",        "docs/roadmap.md"),
    ("docs/setup.md",                    "docs/setup.md"),
    ("docs/docs/fable-mode-setup.md",         "docs/docs/docs/fable-mode-setup.md"),
]


def create_directories():
    """Create all new top-level directories."""
    new_dirs = [
        "core/hwre", "core/structures", "core/geotechnical",
        "core/environmental", "core/transportation", "core/geoinformatics",
        "core/infrastructure", "core/fundamentals", "core/gate",
        "non-core/aptitude", "non-core/analytics",
        "prep/behavioral", "prep/company-profiles", "prep/mock-tests",
        "prep/templates", "prep/hr", "prep/technical",
        "docs",
    ]
    for d in new_dirs:
        (REPO / d).mkdir(parents=True, exist_ok=True)
    print(f"[OK] Created {len(new_dirs)} new directories")


def move_files():
    """Move all directories and files according to MOVE_MAP."""
    moved = 0
    for src_rel, dst_rel in MOVE_MAP:
        src = REPO / src_rel
        dst = REPO / dst_rel
        if not src.exists():
            print(f"[SKIP] Source not found: {src_rel}")
            continue
        if dst.exists():
            # If dst is an empty dir, remove it and re-move
            if dst.is_dir() and not any(dst.iterdir()):
                dst.rmdir()
                print(f"  [RMDIR] {dst_rel} (empty)")
            else:
                print(f"[WARN] Destination non-empty: {dst_rel}")
                continue
        shutil.move(str(src), str(dst))
        moved += 1
        print(f"  [MOVE] {src_rel} -> {dst_rel}")
    # Analytics files
    for src_rel, dst_rel in ANALYTICS_FILES:
        src = REPO / src_rel
        dst = REPO / dst_rel
        if not src.exists():
            print(f"[SKIP] Source not found: {src_rel}")
            continue
        if dst.exists():
            print(f"[WARN] Destination exists: {dst_rel}")
            continue
        shutil.move(str(src), str(dst))
        moved += 1
        print(f"  [MOVE] {src_rel} -> {dst_rel}")
    print(f"[OK] Moved {moved} items")


def cleanup_empty_dirs():
    """Remove empty source directories after moves."""
    removed = 0
    for d in ["civil", "hwre", "gate", "aptitude", "behavioral",
              "interviews", "templates"]:
        path = REPO / d
        if path.exists() and not any(path.iterdir()):
            path.rmdir()
            removed += 1
            print(f"  [RMDIR] {d}/ (empty)")
    print(f"[OK] Removed {removed} empty directories")


def update_markdown_links(filepath):
    """Rewrite all internal markdown links in a file using PATH_REWRITES."""
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


def update_all_links():
    """Walk entire repo and update links in all markdown files."""
    skip_dirs = {".git", "__pycache__", "node_modules", ".vscode", ".idea", ".roo"}
    updated = 0
    for root, dirs, files in os.walk(REPO):
        dirs[:] = [d for d in dirs if d not in skip_dirs]
        for f in files:
            if f.endswith((".md", ".py", ".yml", ".yaml")):
                fp = Path(root) / f
                if update_markdown_links(fp):
                    updated += 1
                    rel = fp.relative_to(REPO)
                    print(f"  [LINK] Updated: {rel}")
    print(f"[OK] Updated links in {updated} files")


def update_validate_index():
    """Update the categorize() function in validate_index.py to use new top-level dirs."""
    vpath = REPO / "scripts" / "validate_index.py"
    if not vpath.exists():
        print("[WARN] validate_index.py not found")
        return
    content = vpath.read_text(encoding="utf-8")

    # Update categorize function
    old_cat = 'if parts[0] in {"aptitude", "behavioral", "civil", "gate", "hwre", "interviews", "resources", "templates"}:'
    new_cat = 'if parts[0] in {"core", "non-core", "prep", "resources", "index", "scripts"}:'
    content = content.replace(old_cat, new_cat)

    # Update the return line
    old_ret = '        return parts[0]\n    return "root"'
    new_ret = '        return parts[0]\n    return "root"'
    # Already fine

    # Also update skip_dirs to include new top-level dirs that are folders
    old_skip = 'skip_dirs = {".git", "__pycache__", "node_modules", ".vscode", ".idea"}'
    new_skip = 'skip_dirs = {".git", "__pycache__", "node_modules", ".vscode", ".idea", ".roo"}'
    content = content.replace(old_skip, new_skip)

    if content != vpath.read_text(encoding="utf-8"):
        vpath.write_text(content, encoding="utf-8")
        print("[OK] Updated validate_index.py categorize function")
    else:
        print("[OK] validate_index.py already up to date")


def main():
    print("=" * 60)
    print("MONOREPO RESTRUCTURING")
    print("=" * 60)

    print("\n--- Step 1: Create directories ---")
    create_directories()

    print("\n--- Step 2: Move files ---")
    move_files()

    print("\n--- Step 3: Cleanup empty dirs ---")
    cleanup_empty_dirs()

    print("\n--- Step 4: Update markdown links ---")
    update_all_links()

    print("\n--- Step 5: Update validate_index.py ---")
    update_validate_index()

    print("\n" + "=" * 60)
    print("RESTRUCTURING COMPLETE")
    print("=" * 60)


if __name__ == "__main__":
    main()
