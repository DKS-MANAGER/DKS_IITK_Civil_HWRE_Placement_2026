# Design Engineer (RCC/Steel) — Role Study Plan

> 4-week preparation roadmap for structural design engineering placements (L&T, Tata Projects, AECOM, Thornton Tomasetti, AEC firms, PSUs).
> **Canonical Study:** [`rcc-design.md`](rcc-design.md) · [`../steel/steel-design.md`](../steel/steel-design.md) · [`../structural-analysis/structural-analysis.md`](../structural-analysis/structural-analysis.md)

---

## Role Overview

**What design engineers do:** Design reinforced concrete and steel structures — beams, slabs, columns, footings, connections — ensuring safety, serviceability, and economy per IS codes.

**Day-to-day:** Structural modeling (STAAD/ETABS), member design per IS 456/IS 800, detailing and bar bending schedules, coordination with architects and contractors, design review and optimization.

**Civil/M.Tech advantage:** Direct domain match. Strong foundation in analysis, RCC, and steel design. Thesis work in structures is a major differentiator.

**Target companies:** L&T, Tata Projects, AECOM, Thornton Tomasetti, CBRE, AEC firms, NBCC, CPWD, state PWD, consulting firms with structural practice.

---

## Topic 1: Structural Analysis

### Why This Matters
Every design starts with analysis — you must compute the forces before you can design the members.

### What to Learn
- [ ] Determinacy & indeterminacy ($D_s$, $D_k$)
- [ ] Moment distribution (Hardy Cross)
- [ ] Influence lines for beams and frames
- [ ] Slope-deflection method
- [ ] Matrix/stiffness method (software basis)
- [ ] Load combinations (IS 456 Table 18, IS 800)

### Study Material
| Topic | File | Depth |
|:------|:-----|:------|
| Structural Analysis | [structural-analysis.md](../structural-analysis/structural-analysis.md) | Comprehensive |
| Practice | [PRACTICE.md](../structural-analysis/PRACTICE.md) | 15 solved problems |
| Topic Test | [TEST.md](../structural-analysis/TEST.md) | 15 questions |
| Interview | [INTERVIEW.md](../structural-analysis/INTERVIEW.md) | 20+ Q&A |

### Worked Example
> **"Analyze a continuous beam using moment distribution."**
>
> 1. Fixed-end moments for each span
> 2. Distribution factors at each joint
> 3. Carry-over factors
> 4. Iterate until convergence
> 5. Draw BMD and SFD
>
> → Full walkthrough in [structural-analysis.md](../structural-analysis/structural-analysis.md)

### Interview Questions
1. Explain the moment distribution method. — *Tests: analysis fundamentals*
2. What is the difference between stiffness and flexibility methods? — *Tests: method understanding*
3. How do you determine load combinations for a building? — *Tests: IS code knowledge*
4. What are influence lines and how are they used? — *Tests: practical application*

---

## Topic 2: RCC Design (IS 456)

### Why This Matters
RCC is the most tested structural topic in every core civil interview.

### What to Learn
- [ ] Limit state design philosophy
- [ ] Beam design (singly/doubly reinforced)
- [ ] Shear design & stirrups
- [ ] Column design (short/long, tied)
- [ ] Slab design (one-way, two-way)
- [ ] Footing design (isolated, combined)
- [ ] Detailing requirements (cover, laps, curtailment)

### Study Material
| Topic | File | Depth |
|:------|:-----|:------|
| RCC Design | [rcc-design.md](rcc-design.md) | Comprehensive |
| Practice | [PRACTICE.md](PRACTICE.md) | 15 solved problems |
| Topic Test | [TEST.md](TEST.md) | 15 questions |
| Interview | [INTERVIEW.md](INTERVIEW.md) | 20+ Q&A |

### Worked Example
> **"Design a singly reinforced beam for a given moment."**
>
> 1. Given: M_u = 150 kN·m, f_ck = 25 MPa, f_y = 415 MPa
> 2. Check: M_u,lim = 0.138 × f_ck × b × d²
> 3. If M_u > M_u,lim → doubly reinforced
> 4. Calculate A_st from: M_u = 0.87 × f_y × A_st × (d − 0.42x_u)
> 5. Check shear: τ_v = V_u/(b×d), compare with τ_c,max
>
> → Full walkthrough in [rcc-design.md](rcc-design.md)

### Interview Questions
1. Explain limit state design philosophy. — *Tests: design fundamentals*
2. What is the difference between working stress and limit state design? — *Tests: method comparison*
3. How do you design a column for biaxial bending? — *Tests: advanced design*
4. What are the detailing requirements for seismic zones? — *Tests: IS 13920 knowledge*
5. How do you check a beam for shear? — *Tests: shear design*

---

## Topic 3: Steel Design (IS 800)

### Why This Matters
Steel structures are increasingly important for industrial and high-rise construction.

### What to Learn
- [ ] Tension member design
- [ ] Compression member design (buckling)
- [ ] Bolted connections (bearing, friction/HSFG)
- [ ] Welded connections (fillet, butt)
- [ ] Beam design (laterally supported/unsupported)
- [ ] Plate girders & stiffeners

### Study Material
| Topic | File | Depth |
|:------|:-----|:------|
| Steel Design | [steel-design.md](../steel/steel-design.md) | Comprehensive |
| Practice | [PRACTICE.md](../steel/PRACTICE.md) | 15 solved problems |
| Topic Test | [TEST.md](../steel/TEST.md) | 15 questions |
| Interview | [INTERVIEW.md](../steel/INTERVIEW.md) | 20+ Q&A |

### Worked Example
> **"Design a bolted connection."**
>
> 1. Determine design bolt value V_db = least of shear, bearing, tension
> 2. Shear: V_dsb = f_ub(n_n·A_nb + n_s·A_sb)/(√3·γ_mb)
> 3. Bearing: V_dpb = 2.5·k_b·d·t·f_u/γ_mb
> 4. Number of bolts n = P/V_db
> 5. Arrange with pitch ≥ 2.5d, check block shear
>
> → Full walkthrough in [steel-design.md](../steel/steel-design.md)

### Interview Questions
1. What is the difference between bolted and welded connections? — *Tests: connection knowledge*
2. How do you check a compression member for buckling? — *Tests: stability knowledge*
3. What is lateral-torsional buckling? — *Tests: advanced steel concepts*
4. Explain the effective length of a column. — *Tests: design fundamentals*

---

## Topic 4: Interview Strategy & Rapid Revision

### Interview Strategy
| Round | Format | Focus |
|:------|:-------|:------|
| OA | Aptitude + technical MCQs | Broad knowledge |
| Technical 1 | Subject questions | Analysis + design depth |
| Technical 2 | Project discussion | Thesis + projects |
| HR | Behavioral + motivation | Why design? Why this company? |

---

## Rapid Revision

### Must-Memorize Formulas
| Formula | Equation | Code |
|:--------|:---------|:-----|
| Flexure (singly reinforced) | M_u = 0.87f_yA_st(d − 0.42x_u) | IS 456 |
| Balanced section | x_u,max/d = 0.48 (Fe415) | IS 456 |
| Shear capacity | V_u = τ_c × b × d | IS 456 |
| Column (short, axial) | P_u = 0.4f_ckA_c + 0.67f_yA_sc | IS 456 |
| Development length | L_d = 0.87f_y·φ/(4τ_bd) | IS 456 |
| Bolt strength (shear) | V_dsb = f_ub·n·A_nb/(√3·γ_mb) | IS 800 |
| Weld strength | P_dw = L_w·t_t·f_u/(√3·γ_mw) | IS 800 |
| Compression member | P_d = A_e·f_cd | IS 800 |
| Load combination (ultimate) | 1.5(DL + LL) | IS 456 Table 18 |

### Key IS Code Values
| Parameter | Value | Code |
|:----------|:------|:-----|
| Partial safety factor (concrete) | γ_m = 1.5 | IS 456 |
| Partial safety factor (steel) | γ_m0 = 1.10, γ_m1 = 1.25 | IS 800 |
| Min cover (beams) | 25 mm | IS 456 |
| Min cover (columns) | 40 mm | IS 456 |
| Min cover (footing) | 75 mm | IS 456 |
| Max steel (% of bD) | 4% (beams), 6% (columns) | IS 456 |
| Min pitch of bolts | 2.5d | IS 800 |
| Max slenderness (compression) | 180 | IS 800 |

### Last-Minute Checklist
- [ ] Reviewed moment distribution method
- [ ] Reviewed beam design (singly reinforced)
- [ ] Reviewed column design (short, tied)
- [ ] Reviewed bolted connection design
- [ ] Reviewed load combinations (IS 456 Table 18)
- [ ] Reviewed development length & detailing rules
- [ ] Prepared 3-minute thesis pitch
- [ ] Researched [company] recent structural projects

---

## Cross-Links

| Resource | Link |
|:---------|:-----|
| RCC Design | [rcc-design.md](rcc-design.md) |
| Steel Design | [steel-design.md](../steel/steel-design.md) |
| Structural Analysis | [structural-analysis.md](../structural-analysis/structural-analysis.md) |
| Structures Companion | [structures.md](../structures/structures.md) |
| Structural Role Plan | [role-study-plan.md](../structures/role-study-plan.md) |
| Technical Interview Bank | [../../prep/interview/technical/technical-interview-bank.md](../../prep/interview/technical/technical-interview-bank.md) |
| Project Discussion | [../../prep/interview/technical/project-discussion.md](../../prep/interview/technical/project-discussion.md) |
| Behavioral Guide | [../../prep/behavioral/behavioral-interview-guide.md](../../prep/behavioral/behavioral-interview-guide.md) |

---

*Based on role-study-plan-template.md. Customized for Design Engineer (RCC/Steel) role.*