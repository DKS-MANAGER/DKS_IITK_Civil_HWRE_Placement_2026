#!/usr/bin/env python3
"""Extract RCC chapter content from GATE-O-PEDIA for reference."""
import re, os, json

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_DIR = os.path.dirname(SCRIPT_DIR)
SRC_FILE = os.path.join(os.path.dirname(REPO_DIR), "GATE-O-PEDIA - CIVIL ENGINEERING.txt")
OUT_FILE = os.path.join(SCRIPT_DIR, "rcc_preview.txt")

def main():
    with open(SRC_FILE, "r", encoding="utf-8", errors="replace") as f:
        lines = f.readlines()
    
    total = len(lines)
    print(f"Total lines in source: {total}")
    
    # RCC Chapter 4: lines 4756-6886 (1-indexed), 0-indexed: 4755-6885
    start, end = 4755, 6885
    rcc = lines[start:end+1]
    print(f"RCC chapter: lines {start+1}-{end+1} ({len(rcc)} lines)")
    
    # Extract meaningful content
    output = []
    output.append(f"=== RCC CHAPTER EXTRACTION ===")
    output.append(f"Source lines: {start+1}-{end+1} ({len(rcc)} lines)")
    output.append("")
    
    # Find section headers and key formulas
    for i, line in enumerate(rcc):
        s = line.strip()
        if not s:
            output.append("")
            continue
        # Keep lines that are short (headers) or contain formulas
        if len(s) < 200:
            output.append(f"L{i+start+1}: {s}")
    
    with open(OUT_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(output))
    
    print(f"Wrote {len(output)} lines to {OUT_FILE}")
    
    # Also print summary of what we found
    sections = []
    for i, line in enumerate(rcc):
        s = line.strip()
        if re.match(r'^4\.\d', s) and len(s) < 100:
            sections.append(f"  L{i+start+1}: {s}")
    
    print(f"\nFound {len(sections)} section headers:")
    for s in sections[:30]:
        print(s)
    if len(sections) > 30:
        print(f"  ... and {len(sections)-30} more")

if __name__ == "__main__":
    main()
