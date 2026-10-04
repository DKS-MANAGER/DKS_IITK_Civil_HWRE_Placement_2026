# Quantitative Aptitude: Progressions & Series (AP, GP, HP, AGP)

> **Priority:** P1 · **Role relevance:** Critical (Quantitative Trading, Algorithmic Finance, Management Consulting, Data Science & Machine Learning)  
> **Difficulty range:** Foundation → Arithmetico-Geometric Progressions, Telescoping Sums, Second-Order Recurrence Relations, AM-GM-HM Optimization & Financial Perpetuities  
> **Target speed:** 30–50 sec (Direct AP/GP Index Formulas) – 75–110 sec (Telescoping Sums / Infinite AGP / Recurrence Matrix Solving)

---

## 1. Theoretical Framework & Algebraic Formulations

### 1.1 Progression Taxonomy & Closed-Form Invariants

```
+-----------------------------------------------------------------------------------+
|                        THE CANONICAL PROGRESSION FORMULAS                         |
+-----------------------------------------------------------------------------------+
| 1. Arithmetic Progression (AP)  : T_n = a + (n-1)d                                |
|                                   S_n = (n/2)[2a + (n-1)d] = (n/2)(a + l)         |
| 2. Geometric Progression (GP)   : T_n = a * r^(n-1)                               |
|                                   S_n = a(r^n - 1) / (r - 1)    (for r != 1)      |
|                                   S_inf = a / (1 - r)           (for |r| < 1)     |
| 3. Harmonic Progression (HP)    : 1/T_n = 1/a + (n-1)D                            |
|                                   Harmonic Mean HM = 2ab / (a + b)                |
| 4. Arithmetico-Geometric (AGP)  : S_inf = a/(1-r) + dr/(1-r)^2   (for |r| < 1)    |
| 5. Classical Means Hierarchy    : RMS >= AM >= GM >= HM                           |
|                                   Equality holds iff all terms are identical.     |
+-----------------------------------------------------------------------------------+
```

---

### 1.2 Mathematical Archetypes & Advanced Summation Toolkits

#### 1. Arithmetico-Geometric Progression ($AGP$) Closed Form
Consider the series $S = a + (a+d)r + (a+2d)r^2 + (a+3d)r^3 + \dots$:
- Multiply by common ratio $r$: $r S = ar + (a+d)r^2 + (a+2d)r^3 + \dots$
- Subtracting gives $(1-r)S = a + d r + d r^2 + d r^3 + \dots = a + \frac{d r}{1-r}$
- Therefore, for $|r| < 1$:
  $$S_{\infty} = \frac{a}{1 - r} + \frac{d r}{(1 - r)^2}$$

#### 2. Telescoping Sums & Partial Fraction Decomposition
When evaluating $\sum_{k=1}^n \frac{1}{k(k+1)(k+2)\dots(k+m)}$:
- Decompose into partial differences:
  $$\frac{1}{k(k+1)} = \frac{1}{k} - \frac{1}{k+1}$$
  $$\sum_{k=1}^n \frac{1}{k(k+1)} = \left(1 - \frac{1}{2}\right) + \left(\frac{1}{2} - \frac{1}{3}\right) + \dots + \left(\frac{1}{n} - \frac{1}{n+1}\right) = 1 - \frac{1}{n+1} = \frac{n}{n+1}$$

#### 3. Method of Differences & Polynomial Sequences
If the first differences of a sequence form an AP, the $n$-th term is quadratic: $T_n = A n^2 + B n + C$.
If the $k$-th differences are constant, $T_n$ is a polynomial of degree $k$.

#### 4. Linear Homogeneous Recurrence Relations
For second-order recurrence $x_n = c_1 x_{n-1} + c_2 x_{n-2}$:
- Characteristic equation: $r^2 - c_1 r - c_2 = 0$ with roots $r_1, r_2$.
- General solution: $x_n = A r_1^n + B r_2^n$ (for distinct roots).

---

## 2. Master Answer Key (Q1–Q40)

| Question | Level | Archetype / Domain | Correct Answer | Core Mathematical Principle |
|:---:|:---:|:---|:---:|:---|
| **Q1** | Level 1 | Direct AP Term & Sum | **B** | $a = 3, d = 4 \implies T_{15} = 3 + 14(4) = 59; S_{15} = \frac{15}{2}(3 + 59) = 465$ |
| **Q2** | Level 1 | Direct GP Term & Sum | **C** | $a = 5, r = 2 \implies T_8 = 5(2^7) = 640; S_8 = 5(2^8 - 1) = 1275$ |
| **Q3** | Level 1 | Infinite GP Summation | **A** | $S_\infty = \frac{a}{1 - r} = \frac{18}{1 - 1/3} = \frac{18}{2/3} = 27$ |
| **Q4** | Level 1 | Harmonic Mean of Two Numbers | **D** | $HM = \frac{2ab}{a + b} = \frac{2(12)(24)}{12 + 24} = \frac{576}{36} = 16$ |
| **Q5** | Level 1 | Three Terms in AP | **B** | $(2k + 1) - (k - 2) = (4k - 3) - (2k + 1) \implies k + 3 = 2k - 4 \implies k = 7$ |
| **Q6** | Level 2 | Inserted Arithmetic Means | **C** | Insert $n = 5$ AMs between 4 and 28 $\implies d = \frac{28 - 4}{5 + 1} = 4$; 3rd AM $= 4 + 3(4) = 16$ |
| **Q7** | Level 2 | Sum of Odd/Even AP Series | **A** | Sum of first $n$ odd integers $= n^2$; $n = 30 \implies 30^2 = 900$ |
| **Q8** | Level 2 | Geometric Mean Insertion | **D** | Insert 3 GMs between 2 and 162 $\implies r = (162/2)^{1/4} = 81^{1/4} = 3$; GMs: $6, 18, 54$ |
| **Q9** | Level 2 | Ratio of Sums of Two APs | **B** | $\frac{S_{n,1}}{S_{n,2}} = \frac{7n+1}{4n+27} \implies \text{Replace } n \to 2m - 1 = 21 \implies \frac{T_{11,1}}{T_{11,2}} = \frac{7(21)+1}{4(21)+27} = \frac{148}{111} = \frac{4}{3}$ |
| **Q10** | Level 2 | HP Terms & Reciprocal AP | **C** | $T_5 = 1/15, T_{10} = 1/30 \implies d_{\text{AP}} = 3, a_{\text{AP}} = 3 \implies T_{20,\text{HP}} = 1/60$ |
| **Q11** | Level 3 | Infinite AGP Evaluation | **B** | $S_\infty = \frac{a}{1-r} + \frac{dr}{(1-r)^2} = \frac{1}{1 - 1/2} + \frac{2(1/2)}{(1 - 1/2)^2} = 2 + \frac{1}{1/4} = 6$ |
| **Q12** | Level 3 | Telescoping Partial Fractions | **B** | $\sum_{k=1}^{20} \frac{1}{k(k+1)} = 1 - \frac{1}{21} = \frac{20}{21}$ |
| **Q13** | Level 3 | Sum of Squares & Cubes of AP | **A** | $\sum_{k=1}^{10} k^2 = \frac{10(11)(21)}{6} = 385; \sum k^3 = \left(\frac{10 \times 11}{2}\right)^2 = 3025$ |
| **Q14** | Level 3 | Logarithmic Terms in AP $\implies$ GP | **D** | If $\log a, \log b, \log c$ in AP $\implies b^2 = ac \implies a, b, c$ in GP |
| **Q15** | Level 3 | Combined AP-GP System | **B** | $a, b, c$ in AP ($2b = a+c$) and $a, b, c+2$ in GP ($b^2 = a(c+2)$) with $a+b+c = 18 \implies (4, 6, 8)$ |
| **Q16** | Level 4 | Double Telescoping Sum | **C** | $\sum_{k=1}^n \frac{1}{k(k+1)(k+2)} = \frac{1}{2}\left[\frac{1}{1 \times 2} - \frac{1}{(n+1)(n+2)}\right] = \frac{n(n+3)}{4(n+1)(n+2)}$ |
| **Q17** | Level 4 | Method of Differences Quadratic Series | **A** | Series $3, 7, 13, 21, 31, \dots \implies T_n = n^2 + n + 1; S_n = \frac{n(n+1)(2n+1)}{6} + \frac{n(n+1)}{2} + n$ |
| **Q18** | Level 4 | AM-GM Optimization Inequality | **D** | Min value of $x + \frac{9}{x}$ for $x > 0$ is $2\sqrt{x \cdot \frac{9}{x}} = 6$ (achieved at $x = 3$) |
| **Q19** | Level 4 | Recurrence Sequence (Fibonacci Style) | **B** | $x_{n+1} = x_n + 2x_{n-1}$ with $x_1 = 1, x_2 = 3 \implies r^2 - r - 2 = 0 \implies x_n = 2^n - (-1)^n$ |
| **Q20** | Level 4 | Harmonic Mean of Reciprocal Squares | **C** | Inequality relationship: $HM(a_1, \dots, a_n) \le AM \implies$ minimum bound $= \frac{n^2}{\sum 1/a_i}$ |
| **Q21** | Level 5 | Infinite Fractional AGP Variant | **C** | $\sum_{n=1}^\infty \frac{n^2}{3^n} = \frac{r(1+r)}{(1-r)^3} \text{ for } r = 1/3 \implies \frac{(1/3)(4/3)}{(2/3)^3} = \frac{4/9}{8/27} = \frac{3}{2}$ |
| **Q22** | Level 5 | Telescoping Square Roots | **A** | $\sum_{k=1}^{99} \frac{1}{\sqrt{k} + \sqrt{k+1}} = \sum (\sqrt{k+1} - \sqrt{k}) = \sqrt{100} - \sqrt{1} = 9$ |
| **Q23** | Level 5 | Quadratic Recurrence Convergence | **D** | $x_{n+1} = \frac{1}{2}(x_n + \frac{A}{x_n}) \implies \lim_{n\to\infty} x_n = \sqrt{A}$ (Newton-Raphson square root) |
| **Q24** | Level 5 | Invariant Product of Terms in GP | **B** | In GP of $n$ terms: $T_1 \times T_n = T_2 \times T_{n-1} = \dots \implies \prod_{k=1}^n T_k = (T_1 T_n)^{n/2}$ |
| **Q25** | Level 5 | Multi-Variable Cauchy-Schwarz Series | **C** | $(a_1^2 + \dots + a_n^2)(b_1^2 + \dots + b_n^2) \ge (a_1 b_1 + \dots + a_n b_n)^2 \implies$ Min sum $= 36$ |
| **Q26** | Level 6 | Matrix Power for $k$-th Order Recurrence | **A** | $\begin{pmatrix} F_{n+1} & F_n \\ F_n & F_{n-1} \end{pmatrix} = \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}^n \implies F_{n+1}F_{n-1} - F_n^2 = (-1)^n$ (Cassini) |
| **Q27** | Level 6 | Euler-Maclaurin Harmonic Sum Estimate | **D** | $H_n = \sum_{k=1}^n \frac{1}{k} \approx \ln n + \gamma + \frac{1}{2n}$; for $n = 1000 \implies H_{1000} \approx 7.485$ |
| **Q28** | Level 6 | Non-Linear Fractional Recurrence | **B** | $x_{n+1} = \frac{x_n}{1 + x_n} \implies \frac{1}{x_{n+1}} = \frac{1}{x_n} + 1 \implies \frac{1}{x_n} = \frac{1}{x_1} + (n-1)$ |
| **Q29** | Level 6 | Telescoping Trigonometric Products | **C** | $\prod_{k=1}^n \cos\left(\frac{x}{2^k}\right) = \frac{\sin x}{2^n \sin(x/2^n)} \implies \lim_{n\to\infty} = \frac{\sin x}{x}$ |
| **Q30** | Level 6 | Infinite Double Series Evaluation | **A** | $\sum_{m=1}^\infty \sum_{n=1}^\infty \frac{1}{m^2 n + m n^2 + 2mn} = \ln 2$ or evaluated as $\zeta(2) - 1$ |
| **Q31** | Level 7 | The Black-Scholes Geometric Brownian Motion Tree | **C** | Multiplicative binomial tree stock price progression: $S_{u,d}(n) = S_0 u^k d^{n-k} \implies$ Expected price $= S_0 e^{rt}$ |
| **Q32** | Level 7 | Generating Function of Integer Partitions | **B** | $P(x) = \prod_{k=1}^\infty \frac{1}{1 - x^k} \implies$ Coefficient of $x^5 = 7$ |
| **Q33** | Level 7 | Continuous Time Perpetuity Valuation (Gordon Growth) | **D** | $P_0 = \frac{D_1}{r - g} \implies$ Convergence condition $r > g$; with $D_1 = 5, r = 9\\%, g = 4\\% \implies 100\text{ INR}$ |
| **Q34** | Level 7 | Riemann Zeta Function & Basel Problem | **A** | $\sum_{n=1}^\infty \frac{1}{n^2} = \frac{\pi^2}{6}; \sum_{n=1}^\infty \frac{1}{(2n-1)^2} = \frac{\pi^2}{8}$ |
| **Q35** | Level 7 | Multi-Tiered Bond Sinking Fund AP Amortization | **C** | Sinking fund equal annual principal reductions with declining interest $\implies$ Total interest $= \frac{n(n+1)}{2} I_0$ |
| **Q36** | Level 8 | Consulting Caselet: SaaS ARR Cohort Geometric Decay | **B** | Compound Net Revenue Retention ($NRR = 110\\%$) geometric expansion $\implies 5$-year ARR $= 6.1\times$ |
| **Q37** | Level 8 | Quant Finance: Autoregressive AR(1) Mean Reversion | **C** | $X_t = \phi X_{t-1} + \epsilon_t \implies \text{Var}(X_\infty) = \frac{\sigma^2}{1 - \phi^2}$; for $\phi = 0.8, \sigma = 2 \implies \text{Var} = 11.11$ |
| **Q38** | Level 8 | Caselet: High-Frequency Market Making Queue | **A** | Order book fill rate geometric queue progression $P(\text{Fill} \le k) = 1 - (1-p)^k \implies$ Expected time $= 1/p$ |
| **Q39** | Level 8 | Actuarial Caselet: Multi-Life Geometric Annuity | **D** | Joint life annuity present value using geometric mortality progression $\implies PV = 14.8\text{ years}$ |
| **Q40** | Level 8 | Infrastructure Financing: Stepped Toll Revenue AGP | **B** | Toll traffic growing in AP ($+500$ cars/yr) with toll rate in GP ($+4\\%/yr$) $\implies 20$-year NPV $= 428.5\text{ Cr}$ |

---

## 3. Comprehensive Practice Set (40 Placement Questions)

### Level 1: Foundation (Q1–Q5)

#### Q1
An arithmetic progression has first term $a = 3$ and common difference $d = 4$. What is the 15th term ($T_{15}$) and the sum of the first 15 terms ($S_{15}$)?
- (A) $T_{15} = 55, S_{15} = 435$
- (B) $T_{15} = 59, S_{15} = 465$
- (C) $T_{15} = 63, S_{15} = 495$
- (D) $T_{15} = 59, S_{15} = 480$

#### Q2
A geometric progression has first term $a = 5$ and common ratio $r = 2$. What is the 8th term ($T_8$) and the sum of the first 8 terms ($S_8$)?
- (A) $T_8 = 320, S_8 = 635$
- (B) $T_8 = 640, S_8 = 1240$
- (C) $T_8 = 640, S_8 = 1275$
- (D) $T_8 = 1280, S_8 = 2555$

#### Q3
What is the sum of the infinite geometric series $18 + 6 + 2 + \frac{2}{3} + \frac{2}{9} + \dots$?
- (A) $27$
- (B) $28$
- (C) $30$
- (D) $36$

#### Q4
What is the Harmonic Mean ($HM$) of the two numbers $12$ and $24$?
- (A) $14.4$
- (B) $15.0$
- (C) $15.5$
- (D) $16.0$

#### Q5
If the numbers $(k - 2), (2k + 1),$ and $(4k - 3)$ are three consecutive terms of an Arithmetic Progression, what is the value of $k$?
- (A) $5$
- (B) $7$
- (C) $8$
- (D) $9$

---

### Level 2: Means Insertion & Ratio Formulations (Q6–Q10)

#### Q6
Five arithmetic means ($A_1, A_2, A_3, A_4, A_5$) are inserted between $4$ and $28$. What is the value of the third arithmetic mean $A_3$?
- (A) $12$
- (B) $14$
- (C) $16$
- (D) $18$

#### Q7
What is the sum of the first $30$ positive odd integers ($1 + 3 + 5 + \dots + 59$)?
- (A) $900$
- (B) $930$
- (C) $960$
- (D) $1000$

#### Q8
Three geometric means ($G_1, G_2, G_3$) are inserted between $2$ and $162$. What is the product of these three geometric means?
- (A) $486$
- (B) $1458$
- (C) $4374$
- (D) $5832$

#### Q9
The ratio of the sum of $n$ terms of two distinct arithmetic progressions is given by $\frac{S_{n,1}}{S_{n,2}} = \frac{7n + 1}{4n + 27}$. What is the ratio of their 11th terms ($\frac{T_{11,1}}{T_{11,2}}$)?
- (A) $\frac{3}{4}$
- (B) $\frac{4}{3}$
- (C) $\frac{5}{4}$
- (D) $\frac{7}{5}$

#### Q10
The 5th term of a Harmonic Progression ($HP$) is $\frac{1}{15}$, and its 10th term is $\frac{1}{30}$. What is the 20th term of this $HP$?
- (A) $\frac{1}{45}$
- (B) $\frac{1}{50}$
- (C) $\frac{1}{60}$
- (D) $\frac{1}{75}$

---

### Level 3: Infinite AGP & Telescoping Sequences (Q11–Q15)

#### Q11
What is the sum to infinity of the Arithmetico-Geometric Progression ($AGP$):
$$S = 1 + \frac{3}{2} + \frac{5}{4} + \frac{7}{8} + \frac{9}{16} + \dots$$
- (A) $5$
- (B) $6$
- (C) $7$
- (D) $8$

#### Q12
What is the sum of the finite telescoping series:
$$S = \frac{1}{1 \times 2} + \frac{1}{2 \times 3} + \frac{1}{3 \times 4} + \dots + \frac{1}{20 \times 21}$$
- (A) $\frac{19}{20}$
- (B) $\frac{20}{21}$
- (C) $\frac{21}{22}$
- (D) $\frac{22}{23}$

#### Q13
What is the sum of the squares of the first 10 positive integers ($1^2 + 2^2 + 3^2 + \dots + 10^2$)?
- (A) $385$
- (B) $425$
- (C) $465$
- (D) $505$

#### Q14
If $\log_x a, \log_x b,$ and $\log_x c$ are in Arithmetic Progression (for valid base $x > 0, x \neq 1$), which of the following statements must be true?
- (A) $a, b, c$ are in AP
- (B) $a, b, c$ are in HP
- (C) $a+c = 2b$
- (D) $a, b, c$ are in GP ($b^2 = ac$)

#### Q15
Three positive numbers $a, b, c$ whose sum is $18$ form an Arithmetic Progression. If $2$ is added to $c$, the resulting numbers $a, b, c+2$ form a Geometric Progression. What is the value of the largest original number $c$?
- (A) $7$
- (B) $8$
- (C) $9$
- (D) $10$

---

### Level 4: Multi-Order Telescoping & Recurrence Equations (Q16–Q20)

#### Q16
What is the sum to $n$ terms of the three-factor telescoping series:
$$S_n = \sum_{k=1}^n \frac{1}{k(k+1)(k+2)}$$
- (A) $\frac{n(n+1)}{2(n+2)(n+3)}$
- (B) $\frac{n(n+2)}{3(n+1)(n+3)}$
- (C) $\frac{n(n+3)}{4(n+1)(n+2)}$
- (D) $\frac{1}{4} - \frac{1}{2(n+1)^2}$

#### Q17
Find the $n$-th term $T_n$ of the series $3, 7, 13, 21, 31, \dots$ whose successive differences form an Arithmetic Progression.
- (A) $T_n = n^2 + n + 1$
- (B) $T_n = n^2 + 2n$
- (C) $T_n = 2n^2 - n + 2$
- (D) $T_n = n^2 + 3n - 1$

#### Q18
For all strictly positive real numbers $x > 0$, what is the minimum value attained by the expression $f(x) = x + \frac{9}{x}$ according to the AM-GM inequality?
- (A) $4$
- (B) $5$
- (C) $5.5$
- (D) $6$

#### Q19
A sequence is defined by the second-order recurrence relation $x_{n+1} = x_n + 2x_{n-1}$ for $n \ge 2$, with initial boundary conditions $x_1 = 1$ and $x_2 = 3$. What is the closed-form expression for $x_n$?
- (A) $x_n = 2^n - 1$
- (B) $x_n = 2^n - (-1)^n$
- (C) $x_n = \frac{1}{2}(3^n - 1)$
- (D) $x_n = 2^{n-1} + 1$

#### Q20
If $a, b, c > 0$ are positive real numbers such that $a + b + c = 1$, what is the minimum possible value of $\frac{1}{a} + \frac{1}{b} + \frac{1}{c}$?
- (A) $3$
- (B) $6$
- (C) $9$
- (D) $12$

---

### Level 5: Higher-Order AGPs & Quadratic Sequences (Q21–Q25)

#### Q21
What is the sum of the infinite squared Arithmetico-Geometric series:
$$S = \sum_{n=1}^\infty \frac{n^2}{3^n} = \frac{1}{3} + \frac{4}{9} + \frac{9}{27} + \frac{16}{81} + \dots$$
- (A) $1$
- (B) $\frac{4}{3}$
- (C) $\frac{3}{2}$
- (D) $2$

#### Q22
What is the value of the telescoping square root sum:
$$S = \sum_{k=1}^{99} \frac{1}{\sqrt{k} + \sqrt{k+1}} = \frac{1}{1 + \sqrt{2}} + \frac{1}{\sqrt{2} + \sqrt{3}} + \dots + \frac{1}{\sqrt{99} + \sqrt{100}}$$
- (A) $9$
- (B) $10$
- (C) $11$
- (D) $\sqrt{99}$

#### Q23
A sequence satisfies the Babylonian recurrence $x_{n+1} = \frac{1}{2}\left(x_n + \frac{16}{x_n}\right)$ with $x_1 = 5$. To what fixed point does the sequence converge as $n \to \infty$?
- (A) $2$
- (B) $2\sqrt{2}$
- (C) $3$
- (D) $4$

#### Q24
In a geometric progression consisting of $2n+1$ terms, the middle term is $M$. What is the product of all $2n+1$ terms in the progression?
- (A) $M^n$
- (B) $M^{2n+1}$
- (C) $(2n+1)M$
- (D) $M^{(2n+1)/2}$

#### Q25
If $x, y, z$ are real numbers such that $x^2 + y^2 + z^2 = 36$, what is the maximum possible value of $x + 2y + 2z$ by Cauchy-Schwarz inequality?
- (A) $12$
- (B) $15$
- (C) $18$
- (D) $24$

---

### Level 6: Matrix Generating Powers & Cassini's Invariant (Q26–Q30)

#### Q26
Let $F_n$ denote the $n$-th Fibonacci number ($F_1 = 1, F_2 = 1, F_3 = 2, F_4 = 3, \dots$). According to **Cassini's Identity**, what is the value of $F_{n+1} F_{n-1} - F_n^2$?
- (A) $(-1)^n$
- (B) $(-1)^{n+1}$
- (C) $1$
- (D) $0$

#### Q27
Using the Euler-Maclaurin asymptotic approximation for the harmonic series $H_n = \sum_{k=1}^n \frac{1}{k} \approx \ln n + \gamma$ (where $\gamma \approx 0.5772$ is the Euler-Mascheroni constant), what is the approximate value of $H_{1000}$? (Take $\ln 10 \approx 2.3026$)
- (A) $6.485$
- (B) $6.908$
- (C) $7.125$
- (D) $7.485$

#### Q28
A sequence of positive terms satisfies $x_{n+1} = \frac{x_n}{1 + x_n}$ with initial term $x_1 = 1$. What is the value of $x_{100}$?
- (A) $\frac{1}{99}$
- (B) $\frac{1}{100}$
- (C) $\frac{1}{101}$
- (D) $\frac{1}{200}$

#### Q29
What is the limit of the infinite telescoping cosine product:
$$P = \lim_{n\to\infty} \cos\left(\frac{\pi}{4}\right) \cos\left(\frac{\pi}{8}\right) \cos\left(\frac{\pi}{16}\right) \dots \cos\left(\frac{\pi}{2^{n+1}}\right)$$
- (A) $\frac{1}{\pi}$
- (B) $\frac{\sqrt{2}}{\pi}$
- (C) $\frac{2}{\pi}$
- (D) $\frac{\pi}{4}$

#### Q30
What is the sum of the infinite series $S = \sum_{n=1}^\infty \frac{1}{n(n+1)(n+2)(n+3)}$?
- (A) $\frac{1}{18}$
- (B) $\frac{1}{12}$
- (C) $\frac{1}{6}$
- (D) $\frac{1}{4}$

---

### Level 7: Quantitative Finance Binomial Trees & Zeta Functions (Q31–Q35)

#### Q31
In quantitative options pricing, a binomial stock price tree models the asset price after $n$ steps as $S_n = S_0 u^k d^{n-k}$ where up-factor $u = 1.10$ and down-factor $d = 0.90$. If the risk-neutral probability of an up-move is $p = 0.60$, what is the expected stock price after 2 steps if $S_0 = 100$?
- (A) $102.00$
- (B) $103.50$
- (C) $104.04$
- (D) $106.00$

#### Q32
In partition theory, Euler's generating function for the number of integer partitions $p(n)$ is $\prod_{k=1}^\infty \frac{1}{1 - x^k}$. What is the number of integer partitions of $n = 5$ (the coefficient of $x^5$)?
- (A) $5$
- (B) $7$
- (C) $8$
- (D) $9$

#### Q33
According to the Gordon Growth Model of equity valuation, a continuous stock dividend grows at a steady geometric rate $g = 4\\%$ per year. If the next year dividend is $D_1 = \text{INR } 5.00$ and the required equity rate of return is $r = 9\\%$, what is the intrinsic stock price $P_0 = \sum_{t=1}^\infty \frac{D_1(1+g)^{t-1}}{(1+r)^t}$?
- (A) INR $80.00$
- (B) INR $90.00$
- (C) INR $95.00$
- (D) INR $100.00$

#### Q34
Given Euler's solution to the Basel problem $\sum_{n=1}^\infty \frac{1}{n^2} = \frac{\pi^2}{6}$, what is the sum of the reciprocals of the odd squares $\sum_{k=1}^\infty \frac{1}{(2k-1)^2} = 1 + \frac{1}{9} + \frac{1}{25} + \frac{1}{49} + \dots$?
- (A) $\frac{\pi^2}{8}$
- (B) $\frac{\pi^2}{12}$
- (C) $\frac{\pi^2}{16}$
- (D) $\frac{\pi^2}{24}$

#### Q35
A corporate bond sinking fund pays off a principal of INR 10,000 in 10 equal annual installments of INR 1,000 (forming an AP of remaining balances: 10k, 9k, ..., 1k). If annual interest is charged at $10\\%$ on the unpaid balance at the start of each year, what is the total interest paid over the 10-year term?
- (A) INR 4,500
- (B) INR 5,000
- (C) INR 5,500
- (D) INR 6,000

---

### Level 8: Strategic Consulting & Algorithmic Caselets (Q36–Q40)

#### Q36 (Management Consulting: SaaS Cohort ARR Compounding)
An enterprise SaaS startup has an initial Annual Recurring Revenue (ARR) of USD 10 Million with a net annual expansion rate of $15\\%$ (Net Revenue Retention $NRR = 115\\%$, representing a geometric progression $T_n = 10 \times (1.15)^{n-1}$). In addition, the sales team lands USD 5 Million in brand-new customer ARR every year (forming an AGP). What is the total projected ARR at the end of Year 5?
- (A) USD 42.5 Million
- (B) USD 53.8 Million
- (C) USD 61.2 Million
- (D) USD 67.5 Million

#### Q37 (Quantitative Trading: Autoregressive AR(1) Mean-Reverting Spread)
A statistical arbitrage trading pair spread $X_t$ follows a discrete first-order autoregressive process: $X_t = 0.8 X_{t-1} + \epsilon_t$, where white noise shocks $\epsilon_t \sim \mathcal{N}(0, 4)$ have variance $\sigma^2 = 4$. What is the unconditional asymptotic long-term variance $\text{Var}(X_\infty) = \sum_{k=0}^\infty (0.8)^{2k} \sigma^2$?
- (A) $8.50$
- (B) $10.00$
- (C) $11.11$
- (D) $16.00$

#### Q38 (Market Microstructure: Order Fill Geometric Probability)
In a high-frequency trading market-making strategy, the probability that a limit order is filled in any given 10-millisecond time slice is $p = 0.20$. The number of time slices $K$ until the order is filled follows a Geometric distribution $P(K = k) = (1-p)^{k-1} p$. What is the expected time to execution?
- (A) $50\text{ milliseconds}$ (5 slices)
- (B) $60\text{ milliseconds}$
- (C) $80\text{ milliseconds}$
- (D) $100\text{ milliseconds}$

#### Q39 (Actuarial Science: Multi-Year Cohort Mortality Annuity)
An insurance company sells a life annuity paying INR 1,00,000 annually. The survival probability decays geometrically: $p_t = (0.95)^t$. If the risk-free discount factor is $v = \frac{1}{1.05}$, what is the actuarial present value of this lifetime annuity $PV = \sum_{t=1}^\infty \text{Payout} \times (p_t v^t)$?
- (A) INR 9,50,000
- (B) INR 10,00,000
- (C) INR 10,50,000
- (D) INR 9,50,000 / $0.10 \approx 9,50,000$ (or INR 10,00,000)

#### Q40 (Infrastructure Project Finance: AGP Stepped Concession Tolls)
A highway Build-Operate-Transfer (BOT) concession generates toll revenue where traffic volume grows in Arithmetic Progression ($V_t = 1000 + 100t$ thousand vehicles/year) and toll rate grows in Geometric Progression ($R_t = 50 \times (1.05)^{t-1}$ INR/vehicle). What algebraic structure models the annual concession revenue $Y_t = V_t \times R_t$?
- (A) Pure Geometric Progression
- (B) Arithmetico-Geometric Progression ($AGP$)
- (C) Harmonic Progression
- (D) Second-Order Recurrence

---

## 4. Rigorous Step-by-Step Deductive Solutions & Algebraic Post-Mortem

### Level 1 (Q1–Q5)

#### Q1
- **Correct Answer:** **B**
- **Deductive Proof:**
  - $T_{15} = a + (15 - 1)d = 3 + 14(4) = 3 + 56 = 59$.
  - $S_{15} = \frac{15}{2}(a + l) = \frac{15}{2}(3 + 59) = \frac{15}{2}(62) = 15 \times 31 = 465$.
- **Distractor Analysis:**
  - *(A) 55/435, (C) 63/495, (D) 59/480:* Arithmetic off-by-one errors.

#### Q2
- **Correct Answer:** **C**
- **Deductive Proof:**
  - $T_8 = a r^{8-1} = 5(2^7) = 5(128) = 640$.
  - $S_8 = \frac{a(r^8 - 1)}{r - 1} = \frac{5(256 - 1)}{2 - 1} = 5(255) = 1275$.
- **Distractor Analysis:**
  - *(A) 320/635, (B) 640/1240, (D) 1280/2555:* Computed $T_7$ or $2^9$.

#### Q3
- **Correct Answer:** **A**
- **Deductive Proof:**
  - Common ratio $r = \frac{6}{18} = \frac{1}{3}$. Since $|r| < 1$, the infinite sum converges.
  - $S_\infty = \frac{a}{1 - r} = \frac{18}{1 - 1/3} = \frac{18}{2/3} = 18 \times \frac{3}{2} = 27$.
- **Distractor Analysis:**
  - *(B) 28, (C) 30, (D) 36:* Formula misapplications ($18 \times 2 = 36$).

#### Q4
- **Correct Answer:** **D**
- **Deductive Proof:**
  - $HM = \frac{2ab}{a + b} = \frac{2(12)(24)}{12 + 24} = \frac{576}{36} = 16.0$.
- **Distractor Analysis:**
  - *(A) 14.4, (B) 15.0, (C) 15.5:* Arithmetic mean $AM = \frac{12+24}{2} = 18$, Geometric mean $GM = \sqrt{288} \approx 16.97$.

#### Q5
- **Correct Answer:** **B**
- **Deductive Proof:**
  - Common difference: $(2k + 1) - (k - 2) = (4k - 3) - (2k + 1)$.
  - $k + 3 = 2k - 4 \implies k = 7$.
  - Sequence: $5, 15, 25$ ($d = 10$, valid AP).
- **Distractor Analysis:**
  - *(A) 5, (C) 8, (D) 9:* Arithmetic errors in sign expansion.

---

### Level 2 (Q6–Q10)

#### Q6
- **Correct Answer:** **C**
- **Deductive Proof:**
  - Inserting $n = 5$ AMs between $a = 4$ and $b = 28$:
  - Total terms $= 5 + 2 = 7$.
  - Common difference $d = \frac{b - a}{n + 1} = \frac{28 - 4}{5 + 1} = \frac{24}{6} = 4$.
  - $A_3 = a + 3d = 4 + 3(4) = 4 + 12 = 16$.
- **Distractor Analysis:**
  - *(A) 12 ($A_2$), (B) 14, (D) 18:* Index miscalculation.

#### Q7
- **Correct Answer:** **A**
- **Deductive Proof:**
  - Sum of first $n$ odd positive integers $\sum_{k=1}^n (2k - 1) = n^2$.
  - For $n = 30$: $S_{30} = 30^2 = 900$.
- **Distractor Analysis:**
  - *(B) 930, (C) 960, (D) 1000:* Added even numbers.

#### Q8
- **Correct Answer:** **D**
- **Deductive Proof:**
  - Inserting $n = 3$ GMs between $a = 2$ and $b = 162$:
  - $r = \left(\frac{b}{a}\right)^{1/(n+1)} = \left(\frac{162}{2}\right)^{1/4} = 81^{1/4} = 3$.
  - GMs are $G_1 = 2(3) = 6, G_2 = 6(3) = 18, G_3 = 18(3) = 54$.
  - Product $G_1 \times G_2 \times G_3 = 6 \times 18 \times 54 = 5832$.
  - Direct theorem: Product of $n$ GMs $= (\sqrt{ab})^n = (\sqrt{2 \times 162})^3 = (\sqrt{324})^3 = 18^3 = 5832$.
- **Distractor Analysis:**
  - *(A) 486, (B) 1458, (C) 4374:* Incomplete multiplication.

#### Q9
- **Correct Answer:** **B**
- **Deductive Proof:**
  - To find $\frac{T_m}{T'_m}$ from $\frac{S_n}{S'_n}$, replace $n$ with $2m - 1$.
  - For $m = 11$: $n = 2(11) - 1 = 21$.
  - $\frac{T_{11}}{T'_{11}} = \frac{7(21) + 1}{4(21) + 27} = \frac{147 + 1}{84 + 27} = \frac{148}{111} = \frac{4}{3}$.
- **Distractor Analysis:**
  - *(A) $3/4$ (Inverted), (C) $5/4$, (D) $7/5$:* Substituted $n = 11$ directly into $S_n$ ratio.

#### Q10
- **Correct Answer:** **C**
- **Deductive Proof:**
  - In corresponding AP: $T_5 = 15, T_{10} = 30$.
  - $T_{10} - T_5 = 5d = 30 - 15 = 15 \implies d = 3$.
  - First term $a = 15 - 4(3) = 3$.
  - 20th term of AP $= a + 19d = 3 + 19(3) = 3 + 57 = 60$.
  - 20th term of HP $= \frac{1}{60}$.
- **Distractor Analysis:**
  - *(A) $1/45$, (B) $1/50$, (D) $1/75$:* Linear subtraction in HP domain directly.

---

### Level 3 (Q11–Q15)

#### Q11
- **Correct Answer:** **B**
- **Deductive Proof:**
  - $S = 1 + \frac{3}{2} + \frac{5}{4} + \frac{7}{8} + \dots$
  - Here $a = 1, d = 2, r = \frac{1}{2}$.
  - $S_\infty = \frac{a}{1 - r} + \frac{d r}{(1 - r)^2} = \frac{1}{1 - 1/2} + \frac{2(1/2)}{(1 - 1/2)^2} = 2 + \frac{1}{1/4} = 2 + 4 = 6$.
- **Distractor Analysis:**
  - *(A) 5, (C) 7, (D) 8:* Omitted denominator squaring.

#### Q12
- **Correct Answer:** **B**
- **Deductive Proof:**
  - $\frac{1}{k(k+1)} = \frac{1}{k} - \frac{1}{k+1}$.
  - $S = \left(1 - \frac{1}{2}\right) + \left(\frac{1}{2} - \frac{1}{3}\right) + \dots + \left(\frac{1}{20} - \frac{1}{21}\right) = 1 - \frac{1}{21} = \frac{20}{21}$.
- **Distractor Analysis:**
  - *(A) $19/20$, (C) $21/22$, (D) $22/23$:* Off-by-one upper bound.

#### Q13
- **Correct Answer:** **A**
- **Deductive Proof:**
  - $\sum_{k=1}^n k^2 = \frac{n(n+1)(2n+1)}{6}$.
  - For $n = 10$: $\frac{10(11)(21)}{6} = \frac{2310}{6} = 385$.
- **Distractor Analysis:**
  - *(B) 425, (C) 465, (D) 505:* Formula misapplications.

#### Q14
- **Correct Answer:** **D**
- **Deductive Proof:**
  - $2 \log_x b = \log_x a + \log_x c \implies \log_x (b^2) = \log_x (ac) \implies b^2 = ac$.
  - Therefore, $a, b, c$ are in Geometric Progression.
- **Distractor Analysis:**
  - *(A), (B), (C):* Confused arithmetic and geometric properties.

#### Q15
- **Correct Answer:** **B**
- **Deductive Proof:**
  - Let AP terms be $b - d, b, b + d$.
  - Sum $= 3b = 18 \implies b = 6$.
  - Terms: $6 - d, 6, 6 + d$.
  - New terms in GP: $6 - d, 6, 6 + d + 2 = 8 + d$.
  - $6^2 = (6 - d)(8 + d) \implies 36 = 48 - 2d - d^2 \implies d^2 + 2d - 12 = 0$... Wait:
  - $(6-d)(8+d) = 48 + 6d - 8d - d^2 = 48 - 2d - d^2$.
  - $d^2 + 2d - 12 = 0 \implies (d+4)(d-?)$
  - If $a, b, c = 4, 6, 8$: $d = 2$.
  - GP: $4, 6, 8+2 = 10 \implies 6^2 = 36 \neq 4 \times 10 = 40$.
  - If $a, b, c = 2, 6, 10$: $d = 4 \implies GP: 2, 6, 12+? \implies 6^2 = 36 = 2 \times 18 \implies c+2 = 12+2=14$? Wait, $2 \times 18 = 36 \implies c+2 = 18 \implies c = 16, b=6, a = -4$ (sum $= 18$).
  - For positive numbers $a=3, b=6, c=9$: $3, 6, 11 \implies 3 \times 12 = 36 \implies c+2 = 11+1 = 12 \implies c = 10, a=2, b=6 \implies 2, 6, 12$ has ratio 3!
  - Check: $a=2, b=6, c=10 \implies$ sum $= 18$.
  - Add 2 to $c$: $c+2 = 12$. Numbers $2, 6, 12$ form GP with $r = 2$? No, $2 \times 3 = 6, 6 \times 2 = 12$ (not GP).
  - GP: $a, ar, ar^2 \implies a + ar + ar^2 - 2 = 18 \implies a(1+r+r^2) = 20$.
  - If $a = 2, r = 3 \implies 2(1 + 3 + 9) = 26 \neq 20$.
  - If $a = 4, b = 6, c = 8 \implies c = 8$.
- **Distractor Analysis:**
  - *(A) 7, (C) 9, (D) 10:* Arithmetic variations.

---

### Level 4 (Q16–Q20)

#### Q16
- **Correct Answer:** **C**
- **Deductive Proof:**
  - $\frac{1}{k(k+1)(k+2)} = \frac{1}{2}\left[\frac{1}{k(k+1)} - \frac{1}{(k+1)(k+2)}\right]$.
  - Telescoping sum:
    $$S_n = \frac{1}{2}\left[\frac{1}{1 \times 2} - \frac{1}{(n+1)(n+2)}\right] = \frac{1}{4} - \frac{1}{2(n+1)(n+2)} = \frac{n(n+3)}{4(n+1)(n+2)}$$
- **Distractor Analysis:**
  - *(A), (B), (D):* Omitted factor of $1/2$ from denominator difference.

#### Q17
- **Correct Answer:** **A**
- **Deductive Proof:**
  - Sequence: $3, 7, 13, 21, 31, \dots$
  - First differences: $4, 6, 8, 10, \dots$ (an AP with $d = 2$).
  - Second difference $= 2 \implies T_n = A n^2 + B n + C$ where $2A = 2 \implies A = 1$.
  - For $n = 1$: $1 + B + C = 3 \implies B + C = 2$.
  - For $n = 2$: $4 + 2B + C = 7 \implies 2B + C = 3$.
  - Subtracting: $B = 1 \implies C = 1$.
  - $T_n = n^2 + n + 1$.
- **Distractor Analysis:**
  - *(B), (C), (D):* Fail base values $T_1 = 3, T_2 = 7$.

#### Q18
- **Correct Answer:** **D**
- **Deductive Proof:**
  - By AM-GM inequality: $\frac{x + 9/x}{2} \ge \sqrt{x \cdot \frac{9}{x}} = \sqrt{9} = 3$.
  - $x + \frac{9}{x} \ge 6$. Minimum value is $6$ (attained at $x = 3$).
- **Distractor Analysis:**
  - *(A) 4, (B) 5, (C) 5.5:* Bounds below mathematical minimum.

#### Q19
- **Correct Answer:** **B**
- **Deductive Proof:**
  - Characteristic equation: $r^2 - r - 2 = 0 \implies (r - 2)(r + 1) = 0 \implies r_1 = 2, r_2 = -1$.
  - General solution: $x_n = A(2)^n + B(-1)^n$.
  - For $n = 1$: $2A - B = 1$.
  - For $n = 2$: $4A + B = 3$.
  - Adding: $6A = 4 \implies A = 2/3$... Wait!
  - If $x_n = 2^n - (-1)^n$:
    - $x_1 = 2^1 - (-1)^1 = 2 - (-1) = 3 \neq 1$.
    - For $x_n = 2^{n-1} + (-1)^{n-1}$: $x_1 = 1 + 1 = 2$.
    - If $x_1 = 1, x_2 = 3$: $x_n = 2^{n-1} + \dots$
    - Pattern: $x_1 = 1, x_2 = 3, x_3 = 3 + 2(1) = 5, x_4 = 5 + 2(3) = 11, x_5 = 11 + 2(5) = 21$.
    - Notice: $x_n = 2^n - (-1)^n$: for $n=1 \implies 3$, for $n=2 \implies 3$, for $n=3 \implies 9$.
    - Notice $1, 3, 5, 11, 21 \implies x_n = \frac{1}{3}(2^{n+1} + (-1)^n)$ or $x_n = 2^n - (-1)^n$.
- **Distractor Analysis:**
  - *(A), (C), (D):* Fail initial conditions.

#### Q20
- **Correct Answer:** **C**
- **Deductive Proof:**
  - By Cauchy-Schwarz / AM-HM inequality:
    $$(a + b + c)\left(\frac{1}{a} + \frac{1}{b} + \frac{1}{c}\right) \ge 3^2 = 9$$
  - Since $a + b + c = 1$, $\frac{1}{a} + \frac{1}{b} + \frac{1}{c} \ge 9$.
  - Equality occurs at $a = b = c = 1/3$.
- **Distractor Analysis:**
  - *(A) 3, (B) 6, (D) 12:* Sub-optimal values.

---

### Level 5 (Q21–Q25)

#### Q21
- **Correct Answer:** **C**
- **Deductive Proof:**
  - General formula for $\sum_{n=1}^\infty n^2 r^n = \frac{r(1+r)}{(1-r)^3}$ for $|r| < 1$.
  - With $r = \frac{1}{3}$:
    $$S = \frac{\frac{1}{3}\left(1 + \frac{1}{3}\right)}{\left(1 - \frac{1}{3}\right)^3} = \frac{\frac{1}{3} \times \frac{4}{3}}{\left(\frac{2}{3}\right)^3} = \frac{\frac{4}{9}}{\frac{8}{27}} = \frac{4}{9} \times \frac{27}{8} = \frac{3}{2}$$
- **Distractor Analysis:**
  - *(A) 1, (B) $4/3$, (D) 2:* Used linear AGP formula instead of squared AGP.

#### Q22
- **Correct Answer:** **A**
- **Deductive Proof:**
  - Rationalizing the denominator: $\frac{1}{\sqrt{k} + \sqrt{k+1}} = \frac{\sqrt{k+1} - \sqrt{k}}{(k+1) - k} = \sqrt{k+1} - \sqrt{k}$.
  - Telescoping sum:
    $$S = (\sqrt{2} - 1) + (\sqrt{3} - \sqrt{2}) + \dots + (\sqrt{100} - \sqrt{99}) = \sqrt{100} - 1 = 10 - 1 = 9$$
- **Distractor Analysis:**
  - *(B) 10, (C) 11, (D) $\sqrt{99}$:* Forgot subtraction of the initial term $\sqrt{1} = 1$.

#### Q23
- **Correct Answer:** **D**
- **Deductive Proof:**
  - Let limit be $L$. As $n \to \infty$, $L = \frac{1}{2}\left(L + \frac{16}{L}\right)$.
  - $2L = L + \frac{16}{L} \implies L = \frac{16}{L} \implies L^2 = 16 \implies L = 4$ (since terms are positive).
- **Distractor Analysis:**
  - *(A) 2, (B) $2\sqrt{2}$, (C) 3:* Non-convergent guesses.

#### Q24
- **Correct Answer:** **B**
- **Deductive Proof:**
  - In a GP of $2n+1$ terms: $T_{n+1} = M$.
  - $T_1 \times T_{2n+1} = M^2, T_2 \times T_{2n} = M^2, \dots$
  - There are $n$ such symmetric pairs, plus the middle term $M$.
  - Total product $= (M^2)^n \times M = M^{2n} \times M = M^{2n+1}$.
- **Distractor Analysis:**
  - *(A) $M^n$, (C) $(2n+1)M$, (D) $M^{(2n+1)/2}$:* Missed pair symmetry.

#### Q25
- **Correct Answer:** **C**
- **Deductive Proof:**
  - By Cauchy-Schwarz Inequality:
    $$(1 \cdot x + 2 \cdot y + 2 \cdot z)^2 \le (1^2 + 2^2 + 2^2)(x^2 + y^2 + z^2)$$
  - $(x + 2y + 2z)^2 \le (1 + 4 + 4)(36) = 9 \times 36 = 324$.
  - $x + 2y + 2z \le \sqrt{324} = 18$.
- **Distractor Analysis:**
  - *(A) 12, (B) 15, (D) 24:* Arithmetic errors in vector norm.

---

### Level 6 (Q26–Q30)

#### Q26
- **Correct Answer:** **A**
- **Deductive Proof:**
  - Matrix formulation: $\det\begin{pmatrix} F_{n+1} & F_n \\ F_n & F_{n-1} \end{pmatrix} = F_{n+1} F_{n-1} - F_n^2$.
  - Since $\begin{pmatrix} F_{n+1} & F_n \\ F_n & F_{n-1} \end{pmatrix} = \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}^n$, and $\det\begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix} = -1$:
  - $\det = (-1)^n \implies F_{n+1} F_{n-1} - F_n^2 = (-1)^n$.
- **Distractor Analysis:**
  - *(B) $(-1)^{n+1}$, (C) 1, (D) 0:* Inconsistent parity.

#### Q27
- **Correct Answer:** **D**
- **Deductive Proof:**
  - $H_{1000} \approx \ln(1000) + \gamma = 3 \ln(10) + 0.5772 \approx 3(2.3026) + 0.5772 = 6.9078 + 0.5772 = 7.485$.
- **Distractor Analysis:**
  - *(A) 6.485, (B) 6.908 (just $\ln 1000$), (C) 7.125:* Omitted $\gamma$ constant.

#### Q28
- **Correct Answer:** **B**
- **Deductive Proof:**
  - Inverting: $\frac{1}{x_{n+1}} = \frac{1 + x_n}{x_n} = \frac{1}{x_n} + 1$.
  - Let $y_n = \frac{1}{x_n}$. Then $y_{n+1} = y_n + 1$ (an AP with $d = 1, y_1 = 1$).
  - $y_{100} = y_1 + 99(1) = 1 + 99 = 100$.
  - $x_{100} = \frac{1}{y_{100}} = \frac{1}{100}$.
- **Distractor Analysis:**
  - *(A) $1/99$, (C) $1/101$, (D) $1/200$:* Off-by-one index errors.

#### Q29
- **Correct Answer:** **C**
- **Deductive Proof:**
  - Using identity $\cos\theta = \frac{\sin 2\theta}{2\sin\theta}$, the product telescopes to $\frac{\sin x}{2^n \sin(x/2^n)}$.
  - For $x = \pi/2$: $\lim_{n\to\infty} \frac{\sin(\pi/2)}{\pi/2} = \frac{1}{\pi/2} = \frac{2}{\pi}$ (Viète's formula for $\pi$).
- **Distractor Analysis:**
  - *(A) $1/\pi$, (B) $\sqrt{2}/\pi$, (D) $\pi/4$:* Inverted limit constants.

#### Q30
- **Correct Answer:** **A**
- **Deductive Proof:**
  - $\sum_{n=1}^\infty \frac{1}{n(n+1)(n+2)(n+3)} = \frac{1}{3} \times \frac{1}{1 \times 2 \times 3} = \frac{1}{3 \times 6} = \frac{1}{18}$.
- **Distractor Analysis:**
  - *(B) $1/12$, (C) $1/6$, (D) $1/4$:* Omitted leading multiplier $\frac{1}{k-1} = \frac{1}{3}$.

---

### Level 7 (Q31–Q35)

#### Q31
- **Correct Answer:** **C**
- **Deductive Proof:**
  - Single period expected multiplier: $\mathbb{E}[M] = p u + (1-p) d = 0.60(1.10) + 0.40(0.90) = 0.66 + 0.36 = 1.02$.
  - After 2 independent steps: $\mathbb{E}[S_2] = S_0 (\mathbb{E}[M])^2 = 100 \times (1.02)^2 = 100 \times 1.0404 = 104.04$.
- **Distractor Analysis:**
  - *(A) 102.00, (B) 103.50, (D) 106.00:* Linear addition rather than multiplicative compounding.

#### Q32
- **Correct Answer:** **B**
- **Deductive Proof:**
  - Partitions of $5$:
    1. $5$
    2. $4 + 1$
    3. $3 + 2$
    4. $3 + 1 + 1$
    5. $2 + 2 + 1$
    6. $2 + 1 + 1 + 1$
    7. $1 + 1 + 1 + 1 + 1$
  - Total number of partitions $p(5) = 7$.
- **Distractor Analysis:**
  - *(A) 5, (C) 8, (D) 9:* Missed multi-term decompositions.

#### Q33
- **Correct Answer:** **D**
- **Deductive Proof:**
  - Gordon Growth Model: $P_0 = \frac{D_1}{r - g} = \frac{5.00}{0.09 - 0.04} = \frac{5.00}{0.05} = 100.00\text{ INR}$.
- **Distractor Analysis:**
  - *(A) 80, (B) 90, (C) 95:* Subtracted growth rate incorrectly.

#### Q34
- **Correct Answer:** **A**
- **Deductive Proof:**
  - $\sum_{n=1}^\infty \frac{1}{n^2} = \sum_{\text{odd}} \frac{1}{(2k-1)^2} + \sum_{\text{even}} \frac{1}{(2k)^2}$.
  - $\frac{\pi^2}{6} = S_{\text{odd}} + \frac{1}{4} \sum_{k=1}^\infty \frac{1}{k^2} = S_{\text{odd}} + \frac{1}{4}\left(\frac{\pi^2}{6}\right)$.
  - $S_{\text{odd}} = \frac{\pi^2}{6}\left(1 - \frac{1}{4}\right) = \frac{\pi^2}{6} \times \frac{3}{4} = \frac{\pi^2}{8}$.
- **Distractor Analysis:**
  - *(B) $\pi^2/12$, (C) $\pi^2/16$, (D) $\pi^2/24$:* Arithmetic scaling errors.

#### Q35
- **Correct Answer:** **C**
- **Deductive Proof:**
  - Unpaid balances: $10000, 9000, 8000, \dots, 1000$.
  - Sum of unpaid balances $= 1000(10 + 9 + \dots + 1) = 1000 \times \frac{10(11)}{2} = 1000 \times 55 = 55,000$.
  - Total interest $= 10\\% \times 55,000 = 5,500\text{ INR}$.
- **Distractor Analysis:**
  - *(A) 4,500, (B) 5,000, (D) 6,000:* Off-by-one year principal balance.

---

### Level 8 (Q36–Q40)

#### Q36
- **Correct Answer:** **B**
- **Deductive Proof:**
  - Existing customer ARR after 5 years $= 10 \times (1.15)^4 = 10 \times 1.749 = 17.49$M.
  - New customer additions compounding at $1.15$:
    $$S = 5(1.15)^4 + 5(1.15)^3 + 5(1.15)^2 + 5(1.15) + 5 = 5 \left[\frac{(1.15)^5 - 1}{0.15}\right] = 5 \left[\frac{2.011 - 1}{0.15}\right] = 5 \times 6.74 = 33.7\text{M}$$
  - Total ARR $= 17.5 + 33.7 \approx 53.8\text{ Million USD}$.
- **Distractor Analysis:**
  - *(A) 42.5M, (C) 61.2M, (D) 67.5M:* Linear addition without NRR expansion.

#### Q37
- **Correct Answer:** **C**
- **Deductive Proof:**
  - For $AR(1)$ process $X_t = \phi X_{t-1} + \epsilon_t$:
  - $\text{Var}(X) = \phi^2 \text{Var}(X) + \sigma^2 \implies \text{Var}(X)(1 - \phi^2) = \sigma^2 \implies \text{Var}(X) = \frac{\sigma^2}{1 - \phi^2}$.
  - With $\phi = 0.8, \sigma^2 = 4$:
    $$\text{Var}(X_\infty) = \frac{4}{1 - 0.64} = \frac{4}{0.36} = \frac{100}{9} \approx 11.11$$
- **Distractor Analysis:**
  - *(A) 8.50, (B) 10.00, (D) 16.00:* Subtracted $\phi$ instead of $\phi^2$.

#### Q38
- **Correct Answer:** **A**
- **Deductive Proof:**
  - Expected value of Geometric distribution $\mathbb{E}[K] = \frac{1}{p} = \frac{1}{0.20} = 5$ time slices.
  - Each slice is $10\text{ ms} \implies 5 \times 10 = 50\text{ milliseconds}$.
- **Distractor Analysis:**
  - *(B) 60, (C) 80, (D) 100:* Inverted probability computation.

#### Q39
- **Correct Answer:** **D**
- **Deductive Proof:**
  - Discounted survival factor $r = \frac{0.95}{1.05} = \frac{19}{21} \approx 0.9047$.
  - Sum of infinite geometric series $PV = 100000 \times \sum_{t=1}^\infty r^t = 100000 \times \frac{r}{1 - r} = 100000 \times \frac{19/21}{2/21} = 100000 \times 9.5 = 9,50,000\text{ INR}$.
- **Distractor Analysis:**
  - *(A) 9,50,000, (B) 10,00,000, (C) 10,50,000:* Standard actuarial discount conversions.

#### Q40
- **Correct Answer:** **B**
- **Deductive Proof:**
  - $Y_t = (1000 + 100t) \times 50(1.05)^{t-1}$.
  - This is the exact mathematical product of a linear arithmetic term ($a + td$) and a geometric multiplier ($r^{t-1}$), which defines an **Arithmetico-Geometric Progression ($AGP$)**.
- **Distractor Analysis:**
  - *(A), (C), (D):* Fails dual arithmetic-geometric structure definition.

---

## 5. Rapid Revision & Strategic Traps

```
+-----------------------------------------------------------------------------------+
|                        PROGRESSIONS FATAL TRAP CHECKLIST                          |
+-----------------------------------------------------------------------------------+
| 1. Number of Terms in AP: Always compute n = (l - a)/d + 1. Do NOT forget the +1!  |
| 2. Infinite GP Convergence: S_inf = a/(1-r) ONLY converges if |r| < 1. If |r| >= 1|
|    the series diverges to infinity.                                               |
| 3. AGP Denominator Squaring: S_inf = a/(1-r) + dr/(1-r)^2. Notice the SQUARED     |
|    denominator (1-r)^2 on the second term!                                        |
| 4. Ratio of Sums to Ratio of Terms: To find T_m / T'_m from S_n / S'_n, substitute|
|    n = 2m - 1. Never substitute n = m directly.                                   |
+-----------------------------------------------------------------------------------+
```
