# 📋 Software Page Template

> Use this template when creating or evaluating any software/tool page in this repository.

---

## Template Structure

Every major software/tool page in `software-and-tech/` follows this structure. Not all sections are required for every tool — scale the depth to the tool's relevance.

---

### 1. What is it?

One paragraph. No jargon. Explain like you're telling a first-year student.

```
[Tool Name] is a [type of software] used for [primary purpose].
It is developed by [company/org] and is [open-source/commercial/both].
```

### 2. Why is it used?

The business/engineering problem it solves. Not its feature list — the **pain point**.

```
Engineers use [Tool] because [specific problem] is hard to do manually.
In industry, this matters because [business impact].
```

### 3. Civil Engineering applications

Map to specific Civil sub-disciplines:

| Application | Branch | Context |
|:------------|:-------|:--------|
| [Use case 1] | [Branch] | [When/why used] |
| [Use case 2] | [Branch] | [When/why used] |

### 4. Relevant branches

Which Civil specializations benefit from this tool?

- [ ] Structural
- [ ] Geotechnical
- [ ] Transportation
- [ ] Environmental
- [ ] Hydraulics / HWRE
- [ ] Hydrology
- [ ] Construction Management
- [ ] GIS / Geoinformatics
- [ ] General Civil

### 5. Relevant job roles

Which job roles require or benefit from this tool?

| Role | Required? | Proficiency Needed |
|:-----|:----------|:-------------------|
| [Role 1] | Yes / Useful / Optional | L1 / L2 / L3 / L4 |

### 6. Required prerequisites

What must a student know **before** learning this tool?

```
- [Prerequisite 1]
- [Prerequisite 2]
- [Optional prerequisite]
```

### 7. Required proficiency level

Based on the [priority system](priority-system.md):

| Tag | Level | Rationale |
|:----|:------|:----------|
| `[MUST LEARN]` / `[HIGH ROI]` / etc. | L2 / L3 / L4 | [Why this level] |

### 8. Core features to learn

Only the features relevant to Civil placement. Not the full feature list.

```
Must-know:
1. [Feature 1] — Used for [specific task]
2. [Feature 2] — Used for [specific task]
3. [Feature 3] — Used for [specific task]

Nice-to-know:
4. [Feature 4] — Occasionally useful for [task]
```

### 9. What NOT to waste time learning

Be explicit about what students should skip:

```
Do NOT spend time on:
- [Advanced feature] — only relevant for [niche use case]
- [Plugin/extension] — not used in Civil workflows
- [Menu option] — rarely needed in practice
```

### 10. Typical industry workflow

The standard sequence an engineer follows in practice:

```
Step 1: [Input / Setup] — [What you do]
Step 2: [Processing] — [What you do]
Step 3: [Configuration] — [What you do]
Step 4: [Analysis] — [What you do]
Step 5: [Output] — [What you get]
Step 6: [Validation] — [How you check it]
```

### 11. Example project

A realistic, placement-ready project:

```
Project: [Name]
Objective: [What you're solving]
Tools: [Software + supporting tools]
Prerequisites: [What you need to know first]
Workflow:
    1. [Step]
    2. [Step]
    3. [Step]
Expected Output: [What you produce]
Portfolio Value: [How it looks on resume]
Interview Relevance: [What questions it prepares you for]
```

### 12. Portfolio value

How useful is this project for your GitHub/portfolio?

| Aspect | Assessment |
|:-------|:-----------|
| Visual impact | High / Medium / Low |
| Technical depth | High / Medium / Low |
| Uniqueness | High / Medium / Low |
| Interview story | Strong / Moderate / Weak |

### 13. Resume value

How to position this tool on your resume:

```
❌ Bad:  "Proficient in [Tool]"
❌ Bad:  "Used [Tool] for coursework"
✅ Good: "[Action verb] + [what you did] + [tool] + [result/impact]"
```

Example:
```
✅ "Developed Python automation to process 500+ HEC-RAS output files,
    reducing post-processing time from 3 hours to 15 minutes"
```

### 14. Interview questions

#### Basic (101)
- What is [Tool]?
- When would you use [Tool] vs [Alternative]?

#### Practical (201)
- Walk me through your workflow in [Tool].
- What was the most challenging part of using [Tool]?

#### Technical (301)
- How does [Tool] handle [specific technical scenario]?
- What would you do if [Tool] gave unexpected results?

#### Troubleshooting
- Your model isn't converging. What do you check first?
- Results look wrong. How do you validate?

#### Validation
- How do you know your output is correct?
- What benchmarks do you use?

#### Project Defense
- Explain your project from start to finish.
- Why did you choose [Tool] over alternatives?
- What would you do differently?

### 15. Common mistakes

| Mistake | Why It's Wrong | Correct Approach |
|:--------|:---------------|:-----------------|
| [Mistake 1] | [Why] | [Better approach] |
| [Mistake 2] | [Why] | [Better approach] |
| [Mistake 3] | [Why] | [Better approach] |

### 16. Alternatives

| Alternative | When to Use Instead | Key Difference |
|:------------|:-------------------|:---------------|
| [Alt 1] | [When] | [What's different] |
| [Alt 2] | [When] | [What's different] |

### 17. Free/Open-source alternatives

| Free Option | Replaces | Limitations |
|:------------|:---------|:------------|
| [Free tool] | [Paid tool it replaces] | [What you lose] |

### 18. Industry-standard alternatives

| Industry Tool | Where Used | License |
|:--------------|:-----------|:--------|
| [Tool] | [Company type / industry] | [Cost model] |

### 19. Learning roadmap

```
Beginner (0–10 hrs):
    → Interface tour
    → Basic workflow tutorial
    → Reproduce one example

Intermediate (10–30 hrs):
    → Realistic project with real data
    → Handle common errors
    → Explore 3–5 key features deeply

Advanced (30–60 hrs):
    → Complex project
    → Automation / scripting
    → Optimization
    → Portfolio documentation

Expert (60+ hrs):
    → Custom workflows
    → Troubleshooting edge cases
    → Teaching others
    → Contributing to documentation
```

### 20. Quick reference card

| Property | Value |
|:---------|:------|
| **Type** | [Category] |
| **Developer** | [Company/Org] |
| **License** | [Open-source / Commercial] |
| **Platform** | [Windows / Linux / macOS / Web] |
| **Difficulty** | [Easy / Medium / Hard] |
| **Time to L2** | [Hours] |
| **Time to L3** | [Hours] |
| **Primary use** | [One-line purpose] |
| **Alternative** | [Main competitor] |

---

## Scaling Guidelines

| Tool Importance | Sections to Include |
|:----------------|:-------------------|
| `[MUST LEARN]` | All 20 sections |
| `[HIGH ROI]` | Sections 1–15, 19–20 |
| `[ROLE DEPENDENT]` | Sections 1–10, 14, 19–20 |
| `[SPECIALIZED]` | Sections 1–8, 14, 19–20 |
| `[OPTIONAL]` | Sections 1–5, 20 |

---

*This template ensures consistency across all software pages in the repository.*
