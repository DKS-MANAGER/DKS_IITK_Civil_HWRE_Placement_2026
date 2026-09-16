# Coding-Decoding

> **Priority:** P1 · **Role relevance:** Important (all roles), Critical (Software, Product)
> **Difficulty range:** Easy → Hard · **Time per question:** 30 sec – 2 min

---

## 1. Types

### 1.1 Letter Shift
Each letter shifted by a fixed number.
- **Example:** CAT → DBU (each letter +1)

### 1.2 Reverse Alphabet
A↔Z, B↔Y, C↔X, etc.
- **Example:** CAT → XZG (C=3↔X=24, A=1↔Z=26, T=20↔G=7)

### 1.3 Position Sum
Add the alphabet positions of the letters.
- **Example:** CAT = 3 + 1 + 20 = 24

### 1.4 Substitution
Words replaced by other words.
- **Example:** "If sky is called water, water is called air…"

---

## 2. Key Reference

| Letter | Position | Reverse |
|:------:|:--------:|:-------:|
| A | 1 | Z (26) |
| B | 2 | Y (25) |
| C | 3 | X (24) |
| D | 4 | W (23) |
| E | 5 | V (22) |
| … | … | … |
| Z | 26 | A (1) |

**Reverse pairs:** A↔Z, B↔Y, C↔X, D↔W, E↔V, F↔U, G↔T, H↔S, I↔R, J↔Q, K↔P, L↔O, M↔N

---

## 3. Worked Examples

### Q1 (Easy) — Letter shift
**Q:** If CAT is coded as DBU, how is DOG coded?
**Solution:** Each letter +1: C→D, A→B, T→U. Apply to DOG: D→E, O→P, G→H.
**Answer:** EPH.

### Q2 (Medium) — Position sum
**Q:** If CAT = 24 and DOG = 26, what is the code for TIGER?
**Solution:** C+A+T = 3+1+20 = 24 ✓; D+O+G = 4+15+7 = 26 ✓. So the rule is the sum of positions.
T+I+G+E+R = 20 + 9 + 7 + 5 + 18 = **59**.
**Answer:** 59.

### Q3 (Medium) — Substitution
**Q:** If "sky is called water, water is called air, air is called earth", where do birds fly?
**Solution:** Birds fly in the sky; "sky" is called "water".
**Answer:** Water.

### Q4 (Hard) — Digit substitution
**Q:** If PALE is coded 2134 and EARL is coded 4315, what is the code for PEARL?
**Solution:** From PALE → 2134: P=2, A=1, L=3, E=4. From EARL → 4315: E=4, A=1, R=?, L=3 ⇒ the third digit gives R = 5.
PEARL = P E A R L = 2 4 1 5 3.
**Answer:** 24153.

### Q5 (Hard) — Reverse alphabet
**Q:** If CAT is coded as XZG (reverse alphabet), what is the code for DOG?
**Solution:** D→W, O→L, G→T.
**Answer:** WLT.

---

## 4. Practice (15 Questions)

### Basic
1. CAT → DBU. DOG → ? *(Easy)*
2. CAT = 24, DOG = 26 (position sum). TIGER = ? *(Easy)*
3. "sky is called water." Where do birds fly? *(Easy)*
4. A = 1, B = 2, …, Z = 26. Position sum of CAT = ? *(Easy)*
5. Reverse alphabet: CAT → XZG. DOG → ? *(Easy)*

### Intermediate
6. "red is blue, blue is green, green is yellow." What colour is grass called? *(Medium)*
7. Rule A→C, B→D, C→E (shift +2). HELLO → ? *(Medium)*
8. CAT is coded 3-1-20 (positions written out). DOG → ? *(Medium)*
9. MANGO → NBOHP (shift +1). APPLE → ? *(Medium)*
10. "123" → "321" (reverse the digits). "4567" → ? *(Medium)*

### Advanced
11. PALE = 2134, EARL = 4315. PEARL → ? *(Hard)*
12. CAT is coded 24 (position sum). TIGER → ? *(Hard)*
13. Reverse alphabet: DOG is coded WLT. Decode XZG. *(Hard)*
14. HELLO → IFMMP (shift +1). WORLD → ? *(Hard)*
15. "1234" → "4321" (reverse the digits). "56789" → ? *(Hard)*

### Answer Key
| Q | Ans | Q | Ans | Q | Ans |
|:-:|:---|:-:|:---|:-:|:---|
| 1 | EPH | 6 | Yellow | 11 | 24153 |
| 2 | 59 | 7 | JGNNQ | 12 | 59 |
| 3 | Water | 8 | 4-15-7 | 13 | CAT |
| 4 | 24 | 9 | BQQMF | 14 | XPSME |
| 5 | WLT | 10 | 7654 | 15 | 98765 |

**Notes:** Q6 grass is green → green is called "yellow". Q9: A→B, P→Q, P→Q, L→M, E→F. Q13: reverse alphabet is self-inverse, so XZG decodes back to CAT.

---

## 5. Placement Questions

### Q1 (Easy)
**Q:** If CAT is coded as DBU, how is DOG coded?
- A) EPH  B) FQI  C) DPH  D) EOH
**Answer:** A) EPH. Each letter +1.

### Q2 (Medium)
**Q:** If "sky is called water, water is called air, air is called earth", where do birds fly?
- A) Sky  B) Water  C) Air  D) Earth
**Answer:** B) Water. "Sky" is called "water".

### Q3 (Hard)
**Q:** If HELLO is coded as IFMMP (each letter +1), what is the code for WORLD?
- A) XPSME  B) XQSME  C) XPSMF  D) XQSMF
**Answer:** A) XPSME. W→X, O→P, R→S, L→M, D→E.

---

## 6. Rapid Revision

- **Letter shift:** find the fixed shift, then apply it
- **Reverse:** A↔Z, B↔Y, C↔X (self-inverse)
- **Position sum:** add letter positions
- **Substitution:** replace the word, then answer for the substitute
- **Trap:** confirm the shift is consistent for **every** letter before applying it

---

## 🔗 Cross-Links

- [Series](series.md)
- [Formula Sheet](../FORMULA_SHEET.md)
