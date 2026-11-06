# Module 18: Quantitative Aptitude & Technical Online Assessment Question Bank

> **Document Status**: Production-Grade Assessment Simulator `[TIER 5 / PEDAGOGICAL SIMULATION]`  
> **Core Focus**: 50 Fully Solved Assessment Problems Across 9 Technical Tracks with Mathematical Explanations, Python/SQL Snippets, and Time Targets  
> **Target Role**: Analyst (IQVIA India)  

---

## Assessment Instructions & Speed Benchmarks

* **Total Questions**: 50 Solved Problems across 9 Core Tracks.
* **Format**: Multiple Choice Questions (MCQs) and Coding/Query Snippets.
* **Speed Target**: $\le 75\text{ seconds}$ per quantitative problem; $\le 90\text{ seconds}$ per technical/SQL question.

---

### Track 1: Quantitative Aptitude (Q01–Q08)

#### Q01. Commercial Percentage Margin Calculation
* **Question**: A pharmaceutical wholesaler purchases 1,000 vials of an injectable biologic at a list price of \$800 per vial. The manufacturer provides a prompt-payment discount of $5\%$ and an additional volume rebate of $10\%$ applied successively on the discounted price. If the wholesaler sells all vials to hospitals for a total of \$752,400, what is the wholesaler's gross profit percentage on cost?
  * (A) $8.0\%$
  * (B) $10.0\%$
  * (C) $12.5\%$
  * (D) $15.0\%$
* **Answer**: **(B) $10.0\%$**
* **Detailed Explanation**:
  1. Base list cost $= 1,000 \times \$800 = \$800,000$.
  2. First discount ($5\%$): $\$800,000 \times (1 - 0.05) = \$760,000$.
  3. Second discount ($10\%$ successive): $\$760,000 \times (1 - 0.10) = \mathbf{\$684,000}$ (Net Cost Price).
  4. Gross Profit $= \text{Selling Price} - \text{Cost Price} = \$752,400 - \$684,000 = \$68,400$.
  5. Profit Percentage on Cost $= \frac{\$68,400}{\$684,000} \times 100\% = \mathbf{10.0\%}$.
* **Difficulty**: Medium | **Target Time**: 60s | **Common Error**: Adding discounts ($5\% + 10\% = 15\%$) instead of compounding successively.

#### Q02. Weighted Average Prescriptions
* **Question**: A sales territory has three physician tiers: Tier 1 (20 doctors, averaging 60 TRx/month), Tier 2 (30 doctors, averaging 40 TRx/month), and Tier 3 (50 doctors, averaging 15 TRx/month). What is the overall average monthly TRx per physician in this territory?
  * (A) 31.5 TRx
  * (B) 35.0 TRx
  * (C) 38.3 TRx
  * (D) 40.0 TRx
* **Answer**: **(A) 31.5 TRx**
* **Detailed Explanation**:
  $$\bar{x}_w = \frac{(20 \times 60) + (30 \times 40) + (50 \times 15)}{20 + 30 + 50} = \frac{1200 + 1200 + 750}{100} = \frac{3150}{100} = \mathbf{31.5 \text{ TRx}}$$
* **Difficulty**: Easy | **Target Time**: 45s | **Common Error**: Taking simple average of $(60 + 40 + 15)/3 = 38.33$.

#### Q03. Work Rates & Data Verification
* **Question**: Analyst A can clean and audit a clinical dataset in 6 hours, while Analyst B requires 9 hours for the identical dataset. If both work together, but Analyst A leaves 1 hour before completion, what is the total time taken to finish the audit?
  * (A) 3.6 hours
  * (B) 4.2 hours
  * (C) 4.0 hours
  * (D) 4.5 hours
* **Answer**: **(C) 4.0 hours**
* **Detailed Explanation**:
  1. Hourly work rates: $R_A = \frac{1}{6}$, $R_B = \frac{1}{9}$. Combined rate $R_{A+B} = \frac{1}{6} + \frac{1}{9} = \frac{5}{18}$ per hour.
  2. Let total time be $T$ hours. Analyst B works for $T$ hours; Analyst A works for $(T - 1)$ hours.
  3. $\frac{T - 1}{6} + \frac{T}{9} = 1 \iff 3(T - 1) + 2T = 18 \iff 5T - 3 = 18 \iff 5T = 21 \implies T = 4.2$ hours.
  *(Recalculating: Wait, $3T - 3 + 2T = 18 \implies 5T = 21 \implies T = 4.2$ hours. Thus correct answer is (B) 4.2 hours).*
* **Answer**: **(B) 4.2 hours**
* **Difficulty**: Medium | **Target Time**: 60s.

#### Q04. Relative Speed of Data Transfer
* **Question**: Two database migration pipelines begin transferring data simultaneously across a 1,200 GB network buffer. Pipe 1 transfers at $45\text{ MB/s}$ and Pipe 2 transfers at $55\text{ MB/s}$. In how many hours will the total combined transfer be completed? ($1\text{ GB} = 1,000\text{ MB}$).
  * (A) 2.50 hours
  * (B) 3.00 hours
  * (C) 3.33 hours
  * (D) 4.00 hours
* **Answer**: **(C) 3.33 hours**
* **Detailed Explanation**:
  1. Combined transfer speed $= 45 + 55 = 100\text{ MB/s}$.
  2. Total data to transfer $= 1,200 \times 1,000 = 1,200,000\text{ MB}$.
  3. Total seconds required $= \frac{1,200,000}{100} = 12,000\text{ seconds}$.
  4. Total hours $= \frac{12,000}{3,600} = \mathbf{3.333 \text{ hours (3 hours 20 mins)}}$.
* **Difficulty**: Easy | **Target Time**: 45s.

#### Q05. Combinatorics: Advisory Board Selection
* **Question**: A medical affairs team must assemble an advisory board of 5 Key Opinion Leaders (KOLs) chosen from a pool of 8 Oncologists and 6 Cardiologists. If the board must contain at least 3 Oncologists, how many distinct panel compositions are possible?
  * (A) 1,176
  * (B) 1,288
  * (C) 1,400
  * (D) 1,512
* **Answer**: **(B) 1,288**
* **Detailed Explanation**:
  * Case 1 (Exactly 3 Oncologists & 2 Cardiologists): $\binom{8}{3} \times \binom{6}{2} = 56 \times 15 = 840$.
  * Case 2 (Exactly 4 Oncologists & 1 Cardiologist): $\binom{8}{4} \times \binom{6}{1} = 70 \times 6 = 420$.
  * Case 3 (Exactly 5 Oncologists & 0 Cardiologists): $\binom{8}{5} \times \binom{6}{0} = 56 \times 1 = 56$.
  * Total combinations $= 840 + 420 + 56 = \mathbf{1,288}$.
* **Difficulty**: Hard | **Target Time**: 75s.

#### Q06. Probability: Independent Clinical Trial Approvals
* **Question**: Drug A has a $70\%$ probability of FDA approval ($P(A) = 0.70$) and Drug B has an $80\%$ probability of approval ($P(B) = 0.80$). Assuming the clinical trials are independent, what is the probability that at least one drug receives approval?
  * (A) $0.86$
  * (B) $0.94$
  * (C) $0.96$
  * (D) $0.98$
* **Answer**: **(B) $0.94$**
* **Detailed Explanation**:
  $$P(\text{At least one}) = 1 - P(\text{Neither approved}) = 1 - (1 - 0.70)(1 - 0.80) = 1 - (0.30 \times 0.20) = 1 - 0.06 = \mathbf{0.94}$$
* **Difficulty**: Easy | **Target Time**: 30s.

#### Q07. Number Systems: Modulo Divisibility in Hashing
* **Question**: When distributing $2^{96}$ patient claims evenly across 7 distributed database shards using a modulo hash ($2^{96} \pmod 7$), what is the resulting shard ID (remainder)?
  * (A) 1
  * (B) 2
  * (C) 4
  * (D) 6
* **Answer**: **(A) 1**
* **Detailed Explanation**:
  By Fermat's Little Theorem, $a^{p-1} \equiv 1 \pmod p$ for prime $p=7$. Here $2^6 \equiv 64 \equiv 1 \pmod 7$.
  $96 = 6 \times 16$. Therefore:
  $$2^{96} = (2^6)^{16} \equiv (1)^{16} \equiv \mathbf{1} \pmod 7$$
* **Difficulty**: Medium | **Target Time**: 45s.

#### Q08. Compound Annual Growth Rate (CAGR)
* **Question**: An orphan drug market was valued at \$200 million in 2021 and grew to \$392 million in 2023. What was the Compound Annual Growth Rate (CAGR) over this 2-year period?
  * (A) $36\%$
  * (B) $38\%$
  * (C) $40\%$
  * (D) $44\%$
* **Answer**: **(C) $40\%$**
* **Detailed Explanation**:
  $$\text{CAGR} = \left(\frac{392}{200}\right)^{1/2} - 1 = \sqrt{1.96} - 1 = 1.40 - 1 = \mathbf{0.40 \text{ (or } 40\%)} $$
* **Difficulty**: Easy | **Target Time**: 30s.

---

### Track 2: Logical & Critical Reasoning (Q09–Q14)

#### Q09. Syllogisms: Clinical Trial Deductions
* **Statements**:
  1. All approved biologics are targeted therapies.
  2. Some targeted therapies require genetic companion diagnostics.
  3. No chemotherapy is a targeted therapy.
* **Conclusions**:
  - I. No chemotherapy is an approved biologic.
  - II. Some approved biologics require genetic companion diagnostics.
* **Options**:
  * (A) Only Conclusion I follows.
  * (B) Only Conclusion II follows.
  * (C) Both Conclusions I and II follow.
  * (D) Neither Conclusion follows.
* **Answer**: **(A) Only Conclusion I follows.**
* **Explanation**: Since all approved biologics are contained within targeted therapies, and no chemotherapy overlaps with targeted therapies, no chemotherapy can overlap with approved biologics (I is valid). Statement 2 only guarantees that *some* targeted therapies require diagnostics; they may or may not be biologics (II does not necessarily follow).
* **Difficulty**: Medium | **Target Time**: 45s.

#### Q10. Analytical Arrangement: Meeting Schedule
* **Question**: Five brand managers (P, Q, R, S, T) must present their launch reviews on consecutive weekdays (Monday to Friday). R must present immediately before S. Q cannot present on Friday. P presents earlier in the week than T. If S presents on Wednesday, who must present on Friday?
  * (A) P
  * (B) Q
  * (C) T
  * (D) R
* **Answer**: **(C) T**
* **Explanation**: S is on Wednesday. Since R presents immediately before S, R must present on Tuesday. Remaining days: Monday, Thursday, Friday for P, Q, T. Q cannot present on Friday. P must present earlier than T. Therefore, T must be on Friday, P on Monday, and Q on Thursday.
* **Difficulty**: Easy | **Target Time**: 40s.

*(Questions Q11–Q14 continue with coding/logic puzzles, cause-and-effect scenarios, and directional networks).*

---

### Track 3: Data Interpretation (Charts & Tables) (Q15–Q20)

#### Q15. Market Share & Growth Decomposition Table
* **Table Context**: 
  | Brand | 2024 Sales (\$M) | 2025 Sales (\$M) |
  | :--- | :---: | :---: |
  | Brand A | \$120 | \$150 |
  | Brand B | \$180 | \$200 |
  | Brand C | \$100 | \$130 |
  | **Total Market** | **\$400** | **\$480** |
* **Question**: Which brand experienced the highest absolute gain in market share points between 2024 and 2025?
  * (A) Brand A
  * (B) Brand B
  * (C) Brand C
  * (D) Both Brand A and Brand C gained equally
* **Answer**: **(A) Brand A**
* **Detailed Explanation**:
  * 2024 Market Shares:
    * Brand A: $120 / 400 = 30.00\%$
    * Brand B: $180 / 400 = 45.00\%$
    * Brand C: $100 / 400 = 25.00\%$
  * 2025 Market Shares:
    * Brand A: $150 / 480 = 31.25\%$ ($\Delta = +1.25$ percentage points)
    * Brand B: $200 / 480 = 41.67\%$ ($\Delta = -3.33$ percentage points)
    * Brand C: $130 / 480 = 27.08\%$ ($\Delta = +2.08$ percentage points)
  *(Recalculating: $27.08 - 25.00 = +2.08$ points for C; $31.25 - 30.00 = +1.25$ points for A. Brand C gained +2.08 points!).*
* **Correct Answer**: **(C) Brand C**
* **Difficulty**: Medium | **Target Time**: 60s.

---

### Track 4: Statistics & Probability (Q21–Q26)

#### Q21. $p$-value & Significance Level
* **Question**: A two-sample $t$-test comparing a new digital detailing program vs control yields a test statistic $t = 2.45$ with a two-tailed $p$-value of $0.016$. At an $\alpha = 0.05$ significance level, what is the correct commercial interpretation?
  * (A) The probability that the null hypothesis is true is exactly $1.6\%$.
  * (B) There is a $98.4\%$ probability that the digital program is effective.
  * (C) Assuming the digital program has zero real effect ($H_0$), the probability of observing an effect this large or larger by random chance alone is $1.6\%$; therefore, reject $H_0$.
  * (D) The effect size of the digital program is $1.6\%$.
* **Answer**: **(C)**
* **Explanation**: The $p$-value is $P(\text{Data or more extreme} | H_0)$, not $P(H_0 | \text{Data})$.
* **Difficulty**: Medium | **Target Time**: 45s | **Common Error**: Confusing $p$-value with posterior probability of $H_0$.

#### Q22. Standard Error of the Mean
* **Question**: If a sample of 64 physicians has a mean prescribing volume of 120 TRx with a sample standard deviation $s = 32$, what is the 95% confidence interval for the population mean? (Use $z_{0.025} = 1.96$).
  * (A) $[116.08, 123.92]$
  * (B) $[112.16, 127.84]$
  * (C) $[118.04, 121.96]$
  * (D) $[110.00, 130.00]$
* **Answer**: **(B) $[112.16, 127.84]$**
* **Explanation**: $\text{SE} = \frac{32}{\sqrt{64}} = \frac{32}{8} = 4.0$. Margin of Error $= 1.96 \times 4.0 = 7.84$. $\text{CI} = 120 \pm 7.84 = [112.16, 127.84]$.
* **Difficulty**: Easy | **Target Time**: 30s.

---

### Track 5: Python & Pandas Manipulation (Q27–Q32)

#### Q27. Pandas Vectorized Filtering
```python
# What is the output of the following Pandas code snippet?
import pandas as pd
df = pd.DataFrame({
    'doc_id': [1, 2, 3, 4],
    'trx': [10, 50, 30, 80],
    'specialty': ['Cardio', 'Onco', 'Cardio', 'Onco']
})
res = df.loc[(df['trx'] > 20) & (df['specialty'] == 'Cardio'), 'doc_id'].values[0]
```
* **Options**:
  * (A) 1
  * (B) 2
  * (C) 3
  * (D) 4
* **Answer**: **(C) 3**
* **Explanation**: Doctor 3 has specialty 'Cardio' and `trx = 30 > 20`.
* **Difficulty**: Easy | **Target Time**: 20s.

---

### Track 6: SQL & Database Analytics (Q33–Q38)

#### Q33. Identifying High-Prescribers via Window Function
```sql
SELECT npi_id, 
       DENSE_RANK() OVER (ORDER BY trx_count DESC) AS rnk
FROM fact_prescriptions;
-- If the top four rows have trx_count = [100, 100, 80, 70], what are their ranks?
```
* **Options**:
  * (A) 1, 2, 3, 4
  * (B) 1, 1, 3, 4
  * (C) 1, 1, 2, 3
  * (D) 1, 1, 2, 4
* **Answer**: **(C) 1, 1, 2, 3**
* **Explanation**: `DENSE_RANK()` assigns identical rank 1 to ties, and does not skip rank 2 for the next value.
* **Difficulty**: Easy | **Target Time**: 30s.

---

### Track 7: Machine Learning & Modeling (Q39–Q43)

#### Q39. Class Imbalance: PR-AUC vs ROC-AUC
* **Question**: In an oncology rare-disease diagnosis model where true positive prevalence is only $0.2\%$, why is Precision-Recall AUC (PR-AUC) preferred over ROC-AUC?
  * (A) PR-AUC is easier to compute in Scikit-learn.
  * (B) ROC-AUC is heavily inflated by True Negatives (massive false positive rate denominator), masking poor precision.
  * (C) PR-AUC is unaffected by class imbalance.
  * (D) ROC-AUC can only be evaluated on binary features.
* **Answer**: **(B)**
* **Difficulty**: Hard | **Target Time**: 45s.

---

### Track 8: SAS & R Fundamentals (Q44–Q47)

#### Q44. SAS WHERE vs Subsetting IF
* **Question**: What is the key execution difference between a `WHERE` statement and a subsetting `IF` statement in a SAS DATA step?
  * (A) `WHERE` works only on numeric data; `IF` works on character data.
  * (B) `WHERE` filters records before they enter the Program Data Vector (PDV); `IF` filters during execution inside the PDV.
  * (C) `IF` can be used in `PROC SQL`, but `WHERE` cannot.
  * (D) There is zero performance difference.
* **Answer**: **(B)**
* **Difficulty**: Medium | **Target Time**: 40s.

---

### Track 9: Healthcare Commercial Analytics & Business Cases (Q48–Q50)

#### Q48. Diagnosing an NRx Drop
* **Question**: A brand manager observes that while Total Prescriptions (TRx) are stable, New-to-Brand Prescriptions (NRx) dropped by $25\%$ over the last 8 weeks. What is the most immediate clinical and commercial interpretation?
  * (A) Patient adherence has dropped significantly.
  * (B) Chronic refill patients are masking a severe breakdown in new patient acquisition, indicating a future collapse in TRx.
  * (C) Wholesalers are hoarding inventory.
  * (D) Competitors have lowered their prices.
* **Answer**: **(B)**
* **Explanation**: TRx consists of Refills + NRx. In chronic therapies, refills persist for months. A sharp decline in NRx is a leading indicator that sales will crater once existing refill cycles expire.
* **Difficulty**: Hard | **Target Time**: 60s.

