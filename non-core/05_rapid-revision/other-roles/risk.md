# Risk — Rapid Revision Sheet

> Last-minute cheat sheet. Covers all core formulas, frameworks, and quick-fire Q&A for risk interviews.

---

## Framework 1: Probability & Quantitative Risk

### Core Probability Formulas

| Concept | Formula | Use |
|:--------|:--------|:----|
| Expected Value | E(X) = Σ xᵢ × P(xᵢ) | Average outcome |
| Variance | Var(X) = Σ (xᵢ - μ)² × P(xᵢ) | Spread of outcomes |
| Std Deviation | σ = √Var(X) | Risk measure |
| Covariance | Cov(X,Y) = E[(X-μₓ)(Y-μᵧ)] | Joint variability |
| Correlation | ρ = Cov(X,Y) / (σₓ × σᵧ) | Normalized covariance (-1 to +1) |
| Conditional Probability | P(A|B) = P(A∩B) / P(B) | Probability given event |
| Bayes' Theorem | P(A|B) = P(B|A) × P(A) / P(B) | Update belief with evidence |

### Portfolio Risk Formulas

**2-asset portfolio:**
```
E(Rp) = w₁E(R₁) + w₂E(R₂)
σp = √[w₁²σ₁² + w₂²σ₂² + 2w₁w₂ρσ₁σ₂]
```

**Diversification benefit:**
- ρ = +1: No diversification (σp = weighted avg)
- ρ = 0: Significant reduction
- ρ = -1: Maximum reduction (can eliminate risk entirely)

### Value at Risk (VaR)

**Parametric VaR (assumes normal distribution):**
```
VaRₐ = Zₐ × σ × Portfolio Value
```

| Confidence | Z-score |
|:----------:|:-------:|
| 90% | 1.282 |
| 95% | 1.645 |
| 99% | 2.326 |

**Daily to Annual VaR:**
```
Annual VaR = Daily VaR × √252
Monthly VaR = Daily VaR × √21
```

**Conditional VaR (CVaR / Expected Shortfall):**
```
CVaR = Average of all losses exceeding VaR
CVaR ≈ 2.063 × σ × Portfolio Value (at 99% confidence, normal)
```

### Common Distributions in Risk

| Distribution | Use Case | Key Property |
|:-------------|:---------|:-------------|
| Normal | Market returns (approx.) | Symmetric, bell-shaped |
| Log-normal | Asset prices | Always positive, right-skewed |
| Binomial | Default/no-default | Discrete, 2 outcomes |
| Poisson | Operational loss frequency | Count of rare events |
| Uniform | Scenario analysis | All outcomes equally likely |

---

## Framework 2: Risk Frameworks & Identification

### ISO 31000 Risk Management Process

```
1. Establish Context → 2. Risk Assessment
   (internal/external)    ├─ Identification
                          ├─ Analysis (P × I)
                          └─ Evaluation
                     → 3. Risk Treatment
                        (Avoid/Mitigate/Transfer/Accept)
                     → 4. Monitoring & Review
                     → 5. Communication & Consultation
```

### COSO ERM Framework Components

```
1. Internal Environment  → Risk culture, appetite, tone at top
2. Objective Setting     → Strategic, operations, reporting, compliance
3. Event Identification  → Risks and opportunities
4. Risk Assessment       → Likelihood and impact
5. Risk Response         → Avoid, reduce, share, accept
6. Control Activities    → Policies and procedures
7. Information/Comms     → Risk reporting
8. Monitoring            → Ongoing evaluation
```

### Three Lines of Defense

| Line | Role | Responsibility |
|:-----|:-----|:---------------|
| 1st | Business units | Own and manage risk day-to-day |
| 2nd | Risk management / Compliance | Set frameworks, monitor, challenge |
| 3rd | Internal audit | Independent assurance |

### Risk Response Strategies

| Strategy | Description | Example |
|:---------|:-----------|:--------|
| **Avoid** | Eliminate the risk | Cancel high-risk project |
| **Mitigate** | Reduce probability or impact | Safety training, redundancy |
| **Transfer** | Shift to third party | Insurance, outsourcing |
| **Accept** | Bear the consequences | Contingency budget for known risk |

### Risk Assessment Matrix (5×5)

| | Impact 1 (Negligible) | Impact 2 (Minor) | Impact 3 (Moderate) | Impact 4 (Major) | Impact 5 (Catastrophic) |
|:---|:---:|:---:|:---:|:---:|:---:|
| **P=5 (Almost Certain)** | 5 | 10 | 15 | 20 | **25** |
| **P=4 (Likely)** | 4 | 8 | 12 | **16** | 20 |
| **P=3 (Possible)** | 3 | 6 | 9 | 12 | **15** |
| **P=2 (Unlikely)** | 2 | 4 | 6 | 8 | 10 |
| **P=1 (Rare)** | 1 | 2 | 3 | 4 | 5 |

**Score interpretation:** 1-4 Low (green), 5-9 Medium (yellow), 10-15 High (orange), 16-25 Critical (red)

---

## Framework 3: Financial Risk (Market, Credit, Operational)

### Three Pillars of Financial Risk

| Risk Type | What It Measures | Key Metrics |
|:----------|:-----------------|:------------|
| **Market Risk** | Loss from market price movements | VaR, Duration, DV01 |
| **Credit Risk** | Loss from counterparty default | PD, LGD, EAD, ECL |
| **Operational Risk** | Loss from process/system failures | Loss data, scenario analysis |

### Credit Risk Formulas

```
Expected Loss (EL) = PD × LGD × EAD
Unexpected Loss (UL) = σ_PD × LGD × EAD
```

Where:
- PD = Probability of Default
- LGD = Loss Given Default (1 - Recovery Rate)
- EAD = Exposure at Default

### Basel III Capital Requirements

| Component | Minimum (Basel III) | Description |
|:----------|:-------------------:|:------------|
| CET1 Ratio | 4.5% | Common Equity Tier 1 / RWA |
| Tier 1 Ratio | 6.0% | CET1 + Additional Tier 1 / RWA |
| Total Capital Ratio | 8.0% | Tier 1 + Tier 2 / RWA |
| Capital Conservation Buffer | 2.5% | Additional CET1 buffer |
| Countercyclical Buffer | 0-2.5% | Varies by jurisdiction |
| Leverage Ratio | 3% | Tier 1 / Total Exposure |

### Liquidity Ratios

| Ratio | Formula | Minimum |
|:------|:--------|:-------:|
| LCR | HQLA / Net Cash Outflows (30-day) | 100% |
| NSFR | ASF / RSF (1-year) | 100% |

Where:
- HQLA = High Quality Liquid Assets
- ASF = Available Stable Funding
- RSF = Required Stable Funding

---

## Framework 4: Project Risk with EVM

### Earned Value Metrics

| Metric | Formula | Interpretation |
|:-------|:--------|:---------------|
| CV (Cost Variance) | EV - AC | Negative = over budget |
| SV (Schedule Variance) | EV - PV | Negative = behind schedule |
| CPI (Cost Performance Index) | EV / AC | <1 = over budget |
| SPI (Schedule Performance Index) | EV / PV | <1 = behind schedule |
| EAC (Estimate at Completion) | BAC / CPI | Projected total cost |
| ETC (Estimate to Complete) | EAC - AC | Remaining cost |
| VAC (Variance at Completion) | BAC - EAC | Projected overrun/underrun |
| TCPI | (BAC-EV)/(BAC-AC) | Efficiency needed to complete on budget |

### Schedule Risk Analysis

```
Expected Duration = (O + 4M + P) / 6    [PERT]
Variance = ((P - O) / 6)²
Std Dev = (P - O) / 6
```

Where O = Optimistic, M = Most Likely, P = Pessimistic

---

## 10 Quick-Fire Interview Answers

**Q1: What is Value at Risk (VaR)?**
A: VaR is the maximum expected loss over a given time period at a specified confidence level. For example, "1-day 99% VaR of ₹5 Cr" means there's a 1% chance of losing more than ₹5 Cr in a single day.

**Q2: What are the limitations of VaR?**
A: VaR doesn't tell you the magnitude of losses beyond the threshold. It assumes normal distributions (ignores fat tails), may underestimate correlation in crises, and can create false precision. CVaR (Expected Shortfall) addresses some of these limitations.

**Q3: What is Expected Loss in credit risk?**
A: EL = PD × LGD × EAD. It's the average loss a bank expects from a portfolio over a year. It's built into loan pricing (provisioning). Capital reserves cover unexpected losses, not expected losses.

**Q4: Explain the Three Lines of Defense model.**
A: First line: business units own and manage risk. Second line: risk management and compliance set frameworks and monitor. Third line: internal audit provides independent assurance. This ensures clear accountability and separation of duties.

**Q5: What is Monte Carlo simulation?**
A: A computational technique that uses random sampling to model probability distributions of outcomes. It's used when analytical solutions are too complex — e.g., portfolio risk with many correlated assets, or project completion time with uncertain durations.

**Q6: How does your civil engineering background help in risk management?**
A: Structural reliability analysis IS risk management — it uses probability to ensure structures meet safety targets. Safety factors, load factors (LRFD), and probabilistic design are all risk quantification. I also understand project risk from construction experience.

**Q7: What is stress testing?**
A: Evaluating how a portfolio or organization performs under extreme but plausible scenarios (e.g., 2008 crisis, pandemic, interest rate spike). Unlike VaR, stress tests reveal losses in tail scenarios and help assess survivability.

**Q8: What is the difference between risk and uncertainty?**
A: Risk is quantifiable — you can assign probabilities. Uncertainty is unquantifiable — you don't know the probability distribution. Knight (1921) made this distinction. Risk management focuses on measurable risks; uncertainty requires scenario planning.

**Q9: How do you calculate portfolio VaR?**
A: Parametric method: VaR = Z × σp × Portfolio Value. For a multi-asset portfolio, first compute portfolio σp using the correlation matrix, then apply the Z-score for your confidence level (1.645 for 95%, 2.326 for 99%).

**Q10: What is the difference between VaR and CVaR?**
A: VaR is the threshold loss at a given confidence level (e.g., 99th percentile). CVaR (Expected Shortfall) is the average of all losses exceeding VaR. CVaR captures tail risk better and is subadditive (diversification always reduces CVaR).

---

## Last-Minute Checklist

### Before Any Risk Interview
- [ ] VaR formula and Z-scores for 95% and 99%
- [ ] ECL = PD × LGD × EAD
- [ ] Portfolio σ formula (2-asset)
- [ ] EVM formulas: CPI, SPI, EAC
- [ ] Three Lines of Defense
- [ ] Risk response: Avoid, Mitigate, Transfer, Accept

### Must-Know Formulas
- [ ] E(Rp) = w₁E(R₁) + w₂E(R₂)
- [ ] σp = √[w₁²σ₁² + w₂²σ₂² + 2w₁w₂ρσ₁σ₂]
- [ ] VaR = Z × σ × Portfolio Value
- [ ] ECL = PD × LGD × EAD
- [ ] CPI = EV/AC, SPI = EV/PV
- [ ] EAC = BAC/CPI
- [ ] Expected Value = Σ xᵢP(xᵢ)

### Behavioral Prep
- [ ] "Why risk?" (quantitative skills + structural reliability angle)
- [ ] "Tell me about a time you identified a risk" (STAR story ready)
- [ ] "How do you explain risk to non-technical stakeholders?"
- [ ] Current risk events in the news

---

## Cross-Links

**Risk:**
→ [Risk Overview](risk-overview.md) — Complete preparation system
→ [Role Study Plan](role-study-plan.md) — Structured study plan

**Related:**
→ [Finance Rapid Revision](../finance/finance-rapid-revision.md) — Financial formulas
→ [Consulting Case Frameworks](../consulting/case-frameworks.md) — Case interview prep
→ [Operations Overview](../operations/operations-overview.md) — Operational risk

---

*Last updated: 2026-09-04*
