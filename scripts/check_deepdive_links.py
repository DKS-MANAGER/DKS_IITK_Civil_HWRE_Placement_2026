#!/usr/bin/env python3
"""
check_deepdive_links.py

Verifies that all relative markdown links in the software-and-tech deep-dives
directory and the files that reference them resolve to existing files.
Writes a report to linkcheck_report.txt in the repo root.
"""

import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

FILES = [
    "software-and-tech/deep-dives/README.md",
    "software-and-tech/deep-dives/hec-ras-walkthrough.md",
    "software-and-tech/deep-dives/plaxis-2d-tutorial.md",
    "software-and-tech/deep-dives/openfoam-case-study.md",
    "software-and-tech/deep-dives/swmm-guide.md",
    "software-and-tech/deep-dives/epanet-walkthrough.md",
    "software-and-tech/deep-dives/hec-hms-tutorial.md",
    "software-and-tech/deep-dives/geostudio-slopew-tutorial.md",
    "software-and-tech/README.md",
    "software-and-tech/hwre/hwre-tech-roadmap.md",
    "software-and-tech/geotechnical/geotechnical-tech.md",
    "software-and-tech/cfd/cfd-tech.md",
    "software-and-tech/hydrology/hydrology-tech.md",
    "software-and-tech/environmental/environmental-tech.md",
]

LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")


def main():
    missing = 0
    checked = 0
    issues = []

    for rel in FILES:
        f = REPO_ROOT / rel
        if not f.exists():
            issues.append("MISSING FILE: " + rel)
            missing += 1
            continue
        text = f.read_text(encoding="utf-8")
        for link in LINK_RE.findall(text):
            if link.startswith(("http://", "https://", "mailto:", "#")):
                continue
            target = (f.parent / link).resolve()
            checked += 1
            if not target.exists():
                issues.append("BROKEN in {}: {}".format(rel, link))
                missing += 1

    report = "CHECKED: {}\nMISSING: {}\n".format(checked, missing)
    report += "\n".join(issues)
    (REPO_ROOT / "linkcheck_report.txt").write_text(report, encoding="utf-8")
    print(report)


if __name__ == "__main__":
    main()
