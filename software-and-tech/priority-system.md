# 📊 Software Priority System

> Every tool in this repository is classified by **proficiency level** and **priority tag** to prevent students from spending months on low-value tools.

---

## Proficiency Levels

### L1 — Awareness

**Know what it does and where it is used.**

You can explain the tool to someone, name its primary use case, and identify when it would be the right choice. You cannot use it yourself.

**When L1 is enough:**
- You're in a role where you interact with the tool's output (e.g., a PM reviewing CFD results)
- The tool is relevant to your branch but not your target role
- You need to understand the tool's vocabulary for interviews

**How to achieve L1:**
- Read this repository's page for the tool (15–30 minutes)
- Watch one 10-minute tutorial video
- Understand 2–3 use cases in your domain

---

### L2 — Basic Proficiency

**Can perform standard workflows.**

You can open the tool, follow a known workflow, and produce a standard output. You need guidance for anything non-routine.

**When L2 is enough:**
- The tool is a supporting skill (e.g., Excel for a structural engineer)
- You need it for coursework or a single project component
- It's listed as `[OPTIONAL]` or `[ROLE DEPENDENT]` for your target

**How to achieve L2:**
- Complete one structured tutorial or online course module (5–10 hours)
- Reproduce one example project from documentation
- Use it in one real assignment or project

---

### L3 — Working Proficiency

**Can independently complete a realistic project.**

You can set up a workflow from scratch, troubleshoot common issues, and produce results without hand-holding. This is the **target level for most placement-critical tools**.

**When L3 is required:**
- The tool is `[MUST LEARN]` or `[HIGH ROI]` for your target role
- You plan to put it on your resume
- You need to discuss it intelligently in an interview

**How to achieve L3:**
- Complete a full project using the tool (20–40 hours total)
- Handle real data / real geometry / real boundary conditions
- Encounter and solve at least 3 non-trivial problems independently
- Document your workflow for your portfolio

> ⚠️ **Only list a tool on your resume if you are at L3 or above.**

---

### L4 — Advanced Proficiency

**Can handle complex modelling, automation, customization, or troubleshooting.**

You can write custom scripts/plugins, debug solver convergence, optimize workflows, and handle edge cases. You understand the underlying algorithms.

**When L4 is needed:**
- You are targeting a **specialized role** (CFD Engineer, Computational Researcher, HPC)
- The tool is the **core of your job** (e.g., OpenFOAM for a CFD engineer)
- You are in **M.Tech/PhD research** requiring deep tool expertise

**When L4 is NOT needed:**
- Every other tool in your stack
- Tools you list as "familiar with" rather than "expert in"
- Any tool where L3 covers the interview questions

> ⚠️ **Never recommend L4 knowledge unless there is a genuine role-specific reason.**

---

## Priority Tags

| Tag | Meaning | Action |
|:----|:--------|:-------|
| `[MUST LEARN]` | Non-negotiable for this role/branch | Learn to at least L2; L3 if resume-relevant |
| `[HIGH ROI]` | High placement return for effort invested | Prioritize over `[ROLE DEPENDENT]` tools |
| `[ROLE DEPENDENT]` | Required only for specific roles | Learn only if targeting that role |
| `[SPECIALIZED]` | Needed for niche positions (R&D, CFD, etc.) | Learn only if role demands it |
| `[OPTIONAL]` | Nice to have, not required | Skip unless you have spare time |

### Decision Rule

```
If tag == [MUST LEARN]:
    → Minimum L2, target L3
    → Add to resume if L3

If tag == [HIGH ROI]:
    → Target L3
    → Add to resume if L3
    → Prioritize over [ROLE DEPENDENT] tools

If tag == [ROLE DEPENDENT]:
    → Learn only if targeting that specific role
    → L2 minimum, L3 if core to role

If tag == [SPECIALIZED]:
    → Learn only for niche roles (CFD, R&D, HPC)
    → L2 awareness may be enough for interviews

If tag == [OPTIONAL]:
    → L1 awareness is sufficient
    → Skip if time-constrained
```

---

## Combined Classification Table

| Tool | L1 | L2 | L3 | L4 | Typical Tag |
|:-----|:---|:---|:---|:---|:------------|
| Python | Know what it is | Write basic scripts | Full project workflow | Custom libraries, optimization | `[MUST LEARN]` for most roles |
| Excel | Know formulas exist | Pivot tables, VLOOKUP | Power Query, macros | VBA automation | `[MUST LEARN]` for non-tech roles |
| SQL | Know what databases are | SELECT, JOIN, GROUP BY | Window functions, CTEs | Query optimization, schema design | `[MUST LEARN]` for BA/DA/PA |
| MATLAB | Know it exists | Matrix ops, plotting | ODE solvers, toolboxes | Custom toolboxes, Simulink | `[HIGH ROI]` for research |
| Git | Know version control | Commit, push, pull | Branching, PRs, merge conflicts | CI/CD, automation | `[MUST LEARN]` for tech roles |
| AutoCAD | Know it's CAD | Draw in 2D, dimensions | Create construction drawings | Custom blocks, automation | `[MUST LEARN]` for structural/construction |
| STAAD.Pro | Know it's structural | Model simple frames | Full analysis + design | Dynamic analysis, custom codes | `[MUST LEARN]` for structural |
| ETABS | Know it's for buildings | Model simple building | Full building design | Seismic, advanced loads | `[HIGH ROI]` for structural |
| HEC-RAS | Know it's river modeling | 1D steady flow | Unsteady flow, 2D | Calibration, real projects | `[MUST LEARN]` for HWRE |
| OpenFOAM | Know it's CFD | Run built-in tutorials | Set up custom cases | Solver modification, UDFs | `[SPECIALIZED]` / `[HIGH ROI]` for CFD |
| PLAXIS | Know it's geotech FEM | Simple slope model | Consolidation, seepage | Advanced constitutive models | `[MUST LEARN]` for geotech |
| QGIS / ArcGIS | Know it's GIS | Load layers, basic analysis | Spatial analysis, raster processing | Custom plugins, automation | `[MUST LEARN]` for GIS roles |
| Power BI | Know it's BI | Create basic dashboard | DAX, data modeling | Advanced DAX, row-level security | `[HIGH ROI]` for DA/BA |
| Primavera P6 | Know it's scheduling | Create basic schedule | Resource loading, baseline | Multi-project, earned value | `[MUST LEARN]` for planning |

---

## How to Use This System

### Step 1: Identify Your Tools

From the [`branch-roadmaps.md`](branch-roadmaps.md) or [`role-roadmaps.md`](role-roadmaps.md), identify which tools are tagged for your branch/role.

### Step 2: Check Your Current Level

For each tool, honestly assess: L1 / L2 / L3 / L4.

### Step 3: Apply the Priority Rule

```
Target Level = Required Level from the roadmap tag
Current Level = Your honest assessment
Gap = Target - Current

If Gap > 0:
    → This tool needs attention
    → Use the learning roadmap to plan study time
If Gap <= 0:
    → This tool is covered
    → Move to the next tool
```

### Step 4: Prioritize

If you can't learn everything (you can't), prioritize by:

1. `[MUST LEARN]` tools with the biggest gap first
2. Then `[HIGH ROI]` tools
3. Then `[ROLE DEPENDENT]` tools
4. Skip `[OPTIONAL]` and `[SPECIALIZED]` unless you have time

---

## Anti-Patterns

| ❌ Don't | ✅ Do Instead |
|:---------|:-------------|
| List 15 tools on your resume | List 4–6 tools you can discuss in depth |
| Learn every CAD package | Master AutoCAD, know Civil 3D exists |
| Spend 3 months on OpenFOAM for a PM role | Spend 3 months on Excel + SQL + metrics |
| Claim "Advanced Python" after one script | Claim "Working proficiency" after one project |
| Skip Git because "it's not engineering" | Learn Git — it's a differentiator for technical roles |
| Learn cloud computing for a structural role | Learn ETABS + Revit for structural roles |

---

*See also: [`anti-overload.md`](anti-overload.md) for the "one + one + one" strategy.*
*See also: [`resume-positioning.md`](resume-positioning.md) for how to write proficiency honestly.*
