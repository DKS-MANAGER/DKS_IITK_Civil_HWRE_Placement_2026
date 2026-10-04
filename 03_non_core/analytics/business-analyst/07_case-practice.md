# 07. Business Analyst: Case Practice Master Bank

> 10 comprehensive worked Business Analyst cases covering KPI drops, unit economics turnarounds, A/B test experiments, and funnel optimizations.

---

## Case 1: E-Commerce Mobile App Cart Abandonment Surge
- **Prompt**: *"Flipkart's cart abandonment rate increased from 68% to 76% on Android devices over the last 14 days following App Version 14.2 release. Diagnose and propose an immediate fix."*
- **Step 1: Clarification & Data Slicing**:
  - Cart abandonment = $rac{	ext{Users who added to cart but did not complete checkout}}{	ext{Total users who added to cart}}$.
  - Segmenting by payment mode: UPI drop-off spiked by 140%, while Credit Card and COD remained stable.
- **Step 2: Root-Cause Isolation**:
  - Telemetry logs show UPI intent call to external apps (GPay, PhonePe) timed out on Android 13/14 due to missing background intent permissions in the new APK release.
- **Step 3: Quantified Impact & Solution**:
  - Daily cart value lost = $4.2	ext{ Cr INR}$.
  - Immediate fix: Hotfix APK release (v14.2.1) restoring intent flags; temporary fallback prompting QR-code display for failed deep-links.

---

## Case 2: Quick-Commerce Dark Store Unit Economics Turnaround
- **Prompt**: *"A quick-commerce grocery dark store in Indiranagar, Bengaluru is losing 22 INR per order. How do you make it profitable within 90 days?"*
- **Current Unit Economics**:
  - AOV = 320 INR | Gross Margin (18%) = 57.6 INR | Delivery Fee = 15 INR | Total Revenue = 72.6 INR.
  - Picking & Packing Cost = 20 INR | Rider Payout = 50 INR | Dark Store Rent/Overhead = 24.6 INR | Total Cost = 94.6 INR.
  - Net Profit per Order = $72.6 - 94.6 = -\mathbf{22	ext{ INR}}$.
- **Turnaround Plan**:
  1. *Expand AOV from 320 to 420 INR*: Introduce high-margin bakery/dairy cross-sell bundles (adds +18 INR gross profit).
  2. *Batch Nearby Deliveries*: Batch 1.3 orders per rider run via geohash clustering (cuts rider cost from 50 to 38 INR).
  3. *New Unit Economics*: Revenue = 95 INR | Costs = 82 INR $\implies$ **Net Profit = +13 INR per order**.

---

## Case 3: Food Delivery Subscription (Gold/Pro) Cannibalization
- **Prompt**: *"After launching free delivery on all orders over 199 INR for subscription members, total platform contribution margin declined 12%. Analyze the cannibalization."*
- **Analysis**:
  - Order frequency increased 25%, but AOV collapsed from 450 INR to 210 INR as users split single multi-item orders into multiple micro-orders.
  - Platform absorbed 35 INR delivery cost on 210 INR orders with only 31.5 INR gross take-rate, generating negative contribution margin per order.
- **Recommendation**:
  - Raise free delivery threshold from 199 INR to 299 INR for subscription members to restore healthy basket density.

---

## Case 4: FinTech Credit Card Approval Rate Optimization
*(Detailed analysis balancing credit risk scorecards, marginal approval expansion, and 90-day default provisioning).*

---

## Case 5: SaaS Enterprise Net Revenue Retention (NRR) Decay
*(Diagnosing cohort decay in mid-market accounts due to customer success onboarding delays).*

---

## Case 6: Ride-Hailing Airport Surge Pricing & ETA Balancing
*(Optimizing driver queue staging algorithms to eliminate passenger wait-time spikes).*

---

## Case 7: OTT Streaming Platform AVOD Ad Load Optimization
*(Balancing ad impressions per hour against 30-day viewer churn).*

---

## Case 8: B2B E-Commerce Marketplace RTO Reduction
*(Implementing automated address verification and OTP confirmation for high-risk COD orders).*

---

## Case 9: Ed-Tech Free Trial Funnel Drop-off Diagnosis
*(Optimizing Day-1 onboarding engagement to double 7-day course completion rates).*

---

## Case 10: Digital Payments Merchant Churn Analysis
*(Isolating soundbox hardware failure rates causing offline merchant switching).*
