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
    dest_col_idx = None
    with open(master_index_path, "r", encoding="utf-8") as f:
        for line in f:
            stripped = line.strip()
            if not stripped.startswith("|"):
                dest_col_idx = None
                continue
            if re.match(r"^\|[\s\-:]+\|", stripped):
                continue
            parts = [p.strip() for p in stripped.strip("|").split("|")]
            if dest_col_idx is None:
                for idx, col in enumerate(parts):
                    clean_col = col.lower().strip()
                    if clean_col in ("canonical page", "destination path", "destination"):
                        dest_col_idx = idx
                        break
                continue
            if dest_col_idx is not None and len(parts) > dest_col_idx:
                raw = parts[dest_col_idx]
                # extract link target if markdown link [text](path) or `path`
                m = re.search(r"\[.*?\]\((.*?)\)", raw)
                dest = m.group(1).strip("` ") if m else raw.strip("` ")
                if dest and dest != "-" and not dest.startswith("#"):
                    # Resolve relative to INDEX_DIR if starting with . or ..
                    if dest.startswith("."):
                        resolved = (INDEX_DIR / dest.split("#")[0]).resolve()
                        try:
                            rel = resolved.relative_to(REPO_ROOT)
                            paths.append(str(rel).replace("\\", "/"))
                        except ValueError:
                            paths.append(dest)
                    else:
                        paths.append(dest)
    return paths


def extract_links_from_file(filepath):
    """Extract relative markdown links from a file."""
    links = []
    base_dir = Path(filepath).parent
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    matches = re.findall(r"\[.*?\]\((.*?)\)", content)
    for target in matches:
        if target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        # resolve relative to file directory
        resolved = (base_dir / target.split("#")[0]).resolve()
        try:
            rel = resolved.relative_to(REPO_ROOT)
            links.append(str(rel).replace("\\", "/"))
        except ValueError:
            links.append(target)
    return links


def validate_paths(paths):
    missing = []
    for p in paths:
        if p.startswith(("http://", "https://", "mailto:", "#")):
            continue
        target = REPO_ROOT / p.split("#")[0]
        if not target.exists():
            missing.append(p)
    return missing


def generate_inventory():
    inventory = []
    skip_dirs = {".git", "__pycache__", "node_modules", ".vscode", ".idea", ".roo"}
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
    valid = {
        "core",
        "aptitude",
        "non-core",
        "prep",
        "software-and-tech",
        "resources",
        "docs",
        "index",
        "scripts",
        "_SYSTEM",
        "questions",
    }
    if parts[0] in valid:
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

    print("--> Validating master_index.md...")
    paths = extract_dest_paths(MASTER_INDEX)
    missing = validate_paths(paths)

    if missing:
        print("ERROR: Dangling references in index/master_index.md:")
        for p in missing:
            print(f"  - {p}")
        sys.exit(1)

    print(f"OK: All {len(paths)} referenced paths in master_index.md exist.")

    topics_file = INDEX_DIR / "topics.md"
    if topics_file.exists():
        print("--> Validating topics.md links...")
        t_links = extract_links_from_file(topics_file)
        missing_t = validate_paths(t_links)
        if missing_t:
            print("ERROR: Dangling references in index/topics.md:")
            for p in missing_t:
                print(f"  - {p}")
            sys.exit(1)
        print(f"OK: All {len(t_links)} links in topics.md exist.")

    topic_map_file = INDEX_DIR / "topic_map.md"
    if topic_map_file.exists():
        print("--> Validating topic_map.md links...")
        tm_links = extract_links_from_file(topic_map_file)
        missing_tm = validate_paths(tm_links)
        if missing_tm:
            print("ERROR: Dangling references in index/topic_map.md:")
            for p in missing_tm:
                print(f"  - {p}")
            sys.exit(1)
        print(f"OK: All {len(tm_links)} links in topic_map.md exist.")

    readme_file = INDEX_DIR / "README.md"
    if readme_file.exists():
        print("--> Validating index/README.md links...")
        r_links = extract_links_from_file(readme_file)
        missing_r = validate_paths(r_links)
        if missing_r:
            print("ERROR: Dangling references in index/README.md:")
            for p in missing_r:
                print(f"  - {p}")
            sys.exit(1)
        print(f"OK: All {len(r_links)} links in index/README.md exist.")

    print("--> Generating file_inventory.csv...")
    inventory = generate_inventory()
    write_inventory(inventory)
    print(f"OK: Updated {FILE_INVENTORY} ({len(inventory)} files across {len(set(item['category'] for item in inventory))} categories)")

    # Run count_metrics to keep metrics.json perfectly in sync
    print("--> Updating metrics.json via count_metrics.py...")
    import subprocess
    cmd = [sys.executable, str(REPO_ROOT / "scripts" / "count_metrics.py")]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode == 0:
        print("OK: metrics.json synchronized.")
    else:
        print(f"WARNING: count_metrics.py failed: {res.stderr}")


if __name__ == "__main__":
    main()
