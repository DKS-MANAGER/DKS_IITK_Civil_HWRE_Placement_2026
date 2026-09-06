# 🏗️ STAAD.Pro for Structural Engineering

> **Priority:** P0 — Required (Structural/Construction) | **Target Level:** L3
> **Time to L2:** 20–30 hrs | **Time to L3:** 40–60 hrs
> **Canonical source.** Structural and construction pages link here.

---

## 1. What It Is

STAAD.Pro is a **structural analysis and design software** by Bentley Systems. It is widely used for **frame analysis, steel/concrete design, and dynamic analysis** across buildings, bridges, towers, and industrial structures.

## 2. Where It Is Used

| Application | Context |
|:------------|:--------|
| Frame analysis | Portal frames, trusses, continuous beams |
| Steel design | IS 800 member design |
| Concrete design | IS 456 beam/column design |
| Dynamic analysis | Response spectrum, time-history |
| Industrial structures | Equipment supports, pipe racks |
| Bridge components | Substructure analysis |

## 3. Why Your Target Role Needs It

**Company evidence:**

| Company | Role | STAAD Level |
|:--------|:-----|:------------|
| L&T | Civil Engineer | Basic–Intermediate |
| SPECTRUM | Trainee Design Engineer | Intermediate |
| ASC Infratech | Trainee Engineer | Basic |
| BPCL | Management Trainee | Basic |

> **Interview tip:** "Model a portal frame" and "What is the difference between a beam and a plate element?" are common STAAD asks.

---

## 4. Installation / Setup

| Option | How |
|:-------|:----|
| **STAAD.Pro (student)** | Bentley academic license |
| **STAAD.Pro (full)** | Commercial via institute/company |
| **Alternative** | ETABS (buildings), SAP2000 (general) |

**Setup checklist:**
- [ ] Set units (kN, m, C)
- [ ] Define material constants (E, density, Poisson's ratio)
- [ ] Define member sections (ISMB, ISMC, RCC)
- [ ] Set supports (fixed/pinned)

---

## 5. Core Interface / Workflow

```
Model (nodes, members, sections) → Assign (supports, loads) → Analyze
→ Design (steel/concrete) → Results (forces, reactions, ratios)
```

**Key panels:** Model tree, Geometry, Property, Support, Load, Analysis, Design.

---

## 6. Essential Features (3 High-Value Blocks)

### Block 1: Model Creation

| Feature | Purpose |
|:--------|:--------|
| Node/member creation | Define geometry |
| Member sections | ISMB, ISMC, RCC sections |
| Material constants | E, density, Poisson's ratio |
| Supports | Fixed, pinned, roller |
| Member orientation | Beta angle for section orientation |

### Block 2: Loads & Analysis

| Feature | Purpose |
|:--------|:--------|
| Load cases | Dead, live, wind, seismic |
| Load combinations | IS 456 / IS 800 combinations |
| Analysis types | Static, P-delta, response spectrum |
| Member loads | Point, UDL, trapezoidal |

### Block 3: Design & Results

| Feature | Purpose |
|:--------|:--------|
| Steel design | IS 800 member check |
| Concrete design | IS 456 beam/column |
| Design ratios | Utilization per member |
| Reactions | Support reactions for foundation |
| Bending/shear diagrams | Member force visualization |

---

## 7. Typical Engineering Workflow

```
Step 1: Define nodes + members (geometry)
Step 2: Assign sections + materials
Step 3: Assign supports
Step 4: Apply loads (DL, LL, WL, EQ) + combinations
Step 5: Run analysis
Step 6: Check results (forces, reactions, deflections)
Step 7: Design members (steel/concrete)
Step 8: Review design ratios, iterate
```

---

## 8. Worked Example — Portal Frame Analysis

**Task:** Analyze a steel portal frame (6m span, 4m height) with UDL on the beam.

```
1. Nodes: (0,0), (6,0), (0,4), (6,4)
2. Members: 1 (left column), 2 (beam), 3 (right column)
3. Sections: ISMB 300 for all members
4. Supports: Fixed at nodes 1 and 3
5. Loads: UDL 10 kN/m on beam (member 2)
6. Analysis: Static
7. Check: Max bending moment, deflection, reactions
8. Design: Steel design per IS 800 → check ratio
```

**Output:** Bending moment diagram, reactions, design ratio.

---

## 9. Practice Exercises

### Basic
1. Model a **simply supported beam** (6m, ISMB 300), apply UDL, compare max moment with hand calc (wL²/8)
2. Model a **continuous beam** on 3 supports, apply UDL, check support moments
3. Model a **truss** (roof truss), apply joint loads, check member forces

### Intermediate
4. Model a **portal frame** with fixed base, apply lateral load, check sway
5. Add **load combinations** per IS 456, run design
6. Perform **steel design** of a frame member per IS 800

### Role-Specific (Structural)
7. Model a **G+3 building frame** with gravity + seismic loads
8. Design a **steel warehouse truss** with IS 800 checks
9. Extract **support reactions** for foundation design

---

## 10. Mini-Project — Steel Warehouse Design

```
Objective: Design a steel portal frame warehouse (24m span)
Input: Bay spacing, roof loads (IS 875), steel sections (IS 800)
Workflow:
    1. Model frame geometry (columns + rafter)
    2. Assign ISMB/ISMC sections
    3. Apply dead, live, wind loads + combinations
    4. Run analysis
    5. Design members per IS 800
    6. Check ratios, iterate sections
Expected Output: Design report with member sizes + ratios
Interview Questions It Prepares You For:
    - "How do you model a portal frame in STAAD?"
    - "What is the difference between a beam and a plate element?"
    - "How do you define load combinations per IS 456?"
```

---

## 11. Common Mistakes

| Mistake | Why It's Wrong | Correct Approach |
|:--------|:---------------|:-----------------|
| Wrong member orientation | Section bends wrong way | Set beta angle correctly |
| Missing supports | Unstable model | Define all supports |
| Inconsistent units | Results off by 1000x | Set units once |
| No load combinations | Unsafe design | Define all IS combos |
| Ignoring P-delta | Slender frames under-designed | Enable P-delta for tall/slender |
| Not checking reactions | Foundation wrong | Extract and verify reactions |

---

## 12. Interview Questions

### Basic
- What is the difference between STAAD.Pro and ETABS?
- What is the difference between a beam element and a plate element?
- What is the difference between fixed and pinned supports?

### Workflow
- Walk me through modeling a portal frame in STAAD.
- How do you define load combinations per IS 456?

### Troubleshooting
- Your model shows instability. What do you check?
- Design fails the code check. What do you do?

### Engineering Judgment
- Why did you choose STAAD over ETABS for this structure?
- How do you verify your STAAD results against hand calculations?

---

## 13. Rapid Revision

| Property | Value |
|:---------|:------|
| **Type** | Structural analysis/design |
| **Developer** | Bentley Systems |
| **License** | Commercial (academic available) |
| **Platform** | Windows |
| **Difficulty** | Medium |
| **Time to L2** | 20–30 hrs |
| **Time to L3** | 40–60 hrs |
| **Primary use** | Frame analysis, steel/concrete design |
| **Alternative** | ETABS, SAP2000 |

**Top 5 concepts:** Nodes, Members, Sections, Loads, Design ratios

---

## Theory Linkage

```
STAAD.Pro → Structural Analysis → stiffness method, FEM
          → Loads → IS 875, IS 1893
          → Design → IS 456 (concrete), IS 800 (steel)
          → Boundary conditions → supports
```

---

## Company Linkage

| Company | What to Prepare |
|:--------|:----------------|
| L&T | Portal frame, continuous beam, load combos |
| SPECTRUM | Frame modeling, design checks |
| ASC Infratech | Bridge component design |
| BPCL | Industrial structure analysis |

---

## Cross-Links

| Related Section | Link |
|:----------------|:-----|
| Role Matrix | [`SOFTWARE_ROLE_MATRIX.md`](../SOFTWARE_ROLE_MATRIX.md) |
| Structural Roadmap | [`structural/structural-tech.md`](../structural/structural-tech.md) |
| ETABS (sibling) | [`tools/ETABS.md`](../tools/ETABS.md) |
| Interview Questions | [`software-interview-questions.md`](../software-interview-questions.md) |
| Resume Strategy | [`SOFTWARE_RESUME_STRATEGY.md`](../SOFTWARE_RESUME_STRATEGY.md) |

---

*Canonical source for STAAD.Pro. Do not duplicate in branch pages.*