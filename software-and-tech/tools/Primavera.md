# 📅 Primavera P6 / MS Project for Construction

> **Priority:** P0 — Required (Construction/PM) | **Target Level:** L2–L3
> **Time to L2:** 15–20 hrs | **Time to L3:** 25–35 hrs
> **Canonical source.** Construction and operations pages link here.

---

## 1. What It Is

**Primavera P6** (Oracle) and **MS Project** (Microsoft) are **project scheduling** tools used to plan, schedule, and track construction projects. They implement the **Critical Path Method (CPM)**, resource loading, and earned value management.

## 2. Where It Is Used

| Application | Context |
|:------------|:--------|
| Construction scheduling | Building, infrastructure, industrial projects |
| CPM analysis | Critical path, float, schedule compression |
| Resource loading | Labour, equipment, material allocation |
| Cost control | Earned value, cost loading |
| Baseline tracking | Schedule vs actual progress |
| Tender planning | Pre-construction planning |

## 3. Why Your Target Role Needs It

**Company evidence:**

| Company | Role | Scheduling Level |
|:--------|:-----|:-----------------|
| L&T | Civil Engineer | Basic (Primavera/MS Project) |
| Godrej Properties | AM — Project Execution | Proficient |
| ITC | AUT — Projects | Required |
| BPCL | Management Trainee | Basic |
| HPCL | Officer — Engineering | Required |

> **Interview tip:** "How do you create a WBS for a building project?" and "What is the difference between CPM and PERT?" are common asks.

---

## 4. Installation / Setup

| Option | How |
|:-------|:----|
| **MS Project** | Microsoft 365 (free via IITK) |
| **Primavera P6** | Oracle academic license |
| **Free alternative** | ProjectLibre, GanttProject (for practice) |

**Setup checklist:**
- [ ] Set calendar (working days, holidays)
- [ ] Define project start date
- [ ] Set units (days, hours)
- [ ] Create WBS structure

---

## 5. Core Interface / Workflow

```
Create WBS → Add activities → Set durations → Link dependencies (FS, SS, FF)
→ Assign resources → Level resources → Baseline → Track progress → Earned value
```

**Key panels:** Activity table, Gantt chart, Resource usage, Network diagram.

---

## 6. Essential Features (3 High-Value Blocks)

### Block 1: Scheduling (CPM)

| Feature | Purpose |
|:--------|:--------|
| WBS | Work breakdown structure |
| Activities | Tasks with durations |
| Dependencies | FS (finish-start), SS, FF, SF |
| Critical path | Longest path, zero float |
| Float/slack | Schedule flexibility |
| Milestones | Zero-duration key events |

### Block 2: Resources & Cost

| Feature | Purpose |
|:--------|:--------|
| Resource loading | Assign labour/equipment/material |
| Resource leveling | Resolve overallocation |
| Cost loading | Assign cost to activities |
| Baseline | Save original schedule |

### Block 3: Tracking & EVM

| Feature | Purpose |
|:--------|:--------|
| Progress update | % complete per activity |
| S-curve | Planned vs actual |
| Earned value | SPI, CPI, SV, CV |
| Schedule compression | Crashing, fast-tracking |

---

## 7. Typical Engineering Workflow

```
Step 1: Create WBS (site prep → foundations → structure → finishes)
Step 2: Add activities with durations
Step 3: Link dependencies (FS most common)
Step 4: Identify critical path
Step 5: Assign resources + level
Step 6: Save baseline
Step 7: Update progress weekly
Step 8: Report SPI/CPI (earned value)
```

---

## 8. Worked Example — Small Building Schedule

**Task:** Create a CPM schedule for a small building (foundation → structure → finishes).

```
WBS:
    1. Site Preparation (5 days)
    2. Foundations (10 days) — FS after 1
    3. Structure (20 days) — FS after 2
    4. Roofing (10 days) — FS after 3
    5. Finishes (15 days) — FS after 4
    6. Handover (2 days) — FS after 5

Critical path: 1→2→3→4→5→6 = 62 days (all zero float)
Float: none on critical path
```

**Output:** Gantt chart with critical path highlighted, total duration 62 days.

---

## 9. Practice Exercises

### Basic
1. Create a **5-activity schedule** with FS dependencies, find the critical path
2. Add **milestones** at key completion points
3. Calculate **float** for a non-critical activity

### Intermediate
4. Build a **building schedule** (WBS → activities → dependencies)
5. Assign **resources** (2 labour crews) and check for overallocation
6. Create a **baseline** and update progress to 50%

### Role-Specific (Construction)
7. Create a **foundation-to-handover schedule** for a residential tower
8. Perform **earned value analysis** (SPI, CPI) on a 3-month schedule
9. Compress the schedule by **crashing** the critical path

---

## 10. Mini-Project — Construction Schedule + Dashboard

```
Objective: Create a construction schedule and progress dashboard
Input: Building BOQ, activity list, resource availability
Workflow:
    1. Build WBS + activities + dependencies (Primavera/MS Project)
    2. Identify critical path
    3. Assign resources + cost
    4. Save baseline
    5. Export to Excel → build Power BI dashboard
Expected Output: Gantt chart + critical path + EVM report + dashboard
Interview Questions It Prepares You For:
    - "How do you create a WBS for a building project?"
    - "What is the difference between CPM and PERT?"
    - "How do you handle resource leveling?"
```

---

## 11. Common Mistakes

| Mistake | Why It's Wrong | Correct Approach |
|:--------|:---------------|:-----------------|
| No WBS | Schedule not structured | Break work into WBS first |
| Wrong dependencies | Incorrect critical path | Use FS correctly |
| No resource leveling | Overallocated crews | Level resources |
| No baseline | Can't track progress | Save baseline |
| Ignoring float | Miss schedule flexibility | Track float |
| Updating without logic | Wrong EVM | Update % complete properly |

---

## 12. Interview Questions

### Basic
- What is the critical path method (CPM)?
- What is float and why does it matter?
- What is the difference between CPM and PERT?

### Workflow
- How do you create a WBS for a building project?
- How do you update a schedule?

### Troubleshooting
- Your schedule has negative float. What do you do?
- Resources are overallocated. How do you resolve?

### Engineering Judgment
- Why did you choose Primavera over MS Project?
- How do you verify schedule accuracy?

---

## 13. Rapid Revision

| Property | Value |
|:---------|:------|
| **Type** | Project scheduling |
| **Developer** | Oracle (P6) / Microsoft (MS Project) |
| **License** | Commercial (academic available) |
| **Platform** | Windows |
| **Difficulty** | Medium |
| **Time to L2** | 15–20 hrs |
| **Time to L3** | 25–35 hrs |
| **Primary use** | Construction scheduling, CPM |
| **Alternative** | ProjectLibre (free) |

**Top 5 concepts:** WBS, Activities, Dependencies, Critical Path, EVM

---

## Theory Linkage

```
Primavera → Construction Management → CPM/PERT, scheduling
          → Project Control → earned value, cost control
          → Resource Management → leveling, allocation
```

---

## Company Linkage

| Company | What to Prepare |
|:--------|:----------------|
| L&T | Basic schedule, CPM vs PERT |
| Godrej | WBS, building schedule, resource loading |
| ITC | Project schedule, cost control |
| BPCL / HPCL | Industrial project scheduling |

---

## Cross-Links

| Related Section | Link |
|:----------------|:-----|
| Role Matrix | [`SOFTWARE_ROLE_MATRIX.md`](../SOFTWARE_ROLE_MATRIX.md) |
| Construction Roadmap | [`construction/construction-tech.md`](../construction/construction-tech.md) |
| Excel (BOQ) | [`tools/Excel.md`](../tools/Excel.md) |
| Interview Questions | [`software-interview-questions.md`](../software-interview-questions.md) |
| Resume Strategy | [`SOFTWARE_RESUME_STRATEGY.md`](../SOFTWARE_RESUME_STRATEGY.md) |

---

*Canonical source for Primavera P6 / MS Project. Do not duplicate in branch pages.*