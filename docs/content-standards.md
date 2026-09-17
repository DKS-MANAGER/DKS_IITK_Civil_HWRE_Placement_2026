# Content Standards

> **Quality gates for every piece of content in the repository.**

---

## Definition of Done

A content page is **done** only when it satisfies ALL of the following:

```
✓ Discoverable (findable via navigation or search)
✓ Structurally consistent (follows page type template)
✓ Technically credible (correct equations, units, assumptions)
✓ Placement-relevant (serves a placement preparation purpose)
✓ Practically useful (reduces prep time or improves interview performance)
✓ Cross-linked (connects to related content)
✓ Searchable (has clear headings, keywords, terminology)
✓ Revision-ready (can be used for quick review)
```

---

## Content Quality Checklist

### Technical Correctness

- [ ] All equations are dimensionally consistent
- [ ] Units are stated explicitly
- [ ] Assumptions are documented
- [ ] Sign conventions are clear
- [ ] Numerical examples have verified answers
- [ ] Engineering interpretations are provided (not just math)
- [ ] Contradictions with other pages are resolved

### Placement Relevance

- [ ] Content serves a specific placement preparation purpose
- [ ] Interview applicability is clear
- [ ] Questions test understanding, not just memorization
- [ ] Practical engineering applications are included
- [ ] Software connections are stated where relevant

### Structural Quality

- [ ] Follows the appropriate page type template
- [ ] Heading hierarchy is correct (H1 → H2 → H3 → H4)
- [ ] Tables are properly formatted
- [ ] Code blocks use correct language tags
- [ ] Links use relative paths and are valid
- [ ] No orphan sections (sections that link nowhere)

### Question Quality

Questions should test these levels (in order of value):

| Level | Question Type | Example |
|:------|:-------------|:--------|
| **L5 — Judgment** | "What would you do if…?" | "What if the Froude number is exactly 1.0?" |
| **L4 — Application** | "How would you design…?" | "How would you size this pipe network?" |
| **L3 — Reasoning** | "Why does…?" | "Why does critical flow occur at minimum specific energy?" |
| **L2 — Comparison** | "What is the difference between…?" | "Rankine vs Coulomb earth pressure?" |
| **L1 — Recall** | "Define…", "State…" | "What is Reynolds number?" |

**Target:** At least 60% of interview questions should be L2 or above.

---

## Question Format Standards

### Concept Questions

```markdown
### Q: [Question]

**Answer:**
[2-4 sentence clear answer]

**Key Insight:**
[One sentence — the "why it matters"]

**Follow-up:** [Related question or topic link]
```

### Numerical Questions

```markdown
### Problem [N]: [Title]

**Given:**
- [data 1]
- [data 2]

**Find:** [what to calculate]

**Solution:**
[step-by-step solution with equations]

**Answer:** [final answer with units]

**Common Trap:** [what students get wrong]
```

### Interview Questions

```markdown
### Q: [Question]

**Ideal Answer (2-3 min):**
[Structured answer with key points]

**Follow-up 1:** [deeper question]
**Follow-up 2:** [application question]

**Connected to:** [link to concept page]
```

---

## Duplication Policy

### One Canonical Source Rule

Every concept has **one canonical explanation**. All other references link to it.

```
Canonical: core/hwre/hydraulics/hydraulics.md (Bernoulli section)
    ↑ linked from: prep/interview/technical/technical-interview-bank.md
    ↑ linked from: prep/interview/mock-tests/mock-interview-database.md
    ↑ linked from: core/gate/formulas/gate-civil-formulas.md
    ↑ linked from: prep/interview/quick-revision-system.md
```

### What Counts as Duplication

- Same concept explained in two different files with similar depth → **merge**
- Same concept referenced with a brief summary + link → **OK**
- Same question appearing in multiple question banks → **consolidate**
- Different depth levels of the same concept → **OK if intentional**

---

## File Size Guidelines

| Content Type | Recommended Size | Maximum |
|:-------------|:-----------------|:--------|
| Concept page | 300–600 lines | 800 lines |
| Numerical page | 200–400 lines | 500 lines |
| Interview page | 200–500 lines | 600 lines |
| Career page | 150–300 lines | 400 lines |
| Revision page | 100–200 lines | 300 lines |
| Software page | 200–400 lines | 500 lines |

If a file exceeds the maximum, consider splitting it into sub-topics.

---

## Formatting Rules

### Tables

- Use tables for structured comparison data
- Keep tables under 6 columns when possible
- Left-align text columns, center-align data columns
- Use `---:|` for right-aligned numeric columns

### Code Blocks

- Always specify language: ` ```python `, ` ```bash `, ` ```yaml `
- Include expected output for commands
- Keep code blocks focused and short (<50 lines)

### Links

- Use relative paths for all internal links
- Use descriptive link text (not "click here")
- Verify links before committing

### Emojis

- Use sparingly for navigation/category recognition
- Use in section headers for scanning
- Do not use in technical content

---

## Content Contribution Checklist

Before submitting new content, verify:

- [ ] Page follows the correct template
- [ ] Technical content is accurate
- [ ] Equations are properly formatted (LaTeX)
- [ ] Units are consistent and stated
- [ ] At least 3 interview questions are included
- [ ] Links to related topics exist
- [ ] Links from parent README exist
- [ ] File is under the size limit
- [ ] No duplication of existing canonical content
- [ ] Priority level is assigned
- [ ] Metadata is included (if applicable)

---

## Source & Evidence Policy

Every factual claim, benchmark, and interview projection must be labeled with an evidence level. See [SOURCE_POLICY.md](SOURCE_POLICY.md) and [resources/source-registry.md](../resources/source-registry.md) for the complete policy and register.

| Level | Tag | Meaning & Standard |
|:------|:----|:-------------------|
| **VERIFIED** | `[VERIFIED]` | Confirmed against primary authoritative source (placement cell records, standard textbooks, IS codes, official company JDs). |
| **SOURCE-DERIVED** | `[SOURCE-DERIVED]` | Derived or adapted faithfully from a cited external standard, syllabus, or technical reference. |
| **INFERRED** | `[INFERRED]` | Derived by strict mathematical calculation or logical deduction from verified empirical premises. |
| **PREPARATION HEURISTIC** | `[PREPARATION HEURISTIC]` | Recommended internal repository benchmark, pacing guideline, or diagnostic cutoff. Never claimed as official recruiter criteria. |
| **SELF-REPORTED** | `[SELF-REPORTED]` | Candidate debriefs, alumni testimonies, and unverified student interview recollections. |
| **PREDICTED** | `[PREDICTED]` | Forward-looking market projection, hiring trend estimate, or CTC forecast (requires explicit uncertainty disclaimer). |

**Rules:**
- Label every empirical claim or benchmark in preparation and interview content.
- Cite the canonical source for `[VERIFIED]` and `[SOURCE-DERIVED]` entries.
- Never present `[INFERRED]` or `[PREPARATION HEURISTIC]` as `[VERIFIED]`.
- All `[PREDICTED]` and `[SELF-REPORTED]` metrics must carry appropriate disclaimers.

---

## Naming Conventions

Follow the naming rules in [architecture.md](architecture.md):

- Folders: lowercase, hyphenated, descriptive (`open-channel-flow/`)
- Files: lowercase, hyphenated, descriptive (`hydraulics.md`)
- README.md in each major folder as entry point
- Consistent suffixes: `overview.md`, `guide.md`, `practice.md`

---

## Link Conventions

- Use relative paths for all internal links.
- Use descriptive link text (never "click here").
- Every content page links **up** to its section README.
- Every content page links **sideways** to related topics.
- Question banks link **back** to canonical concept pages.
- Verify links before committing (see [DOCS_LINK_AUDIT.md](_SYSTEM/DOCS_LINK_AUDIT.md)).

---

## Update Conventions

- Update the [Content Registry](_SYSTEM/DOCS_CONTENT_REGISTRY.md) when adding a new topic.
- Update the [File Map](_SYSTEM/DOCS_FILE_MAP.md) when adding/moving/removing a file.
- Keep the [Audit State](_SYSTEM/DOCS_AUDIT_STATE.md) current after meaningful changes.
- Re-run the link audit after any edit to `docs/`.
