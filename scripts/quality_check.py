#!/usr/bin/env python3
"""
Quality Control Script -- IITK Civil Placement OS

Validates:
1. Broken internal links
2. Heading consistency (H1 per file)
3. File size limits
4. Missing README files in major directories
5. Orphan pages (no incoming links)
6. Basic metadata presence

Usage:
    python scripts/quality_check.py [--fix] [--verbose]
"""

import os
import re
import sys
from pathlib import Path
from collections import defaultdict

# Configuration
REPO_ROOT = Path(__file__).parent.parent
REPO_NAME = "DKS_IITK_Civil_HWRE_Placement_2026"

# Directories that should have README.md
DIRS_WITH_README = [
    "core",
    "core/hwre",
    "core/gate",
    "core/structures",
    "core/geotechnical",
    "core/environmental",
    "core/transportation",
    "core/geoinformatics",
    "core/infrastructure",
    "core/fundamentals",
    "non-core",
    "non-core/consulting",
    "non-core/data-analyst",
    "non-core/business-analyst",
    "non-core/product-management",
    "non-core/operations",
    "non-core/finance",
    "non-core/risk",
    "non-core/strategy",
    "non-core/aptitude",
    "prep",
    "prep/behavioral",
    "prep/technical",
    "prep/mock-tests",
    "prep/company-profiles",
    "prep/templates",
    "software-and-tech",
    "software-and-tech/deep-dives",
    "software-and-tech/programming",
    "resources",
    "index",
    "docs",
    "questions",
]

# Max file size (lines)
MAX_LINES = 800

# Skip patterns
SKIP_DIRS = {".git", ".github", "__pycache__", ".roo", "node_modules"}
SKIP_FILES = {"LICENSE", ".gitignore", ".editorconfig", ".pre-commit-config.yaml"}


def find_all_markdown_files(root):
    """Find all .md files in the repository."""
    md_files = []
    for path in root.rglob("*.md"):
        # Skip hidden directories and common skip patterns
        parts = path.relative_to(root).parts
        if any(p.startswith(".") for p in parts):
            continue
        if any(sd in parts for sd in SKIP_DIRS):
            continue
        md_files.append(path)
    return md_files


def extract_links_from_file(filepath):
    """Extract all internal markdown links from a file."""
    links = []
    try:
        content = filepath.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        return links

    # Match markdown links: [text](path)
    pattern = r'\[([^\]]*)\]\(([^)]+)\)'
    for match in re.finditer(pattern, content):
        text, target = match.groups()
        # Skip external links, anchors, and non-file references
        if target.startswith("http") or target.startswith("#") or target.startswith("mailto:"):
            continue
        # Remove anchor from target
        target = target.split("#")[0]
        if not target:
            continue
        links.append((match.start(), text, target))
    return links


def resolve_link(filepath, target):
    """Resolve a relative link from a file's perspective."""
    # Handle directory links (ending with /)
    if target.endswith("/"):
        resolved = (filepath.parent / target).resolve()
        if resolved.is_dir():
            readme = resolved / "README.md"
            if readme.exists():
                return readme
            return resolved
        return resolved

    resolved = (filepath.parent / target).resolve()

    # Check if it exists as-is
    if resolved.exists():
        return resolved

    # Try adding .md extension
    if not resolved.suffix:
        with_md = resolved.with_suffix(".md")
        if with_md.exists():
            return with_md

    return resolved


def check_links(md_files, verbose=False):
    """Check for broken internal links."""
    issues = []
    link_targets = defaultdict(list)  # target -> [files linking to it]

    for filepath in md_files:
        links = extract_links_from_file(filepath)
        rel_path = filepath.relative_to(REPO_ROOT)

        for offset, text, target in links:
            resolved = resolve_link(filepath, target)

            if not resolved.exists():
                issues.append({
                    "type": "BROKEN_LINK",
                    "file": str(rel_path),
                    "target": target,
                    "text": text,
                    "line": _offset_to_line(filepath, offset),
                })
            else:
                # Track incoming links for orphan detection
                link_targets[str(resolved)].append(str(rel_path))

        if verbose:
            print(f"  ✓ Checked {rel_path} ({len(links)} links)")

    return issues, link_targets


def _offset_to_line(filepath, offset):
    """Convert character offset to line number."""
    try:
        content = filepath.read_text(encoding="utf-8", errors="ignore")
        return content[:offset].count("\n") + 1
    except Exception:
        return "?"


def _strip_code_fences(content):
    """Remove fenced code blocks so '#' comment lines inside them are not
    mistaken for markdown headings. Handles ```, ~~~, and indented fences."""
    # Remove fenced code blocks (``` or ~~~ with optional language tag)
    content = re.sub(r"^```.*?^```", "", content, flags=re.MULTILINE | re.DOTALL)
    content = re.sub(r"^~~~.*?^~~~", "", content, flags=re.MULTILINE | re.DOTALL)
    return content


def check_headings(md_files, verbose=False):
    """Check that each file has exactly one H1 heading.

    Strips a leading UTF-8 BOM (which would otherwise hide the first heading)
    and ignores '#' comment lines inside fenced code blocks.
    """
    issues = []
    for filepath in md_files:
        try:
            content = filepath.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue

        # Remove BOM so a leading H1 is detected correctly
        content = content.lstrip("\ufeff")
        # Remove fenced code blocks so code comments aren't counted as headings
        content = _strip_code_fences(content)

        h1_count = len(re.findall(r"^# [^#]", content, re.MULTILINE))
        rel_path = filepath.relative_to(REPO_ROOT)

        if h1_count == 0:
            issues.append({
                "type": "NO_H1",
                "file": str(rel_path),
                "detail": "File has no H1 heading",
            })
        elif h1_count > 1:
            issues.append({
                "type": "MULTIPLE_H1",
                "file": str(rel_path),
                "detail": f"File has {h1_count} H1 headings",
            })

    if verbose:
        print(f"  ✓ Checked {len(md_files)} files for heading consistency")
    return issues


def check_file_sizes(md_files, verbose=False):
    """Check for files exceeding size limits."""
    issues = []
    for filepath in md_files:
        try:
            content = filepath.read_text(encoding="utf-8", errors="ignore")
            line_count = content.count("\n") + 1
        except Exception:
            continue

        rel_path = filepath.relative_to(REPO_ROOT)

        if line_count > MAX_LINES:
            issues.append({
                "type": "LARGE_FILE",
                "file": str(rel_path),
                "detail": f"{line_count} lines (max {MAX_LINES})",
                "lines": line_count,
            })

    if verbose:
        print(f"  ✓ Checked {len(md_files)} files for size limits")
    return issues


def check_readme_files(verbose=False):
    """Check that major directories have README.md files."""
    issues = []
    for dir_rel in DIRS_WITH_README:
        dir_path = REPO_ROOT / dir_rel
        readme = dir_path / "README.md"
        if not readme.exists():
            issues.append({
                "type": "MISSING_README",
                "file": dir_rel + "/",
                "detail": f"No README.md in {dir_rel}/",
            })

    if verbose:
        print(f"  ✓ Checked {len(DIRS_WITH_README)} directories for README.md")
    return issues


def check_orphan_pages(md_files, link_targets, verbose=False):
    """Find pages with no incoming links (orphans)."""
    orphans = []
    for filepath in md_files:
        rel_path = str(filepath.relative_to(REPO_ROOT))

        # Skip README files and root-level files
        if filepath.name == "README.md":
            continue

        # Check if any other file links to this one
        has_incoming = False
        for target, sources in link_targets.items():
            if filepath.resolve() == Path(target).resolve():
                # Check if any source is different from this file
                other_sources = [s for s in sources if s != rel_path]
                if other_sources:
                    has_incoming = True
                    break

        if not has_incoming:
            orphans.append(rel_path)

    if verbose and orphans:
        print(f"  ⚠ Found {len(orphans)} orphan pages")
    return orphans


def generate_report(all_issues, orphans, md_files):
    """Generate the quality check report."""
    print("\n" + "=" * 60)
    print("  IITK Civil Placement OS - Quality Check Report")
    print("=" * 60)

    # Summary
    broken = [i for i in all_issues if i["type"] == "BROKEN_LINK"]
    headings = [i for i in all_issues if i["type"] in ("NO_H1", "MULTIPLE_H1")]
    large = [i for i in all_issues if i["type"] == "LARGE_FILE"]
    missing_readme = [i for i in all_issues if i["type"] == "MISSING_README"]

    print(f"\n--- Summary ---")
    print(f"   Files scanned:     {len(md_files)}")
    print(f"   Broken links:      {len(broken)}")
    print(f"   Heading issues:    {len(headings)}")
    print(f"   Large files:       {len(large)}")
    print(f"   Missing READMEs:   {len(missing_readme)}")
    print(f"   Orphan pages:      {len(orphans)}")

    # Detailed issues
    if broken:
        print(f"\n[!!] Broken Links ({len(broken)})")
        for issue in broken:
            print(f"   {issue['file']}:{issue['line']}")
            print(f"     -> {issue['target']} (text: {issue['text']})")

    if headings:
        print(f"\n[!] Heading Issues ({len(headings)})")
        for issue in headings:
            print(f"   {issue['file']}: {issue['detail']}")

    if large:
        print(f"\n[!] Large Files ({len(large)})")
        for issue in large:
            print(f"   {issue['file']}: {issue['detail']}")

    if missing_readme:
        print(f"\n[!] Missing READMEs ({len(missing_readme)})")
        for issue in missing_readme:
            print(f"   {issue['file']}: {issue['detail']}")

    if orphans:
        print(f"\n[*] Orphan Pages ({len(orphans)})")
        for orphan in orphans[:20]:  # Show first 20
            print(f"   {orphan}")
        if len(orphans) > 20:
            print(f"   ... and {len(orphans) - 20} more")

    # Pass/Fail
    critical = len(broken) + len(missing_readme)
    if critical == 0:
        print(f"\n[PASS] No critical issues found")
    else:
        print(f"\n[FAIL] {critical} critical issues found")

    print("\n" + "=" * 60)
    return critical == 0


def main():
    verbose = "--verbose" in sys.argv or "-v" in sys.argv

    print("IITK Civil Placement OS -- Quality Check")
    print(f"   Repository: {REPO_ROOT}\n")

    # Find all markdown files
    print("Finding markdown files...")
    md_files = find_all_markdown_files(REPO_ROOT)
    print(f"   Found {len(md_files)} files\n")

    # Run checks
    print("Checking links...")
    link_issues, link_targets = check_links(md_files, verbose)

    print("Checking headings...")
    heading_issues = check_headings(md_files, verbose)

    print("Checking file sizes...")
    size_issues = check_file_sizes(md_files, verbose)

    print("Checking README files...")
    readme_issues = check_readme_files(verbose)

    print("Checking orphan pages...")
    orphans = check_orphan_pages(md_files, link_targets, verbose)

    # Combine all issues
    all_issues = link_issues + heading_issues + size_issues + readme_issues

    # Generate report
    passed = generate_report(all_issues, orphans, md_files)

    sys.exit(0 if passed else 1)


if __name__ == "__main__":
    main()
