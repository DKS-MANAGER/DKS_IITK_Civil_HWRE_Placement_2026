# 05. Risk Analyst: Comprehensive Interview Playbook

> Tactical guide for clearing Online Assessments, Quantitative Risk rounds, Modeling cases, and HR/Fit evaluations at Amex, Capital One, Goldman Sachs, Morgan Stanley, and CRISIL.

---

## 1. Selection Process Stages

```text
┌─────────────────────────────────────────────────────────────────────────────────────────┐
│                              RISK SELECTION PIPELINE                                    │
├────────────────────────────┬─────────────────────────────┬──────────────────────────────┤
│    STAGE 1: ONLINE TEST    │  STAGE 2: QUANT & MODELING  │  STAGE 3: RISK CASE & FIT    │
├────────────────────────────┼─────────────────────────────┼──────────────────────────────┤
│ • Probability & Stats (30m)│ • Probability Theory (30m)  │ • Portfolio Loss Case (30m)  │
│ • Quant Aptitude (30m)     │ • Credit Scoring / WoE (25m)│ • Risk vs Growth Trade-offs  │
│ • SQL Coderpad (30m)       │ • VaR & Distributions (25m) │ • "Why Risk from Civil?" Fit │
└────────────────────────────┴─────────────────────────────┴──────────────────────────────┘
```

---

## 2. Stage 2: Quantitative Technical Round (What is Evaluated)

### 1. Probability & Mathematical Foundations
- Rapid mental computation of conditional probabilities using Bayes' rule.
- Properties of Poisson processes, Binomial approximations, and Normal distribution tails ($Z=1.65, 1.96, 2.33$).

### 2. Modeling & Credit Analytics
- Explaining why Logistic Regression is superior to Linear Regression for default prediction (probabilities bounded $[0,1]$, log-odds linearity).
- Explaining how to handle missing values and non-monotonic features using fine and coarse binning with WoE.

---

## 3. Stage 3: Risk Case Interview Framework

When presented with an ambiguous risk case (e.g., *"Our personal loan portfolio's 90-day delinquency spiked from 2.1% to 4.8%. Diagnose and recommend policy changes"*), use this 4-step framework:

```text
                                RISK CASE DIAGNOSTIC FLOW
┌─────────────────────────┐     ┌─────────────────────────┐     ┌─────────────────────────┐
│  1. VINTAGE & COHORTS   │ ──> │ 2. DRIVER DECOMPOSITION │ ──> │ 3. MACRO VS POLICY      │
│ • Isolate loan vintage  │     │ • Origination channel   │     │ • Macro: Inflation,     │
│   (Q1 vs Q3 bookings)   │     │ • Scorecard decile shift│     │   unemployment spike    │
│ • Check early delinquen.│     │ • Bureau score cutoff   │     │ • Policy: Underwriting  │
└─────────────────────────┘     └─────────────────────────┘     │   criteria relaxed      │
                                                                └─────────────────────────┘
                                                                             │
┌─────────────────────────┐     ┌─────────────────────────┐                  │
│ 5. FINANCIAL IMPACT     │ <── │ 4. REMEDIATION POLICY   │ <────────────────┘
│ • Re-compute ECL & CAR  │     │ • Tighten cutoffs       │
│ • Adjust loan pricing   │     │ • Dynamic line reductions│
└─────────────────────────┘     └─────────────────────────┘
```

---

## 4. Stage 4: HR & Fit Round ("Why Risk Analytics from Civil Engineering?")

### Verbatim Placement-Ready Script:
```text
"During my Civil and Water Resources Engineering curriculum at IIT Kanpur, a substantial part of my research
and computational coursework centered around physical and probabilistic risk modeling—evaluating extreme
rainfall-runoff probabilities, predicting structural failure thresholds under stress, and quantifying
uncertainty in complex environmental networks.

Through projects like BridgeRisk and hydrological time-series modeling, I developed a deep appreciation
for applied probability, statistical validation, and the mathematical modeling of rare, high-consequence
tail events.

Institutional risk management applies that exact same first-principles quantitative rigor to economic
and financial systems—modeling credit default probabilities, estimating portfolio Value at Risk, and
ensuring institutional resilience under uncertainty. 

My background gives me strong mathematical foundations, comfort with complex predictive modeling, and an
instinctive discipline for stress-testing assumptions against data—skills that directly translate into
delivering value as a Quantitative Risk Analyst."
```
