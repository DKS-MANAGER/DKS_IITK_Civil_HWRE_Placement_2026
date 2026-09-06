# Probability

> **Priority:** P1 · **Role relevance:** Important (all roles), Critical (Analytics, Software)
> **Difficulty range:** Easy → Very Hard · **Time per question:** 30 sec – 3 min

---

## 1. What You Need to Know

1. Sample space, events, outcomes
2. Basic probability = favorable/total
3. Mutually exclusive events
4. Independent events
5. Conditional probability
6. Addition and multiplication theorems

---

## 2. Formula Sheet

| Concept | Formula |
|:--------|:--------|
| Basic probability | `P(E) = n(E)/n(S)` |
| Complement | `P(not E) = 1 - P(E)` |
| Addition (any) | `P(A∪B) = P(A) + P(B) - P(A∩B)` |
| Mutually exclusive | `P(A∪B) = P(A) + P(B)` |
| Independent | `P(A∩B) = P(A) × P(B)` |
| Conditional | `P(A|B) = P(A∩B)/P(B)` |
| Multiplication | `P(A∩B) = P(A) × P(B|A)` |

---

## 3. Worked Examples

### Q1 (Easy)
**Q:** A die is rolled. P(3 or 5)?
**Solution:** 2/6 = 1/3. **Answer:** 1/3.

### Q2 (Medium)
**Q:** Two coins tossed. P(at least one head)?
**Solution:** P(no head) = 1/4. P(at least 1) = 1-1/4 = 3/4. **Answer:** 3/4.

### Q3 (Medium)
**Q:** Two dice rolled. P(sum = 7)?
**Solution:** Favorable: (1,6),(2,5),(3,4),(4,3),(5,2),(6,1) = 6. Total = 36. P = 6/36 = 1/6.
**Answer:** 1/6.

### Q4 (Hard)
**Q:** P(A) = 0.6, P(B) = 0.5, P(A∩B) = 0.3. P(A∪B)?
**Solution:** 0.6+0.5-0.3 = 0.8. **Answer:** 0.8.

### Q5 (Very Hard)
**Q:** A card drawn from a deck. P(heart or king)?
**Solution:** P(heart) = 13/52. P(king) = 4/52. P(heart∩king) = 1/52. P = 13/52+4/52-1/52 = 16/52 = 4/13.
**Answer:** 4/13.

---

## 4. Practice (15 Questions)

### Basic
1. A die is rolled. P(even number)? *(Easy)*
2. A coin is tossed. P(heads)? *(Easy)*
3. 5 red, 3 blue balls in a bag. P(red)? *(Easy)*
4. P(A) = 0.3. P(not A)? *(Easy)*
5. Two dice. P(sum = 11)? *(Easy)*

### Intermediate
6. Two coins. P(exactly one head)? *(Medium)*
7. P(A)=0.5, P(B)=0.4, independent. P(A∩B)? *(Medium)*
8. A card from deck. P(face card)? *(Medium)*
9. 3 balls drawn from 5 red, 3 blue (without replacement). P(all red)? *(Medium)*
10. P(A∪B)=0.7, P(A)=0.4, P(B)=0.5. P(A∩B)? *(Medium)*

### Advanced
11. Two dice. P(sum ≥ 9)? *(Hard)*
12. P(A)=0.6, P(B)=0.5, P(A∩B)=0.3. P(A|B)? *(Hard)*
13. Bag: 4 red, 3 green, 2 blue. 2 drawn. P(at least 1 red)? *(Hard)*
14. P(A)=0.3, P(B|A)=0.5. P(A∩B)? *(Hard)*
15. 5 people sit randomly in a row. P(2 particular people sit together)? *(Hard)*

---

## 5. Placement Questions

### Q1 (Easy)
**Q:** A die is rolled. P(>4)?
- A) 1/3  B) 1/2  C) 2/3  D) 1/6
**Answer:** A) 1/3. Favorable: 5,6 = 2/6 = 1/3.

### Q2 (Medium)
**Q:** Two dice are rolled. Probability that the sum is 7?
- A) 1/6  B) 1/12  C) 5/36  D) 7/36
**Answer:** A) 1/6. 6 favorable out of 36.

### Q3 (Hard)
**Q:** A bag contains 5 red and 3 blue balls. Two balls are drawn without replacement. Probability that both are red?
- A) 25/64  B) 20/56  C) 10/28  D) Both B and C
**Answer:** D) Both B and C = 20/56 = 5/14. Both simplify to 5/14.

---

## 6. Rapid Revision

- **Must-know:** P = favorable/total; complement = 1-P
- **Shortcut:** P(at least 1) = 1 - P(none)
- **Trap:** Confusing independent with mutually exclusive
- **Common Q:** Cards, dice, coins, balls in bag

---

## 🔗 Cross-Links

- [Formula Sheet](../FORMULA_SHEET.md)
- [Permutations & Combinations](permutations-combinations.md)
- [Topic Test: Probability](../tests/probability-test.md)