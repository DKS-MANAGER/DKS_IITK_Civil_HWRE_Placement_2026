# 01 — Preparation Strategy & Roadmap
## High-Yield Study Architecture, Skill Allocation & Time Optimization

> **Document Status**: Strategic Study Planning Guide `[TIER 5 / PEDAGOGICAL FRAMEWORK]`  
> **Target Role**: Data Scientist / Associate Data Scientist | Tredence Analytics  
> **Candidate Background**: M.Tech Civil Engineering (HWRE), IIT Kanpur · B.Tech Civil Engineering

---

## 1. Core Preparation Philosophy

Preparing for Tredence as an engineering postgraduate requires balancing two simultaneous demands:
1. **The Technical Elimination Threshold**: Passing the competitive online screening test and Round 1 live coding, which rigorously test **Python syntax**, **Pandas manipulation**, **Advanced SQL windowing**, and **applied Statistics**.
2. **The Consulting & Decision Intelligence Differentiator**: Excelling in technical and case interviews by demonstrating the **"Now What?"** — connecting mathematical models (e.g., LightGBM, SARIMA, TreeSHAP) to measurable business outcomes (reducing out-of-stock rates, optimizing promotion spend, preventing churn).

```
┌────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                              THE 3-PILLAR TREDENCE PREPARATION STRATEGY                                │
├───────────────────────────────────┬───────────────────────────────────┬────────────────────────────────┤
│ Pillar 1: Code & Query Fluency    │ Pillar 2: Algorithmic Foundations │ Pillar 3: Business "Now What?" │
├───────────────────────────────────┼───────────────────────────────────┼────────────────────────────────┤
│ • Vectorized NumPy & Pandas       │ • Mathematical loss functions     │ • Issue Trees (MECE)           │
│ • Production SQL window queries   │ • Bias-variance & cross-validation│ • Revenue & EBITDA metrics     │
│ • Zero syntax hesitation on screen│ • TreeSHAP explainability         │ • Executive slide storylining  │
└───────────────────────────────────┴───────────────────────────────────┴────────────────────────────────┘
```

---

## 2. Topic Priority Matrix

Topics are partitioned into three distinct tiers to ensure optimal return on study time:

### Tier P0 (Absolute Core — 65% of Focus)
*Must be mastered to perfection. Any failure here leads to immediate elimination.*
- **SQL Analytics**: Advanced joins, subqueries, Common Table Expressions (CTEs), window functions (`ROW_NUMBER`, `DENSE_RANK`, `LAG`, `LEAD`, moving averages), conditional aggregation (`CASE WHEN`).
- **Python Data Stack**: NumPy vectorization and broadcasting, Pandas indexing, group-by aggregations, missing value imputation, type downcasting, Scikit-learn pipelines.
- **Statistical Inference**: Hypothesis testing ($z$-test, $t$-test, Chi-square, ANOVA), $p$-values, Type I/II errors, statistical power, Central Limit Theorem, confidence intervals.
- **Supervised ML Core**: Linear regression assumptions, Logistic regression loss function, Decision tree splitting criteria (Gini/Entropy), Ensemble methods (Random Forest, XGBoost, LightGBM).
- **Model Evaluation**: ROC-AUC vs PR-AUC (critical for class imbalance), Confusion matrix, precision, recall, F1-score, calibration curves.
- **Candidate Research Defense**: Verbatim translation of candidate's ML infrastructure risk prediction and hydrological time-series modeling into commercial data science language.

### Tier P1 (High Yield & Consulting Differentiator — 25% of Focus)
*Distinguishes the candidate from standard coding candidates during Round 2 and Senior Director interviews.*
- **Time-Series & Forecasting**: Stationarity (ADF test), ACF/PACF, ARIMA/SARIMA, rolling-window out-of-time validation, retail demand forecasting metrics (MAE, RMSE, WAPE).
- **Business Experimentation & A/B Testing**: Sample size calculation formula, Minimum Detectable Effect (MDE), variance reduction via CUPED, network spillover in retail testing.
- **Explainable AI (XAI)**: Cooperative game theory foundations of Shapley values, TreeSHAP mechanics, interpreting local vs global feature importance.
- **Business Problem Framing**: Translating ambiguous business problems into mathematical objective functions and operational recommendations.

### Tier P2 (Extended JD Breadth — 10% of Focus)
*Required for conceptual fluency when discussing modern AI capabilities.*
- **Enterprise GenAI & RAG**: Vector embeddings, cosine similarity, chunking strategies, hybrid retrieval (dense + sparse BM25), reranking, hallucination metrics (Ragas).
- **Deep Learning Fundamentals**: Backpropagation, activation functions (ReLU, Sigmoid), CNNs, LSTM/GRU, Transformers (Self-Attention mechanism).
- **Graph & Recommender Systems**: Collaborative filtering (user-user, item-item, matrix factorization SVD), cold-start problem, Node2Vec intuition.
- **Prescriptive Analytics**: Linear programming (LP), mixed-integer linear programming (MILP), optimization under constraints using `scipy.optimize`.
