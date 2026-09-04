#!/usr/bin/env python3
"""
Full GATE-O-PEDIA Taxonomy Extraction
Reads entire 37K-line file and builds complete subject/topic/formula map.
"""
import re
import os
import json
from collections import defaultdict

REF_PATH = os.path.join('f:', os.sep, '2k26Placement', 'GATE-O-PEDIA - CIVIL ENGINEERING.txt')
OUT_DIR = os.path.join('f:', os.sep, '2k26Placement', 'DKS_IITK_Civil_HWRE_Placement_2026', 'docs', 'audit')
REPORT_PATH = os.path.join(OUT_DIR, 'gate_opedia_full_analysis.md')
TAXONOMY_PATH = os.path.join(OUT_DIR, 'gate_opedia_taxonomy.json')

# Known 18 subjects from TOC
SUBJECTS = {
    'ENGINEERING MECHANICS': {'num': 1, 'pages': '1.1-1.36'},
    'STRENGTH OF MATERIAL': {'num': 2, 'pages': '2.1-2.47'},
    'STRUCTURAL ANALYSIS': {'num': 3, 'pages': '3.1-3.54'},
    'REINFORCED CEMENT CONCRETE': {'num': 4, 'pages': '4.1-4.49'},
    'STEEL STRUCTURE': {'num': 5, 'pages': '5.1-5.62'},
    'ENVIRONMENT ENGINEERING': {'num': 6, 'pages': '6.1-6.83'},
    'GEOTECHNICAL ENGINEERING': {'num': 7, 'pages': '7.1-7.78'},
    'FLUID MECHANICS': {'num': 8, 'pages': '8.1-8.59'},
    'IRRIGATION ENGINEERING': {'num': 9, 'pages': '9.1-9.30'},
    'ENGINEERING HYDROLOGY': {'num': 10, 'pages': '10.1-10.39'},
    'SURVEYING': {'num': 11, 'pages': '11.1-11.69'},
    'HIGHWAY ENGINEERING': {'num': 12, 'pages': '12.1-12.70'},
    'AIRPORT ENGINEERING': {'num': 13, 'pages': '13.1-13.25'},
    'RAILWAY ENGINEERING': {'num': 14, 'pages': '14.1-14.29'},
    'CONSTRUCTION PROJECT MANAGEMENT': {'num': 15, 'pages': '15.1-15.34'},
    'BUILDING MATERIAL CONSTRUCTION': {'num': 16, 'pages': '16.1-16.39'},
    'ENGINEERING MATHEMATICS': {'num': 17, 'pages': '17.1-17.54'},
    'GENERAL APTITUDE': {'num': 18, 'pages': '18.1-18.25'},
}

SKIP_PATTERNS = [
    r'^={3,}',           # Page markers
    r'^GATE WALLAH',     # Header repetition
    r'^GATE-O-PEDIA',    # Publisher header
    r'^CIVIL ENGINEERING$',
    r'^Design Against Static Load$',
    r'^Design Against Dynamic Load$',
]


def is_noise(line):
    """Check if line is boilerplate/noise."""
    for pat in SKIP_PATTERNS:
        if re.match(pat, line.strip()):
            return True
    return False


def extract_subject_boundaries(lines):
    """Find where each subject starts by matching section numbers like '1.1' at line start."""
    boundaries = []
    
    for i, line in enumerate(lines):
        stripped = line.strip()
        # Match top-level section number pattern: "1.1" or "11.1" etc.
        # These appear as "1.1" followed by content, or on their own line
        m = re.match(r'^(\d{1,2})\.1\b', stripped)
        if m:
            chap_num = int(m.group(1))
            if 1 <= chap_num <= 18:
                boundaries.append({
                    'chapter': chap_num,
                    'line': i + 1,
                    'text': stripped[:120]
                })
    
    return boundaries


def extract_topics_in_section(lines, start_idx, end_idx):
    """Extract numbered subtopics within a section."""
    topics = []
    seen = set()
    
    for i in range(start_idx, min(end_idx, len(lines))):
        stripped = lines[i].strip()
        
        # Match patterns like "1.1.1." or "1.2.3."
        m = re.match(r'^(\d+\.\d+\.\d+)\.?\s+(.+)', stripped)
        if m:
            topic_id = m.group(1)
            topic_name = m.group(2).strip()
            if topic_id not in seen and len(topic_name) > 3:
                seen.add(topic_id)
                topics.append({
                    'id': topic_id,
                    'name': topic_name,
                    'line': i + 1
                })
                continue
        
        # Match patterns like "1.1." or "1.2." (2-level topics)
        m = re.match(r'^(\d+\.\d+)\.?\s+([A-Z].+)', stripped)
        if m:
            topic_id = m.group(1)
            topic_name = m.group(2).strip()
            if topic_id not in seen and len(topic_name) > 3:
                seen.add(topic_id)
                topics.append({
                    'id': topic_id,
                    'name': topic_name,
                    'line': i + 1
                })
    
    return topics


def extract_formulas_in_section(lines, start_idx, end_idx):
    """Extract formula-like content from a section."""
    formulas = []
    
    for i in range(start_idx, min(end_idx, len(lines))):
        stripped = lines[i].strip()
        
        # Equation patterns
        if re.match(r'^[A-Z]\s*=\s*.+', stripped) and len(stripped) < 80:
            formulas.append({'line': i+1, 'eq': stripped[:100]})
        elif re.match(r'^[A-Z]\s*[=+−×÷]\s*.+', stripped) and len(stripped) < 80:
            formulas.append({'line': i+1, 'eq': stripped[:100]})
    
    return formulas


def extract_questions_in_section(lines, start_idx, end_idx):
    """Count and categorize questions in a section."""
    questions = {
        'total': 0,
        'mcq': 0,
        'numerical': 0,
        'conceptual': 0,
    }
    
    for i in range(start_idx, min(end_idx, len(lines))):
        stripped = lines[i].strip()
        
        # MCQ pattern (options A/B/C/D)
        if re.match(r'^\(?[A-D]\)?[\.\)]\s+', stripped):
            questions['mcq'] += 1
        
        # Question mark
        if stripped.endswith('?') and len(stripped) > 10:
            questions['total'] += 1
            if re.search(r'(find|calculate|determine|compute|what is the value)', stripped, re.IGNORECASE):
                questions['numerical'] += 1
            else:
                questions['conceptual'] += 1
        
        # Q. pattern
        if re.match(r'^Q\.?\s*\d+', stripped, re.IGNORECASE):
            questions['total'] += 1
    
    return questions


def count_lines_per_subject(lines, boundaries):
    """Count non-blank, non-noise lines per subject."""
    counts = {}
    for i, b in enumerate(boundaries):
        start = b['line'] - 1  # 0-indexed
        end = boundaries[i+1]['line'] - 1 if i+1 < len(boundaries) else len(lines)
        
        meaningful = 0
        for j in range(start, end):
            stripped = lines[j].strip()
            if stripped and not is_noise(stripped):
                meaningful += 1
        
        counts[b['chapter']] = meaningful
    return counts


def extract_all_section_headers(lines):
    """Extract all section-like headers from the full file."""
    headers = []
    for i, line in enumerate(lines):
        stripped = line.strip()
        # Match "X.Y.Z." pattern with following text
        m = re.match(r'^(\d+\.\d+(?:\.\d+)?)\.?\s+(.{5,120})', stripped)
        if m:
            headers.append({
                'line': i+1,
                'id': m.group(1),
                'text': m.group(2).strip(),
                'depth': m.group(1).count('.') + 1
            })
    return headers


def main():
    print("=== GATE-O-PEDIA Full Analysis ===\n")
    
    # Read file
    with open(REF_PATH, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
        lines = content.split('\n')
    
    print(f"File: {len(lines):,} lines, {len(content):,} chars")
    
    # Extract all section headers
    print("\nExtracting section headers...")
    all_headers = extract_all_section_headers(lines)
    print(f"Found {len(all_headers)} section headers")
    
    # Extract subject boundaries
    print("\nFinding subject boundaries...")
    boundaries = extract_subject_boundaries(lines)
    
    # Deduplicate - keep first occurrence of each chapter
    seen_chapters = set()
    unique_boundaries = []
    for b in boundaries:
        if b['chapter'] not in seen_chapters:
            seen_chapters.add(b['chapter'])
            unique_boundaries.append(b)
    boundaries = sorted(unique_boundaries, key=lambda x: x['chapter'])
    
    for b in boundaries:
        subj_name = [k for k, v in SUBJECTS.items() if v['num'] == b['chapter']]
        name = subj_name[0] if subj_name else f"Chapter {b['chapter']}"
        print(f"  Ch {b['chapter']:2d}: {name:40s} (line {b['line']})")
    
    # Count lines per subject
    print("\nCounting content lines per subject...")
    line_counts = count_lines_per_subject(lines, boundaries)
    
    # Build full taxonomy
    taxonomy = {
        'metadata': {
            'total_lines': len(lines),
            'total_chars': len(content),
            'total_section_headers': len(all_headers),
            'subjects_found': len(boundaries),
            'source': 'GATE-O-PEDIA - CIVIL ENGINEERING.txt',
            'publisher': 'Physics Wallah',
            'pages': 947,
        },
        'subjects': [],
        'all_headers_sample': [
            {'line': h['line'], 'id': h['id'], 'text': h['text'][:100], 'depth': h['depth']}
            for h in all_headers[:500]
        ],
    }
    
    # Process each subject
    for i, b in enumerate(boundaries):
        start = b['line'] - 1
        end = boundaries[i+1]['line'] - 1 if i+1 < len(boundaries) else len(lines)
        
        subj_name = [k for k, v in SUBJECTS.items() if v['num'] == b['chapter']]
        name = subj_name[0] if subj_name else f"Chapter {b['chapter']}"
        
        print(f"\nProcessing Ch {b['chapter']}: {name} (lines {b['line']}-{end+1})...")
        
        # Extract topics
        topics = extract_topics_in_section(lines, start, end)
        print(f"  Topics: {len(topics)}")
        
        # Extract formulas
        formulas = extract_formulas_in_section(lines, start, end)
        print(f"  Formulas: {len(formulas)}")
        
        # Extract questions
        questions = extract_questions_in_section(lines, start, end)
        print(f"  Questions: {questions['total']} (MCQ: {questions['mcq']}, Numerical: {questions['numerical']}, Conceptual: {questions['conceptual']})")
        
        # Extract headers for this section
        section_headers = [h for h in all_headers if b['line'] <= h['line'] <= end + 1]
        
        subj_data = {
            'chapter': b['chapter'],
            'name': name,
            'start_line': b['line'],
            'end_line': end + 1,
            'content_lines': line_counts.get(b['chapter'], 0),
            'topics': topics,
            'formula_count': len(formulas),
            'question_count': questions['total'],
            'question_details': questions,
            'section_headers': [
                {'id': h['id'], 'text': h['text'][:100], 'depth': h['depth']}
                for h in section_headers[:200]
            ],
            'sample_formulas': [f['eq'] for f in formulas[:20]],
        }
        taxonomy['subjects'].append(subj_data)
    
    # Save taxonomy
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(TAXONOMY_PATH, 'w', encoding='utf-8') as f:
        json.dump(taxonomy, f, indent=2, ensure_ascii=False)
    print(f"\nTaxonomy saved: {TAXONOMY_PATH}")
    
    # Generate markdown report
    with open(REPORT_PATH, 'w', encoding='utf-8') as f:
        f.write("# GATE-O-PEDIA Complete Analysis\n\n")
        f.write(f"**Source:** `GATE-O-PEDIA - CIVIL ENGINEERING.txt` (Physics Wallah)\n")
        f.write(f"**Total Lines:** {len(lines):,}\n")
        f.write(f"**Total Characters:** {len(content):,}\n")
        f.write(f"**Pages (PDF):** 947\n")
        f.write(f"**Section Headers Found:** {len(all_headers):,}\n\n")
        
        f.write("## Subject Overview\n\n")
        f.write("| # | Subject | Content Lines | Topics | Formulas | Questions |\n")
        f.write("|---|---------|--------------|--------|----------|----------|\n")
        
        total_topics = 0
        total_formulas = 0
        total_questions = 0
        for s in taxonomy['subjects']:
            t = len(s['topics'])
            total_topics += t
            total_formulas += s['formula_count']
            total_questions += s['question_count']
            f.write(f"| {s['chapter']} | {s['name']} | {s['content_lines']:,} | {t} | {s['formula_count']} | {s['question_count']} |\n")
        
        f.write(f"| | **TOTAL** | **{sum(s['content_lines'] for s in taxonomy['subjects']):,}** | **{total_topics}** | **{total_formulas}** | **{total_questions}** |\n\n")
        
        f.write("## Detailed Topic Extraction\n\n")
        for s in taxonomy['subjects']:
            f.write(f"### {s['chapter']}. {s['name']}\n\n")
            f.write(f"- Lines: {s['start_line']}-{s['end_line']} ({s['content_lines']:,} content lines)\n")
            f.write(f"- Topics: {len(s['topics'])}\n")
            f.write(f"- Formulas: {s['formula_count']}\n")
            f.write(f"- Questions: {s['question_count']}\n\n")
            
            if s['topics']:
                f.write("**Topics:**\n\n")
                for t in s['topics']:
                    f.write(f"- `{t['id']}` {t['name']}\n")
                f.write("\n")
            
            if s['sample_formulas']:
                f.write("**Sample Formulas:**\n\n")
                for eq in s['sample_formulas'][:10]:
                    f.write(f"- `{eq}`\n")
                f.write("\n")
            
            if s['section_headers']:
                f.write("**Section Headers (first 30):**\n\n")
                for h in s['section_headers'][:30]:
                    indent = "  " * (h['depth'] - 1)
                    f.write(f"- {indent}`{h['id']}` {h['text']}\n")
                f.write("\n")
            
            f.write("---\n\n")
    
    print(f"Report saved: {REPORT_PATH}")
    print("\n=== Phase A Step 1+2 COMPLETE ===")


if __name__ == '__main__':
    main()
