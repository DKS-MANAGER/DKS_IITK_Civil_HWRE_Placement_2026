# Data Interpretation: Data Sufficiency

> **Priority:** P0 · **Role relevance:** Critical (Universal across Management Consulting, Product Management, Quantitative Trading, Analytics, Core Engineering & Banking)  
> **Difficulty range:** Foundation → 3-Statement Extreme & Hybrid Business Sufficiency · **Target speed:** 45–60 sec (Direct Structural Invariance) – 100–150 sec (Multi-Branch Non-Linear / 3-Statement Constraints)

---

## 1. Mathematical & Theoretical Framework

### 1.1 The Epistemology of Data Sufficiency: Uniqueness vs. Computability
Data Sufficiency (DS) does **not** evaluate your ability to execute tedious mechanical arithmetic. Instead, it measures **deductive completeness**: determining whether a formal mathematical proposition possesses a **unique, well-defined truth value or solution state** within a constrained parameter space.

```
+---------------------------------------------------------------------------------------------------+
|                                 THE DATA SUFFICIENCY DECISION MATRIX                              |
+---------------------------------------------------------------------------------------------------+
| Question Archetype | Sufficient Condition                                | Insufficient Condition |
|--------------------+-----------------------------------------------------+------------------------|
| Value Question     | Exactly ONE unique numerical value is determined.    | Two or more distinct   |
| (e.g., "What is x?")| Any ambiguity renders the statement INSUFFICIENT.   | candidate values exist.|
|--------------------+-----------------------------------------------------+------------------------|
| Yes/No Question    | The proposition yields a definitive YES or a        | The statement permits  |
| (e.g., "Is x > 0?")| definitive NO across 100% of the feasible domain.   | BOTH "Yes" and "No"    |
|                    | (A guaranteed NO is 100% SUFFICIENT!).              | branches to occur.     |
+---------------------------------------------------------------------------------------------------+
```

---

### 1.2 The Two-Statement Elimination Protocol (Standard 5 Options)

For standard two-statement Data Sufficiency questions, the answer choices follow a canonical elimination hierarchy:

- **(A)** Statement (1) ALONE is sufficient, but Statement (2) alone is NOT sufficient.
- **(B)** Statement (2) ALONE is sufficient, but Statement (1) alone is NOT sufficient.
- **(C)** BOTH statements TOGETHER are sufficient, but NEITHER statement ALONE is sufficient.
- **(D)** EACH statement ALONE is sufficient.
- **(E)** Statements (1) and (2) TOGETHER are NOT sufficient (further information is required).

```
                            [ Analyze Question Stem ]
                            Identify Domain & Target
                                       |
                                       v
                            [ Test Statement (1) ]
                                  /         \
                             Sufficient    Not Sufficient
                                /             \
                   Eliminate B, C, E         Eliminate A, D
                              /                 \
                     [ Test Statement (2) ]    [ Test Statement (2) ]
                      /                  \      /                  \
                Sufficient        Not Suff.  Sufficient         Not Suff.
                    |                 |          |                  |
                   (D)               (A)        (B)       [ Combine (1) + (2) ]
                                                           /                 \
                                                     Sufficient           Not Suff.
                                                         |                    |
                                                        (C)                  (E)
```

---

### 1.3 The 3-Statement Combinatorial Architecture

In Tier-1 banking, McKinsey PST, and advanced GMAT/CAT formats, problems feature **three independent statements**: $(1), (2),$ and $(3)$. Candidates must evaluate combinatorial subsets:

1. **Singleton Sufficiency**: Does any statement alone resolve the prompt?
2. **Pairwise Redundancy**: Can any pair of statements resolve the prompt (e.g., $\{1, 2\}$, $\{2, 3\}$, or $\{1, 3\}$)?
3. **Strict Intersection**: Are all three statements required simultaneously (i.e., $(1) \cap (2) \cap (3)$)?
4. **Permanent Underdeterminedness**: Does the degrees-of-freedom count strictly exceed independent constraint equations?

---

## 2. Master Answer Key (Q1–Q40)

| Question | Level | Archetype / Domain | Correct Answer | Core Mathematical Principle |
|:---:|:---:|:---|:---:|:---|
| **Q1** | Level 1 | Linear Single Variable | **A** | Direct linear inversion: 1 equation in 1 unknown |
| **Q2** | Level 1 | Integer Sign Parity | **A** | $n^3 > 0 \iff n > 0$; even powers lose sign information |
| **Q3** | Level 1 | Circle Geometry | **D** | Radius $r$ uniquely determined by either $C = 2\pi r$ or $d = 2r$ |
| **Q4** | Level 1 | Homogeneous Ratio | **A** | $5p - 3q = 0 \implies p/q = 3/5$; sum alone cannot fix ratio |
| **Q5** | Level 1 | LCM / Coprime Divisibility | **C** | $\gcd(2, 3) = 1 \implies \text{lcm}(2, 3) = 6$; single factors insufficient |
| **Q6** | Level 2 | Dependent Linear System | **D** | Both statements are scalar multiples yielding $x + y = 9$ |
| **Q7** | Level 2 | Quadratic Discriminant | **B** | Statement (2) is a perfect square $(x-4)^2 = 0 \implies x = 4$ |
| **Q8** | Level 2 | Arithmetic Mean | **B** | Total sum over total count yields exact mean |
| **Q9** | Level 2 | Linear Diophantine Equation | **A** | $7p + 11n = 100$ has a unique positive integer pair $(8, 4)$ |
| **Q10** | Level 2 | Rectangle Dimensions | **C** | $L + W = 14$ and $LW = 48$ with $L > W$ yields $(8, 6)$ |
| **Q11** | Level 3 | Absolute Value Inequality | **A** | $x^2 < 9 \iff \|x\| < 3$; one-sided bound allows unbounded negatives |
| **Q12** | Level 3 | Consecutive Integer Factorials | **A** | Even $n$ guarantees consecutive even factors $\implies$ divisible by 24 |
| **Q13** | Level 3 | Linear Intercepts & Origin | **D** | Both statements establish $y$-intercept $c = 0$ |
| **Q14** | Level 3 | Principle of Inclusion-Exclusion | **C** | $\|A \cup B\| = \|A\| + \|B\| - \|A \cap B\|$ requires both margins |
| **Q15** | Level 3 | Relative Speed of Approach | **B** | Time to meet depends strictly on sum of speeds $(S_1 + S_2)$ |
| **Q16** | Level 4 | Symmetric Quadratic Ambiguity | **E** | System yields unordered set $\{8, 12\}$; $x$ cannot be identified |
| **Q17** | Level 4 | Directional Inequality | **B** | $x - y > 0 \iff x > y$; absolute value magnitude ignores sign |
| **Q18** | Level 4 | Degenerate Variance | **B** | Zero dispersion occurs if and only if all elements are identical |
| **Q19** | Level 4 | Coprime Divisibility Powers | **D** | $\text{lcm}(24, 18) = 72$ and $\text{lcm}(8, 9) = 72$; both force multiple of 72 |
| **Q20** | Level 4 | Triangle Angle Bounds | **D** | Largest angle $< 90^\circ$ and smallest angle sum $> 90^\circ$ both force acute |
| **Q21** | Level 5 | Weighted Mixture Balance | **C** | Combining absolute component costs with mixing weight ratio |
| **Q22** | Level 5 | Harmonic Work Rate Bounds | **C** | Sum of lower bounds exceeds threshold rate $0.25 \implies T < 4$ days |
| **Q23** | Level 5 | Hypergeometric Probability | **A** | Quadratic in integer $R$ yields exactly one domain-valid root |
| **Q24** | Level 5 | Chinese Remainder Theorem | **C** | Coprime moduli $5$ and $6$ uniquely fix state modulo 30 |
| **Q25** | Level 5 | Quadratic Discriminant Sign | **D** | $ac < 0 \implies -4ac > 0 \implies D > 0$; $D > a^2 > 0$ |
| **Q26** | Level 6 | 3-Statement Symmetric Break | **D** | (1)+(2) yields two pairs; (3) orders variables to select unique root |
| **Q27** | Level 6 | 3-Set Venn Partition | **B** | Any two statements form an independent 2-equation linear system |
| **Q28** | Level 6 | Cylinder Parameter Redundancy | **B** | Any pair uniquely fixes $(r, h)$ through algebraic elimination |
| **Q29** | Level 6 | Orthogonal Slopes | **C** | (1) with either (2) or (3) yields $m_1 m_2 = (4/3)(-3/4) = -1$ |
| **Q30** | Level 6 | Ordered Median Constraint | **D** | All 3 statements combine to resolve the system $a < b < c < d < e$ |
| **Q31** | Level 7 | Variable Division Trap | **C** | Dividing inequality by $y$ requires knowing $\text{sgn}(y) > 0$ |
| **Q32** | Level 7 | Root Multiplicity Trap | **B** | $x^2 = 25 \implies x = \pm 5$; absolute difference $|x - 5| = 0 \implies x = 5$ |
| **Q33** | Level 7 | The False C-Trap | **D** | Factorial $p! = 120$ uniquely identifies positive integer $p = 5$ |
| **Q34** | Level 7 | Factored Difference of Squares | **C** | $(x - y) > 0$ and $(x + y) > 0 \implies (x-y)(x+y) = x^2 - y^2 > 0$ |
| **Q35** | Level 7 | Definite "NO" Triangle Inequality | **C** | $5 + 7 = 12 < 13$ violates triangle inequality $\implies$ definitive NO |
| **Q36** | Level 8 | SaaS Enterprise Metrics | **C** | Product of client count and ARPU gives MRR |
| **Q37** | Level 8 | Operating Cash Flow Breakeven | **C** | Revenue minus total OpEx establishes sign of cash flow |
| **Q38** | Level 8 | LTV to CAC Ratio | **C** | $LTV = (ARPU \times GM)/c = \text{₹}20,00,000$; ratio $20/6 = 3.33 > 3$ |
| **Q39** | Level 8 | Production Capacity Optimization | **C** | Line rates combined establish aggregate daily throughput |
| **Q40** | Level 8 | Linear Programming Extreme Point | **D** | Objective function + resource constraints + total availability |

---

## 3. Comprehensive Practice Set (40 Placement Questions)

### Level 1: Foundation (Q1–Q5)

#### Q1
What is the value of the real variable $x$?
- **Statement (1):** $3x + 14 = 47$
- **Statement (2):** $x + 2y = 25$
- **Options:**
  - (A) Statement (1) ALONE is sufficient, but Statement (2) alone is not sufficient.
  - (B) Statement (2) ALONE is sufficient, but Statement (1) alone is not sufficient.
  - (C) BOTH statements TOGETHER are sufficient, but NEITHER statement ALONE is sufficient.
  - (D) EACH statement ALONE is sufficient.
  - (E) Statements (1) and (2) TOGETHER are NOT sufficient.

#### Q2
Is the integer $n$ strictly positive?
- **Statement (1):** $n^3 > 0$
- **Statement (2):** $n^2 > 0$
- **Options:**
  - (A) Statement (1) ALONE is sufficient, but Statement (2) alone is not sufficient.
  - (B) Statement (2) ALONE is sufficient, but Statement (1) alone is not sufficient.
  - (C) BOTH statements TOGETHER are sufficient, but NEITHER statement ALONE is sufficient.
  - (D) EACH statement ALONE is sufficient.
  - (E) Statements (1) and (2) TOGETHER are NOT sufficient.

#### Q3
What is the area of circle $C$?
- **Statement (1):** The circumference of circle $C$ is $12\pi\text{ cm}$.
- **Statement (2):** The diameter of circle $C$ is $12\text{ cm}$.
- **Options:**
  - (A) Statement (1) ALONE is sufficient, but Statement (2) alone is not sufficient.
  - (B) Statement (2) ALONE is sufficient, but Statement (1) alone is not sufficient.
  - (C) BOTH statements TOGETHER are sufficient, but NEITHER statement ALONE is sufficient.
  - (D) EACH statement ALONE is sufficient.
  - (E) Statements (1) and (2) TOGETHER are NOT sufficient.

#### Q4
What is the numerical ratio of $p$ to $q$ (where $q \ne 0$)?
- **Statement (1):** $5p - 3q = 0$
- **Statement (2):** $p + q = 24$
- **Options:**
  - (A) Statement (1) ALONE is sufficient, but Statement (2) alone is not sufficient.
  - (B) Statement (2) ALONE is sufficient, but Statement (1) alone is not sufficient.
  - (C) BOTH statements TOGETHER are sufficient, but NEITHER statement ALONE is sufficient.
  - (D) EACH statement ALONE is sufficient.
  - (E) Statements (1) and (2) TOGETHER are NOT sufficient.

#### Q5
Is the positive integer $k$ divisible by 6?
- **Statement (1):** $k$ is divisible by 2.
- **Statement (2):** $k$ is divisible by 3.
- **Options:**
  - (A) Statement (1) ALONE is sufficient, but Statement (2) alone is not sufficient.
  - (B) Statement (2) ALONE is sufficient, but Statement (1) alone is not sufficient.
  - (C) BOTH statements TOGETHER are sufficient, but NEITHER statement ALONE is sufficient.
  - (D) EACH statement ALONE is sufficient.
  - (E) Statements (1) and (2) TOGETHER are NOT sufficient.

---

### Level 2: Intermediate (Q6–Q10)

#### Q6
What is the value of $(x + y)$?
- **Statement (1):** $2x + 2y = 18$
- **Statement (2):** $4x + 4y = 36$
- **Options:**
  - (A) Statement (1) ALONE is sufficient, but Statement (2) alone is not sufficient.
  - (B) Statement (2) ALONE is sufficient, but Statement (1) alone is not sufficient.
  - (C) BOTH statements TOGETHER are sufficient, but NEITHER statement ALONE is sufficient.
  - (D) EACH statement ALONE is sufficient.
  - (E) Statements (1) and (2) TOGETHER are NOT sufficient.

#### Q7
What is the value of the real number $x$?
- **Statement (1):** $x^2 - 7x + 12 = 0$
- **Statement (2):** $x^2 - 8x + 16 = 0$
- **Options:**
  - (A) Statement (1) ALONE is sufficient, but Statement (2) alone is not sufficient.
  - (B) Statement (2) ALONE is sufficient, but Statement (1) alone is not sufficient.
  - (C) BOTH statements TOGETHER are sufficient, but NEITHER statement ALONE is sufficient.
  - (D) EACH statement ALONE is sufficient.
  - (E) Statements (1) and (2) TOGETHER are NOT sufficient.

#### Q8
What is the arithmetic mean score of a cohort of 10 students in an assessment?
- **Statement (1):** The sum of the scores of the top 5 students is 420.
- **Statement (2):** The sum of the scores of all 10 students is 780.
- **Options:**
  - (A) Statement (1) ALONE is sufficient, but Statement (2) alone is not sufficient.
  - (B) Statement (2) ALONE is sufficient, but Statement (1) alone is not sufficient.
  - (C) BOTH statements TOGETHER are sufficient, but NEITHER statement ALONE is sufficient.
  - (D) EACH statement ALONE is sufficient.
  - (E) Statements (1) and (2) TOGETHER are NOT sufficient.

#### Q9
A student purchased only pens at `₹7` each and notebooks at `₹11` each, purchasing at least one of each item. How many pens did the student purchase?
- **Statement (1):** The total expenditure on pens and notebooks was exactly `₹100`.
- **Statement (2):** The total number of items purchased was 12.
- **Options:**
  - (A) Statement (1) ALONE is sufficient, but Statement (2) alone is not sufficient.
  - (B) Statement (2) ALONE is sufficient, but Statement (1) alone is not sufficient.
  - (C) BOTH statements TOGETHER are sufficient, but NEITHER statement ALONE is sufficient.
  - (D) EACH statement ALONE is sufficient.
  - (E) Statements (1) and (2) TOGETHER are NOT sufficient.

#### Q10
In a rectangle where the length $L$ is strictly greater than the width $W$, what is the length $L$?
- **Statement (1):** The area of the rectangle is $48\text{ cm}^2$.
- **Statement (2):** The perimeter of the rectangle is $28\text{ cm}$.
- **Options:**
  - (A) Statement (1) ALONE is sufficient, but Statement (2) alone is not sufficient.
  - (B) Statement (2) ALONE is sufficient, but Statement (1) alone is not sufficient.
  - (C) BOTH statements TOGETHER are sufficient, but NEITHER statement ALONE is sufficient.
  - (D) EACH statement ALONE is sufficient.
  - (E) Statements (1) and (2) TOGETHER are NOT sufficient.

---

### Level 3: Hard (Q11–Q15)

#### Q11
Is the real number $x$ strictly within the interval $(-3, 3)$ (i.e., is $|x| < 3$)?
- **Statement (1):** $x^2 < 9$
- **Statement (2):** $x < 3$
- **Options:**
  - (A) Statement (1) ALONE is sufficient, but Statement (2) alone is not sufficient.
  - (B) Statement (2) ALONE is sufficient, but Statement (1) alone is not sufficient.
  - (C) BOTH statements TOGETHER are sufficient, but NEITHER statement ALONE is sufficient.
  - (D) EACH statement ALONE is sufficient.
  - (E) Statements (1) and (2) TOGETHER are NOT sufficient.

#### Q12
For a positive integer $n$, is the product $P = n(n+1)(n+2)$ divisible by 12?
- **Statement (1):** $n$ is an even integer.
- **Statement (2):** $n$ is a multiple of 3.
- **Options:**
  - (A) Statement (1) ALONE is sufficient, but Statement (2) alone is not sufficient.
  - (B) Statement (2) ALONE is sufficient, but Statement (1) alone is not sufficient.
  - (C) BOTH statements TOGETHER are sufficient, but NEITHER statement ALONE is sufficient.
  - (D) EACH statement ALONE is sufficient.
  - (E) Statements (1) and (2) TOGETHER are NOT sufficient.

#### Q13
Does the straight line $L: y = mx + c$ in the Cartesian plane pass through the origin $(0,0)$?
- **Statement (1):** Line $L$ passes through the points $(4, 6)$ and $(8, 12)$.
- **Statement (2):** The $x$-intercept of line $L$ is 0.
- **Options:**
  - (A) Statement (1) ALONE is sufficient, but Statement (2) alone is not sufficient.
  - (B) Statement (2) ALONE is sufficient, but Statement (1) alone is not sufficient.
  - (C) BOTH statements TOGETHER are sufficient, but NEITHER statement ALONE is sufficient.
  - (D) EACH statement ALONE is sufficient.
  - (E) Statements (1) and (2) TOGETHER are NOT sufficient.

#### Q14
In a batch of 50 undergraduate engineers, each student is enrolled in at least one of two core subjects: Fluid Mechanics ($F$) or Structural Analysis ($S$). How many students are enrolled in BOTH subjects?
- **Statement (1):** 35 students are enrolled in Fluid Mechanics.
- **Statement (2):** 28 students are enrolled in Structural Analysis.
- **Options:**
  - (A) Statement (1) ALONE is sufficient, but Statement (2) alone is not sufficient.
  - (B) Statement (2) ALONE is sufficient, but Statement (1) alone is not sufficient.
  - (C) BOTH statements TOGETHER are sufficient, but NEITHER statement ALONE is sufficient.
  - (D) EACH statement ALONE is sufficient.
  - (E) Statements (1) and (2) TOGETHER are NOT sufficient.

#### Q15
Two express trains $T_1$ and $T_2$ depart simultaneously from terminal stations $A$ and $B$, which are separated by $360\text{ km}$, traveling directly towards each other on parallel tracks. How many hours after departure will they meet?
- **Statement (1):** Train $T_1$ travels at a uniform speed of $70\text{ km/h}$.
- **Statement (2):** The sum of the speeds of $T_1$ and $T_2$ is $120\text{ km/h}$.
- **Options:**
  - (A) Statement (1) ALONE is sufficient, but Statement (2) alone is not sufficient.
  - (B) Statement (2) ALONE is sufficient, but Statement (1) alone is not sufficient.
  - (C) BOTH statements TOGETHER are sufficient, but NEITHER statement ALONE is sufficient.
  - (D) EACH statement ALONE is sufficient.
  - (E) Statements (1) and (2) TOGETHER are NOT sufficient.

---

### Level 4: Very Hard (Q16–Q20)

#### Q16
What is the exact numerical value of the real variable $x$?
- **Statement (1):** $x + y = 20$
- **Statement (2):** $xy = 96$
- **Options:**
  - (A) Statement (1) ALONE is sufficient, but Statement (2) alone is not sufficient.
  - (B) Statement (2) ALONE is sufficient, but Statement (1) alone is not sufficient.
  - (C) BOTH statements TOGETHER are sufficient, but NEITHER statement ALONE is sufficient.
  - (D) EACH statement ALONE is sufficient.
  - (E) Statements (1) and (2) TOGETHER are NOT sufficient.

#### Q17
Is the real variable $x$ strictly greater than $y$?
- **Statement (1):** $|x| > |y|$
- **Statement (2):** $x - y > 0$
- **Options:**
  - (A) Statement (1) ALONE is sufficient, but Statement (2) alone is not sufficient.
  - (B) Statement (2) ALONE is sufficient, but Statement (1) alone is not sufficient.
  - (C) BOTH statements TOGETHER are sufficient, but NEITHER statement ALONE is sufficient.
  - (D) EACH statement ALONE is sufficient.
  - (E) Statements (1) and (2) TOGETHER are NOT sufficient.

#### Q18
What is the standard deviation of the finite dataset $S = \{a, b, c, d, e\}$?
- **Statement (1):** The arithmetic mean of dataset $S$ is 25.
- **Statement (2):** Every element in dataset $S$ is equal to 25 (i.e., $a = b = c = d = e = 25$).
- **Options:**
  - (A) Statement (1) ALONE is sufficient, but Statement (2) alone is not sufficient.
  - (B) Statement (2) ALONE is sufficient, but Statement (1) alone is not sufficient.
  - (C) BOTH statements TOGETHER are sufficient, but NEITHER statement ALONE is sufficient.
  - (D) EACH statement ALONE is sufficient.
  - (E) Statements (1) and (2) TOGETHER are NOT sufficient.

#### Q19
Is the positive integer $M$ divisible by 72?
- **Statement (1):** $M$ is divisible by both 24 and 18.
- **Statement (2):** $M$ is divisible by both 8 and 9.
- **Options:**
  - (A) Statement (1) ALONE is sufficient, but Statement (2) alone is not sufficient.
  - (B) Statement (2) ALONE is sufficient, but Statement (1) alone is not sufficient.
  - (C) BOTH statements TOGETHER are sufficient, but NEITHER statement ALONE is sufficient.
  - (D) EACH statement ALONE is sufficient.
  - (E) Statements (1) and (2) TOGETHER are NOT sufficient.

#### Q20
Is triangle $ABC$ strictly an acute-angled triangle?
- **Statement (1):** The greatest interior angle of triangle $ABC$ is strictly less than $90^\circ$.
- **Statement (2):** The sum of any two interior angles of triangle $ABC$ is strictly greater than $90^\circ$.
- **Options:**
  - (A) Statement (1) ALONE is sufficient, but Statement (2) alone is not sufficient.
  - (B) Statement (2) ALONE is sufficient, but Statement (1) alone is not sufficient.
  - (C) BOTH statements TOGETHER are sufficient, but NEITHER statement ALONE is sufficient.
  - (D) EACH statement ALONE is sufficient.
  - (E) Statements (1) and (2) TOGETHER are NOT sufficient.

---

### Level 5: Expert (Q21–Q25)

#### Q21
What is the cost per kilogram of a blend composed exclusively of tea Grade $A$ and tea Grade $B$?
- **Statement (1):** Grade $A$ costs `₹400/kg` and Grade $B$ costs `₹600/kg`.
- **Statement (2):** Grade $A$ and Grade $B$ are blended in the ratio $3:2$ by weight.
- **Options:**
  - (A) Statement (1) ALONE is sufficient, but Statement (2) alone is not sufficient.
  - (B) Statement (2) ALONE is sufficient, but Statement (1) alone is not sufficient.
  - (C) BOTH statements TOGETHER are sufficient, but NEITHER statement ALONE is sufficient.
  - (D) EACH statement ALONE is sufficient.
  - (E) Statements (1) and (2) TOGETHER are NOT sufficient.

#### Q22
Working concurrently at their respective constant positive rates, can engineers $P, Q,$ and $R$ complete a critical software deployment in strictly less than 4 days?
- **Statement (1):** Working alone, engineer $P$ takes 8 days, and engineer $Q$ takes 12 days.
- **Statement (2):** Working alone, engineer $R$ takes strictly less than 6 days.
- **Options:**
  - (A) Statement (1) ALONE is sufficient, but Statement (2) alone is not sufficient.
  - (B) Statement (2) ALONE is sufficient, but Statement (1) alone is not sufficient.
  - (C) BOTH statements TOGETHER are sufficient, but NEITHER statement ALONE is sufficient.
  - (D) EACH statement ALONE is sufficient.
  - (E) Statements (1) and (2) TOGETHER are NOT sufficient.

#### Q23
An urn contains exactly 10 balls, each colored either Red or Blue. If two balls are drawn at random simultaneously without replacement, what is the probability that both drawn balls are Red?
- **Statement (1):** The probability of drawing at least one Red ball is $2/3$.
- **Statement (2):** The probability of drawing two balls of different colors is $8/15$.
- **Options:**
  - (A) Statement (1) ALONE is sufficient, but Statement (2) alone is not sufficient.
  - (B) Statement (2) ALONE is sufficient, but Statement (1) alone is not sufficient.
  - (C) BOTH statements TOGETHER are sufficient, but NEITHER statement ALONE is sufficient.
  - (D) EACH statement ALONE is sufficient.
  - (E) Statements (1) and (2) TOGETHER are NOT sufficient.

#### Q24
What is the remainder when the positive integer $N$ is divided by 30?
- **Statement (1):** When $N$ is divided by 5, the remainder is 3.
- **Statement (2):** When $N$ is divided by 6, the remainder is 2.
- **Options:**
  - (A) Statement (1) ALONE is sufficient, but Statement (2) alone is not sufficient.
  - (B) Statement (2) ALONE is sufficient, but Statement (1) alone is not sufficient.
  - (C) BOTH statements TOGETHER are sufficient, but NEITHER statement ALONE is sufficient.
  - (D) EACH statement ALONE is sufficient.
  - (E) Statements (1) and (2) TOGETHER are NOT sufficient.

#### Q25
Does the quadratic equation $ax^2 + bx + c = 0$ (where $a \ne 0$ and $a, b, c \in \mathbb{R}$) possess two distinct real roots?
- **Statement (1):** $ac < 0$
- **Statement (2):** $b^2 - 4ac > a^2$
- **Options:**
  - (A) Statement (1) ALONE is sufficient, but Statement (2) alone is not sufficient.
  - (B) Statement (2) ALONE is sufficient, but Statement (1) alone is not sufficient.
  - (C) BOTH statements TOGETHER are sufficient, but NEITHER statement ALONE is sufficient.
  - (D) EACH statement ALONE is sufficient.
  - (E) Statements (1) and (2) TOGETHER are NOT sufficient.

---

### Level 6: Extreme 3-Statement Sufficiency (Q26–Q30)

#### Q26
What is the exact value of the real variable $x$?
- **Statement (1):** $x + y = 20$
- **Statement (2):** $xy = 96$
- **Statement (3):** $x > y > 0$
- **Options:**
  - (A) Statement (1) alone is sufficient.
  - (B) Statements (1) and (2) together are sufficient, but (3) is not needed.
  - (C) Statements (1) and (3) together are sufficient.
  - (D) All three statements (1), (2), and (3) together are required and sufficient.
  - (E) Statements (1), (2), and (3) together are NOT sufficient.

#### Q27
In a cohort of 100 students, each student studies at least one of three subjects: Physics ($P$), Chemistry ($C$), and Mathematics ($M$). How many students study ALL THREE subjects?
- **Statement (1):** Exactly 50 students study Physics, 50 study Chemistry, and 50 study Mathematics.
- **Statement (2):** Exactly 30 students study exactly two of the three subjects.
- **Statement (3):** Exactly 60 students study exactly one of the three subjects.
- **Options:**
  - (A) Statement (1) alone is sufficient.
  - (B) Any two of the three statements together are sufficient.
  - (C) Statements (1) and (2) together are sufficient, but (3) is required if (1) is absent.
  - (D) All three statements together are necessary.
  - (E) Statements (1), (2), and (3) together are NOT sufficient.

#### Q28
What is the total volume of a solid right circular cylinder?
- **Statement (1):** The curved surface area is $120\pi\text{ cm}^2$.
- **Statement (2):** The total surface area is $192\pi\text{ cm}^2$.
- **Statement (3):** The height of the cylinder is $10\text{ cm}$.
- **Options:**
  - (A) Statement (1) alone is sufficient.
  - (B) Any two of the three statements together are sufficient.
  - (C) Statements (1) and (2) together are sufficient, but (3) is strictly required for (1).
  - (D) All three statements together are necessary.
  - (E) Statements (1), (2), and (3) together are NOT sufficient.

#### Q29
Are the two straight lines $L_1$ and $L_2$ mutually perpendicular in the coordinate plane?
- **Statement (1):** Line $L_1$ passes through $(0, 0)$ and $(3, 4)$.
- **Statement (2):** Line $L_2$ has an $x$-intercept of 4 and a $y$-intercept of 3.
- **Statement (3):** Line $L_2$ is parallel to the linear locus $3x + 4y = 12$.
- **Options:**
  - (A) Statement (1) alone is sufficient.
  - (B) Statements (2) and (3) together are sufficient.
  - (C) Statement (1) combined with EITHER Statement (2) OR Statement (3) is sufficient.
  - (D) All three statements together are necessary.
  - (E) Statements (1), (2), and (3) together are NOT sufficient.

#### Q30
What is the median of a dataset of five distinct integers $\{a, b, c, d, e\}$ arranged in strictly ascending order: $a < b < c < d < e$?
- **Statement (1):** The arithmetic mean of the dataset is 20.
- **Statement (2):** The range of the dataset is 16, and the smallest integer is $a = 12$.
- **Statement (3):** The integers form an arithmetic progression where $c = (b + d)/2$ and $d - b = 6$.
- **Options:**
  - (A) Statement (1) alone is sufficient.
  - (B) Statements (1) and (2) together are sufficient.
  - (C) Statements (2) and (3) together are sufficient.
  - (D) All three statements (1), (2), and (3) together are necessary and sufficient.
  - (E) Statements (1), (2), and (3) together are NOT sufficient.

---

### Level 7: Trap & Boundary Inferences (Q31–Q35)

#### Q31 (The Division-by-Variable Inequality Trap)
Is the inequality $\frac{x}{y} > 1$ satisfied?
- **Statement (1):** $x > y$
- **Statement (2):** $y > 0$
- **Options:**
  - (A) Statement (1) ALONE is sufficient, but Statement (2) alone is not sufficient.
  - (B) Statement (2) ALONE is sufficient, but Statement (1) alone is not sufficient.
  - (C) BOTH statements TOGETHER are sufficient, but NEITHER statement ALONE is sufficient.
  - (D) EACH statement ALONE is sufficient.
  - (E) Statements (1) and (2) TOGETHER are NOT sufficient.

#### Q32 (The Root Multiplicity & Sign Trap)
Is the real variable $x$ equal to 5?
- **Statement (1):** $x^2 = 25$
- **Statement (2):** $|x - 5| = 0$
- **Options:**
  - (A) Statement (1) ALONE is sufficient, but Statement (2) alone is not sufficient.
  - (B) Statement (2) ALONE is sufficient, but Statement (1) alone is not sufficient.
  - (C) BOTH statements TOGETHER are sufficient, but NEITHER statement ALONE is sufficient.
  - (D) EACH statement ALONE is sufficient.
  - (E) Statements (1) and (2) TOGETHER are NOT sufficient.

#### Q33 (The False C-Trap)
If $p$ and $q$ are positive integers, what is the value of $p$?
- **Statement (1):** $p! = 120$
- **Statement (2):** $p + q = 12$ and $q = 7$
- **Options:**
  - (A) Statement (1) ALONE is sufficient, but Statement (2) alone is not sufficient.
  - (B) Statement (2) ALONE is sufficient, but Statement (1) alone is not sufficient.
  - (C) BOTH statements TOGETHER are sufficient, but NEITHER statement ALONE is sufficient.
  - (D) EACH statement ALONE is sufficient.
  - (E) Statements (1) and (2) TOGETHER are NOT sufficient.

#### Q34 (Factored Difference of Squares)
Is $(x^2 - y^2) > 0$?
- **Statement (1):** $x - y > 0$
- **Statement (2):** $x + y > 0$
- **Options:**
  - (A) Statement (1) ALONE is sufficient, but Statement (2) alone is not sufficient.
  - (B) Statement (2) ALONE is sufficient, but Statement (1) alone is not sufficient.
  - (C) BOTH statements TOGETHER are sufficient, but NEITHER statement ALONE is sufficient.
  - (D) EACH statement ALONE is sufficient.
  - (E) Statements (1) and (2) TOGETHER are NOT sufficient.

#### Q35 (The Definite "NO" Triangle Inequality Trap)
Do three distinct points $A, B,$ and $C$ in the Euclidean plane form the vertices of a non-degenerate triangle?
- **Statement (1):** The segment length $AB = 5\text{ cm}$ and segment length $BC = 7\text{ cm}$.
- **Statement (2):** The segment length $AC = 13\text{ cm}$.
- **Options:**
  - (A) Statement (1) ALONE is sufficient, but Statement (2) alone is not sufficient.
  - (B) Statement (2) ALONE is sufficient, but Statement (1) alone is not sufficient.
  - (C) BOTH statements TOGETHER are sufficient, but NEITHER statement ALONE is sufficient.
  - (D) EACH statement ALONE is sufficient.
  - (E) Statements (1) and (2) TOGETHER are NOT sufficient.

---

### Level 8: Hybrid Business & Analytical Sufficiency Caselets (Q36–Q40)

**Scenario Context:**  
Apex Dynamics is a high-growth B2B enterprise software company. The Board of Directors is evaluating quarterly operational cash flows, unit economics, customer churn dynamics, and production capacity.

#### Q36
What was Apex Dynamics' total Monthly Recurring Revenue ($MRR$) at the conclusion of Q4?
- **Statement (1):** Apex had exactly 400 active enterprise client accounts at the end of Q4.
- **Statement (2):** The Average Revenue Per User ($ARPU$) across all active enterprise accounts in Q4 was `₹1,25,000` per month.
- **Options:**
  - (A) Statement (1) ALONE is sufficient, but Statement (2) alone is not sufficient.
  - (B) Statement (2) ALONE is sufficient, but Statement (1) alone is not sufficient.
  - (C) BOTH statements TOGETHER are sufficient, but NEITHER statement ALONE is sufficient.
  - (D) EACH statement ALONE is sufficient.
  - (E) Statements (1) and (2) TOGETHER are NOT sufficient.

#### Q37
Did Apex Dynamics achieve a positive Operating Cash Flow ($OCF > 0$) during the fiscal year?
- **Statement (1):** Total gross revenue generated was `₹120 crore`, with a gross profit margin of 80%.
- **Statement (2):** Total operating expenses (inclusive of COGS, R&D, Sales & Marketing, and G&A) amounted to `₹98 crore`.
- **Options:**
  - (A) Statement (1) ALONE is sufficient, but Statement (2) alone is not sufficient.
  - (B) Statement (2) ALONE is sufficient, but Statement (1) alone is not sufficient.
  - (C) BOTH statements TOGETHER are sufficient, but NEITHER statement ALONE is sufficient.
  - (D) EACH statement ALONE is sufficient.
  - (E) Statements (1) and (2) TOGETHER are NOT sufficient.

#### Q38
Is the Customer Lifetime Value to Customer Acquisition Cost ratio ($LTV/CAC$) of Apex Dynamics strictly greater than 3.0?
*(Formula: $LTV = \frac{ARPU \times GM}{c}$, where $GM$ is gross margin percentage and $c$ is monthly customer churn rate).*
- **Statement (1):** The Customer Acquisition Cost ($CAC$) is `₹6,00,000`, and the monthly $ARPU$ is `₹1,00,000`.
- **Statement (2):** The gross profit margin is $80\%$, and the monthly customer churn rate is $4.0\%$.
- **Options:**
  - (A) Statement (1) ALONE is sufficient, but Statement (2) alone is not sufficient.
  - (B) Statement (2) ALONE is sufficient, but Statement (1) alone is not sufficient.
  - (C) BOTH statements TOGETHER are sufficient, but NEITHER statement ALONE is sufficient.
  - (D) EACH statement ALONE is sufficient.
  - (E) Statements (1) and (2) TOGETHER are NOT sufficient.

#### Q39
Can Apex Dynamics' hardware assembly facility fulfill an expedited order of 15,000 telematics units within 10 operating days?
- **Statement (1):** Production Line 1 operates at a certified rate of 900 units per day.
- **Statement (2):** Production Line 2 produces $40\%$ more units per day than Production Line 3, and Line 3 produces 500 units per day.
- **Options:**
  - (A) Statement (1) ALONE is sufficient, but Statement (2) alone is not sufficient.
  - (B) Statement (2) ALONE is sufficient, but Statement (1) alone is not sufficient.
  - (C) BOTH statements TOGETHER are sufficient, but NEITHER statement ALONE is sufficient.
  - (D) EACH statement ALONE is sufficient.
  - (E) Statements (1) and (2) TOGETHER are NOT sufficient.

#### Q40
What is the profit-maximizing daily production quantity of enterprise server units (Product $X$)?
- **Statement (1):** The contribution margins are `₹15,000` per unit of $X$ and `₹25,000` per unit of $Y$.
- **Statement (2):** Production requires 2 hours of fabrication and 3 hours of testing per unit of $X$, versus 4 hours of fabrication and 2 hours of testing per unit of $Y$.
- **Statement (3):** Daily plant capacity is constrained to at most 80 fabrication hours and 60 testing hours, with non-negativity constraints $X, Y \ge 0$.
- **Options:**
  - (A) Statement (1) alone is sufficient.
  - (B) Statements (1) and (2) together are sufficient.
  - (C) Statements (2) and (3) together are sufficient.
  - (D) All three statements (1), (2), and (3) together are necessary and sufficient.
  - (E) Statements (1), (2), and (3) together are NOT sufficient.

---

## 4. Rigorous Step-by-Step Solutions & Deductive Derivations

### Level 1 (Q1–Q5)

#### Q1
- **Target:** Value of $x \in \mathbb{R}$.
- **Statement (1):** $3x + 14 = 47 \implies 3x = 33 \implies x = 11$. Exactly one unique real solution. **Sufficient.**
- **Statement (2):** $x + 2y = 25 \implies x = 25 - 2y$. Without knowing $y$, $x$ can take infinitely many values (e.g., if $y=0, x=25$; if $y=7, x=11$). **Not sufficient.**
- **Conclusion:** Statement (1) alone is sufficient.  
- **Correct Answer:** **A**

#### Q2
- **Target:** Is $n > 0$ for integer $n$?
- **Statement (1):** $n^3 > 0$. Since odd powers strictly preserve sign:
  $$n^3 > 0 \iff n > 0$$
  This provides an unequivocal, definitive YES. **Sufficient.**
- **Statement (2):** $n^2 > 0$. Even powers square out negative signs:
  $$n^2 > 0 \iff n \ne 0$$
  If $n = 4 \implies n > 0$ (YES). If $n = -4 \implies n \not> 0$ (NO). Yields both YES and NO. **Not sufficient.**
- **Conclusion:** Statement (1) alone is sufficient.  
- **Correct Answer:** **A**

#### Q3
- **Target:** $\text{Area} = \pi r^2$. Sufficient if radius $r$ is uniquely determined.
- **Statement (1):** Circumference $= 2\pi r = 12\pi \implies r = 6\text{ cm} \implies \text{Area} = 36\pi\text{ cm}^2$. **Sufficient.**
- **Statement (2):** Diameter $= 2r = 12\text{ cm} \implies r = 6\text{ cm} \implies \text{Area} = 36\pi\text{ cm}^2$. **Sufficient.**
- **Conclusion:** EACH statement alone is sufficient.  
- **Correct Answer:** **D**

#### Q4
- **Target:** The numerical ratio $\frac{p}{q}$.
- **Statement (1):** $5p - 3q = 0 \implies 5p = 3q \implies \frac{p}{q} = \frac{3}{5}$. Exactly one unique ratio. **Sufficient.**
- **Statement (2):** $p + q = 24$. If $p = 12, q = 12 \implies p/q = 1$. If $p = 6, q = 18 \implies p/q = 1/3$. **Not sufficient.**
- **Conclusion:** Statement (1) alone is sufficient.  
- **Correct Answer:** **A**

#### Q5
- **Target:** Is $k$ divisible by 6 (where $k \in \mathbb{Z}^+$)?
- **Statement (1):** $k$ is divisible by 2. If $k=6$, YES. If $k=4$, NO ($4/6$ not integer). **Not sufficient.**
- **Statement (2):** $k$ is divisible by 3. If $k=6$, YES. If $k=9$, NO ($9/6$ not integer). **Not sufficient.**
- **Combined (1) + (2):** $k$ is a multiple of 2 AND a multiple of 3. Since $\gcd(2, 3) = 1$, $k$ must be a multiple of $\text{lcm}(2, 3) = 6$. Therefore, $k$ is definitively divisible by 6 (Definitive YES). **Sufficient.**
- **Conclusion:** Both statements together are sufficient.  
- **Correct Answer:** **C**

---

### Level 2 (Q6–Q10)

#### Q6
- **Target:** Value of $(x + y)$.
- **Statement (1):** $2x + 2y = 18 \implies 2(x + y) = 18 \implies x + y = 9$. **Sufficient.**
- **Statement (2):** $4x + 4y = 36 \implies 4(x + y) = 36 \implies x + y = 9$. **Sufficient.**
- **Conclusion:** EACH statement alone is sufficient.  
- **Correct Answer:** **D**

#### Q7
- **Target:** Unique real value of $x$.
- **Statement (1):** $x^2 - 7x + 12 = 0 \implies (x - 3)(x - 4) = 0 \implies x \in \{3, 4\}$. Two distinct real solutions. **Not sufficient.**
- **Statement (2):** $x^2 - 8x + 16 = 0 \implies (x - 4)^2 = 0 \implies x = 4$. Exactly one repeated real root. Uniquely determines $x$. **Sufficient.**
- **Conclusion:** Statement (2) alone is sufficient.  
- **Correct Answer:** **B**

#### Q8
- **Target:** Mean score $\mu = \frac{\sum_{i=1}^{10} x_i}{10}$.
- **Statement (1):** $\sum_{i=1}^5 x_{(i)} = 420$. The bottom 5 scores are completely unconstrained. **Not sufficient.**
- **Statement (2):** $\sum_{i=1}^{10} x_i = 780 \implies \mu = \frac{780}{10} = 78$. Exactly one unique mean. **Sufficient.**
- **Conclusion:** Statement (2) alone is sufficient.  
- **Correct Answer:** **B**

#### Q9
- **Target:** Number of pens $p \in \mathbb{Z}^+$ such that $7p + 11n = \text{Total}$, with $n \in \mathbb{Z}^+$.
- **Statement (1):** Total $= 100 \implies 7p + 11n = 100$.
  - We test integer constraints $n \ge 1$:
    $$11n < 100 \implies n \in \{1, 2, \dots, 9\}$$
  - Checking residues:
    - $n = 1: 100 - 11 = 89$ (not divisible by 7)
    - $n = 2: 100 - 22 = 78$ (not divisible by 7)
    - $n = 3: 100 - 33 = 67$ (not divisible by 7)
    - $n = 4: 100 - 44 = 56 = 7 \times 8 \implies p = 8$
    - $n = 5: 100 - 55 = 45$ (not div by 7)
    - $n = 6: 100 - 66 = 34$ (not div by 7)
    - $n = 7: 100 - 77 = 23$ (not div by 7)
    - $n = 8: 100 - 88 = 12$ (not div by 7)
    - $n = 9: 100 - 99 = 1$ (not div by 7)
  - The Diophantine equation has exactly **one unique positive integer solution**: $(p = 8, n = 4)$. Thus $p = 8$ is uniquely determined! **Sufficient.**
- **Statement (2):** $p + n = 12$. Multiple positive integer pairs satisfy this: $(1, 11), (2, 10), \dots, (8, 4)$. $p$ is not unique. **Not sufficient.**
- **Conclusion:** Statement (1) alone is sufficient.  
- **Correct Answer:** **A**

#### Q10
- **Target:** Length $L$ in rectangle with $L > W > 0$.
- **Statement (1):** $L \cdot W = 48$. Infinitely many factor pairs (e.g., $12 \times 4, 8 \times 6, 16 \times 3$). **Not sufficient.**
- **Statement (2):** $2(L + W) = 28 \implies L + W = 14$. Infinitely many pairs (e.g., $10 + 4, 8 + 6, 9 + 5$). **Not sufficient.**
- **Combined (1) + (2):** $L + W = 14$ and $L \cdot W = 48$.
  - Setting up the characteristic quadratic:
    $$t^2 - 14t + 48 = 0 \implies (t - 6)(t - 8) = 0 \implies t \in \{6, 8\}$$
  - Since the prompt specifies $L > W$, we must assign $L = 8\text{ cm}$ and $W = 6\text{ cm}$. Exactly one unique value for $L$. **Sufficient.**
- **Conclusion:** Both statements together are sufficient.  
- **Correct Answer:** **C**

---

### Level 3 (Q11–Q15)

#### Q11
- **Target:** Is $|x| < 3$ (which is algebraically equivalent to $-3 < x < 3$)?
- **Statement (1):** $x^2 < 9$. Taking the principal square root of both sides:
  $$\sqrt{x^2} < \sqrt{9} \implies |x| < 3$$
  This yields a definitive, guaranteed YES. **Sufficient.**
- **Statement (2):** $x < 3$. If $x = 0 \implies |0| = 0 < 3$ (YES). If $x = -10 \implies |-10| = 10 \not< 3$ (NO). Yields both YES and NO. **Not sufficient.**
- **Conclusion:** Statement (1) alone is sufficient.  
- **Correct Answer:** **A**

#### Q12
- **Target:** Is $P = n(n+1)(n+2)$ divisible by 12 (where $n \in \mathbb{Z}^+$)?
  - Notice that $P$ is the product of 3 consecutive integers, which is always divisible by $3! = 6$. For $P$ to be divisible by 12, it must have at least one additional factor of 2 (i.e., $4 \mid P$).
- **Statement (1):** $n$ is even.
  - If $n$ is even, both $n$ and $(n+2)$ are consecutive even integers. In any two consecutive even integers, one is a multiple of 2 and the other is a multiple of 4.
  - Hence, the product $n(n+2)$ is divisible by $2 \times 4 = 8$.
  - Since $(n+1)$ or one of the even numbers provides the factor of 3, the overall product is divisible by $8 \times 3 = 24$.
  - Since $24$ is a multiple of 12, $P$ is definitively divisible by 12! **Sufficient.**
- **Statement (2):** $n$ is a multiple of 3.
  - If $n = 3 \implies P = 3 \times 4 \times 5 = 60$, and $60 / 12 = 5$ (YES).
  - If $n = 9 \implies P = 9 \times 10 \times 11 = 990$, and $990 / 12 = 82.5$ (NO).
  - Yields both YES and NO. **Not sufficient.**
- **Conclusion:** Statement (1) alone is sufficient.  
- **Correct Answer:** **A**

#### Q13
- **Target:** Does $y = mx + c$ have $y$-intercept $c = 0$?
- **Statement (1):** Line passes through $(4, 6)$ and $(8, 12)$.
  - Slope $m = \frac{12 - 6}{8 - 4} = \frac{6}{4} = 1.5$.
  - Line equation: $y - 6 = 1.5(x - 4) \implies y = 1.5x - 6 + 6 \implies y = 1.5x$.
  - Thus $c = 0$, meaning it passes through $(0, 0)$. Definitive YES. **Sufficient.**
- **Statement (2):** The $x$-intercept is 0.
  - The $x$-intercept is the point $(x_0, 0)$. If $x_0 = 0$, the line passes through $(0, 0)$ by definition. Definitive YES. **Sufficient.**
- **Conclusion:** EACH statement alone is sufficient.  
- **Correct Answer:** **D**

#### Q14
- **Target:** $|F \cap S|$ where $|F \cup S| = 50$ (since every student is enrolled in at least one subject).
  - Principle of Inclusion-Exclusion:
    $$|F \cup S| = |F| + |S| - |F \cap S| \implies 50 = |F| + |S| - |F \cap S|$$
- **Statement (1):** $|F| = 35$. $|S|$ is unknown. **Not sufficient.**
- **Statement (2):** $|S| = 28$. $|F|$ is unknown. **Not sufficient.**
- **Combined (1) + (2):**
  $$50 = 35 + 28 - |F \cap S| \implies 50 = 63 - |F \cap S| \implies |F \cap S| = 13$$
  Exactly one unique solution. **Sufficient.**
- **Conclusion:** Both statements together are sufficient.  
- **Correct Answer:** **C**

#### Q15
- **Target:** Meeting time $t = \frac{D}{S_1 + S_2} = \frac{360}{S_1 + S_2}$. Sufficient if $(S_1 + S_2)$ is uniquely known.
- **Statement (1):** $S_1 = 70\text{ km/h}$. $S_2$ is unconstrained. **Not sufficient.**
- **Statement (2):** $S_1 + S_2 = 120\text{ km/h}$.
  $$t = \frac{360}{120} = 3\text{ hours}$$
  Exactly one unique value. **Sufficient.**
- **Conclusion:** Statement (2) alone is sufficient.  
- **Correct Answer:** **B**

---

### Level 4 (Q16–Q20)

#### Q16
- **Target:** Value of $x \in \mathbb{R}$.
- **Statement (1):** $x + y = 20$. Infinitely many values for $x$. **Not sufficient.**
- **Statement (2):** $xy = 96$. Infinitely many values for $x$. **Not sufficient.**
- **Combined (1) + (2):**
  - Substituting $y = 20 - x$ into (2):
    $$x(20 - x) = 96 \implies x^2 - 20x + 96 = 0 \implies (x - 8)(x - 12) = 0$$
  - This yields two distinct possible values: $x = 8$ (with $y = 12$) OR $x = 12$ (with $y = 8$).
  - Neither statement specifies whether $x > y$ or $x < y$. Because the system is completely symmetric with respect to $x$ and $y$, $x$ cannot be uniquely determined.
- **Conclusion:** Statements (1) and (2) TOGETHER are NOT sufficient.  
- **Correct Answer:** **E**

#### Q17
- **Target:** Is $x > y$?
- **Statement (1):** $|x| > |y|$.
  - If $x = -10$ and $y = 2 \implies |-10| > |2|$, but $-10 < 2$ (NO).
  - If $x = 10$ and $y = 2 \implies |10| > |2|$, and $10 > 2$ (YES).
  - Yields both YES and NO. **Not sufficient.**
- **Statement (2):** $x - y > 0 \iff x > y$.
  - This is identical to the target question. Definitive YES. **Sufficient.**
- **Conclusion:** Statement (2) alone is sufficient.  
- **Correct Answer:** **B**

#### Q18
- **Target:** Standard deviation $\sigma$ of dataset $S = \{a, b, c, d, e\}$.
- **Statement (1):** $\mu = 25$. Data dispersion around 25 is unconstrained (e.g., $\{25, 25, 25, 25, 25\} \implies \sigma = 0$; $\{5, 15, 25, 35, 45\} \implies \sigma > 0$). **Not sufficient.**
- **Statement (2):** $a = b = c = d = e = 25$.
  - All deviations from the mean $(x_i - \mu) = 0$.
  - Hence $\sigma = \sqrt{\frac{\sum 0^2}{5}} = 0$.
  - Exactly one unique numerical value ($\sigma = 0$). **Sufficient.**
- **Conclusion:** Statement (2) alone is sufficient.  
- **Correct Answer:** **B**

#### Q19
- **Target:** Is positive integer $M$ divisible by 72?
  - Prime factorization: $72 = 2^3 \times 3^2 = 8 \times 9$.
- **Statement (1):** $24 \mid M$ and $18 \mid M$.
  - $24 = 2^3 \times 3$ and $18 = 2 \times 3^2$.
  - Thus $M$ must be a multiple of $\text{lcm}(24, 18) = \text{lcm}(2^3 \times 3, 2 \times 3^2) = 2^3 \times 3^2 = 72$.
  - Therefore, $M$ is guaranteed to be a multiple of 72. Definitive YES. **Sufficient.**
- **Statement (2):** $8 \mid M$ and $9 \mid M$.
  - Since $\gcd(8, 9) = 1$, $M$ must be a multiple of $\text{lcm}(8, 9) = 8 \times 9 = 72$.
  - Therefore, $M$ is guaranteed to be a multiple of 72. Definitive YES. **Sufficient.**
- **Conclusion:** EACH statement alone is sufficient.  
- **Correct Answer:** **D**

#### Q20
- **Target:** Is $\triangle ABC$ acute-angled (i.e., are all three interior angles $< 90^\circ$)?
- **Statement (1):** The greatest angle $\theta_{\max} < 90^\circ$.
  - Since the largest angle is strictly less than $90^\circ$, all other angles must also be strictly less than $90^\circ$.
  - By definition, the triangle is acute-angled. Definitive YES. **Sufficient.**
- **Statement (2):** The sum of any two interior angles is strictly greater than $90^\circ$.
  - Let the angles be ordered: $\alpha \le \beta \le \gamma$.
  - The smallest pairwise sum is $\alpha + \beta$.
  - We are given that $\alpha + \beta > 90^\circ$.
  - In any Euclidean triangle:
    $$\alpha + \beta + \gamma = 180^\circ \implies \gamma = 180^\circ - (\alpha + \beta)$$
  - Since $\alpha + \beta > 90^\circ$, it follows that:
    $$\gamma < 180^\circ - 90^\circ = 90^\circ$$
  - Since the largest angle $\gamma < 90^\circ$, all three angles are acute. Definitive YES. **Sufficient.**
- **Conclusion:** EACH statement alone is sufficient.  
- **Correct Answer:** **D**

---

### Level 5 (Q21–Q25)

#### Q21
- **Target:** Weighted cost per kg $C_{\text{blend}} = \frac{C_A w_A + C_B w_B}{w_A + w_B}$.
- **Statement (1):** $C_A = 400, C_B = 600$. Weight proportions $w_A : w_B$ are unknown. **Not sufficient.**
- **Statement (2):** $w_A : w_B = 3 : 2$. Absolute costs $C_A, C_B$ are unknown. **Not sufficient.**
- **Combined (1) + (2):**
  $$C_{\text{blend}} = \frac{400(3) + 600(2)}{3 + 2} = \frac{1200 + 1200}{5} = \frac{2400}{5} = \text{₹}480/\text{kg}$$
  Exactly one unique cost. **Sufficient.**
- **Conclusion:** Both statements together are sufficient.  
- **Correct Answer:** **C**

#### Q22
- **Target:** Is total completion time $T < 4\text{ days} \iff R_{\text{total}} = R_P + R_Q + R_R > \frac{1}{4} = 0.250\text{ day}^{-1}$?
- **Statement (1):** $R_P = \frac{1}{8} = 0.125$, $R_Q = \frac{1}{12} \approx 0.0833$.
  - Combined rate $R_P + R_Q = \frac{5}{24} \approx 0.2083$.
  - If $R_R = 0.01 \implies R_{\text{total}} = 0.2183 < 0.25 \implies T > 4$ (NO).
  - If $R_R = 0.10 \implies R_{\text{total}} = 0.3083 > 0.25 \implies T < 4$ (YES).
  - Yields both YES and NO. **Not sufficient.**
- **Statement (2):** $T_R < 6\text{ days} \implies R_R > \frac{1}{6} \approx 0.1667$.
  - Without rates for $P$ and $Q$, total rate is unconstrained. **Not sufficient.**
- **Combined (1) + (2):**
  $$R_{\text{total}} = R_P + R_Q + R_R = \frac{5}{24} + R_R$$
  - Since $R_R > \frac{1}{6} = \frac{4}{24}$:
    $$R_{\text{total}} > \frac{5}{24} + \frac{4}{24} = \frac{9}{24} = \frac{3}{8} = 0.375\text{ day}^{-1}$$
  - Since $0.375 > 0.250$, we have:
    $$T = \frac{1}{R_{\text{total}}} < \frac{1}{0.375} = \frac{8}{3} \approx 2.67\text{ days} < 4\text{ days}$$
  - This guarantees an unequivocal, definitive YES! **Sufficient.**
- **Conclusion:** Both statements together are sufficient.  
- **Correct Answer:** **C**

#### Q23
- **Target:** Probability $P(\text{both Red}) = \frac{R(R-1)}{10 \times 9} = \frac{R(R-1)}{90}$, where $R \in \{0, 1, \dots, 10\}$.
- **Statement (1):** $P(\text{at least one Red}) = 1 - P(\text{both Blue}) = \frac{2}{3}$.
  - $P(\text{both Blue}) = \frac{(10 - R)(9 - R)}{90} = 1 - \frac{2}{3} = \frac{1}{3} = \frac{30}{90}$.
  - $(10 - R)(9 - R) = 30$.
  - Factoring: $(10 - R)$ and $(9 - R)$ are consecutive integers whose product is 30.
  - Since $6 \times 5 = 30 \implies 10 - R = 6 \implies R = 4$.
  - (The second algebraic root $(-5) \times (-6) = 30 \implies 10 - R = -5 \implies R = 15 > 10$, which violates domain constraints).
  - Thus $R = 4$ uniquely!
  - $P(\text{both Red}) = \frac{4 \times 3}{90} = \frac{12}{90} = \frac{2}{15}$. Exactly one unique probability. **Sufficient.**
- **Statement (2):** $P(\text{different colors}) = \frac{2 R (10 - R)}{90} = \frac{8}{15} = \frac{48}{90}$.
  - $2R(10 - R) = 48 \implies R(10 - R) = 24 \implies R^2 - 10R + 24 = 0 \implies (R - 4)(R - 6) = 0$.
  - $R$ can be either 4 OR 6:
    - If $R = 4 \implies P(\text{both Red}) = \frac{4 \times 3}{90} = \frac{12}{90} = \frac{2}{15}$.
    - If $R = 6 \implies P(\text{both Red}) = \frac{6 \times 5}{90} = \frac{30}{90} = \frac{1}{3}$.
  - Two distinct probabilities exist. **Not sufficient.**
- **Conclusion:** Statement (1) alone is sufficient.  
- **Correct Answer:** **A**

#### Q24
- **Target:** Remainder when positive integer $N$ is divided by 30.
- **Statement (1):** $N \equiv 3 \pmod 5$. Remainders mod 30 can be $\{3, 8, 13, 18, 23, 28\}$. Six possibilities. **Not sufficient.**
- **Statement (2):** $N \equiv 2 \pmod 6$. Remainders mod 30 can be $\{2, 8, 14, 20, 26\}$. Five possibilities. **Not sufficient.**
- **Combined (1) + (2):**
  - We have the simultaneous system of congruences:
    $$\begin{cases} N \equiv 3 \pmod 5 \\ N \equiv 2 \pmod 6 \end{cases}$$
  - Since $\gcd(5, 6) = 1$, by the **Chinese Remainder Theorem**, there exists a **unique solution modulo $5 \times 6 = 30$**.
  - Testing the candidates from Statement (2) modulo 5:
    - $2 \pmod 5 = 2 \ne 3$
    - $8 \pmod 5 = 3$ (MATCH!)
    - $14 \pmod 5 = 4 \ne 3$
    - $20 \pmod 5 = 0 \ne 3$
    - $26 \pmod 5 = 1 \ne 3$
  - The unique remainder modulo 30 is $8$. **Sufficient.**
- **Conclusion:** Both statements together are sufficient.  
- **Correct Answer:** **C**

#### Q25
- **Target:** Does $ax^2 + bx + c = 0$ have two distinct real roots? (Condition: Discriminant $D = b^2 - 4ac > 0$).
- **Statement (1):** $ac < 0$.
  - If $ac < 0$, then $-4ac > 0$.
  - For any real coefficient $b$, $b^2 \ge 0$.
  - Hence, $D = b^2 + (-4ac) \ge 0 + (-4ac) > 0$.
  - The discriminant is strictly positive regardless of the value of $b$! Definitive YES. **Sufficient.**
- **Statement (2):** $b^2 - 4ac > a^2$.
  - Since $a \ne 0$, $a^2 > 0$ strictly.
  - Thus $D = b^2 - 4ac > a^2 > 0$, guaranteeing $D > 0$. Definitive YES. **Sufficient.**
- **Conclusion:** EACH statement alone is sufficient.  
- **Correct Answer:** **D**

---

### Level 6 (Q26–Q30)

#### Q26
- **Target:** Exact value of $x$.
- **Statements (1) and (2):**
  - $x + y = 20$ and $xy = 96 \implies (x - 8)(x - 12) = 0$.
  - Permissible pairs are $(x=12, y=8)$ OR $(x=8, y=12)$. Two values for $x$.
- **Statement (3):**
  - Introduces the ordering constraint $x > y > 0$.
  - This eliminates $(x=8, y=12)$ and uniquely selects $(x=12, y=8)$.
- **Sufficiency of Subsets:**
  - Statements (1) and (3) alone leave infinitely many pairs (e.g., $x=15, y=5$; $x=11, y=9$).
  - Statements (2) and (3) alone leave infinitely many pairs (e.g., $x=96, y=1$; $x=24, y=4$).
  - All three statements (1), (2), and (3) are required simultaneously.
- **Correct Answer:** **D**

#### Q27
- **Target:** Number of students studying all three subjects ($s_3 = |P \cap C \cap M|$).
  - Partition equations for 3 sets where total $|P \cup C \cup M| = 100$:
    1. $s_1 + s_2 + s_3 = 100$
    2. Sum of singletons: $|P| + |C| + |M| = s_1 + 2s_2 + 3s_3$
  - Subtracting (1) from (2):
    $$s_2 + 2s_3 = (|P| + |C| + |M|) - 100$$
- **Evaluating Pairs:**
  - **Pair (1) + (2):** Statement (1) gives $\sum = 50 + 50 + 50 = 150$. Statement (2) gives $s_2 = 30$.
    $$30 + 2s_3 = 150 - 100 = 50 \implies 2s_3 = 20 \implies s_3 = 10\text{ (Sufficient)}$$
  - **Pair (2) + (3):** Statement (2) gives $s_2 = 30$, Statement (3) gives $s_1 = 60$.
    $$60 + 30 + s_3 = 100 \implies s_3 = 10\text{ (Sufficient)}$$
  - **Pair (1) + (3):** Statement (1) gives $\sum = 150$, Statement (3) gives $s_1 = 60$.
    - From (1): $60 + s_2 + s_3 = 100 \implies s_2 + s_3 = 40 \implies s_2 = 40 - s_3$.
    - From (2): $60 + 2s_2 + 3s_3 = 150 \implies 2(40 - s_3) + 3s_3 = 90 \implies 80 + s_3 = 90 \implies s_3 = 10\text{ (Sufficient)}$.
- **Conclusion:** ANY two of the three statements together are sufficient!  
- **Correct Answer:** **B**

#### Q28
- **Target:** Cylinder volume $V = \pi r^2 h$. Uniquely determined if $(r, h)$ are known.
  - Formula: Curved Surface Area $CSA = 2\pi r h$; Total Surface Area $TSA = 2\pi r h + 2\pi r^2$.
- **Evaluating Pairs:**
  - **Pair (1) + (2):**
    - $CSA = 2\pi r h = 120\pi \implies r h = 60$.
    - $TSA - CSA = 2\pi r^2 = 192\pi - 120\pi = 72\pi \implies r^2 = 36 \implies r = 6\text{ cm}$.
    - $h = 60 / 6 = 10\text{ cm} \implies V = \pi (6)^2 (10) = 360\pi\text{ cm}^3$. **Sufficient.**
  - **Pair (1) + (3):**
    - $2\pi r h = 120\pi$ and $h = 10 \implies 2\pi r (10) = 120\pi \implies r = 6\text{ cm} \implies V = 360\pi\text{ cm}^3$. **Sufficient.**
  - **Pair (2) + (3):**
    - $2\pi r(10) + 2\pi r^2 = 192\pi \implies 2\pi(r^2 + 10r) = 192\pi \implies r^2 + 10r - 96 = 0$.
    - Factoring: $(r + 16)(r - 6) = 0 \implies r = 6\text{ cm}$. **Sufficient.**
- **Conclusion:** Any two of the three statements together are sufficient.  
- **Correct Answer:** **B**

#### Q29
- **Target:** Are $L_1$ and $L_2$ perpendicular ($m_1 \cdot m_2 = -1$)?
- **Statement (1):** Passes through $(0, 0)$ and $(3, 4) \implies m_1 = \frac{4 - 0}{3 - 0} = \frac{4}{3}$. (Alone not sufficient).
- **Statement (2):** Intercepts $(4, 0)$ and $(0, 3) \implies m_2 = -\frac{y\text{-int}}{x\text{-int}} = -\frac{3}{4}$.
  - Combining (1) and (2): $m_1 \cdot m_2 = \left(\frac{4}{3}\right) \left(-\frac{3}{4}\right) = -1$. Perpendicular! (Sufficient).
- **Statement (3):** Parallel to $3x + 4y = 12 \implies 4y = -3x + 12 \implies m_2 = -\frac{3}{4}$.
  - Combining (1) and (3): $m_1 \cdot m_2 = \left(\frac{4}{3}\right) \left(-\frac{3}{4}\right) = -1$. Perpendicular! (Sufficient).
- **Conclusion:** Statement (1) combined with EITHER Statement (2) OR Statement (3) is sufficient.  
- **Correct Answer:** **C**

#### Q30
- **Target:** Median $c$ of sorted dataset $a < b < c < d < e$.
- **Combining All Statements:**
  - From Statement (2): $a = 12$ and range $e - a = 16 \implies e = 28$.
  - From Statement (3): $b, c, d$ form an arithmetic progression with common difference $d - b = 6 \implies c - b = 3$ and $d - c = 3$. Thus $b = c - 3$ and $d = c + 3$.
  - Now our set is: $\{12, c - 3, c, c + 3, 28\}$.
  - From Statement (1): Mean $= 20 \implies \text{Sum} = 5 \times 20 = 100$.
  - Summing the terms:
    $$12 + (c - 3) + c + (c + 3) + 28 = 100 \implies 40 + 3c = 100 \implies 3c = 60 \implies c = 20$$
  - Checking strict order: $a = 12 < b = 17 < c = 20 < d = 23 < e = 28$. Strictly satisfied!
  - Removing any single statement leaves $c$ underdetermined.
- **Conclusion:** All three statements together are required and sufficient.  
- **Correct Answer:** **D**

---

### Level 7 (Q31–Q35)

#### Q31
- **Target:** Is $\frac{x}{y} > 1$?
- **Statement (1):** $x > y$.
  - If $x = 5, y = 2 \implies 5/2 = 2.5 > 1$ (YES).
  - If $x = -2, y = -5 \implies -2 > -5$, but $(-2)/(-5) = 0.4 < 1$ (NO).
  - Yields both YES and NO. **Not sufficient.**
- **Statement (2):** $y > 0$. Without relation to $x$, $x/y$ is unconstrained. **Not sufficient.**
- **Combined (1) + (2):**
  - We have $x > y$ and $y > 0$.
  - Because $y > 0$, dividing both sides by $y$ preserves the inequality direction:
    $$\frac{x}{y} > \frac{y}{y} \implies \frac{x}{y} > 1$$
  - This guarantees a definitive YES. **Sufficient.**
- **Conclusion:** Both statements together are sufficient.  
- **Correct Answer:** **C**

#### Q32
- **Target:** Is $x = 5$?
- **Statement (1):** $x^2 = 25 \implies x = 5$ or $x = -5$. Not unique. **Not sufficient.**
- **Statement (2):** $|x - 5| = 0$. Since absolute value is zero if and only if its argument is zero:
  $$x - 5 = 0 \implies x = 5$$
  Definitive YES. **Sufficient.**
- **Conclusion:** Statement (2) alone is sufficient.  
- **Correct Answer:** **B**

#### Q33
- **Target:** Positive integer $p$.
- **Statement (1):** $p! = 120$. Since $1! = 1, 2! = 2, 3! = 6, 4! = 24, 5! = 120, 6! = 720$, the factorial function is strictly monotonically increasing on positive integers. Thus $p = 5$ uniquely! **Sufficient.**
- **Statement (2):** $p + q = 12$ and $q = 7 \implies p = 12 - 7 = 5$. Uniquely determined! **Sufficient.**
- **Conclusion:** EACH statement alone is sufficient.  
- **Correct Answer:** **D**

#### Q34
- **Target:** Is $(x^2 - y^2) > 0$?
  - Algebraic factorization: $(x^2 - y^2) = (x - y)(x + y)$.
- **Statement (1):** $x - y > 0$. Sign of $(x + y)$ is unknown. **Not sufficient.**
- **Statement (2):** $x + y > 0$. Sign of $(x - y)$ is unknown. **Not sufficient.**
- **Combined (1) + (2):**
  - $(x - y) > 0$ (strictly positive).
  - $(x + y) > 0$ (strictly positive).
  - The product of two strictly positive real numbers is strictly positive:
    $$(x^2 - y^2) = (x - y)(x + y) > 0$$
  - Definitive YES. **Sufficient.**
- **Conclusion:** Both statements together are sufficient.  
- **Correct Answer:** **C**

#### Q35
- **Target:** Do points $A, B, C$ form a valid non-degenerate triangle?
  - Fundamental Triangle Inequality: A triangle exists if and only if the sum of any two side lengths is strictly greater than the third side length.
- **Statement (1):** $AB = 5, BC = 7$. Third side $AC$ unknown. **Not sufficient.**
- **Statement (2):** $AC = 13$. Other sides unknown. **Not sufficient.**
- **Combined (1) + (2):**
  - Side lengths are 5, 7, and 13.
  - Test the triangle inequality on the two smaller sides:
    $$5 + 7 = 12$$
  - Since $12 < 13$, the sum of the two smaller sides is strictly less than the longest side!
  - Therefore, it is geometrically impossible for these three points to form a triangle.
  - This provides a definitive, 100% guaranteed **NO**!
  - In Data Sufficiency, a definitive NO is completely **SUFFICIENT**.
- **Conclusion:** Both statements together are sufficient.  
- **Correct Answer:** **C**

---

### Level 8 (Q36–Q40)

#### Q36
- **Target:** $MRR = \text{Client Count} \times ARPU$.
- **Statement (1):** Client count $= 400$. ARPU unknown. **Not sufficient.**
- **Statement (2):** $ARPU = \text{₹}1,25,000/\text{month}$. Client count unknown. **Not sufficient.**
- **Combined (1) + (2):**
  $$MRR = 400 \times 1,25,000 = \text{₹}5,00,00,000 = \text{₹}5\text{ crore/month}$$
  Exactly one unique revenue value. **Sufficient.**
- **Conclusion:** Both statements together are sufficient.  
- **Correct Answer:** **C**

#### Q37
- **Target:** Is $\text{Operating Cash Flow } (OCF) > 0$?
  - $OCF = \text{Gross Revenue} - \text{Total Operating Cash Outflows}$.
- **Statement (1):** Revenue $= \text{₹}120\text{ crore}$, Gross margin $= 80\% \implies \text{COGS} = 20\% = \text{₹}24\text{ crore}$. Operating expenses (SG&A, R&D) are unknown. **Not sufficient.**
- **Statement (2):** Total operating expenses $= \text{₹}98\text{ crore}$. Total revenue is unknown. **Not sufficient.**
- **Combined (1) + (2):**
  $$OCF = \text{Revenue} - \text{Total OpEx} = 120 - 98 = +\text{₹}22\text{ crore} > 0$$
  Definitive YES. **Sufficient.**
- **Conclusion:** Both statements together are sufficient.  
- **Correct Answer:** **C**

#### Q38
- **Target:** Is $\frac{LTV}{CAC} > 3.0$?
  - Where $LTV = \frac{ARPU \times GM}{c}$.
- **Statement (1):** $CAC = \text{₹}6,00,000$ and $ARPU = \text{₹}1,00,000/\text{month}$. $GM$ and $c$ unknown. **Not sufficient.**
- **Statement (2):** $GM = 0.80$ and $c = 0.04/\text{month}$. $CAC$ and $ARPU$ unknown. **Not sufficient.**
- **Combined (1) + (2):**
  $$LTV = \frac{1,00,000 \times 0.80}{0.04} = \frac{80,000}{0.04} = \text{₹}20,00,000$$
  $$\frac{LTV}{CAC} = \frac{20,00,000}{6,00,000} = \frac{10}{3} \approx 3.33$$
  Since $3.33 > 3.0$, this yields an unequivocal definitive YES. **Sufficient.**
- **Conclusion:** Both statements together are sufficient.  
- **Correct Answer:** **C**

#### Q39
- **Target:** Can total production meet $15,000\text{ units}$ in 10 days $\iff \text{Total Capacity} \ge 1,500\text{ units/day}$?
- **Statement (1):** Line 1 capacity $= 900\text{ units/day}$. Line 2 and 3 capacities unknown. **Not sufficient.**
- **Statement (2):** Line 3 capacity $= 500\text{ units/day}$. Line 2 produces $40\%$ more $\implies 500 \times 1.40 = 700\text{ units/day}$. Line 1 unknown. **Not sufficient.**
- **Combined (1) + (2):**
  $$\text{Total Daily Capacity} = \text{Line 1} + \text{Line 2} + \text{Line 3} = 900 + 700 + 500 = 2,100\text{ units/day}$$
  - In 10 days, output is $2,100 \times 10 = 21,000\text{ units} \ge 15,000\text{ units}$.
  - Definitive YES. **Sufficient.**
- **Conclusion:** Both statements together are sufficient.  
- **Correct Answer:** **C**

#### Q40
- **Target:** Optimal production quantity $X^*$ to maximize profit $Z = 15,000X + 25,000Y$.
- **Linear Programming Analysis:**
  - Statement (1) provides the gradient vector of the objective function: $c = [15000, 25000]^T$.
  - Statement (2) provides the left-hand constraint coefficients:
    $$\begin{cases} 2X + 4Y \le \text{Capacity}_1 \\ 3X + 2Y \le \text{Capacity}_2 \end{cases}$$
  - Statement (3) provides the right-hand resource limits:
    $$\begin{cases} 2X + 4Y \le 80 \\ 3X + 2Y \le 60 \\ X, Y \ge 0 \end{cases}$$
  - Together, (2) and (3) define a bounded, non-empty, convex polygonal feasible region in $\mathbb{R}^2$.
  - Statement (1) provides the linear objective function $Z$. By the Fundamental Theorem of Linear Programming, a linear function on a compact convex polygon attains its global maximum at one or more extreme vertices.
  - Computing the vertex coordinates:
    - $(0, 0) \implies Z = 0$
    - $(20, 0) \implies Z = 300,000$
    - $(0, 20) \implies Z = 500,000$
    - Intersection of $2X + 4Y = 80$ and $3X + 2Y = 60$:
      - Multiply second equation by 2: $6X + 4Y = 120$.
      - Subtract first equation: $4X = 40 \implies X = 10, Y = 15$.
      - $Z(10, 15) = 15,000(10) + 25,000(15) = 150,000 + 375,000 = 525,000$.
    - The unique maximum occurs at $(X^* = 10, Y^* = 15)$.
  - Thus $X^* = 10$ is uniquely determined!
  - Omitting any statement makes either the objective function or the polytope vertices uncomputable. All 3 statements are strictly required.
- **Conclusion:** All three statements together are necessary and sufficient.  
- **Correct Answer:** **D**

---

## 5. Rapid Revision & Strategic Exam Traps

```
+---------------------------------------------------------------------------------------------------+
|                            THE 5 DEADLIEST DATA SUFFICIENCY TRAPS                                 |
+---------------------------------------------------------------------------------------------------+
| 1. The Value vs. Range Mirage:                                                                    |
|    Finding a bounded inequality (e.g., 2 < x < 5) is NOT sufficient if the question asks        |
|    "What is the value of x?". A value question demands exactly ONE number.                       |
|---------------------------------------------------------------------------------------------------|
| 2. The Definite "NO" Illusion:                                                                    |
|    A statement that proves a proposition is FALSE provides 100% SUFFICIENCY for Yes/No questions. |
|    Sufficiency requires resolving truth value certainty, NOT validating affirmative bias!         |
|---------------------------------------------------------------------------------------------------|
| 3. The Unwarranted Assumption Trap:                                                               |
|    Never assume variables are positive, non-zero, or integers unless explicitly specified in      |
|    the problem stem! Always stress-test against 0, fractions, and negative reals.                 |
|---------------------------------------------------------------------------------------------------|
| 4. The Quadratic Multiplicity Ambiguity:                                                          |
|    x² = k yields x = ±√k. Unless a sign constraint is attached, two candidate values render the   |
|    statement INSUFFICIENT for value prompts.                                                      |
|---------------------------------------------------------------------------------------------------|
| 5. The "C-Trap" vs "D-Trap":                                                                      |
|    Never carry information from Statement (1) over when evaluating Statement (2) independently!   |
|    Evaluate Statement (2) with a completely cleared mental slate.                                 |
+---------------------------------------------------------------------------------------------------+
```

---

## 🔗 Cross-Links & Conceptual Continuations

- [Bar & Line Graphs](bar-and-line-graphs.md) — Temporal Trend Analysis & Dual-Axis Interpretation
- [Tables & Caselets](tables-and-caselets.md) — Complex Tabular Matrices & Multi-Attribute Caselets
- [Pie Charts](pie-charts.md) — Proportional Angle ($\theta$) and Multi-Tier Portfolio Share
- [Mixed Graphs](mixed-graphs.md) — Multi-Chart Synthesis & Integrated Caselets
- [Formula Sheet](../FORMULA_SHEET.md) — Quantitative Shortcuts, Number Theory & Mensuration
