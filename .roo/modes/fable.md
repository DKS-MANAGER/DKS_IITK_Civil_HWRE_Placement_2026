# 🎯 Fable — Placement Preparation Command Center

> **Your one-stop hub for IIT Kanpur Civil / HWRE Placement Preparation (Dec 2026)**
> Structured execution protocol + study planner + progress tracker + interview prep

---

## 📌 Quick Navigation

| Section | Description |
|---------|-------------|
| [Role Definition](#role-definition) | Core Fable mode behavior and protocol |
| [📋 Study Planner](#-study-planner) | Daily/weekly study schedule with time blocks |
| [📊 Progress Dashboard](#-progress-dashboard) | Track completion across all 46 topics |
| [🔥 Interview Prep Matrix](#-interview-prep-matrix) | Company-wise preparation targets |
| [⚡ Daily Checklist](#-daily-checklist) | Morning, afternoon, evening routines |
| [📚 Topic Quick-Links](#-topic-quick-links) | Direct links to all content areas |
| [🏗️ Phase Tracker](#-phase-tracker) | 5-phase roadmap with KPIs |
| [📝 Mock Interview Tracker](#-mock-interview-tracker) | Track mock sessions and feedback |
| [🛡️ Fable Protocol](#-fable-protocol) | Stage-based execution protocol |

---

## Role Definition

You are a highly skilled software engineer operating in Fable Mode — a structured, stage-based execution protocol for systematic code generation, verification, and quality assurance.

Your core behavior:
1. Always output a numbered stage map at the start of any task
2. Execute stages sequentially: ANALYZE → PLAN → IMPLEMENT → VERIFY → REVIEW → COMPLETE
3. Run actual terminal commands for verification — never claim success without showing command output
4. Perform failable checks at each stage transition
5. Generate a 5-pass double-check report (correctness, style, integration, documentation, security) before marking any task complete

You must NEVER:
- Skip the stage map output
- Mark VERIFY stage complete without running terminal commands
- Batch multiple file writes without intermediate confirmation
- Proceed to next stage when a failable check fails
- Claim "tests pass" without showing actual test output

You must ALWAYS:
- Use read_file before modifying any file
- Execute verification commands via execute_command
- Show actual command output
- Return to previous stage on failure
- Provide a final status report with the double-check report

## Short Description

Structured stage-based execution protocol with mandatory verification and double-check reports. Also serves as the one-stop placement preparation command center for IITK Civil/HWRE.

## When to Use

Use Fable mode for any coding task that requires high reliability: feature implementation, bug fixes, refactoring, or multi-file changes. It enforces a rigorous stage-gate process with terminal verification at every step, preventing premature completion and ensuring code quality.

## Available Tools

- read_file
- write_to_file
- apply_diff
- search_files
- list_files
- execute_command
- read_command_output
- ask_followup_question
- attempt_completion
- update_todo_list
- new_task
- switch_mode
- skill

---

## 📋 Study Planner

### Daily Time Blocks (Weekday)

| Time Block | Activity | Duration | Target |
|------------|----------|----------|--------|
| **06:00–07:00** | 🔢 Aptitude Speed Drill | 60 min | 20 problems (mix of topics) |
| **07:00–07:30** | 📖 Flashcard Recall (Core) | 30 min | 30 flashcards, 90%+ recall |
| **08:00–10:00** | 🏗️ Core Civil Revision | 120 min | 1 topic deep-dive + 5 numericals |
| **10:00–10:15** | ☕ Break | 15 min | — |
| **10:15–12:00** | 💻 Coding / Python / SQL | 105 min | 1 script or 2 SQL problems |
| **12:00–13:00** | 🍽️ Lunch + Review Notes | 60 min | Skim morning notes |
| **13:00–14:30** | 🌊 HWRE / CFD / OpenFOAM | 90 min | 1 topic + OpenFOAM case |
| **14:30–14:45** | ☕ Break | 15 min | — |
| **14:45–16:00** | 🎤 Behavioral / Mock Interview | 75 min | 2 STAR stories + 1 mock Q&A |
| **16:00–17:00** | 📊 Data Interpretation / GATE | 60 min | 1 DI set or 5 GATE PYQs |
| **17:00–17:30** | 📝 Daily Review & Log | 30 min | Update tracker, fill gaps |
| **21:00–22:00** | 📚 Light Reading / Company Intel | 60 min | Company profile or interview experience |

**Total Study: ~8.5 hours/day**

### Weekend Time Blocks

| Time Block | Activity | Duration | Target |
|------------|----------|----------|--------|
| **08:00–10:00** | 🏗️ Core Civil Deep Dive | 120 min | Full topic coverage + derivations |
| **10:00–10:15** | ☕ Break | 15 min | — |
| **10:15–12:00** | 🎤 Mock Interview Session | 105 min | Full mock (tech + HR) |
| **12:00–13:00** | 🍽️ Lunch | 60 min | — |
| **13:00–15:00** | 💻 Coding + Projects | 120 min | 2 scripts or project work |
| **15:00–15:15** | ☕ Break | 15 min | — |
| **15:15–17:00** | 📊 GATE Practice + Aptitude | 105 min | 10 GATE problems + 20 aptitude |
| **17:00–18:00** | 📝 Weekly Review & Planning | 60 min | Update roadmap, plan next week |

**Total Weekend Study: ~7.5 hours/day**

---

## 📊 Progress Dashboard

### Overall Completion Tracker

| Category | Files | Completed | % | Status |
|----------|-------|-----------|---|--------|
| 🏗️ Core Civil | 14 | ___ | __% | ⬜ |
| 💧 HWRE | 7 | ___ | __% | ⬜ |
| 🧮 Aptitude | 14 | ___ | __% | ⬜ |
| 🎤 Behavioral | 6 | ___ | __% | ⬜ |
| 📋 GATE | 4 | ___ | __% | ⬜ |
| 🏢 Interviews | 8 | ___ | __% | ⬜ |
| 📄 Templates | 4 | ___ | __% | ⬜ |
| 📚 Resources | 5 | ___ | __% | ⬜ |
| 🗂️ Index/Nav | 4 | ___ | __% | ⬜ |
| **TOTAL** | **66** | ___ | **__%** | ⬜ |

### Topic-Level Completion

#### 🏗️ Core Civil Engineering
| Topic | File | Read | Notes | Numericals | Interview Ready |
|-------|------|------|-------|------------|-----------------|
| Hydraulics | [`hydraulics.md`](../civil/hydraulics/hydraulics.md) | ⬜ | ⬜ | ⬜ | ⬜ |
| Turbulence Modeling | [`turbulence-modeling.md`](../civil/hydraulics/turbulence-modeling.md) | ⬜ | ⬜ | ⬜ | ⬜ |
| Open Channel Flow | [`open-channel-flow.md`](../civil/open_channel_flow/open-channel-flow.md) | ⬜ | ⬜ | ⬜ | ⬜ |
| Hydrology | [`hydrology.md`](../civil/hydrology/hydrology.md) | ⬜ | ⬜ | ⬜ | ⬜ |
| Sediment Transport | [`sediment-transport.md`](../civil/hydrology/sediment-transport.md) | ⬜ | ⬜ | ⬜ | ⬜ |
| Structures | [`structures.md`](../civil/structures/structures.md) | ⬜ | ⬜ | ⬜ | ⬜ |
| Geotechnical | [`geotechnical.md`](../civil/geotechnical/geotechnical.md) | ⬜ | ⬜ | ⬜ | ⬜ |
| Foundations | [`civil-engineering-foundations.md`](../civil/fundamentals/civil-engineering-foundations.md) | ⬜ | ⬜ | ⬜ | ⬜ |
| **Environmental Engg** | [`environmental-engineering.md`](../civil/environmental/environmental-engineering.md) | ⬜ | ⬜ | ⬜ | ⬜ |
| **Geoinformatics** | [`geoinformatics.md`](../civil/geoinformatics/geoinformatics.md) | ⬜ | ⬜ | ⬜ | ⬜ |
| **Infrastructure Engg & Mgmt** | [`infrastructure-engineering-management.md`](../civil/infrastructure/infrastructure-engineering-management.md) | ⬜ | ⬜ | ⬜ | ⬜ |
| **Transportation Engg** | [`transportation-engineering.md`](../civil/transportation/transportation-engineering.md) | ⬜ | ⬜ | ⬜ | ⬜ |
| Water Resources | [`water-resources-engineering.md`](../civil/water_resources/water-resources-engineering.md) | ⬜ | ⬜ | ⬜ | ⬜ |

#### 💧 HWRE
| Topic | File | Read | Notes | Numericals | Interview Ready |
|-------|------|------|-------|------------|-----------------|
| Irrigation | [`irrigation-engineering.md`](../hwre/irrigation/irrigation-engineering.md) | ⬜ | ⬜ | ⬜ | ⬜ |
| Wastewater | [`wastewater-engineering.md`](../hwre/wastewater/wastewater-engineering.md) | ⬜ | ⬜ | ⬜ | ⬜ |
| Water Supply | [`water-supply.md`](../hwre/water_supply/water-supply.md) | ⬜ | ⬜ | ⬜ | ⬜ |
| Groundwater | [`groundwater.md`](../hwre/water_supply/groundwater.md) | ⬜ | ⬜ | ⬜ | ⬜ |
| Flood Control | [`flood-control.md`](../hwre/flood_control/flood-control.md) | ⬜ | ⬜ | ⬜ | ⬜ |
| HWRE Exam Notes | [`hwre-exam-notes.md`](../hwre/exam_notes/hwre-exam-notes.md) | ⬜ | ⬜ | ⬜ | ⬜ |

#### 🧮 Aptitude
| Topic | File | Read | Solved | Speed Target |
|-------|------|------|--------|--------------|
| Basics | [`aptitude-basics.md`](../aptitude/quantitative/aptitude-basics.md) | ⬜ | ⬜ | < 2 min/q |
| Averages | [`averages.md`](../aptitude/quantitative/averages.md) | ⬜ | ⬜ | < 1.5 min/q |
| Percentages | [`percentages.md`](../aptitude/quantitative/percentages.md) | ⬜ | ⬜ | < 1 min/q |
| Profit & Loss | [`profit-loss-discount.md`](../aptitude/quantitative/profit-loss-discount.md) | ⬜ | ⬜ | < 2 min/q |
| Speed/Time/Distance | [`speed-time-distance.md`](../aptitude/quantitative/speed-time-distance.md) | ⬜ | ⬜ | < 2 min/q |
| Time & Work | [`time-work.md`](../aptitude/quantitative/time-work.md) | ⬜ | ⬜ | < 1.5 min/q |
| Ratio & Proportion | [`ratio-proportion.md`](../aptitude/quantitative/ratio-proportion.md) | ⬜ | ⬜ | < 1.5 min/q |
| Probability | [`probability.md`](../aptitude/quantitative/probability.md) | ⬜ | ⬜ | < 2 min/q |
| Data Interpretation | [`data-interpretation.md`](../aptitude/quantitative/data-interpretation.md) | ⬜ | ⬜ | < 5 min/set |
| Shortcuts | [`aptitude-shortcuts.md`](../aptitude/shortcuts/aptitude-shortcuts.md) | ⬜ | ⬜ | Master 20+ |
| Logical Reasoning | [`reasoning-practice.md`](../aptitude/logical_reasoning/reasoning-practice.md) | ⬜ | ⬜ | < 3 min/q |
| Verbal Ability | [`verbal-ability.md`](../aptitude/verbal/verbal-ability.md) | ⬜ | ⬜ | — |

---

## 🔥 Interview Prep Matrix

### Company-Wise Preparation Status

| Company | CTC | Round | Prep Status | Mock Done | Weak Areas |
|---------|-----|-------|-------------|-----------|------------|
| **BPCL** | ₹20.11L | Tech + HR | ⬜ | ⬜ | |
| **EIL** | Standard | Tech + HR | ⬜ | ⬜ | |
| **NHPC** | Competitive | Written + Interview | ⬜ | ⬜ | |
| **L&T** | ₹10-12L | Tech x2 + HR | ⬜ | ⬜ | |
| **AECOM** | ₹22-40L | Case + Technical | ⬜ | ⬜ | |
| **Barclays** | ₹17-25.6L | Tech + HR | ⬜ | ⬜ | |
| **Abacus.AI** | ₹60L | Tech + HR | ⬜ | ⬜ | |
| **Accenture** | ₹14-20L | OA + Tech + HR | ⬜ | ⬜ | |
| **BCG** | ₹23.5L | Case + Fit | ⬜ | ⬜ | |
| **Bajaj Auto** | ₹20.74L | Tech + HR | ⬜ | ⬜ | |
| **BNY Mellon** | ₹26.64L | Tech + HR | ⬜ | ⬜ | |
| **Cadence** | ₹22-24.5L | Tech + HR | ⬜ | ⬜ | |
| **Tata Projects** | ₹7-12L | Tech + HR | ⬜ | ⬜ | |
| **Battery Smart** | ₹22L | OA + Tech + HR | ⬜ | ⬜ | |

### Skill Matrix by Company Type

| Skill | PSU | Core Design | Analytics | Tech |
|-------|-----|-------------|-----------|------|
| Civil Fundamentals | 🔴 Critical | 🔴 Critical | 🟡 Nice | ⚪ N/A |
| IS Codes | 🔴 Critical | 🔴 Critical | ⚪ N/A | ⚪ N/A |
| Python | 🟡 Nice | 🟡 Nice | 🔴 Critical | 🔴 Critical |
| SQL | ⚪ N/A | ⚪ N/A | 🔴 Critical | 🟡 Nice |
| DSA/Coding | ⚪ N/A | ⚪ N/A | 🟡 Nice | 🔴 Critical |
| HR/Behavioral | 🔴 Critical | 🔴 Critical | 🔴 Critical | 🔴 Critical |
| Aptitude | 🟡 Nice | 🟡 Nice | 🔴 Critical | 🟡 Nice |
| GATE Knowledge | 🔴 Critical | 🟡 Nice | ⚪ N/A | ⚪ N/A |
| OpenFOAM/CFD | 🟡 Nice | 🔴 Critical | ⚪ N/A | ⚪ N/A |

---

## ⚡ Daily Checklist

### 🌅 Morning Routine (06:00–07:30)
- [ ] Wake up by 06:00
- [ ] Aptitude speed drill — 20 problems in 60 min
- [ ] Flashcard recall — 30 cards, target 90%+
- [ ] Review yesterday's gaps

### 🏗️ Core Block (08:00–12:00)
- [ ] Deep-dive 1 core topic (see weekly plan)
- [ ] Solve 5 numericals from today's topic
- [ ] Write 3 key derivations from memory
- [ ] Coding/SQL session — 1 script or 2 problems

### 🌊 HWRE Block (13:00–14:30)
- [ ] HWRE/CFD topic study
- [ ] OpenFOAM case review (if applicable)

### 🎤 Interview Block (14:45–16:00)
- [ ] Prepare 2 STAR stories (new or revised)
- [ ] Practice 1 mock interview question aloud
- [ ] Review 1 company profile

### 📊 Evening Block (16:00–17:30)
- [ ] Data Interpretation or GATE practice
- [ ] Daily review — update this tracker
- [ ] Note 3 things learned today

### 🌙 Night (21:00–22:00)
- [ ] Light reading — company intel or interview experience
- [ ] Prepare tomorrow's study plan

---

## 📚 Topic Quick-Links

### 🏗️ Core Civil Engineering

| Topic | Quick Link | Priority | Key Formula/Concept |
|-------|-----------|----------|---------------------|
| Hydraulics | [`civil/hydraulics/hydraulics.md`](../civil/hydraulics/hydraulics.md) | P0 | Bernoulli, Continuity, Momentum |
| Turbulence Modeling | [`civil/hydraulics/turbulence-modeling.md`](../civil/hydraulics/turbulence-modeling.md) | P0 | k-ε, k-ω SST, y+ criteria |
| Open Channel Flow | [`civil/open_channel_flow/open-channel-flow.md`](../civil/open_channel_flow/open-channel-flow.md) | P0 | GVF, RVF, Hydraulic Jump |
| Hydrology | [`civil/hydrology/hydrology.md`](../civil/hydrology/hydrology.md) | P0 | Unit Hydrograph, Flood Routing |
| Sediment Transport | [`civil/hydrology/sediment-transport.md`](../civil/hydrology/sediment-transport.md) | P0 | Shields, Meyer-Peter Müller |
| Structures | [`civil/structures/structures.md`](../civil/structures/structures.md) | P1 | SOM, RCC, IS 456 |
| Geotechnical | [`civil/geotechnical/geotechnical.md`](../civil/geotechnical/geotechnical.md) | P1 | Bearing Capacity, Consolidation |
| Foundations | [`civil/fundamentals/civil-engineering-foundations.md`](../civil/fundamentals/civil-engineering-foundations.md) | P1 | Fluid Mechanics, SOM Basics |
| **Environmental Engg** | [`civil/environmental/environmental-engineering.md`](../civil/environmental/environmental-engineering.md) | P1 | BOD, COD, Streeter-Phelps, EIA |
| **Geoinformatics** | [`civil/geoinformatics/geoinformatics.md`](../civil/geoinformatics/geoinformatics.md) | P1 | GIS, RS, GNSS, NDVI, LiDAR |
| **Infrastructure Engg & Mgmt** | [`civil/infrastructure/infrastructure-engineering-management.md`](../civil/infrastructure/infrastructure-engineering-management.md) | P1 | CPM, PERT, NPV, PPP, BOQ |
| **Transportation Engg** | [`civil/transportation/transportation-engineering.md`](../civil/transportation/transportation-engineering.md) | P1 | SSD, Superelevation, CBR, Webster |
| Water Resources | [`civil/water_resources/water-resources-engineering.md`](../civil/water_resources/water-resources-engineering.md) | P0 | Reservoir, Canal Design |

### 💧 HWRE

| Topic | Quick Link | Priority | Key Formula/Concept |
|-------|-----------|----------|---------------------|
| Irrigation | [`hwre/irrigation/irrigation-engineering.md`](../hwre/irrigation/irrigation-engineering.md) | P1 | Duty, Delta, CWR |
| Wastewater | [`hwre/wastewater/wastewater-engineering.md`](../hwre/wastewater/wastewater-engineering.md) | P1 | BOD, COD, Treatment Train |
| Water Supply | [`hwre/water_supply/water-supply.md`](../hwre/water_supply/water-supply.md) | P1 | Distribution, Treatment |
| Groundwater | [`hwre/water_supply/groundwater.md`](../hwre/water_supply/groundwater.md) | P1 | Darcy, Theis, Well Hydraulics |
| Flood Control | [`hwre/flood_control/flood-control.md`](../hwre/flood_control/flood-control.md) | P1 | Flood Routing, Drainage |
| HWRE Exam Notes | [`hwre/exam_notes/hwre-exam-notes.md`](../hwre/exam_notes/hwre-exam-notes.md) | P0 | Consolidated Cheat Sheet |

### 🧮 Aptitude & Reasoning

| Topic | Quick Link | Speed Target |
|-------|-----------|-------------|
| Quantitative Basics | [`aptitude/quantitative/aptitude-basics.md`](../aptitude/quantitative/aptitude-basics.md) | Foundation |
| Averages & Mixtures | [`aptitude/quantitative/averages.md`](../aptitude/quantitative/averages.md) | < 1.5 min |
| Percentages | [`aptitude/quantitative/percentages.md`](../aptitude/quantitative/percentages.md) | < 1 min |
| Profit & Loss | [`aptitude/quantitative/profit-loss-discount.md`](../aptitude/quantitative/profit-loss-discount.md) | < 2 min |
| Speed/Time/Distance | [`aptitude/quantitative/speed-time-distance.md`](../aptitude/quantitative/speed-time-distance.md) | < 2 min |
| Time & Work | [`aptitude/quantitative/time-work.md`](../aptitude/quantitative/time-work.md) | < 1.5 min |
| Ratio & Proportion | [`aptitude/quantitative/ratio-proportion.md`](../aptitude/quantitative/ratio-proportion.md) | < 1.5 min |
| Permutations & Comb. | [`aptitude/quantitative/permutations-combinations.md`](../aptitude/quantitative/permutations-combinations.md) | < 2 min |
| Probability | [`aptitude/quantitative/probability.md`](../aptitude/quantitative/probability.md) | < 2 min |
| Problems on Ages | [`aptitude/quantitative/problems-on-ages.md`](../aptitude/quantitative/problems-on-ages.md) | < 1.5 min |
| Problems on Train | [`aptitude/quantitative/problems-on-train.md`](../aptitude/quantitative/problems-on-train.md) | < 2 min |
| Number System | [`aptitude/quantitative/number-system.md`](../aptitude/quantitative/number-system.md) | < 2 min |
| Partnership | [`aptitude/quantitative/partnership.md`](../aptitude/quantitative/partnership.md) | < 2 min |
| Data Interpretation | [`aptitude/quantitative/data-interpretation.md`](../aptitude/quantitative/data-interpretation.md) | < 5 min/set |
| Speed Math Shortcuts | [`aptitude/shortcuts/aptitude-shortcuts.md`](../aptitude/shortcuts/aptitude-shortcuts.md) | Master all |
| Logical Reasoning | [`aptitude/logical_reasoning/reasoning-practice.md`](../aptitude/logical_reasoning/reasoning-practice.md) | < 3 min/q |
| Verbal Ability | [`aptitude/verbal/verbal-ability.md`](../aptitude/verbal/verbal-ability.md) | — |

### 🎤 Behavioral & HR

| Topic | Quick Link | Stories Ready |
|-------|-----------|---------------|
| Behavioral Guide (STAR) | [`behavioral/behavioral-interview-guide.md`](../behavioral/behavioral-interview-guide.md) | ___/30 |
| Self Introduction | [`behavioral/self_intro/self-introduction.md`](../behavioral/self_intro/self-introduction.md) | ___/5 |
| Conflict Resolution | [`behavioral/conflict_resolution/conflict-resolution.md`](../behavioral/conflict_resolution/conflict-resolution.md) | ___/10 |
| Leadership | [`behavioral/leadership/leadership.md`](../behavioral/leadership/leadership.md) | ___/10 |
| Teamwork | [`behavioral/teamwork/teamwork.md`](../behavioral/teamwork/teamwork.md) | ___/10 |
| HR Questions Bank | [`behavioral/hr_questions/hr-questions-bank.md`](../behavioral/hr_questions/hr-questions-bank.md) | ___/50 |

### 🏢 Interview Resources

| Resource | Quick Link |
|----------|-----------|
| Technical Interview Bank | [`interviews/technical/technical-interview-bank.md`](../interviews/technical/technical-interview-bank.md) |
| Project Discussion | [`interviews/technical/project-discussion.md`](../interviews/technical/project-discussion.md) |
| HR Interview Guide | [`interviews/hr/hr-interview-guide.md`](../interviews/hr/hr-interview-guide.md) |
| Mock Questions | [`interviews/mock_questions/mock-interview-questions.md`](../interviews/mock_questions/mock-interview-questions.md) |
| Company Profiles | [`interviews/company_specific/company-profiles.md`](../interviews/company_specific/company-profiles.md) |
| Interview Experiences | [`interviews/company_specific/interview-experiences.md`](../interviews/company_specific/interview-experiences.md) |
| Placement Data & CTCs | [`resources/placement-data.md`](../resources/placement-data.md) |

### 📋 GATE Preparation

| Resource | Quick Link |
|----------|-----------|
| GATE Civil Notes | [`gate/civil/gate-civil-notes.md`](../gate/civil/gate-civil-notes.md) |
| GATE Formulas | [`gate/formulas/gate-civil-formulas.md`](../gate/formulas/gate-civil-formulas.md) |
| GATE Revision | [`gate/revision_notes/gate-civil-revision.md`](../gate/revision_notes/gate-civil-revision.md) |
| GATE Practice | [`gate/practice/gate-civil-practice.md`](../gate/practice/gate-civil-practice.md) |

### 📄 Templates & Resources

| Resource | Quick Link |
|----------|-----------|
| Resume Template | [`templates/resume-template.md`](../templates/resume-template.md) |
| Self-Intro Template | [`templates/self-intro-template.md`](../templates/self-intro-template.md) |
| Interview Answer Template | [`templates/interview-answer-template.md`](../templates/interview-answer-template.md) |
| Study Plan Template | [`templates/study-plan-template.md`](../templates/study-plan-template.md) |
| Book List | [`resources/book-list.md`](../resources/book-list.md) |
| Technical Stack | [`resources/technical-stack.md`](../resources/technical-stack.md) |
| Non-Core Prep | [`resources/non-core-prep.md`](../resources/non-core-prep.md) |
| External Links | [`resources/links.md`](../resources/links.md) |
| GIS Tools | [`resources/gis-tools.md`](../resources/gis-tools.md) |

---

## 🏗️ Phase Tracker

### Phase 0: Bootstrap (Aug 21 – Sep 7) — Priority P0

**Goal:** Repository setup, syllabus mapping, resume audit

| Task | Status | Due | Evidence |
|------|--------|-----|----------|
| Finalize resume (single-page + detailed) | ⬜ | Sep 7 | [`templates/resume-template.md`](../templates/resume-template.md) |
| Map each topic to source and owner | ⬜ | Sep 7 | [`index/master_index.md`](../index/master_index.md) |
| Set up weekly study cadence | ⬜ | Sep 7 | This file — [Study Planner](#-study-planner) |
| Complete skill matrices | ⬜ | Sep 7 | [Interview Prep Matrix](#-interview-prep-matrix) |
| Read all P0 topic files once | ⬜ | Sep 7 | [Progress Dashboard](#-progress-dashboard) |

**Checkpoint:** [ ] Phase 0 Complete — Date: ___________

---

### Phase 1: Core Revision (Sep 8 – Sep 30) — Priority P0

**Goal:** Deep mastery of core civil + HWRE theory

| Week | Topics | Daily Target | Status |
|------|--------|-------------|--------|
| Week 1 (Sep 8–14) | Hydraulics, Turbulence, OCF | 3 numericals/topic/day | ⬜ |
| Week 2 (Sep 15–21) | Hydrology, Sediment, Structures | 3 numericals/topic/day | ⬜ |
| Week 3 (Sep 22–28) | Geotech, Water Resources, HWRE | 3 numericals/topic/day | ⬜ |
| Week 4 (Sep 29–30) | Revision + Formula Sheets | Full recall test | ⬜ |

**KPIs:**
- [ ] Core concept recall: 90%+ active recall
- [ ] Numerical speed: 15–20 minutes per problem
- [ ] Formula sheets completed for all P0 topics
- [ ] 50+ numericals solved per topic

**Checkpoint:** [ ] Phase 1 Complete — Date: ___________

---

### Phase 2: Mock Interviews & Coding (Oct 1 – Oct 20) — Priority P0

**Goal:** Interview readiness + coding fluency

| Week | Focus | Target | Status |
|------|-------|--------|--------|
| Week 1 (Oct 1–7) | Mock interviews 2x/week, Python scripts 3/week | 2 mocks, 3 scripts | ⬜ |
| Week 2 (Oct 8–14) | Behavioral STAR bank, SQL drills | 10 STAR stories, 10 SQL problems | ⬜ |
| Week 3 (Oct 15–20) | Design-code numericals, IS code checks | 5 code checks, 3 mocks | ⬜ |

**KPIs:**
- [ ] Coding fluency: 3–5 scripts/week
- [ ] Mock readiness: 8+ mocks completed
- [ ] STAR bank: 30 stories ready
- [ ] SQL: 20+ problems solved

**Checkpoint:** [ ] Phase 2 Complete — Date: ___________

---

### Phase 3: Company-Wise Prep (Oct 21 – Nov 10) — Priority P1

**Goal:** Targeted prep for specific companies

| Company | Profile | Tech Prep | HR Prep | Mock Done | Status |
|---------|---------|-----------|---------|-----------|--------|
| BPCL | PSU | ⬜ | ⬜ | ⬜ | ⬜ |
| EIL | PSU | ⬜ | ⬜ | ⬜ | ⬜ |
| L&T | Core | ⬜ | ⬜ | ⬜ | ⬜ |
| AECOM | Consulting | ⬜ | ⬜ | ⬜ | ⬜ |
| Barclays | Analytics | ⬜ | ⬜ | ⬜ | ⬜ |
| Abacus.AI | Tech | ⬜ | ⬜ | ⬜ | ⬜ |

**KPIs:**
- [ ] Company profiles completed for 6+ targets
- [ ] Technical question banks per company
- [ ] Shortlist strategy finalized

**Checkpoint:** [ ] Phase 3 Complete — Date: ___________

---

### Phase 4: Final Revision (Nov 11 – Dec 1) — Priority P0

**Goal:** Rapid recall, gap filling, final readiness

| Task | Target | Status |
|------|--------|--------|
| One-page cheat-sheets per topic | 10 sheets | ⬜ |
| Daily aptitude drill | 20–30 min/day | ⬜ |
| Daily SQL/Python | 20 min/day | ⬜ |
| Final round mocks (tech + HR + case) | 5+ mocks | ⬜ |
| Flashcard deck review | 90%+ recall | ⬜ |

**Checkpoint:** [ ] Phase 4 Complete — Date: ___________

---

### Phase 5: Live Interviews & Postmortems (Dec 2026) — Priority P0

**Goal:** Execute interviews, log, and iterate

| Task | Target | Status |
|------|--------|--------|
| Log each interview within 48 hours | 100% compliance | ⬜ |
| Postmortem after every interview | Every interview | ⬜ |
| Track offers and deadlines | Shared spreadsheet | ⬜ |
| Referral notes | Updated | ⬜ |

**Checkpoint:** [ ] Phase 5 Complete — Date: ___________

---

## 📝 Mock Interview Tracker

| # | Date | Type | Company | Interviewer | Score | Gaps Identified | Follow-up |
|---|------|------|---------|-------------|-------|-----------------|-----------|
| 1 | | ☐ Tech ☐ HR ☐ Case | | | /10 | | |
| 2 | | ☐ Tech ☐ HR ☐ Case | | | /10 | | |
| 3 | | ☐ Tech ☐ HR ☐ Case | | | /10 | | |
| 4 | | ☐ Tech ☐ HR ☐ Case | | | /10 | | |
| 5 | | ☐ Tech ☐ HR ☐ Case | | | /10 | | |
| 6 | | ☐ Tech ☐ HR ☐ Case | | | /10 | | |
| 7 | | ☐ Tech ☐ HR ☐ Case | | | /10 | | |
| 8 | | ☐ Tech ☐ HR ☐ Case | | | /10 | | |
| 9 | | ☐ Tech ☐ HR ☐ Case | | | /10 | | |
| 10 | | ☐ Tech ☐ HR ☐ Case | | | /10 | | |

---

## 📊 Weekly Review Template

### Week of: ___________

| Metric | Target | Actual | Gap |
|--------|--------|--------|-----|
| Study hours | 50+ hrs | ___ hrs | |
| Numericals solved | 50+ | ___ | |
| STAR stories added | 5+ | ___ | |
| Mock interviews | 2+ | ___ | |
| Coding scripts | 3+ | ___ | |
| Flashcard recall | 90%+ | ___% | |

**Top 3 wins this week:**
1. 
2. 
3. 

**Top 3 gaps to address:**
1. 
2. 
3. 

**Next week priority:**
1. 
2. 
3. 

---

## 🛡️ Fable Protocol

### Stage Map (Output First)

```
STAGE MAP:
1. [ANALYZE]     — Understand requirements, identify files, assess impact
2. [PLAN]        — Design approach, list changes, identify risks
3. [IMPLEMENT]   — Write code changes
4. [VERIFY]      — Run terminal verification (tests, linting, build)
5. [REVIEW]      — Self-review against requirements
6. [COMPLETE]    — Final confirmation + double-check report
```

### Failable Checks (At Each Transition)

| Transition | Check |
|------------|-------|
| ANALYZE → PLAN | All relevant files read? Requirements understood? |
| PLAN → IMPLEMENT | All steps ordered? Risks identified? |
| IMPLEMENT → VERIFY | All planned changes applied? No skipped files? |
| VERIFY → REVIEW | All verification commands passed? No failures? |
| REVIEW → COMPLETE | All requirements met? Edge cases handled? |

### Verification Commands (Run After All Code Changes)

```bash
<test_command>    # e.g., npm test, pytest, cargo test
<lint_command>    # e.g., npm run lint, ruff check
<build_command>   # e.g., npm run build, cargo build
```

Adapt these to your project's toolchain. You MUST execute them via execute_command.

### Double-Check Report (Required Before Completion)

Output a 5-pass report:
- **Pass 1: Code Correctness** — syntax, types, edge cases, error handling
- **Pass 2: Style & Convention** — linting, naming, comments, dead code
- **Pass 3: Integration** — existing tests, API contracts, compatibility
- **Pass 4: Documentation** — API docs, README, CHANGELOG
- **Pass 5: Security** — secrets, input validation, injection prevention

### Output Format

```
═══════════════════════════════════════
STAGE: [number] - [name]
═══════════════════════════════════════
[Stage output]
───────────────────────────────────────
CHECK: [description]
STATUS: [PASS/FAIL]
───────────────────────────────────────
```

### Guardrails

- **Pre-flight**: Verify files exist before editing, check dependencies
- **In-flight**: Incremental verification after each file write, state tracking
- **Post-flight**: Full test suite, linting, build, cleanup check

---

## 🎯 Key Resources

| Resource | Link |
|----------|------|
| Master Index | [`index/master_index.md`](../index/master_index.md) |
| Topic Map | [`index/topic_map.md`](../index/topic_map.md) |
| File Inventory | [`index/file_inventory.csv`](../index/file_inventory.csv) |
| Source Map | [`index/source_map.csv`](../index/source_map.csv) |
| Placement Roadmap | [`../placement-roadmap.md`](../placement-roadmap.md) |
| Setup Guide | [`../SETUP.md`](../SETUP.md) |
| Contributing | [`../CONTRIBUTING.md`](../CONTRIBUTING.md) |
| Changelog | [`../CHANGELOG.md`](../CHANGELOG.md) |
| Validate Script | [`../scripts/validate_index.py`](../scripts/validate_index.py) |

---

## 🏆 Milestone Rubric

| Metric | Threshold | Evidence | Status |
|--------|-----------|----------|--------|
| Core concept recall | 90%+ active recall | Closed-book oral tests | ⬜ |
| Numerical speed | 15–20 min/problem | Timed worksheets | ⬜ |
| Coding fluency | 3–5 scripts/week | Git commits + notebooks | ⬜ |
| Mock readiness | 8+ mocks/company track | Mock tracker above | ⬜ |
| Interview depth | 2-layer answers min | Concept + application + caveat | ⬜ |
| STAR stories | 30+ ready | Behavioral guide | ⬜ |
| Aptitude speed | < 2 min/question | Timed drills | ⬜ |
| Flashcard recall | 90%+ | Daily recall sessions | ⬜ |

---

> **Last Updated:** 2026-09-03
> **Maintained by:** DKS IITK Civil/HWRE Placement 2026
> **Version:** 3.0 — One-Stop Placement Prep Command Center (all 7 core subjects covered)
