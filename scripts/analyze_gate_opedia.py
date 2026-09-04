#!/usr/bin/env python3
"""
GATE-O-PEDIA Analysis Script
Reads the entire reference file and extracts:
- Subject taxonomy
- Topic hierarchy
- Formula patterns
- Question patterns
- Numerical patterns
- Key concepts
"""

import re
import os
import json
from collections import defaultdict, OrderedDict

REFERENCE_PATH = os.path.join(os.path.dirname(__file__), '..', '..', 'GATE-O-PEDIA - CIVIL ENGINEERING.txt')
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), '..', 'docs', 'audit')
OUTPUT_FILE = os.path.join(OUTPUT_DIR, 'gate_opedia_taxonomy.json')
REPORT_FILE = os.path.join(OUTPUT_DIR, 'gate_opedia_structure.md')


def read_reference(path):
    """Read the entire GATE-O-PEDIA file."""
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
        lines = content.split('\n')
    return content, lines


def extract_heading_structure(lines):
    """Extract all headings (# ## ### ####) and their levels."""
    headings = []
    for i, line in enumerate(lines, 1):
        stripped = line.strip()
        # Match markdown headings
        m = re.match(r'^(#{1,6})\s+(.+)$', stripped)
        if m:
            level = len(m.group(1))
            title = m.group(2).strip()
            headings.append({
                'line': i,
                'level': level,
                'title': title,
                'depth': 'H' + str(level)
            })
    return headings


def classify_subjects(headings):
    """Identify major subject sections from H1/H2 headings."""
    subjects = []
    for h in headings:
        if h['level'] == 1:
            subjects.append({
                'name': h['title'],
                'line': h['line'],
                'topics': []
            })
        elif h['level'] == 2 and subjects:
            subjects[-1]['topics'].append({
                'name': h['title'],
                'line': h['line'],
                'subtopics': []
            })
        elif h['level'] == 3 and subjects and subjects[-1]['topics']:
            subjects[-1]['topics'][-1]['subtopics'].append({
                'name': h['title'],
                'line': h['line']
            })
    return subjects


def extract_formulas(content):
    """Extract formula patterns from the content."""
    formulas = []
    # Common formula patterns
    patterns = [
        r'[A-Z]\s*=\s*[^=\n]{2,30}',          # X = expression
        r'\$\$[^$]+\$\$',                        # LaTeX display math
        r'\$[^$]+\$',                            # LaTeX inline math
        r'[A-Z]\s*\([^)]+\)\s*=',               # Function definitions
    ]
    
    # Find lines with equations
    lines = content.split('\n')
    for i, line in enumerate(lines, 1):
        stripped = line.strip()
        # Look for equation-like content
        if re.search(r'[A-Z]\s*[=]\s*[0-9A-Z]', stripped) and len(stripped) < 200:
            formulas.append({
                'line': i,
                'content': stripped[:150]
            })
        elif stripped.startswith('$$') or (stripped.startswith('$') and stripped.endswith('$') and len(stripped) > 5):
            formulas.append({
                'line': i,
                'content': stripped[:200]
            })
    
    return formulas


def extract_questions(content, lines):
    """Extract question patterns."""
    questions = {
        'conceptual': [],
        'numerical': [],
        'comparison': [],
        'definition': [],
        'short_answer': [],
        'formula_based': []
    }
    
    for i, line in enumerate(lines, 1):
        stripped = line.strip()
        
        # MCQ pattern
        if re.match(r'^(Q\.?\s*\d+|Question\s*\d+|\d+\.\s+[A-Z])', stripped, re.IGNORECASE):
            questions['conceptual'].append({'line': i, 'text': stripped[:120]})
        
        # Numerical pattern
        if re.search(r'(find|calculate|determine|compute|estimate|what is the value)', stripped, re.IGNORECASE):
            if re.search(r'(\d+\.?\d*\s*(m|mm|cm|km|N|kN|Pa|MPa|GPa|kPa|kg|m2|m3|s|rad|deg|kW|MW))', stripped):
                questions['numerical'].append({'line': i, 'text': stripped[:120]})
        
        # Comparison pattern
        if re.search(r'(difference between|compare|versus|vs\.?|distinguish)', stripped, re.IGNORECASE):
            questions['comparison'].append({'line': i, 'text': stripped[:120]})
        
        # Definition pattern
        if re.search(r'(define|what is|what are|state|explain the (concept|meaning|significance))', stripped, re.IGNORECASE):
            questions['definition'].append({'line': i, 'text': stripped[:120]})
    
    return questions


def extract_key_concepts(content):
    """Extract emphasized concepts (bold text, important markers)."""
    concepts = []
    # Bold text patterns
    for m in re.finditer(r'\*\*([^*]{3,80})\*\*', content):
        concepts.append(m.group(1).strip())
    
    # Deduplicate while preserving order
    seen = set()
    unique = []
    for c in concepts:
        if c.lower() not in seen and not c.startswith('http'):
            seen.add(c.lower())
            unique.append(c)
    
    return unique[:200]  # Cap at 200


def extract_numerical_patterns(content):
    """Identify numerical problem types."""
    patterns = defaultdict(int)
    
    # Common numerical categories in civil engineering
    categories = {
        'beam_design': r'(beam|bending|moment|shear|deflection)',
        'column_design': r'(column|buckling|slenderness|axial)',
        'soil_mechanics': r'(bearing capacity|settlement|consolidation|compaction|shear strength|earth pressure)',
        'fluid_mechanics': r'(Bernoulli|Reynolds|pipe flow|head loss|friction factor)',
        'hydraulics': r'(hydraulic jump|specific energy|critical flow| Manning|Chezy)',
        'hydrology': r'(runoff|hydrograph|unit hydrograph|flood|rainfall|infiltration)',
        'water_resources': r'(reservoir|canal|dam|irrigation|groundwater|well)',
        'structural_analysis': r'(truss|frame|moment distribution|slope deflection|matrix)',
        'rcc_design': r'(reinforced concrete|IS 456|limit state|working stress|slab|footing)',
        'steel_design': r'(steel|IS 800|connection|bolt|weld|tension member)',
        'surveying': r'(leveling|traverse|contour|total station|GPS|GIS)',
        'transportation': r'(highway|pavement|traffic|geometric design|IRC)',
        'environmental': r'(water treatment|wastewater|BOD|COD|pollution|sludge)',
        'geotechnical': r'(slope stability|foundation|pile|caisson|retaining wall)',
        'dimensional_analysis': r'(Buckingham|dimensional|similitude|model test)',
        'turbulence': r'(turbulent|Reynolds stress|k-epsilon|boundary layer|viscous)',
    }
    
    content_lower = content.lower()
    for cat, pattern in categories.items():
        count = len(re.findall(pattern, content_lower))
        patterns[cat] = count
    
    return dict(patterns)


def build_subject_line_ranges(headings):
    """Build line ranges for each H1 subject."""
    ranges = []
    h1_positions = [h for h in headings if h['level'] == 1]
    
    for i, h in enumerate(h1_positions):
        start = h['line']
        end = h1_positions[i + 1]['line'] - 1 if i + 1 < len(h1_positions) else None
        ranges.append({
            'name': h['title'],
            'start': start,
            'end': end,
            'line_span': (end - start) if end else 'to_end'
        })
    
    return ranges


def count_questions_per_subject(lines, subject_ranges):
    """Count question-like lines per subject section."""
    counts = {}
    for sr in subject_ranges:
        start = sr['start'] - 1  # 0-indexed
        end = sr['end'] - 1 if sr['end'] else len(lines)
        section_lines = lines[start:end]
        q_count = 0
        for line in section_lines:
            stripped = line.strip()
            if re.match(r'^(Q\.?\s*\d+|Question\s*\d+|\d+\.)', stripped, re.IGNORECASE):
                q_count += 1
            elif re.search(r'(What|Why|How|When|Where|Explain|Define|Describe|Compare|Differentiate)', stripped[:50], re.IGNORECASE) and stripped.endswith('?'):
                q_count += 1
        counts[sr['name']] = q_count
    return counts


def main():
    print("Reading GATE-O-PEDIA reference file...")
    content, lines = read_reference(REFERENCE_PATH)
    print(f"Total lines: {len(lines):,}")
    print(f"Total characters: {len(content):,}")
    
    # 1. Extract heading structure
    print("\nExtracting heading structure...")
    headings = extract_heading_structure(lines)
    print(f"Total headings found: {len(headings)}")
    
    h1_count = sum(1 for h in headings if h['level'] == 1)
    h2_count = sum(1 for h in headings if h['level'] == 2)
    h3_count = sum(1 for h in headings if h['level'] == 3)
    h4_count = sum(1 for h in headings if h['level'] == 4)
    print(f"  H1: {h1_count}, H2: {h2_count}, H3: {h3_count}, H4: {h4_count}")
    
    # 2. Classify subjects
    print("\nClassifying subjects and topics...")
    subjects = classify_subjects(headings)
    for s in subjects:
        t_count = len(s['topics'])
        st_count = sum(len(t['subtopics']) for t in s['topics'])
        print(f"  [{s['name']}] - {t_count} topics, {st_count} subtopics")
    
    # 3. Build subject line ranges
    print("\nBuilding subject line ranges...")
    subject_ranges = build_subject_line_ranges(headings)
    for sr in subject_ranges:
        span = sr['line_span']
        print(f"  {sr['name']}: lines {sr['start']}-{sr['end'] or 'END'} ({span} lines)")
    
    # 4. Extract formulas
    print("\nExtracting formula patterns...")
    formulas = extract_formulas(content)
    print(f"  Found {len(formulas)} formula-like entries")
    
    # 5. Extract questions
    print("\nExtracting question patterns...")
    questions = extract_questions(content, lines)
    for qtype, qlist in questions.items():
        print(f"  {qtype}: {len(qlist)}")
    
    # 6. Extract key concepts
    print("\nExtracting key concepts...")
    concepts = extract_key_concepts(content)
    print(f"  Found {len(concepts)} unique bold concepts")
    
    # 7. Numerical patterns
    print("\nNumerical pattern distribution:")
    num_patterns = extract_numerical_patterns(content)
    for cat, count in sorted(num_patterns.items(), key=lambda x: -x[1]):
        print(f"  {cat}: {count}")
    
    # 8. Questions per subject
    print("\nQuestions per subject section:")
    q_per_subject = count_questions_per_subject(lines, subject_ranges)
    for name, count in sorted(q_per_subject.items(), key=lambda x: -x[1]):
        print(f"  {name}: {count}")
    
    # 9. First 10 H1 headings (subject names)
    print("\n=== SUBJECT LIST (H1 headings) ===")
    for h in headings:
        if h['level'] == 1:
            print(f"  Line {h['line']:5d}: {h['title']}")
    
    # Build complete taxonomy
    taxonomy = {
        'metadata': {
            'total_lines': len(lines),
            'total_chars': len(content),
            'total_headings': len(headings),
            'h1_count': h1_count,
            'h2_count': h2_count,
            'h3_count': h3_count,
            'h4_count': h4_count,
            'total_formulas': len(formulas),
            'total_concepts': len(concepts),
        },
        'subjects': [],
        'subject_ranges': subject_ranges,
        'questions_by_type': {k: len(v) for k, v in questions.items()},
        'questions_by_subject': q_per_subject,
        'numerical_patterns': num_patterns,
        'sample_formulas': formulas[:50],
        'top_concepts': concepts[:100],
    }
    
    for s in subjects:
        subj_data = {
            'name': s['name'],
            'line': s['line'],
            'topics': []
        }
        for t in s['topics']:
            topic_data = {
                'name': t['name'],
                'line': t['line'],
                'subtopics': [st['name'] for st in t['subtopics']]
            }
            subj_data['topics'].append(topic_data)
        taxonomy['subjects'].append(subj_data)
    
    # Save taxonomy JSON
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(taxonomy, f, indent=2, ensure_ascii=False)
    print(f"\nTaxonomy saved to: {OUTPUT_FILE}")
    
    # Save structure report as markdown
    with open(REPORT_FILE, 'w', encoding='utf-8') as f:
        f.write("# GATE-O-PEDIA Structure Analysis\n\n")
        f.write(f"**Source:** `GATE-O-PEDIA - CIVIL ENGINEERING.txt`\n")
        f.write(f"**Total Lines:** {len(lines):,}\n")
        f.write(f"**Total Characters:** {len(content):,}\n\n")
        
        f.write("## Heading Statistics\n\n")
        f.write(f"| Level | Count |\n|-------|-------|\n")
        f.write(f"| H1 (Subjects) | {h1_count} |\n")
        f.write(f"| H2 (Topics) | {h2_count} |\n")
        f.write(f"| H3 (Subtopics) | {h3_count} |\n")
        f.write(f"| H4 (Details) | {h4_count} |\n\n")
        
        f.write("## Subject Taxonomy\n\n")
        for s in subjects:
            f.write(f"### {s['name']} (Line {s['line']})\n\n")
            for t in s['topics']:
                f.write(f"- **{t['name']}** (Line {t['line']})\n")
                for st in t['subtopics']:
                    f.write(f"  - {st['name']}\n")
            f.write("\n")
        
        f.write("## Subject Line Ranges\n\n")
        f.write("| Subject | Start | End | Lines |\n")
        f.write("|---------|-------|-----|-------|\n")
        for sr in subject_ranges:
            f.write(f"| {sr['name']} | {sr['start']} | {sr['end'] or 'END'} | {sr['line_span']} |\n")
        f.write("\n")
        
        f.write("## Numerical Pattern Distribution\n\n")
        f.write("| Category | Mentions |\n|----------|----------|\n")
        for cat, count in sorted(num_patterns.items(), key=lambda x: -x[1]):
            f.write(f"| {cat} | {count} |\n")
        f.write("\n")
        
        f.write("## Questions by Subject\n\n")
        f.write("| Subject | Questions |\n|---------|----------|\n")
        for name, count in sorted(q_per_subject.items(), key=lambda x: -x[1]):
            if count > 0:
                f.write(f"| {name} | {count} |\n")
        f.write("\n")
        
        f.write("## Questions by Type\n\n")
        f.write("| Type | Count |\n|------|-------|\n")
        for qtype, qlist in questions.items():
            f.write(f"| {qtype} | {len(qlist)} |\n")
        f.write("\n")
        
        f.write("## Top 100 Key Concepts (Bold Text)\n\n")
        for i, c in enumerate(concepts[:100], 1):
            f.write(f"{i}. {c}\n")
        f.write("\n")
    
    print(f"Structure report saved to: {REPORT_FILE}")
    print("\nDONE - Phase A Step 1 complete.")


if __name__ == '__main__':
    main()
