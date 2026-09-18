# 03. Analytics: Commercial Decision Science & Telemetry

> Deep-dive business metrics, A/B testing statistical frameworks, customer lifetime value modeling, and cohort decay analysis.

---

## 1. Commercial Telemetry & Metric Taxonomy

### The AARRR Pirate Metric Framework
```text
ACQUISITION: Visitors arriving via organic search, paid ads, referrals (Metric: CAC, Click-Through-Rate)
    ↓
ACTIVATION: User experiences the "Aha! Moment" (Metric: First-action completion rate, 24h Setup %)
    ↓
RETENTION: User returns repeatedly over time (Metric: Day-1, Day-7, Day-30 Cohort Retention %)
    ↓
REVENUE: User generates commercial value (Metric: ARPU, AOV, Gross Margin, Expansion MRR)
    ↓
REFERRAL: User invites peers (Metric: K-Factor Viral Coefficient = Invites × Conversion %)
```

---

## 2. A/B Testing & Statistical Experimentation

### Sample Size Determination Formula
$$N = \frac{16 \cdot \sigma^2}{\Delta^2}$$
Where:
- $\sigma^2$: Baseline variance of the target metric.
- $\Delta = \mu_{\text{treatment}} - \mu_{\text{control}}$: Minimum Detectable Effect (MDE).
- Factor $16$: Derived from standard $\alpha = 0.05$ (5% False Positive rate) and $\beta = 0.20$ (80% Statistical Power).

### Common Experimentation Pitfalls & Mitigations
1. **Sample Ratio Mismatch (SRM)**: Traffic split deviates from 50/50. Caused by bot filtering skew, browser redirection lags, or buggy CDN hashing.
2. **Peeking Problem (P-Hacking)**: Stopping an experiment as soon as $p < 0.05$. Inflates true false positive rate from 5% to $>30%$. Must adhere to fixed sample sizes or use Sequential Testing (e.g., SPRT).
3. **Novelty Effect vs. Primacy Effect**: Early metric spikes due to user curiosity that decay to zero after 2 weeks.
