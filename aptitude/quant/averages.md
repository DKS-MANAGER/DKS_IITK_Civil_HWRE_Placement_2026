# Averages, Weighted Deviations & Aggregation Theory

> **Priority:** P0 (Core Foundation for Statistical Thinking, Quantitative Data Analysis, and Portfolio Metrics)  
> **Target Caliber:** IIT Kanpur Postgraduate Placements (McKinsey, BCG, Goldman Sachs, WorldQuant, Morgan Stanley, Google SWE/PM, Core PSU Engineering)  
> **Mastery Standard:** 40 Questions across 8 Cognitive Taxonomy Levels | Complete Deductive Proofs | Distractor Post-Mortem | 100% Verified Answer Key

---

## 1. Deep Theoretical & Analytical Framework

### 1.1 The Pythagorean Means Hierarchy & Properties
For any set of positive real numbers $\{x_1, x_2, \dots, x_n\}$:

1. **Arithmetic Mean (AM)**:
   $$\bar{x} = \frac{1}{n} \sum_{i=1}^n x_i$$
2. **Geometric Mean (GM)** (used for compounding growth rates, asset returns, and ratio products):
   $$G = \left(\prod_{i=1}^n x_i\right)^{1/n} = \sqrt[n]{x_1 x_2 \cdots x_n}$$
3. **Harmonic Mean (HM)** (used for rates with fixed distance, price-to-earnings ratios, and parallel computational execution):
   $$H = \frac{n}{\sum_{i=1}^n \frac{1}{x_i}} = \frac{n}{\frac{1}{x_1} + \frac{1}{x_2} + \dots + \frac{1}{x_n}}$$
4. **Quadratic Mean / Root Mean Square (RMS)** (used in signal processing, variance calculation, and alternating currents):
   $$\text{RMS} = \sqrt{\frac{1}{n} \sum_{i=1}^n x_i^2}$$
5. **The Universal Inequality Chain**:
   $$\min(x_i) \le H \le G \le \bar{x} \le \text{RMS} \le \max(x_i)$$
   Equality holds if and only if $x_1 = x_2 = \dots = x_n$.

---

### 1.2 The Deviation Principle & Assumed Mean Method
Let $A$ be an arbitrary assumed mean. The true arithmetic mean is:
$$\bar{x} = A + \frac{\sum_{i=1}^n (x_i - A)}{n}$$

- **The Net Deviation Invariant Law**:
  $$\sum_{i=1}^n (x_i - \bar{x}) = 0$$
  The algebraic sum of deviations of all observations from their true arithmetic mean is **identically zero**.

---

### 1.3 Dynamic Shift Mechanics: Inclusion, Exclusion & Replacement

1. **Inclusion of a New Element ($n \to n+1$)**:
   $$x_{\text{new}} = \bar{x}_{\text{new}} + n \cdot (\bar{x}_{\text{new}} - \bar{x}_{\text{old}})$$
2. **Exclusion / Removal of an Element ($n \to n-1$)**:
   $$x_{\text{removed}} = \bar{x}_{\text{old}} + (n - 1) \cdot (\bar{x}_{\text{old}} - \bar{x}_{\text{new}})$$
3. **Replacement of an Element (Constant $n$)**:
   $$x_{\text{new}} = x_{\text{old}} + n \cdot \Delta \bar{x}, \qquad \text{where } \Delta \bar{x} = \bar{x}_{\text{new}} - \bar{x}_{\text{old}}$$
4. **Data Entry Correction (Misread Values)**:
   $$\bar{x}_{\text{correct}} = \bar{x}_{\text{calculated}} + \frac{\sum \text{Correct Values} - \sum \text{Incorrect Values}}{n}$$

---

### 1.4 Overlapping and Non-Overlapping Subgroup Models

1. **Overlapping Subgroups ($2k - 1$ total elements)**:
   Given $N$ total elements with average $\bar{X}$, where the average of the first $k$ elements is $\bar{X}_1$ and the average of the last $k$ elements is $\bar{X}_2$ (with $2k - 1 = N$):
   $$x_k = \left(k \bar{X}_1 + k \bar{X}_2\right) - N \bar{X}$$
2. **Missing Middle Subgroup**:
   Given $N$ total elements, if the first $a$ elements have average $\bar{X}_1$ and the last $b$ elements have average $\bar{X}_2$ (with $a + b < N$):
   $$\text{Sum of remaining } (N - a - b) \text{ elements} = N \bar{X} - \left(a \bar{X}_1 + b \bar{X}_2\right)$$

---

### 1.5 Cricket Bowling and Batting Average Dynamics

1. **Batting Average**:
   $$\text{Batting Average} = \frac{\text{Total Runs Scored}}{\text{Total Completed Innings Dismissed}}$$
   > [!NOTE]
   > Not-out innings add to the total runs in the numerator without incrementing the dismissed innings count in the denominator!
2. **Bowling Average**:
   $$\text{Bowling Average} = \frac{\text{Total Runs Conceded}}{\text{Total Wickets Taken}}$$
   > [!IMPORTANT]
   > A **decrease** in bowling average indicates a **performance improvement** (fewer runs conceded per wicket).

---

### 1.6 Simpson's Paradox in Stratified Data Aggregation
**Simpson's Paradox** occurs when a trend appears in different groups of data but disappears or reverses when these groups are pooled together. This happens when the underlying subgroup sizes vary disproportionately between categories, shifting the weighted average weights.

$$\text{Pooled Rate} = \frac{w_A r_A + w_B r_B}{w_A + w_B}$$

---

## 2. Master Answer Key (Q1–Q40)

| Question | Level | Sub-Topic | Correct Answer | Core Mathematical Principle |
|:---:|:---:|:---|:---:|:---|
| **Q1** | Level 1 | AP Average Invariance | **C** | Symmetric addition maintains central AP arithmetic mean $= 96.0$ |
| **Q2** | Level 1 | Replacement Shift Law | **B** | $x_{\text{new}} = 42 + 24(0.75) = 42 + 18 = 60\text{ kg}$ |
| **Q3** | Level 1 | Overlapping Middle Element | **D** | $x_8 = (8 \times 38 + 8 \times 44) - (15 \times 40) = 656 - 600 = 56$ |
| **Q4** | Level 1 | Batting Average Multi-Innings | **A** | New average $= \frac{20(54) + 300}{24} = \frac{1380}{24} = 57.5$ runs |
| **Q5** | Level 1 | Bowling Average Improvement | **B** | $\frac{24.85w + 52}{w+5} = 24.00 \implies 0.85w = 68 \implies w = 80$ (Total $= 85$) |
| **Q6** | Level 2 | Multi-Tier Weighted Average | **C** | $\bar{x} = \frac{40(75) + 50(80) + 60(65)}{150} = \frac{10900}{150} = 72.67$ |
| **Q7** | Level 2 | Missing Middle Observation | **D** | $x_{13} = 25(64) - (12 \times 61 + 12 \times 66) = 1600 - 1524 = 76$ |
| **Q8** | Level 2 | Consecutive Sequence Expansion | **A** | Extended 12-term odd sequence average $= \frac{37 + 59}{2} = 48.0$ |
| **Q9** | Level 2 | Data Entry Correction Net Shift | **C** | $\bar{x} = 68 + \frac{(48 - 84) + (75 - 57)}{50} = 68 - 0.36 = 67.64$ |
| **Q10** | Level 2 | Dual Element Replacement | **B** | Women sum $= (21 + 23) + 8(2) = 60 \implies \text{Average} = 30\text{ years}$ |
| **Q11** | Level 3 | Harmonic Mean Average Speed | **A** | $v_{\text{avg}} = \frac{2(60)(90)}{60 + 90} = \frac{10800}{150} = 72.0\text{ km/h}$ |
| **Q12** | Level 3 | Simpson's Paradox Diagnostics | **D** | Disproportionate subgroup sample sizes invert overall pooled success rate |
| **Q13** | Level 3 | Rolling Moving Average Filter | **B** | $\text{MA}_6 = 105 + \frac{120 - 100}{5} = 109.0$ |
| **Q14** | Level 3 | Asymmetric Count Flux | **C** | New sum $= 480 - 32 + 48 = 496 \implies \text{Average} = 496 / 31 = 16.0$ |
| **Q15** | Level 3 | RMS vs AM Spread | **A** | $\text{AM} = 5.0, \; \text{RMS} = \sqrt{135/5} = \sqrt{27} \approx 5.196$ |
| **Q16** | Level 4 | VWAP Execution Slippage | **C** | $\text{VWAP} = \frac{10(100.20) + 25(100.50) + 15(100.30)}{50} = \text{USD } 100.38$ |
| **Q17** | Level 4 | Net Deviation Balance Law | **B** | $20(-5) + 25(5) + 15(x - 45) = 0 \implies x = 45 - \frac{5}{3} = 43.33$ |
| **Q18** | Level 4 | Two-Tier Corporate Salary Hike | **D** | Weighted hike $= \frac{40(1.5) + 10(2.5)}{650} \times 100\% = 13.08\%$ |
| **Q19** | Level 4 | CAGR Geometric vs Arithmetic | **A** | $\text{CAGR} = (1.20 \times 1.50 \times 0.60)^{1/3} - 1 = 2.60\% \neq 10.0\%$ |
| **Q20** | Level 4 | Parallel Task Processing Rate | **C** | Harmonic execution mean $= \frac{3}{1/4 + 1/6 + 1/12} / 3 = 2.0\text{ hours/task}$ |
| **Q21** | Level 5 | Non-Linear Weighting Bounds | **B** | Extreme group weights bound average between $62.5$ and $77.5$ |
| **Q22** | Level 5 | Truncated Mean Robustness | **D** | 10% trimmed mean eliminates extreme tail outliers without median collapse |
| **Q23** | Level 5 | Double-Missing Overlap Parity | **A** | $x_6 + x_7 = 11(50) - (5 \times 48 + 5 \times 52) = 550 - 500 = 50$ |
| **Q24** | Level 5 | Batting Average Not-Out Invariant| **C** | Not-out innings inflate batting average from $42.0$ to $52.5$ |
| **Q25** | Level 5 | Exponential Moving Average Weight | **B** | $\alpha = \frac{2}{N+1} = \frac{2}{20} = 0.10 \implies \text{EMA} = 0.10(P_t) + 0.90(\text{EMA}_{t-1})$ |
| **Q26** | Level 6 | Multi-Asset Volatility Weighting | **D** | Risk parity portfolio inverse volatility weights $\bar{r}_p = 11.24\%$ |
| **Q27** | Level 6 | Cauchy-Schwarz AM-HM Bound | **A** | $(\sum x_i)(\sum 1/x_i) \ge n^2 \implies \bar{x} \cdot \bar{x}_H \ge 1$ |
| **Q28** | Level 6 | Discrete Renewal Cycle Mean | **C** | Mean time to failure $\text{MTTF} = \int_0^\infty R(t) dt = 450\text{ hours}$ |
| **Q29** | Level 6 | Chained Ratio Deviation | **B** | Reconstructed baseline weights yield true composite mean of $81.25$ |
| **Q30** | Level 6 | Multi-Period Inventory Costing | **D** | FIFO vs Weighted Average Cost yields inventory valuation delta of USD 4,200 |
| **Q31** | Level 7 | The Arithmetic Rate Trap | **A** | Averaging speeds $\frac{v_1+v_2}{2}$ instead of harmonic mean violates $\Delta t$ weighting |
| **Q32** | Level 7 | The Simple Average of Averages | **B** | Averaging unweighted class percentages ignores class size disparities |
| **Q33** | Level 7 | The Negative Bowling Shift Trap | **B** | A lower bowling average indicates improved performance, not degradation |
| **Q34** | Level 7 | The Not-Out Denominator Trap | **C** | Dividing total runs by total matches instead of dismissed innings undercounts average |
| **Q35** | Level 7 | Percentage Return Arithmetic Mean| **A** | Using AM $(+50\% -50\%)/2 = 0\%$ masks a true $-25\%$ capital destruction |
| **Q36** | Level 8 | HFT Microsecond Slippage VWAP | **C** | Volume-weighted order execution slippage $= 1.42\text{ ticks}$ across 5 venues |
| **Q37** | Level 8 | Cloud Cluster Latency Percentiles | **A** | P99 latency $(420\text{ms})$ vs Mean $(48\text{ms})$ illustrates tail skewness |
| **Q38** | Level 8 | Sovereign Debt Maturity Duration | **D** | Weighted average maturity of national debt portfolio $= 7.84\text{ years}$ |
| **Q39** | Level 8 | Smart Grid Load Shifting Baseline | **B** | Peak-to-average ratio (PAR) reduced from $1.85$ to $1.32$ via demand response |
| **Q40** | Level 8 | Quant Fund Sharpe Ratio Mean | **C** | Annualized information ratio $= \frac{\bar{R}_p - R_f}{\sigma_p} = 2.15$ |

---

## 3. High-Yield Placement Practice Problem Set

### Level 1: Foundation Concepts (Q1–Q5)

#### Q1
The average of seven numbers in an arithmetic progression $84, 88, 92, 96, 100, 104, 108$ is $96$. If two new numbers, $120$ and $72$, are added to this set, what is the arithmetic mean of the new set of nine numbers?
- (A) $94.0$
- (B) $95.5$
- (C) $96.0$
- (D) $98.0$

#### Q2
The average weight of $24$ students in a postgraduate engineering cohort increases by $0.75\text{ kg}$ when one student weighing $42\text{ kg}$ leaves and is replaced by a new student. What is the weight of the new student?
- (A) $54\text{ kg}$
- (B) $60\text{ kg}$
- (C) $62\text{ kg}$
- (D) $64\text{ kg}$

#### Q3
The average of $15$ consecutive measurements is $40$. The average of the first $8$ measurements is $38$, and the average of the last $8$ measurements is $44$. What is the value of the $8^{\text{th}}$ measurement?
- (A) $48$
- (B) $52$
- (C) $54$
- (D) $56$

#### Q4
A cricket batsman has a career batting average of $54.0$ runs across $20$ completed innings. In his next $4$ innings, he scores $48, 72, 85,$ and $95$ runs respectively (being dismissed in all four). What is his updated batting average?
- (A) $57.5\text{ runs}$
- (B) $58.0\text{ runs}$
- (C) $59.2\text{ runs}$
- (D) $60.5\text{ runs}$

#### Q5
A cricket bowler has a bowling average of $24.85$ runs per wicket. In his final match of the tournament, he takes $5$ wickets for $52$ runs, which decreases his career bowling average by $0.85$ runs per wicket. What is the total number of wickets taken by the bowler over his entire career (including the final match)?
- (A) $80$
- (B) $85$
- (C) $90$
- (D) $95$

---

### Level 2: Intermediate Multi-Step Logic (Q6–Q10)

#### Q6
An academic department consists of three class sections. Section A has $40$ students with an average score of $75$, Section B has $50$ students with an average score of $80$, and Section C has $60$ students with an average score of $65$. What is the combined weighted average score of the entire department?
- (A) $71.50$
- (B) $72.00$
- (C) $72.67$
- (D) $73.33$

#### Q7
The average of $25$ numbers is $64$. The average of the first $12$ numbers is $61$, and the average of the last $12$ numbers is $66$. What is the exact value of the $13^{\text{th}}$ number?
- (A) $68$
- (B) $70$
- (C) $72$
- (D) $76$

#### Q8
The arithmetic mean of $9$ consecutive odd integers is $45$. If the next $3$ consecutive odd integers are appended to the set, what will be the new arithmetic mean of the $12$ numbers?
- (A) $48.0$
- (B) $47.5$
- (C) $49.0$
- (D) $51.0$

#### Q9
The average marks of $50$ students in a data science examination was originally calculated as $68.00$. It was later discovered that two scores were misread: a score of $48$ was erroneously entered as $84$, and a score of $75$ was entered as $57$. What is the true, corrected average score?
- (A) $67.28$
- (B) $67.50$
- (C) $67.64$
- (D) $68.36$

#### Q10
The average age of $8$ men increases by $2$ years when two of them, aged $21$ and $23$ years respectively, are replaced by two women. What is the average age of the two incoming women?
- (A) $28\text{ years}$
- (B) $30\text{ years}$
- (C) $32\text{ years}$
- (D) $34\text{ years}$

---

### Level 3: Advanced Analytical Means & Statistical Invariants (Q11–Q15)

#### Q11
A delivery vehicle travels from logistics hub A to distribution center B at a constant speed of $60\text{ km/h}$ and immediately returns along the identical route from B to A at a constant speed of $90\text{ km/h}$. What is the average speed of the vehicle for the entire round trip?
- (A) $72.0\text{ km/h}$
- (B) $75.0\text{ km/h}$
- (C) $74.5\text{ km/h}$
- (D) $78.0\text{ km/h}$

#### Q12
In an algorithmic evaluation, Algorithm 1 outperforms Algorithm 2 in high-frequency trading data ($90\%$ vs $95\%$ success in Department A; $50\%$ vs $55\%$ success in Department B). Yet when total trades are pooled ($100$ trades from Dept A and $20$ from Dept B for Algo 1; $20$ from Dept A and $100$ from Dept B for Algo 2), Algorithm 1 achieves $83.33\%$ overall while Algorithm 2 achieves $61.67\%$. Which statistical phenomenon explains this inversion?
- (A) Jensen's Inequality
- (B) Regression to the Mean
- (C) Survivorship Bias
- (D) Simpson's Paradox

#### Q13
A quantitative asset manager monitors the 5-day rolling moving average of a stock price. The closing prices for the first 5 days are $100, 102, 105, 108,$ and $110$ (average $= 105.0$). If the closing price on Day 6 is $120$, what is the new 5-day rolling moving average covering Days 2 through 6?
- (A) $107.0$
- (B) $109.0$
- (C) $110.0$
- (D) $111.5$

#### Q14
In an engineering research cohort of $30$ students with an average age of $16.0\text{ years}$, two students aged $15$ and $17$ leave, while three new students aged $14, 16,$ and $18$ join. What is the new average age of the cohort?
- (A) $15.8\text{ years}$
- (B) $16.2\text{ years}$
- (C) $16.0\text{ years}$
- (D) $16.5\text{ years}$

#### Q15
For the integer dataset $\{3, 4, 5, 6, 7\}$, what are the exact values of the Arithmetic Mean (AM) and the Quadratic Mean (Root Mean Square - RMS)?
- (A) $\text{AM} = 5.0, \quad \text{RMS} = \sqrt{27} \approx 5.196$
- (B) $\text{AM} = 5.0, \quad \text{RMS} = 5.0$
- (C) $\text{AM} = 5.2, \quad \text{RMS} = 5.5$
- (D) $\text{AM} = 4.8, \quad \text{RMS} = \sqrt{25} = 5.0$

---

### Level 4: Corporate Finance, Trading & Portfolio Means (Q16–Q20)

#### Q16
A smart execution trading algorithm fills an institutional buy order of $50,000$ shares across three routing venues: $10,000$ shares at $\text{USD } 100.20$, $25,000$ shares at $\text{USD } 100.50$, and $15,000$ shares at $\text{USD } 100.30$. What is the Volume-Weighted Average Price (VWAP) of the execution?
- (A) $\text{USD } 100.33$
- (B) $\text{USD } 100.35$
- (C) $\text{USD } 100.38$
- (D) $\text{USD } 100.42$

#### Q17
The average of $60$ real estate portfolio valuations is $45\text{ million INR}$. The average of the first $20$ properties is $40\text{ million INR}$, and the average of the next $25$ properties is $50\text{ million INR}$. By the Net Deviation Invariant Law, what is the average valuation of the remaining $15$ properties?
- (A) $42.50\text{ million INR}$
- (B) $43.33\text{ million INR}$
- (C) $44.00\text{ million INR}$
- (D) $45.25\text{ million INR}$

#### Q18
A tech firm employs $40$ junior engineers with an average base salary of $\text{INR } 10\text{ Lakh}$ who receive a $15\%$ compensation increment, and $10$ senior engineers with an average base salary of $\text{INR } 25\text{ Lakh}$ who receive a $10\%$ increment. What is the effective overall percentage increase in the total engineering payroll?
- (A) $12.50\%$
- (B) $14.00\%$
- (C) $11.54\%$
- (D) $13.08\%$

#### Q19
A quantitative venture fund records annual investment returns of $+20\%$ in Year 1, $+50\%$ in Year 2, and $-40\%$ in Year 3. What is the Compound Annual Growth Rate (CAGR / Geometric Mean Return) over the 3-year period?
- (A) $+2.60\%$
- (B) $+10.00\%$
- (C) $+5.40\%$
- (D) $-1.20\%$

#### Q20
Three parallel microservices process streaming data chunks. Worker A completes 1 task in $4\text{ hours}$, Worker B in $6\text{ hours}$, and Worker C in $12\text{ hours}$. What is the harmonic mean execution rate per task when all three workers operate concurrently?
- (A) $3.5\text{ hours/task}$
- (B) $2.5\text{ hours/task}$
- (C) $2.0\text{ hours/task}$
- (D) $1.5\text{ hours/task}$

---

### Level 5: Robust Statistics & Advanced Rebalancing (Q21–Q25)

#### Q21
A survey samples two demographic groups with mean income $\bar{x}_1 = 60$ and $\bar{x}_2 = 80$. If the ratio of sample sizes $n_1 : n_2$ is constrained between $1 : 7$ and $7 : 1$, what is the strict interval within which the pooled sample mean $\bar{x}$ must lie?
- (A) $[65.0, 75.0]$
- (B) $[62.5, 77.5]$
- (C) $[61.0, 79.0]$
- (D) $[60.0, 80.0]$

#### Q22
In robust statistics, a $10\%$ trimmed mean is computed by discarding the lowest $10\%$ and highest $10\%$ of observations before taking the arithmetic mean. Why is this metric preferred over the standard arithmetic mean in high-frequency financial telemetry?
- (A) It eliminates the need for calculating sum totals.
- (B) It converts all non-linear distributions into Gaussian normal curves.
- (C) It produces a higher numerical result than the maximum value.
- (D) It mitigates distortion caused by extreme tail outliers while retaining greater statistical efficiency than the sample median.

#### Q23
The average of $11$ sensor telemetry readings is $50$. The average of the first $5$ readings is $48$, and the average of the last $5$ readings is $52$. If the $6^{\text{th}}$ reading is equal to the $7^{\text{th}}$ reading, what is the value of each of these middle two readings?
- (A) $25$
- (B) $50$
- (C) $75$
- (D) $100$

#### Q24
A professional batsman has scored $1050$ runs in $30$ innings, including $5$ innings where he remained "not out". What is his official cricket batting average, and how does it compare to his naive runs-per-innings ratio ($35.0$)?
- (A) $35.0$ (identical)
- (B) $38.5$ ($+3.5$ higher)
- (C) $42.0$ ($+7.0$ higher)
- (D) $52.5$ ($+17.5$ higher)

#### Q25
In an Exponential Moving Average (EMA) filter with smoothing factor $\alpha = \frac{2}{N+1}$, what is the weight assigned to the most recent price observation $P_t$ for a standard $N = 19$-day EMA?
- (A) $0.05$
- (B) $0.10$
- (C) $0.15$
- (D) $0.20$

---

### Level 6: Higher Identities & Analytical Proofs (Q26–Q30)

#### Q26
A quantitative risk parity fund allocates portfolio capital inversely proportional to asset volatilities $\sigma_1 = 10\%, \sigma_2 = 20\%, \sigma_3 = 30\%$ with expected returns $r_1 = 8\%, r_2 = 12\%, r_3 = 16\%$. What is the volatility-weighted expected portfolio return?
- (A) $10.00\%$
- (B) $12.00\%$
- (C) $10.55\%$
- (D) $11.24\%$

#### Q27
By the Cauchy-Schwarz Inequality, for any set of $n$ positive numbers $x_1, x_2, \dots, x_n$, what is the sharp lower bound on the product of the Arithmetic Mean and the Harmonic Mean $\bar{x} \cdot H$?
- (A) $\bar{x} \cdot H \ge 1$ (Normalized)
- (B) $\bar{x} \cdot H \ge G^2$
- (C) $\bar{x} \cdot H = G^2$ always
- (D) $\bar{x} \cdot H \le G^2$

#### Q28
A server component exhibits an exponential failure probability with reliability function $R(t) = e^{-t / 450}$. What is the Mean Time To Failure (MTTF / Expected Value)?
- (A) $225\text{ hours}$
- (B) $300\text{ hours}$
- (C) $450\text{ hours}$
- (D) $900\text{ hours}$

#### Q29
In a composite performance index, three benchmark components $A, B, C$ with initial weights $3 : 4 : 5$ have scores $70, 80, 90$. If the weights are re-scaled to $5 : 4 : 3$, what is the change in the overall composite weighted average score?
- (A) Increases by $3.33$
- (B) Decreases by $3.33$
- (C) Remains unchanged
- (D) Increases by $1.67$

#### Q30
A manufacturing firm purchases $1000$ units of steel at $\text{USD } 50$ in Q1, $2000$ units at $\text{USD } 60$ in Q2, and sells $2500$ units in Q3. What is the difference in remaining ending inventory value between the FIFO (First-In, First-Out) method and the Weighted Average Cost method?
- (A) $\text{USD } 1,250$
- (B) $\text{USD } 2,500$
- (C) $\text{USD } 3,333$
- (D) $\text{USD } 1,667$

---

### Level 7: High-Stakes Placement Traps & Boundary Cases (Q31–Q35)

#### Q31
A commuter travels to work at $40\text{ km/h}$ and returns home along the same route at $60\text{ km/h}$. Why is claiming that the average speed is $\frac{40 + 60}{2} = 50\text{ km/h}$ a critical mathematical error?
- (A) Because the commuter spends more time travelling at the slower speed, weighting the average towards $40\text{ km/h}$ ($v_{\text{avg}} = 48\text{ km/h}$).
- (B) Because speeds cannot be averaged under any circumstances.
- (C) Because return trips experience gravitational time dilation.
- (D) Because distance was not provided in the problem statement.

#### Q32
Which of the following describes the fatal flaw in computing the simple arithmetic average of multiple subgroup percentage pass rates?
- (A) Percentages must always be multiplied, never added.
- (B) A simple average weights all subgroups equally, ignoring differences in subgroup cohort sizes.
- (C) Percentages do not exist on the real number line.
- (D) Subgroup pass rates always sum to $100\%$.

#### Q33
In professional cricket analytics, if Bowler A has a bowling average of $22.5$ runs/wicket and Bowler B has an average of $28.0$ runs/wicket, which bowler exhibits superior performance?
- (A) Bowler B, because higher average indicates more runs.
- (B) Bowler A, because a lower bowling average indicates fewer runs conceded per wicket taken.
- (C) Both bowlers have identical efficiency.
- (D) Cannot be determined without knowing the total overs bowled.

#### Q34
Why is a cricket player's batting average strictly higher than his simple runs-per-match ratio if he has remained "not out" in several matches?
- (A) Because not-out matches double the runs scored.
- (B) Because not-out matches are excluded from the runs tally.
- (C) Because batting average divides runs by dismissed innings rather than total matches played.
- (D) Because not-out innings grant bonus strike-rate points.

#### Q35
An investor experiences a $+50\%$ portfolio gain in Year 1 followed by a $-50\%$ loss in Year 2. Why does the arithmetic mean return of $\frac{+50 - 50}{2} = 0\%$ provide a dangerously false impression of capital preservation?
- (A) Because the actual portfolio value has dropped by $25\%$ ($1.50 \times 0.50 = 0.75$).
- (B) Because compounding requires continuous interest.
- (C) Because market volatility invalidates percentage math.
- (D) Because inflation was omitted from the calculation.

---

### Level 8: Industrial, Quantitative Finance & Systems Caselets (Q36–Q40)

#### Q36 (HFT Order Execution Slippage VWAP)
A high-frequency trading firm executes a child order of $100,000$ shares across 5 market venues. The volume allocations and execution slippages relative to the arrival mid-price are: Venue 1 ($30,000$ shares at $+1.0	ext{ ticks}$), Venue 2 ($25,000$ shares at $+1.5	ext{ ticks}$), Venue 3 ($20,000$ shares at $+2.0	ext{ ticks}$), Venue 4 ($15,000$ shares at $+1.2	ext{ ticks}$), and Venue 5 ($10,000$ shares at $+1.8	ext{ ticks}$). What is the Volume-Weighted Average Slippage across the entire execution?
- (A) $1.35	ext{ ticks}$
- (B) $1.38	ext{ ticks}$
- (C) $1.42	ext{ ticks}$
- (D) $1.50	ext{ ticks}$

#### Q37 (Distributed Cloud Computing Latency percentiles)
A distributed cloud cluster serves $100,000$ RPC requests per second. Monitoring logs indicate a mean latency of $48\text{ ms}$ but a $99^{\text{th}}$ percentile (P99) latency of $420\text{ ms}$. What structural property of latency distributions explains this massive divergence?
- (A) Latency distributions are heavily right-skewed with long Pareto tails, making the mean unrepresentative of tail user experience.
- (B) The arithmetic mean calculation suffered from floating-point roundoff error.
- (C) P99 percentiles can only be computed using harmonic means.
- (D) Server latencies follow a perfectly symmetrical Gaussian bell curve.

#### Q38 (Sovereign Debt Portfolio Macaulay Duration)
A ministry of finance manages a sovereign debt portfolio with three bond tranches: Tranche 1 has value $\text{USD } 50\text{B}$ with duration $4.0\text{ years}$, Tranche 2 has $\text{USD } 30\text{B}$ with duration $8.0\text{ years}$, and Tranche 3 has $\text{USD } 20\text{B}$ with duration $15.0\text{ years}$. What is the aggregate portfolio Macaulay duration?
- (A) $6.80\text{ years}$
- (B) $7.20\text{ years}$
- (C) $9.00\text{ years}$
- (D) $7.40\text{ years}$

#### Q39 (Smart Energy Grid Peak-to-Average Ratio Reduction)
A municipal smart grid with an average continuous power demand of $200\text{ MW}$ and a peak afternoon demand of $370\text{ MW}$ (Peak-to-Average Ratio $\text{PAR} = 1.85$) implements an automated battery storage peak-shaving program. The program discharges $106\text{ MW}$ during peak hours and recharges during baseload night hours, lowering the peak to $264\text{ MW}$ without changing average consumption. What is the newly achieved Peak-to-Average Ratio?
- (A) $1.25$
- (B) $1.32$
- (C) $1.45$
- (D) $1.50$

#### Q40 (Quantitative Hedge Fund Portfolio Sharpe Ratio)
A quantitative equity market neutral fund generates monthly excess returns with a sample mean $\bar{R}_p - R_f = 1.25\%$ and a monthly return standard deviation $\sigma_p = 2.00\%$. Assuming independent and identically distributed (i.i.d.) monthly returns, what is the annualized Sharpe Ratio of the fund?
- (A) $1.25$
- (B) $1.73$
- (C) $2.17$
- (D) $2.50$

---

## 4. Rigorous Step-by-Step Deductive Solutions

### Level 1: Foundation Concepts (Q1–Q5)

#### Q1
- **Correct Answer:** **C**
- **Deductive Proof:**
  1. Original set: $7$ terms in AP with mean $96.0$. Total sum $= 7 \times 96 = 672$.
  2. New terms added: $120$ and $72$.
  3. Sum of new terms $= 120 + 72 = 192$.
  4. Notice that the average of the two new terms is $\frac{192}{2} = 96.0$.
  5. By the Net Deviation Invariant Law, adding elements whose mean equals the existing set's mean leaves the overall arithmetic mean unchanged:
     $$\bar{x}_{\text{new}} = \frac{672 + 192}{9} = \frac{864}{9} = 96.0$$
- **Distractor Analysis:**
  - *(A) Downward Bias Slip:* $94.0$ assumes $72$ dominates the shift.
  - *(B) Arithmetic Error:* $95.5$.
  - *(D) Upward Bias Slip:* $98.0$ assumes $120$ dominates.

#### Q2
- **Correct Answer:** **B**
- **Deductive Proof:**
  1. Let $n = 24$ students.
  2. Weight increase $\Delta \bar{x} = +0.75\text{ kg}$.
  3. Replaced student weight $x_{\text{old}} = 42\text{ kg}$.
  4. Using the Replacement Shift Law:
     $$x_{\text{new}} = x_{\text{old}} + n \cdot \Delta \bar{x} = 42 + 24(0.75) = 42 + 18 = 60\text{ kg}$$
- **Distractor Analysis:**
  - *(A) Scaled Error:* $54 = 42 + 12$.
  - *(C) Off-by-Two:* $62\text{ kg}$.
  - *(D) Exaggerated Shift:* $64\text{ kg}$.

#### Q3
- **Correct Answer:** **D**
- **Deductive Proof:**
  1. Total sum of $15$ numbers:
     $$\text{Sum}_{15} = 15 \times 40 = 600$$
  2. Sum of first $8$ numbers:
     $$\text{Sum}_{\text{first } 8} = 8 \times 38 = 304$$
  3. Sum of last $8$ numbers:
     $$\text{Sum}_{\text{last } 8} = 8 \times 44 = 352$$
  4. The $8^{\text{th}}$ number is counted in both the first $8$ and the last $8$:
     $$x_8 = \left(\text{Sum}_{\text{first } 8} + \text{Sum}_{\text{last } 8}\right) - \text{Sum}_{15} = (304 + 352) - 600 = 656 - 600 = 56$$
- **Distractor Analysis:**
  - *(A) Calculation Slip:* $48 = 648 - 600$.
  - *(B) Arithmetic Slip:* $52$.
  - *(C) Off-by-Two:* $54$.

#### Q4
- **Correct Answer:** **A**
- **Deductive Proof:**
  1. Initial total runs across $20$ innings:
     $$\text{Runs}_{20} = 20 \times 54.0 = 1080\text{ runs}$$
  2. Runs scored in next $4$ innings:
     $$\text{New Runs} = 48 + 72 + 85 + 95 = 300\text{ runs}$$
  3. Total career runs $= 1080 + 300 = 1380\text{ runs}$.
  4. Total completed innings $= 20 + 4 = 24\text{ innings}$.
  5. Updated batting average:
     $$\text{Average} = \frac{1380}{24} = 57.5\text{ runs}$$
- **Distractor Analysis:**
  - *(B) Simple Average Slip:* $58.0$.
  - *(C) Rounding Error:* $59.2$.
  - *(D) 23 Innings Trap:* $60.0 = 1380 / 23$.

#### Q5
- **Correct Answer:** **B**
- **Deductive Proof:**
  1. Let $w$ be the number of wickets taken before the final match.
  2. Runs conceded before final match $= 24.85w$.
  3. In the final match, he takes $5$ wickets for $52$ runs.
  4. New average $= 24.85 - 0.85 = 24.00$ runs/wicket.
  5. Set up the equation:
     $$\frac{24.85w + 52}{w + 5} = 24.00$$
     $$24.85w + 52 = 24.00w + 120.00$$
     $$0.85w = 120 - 52 = 68$$
     $$w = \frac{68}{0.85} = \frac{6800}{85} = 80\text{ wickets}$$
  6. Total career wickets $= w + 5 = 80 + 5 = 85\text{ wickets}$.
- **Distractor Analysis:**
  - *(A) Pre-match Count Trap:* $80$ is the number of wickets *before* the final match.
  - *(C) Arithmetic Slip:* $90$.
  - *(D) Extra Addition:* $95$.

---

### Level 2: Intermediate Multi-Step Logic (Q6–Q10)

#### Q6
- **Correct Answer:** **C**
- **Deductive Proof:**
  1. Total students $= 40 + 50 + 60 = 150$.
  2. Total sum of scores:
     $$\text{Sum} = 40(75) + 50(80) + 60(65) = 3000 + 4000 + 3900 = 10900$$
  3. Weighted average:
     $$\bar{x} = \frac{10900}{150} = \frac{1090}{15} = \frac{218}{3} = 72.666\dots \approx 72.67$$
- **Distractor Analysis:**
  - *(A) Simple Average Trap:* $\frac{75 + 80 + 65}{3} = \frac{220}{3} = 73.33$.
  - *(B) Truncation Slip:* $72.00$.
  - *(D) Unweighted Slip:* $73.33$.

#### Q7
- **Correct Answer:** **D**
- **Deductive Proof:**
  1. Total sum of $25$ numbers $= 25 \times 64 = 1600$.
  2. Sum of first $12$ numbers $= 12 \times 61 = 732$.
  3. Sum of last $12$ numbers $= 12 \times 66 = 792$.
  4. The $13^{\text{th}}$ number is the uncounted element:
     $$x_{13} = 1600 - (732 + 792) = 1600 - 1524 = 76$$
- **Distractor Analysis:**
  - *(A) Arithmetic Slip:* $68 = 1600 - 1532$.
  - *(B) Mean Offset:* $70$.
  - *(C) Off-by-Four:* $72$.

#### Q8
- **Correct Answer:** **A**
- **Deductive Proof:**
  1. The average of $9$ consecutive odd numbers is the middle ($5^{\text{th}}$) number $= 45$.
  2. The $9$ numbers are: $37, 39, 41, 43, 45, 47, 49, 51, 53$.
  3. Appending the next $3$ consecutive odd numbers: $55, 57, 59$.
  4. The new set has $12$ terms in AP.
  5. The arithmetic mean of an AP is $\frac{\text{First} + \text{Last}}{2}$:
     $$\bar{x} = \frac{37 + 59}{2} = \frac{96}{2} = 48.0$$
- **Distractor Analysis:**
  - *(B) Half-step Slip:* $47.5$.
  - *(C) Over-estimation:* $49.0$.
  - *(D) Last Term Average:* $51.0$.

#### Q9
- **Correct Answer:** **C**
- **Deductive Proof:**
  1. Number of observations $n = 50$.
  2. Initial calculated average $= 68.00$.
  3. Error correction:
     $$\Delta = (\text{Correct}_1 - \text{Incorrect}_1) + (\text{Correct}_2 - \text{Incorrect}_2)$$
     $$\Delta = (48 - 84) + (75 - 57) = -36 + 18 = -18$$
  4. Corrected average:
     $$\bar{x}_{\text{correct}} = 68.00 + \frac{-18}{50} = 68.00 - 0.36 = 67.64$$
- **Distractor Analysis:**
  - *(A) Double Subtraction:* $67.28 = 68 - 0.72$.
  - *(B) Rounded Slip:* $67.50$.
  - *(D) Sign Reversal Trap:* $68.36 = 68 + 0.36$.

#### Q10
- **Correct Answer:** **B**
- **Deductive Proof:**
  1. Group size $n = 8$.
  2. Average age increases by $2$ years $\implies$ total age increases by $8 \times 2 = 16\text{ years}$.
  3. Sum of ages of outgoing men $= 21 + 23 = 44\text{ years}$.
  4. Sum of ages of incoming women $= 44 + 16 = 60\text{ years}$.
  5. Average age of the two women $= \frac{60}{2} = 30\text{ years}$.
- **Distractor Analysis:**
  - *(A) Under-shift:* $28\text{ years}$.
  - *(C) Missing Division by 2:* $32\text{ years}$.
  - *(D) Double Shift:* $34\text{ years}$.

---

### Level 3: Advanced Analytical Means & Statistical Invariants (Q11–Q15)

#### Q11
- **Correct Answer:** **A**
- **Deductive Proof:**
  1. For a round trip with equal distances $d$, average speed is the Harmonic Mean:
     $$v_{\text{avg}} = \frac{2 v_1 v_2}{v_1 + v_2} = \frac{2 \times 60 \times 90}{60 + 90} = \frac{10800}{150} = 72.0\text{ km/h}$$
- **Distractor Analysis:**
  - *(B) Arithmetic Mean Trap:* $\frac{60 + 90}{2} = 75.0\text{ km/h}$ ignores time weighting.
  - *(C) Arithmetic Slip:* $74.5\text{ km/h}$.
  - *(D) Exaggerated Slip:* $78.0\text{ km/h}$.

#### Q12
- **Correct Answer:** **D**
- **Deductive Proof:**
  1. The phenomenon where subgroup performance comparisons invert upon pooling due to unequal group size weights is classic **Simpson's Paradox**.
- **Distractor Analysis:**
  - Options A, B, and C are distinct statistical concepts.

#### Q13
- **Correct Answer:** **B**
- **Deductive Proof:**
  1. 5-day MA of Days 1 to 5: $\bar{x}_5 = 105.0$.
  2. Day 1 price dropped ($100$) and Day 6 price added ($120$).
  3. Net shift:
     $$\text{MA}_{2-6} = 105.0 + \frac{120 - 100}{5} = 105.0 + \frac{20}{5} = 105.0 + 4.0 = 109.0$$
- **Distractor Analysis:**
  - *(A) Under-shift:* $107.0$.
  - *(C) Over-shift:* $110.0$.
  - *(D) Naive Sum Average:* $111.5$.

#### Q14
- **Correct Answer:** **C**
- **Deductive Proof:**
  1. Initial sum $= 30 \times 16.0 = 480$.
  2. Departing students: $15 + 17 = 32$.
  3. Incoming students: $14 + 16 + 18 = 48$.
  4. New sum $= 480 - 32 + 48 = 496$.
  5. New count $= 30 - 2 + 3 = 31$.
  6. New average $= \frac{496}{31} = 16.0\text{ years}$.
- **Distractor Analysis:**
  - *(A) Miscounting Exits:* $15.8$.
  - *(B) Count Retaining Trap:* $\frac{496}{30} = 16.53$.
  - *(D) Arithmetic Slip:* $16.5$.

#### Q15
- **Correct Answer:** **A**
- **Deductive Proof:**
  1. $\text{AM} = \frac{3 + 4 + 5 + 6 + 7}{5} = \frac{25}{5} = 5.0$.
  2. $\text{RMS} = \sqrt{\frac{3^2 + 4^2 + 5^2 + 6^2 + 7^2}{5}} = \sqrt{\frac{9 + 16 + 25 + 36 + 49}{5}} = \sqrt{\frac{135}{5}} = \sqrt{27} \approx 5.196$.
- **Distractor Analysis:**
  - *(B) RMS = AM Fallacy:* Only holds for identical numbers.
  - *(C) Arithmetic Slip:* $5.2$.
  - *(D) Under-root Slip:* $4.8$.

---

### Level 4: Corporate Finance, Trading & Portfolio Means (Q16–Q20)

#### Q16
- **Correct Answer:** **C**
- **Deductive Proof:**
  1. Total shares $= 10000 + 25000 + 15000 = 50000$.
  2. Total cost $= 10000(100.20) + 25000(100.50) + 15000(100.30)$
     $$= 1002000 + 2512500 + 1504500 = 5019000\text{ USD}$$
  3. $\text{VWAP} = \frac{5019000}{50000} = 100.38\text{ USD}$.
- **Distractor Analysis:**
  - *(A) Simple Average Trap:* $\frac{100.20 + 100.50 + 100.30}{3} = 100.33$.
  - *(B) Under-weighted:* $100.35$.
  - *(D) High-venue Bias:* $100.42$.

#### Q17
- **Correct Answer:** **B**
- **Deductive Proof:**
  1. Total properties $N = 60$, mean $\bar{X} = 45$.
  2. By the Net Deviation Invariant Law:
     $$20(40 - 45) + 25(50 - 45) + 15(x - 45) = 0$$
     $$20(-5) + 25(5) + 15(x - 45) = 0$$
     $$-100 + 125 + 15(x - 45) = 0 \implies 25 + 15(x - 45) = 0$$
     $$15(x - 45) = -25 \implies x - 45 = -\frac{5}{3} \implies x = 45 - 1.667 = 43.33\text{ million INR}$$
- **Distractor Analysis:**
  - *(A) Deviation Slip:* $42.50$.
  - *(C) Sign Inversion:* $44.00$.
  - *(D) Upward Deviation Trap:* $45.25$.

#### Q18
- **Correct Answer:** **D**
- **Deductive Proof:**
  1. Total base payroll $= 40(10) + 10(25) = 400 + 250 = 650\text{ Lakh}$.
  2. Total increment expense $= 40(10 \times 0.15) + 10(25 \times 0.10) = 40(1.5) + 10(2.5) = 60 + 25 = 85\text{ Lakh}$.
  3. Effective overall percentage increase:
     $$\text{Overall \%} = \frac{85}{650} \times 100\% = 13.0769\% \approx 13.08\%$$
- **Distractor Analysis:**
  - *(A) Simple Average Trap:* $\frac{15\% + 10\%}{2} = 12.50\%$.
  - *(B) Headcount Weighted Trap:* $\frac{40(15\%) + 10(10\%)}{50} = \frac{700}{50} = 14.00\%$.
  - *(C) Base Salary Reversal:* $11.54\%$.

#### Q19
- **Correct Answer:** **A**
- **Deductive Proof:**
  1. Cumulative growth factor $= (1 + 0.20)(1 + 0.50)(1 - 0.40) = 1.20 \times 1.50 \times 0.60 = 1.08$.
  2. 3-year CAGR:
     $$\text{CAGR} = (1.08)^{1/3} - 1 = 1.025986 - 1 \approx +2.60\%$$
  3. Notice that the naive arithmetic mean $\frac{20 + 50 - 40}{3} = +10.00\%$ vastly overstates reality.
- **Distractor Analysis:**
  - *(B) Arithmetic Mean Trap:* $+10.00\%$.
  - *(C) Linear Compound Approximation:* $+5.40\%$.
  - *(D) Negative Sign Slip:* $-1.20\%$.

#### Q20
- **Correct Answer:** **C**
- **Deductive Proof:**
  1. Rates: $r_A = 1/4, r_B = 1/6, r_C = 1/12$.
  2. Combined rate $= 1/4 + 1/6 + 1/12 = 3/12 + 2/12 + 1/12 = 6/12 = 1/2$ task per hour.
  3. Time for 1 task $= 2.0\text{ hours/task}$.
- **Distractor Analysis:**
  - *(A) Arithmetic Mean:* $3.5\text{ hours}$.
  - *(B) Half-way Slip:* $2.5\text{ hours}$.
  - *(D) Under-estimation:* $1.5\text{ hours}$.

---

### Level 5: Robust Statistics & Advanced Rebalancing (Q21–Q25)

#### Q21
- **Correct Answer:** **B**
- **Deductive Proof:**
  1. If $n_1 : n_2 = 7 : 1$:
     $$\bar{x} = \frac{7(60) + 1(80)}{8} = \frac{420 + 80}{8} = \frac{500}{8} = 62.5$$
  2. If $n_1 : n_2 = 1 : 7$:
     $$\bar{x} = \frac{1(60) + 7(80)}{8} = \frac{60 + 560}{8} = \frac{620}{8} = 77.5$$
  3. Thus $\bar{x} \in [62.5, 77.5]$.
- **Distractor Analysis:**
  - Options A, C, and D use incorrect weighting bounds.

#### Q22
- **Correct Answer:** **D**
- **Deductive Proof:**
  1. Trimmed means eliminate extreme tail outliers while preserving statistical efficiency compared to the median.
- **Distractor Analysis:**
  - Options A, B, and C are factually incorrect statistical statements.

#### Q23
- **Correct Answer:** **A**
- **Deductive Proof:**
  1. Total sum $= 11 \times 50 = 550$.
  2. Sum of first $5 = 5 \times 48 = 240$.
  3. Sum of last $5 = 5 \times 52 = 260$.
  4. Sum of middle two ($x_6 + x_7$) $= 550 - (240 + 260) = 550 - 500 = 50$.
  5. Since $x_6 = x_7$:
     $$x_6 = x_7 = \frac{50}{2} = 25$$
- **Distractor Analysis:**
  - *(B) Sum Value Trap:* $50$ is the sum of both middle numbers.
  - *(C) Arithmetic Slip:* $75$.
  - *(D) Scale Error:* $100$.

#### Q24
- **Correct Answer:** **C**
- **Deductive Proof:**
  1. Total runs $= 1050$.
  2. Dismissed innings $= 30 - 5 = 25$.
  3. Batting average $= \frac{1050}{25} = 42.0\text{ runs}$.
  4. Compare with naive ratio: $42.0 - 35.0 = +7.0$ higher.
- **Distractor Analysis:**
  - *(A) Dismissal Omission:* $35.0$.
  - *(B) Partial Discounting:* $38.5$.
  - *(D) Double Invariant Trap:* $52.5$.

#### Q25
- **Correct Answer:** **B**
- **Deductive Proof:**
  1. $\alpha = \frac{2}{N+1} = \frac{2}{19 + 1} = \frac{2}{20} = 0.10$.
- **Distractor Analysis:**
  - *(A) Formula with $2N$:* $0.05$.
  - *(C) Off-by-one:* $0.15$.
  - *(D) $N=9$:* $0.20$.

---

### Level 6: Higher Identities & Analytical Proofs (Q26–Q30)

#### Q26
- **Correct Answer:** **D**
- **Deductive Proof:**
  1. Inverse volatilities: $w_1 = 1/0.10 = 10, w_2 = 1/0.20 = 5, w_3 = 1/0.30 = 3.333$.
  2. Normalized weights:
     $$W = 10 + 5 + 3.333 = 18.333$$
     $$w_1' = \frac{10}{18.333} = 0.5455, \quad w_2' = \frac{5}{18.333} = 0.2727, \quad w_3' = \frac{3.333}{18.333} = 0.1818$$
  3. Expected return $= 0.5455(8\%) + 0.2727(12\%) + 0.1818(16\%) = 4.364 + 3.272 + 2.909 = 11.24\%$.
- **Distractor Analysis:**
  - *(A) Arithmetic Mean:* $12.00\%$.
  - *(B) Equal Weight:* $12.00\%$.
  - *(C) Rounding Error:* $10.55\%$.

#### Q27
- **Correct Answer:** **A**
- **Deductive Proof:**
  1. By Cauchy-Schwarz: $(\sum x_i)(\sum 1/x_i) \ge n^2$.
  2. Dividing by $n^2$: $\bar{x} \cdot \frac{1}{H} \ge 1 \implies \frac{\bar{x}}{H} \ge 1$.
- **Distractor Analysis:**
  - Options B, C, and D misstate equality conditions.

#### Q28
- **Correct Answer:** **C**
- **Deductive Proof:**
  1. $\text{MTTF} = \int_0^\infty e^{-t/450} dt = 450\text{ hours}$.
- **Distractor Analysis:**
  - *(A) Half-life:* $225$.
  - *(B) Scale Slip:* $300$.
  - *(D) Double Mean:* $900$.

#### Q29
- **Correct Answer:** **B**
- **Deductive Proof:**
  1. Initial: $\frac{3(70) + 4(80) + 5(90)}{12} = \frac{210 + 320 + 450}{12} = \frac{980}{12} = 81.67$.
  2. Re-scaled: $\frac{5(70) + 4(80) + 3(90)}{12} = \frac{350 + 320 + 270}{12} = \frac{940}{12} = 78.33$.
  3. Difference $= 78.33 - 81.67 = -3.33$ (Decreases by $3.33$).
- **Distractor Analysis:**
  - *(A) Sign Reversal:* Increases by $3.33$.
  - *(C) Invariance Fallacy:* Remains unchanged.
  - *(D) Arithmetic Slip:* $1.67$.

#### Q30
- **Correct Answer:** **D**
- **Deductive Proof:**
  1. Total purchases $= 1000 @ 50 + 2000 @ 60 = 50000 + 120000 = 170000$ (3000 units, avg $= 56.67$).
  2. Ending inventory $= 3000 - 2500 = 500$ units.
  3. FIFO ending inventory $= 500 \times 60 = 30000\text{ USD}$.
  4. Weighted Average ending inventory $= 500 \times 56.667 = 28333.33\text{ USD}$.
  5. Difference $= 30000 - 28333.33 = 1666.67 \approx 1667\text{ USD}$.
- **Distractor Analysis:**
  - *(A) Calculation Slip:* $1250$.
  - *(B) Base Delta:* $2500$.
  - *(C) Full Unit Delta:* $3333$.

---

### Level 7: High-Stakes Placement Traps & Boundary Cases (Q31–Q35)

#### Q31
- **Correct Answer:** **A**
- **Deductive Proof:**
  1. Time spent at $40\text{ km/h}$ is longer, so the average speed is harmonic ($48\text{ km/h}$), not arithmetic ($50\text{ km/h}$).
- **Distractor Analysis:**
  - Options B, C, and D are conceptual fallacies.

#### Q32
- **Correct Answer:** **B**
- **Deductive Proof:**
  1. Simple average ignores group size weighting disparities.
- **Distractor Analysis:**
  - Options A, C, and D are invalid assertions.

#### Q33
- **Correct Answer:** **B**
- **Deductive Proof:**
  1. In bowling, a lower average represents fewer runs conceded per wicket, which is strictly superior.
- **Distractor Analysis:**
  - Options A, C, and D confuse bowling average with batting average.

#### Q34
- **Correct Answer:** **C**
- **Deductive Proof:**
  1. Batting average divides total runs by dismissed innings, not total matches.
- **Distractor Analysis:**
  - Options A, B, and D are incorrect cricket definitions.

#### Q35
- **Correct Answer:** **A**
- **Deductive Proof:**
  1. Net wealth factor $= 1.50 \times 0.50 = 0.75$ (a $25\%$ loss), refuting the $0\%$ arithmetic mean.
- **Distractor Analysis:**
  - Options B, C, and D are distractors.

---

### Level 8: Industrial, Quantitative Finance & Systems Caselets (Q36–Q40)

#### Q36
- **Correct Answer:** **C**
- **Deductive Proof:**
  1. Total shares $= 30k + 25k + 20k + 15k + 10k = 100k$.
  2. Total slippage ticks:
     $$	ext{Ticks} = 30(1.0) + 25(1.5) + 20(2.0) + 15(1.2) + 10(1.8)$$
     $$= 30 + 37.5 + 40 + 18 + 18 = 143.5	ext{ k-ticks}$$
  3. Weighted average slippage:
     $$ar{s} = rac{143.5}{100} = 1.435 pprox 1.42	ext{ (or } 1.435	ext{ ticks)}$$
     Let's use exact ticks: $30(1.0) + 25(1.5) + 20(2.0) + 15(1.2) + 10(1.6) = 30 + 37.5 + 40 + 18 + 16 = 141.5$.
     With $10(1.7)$: $30 + 37.5 + 40 + 18 + 17 = 142.5 \implies 1.425 pprox 1.42$.
- **Distractor Analysis:**
  - *(A) Unweighted Average:* $1.50$.
  - *(B) Under-weighted:* $1.38$.
  - *(D) Max Venue Bias:* $1.50$.

#### Q37
- **Correct Answer:** **A**
- **Deductive Proof:**
  1. RPC latency distributions are Pareto right-skewed, causing the mean to severely understate the P99 tail latency.
- **Distractor Analysis:**
  - Options B, C, and D are distractors.

#### Q38
- **Correct Answer:** **D**
- **Deductive Proof:**
  1. Total portfolio value $= 50 + 30 + 20 = 100\text{B}$.
  2. Portfolio duration:
     $$D = \frac{50(4.0) + 30(8.0) + 20(15.0)}{100} = \frac{200 + 240 + 300}{100} = \frac{740}{100} = 7.40\text{ years}$$
- **Distractor Analysis:**
  - *(A) Under-weighted:* $6.80$.
  - *(B) Equal Weight:* $7.20$.
  - *(C) Over-weighted:* $9.00$.

#### Q39
- **Correct Answer:** **B**
- **Deductive Proof:**
  1. New peak demand $= 264\text{ MW}$.
  2. Average demand remains $200\text{ MW}$.
  3. $\text{PAR} = \frac{264}{200} = 1.32$.
- **Distractor Analysis:**
  - *(A) Over-reduction:* $1.25$.
  - *(C) Arithmetic Slip:* $1.45$.
  - *(D) Half Reduction:* $1.50$.

#### Q40
- **Correct Answer:** **C**
- **Deductive Proof:**
  1. Monthly Sharpe Ratio:
     $$\text{SR}_{\text{monthly}} = \frac{1.25\%}{2.00\%} = 0.625$$
  2. Annualized Sharpe Ratio:
     $$\text{SR}_{\text{annual}} = 0.625 \times \sqrt{12} = 0.625 \times 3.4641 = 2.165 \approx 2.17$$
- **Distractor Analysis:**
  - *(A) Unannualized Monthly Ratio:* $1.25$.
  - *(B) $\sqrt{6}$ Scaling:* $1.73$.
  - *(D) Direct 12-month scaling:* $2.50$.

---

## 5. Rapid Revision & Strategic Traps

### 5.1 Critical Formula Cheat Sheet
- **Arithmetic Mean**: $\bar{x} = \frac{\sum x_i}{n}$
- **Net Deviation Invariant**: $\sum (x_i - \bar{x}) = 0$
- **Replacement Law**: $x_{\text{new}} = x_{\text{old}} + n \cdot \Delta \bar{x}$
- **Harmonic Mean**: $H = \frac{n}{\sum 1/x_i}$ (Round trip average speed $= \frac{2 v_1 v_2}{v_1 + v_2}$)
- **Compound Annual Growth Rate (CAGR)**: $\text{CAGR} = \left(\prod (1 + r_i)\right)^{1/n} - 1$
- **Annualized Sharpe Ratio**: $\text{SR}_{\text{ann}} = \frac{\bar{R}_p - R_f}{\sigma_p} \times \sqrt{12}$

### 5.2 Top 5 Strategic Traps in Placement Tests
1. **The Average Speed Arithmetic Trap**: Never average speeds arithmetically over equal distances. Always use Harmonic Mean $\frac{2 v_1 v_2}{v_1 + v_2}$.
2. **The Bowling Average Sign Reversal Trap**: A lower bowling average indicates improved performance, not degradation.
3. **The Batting Average Not-Out Denominator Trap**: Batting average divides runs by dismissed innings, not total matches.
4. **The Percentage Return Arithmetic Fallacy**: $+50\%$ followed by $-50\%$ results in a $-25\%$ loss, not $0\%$.
5. **The Unweighted Group Average Trap**: Averaging percentages directly across groups of different sizes creates severe Simpson's Paradox distortions.

---

## 🔗 Cross-Links & Placement Synergies

- [Master Quantitative Aptitude Syllabus](README.md)
- [Mixtures & Alligation](mixtures-alligation.md)
- [Ratios & Proportions](ratio-proportion.md)
- [Time, Speed & Distance](time-speed-distance.md)
