# 01. Risk Analyst: Placement & Job Guide

> Comprehensive IIT Kanpur placement guide for **Risk Management, Credit Risk, Market Risk, and Quantitative Risk Analytics** profiles: Target companies, salary benchmarks, hiring roles, eligibility, day-to-day deliverables, and placement preparation roadmap.

---

## 1. Target Companies & Job Offerings at IITK

> *[HISTORICAL / PREPARATION HEURISTIC]* Compensation packages and eligibility criteria vary by hiring season, company policy, and specific recruitment tracks.

| Dimension | Details |
|:---|:---|
| **Target Hiring Companies** | American Express, Capital One, Goldman Sachs (Risk), Morgan Stanley, Barclays, Citi, Standard Chartered, HSBC, Credit Suisse / UBS, EXL Risk, Fractal Analytics, CRISIL, ICRA, Nomura |
| **Typical Job Designations** | Risk Analyst, Credit Risk Strategy Analyst, Market Risk Quantitative Analyst, Decision Science Analyst, Model Risk Governance Associate, Quantitative Risk Consultant |
| **Typical Campus CTC Range** | `[HISTORICAL]` 12 LPA - 28 LPA (Fixed Base + Annual Performance Bonus + Relocation/Joining Bonus) |
| **Department Eligibility** | `[HISTORICAL]` Open to B.Tech, M.Tech, and Dual Degree across all engineering departments including Civil Engineering / HWRE. CPI cutoff typically ranges between 6.5 and 8.0+. |

---

## 2. Risk Role Variants & Industry Specializations

Risk management in institutional banking, fintech, and asset management encompasses several distinct quantitative tracks:

```text
                                  RISK ROLE VARIANTS
┌─────────────────────────────────────────────────────────────────────────────────────────┐
│                                                                                         │
│  ┌──────────────────────┐  ┌──────────────────────┐  ┌──────────────────────────────┐  │
│  │     Credit Risk      │  │     Market Risk      │  │  Quantitative / Model Risk   │  │
│  │  • PD, LGD, EAD, ECL │  │  • VaR, CVaR / ES    │  │  • Stochastic calculus, SDEs │  │
│  │  • Scorecards, WoE/IV│  │  • Greeks, Volatility│  │  • Monte Carlo simulation    │  │
│  │  • Delinquency roll  │  │  • Stress testing,   │  │  • Backtesting & benchmark-  │  │
│  │    rate modeling     │  │    historical simulation│  ing validation models       │  │
│  └──────────────────────┘  └──────────────────────┘  └──────────────────────────────┘  │
│                                                                                         │
│  ┌──────────────────────┐  ┌──────────────────────┐  ┌──────────────────────────────┐  │
│  │  Fraud / FinCrime    │  │   Operational Risk   │  │ Project & Infrastructure Risk│  │
│  │  • Anomaly detection │  │  • Loss frequency/sev│  │  • Cost/schedule uncertainty │  │
│  │  • Graph ML networks │  │  • Three Lines of    │  │  • Extreme value hydrology & │  │
│  │  • Real-time scoring │  │    Defense, Basel OR │  │    structural reliability    │  │
│  └──────────────────────┘  └──────────────────────┘  └──────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Job-to-Preparation Matrix

| Job Requirement | What Company Tests in Selection | Repository Preparation Module | Evidence to Showcase on Resume |
|:---|:---|:---|:---|
| **Credit Scoring & ML Models** | Live Technical / Scorecard Case | [03_domain-knowledge.md](03_domain-knowledge.md) & [04_tools-and-technical.md](04_tools-and-technical.md) | WoE/IV scorecard, Logistic regression, XGBoost |
| **Statistical & Probability Math**| OA Quantitative Screening | [04_tools-and-technical.md](04_tools-and-technical.md) & [06_question-bank.md](06_question-bank.md) | Bayes' theorem, Normal/Poisson distributions |
| **Portfolio Risk & VaR** | Quantitative Risk Interview Round | [03_domain-knowledge.md](03_domain-knowledge.md) & [07_practice-and-cases.md](07_practice-and-cases.md) | Parametric/Historical VaR, Expected Shortfall |
| **SQL & Portfolio Analytics** | Live Coderpad SQL Round | [../../business-analyst/04_data-and-analytics/sql-practice.md](../business-analyst/04_data-and-analytics/sql-practice.md) | Delinquency cohorts, roll-rate migration queries |
| **Civil/HWRE Background** | Resume Defense & Uncertainty Modeling | [11_projects.md](11_projects.md) | BridgeRisk ML failure modeling / Flood extremes |

---

## 4. What a Risk Analyst Actually Does (Day-to-Day Deliverables)

1. **Credit Underwriting & Policy Tuning**: Setting cutoff credit scores ($FICO / CIBIL$) to balance loan approval volume against 90-day non-performing asset (NPA) loss rates.
2. **Value at Risk (VaR) & Sensitivity Reporting**: Computing daily parametric and historical 99% 1-day VaR across multi-asset trading books to ensure compliance with regulatory capital mandates.
3. **Loss Provisioning & IFRS 9 / CECL Modeling**: Calculating Expected Credit Loss ($ECL = PD 	imes LGD 	imes EAD$) across multi-stage loan portfolios.
4. **Stress Testing & Macroeconomic Scenarios**: Simulating portfolio survival under severe macroeconomic shocks (e.g. GDP contraction, interest rate spikes, commodity inflation).
