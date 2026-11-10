# Module 06 — Model Performance Monitoring & Back-Testing Methodologies

This module covers the core day-to-day operational responsibility of the **QA Model Monitoring** team at Barclays: establishing surveillance frameworks, defining early warning triggers, back-testing predictive accuracy, and formulating remediation recommendations for model governance committees.

---

## 1. The Core Purpose & Philosophy of Model Monitoring

Model monitoring is not an academic post-mortem; it is **real-time defensive surveillance**:
- **Why Models Deteriorate**: Even if a credit risk model was mathematically flawless at development, external reality shifts. Changes in underwriting policies, competitor credit card offers, macroeconomic recessions, and consumer borrowing habits induce **data drift** and **concept drift**.
- **The Cost of Undetected Degradation**: If an uncalibrated PD model underestimates default probabilities by 25%, the bank under-provisions for IFRS 9 Expected Credit Loss, risks supervisory enforcement actions from the Prudential Regulation Authority (PRA), and holds insufficient Common Equity Tier 1 (CET1) capital.

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                              THE THREE PILLARS OF MODEL HEALTH                         │
├────────────────────┬───────────────────────────────────┬───────────────────────────────┤
│    Health Pillar   │         Core Question Asked       │       Key Monitored Metrics   │
├────────────────────┼───────────────────────────────────┼───────────────────────────────┤
│ 1. Discrimination  │ "Can the model still rank-order   │ • ROC Curve & ROC-AUC         │
│                    │  good vs. bad borrowers?"         │ • Gini Coefficient           │
│                    │                                   │ • Kolmogorov-Smirnov (KS) stat│
├────────────────────┼───────────────────────────────────┼───────────────────────────────┤
│ 2. Calibration     │ "Do the predicted probabilities   │ • Observed vs. Predicted PD   │
│                    │  match actual realized default %?"│ • Brier Score, Log Loss       │
│                    │                                   │ • Hosmer-Lemeshow Goodness    │
├────────────────────┼───────────────────────────────────┼───────────────────────────────┤
│ 3. Stability       │ "Has the incoming population or   │ • Population Stability (PSI)  │
│                    │  underlying feature mix shifted?" │ • Characteristic Stability    │
│                    │                                   │ • Missing value & drop trends │
└────────────────────┴───────────────────────────────────┴───────────────────────────────┘
```

---

## 2. The Traffic-Light Trigger Framework

Barclays establishes standardized **Traffic-Light Thresholds** to govern model monitoring reporting and trigger automated governance escalations:

```
┌───────────────┬───────────────────────────────────┬────────────────────────────────────────────────────────┐
│ Traffic Light │          Threshold State          │                   Mandated Governance Action           │
├───────────────┼───────────────────────────────────┼────────────────────────────────────────────────────────┤
│ GREEN         │ Model performing within expected  │ • Continue normal model usage.                         │
│ (Satisfactory)│ bounds; zero tolerance breaches.  │ • Maintain scheduled quarterly monitoring cadence.     │
├───────────────┼───────────────────────────────────┼────────────────────────────────────────────────────────┤
│ AMBER         │ Moderate deterioration detected;  │ • Flag as early warning in Model Monitoring Pack (MMP).│
│ (Review)      │ early warning threshold breached. │ • Increase monitoring frequency to monthly.            │
│               │                                   │ • Initiate root cause diagnostic investigation.        │
├───────────────┼───────────────────────────────────┼────────────────────────────────────────────────────────┤
│ RED           │ Severe deterioration or stability │ • Immediate escalation to Model Governance Committee.  │
│ (Breach)      │ breakdown; critical breach.       │ • Implement immediate Post Model Adjustment (PMA).     │
│               │                                   │ • Formally schedule model recalibration or rebuild.    │
└───────────────┴───────────────────────────────────┴────────────────────────────────────────────────────────┘
```

### 2.1 Standardized Monitored Metric Thresholds
```
┌─────────────────────────┬──────────────────────┬──────────────────────┬──────────────────────┐
│         Metric          │        Green         │        Amber         │         Red          │
├─────────────────────────┼──────────────────────┼──────────────────────┼──────────────────────┤
│ Population Stability    │ $\text{PSI} < 0.10$  │ $0.10 \le \text{PSI}│ $\text{PSI} > 0.25$  │
│ Index (PSI)             │ (No significant shift│ \le 0.25$ (Moderate) │ (Significant shift)  │
├─────────────────────────┼──────────────────────┼──────────────────────┼──────────────────────┤
│ Gini Drop vs.           │ $\Delta \text{Gini}  │ $10\% \le \Delta     │ $\Delta \text{Gini}  │
│ Development Benchmark   │ < 10\%$ relative     │ \text{Gini} \le 20\%$│ > 20\%$ relative     │
├─────────────────────────┼──────────────────────┼──────────────────────┼──────────────────────┤
│ Kolmogorov-Smirnov (KS) │ $\text{KS} \ge 35\%$ │ $25\% \le \text{KS}  │ $\text{KS} < 25\%$   │
│                         │                      │ < 35\%$              │                      │
├─────────────────────────┼──────────────────────┼──────────────────────┼──────────────────────┤
│ PD Calibration Ratio    │ $0.90 \le \text{O/E} │ 0.80 \le \text{O/E}  │ $\text{O/E} < 0.70$  │
│ (Observed / Expected)   │ \le 1.10$            │ < 0.90 \text{ or }   │ \text{ or }          │
│                         │                      │ 1.10 < \text{O/E}    │ \text{O/E} > 1.30$   │
│                         │                      │ \le 1.30$            │                      │
└─────────────────────────┴──────────────────────┴──────────────────────┴──────────────────────┘
```

---

## 3. Back-Testing Methodologies in Banking

**Back-testing** evaluates a model’s historical predictive accuracy by comparing initial ex-ante predictions against actual ex-post realized outcomes across a completed observation window (typically 12 months for 1-year default predictions).

### 3.1 Predicted vs. Realized Default Rates (Binomial Test)
To test whether the observed default count $D$ in a rating grade with $N$ accounts and predicted default probability $p$ is statistically consistent with model calibration, analysts perform a **One-Sided Binomial Hypothesis Test**:

$$H_0: p_{\text{actual}} \le p_{\text{model}} \quad \text{vs.} \quad H_1: p_{\text{actual}} > p_{\text{model}}$$

Under the Normal approximation (valid for $N \cdot p \ge 5$):

$$Z = \frac{D - N \cdot p}{\sqrt{N \cdot p \cdot (1 - p)}}$$

- If $Z > 1.645$ (at 95% confidence level), the null hypothesis is rejected: **the model statistically underestimates default rates**, triggering a calibration breach.

### 3.2 Realized vs. Predicted LGD & EAD Back-Testing
1. **LGD Back-Testing**: Compares the historical predicted downturn LGD against the completed workout recoveries of defaulted cohorts:
   - Challenge: Realized workout LGD requires a 2-to-5-year multi-year recovery resolution window. Quants track **cumulative recovery curves** to detect early shortfalls.
2. **EAD Back-Testing**: Evaluates whether realized drawdowns on defaulted revolving facilities matched the predicted Credit Conversion Factor (CCF):
   $$\text{CCF Forecast Error} = \text{CCF}_{\text{realized}} - \text{CCF}_{\text{predicted}}$$
   - Systematic negative forecast errors indicate that the bank is underestimating exposure at default.

---

## 4. The Decision Matrix for Model Remediation

When model monitoring identifies a performance or stability breach, the QA Model Monitoring analyst must recommend one of four concrete operational actions:

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                        MODEL REMEDIATION DECISION HIERARCHY                            │
├────────────────────┬───────────────────────────────────┬───────────────────────────────┤
│ Remediation Action │         When to Recommend         │       Governance Mechanism    │
├────────────────────┼───────────────────────────────────┼───────────────────────────────┤
│ 1. Increase        │ Minor transient spike in PSI      │ • Monthly tracking report.    │
│    Monitoring      │ (0.10–0.15) driven by temporary   │ • Re-evaluate next quarter    │
│                    │ seasonal promotion.               │   before altering model.      │
├────────────────────┼───────────────────────────────────┼───────────────────────────────┤
│ 2. Post Model      │ Model underpredicts default rate  │ • Calculate dollar capital /  │
│    Adjustment (PMA)│ due to sudden macroeconomic shock │   provision top-up overlay.   │
│                    │ (e.g., energy price spike).       │ • Approved by Committee.      │
├────────────────────┼───────────────────────────────────┼───────────────────────────────┤
│ 3. Parameter       │ Discrimination remains strong     │ • Re-estimate intercept /     │
│    Recalibration   │ (Gini high), but calibration is   │   scaling factors on recent   │
│                    │ systematically biased (O/E shift).│   data; keep scorecard bins.  │
├────────────────────┼───────────────────────────────────┼───────────────────────────────┤
│ 4. Full Model      │ Fundamental structural failure:   │ • Formal project charter to   │
│    Redevelopment   │ Gini drops > 25%, feature signs   │   retire old model and train  │
│                    │ invert, severe permanent drift.   │   new model from scratch.     │
└────────────────────┴───────────────────────────────────┴───────────────────────────────┘
```

