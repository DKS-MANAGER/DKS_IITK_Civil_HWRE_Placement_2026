# 20 Enterprise Business Analytics Cases across Tredence Verticals

**Target Role:** Data Scientist / Associate Data Scientist | Tredence Analytics  
**Context:** IIT Kanpur Placement Season 2026–27  
**Verticals Covered:** Retail & CPG, TMT, Healthcare, Industrials & Supply Chain, Hospitality

---

## Vertical 1: Retail & Consumer Packaged Goods (CPG)

### Case 1: Fresh Produce Demand Forecasting & Spoilage Reduction
- **Business Context:** A nationwide supermarket chain suffers $\$18\text{M}$ in annual losses due to expired dairy and fresh produce while experiencing frequent weekend stockouts on top SKUs.
- **Analytical Formulation:** Quantile Regression demand forecasting at Store $\times$ SKU $\times$ Day level. Forecast the 10th, 50th, and 90th demand percentiles to inform probabilistic inventory safety stock.
- **Key Features:** Lagged 7/14/28-day sales, weather forecasts (temperature, precipitation), local events/holidays, price elasticities, promotion status.
- **Modeling Choice:** LightGBM with custom Pinball / Quantile Loss ($\tau \in \{0.10, 0.50, 0.90\}$) alongside hierarchical reconciliation (MinT).
- **Evaluation:** WAPE (volume-weighted) and Under-stock vs Over-stock Cost Loss.
- **"Now What?" Last-Mile Operationalization:** Pushes automated daily order suggestions to store ordering tablets at 5:00 AM, showing buffer margins and expected spoilage risk.

---

### Case 2: Trade Promotion Optimization (TPO) for CPG Brands
- **Business Context:** A Fortune 500 food manufacturer spends $20\%$ of gross revenue on retail trade promotions (e.g., "Buy 2 Get 1 Free" at Walmart/Target), but $65\%$ of campaigns fail to generate incremental EBITDA.
- **Analytical Formulation:** Causal Machine Learning (Uplift / Meta-Learners: C-Forest) combined with Mixed Integer Linear Programming (MILP).
- **Key Features:** Promotional discount depth, display placement (endcap vs aisle), circular ad feature, competitor promotional calendar, baseline baseline non-promo sales.
- **Modeling Choice:** Two-Model Uplift framework estimating Conditional Average Treatment Effect (CATE) + PuLP optimization solver to allocate promotion budgets across 52 weeks.
- **Evaluation:** Qini Curve, Incremental Return on Trade Investment (ROTI).
- **"Now What?":** Tredence TPO interactive simulator allowing brand managers to model promotion depth and immediately visualize predicted retailer margin vs brand margin.

---

### Case 3: Dynamic Markdown & Clearance Pricing Optimization
- **Business Context:** An apparel retailer enters the final 6 weeks of summer with excess seasonal inventory. Selling at full price causes high end-of-season write-offs; premature discounting destroys gross margins.
- **Analytical Formulation:** Non-linear dynamic programming / Multi-period price optimization under finite inventory constraint:
  $$\max_{p_1, \dots, p_T} \sum_{t=1}^T p_t \cdot d_t(p_t) \quad \text{s.t.} \quad \sum_{t=1}^T d_t(p_t) \le I_0$$
- **Key Features:** Current inventory depth, sell-through velocity, days remaining in season, competitor price ratio, historic price elasticity.
- **Modeling Choice:** Constant Elasticity Demand Model $\ln(d) = \alpha - \epsilon \ln(p)$ fit via Bayesian Ridge regression + Scipy SLSQP constrained optimizer.
- **Evaluation:** Realized gross margin dollars, End-of-season inventory clearance rate ($> 95\%$).
- **"Now What?":** Automated markdown schedules sent weekly to store tagging systems, adjusting discount stickers from $15\%$ to $30\%$ only for slow-moving store-SKU combinations.

---

### Case 4: Omnichannel Customer Churn Mitigation & Uplift Modeling
- **Business Context:** An omnichannel cosmetics brand loses $22\%$ of loyalty members annually. Mass emailing discounts to all dormant users costs millions in margin cannibalization for customers who would have purchased anyway ("Sure Things").
- **Analytical Formulation:** Uplift Modeling categorizing customers into 4 quadrants: *Persuadables, Sure Things, Lost Causes, Sleeping Dogs*. Focus interventions strictly on *Persuadables*.
- **Key Features:** Recency, Frequency, Monetary value (RFM), days since last web login, customer service complaints, email click-through rate.
- **Modeling Choice:** X-Learner using LightGBM base learners to predict individual treatment effect $\tau_i$.
- **Evaluation:** Cumulative Gain / Qini score on held-out A/B experiment.
- **"Now What?":** Marketing automation syncs with CRM; only Persuadables receive high-value promo codes, saving $\$1.2\text{M}$ in wasted promotional discounts.

---

### Case 5: Market Basket Analysis & Next-Best-Action (NBA) Engine
- **Business Context:** A B2B wholesale club wants to increase average transaction basket size and cross-sell high-margin private-label goods.
- **Analytical Formulation:** Association Rule Mining + Matrix Factorization with implicit feedback (ALS).
- **Key Features:** Co-purchase frequency, purchase sequence time intervals, customer trade industry (restaurant vs convenience store).
- **Modeling Choice:** Implicit ALS (Hu-Koren-Volinsky) on Spark + FP-Growth association rules (Support, Confidence, Lift).
- **Evaluation:** NDCG@5, Precision@5, Cross-sell Conversion Rate.
- **"Now What?":** Real-time recommendations surfaced at B2B call-center order entry and digital checkout prompts.

---

### Case 6: Computer Vision for On-Shelf Availability (OSA)
- **Business Context:** CPG beverage brand experiences $8\%$ lost sales because products are sitting in the retail store backroom instead of being replenished onto physical store shelves.
- **Analytical Formulation:** Object Detection & Visual Void Segmentation.
- **Key Features:** High-resolution RGB images from shelf-mounted cameras or handheld store auditor phones.
- **Modeling Choice:** YOLOv11 for bounding box detection of branded SKU bottles + ResNet-based empty shelf void classifier.
- **Evaluation:** Mean Average Precision (mAP@0.5), IoU, False Out-of-Stock alert rate.
- **"Now What?":** Alerts sent via push notification to store stockers' handheld devices: *"Aisle 4, Shelf 2: Brand X 1L Cola is empty on shelf; 4 cases available in backroom storage."*

---

## Vertical 2: Technology, Media & Telecom (TMT)

### Case 7: Telecom Postpaid Subscriber Churn Early Warning System
- **Business Context:** A telecom operator with $15\text{M}$ postpaid subscribers experiences $1.8\%$ monthly churn. Acquiring a new subscriber costs $\$250$; retaining an existing one costs $\$40$.
- **Analytical Formulation:** Binary classification with severe class imbalance ($1.8\%$ positive), outputting well-calibrated probabilities.
- **Key Features:** Dropped call frequency, network latency, data overage fees, customer support ticket sentiment, contract tenure, competitor promo presence.
- **Modeling Choice:** LightGBM with `scale_pos_weight` + Isotonic regression calibration + TreeSHAP for explainability.
- **Evaluation:** PR-AUC, FPV (False Positive Value), Net Retention Profitability.
- **"Now What?":** CRM dashboard shows top 3 churn drivers per account (e.g., "Frequent 5G drops in home zip code") with prescriptive remedies (e.g., complimentary network signal booster + 10GB data voucher).

---

### Case 8: B2B SaaS Enterprise Account Expansion & Upsell Propensity
- **Business Context:** Enterprise cloud software vendor wants to identify which existing mid-market clients are ready for enterprise multi-seat license upgrades.
- **Analytical Formulation:** Multi-class classification: Downsell, Flat, Expansion.
- **Key Features:** Active daily user count, license utilization percentage ($> 90\%$), API call growth rate, adoption of premium security add-on features.
- **Modeling Choice:** CatBoost classifier with ordered target encoding.
- **Evaluation:** Top-Decile Lift, Precision@100 Accounts.
- **"Now What?":** Scores automatically populate Salesforce CRM, generating sales-qualified leads (SQLs) for account executives with suggested upgrade pitch decks.

---

### Case 9: Network Traffic Anomaly & Cyber Intrusion Detection
- **Business Context:** Telecom backbone network experiences DDoS surges and routing outages causing SLA breach penalties.
- **Analytical Formulation:** Unsupervised anomaly detection on high-frequency streaming telemetry.
- **Key Features:** Packet arrival rate, byte volume variance, SYN-to-ACK ratio, entropy of destination IP addresses.
- **Modeling Choice:** Streaming Isolation Forest + Graph Neural Networks (GCN) detecting aberrant sub-graph topologies.
- **Evaluation:** Detection Latency ($< 5\text{ seconds}$), Precision at 1% False Positive Rate.
- **"Now What?":** Triggers automated SDN (Software Defined Networking) traffic rerouting and blackholing malicious IP subnets.

---

### Case 10: Video Streaming Churn & Content Recommender
- **Business Context:** An OTT streaming service suffers post-binge cancellation (users cancel immediately after watching a flagship series season).
- **Analytical Formulation:** Sequence-aware deep recommendation modeling next-item watch propensity.
- **Key Features:** Watch time completion percentage, viewing time-of-day, genre transition entropy, days since last watch.
- **Modeling Choice:** Two-Tower Deep Neural Network (User Tower + Video Item Tower) with approximate nearest neighbor (HNSW) retrieval.
- **Evaluation:** HitRate@10, Mean Reciprocal Rank (MRR), 30-day Post-Binge Retention Lift.
- **"Now What?":** Automatically generates personalized "What to Watch Next" home screen slates and push notifications 24 hours before a user completes the season finale.

---

## Vertical 3: Healthcare & Life Sciences

### Case 11: 30-Day Hospital Readmission Risk Prediction
- **Business Context:** Under CMS guidelines, hospitals face heavy federal penalties if heart failure or pneumonia patients are readmitted within 30 days of discharge.
- **Analytical Formulation:** Supervised binary risk scoring with strict explainability requirements.
- **Key Features:** Comorbidities (Charlson index), length of stay, discharge destination, medication count, blood glucose levels, prior emergency visits.
- **Modeling Choice:** XGBoost with TreeSHAP local explanations for clinical compliance.
- **Evaluation:** ROC-AUC, Sensitivity at 80% Specificity.
- **"Now What?":** Electronic Health Record (EHR) alerts discharge nurses to schedule home health visits, follow-up telehealth calls, and medication reconciliation for top-quartile risk patients.

---

### Case 12: Healthcare Insurance Fraud, Waste, and Abuse (FWA)
- **Business Context:** Health insurer processes $\$10\text{B}$ in claims annually, with an estimated $3 - 5\%$ lost to fraudulent billing schemes (upcoding, phantom billing).
- **Analytical Formulation:** Bipartite graph network analysis combined with semi-supervised anomaly detection.
- **Key Features:** Provider billing velocity, ratio of rare procedure codes to common codes, shared patient networks across multiple clinics.
- **Modeling Choice:** Graph Convolutional Networks (GCN) + Isolation Forest on provider embedding vectors.
- **Evaluation:** Audit Recovery Rate, False Accusation Rate ($< 2\%$).
- **"Now What?":** Special Investigation Unit (SIU) receives audit-ready dossiers highlighting anomalous billing clusters and sub-graph collusion rings.

---

### Case 13: Emergency Department Bed & ICU Capacity Forecasting
- **Business Context:** Urban hospital network experiences severe ER crowding and diversion due to unpredicted patient admission surges.
- **Analytical Formulation:** Multi-step multivariate time-series forecasting.
- **Key Features:** Weather forecasts, local respiratory illness trends, ambulance dispatch telemetry, historical day-of-week arrival curves.
- **Modeling Choice:** SARIMAX with exogenous epidemiological variables.
- **Evaluation:** RMSE, Peak Hour Under-prediction Error.
- **"Now What?":** Hospital staffing system dynamically adjusts on-call nurse staffing schedules 48 hours in advance.

---

## Vertical 4: Industrials, Logistics & Supply Chain

### Case 14: Predictive Maintenance for Heavy Industrial Machinery
- **Business Context:** Manufacturing plant experiences catastrophic gearbox failures costing $\$150,000$ per hour of unplanned downtime.
- **Analytical Formulation:** Remaining Useful Life (RUL) estimation using sensor degradation telemetry.
- **Key Features:** Vibration frequency harmonics (FFT spectral features), bearing temperature, motor current draw, operating hours since last overhaul.
- **Modeling Choice:** Temporal Convolutional Network (TCN) / LSTM survival regression predicting RUL in hours.
- **Evaluation:** Mean Absolute Error of RUL, False Alarm Rate per operating month.
- **"Now What?":** Automatically generates SAP maintenance work orders when predicted RUL drops below 72 operating hours.

---

### Case 15: Multi-Echelon Inventory Optimization (MEIO)
- **Business Context:** Global industrial supplier holds $\$200\text{M}$ in safety stock inventory across central warehouses, regional hubs, and local branch depots.
- **Analytical Formulation:** Non-linear stochastic programming optimizing reorder points $(s, S)$ across multi-tier networks.
- **Key Features:** Stochastic lead times, demand variance, transportation transit times, target service level ($98\%$).
- **Modeling Choice:** Simulation-optimization combining Monte Carlo lead-time simulation with gradient-based safety stock optimization.
- **Evaluation:** Total Inventory Holding Cost Reduction while preserving $\ge 98\%$ Fill Rate.
- **"Now What?":** Supply chain planners receive automated weekly reorder point adjustments in their ERP.

---

### Case 16: Last-Mile Delivery Dynamic Route & ETA Optimization
- **Business Context:** E-commerce delivery fleet suffers missed delivery windows and excessive fuel consumption.
- **Analytical Formulation:** Dynamic Vehicle Routing Problem with Time Windows (VRPTW).
- **Key Features:** Real-time GPS vehicle coordinates, live traffic congestion, historical delivery drop-off dwell times, package dimensions.
- **Modeling Choice:** Machine learning ETA regression (LightGBM) feeding into Google OR-Tools routing solver.
- **Evaluation:** On-Time Delivery Rate ($\% \pm 15\text{ mins}$), Fuel Cost per Package.
- **"Now What?":** Turn-by-turn mobile app for drivers dynamically re-orders drop sequence when unexpected traffic occurs.

---

### Case 17: Tier-2 Supplier Disruption Risk Propagation
- **Business Context:** Automotive OEM halts assembly lines because a Tier-2 semiconductor supplier shut down due to a regional factory fire.
- **Analytical Formulation:** Directed Graph Network percolation & cascade failure modeling.
- **Key Features:** Supplier single-sourcing flags, inventory buffers at each supply chain node, geographic risk indices.
- **Modeling Choice:** Graph representation learning + Monte Carlo shock simulation.
- **Evaluation:** Supply Chain Resilience Index, Bottleneck Identification Precision.
- **"Now What?":** Procurement dashboard flags high-risk single-source components and initiates automated second-source supplier onboarding.

---

## Vertical 5: Hospitality, Travel & Consumer Services

### Case 18: Dynamic Hotel Room Pricing Optimization
- **Business Context:** Luxury hotel chain with 50 properties wants to maximize Revenue Per Available Room (RevPAR).
- **Analytical Formulation:** Multi-period dynamic revenue management under stochastic booking arrivals:
  $$\max_{p} \text{RevPAR} = \text{Occupancy}(p) \times p$$
- **Key Features:** Booking window lead time, competitor published rates, local convention/concert schedules, historical booking pace curves.
- **Modeling Choice:** Elasticity-constrained gradient boosting demand model + dynamic programming policy.
- **Evaluation:** RevPAR Lift, Average Daily Rate (ADR) optimization.
- **"Now What?":** Automated price updates pushed twice daily to Central Reservation Systems (CRS) and OTA channels (Expedia, Booking.com).

---

### Case 19: Hotel & Airline Booking Cancellation Prediction
- **Business Context:** Online travel agency suffers revenue volatility due to high free-cancellation rates ($35\%$).
- **Analytical Formulation:** Supervised binary classification predicting probability of booking cancellation before check-in.
- **Key Features:** Lead time to check-in, refundable vs non-refundable rate, customer historical cancellation rate, payment method, room type.
- **Modeling Choice:** XGBoost classifier with probability calibration (Platt scaling).
- **Evaluation:** ROC-AUC, Brier Score.
- **"Now What?":** Enables targeted overbooking algorithms and selective non-refundable promo discount upsells for high cancellation risk bookings.

---

### Case 20: Guest Loyalty Tier Personalization & Rewards Optimization
- **Business Context:** Hotel loyalty program members disengage when reward redemption thresholds feel unattainable.
- **Analytical Formulation:** Multi-Armed Contextual Bandit optimizing personalized point multiplier offers.
- **Key Features:** Past stay frequency, amenity spend (dining, spa), reward point balance, travel purpose (business vs leisure).
- **Modeling Choice:** LinUCB / Thompson Sampling Contextual Bandit.
- **Evaluation:** Offer Conversion Lift, Incremental Room Nights Booked.
- **"Now What?":** Mobile guest app surfaces dynamic personalized reward challenges (e.g., "Stay 2 nights this month and earn double bonus points").
