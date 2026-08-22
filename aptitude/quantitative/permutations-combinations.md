# Permutations & Combinations

## Concept Definitions

- **Factorial ($n!$)**: Product of all positive integers up to $n$.
  - $n! = n \times (n-1) \times \dots \times 1$
  - Note: $0! = 1$ and $1! = 1$.
- **Permutation ($nPr$)**: An arrangement where order matters.
- **Combination ($nCr$)**: A selection where order does not matter.
- **Multiplication Principle (AND Rule)**: If event 1 can occur in $m$ ways and event 2 in $n$ ways, both can occur in $m \times n$ ways.
- **Addition Principle (OR Rule)**: If event 1 can occur in $m$ ways and event 2 in $n$ ways, either can occur in $m + n$ ways.

---

## Key Formulas & Shortcuts

### Fundamental Formulas
- **Permutations**:
  $$nPr = \frac{n!}{(n-r)!}$$
- **Combinations**:
  $$nCr = \frac{n!}{r!(n-r)!}$$
- **Relationship**:
  $$nPr = r! \times nCr$$

### Important Properties
- $nC_0 = nC_n = 1$
- $nC_1 = n$
- $nCr = nC_{n-r}$

### Arrangements with Repetition
If $n$ objects contain $p$ of one type, $q$ of another, and $r$ of a third:
$$\text{Unique arrangements} = \frac{n!}{p! \cdot q! \cdot r!}$$

### Circular Permutations
- Distinct clockwise/counterclockwise orders:
  $$\text{Arrangements} = (n - 1)!$$
- Clockwise and counterclockwise not distinguishable (e.g., necklace):
  $$\text{Arrangements} = \frac{(n - 1)!}{2}$$

---

## Practice Problems

### Problem 1
In how many ways can the letters of "LEADING" be arranged so that the vowels always come together?

### Problem 2
A committee of 5 members is to be formed from 6 men and 4 women such that it contains at least 3 men. Find the number of ways.

### Problem 3
In how many ways can 6 people be seated around a circular table?

### Problem 4
In how many ways can a group of 5 men and 2 women be selected from 7 men and 3 women?

### Problem 5
How many 4-digit numbers can be formed using digits 1, 2, 3, 4, 5, 6, 7 (without repetition) such that the number is divisible by 5?

---

## Step-by-Step Solutions

### Solution 1
1. Word "LEADING" has 7 letters: 3 vowels (E, A, I) and 4 consonants (L, D, N, G).
2. Group the 3 vowels as a single unit: `(EAI)`. Now arrange 5 units: `(EAI), L, D, N, G`.
3. Arrangements of 5 units $= 5! = 120$.
4. Internal arrangements of vowels $= 3! = 6$.
5. Total ways $= 5! \times 3! = 120 \times 6 = 720$.
6. **Answer**: **720** ways.

### Solution 2
1. At least 3 men means three cases:
   - **Case 1**: 3 men, 2 women $\to 6C_3 \times 4C_2 = 20 \times 6 = 120$.
   - **Case 2**: 4 men, 1 woman $\to 6C_4 \times 4C_1 = 15 \times 4 = 60$.
   - **Case 3**: 5 men, 0 women $\to 6C_5 \times 4C_0 = 6 \times 1 = 6$.
2. Total $= 120 + 60 + 6 = 186$.
3. **Answer**: **186** ways.

### Solution 3
1. Number of people $n = 6$. Clockwise and counterclockwise are distinct.
2. Arrangements $= (6 - 1)! = 5! = 120$.
3. **Answer**: **120** ways.

### Solution 4
1. Select 5 men from 7: $7C_5 = 7C_2 = 21$.
2. Select 2 women from 3: $3C_2 = 3$.
3. Total ways $= 21 \times 3 = 63$.
4. **Answer**: **63** ways.

### Solution 5
1. A number divisible by 5 must end in 5 (the only valid digit from the set).
2. Units place is fixed. Remaining 3 positions filled from 6 digits: $6P_3 = 6 \times 5 \times 4 = 120$.
3. **Answer**: **120** numbers.

---

## References

* [Aptitude](https://github.com/DKS-MANAGER/Aptitude) — Permutations and combinations
* [Aptitude-For-Placements](https://github.com/DKS-MANAGER/Aptitude-For-Placements) — Practice problems
