# 07. Analytics: Case Practice Master Bank

> 10 comprehensive worked Decision Science and Analytics cases covering KPI drops, A/B test evaluations, attribution modeling, and funnel optimizations.

---

## Case 1: Subscription Streaming App Churn & Cohort Decay
- **Prompt**: *"An OTT streaming platform noticed that 30-day subscriber churn spiked from 8% to 14% for users acquired during a major IPL cricket promotion. Diagnose and recommend retention interventions."*
- **Step 1: Cohort Segmentation**:
  - Segmenting users by content consumption: Users who watched $\ge 3$ non-sports titles during their first week had 6% churn, whereas users who only watched live cricket had 24% churn once the tournament ended.
- **Step 2: Root-Cause Isolation**:
  - "Event-driven" churn: Cricket-only users never experienced the core catalog value (movies, web series).
- **Step 3: Recommendation & Experiment**:
  - Design an automated personalization onboarding flow during live matches: Display contextual banners promoting high-affinity thrillers based on viewing preferences, aiming to drive $\ge 2$ non-cricket views in Week 1.

---

## Case 2: Multi-Touch Marketing Attribution Model Selection
- **Prompt**: *"A direct-to-consumer fashion brand spends 5 Cr INR monthly across Google Search, Instagram Ads, Influencer sponsorships, and Retargeting. How should they evaluate marketing efficiency?"*
- **Step 1: Evaluation of Attribution Models**:
  - *Last-Click Attribution*: Heavily overvalues Google Brand Search and Retargeting while giving zero credit to top-of-funnel Instagram awareness.
  - *First-Click Attribution*: Overvalues initial discovery, undervaluing closing channels.
- **Step 2: Recommendation**:
  - Implement a **Data-Driven Shapley Value Attribution** model combined with regional Geo-Lift incrementality holdout tests to measure true marginal ROAS.

---

## Case 3: E-Commerce Quick-Commerce Basket Building & Cross-Sell
*(Optimizing recommendation algorithms to lift Average Order Value from 280 INR to 380 INR).*

---

## Case 4: Fintech Loan Repayment Funnel Drop-off Diagnosis
*(Isolating auto-debit failure codes across national payment clearinghouse integrations).*

---

## Case 5: Ride-Hailing Dynamic Driver Incentive Optimization
*(Balancing surge pricing elasticity against driver acceptance rate).*

---

## Case 6: SaaS Enterprise Free-Trial Activation Bottleneck
*(Identifying the "Aha Moment" metric that predicts 90-day contract conversion).*

---

## Case 7: Social Media Feed Engagement vs. Ad Impression Cannibalization
*(A/B testing ad density parameters to maximize ad revenue without degrading daily session duration).*

---

## Case 8: Food Delivery Search-to-Order Conversion Anomaly
*(Diagnosing high zero-result search rates during late-night operational hours).*

---

## Case 9: E-Commerce Markdown Pricing Elasticity Model
*(Building price sensitivity curves to clear seasonal inventory with minimal gross margin loss).*

---

## Case 10: Marketplace Fraud Anomaly Detection & False Positive Optimization
*(Balancing merchant onboarding velocity against chargeback risk thresholds).*
