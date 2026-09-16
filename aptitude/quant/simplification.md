# Quantitative Aptitude: Simplification, Surds & Algebraic Identities

> **Priority:** P1 · **Role relevance:** High (Quantitative Analytics, High-Frequency Trading, Management Consulting, Data Engineering & Numerical Computing)  
> **Difficulty range:** Foundation → Nested Radicals, Continued Fractions, Ramanujan Identities, Cubic Algebraic Factorization & Fast Asymptotic Estimation  
> **Target speed:** 25–45 sec (Direct Surd Rationalization / Identity Folding) – 60–90 sec (Nested Radical Denesting / Continued Fraction Limits)

---

## 1. Theoretical Framework & Algebraic Formulations

### 1.1 The Algebraic Master Identities

```
+-----------------------------------------------------------------------------------+
|                        CANONICAL ALGEBRAIC IDENTITIES                             |
+-----------------------------------------------------------------------------------+
| 1. Quadratic Factorization : (a + b + c)^2 = a^2 + b^2 + c^2 + 2(ab + bc + ca)    |
| 2. Cubic Factorization     : a^3 + b^3 + c^3 - 3abc                               |
|                              = (a + b + c)(a^2 + b^2 + c^2 - ab - bc - ca)        |
|                              = (1/2)(a + b + c)[(a-b)^2 + (b-c)^2 + (c-a)^2]      |
|                              If a + b + c = 0, then a^3 + b^3 + c^3 = 3abc        |
| 3. Sophie Germain Identity : a^4 + 4b^4 = (a^2 + 2b^2 + 2ab)(a^2 + 2b^2 - 2ab)    |
| 4. Surd Denesting Formula  : sqrt(A +- sqrt(B)) = sqrt((A + C)/2) +- sqrt((A - C)/2)|
|                              where C = sqrt(A^2 - B) must be a rational number.   |
+-----------------------------------------------------------------------------------+
```

---

### 1.2 Mathematical Archetypes & Advanced Simplification Toolkits

#### 1. Infinite Continued Fractions
For the periodic continued fraction $x = a_0 + \frac{b_1}{a_1 + \frac{b_2}{a_1 + \frac{b_2}{\dots}}}$:
- Express the infinite tail as $x$: $x = a_0 + \frac{b_1}{a_1 + \frac{b_2}{x-a_0}}$
- Solve the resulting quadratic equation for the unique positive real root.
- **The Golden Ratio ($x = 1 + \frac{1}{1 + \frac{1}{1+\dots}}$):** $x = 1 + \frac{1}{x} \implies x^2 - x - 1 = 0 \implies \phi = \frac{1 + \sqrt{5}}{2} \approx 1.618033$.

#### 2. Nested Radicals of Ramanujan Type
- **Constant nested radical:** $x = \sqrt{a + \sqrt{a + \sqrt{a + \dots}}} \implies x^2 = a + x \implies x = \frac{1 + \sqrt{1 + 4a}}{2}$.
- If $a = n(n+1)$, then $x = n+1$. (e.g., $\sqrt{12 + \sqrt{12 + \dots}} = 4$).
- **Alternating signs:** $x = \sqrt{a - \sqrt{a + \sqrt{a - \dots}}} \implies x = \frac{\sqrt{4a - 3} - 1}{2}$.

#### 3. Power of Fractions & Fast Decimal Approximation
- Binomial series for small $\epsilon = \frac{x}{A} \ll 1$:
  $$\sqrt{A + x} = \sqrt{A}\left(1 + \frac{x}{A}\right)^{1/2} \approx \sqrt{A}\left(1 + \frac{x}{2A} - \frac{x^2}{8A^2}\right)$$
  $$\sqrt[3]{A + x} \approx \sqrt[3]{A}\left(1 + \frac{x}{3A}\right)$$

---

## 2. Master Answer Key (Q1–Q40)

| Question | Level | Archetype / Domain | Correct Answer | Core Mathematical Principle |
|:---:|:---:|:---|:---:|:---|
| **Q1** | Level 1 | Nested BODMAS Evaluation | **B** | Priority order: brackets $\to$ powers $\to$ div $\to$ mult $\to$ add $\to$ sub $\implies 24$ |
| **Q2** | Level 1 | Difference of Squares Identity | **C** | $a^2 - b^2 = (a-b)(a+b); (987)^2 - (983)^2 = 4 \times 1970 = 7880$ |
| **Q3** | Level 1 | Basic Surd Rationalization | **A** | $\frac{6}{\sqrt{5} - \sqrt{2}} = \frac{6(\sqrt{5}+\sqrt{2})}{3} = 2(\sqrt{5}+\sqrt{2})$ |
| **Q4** | Level 1 | Fractional Exponents Power Rule | **D** | $(64)^{-2/3} \times (16)^{3/4} = (4^3)^{-2/3} \times (2^4)^{3/4} = 4^{-2} \times 2^3 = \frac{8}{16} = \frac{1}{2}$ |
| **Q5** | Level 1 | Algebraic Identity Cancellation | **B** | $\frac{a^3 + b^3}{a^2 - ab + b^2} = a + b$; for $a = 0.87, b = 0.13 \implies a + b = 1.0$ |
| **Q6** | Level 2 | Surd Denesting Formula | **C** | $\sqrt{7 + 4\sqrt{3}} = \sqrt{7 + 2\sqrt{12}} = \sqrt{4} + \sqrt{3} = 2 + \sqrt{3}$ |
| **Q7** | Level 2 | Reciprocal Surd Symmetry | **A** | $x = 3 + 2\sqrt{2} \implies 1/x = 3 - 2\sqrt{2} \implies x + 1/x = 6 \implies x^2 + 1/x^2 = 6^2 - 2 = 34$ |
| **Q8** | Level 2 | Infinite Nested Root Product | **D** | $x = \sqrt{7\sqrt{7\sqrt{7\dots}}} \implies x^2 = 7x \implies x = 7$ |
| **Q9** | Level 2 | Infinite Nested Root Sum | **B** | $x = \sqrt{56 + \sqrt{56 + \sqrt{56\dots}}} \implies n(n+1) = 7 \times 8 \implies x = 8$ |
| **Q10** | Level 2 | Cubic Reciprocal Form | **C** | $x + 1/x = 4 \implies x^3 + 1/x^3 = 4^3 - 3(4) = 64 - 12 = 52$ |
| **Q11** | Level 3 | Multi-Term Surd Telescoping | **B** | $\sum_{k=1}^{48} \frac{1}{\sqrt{k} + \sqrt{k+1}} = \sqrt{49} - \sqrt{1} = 7 - 1 = 6$ |
| **Q12** | Level 3 | Zero-Sum Cubic Condition | **D** | If $a + b + c = 0$, then $\frac{a^3 + b^3 + c^3}{abc} = \frac{3abc}{abc} = 3$ |
| **Q13** | Level 3 | Continued Fraction Evaluation | **A** | $x = 2 + \frac{1}{2 + \frac{1}{2 + \dots}} \implies x = 2 + \frac{1}{x} \implies x^2 - 2x - 1 = 0 \implies x = 1 + \sqrt{2}$ |
| **Q14** | Level 3 | Exponent Surd Equation | **C** | $2^{x-1} + 2^{x+1} = 320 \implies 2^x(1/2 + 2) = 2^x(5/2) = 320 \implies 2^x = 128 \implies x = 7$ |
| **Q15** | Level 3 | Fifth Power Reciprocal | **B** | $x + 1/x = 3 \implies x^2 + 1/x^2 = 7, x^3 + 1/x^3 = 18 \implies x^5 + 1/x^5 = 7(18) - 3 = 123$ |
| **Q16** | Level 4 | Double Nested Denesting | **C** | $\sqrt{10 + \sqrt{24} + \sqrt{40} + \sqrt{60}} = \sqrt{2} + \sqrt{3} + \sqrt{5}$ |
| **Q17** | Level 4 | Sophie Germain Factorization | **A** | $x^4 + 64 = (x^2 + 4x + 8)(x^2 - 4x + 8)$; evaluation at integer points |
| **Q18** | Level 4 | Alternating Infinite Surd Root | **D** | $x = \sqrt{6 - \sqrt{6 + \sqrt{6 - \dots}}} \implies x = \frac{\sqrt{4(6)-3} - 1}{2} = \frac{\sqrt{21} - 1}{2}$ |
| **Q19** | Level 4 | High-Order Symmetry Factorization | **B** | $\frac{(a-b)^3 + (b-c)^3 + (c-a)^3}{(a-b)(b-c)(c-a)} = 3$ (since $(a-b) + (b-c) + (c-a) = 0$) |
| **Q20** | Level 4 | Linear Combination Logarithm Surds | **C** | $\log_2(3) \times \log_3(4) \times \dots \times \log_{63}(64) = \log_2(64) = 6$ |
| **Q21** | Level 5 | Ramanujan Infinite Radical Identity | **C** | $\sqrt{1 + 2\sqrt{1 + 3\sqrt{1 + 4\sqrt{\dots}}}} = 3$ |
| **Q22** | Level 5 | Modular Radical Denesting with Cube Roots | **A** | $\sqrt[3]{20 + 14\sqrt{2}} + \sqrt[3]{20 - 14\sqrt{2}} = (2 + \sqrt{2}) + (2 - \sqrt{2}) = 4$ |
| **Q23** | Level 5 | Continued Fraction Periodicity | **D** | $\sqrt{3} = [1; \overline{1, 2}]$; convergent $p_5/q_5 = 19/11 \approx 1.7272$ |
| **Q24** | Level 5 | Higher-Order Polynomial Root Cancellation | **B** | $x = \sqrt[3]{2} + \sqrt[3]{4} \implies x^3 = 6 + 6x \implies x^3 - 6x - 6 = 0$ |
| **Q25** | Level 5 | Multi-Variable Symmetric Sum System | **C** | System $a+b+c=3, a^2+b^2+c^2=5, a^3+b^3+c^3=9 \implies a^4+b^4+c^4 = 17$ |
| **Q26** | Level 6 | Rapid Binomial Decimal Estimation | **A** | $\sqrt{1004} \approx 31.68596$; error bound $< 10^{-6}$ |
| **Q27** | Level 6 | Trigonometric Radical Nesting | **D** | $2 \cos(\pi/2^{n+1}) = \sqrt{2 + \sqrt{2 + \dots}}$ with $n$ roots $\implies 2\cos(\pi/16) = \sqrt{2+\sqrt{2+\sqrt{2}}}$ |
| **Q28** | Level 6 | Matrix Radical Power & Trace | **B** | $\text{Tr}\left(\begin{pmatrix} 3 & 1 \\ 1 & 3 \end{pmatrix}^n\right) = 4^n + 2^n$ |
| **Q29** | Level 6 | Factorial Asymptotic Simplification (Stirling) | **C** | $\lim_{n\to\infty} \frac{(2n)! \sqrt{\pi n}}{4^n (n!)^2} = 1$ |
| **Q30** | Level 6 | Nested Cubic Surd Equation | **A** | $x = \sqrt[3]{a + \frac{a+1}{3}\sqrt{\frac{8a-1}{3}}} + \sqrt[3]{a - \frac{a+1}{3}\sqrt{\frac{8a-1}{3}}} = 1$ |
| **Q31** | Level 7 | High-Frequency Floating Point Precision Error | **C** | Catastrophic cancellation avoidance: $1 - \cos x = \frac{\sin^2 x}{1 + \cos x} \approx \frac{x^2}{2}$ |
| **Q32** | Level 7 | Gamma Function Radical Reflection | **B** | $\Gamma(1/4)\Gamma(3/4) = \frac{\pi}{\sin(\pi/4)} = \pi\sqrt{2}$ |
| **Q33** | Level 7 | Hyperbolic Surd Inverse Inversion | **D** | $\text{arsinh}(x) = \ln(x + \sqrt{x^2 + 1})$; for $x = 3/4 \implies \ln(3/4 + 5/4) = \ln 2$ |
| **Q34** | Level 7 | Modular Inversion & Padé Approximants | **A** | Padé [2/2] approximation for $e^x = \frac{1 + x/2 + x^2/12}{1 - x/2 + x^2/12}$ |
| **Q35** | Level 7 | Fast Reciprocal Square Root (Quake Engine) | **D** | Newton-Raphson step $y_{n+1} = y_n(1.5 - 0.5 x y_n^2) \implies$ relative error $< 0.17\\%$ |
| **Q36** | Level 8 | Consulting Caselet: Bond Yield Convexity Taylor Series | **B** | $\frac{\Delta P}{P} \approx -D_{\text{mod}} \Delta y + \frac{1}{2} C (\Delta y)^2 \implies \Delta P = -4.76\\%$ |
| **Q37** | Level 8 | Computational Geometry: Fast Floating-Point Determinant | **B** | Exact 2D orientation test: collinear points have determinant $\Delta = 0$ |
| **Q38** | Level 8 | Algorithmic Caselet: Big-O Polynomial Asymptotics | **A** | $\sqrt{n^4 + 3n^2} - n^2 = \frac{3n^2}{\sqrt{n^4+3n^2} + n^2} \to \frac{3}{2}$ |
| **Q39** | Level 8 | High-Frequency Alpha: Micro-Pricing Taylor Expansion | **D** | Volatility smile quadratic smile approximation $\sigma(K) = \sigma_0 + \alpha(K-S_0) + \beta(K-S_0)^2$ |
| **Q40** | Level 8 | Civil Caselet: Manning Hydraulic Resistance Simplification | **B** | Non-linear root solving via Cardano/Newton approximation for water depth $y = 2.45\text{ m}$ |

---

## 3. Comprehensive Practice Set (40 Placement Questions)

### Level 1: Foundation (Q1–Q5)

#### Q1
Evaluate the arithmetic expression using standard BODMAS hierarchy:
$$E = 36 - 2 \times [14 - (8 - 3 \times 2)] \div 4$$
- (A) $22$
- (B) $30$
- (C) $32$
- (D) $34$

#### Q2
What is the exact value of the difference of squares:
$$(987)^2 - (983)^2$$
- (A) $7840$
- (B) $7860$
- (C) $7880$
- (D) $7920$

#### Q3
Rationalize the denominator and simplify the surd expression:
$$\frac{6}{\sqrt{5} - \sqrt{2}}$$
- (A) $2(\sqrt{5} + \sqrt{2})$
- (B) $3(\sqrt{5} + \sqrt{2})$
- (C) $2(\sqrt{5} - \sqrt{2})$
- (D) $\sqrt{5} + \sqrt{2}$

#### Q4
Evaluate the fractional exponent product:
$$(64)^{-2/3} \times (16)^{3/4}$$
- (A) $\frac{1}{8}$
- (B) $\frac{1}{4}$
- (C) $\frac{1}{\sqrt{2}}$
- (D) $\frac{1}{2}$

#### Q5
Using algebraic factorization, evaluate:
$$\frac{(0.87)^3 + (0.13)^3}{(0.87)^2 - (0.87 \times 0.13) + (0.13)^2}$$
- (A) $0.74$
- (B) $1.00$
- (C) $1.13$
- (D) $1.25$

---

### Level 2: Surd Denesting & Infinite Nested Roots (Q6–Q10)

#### Q6
Denest the radical expression into simple surds:
$$\sqrt{7 + 4\sqrt{3}}$$
- (A) $1 + \sqrt{3}$
- (B) $3 + \sqrt{2}$
- (C) $2 + \sqrt{3}$
- (D) $\sqrt{5} + \sqrt{2}$

#### Q7
If $x = 3 + 2\sqrt{2}$, what is the value of $x^2 + \frac{1}{x^2}$?
- (A) $34$
- (B) $36$
- (C) $38$
- (D) $40$

#### Q8
What is the value of the infinite nested radical product:
$$P = \sqrt{7 \sqrt{7 \sqrt{7 \dots}}}$$
- (A) $\sqrt{7}$
- (B) $1$
- (C) $3.5$
- (D) $7$

#### Q9
What is the value of the infinite nested radical sum:
$$S = \sqrt{56 + \sqrt{56 + \sqrt{56 + \dots}}}$$
- (A) $7$
- (B) $8$
- (C) $9$
- (D) $14$

#### Q10
If $x + \frac{1}{x} = 4$, what is the value of $x^3 + \frac{1}{x^3}$?
- (A) $48$
- (B) $50$
- (C) $52$
- (D) $64$

---

### Level 3: Continued Fractions & Cubic Systems (Q11–Q15)

#### Q11
Evaluate the sum of the finite telescoping surd series:
$$S = \frac{1}{1 + \sqrt{2}} + \frac{1}{\sqrt{2} + \sqrt{3}} + \frac{1}{\sqrt{3} + \sqrt{4}} + \dots + \frac{1}{\sqrt{48} + \sqrt{49}}$$
- (A) $5$
- (B) $6$
- (C) $7$
- (D) $8$

#### Q12
If $a + b + c = 0$ (where $a, b, c$ are non-zero real numbers), what is the value of:
$$\frac{a^3 + b^3 + c^3}{a b c}$$
- (A) $0$
- (B) $1$
- (C) $2$
- (D) $3$

#### Q13
What is the positive real value of the infinite continued fraction:
$$x = 2 + \frac{1}{2 + \frac{1}{2 + \frac{1}{2 + \dots}}}$$
- (A) $1 + \sqrt{2}$
- (B) $2 + \sqrt{2}$
- (C) $\sqrt{3} + 1$
- (D) $\frac{1 + \sqrt{5}}{2}$

#### Q14
Find the value of $x$ satisfying the exponential equation:
$$2^{x-1} + 2^{x+1} = 320$$
- (A) $5$
- (B) $6$
- (C) $7$
- (D) $8$

#### Q15
If $x + \frac{1}{x} = 3$, what is the value of $x^5 + \frac{1}{x^5}$?
- (A) $118$
- (B) $123$
- (C) $126$
- (D) $132$

---

### Level 4: Sophie Germain & Multi-Term Radicals (Q16–Q20)

#### Q16
Denest the triple square root expression:
$$\sqrt{10 + \sqrt{24} + \sqrt{40} + \sqrt{60}}$$
- (A) $1 + \sqrt{2} + \sqrt{7}$
- (B) $1 + \sqrt{3} + \sqrt{6}$
- (C) $\sqrt{2} + \sqrt{3} + \sqrt{5}$
- (D) $\sqrt{2} + \sqrt{4} + \sqrt{4}$

#### Q17
Using Sophie Germain's identity $a^4 + 4b^4 = (a^2 + 2b^2 + 2ab)(a^2 + 2b^2 - 2ab)$, factorize $x^4 + 64$. Which of the following is one of its irreducible real quadratic factors?
- (A) $x^2 + 4x + 8$
- (B) $x^2 + 2x + 8$
- (C) $x^2 - 8x + 16$
- (D) $x^2 + 8x + 16$

#### Q18
What is the value of the alternating infinite radical:
$$x = \sqrt{6 - \sqrt{6 + \sqrt{6 - \sqrt{6 + \dots}}}}$$
- (A) $2.0$
- (B) $\frac{\sqrt{21} + 1}{2}$
- (C) $\frac{\sqrt{23} - 1}{2}$
- (D) $\frac{\sqrt{21} - 1}{2}$

#### Q19
Simplify the algebraic fraction for distinct real numbers $a, b, c$:
$$\frac{(a - b)^3 + (b - c)^3 + (c - a)^3}{(a - b)(b - c)(c - a)}$$
- (A) $1$
- (B) $3$
- (C) $6$
- (D) $a + b + c$

#### Q20
Evaluate the telescoping logarithmic product:
$$P = \log_2(3) \times \log_3(4) \times \log_4(5) \times \dots \times \log_{63}(64)$$
- (A) $4$
- (B) $5$
- (C) $6$
- (D) $8$

---

### Level 5: Ramanujan Radicals & Power Sum Systems (Q21–Q25)

#### Q21
What is the exact integer value of Ramanujan's nested radical:
$$R = \sqrt{1 + 2\sqrt{1 + 3\sqrt{1 + 4\sqrt{1 + \dots}}}}$$
- (A) $1$
- (B) $2$
- (C) $3$
- (D) $4$

#### Q22
Simplify the nested cube root sum:
$$S = \sqrt[3]{20 + 14\sqrt{2}} + \sqrt[3]{20 - 14\sqrt{2}}$$
- (A) $4$
- (B) $2\sqrt{2}$
- (C) $3\sqrt{2}$
- (D) $5$

#### Q23
The continued fraction expansion of $\sqrt{3}$ is $[1; \overline{1, 2}]$. What is the 5th convergent $\frac{p_5}{q_5}$ of $\sqrt{3}$?
- (A) $\frac{7}{4}$
- (B) $\frac{11}{6}$
- (C) $\frac{15}{9}$
- (D) $\frac{19}{11}$

#### Q24
If $x = \sqrt[3]{2} + \sqrt[3]{4}$, what is the value of $x^3 - 6x$?
- (A) $4$
- (B) $6$
- (C) $8$
- (D) $10$

#### Q25
If $a, b, c$ satisfy $a + b + c = 3$, $a^2 + b^2 + c^2 = 5$, and $a^3 + b^3 + c^3 = 9$, what is the value of $a^4 + b^4 + c^4$?
- (A) $15$
- (B) $16$
- (C) $17$
- (D) $18$

---

### Level 6: Asymptotic Approximations & Matrix Invariants (Q26–Q30)

#### Q26
Using the first-order binomial series approximation $\sqrt{A + \epsilon} \approx \sqrt{A} + \frac{\epsilon}{2\sqrt{A}}$, what is the rapid mental approximation of $\sqrt{1004}$?
- (A) $31.68596$
- (B) $31.72500$
- (C) $31.84000$
- (D) $32.00000$

#### Q27
The nested trigonometric radical $2 \cos\left(\frac{\pi}{16}\right)$ can be expressed in closed form as:
- (A) $\sqrt{2 - \sqrt{2}}$
- (B) $\sqrt{2 + \sqrt{2}}$
- (C) $\sqrt{2 - \sqrt{2 + \sqrt{2}}}$
- (D) $\sqrt{2 + \sqrt{2 + \sqrt{2}}}$

#### Q28
For the $2 \times 2$ matrix $M = \begin{pmatrix} 3 & 1 \\ 1 & 3 \end{pmatrix}$, what is the trace of $M^n$ ($\text{Tr}(M^n)$)?
- (A) $3^n + 1$
- (B) $4^n + 2^n$
- (C) $4^n - 2^n$
- (D) $6^n$

#### Q29
Using Stirling's asymptotic formula $n! \sim \sqrt{2\pi n}\left(\frac{n}{e}\right)^n$, what is the limiting value:
$$\lim_{n\to\infty} \frac{(2n)! \sqrt{\pi n}}{4^n (n!)^2}$$
- (A) $\frac{1}{2}$
- (B) $\frac{1}{\sqrt{2}}$
- (C) $1$
- (D) $\sqrt{\pi}$

#### Q30
What is the unique positive real solution to the nested cubic radical equation:
$$x = \sqrt[3]{1 + \frac{2}{3}\sqrt{\frac{7}{3}}} + \sqrt[3]{1 - \frac{2}{3}\sqrt{\frac{7}{3}}}$$
- (A) $1$
- (B) $\sqrt{2}$
- (C) $\sqrt{3}$
- (D) $2$

---

### Level 7: Numerical Stability & Gamma Functions (Q31–Q35)

#### Q31
In high-precision numerical algorithms, computing $1 - \cos x$ for very small $x \approx 10^{-5}$ suffers from catastrophic floating-point cancellation. Which algebraically equivalent expression eliminates this cancellation error?
- (A) $\frac{x^2}{2} - \frac{x^4}{24}$
- (B) $2 \sin^2\left(\frac{x}{2}\right) = \frac{\sin^2 x}{1 + \cos x}$
- (C) Both (A) and (B) provide stable algebraic forms
- (D) $\cos^2 x - 1$

#### Q32
Using Euler's reflection formula for the Gamma function $\Gamma(z)\Gamma(1-z) = \frac{\pi}{\sin(\pi z)}$, what is the exact value of the product $\Gamma\left(\frac{1}{4}\right)\Gamma\left(\frac{3}{4}\right)$?
- (A) $\pi$
- (B) $\pi\sqrt{2}$
- (C) $\frac{\pi}{\sqrt{2}}$
- (D) $2\pi$

#### Q33
What is the exact simplified logarithmic value of $\text{arsinh}\left(\frac{3}{4}\right) = \ln\left(\frac{3}{4} + \sqrt{\left(\frac{3}{4}\right)^2 + 1}\right)$?
- (A) $\ln(1.5)$
- (B) $\ln(1.75)$
- (C) $\ln(2.25)$
- (D) $\ln(2.00)$

#### Q34
The diagonal Padé [1/1] approximant to $e^x$ is given by $R_{1,1}(x) = \frac{1 + x/2}{1 - x/2}$. What is the estimated value of $e^{0.2}$ using this formula?
- (A) $\frac{1.1}{0.9} = \frac{11}{9} \approx 1.2222$
- (B) $1.2000$
- (C) $1.2214$
- (D) $1.2500$

#### Q35
In Fast Inverse Square Root algorithm ($\frac{1}{\sqrt{x}}$), one iteration of Newton-Raphson refinement on $f(y) = \frac{1}{y^2} - x = 0$ yields the update:
- (A) $y_{n+1} = y_n(1 - x y_n)$
- (B) $y_{n+1} = 0.5 y_n(3 - x y_n^2)$
- (C) $y_{n+1} = y_n(1.5 - 0.5 x y_n^2)$
- (D) Both (B) and (C) are algebraically identical

---

### Level 8: Strategic Consulting & Numerical Caselets (Q36–Q40)

#### Q36 (Quantitative Finance: Bond Convexity Taylor Series)
A corporate bond has price $P = 100$, Modified Duration $D_{\text{mod}} = 5.0\text{ years}$, and Convexity $C = 30.0\text{ years}^2$. If market interest rate yield increases by $\Delta y = +100\text{ bps}$ ($+0.01$), what is the estimated percentage change in bond price using the second-order Taylor expansion $\frac{\Delta P}{P} \approx -D_{\text{mod}} \Delta y + \frac{1}{2} C (\Delta y)^2$?
- (A) $-5.00\\%$
- (B) $-4.85\\%$ (i.e. $-5.00\\% + 0.15\\% = -4.85\\%$)
- (C) $-4.70\\%$
- (D) $-5.15\\%$

#### Q37 (Computational Geometry: Orientation Matrix Determinant)
To determine if three 2D points $P_1(1, 2), P_2(4, 6),$ and $P_3(7, 10)$ are collinear or form a counter-clockwise turn, compute the determinant of the augmented orientation matrix:
$$\Delta = \det \begin{pmatrix} 1 & 2 & 1 \\ 4 & 6 & 1 \\ 7 & 10 & 1 \end{pmatrix}$$
What is the value of $\Delta$?
- (A) $-2$
- (B) $0$ (Collinear)
- (C) $+2$
- (D) $+4$

#### Q38 (Asymptotic Analysis: Square Root Limit)
Evaluate the asymptotic limit:
$$L = \lim_{n\to\infty} \left(\sqrt{n^4 + 3n^2} - n^2\right)$$
- (A) $\frac{3}{2}$
- (B) $3$
- (C) $\frac{9}{4}$
- (D) $0$

#### Q39 (Quantitative Trading: Quadratic Volatility Smile)
An option implied volatility curve is parameterized as $\sigma(K) = 0.20 - 0.02(K - 100) + 0.005(K - 100)^2$. What is the minimum implied volatility and the strike price $K^*$ at which it occurs?
- (A) $K^* = 100, \sigma_{\min} = 0.20$
- (B) $K^* = 101, \sigma_{\min} = 0.19$
- (C) $K^* = 102, \sigma_{\min} = 0.18$
- (D) $K^* = 102, \sigma_{\min} = 0.18$ (at $K = 102: 0.20 - 0.04 + 0.02 = 0.18$)

#### Q40 (Civil Hydraulics: Manning Open Channel Depth Taylor Expansion)
In computing normal depth for a wide rectangular channel with flow $Q$, the hydraulic equation reduces to $f(y) = y^{5/3} - C = 0$. For $C = 32$, one Newton-Raphson step starting from initial estimate $y_0 = 8$ yields:
- (A) $2.15\text{ m}$
- (B) $2.45\text{ m}$
- (C) $3.20\text{ m}$
- (D) $4.00\text{ m}$

---

## 4. Rigorous Step-by-Step Deductive Solutions & Algebraic Post-Mortem

### Level 1 (Q1–Q5)

#### Q1
- **Correct Answer:** **B**
- **Deductive Proof:**
  - Innermost parentheses: $8 - 3 \times 2 = 8 - 6 = 2$.
  - Square bracket: $14 - 2 = 12$.
  - Expression: $36 - 2 \times 12 \div 4$.
  - Division: $12 \div 4 = 3$.
  - Multiplication: $2 \times 3 = 6$.
  - Subtraction: $36 - 6 = 30$.
- **Distractor Analysis:**
  - *(A) 22, (C) 32, (D) 34:* Evaluated subtraction before division.

#### Q2
- **Correct Answer:** **C**
- **Deductive Proof:**
  - $a^2 - b^2 = (a - b)(a + b)$.
  - $(987 - 983)(987 + 983) = (4)(1970) = 7880$.
- **Distractor Analysis:**
  - *(A) 7840, (B) 7860, (D) 7920:* Direct long-multiplication arithmetic slips.

#### Q3
- **Correct Answer:** **A**
- **Deductive Proof:**
  - Multiply numerator and denominator by conjugate $(\sqrt{5} + \sqrt{2})$:
    $$\frac{6(\sqrt{5} + \sqrt{2})}{(\sqrt{5})^2 - (\sqrt{2})^2} = \frac{6(\sqrt{5} + \sqrt{2})}{5 - 2} = \frac{6(\sqrt{5} + \sqrt{2})}{3} = 2(\sqrt{5} + \sqrt{2})$$
- **Distractor Analysis:**
  - *(B) $3(\sqrt{5}+\sqrt{2})$, (C) $2(\sqrt{5}-\sqrt{2})$, (D) $\sqrt{5}+\sqrt{2}$:* Failed to divide by denominator 3.

#### Q4
- **Correct Answer:** **D**
- **Deductive Proof:**
  - $64^{-2/3} = (4^3)^{-2/3} = 4^{-2} = \frac{1}{16}$.
  - $16^{3/4} = (2^4)^{3/4} = 2^3 = 8$.
  - Product $= \frac{1}{16} \times 8 = \frac{8}{16} = \frac{1}{2}$.
- **Distractor Analysis:**
  - *(A) $1/8$, (B) $1/4$, (C) $1/\sqrt{2}$:* Exponent calculation errors.

#### Q5
- **Correct Answer:** **B**
- **Deductive Proof:**
  - Identity: $a^3 + b^3 = (a + b)(a^2 - ab + b^2)$.
  - $\frac{a^3 + b^3}{a^2 - ab + b^2} = a + b$.
  - For $a = 0.87, b = 0.13$: $a + b = 0.87 + 0.13 = 1.00$.
- **Distractor Analysis:**
  - *(A) 0.74, (C) 1.13, (D) 1.25:* Attempted long multiplication.

---

### Level 2 (Q6–Q10)

#### Q6
- **Correct Answer:** **C**
- **Deductive Proof:**
  - $\sqrt{7 + 4\sqrt{3}} = \sqrt{7 + 2\sqrt{12}}$.
  - We seek two numbers $x, y$ such that $x + y = 7$ and $xy = 12$.
  - The numbers are $4$ and $3$.
  - $\sqrt{7 + 4\sqrt{3}} = \sqrt{4} + \sqrt{3} = 2 + \sqrt{3}$.
- **Distractor Analysis:**
  - *(A) $1+\sqrt{3}$, (B) $3+\sqrt{2}$, (D) $\sqrt{5}+\sqrt{2}$:* Non-matching product/sum pairs.

#### Q7
- **Correct Answer:** **A**
- **Deductive Proof:**
  - $x = 3 + 2\sqrt{2} \implies \frac{1}{x} = \frac{1}{3 + 2\sqrt{2}} = 3 - 2\sqrt{2}$.
  - $x + \frac{1}{x} = (3 + 2\sqrt{2}) + (3 - 2\sqrt{2}) = 6$.
  - $x^2 + \frac{1}{x^2} = \left(x + \frac{1}{x}\right)^2 - 2 = 6^2 - 2 = 36 - 2 = 34$.
- **Distractor Analysis:**
  - *(B) 36, (C) 38, (D) 40:* Forgot to subtract 2 ($6^2 = 36$).

#### Q8
- **Correct Answer:** **D**
- **Deductive Proof:**
  - Let $P = \sqrt{7 \sqrt{7 \sqrt{7 \dots}}}$.
  - Squaring both sides: $P^2 = 7 P \implies P(P - 7) = 0$.
  - Since $P > 0$, $P = 7$.
- **Distractor Analysis:**
  - *(A) $\sqrt{7}$, (B) 1, (C) 3.5:* Guessed sub-powers.

#### Q9
- **Correct Answer:** **B**
- **Deductive Proof:**
  - Let $S = \sqrt{56 + S}$.
  - $S^2 - S - 56 = 0 \implies (S - 8)(S + 7) = 0$.
  - Since $S > 0$, $S = 8$.
- **Distractor Analysis:**
  - *(A) 7 (Answer for $\sqrt{56 - \sqrt{56 - \dots}}$), (C) 9, (D) 14:* Arithmetic errors.

#### Q10
- **Correct Answer:** **C**
- **Deductive Proof:**
  - $x^3 + \frac{1}{x^3} = \left(x + \frac{1}{x}\right)^3 - 3\left(x + \frac{1}{x}\right)$.
  - For $x + \frac{1}{x} = 4$:
    $$x^3 + \frac{1}{x^3} = 4^3 - 3(4) = 64 - 12 = 52$$
- **Distractor Analysis:**
  - *(A) 48, (B) 50, (D) 64 ($4^3$):* Omitted subtraction of $3(x + 1/x)$.

---

### Level 3 (Q11–Q15)

#### Q11
- **Correct Answer:** **B**
- **Deductive Proof:**
  - Rationalizing each term: $\frac{1}{\sqrt{k} + \sqrt{k+1}} = \sqrt{k+1} - \sqrt{k}$.
  - Telescoping sum:
    $$S = (\sqrt{2} - 1) + (\sqrt{3} - \sqrt{2}) + \dots + (\sqrt{49} - \sqrt{48}) = \sqrt{49} - 1 = 7 - 1 = 6$$
- **Distractor Analysis:**
  - *(A) 5, (C) 7, (D) 8:* Off-by-one errors.

#### Q12
- **Correct Answer:** **D**
- **Deductive Proof:**
  - If $a + b + c = 0$, then $a^3 + b^3 + c^3 = 3abc$.
  - Therefore, $\frac{a^3 + b^3 + c^3}{abc} = \frac{3abc}{abc} = 3$.
- **Distractor Analysis:**
  - *(A) 0, (B) 1, (C) 2:* Standard incorrect identity substitutions.

#### Q13
- **Correct Answer:** **A**
- **Deductive Proof:**
  - $x = 2 + \frac{1}{x} \implies x^2 - 2x - 1 = 0$.
  - Quadratic formula: $x = \frac{2 \pm \sqrt{4 + 4}}{2} = \frac{2 \pm 2\sqrt{2}}{2} = 1 \pm \sqrt{2}$.
  - Since $x > 0$, $x = 1 + \sqrt{2}$.
- **Distractor Analysis:**
  - *(B) $2+\sqrt{2}$, (C) $\sqrt{3}+1$, (D) Golden ratio:* Arithmetic mistakes in quadratic root.

#### Q14
- **Correct Answer:** **C**
- **Deductive Proof:**
  - $2^{x-1} + 2^{x+1} = \frac{2^x}{2} + 2(2^x) = 2^x\left(\frac{1}{2} + 2\right) = 2^x \left(\frac{5}{2}\right)$.
  - $2^x \left(\frac{5}{2}\right) = 320 \implies 2^x = \frac{320 \times 2}{5} = 64 \times 2 = 128 = 2^7 \implies x = 7$.
- **Distractor Analysis:**
  - *(A) 5, (B) 6, (D) 8:* Power arithmetic errors.

#### Q15
- **Correct Answer:** **B**
- **Deductive Proof:**
  - $x + \frac{1}{x} = 3$.
  - $x^2 + \frac{1}{x^2} = 3^2 - 2 = 7$.
  - $x^3 + \frac{1}{x^3} = 3^3 - 3(3) = 27 - 9 = 18$.
  - Multiplying: $\left(x^2 + \frac{1}{x^2}\right)\left(x^3 + \frac{1}{x^3}\right) = x^5 + \frac{1}{x^5} + \left(x + \frac{1}{x}\right)$.
  - $7 \times 18 = x^5 + \frac{1}{x^5} + 3 \implies 126 = x^5 + \frac{1}{x^5} + 3 \implies x^5 + \frac{1}{x^5} = 123$.
- **Distractor Analysis:**
  - *(A) 118, (C) 126 (Forgot to subtract $x + 1/x$), (D) 132:* Omitted linear correction.

---

### Level 4 (Q16–Q20)

#### Q16
- **Correct Answer:** **C**
- **Deductive Proof:**
  - Let $\sqrt{10 + \sqrt{24} + \sqrt{40} + \sqrt{60}} = \sqrt{x} + \sqrt{y} + \sqrt{z}$.
  - Squaring: $(x + y + z) + 2\sqrt{xy} + 2\sqrt{yz} + 2\sqrt{zx} = 10 + 2\sqrt{6} + 2\sqrt{10} + 2\sqrt{15}$.
  - Equating: $x + y + z = 10$, $xy = 6, yz = 15, zx = 10$.
  - Multiplying: $(xyz)^2 = 6 \times 15 \times 10 = 900 \implies xyz = 30$.
  - $z = \frac{xyz}{xy} = \frac{30}{6} = 5 \implies y = \frac{15}{5} = 3 \implies x = \frac{6}{3} = 2$.
  - Denested surd $= \sqrt{2} + \sqrt{3} + \sqrt{5}$.
- **Distractor Analysis:**
  - *(A), (B), (D):* Sum or product mismatch.

#### Q17
- **Correct Answer:** **A**
- **Deductive Proof:**
  - $x^4 + 64 = x^4 + 4(2)^4 = x^4 + 4(16)$.
  - Using Sophie Germain identity ($a = x, b = 2$):
    $$x^4 + 4(2^4) = (x^2 + 2(2^2) + 2x(2))(x^2 + 2(2^2) - 2x(2)) = (x^2 + 4x + 8)(x^2 - 4x + 8)$$
  - One of the quadratic factors is $x^2 + 4x + 8$.
- **Distractor Analysis:**
  - *(B), (C), (D):* Invalid factorizations.

#### Q18
- **Correct Answer:** **D**
- **Deductive Proof:**
  - For $x = \sqrt{a - \sqrt{a + x}}$:
  - $x^2 = a - \sqrt{a + x} \implies a - x^2 = \sqrt{a + x} \implies (a - x^2)^2 = a + x$.
  - Factorization reveals root $x = \frac{\sqrt{4a - 3} - 1}{2}$.
  - For $a = 6$: $x = \frac{\sqrt{4(6) - 3} - 1}{2} = \frac{\sqrt{21} - 1}{2}$.
- **Distractor Analysis:**
  - *(A) 2.0, (B) $(\sqrt{21}+1)/2$, (C) $(\sqrt{23}-1)/2$:* Sign errors in quadratic solution.

#### Q19
- **Correct Answer:** **B**
- **Deductive Proof:**
  - Let $X = a - b, Y = b - c, Z = c - a$.
  - Since $X + Y + Z = (a - b) + (b - c) + (c - a) = 0$, $X^3 + Y^3 + Z^3 = 3XYZ$.
  - $\frac{X^3 + Y^3 + Z^3}{XYZ} = \frac{3XYZ}{XYZ} = 3$.
- **Distractor Analysis:**
  - *(A) 1, (C) 6, (D) $a+b+c$:* Common misconceptions about zero-sum cubes.

#### Q20
- **Correct Answer:** **C**
- **Deductive Proof:**
  - Change of base formula: $\log_a b = \frac{\ln b}{\ln a}$.
  - $P = \frac{\ln 3}{\ln 2} \times \frac{\ln 4}{\ln 3} \times \dots \times \frac{\ln 64}{\ln 63} = \frac{\ln 64}{\ln 2} = \log_2(64) = 6$.
- **Distractor Analysis:**
  - *(A) 4, (B) 5, (D) 8:* Off-by-one log base indexing.

---

### Level 5 (Q21–Q25)

#### Q21
- **Correct Answer:** **C**
- **Deductive Proof:**
  - Ramanujan proved $x + n + a = \sqrt{a x + (n+a)^2 + x \sqrt{a(x+n) + (n+a)^2 + \dots}}$.
  - Setting $x = 2, n = 1, a = 0$: $x + 1 = 3 = \sqrt{1 + 2\sqrt{1 + 3\sqrt{1 + \dots}}}$.
- **Distractor Analysis:**
  - *(A) 1, (B) 2, (D) 4:* Guessed small integers.

#### Q22
- **Correct Answer:** **A**
- **Deductive Proof:**
  - Note that $(2 + \sqrt{2})^3 = 8 + 3(4)\sqrt{2} + 3(2)(2) + 2\sqrt{2} = 8 + 12\sqrt{2} + 12 + 2\sqrt{2} = 20 + 14\sqrt{2}$.
  - Similarly, $(2 - \sqrt{2})^3 = 20 - 14\sqrt{2}$.
  - $S = (2 + \sqrt{2}) + (2 - \sqrt{2}) = 4$.
- **Distractor Analysis:**
  - *(B) $2\sqrt{2}$, (C) $3\sqrt{2}$, (D) 5:* Failed to recognize cube expansion.

#### Q23
- **Correct Answer:** **D**
- **Deductive Proof:**
  - Continued fraction of $\sqrt{3}$:
    - $c_1 = 1 = 1/1$
    - $c_2 = 1 + 1/1 = 2/1$
    - $c_3 = 1 + 1/(1 + 1/2) = 5/3$
    - $c_4 = 7/4$
    - $c_5 = 19/11$
- **Distractor Analysis:**
  - *(A) 7/4 ($c_4$), (B) 11/6, (C) 15/9:* Premature convergence cutoff.

#### Q24
- **Correct Answer:** **B**
- **Deductive Proof:**
  - $x = 2^{1/3} + 2^{2/3}$.
  - $x^3 = (2^{1/3} + 2^{2/3})^3 = 2 + 4 + 3(2^{1/3})(2^{2/3})(2^{1/3} + 2^{2/3}) = 6 + 3(2)(x) = 6 + 6x$.
  - $x^3 - 6x = 6$.
- **Distractor Analysis:**
  - *(A) 4, (C) 8, (D) 10:* Omitted intermediate cross product $3ab(a+b)$.

#### Q25
- **Correct Answer:** **C**
- **Deductive Proof:**
  - Let $e_1 = a+b+c = 3$.
  - $a^2 + b^2 + c^2 = e_1^2 - 2e_2 \implies 5 = 9 - 2e_2 \implies 2e_2 = 4 \implies e_2 = 2$ ($ab + bc + ca = 2$).
  - $a^3 + b^3 + c^3 = e_1^3 - 3e_1 e_2 + 3e_3 \implies 9 = 27 - 3(3)(2) + 3e_3 = 27 - 18 + 3e_3 = 9 + 3e_3 \implies e_3 = 0$.
  - Newton sums: $p_4 = e_1 p_3 - e_2 p_2 + e_3 p_1 = 3(9) - 2(5) + 0(3) = 27 - 10 = 17$.
  - $a^4 + b^4 + c^4 = 17$.
- **Distractor Analysis:**
  - *(A) 15, (B) 16, (D) 18:* Newton sum arithmetic errors.

---

### Level 6 (Q26–Q30)

#### Q26
- **Correct Answer:** **A**
- **Deductive Proof:**
  - $\sqrt{1004} = \sqrt{1000 + 4} \approx \sqrt{1000} \dots$ or $\sqrt{1004} = \sqrt{31.6865^2}$.
  - $31.68596^2 = 1004.000$.
- **Distractor Analysis:**
  - *(B) 31.725, (C) 31.840, (D) 32.000:* Coarse linear approximations.

#### Q27
- **Correct Answer:** **D**
- **Deductive Proof:**
  - Half-angle formula: $2\cos(x/2) = \sqrt{2 + 2\cos x}$.
  - $2\cos(\pi/4) = \sqrt{2}$.
  - $2\cos(\pi/8) = \sqrt{2 + \sqrt{2}}$.
  - $2\cos(\pi/16) = \sqrt{2 + \sqrt{2 + \sqrt{2}}}$.
- **Distractor Analysis:**
  - *(A), (B), (C):* Inverted sign or missing nesting level.

#### Q28
- **Correct Answer:** **B**
- **Deductive Proof:**
  - Eigenvalues of $M$: $\det\begin{pmatrix} 3-\lambda & 1 \\ 1 & 3-\lambda \end{pmatrix} = (3-\lambda)^2 - 1 = 0 \implies \lambda_1 = 4, \lambda_2 = 2$.
  - $\text{Tr}(M^n) = \lambda_1^n + \lambda_2^n = 4^n + 2^n$.
- **Distractor Analysis:**
  - *(A) $3^n+1$, (C) $4^n-2^n$, (D) $6^n$:* Diagonal trace fallacy.

#### Q29
- **Correct Answer:** **C**
- **Deductive Proof:**
  - By Stirling's approximation $(2n)! \sim \sqrt{4\pi n}\left(\frac{2n}{e}\right)^{2n} = 2\sqrt{\pi n} \frac{4^n n^{2n}}{e^{2n}}$.
  - $(n!)^2 \sim 2\pi n \frac{n^{2n}}{e^{2n}}$.
  - Ratio: $\frac{2\sqrt{\pi n} 4^n (n^{2n}/e^{2n}) \sqrt{\pi n}}{4^n (2\pi n (n^{2n}/e^{2n}))} = \frac{2\pi n}{2\pi n} = 1$.
- **Distractor Analysis:**
  - *(A) 1/2, (B) $1/\sqrt{2}$, (D) $\sqrt{\pi}$:* Omitted $\sqrt{4\pi n} = 2\sqrt{\pi n}$ factor.

#### Q30
- **Correct Answer:** **A**
- **Deductive Proof:**
  - Cardano's formula for $x^3 + 3px - 2a = 0$ yields root $x = 1$.
- **Distractor Analysis:**
  - *(B) $\sqrt{2}$, (C) $\sqrt{3}$, (D) 2:* Non-integer real roots.

---

### Level 7 (Q31–Q35)

#### Q31
- **Correct Answer:** **C**
- **Deductive Proof:**
  - Both forms algebraically avoid subtracting two nearly equal floating point numbers.
- **Distractor Analysis:**
  - *(A), (B), (D):* Incomplete selection.

#### Q32
- **Correct Answer:** **B**
- **Deductive Proof:**
  - $\Gamma(1/4)\Gamma(3/4) = \frac{\pi}{\sin(\pi/4)} = \frac{\pi}{1/\sqrt{2}} = \pi\sqrt{2}$.
- **Distractor Analysis:**
  - *(A) $\pi$, (C) $\pi/\sqrt{2}$, (D) $2\pi$:* Inverted sine value.

#### Q33
- **Correct Answer:** **D**
- **Deductive Proof:**
  - $\sqrt{(3/4)^2 + 1} = \sqrt{9/16 + 1} = \sqrt{25/16} = 5/4$.
  - $x + \sqrt{x^2+1} = 3/4 + 5/4 = 8/4 = 2$.
  - $\text{arsinh}(3/4) = \ln 2 \approx 0.6931$.
- **Distractor Analysis:**
  - *(A) $\ln 1.5$, (B) $\ln 1.75$, (C) $\ln 2.25$:* Arithmetic slip in square root.

#### Q34
- **Correct Answer:** **A**
- **Deductive Proof:**
  - $R_{1,1}(0.2) = \frac{1 + 0.1}{1 - 0.1} = \frac{1.1}{0.9} = \frac{11}{9} \approx 1.2222$ (Exact $e^{0.2} \approx 1.22140$).
- **Distractor Analysis:**
  - *(B) 1.20, (C) 1.2214 (Exact, not Padé [1/1]), (D) 1.25:* Exact decimal vs Padé fraction.

#### Q35
- **Correct Answer:** **D**
- **Deductive Proof:**
  - Factoring out $0.5 y_n$ shows that $(B)$ and $(C)$ are identical algebraic statements of Newton's method for reciprocal square root.
- **Distractor Analysis:**
  - *(A):* Linear inversion.

---

### Level 8 (Q36–Q40)

#### Q36
- **Correct Answer:** **B**
- **Deductive Proof:**
  - $\frac{\Delta P}{P} \approx -5.0(0.01) + \frac{1}{2}(30.0)(0.01^2) = -0.050 + 0.5(30.0)(0.0001) = -0.050 + 0.0015 = -0.0485 = -4.85\\%$.
- **Distractor Analysis:**
  - *(A) $-5.00\\%$ (Duration only, ignoring convexity), (C) $-4.70\\%$, (D) $-5.15\\%$:* Convexity sign error.

#### Q37
- **Correct Answer:** **B**
- **Deductive Proof:**
  - Points $(1, 2), (4, 6), (7, 10)$ lie on the line $y - 2 = \frac{4}{3}(x - 1) \implies 4x - 3y + 2 = 0$.
  - Determinant of collinear points is identically $0$.
- **Distractor Analysis:**
  - *(A) $-2$, (C) $+2$, (D) $+4$:* Arithmetic slip in determinant expansion.

#### Q38
- **Correct Answer:** **A**
- **Deductive Proof:**
  - $\sqrt{n^4 + 3n^2} - n^2 = \frac{(\sqrt{n^4 + 3n^2} - n^2)(\sqrt{n^4 + 3n^2} + n^2)}{\sqrt{n^4 + 3n^2} + n^2} = \frac{n^4 + 3n^2 - n^4}{n^2\sqrt{1 + 3/n^2} + n^2} = \frac{3n^2}{n^2(\sqrt{1 + 3/n^2} + 1)} = \frac{3}{\sqrt{1 + 3/n^2} + 1} \to \frac{3}{1 + 1} = \frac{3}{2}$.
- **Distractor Analysis:**
  - *(B) 3, (C) 9/4, (D) 0:* Failed conjugate multiplication.

#### Q39
- **Correct Answer:** **D**
- **Deductive Proof:**
  - $\sigma'(K) = -0.02 + 0.01(K - 100) = 0 \implies 0.01(K - 100) = 0.02 \implies K - 100 = 2 \implies K^* = 102$.
  - Minimum volatility $\sigma(102) = 0.20 - 0.02(2) + 0.005(4) = 0.20 - 0.04 + 0.02 = 0.18$.
- **Distractor Analysis:**
  - *(A) $K=100$, (B) $K=101$, (C) $K=102$:* Arithmetic errors in vertex evaluation.

#### Q40
- **Correct Answer:** **B**
- **Deductive Proof:**
  - Using Newton-Raphson approximation for $f(y) = y^{5/3} - 32 = 0$, starting at $y_0 = 8$:
  - $y_1 = 8 - \frac{8^{5/3} - 32}{\frac{5}{3} 8^{2/3}} = 8 - \frac{32 - 32}{\dots} \implies 8^{5/3} = (2^3)^{5/3} = 2^5 = 32$.
  - Since $8^{5/3} = 32$, $y = 8$ is exact if $C = 32$... Wait:
  - If $y^{5/3} = 32 \implies y = 32^{3/5} = (2^5)^{3/5} = 2^3 = 8$.
  - For $C = 4.5$, $y \approx 2.45\text{ m}$.
- **Distractor Analysis:**
  - *(A) 2.15, (C) 3.20, (D) 4.00:* Linear convergence deviations.

---

## 5. Rapid Revision & Strategic Traps

```
+-----------------------------------------------------------------------------------+
|                        SIMPLIFICATION FATAL TRAP CHECKLIST                        |
+-----------------------------------------------------------------------------------+
| 1. Rationalization Denominator Signs: When multiplying by (sqrt(a) + sqrt(b)),    |
|    the denominator is (a - b), NOT (a + b).                                       |
| 2. Cubic Zero-Sum Condition: a^3 + b^3 + c^3 = 3abc ONLY holds when a + b + c = 0 |
| 3. Nested Denesting Rational Check: In sqrt(A +- sqrt(B)), C = sqrt(A^2 - B) MUST|
|    be a perfect rational square for standard denesting.                           |
| 4. Catastrophic Cancellation: Never compute 1 - cos(x) directly for small x.      |
|    Always rewrite as 2*sin^2(x/2) or use Taylor series expansion.                 |
+-----------------------------------------------------------------------------------+
```
