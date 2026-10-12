# Module 01: Aptitude, Logical Reasoning, and Verbal Ability

> **Module Code**: DEL-M01  
> **Priority**: P1 (Core Placement Foundation)  
> **Target Assessment**: Deloitte USI Online Assessment Round 1 (Cognitive & Verbal Section)  
> **Standard**: Complete textbook explanations, foundational derivations, shortcuts, worked numericals, and full solutions.

---

## 1. Quantitative Aptitude — Arithmetic & Algebraic Foundations

### 1.1 Percentages, Ratios, and Proportions

#### Conceptual Foundations
* **Percentage**: A fraction with denominator 100. Multiplying factor $F = 1 + \frac{P}{100}$ for an increase, and $F = 1 - \frac{P}{100}$ for a decrease.
* **Successive Percentage Changes**: If a value changes by $+a\%$ and then by $+b\%$, the net percentage change is:
  $$\text{Net Change} = a + b + \frac{a \cdot b}{100}\%$$
* **Ratio & Proportion**: A ratio $a : b$ expresses relative magnitude. If $a : b = c : d$, then $a \cdot d = b \cdot c$.
* **Compounded Ratio**: The compounded ratio of $(a : b)$ and $(c : d)$ is $ac : bd$.

#### Worked Example 1 (Successive Changes)
**Problem**: A corporate client's cloud infrastructure bill increases by 25% in Q1 due to model training workloads, and subsequently decreases by 20% in Q2 after reserved instance optimization. What is the net percentage change in the client's cloud spend over the two quarters?

**Step-by-Step Calculation**:
1. Initial baseline spend = $S_0$.
2. Spending after Q1 increase: $S_1 = S_0 \times (1 + 0.25) = 1.25 \, S_0$.
3. Spending after Q2 decrease: $S_2 = S_1 \times (1 - 0.20) = 1.25 \, S_0 \times 0.80$.
4. Calculating multiplier: $1.25 \times 0.80 = 1.00$.
5. Net change: $\frac{1.00 S_0 - S_0}{S_0} \times 100\% = 0\%$.
6. *Using Formula*: $\text{Net} = 25 + (-20) + \frac{25 \times (-20)}{100} = 5 - 5 = 0\%$.
*Insight*: A $25\%$ increase followed by a $20\%$ decrease restores the original value because $0.25 = \frac{1}{4}$ up requires $\frac{1}{4+1} = \frac{1}{5} = 20\%$ down to neutralize.

---

### 1.2 Averages, Weighted Averages, and Alligation

#### The Alligation Cross Rule
When two ingredients of unit costs/values $C_1$ (cheaper) and $C_2$ (dearer) are mixed to produce an average mixture value $C_m$:
$$\frac{Q_1}{Q_2} = \frac{C_2 - C_m}{C_m - C_1}$$

```text
Cheaper Value (C1)           Dearer Value (C2)
              \             /
               \           /
             Mean Value (Cm)
               /           \
              /             \
      (C2 - Cm)      :      (Cm - C1)
       [Ratio of Cheaper] : [Ratio of Dearer]
```

#### Worked Example 2 (Alligation in Business Operations)
**Problem**: An offshore delivery team has senior consultants billing at $85/hr and junior analysts billing at $35/hr. If the blended project target billing rate is $50/hr across a 30-member project team, how many junior analysts and senior consultants must be allocated?

**Step-by-Step Calculation**:
1. $C_1 = 35$ (Junior), $C_2 = 85$ (Senior), $C_m = 50$.
2. Ratio $\frac{Q_{\text{Junior}}}{Q_{\text{Senior}}} = \frac{85 - 50}{50 - 35} = \frac{35}{15} = \frac{7}{3}$.
3. Total parts $= 7 + 3 = 10$ parts.
4. Each part $= \frac{30}{10} = 3$ members.
5. Junior Analysts $= 7 \times 3 = 21$ members.
6. Senior Consultants $= 3 \times 3 = 9$ members.
*Verification*: Blended rate $= \frac{(21 \times 35) + (9 \times 85)}{30} = \frac{735 + 765}{30} = \frac{1500}{30} = $50/hr.

---

### 1.3 Profit, Loss, Discount, and Commercial Mathematics

* **Cost Price (CP)**, **Selling Price (SP)**, **Marked Price (MP)**.
* **Profit %** $= \frac{\text{SP} - \text{CP}}{\text{CP}} \times 100$; **Loss %** $= \frac{\text{CP} - \text{SP}}{\text{CP}} \times 100$.
* **Discount %** $= \frac{\text{MP} - \text{SP}}{\text{MP}} \times 100$.
* **Relation between MP and CP**:
  $$\frac{\text{MP}}{\text{CP}} = \frac{100 + \text{Profit}\%}{100 - \text{Discount}\%}$$

#### Worked Example 3
**Problem**: A technology vendor marks up an enterprise software license such that after offering a 15% discount to corporate partners, they still realize a net profit margin of 19%. What was the initial percentage markup over cost price?

**Step-by-Step Calculation**:
1. Let $\text{CP} = 100$.
2. Required profit $= 19\% \implies \text{SP} = 119$.
3. Discount $= 15\% \implies \text{SP} = \text{MP} \times (1 - 0.15) = 0.85 \, \text{MP}$.
4. $0.85 \, \text{MP} = 119 \implies \text{MP} = \frac{119}{0.85} = \frac{11900}{85} = 140$.
5. Markup over CP $= \frac{140 - 100}{100} \times 100\% = 40\%$.

---

### 1.4 Time and Work, Efficiency, and Pipelines

* If person A completes a job in $T_A$ days, A's 1-day rate $= \frac{1}{T_A}$.
* Combined rate: $\frac{1}{T_{\text{combined}}} = \frac{1}{T_A} + \frac{1}{T_B}$.
* **Efficiency Principle**: Rate $\propto$ Efficiency. If A is twice as efficient as B, A takes half the time of B.

#### Worked Example 4
**Problem**: Data Engineer A can build a data extraction pipeline in 12 days. Data Engineer B is 50% more efficient than A. After working together for 3 days, Engineer A is reassigned to another client project. In how many additional days will Engineer B complete the remaining pipeline?

**Step-by-Step Calculation**:
1. Engineer A's 1-day work $= \frac{1}{12}$.
2. Engineer B is 50% more efficient $\implies$ B's rate $= 1.5 \times \frac{1}{12} = \frac{1}{8}$ per day (B alone takes 8 days).
3. Combined 1-day work $= \frac{1}{12} + \frac{1}{8} = \frac{2 + 3}{24} = \frac{5}{24}$.
4. Work completed in 3 days $= 3 \times \frac{5}{24} = \frac{15}{24} = \frac{5}{8}$.
5. Remaining work $= 1 - \frac{5}{8} = \frac{3}{8}$.
6. Days required by B alone to complete remaining work:
   $$\text{Time} = \frac{\text{Remaining Work}}{\text{B's Daily Rate}} = \frac{3/8}{1/8} = 3 \text{ days}.$$

---

### 1.5 Time, Speed, Distance, and Relative Motion

* $\text{Speed} = \frac{\text{Distance}}{\text{Time}}$. Conversion: $1\text{ km/h} = \frac{5}{18}\text{ m/s}$.
* **Average Speed** for equal distances: $v_{\text{avg}} = \frac{2 v_1 v_2}{v_1 + v_2}$.
* **Relative Speed**:
  * Opposite directions: $v_{\text{rel}} = v_1 + v_2$.
  * Same direction: $v_{\text{rel}} = |v_1 - v_2|$.

---

### 1.6 Permutations, Combinations, and Probability

* **Permutations (Order Matters)**: $^n P_r = \frac{n!}{(n-r)!}$.
* **Combinations (Selection Only)**: $^n C_r = \frac{n!}{r! (n-r)!}$.
* **Addition Rule**: $P(A \cup B) = P(A) + P(B) - P(A \cap B)$.
* **Independent Events**: $P(A \cap B) = P(A) \cdot P(B)$.
* **Conditional Probability**: $P(A \mid B) = \frac{P(A \cap B)}{P(B)}$.

#### Worked Example 5
**Problem**: An analytics project committee of 5 members is to be formed from 6 Data Scientists and 4 Business Consultants. What is the probability that the committee contains at least 3 Data Scientists?

**Step-by-Step Calculation**:
1. Total possible committees of 5 from $(6 + 4 = 10)$ candidates:
   $$\text{Total} = ^{10}C_5 = \frac{10 \times 9 \times 8 \times 7 \times 6}{5 \times 4 \times 3 \times 2 \times 1} = 252.$$
2. Favorable cases (At least 3 Data Scientists):
   * **Case 1 (Exactly 3 DS, 2 BC)**:
     $$^6C_3 \times ^4C_2 = \frac{6 \times 5 \times 4}{3 \times 2 \times 1} \times \frac{4 \times 3}{2 \times 1} = 20 \times 6 = 120.$$
   * **Case 2 (Exactly 4 DS, 1 BC)**:
     $$^6C_4 \times ^4C_1 = 15 \times 4 = 60.$$
   * **Case 3 (All 5 DS, 0 BC)**:
     $$^6C_5 \times ^4C_0 = 6 \times 1 = 6.$$
3. Total favorable outcomes $= 120 + 60 + 6 = 186$.
4. Probability:
   $$P = \frac{186}{252} = \frac{31}{42} \approx 0.7381 \, (73.81\%).$$

---

## 2. Logical and Analytical Reasoning

### 2.1 Deductive Logic & Categorical Syllogisms

* Syllogisms evaluate valid logical consequences of formal premises:
  * **A (Universal Affirmative)**: All $S$ are $P$.
  * **E (Universal Negative)**: No $S$ are $P$.
  * **I (Particular Affirmative)**: Some $S$ are $P$.
  * **O (Particular Negative)**: Some $S$ are not $P$.

```text
Euler Diagram Representations:
[ All A are B ]          [ No A are B ]          [ Some A are B ]
   ┌───────┐                ┌───┐    ┌───┐             ┌───┬───┐
   │ B ┌───┐│               │ A │    │ B │             │ A │ B │
   │   │ A ││               └───┘    └───┘             └───┴───┘
   │   └───┘│                                            Overlap
   └────────┘
```

#### Venn Resolution Rules
1. Two negative premises yield no definite conclusion.
2. Two particular premises yield no definite conclusion.
3. If one premise is negative, the conclusion must be negative.
4. "Only A is B" translates to "All B are A".

---

### 2.2 Analytical Puzzles & Constraint-Based Arrangements

#### Standard Linear & Circular Constraint Solving Framework
1. **Count Entities & Draw Grid**: Draw 6/8 slots.
2. **Anchor Direct Clues First**: Place clues with fixed positions (e.g., "A sits second from the left").
3. **Link Relative Clues**: Use clues referencing already-placed entities (e.g., "B sits 3 places to the right of A").
4. **Test Split Possibilities**: If a binary fork arises, create two parallel scratch diagrams. Prune the invalid branch immediately upon contradiction.

---

## 3. Data Interpretation (DI) & Quantitative Chart Analysis

* **Common Chart Formats**: Tabular grids, stacked bar charts, multi-line trend graphs, pie charts, and radar plots.
* **Key Formulas in DI**:
  * Percentage Growth: $\frac{\text{Value}_{t} - \text{Value}_{t-1}}{\text{Value}_{t-1}} \times 100\%$.
  * Compound Annual Growth Rate (CAGR): $\left(\frac{\text{Final}}{\text{Initial}}\right)^{\frac{1}{n}} - 1$.
  * Market Share: $\frac{\text{Company Sales}}{\text{Total Market Sales}} \times 100\%$.

---

## 4. Verbal Ability & Business English

### 4.1 Sentence Correction & Grammatical Standards
* **Subject-Verb Agreement**: Words between subject and verb (prepositional phrases like *together with, along with, as well as*) do not change the subject's number.
  * *Incorrect*: "The database of enterprise transactions, along with real-time logs, are failing."
  * *Correct*: "The database [singular] of enterprise transactions, along with real-time logs, **is** failing."
* **Modifiers**: A modifying phrase must immediately precede or follow the noun it modifies.
  * *Incorrect*: "Having completed the SQL audit, the report was submitted by the analyst." (Dangling modifier — the report did not complete the audit).
  * *Correct*: "Having completed the SQL audit, the **analyst** submitted the report."
* **Parallelism**: Items in a series must share grammatical form.
  * *Incorrect*: "The role requires analyzing data, building pipelines, and to present findings."
  * *Correct*: "The role requires analyzing data, building pipelines, and **presenting** findings."

---

## 5. Timed Solving Strategies & Sectional Drills

```text
TIMED ASSESSMENT TIME BUDGET (Round 1 Strategy):
• Easy Arithmetic & Direct Grammar: 45–50 seconds per question.
• Multi-step Algebra & DI Tables: 75–90 seconds per question.
• Complex Logic Puzzles (Grouped 4-Q set): 3.5 to 4 minutes total for the set.
• Unsolvable / Time-Trap Threshold: If no clear approach emerges within 40 seconds, eliminate options and move forward.
```

---

## 6. Self-Assessment Checklist

- [ ] Can compute successive percentage changes mentally using fractional multipliers.
- [ ] Mastered the alligation cross method for mixture and weighted rate problems.
- [ ] Can write Euler/Venn diagrams for complex negative and conditional syllogisms.
- [ ] Able to solve an 8-person circular seating arrangement with inward/outward facing constraints within 3.5 minutes.
- [ ] Confident identifying dangling modifiers, pronoun-antecedent ambiguity, and parallelism errors.
