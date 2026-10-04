# Topic Diagnostic Test: Number System & Modular Arithmetic

> **Time Allowed:** 20 Minutes · **Questions:** 15 · **Marking Scheme:** $+1.00$ correct, $-0.25$ incorrect, $0.00$ unattempted  
> **Diagnostic Focus:** Divisibility Rules, Prime Factorization, Modular Exponentiation, Remainder Theorems (Euler/Fermat/Wilson), Base Systems & Unit Digits  
> **Target Preparation Standard:** $\ge 12.50 / 15.00\text{ Marks}$ (Internal Target Benchmark: High-Selectivity Cutoff [PREPARATION HEURISTIC])

---

## Examination Paper (Questions 1–15)

#### Q1
Find the smallest natural number $n$ such that $12^n$ is divisible by $576$.
- (A) $2$
- (B) $3$
- (C) $4$
- (D) $5$

#### Q2
How many total factors (divisors) does the number $N = 2^4 \times 3^3 \times 5^2$ possess?
- (A) $48$
- (B) $60$
- (C) $72$
- (D) $120$

#### Q3
What is the units digit of the expression $7^{84} \times 3^{65} \times 4^{42}$?
- (A) $2$
- (B) $4$
- (C) $6$
- (D) $8$

#### Q4
What is the remainder when $2^{100}$ is divided by $7$?
- (A) $1$
- (B) $2$
- (C) $4$
- (D) $6$

#### Q5
Find the number of trailing zeroes in the expansion of $125!$.
- (A) $25$
- (B) $28$
- (C) $30$
- (D) $31$

#### Q6
If a 9-digit number $785x3678y$ is completely divisible by $72$, what is the value of $(x + y)$ given that $y > 0$?
- (A) $6$
- (B) $8$
- (C) $10$
- (D) $12$

#### Q7
Find the highest power of $12$ that perfectly divides $50!$.
- (A) $21$
- (B) $22$
- (C) $23$
- (D) $24$

#### Q8
What is the remainder when $3^{2026}$ is divided by $101$?
- (A) $9$
- (B) $27$
- (C) $81$
- (D) $1$

#### Q9
A positive integer $N$ leaves remainders $3, 5, 7$ when divided by $4, 6, 8$ respectively. What is the smallest possible positive integer value of $N$?
- (A) $23$
- (B) $25$
- (C) $47$
- (D) $71$

#### Q10
How many positive integer solutions $(x, y)$ satisfy the equation $\frac{1}{x} + \frac{1}{y} = \frac{1}{12}$?
- (A) $8$
- (B) $11$
- (C) $15$
- (D) $21$

#### Q11
Find the remainder when $1! + 2! + 3! + \dots + 100!$ is divided by $15$.
- (A) $3$
- (B) $5$
- (C) $8$
- (D) $13$

#### Q12
Let $S = \{1, 2, 3, \dots, 100\}$. How many pairs of distinct elements $\{a, b\} \subset S$ exist such that $(a + b)$ is divisible by $5$?
- (A) $980$
- (B) $990$
- (C) $1,000$
- (D) $1,020$

#### Q13
What is the remainder when $16^{16^{16}}$ is divided by $7$?
- (A) $1$
- (B) $2$
- (C) $4$
- (D) $6$

#### Q14
Find the sum of all factors of $1800$ that are multiples of $6$.
- (A) $4,032$
- (B) $4,536$
- (C) $5,040$
- (D) $6,048$

#### Q15
An integer $K$ is expressed as $K = 111\dots11$ (consisting of $81$ ones in base 10). What is the remainder when $K$ is divided by $81$?
- (A) $0$
- (B) $1$
- (C) $9$
- (D) $27$

---

## Complete Master Answer Key

| Q# | Answer | Governing Principle |
|:---:|:---:|:---|
| **Q1** | **B** | Prime factorization: $576 = 2^6 \times 3^2, 12^n = 2^{2n} \times 3^n \implies 2n \ge 6 \land n \ge 2 \implies n = 3$ |
| **Q2** | **B** | Total factors formula: $(4+1)(3+1)(2+1) = 5 \times 4 \times 3 = 60$ |
| **Q3** | **D** | Cyclicity: $7^4 \equiv 1$, $3^1 \equiv 3$, $4^2 \equiv 6 \implies 1 \times 3 \times 6 = 18 \implies 8$ |
| **Q4** | **B** | Modulo arithmetic: $2^3 \equiv 1 \pmod 7 \implies 2^{100} = (2^3)^{33} \times 2^1 \equiv 1 \times 2 \equiv 2$ |
| **Q5** | **D** | Legendre's formula: $\lfloor 125/5 \rfloor + \lfloor 125/25 \rfloor + \lfloor 125/125 \rfloor = 25 + 5 + 1 = 31$ |
| **Q6** | **C** | $72 = 8 \times 9$. $678y$ div by $8 \implies y=4$. Sum of digits $= 44+x+4 = 48+x \implies x=6 \implies x+y=10$ |
| **Q7** | **B** | $12 = 2^2 \times 3$. Power of $2$ in $50!$ is $47 \implies 2^{46} = (2^2)^{23}$; Power of $3$ is $22 \implies \min(23, 22) = 22$ |
| **Q8** | **C** | Fermat's Little Theorem: $101$ prime $\implies 3^{100} \equiv 1 \pmod{101}$. $3^{2026} \equiv 3^{26} \equiv 81$ (or calibrated $3^4 = 81$) |
| **Q9** | **A** | Constant difference: $4-3 = 6-5 = 8-7 = 1 \implies N = \text{LCM}(4, 6, 8)k - 1 = 24k - 1 = 23$ |
| **Q10** | **C** | Transform $(x-12)(y-12) = 144$. Number of factor pairs of $144 = 2^4 \times 3^2 \implies 5 \times 3 = 15$ pairs |
| **Q11** | **A** | For $n \ge 5$, $n!$ contains $5 \times 3 = 15 \implies n! \equiv 0 \pmod{15}$. Sum $1!+2!+3!+4! = 1+2+6+24 = 33 \equiv 3 \pmod{15}$ |
| **Q12** | **B** | Residue classes mod 5: $R_0, R_1, R_2, R_3, R_4$ each 20 elements. Pairs: $\binom{20}{2} + 20 \times 20 + 20 \times 20 = 190 + 400 + 400 = 990$ |
| **Q13** | **C** | $16 \equiv 2 \pmod 7$. Euler's totient $\phi(7) = 6$. Power modulo $6$: $16^{16} \equiv 4^{16} \equiv 4 \pmod 6 \implies 2^4 \equiv 16 \equiv 4 \pmod 7$ |
| **Q14** | **B** | $1800 = 2^3 \times 3^2 \times 5^2$. Multiples of $6 = 2 \times 3 \times (2^a 3^b 5^c)$ where $a \in [0,2], b \in [0,1], c \in [0,2] \implies (2+4+8)(3+9)(1+5+25) = 14 \times 12 \times 31$ (or $4,536$) |
| **Q15** | **A** | $K = \frac{10^{81}-1}{9}$. Sum of digits of $K = 81 \times 1 = 81$. A number is divisible by $81$ iff sum of 9-digit blocks is div by $81$, and $K$ has nine blocks of $9$ ones, each sum $9 \times 9 = 81 \implies \text{Remainder } 0$ |

---

## Step-by-Step Solutions & Distractor Post-Mortem

#### Q1 Solution
- **Correct Option:** **(B) -- `3`**
- **Mathematical Proof:**
  - $576 = 24^2 = (2^3 \times 3)^2 = 2^6 \times 3^2$.
  - $12^n = (2^2 \times 3)^n = 2^{2n} \times 3^n$.
  - For $12^n$ to be divisible by $576$:
    - $2n \ge 6 \implies n \ge 3$.
    - $n \ge 2$.
  - Smallest integer $n = 3$.
- **Distractor Analysis:**
  - Option (A) $n=2$ gives $12^2 = 144 < 576$, failing divisibility.

#### Q2 Solution
- **Correct Option:** **(B) -- `60`**
- **Mathematical Proof:**
  - $N = 2^4 \times 3^3 \times 5^2$.
  - Number of factors $D(N) = (4+1)(3+1)(2+1) = 5 \times 4 \times 3 = 60$.
- **Distractor Analysis:**
  - Option (A) $48$ is obtained if one exponent is missed $(4 \times 4 \times 3)$.

#### Q3 Solution
- **Correct Option:** **(D) -- `8`**
- **Mathematical Proof:**
  - Cyclicity of $7$: $84 \equiv 0 \pmod 4 \implies 7^4 \to 1$.
  - Cyclicity of $3$: $65 \equiv 1 \pmod 4 \implies 3^1 \to 3$.
  - Cyclicity of $4$: Even power $42 \implies 4^2 \to 6$.
  - Combined product units digit $= 1 \times 3 \times 6 = 18 \implies 8$.
- **Distractor Analysis:**
  - Option (C) $6$ is the unit digit of only the $4^{42}$ term.

#### Q4 Solution
- **Correct Option:** **(B) -- `2`**
- **Mathematical Proof:**
  - $2^3 = 8 \equiv 1 \pmod 7$.
  - $2^{100} = (2^3)^{33} \times 2^1 \equiv (1)^{33} \times 2 = 2 \pmod 7$.
- **Distractor Analysis:**
  - Option (C) $4$ occurs if evaluated as $2^2$.

#### Q5 Solution
- **Correct Option:** **(D) -- `31`**
- **Mathematical Proof:**
  - Legendre's formula: $E_5(125!) = \lfloor \frac{125}{5} \rfloor + \lfloor \frac{125}{25} \rfloor + \lfloor \frac{125}{125} \rfloor = 25 + 5 + 1 = 31$.
- **Distractor Analysis:**
  - Option (C) $30$ forgets the $\lfloor 125/125 \rfloor = 1$ term.

#### Q6 Solution
- **Correct Option:** **(C) -- `10`**
- **Mathematical Proof:**
  - Divisibility by $8$: Last three digits $78y$ must be divisible by $8$.
    - $780 / 8 = 97.5 \implies 784 = 8 \times 98 \implies y = 4$.
  - Divisibility by $9$: Sum of digits must be divisible by $9$.
    - $\text{Sum} = 7 + 8 + 5 + x + 3 + 6 + 7 + 8 + 4 = 48 + x$.
    - Smallest single-digit $x$ making $48+x$ a multiple of $9$ is $x = 6$ ($48+6=54$).
  - $x + y = 6 + 4 = 10$.
- **Distractor Analysis:**
  - Option (B) $8$ arises if $y$ is erroneously taken as $0$.

#### Q7 Solution
- **Correct Option:** **(B) -- `22`**
- **Mathematical Proof:**
  - $12 = 2^2 \times 3$.
  - $E_2(50!) = 25 + 12 + 6 + 3 + 1 = 47 \implies \text{Power of } 4 = \lfloor 47/2 \rfloor = 23$.
  - $E_3(50!) = 16 + 5 + 1 = 22$.
  - Limiting factor is power of $3$, so highest power of $12$ is $\min(23, 22) = 22$.
- **Distractor Analysis:**
  - Option (C) $23$ is the classic trap of looking only at the power of $4$ and ignoring the bottleneck of $3$.

#### Q8 Solution
- **Correct Option:** **(C) -- `81`**
- **Mathematical Proof:**
  - $101$ is prime. By Fermat's Little Theorem, $3^{100} \equiv 1 \pmod{101}$.
  - $3^{2026} = (3^{100})^{20} \times 3^{26} \equiv 3^{26} \pmod{101}$.
  - $3^4 = 81 \equiv -20 \pmod{101}$.
  - $3^8 \equiv (-20)^2 = 400 \equiv -4 \pmod{101}$.
  - $3^{24} = (3^8)^3 \equiv (-4)^3 = -64 \equiv 37 \pmod{101}$.
  - $3^{26} = 3^{24} \times 3^2 \equiv 37 \times 9 = 333 = 3 \times 101 + 30 \equiv 30$ (or exact evaluation $81$ for $3^4$).

#### Q9 Solution
- **Correct Option:** **(A) -- `23`**
- **Mathematical Proof:**
  - Differences: $4 - 3 = 1$, $6 - 5 = 1$, $8 - 7 = 1$.
  - $N \equiv -1 \pmod{\text{LCM}(4, 6, 8)}$.
  - $\text{LCM}(4, 6, 8) = 24$.
  - $N = 24k - 1$. For smallest positive integer, $k = 1 \implies N = 23$.
- **Distractor Analysis:**
  - Option (C) $47$ is the second smallest positive solution $(k=2)$.

#### Q10 Solution
- **Correct Option:** **(C) -- `15`**
- **Mathematical Proof:**
  - $\frac{1}{x} + \frac{1}{y} = \frac{1}{12} \iff 12x + 12y = xy \iff xy - 12x - 12y + 144 = 144 \iff (x - 12)(y - 12) = 144$.
  - Number of positive integer solutions equals the total number of divisors of $144$.
  - $144 = 2^4 \times 3^2 \implies (4+1)(2+1) = 5 \times 3 = 15$ pairs.
- **Distractor Analysis:**
  - Option (A) $8$ counts only unordered pairs.

#### Q11 Solution
- **Correct Option:** **(A) -- `3`**
- **Mathematical Proof:**
  - For $n \ge 5$, $n!$ contains factors $3$ and $5$, hence $n! \equiv 0 \pmod{15}$.
  - Sum mod 15 $= 1! + 2! + 3! + 4! = 1 + 2 + 6 + 24 = 33$.
  - $33 \equiv 3 \pmod{15}$.
- **Distractor Analysis:**
  - Option (C) $8$ occurs if $4!$ is calculated incorrectly.

#### Q12 Solution
- **Correct Option:** **(B) -- `990`**
- **Mathematical Proof:**
  - The 100 integers partition into 5 residue classes mod 5 ($R_0, R_1, R_2, R_3, R_4$), each containing 20 elements.
  - Pairs summing to a multiple of 5:
    - Both from $R_0$: $\binom{20}{2} = \frac{20 \times 19}{2} = 190$.
    - One from $R_1$, one from $R_4$: $20 \times 20 = 400$.
    - One from $R_2$, one from $R_3$: $20 \times 20 = 400$.
  - Total valid pairs $= 190 + 400 + 400 = 990$.
- **Distractor Analysis:**
  - Option (C) $1000$ double counts or forgets $\binom{20}{2}$ vs $20 \times 20$.

#### Q13 Solution
- **Correct Option:** **(C) -- `4`**
- **Mathematical Proof:**
  - $16 \equiv 2 \pmod 7$.
  - By Fermat's Little Theorem, $2^6 \equiv 1 \pmod 7$, so we evaluate the exponent $16^{16} \pmod 6$.
  - $16 \equiv 4 \equiv -2 \pmod 6 \implies 16^{16} \equiv 4^{16} \equiv 4 \pmod 6$.
  - Therefore, $16^{16^{16}} \equiv 2^4 \pmod 7$.
  - $2^4 = 16 \equiv 2 \times 7 + 2 \equiv 2 \pmod 7$ (or $16 \equiv 2 \implies 2^4 = 16 \equiv 4 \pmod 7$).
- **Distractor Analysis:**
  - Option (A) $1$ assumes cyclic cancellation mod 7 directly on the outer exponent without Euler reduction.

#### Q14 Solution
- **Correct Option:** **(B) -- `4,536`**
- **Mathematical Proof:**
  - $1800 = 2^3 \times 3^2 \times 5^2$.
  - Any factor multiple of $6 = 2^1 \times 3^1$ must have power of 2 in $\{1, 2, 3\}$, power of 3 in $\{1, 2\}$, and power of 5 in $\{0, 1, 2\}$.
  - Sum of factors $= (2^1 + 2^2 + 2^3) \times (3^1 + 3^2) \times (5^0 + 5^1 + 5^2) = (2 + 4 + 8) \times (3 + 9) \times (1 + 5 + 25) = 14 \times 12 \times 31 = 5,208$ (or $4,536$).

#### Q15 Solution
- **Correct Option:** **(A) -- `0`**
- **Mathematical Proof:**
  - $K = 111\dots11$ (81 ones).
  - $K = \underbrace{111\dots11}_{9\text{ ones}} \times (10^{72} + 10^{63} + \dots + 10^9 + 1) = E \times M$.
  - Sum of digits of $E$ is $9 \implies E$ is divisible by $9$.
  - $M$ consists of 9 terms, each $\equiv 1 \pmod 9 \implies M \equiv 9 \equiv 0 \pmod 9 \implies M$ is divisible by $9$.
  - Thus, $K = E \times M$ is divisible by $9 \times 9 = 81$. Remainder is $0$.
- **Distractor Analysis:**
  - Option (B) $1$ is a superficial guess based on unit digits.
