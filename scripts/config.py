"""
Central repository configuration module.
Provides canonical paths, subsystem directories, skip lists, and threshold constants
for all maintenance scripts, validators, and metrics engines.
"""

from pathlib import Path

# Repository root directory (F:/2k26Placement/DKS_IITK_Civil_HWRE_Placement_2026)
REPO_ROOT = Path(__file__).resolve().parent.parent

# Top-level directory topology
SUBSYSTEM_DIRS = {
    "core": REPO_ROOT / "core",
    "aptitude": REPO_ROOT / "aptitude",
    "non-core": REPO_ROOT / "non-core",
    "prep": REPO_ROOT / "prep",
    "software-and-tech": REPO_ROOT / "software-and-tech",
    "resources": REPO_ROOT / "resources",
    "docs": REPO_ROOT / "docs",
    "index": REPO_ROOT / "index",
    "scripts": REPO_ROOT / "scripts",
}

# Directories to skip when scanning markdown files
SKIP_DIRS = {
    ".git",
    ".github",
    ".vscode",
    ".idea",
    ".roo",
    "node_modules",
    "__pycache__",
    "_artifacts",
}

# Primary canonical reference files
DOCS_DIR = REPO_ROOT / "docs"
INDEX_DIR = REPO_ROOT / "index"
MASTER_INDEX_PATH = INDEX_DIR / "master_index.md"
TOPICS_PATH = INDEX_DIR / "topics.md"
TOPIC_MAP_PATH = INDEX_DIR / "topic_map.md"
METRICS_JSON_PATH = INDEX_DIR / "metrics.json"
FILE_INVENTORY_PATH = INDEX_DIR / "file_inventory.csv"
README_PATH = REPO_ROOT / "README.md"
MASTER_NAVIGATION_PATH = DOCS_DIR / "MASTER_NAVIGATION.md"
TESTING_GUIDE_PATH = DOCS_DIR / "TESTING_GUIDE.md"
READINESS_SCORECARD_PATH = REPO_ROOT / "prep" / "READINESS_SCORECARD.md"

# Canonical Subject Guide Definitions
CANONICAL_SUBJECT_GUIDES = [
    ("Hydraulics", "core/hwre/hydraulics/hydraulics.md"),
    ("Open Channel Flow", "core/hwre/open_channel_flow/open-channel-flow.md"),
    ("Hydrology", "core/hwre/hydrology/hydrology.md"),
    ("Water Resources", "core/hwre/water_resources/water-resources-engineering.md"),
    ("Flood Control", "core/hwre/flood_control/flood-control.md"),
    ("Irrigation", "core/hwre/irrigation/irrigation-engineering.md"),
    ("Structural Analysis", "core/structural-analysis/structural-analysis.md"),
    ("RCC Design", "core/rcc/rcc-design.md"),
    ("Steel Design", "core/steel/steel-design.md"),
    ("Strength of Materials", "core/fundamentals/strength-of-materials.md"),
    ("Engineering Mechanics", "core/fundamentals/engineering-mechanics.md"),
    ("Geotechnical", "core/geotechnical/geotechnical.md"),
    ("Environmental", "core/environmental/environmental-engineering.md"),
    ("Transportation", "core/transportation/transportation-engineering.md"),
    ("Geoinformatics", "core/geoinformatics/geoinformatics.md"),
    ("Infrastructure", "core/infrastructure/infrastructure-engineering-management.md"),
]

# Canonical 6-Tier Provenance Labels
PROVENANCE_LABELS = [
    "[VERIFIED]",
    "[SOURCE-DERIVED]",
    "[INFERRED]",
    "[PREPARATION HEURISTIC]",
    "[SELF-REPORTED]",
    "[PREDICTED]",
]

# Maximum recommended file size in lines for modular reading
MAX_RECOMMENDED_LINES = 800
