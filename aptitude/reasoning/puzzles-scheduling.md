# Puzzles & Scheduling

> **Priority:** P1 · **Role relevance:** Critical (Consulting, Product, Software, Ops/GM)
> **Difficulty range:** Medium → Very Hard · **Time per question:** 2 – 5 min

---

## 1. What You Need to Know

1. Multi-variable puzzles
2. Floor / stack puzzles
3. Day / month scheduling
4. Selection & grouping puzzles
5. Systematic elimination

---

## 2. Strategy

1. **List all variables** (people, floors, days, colours, …)
2. **Draw a grid** — one row/column per variable
3. **Place the solid clues first** (fixed positions)
4. **Use elimination** for conditional clues
5. **Split into cases** when two possibilities remain
6. **Verify** every clue is satisfied before committing

---

## 3. Worked Examples

### Q1 (Medium) — Floor puzzle
**Q:** Five people A, B, C, D, E live on floors 1–5 (bottom to top). A lives above C. B lives on floor 3. D lives below B. E lives on the top floor. Who lives on floor 2?
**Solution:** E = 5, B = 3. D below B ⇒ D ∈ {1, 2}. A and C take the remaining two floors with A above C.
- Case D = 1: A, C ∈ {2, 4} ⇒ A = 4, C = 2 ⇒ floor 2 = C.
- Case D = 2: A, C ∈ {1, 4} ⇒ A = 4, C = 1 ⇒ floor 2 = D.
Both cases are valid.
**Answer:** Cannot be determined.

### Q2 (Medium) — Day scheduling
**Q:** Five friends A, B, C, D, E are each scheduled on one day, Monday–Friday. A is on Monday. C is exactly two days after A. E is on Friday. B is scheduled before D. Who is on Thursday?
**Solution:** A = Mon; C = Mon + 2 = Wed; E = Fri. B and D take Tue and Thu, and B is before D ⇒ B = Tue, D = Thu.
**Answer:** D.

### Q3 (Hard) — Stack puzzle
**Q:** Seven boxes P–V are stacked, position 1 (bottom) to 7 (top). P is at the bottom. R is immediately above P. U is immediately above R. T is at the top. Q is immediately below T. V is immediately above S. Which box is exactly in the middle (position 4)?
**Solution:** P = 1, R = 2, U = 3, T = 7, Q = 6. S and V take positions 4 and 5 with V immediately above S ⇒ S = 4, V = 5.
**Answer:** S.

---

## 4. Practice (10 Questions — answers below)

### Medium
1. Five people on floors 1–5. A above B, C on floor 2, D below C, E on the top floor. Who is on floor 4?
2. Six people work Monday–Saturday, one each. A is on Wednesday. B is on Monday. C is two days after A. D is on Saturday. E is scheduled before F. Who is on Thursday?
3. Four people A, B, C, D in a row (left to right). A is left of B. B is left of C. D is left of A. Give the order.
4. Five houses in a row have five colours. Yellow is at the far left. The black house is exactly in the middle. The green house is immediately right of the black house. The red house is left of the blue house. Which colour is second from the left?
5. Five people W, X, Y, Z, V on floors 1–5. V is on floor 4. Y is on floor 1. Z is immediately above Y. W is above X. Who is on floor 3?

### Hard
6. Six people A–F split into two groups of three. A is with B. C is with D. E is not in A's group. Which group is F in?
7. Five events V, W, X, Y, Z occur on Monday–Friday, one per day. W is before X. Y is on Friday. V is on the day immediately before W. Z is on Monday. Which day is X?
8. Eight people live on floors 1–8. The number of floors between A and B equals the number between C and D. A is on floor 2, B on floor 5, C on floor 4, and D is above C. Which floor is D on?
9. Six people P, Q, R, S, T, U are interviewed Monday–Saturday, one per day. R is on Monday. P is on Tuesday. T is on Wednesday. Q is on Friday. S is immediately after Q. Who is on Thursday?
10. Seven people A–G finish a race in positions 1–7. A finishes 4th. E finishes immediately after A. D finishes last. G finishes 6th. B finishes immediately before C. F is not adjacent to A. Who finishes 2nd?

### Answer Key
| Q | Answer | Reasoning |
|:-:|:------|:----------|
| 1 | A | C = 2, D = 1, E = 5; A, B ∈ {3, 4} with A above B ⇒ A = 4, B = 3. |
| 2 | F | Wed = A, Mon = B, C = Fri, Sat = D; E, F ∈ {Tue, Thu}, E before F ⇒ F = Thu. |
| 3 | D, A, B, C | D < A, A < B, B < C ⇒ single order D–A–B–C. |
| 4 | Red | Yellow = 1, black = 3, green = 4. Red and blue fill 2 and 5 with red left of blue ⇒ red = 2, blue = 5. |
| 5 | X | V = 4, Y = 1, Z = 2; W, X ∈ {3, 5} with W above X ⇒ W = 5, X = 3. |
| 6 | With A and B | {A, B, F} and {C, D, E} — E is out of A's group, so E joins C and D; F fills A's group. |
| 7 | Thursday | Mon = Z, Fri = Y. V immediately before W, X after W ⇒ V = Tue, W = Wed, X = Thu. |
| 8 | Floor 7 | Between A (2) and B (5) = 2 floors; D above C (4) with 2 between ⇒ D = 7. |
| 9 | U | Mon = R, Tue = P, Wed = T, Fri = Q, Sat = S (immediately after Q) ⇒ Thursday = U. |
| 10 | B | A = 4, E = 5, D = 7, G = 6. Positions 1–3 hold B, C, F. B immediately before C and F not adjacent to A (F ≠ 3) force F = 1, B = 2, C = 3 ⇒ 2nd = B. |

---

## 5. Placement Questions

### Q1 (Medium)
**Q:** Five people A, B, C, D, E live on floors 1–5. A lives above C. B lives on floor 3. D lives below B. E lives on the top floor. Who lives on floor 2?
- A) C  B) D  C) A  D) Cannot be determined
**Answer:** D) Cannot be determined — two valid arrangements exist (see Worked Example Q1).

### Q2 (Hard)
**Q:** Five friends are scheduled Monday–Friday, one per day. A is on Monday. C is exactly two days after A. E is on Friday. B is before D. Who is on Thursday?
- A) B  B) C  C) D  D) Cannot be determined
**Answer:** C) D. A = Mon, C = Wed, E = Fri; B = Tue, D = Thu.

---

## 6. Rapid Revision

- **Grid** every variable; **fix** the solid clues first
- **Case-split** on the last ambiguity, then verify each case
- Recognise when a puzzle is **not fully determined** — that is a valid answer
- **Trap:** missing a case, or assuming "after" means "immediately after"

---

## 🔗 Cross-Links

- [Seating Arrangement](seating-arrangement.md)
- [Order & Ranking](order-ranking.md)
