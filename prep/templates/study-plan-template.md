# Study Plan & Timeline

> Based on Civil_Placement_IITK roadmap for Dec 2026 placements

## Overview

| Phase | Timeline | Focus | Deliverable | Priority |
|-------|----------|-------|-------------|----------|
| **Phase 0** | Aug 21–Sep 7 | Repo bootstrap, syllabus map, resume/CV audit, self onboarding | `/resumes` templates, folder taxonomy, issue labels | P0 |
| **Phase 1** | Sep 8–Sep 30 | Core revision: fluid mechanics, turbulence, hydraulics, hydrology, SOM, geotech | Topic notes in `/core`, formula sheets, derivation logs | P0 |
| **Phase 2** | Oct 1–Oct 20 | Mock interviews, viva-style grilling, design-code numericals, coding drills | `/mock-interviews`, answer bank, error log | P0 |
| **Phase 3** | Oct 21–Nov 10 | Company-wise prep: PSUs, core design/consulting, analytics, shortlists | PRs in `/company-profiles`, role matrices | P1 |
| **Phase 4** | Nov 11–Dec 1 | Final revision: rapid recall, GD/HR, aptitude, case-study reps | Consolidated cheat-sheets, flashcards, mock scores | P0 |
| **Phase 5** | Dec 2026 | Live interview logging, offer tracking, postmortems, referral notes | `/interview-experiences` updated in real time | P0 |

---

## Phase 0: Bootstrap (Aug 21–Sep 7)

### Goals
1. Audit existing resume/CV
2. Map remaining syllabus gaps
3. Set up folder taxonomy
4. Create issue labels for tracking

### Deliverables
- [ ] Resume templates in `prep/templates/resume-template.md`
- [ ] Folder taxonomy established
- [ ] Issue labels: `good-first-issue`, `core`, `analytics`, `PSU`, `interview`
- [ ] Self onboarding document

### Daily Schedule (2-3 hours)
- 1 hour: Resume/CV refinement
- 1 hour: Syllabus mapping against notes
- 1 hour: Folder setup / Git workflow practice

---

## Phase 1: Core Revision (Sep 8–Sep 30)

### Week 1: Fluid Mechanics & Hydraulics
| Topic | Resources | Status |
|-------|-----------|--------|
| Bernoulli's equation | IITK HWRE course slides; Munson/White | ⬜ |
| Continuity & momentum | Munson/White; derivations in class notes | ⬜ |
| Viscous flow | White; class notes | ⬜ |
| Pipe friction | Moody diagram, Colebrook equation | ⬜ |
| Open channel flow | Subramanya; class notes | ⬜ |

### Week 2: Turbulence & CFD
| Topic | Resources | Status |
|-------|-----------|--------|
| RANS closures | Pope, *Turbulent Flows*; OpenFOAM docs | ⬜ |
| Wall functions | OpenFOAM guide; y+ post-processing notes | ⬜ |
| LES vs DNS | Course notes | ⬜ |
| OpenFOAM basics | [CFD & Numerical Modeling](README.md#cfd--numerical-modeling) | ⬜ |
| Mesh generation | blockMesh, snappyHexMesh | ⬜ |

### Week 3: Hydrology & Geotech
| Topic | Resources | Status |
|-------|-----------|--------|
| Unit hydrograph | Subramanya, *Engg. Hydrology* | ⬜ |
| Rainfall-runoff | IITK hydrology course notes | ⬜ |
| Groundwater flow | Darcy, Theis equation | ⬜ |
| Soil mechanics | Basic geotech text + IITK notes | ⬜ |
| Bearing capacity | Terzaghi, Meyerhof equations | ⬜ |

### Week 4: Structures & Geotech Depth
| Topic | Resources | Status |
|-------|-----------|--------|
| SOM: bending/shear | Timoshenko / class notes | ⬜ |
| Deflection methods | Double integration, conjugate beam | ⬜ |
| RCC design | IS 456; class notes | ⬜ |
| Steel design | IS 800; class notes | ⬜ |
| Slope stability | Bishop's method; IS practice problems | ⬜ |

### Milestone Checkpoint (Sep 30)
- Review formula sheets for completeness
- Validate derivations with reference solutions
- Update formula sheets in `core/gate/formulas/`

---

## Phase 2: Mock Interviews (Oct 1–Oct 20)

### Schedule
- **Daily**: 1 coding/quant problem (30 min) + review (15 min)
- **Every 3 days**: 1 mock technical interview (60 min)
- **Weekly**: 1 viva/session with study group (90 min)

### Practice Areas
| Area | Focus | Resources |
|------|-------|-----------|
| **GATE technical** | Formula recall, derivations | `/core/formula-sheets`, GATE PYQs |
| **PSU technical** | IS code familiarity, numerical problems | Class notes, IS handbooks |
| **Design problems** | Load calculations, code checks | Textbooks, previous project work |
| **Coding drills** | Python, SQL, DSA basics | HackerRank, LeetCode, GFG |

### Output Tracking
- Log every mock interview with timestamp
- Record mistakes and corrected methods
- Maintain error log per subject area

---

## Phase 3: Company-Specific Prep (Oct 21–Nov 10)

### PSU Track (Oct 21–Nov 3)
- **Target companies**: BPCL, EIL, NHPC, NTPC, WAPCOS
- **Focus areas**: GATE fundamentals, IS codes, project defense
- **Deliverable**: `prep/company-profiles/company-profiles.md` (PSU section)

### Core Design/Consulting (Nov 4–Nov 10)
- **Target companies**: L&T, AECOM, Tata Projects
- **Focus areas**: Structural design, site logic, construction methods
- **Deliverable**: `prep/company-profiles/company-profiles.md` (Core Design section)

### Analytics/Quant Track (Oct 21–Nov 10)
- **Target companies**: Abacus.AI, Accenture, Barclays, Merilytics
- **Focus areas**: Python, SQL, stats, ML fundamentals
- **Deliverable**: `non-core/analytics/non-core-prep.md` (Analytics section)

---

## Phase 4: Final Revision (Nov 11–Dec 1)

### Rapid Recall Schedule
| Subject | Days/Week | Minutes/Session | Tools |
|---------|-----------|-----------------|-------|
| Fluid Mechanics | 3 | 20 | Formula cards |
| Geotechnical | 3 | 20 | Formula cards |
| Structures | 2 | 20 | Formula cards |
| Environment | 2 | 15 | Formula cards |
| Transportation | 2 | 15 | Formula cards |
| Quant/Analytics | 4 | 30 | Coding platforms |

### GD/HR Preparation
- **Topics**: Current affairs, engineering ethics, sustainability
- **Practice frequency**: Daily 15-min GD drill with study group
- **Resources**: Case study decks, current events summaries

### Case Study Practice
- [Data-Science-Analytical-Handbook](https://moshesham.github.io/Data-Science-Analytical-Handbook/exercises/)
- Simulate timed solve → explain → review loop
- Focus on business framing and communication

### Weekly Full-Length Mocks
- Week 1 (Nov 11): Full mock test (3 hours) + analysis
- Week 2 (Nov 18): GD/PI mock + feedback
- Week 3 (Nov 25): Final comprehensive review

---

## Phase 5: Interview Season (Dec 2026)

### Real-Time Tracking
- Log each interview within 48 hours:
  - Company, role, location, date
  - Rounds: Resume, online test, technical, HR, GD
  - Technical questions asked + follow-up depth
  - HR questions asked
  - Postmortem: 3 weak areas + 3 improvement actions

### Post-Interview Workflow
1. Update `prep/company-profiles/interview-experiences.md` immediately
2. Share learnings with study group
3. Update company-specific notes
4. Schedule feedback session with study group

---

## References

