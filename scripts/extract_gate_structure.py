#!/usr/bin/env python3
"""Extract the structural outline of GATE-O-PEDIA to understand its format."""
import os
import sys

REF_PATH = os.path.join('f:', os.sep, '2k26Placement', 'GATE-O-PEDIA - CIVIL ENGINEERING.txt')
OUT_PATH = os.path.join('f:', os.sep, '2k26Placement', 'DKS_IITK_Civil_HWRE_Placement_2026', 'scripts', 'gate_preview.txt')

def main():
    print(f"Reading: {REF_PATH}")
    print(f"Exists: {os.path.exists(REF_PATH)}")
    
    with open(REF_PATH, 'r', encoding='utf-8', errors='ignore') as f:
        lines = f.readlines()
    
    print(f"Total lines: {len(lines)}")
    
    with open(OUT_PATH, 'w', encoding='utf-8') as out:
        out.write(f"=== GATE-O-PEDIA STRUCTURE PREVIEW ===\n")
        out.write(f"Total lines: {len(lines)}\n\n")
        
        # Show first 200 non-empty lines
        out.write("=== FIRST 200 NON-EMPTY LINES (Lines 1-2000) ===\n")
        count = 0
        for i, line in enumerate(lines[:2000], 1):
            stripped = line.rstrip()
            if stripped and stripped.strip():
                out.write(f"{i:5d}: {stripped[:200]}\n")
                count += 1
                if count >= 200:
                    break
        
        # Find lines that look like subject headers (ALL CAPS, or numbered sections)
        out.write("\n=== POSSIBLE SUBJECT HEADERS (ALL CAPS or numbered) ===\n")
        for i, line in enumerate(lines, 1):
            stripped = line.strip()
            if stripped and len(stripped) > 3 and len(stripped) < 100:
                # All caps lines
                if stripped.isupper() and not stripped.startswith(('Q.', 'Q ', '(')):
                    out.write(f"{i:5d}: [ALLCAPS] {stripped}\n")
                # Lines starting with subject-like patterns
                elif stripped.startswith(('Unit ', 'Chapter ', 'Module ', 'Section ', 'PART ', 'Part ')):
                    out.write(f"{i:5d}: [SECTION] {stripped}\n")
                # Lines that are just a subject name (short, no period, no digits at start)
                elif len(stripped) < 60 and stripped[0].isupper() and not stripped[0].isdigit():
                    if not any(c in stripped for c in ['=', '(', ')', '{', '}', '<', '>']):
                        # Check if next line is empty (header-like behavior)
                        if i < len(lines) and not lines[i].strip():
                            out.write(f"{i:5d}: [HEADER?] {stripped}\n")
        
        # Count lines by pattern
        out.write("\n=== LINE PATTERN ANALYSIS ===\n")
        patterns = {
            'blank': 0,
            'all_caps': 0,
            'question_mark': 0,
            'formula_like': 0,
            'numbered_list': 0,
            'bullet_list': 0,
            'short_text': 0,
            'long_text': 0,
        }
        for line in lines:
            stripped = line.strip()
            if not stripped:
                patterns['blank'] += 1
            elif stripped.isupper() and len(stripped) > 3:
                patterns['all_caps'] += 1
            elif stripped.endswith('?'):
                patterns['question_mark'] += 1
            elif '=' in stripped and len(stripped) < 100:
                patterns['formula_like'] += 1
            elif len(stripped) < 60:
                patterns['short_text'] += 1
            else:
                patterns['long_text'] += 1
        
        for p, c in patterns.items():
            out.write(f"  {p}: {c}\n")
    
    print(f"Preview written to: {OUT_PATH}")
    print(f"File size: {os.path.getsize(OUT_PATH)} bytes")

if __name__ == '__main__':
    main()
