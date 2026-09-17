#!/usr/bin/env python3
"""Extract Steel Structures chapter content from GATE-O-PEDIA for reference."""
import re, os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_DIR = os.path.dirname(SCRIPT_DIR)
SRC_FILE = os.path.join(os.path.dirname(REPO_DIR), "GATE-O-PEDIA - CIVIL ENGINEERING.txt")
OUT_FILE = os.path.join(SCRIPT_DIR, "steel_preview.txt")

def main():
    with open(SRC_FILE, "r", encoding="utf-8", errors="replace") as f:
        lines = f.readlines()
    
    total = len(lines)
    print(f"Total lines in source: {total}")
    
    # Steel Structures Chapter 5: lines 6887-8872 (1-indexed), 0-indexed: 6886-8871
    start, end = 6886, 8871
    steel = lines[start:end+1]
    print(f"Steel chapter: lines {start+1}-{end+1} ({len(steel)} lines)")
    
    output = []
    output.append(f"=== STEEL STRUCTURES CHAPTER EXTRACTION ===")
    output.append(f"Source lines: {start+1}-{end+1} ({len(steel)} lines)")
    output.append("")
    
    for i, line in enumerate(steel):
        s = line.strip()
        if not s:
            output.append("")
            continue
        if len(s) < 200:
            output.append(f"L{i+start+1}: {s}")
    
    with open(OUT_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(output))
    
    print(f"Wrote {len(output)} lines to {OUT_FILE}")
    
    # Print section headers
    sections = []
    for i, line in enumerate(steel):
        s = line.strip()
        if re.match(r'^5\.\d', s) and len(s) < 100:
            sections.append(f"  L{i+start+1}: {s}")
    
    print(f"\nFound {len(sections)} section headers:")
    for s in sections[:40]:
        print(s)
    if len(sections) > 40:
        print(f"  ... and {len(sections)-40} more")

if __name__ == "__main__":
    main()
