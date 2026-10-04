# 04. Business Analyst: Applied Statistics & Experimentation

> Practical, placement-focused statistical techniques: A/B testing, hypothesis testing, sample size calculation, and statistical bias diagnosis.

---

## 1. Applied Experimentation & A/B Testing Framework

Business Analysts use A/B testing to validate product, pricing, and algorithmic changes before full rollout.

```text
                             A/B TESTING WORKFLOW
┌──────────────────────┐     ┌──────────────────────┐     ┌──────────────────────┐
│  1. HYPOTHESIS & MDE │ ──> │  2. SAMPLE SIZING    │ ──> │ 3. SPLIT & EXECUTION │
│  State null ($H_0$)  │     │  Power = 80% (β=0.20)│     │  50/50 Randomization │
│  Target lift ($\Delta$)│   │  Significance α=0.05 │     │  Check SRM Bias      │
└──────────────────────┘     └──────────────────────┘     └──────────────────────┘
                                                                     │
┌──────────────────────┐     ┌──────────────────────┐                │
│ 5. DECISION & ROLLOUT│ <── │ 4. HYPOTHESIS TEST   │ <──────────────┘
│ Rollout if p < 0.05  │     │ 2-sample Z-test /    │
│ & Guardrails intact  │     │ Chi-Square test      │
└──────────────────────┘     └──────────────────────┘
```

### Key Statistical Formulas
| Concept | Mathematical Formula | Practical Placement Interpretation |
|:---|:---|:---|
| **Sample Size per Variant ($N$)** | $N pprox rac{16 \cdot p(1-p)}{\Delta^2}$ | For baseline conversion $p = 5\%$ ($0.05$) and absolute MDE $\Delta = 0.5\%$ ($0.005$):<br>$N pprox rac{16 	imes 0.05 	imes 0.95}{(0.005)^2} = rac{0.76}{0.000025} = \mathbf{30,400	ext{ users/variant}}$. |
| **Z-Score for Proportions** | $Z = rac{\hat{p}_B - \hat{p}_A}{\sqrt{\hat{p}(1-\hat{p})\left(rac{1}{N_A} + rac{1}{N_B}ight)}}$ | Test statistic to evaluate if conversion difference between Variant B and Variant A is statistically significant ($|Z| > 1.96 \implies p < 0.05$). |
| **Sample Ratio Mismatch (SRM)**| $\chi^2 = \sum rac{(O_i - E_i)^2}{E_i}$ | Validates if traffic allocation split (e.g. 50/50) was corrupted by technical redirection or bot-filtering bugs ($p < 0.001$ invalidates test). |

---

## 2. Statistical Traps & Interview Gotchas

### 1. Simpson's Paradox
- **Phenomenon**: A trend appears in different groups of data but disappears or reverses when these groups are combined.
- **Classic BA Case**: Variant B has a higher overall conversion rate (4.2% vs 3.8%) than Variant A, but Variant A had higher conversion in both Mobile (5% vs 4.8%) and Desktop (2% vs 1.9%).
- **Root Cause**: Traffic allocation mix shift—Variant B was accidentally shown to 80% Mobile users (higher baseline conversion), confounding overall results.

### 2. Type I vs. Type II Errors
- **Type I Error ($lpha$, False Positive)**: Concluding a feature increased conversion when it actually had no effect (controlled at 5%).
- **Type II Error ($eta$, False Negative)**: Missing a true positive lift because sample size was too small (Power $1-eta = 80\%$).

### 3. Correlation vs. Causation
- **Classic BA Case**: Users who add $\ge 3$ items to their wishlist have $4	imes$ higher 30-day retention.
- **Trap**: Forcing users to add items to their wishlist will not increase retention 4x. Wishlist usage is a symptom of high organic intent, not the causal driver.
