# Seating Arrangement

> **Priority:** P0 · **Role relevance:** Critical (Consulting, Product, Software, Ops/GM)
> **Difficulty range:** Easy → Very Hard · **Time per question:** 1 – 4 min

---

## 1. What You Need to Know

1. Linear arrangement (single row)
2. Two-row parallel arrangement
3. Circular arrangement (facing center/outward)
4. Facing direction logic
5. Relative position clues

---

## 2. Core Concepts

- **Linear**: people in a straight line.
- **Circular**: people around a circle, facing center or outward.
- **Facing North**: left = arrangement's left.
- **Facing South**: left = arrangement's right.
- **Circular (facing center)**: clockwise = left.
- **Circular (facing outward)**: clockwise = right.

---

## 3. Standard Methods

1. **Identify solid clues** — fixed positions first.
2. **Draw cases** — if a clue has two possibilities, draw both.
3. **Place relative clues** — "third to the left of" etc.
4. **Eliminate** invalid cases as more clues are read.
5. **Verify** all clues are satisfied.

---

## 4. Fast Methods / Shortcuts

### Shortcut 1: Solid Clues First
**When useful:** Arrangements with fixed positions.
**Why it works:** Fixed positions anchor the whole arrangement.
**Example:** "A sits at the extreme right" — place A first.
**When NOT to use:** When all clues are relative.

### Shortcut 2: Case Elimination
**When useful:** Clues with two possibilities.
**Why it works:** Drawing both cases and eliminating one saves rework.
**Example:** "B sits third to the right of F" — two possible positions for B.
**When NOT to use:** When a clue uniquely determines position.

---

## 5. Worked Examples

### Example 1 (Easy)
**Q:** Five people A,B,C,D,E in a row. A at extreme left, B second to the right of A. Who is second from right if C is at extreme right?
**Method:** Place A (left), C (right). B second right of A = position 3. **Answer:** D or E (positions 2,4).

### Example 2 (Medium)
**Q:** Eight friends around a circle facing center. B sits third to the right of F. Only two between B and G. A second to the left of D. D not neighbor of B or G. C third to the right of H. E not neighbor of G. Who sits third to the left of C?
**Method:** Draw circle, place solid clues, eliminate. **Answer:** (solve systematically).

### Example 3 (Hard)
**Q:** Twelve people in two parallel rows of six. Row 1 faces South, Row 2 faces North. Various relative clues. Who sits opposite E?
**Method:** Build both rows, match facing pairs. **Answer:** (solve systematically).

---

## 6. Common Traps

| Trap | Why it's wrong | Correct approach |
|:-----|:---------------|:-----------------|
| Wrong facing direction | Left/right flips | Check facing direction |
| Circular clockwise/left confusion | Depends on facing | Facing center: clockwise=left |
| Missing a case | Two possibilities | Draw both cases |
| Not verifying all clues | Partial solution | Check every clue |

---

## 7. Practice — Basic

1. Five people in a row, A at extreme left. Who is at extreme right if B is 3rd? *(Easy, 1 min)*
2. Four people around a circle facing center. A opposite C. B right of A. Who left of C? *(Easy, 1 min)*
3. Six people in a row. A and B at ends. C second from left. Who is 4th? *(Easy, 1 min)*

---

## 8. Practice — Intermediate

4. Eight people in a row. A third from left, B fourth from right. How many between? *(Medium, 1 min)*
5. Six people around a circle facing center. A right of B, C opposite D. Arrange. *(Medium, 2 min)*
6. Two rows of five. Row 1 faces North, Row 2 faces South. Match facing pairs. *(Medium, 3 min)*

---

## 9. Practice — Advanced

7. Eight friends around a circle facing center with multiple relative clues. *(Hard, 4 min)*
8. Twelve people in two parallel rows with complex clues. *(Hard, 4 min)*
9. Circular arrangement facing outward with mixed clues. *(Hard, 4 min)*

---

## 10. Placement Questions

### Q1 (Easy, 1 min)
**Q:** Five people A,B,C,D,E sit in a row. A is at the extreme left and E at the extreme right. B sits second to the right of A. Who sits in the middle?
- A) B  B) C  C) D  D) Cannot be determined
- **Answer:** D) Cannot be determined
- **Explanation:** Positions: A, _, B, _, E. C and D fill positions 2 and 4 in either order.
- **Fast method:** Place solid clues, note ambiguity.
- **Concept:** Linear arrangement. **Difficulty:** Easy. **Time:** 1 min. **Trap:** Assuming a specific order.

### Q2 (Medium, 2 min)
**Q:** Six people sit around a circular table facing the center. A sits opposite D. B sits to the immediate right of A. C sits to the immediate left of D. Who sits opposite B?
- A) C  B) E  C) F  D) Cannot be determined
- **Answer:** D) Cannot be determined
- **Explanation:** E and F positions are not fixed by the clues.
- **Fast method:** Draw circle, place fixed pairs.
- **Concept:** Circular arrangement. **Difficulty:** Medium. **Time:** 2 min. **Trap:** Assuming E/F positions.

---

## 11. Rapid Revision

- **Must-know:** Facing direction logic; solid clues first
- **Shortcut:** Draw cases, eliminate
- **Trap:** Facing direction flips left/right
- **Common Q:** Linear, circular, two-row

---

## 🔗 Cross-Links

- [Rapid Revision](../RAPID_REVISION.md)
- [Puzzles & Scheduling](puzzles-scheduling.md)
- [Order & Ranking](order-ranking.md)
- [Topic Test: Seating Arrangement](../tests/seating-arrangement-test.md)
