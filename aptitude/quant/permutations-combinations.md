# Permutations & Combinations

> **Priority:** P1 · **Role relevance:** Important (all roles), Critical (Software, Analytics)
> **Difficulty range:** Easy → Very Hard · **Time per question:** 30 sec – 3 min

---

## 1. What You Need to Know

1. Fundamental counting principle (multiplication/addition)
2. Permutations (order matters): nPr
3. Combinations (order doesn't matter): nCr
4. Circular permutations
5. Restrictions and conditions
6. Repetition

---

## 2. Formula Sheet

| Concept | Formula |
|:--------|:--------|
| nPr | `n!/(n-r)!` |
| nCr | `n!/[r!(n-r)!]` |
| nCr = nC(n-r) | |
| 0! | = 1 |
| Circular perm | `(n-1)!` |
| Repetition (r positions) | `n^r` |
| nPr = nCr × r! | |

---

## 3. Key Principles

**Multiplication principle:** If task A can be done in m ways and task B in n ways, both together = m × n.

**Addition principle:** If task A can be done in m ways OR task B in n ways, total = m + n.

---

## 4. Worked Examples

### Q1 (Easy)
**Q:** How many 3-digit numbers can be formed from 1,2,3,4,5 (no repetition)?
**Solution:** 5P3 = 5×4×3 = 60. **Answer:** 60.

### Q2 (Medium)
**Q:** In how many ways can 5 people sit around a circular table?
**Solution:** (5-1)! = 4! = 24. **Answer:** 24.

### Q3 (Medium)
**Q:** From 8 people, choose 3 for a committee.
**Solution:** 8C3 = 8!/(3!5!) = (8×7×6)/(3×2×1) = 56. **Answer:** 56.

### Q4 (Hard)
**Q:** How many words can be formed from "MISSISSIPPI"?
**Solution:** 11!/(4!4!2!1!) = 39916800/(24×24×2) = 34650.
**Answer:** 34,650.

### Q5 (Very Hard)
**Q:** 5 men and 3 women sit in a row. No two women together. Number of arrangements?
**Solution:** Arrange 5 men: 5! = 120. Women in 6 gaps: 6P3 = 120. Total = 120×120 = 14400.
**Answer:** 14,400.

---

## 5. Practice (15 Questions)

### Basic
1. 5P2 = ? *(Easy)*
2. 10C3 = ? *(Easy)*
3. How many 4-digit numbers from 1-9 (no repetition)? *(Easy)*
4. 7 people in a line. How many arrangements? *(Easy)*
5. 6C2 = ? *(Easy)*

### Intermediate
6. 8C3 = ? *(Medium)*
7. How many 3-letter codes from A-Z (repetition allowed)? *(Medium)*
8. 5 people around a circle. Arrangements? *(Medium)*
9. From 10 books, choose 3 and arrange them. *(Medium)*
10. In how many ways can "DAUGHTER" be arranged? *(Medium)*

### Advanced
11. How many arrangements of "MATHEMATICS" with vowels together? *(Hard)*
12. 4 men, 3 women in a row, women not together. *(Hard)*
13. 10 people, choose president, VP, secretary. *(Hard)*
14. How many 5-digit numbers are divisible by 5 using 1,2,3,4,5? *(Hard)*
15. In how many ways can 8 identical balls be distributed among 3 boxes? *(Hard)*

---

## 6. Placement Questions

### Q1 (Easy)
**Q:** 6C2 = ?
- A) 15  B) 30  C) 12  D) 20
**Answer:** A) 15. 6×5/2 = 15.

### Q2 (Medium)
**Q:** How many 4-digit numbers can be formed from digits 1-9 without repetition?
- A) 3024  B) 6561  C) 5040  D) 4096
**Answer:** A) 3024. 9P4 = 9×8×7×6 = 3024.

### Q3 (Hard)
**Q:** How many ways to arrange the letters of "BANANA"?
- A) 720  B) 60  C) 360  D) 120
**Answer:** B) 60. 6!/(3!×2!) = 720/12 = 60.

---

## 7. Rapid Revision

- **Order matters** → Permutation (nPr)
- **Order doesn't matter** → Combination (nCr)
- **Circular** → (n-1)!
- **Repetition allowed** → n^r
- **Letters of word** → n!/(repetitions!)
- **Traps:** Distinguish between choosing and arranging

---

## 🔗 Cross-Links

- [Formula Sheet](../FORMULA_SHEET.md)
- [Probability](probability.md)
- [Topic Test: P&C](../tests/permutations-combinations-test.md)