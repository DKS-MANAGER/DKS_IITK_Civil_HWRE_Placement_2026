# Business Analyst — Rapid Revision Sheet

> Canonical, condensed 60/30/10/5-minute emergency revision sheet for Business Analyst interviews and Online Assessments.

---

## 🔗 Canonical Learning Source
- 📖 [Complete Business Analyst Preparation Track](../../01_roles/business-analyst/README.md)

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

### 1. Metric Drop Diagnostic (5-Step Framework)
$$\text{Verify Data Telemetry} \longrightarrow \text{Mathematical Driver Tree} \longrightarrow \text{Segment Cuts} \longrightarrow \text{Root Cause} \longrightarrow \text{Action}$$

### 2. AARRR Funnel Architecture
- **Acquisition** (CAC, CTR) $\rightarrow$ **Activation** (Signup %) $\rightarrow$ **Retention** (D30 Churn) $\rightarrow$ **Revenue** (AOV, Take Rate) $\rightarrow$ **Referral** ($K$-factor).

---

## 2. 30-Minute Core Revision: Formulas & Equations

| Metric | Formula | Practical Rule of Thumb |
|:---|:---|:---|
| **CAC** | $\frac{\text{S\&M Spend}}{\text{New Customers}}$ | Acquisition cost per paying user |
| **LTV** | $\frac{\text{ARPU} \times \text{Gross Margin } \%}{\text{Monthly Churn}}$ | Lifetime gross margin per user |
| **LTV / CAC** | $\frac{\text{LTV}}{\text{CAC}}$ | Benchmark $\ge 3.0\times$ |
| **CM2** | $\text{CM1} - (\text{Fulfillment} + \text{PG} + \text{Delivery})$ | True operational order margin |
| **Sample Size (A/B)** | $N \approx \frac{16 \cdot p(1-p)}{\Delta^2}$ | Sizing two-proportion tests |

---

## 3. 10-Minute Rapid Revision: Common Traps & High-Yield Q&A

### ⚠️ Common Interview Traps
- Confusing correlation with causation (e.g. wishlist usage vs organic intent).
- Ignoring integer division truncation in SQL (`1.0 * a / b`).
- Missing Sample Ratio Mismatch (SRM) before declaring A/B test winners.

### ⚡ Rapid Practice Questions & Answers
1. **Q**: *Cart abandonment surged 10% after app release. Diagnose.* -> **A**: Isolate by OS/payment mode -> check UPI deep-link latency or intent permission crashes.
2. **Q**: *AOV rose 20% but total revenue fell 10%. Why?* -> **A**: Total order volume collapsed ($>25\%$ drop) due to removal of low-ticket entry SKUs.

---

## 4. 5-Minute Pre-Interview Checklist & Narrative

### 🎯 5-Minute Readiness Audit
- [ ] SQL execution order reviewed (`FROM` -> `WHERE` -> `GROUP BY` -> `HAVING` -> `SELECT` -> `ORDER BY`).
- [ ] Excel formulas memorized (`XLOOKUP`, `SUMIFS`, `INDEX/MATCH`).
- [ ] 5-step metric drop framework ready.

### 🗣️ The 60-Second "Why Business Analyst from Civil?" Pitch
> *"My Civil Engineering background at IIT Kanpur grounded me in rigorous quantitative problem solving, data modeling under physical constraints, and analyzing complex networks. I am applying this structured, analytical discipline to high-velocity decision-making in Business Analyst."*
