#!/usr/bin/env python3
"""Analyze content completeness per subject and generate CONTENT_MATRIX.md."""
import os
import re
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
SYSTEM_DIR = REPO_ROOT / "_SYSTEM"

def read_file_safe(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            return f.read()
    except:
        return ""

def count_words(text):
    return len(text.split())

def has_section(text, patterns):
    """Check if any of the regex patterns match in the text."""
    for p in patterns:
        if re.search(p, text, re.IGNORECASE):
            return True
    return False

def has_formulae(text):
    """Check for mathematical formulas/equations."""
    patterns = [
        r'\$\$.*\$\$',  # LaTeX display math
        r'\$[^$]+\$',   # LaTeX inline math
        r'[=≥≤±∑∫∂∇]',  # Math symbols
        r'\\frac',       # LaTeX fractions
        r'\\sqrt',       # LaTeX square root
        r'\\alpha|\\beta|\\gamma|\\epsilon|\\sigma|\\tau|\\omega',  # Greek letters
        r'Q\s*=', r'V\s*=', r'A\s*=', r'P\s*=', r'S\s*=',  # Common variable assignments
        r'm²/s|kg/m³|N/m²|Pa|kPa|MPa|mm/year',  # Units
    ]
    return has_section(text, patterns)

def has_examples(text):
    """Check for solved examples."""
    patterns = [
        r'#{1,4}\s*(Example|Problem|Solution|Solved|Numerical|Calculation)',
        r'Given:|Find:|Solution:|Answer:',
        r'### (Ex|Prob|Sol)',
        r'Step \d+:',
    ]
    return has_section(text, patterns)

def has_mcqs(text):
    """Check for MCQ/test questions."""
    patterns = [
        r'#{1,4}\s*(MCQ|Multiple.Choice|Test\s|Quiz)',
        r'\(a\)|\(b\)|\(c\)|\(d\)',
        r'[A-D]\.\s',
        r'Answer:|Correct:',
    ]
    count = 0
    for p in patterns:
        count += len(re.findall(p, text, re.IGNORECASE))
    return count >= 3  # At least 3 MCQ-like patterns

def has_interview_questions(text):
    """Check for interview-specific questions."""
    patterns = [
        r'#{1,4}\s*(Interview|Q\d+:|Q&A)',
        r'What is the.*\?|Explain.*\.|Describe.*\.|How does.*\?',
        r'Follow-up|follow.up',
        r'Interviewer.*test|interview.*ask',
    ]
    count = 0
    for p in patterns:
        count += len(re.findall(p, text, re.IGNORECASE))
    return count >= 3

def has_revision(text):
    """Check for rapid revision content."""
    patterns = [
        r'#{1,4}\s*(Quick\s+Revision|Rapid\s+Revision|Summary|Cheat\s+Sheet|Key\s+Points)',
        r'#{1,4}\s*(Must\s+Remember|Key\s+Formulas|Formula\s+Sheet)',
        r'RAPID|REVISION|SUMMARY|CHEAT',
    ]
    return has_section(text, patterns)

def has_conceptual_questions(text):
    """Check for conceptual questions."""
    patterns = [
        r'#{1,3}\s*(Conceptual|Short\s+Answer|Theory\s+Questions)',
        r'What\s+is\s+the\s+difference\s+between',
        r'Why\s+do\s+we|Why\s+is\s+it|Why\s+does',
        r'EXPLAIN|Compare|Contrast',
    ]
    count = 0
    for p in patterns:
        count += len(re.findall(p, text, re.IGNORECASE))
    return count >= 3

def has_cross_links(text):
    """Check for cross-reference links."""
    links = re.findall(r'\[([^\]]*)\]\(([^)]*\.md[^)]*)\)', text)
    return len(links) >= 2

# Define subjects to analyze
SUBJECTS = [
    # Core Civil
    ("Structural Analysis", "core/structural-analysis/structural-analysis.md", "CORE", "Structural"),
    ("RCC Design", "core/rcc/rcc-design.md", "CORE", "Structural"),
    ("Steel Design", "core/steel/steel-design.md", "CORE", "Structural"),
    ("Structures (综合)", "core/structures/structures.md", "CORE", "Structural"),
    ("Geotechnical", "core/geotechnical/geotechnical.md", "CORE", "Geotechnical"),
    ("Transportation", "core/transportation/transportation-engineering.md", "CORE", "Transportation"),
    ("Transportation Software", "core/transportation/transportation-software.md", "CORE", "Transportation"),
    ("Environmental Eng.", "core/environmental/environmental-engineering.md", "CORE", "Environmental"),
    ("Engineering Mechanics", "core/fundamentals/engineering-mechanics.md", "CORE", "Fundamentals"),
    ("Strength of Materials", "core/fundamentals/strength-of-materials.md", "CORE", "Fundamentals"),
    ("Civil Foundations", "core/fundamentals/civil-engineering-foundations.md", "CORE", "Fundamentals"),
    ("Geoinformatics", "core/geoinformatics/geoinformatics.md", "CORE", "Geoinformatics"),
    ("Infrastructure Mgmt", "core/infrastructure/infrastructure-engineering-management.md", "CORE", "Infrastructure"),
    # HWRE
    ("Hydraulics", "core/hwre/hydraulics/hydraulics.md", "HWRE", "Hydraulics"),
    ("Turbulence Modeling", "core/hwre/hydraulics/turbulence-modeling.md", "HWRE", "Hydraulics"),
    ("Hydrology", "core/hwre/hydrology/hydrology.md", "HWRE", "Hydrology"),
    ("Sediment Transport", "core/hwre/hydrology/sediment-transport.md", "HWRE", "Hydrology"),
    ("Open Channel Flow", "core/hwre/open_channel_flow/open-channel-flow.md", "HWRE", "OCF"),
    ("Water Resources", "core/hwre/water_resources/water-resources-engineering.md", "HWRE", "Water Resources"),
    ("Flood Control", "core/hwre/flood_control/flood-control.md", "HWRE", "Flood Control"),
    ("Irrigation", "core/hwre/irrigation/irrigation-engineering.md", "HWRE", "Irrigation"),
    ("Wastewater", "core/hwre/wastewater/wastewater-engineering.md", "HWRE", "Wastewater"),
    ("Water Supply", "core/hwre/water_supply/water-supply.md", "HWRE", "Water Supply"),
    ("Groundwater", "core/hwre/water_supply/groundwater.md", "HWRE", "Groundwater"),
    # GATE
    ("GATE Civil Notes", "core/gate/civil/gate-civil-notes.md", "GATE", "GATE"),
    ("GATE Formulas", "core/gate/formulas/gate-civil-formulas.md", "GATE", "GATE"),
    ("GATE Practice", "core/gate/practice/gate-civil-practice.md", "GATE", "GATE"),
    ("GATE Revision", "core/gate/revision_notes/gate-civil-revision.md", "GATE", "GATE"),
    # Non-Core
    ("Non-Core Prep", "non-core/analytics/non-core-prep.md", "NON-CORE", "Analytics"),
    ("Technical Stack", "non-core/analytics/technical-stack.md", "NON-CORE", "Analytics"),
    ("Aptitude Basics", "non-core/aptitude/quantitative/aptitude-basics.md", "NON-CORE", "Aptitude"),
    ("Consulting Overview", "non-core/consulting/consulting-overview.md", "NON-CORE", "Consulting"),
    ("Case Frameworks", "non-core/consulting/case-frameworks.md", "NON-CORE", "Consulting"),
    ("Case Bank", "non-core/consulting/case-bank.md", "NON-CORE", "Consulting"),
    ("Data Analyst", "non-core/data-analyst/da-overview.md", "NON-CORE", "Data Analyst"),
    ("Statistics Practice", "non-core/data-analyst/statistics-practice.md", "NON-CORE", "Data Analyst"),
    ("Finance Overview", "non-core/finance/finance-overview.md", "NON-CORE", "Finance"),
    ("PM Overview", "non-core/product-management/pm-overview.md", "NON-CORE", "Product"),
    # Interview
    ("Tech Interview Bank", "prep/interview/technical/technical-interview-bank.md", "INTERVIEW", "Technical"),
    ("Project Discussion", "prep/interview/technical/project-discussion.md", "INTERVIEW", "Technical"),
    ("HR Interview Guide", "prep/interview/hr/hr-interview-guide.md", "INTERVIEW", "HR"),
    ("Quick Revision Sys", "prep/interview/quick-revision-system.md", "INTERVIEW", "Revision"),
    # Behavioral
    ("Behavioral Guide", "prep/behavioral/behavioral-interview-guide.md", "BEHAVIORAL", "Behavioral"),
    ("HR Questions Bank", "prep/behavioral/hr_questions/hr-questions-bank.md", "BEHAVIORAL", "HR"),
    ("Self Introduction", "prep/behavioral/self_intro/self-introduction.md", "BEHAVIORAL", "Self Intro"),
    ("Answer Frameworks", "prep/behavioral/frameworks/answer-framework-library.md", "BEHAVIORAL", "Frameworks"),
    # Software-Tech
    ("CFD Tech", "software-and-tech/cfd/cfd-tech.md", "SOFTWARE", "CFD"),
    ("Python", "software-and-tech/programming/python.md", "SOFTWARE", "Programming"),
    ("HEC-RAS Walkthrough", "software-and-tech/deep-dives/hec-ras-walkthrough.md", "SOFTWARE", "Deep Dives"),
    ("OpenFOAM Case Study", "software-and-tech/deep-dives/openfoam-case-study.md", "SOFTWARE", "Deep Dives"),
]

def score_subject(has_theory, has_formulae, has_examples, has_mcqs, has_interview, has_revision, has_conceptual, has_links):
    """Score 0-10 based on completeness."""
    score = 0
    if has_theory: score += 2
    if has_formulae: score += 1.5
    if has_examples: score += 1.5
    if has_conceptual: score += 1
    if has_mcqs: score += 1
    if has_interview: score += 1.5
    if has_revision: score += 1
    if has_links: score += 0.5
    return round(min(score, 10), 1)

def main():
    lines = []
    lines.append("# CONTENT_MATRIX.md — Per-Subject Completeness Analysis")
    lines.append("")
    lines.append("Generated by analyze_content.py")
    lines.append("")
    
    # Header
    lines.append("| Subject | Track | Domain | Words | Theory | Formulae | Examples | ConceptQ | MCQs | Interview | Revision | Links | Score | Status |")
    lines.append("|---------|-------|--------|------:|:------:|:--------:|:--------:|:--------:|:----:|:---------:|:--------:|:-----:|------:|--------|")
    
    for name, rel_path, track, domain in SUBJECTS:
        filepath = REPO_ROOT / rel_path
        text = read_file_safe(filepath)
        words = count_words(text)
        
        has_th = has_section(text, [r'#{1,3}\s+', r'##\s+\w'])
        has_fo = has_formulae(text)
        has_ex = has_examples(text)
        has_cq = has_conceptual_questions(text)
        has_mc = has_mcqs(text)
        has_iq = has_interview_questions(text)
        has_rv = has_revision(text)
        has_lk = has_cross_links(text)
        
        sc = score_subject(has_th, has_fo, has_ex, has_mc, has_iq, has_rv, has_cq, has_lk)
        
        if sc >= 8: status = '✓ STRONG'
        elif sc >= 6: status = '△ GOOD'
        elif sc >= 4: status = '△ NEEDS WORK'
        elif sc >= 2: status = '⚠ WEAK'
        else: status = '✗ EMPTY'
        
        def sym(b):
            return '✓' if b else '✗'
        
        lines.append(f"| {name} | {track} | {domain} | {words} | {sym(has_th)} | {sym(has_fo)} | {sym(has_ex)} | {sym(has_cq)} | {sym(has_mc)} | {sym(has_iq)} | {sym(has_rv)} | {sym(has_lk)} | {sc}/10 | {status} |")
    
    lines.append("")
    lines.append("## Score Legend")
    lines.append("- **Theory (2 pts)**: Conceptual explanations exist")
    lines.append("- **Formulae (1.5 pts)**: Mathematical equations/formulas present")
    lines.append("- **Examples (1.5 pts)**: Solved examples with steps")
    lines.append("- **ConceptQ (1 pt)**: Conceptual understanding questions")
    lines.append("- **MCQs (1 pt)**: Multiple-choice test questions")
    lines.append("- **Interview (1.5 pts)**: Interview-specific Q&A")
    lines.append("- **Revision (1 pt)**: Rapid revision/summary content")
    lines.append("- **Links (0.5 pts)**: Cross-references to related topics")
    lines.append("")
    lines.append("## Priority Gaps (P0)")
    lines.append("")
    lines.append("Subjects scoring < 5 that need immediate content creation:")
    lines.append("")
    
    # Calculate stats
    all_scores = []
    for name, rel_path, track, domain in SUBJECTS:
        filepath = REPO_ROOT / rel_path
        text = read_file_safe(filepath)
        words = count_words(text)
        has_th = has_section(text, [r'#{1,3}\s+'])
        has_fo = has_formulae(text)
        has_ex = has_examples(text)
        has_cq = has_conceptual_questions(text)
        has_mc = has_mcqs(text)
        has_iq = has_interview_questions(text)
        has_rv = has_revision(text)
        has_lk = has_cross_links(text)
        sc = score_subject(has_th, has_fo, has_ex, has_mc, has_iq, has_rv, has_cq, has_lk)
        all_scores.append((name, sc, words))
    
    weak = [(n, s, w) for n, s, w in all_scores if s < 5]
    for n, s, w in weak:
        lines.append(f"- **{n}**: {s}/10 ({w} words)")
    
    lines.append("")
    lines.append("## Comprehensive Missing Components")
    lines.append("")
    lines.append("The following components are missing across ALL subjects:")
    lines.append("")
    lines.append("1. **Rapid Revision Sheets** — Only HWRE subjects have some; all others need dedicated revision files")
    lines.append("2. **Subject-level MCQ banks** — The `questions/` directory has only 1 file")
    lines.append("3. **Numerical practice sets** — Most subjects have 1-2 examples, need 10+ per subject")
    lines.append("4. **Separate formula sheets** — Only GATE has a dedicated formula file")
    
    output = '\n'.join(lines)
    
    with open(SYSTEM_DIR / 'CONTENT_MATRIX.md', 'w', encoding='utf-8') as f:
        f.write(output)
    
    print("=== CONTENT MATRIX GENERATED ===")
    print(f"Subjects analyzed: {len(SUBJECTS)}")
    
    scores = [s for _, s, _ in all_scores]
    print(f"Average score: {sum(scores)/len(scores):.1f}/10")
    print(f"Strong (>=8): {sum(1 for s in scores if s >= 8)}")
    print(f"Good (6-7): {sum(1 for s in scores if 6 <= s < 8)}")
    print(f"Needs work (4-5): {sum(1 for s in scores if 4 <= s < 6)}")
    print(f"Weak (<4): {sum(1 for s in scores if s < 4)}")
    print(f"\nP0 gaps (score < 5):")
    for n, s, w in weak:
        print(f"  {n}: {s}/10 ({w} words)")

if __name__ == '__main__':
    main()
