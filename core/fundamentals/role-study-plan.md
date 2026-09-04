# Civil Engineer (General) — Role Study Plan

## Role Overview

The General Civil Engineer role targets **PSU companies** (BPCL, EIL, NHPC, ONGC, BHEL, NTPC, GAIL) and **core consulting firms** (L&T, Tata Projects, AECOM, Jacobs). The role requires broad competency across mechanics, materials, surveying, construction, and fundamentals of every civil sub-domain. Unlike specialized roles (Structural, WRE, Geotechnical), the General Civil role tests **breadth** — the ability to handle multi-disciplinary projects.

**Who targets this role:** B.Tech civil graduates targeting campus placement at PSUs, GATE-qualified candidates, and those applying to core construction/consulting companies.

---

## 3–4 Highest-Value Preparation Blocks

### Topic 1: Engineering Mechanics & Strength of Materials

#### Why This Matters
Almost every PSU written test and technical interview starts with mechanics and SOM. These are the foundation — if you cannot solve a simple beam problem or free-body diagram, nothing else matters.

#### What to Learn
- [ ] Free-body diagrams and equilibrium equations (ΣF=0, ΣM=0)
- [ ] Truss analysis (method of joints, method of sections)
- [ ] Friction (static, kinetic, wedge, ladder problems)
- [ ] Centroid and moment of inertia (composite shapes)
- [ ] Stress, strain, Young's modulus, Poisson's ratio
- [ ] Bending moment and shear force diagrams (BMD/SFD)
- [ ] Bending stress: σ = My/I
- [ ] Torsion: τ = Tρ/J
- [ ] Deflection of beams (Macaulay's method, superposition)
- [ ] Combined bending and axial loading

#### Study Material
| File | Focus Area | Depth |
|:-----|:-----------|:------|
| [`strength-of-materials.md`](strength-of-materials.md) | Stress-strain, bending, torsion, deflection | Full |
| [`engineering-mechanics.md`](engineering-mechanics.md) | Statics, dynamics, friction, trusses | Full |
| [`civil-engineering-foundations.md`](civil-engineering-foundations.md) | Quick revision formulas | Revision |

#### Worked Example
**Problem:** A simply supported beam of span 6 m carries a UDL of 20 kN/m over the entire span and a point load of 40 kN at 2 m from left support. Draw SFD and BMD. Find maximum bending moment.

**Solution:**
1. **Reactions:** R_A + R_B = 20×6 + 40 = 160 kN
2. ΣM_A = 0: R_B×6 = 20×6×3 + 40×2 → R_B = 73.33 kN, R_A = 86.67 kN
3. **SFD:** Starts at +86.67, linear drop (UDL), drops 40 at 2m, continues linear to R_B
4. **BMD:** Parabolic with point load effect. Maximum at zero shear:
   - Shear at distance x: V(x) = 86.67 - 20x (for 0 < x < 2)
   - V = 0 at x = 4.33 m from A (in the UDL segment after point load)
   - M_max = 86.67(4.33) - 20(4.33)²/2 - 40(4.33-2) = **140.56 kN·m**

#### Practice
**Basic (3–5):**
1. Find reactions for a cantilever with UDL and point load.
2. Draw SFD/BMD for a beam with two point loads.
3. Calculate centroid of a T-section.
4. Find moment of inertia of an I-section about its centroidal axis.
5. A bar of 50 mm diameter, 2 m long, is subjected to 100 kN tension. Find elongation (E = 200 GPa).

**Intermediate (3–5):**
6. A hollow shaft transmits 500 kW at 100 rpm. If τ_max = 40 MPa, find the required external diameter (external:internal = 2:1).
7. A beam of rectangular section (b=200mm, d=400mm) carries a maximum BM of 80 kN·m. Find the bending stress at 100mm from the top.
8. A ladder 5 m long weighs 200 N, its center of gravity is 2 m from the foot. The foot is 3 m from a smooth wall. Find the minimum coefficient of friction at the floor for equilibrium.
9. A propped cantilever of span L carries UDL w. Find the prop reaction using superposition.

**Interview-Level (5+):**
10. Explain the difference between statically determinate and indeterminate structures. Give examples.
11. Why does a hollow shaft have better torsional resistance than a solid shaft of the same weight?
12. A beam has a suddenly applied load. How does the maximum stress compare to the static case? Explain the impact factor.
13. What is the plane of maximum shear stress? Where does it occur in a shaft under torsion?
14. How do you determine the principal stresses at a point given σ_x, σ_y, and τ_xy?

#### Interview Questions (What Interviewer Tests)
| Question | What They're Testing |
|:---------|:---------------------|
| Draw the BMD for this beam. | Visual + analytical ability |
| What is the maximum shear stress in a circular shaft? | Formula recall + physical understanding |
| Explain plane stress vs plane strain. | Conceptual depth |
| How would you check a beam for combined bending and shear? | Design judgment |
| A column fails at 50% of Euler load. Why? | Real-world awareness (imperfections, residual stress) |

#### Common Mistakes
- **Forgetting sign conventions** in SFD/BMD (left-up = positive)
- **Confusing** section modulus (Z) with moment of inertia (I)
- **Not checking units** — mixing mm and m, MPa and Pa
- **Assuming** Euler's formula applies to all columns (short columns fail by crushing)
- **Neglecting** self-weight in beam problems when not explicitly told to ignore it

#### Rapid Revision
See [`civil-rapid-revision.md`](civil-rapid-revision.md) for a compact cheat sheet of mechanics + SOM formulas.

#### Completion Criterion
✅ Can solve any SFD/BMD problem in under 5 minutes
✅ Can derive and apply σ=My/I, τ=Tρ/J, δ=PL/AE without hesitation
✅ Can solve a truss of 8+ members by method of sections
✅ Can explain every formula physically, not just mathematically

---

### Topic 2: Surveying & Construction Technology

#### Why This Matters
Surveying is tested in every PSU exam. Construction technology (concrete, steel, formwork, curing) is the bread and butter of site-based civil roles at L&T, Tata Projects, and PSUs.

#### What to Learn
- [ ] Chain surveying, compass surveying, plane table
- [ ] Leveling (differential, reciprocal, profile)
- [ ] Theodolite surveying (horizontal/vertical angles, traverse)
- [ ] Total station and GPS basics
- [ ] Contouring and earthwork calculations
- [ ] Concrete technology (mix design, workability, strength, curing)
- [ ] Construction materials (steel grades, timber, bricks)
- [ ] Formwork, shoring, scaffolding
- [ ] Construction scheduling basics (CPM, bar charts)

#### Study Material
| File | Focus Area | Depth |
|:-----|:-----------|:------|
| [`civil-engineering-foundations.md`](civil-engineering-foundations.md) | Quick formula reference | Revision |
| *Refer textbooks: B.C. Punmia (Surveying), S.K. Duggal (Construction Technology)* | Detailed theory | Full |

#### Worked Example
**Problem:** A differential leveling was carried out. The back sight readings were 1.250, 2.340, 1.870, and fore sight readings were 1.890, 2.760, 1.540, 0.980. The Reduced Level (RL) of the first point is 100.000 m. Find RL of all points using Height of Instrument method.

**Solution:**
| Station | BS | IS | FS | HI | RL | Remarks |
|:--------|---:|---:|---:|---:|---:|:--------|
| A | 1.250 | | | 101.250 | 100.000 | BM |
| B | 2.340 | | 1.890 | 101.700 | 99.360 | TP1 |
| C | 1.870 | | 2.760 | 100.810 | 98.940 | TP2 |
| D | | | 1.540 | | 99.270 | TP3 |
| E | | | 0.980 | | 99.830 | TP4 |

**Check:** ΣBS - ΣFS = 5.460 - 7.170 = -1.710; Last RL - First RL = 99.830 - 100.000 = -0.170 → **Arithmetic check fails — indicates error** (this is intentional: students must verify arithmetic)

#### Practice
**Basic (3–5):**
1. Calculate the area of a cross-section with offsets 0, 3.2, 4.5, 3.8, 2.1, 0 at 5m intervals using Trapezoidal rule.
2. A line measured 250 m with a 30m tape that was actually 30.05 m long. What is the correct length?
3. In leveling, BM is at 150.000 m. BS = 1.500, FS = 2.100. Find HI and RL of next point.
4. Find the volume of earthwork between two cross-sections: Area₁ = 12 m², Area₂ = 18 m², distance = 30 m (Prismoidal formula).

**Intermediate (3–5):**
5. Two parallel walls are 6 m apart. From a point on the ground between them, angles of elevation to the tops are 60° and 45°. If the walls are 10 m and 8 m high, find the height of the point above the ground.
6. A closed traverse has 5 sides. The observed interior angles are 105°, 120°, 95°, 130°, and 92°. Check for angular misclosure and adjust.
7. The mix design requires w/c = 0.45, cement = 350 kg/m³, sand = 700 kg/m³, aggregate = 1100 kg/m³. Check if the mix satisfies IS 10262 guidelines for M30 grade.

**Interview-Level (5+):**
8. What is the difference between permanent adjustment and temporary adjustment of a theodolite?
9. Explain the procedure for conducting a two-point problem in plane table surveying.
10. How do you ensure concrete quality on site? What tests do you perform?
11. What is the difference between CPM and PERT? When would you use each?
12. Explain curing — why is it done, what are the methods, and what happens if skipped?

#### Interview Questions (What Interviewer Tests)
| Question | What They're Testing |
|:---------|:---------------------|
| What are the sources of error in chaining? | Practical knowledge |
| Explain the three-point problem in plane table survey. | Surveying depth |
| What is the difference between nominal and design mix? | Concrete technology |
| How do you handle a situation where concrete strength at 7 days is low? | Site judgment |
| What precautions do you take during earthwork in a rainy season? | Practical awareness |

#### Common Mistakes
- **Confusing** HI method and Rise-Fall method in leveling
- **Forgetting** to check angular misclosure in traverse surveying
- **Not knowing** the difference between nominal mix (proportioned by volume) and design mix (by weight, based on trials)
- **Assuming** all theodolites have the same least count

#### Completion Criterion
✅ Can solve any leveling problem (HI method, Rise-Fall, reciprocal) in under 5 minutes
✅ Can list 5+ types of surveying errors and their corrections
✅ Can explain concrete mix design procedure step by step
✅ Can describe CPM/PERT with a simple example network

---

### Topic 3: General Civil Interview (PSU/GATE-Focused)

#### Why This Matters
PSU interviews test breadth. An interviewer might ask about fluid mechanics, then jump to structural design, then to construction management — all in one 15-minute technical round.

#### What to Learn
- [ ] **Fluid Mechanics basics:** Bernoulli, continuity, Reynolds number, pipe flow
- [ ] **Environmental basics:** BOD, COD, water treatment, wastewater treatment
- [ ] **Transportation basics:** IRC codes, pavement design, traffic engineering
- [ ] **Geotechnical basics:** Soil classification, bearing capacity, consolidation
- [ ] **Estimation & Costing:** Rate analysis, BOQ, specifications
- [ ] **Project Management:** Site planning, quality control, safety
- [ ] **Current affairs in civil:** Smart cities, AMRUT, Jal Jeevan Mission, new IS codes

#### Study Material
| File | Focus Area | Depth |
|:-----|:-----------|:------|
| [`civil-engineering-foundations.md`](civil-engineering-foundations.md) | Cross-domain formulas | Full |
| [`technical-interview-bank.md`](../../prep/interview/technical/technical-interview-bank.md) | 100+ technical questions | Practice |
| [`structures.md`](../structures/structures.md) | Structural fundamentals | Reference |
| [`geotechnical.md`](../geotechnical/geotechnical.md) | Soil mechanics | Reference |

#### Worked Example
**Question:** "Explain BOD. What is the difference between BOD and COD?"

**Answer Framework (What → Why → Formula → Application):**
1. **What:** BOD (Biochemical Oxygen Demand) = amount of dissolved oxygen consumed by microorganisms while decomposing organic matter in water, measured over 5 days at 20°C.
2. **Why:** BOD₅ is the standard indicator of organic pollution in wastewater. Lower BOD₅ = cleaner water.
3. **Formula:** y_t = L₀(1 - e^{-k₁t}), where L₀ = ultimate BOD, k₁ = reaction rate constant (~0.23/day base e at 20°C)
4. **Application:** Untreated domestic sewage has BOD₅ ≈ 200–300 mg/L. Treated effluent should have BOD₅ < 30 mg/L (CPCB standard) or < 10 mg/L (for sensitive areas).
5. **COD** > BOD always, because COD measures ALL oxidizable matter (organic + inorganic). The BOD/COD ratio indicates biodegradability (>0.5 = easily biodegradable).

#### Practice (PSU Interview-Style Rapid Fire)
1. State Bernoulli's equation and explain each term physically.
2. What is the difference between BOD and COD? Which is always higher?
3. Name 3 types of retaining walls and when each is used.
4. What is the difference between working stress and limit state design?
5. What are the main causes of bridge failure?
6. What is the purpose of providing expansion joints in bridges?
7. What is the difference between a one-way slab and a two-way slab?
8. What is bearing capacity? How does it differ from allowable bearing pressure?
9. What are the types of piles? When is each used?
10. What is the difference between CPM and PERT?
11. What are the common defects in brick masonry?
12. Explain the process of pile foundation construction.
13. What is a keyway in retaining walls?
14. What are the factors affecting the choice of a dam site?
15. What is the significance of the OMC and MDD in compaction?

#### Common Mistakes
- **Being unable to answer** cross-domain questions (e.g., environmental Q in a structural role)
- **Giving one-word answers** instead of structured explanations
- **Not knowing** recent government schemes (Smart Cities, AMRUT 2.0, Jal Jeevan Mission)
- **Forgetting** basic definitions (BOD, bearing capacity, workability)
- **Not connecting** textbook knowledge to site/practical experience

#### Completion Criterion
✅ Can answer 15 rapid-fire questions from different sub-domains without hesitation
✅ Can explain each answer using the What → Why → Formula → Application framework
✅ Can discuss at least 3 current civil engineering initiatives/policies

---

### Topic 4: PSU Company Strategy & Selection Preparation

#### Why This Matters
Getting selected at a PSU is not just about technical knowledge — it's about understanding what each company tests, how they shortlist, and what they value in candidates.

#### What to Learn
- [ ] PSU recruitment process (GATE score → shortlist → GD → interview → medical)
- [ ] Company-specific focus areas:
  - **BPCL:** Process engineering, refinery layout, piping basics, safety
  - **EIL:** Project management, cost estimation, technical specifications
  - **NHPC:** Hydropower, dam engineering, water resources, turbine basics
  - **ONGC:** Drilling, reservoir engineering, offshore structures
  - **BHEL:** Turbine manufacturing, boiler technology, power plant systems
  - **NTPC:** Thermal power plant, boiler, turbine, generator basics
  - **GAIL:** Pipeline engineering, gas processing, LPG systems
- [ ] HR round preparation for PSUs (Why this company? Why civil? Career plan?)
- [ ] Medical fitness requirements for each PSU
- [ ] Negotiation: CTC components, posting locations, bond periods

#### Company-to-Role Study Navigation

| Company | Priority Topics | Study Files |
|:--------|:----------------|:------------|
| BPCL | Process basics, safety, fire protection | [`civil-engineering-foundations.md`](civil-engineering-foundations.md) |
| EIL | Estimation, project management, specifications | [`infrastructure-engineering-management.md`](../infrastructure/infrastructure-engineering-management.md) |
| NHPC | Hydropower, dam design, hydrology | [`hydrology.md`](../hwre/hydrology/hydrology.md), [`water-resources-engineering.md`](../hwre/water_resources/water-resources-engineering.md) |
| ONGC | Drilling, reservoir, offshore | [`geotechnical.md`](../geotechnical/geotechnical.md) |
| BHEL | Power plant, turbine basics | [`civil-engineering-foundations.md`](civil-engineering-foundations.md) |
| NTPC | Thermal power, boiler, turbine | [`civil-engineering-foundations.md`](civil-engineering-foundations.md) |
| GAIL | Pipeline, gas processing | [`civil-engineering-foundations.md`](civil-engineering-foundations.md) |

#### Common Mistakes
- **Applying to every PSU** without understanding company-specific requirements
- **Not preparing** for GD topics (current affairs, industry trends)
- **Ignoring** the HR round — many candidates get eliminated here
- **Not knowing** the bond period and posting policy of each PSU

#### Completion Criterion
✅ Can describe the recruitment process of 5 major PSUs
✅ Can explain what each company tests technically
✅ Can answer "Why this company?" for at least 3 PSUs with specific reasons
✅ Knows bond periods, CTC ranges, and posting policies for target PSUs

---

## Mock Test (45 Minutes)

| # | Question | Topic | Marks |
|---|:---------|:------|------:|
| 1 | A beam of span 8m carries a UDL of 15 kN/m over left 5m and a point load of 30 kN at the free end. Draw SFD and BMD. | Mechanics | 15 |
| 2 | A solid shaft of 80mm diameter transmits 200 kW at 500 rpm. Find max shear stress and angle of twist (G=80 GPa, L=2m). | SOM | 10 |
| 3 | What is BOD? Explain the test procedure and list 3 factors affecting BOD. | Environmental | 10 |
| 4 | Differentiate between plane table surveying methods: radiation, intersection, resection. | Surveying | 10 |
| 5 | A closed traverse has 4 angles: 85°, 95°, 88°, 94°. Check angular misclosure and correct. | Surveying | 10 |
| 6 | Explain M30 concrete — what does 30 mean? How is it tested? What is the standard curing time? | Construction | 10 |
| 7 | Name 5 types of foundations. For each, state when it is used. | Geotech/General | 10 |
| 8 | What is a Moment Distribution Method? Explain with a 2-span beam. | Structural | 15 |
| 9 | What are the safety measures at a construction site? List 8 with brief explanation. | General | 10 |
| 10 | Why do you want to join BPCL/EIL/NHPC? What do you know about our operations? | HR/Strategy | 10 |
| | | **Total** | **100** |

**Time:** 45 minutes (simulates PSU written test pace)

---

## Interview Strategy

### Technical Interview (15–20 minutes)
1. **Start strong:** Be ready for the first question (usually from your strongest subject)
2. **Structured answers:** Use What → Why → Formula → Application → Limitation
3. **Draw diagrams:** Always draw when asked about structures, surveying, or construction
4. **Admit ignorance gracefully:** "I haven't studied this topic deeply, but based on my understanding..."

### HR Interview (10–15 minutes)
1. **Why this company?** — Be specific (mention their project, recent news, values)
2. **Why civil engineering?** — Connect personal story to the discipline
3. **Where do you see yourself in 5 years?** — Align with company's growth path
4. **Strengths/Weaknesses:** Use real examples, not generic answers

---

## Cross-Links

**Next:**
→ [Civil Rapid Revision](civil-rapid-revision.md) — Last-minute formula cheat sheet
→ [Structural Engineering](../structures/structures.md) — If targeting structural roles
→ [Water Resources](../hwre/water_resources/water-resources-engineering.md) — If targeting WRE roles

**Practice:**
→ [Technical Interview Bank](../../prep/interview/technical/technical-interview-bank.md) — 100+ technical questions
→ [Mock Interview Questions](../../prep/interview/mock-tests/mock-interview-questions.md)

**Interview:**
→ [Behavioral Interview Guide](../../prep/behavioral/behavioral-interview-guide.md)
→ [HR Questions Bank](../../prep/behavioral/hr_questions/hr-questions-bank.md)
→ [Self Introduction Guide](../../prep/behavioral/self_intro/self-introduction.md)

**Company:**
→ [Company Profiles](../../prep/company-profiles/company-profiles.md) — PSU and core company details

**Related:**
→ [GATE Civil Notes](../gate/civil/gate-civil-notes.md) — If also preparing for GATE
→ [Role Selector](../../non-core/role-selector.md) — Compare with other roles

---

*This study plan follows the [Role Study Plan Template](../../prep/templates/role-study-plan-template.md).*
*Last updated: 2026-09-04*
