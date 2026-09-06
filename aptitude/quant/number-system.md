# Number System

> **Priority:** P0 · **Role relevance:** Important–Critical (all roles)
> **Difficulty range:** Easy → Very Hard · **Time per question:** 30 sec – 3 min

---

## 1. What You Need to Know

1. Number classifications
2. Divisibility rules
3. Unit digit cyclicity
4. Remainders
5. Number of factors
6. Sum of series

---

## 2. Core Concepts

- **Natural, whole, integer, rational, irrational, real** numbers.
- **Prime** numbers (>1, only 2 factors). 2 is the only even prime.
- **Co-prime** numbers (HCF = 1).
- **Unit digit cyclicity** — powers repeat in cycles.
- **Number of factors** from prime factorization.

---

## 3. Formula Sheet

| Concept | Formula |
|:--------|:--------|
| Sum of n naturals | `n(n+1)/2` |
| Sum of squares | `n(n+1)(2n+1)/6` |
| Sum of cubes | `[n(n+1)/2]²` |
| Sum of first n odds | `n²` |
| Sum of first n evens | `n(n+1)` |
| Number of factors of `p^a q^b` | `(a+1)(b+1)` |
| Unit digit cyclicity | 2,3,7,8 → cycle 4; 4,9 → cycle 2 |

---

## 4. Standard Methods

1. **Classify** the number type.
2. **For unit digits** — find the cycle, reduce exponent mod cycle.
3. **For factors** — prime factorize, apply formula.
4. **For remainders** — use modular arithmetic.

---

## 5. Fast Methods / Shortcuts

### Shortcut 1: Unit Digit Cyclicity
**When useful:** Finding the last digit of a large power.
**Why it works:** The unit digit of powers repeats in a fixed cycle.
**Example:** Unit digit of `7^562`: cycle of 7 is 4 (7,9,3,1). `562 mod 4 = 2` → `7² = 49` → unit digit 9.
**When NOT to use:** When the base ends in 0,1,5,6 (always same digit).

### Shortcut 2: Number of Factors
**When useful:** Counting divisors of a number.
**Why it works:** Each prime exponent can be chosen in (a+1) ways.
**Example:** 360 = `2³×3²×5`. Factors = `(3+1)(2+1)(1+1) = 24`.
**When NOT to use:** When counting prime factors only.

---

## 6. Worked Examples

### Example 1 (Easy)
**Q:** Is 1 prime or composite?
**Method:** Definition. **Calculation:** 1 has only one factor. **Answer:** Neither.

### Example 2 (Medium)
**Q:** Unit digit of `(287)^562 × (124)^321`?
**Method:** Cyclicity. **Calculation:** 7-cycle: `562 mod 4 = 2` → 9. 4-cycle: odd → 4. `9×4 = 36` → 6. **Answer:** 6.

### Example 3 (Medium)
**Q:** Number of factors of 360 excluding 1 and itself?
**Method:** Prime factorize. **Calculation:** `2³×3²×5`. Factors = 24. Excluding = 22. **Answer:** 22.

### Example 4 (Hard)
**Q:** Remainder when `2^31` is divided by 5?
**Method:** Modulo cycle. **Calculation:** 2-cycle mod 5 = 2,4,3,1 (length 4). `31 mod 4 = 3` → `2³ = 8 ≡ 3`. **Answer:** 3.

### Example 5 (Very Hard)
**Q:** Number of trailing zeroes in 100!?
**Method:** Count factors of 5. **Calculation:** `⌊100/5⌋ + ⌊100/25⌋ = 20 + 4 = 24`. **Answer:** 24.

---

## 7. Common Traps

| Trap | Why it's wrong | Correct approach |
|:-----|:---------------|:-----------------|
| 1 is prime | 1 has one factor | 1 is neither prime nor composite |
| Wrong cyclicity | Different bases cycle differently | Check base's cycle |
| Forgetting 0/1/5/6 bases | Always same digit | No cycle needed |
| Counting 1 and itself as factors | Formula counts all | Subtract 2 if excluding |

---

## 8. Practice — Basic

1. Is 17 prime? *(Easy, 30 sec)*
2. Unit digit of `3^4`? *(Easy, 30 sec)*
3. Sum of first 10 natural numbers? *(Easy, 30 sec)*
4. Number of factors of 12? *(Easy, 60 sec)*
5. Is 15 prime or composite? *(Easy, 30 sec)*

---

## 9. Practice — Intermediate

6. Unit digit of `7^123`? *(Medium, 60 sec)*
7. Number of factors of 72? *(Medium, 60 sec)*
8. Sum of first 20 odd numbers? *(Medium, 30 sec)*
9. Remainder when `3^50` divided by 5? *(Medium, 90 sec)*
10. Number of zeroes in 50!? *(Medium, 90 sec)*

---

## 10. Practice — Advanced

11. Unit digit of `(287)^562 × (124)^321`? *(Hard, 2 min)*
12. A number divided by 899 leaves 63. Remainder when divided by 29? *(Hard, 2 min)*
13. Number of positive integers n ≤ 100 with `n²-1` divisible by 8? *(Hard, 2 min)*
14. Remainder when `7^100` divided by 100? *(Hard, 3 min)*
15. Sum of all numbers between 100 and 300 divisible by 4? *(Hard, 2 min)*

---

## 11. Placement Questions

### Q1 (Easy, 30 sec)
**Q:** Which of the following is a prime number?
- A) 21  B) 23  C) 27  D) 33
- **Answer:** B) 23
- **Explanation:** 23 has only factors 1 and 23.
- **Fast method:** Check divisibility by primes up to √23.
- **Concept:** Prime numbers. **Difficulty:** Easy. **Time:** 30 sec. **Trap:** None.

### Q2 (Medium, 60 sec)
**Q:** The unit digit of `7^123` is?
- A) 7  B) 9  C) 3  D) 1
- **Answer:** C) 3
- **Explanation:** 7-cycle = 7,9,3,1 (length 4). `123 mod 4 = 3` → `7³ = 343` → unit digit 3.
- **Fast method:** Reduce exponent mod cycle length.
- **Concept:** Cyclicity. **Difficulty:** Medium. **Time:** 60 sec. **Trap:** Wrong cycle position.

### Q3 (Hard, 2 min)
**Q:** The number of zeroes at the end of 100! is?
- A) 20  B) 24  C) 22  D) 25
- **Answer:** B) 24
- **Explanation:** `⌊100/5⌋ + ⌊100/25⌋ = 20 + 4 = 24`.
- **Fast method:** Legendre's formula.
- **Concept:** Trailing zeroes. **Difficulty:** Hard. **Time:** 2 min. **Trap:** Counting only 100/5 = 20.

---

## 12. Rapid Revision

- **Must-know:** Divisibility rules, unit digit cyclicity
- **Shortcut:** Number of factors `(a+1)(b+1)`
- **Trap:** 1 is neither prime nor composite
- **Common Q:** Remainders, factors, unit digits, trailing zeroes

---

## 🔗 Cross-Links

- [Formula Sheet](../FORMULA_SHEET.md)
- [HCF & LCM](hcf-lcm.md)
- [Simplification](simplification.md)
- [Topic Test: Number System](../tests/number-system-test.md)
