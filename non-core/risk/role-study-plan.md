# Risk — Role Study Plan

## Role Overview

The Risk role targets **risk management positions** at banks (Barclays, HSBC, JP Morgan), **consulting firms** (Deloitte Risk Advisory, PwC, EY), **insurance companies** (LIC, SBI Life, ICICI Prudential), and **corporate risk departments** (Tata, Reliance). The role covers probability analysis, quantitative risk modeling, risk frameworks, and mitigation strategies. Civil engineers' background in structural reliability, probabilistic analysis, and safety factors provides a unique advantage.

**Who targets this role:** B.Tech/M.Tech graduates with quantitative aptitude, structural/reliability engineering background, GATE qualifiers, students interested in financial risk, enterprise risk, or project risk.

---

## 3–4 Highest-Value Preparation Blocks

### Topic 1: Probability & Quantitative Risk Analysis

#### Why This Matters
Risk is fundamentally about quantifying uncertainty. Probability theory, expected value, standard deviation, and distributions are the mathematical language of risk management. Every risk interview tests quantitative reasoning.

#### What to Learn
- [ ] Probability fundamentals: Conditional probability, Bayes' theorem, independence
- [ ] Expected value and standard deviation of random variables
- [ ] Common distributions: Normal, Binomial, Poisson, Uniform, Log-normal
- [ ] Central Limit Theorem and its application to risk aggregation
- [ ] Value at Risk (VaR): Definition, parametric method, historical simulation
- [ ] Conditional VaR (CVaR / Expected Shortfall)
- [ ] Monte Carlo simulation concept: generating probability distributions of outcomes
- [ ] Correlation and covariance in multi-asset risk

#### Study Material
| File | Focus Area | Depth |
|:-----|:-----------|:------|
| [`risk-overview.md`](risk-overview.md) | Probability, risk assessment | Full |
| [`aptitude-basics.md`](../aptitude/quantitative/aptitude-basics.md) | Probability fundamentals | Reference |

#### Worked Example
**Problem:** A portfolio has two assets:
- Asset A: Expected return = 12%, Standard deviation = 18%
- Asset B: Expected return = 8%, Standard deviation = 12%
- Weight A = 60%, Weight B = 40%
- Correlation ρ = 0.3

Calculate: (a) Portfolio expected return, (b) Portfolio standard deviation, (c) VaR at 95% confidence for ₹100 Cr portfolio over 1 day.

**Solution:**
1. **Portfolio expected return:**
   - E(Rp) = 0.6 × 12% + 0.4 × 8% = 7.2% + 3.2% = **10.4%**

2. **Portfolio standard deviation:**
   - σp² = w₁²σ₁² + w₂²σ₂² + 2w₁w₂ρσ₁σ₂
   - σp² = (0.6)²(0.18)² + (0.4)²(0.12)² + 2(0.6)(0.4)(0.3)(0.18)(0.12)
   - σp² = 0.36 × 0.0324 + 0.16 × 0.0144 + 0.48 × 0.3 × 0.0216
   - σp² = 0.01166 + 0.00230 + 0.00311 = 0.01707
   - σp = √0.01707 = **13.07%**

3. **VaR at 95% (1-day):**
   - Daily σp = 13.07% / √252 = 0.825%
   - VaR₉₅ = 1.645 × 0.825% × ₹100 Cr = **₹1.36 Cr**
   - Interpretation: 95% confidence that 1-day loss will not exceed ₹1.36 Cr

4. **CVaR (Expected Shortfall):**
   - CVaR ≈ 2.063 × 0.825% × ₹100 = **₹1.70 Cr** (average loss beyond VaR)

**Key insight:** "Diversification reduces risk — with ρ=0.3, portfolio σ (13.07%) is less than weighted average (15.6%). This is the benefit of diversification."

#### Practice
**Basic (3–5):**
1. Define expected value and standard deviation. Give a financial example.
2. A project has 60% chance of ₹50 Cr profit and 40% chance of ₹20 Cr loss. Find expected value.
3. What is Value at Risk (VaR)? Interpret "1-day 99% VaR = ₹5 Cr."
4. Explain the difference between VaR and CVaR.
5. What distribution is most commonly used in financial risk modeling? Why?

**Intermediate (3–5):**
6. Compute portfolio VaR for 3 assets given weights, σ, and correlation matrix.
7. Perform a simple Monte Carlo simulation (describe the process, not code).
8. What is the Central Limit Theorem? How does it apply to risk aggregation?
9. A loss distribution has mean = -₹2 Cr, σ = ₹5 Cr. Estimate 99% VaR assuming normal distribution.
10. Explain conditional probability using a medical testing example.

**Interview-Level (5+):**
11. What are the limitations of VaR? Why did it fail in 2008?
12. Compare parametric VaR, historical simulation, and Monte Carlo simulation.
13. How do you model correlation between assets during a crisis (correlation breakdown)?
14. What is stress testing vs scenario analysis vs VaR?
15. Explain how Monte Carlo simulation is used in project risk analysis.

#### Interview Questions (What Interviewer Tests)
| Question | What They're Testing |
|:---------|:---------------------|
| Compute VaR for this portfolio | Quantitative skill |
| What are the limitations of VaR? | Critical thinking |
| Explain Monte Carlo simulation | Conceptual depth |
| How would you model operational risk? | Applied knowledge |
| Difference between market risk and credit risk? | Domain knowledge |

#### Common Mistakes
- **Assuming** normal distribution without checking — financial returns are fat-tailed
- **Ignoring** correlation — diversification benefit depends critically on ρ
- **Confusing** VaR with maximum loss — VaR is a percentile, not a worst case
- **Using** daily VaR for monthly decisions without scaling
- **Not understanding** that VaR doesn't tell you the size of loss beyond the threshold

#### Completion Criterion
✅ Can compute portfolio expected return and standard deviation
✅ Can calculate and interpret VaR (parametric method)
✅ Can explain Monte Carlo simulation conceptually
✅ Can distinguish between different risk types and measurement methods

---

### Topic 2: Risk Frameworks & Identification

#### Why This Matters
Interviewers test not just quantitative skills but also your ability to systematically identify, categorize, and manage risks. Risk frameworks provide the structured approach that organizations use.

#### What to Learn
- [ ] Enterprise Risk Management (ERM): COSO framework, ISO 31000
- [ ] Risk identification techniques: Brainstorming, checklists, SWOT, PESTLE
- [ ] Risk assessment: Probability × Impact matrix, risk scoring
- [ ] Risk categories: Strategic, operational, financial, compliance, reputational
- [ ] Risk response: Avoid, mitigate, transfer, accept
- [ ] Risk appetite vs risk tolerance
- [ ] Key Risk Indicators (KRIs) and Risk Reporting
- [ ] Three Lines of Defense model

#### Study Material
| File | Focus Area | Depth |
|:-----|:-----------|:------|
| [`risk-overview.md`](risk-overview.md) | Risk frameworks, identification | Full |

#### Worked Example
**Problem:** A construction company is building a bridge. Identify the top 5 risks, assess them using a 5×5 probability-impact matrix, and propose mitigation strategies.

**Solution:**

| # | Risk | Probability (1-5) | Impact (1-5) | Score | Category | Mitigation |
|---|:-----|:-----------------:|:------------:|:-----:|:---------|:-----------|
| 1 | Cost overrun due to material price increase | 4 | 4 | **16** | Financial | Lock-in material contracts, price escalation clause |
| 2 | Delay due to monsoon/weather | 5 | 3 | **15** | Operational | Build weather buffer into schedule, monsoon-proof work areas |
| 3 | Design error discovered during construction | 2 | 5 | **10** | Technical | Third-party design review, BIM clash detection |
| 4 | Labor shortage / strike | 3 | 4 | **12** | Operational | Cross-training, multiple labor suppliers, retention bonuses |
| 5 | Environmental clearance delay | 3 | 5 | **15** | Compliance | Early engagement with MOEF, parallel processing |

**Risk Heat Map:**

```
Impact →    1      2      3      4      5
Prob ↓
  5       (5)   (10)   (15)   (20)   (25)
  4       (4)    (8)   (12)  [16]    (20)
  3       (3)    (6)    (9)  [12]   [15]
  2       (2)    (4)    (6)    (8)   [10]
  1       (1)    (2)    (3)    (4)    (5)

[xx] = Active risks in this project
```

**Key insight:** "Risk 1 (cost overrun) has the highest score of 16 and should be the top priority. However, Risk 5 (clearance delay) could halt the entire project — a qualitative judgment that the matrix alone doesn't capture."

#### Practice
**Basic (3–5):**
1. What is enterprise risk management? How does it differ from project risk management?
2. Name 4 risk response strategies with an example for each.
3. What is the difference between risk appetite and risk tolerance?
4. Explain the Three Lines of Defense model.
5. What are Key Risk Indicators (KRIs)? Give 3 examples.

**Intermediate (3–5):**
6. Create a risk register for launching a new product (identify 8+ risks).
7. What is the COSO ERM framework? Describe its components.
8. How would you conduct a PESTLE analysis for a new infrastructure project?
9. Explain the difference between inherent risk and residual risk.
10. What is risk appetite statement? Why do companies need one?

**Interview-Level (5+):**
11. How do you prioritize risks when multiple have the same probability-impact score?
12. What is emerging risk? How do you identify risks that haven't occurred yet?
13. How do you build a risk culture in an organization?
14. Compare ISO 31000 with COSO ERM. Which would you recommend?
15. How does climate change affect infrastructure risk assessment?

#### Common Mistakes
- **Treating** all risks equally — use the probability-impact matrix
- **Ignoring** interconnected risks — one risk can trigger others
- **Confusing** risk with uncertainty — risk is quantifiable, uncertainty is not
- **Focusing** only on negative risks — positive risks (opportunities) exist too
- **Not updating** risk registers — risks evolve throughout a project

#### Completion Criterion
✅ Can apply ISO 31000 or COSO framework systematically
✅ Can construct a risk register with probability-impact scoring
✅ Can distinguish between risk types and appropriate responses
✅ Can explain the Three Lines of Defense model

---

### Topic 3: Financial Risk Management (Market, Credit, Operational)

#### Why This Matters
For banking and financial services roles, understanding the three pillars of financial risk — market risk, credit risk, and operational risk — is essential. These are tested heavily in interviews.

#### What to Learn
- [ ] Market risk: Interest rate risk, equity risk, currency risk, commodity risk
- [ ] Credit risk: Default probability, loss given default (LGD), exposure at default (EAD)
- [ ] Expected Loss = PD × LGD × EAD
- [ ] Credit scoring and rating models
- [ ] Operational risk: Basel framework, loss distribution approach
- [ ] Basel III capital requirements: CET1, Tier 1, Total Capital ratios
- [ ] Liquidity risk: Liquidity Coverage Ratio (LCR), Net Stable Funding Ratio (NSFR)
- [ ] Hedging: Forward contracts, options, swaps

#### Study Material
| File | Focus Area | Depth |
|:-----|:-----------|:------|
| [`risk-overview.md`](risk-overview.md) | Financial risk, Basel | Full |
| [`finance-overview.md`](../finance/finance-overview.md) | Financial context | Reference |

#### Worked Example
**Problem:** A bank has the following portfolio:
- Corporate loans: ₹10,000 Cr, PD = 2%, LGD = 45%
- Retail loans: ₹5,000 Cr, PD = 5%, LGD = 30%
- Market risk: Daily VaR₉₉ = ₹50 Cr
- Operational risk: Annual loss = ₹200 Cr (average)

Calculate: (a) Expected credit loss for each segment, (b) Total expected credit loss, (c) What Basel III CET1 capital is needed?

**Solution:**
1. **Expected Credit Loss (ECL):**
   - Corporate: ECL = PD × LGD × EAD = 0.02 × 0.45 × 10,000 = **₹90 Cr**
   - Retail: ECL = 0.05 × 0.30 × 5,000 = **₹75 Cr**
   - **Total ECL = ₹165 Cr**

2. **Unexpected Loss (using 99.9% confidence):**
   - Assuming normal loss distribution:
   - UL_corporate ≈ 2.33 × √(PD × (1-PD)) × LGD × EAD
   - UL_corporate = 2.33 × √(0.02 × 0.98) × 0.45 × 10,000 = 2.33 × 0.14 × 4,500 = **₹1,468 Cr**
   - (Simplified; actual Basel uses more complex formulas)

3. **Minimum CET1 Capital (Basel III):**
   - Credit risk capital (simplified): ~₹1,500 Cr
   - Market risk capital: VaR₉₉ × 10 (multiplier) = ₹500 Cr
   - Operational risk capital: ₹200 Cr (or calculated via SMA)
   - **Total risk-weighted assets ≈ ₹12,000 Cr**
   - **Minimum CET1 = 4.5% × 12,000 = ₹540 Cr**

**Key insight:** "Credit loss is the biggest risk driver. The LGD of 45% for corporate loans means the bank expects to recover only 55% of defaulted loans. Collateral and recovery strategies are critical."

#### Practice
**Basic (3–5):**
1. What is Expected Loss? Write the formula.
2. Define PD, LGD, and EAD with examples.
3. What is the difference between market risk and credit risk?
4. Explain the three pillars of Basel II/III.
5. What is the difference between CET1 and Tier 1 capital?

**Intermediate (3–5):**
6. Calculate ECL for a loan portfolio given PD, LGD, and EAD for each segment.
7. What is a credit rating migration matrix? How does it affect portfolio risk?
8. Explain interest rate risk: What happens to bond prices when rates rise by 1%?
9. What is a stress test? How does it differ from VaR?
10. How do banks calculate operational risk capital under Basel III SMA?

**Interview-Level (5+):**
11. How did the 2008 financial crisis change risk management?
12. What are the challenges of implementing Basel III in Indian banks?
13. How would you design a risk dashboard for a bank's CEO?
14. Explain counterparty credit risk and CVA (Credit Valuation Adjustment).
15. What is model risk? How do you manage it?

#### Common Mistakes
- **Ignoring** correlation between credit and market risks
- **Confusing** expected loss with unexpected loss — capital covers unexpected loss
- **Not understanding** that VaR doesn't tell you the magnitude of extreme losses
- **Treating** all loan segments as having the same risk profile
- **Forgetting** that Basel requirements are minimums — banks often hold more

#### Completion Criterion
✅ Can compute Expected Credit Loss (ECL) for a portfolio
✅ Can explain the three pillars of Basel III
✅ Can distinguish market, credit, and operational risk
✅ Can describe how capital requirements are calculated

---

### Topic 4: Risk Case Studies & Interview Scenarios

#### Why This Matters
Risk interviews often present real-world scenarios: "A bank's portfolio has lost 20% — what happened?" or "How would you set up a risk management framework for a startup?" Structured thinking is tested.

#### What to Learn
- [ ] Risk incident analysis: Root cause, contributing factors, lessons learned
- [ ] Scenario analysis: Best case, base case, worst case
- [ ] Stress testing: Historical scenarios (2008 crisis, COVID), hypothetical scenarios
- [ ] Risk reporting: Dashboard design, escalation protocols
- [ ] Project risk management: Earned Value-based risk, schedule risk analysis
- [ ] Civil engineering risk: Structural reliability, safety factors, probabilistic design

#### Study Material
| File | Focus Area | Depth |
|:-----|:-----------|:------|
| [`risk-overview.md`](risk-overview.md) | Case scenarios, frameworks | Full |
| [`project-discussion.md`](../../prep/interview/technical/project-discussion.md) | Project risk discussion | Reference |

#### Worked Example
**Problem:** "A major infrastructure project (₹5,000 Cr) is 60% complete but has consumed 75% of its budget. What risk analysis would you perform?"

**Solution:**
1. **Diagnose — Earned Value Analysis:**
   - PV (Planned Value) = 60% of ₹5,000 = ₹3,000 Cr
   - AC (Actual Cost) = 75% of ₹5,000 = ₹3,750 Cr
   - EV (Earned Value) = 60% of ₹5,000 = ₹3,000 Cr (if work is on schedule)
   - CPI = EV/AC = 3,000/3,750 = **0.80** (severe cost overrun)
   - SPI = EV/PV = 3,000/3,000 = **1.00** (on schedule)
   - EAC = BAC/CPI = 5,000/0.80 = **₹6,250 Cr** (projected total cost)
   - Variance at Completion = BAC - EAC = -₹1,250 Cr (25% overrun)

2. **Root Cause Analysis:**
   - Material cost escalation? (Steel, cement price increase)
   - Design changes / scope creep?
   - Contractor inefficiency?
   - Regulatory delays with associated costs?
   - Inaccurate original estimates?

3. **Risk Register Update:**
   - New risk: Cost overrun — Probability: 5/5, Impact: 5/5, Score: **25 (Critical)**
   - Mitigation: Renegotiate contracts, value engineering, additional funding approval

4. **Forward-Looking Analysis:**
   - What remaining work can be optimized?
   - Can scope be reduced without compromising functionality?
   - Are there claims/subcontractor disputes pending?

**Key insight:** "A CPI of 0.80 means for every ₹1 spent, only ₹0.80 of value is earned. At this rate, the project will overrun by ₹1,250 Cr. Immediate corrective action is needed."

#### Practice
**Basic (3–5):**
1. What is root cause analysis? Name 2 techniques.
2. How do you create a risk dashboard? What metrics would you include?
3. Explain the concept of "risk transfer" in construction (insurance, contracts).
4. What is the difference between risk monitoring and risk review?
5. How does EVM help in project risk management?

**Intermediate (3–5):**
6. "A bank's VaR model predicted max daily loss of ₹10 Cr at 99% confidence, but actual loss was ₹50 Cr. What happened?" — Analyze.
7. Design a risk management framework for an e-commerce startup.
8. "A dam project faces seismic risk. How would you assess and mitigate it?"
9. Perform a scenario analysis for a company considering entering a new market.
10. "Our project's SPI dropped from 1.1 to 0.9 in one month. What would you investigate?"

**Interview-Level (5+):**
11. "How would you explain risk to a non-technical board member?"
12. "What risk factors should a bank consider before lending to a construction company?" — Use your civil background.
13. "Describe a time you identified and mitigated a risk in a project." — Use STAR framework.
14. "How would climate change affect infrastructure project risk over the next 20 years?"
15. "A cyber attack has compromised customer data. Walk me through the risk response."

#### Common Mistakes
- **Not quantifying** risks — "something might go wrong" is not risk management
- **Ignoring** project interdependencies — schedule risk affects cost risk
- **Focusing** only on financial risks — operational and reputational risks matter too
- **Not having** a communication plan for risk escalation
- **Treating** risk management as a one-time exercise rather than ongoing

#### Completion Criterion
✅ Can analyze a project using EVM metrics (CPI, SPI, EAC)
✅ Can construct a risk dashboard with appropriate KRIs
✅ Can apply structured thinking to novel risk scenarios
✅ Can communicate risk findings to non-technical stakeholders

---

## Mock Test (45 Minutes)

| # | Question | Topic | Marks |
|---|:---------|:------|------:|
| 1 | Portfolio: Asset A (₹200 Cr, σ=20%), Asset B (₹100 Cr, σ=15%), ρ=0.4. Compute: (a) Portfolio return if A returns 10%, B returns 6%, (b) Portfolio σ, (c) 1-day 99% VaR. | Quantitative Risk | 25 |
| 2 | A project has risks: material price (P=0.8, I=₹50 Cr), weather delay (P=0.6, I=₹30 Cr), design error (P=0.3, I=₹100 Cr), labor shortage (P=0.5, I=₹20 Cr). Create a risk register, compute risk scores, and propose mitigations for top 3 risks. | Risk Framework | 25 |
| 3 | Bank portfolio: Corporate loans ₹8,000 Cr (PD=1.5%, LGD=40%), Retail loans ₹4,000 Cr (PD=4%, LGD=25%). Calculate ECL for each segment and total. If regulatory CET1 requirement is 6%, how much capital is needed? | Credit Risk | 25 |
| 4 | "A major project is behind schedule and over budget. CPI=0.75, SPI=0.85. BAC=₹2,000 Cr. Calculate EAC, variance at completion, and estimate completion time if original schedule was 24 months. What corrective actions would you recommend?" | Project Risk | 15 |
| 5 | Explain the difference between VaR and CVaR. Why might a regulator prefer CVaR? What are the main criticisms of VaR as a risk measure? | Risk Theory | 10 |
| | | **Total** | **100** |

---

## Interview Strategy

### Technical Interview (15–20 minutes)
1. **Start with fundamentals** — probability, distributions, expected value
2. **Show structured thinking** — use frameworks (risk register, 3 lines of defense)
3. **Link to civil engineering** — structural reliability, probabilistic design, safety factors
4. **Quantify everything** — "The risk score is 16 (High)" not just "it's a big risk"

### Behavioral / Case Study
- **Have 2-3 STAR stories** about identifying and managing risk
- **Know recent risk events** — banking crises, climate events, project failures
- **Practice explaining** risk concepts to a non-technical audience

### Unique Positioning (Civil → Risk)
- "I understand structural reliability analysis — it's the original probabilistic risk framework"
- "Civil engineers deal with safety factors — which is risk quantification in practice"
- "Infrastructure projects have complex risk interdependencies — I've studied these"

---

## Cross-Links

**Next:**
→ [Risk Overview](risk-overview.md) — Complete preparation system

**Study:**
→ [Finance Study Plan](../finance/role-study-plan.md) — For financial risk context
→ [Quantitative Aptitude](../aptitude/quantitative/aptitude-basics.md) — Probability fundamentals

**Interview:**
→ [Technical Interview Bank](../../prep/interview/technical/technical-interview-bank.md)
→ [Behavioral Guide](../../prep/behavioral/behavioral-interview-guide.md)
→ [HR Questions](../../prep/behavioral/hr_questions/hr-questions-bank.md)

**Related:**
→ [Strategy Overview](../strategy/strategy-overview.md) — For strategic risk context
→ [Operations Overview](../operations/operations-overview.md) — For operational risk

---

*This study plan follows the [Role Study Plan Template](../../prep/templates/role-study-plan-template.md).*
*Last updated: 2026-09-04*
