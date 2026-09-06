# Series

> **Priority:** P0 · **Role relevance:** Critical (Consulting, Analytics, Product, Software, Ops/GM)
> **Difficulty range:** Easy → Very Hard · **Time per question:** 30 sec – 2 min

---

## 1. What You Need to Know

1. Number series (arithmetic, geometric, alternating)
2. Letter series
3. Square/cube series
4. Mixed/combined series
5. Wrong-term series

---

## 2. Core Concepts

A **series** is a sequence of numbers/letters following a pattern. The pattern can be:
- **Arithmetic** — add/subtract a constant
- **Geometric** — multiply/divide by a constant
- **Alternating** — two interleaved series
- **Square/cube** — based on perfect powers
- **Prime** — based on prime numbers
- **Mixed** — combination of operations

---

## 3. Standard Methods

1. **Check differences** between consecutive terms.
2. **Check ratios** if differences aren't constant.
3. **Look for alternating patterns** — separate odd/even positions.
4. **Check square/cube/prime** relationships.
5. **Verify** the pattern predicts the next term.

---

## 4. Fast Methods / Shortcuts

### Shortcut 1: Difference Method
**When useful:** Most number series.
**Why it works:** The pattern is often in the differences (first, second, or third order).
**Example:** 2, 5, 10, 17, 26 → differences 3,5,7,9 (odd numbers) → next = 26+11 = 37.
**When NOT to use:** When differences are not consistent.

### Shortcut 2: Alternating Series
**When useful:** Two patterns interleaved.
**Why it works:** Odd and even positions follow separate patterns.
**Example:** 2, 5, 4, 10, 6, 15 → odd: 2,4,6 (+2); even: 5,10,15 (+5). Next = 8.
**When NOT to use:** When a single pattern fits.

---

## 5. Worked Examples

### Example 1 (Easy)
**Q:** 2, 4, 6, 8, ? 
**Method:** Arithmetic (+2). **Answer:** 10.

### Example 2 (Medium)
**Q:** 2, 6, 18, 54, ?
**Method:** Geometric (×3). **Answer:** 162.

### Example 3 (Medium)
**Q:** 1, 4, 9, 16, 25, ?
**Method:** Squares (1²,2²,3²,4²,5²). **Answer:** 36.

### Example 4 (Hard)
**Q:** 3, 7, 15, 31, 63, ?
**Method:** Each = previous ×2 + 1. **Calculation:** 63×2+1 = 127. **Answer:** 127.

### Example 5 (Very Hard)
**Q:** 2, 5, 4, 10, 6, 15, ?
**Method:** Alternating. **Calculation:** Odd: 2,4,6 (+2) → next 8. **Answer:** 8.

---

## 6. Common Traps

| Trap | Why it's wrong | Correct approach |
|:-----|:---------------|:-----------------|
| Assuming arithmetic | Pattern may be geometric | Check ratios too |
| Missing alternating pattern | Two series hidden | Separate odd/even positions |
| Stopping at first difference | Second-order pattern | Check higher-order differences |
| Ignoring prime/square patterns | Non-linear | Consider powers and primes |

---

## 7. Practice — Basic

1. 1, 3, 5, 7, ? *(Easy, 30 sec)*
2. 2, 4, 8, 16, ? *(Easy, 30 sec)*
3. 10, 20, 30, 40, ? *(Easy, 30 sec)*
4. 1, 8, 27, 64, ? *(Easy, 30 sec)*
5. 5, 10, 20, 40, ? *(Easy, 30 sec)*

---

## 8. Practice — Intermediate

6. 2, 5, 10, 17, 26, ? *(Medium, 60 sec)*
7. 3, 9, 27, 81, ? *(Medium, 30 sec)*
8. 1, 1, 2, 3, 5, 8, ? *(Medium, 60 sec)*
9. 100, 81, 64, 49, ? *(Medium, 60 sec)*
10. 2, 3, 5, 7, 11, ? *(Medium, 60 sec)*

---

## 9. Practice — Advanced

11. 3, 7, 15, 31, 63, ? *(Hard, 2 min)*
12. 2, 5, 4, 10, 6, 15, ? *(Hard, 2 min)*
13. 1, 4, 27, 256, ? *(Hard, 2 min)*
14. 5, 11, 23, 47, 95, ? *(Hard, 2 min)*
15. 2, 6, 12, 20, 30, ? *(Hard, 2 min)*

---

## 10. Placement Questions

### Q1 (Easy, 30 sec)
**Q:** Find the next term: 2, 6, 18, 54, ?
- A) 108  B) 162  C) 144  D) 216
- **Answer:** B) 162
- **Explanation:** Multiply by 3 each time. 54×3 = 162.
- **Fast method:** Geometric progression.
- **Concept:** Geometric series. **Difficulty:** Easy. **Time:** 30 sec. **Trap:** None.

### Q2 (Medium, 60 sec)
**Q:** Find the next term: 2, 5, 10, 17, 26, ?
- A) 35  B) 37  C) 36  D) 39
- **Answer:** B) 37
- **Explanation:** Differences 3,5,7,9 (odd numbers). Next diff = 11. 26+11 = 37.
- **Fast method:** Difference method.
- **Concept:** Second-order series. **Difficulty:** Medium. **Time:** 60 sec. **Trap:** Choosing 35 (adding 9).

### Q3 (Hard, 2 min)
**Q:** Find the next term: 3, 7, 15, 31, 63, ?
- A) 125  B) 127  C) 126  D) 129
- **Answer:** B) 127
- **Explanation:** Each = previous ×2 + 1. 63×2+1 = 127.
- **Fast method:** Pattern ×2+1.
- **Concept:** Mixed series. **Difficulty:** Hard. **Time:** 2 min. **Trap:** Choosing 125 (×2-1).

---

## 11. Rapid Revision

- **Must-know:** Check differences, ratios, alternating patterns
- **Shortcut:** Difference method; separate odd/even positions
- **Trap:** Missing alternating series
- **Common Q:** Arithmetic, geometric, square/cube, alternating

---

## 🔗 Cross-Links

- [Rapid Revision](../RAPID_REVISION.md)
- [Coding-Decoding](coding-decoding.md)
- [Topic Test: Series](../tests/series-test.md)
