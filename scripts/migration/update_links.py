#!/usr/bin/env python3
"""
[HISTORICAL MIGRATION TOOL - ARCHIVED]
update_links.py

Preserved for historical provenance of the monorepo restructuring (Sep 2026).
WARNING: Do not execute in active production. Contains historical rewrite rules
that may duplicate paths if run on the current repository layout.
"""

import os
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent.parent

# HISTORICAL REWRITES (Preserved for reference only)
PATH_REWRITES = [
    ("core/hwre/hydraulics/",           "core/hwre/hydraulics/"),
    ("core/hwre/open_channel_flow/",    "core/hwre/open_channel_flow/"),
    ("core/hwre/hydrology/",            "core/hwre/hydrology/"),
    ("core/hwre/water_resources/",      "core/hwre/water_resources/"),
    ("core/hwre/exam_notes/",           "core/hwre/exam_notes/"),
    ("core/hwre/flood_control/",        "core/hwre/flood_control/"),
    ("core/hwre/hydraulics_notes/",     "core/hwre/hydraulics_notes/"),
    ("core/hwre/irrigation/",           "core/hwre/irrigation/"),
    ("core/hwre/wastewater/",           "core/hwre/wastewater/"),
    ("core/hwre/water_supply/",         "core/hwre/water_supply/"),
    ("core/structures/",                "core/structures/"),
    ("core/geotechnical/",              "core/geotechnical/"),
    ("core/environmental/",             "core/environmental/"),
    ("core/transportation/",            "core/transportation/"),
    ("core/geoinformatics/",            "core/geoinformatics/"),
    ("core/infrastructure/",            "core/infrastructure/"),
    ("core/fundamentals/",              "core/fundamentals/"),
    ("core/gate/",                      "core/gate/"),
    ("non-core/aptitude/",              "aptitude/"),
    ("non-core/analytics/technical-stack.md", "non-core/analytics/technical-stack.md"),
    ("non-core/analytics/non-core-prep.md",   "non-core/analytics/non-core-prep.md"),
    ("prep/behavioral/",                "prep/behavioral/"),
    ("prep/company-profiles/",          "prep/company-profiles/"),
    ("prep/mock-tests/",                "prep/mock-tests/"),
    ("prep/hr/",                        "prep/interview/hr/"),
    ("prep/technical/",                 "prep/interview/technical/"),
    ("prep/templates/",                 "prep/templates/"),
    ("docs/roadmap.md",                 "docs/roadmap.md"),
    ("docs/setup.md",                   "docs/setup.md"),
    ("docs/fable-mode-setup.md",        "docs/fable-mode-setup.md"),
]

def main():
    print("[WARNING] This is an archived historical migration tool.")
    print("Execution is blocked in production to prevent unintended link modifications.")
    print("For live link validation, use `python scripts/validate_links.py` or `python scripts/audit_repo.py`.")

if __name__ == "__main__":
    main()
