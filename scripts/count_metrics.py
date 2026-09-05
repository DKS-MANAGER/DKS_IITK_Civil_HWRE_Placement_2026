#!/usr/bin/env python3
"""
count_metrics.py — Automatically count repository metrics.

Counts markdown files, interview questions, mock sessions,
company profiles, numerical examples, and software deep-dives.
Outputs a JSON summary and a markdown table for README injection.

Usage:
    python scripts/count_metrics.py
    python scripts/count_metrics.py --json      # JSON output only
    python scripts/count_metrics.py --update     # Auto-update README.md badge + table
"""

import os
import re
import json
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
README_PATH = os.path.join(REPO_ROOT, "README.md")


def count_markdown_files():
    """Count all .md files excluding hidden dirs and node_modules."""
    skip = {".git", ".github", ".vscode", ".idea", "node_modules", "__pycache__"}
    count = 0
    for root, dirs, files in os.walk(REPO_ROOT):
        dirs[:] = [d for d in dirs if d not in skip]
        for f in files:
            if f.endswith(".md"):
                count += 1
    return count


def count_interview_questions():
    r"""Count distinct interview questions across all banks.

    Looks for patterns like ### Q\d+: or ### Q\d+\d+: in interview-related files.
    Also counts STAR stories (### Story \d+), HR questions, etc.
    """
    total = 0
    breakdown = {}

    def _count_pattern(filepath, pattern):
        """Count matches of a regex in a file. Returns count."""
        full = os.path.join(REPO_ROOT, filepath)
        if not os.path.exists(full):
            return 0
        with open(full, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
        matches = re.findall(pattern, content, re.IGNORECASE)
        return len(matches)

    # Files containing numbered interview questions (use non-capturing groups)
    q_file = "prep/technical/technical-interview-bank.md"
    c = _count_pattern(q_file, r"### Q\d+:")
    if c:
        breakdown[q_file] = c
        total += c

    mock_q = "prep/mock-tests/mock-interview-questions.md"
    c = _count_pattern(mock_q, r"### Q\d+:")
    if c:
        breakdown[mock_q] = c
        total += c

    proj_def = "prep/technical/project-defense-guide.md"
    c = _count_pattern(proj_def, r"### Q\d+:|### Question \d+:")
    if c:
        breakdown[proj_def] = c
        total += c

    hr_bank = "prep/behavioral/hr_questions/hr-questions-bank.md"
    c = _count_pattern(hr_bank, r"### HR\d+:|### Q\d+:|### Question \d+:")
    if c:
        breakdown[hr_bank] = c
        total += c

    hr_hybrid = "prep/behavioral/hr_questions/hr-technical-hybrid-questions.md"
    c = _count_pattern(hr_hybrid, r"### Q\d+:|### Question \d+:")
    if c:
        breakdown[hr_hybrid] = c
        total += c

    # Count question bank sections in core subject guides
    core_subjects = [
        "core/hwre/hydraulics/hydraulics.md",
        "core/hwre/open_channel_flow/open-channel-flow.md",
        "core/hwre/hydrology/hydrology.md",
        "core/hwre/water_resources/water-resources-engineering.md",
        "core/structures/structures.md",
        "core/geotechnical/geotechnical.md",
        "core/environmental/environmental-engineering.md",
        "core/transportation/transportation-engineering.md",
        "core/geoinformatics/geoinformatics.md",
    ]

    for rel_path in core_subjects:
        c = _count_pattern(rel_path, r"### Q\d+:|### \d+\.\s")
        if c:
            breakdown[rel_path] = c
            total += c

    # Count behavioral STAR stories and scenarios
    behav = "prep/behavioral/behavioral-interview-guide.md"
    c = _count_pattern(behav, r"### Story \d+|### Scenario \d+|### Q\d+:")
    if c:
        breakdown[behav + " (stories/scenarios)"] = c
        total += c

    # Count non-core questions
    case_bank = "non-core/consulting/case-bank.md"
    c = _count_pattern(case_bank, r"### Case \d+:|### Case [A-Z]:")
    if c:
        breakdown[case_bank] = c
        total += c

    guess = "non-core/guesstimates/guesstimate-guide.md"
    c = _count_pattern(guess, r"### Q\d+:|### Problem \d+:|### Practice \d+:")
    if c:
        breakdown[guess] = c
        total += c

    # Count GATE practice questions
    gate = "core/gate/practice/gate-civil-practice.md"
    c = _count_pattern(gate, r"### Q\d+:|### Question \d+:")
    if c:
        breakdown[gate] = c
        total += c

    return total, breakdown


def count_mock_sessions():
    """Count role-specific mock test files in prep/mock-tests/."""
    mock_dir = os.path.join(REPO_ROOT, "prep/mock-tests")
    if not os.path.isdir(mock_dir):
        return 0

    count = 0
    for f in os.listdir(mock_dir):
        if f.startswith("mock-test-") and f.endswith(".md"):
            count += 1
    return count


def count_company_profiles():
    """Count company profiles."""
    profiles_dir = os.path.join(REPO_ROOT, "prep/company-profiles")
    if not os.path.isdir(profiles_dir):
        return 0

    count = 0
    for f in os.listdir(profiles_dir):
        if f.endswith(".md") and f.lower() not in ("readme.md", "index.md"):
            count += 1
    return count


def count_numerical_examples():
    """Count worked numerical examples across subject guides."""
    total = 0

    subject_files = [
        "core/hwre/hydraulics/hydraulics.md",
        "core/hwre/open_channel_flow/open-channel-flow.md",
        "core/hwre/hydrology/hydrology.md",
        "core/hwre/water_resources/water-resources-engineering.md",
        "core/structures/structures.md",
        "core/geotechnical/geotechnical.md",
        "core/environmental/environmental-engineering.md",
        "core/transportation/transportation-engineering.md",
    ]

    for rel_path in subject_files:
        full_path = os.path.join(REPO_ROOT, rel_path)
        if os.path.exists(full_path):
            with open(full_path, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()
            # Count ### Example \d+ patterns
            examples = re.findall(r"### Example \d+", content, re.IGNORECASE)
            total += len(examples)

    return total


def count_software_deep_dives():
    """Count software deep-dive walkthroughs."""
    deep_dives_dir = os.path.join(REPO_ROOT, "software-and-tech/deep-dives")
    if not os.path.isdir(deep_dives_dir):
        return 0

    count = 0
    for f in os.listdir(deep_dives_dir):
        if f.endswith(".md") and f.lower() not in ("readme.md",):
            count += 1
    return count


def count_noncore_tracks():
    """Count non-core career tracks with actual content."""
    noncore_dir = os.path.join(REPO_ROOT, "non-core")
    tracks = 0
    for d in os.listdir(noncore_dir):
        full = os.path.join(noncore_dir, d)
        if os.path.isdir(full) and d not in ("common", "aptitude", "guesstimates",
                                               "case-interviews", "resume-positioning",
                                               "quick-revision", "mock-interviews"):
            # Check if it has at least one .md file (not just README)
            md_files = [f for f in os.listdir(full) if f.endswith(".md") and f.lower() != "readme.md"]
            if md_files:
                tracks += 1
    return tracks


def count_subject_guides():
    """Count canonical subject guides in core/."""
    guides = []
    subjects = [
        ("Hydraulics", "core/hwre/hydraulics/hydraulics.md"),
        ("Open Channel Flow", "core/hwre/open_channel_flow/open-channel-flow.md"),
        ("Hydrology", "core/hwre/hydrology/hydrology.md"),
        ("Water Resources", "core/hwre/water_resources/water-resources-engineering.md"),
        ("Flood Control", "core/hwre/flood_control/"),
        ("Irrigation", "core/hwre/irrigation/"),
        ("Structures", "core/structures/structures.md"),
        ("Geotechnical", "core/geotechnical/geotechnical.md"),
        ("Environmental", "core/environmental/environmental-engineering.md"),
        ("Transportation", "core/transportation/transportation-engineering.md"),
        ("Geoinformatics", "core/geoinformatics/geoinformatics.md"),
        ("Infrastructure", "core/infrastructure/infrastructure-engineering-management.md"),
    ]

    for name, path in subjects:
        full_path = os.path.join(REPO_ROOT, path)
        if os.path.isdir(full_path):
            # It's a directory — count as a subject area
            md_files = [f for f in os.listdir(full_path)
                       if f.endswith(".md") and f.lower() != "readme.md"]
            if md_files:
                guides.append(name)
        elif os.path.isfile(full_path):
            guides.append(name)

    return len(guides), guides


def generate_metrics():
    """Generate all metrics."""
    md_count = count_markdown_files()
    total_q, q_breakdown = count_interview_questions()
    mock_count = count_mock_sessions()
    company_count = count_company_profiles()
    numerical_count = count_numerical_examples()
    deep_dive_count = count_software_deep_dives()
    noncore_count = count_noncore_tracks()
    subject_count, subjects = count_subject_guides()

    return {
        "markdown_files": md_count,
        "interview_qa_total": total_q,
        "interview_qa_breakdown": q_breakdown,
        "mock_sessions": mock_count,
        "company_profiles": company_count,
        "numerical_examples": numerical_count,
        "software_deep_dives": deep_dive_count,
        "noncore_tracks": noncore_count,
        "subject_guides": subject_count,
        "subject_names": subjects,
    }


def update_readme(metrics):
    """Update README.md badge and metrics table with accurate counts."""
    if not os.path.exists(README_PATH):
        print("[ERROR] README.md not found at " + README_PATH)
        return False

    with open(README_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    # Update badge: Content-105%2B → Content-XXX
    new_count = metrics["markdown_files"]
    content = re.sub(
        r"Content-\d+\+%2B",
        f"Content-{new_count}",
        content
    )

    # Update the "At a Glance" table
    replacements = {
        r"\| Markdown Files \|.*\|": f"| Markdown Files | {metrics['markdown_files']} |",
        r"\| Subject Guides \|.*\|": f"| Subject Guides | {metrics['subject_guides']} |",
        r"\| Interview Q&As \|.*\|": f"| Interview Q&As | {metrics['interview_qa_total']} |",
        r"\| Mock Interview Sessions \|.*\|": f"| Mock Interview Sessions | {metrics['mock_sessions']} |",
        r"\| Software Deep-Dives \|.*\|": f"| Software Deep-Dives | {metrics['software_deep_dives']} |",
        r"\| Company Profiles \|.*\|": f"| Company Profiles | {metrics['company_profiles']}+ |",
        r"\| Non-Core Career Tracks \|.*\|": f"| Non-Core Career Tracks | {metrics['noncore_tracks']} |",
        r"\| Numerical Worked Examples \|.*\|": f"| Numerical Worked Examples | {metrics['numerical_examples']} |",
    }

    for pattern, replacement in replacements.items():
        content = re.sub(pattern, replacement, content)

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(content)

    return True


def main():
    metrics = generate_metrics()

    if "--json" in sys.argv:
        print(json.dumps(metrics, indent=2))
        return

    # Print summary table
    print("=" * 60)
    print("  Repository Metrics (Auto-Generated)")
    print("=" * 60)
    print(f"  Markdown Files:         {metrics['markdown_files']}")
    print(f"  Subject Guides:         {metrics['subject_guides']}")
    print(f"  Interview Q&As:         {metrics['interview_qa_total']}")
    print(f"  Mock Sessions:          {metrics['mock_sessions']}")
    print(f"  Software Deep-Dives:    {metrics['software_deep_dives']}")
    print(f"  Company Profiles:       {metrics['company_profiles']}+")
    print(f"  Non-Core Tracks:        {metrics['noncore_tracks']}")
    print(f"  Numerical Examples:     {metrics['numerical_examples']}")
    print("=" * 60)

    if metrics["interview_qa_breakdown"]:
        print("\n  Interview Q&A Breakdown:")
        for source, count in sorted(metrics["interview_qa_breakdown"].items()):
            print(f"    {source}: {count}")

    if "--update" in sys.argv:
        if update_readme(metrics):
            print("\n[OK] README.md updated with accurate counts.")
        else:
            print("\n[ERROR] Failed to update README.md.")

    # Also output JSON for programmatic use
    json_path = os.path.join(REPO_ROOT, "index", "metrics.json")
    os.makedirs(os.path.dirname(json_path), exist_ok=True)
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(metrics, f, indent=2)
    print(f"\n[OK] Metrics saved to index/metrics.json")


if __name__ == "__main__":
    main()
