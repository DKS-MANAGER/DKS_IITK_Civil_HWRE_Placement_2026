# Structural Engineer — Study Plan

> 4-week preparation roadmap for structural engineering placements (L&T, TATA Projects, AECOM, Thornton Tomasetti, PSUs).

---

## Role Overview

**What structural engineers do:** Analyze and design load-carrying systems — buildings, bridges, industrial structures. Ensure safety, serviceability, and economy.

**Day-to-day:** Structural analysis (FEM), RC/steel design per IS codes, detailing, project coordination, quality control.

**Civil/M.Tech advantage:** Direct domain match. Strong foundation in mechanics, analysis, and design. Thesis work in structures is a major differentiator.

**Target companies:** L&T, TATA Projects, AECOM, Thornton Tomasetti, CBRE, NBCC, CPWD, state PWD, consulting firms with structural practice.

---

## Topic 1: Structural Analysis

### Why This Matters
Foundation of all structural work. Every interview tests analysis fundamentals.

### What to Learn
- [ ] Stiffness matrix method / Direct stiffness method
- [ ] Moment distribution (Hardy Cross)
- [ ] Influence lines for beams and frames
- [ ] Slope-deflection method
- [ ] Matrix analysis concepts
- [ ] Load combinations (IS 456 Table 18, IS 800)

### Study Material
| Topic | File | Depth |
|:------|:-----|:------|
| Structural Analysis | [structural-analysis.md](../structural-analysis/structural-analysis.md) | 3,887 words |
| Structures | [structures.md](structures.md) | 1,989 words |

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
2. What is the difference between stiffness method and flexibility method? — *Tests: method understanding*
3. How do you determine load combinations for a building? — *Tests: IS code knowledge*
4. What are influence lines and how are they used? — *Tests: practical application*
5. How do you check a structure for progressive collapse? — *Tests: advanced knowledge*

---

## Topic 2: RCC Design (IS 456)

### Why This Matters
Most structural engineering roles require RC design proficiency.

### What to Learn
- [ ] Limit state design philosophy
- [ ] Beam design (singly/doubly reinforced)
- [ ] Shear design
- [ ] Column design (short/long, tied/column)
- [ ] Slab design (one-way, two-way)
- [ ] Footing design
- [ ] Detailing requirements

### Study Material
| Topic | File | Depth |
|:------|:-----|:------|
| RCC Design | [rcc-design.md](../rcc/rcc-design.md) | 5,759 words — comprehensive |
| Structures | [structures.md](structures.md) | IS 456 provisions |

### Worked Example
> **"Design a singly reinforced beam for a given moment."**
>
> 1. Given: M_u = 250 kN·m, f_ck = 25 MPa, f_y = 415 MPa
> 2. Check: M_u,lim = 0.138 × f_ck × b × d²
> 3. If M_u > M_u,lim → doubly reinforced
> 4. Calculate A_st from: M_u = 0.87 × f_y × A_st × (d − 0.42x_u)
> 5. Check shear: τ_v = V_u/(b×d), compare with τ_c,max
>
> → Full walkthrough in [rcc-design.md](../rcc/rcc-design.md)

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
- [ ] Bolted connections (bearing, friction)
- [ ] Welded connections
- [ ] Beam design (laterally supported/unsupported)
- [ ] Plate girders

### Study Material
| Topic | File | Depth |
|:------|:-----|:------|
| Steel Design | [steel-design.md](../steel/steel-design.md) | 4,965 words |
| Structures | [structures.md](structures.md) | IS 800 provisions |

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
| HR | Behavioral + motivation | Why structures? Why this company? |

---

## Rapid Revision

### Must-Memorize Formulas
| Formula | Equation | Code |
|:--------|:---------|:-----|
| Flexure (singly reinforced) | M_u = 0.87f_yA_st(d − 0.42x_u) | IS 456 |
| Balanced section | x_u,max/d = 0.48 (Fe415), 0.53 (Fe500) | IS 456 |
| Shear capacity | V_u = τ_c × b × d | IS 456 |
| Column (short, axial) | P_u = 0.4f_ckA_c + 0.67f_yA_sc | IS 456 |
| Euler buckling | P_cr = π²EI/L_e² | Theory |
| Bolt strength (bearing) | V_dsb = d_b × t × f_ub / (√3 × γ_mb) | IS 800 |
| Weld strength | V_dws = l_w × t × f_u / (√3 × γ_mw) | IS 800 |
| Load combination (ultimate) | 1.5(DL + LL) | IS 456 Table 18 |

### Key IS Code Values
| Parameter | Value | Code |
|:----------|:------|:-----|
| Partial safety factor (concrete) | γ_m = 1.5 | IS 456 |
| Partial safety factor (steel) | γ_m0 = 1.10, γ_m1 = 1.25 | IS 800 |
| Modular ratio | m = 280/(3σ_cbc) | IS 456 |
| Min cover (beams) | 25 mm | IS 456 |
| Min cover (columns) | 40 mm | IS 456 |
| Max steel (% of bD) | 4% (columns), 4% (beams) | IS 456 |

### Last-Minute Checklist
- [ ] Reviewed moment distribution method
- [ ] Reviewed beam design (singly reinforced)
- [ ] Reviewed column design (short, tied)
- [ ] Reviewed bolted connection design
- [ ] Reviewed load combinations (IS 456 Table 18)
- [ ] Prepared 3-minute thesis pitch
- [ ] Researched [company] recent structural projects

---

## Cross-Links

| Resource | Link |
|:---------|:-----|
| Structural Analysis | [structural-analysis.md](../structural-analysis/structural-analysis.md) |
| RCC Design | [rcc-design.md](../rcc/rcc-design.md) |
| Steel Design | [steel-design.md](../steel/steel-design.md) |
| Structures | [structures.md](structures.md) |
| Technical Interview Bank | [../../prep/interview/technical/technical-interview-bank.md](../../prep/interview/technical/technical-interview-bank.md) |
| Project Discussion | [../../prep/interview/technical/project-discussion.md](../../prep/interview/technical/project-discussion.md) |
| Behavioral Guide | [../../prep/behavioral/behavioral-interview-guide.md](../../prep/behavioral/behavioral-interview-guide.md) |

---

*Based on role-study-plan-template.md. Customized for Structural Engineer role.*
