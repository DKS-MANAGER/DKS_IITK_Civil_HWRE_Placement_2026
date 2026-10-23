# 07. Product Analytics: Practice Cases & Deep Telemetry Investigations

> **Track**: Product Analytics & Growth Data Science  
> **Target Audience**: IIT Kanpur candidates preparing for Product Analyst, Data Analyst, and Experimentation interviews.  
> **Content Structure**: Real-world product funnels, SQL cohort queries, A/B test failure diagnostics, and executive interview defenses.

---

## Case 1: Diagnosing a Sudden Drop in Fintech Checkout Conversion

### Business Situation
You are the Lead Product Analyst for a UPI payments app. Following the release of mobile app version `v5.4.0` on Tuesday morning, the product management team sounds an alarm: the core metric **Payment Success Rate (PSR)** has declined sharply from $88.5\%$ to $81.2\%$, threatening quarterly transaction volume targets.

### Provided Telemetry Data
The core transaction funnel comprises 4 steps:
1. `initiate_payment`: User taps "Pay" and enters amount.
2. `select_bank_account`: User selects debit bank account from linked list.
3. `enter_upi_pin`: App launches secure banking SDK keypad for 6-digit MPIN.
4. `payment_confirmed`: Bank NPCI gateway returns successful transaction receipt.

Funnel data captured over the 48 hours post-release across 200,000 transaction attempts:

| Funnel Step | Baseline (`v5.3.9`) Conversion | New Version (`v5.4.0`) Conversion | Drop-Off Delta |
| :--- | :---: | :---: | :---: |
| Step 1 $\to$ Step 2 (`initiate` $\to$ `select_bank`) | $98.2\%$ | $98.1\%$ | $-0.1\%$ |
| Step 2 $\to$ Step 3 (`select_bank` $\to$ `enter_pin`) | $94.5\%$ | **$86.0\%$** | **$-8.5\%$ (Major Anomaly!)** |
| Step 3 $\to$ Step 4 (`enter_pin` $\to$ `confirmed`) | $95.5\%$ | $96.1\%$ | $+0.6\%$ |

---

### Step-by-Step Diagnostic & Root Cause Investigation

#### 1. Funnel Drop-off Localization
The data immediately pinpoints the exact point of friction: Step 2 to Step 3 (`select_bank_account` to `enter_upi_pin`), where conversion collapsed by **$8.5$ percentage points**. Step 1 and Step 4 are operating within normal variance.

#### 2. Multi-Dimensional Dimensional Slicing (SQL Investigation)
To isolate the root cause, you execute a SQL dimensional breakdown of the Step 2 $\to$ Step 3 drop-off across three dimensions: Device Platform, App Version, and Bank Provider:

```sql
SELECT 
    device_platform,
    app_version,
    bank_provider,
    COUNT(DISTINCT CASE WHEN event_name = 'select_bank_account' THEN user_id END) AS users_selected_bank,
    COUNT(DISTINCT CASE WHEN event_name = 'enter_upi_pin' THEN user_id END) AS users_entered_pin,
    ROUND(100.0 * COUNT(DISTINCT CASE WHEN event_name = 'enter_upi_pin' THEN user_id END) / 
          NULLIF(COUNT(DISTINCT CASE WHEN event_name = 'select_bank_account' THEN user_id END), 0), 2) AS step2_to_3_cvr
FROM app_telemetry_events
WHERE timestamp >= '2026-10-21 00:00:00'
GROUP BY 1, 2, 3
ORDER BY users_selected_bank DESC;
```

#### Query Findings:
- iOS users on `v5.4.0`: Conversion is $94.8\%$ (Healthy).
- Android users on `v5.3.9` (old version): Conversion is $94.4\%$ (Healthy).
- Android users on `v5.4.0` across State Bank of India & HDFC Bank: Conversion is $94.1\%$ (Healthy).
- **Android users on `v5.4.0` with Android OS 14 specifically**: Conversion collapsed to **$42.3\%$**!

#### 3. Root Cause Isolation & Resolution
Inspecting client-side Android error logs reveals an unhandled permission exception: In Android 14, a new OS security sandbox blocks background activity launches. The secure banking MPIN overlay failed to launch, leaving users stuck on a frozen loading spinner until they force-closed the app.
- **Action**: Immediate hotfix patch `v5.4.1` deployed within 3 hours. Metric recovered back to $88.6\%$.

---

## Case 2: A/B Test Diagnostic: Sample Ratio Mismatch & Power Audit

### Situation
A food delivery app runs an A/B test to evaluate a "One-Click Reorder" widget on the home feed:
- Variant A (Control): Standard feed layout.
- Variant B (Treatment): Sticky horizontal carousel with previous orders.
- Randomization configuration: Target $50:50$ user split.
- Test run duration: 14 days.

### Logged Results
- Total unique visitors exposed:
  - Control ($N_A$): $122,400\text{ users}$
  - Treatment ($N_B$): $127,600\text{ users}$
  - Total ($N$): $250,000\text{ users}$
- Reported Metric: Treatment showed a statistically significant $+4.2\%$ lift in average order value (AOV) with $p = 0.012$.
- The Product Manager requests permission to ship Treatment to $100\%$ of users immediately.

---

### Candidate Analysis: Validating Test Integrity

#### Step 1: Chi-Square Test for Sample Ratio Mismatch (SRM)
Before evaluating any metrics (AOV, conversion, retention), you must verify whether the sample split was unbiased:
- Expected users per variant: $E_A = E_B = 250,000 \times 0.50 = 125,000$.
- Observed users: $O_A = 122,400$, $O_B = 127,600$.
- Deviations: $|O - E| = |122,400 - 125,000| = 2,600\text{ users}$.

$$\chi^2 = \frac{(122,400 - 125,000)^2}{125,000} + \frac{(127,600 - 125,000)^2}{125,000} = \frac{(-2600)^2}{125,000} + \frac{(2600)^2}{125,000} = \frac{6,760,000}{125,000} + \frac{6,760,000}{125,000} = 54.08 + 54.08 = \mathbf{108.16}$$

#### Critical Value Comparison:
For 1 degree of freedom, $\chi^2_{0.05} = 3.841$ and $\chi^2_{0.001} = 10.828$.
Here, $\chi^2 = 108.16 \implies p \approx 2.4 \times 10^{-25}$.

#### Conclusion & Decision:
**Severe Sample Ratio Mismatch (SRM) confirmed!** 
The odds of this imbalance occurring by random chance are less than 1 in $10^{24}$. The treatment variant experienced systematic selection bias (e.g., users who placed orders triggered redundant event logs, or tracking cookies were dropped unevenly). 
**Executive Recommendation**: Reject the launch proposal. The reported $+4.2\%$ lift is a statistical artifact of the sample imbalance. Halt the test, patch the telemetry assignment bug, and re-run.

---

## Executive Interview Defense Probes

> **Q1**: *"What is the difference between a Pre-Post analysis and an A/B test? Why can't we just compare conversion this month vs. last month?"*  
> **Model Answer**: "A Pre-Post comparison is fundamentally flawed because it confounds the feature change with uncontrollable external variables—such as seasonality (festive surges vs. post-holiday slumps), marketing campaigns, competitor promotions, macroeconomic shifts, and app crashes. An A/B test is a randomized controlled trial that exposes both cohorts simultaneously under identical macroeconomic and seasonal conditions, isolating the true causal treatment effect."

> **Q2**: *"If a metric lift is statistically significant ($p = 0.03$), does that automatically mean we should ship the feature?"*  
> **Model Answer**: "No. Statistical significance only tells us that the observed difference is unlikely due to random chance; it does not measure **business impact or practical significance**. We must evaluate three factors: (1) **Magnitude of Effect vs. Engineering Maintenance Cost**: A $+0.1\%$ lift that costs $₹50\text{ Lakhs/year}$ to maintain may have negative ROI. (2) **Impact on Guardrail Metrics**: Did checkout speed increase at the expense of an increase in customer support tickets or refund rates? (3) **Novelty Bias**: Did users click the new button simply because it was unfamiliar, with engagement decaying after 14 days?"
