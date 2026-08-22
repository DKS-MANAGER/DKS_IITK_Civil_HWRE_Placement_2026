# Number System

## Concept Definitions

- **Natural Numbers ($\mathbb{N}$)**: $1, 2, 3, 4, \dots$
- **Whole Numbers ($\mathbb{W}$)**: $0, 1, 2, 3, \dots$
- **Integers ($\mathbb{Z}$)**: $\dots, -3, -2, -1, 0, 1, 2, 3, \dots$
- **Rational Numbers**: Expressible as $\frac{p}{q}$ where $q \neq 0$.
- **Irrational Numbers**: Cannot be expressed as $\frac{p}{q}$ (e.g., $\sqrt{2}, \pi$).
- **Prime Numbers**: Greater than 1 with exactly two factors: 1 and itself. (2 is the only even prime.)
- **Composite Numbers**: Greater than 1 and not prime. (1 is neither prime nor composite.)
- **Co-prime Numbers**: Two numbers whose HCF is 1.

---

## Key Formulas & Shortcuts

### Sum of Series
1. **First $n$ natural numbers**:
   $$S_n = \frac{n(n+1)}{2}$$
2. **Sum of squares**:
   $$S_n^2 = \frac{n(n+1)(2n+1)}{6}$$
3. **Sum of cubes**:
   $$S_n^3 = \left[\frac{n(n+1)}{2}\right]^2$$
4. **First $n$ odd numbers**:
   $$S_{odd} = n^2$$
5. **First $n$ even numbers**:
   $$S_{even} = n(n+1)$$

### Progressions
- **Arithmetic Progression (AP)**:
  - $n^{\text{th}}$ term: $T_n = a + (n-1)d$
  - Sum of $n$ terms: $S_n = \frac{n}{2}[2a + (n-1)d] = \frac{n}{2}(a + l)$
- **Geometric Progression (GP)**:
  - $n^{\text{th}}$ term: $T_n = a \cdot r^{n-1}$
  - Sum of $n$ terms ($r \neq 1$): $S_n = \frac{a(r^n - 1)}{r - 1}$

### Number of Factors
If $N = p^a \cdot q^b \cdot r^c \dots$:
$$\text{Total factors} = (a+1)(b+1)(c+1)\dots$$

---

## Practice Problems

### Problem 1
Find the unit digit of $(287)^{562} \times (124)^{321}$.

### Problem 2
Find the sum of all natural numbers between 100 and 300 that are exactly divisible by 4.

### Problem 3
Find the total number of factors of 360, excluding 1 and the number itself.

### Problem 4
A number divided by 899 leaves remainder 63. What is the remainder when divided by 29?

### Problem 5
Find the number of trailing zeroes in $100!$.

---

## Step-by-Step Solutions

### Solution 1
1. Unit digit of $287^{562}$: base ends in 7, cyclicity 4.
   - $562 \div 4 = 140$ remainder $2$. So unit digit $= 7^2 = 9$.
2. Unit digit of $124^{321}$: base ends in 4, cyclicity 2. Exponent is odd, so unit digit $= 4$.
3. Final unit digit $= 9 \times 4 = 36 \implies 6$.
4. **Answer**: **6**.

### Solution 2
1. First number after 100 divisible by 4 is 104. Last before 300 is 296.
2. AP: $a = 104$, $l = 296$, $d = 4$.
3. Find $n$:
   $$296 = 104 + (n-1)4 \implies 192 = (n-1)4 \implies n = 49$$
4. Sum:
   $$S_{49} = \frac{49}{2}(104 + 296) = \frac{49}{2} \times 400 = 9800$$
5. **Answer**: **9800**.

### Solution 3
1. Prime factorization: $360 = 2^3 \times 3^2 \times 5^1$.
2. Total factors $= (3+1)(2+1)(1+1) = 4 \times 3 \times 2 = 24$.
3. Excluding 1 and 360: $24 - 2 = 22$.
4. **Answer**: **22**.

### Solution 4
1. Let number $N = 899k + 63$.
2. Since $899 = 29 \times 31$, $899k$ is divisible by 29.
3. Remainder of 63 divided by 29:
   $$63 = 29 \times 2 + 5$$
4. **Answer**: **5**.

### Solution 5
1. Trailing zeroes come from factors of 10 ($2 \times 5$). Since 2 is abundant, count factors of 5.
2. Apply Legendre's formula:
   $$\left\lfloor \frac{100}{5} \right\rfloor + \left\lfloor \frac{100}{25} \right\rfloor + \left\lfloor \frac{100}{125} \right\rfloor = 20 + 4 + 0 = 24$$
3. **Answer**: **24**.

---

## References

* [Aptitude](https://github.com/DKS-MANAGER/Aptitude) — Number system
* [Aptitude-For-Placements](https://github.com/DKS-MANAGER/Aptitude-For-Placements) — Number system practice problems
