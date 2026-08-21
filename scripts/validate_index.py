#!/usr/bin/env python3
"""
validate_index.py

Pre-commit hook to validate index/master_index.md references and regenerate
index/file_inventory.csv. Fails the commit if any Destination Path in
master_index.md points to a missing file.
"""

import csv
import os
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
INDEX_DIR = REPO_ROOT / "index"
MASTER_INDEX = INDEX_DIR / "master_index.md"
FILE_INVENTORY = INDEX_DIR / "file_inventory.csv"


def extract_dest_paths(master_index_path):
    paths = []
    with open(master_index_path, "r", encoding="utf-8") as f:
        for line in f:
            stripped = line.strip()
            if not stripped.startswith("|"):
                continue
            if "Destination Path" in stripped or re.match(r"^\|[\s-]+\|", stripped):
                continue
            parts = [p.strip() for p in stripped.strip("|").split("|")]
            if len(parts) >= 5:
                dest = parts[4]
                if dest and dest != "Destination Path":
                    paths.append(dest)
    return paths


def validate_paths(paths):
    missing = []
    for p in paths:
        if p.startswith(("http://", "https://", "mailto:")):
            continue
        target = REPO_ROOT / p
        if not target.exists():
            missing.append(p)
    return missing


def generate_inventory():
    inventory = []
    skip_dirs = {".git", "__pycache__", "node_modules", ".vscode", ".idea"}
    for root, dirs, files in os.walk(REPO_ROOT):
        dirs[:] = sorted([d for d in dirs if d not in skip_dirs])
        for f in sorted(files):
            if f.startswith(".") and f not in {
                ".gitignore",
                ".editorconfig",
                ".pre-commit-config.yaml",
            }:
                continue
            full_path = Path(root) / f
            rel_path = full_path.relative_to(REPO_ROOT)
            try:
                size = full_path.stat().st_size
            except OSError:
                size = 0
            inventory.append(
                {
                    "path": str(rel_path).replace("\\", "/"),
                    "filename": f,
                    "size_bytes": size,
                    "category": categorize(rel_path),
                    "has_references": "",
                    "has_empty_sections": "",
                    "naming_ok": "yes",
                    "topic_match": "yes",
                    "notes": "",
                }
            )
    return inventory


def categorize(rel_path):
    parts = rel_path.parts
    if parts[0] in {"aptitude", "behavioral", "civil", "gate", "hwre", "interviews", "resources", "templates"}:
        return parts[0]
    return "root"


def write_inventory(inventory):
    fieldnames = [
        "path",
        "filename",
        "size_bytes",
        "category",
        "has_references",
        "has_empty_sections",
        "naming_ok",
        "topic_match",
        "notes",
    ]
    with open(FILE_INVENTORY, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(inventory)


def main():
    if not MASTER_INDEX.exists():
        print(f"ERROR: {MASTER_INDEX} not found")
        sys.exit(1)

    paths = extract_dest_paths(MASTER_INDEX)
    missing = validate_paths(paths)

    if missing:
        print("ERROR: Dangling references in index/master_index.md:")
        for p in missing:
            print(f"  - {p}")
        print("\nFix the above paths before committing.")
        sys.exit(1)

    print("OK: All referenced paths in master_index.md exist.")

    inventory = generate_inventory()
    write_inventory(inventory)
    print(f"OK: Updated {FILE_INVENTORY} ({len(inventory)} files)")


if __name__ == "__main__":
    main()
