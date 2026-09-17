#!/usr/bin/env python3
"""
Corrected GATE-O-PEDIA Analysis using GATE WALLAH header-based boundaries.
Then audit repository coverage and build gap matrix.
"""
import re
import os
import json
from collections import defaultdict

REF_PATH = os.path.join('f:', os.sep, '2k26Placement', 'GATE-O-PEDIA - CIVIL ENGINEERING.txt')
REPO_PATH = os.path.join('f:', os.sep, '2k26Placement', 'DKS_IITK_Civil_HWRE_Placement_2026')
OUT_DIR = os.path.join(REPO_PATH, 'docs', 'audit')

# Corrected subject boundaries based on GATE WALLAH header analysis
SUBJECTS = [
    {'num': 1,  'name': 'Engineering Mechanics',           'start': 1,     'end': 1189,   'gate_chapters': 7},
    {'num': 2,  'name': 'Strength of Materials',            'start': 1190,  'end': 3040,   'gate_chapters': 6},
    {'num': 3,  'name': 'Structural Analysis',              'start': 3041,  'end': 4755,   'gate_chapters': 6},
    {'num': 4,  'name': 'Reinforced Cement Concrete',       'start': 4756,  'end': 6886,   'gate_chapters': 9},
    {'num': 5,  'name': 'Steel Structures',                 'start': 6887,  'end': 8872,   'gate_chapters': 10},
    {'num': 6,  'name': 'Environmental Engineering',        'start': 8873,  'end': 13930,  'gate_chapters': 5},
    {'num': 7,  'name': 'Geotechnical Engineering',         'start': 13931, 'end': 17157,  'gate_chapters': 12},
    {'num': 8,  'name': 'Fluid Mechanics',                  'start': 17158, 'end': 21098,  'gate_chapters': 8},
    {'num': 9,  'name': 'Irrigation Engineering',           'start': 21099, 'end': 22203,  'gate_chapters': 7},
    {'num': 10, 'name': 'Engineering Hydrology',            'start': 22204, 'end': 23892,  'gate_chapters': 9},
    {'num': 11, 'name': 'Surveying',                        'start': 23893, 'end': 26530,  'gate_chapters': 12},
    {'num': 12, 'name': 'Highway Engineering',              'start': 26531, 'end': 29526,  'gate_chapters': 4},
    {'num': 13, 'name': 'Airport Engineering',              'start': 29527, 'end': 30151,  'gate_chapters': 10},
    {'num': 14, 'name': 'Railway Engineering',              'start': 30152, 'end': 30889,  'gate_chapters': 10},
    {'num': 15, 'name': 'Construction Project Management',  'start': 30890, 'end': 32298,  'gate_chapters': 10},
    {'num': 16, 'name': 'Building Materials & Construction','start': 32299, 'end': 33693,  'gate_chapters': 7},
    {'num': 17, 'name': 'Engineering Mathematics',          'start': 33694, 'end': 36879,  'gate_chapters': 7},
    {'num': 18, 'name': 'General Aptitude',                 'start': 36880, 'end': 37734,  'gate_chapters': 12},
]

# Repository file map
REPO_FILES = {}

def scan_repo_files():
    """Scan all .md files in the repository."""
    global REPO_FILES
    for root, dirs, files in os.walk(REPO_PATH):
        # Skip hidden dirs and scripts
        dirs[:] = [d for d in dirs if not d.startswith('.') and d not in ['node_modules', 'scripts', '__pycache__']]
        for f in files:
            if f.endswith('.md'):
                full = os.path.join(root, f)
                rel = os.path.relpath(full, REPO_PATH)
                try:
                    with open(full, 'r', encoding='utf-8', errors='ignore') as fh:
                        content = fh.read()
                        lines = content.split('\n')
                    REPO_FILES[rel] = {
                        'lines': len(lines),
                        'chars': len(content),
                        'headings': extract_headings(lines),
                        'content': content,
                    }
                except Exception:
                    pass

def extract_headings(lines):
    """Extract all headings from markdown."""
    headings = []
    for line in lines:
        m = re.match(r'^(#{1,6})\s+(.+)', line.strip())
        if m:
            headings.append({'level': len(m.group(1)), 'title': m.group(2).strip()})
    return headings

def count_questions(filepath_data):
    """Count questions in a repo file."""
    content = filepath_data.get('content', '')
    count = 0
    count += len(re.findall(r'###\s*Q\d+:', content))
    count += len(re.findall(r'\d+\.\s+.*\?', content))
    return count

def extract_repo_subject_coverage():
    """Map repository files to GATE-O-PEDIA subjects."""
    coverage = {}
    for subj in SUBJECTS:
        name = subj['name'].lower()
        subj_files = []
        
        for fpath, fdata in REPO_FILES.items():
            fpath_lower = fpath.lower()
            fname_lower = os.path.basename(fpath).lower()
            
            # Match subject to repo files
            matched = False
            if subj['num'] == 1 and any(k in fpath_lower for k in ['mechanics', 'engineering_mechanics']):
                matched = True
            elif subj['num'] == 2 and any(k in fpath_lower for k in ['strength', 'som', 'stress', 'strain']):
                matched = True
            elif subj['num'] == 3 and any(k in fpath_lower for k in ['structural_analysis', 'structural-analysis']):
                matched = True
            elif subj['num'] == 4 and any(k in fpath_lower for k in ['rcc', 'reinforced', 'concrete']):
                if 'steel' not in fpath_lower:
                    matched = True
            elif subj['num'] == 5 and any(k in fpath_lower for k in ['steel']):
                matched = True
            elif subj['num'] == 6 and any(k in fpath_lower for k in ['environment', 'environmental', 'water_treatment', 'wastewater']):
                matched = True
            elif subj['num'] == 7 and any(k in fpath_lower for k in ['geotech', 'soil', 'foundation']):
                matched = True
            elif subj['num'] == 8 and any(k in fpath_lower for k in ['fluid_mechanics', 'fluid-mechanics', 'fluids']):
                if 'open_channel' not in fpath_lower:
                    matched = True
            elif subj['num'] == 9 and any(k in fpath_lower for k in ['irrigation']):
                matched = True
            elif subj['num'] == 10 and any(k in fpath_lower for k in ['hydrology']):
                matched = True
            elif subj['num'] == 11 and any(k in fpath_lower for k in ['survey', 'surveying', 'geomatics', 'geoinformatics']):
                matched = True
            elif subj['num'] == 12 and any(k in fpath_lower for k in ['highway', 'transportation', 'traffic', 'pavement']):
                matched = True
            elif subj['num'] == 13 and any(k in fpath_lower for k in ['airport']):
                matched = True
            elif subj['num'] == 14 and any(k in fpath_lower for k in ['railway']):
                matched = True
            elif subj['num'] == 15 and any(k in fpath_lower for k in ['construction', 'project_management', 'project-management', 'estimation', 'scheduling', 'cpm', 'pert']):
                matched = True
            elif subj['num'] == 16 and any(k in fpath_lower for k in ['building_material', 'building-material', 'cement', 'brick', 'timber', 'aggregate']):
                matched = True
            elif subj['num'] == 17 and any(k in fpath_lower for k in ['math', 'mathematics', 'calculus', 'algebra', 'probability', 'statistics', 'differential']):
                matched = True
            elif subj['num'] == 18 and any(k in fpath_lower for k in ['aptitude', 'quantitative', 'verbal', 'reasoning']):
                matched = True
            
            # Also check HWRE subtopics
            if subj['num'] == 8 and any(k in fpath_lower for k in ['hydraulics']):
                matched = True
            if subj['num'] == 10 and any(k in fpath_lower for k in ['water_resources', 'water-resources']):
                matched = True
            
            if matched:
                subj_files.append(fpath)
        
        coverage[subj['name']] = {
            'files': subj_files,
            'file_count': len(subj_files),
            'total_lines': sum(REPO_FILES[f]['lines'] for f in subj_files),
            'total_chars': sum(REPO_FILES[f]['chars'] for f in subj_files),
        }
    
    return coverage


def extract_source_topics(lines, start, end):
    """Extract topics from a subject section."""
    topics = []
    seen = set()
    for i in range(start - 1, min(end, len(lines))):
        stripped = lines[i].strip()
        m = re.match(r'^(\d+\.\d+(?:\.\d+)?)\.?\s+(.{5,120})', stripped)
        if m:
            tid = m.group(1)
            tname = m.group(2).strip()
            if tid not in seen and len(tname) > 3:
                seen.add(tid)
                topics.append({'id': tid, 'name': tname, 'line': i+1})
    return topics


def main():
    print("=== GATE-O-PEDIA Corrected Analysis + Repository Audit ===\n")
    
    # Read reference file
    with open(REF_PATH, 'r', encoding='utf-8', errors='ignore') as f:
        ref_content = f.read()
        ref_lines = ref_content.split('\n')
    
    # Scan repository
    print("Scanning repository files...")
    scan_repo_files()
    print(f"Found {len(REPO_FILES)} markdown files in repository\n")
    
    # Analyze each subject
    results = []
    for subj in SUBJECTS:
        start = subj['start']
        end = subj['end']
        content_lines = end - start + 1
        
        # Extract topics from source
        topics = extract_source_topics(ref_lines, start, end)
        
        # Count formulas in section
        formula_count = 0
        for i in range(start-1, min(end, len(ref_lines))):
            stripped = ref_lines[i].strip()
            if re.match(r'^[A-Z]\s*=\s*.+', stripped) and len(stripped) < 80:
                formula_count += 1
        
        print(f"Ch {subj['num']:2d}: {subj['name']:40s} | Lines {start:5d}-{end:5d} ({content_lines:5d}) | Topics: {len(topics):3d} | Formulas: {formula_count:3d}")
        
        results.append({
            **subj,
            'content_lines': content_lines,
            'source_topics': topics,
            'source_topic_count': len(topics),
            'source_formula_count': formula_count,
        })
    
    # Repository coverage
    print("\n\n=== REPOSITORY COVERAGE ===\n")
    coverage = extract_repo_subject_coverage()
    
    for subj in SUBJECTS:
        cov = coverage[subj['name']]
        status = "COVERED" if cov['file_count'] > 0 else "MISSING"
        print(f"Ch {subj['num']:2d}: {subj['name']:40s} | Files: {cov['file_count']:3d} | Lines: {cov['total_lines']:5d} | Status: {status}")
        if cov['files']:
            for fp in cov['files'][:5]:
                print(f"         -> {fp}")
    
    # Build gap matrix
    print("\n\n=== GAP MATRIX ===\n")
    gap_matrix = []
    for subj in SUBJECTS:
        src = next(r for r in results if r['num'] == subj['num'])
        cov = coverage[subj['name']]
        
        if cov['file_count'] == 0:
            action = 'ADD'
            depth = 'NONE'
        elif src['source_topic_count'] > 20 and cov['total_lines'] < 200:
            action = 'DEEPEN'
            depth = 'SHALLOW'
        elif cov['total_lines'] > 2000:
            action = 'KEEP'
            depth = 'DEEP'
        elif cov['total_lines'] > 500:
            action = 'KEEP'
            depth = 'MODERATE'
        else:
            action = 'DEEPEN'
            depth = 'THIN'
        
        gap_matrix.append({
            'subject': subj['name'],
            'source_topics': src['source_topic_count'],
            'source_formulas': src['source_formula_count'],
            'repo_files': cov['file_count'],
            'repo_lines': cov['total_lines'],
            'depth': depth,
            'action': action,
        })
        
        print(f"{subj['name']:40s} | Src Topics: {src['source_topic_count']:3d} | Repo Files: {cov['file_count']:3d} | Depth: {depth:10s} | Action: {action}")
    
    # Save comprehensive results
    final = {
        'metadata': {
            'source_file': 'GATE-O-PEDIA - CIVIL ENGINEERING.txt',
            'publisher': 'Physics Wallah',
            'total_lines': len(ref_lines),
            'total_chars': len(ref_content),
            'total_repo_files': len(REPO_FILES),
        },
        'subjects': results,
        'repository_coverage': {k: {kk: vv for kk, vv in v.items() if kk != 'content'} for k, v in coverage.items()},
        'gap_matrix': gap_matrix,
    }
    
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(os.path.join(OUT_DIR, 'gate_opedia_corrected_analysis.json'), 'w', encoding='utf-8') as f:
        json.dump(final, f, indent=2, ensure_ascii=False, default=str)
    
    print(f"\nResults saved to: {os.path.join(OUT_DIR, 'gate_opedia_corrected_analysis.json')}")
    print("\n=== PHASE A COMPLETE + PHASE B MATRIX BUILT ===")


if __name__ == '__main__':
    main()
