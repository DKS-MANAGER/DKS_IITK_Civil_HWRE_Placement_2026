# Transportation Engineer — Role Study Plan

> **Role:** Transportation Engineer
> **Tier:** B — Important Alternatives
> **Current Score:** 50/80 (63%) → **Target: ≥64/80 (80%)**
> **Track:** Core Civil (NHAI, IRCON, Airport Authority, Railways, Consulting)

---

## Why This Role?

Transportation engineering is one of the highest-demand civil engineering roles in India. NHAI alone is building 25+ km/day of highways, and the National Infrastructure Pipeline (NIP) allocates ₹20+ lakh crore to roads and railways. Every major consulting firm (L&T, AECOM, Tata Projects, WSP) and PSU (NHAI, IRCON, RITES, Airport Authority of India) hires transportation engineers. The role spans geometric design, traffic engineering, pavement design, railway engineering, and airport planning — all of which are placement-testable topics.

**Why you specifically need this:**
- PSU recruitment (NHAI, IRCON, RITES, AAI) directly tests IRC/MoRTH standards
- Consulting interviews test your ability to design highways, signals, and pavements
- GATE CE has 8-12% weightage for Transportation Engineering

---

## Topic 1: Highway Geometric Design (IRC Standards)

### Why This Topic?
Every NHAI/IRCON interview starts with geometric design. You will be asked to design horizontal curves, vertical curves, and sight distances. IRC:73 and IRC:78 are the standards used in practice.

### What to Learn

- [ ] **Horizontal curve design:** Minimum radius, superelevation, extra widening
  - Formula: R_min = V² / [127(e + f)]
  - IRC recommended f values (0.17 for 30 km/h down to 0.12 for 120 km/h)
  - Superelevation runoff: L_d = w·n·e·b / Δ
- [ ] **Vertical curve design:** Summit curves, valley curves, K-values
  - Summit curve: L = N·V²/46.7 (SSD-based)
  - For SSD ≥ L: L = N·S²/4.4
  - For SSD < L: L = 2S - 4.4/N
- [ ] **Sight distances:** SSD, OSD, intermediate sight distance
  - SSD = 0.278·V·t + V²/[254(f ± G)]
  - OSD = d₁ + d₂ + d₃ (reaction + overtaking + oncoming)
  - IRC SSD table: 24m (30 km/h) to 260m (120 km/h)
- [ ] **Gradient standards:** Ruling, limiting, exceptional gradients per road class
- [ ] **Width standards:** Carriageway width, right-of-way, camber per road class

### Study Material

| File | What to Study | Lines |
|:-----|:-------------|:------|
| [`transportation-engineering.md`](transportation-engineering.md) | §1 Highway Engineering (lines 1-208) | 208 |
| [`civil-engineering-foundations.md`](../fundamentals/civil-engineering-foundations.md) | Quick formulas | 233 |
| [`gate-civil-notes.md`](../gate/civil/gate-civil-notes.md) | Transportation section | 256 |

### Worked Example: Horizontal Curve + Vertical Curve Design

**Problem:** Design a horizontal curve for a NH on plain terrain with design speed 100 km/h. Also design the summit curve for a +4% and -2% grade intersection.

**Solution (Horizontal):**
1. Given: V = 100 km/h, e_max = 0.06 (plain), f = 0.13 (IRC for 100 km/h)
2. R_min = V² / [127(e + f)] = 100² / [127(0.06 + 0.13)] = 10000 / 24.13 = **414.4 m**
3. Use R = 450 m (practical round-up)
4. Check superelevation needed: e = V²/(127R) - f = 10000/(127×450) - 0.13 = 0.175 - 0.13 = **0.045 (4.5%)**

**Solution (Summit Curve):**
1. Given: G₁ = +4%, G₂ = -2%, V = 100 km/h
2. N = |G₁ - G₂| = |4 - (-2)| = 6%
3. SSD for 100 km/h = 185 m (IRC table)
4. Check: L = N·S²/4.4 = 6 × 185² / 4.4 = 6 × 34225 / 4.4 = **46,670 m** — this is clearly SSD ≥ L
5. Use L = N·V²/46.7 = 6 × 100² / 46.7 = 60000/46.7 = **1284.8 m → use 1285 m**
6. Check SSD condition: L = 1285 m > SSD = 185 m ✓ (SSD < L case: L = 2S - 4.4/N = 370 - 73.3 = 296.7 m, but we used the design speed formula which governs)

### Practice

**Basic (3-5):**
1. Calculate R_min for V = 60 km/h, e = 0.07, f = 0.15. [Answer: 283.7 m]
2. Find SSD for V = 80 km/h, t = 2.5 s, f = 0.15, G = -3%. [Answer: ~102 m]
3. What is the ruling gradient for NH on rolling terrain? [Answer: 4%]
4. Calculate OSD for V_b = 40 km/h, V = 80 km/h, a = 1.2 m/s², T = 9 s.

**Intermediate (3-5):**
5. Design a valley curve for a +3% meeting -5% grade at V = 100 km/h. Headlight sight distance governs.
6. A 2-lane NH has capacity 3500 pcu/hr. If design volume is 2800 pcu/hr, what is the LOS?
7. Calculate superelevation runoff length for a 2-lane road with e = 0.06, lane width 3.75 m, rotation rate 1/150.

**Interview-Level (5+):**
8. Why does IRC recommend different f values for different speeds? What happens if you use a constant f?
9. A highway passes through a hilly area. The available radius is 150 m. What design speed should you use? How would you ensure safety?
10. What is the difference between a summit curve designed for SSD vs OSD? Which governs?
11. How do you decide between a single summit curve vs compound vertical alignment?
12. Explain the concept of "design speed" vs "posted speed" vs "operating speed."

### Interview Questions

| Q# | Question | Depth |
|:---|:---------|:------|
| Q1 | What is superelevation and why is it needed? | Fundamentals |
| Q2 | How do you determine the minimum radius of a horizontal curve? | Applied |
| Q3 | Explain the difference between SSD and OSD. | Fundamentals |
| Q4 | How would you design a highway through a mountainous terrain? | Applied |
| Q5 | What are the IRC standards for lane width and shoulder width? | Fundamentals |
| Q6 | A client wants to reduce the curve radius to save land. What factors do you consider? | Deep |

### Common Mistakes

1. **Using wrong friction factor** — f depends on design speed; don't use f = 0.15 for V > 80 km/h
2. **Confusing SSD cases** — Check if SSD ≥ L or SSD < L before applying the formula
3. **Ignoring camber** — Camber is needed for drainage; its slope depends on pavement type
4. **Forgetting gradient correction** — SSD formula includes G (gradient); uphill = +, downhill = -

### Completion Criterion

- [ ] Can solve horizontal curve design from memory
- [ ] Can calculate SSD/OSD for any design speed
- [ ] Can design summit and valley curves
- [ ] Know IRC standards for all road classes

---

## Topic 2: Traffic Engineering & Signal Design

### Why This Topic?
Traffic engineering is a core interview topic for NHAI, consulting firms, and smart city projects. Signal design (Webster's method), traffic flow theory, and capacity analysis are frequently tested.

### What to Learn

- [ ] **Traffic flow fundamentals:** q = k·v, Greenshields model, flow-density diagram
  - q_max = v_f · k_j / 4
  - Optimal: v_opt = v_f/2, k_opt = k_j/2
- [ ] **Traffic studies:** Speed, volume, O-D, parking, accidents
  - Time mean speed vs space mean speed
  - 85th percentile speed → basis for speed limits
- [ ] **Signal design:** Webster's method, phase design, saturation flow
  - C_o = (1.5L + 5) / (1 - ΣY_i)
  - Effective green: g_i = Y_i/ΣY_j × (C - L)
  - Saturation flow: s = 525 · w_h (IRC SP:88)
  - Degree of saturation: X_i = q_i / [s_i × (g_i/C)] ≤ 0.85-0.90
- [ ] **Level of Service (LOS):** A-F classification for Indian conditions
- [ ] **PCU factors:** Indian vehicle mix (IRC standards)
- [ ] **Capacity analysis:** PCU/hr for different road configurations

### Study Material

| File | What to Study | Lines |
|:-----|:-------------|:------|
| [`transportation-engineering.md`](transportation-engineering.md) | §Traffic Engineering (lines 130-208) | 78 |
| [`transportation-engineering.md`](transportation-engineering.md) | §Highway Capacity (lines 98-128) | 30 |
| [`transportation-software.md`](transportation-software.md) | Signal optimization tools | 103 |

### Worked Example: Webster's Signal Design

**Problem:** A 4-leg intersection has 2 phases. Phase 1 (NS): flow = 800 pcu/hr, saturation flow = 1800 pcu/hr. Phase 2 (EW): flow = 600 pcu/hr, saturation flow = 1600 pcu/hr. Lost time per phase = 4 s. Find optimal cycle length and green splits.

**Solution:**
1. Flow ratios: y₁ = 800/1800 = 0.444, y₂ = 600/1600 = 0.375
2. ΣY = 0.444 + 0.375 = 0.819
3. Total lost time: L = 2 × 4 = 8 s
4. C_o = (1.5L + 5) / (1 - ΣY) = (1.5×8 + 5) / (1 - 0.819) = 17 / 0.181 = **93.9 s → use 95 s**
5. Effective green time: C - L = 95 - 8 = 87 s
6. g₁ = (0.444/0.819) × 87 = 0.542 × 87 = **47.2 s**
7. g₂ = (0.375/0.819) × 87 = 0.458 × 87 = **39.8 s**
8. Check: g₁ + g₂ + L = 47.2 + 39.8 + 8 = 95 s ✓
9. Degree of saturation: X₁ = 800/[1800 × (47.2/95)] = 800/893.7 = 0.895 ≤ 0.90 ✓

### Practice

**Basic (3-5):**
1. Given v_f = 80 km/h, k_j = 120 veh/km, find q_max. [Answer: 2400 veh/hr]
2. Find space mean speed if spot speeds are 40, 50, 60 km/h. [Answer: 49.0 km/h]
3. What LOS corresponds to v/c = 0.65? [Answer: LOS C]
4. Calculate PCU for a mixed traffic stream: 200 cars, 50 buses, 100 two-wheelers, 30 auto-rickshaws.

**Intermediate (3-5):**
5. Design signal timing for a 3-phase intersection with given flows and saturation flows.
6. A road has v_f = 60 km/h and k_j = 150 veh/km. What is the jam-to-capacity ratio? Draw the flow-density diagram.
7. Calculate the all-red time for a 20 m wide intersection with V = 40 km/h and vehicle length = 6 m.

**Interview-Level (5+):**
8. How would you handle a saturated intersection where Webster's gives C_o > 120 s?
9. Explain the fundamental diagram of traffic flow. What happens in the unstable region?
10. What are the limitations of Greenshields' model? What are better alternatives?
11. How do you account for mixed traffic (Indian conditions) in capacity analysis?
12. What is the difference between macroscopic and microscopic traffic models?

### Interview Questions

| Q# | Question | Depth |
|:---|:---------|:------|
| Q1 | What is the relationship between flow, density, and speed? | Fundamentals |
| Q2 | Explain Webster's method for signal design. | Applied |
| Q3 | What is LOS and how is it determined? | Fundamentals |
| Q4 | How do you handle pedestrians in signal design? | Applied |
| Q5 | What are PCU factors and why are they used? | Fundamentals |
| Q6 | A signalized intersection has X = 0.95. What does this mean and what would you do? | Deep |

### Common Mistakes

1. **Using arithmetic mean for speed** — Always use harmonic mean for space mean speed
2. **Ignoring lost time** — Webster's formula requires total lost time; don't skip it
3. **Wrong PCU factors** — IRC values differ from AASHTO; know the Indian standards
4. **Confusing flow ratio with degree of saturation** — Y_i = q/s (flow ratio), X_i = q/(s·g/C) (DoS)

### Completion Criterion

- [ ] Can derive Greenshields' model equations
- [ ] Can design a signal from scratch using Webster's
- [ ] Can determine LOS for any road configuration
- [ ] Know Indian PCU factors by heart

---

## Topic 3: Pavement Design (Flexible & Rigid)

### Why This Topic?
NHAI projects require pavement design expertise. IRC:37 (flexible) and IRC:58 (rigid) are the governing codes. This is a high-value interview topic for both PSU and consulting roles.

### What to Learn

- [ ] **Flexible pavement (IRC:37):** Layer structure, CBR method, traffic estimation
  - Layers: Surface (BC) → Binder (DBM) → Base (WMM) → Sub-base (GSB) → Subgrade
  - CBR-based design tables (IRC:37-2018)
  - Layer coefficients: BC=0.35, DBM=0.25, WMM=0.15, GSB=0.08
- [ ] **Rigid pavement (IRC:58):** PCA method, Westergaard stresses, joint design
  - Slab thickness, dowel bars, tie bars
  - Temperature gradient stresses
- [ ] **Traffic estimation:** Cummulative standard axles (CSA), vehicle growth rate
  - Design traffic = Σ(n_i × D_f × L_f × G) in msa
- [ ] **Subgrade evaluation:** CBR testing, CBR classification
- [ ] **Pavement failure modes:** Rutting, cracking, pumping, faulting

### Study Material

| File | What to Study | Lines |
|:-----|:-------------|:------|
| [`transportation-engineering.md`](transportation-engineering.md) | §Pavement Design (lines 211-300+) | ~90 |
| [`geotechnical.md`](../geotechnical/geotechnical.md) | Soil properties, CBR | 277 |

### Worked Example: Flexible Pavement Design

**Problem:** Design a flexible pavement for a NH with the following data: Design CBR = 5%, Traffic = 10 msa, CBR of sub-base = 30%. Determine layer thicknesses.

**Solution:**
1. From IRC:37 table: For CBR = 5%, traffic = 10 msa → Total thickness = **350 mm**
2. Layer composition (IRC guidelines):
   - Surface (BC): 50 mm
   - Binder (DBM): 70 mm
   - Base (WMM): 200 mm
   - Sub-base (GSB): 30 mm (minimum)
   - Total: 50 + 70 + 200 + 30 = 350 mm ✓
3. Check subgrade CBR ≥ 5% → If not, improve with lime stabilization or replace

### Practice

**Basic (3-5):**
1. What is the total pavement thickness for CBR = 3% and traffic = 100 msa? [Answer: ~670 mm]
2. Name the layers of a flexible pavement from top to bottom.
3. What is the minimum CBR required for subgrade? [Answer: 5%]
4. Calculate design traffic: Initial traffic = 2000 cvpd, growth = 7.5%, design life = 10 years, D_f = 0.75.

**Intermediate (3-5):**
5. Compare flexible vs rigid pavement: when would you choose each?
6. Design the rigid pavement slab thickness for V = 80 km/h, traffic = 20 msa, k = 30 kg/cm³.
7. A flexible pavement shows longitudinal cracking. What are the possible causes and remedies?

**Interview-Level (5+):**
8. How does temperature affect rigid pavement design? What is the critical curling stress?
9. What is the difference between IRC:37-2001 and IRC:37-2018? What changed?
10. Explain the concept of "equivalent standard axle load" (ESAL).
11. How would you rehabilitate a failed flexible pavement? What are the options?
12. What is reflective cracking and how do you prevent it?

### Completion Criterion

- [ ] Can determine pavement thickness from CBR tables
- [ ] Can calculate cumulative standard axles
- [ ] Knows the difference between flexible and rigid pavement design
- [ ] Understands failure modes and rehabilitation options

---

## Topic 4: Railway & Airport Engineering

### Why This Topic?
IRCON, RITES, and Airport Authority of India (AAI) specifically test railway and airport topics. These are niche but high-value for PSU interviews.

### What to Learn

- [ ] **Railway track geometry:** Gauge, super-elevation, transition curves, cant deficiency
  - Superelevation: e = G·V²/(127R) (G = gauge width)
  - Cant deficiency: Cd = G·V²/(127R) - e_actual
- [ ] **Railway capacity:** Tonnes per day, train formations, signaling
- [ ] **Airport planning:** Runway orientation, terminal layout, aircraft classification
  - Runway length: governed by elevation, temperature, gradient
  - ICAO Annex 14 standards
- [ ] **Airport pavement:** Flexible vs rigid (FAA/ICAO methods)
- [ ] **Navigation aids:** ILS, VASI, PAPI basics

### Study Material

| File | What to Study | Lines |
|:-----|:-------------|:------|
| [`transportation-engineering.md`](transportation-engineering.md) | §Railway/Airport sections | ~100 |
| [`transportation-software.md`](transportation-software.md) | Planning tools | 103 |

### Worked Example: Railway Superelevation

**Problem:** A broad gauge (1676 mm) railway track has a curve radius of 500 m. The maximum speed is 100 km/h. Calculate the required superelevation and check if cant deficiency is within limits.

**Solution:**
1. G = 1676 mm = 1.676 m, R = 500 m, V = 100 km/h
2. e = G·V²/(127·R) = 1.676 × 100² / (127 × 500) = 16760 / 63500 = **0.264 m = 264 mm**
3. Maximum cant deficiency for BG = 76 mm (Indian Railways standard)
4. Check: Is e_within limits? Maximum e for BG = 165 mm → **264 mm exceeds limit!**
5. Solution: Reduce V or increase R. For e = 165 mm: V = √(165 × 127 × 500 / 1676) = √(6238) = **78.9 km/h → 80 km/h**
6. At V = 80 km/h: e = 1.676 × 6400 / 63500 = 169.2 mm ≈ 170 mm (slightly over; use cant deficiency = 170 - 165 = 5 mm, acceptable)

### Practice

**Basic (3-5):**
1. What is the standard gauge for Indian Railways? [Answer: 1676 mm (BG)]
2. Calculate superelevation for MG (1000 mm) track, R = 300 m, V = 60 km/h. [Answer: 284 mm]
3. What is the minimum runway length for an airport at 500 m elevation?
4. Define ICAO aircraft classification codes.

**Intermediate (3-5):**
5. Design the runway orientation for a location where the wind rose shows 60% winds from the east and 30% from the southeast.
6. What is the effect of temperature on runway length requirement?
7. Explain the difference between flexible and rigid airport pavements.

**Interview-Level (5+):**
8. How does cant excess differ from cant deficiency? What are the safety implications?
9. A railway station needs platform extension. What factors govern the design?
10. Explain the runway capacity concept. What limits it?
11. How do you determine the approach obstacle limitation surface (OLS)?
12. What are the recent developments in Indian railway infrastructure (BULLET TRAIN, RRTS)?

### Completion Criterion

- [ ] Can calculate superelevation and cant deficiency
- [ ] Knows ICAO runway standards
- [ ] Understands aircraft classification and terminal planning
- [ ] Aware of Indian railway modernization projects

---

## Mock Test (45 minutes, 100 marks)

| Q# | Topic | Marks | Difficulty |
|:---|:------|:-----:|:-----------|
| Q1 | Design a horizontal curve for V = 80 km/h, plain terrain. Find R_min and superelevation. | 12 | Basic |
| Q2 | Calculate SSD for V = 100 km/h on a -4% gradient. | 8 | Basic |
| Q3 | Design a signal for a 2-phase intersection using Webster's method. | 15 | Intermediate |
| Q4 | A flexible pavement has CBR = 3% and traffic = 50 msa. Design the layer thickness. | 15 | Intermediate |
| Q5 | Compare Greenshields and Greenberg traffic flow models. Which is more realistic? | 10 | Intermediate |
| Q6 | A broad gauge curve has R = 600 m. Find the maximum permissible speed considering superelevation and cant deficiency limits. | 12 | Intermediate |
| Q7 | Explain the PCA method for rigid pavement design. What inputs are needed? | 10 | Interview |
| Q8 | How would you handle a saturated intersection where standard signal design fails? | 10 | Interview |
| Q9 | A NH passes through a hilly area. Discuss the geometric design challenges and solutions. | 8 | Interview |

**Total: 100 marks | Time: 45 minutes | Pass: 60 marks**

---

## Interview Strategy

### Round Structure (Typical PSU / Consulting)

| Round | Focus | Preparation |
|:------|:------|:------------|
| **Round 1: Written/Aptitude** | Quantitative + Technical basics | Aptitude formulas + IRC standards |
| **Round 2: Technical** | Design problems, code provisions | Geometric design, pavement, traffic |
| **Round 3: HR** | Behavioral, fit, salary | STAR stories, company research |

### Company-Specific Navigation

| Company | Key Focus Areas | Study Priority |
|:--------|:---------------|:---------------|
| **NHAI** | Highway design (IRC), toll management, BOT projects | Topics 1, 2, 3 |
| **IRCON** | Railway track, bridge engineering, construction | Topics 1, 4 |
| **RITES** | Multi-modal transport, feasibility studies | Topics 1, 2, 4 |
| **Airport Authority (AAI)** | Airport planning, runway design, navigation | Topic 4 |
| **L&T / AECOM** | Highway design, traffic studies, pavement | Topics 1, 2, 3 |
| **WSP / Arup** | Multi-modal transport planning, ITS | Topics 2, 3 |

### Behavioral Prep

Prepare 3 STAR stories for transportation context:
1. **Technical challenge:** Solving a design problem in a project/course
2. **Teamwork:** Working with survey team / construction crew
3. **Learning:** Adapting to new software (AutoCAD Civil 3D, HCS, Synchro)

---

## Cross-Links

- [`transportation-engineering.md`](transportation-engineering.md) — Full subject reference (642 lines)
- [`transportation-software.md`](transportation-software.md) — Software tools (Synchro, HCS, OpenRoads)
- [`geotechnical.md`](../geotechnical/geotechnical.md) — Pavement subgrade design
- [`structures.md`](../structures/structures.md) — Bridge engineering integration
- [`infrastructure-engineering-management.md`](../infrastructure/infrastructure-engineering-management.md) — PM aspects of transport projects
- [`civil-rapid-revision.md`](../fundamentals/civil-rapid-revision.md) — Quick formula reference
- [`technical-interview-bank.md`](../../prep/interview/technical/technical-interview-bank.md) — 100+ interview questions
- [`company-profiles.md`](../../prep/company-profiles/company-profiles.md) — Company-specific strategies

---

## References

- IRC:73 — Geometric Design Standards for Rural Highways
- IRC:78 — Standard Specifications for Road Bridges
- IRC:37-2018 — Code of Practice for Design of Flexible Pavements
- IRC:58-2015 — Code of Practice for Design of Cement Concrete Pavements
- IRC SP:88 — Guidelines for Traffic Signal Design
- IRC:102 — Guidelines for Capacity of Urban Roads
- MoRTH — Specifications for Road and Bridge Works
- ICAO Annex 14 — Aerodromes
* [awesome-civil-engineering](https://github.com/awesome-civil-engineering/awesome-civil-engineering)
