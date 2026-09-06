# 🏗️ Revit / Navisworks for BIM

> **Priority:** P1 — High-value (BIM/Structural/Construction) | **Target Level:** L2–L3
> **Time to L2:** 20–30 hrs | **Time to L3:** 40–60 hrs
> **Canonical source.** BIM, structural, construction pages link here.

---

## 1. What It Is

**Revit** (Autodesk) is **Building Information Modeling (BIM)** software — a 3D parametric model of a building where every element (wall, beam, column) carries data (material, dimensions, cost). **Navisworks** is the coordination tool for **clash detection** and model review.

## 2. Where It Is Used

| Application | Context |
|:------------|:--------|
| 3D structural modeling | Beams, columns, slabs, rebar |
| BIM coordination | Link architectural/MEP/structural models |
| Clash detection | Navisworks — find conflicts |
| Quantity takeoff | Schedules from model |
| 4D/5D BIM | Schedule + cost linked to model |
| Documentation | Drawings, sheets from model |

## 3. Why Your Target Role Needs It

**Company evidence:**

| Company | Role | Revit Level |
|:--------|:-----|:------------|
| Thornton Tomasetti | Structural Engineer | Proficient |
| Godrej Properties | AM — Project Execution | Awareness |
| Reliance New Energy | Team Member | Basic (BIM) |

> **Interview tip:** "What is the difference between CAD and BIM?" and "What is clash detection?" are common asks.

---

## 4. Installation / Setup

| Option | How |
|:-------|:----|
| **Revit (student)** | Autodesk Education — free |
| **Navisworks** | Autodesk Education — free |
| **Alternative** | ArchiCAD, OpenBuildings |

**Setup checklist:**
- [ ] Set project units (mm)
- [ ] Set levels (story heights)
- [ ] Set grids
- [ ] Load structural families (columns, beams, walls)

---

## 5. Core Interface / Workflow

```
Set levels/grids → Model elements (walls, columns, beams, slabs)
→ Add rebar → Link models → Clash detect (Navisworks) → Schedules → Sheets
```

**Key panels:** Project Browser, Properties palette, Ribbon, View controls.

---

## 6. Essential Features (3 High-Value Blocks)

### Block 1: Modeling

| Feature | Purpose |
|:--------|:--------|
| Levels & grids | Vertical/horizontal reference |
| Walls, columns, beams | Structural elements |
| Floors & slabs | Horizontal elements |
| Families | Parametric element types |
| Rebar | Reinforcement modeling |

### Block 2: Coordination (Navisworks)

| Feature | Purpose |
|:--------|:--------|
| Model linking | Link architectural/MEP/structural |
| Clash detection | Find geometric conflicts |
| Clash report | Document and assign clashes |
| 4D simulation | Link schedule to model |

### Block 3: Documentation

| Feature | Purpose |
|:--------|:--------|
| Schedules | Quantity takeoff, material lists |
| Sheets | Drawing sheets from views |
| Sections/elevations | Cut from model |
| Tags | Annotate elements |

---

## 7. Typical Engineering Workflow

```
Step 1: Set levels + grids
Step 2: Model structural elements (columns, beams, slabs, walls)
Step 3: Add rebar (if detailing)
Step 4: Link architectural + MEP models
Step 5: Run clash detection in Navisworks
Step 6: Resolve clashes
Step 7: Extract schedules + sheets
```

---

## 8. Worked Example — Structural Model + Clash Check

**Task:** Model a 2-story frame and run a clash check.

```
1. Set levels: Ground, Level 1 (3m), Level 2 (6m)
2. Set grids: A, B, C (4m) × 1, 2, 3 (4m)
3. Model columns (400×400) at grid intersections
4. Model beams (300×450) on grids
5. Model floor slabs (150mm) at each level
6. Link an architectural model (from template)
7. Run clash detection in Navisworks (structural vs architectural)
8. Review clash report, resolve conflicts
```

**Output:** Coordinated model + clash report.

---

## 9. Practice Exercises

### Basic
1. Create a 2-story frame with levels, grids, columns, beams, slabs
2. Create a **schedule** of columns (count, volume)
3. Create a **sheet** with plan + section views

### Intermediate
4. Add **rebar** to a beam and schedule it
5. Link an architectural model and run **clash detection**
6. Create a **4D simulation** (link schedule to model)

### Role-Specific (BIM)
7. Model a **structural frame** and coordinate with MEP
8. Produce a **clash report** with assigned responsibilities
9. Extract **quantity takeoff** for BOQ

---

## 10. Mini-Project — BIM Coordination

```
Objective: Coordinate a structural model with architectural/MEP
Input: Structural model, architectural model, MEP model
Workflow:
    1. Model structural frame in Revit
    2. Link architectural + MEP models
    3. Run clash detection in Navisworks
    4. Categorize clashes (hard/soft)
    5. Resolve and re-check
    6. Produce clash report + coordinated model
Expected Output: Coordinated model + clash report + schedule
Interview Questions It Prepares You For:
    - "What is the difference between CAD and BIM?"
    - "What is clash detection and how do you perform it?"
    - "How does 4D BIM differ from 3D BIM?"
```

---

## 11. Common Mistakes

| Mistake | Why It's Wrong | Correct Approach |
|:--------|:---------------|:-----------------|
| Modeling in wrong units | Dimensions off | Set mm units |
| No levels/grids | Uncoordinated model | Set references first |
| Ignoring families | Wrong element types | Use correct families |
| No model linking | Miss clashes | Link all disciplines |
| Not running clash detection | Conflicts on site | Run Navisworks clash |
| No LOD awareness | Wrong detail level | Match LOD to project stage |

---

## 12. Interview Questions

### Basic
- What is the difference between CAD and BIM?
- What is clash detection?
- What is IFC and why is it important?

### Workflow
- How do you create a structural model in Revit?
- How do you extract quantities?

### Troubleshooting
- Your model has coordination issues. How do you resolve?
- Clash report shows 100 clashes. How do you prioritize?

### Engineering Judgment
- Why did you choose Revit over AutoCAD for this project?
- How do you verify model accuracy?

---

## 13. Rapid Revision

| Property | Value |
|:---------|:------|
| **Type** | BIM authoring / coordination |
| **Developer** | Autodesk |
| **License** | Commercial (free for students) |
| **Platform** | Windows |
| **Difficulty** | Medium-Hard |
| **Time to L2** | 20–30 hrs |
| **Time to L3** | 40–60 hrs |
| **Primary use** | 3D modeling, coordination |
| **Alternative** | ArchiCAD, OpenBuildings |

**Top 5 concepts:** Levels, Grids, Families, Clash Detection, Schedules

---

## Theory Linkage

```
Revit → BIM → parametric modeling, LOD
      → Construction → coordination, quantity takeoff
      → Structural → 3D structural modeling, rebar
```

---

## Company Linkage

| Company | What to Prepare |
|:--------|:----------------|
| Thornton Tomasetti | Structural model, rebar, sheets |
| Godrej | BIM awareness, coordination |
| Reliance New Energy | Clash check, 3D model review |

---

## Cross-Links

| Related Section | Link |
|:----------------|:-----|
| Role Matrix | [`SOFTWARE_ROLE_MATRIX.md`](../SOFTWARE_ROLE_MATRIX.md) |
| BIM Roadmap | [`bim/bim-tech.md`](../bim/bim-tech.md) |
| BIM Study Plan | [`bim/role-study-plan.md`](../bim/role-study-plan.md) |
| AutoCAD (2D) | [`tools/AutoCAD.md`](../tools/AutoCAD.md) |
| Interview Questions | [`software-interview-questions.md`](../software-interview-questions.md) |

---

*Canonical source for Revit/Navisworks. Do not duplicate in branch pages.*