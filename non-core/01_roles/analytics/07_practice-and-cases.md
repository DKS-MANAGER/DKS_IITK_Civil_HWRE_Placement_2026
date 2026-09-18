# 07. Analytics: Worked Practice Cases & Decision Models

> Realistic data-driven business cases covering churn modeling, funnel attribution, and marketing mix modeling.

---

## Case 1: Subscription Churn Spike Investigation

### Scenario Prompt
*"A streaming video subscription platform observed a 28% increase in monthly churn for users in their 2nd month of subscription. You are tasked with analyzing the underlying behavioral signals and proposing an automated retention engine."*

### Analytical Approach & SQL Telemetry
1. **Cohort Segmentation**: Segmented users by content consumption depth (Hours watched in Month 1) and device type.
2. **Key Behavioral Finding**: Users who watched $<3$ distinct content genres in their first 14 days experienced an 82% churn probability in Month 2.
3. **Recommendation**: Implement an automated personalized recommendation carousel pushing cross-genre top-rated shows to Day-7 users with low genre breadth.

---

## Case 2: Multi-Touch E-Commerce Attribution Model
*(Full comparative evaluation of First-Touch, Last-Touch, Linear, and Markov-Chain attribution models to optimize a 5 Cr INR digital ad budget).*
