# Civil Engineer (General) — Rapid Revision Sheet

> Last-minute cheat sheet for PSU/GATE technical interviews. Covers all sub-domains.

---

## Framework 1: Strength of Materials

### Stress & Strain
| Quantity | Formula | Unit |
|:---------|:--------|:-----|
| Normal stress | σ = P/A | MPa |
| Shear stress | τ = V/A | MPa |
| Strain | ε = δ/L | dimensionless |
| Young's modulus | E = σ/ε | GPa |
| Poisson's ratio | ν = -ε_lat/ε_long | — |
| Shear modulus | G = E/(2(1+ν)) | GPa |
| Bulk modulus | K = E/(3(1-2ν)) | GPa |
| Volumetric strain | ε_v = ε_x + ε_y + ε_z | — |

### Thermal Stress
- Free expansion: δ = αLΔT
- If constrained: σ = EαΔT (compressive if heated, tensile if cooled)

### Bending
| Quantity | Formula |
|:---------|:--------|
| Bending stress | σ = My/I |
| Section modulus | Z = I/y_max |
| Moment of inertia (rect.) | I = bd³/12 |
| Moment of inertia (circle) | I = πd⁴/64 |
| Moment of inertia (I-section) | I = (BD³ - bd³)/12 (subtract hollow) |

### Torsion
| Quantity | Formula |
|:---------|:--------|
| Torsional shear | τ = Tρ/J |
| Polar moment (solid shaft) | J = πd⁴/32 |
| Polar moment (hollow) | J = π(D⁴-d⁴)/32 |
| Angle of twist | θ = TL/(GJ) |

### Deflection of Beams (Standard Cases)
| Loading | Max Deflection | Location |
|:--------|:---------------|:---------|
| Cantilever + point load P at free end | PL³/(3EI) | Free end |
| Cantilever + UDL w | wL⁴/(8EI) | Free end |
| Simply supported + point load P at center | PL³/(48EI) | Center |
| Simply supported + UDL w | 5wL⁴/(384EI) | Center |

---

## Framework 2: Engineering Mechanics

### Equilibrium (2D)
- ΣF_x = 0, ΣF_y = 0, ΣM = 0
- **Always** draw FBD first

### Friction
| Type | Formula |
|:-----|:--------|
| Static | F ≤ μ_s × N |
| Kinetic | F = μ_k × N |
| Wedge | Depends on geometry; draw FBD of each surface |
| Ladder | ΣM about foot = 0; check μ at floor |

### Truss Analysis
- **Method of Joints:** Isolate each joint; ΣF_x = 0, ΣF_y = 0 (2 equations per joint)
- **Method of Sections:** Cut through 3 members; ΣM about one point eliminates 2 unknowns
- **Zero-force members:** At a joint with 2 non-collinear members and no external load, both are zero

### Centroid & Moment of Inertia
| Shape | Centroid (y from base) | I (about centroidal axis) |
|:------|:----------------------|:--------------------------|
| Rectangle | d/2 | bd³/12 |
| Triangle | h/3 | bh³/36 |
| Circle | r | πr⁴/4 |
| Semicircle | 4r/(3π) from base | ≈ 0.11r⁴ |

---

## Framework 3: Surveying Quick Facts

### Leveling
- **HI Method:** HI = BM + BS; RL = HI - FS (or IS)
- **Rise-Fall:** Rise = Previous IS/BS - Current IS/FS; RL = Previous RL + Rise (or - Fall)
- **Arithmetic check:** ΣBS - ΣFS = ΣRise - ΣFall = Last RL - First RL
- **Reciprocal leveling:** Eliminates curvature + refraction errors

### Errors in Surveying
| Error Type | Correction |
|:-----------|:-----------|
| Tape too long | Subtract (measured > actual) |
| Tape too short | Add |
| Temperature (above std) | Subtract (tape expands) |
| Sag (chain suspended) | Subtract (measured > horizontal) |
| Slope | Subtract (slope > horizontal) |

### Earthwork Volume
- **Trapezoidal:** V = (A₁ + A₂)/2 × L
- **Prismoidal:** V = L/6 × (A₁ + 4A_mid + A₂)

### Plane Table
- **Radiation:** One-point method; fast for small areas
- **Intersection:** Two-point method; for inaccessible points
- **Resection:** Three-point problem; locating the station

---

## Framework 4: Concrete Technology

| Property | How Measured | Standard |
|:---------|:-------------|:---------|
| Workability | Slump test (mm) | IS 1199 |
| Strength | Cube test (150mm) | IS 516 |
| Quality | NDT: Rebound hammer, UPV | IS 13311 |
| Durability | Chloride penetration, carbonation | IS 456 |

### Mix Design Quick Reference (M30 Example)
- w/c ratio: 0.40–0.45 (lower = stronger, less durable)
- Cement content: 320–400 kg/m³
- Sand: 25–35% of total aggregate
- Aggregate: Angular, well-graded
- Admixtures: As needed for workability

### Curing
- **Minimum:** 7 days (IS 456); recommended 14–28 days
- **Methods:** Water curing (best), membrane curing, steam curing
- **Impact:** 7 days water curing → ~65% of 28-day strength

---

## Framework 5: Environmental Quick Facts

| Parameter | Drinking Standard (IS 10500) | Significance |
|:----------|:----------------------------:|:-------------|
| pH | 6.5–8.5 | Acidity/alkalinity |
| TDS | ≤ 500 mg/L (acceptable) | Mineralization |
| Hardness | ≤ 200 mg/L | Scaling, soap usage |
| Chloride | ≤ 250 mg/L | Corrosion, taste |
| Fluoride | 0.6–1.2 mg/L | Dental health |
| DO | ≥ 5 mg/L (aquatic) | Life support |
| BOD₅ | ≤ 30 mg/L (effluent) | Organic pollution |

### BOD Formula
- y_t = L₀(1 - e^{-k₁t})
- Temperature correction: k_T = k₂₀ × θ^{(T-20)}, θ = 1.047
- At 20°C, k₁ ≈ 0.23/day (base e)

---

## Framework 6: Geotechnical Quick Facts

| Concept | Key Formula/Value |
|:--------|:------------------|
| Phase relationship | Se = wG_s |
| Dry unit weight | γ_d = G_sγ_w/(1+e) |
| Compaction | Modified Proctor: 4.89 kg rammer, 450mm drop, 625 cm³ mould |
| Bearing capacity (Terzaghi, strip) | q_u = cN_c + γD_fN_q + 0.5γBN_γ |
| Consolidation settlement | S_c = C_cH/(1+e₀) × log₁₀(σ'_f/σ'_₀) |
| Permeability (constant head) | k = QL/(Aht) |
| Permeability (falling head) | k = (aL/At)ln(h₁/h₂) |

---

## Framework 7: Transportation Quick Facts

| Topic | Key Point |
|:------|:----------|
| IRC code for bridges | IRC 6 (loads), IRC 21 (concrete), IRC 24 (steel) |
| Pavement design | CBR method (IRC:37),IRC:58 for rigid |
| Traffic signals | Webster's formula: C₀ = (1.5L + 5)/(1 - Y) |
| Road classification | NH > SH > MDR > ODR > VR |
| Sight distance | SSD = vt + v²/(2gf) (driver reaction + braking) |

---

## Framework 8: Quick-Fire Interview Answers (15)

1. **"What is the unit of stress?"** — N/m² or Pa (MPa for practical use)
2. **"What does a positive BM mean?"** — Bottom fibers in tension (sagging)
3. **"What is the difference between RCC and PSC?"** — RCC is unreinforced concrete; PSC uses pre-stressing to create pre-compression
4. **"Why is concrete cured?"** — To maintain moisture for hydration, improving strength and durability
5. **"What is slump?"** — Measure of workability; cone is filled, lifted, and the settlement is measured
6. **"What is the bearing capacity of soil?"** — Maximum pressure soil can support without shear failure or excessive settlement
7. **"What is a flow net?"** — Orthogonal grid of flow lines + equipotential lines for seepage analysis
8. **"What is the difference between dam and barrage?"** — Dam stores water (impounds); barrage controls flow (regulates)
9. **"What is specific energy in open channel flow?"** — E = y + V²/(2g); energy per unit weight measured from channel bed
10. **"What is the critical depth?"** — Depth at which specific energy is minimum for a given discharge
11. **"What is a hydraulic jump?"** — Rapid transition from supercritical to subcritical flow; dissipates energy
12. **"What is the difference between PERT and CPM?"** — PERT is probabilistic (time不确定); CPM is deterministic (time已知)
13. **"What is the purpose of a shear key?"** — Provides additional shear resistance in beam-column joints and retaining walls
14. **"What is the difference between working stress and limit state?"** — WS uses factor of safety on loads/stresses; LS uses partial safety factors on loads and materials
15. **"What is the most common cause of structural failure?"** — Inadequate design, poor construction quality, overloading, or unexpected loading conditions

---

## Last-Minute Checklist

- [ ] All formulae memorized (σ=My/I, τ=Tρ/J, δ=PL/AE)
- [ ] BMD/SFD sign conventions correct
- [ ] Truss analysis method of joints vs sections clear
- [ ] BOD/COD definitions and differences crisp
- [ ] Surveying leveling methods (HI vs Rise-Fall) clear
- [ ] Concrete mix design steps known
- [ ] At least 3 PSU company-specific facts prepared
- [ ] Self-introduction ready (2 minutes)
- [ ] "Why this company?" answered for top 3 choices

---

## Cross-Links

**Study:**
→ [Civil Engineering Foundations](civil-engineering-foundations.md) — Full formula sheet
→ [Role Study Plan](role-study-plan.md) — Detailed preparation guide

**Deeper:**
→ [Structural Engineering](../structures/structures.md)
→ [Geotechnical Engineering](../geotechnical/geotechnical.md)
→ [Environmental Engineering](../environmental/environmental-engineering.md)

**Interview:**
→ [Technical Interview Bank](../../prep/interview/technical/technical-interview-bank.md)
→ [Behavioral Guide](../../prep/behavioral/behavioral-interview-guide.md)

---

*Last updated: 2026-09-04*
