#!/usr/bin/env python3
"""Find ALL occurrences of subject name headers in the GATE-O-PEDIA file."""
import re
import os

REF_PATH = os.path.join('f:', os.sep, '2k26Placement', 'GATE-O-PEDIA - CIVIL ENGINEERING.txt')
OUT_PATH = os.path.join('f:', os.sep, '2k26Placement', 'DKS_IITK_Civil_HWRE_Placement_2026', 'scripts', 'subject_headers.txt')

SUBJECT_NAMES = [
    'ENGINEERING MECHANICS',
    'STRENGTH OF MATERIAL',
    'STRUCTURAL ANALYSIS',
    'REINFORCED CEMENT CONCRETE',
    'STEEL STRUCTURE',
    'ENVIRONMENT ENGINEERING',
    'GEOTECHNICAL ENGINEERING',
    'FLUID MECHANICS',
    'IRRIGATION ENGINEERING',
    'ENGINEERING HYDROLOGY',
    'SURVEYING',
    'HIGHWAY ENGINEERING',
    'AIRPORT ENGINEERING',
    'RAILWAY ENGINEERING',
    'CONSTRUCTION PROJECT MANAGEMENT',
    'BUILDING MATERIAL CONSTRUCTION',
    'ENGINEERING MATHEMATICS',
    'GENERAL APTITUDE',
]

# Also look for broader patterns
SECTION_PATTERNS = [
    (r'^(\d{1,2})\.1\b', 'SECTION_X.1'),
    (r'^(?:Fundamental|Basics?|Introduction|Overview)', 'TOPIC_HEADER'),
]

def main():
    with open(REF_PATH, 'r', encoding='utf-8', errors='ignore') as f:
        lines = f.readlines()
    
    print(f"Total lines: {len(lines)}")
    
    with open(OUT_PATH, 'w', encoding='utf-8') as out:
        # Find all subject name occurrences
        out.write("=== ALL SUBJECT NAME OCCURRENCES ===\n\n")
        for name in SUBJECT_NAMES:
            occurrences = []
            for i, line in enumerate(lines, 1):
                stripped = line.strip().upper()
                if name in stripped and len(stripped) < 120:
                    occurrences.append(i)
            out.write(f"{name}: {len(occurrences)} occurrences\n")
            for occ in occurrences[:5]:
                out.write(f"  Line {occ}: {lines[occ-1].strip()[:100]}\n")
            if len(occurrences) > 5:
                out.write(f"  ... and {len(occurrences)-5} more\n")
            out.write("\n")
        
        # Find ALL X.1 section headers
        out.write("\n=== ALL 'X.1' SECTION BOUNDARIES ===\n\n")
        for i, line in enumerate(lines, 1):
            stripped = line.strip()
            m = re.match(r'^(\d{1,2})\.1\b', stripped)
            if m:
                chap = int(m.group(1))
                if 1 <= chap <= 18:
                    out.write(f"Line {i:5d}: Ch {chap:2d} | {stripped[:120]}\n")
        
        # Find GATE WALLAH header + subject name patterns
        out.write("\n=== GATE WALLAH HEADER PATTERNS ===\n\n")
        for i, line in enumerate(lines, 1):
            stripped = line.strip()
            if 'GATE WALLAH' in stripped or 'GATE-O-PEDIA' in stripped:
                # Show next 2 lines for context
                context = ''
                if i < len(lines):
                    context = lines[i].strip()[:80]
                out.write(f"Line {i:5d}: {stripped[:80]} | Next: {context}\n")
        
        # Find page markers to understand content distribution
        out.write("\n=== PAGE MARKER DISTRIBUTION (every 50th page) ===\n\n")
        for i, line in enumerate(lines, 1):
            m = re.match(r'===== Page (\d+) / 947 =====', line.strip())
            if m:
                page = int(m.group(1))
                if page % 50 == 0 or page <= 5:
                    out.write(f"Line {i:5d}: Page {page}\n")
        
        # Find content density (non-blank lines per 100-line window)
        out.write("\n=== CONTENT DENSITY (lines with content per 500-line window) ===\n\n")
        window = 500
        for start in range(0, len(lines), window):
            end = min(start + window, len(lines))
            content_count = sum(1 for l in lines[start:end] if l.strip())
            page_match = re.match(r'===== Page (\d+)', lines[start].strip()) if start < len(lines) else None
            page_info = f" (Page ~{page_match.group(1)})" if page_match else ""
            out.write(f"Lines {start+1:5d}-{end:5d}:{page_info} {content_count:4d} content lines\n")
    
    print(f"Subject headers written to: {OUT_PATH}")
    print(f"File size: {os.path.getsize(OUT_PATH)} bytes")

if __name__ == '__main__':
    main()
