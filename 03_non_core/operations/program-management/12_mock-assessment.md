# 12. Program Management: Comprehensive Technical Mock Assessment

> **Exam Focus**: Schedule Network Analysis (CPM/PERT), Earned Value Systems (EVM) & Program Governance  
> **Target Audience**: IIT Kanpur candidates preparing for Technical Program Manager (TPM), Project Lead, and Corporate Operations assessments.  
> **Duration**: 60 Minutes  
> **Total Marks**: 50 Marks (+2 for correct MCQ, -0.66 for incorrect; Full stepwise credit for analytical derivations).  
> **Calculators**: Scientific calculator permitted.

---

## Section A: Conceptual & Quantitative Program MCQs (10 Marks)

### Q1. Total Float vs. Free Float
Activity $K$ has an Early Start ($ES$) of day 10, an Early Finish ($EF$) of day 18, and a Late Finish ($LF$) of day 24. The earliest start time of all immediate successor activities is day 21 ($\min \{ES_{\text{succ}}\} = 21$). What are the Total Float ($TF$) and Free Float ($FF$) of Activity $K$?
- **(a)** $TF = 6\text{ days}$, $FF = 3\text{ days}$
- **(b)** $TF = 6\text{ days}$, $FF = 6\text{ days}$
- **(c)** $TF = 8\text{ days}$, $FF = 3\text{ days}$
- **(d)** $TF = 3\text{ days}$, $FF = 0\text{ days}$

### Q2. PERT Expected Task Duration & Variance
An engineering activity has an optimistic time $a = 6\text{ days}$, a most likely time $m = 11\text{ days}$, and a pessimistic time $b = 22\text{ days}$. According to standard PERT Beta distribution formulas, what are the expected duration ($t_e$) and variance ($\sigma^2$)?
- **(a)** $t_e = 12.0\text{ days}$, $\sigma^2 = 7.11$
- **(b)** $t_e = 13.0\text{ days}$, $\sigma^2 = 2.67$
- **(c)** $t_e = 12.0\text{ days}$, $\sigma^2 = 2.67$
- **(d)** $t_e = 11.0\text{ days}$, $\sigma^2 = 7.11$

### Q3. Earned Value Performance Interpretation
At Month 6 of a corporate digital transformation program, an EVM audit reports: Cost Performance Index $CPI = 1.15$ and Schedule Performance Index $SPI = 0.85$. This indicates that the program is currently:
- **(a)** Over budget and ahead of schedule.
- **(b)** Under budget and ahead of schedule.
- **(c)** Over budget and behind schedule.
- **(d)** Under budget and behind schedule.

### Q4. Crashing Cost Slope
Activity $M$ has a normal duration of 10 days at a cost of $₹40,000$. It can be crashed to a minimum duration of 6 days at a total cost of $₹64,000$. Assuming a linear cost-time relationship, what is the cost slope (crash cost per day saved) for Activity $M$?
- **(a)** $₹4,000/\text{day}$
- **(b)** $₹6,000/\text{day}$
- **(c)** $₹10,667/\text{day}$
- **(d)** $₹24,000/\text{day}$

### Q5. RACI Responsibility Assignment Rule
In a properly configured RACI stakeholder governance matrix, for any single task or deliverable:
- **(a)** Multiple individuals can be assigned 'Accountable' (A) to ensure joint executive responsibility.
- **(b)** Exactly one person must be assigned 'Accountable' (A) to avoid ambiguous decision ownership.
- **(c)** Every stakeholder must be marked either 'Responsible' (R) or 'Accountable' (A).
- **(d)** 'Informed' (I) stakeholders have veto power over milestone releases.

---

## Section B: Analytical PERT Program Completion Probability (15 Marks)

### Problem 6: Statistical Project Duration Derivation
A defense satellite communication program has a critical path consisting of four independent, sequential engineering activities ($P \to Q \to R \to S$):

| Activity | Optimistic Time ($a$, Weeks) | Most Likely Time ($m$, Weeks) | Pessimistic Time ($b$, Weeks) |
| :---: | :---: | :---: | :---: |
| **P** | 5 | 8 | 17 |
| **Q** | 6 | 10 | 14 |
| **R** | 7 | 12 | 23 |
| **S** | 4 | 7 | 16 |

#### Candidate Tasks:
1. Calculate the expected duration ($t_e$) and variance ($\sigma^2$) for each of the four activities.
2. Determine the expected total program completion duration ($\mu_{\text{project}}$) and total standard deviation ($\sigma_{\text{project}}$).
3. The board of directors has committed to deliver the system to the client within $45\text{ weeks}$. Calculate the probability that the program will be completed on or before this 45-week deadline. (Standard Normal distribution values: $\Phi(0.50) = 0.6915, \Phi(1.00) = 0.8413, \Phi(1.25) = 0.8944, \Phi(1.50) = 0.9332$).

---

## Section C: Earned Value Forecasting & Schedule Crashing (15 Marks)

### Problem 7: Project Crashing for Liquidated Damages Mitigation
A high-priority commercial contract has a baseline duration of 30 days. The contract stipulates a penalty of $₹15,000\text{ per day}$ for every day the project extends beyond 25 days. The Critical Path currently consists of three activities:
- Activity 1: Current duration $10\text{ days}$, crashable to $7\text{ days}$, crash cost slope $= ₹6,000/\text{day}$.
- Activity 2: Current duration $12\text{ days}$, crashable to $9\text{ days}$, crash cost slope $= ₹9,000/\text{day}$.
- Activity 3: Current duration $8\text{ days}$, crashable to $6\text{ days}$, crash cost slope $= ₹18,000/\text{day}$.

#### Tasks:
1. If no crashing is performed, what is the total liquidated damages penalty incurred?
2. Formulate the optimal, least-cost crashing sequence to reduce the project duration to 25 days.
3. Compute the net financial savings achieved by crashing versus paying the contract penalties.

---

## Section D: Cross-Functional Governance & RACI Conflict (10 Marks)

### Scenario: The Product-Engineering Release Stalemate
Two weeks before the scheduled launch of an AI-powered automated loan approval engine, the Head of Compliance demands halting the release due to unverified regulatory explainability checks. The Product Lead insists on launching immediately to meet quarterly revenue targets, stating that compliance risks can be patched post-launch. The Engineering Lead refuses to deploy code without written legal sign-off.
1. As the Program Manager, detail your immediate 48-hour intervention framework to break this deadlock.
2. Construct a formal RACI matrix covering: Feature Scope, Regulatory Sign-Off, Security Audit, and Final Deployment Go/No-Go.

---

# Comprehensive Solutions & Scoring Rubric

---

### Solution Q1: Total Float vs. Free Float
- **Correct Option: (a)** $TF = 6\text{ days}$, $FF = 3\text{ days}$
- **Derivation**:
  - $ES = 10, EF = 18, LF = 24$.
  - Duration $D = EF - ES = 18 - 10 = 8\text{ days}$.
  - Late Start $LS = LF - D = 24 - 8 = 16\text{ days}$.
  - Total Float ($TF$):
    $$TF = LS - ES = 16 - 10 = \mathbf{6 \text{ days}} \quad (\text{or } LF - EF = 24 - 18 = 6)$$
  - Free Float ($FF$):
    $$FF = \min \{ES_{\text{succ}}\} - EF = 21 - 18 = \mathbf{3 \text{ days}}$$
- **Distractor Analysis**:
  - *(b) is wrong*: Confused Free Float with Total Float.

---

### Solution Q2: PERT Expected Task Duration & Variance
- **Correct Option: (a)** $t_e = 12.0\text{ days}$, $\sigma^2 = 7.11$
- **Calculation**:
  $$t_e = \frac{a + 4m + b}{6} = \frac{6 + 4(11) + 22}{6} = \frac{6 + 44 + 22}{6} = \frac{72}{6} = \mathbf{12.0 \text{ days}}$$
  $$\sigma = \frac{b - a}{6} = \frac{22 - 6}{6} = \frac{16}{6} = 2.667 \text{ days}$$
  $$\sigma^2 = (2.667)^2 = \mathbf{7.11}$$
- **Distractor Analysis**:
  - *(c) is wrong*: $2.67$ is the standard deviation $\sigma$, not the variance $\sigma^2$.

---

### Solution Q3: Earned Value Performance Interpretation
- **Correct Option: (d)** Under budget and behind schedule.
- **Explanation**:
  - $CPI = 1.15 > 1.0 \implies$ Cost favorable (Under budget).
  - $SPI = 0.85 < 1.0 \implies$ Schedule unfavorable (Behind schedule).

---

### Solution Q4: Crashing Cost Slope
- **Correct Option: (b)** $₹6,000/\text{day}$
- **Calculation**:
  $$\text{Cost Slope} = \frac{\text{Crash Cost} - \text{Normal Cost}}{\text{Normal Duration} - \text{Crash Duration}} = \frac{₹64,000 - ₹40,000}{10 - 6} = \frac{₹24,000}{4 \text{ days}} = \mathbf{₹6,000/\text{day}}$$

---

### Solution Q5: RACI Responsibility Rule
- **Correct Option: (b)** Exactly one person must be assigned 'Accountable' (A) to prevent diffusion of responsibility.

---

### Solution Problem 6: PERT Program Duration & Probability
1. **Activity-by-Activity Calculations**:
   - **Activity P**:
     $$t_{e,P} = \frac{5 + 4(8) + 17}{6} = \frac{54}{6} = 9.0\text{ wks}; \quad \sigma^2_P = \left(\frac{17 - 5}{6}\right)^2 = 2^2 = 4.0$$
   - **Activity Q**:
     $$t_{e,Q} = \frac{6 + 4(10) + 14}{6} = \frac{60}{6} = 10.0\text{ wks}; \quad \sigma^2_Q = \left(\frac{14 - 6}{6}\right)^2 = \left(\frac{8}{6}\right)^2 = 1.778$$
   - **Activity R**:
     $$t_{e,R} = \frac{7 + 4(12) + 23}{6} = \frac{78}{6} = 13.0\text{ wks}; \quad \sigma^2_R = \left(\frac{23 - 7}{6}\right)^2 = \left(\frac{16}{6}\right)^2 = 7.111$$
   - **Activity S**:
     $$t_{e,S} = \frac{4 + 4(7) + 16}{6} = \frac{48}{6} = 8.0\text{ wks}; \quad \sigma^2_S = \left(\frac{16 - 4}{6}\right)^2 = 2^2 = 4.0$$
2. **Total Critical Path Metrics**:
   $$\mu_{\text{project}} = 9.0 + 10.0 + 13.0 + 8.0 = \mathbf{40.0 \text{ weeks}}$$
   $$\sigma^2_{\text{project}} = 4.0 + 1.778 + 7.111 + 4.0 = 16.889 \implies \sigma_{\text{project}} = \sqrt{16.889} \approx \mathbf{4.11 \text{ weeks}}$$
3. **Probability of Finishing within 45 Weeks**:
   $$Z = \frac{T_s - \mu_{\text{project}}}{\sigma_{\text{project}}} = \frac{45.0 - 40.0}{4.11} = \frac{5.0}{4.11} \approx \mathbf{+1.216} \approx \mathbf{+1.22}$$
   - Interpolating: $\Phi(1.22) \approx \mathbf{88.88\%}$ (approximately **$89\%$ probability**).

---

### Solution Problem 7: Project Crashing
1. **Uncrashed Baseline Penalty**:
   - Total duration $= 10 + 12 + 8 = 30\text{ days}$.
   - Target deadline $= 25\text{ days}$. Delay $= 30 - 25 = 5\text{ days}$.
   - Total penalty $= 5\text{ days} \times ₹15,000/\text{day} = \mathbf{₹75,000}$.
2. **Least-Cost Crashing Sequence**:
   - Compare crash cost slopes against penalty ($₹15,000/\text{day}$):
     - Activity 1: $₹6,000/\text{day}$ (Cheapest). Crash by maximum available: $3\text{ days}$ ($10 \to 7$). Cost $= 3 \times 6,000 = ₹18,000$. New duration $= 27\text{ days}$.
     - Activity 2: $₹9,000/\text{day}$ ($< ₹15,000$). Crash by required $2\text{ days}$ ($12 \to 10$). Cost $= 2 \times 9,000 = ₹18,000$. New duration $= 25\text{ days}$.
     - Activity 3: $₹18,000/\text{day}$ ($> ₹15,000$). Do NOT crash (cheaper to pay penalty than crash Activity 3).
   - **Total Crashing Investment**: $18,000 + 18,000 = \mathbf{₹36,000}$.
3. **Net Financial Savings**:
   $$\text{Net Savings} = \text{Avoided Penalties } (₹75,000) - \text{Crash Cost } (₹36,000) = \mathbf{+₹39,000}$$
