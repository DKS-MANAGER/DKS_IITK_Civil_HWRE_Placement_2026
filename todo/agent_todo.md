# Agent TODO — DKS IITK Civil / HWRE Placement 2026

## Purpose
This file tracks all remaining work for the repository build. It is used by the agent to continue work in chunks without hitting output limits.

## Completed Phases
- [x] Phase 1: Discovery — Scanned all 10 source repos and 1 gist
- [x] Phase 2: Classification — Classified files by topic and usefulness
- [x] Phase 3: Indexing — Created master_index.md, source_map.csv, topic_map.md
- [x] Phase 4: Repository Structure — Created all directories

## Remaining Phases

### Phase 5: Extraction & Content Generation
Write the following canonical notes. Each note must paraphrase source content and include source references at the bottom.

#### Priority P0 — Core Placement Prep
- [ ] civil/fundamentals/civil-engineering-foundations.md
- [ ] civil/hydraulics/hydraulics.md
- [ ] civil/hydraulics/turbulence-modeling.md
- [ ] civil/open_channel_flow/open-channel-flow.md
- [ ] civil/hydrology/hydrology.md
- [ ] civil/hydrology/sediment-transport.md
- [ ] civil/water_resources/water-resources-engineering.md
- [ ] civil/geotechnical/geotechnical.md
- [ ] civil/structures/structures.md
- [ ] hwre/irrigation/irrigation-engineering.md
- [ ] hwre/water_supply/groundwater.md
- [ ] hwre/water_supply/water-supply.md
- [ ] hwre/wastewater/wastewater-engineering.md
- [ ] hwre/flood_control/flood-control.md
- [ ] aptitude/quantitative/aptitude-basics.md
- [ ] aptitude/quantitative/data-interpretation.md
- [ ] aptitude/quantitative/percentages.md
- [ ] aptitude/quantitative/time-work.md
- [ ] aptitude/quantitative/speed-time-distance.md
- [ ] aptitude/quantitative/probability.md
- [ ] aptitude/quantitative/permutations-combinations.md
- [ ] aptitude/quantitative/profit-loss-discount.md
- [ ] aptitude/shortcuts/aptitude-shortcuts.md
- [ ] aptitude/logical_reasoning/reasoning-practice.md
- [ ] aptitude/verbal/verbal-ability.md
- [ ] behavioral/self_intro/self-introduction.md
- [ ] behavioral/teamwork/teamwork.md
- [ ] behavioral/leadership/leadership.md
- [ ] behavioral/conflict_resolution/conflict-resolution.md
- [ ] behavioral/behavioral-interview-guide.md
- [ ] behavioral/hr_questions/hr-questions-bank.md
- [ ] interviews/technical/technical-interview-bank.md
- [ ] interviews/hr/hr-interview-guide.md
- [ ] interviews/company_specific/company-profiles.md
- [ ] interviews/company_specific/interview-experiences.md
- [ ] interviews/mock_questions/mock-interview-questions.md
- [ ] gate/formulas/gate-civil-formulas.md
- [ ] gate/revision_notes/gate-civil-revision.md
- [ ] gate/practice/gate-civil-practice.md
- [ ] resources/book_list.md
- [ ] resources/paper_list.md
- [ ] resources/links.md
- [ ] resources/technical-stack.md
- [ ] resources/non-core-prep.md
- [ ] resources/placement-data.md
- [ ] templates/resume-template.md
- [ ] templates/self_intro_template.md
- [ ] templates/interview_answer_template.md
- [ ] templates/study_plan_template.md
- [ ] placement-roadmap.md

#### Priority P1 — Additional Content
- [ ] aptitude/quantitative/ratio-proportion.md
- [ ] aptitude/quantitative/number-system.md
- [ ] aptitude/quantitative/averages.md
- [ ] aptitude/quantitative/problems-on-ages.md
- [ ] aptitude/quantitative/partnership.md
- [ ] aptitude/quantitative/problems-on-train.md
- [ ] hwre/irrigation/irrigation-engineering.md (expanded)
- [ ] hwre/exam_notes/hwre-exam-notes.md
- [ ] gate/civil/gate-civil-notes.md
- [ ] interviews/company_specific/tech-mahindra.md
- [ ] interviews/company_specific/schneider-electric.md
- [ ] interviews/company_specific/musigma.md
- [ ] interviews/company_specific/johnson-controls.md
- [ ] interviews/company_specific/hubstream.md
- [ ] interviews/company_specific/hiremi.md
- [ ] interviews/company_specific/expeditor.md
- [ ] interviews/company_specific/deltax.md
- [ ] interviews/company_specific/darwin-box.md
- [ ] interviews/company_specific/cei-american.md

### Phase 6: Final Files
- [ ] README.md — Repo overview, structure, usage
- [ ] LICENSE — MIT License
- [ ] CHANGELOG.md — Build summary with phases
- [ ] todo/agent_todo.md — This file (already created)

### Phase 7: Quality Check
- [ ] Verify all source references are present at bottom of each note
- [ ] Verify no long verbatim passages are copied
- [ ] Verify all formulas and definitions are preserved accurately
- [ ] Verify directory structure matches plan
- [ ] Verify index files are complete and accurate
- [ ] Verify README has correct structure description
- [ ] Verify CHANGELOG documents all phases
- [ ] Verify all company interview experience files are included
- [ ] Verify Aptitude-For-Placements problem sets are referenced
- [ ] Verify GATE material is properly attributed

## Duplicates to Resolve
- Behavioral interview tips appear in 3 repos (awesome-behavioral-interviews, behavioral-interview-list-of-questions, interview-handbook-2026) → Merged into one note
- Technical questions appear in 3 repos (Civil_Placement_IITK, interview-handbook-2026, campus-placement-prep) → Merged into one note
- Aptitude basics appear in 3 repos (Aptitude, Aptitude-For-Placements, campus-placement-prep) → Merged into one note
- Water resources software appears in 2 repos (Civil_Placement_IITK, awesome-civil-engineering) → Merged into one note

## Conflicts to Verify
- Civil_Placement_IITK mentions OpenFOAM/SedFoam for CFD; awesome-civil-engineering mentions FLOW-3D, OpenFOAM → Keep both, note differences
- Aptitude repo has 34 topics with LaTeX; Aptitude-For-Placements has plain text problems → Merge concepts, keep problem sets separate
- Placement_Preparation has old interview experiences (2011 onwards); Civil_Placement_IITK has recent company profiles → Keep both, label clearly

## Notes Still to Convert
- All 34 Aptitude topic files from Aptitude/ need to be summarized into aptitude-basics.md
- All Aptitude-For-Placements problem sets need to be referenced in aptitude-basics.md
- Placement_Preparation interview experiences need to be summarized in interview-experiences.md
- Civil_Placement_IITK placement_data.csv needs to be converted to placement-data.md
- awesome-civil-engineering resources.json needs to be converted to links.md

## Source Mappings Still to Finalize
- Map all 10 Aptitude-For-Placements subfolders to aptitude topics
- Map all 11 Placement_Preparation interview experiences to company_specific files
- Map all 34 Aptitude topic files to aptitude topics
- Map GATE_Civil_Study_Material_2027.md sections to gate/ files

## Sections Still to Organize
- hwre/exam_notes/ — Needs content from Civil_Placement_IITK and GATE material
- gate/civil/ — Needs chapter-wise notes from GATE_Civil_Study_Material_2027.md
- resources/ — Needs consolidation of all external links

## Cleanup Tasks
- [ ] Remove any empty directories after content generation
- [ ] Verify no source files were modified (treat as read-only)
- [ ] Verify all generated files have proper markdown formatting
- [ ] Verify all generated files have source references at bottom
- [ ] Verify file naming is consistent (lowercase with hyphens)
- [ ] Verify no temporary files remain in repo root

## Batch Work Items for Agent
1. Write all P0 notes (46 files) in parallel using multiple agents
2. Write all P1 notes (20 files) in parallel using multiple agents
3. Write final files (README, LICENSE, CHANGELOG)
4. Run quality checks on all generated files
5. Finalize index files if any topics were missed
