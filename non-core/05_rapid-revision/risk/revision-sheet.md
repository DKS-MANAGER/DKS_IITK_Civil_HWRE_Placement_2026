# Risk Analyst — Rapid Revision Sheet

> Canonical, condensed 60/30/10/5-minute emergency revision sheet for Risk Analyst interviews and Online Assessments.

---

## 🔗 Canonical Learning Source
- 📖 [Complete Risk Analyst Preparation Track](../../01_roles/risk/README.md)

---

## ⏱️ Time-Based Revision Hierarchy

```text
┌─────────────────────────┬─────────────────────────┬─────────────────────────┬─────────────────────────┐
│     60-MIN REVISION     │     30-MIN REVISION     │     10-MIN REVISION     │   5-MIN PRE-INTERVIEW   │
│ Complete framework &    │ Core formulas, metrics  │ High-frequency trap     │ Mental composure,       │
│ question review         │ & issue tree structures │ review & shortcuts      │ pitch & checklist       │
└─────────────────────────┴─────────────────────────┴─────────────────────────┴─────────────────────────┘
```

---

## 1. 60-Minute Deep Revision: Core Frameworks

### 1. Credit Risk Scorecard Development
$$\text{Raw Feature} \longrightarrow \text{Fine Binning} \longrightarrow \text{Coarse/WoE Binning} \longrightarrow \text{Logistic Regression} \longrightarrow \text{Score Scaling}$$

### 2. Market Risk & Basel Governance
- **CAR**: $\frac{\text{Tier 1} + \text{Tier 2 Capital}}{\text{RWA}} \ge 9\% + 2.5\%$ CCB.
- **Three Lines of Defense**: Front Office (1st) $\rightarrow$ Risk/Compliance (2nd) $\rightarrow$ Internal Audit (3rd).

---

## 2. 30-Minute Core Revision: Formulas & Equations

| Risk Formula | Mathematical Definition | Context |
|:---|:---|:---|
| **Expected Loss (EL)** | $EL = PD \times LGD \times EAD$ | Provisioned loss |
| **Unexpected Loss (UL)** | $UL = EAD \times \sqrt{PD \cdot \sigma_{LGD}^2 + LGD^2 \cdot \sigma_{PD}^2}$ | Capital reserve charge |
| **Weight of Evidence (WoE)**| $\ln \left(\frac{G_i / G_{\text{total}}}{B_i / B_{\text{total}}}\right)$ | Feature risk transformation |
| **Information Value (IV)** | $\sum (Dist\_Good - Dist\_Bad) \times WoE$ | Predictive power ($>0.3$ strong) |
| **1-Day Parametric VaR**| $Z_{\alpha} \times \sigma_p \times V_p$ | 99% 1-day tail risk ($Z=2.326$) |
| **Time Scaling** | $\text{VaR}_{T\text{-day}} = \text{VaR}_{1\text{-day}} \times \sqrt{T}$ | $\sqrt{10} \approx 3.162$ for Basel 10d |

---

## 3. 10-Minute Rapid Revision: Common Traps & High-Yield Q&A

### ⚠️ Common Interview Traps
- Assuming financial returns are normally distributed (ignores fat-tail kurtosis).
- Misinterpreting Population Stability Index ($PSI \ge 0.25$ mandates model rebuild).
- Using Accuracy instead of PR-AUC / ROC-AUC on highly imbalanced default data.

### ⚡ Rapid Practice Questions & Answers
1. **Q**: *A bank has 50 Cr drawn, 20 Cr undrawn (CCF=50%), PD=2%, LGD=40%. Calculate EL.* -> **A**: $EAD = 50 + 10 = 60\text{ Cr} \implies EL = 0.02 \times 0.40 \times 60 = 0.48\text{ Cr} = 48\text{ Lakh INR}$.
2. **Q**: *Why is Expected Shortfall better than VaR?* -> **A**: ES is a coherent risk measure (sub-additive) measuring average tail severity, whereas VaR only measures threshold.

---

## 4. 5-Minute Pre-Interview Checklist & Narrative

### 🎯 5-Minute Readiness Audit
- [ ] Bayes' Theorem and Poisson distribution formulas fresh.
- [ ] WoE / IV / KS / Gini / PSI definitions verified.
- [ ] BridgeRisk / Extreme value project pitch ready.

### 🗣️ The 60-Second "Why Risk Analyst from Civil?" Pitch
> *"My Civil Engineering background at IIT Kanpur grounded me in rigorous quantitative problem solving, data modeling under physical constraints, and analyzing complex networks. I am applying this structured, analytical discipline to high-velocity decision-making in Risk Analyst."*
