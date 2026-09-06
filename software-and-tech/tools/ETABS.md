# 🏢 ETABS for Structural Engineering

> **Priority:** P0 — Required (Structural) | **Target Level:** L3
> **Time to L2:** 20–30 hrs | **Time to L3:** 40–50 hrs
> **Canonical source.** Structural pages link here.

---

## 1. What It Is

ETABS (Extended 3D Analysis of Building Systems) is a **structural analysis and design software** by Computers and Structures Inc. (CSI), specialized for **building structures**. It is the industry standard for multi-story building analysis, seismic design, and code-based design.

## 2. Where It Is Used

| Application | Context |
|:------------|:--------|
| Multi-story building analysis | G+10, G+20 residential/commercial towers |
| Seismic design | Response spectrum, equivalent static, pushover |
| Wind load analysis | Lateral load distribution |
| Concrete design | Beams, columns, slabs, shear walls per IS 456 |
| Steel design | Frames per IS 800 |
| Dynamic analysis | Modal, time-history |

## 3. Why Your Target Role Needs It

**Company evidence:**

| Company | Role | ETABS Level |
|:--------|:-----|:------------|
| Thornton Tomasetti | Structural Engineer | Proficient |
| SPECTRUM | Trainee Design Engineer | Basic |
| Hilti | Graduate Engineer | Intermediate |
| Smarttrak AI | Structural Engineer | Required |
| L&T | Civil Engineer | Basic |

> **Interview tip:** "Model a G+15 building with moment frames" is a common ETABS ask at structural consultancies.

---

## 4. Installation / Setup

| Option | How |
|:-------|:----|
| **ETABS (student)** | CSI offers free student version (limited members) |
| **ETABS (full)** | Commercial license via institute/company |
| **Alternative** | SAP2000 (general FEA), STAAD.Pro (frame design) |

**Setup checklist:**
- [ ] Set units (kN, m, C) — consistent throughout
- [ ] Set grid system (spacing, story heights)
- [ ] Define materials (M25, M30, Fe415, Fe500)
- [ ] Define sections (beam, column, slab, wall)

---

## 5. Core Interface / Workflow

```
Define (materials, sections, loads) → Draw (grid, members) → Assign (supports, diaphragms)
→ Analyze (gravity + lateral) → Design (concrete/steel) → Results (forces, drift, ratios)
```

**Key panels:** Model Explorer (tree), Property Manager, Grid System, Load Patterns.

---

## 6. Essential Features (3 High-Value Blocks)

### Block 1: Model Creation

| Feature | Purpose |
|:--------|:--------|
| Grid system | Define column grid and story levels |
| Materials | Concrete/steel properties (E, fck, fy) |
| Frame sections | Beam/column dimensions and reinforcement |
| Slab/wall sections | Shell elements for floors and shear walls |
| Draw tools | Place members on grid |

### Block 2: Loads & Analysis

| Feature | Purpose |
|:--------|:--------|
| Load patterns | Dead, live, wind, seismic (IS 875, IS 1893) |
| Load combinations | 1.5(DL+LL), 1.2(DL+LL+EQ), etc. per IS 456 |
| Diaphragm | Rigid floor diaphragm for lateral distribution |
| Supports | Fixed/pinned at base |
| Analysis types | Equivalent static, response spectrum, time-history |

### Block 3: Design & Results

| Feature | Purpose |
|:--------|:--------|
| Concrete design | Beam/column design per IS 456 |
| Steel design | Frame design per IS 800 |
| Story drift | Inter-story drift check per IS 1893 |
| Member forces | Bending moment, shear, axial |
| Design ratios | Utilization ratio per member |

---

## 7. Typical Engineering Workflow

```
Step 1: Define grid + story levels
Step 2: Define materials + sections
Step 3: Draw columns, beams, slabs, shear walls
Step 4: Assign supports (fixed base)
Step 5: Define loads (DL, LL, WL, EQ) + combinations
Step 6: Assign diaphragm (rigid)
Step 7: Run analysis
Step 8: Check results (drift, forces, reactions)
Step 9: Design members (concrete/steel)
Step 10: Review design ratios, iterate sections
```

---

## 8. Worked Example — G+3 Building Analysis

**Task:** Model and analyze a 4-story (G+3) RCC building frame.

```
1. Grid: 3 bays × 3 bays at 4m, story height 3m
2. Materials: M25 concrete, Fe415 steel
3. Sections: Column 400×400, Beam 300×450, Slab 150mm
4. Loads: DL=1.5 kN/m² (floor finish), LL=3 kN/m² (IS 875)
5. Seismic: Zone III, R=5, I=1 (IS 1893)
6. Combinations: 1.5(DL+LL), 1.2(DL+LL+EQX), 1.5(DL+EQX), etc.
7. Diaphragm: Rigid at each floor
8. Analyze → check story drift < 0.004h (IS 1893)
9. Design columns/beams → check ratios < 1.0
```

**Output:** Member forces, design ratios, drift values, base reactions.

---

## 9. Practice Exercises

### Basic
1. Model a **single-bay portal frame** (2 columns + 1 beam), apply point load, check moments
2. Model a **continuous beam** on 3 supports, apply UDL, compare with hand calc
3. Define materials and sections for a G+3 building

### Intermediate
4. Model a **G+3 building** with rigid diaphragm, apply DL+LL, run analysis
5. Add **seismic load** (response spectrum, Zone III), check story drift
6. Design a **column** and check the reinforcement ratio

### Role-Specific (Structural)
7. Model a **G+10 building** with shear walls, run response spectrum analysis
8. Perform a **pushover analysis** and extract the capacity curve
9. Check **inter-story drift** compliance per IS 1893

---

## 10. Mini-Project — Multi-Story Building Design

```
Objective: Design a G+5 RCC building in Seismic Zone IV
Input: Architectural plan, IS 875 loads, IS 1893 seismic parameters
Workflow:
    1. Define grid, materials, sections
    2. Model frame + slab + shear walls
    3. Apply DL, LL, WL, EQ loads + combinations
    4. Run analysis, check drift
    5. Design members per IS 456
    6. Extract design ratios and iterate
Expected Output: Model + design report + drift check + reinforcement summary
Interview Questions It Prepares You For:
    - "How do you model a shear wall in ETABS?"
    - "How do you check inter-story drift?"
    - "What load combinations did you use and why?"
```

---

## 11. Common Mistakes

| Mistake | Why It's Wrong | Correct Approach |
|:--------|:---------------|:-----------------|
| Inconsistent units | Results off by 1000x | Set units once, stay consistent |
| No diaphragm | Lateral loads distribute wrong | Assign rigid diaphragm |
| Wrong supports | Unstable or over-constrained model | Fixed base for buildings |
| Missing load combinations | Unsafe design | Define all IS 456 combos |
| Ignoring drift | Fails seismic check | Check drift per IS 1893 |
| Over-meshing slabs | Slow, unnecessary | Use appropriate mesh |

---

## 12. Interview Questions

### Basic
- What is the difference between ETABS and STAAD.Pro?
- What is a rigid diaphragm and why is it used?
- What is the difference between equivalent static and response spectrum analysis?

### Workflow
- Walk me through modeling a multi-story building in ETABS.
- How do you apply seismic loads per IS 1893?

### Troubleshooting
- Your model shows instability. What do you check?
- Story drift exceeds the limit. What do you do?

### Engineering Judgment
- Why did you choose a rigid diaphragm for this building?
- How do you decide between shear walls and moment frames?

### Follow-up
- What would happen if you removed the diaphragm?
- How would you handle a soft-story irregularity?

---

## 13. Rapid Revision

| Property | Value |
|:---------|:------|
| **Type** | Building structural analysis/design |
| **Developer** | CSI |
| **License** | Commercial (student version available) |
| **Platform** | Windows |
| **Difficulty** | Medium |
| **Time to L2** | 20–30 hrs |
| **Time to L3** | 40–50 hrs |
| **Primary use** | Multi-story building design |
| **Alternative** | STAAD.Pro, SAP2000 |

**Top 5 concepts:** Grid, Materials, Loads, Diaphragm, Design ratios

---

## Theory Linkage

```
ETABS → Structural Analysis → FEM → stiffness method
      → Loads → IS 875 (DL/LL/WL), IS 1893 (seismic)
      → Boundary conditions → supports, diaphragms
      → Design → IS 456 (concrete), IS 800 (steel)
```

---

## Company Linkage

| Company | What to Prepare |
|:--------|:----------------|
| Thornton Tomasetti | G+15 building, shear walls, response spectrum |
| SPECTRUM | G+3 building, basic modeling |
| Hilti | Model + extract anchor forces |
| Smarttrak AI | Solar structure FEA |

---

## Cross-Links

| Related Section | Link |
|:----------------|:-----|
| Role Matrix | [`SOFTWARE_ROLE_MATRIX.md`](../SOFTWARE_ROLE_MATRIX.md) |
| Structural Roadmap | [`structural/structural-tech.md`](../structural/structural-tech.md) |
| STAAD.Pro (sibling) | [`tools/STAAD.md`](../tools/STAAD.md) |
| Interview Questions | [`software-interview-questions.md`](../software-interview-questions.md) |
| Resume Strategy | [`SOFTWARE_RESUME_STRATEGY.md`](../SOFTWARE_RESUME_STRATEGY.md) |

---

*Canonical source for ETABS. Do not duplicate in branch pages.*