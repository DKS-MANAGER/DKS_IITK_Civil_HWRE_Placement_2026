# Order & Ranking

> **Priority:** P1 · **Role relevance:** Important (all roles)
> **Difficulty range:** Easy → Hard · **Time per question:** 30 sec – 2 min

---

## 1. Key Formulas

### From One Side
- Position from one side = Rank from that side
- Position from other side = Total + 1 - Position from first side

### From Both Sides
- If a person is ranked X from left and Y from right in a row of N people:
  - **N = X + Y - 1**

### Overlapping (Same Person)
- If counted from both sides, person is at position X from left and Y from right:
  - **N = X + Y - 1** (overlapping case)

### Non-Overlapping (Different People)
- Two people, positions don't overlap:
  - **N = X + Y + (people between them) - 1** or adjust

---

## 2. Worked Examples

### Q1 (Easy)
**Q:** In a row of 10 students, A is 4th from the left. What is position from right?
**Solution:** 10 + 1 - 4 = 7th from right.
**Answer:** 7th from right.

### Q2 (Medium)
**Q:** In a row, A is 5th from left and 8th from right. How many students?
**Solution:** N = 5 + 8 - 1 = 12.
**Answer:** 12 students.

### Q3 (Hard)
**Q:** A is 10th from left, B is 15th from right in a row of 25 students. How many between A and B?
**Solution:** A from right = 25+1-10 = 16. B from left = 25+1-15 = 11. Between = 16-11-1 = 4 (if A is right of B) or 10-11+1... Let me recalculate. A is at position 10, B at position 11 (from left). Between = 11-10-1 = 0. That's too few. Let me re-think: B from right is 15th, so B from left = 25+1-15 = 11. Between = |10-11|-1 = 0. They're adjacent.
**Answer:** 0 (adjacent).

### Q4 (Very Hard)
**Q:** In a class of 50, A is 15th from top and B is 20th from bottom. How many between A and B?
**Solution:** A from bottom = 50+1-15 = 36. B from top = 50+1-20 = 31. Between = 31-15-1 = 15.
**Answer:** 15 students.

---

## 3. Practice (15 Questions)

### Basic
1. In a row of 15, A is 6th from left. Position from right? *(Easy)*
2. A is 8th from left and 12th from right. Total people? *(Easy)*
3. In a row of 20, A is 5th from left, B is 8th from right. How many between? *(Easy)*
4. A is 3rd from top, B is 7th from bottom in 15 students. Between? *(Easy)*
5. In a row, A is 10th from left and 10th from right. Total? *(Easy)*

### Intermediate
6. A is 12th from left, B is 18th from right in 25 students. Between? *(Medium)*
7. In a row, A is 5th from left, B is 8th from right, 3 between them. Total? *(Medium)*
8. A is 20th from top, B is 15th from bottom in 40 students. Between? *(Medium)*
9. In a class, A is 10th from top and 25th from bottom. How many students? *(Medium)*
10. A is 8th from left, B is 12th from right, 4 between them. Total students? *(Medium)*

### Advanced
11. In a row of 30, A is 10th from left, B is 12th from right. C is exactly between A and B. C's position from left? *(Hard)*
12. A is 15th from top, B is 20th from bottom in 40 students. How many between A and B? *(Hard)*
13. In a row, A is 5th from left, B is 10th from right. If A and B swap positions, B is now 8th from left. Total students? *(Hard)*
14. A is 12th from left in a row. If 5 more people join from the right, A becomes 12th from right too. Total people now? *(Hard)*
15. In a class of 45, A is 15th from top. After 10 new students join at the bottom, A's rank from top? *(Hard)*

---

## 4. Placement Questions

### Q1 (Easy)
**Q:** In a row of 20 students, A is 8th from the left. Position from right?
- A) 12th  B) 13th  C) 11th  D) 14th
**Answer:** B) 13th. 20+1-8 = 13.

### Q2 (Medium)
**Q:** In a row, A is 10th from left and 15th from right. Total students?
- A) 23  B) 24  C) 25  D) 26
**Answer:** B) 24. 10+15-1 = 24.

### Q3 (Hard)
**Q:** In a row of 30, A is 10th from left, B is 12th from right. How many between A and B?
- A) 7  B) 8  C) 9  D) 10
**Answer:** C) 9. B from left = 30+1-12 = 19. Between = 19-10-1 = 8. Hmm, let me recheck: positions 10 and 19, between = 19-10-1 = 8. But wait, B is 12th from right in 30 = position 19 from left. Between 10 and 19 = 8. **Answer: B) 8**.

---

## 5. Rapid Revision

- **From other side:** Total + 1 - Position from first side
- **Total people:** X + Y - 1 (overlapping)
- **Between:** |Position1 - Position2| - 1
- **Trap:** Confusing overlapping vs non-overlapping

---

## 🔗 Cross-Links

- [Seating Arrangement](seating-arrangement.md)
- [Formula Sheet](../FORMULA_SHEET.md)