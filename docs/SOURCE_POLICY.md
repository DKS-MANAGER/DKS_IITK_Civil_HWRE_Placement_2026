# Source Policy

> **Evidence and provenance policy for all content.** Every claim must be traceable to a source or explicitly labeled with its confidence level.

---

## Evidence Levels

Every content page must label its claims with one of these levels:

| Level | Label | Meaning |
|:------|:------|:--------|
| **VERIFIED** | ✅ | Confirmed against a reliable source (textbook, GATE paper, official document) |
| **SOURCE-DERIVED** | 📚 | Derived from a named source (e.g., GATE-O-Pedia) |
| **INFERRED** | 🔍 | Reasoned from first principles; not directly sourced |
| **PREDICTED** | ⚠️ | Forward-looking estimate (e.g., expected CTC, likely questions) |

---

## Rules

1. **Label every claim.** Use the level markers above in tables or inline.
2. **Name the source.** For VERIFIED and SOURCE-DERIVED, cite the specific source.
3. **Do not present INFERRED as VERIFIED.** Mark it clearly.
4. **PREDICTED content** (CTC ranges, company forecasts) must carry a disclaimer.
5. **No unlabeled claims** in technical content.

---

## Source Provenance

Raw source material is tracked in [`sources/`](sources/). See [`sources/gate-o-pedia.md`](sources/gate-o-pedia.md) for the GATE-O-Pedia source text.

---

## Verification Workflow

1. When adding a claim, determine its evidence level.
2. If VERIFIED, add the source citation.
3. If INFERRED, state the reasoning.
4. If PREDICTED, add a disclaimer.
5. Cross-check against the [content standards](content-standards.md) quality gates.

---

## Related

- [Content Standards](content-standards.md) — quality gates
- [Contributing](CONTRIBUTING.md) — how to add content
- [Content Registry](_SYSTEM/DOCS_CONTENT_REGISTRY.md) — canonical topic map

---

> **Back to:** [README](README.md) · [Main README](../README.md)