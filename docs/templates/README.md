# Content Templates

> Canonical page templates for consistent content creation across the repository.

---

## Available Templates

| Template | Content Type | Use For |
|:---------|:-------------|:--------|
| [concept.md](concept.md) | Concept | Theory + equations + application |
| [numerical.md](numerical.md) | Numerical | Problem + solution + interpretation |
| [interview.md](interview.md) | Interview | Question + answer + follow-up |
| [software.md](software.md) | Software | Purpose + workflow + project + interview |
| [career.md](career.md) | Career | Role + skills + roadmap + interview |
| [project.md](project.md) | Project | Problem + methodology + defense Qs |
| [revision.md](revision.md) | Revision | High-density last-minute summary |
| [resource.md](resource.md) | Resource | External references with assessment |

---

## How to Use

1. **Choose the template** that matches your content type
2. **Copy the template** to the target location
3. **Fill in the content** following the structure
4. **Verify** against the [Content Standards](../content-standards.md)
5. **Link** the new page from its parent README

---

## Metadata

Every template includes a metadata block at the top:

```yaml
---
Category: core | non-core | prep | software | resource
Branch: hwre | structural | geotechnical | environmental | transportation | ...
Role: [target role]
Level: beginner | intermediate | advanced | interview
Priority: P0 | P1 | P2 | P3
Type: concept | numerical | interview | software | project | career | revision
Prerequisites: [list of prerequisite topics]
---
```

See [Content Standards](../content-standards.md) for the full taxonomy.

---

## Related

- [Architecture](../architecture.md) — folder structure and naming
- [Content Standards](../content-standards.md) — quality gates and formatting rules
