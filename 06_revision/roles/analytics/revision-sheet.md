# Analytics & Decision Science — Rapid Revision Sheet

> Canonical, condensed 60/30/10/5-minute emergency revision sheet for Analytics & Decision Science interviews and Online Assessments.

---

## 🔗 Canonical Learning Source
- 📖 [Complete Analytics & Decision Science Preparation Track](../../01_roles/analytics/README.md)

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

### 1. The Experimentation Lifecycle
$$\text{Hypothesis \& MDE} \longrightarrow \text{Sample Sizing} \longrightarrow \text{Randomized Split} \longrightarrow \text{SRM Check} \longrightarrow \text{Z-Test / Rollout}$$

### 2. User Cohort Retention Matrix
- Track registration cohorts over Week-0 to Week-12 to isolate genuine retention decay from acquisition mix shifts.

---

## 2. 30-Minute Core Revision: Formulas & Equations

| Concept | Formula | Application |
|:---|:---|:---|
| **A/B Sample Size** | $N \approx \frac{16 \cdot p(1-p)}{\Delta^2}$ | Sample size per variant |
| **SRM Chi-Square** | $\chi^2 = \sum \frac{(O_i - E_i)^2}{E_i}$ | Sample Ratio Mismatch check ($p<0.001$) |
| **DAU / MAU** | $\frac{\text{DAU}}{\text{MAU}}$ | User engagement stickiness |
| **Viral K-Factor** | $i \times c$ | Invites per user $\times$ conversion |

---

## 3. 10-Minute Rapid Revision: Common Traps & High-Yield Q&A

### ⚠️ Common Interview Traps
- Peeking at A/B test results and stopping early (inflates false positive rate to $>30\%$).
- Confusing statistical significance with business practical significance.
- Writing slow nested Python loops instead of vectorized Pandas/NumPy operations.

### ⚡ Rapid Practice Questions & Answers
1. **Q**: *Calculate sample size for 5% baseline and 0.5% absolute MDE.* -> **A**: $N \approx \frac{16 \times 0.05 \times 0.95}{(0.005)^2} = 30,400$ users per variant.
2. **Q**: *What evaluation metric for 1% imbalanced fraud?* -> **A**: Precision-Recall AUC (PR-AUC) or ROC-AUC with F1-score; never raw accuracy.

---

## 4. 5-Minute Pre-Interview Checklist & Narrative

### 🎯 5-Minute Readiness Audit
- [ ] Pandas vectorized aggregations and datetime methods reviewed.
- [ ] SQL window functions (`DENSE_RANK`, `LAG`, `SUM() OVER()`) clear.
- [ ] A/B testing MDE, Power (80%), and Significance (5%) math ready.

### 🗣️ The 60-Second "Why Analytics & Decision Science from Civil?" Pitch
> *"My Civil Engineering background at IIT Kanpur grounded me in rigorous quantitative problem solving, data modeling under physical constraints, and analyzing complex networks. I am applying this structured, analytical discipline to high-velocity decision-making in Analytics & Decision Science."*
