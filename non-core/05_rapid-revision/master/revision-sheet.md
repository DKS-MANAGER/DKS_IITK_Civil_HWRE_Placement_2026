# Master Non-Core Placement Emergency Revision Sheet

> Universal 60-minute emergency cheat sheet covering all high-frequency quantitative, case, behavioral, and technical topics across non-core campus interviews at IIT Kanpur.

---

## ⏱️ Time-Based Master Revision Timeline

```text
┌─────────────────────────┬─────────────────────────┬─────────────────────────┬─────────────────────────┐
│     60-MIN OVERVIEW     │     30-MIN MATH & SQL   │     10-MIN CASES & FIT  │   5-MIN FINAL FOCUS     │
│ Complete cross-role     │ Mental math shortcuts,  │ Core issue trees,       │ Pitch delivery,         │
│ formula & concept audit │ SQL execution & stats   │ 4 STAR stories          │ checklist & composure   │
└─────────────────────────┴─────────────────────────┴─────────────────────────┴─────────────────────────┘
```

---

## 1. Universal Business & Quantitative Formulas

| Formula / Metric | Mathematical Expression | Practical Interpretation |
|:---|:---|:---|
| **Rule of 72 (Doubling)** | $t \approx \frac{72}{g\%}$ | At 8% growth, doubles in $\frac{72}{8} = 9$ years. |
| **CAGR Approximation** | $\text{CAGR} \approx \frac{\text{Total Growth } \%}{n} \times 0.9$ | Fast multi-year compounded growth. |
| **Customer Lifetime Value**| $LTV = \frac{\text{ARPU} \times \text{Gross Margin } \%}{\text{Monthly Churn}}$ | Net gross profit per customer lifespan. |
| **Customer Acquisition Cost**| $CAC = \frac{\text{Total S\&M Spend}}{\text{New Customers Acquired}}$ | Marketing cost per acquired user ($LTV/CAC \ge 3\times$). |
| **Contribution Margin 2**| $\text{CM1} - (\text{Fulfillment} + \text{PG Fee} + \text{Delivery})$ | True operational profit per order. |
| **A/B Test Sample Size** | $N \approx \frac{16 \cdot p(1-p)}{\Delta^2}$ | Users needed per variant ($\alpha=0.05, \beta=0.20$). |
| **Little's Law** | $L = \lambda \times W$ | Inventory = Throughput $\times$ Lead Time. |
| **Expected Credit Loss** | $EL = PD \times LGD \times EAD$ | 1-year anticipated default loss. |

---

## 2. Universal SQL Querying Execution Order & Syntax

```text
1. FROM & JOIN  ──>  2. WHERE  ──>  3. GROUP BY  ──>  4. HAVING  ──>  5. SELECT  ──>  6. DISTINCT  ──>  7. ORDER BY  ──>  8. LIMIT
```
- **Window Functions**: `ROW_NUMBER()` (Unique sequential), `RANK()` (Skips ties), `DENSE_RANK()` (No skipping).
- **Lag/Lead**: `LAG(col, 1) OVER (PARTITION BY id ORDER BY date)`.

---

## 3. The 4 Universal STAR Stories (Have These Ready)
1. **Inclusive Leadership**: Leading a team through technical disagreement with an objective decision matrix.
2. **Overcoming Failure (CARL)**: Rapid root-cause diagnosis after model divergence without making emotional excuses.
3. **Influencing Without Authority**: Persuading an external team to adopt an automated Python validation script.
4. **Ambiguity / Pressure**: Prioritizing 80/20 critical factors under a tight 48-hour project deadline.

---

## 4. Universal 5-Minute Pre-Interview Checklist
- [ ] 90-second *"Walk me through your resume"* pitch polished.
- [ ] Verbatim *"Why Non-Core from Civil Engineering?"* answer fresh.
- [ ] Speed math shortcuts verified (Rule of 72, fraction-to-percentages).
- [ ] Pen, paper, and glass of water ready; posture upright, calm, and confident.
