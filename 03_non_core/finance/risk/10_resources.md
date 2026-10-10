# 10. Risk Analytics: Curated References & Learning Resources

> Authoritative textbooks, regulatory standards, model risk management guidelines, and data sandboxes for IIT Kanpur students targeting quantitative risk management and credit analytics roles.
> 
> *All resources listed below are evaluated for mathematical rigor, compliance relevance, and applicability to risk analytics interviews ([OTHER CREDIBLE SOURCE]).*

---

## 1. Foundational Textbooks & Academic Treatises

### 1.1 Market Risk & Quantitative Derivatives
1. **Risk Management and Financial Institutions** (John C. Hull, University of Toronto)
   - *Why it matters*: The definitive textbook on market risk, parametric and historical Value at Risk (VaR), Expected Shortfall (ES), credit default swaps (CDS), and Basel capital accords.
   - *Best for*: Mastering VaR calculation methods, volatility modeling (EWMA/GARCH), and stress testing scenarios.
2. **Options, Futures, and Other Derivatives** (John C. Hull)
   - *Why it matters*: Standard reference for derivative pricing, Greeks ($\Delta, \Gamma, \Theta, \mathcal{V}, \rho$), and interest rate risk modeling.

### 1.2 Credit Risk Modeling & Retail Scorecards
1. **Credit Risk Scorecards: Developing and Implementing Intelligent Credit Scoring** (Naeem Siddiqi, SAS Institute)
   - *Why it matters*: The industry benchmark for developing application and behavioral credit scorecards. Explains Weight of Evidence (WoE), Information Value (IV), coarse classing, rejected applicant inference, and scorecard scaling points.
   - *Best for*: Technical interview rounds at Citi, American Express, Capital One, and retail banking analytics teams.
2. **The Basel Handbook: A Guide for Financial Practitioners** (Michael Ong)
   - *Why it matters*: In-depth explanation of the Foundation and Advanced Internal Ratings-Based (IRB) approaches for calculating Probability of Default (PD), Loss Given Default (LGD), and Exposure at Default (EAD).

---

## 2. Official Regulatory Guidelines & Model Risk Standards

1. **Federal Reserve SR 11-7 / OCC Bulletin 2011-12: Guidance on Model Risk Management**
   - *Official Reference*: [Board of Governors of the Federal Reserve System — SR 11-7](https://www.federalreserve.gov/supervisionreg/srletters/sr1107.htm)
   - *Why it matters*: The universally accepted regulatory framework governing Model Risk Management (MRM). Outlines requirements for model development, independent model validation, conceptual soundness, data lineage, and ongoing monitoring.
   - *Crucial for*: Model validation and quantitative risk associate interviews.
2. **Basel Committee on Banking Supervision (BCBS) Standards**
   - *Official Portal*: [Bank for International Settlements (BIS)](https://www.bis.org/bcbs/)
   - *Key Documents*:
     - **BCBS 239**: Principles for Effective Risk Data Aggregation and Risk Reporting.
     - **BCBS Basel III**: Capital adequacy framework (Minimum Capital Requirements, Capital Conservation Buffer, Countercyclical Capital Buffer).
     - **FRTB (Fundamental Review of the Trading Book)**: Standardized and internal models approaches for market risk replacing Basel II.5.
3. **Reserve Bank of India (RBI) Master Directions**
   - *Official Portal*: [RBI Notifications & Regulatory Framework](https://www.rbi.org.in/)
   - *Key Directions*:
     - Master Direction on Prudential Norms on Income Recognition, Asset Classification and Provisioning pertaining to Advances (IRAC Norms).
     - Master Direction on Basel III Capital Regulations for Indian Scheduled Commercial Banks.

---

## 3. Computational Tooling & Open-Source Python Libraries

1. **OptBinning (Python Library)**
   - *Repository*: `pip install optbinning` / [GitHub optbinning](https://github.com/guillermo-navas-palencia/optbinning)
   - *Why it matters*: Production-grade library for optimal binning, monotonic WoE calculation, and automated constraint satisfaction for credit scoring.
2. **Statsmodels & Scikit-Learn**
   - `statsmodels.api.Logit`: Used for statistical inference, p-values, and odds ratios in default prediction.
   - `sklearn.metrics`: For evaluating ROC-AUC, Precision-Recall curves, Brier score calibration, and confusion matrices.
3. **Public Credit Risk Benchmark Datasets**
   - **Home Credit Default Risk** (Kaggle Benchmark): Real-world anonymized credit application dataset with complex relational tables, ideal for scorecard and GBDT credit modeling.
   - **German Credit Dataset** (UCI Machine Learning Repository): Classic benchmark dataset for evaluating WoE, logistic regression, and cost-sensitive classification.

---

## 4. Cross-Repository Preparation Links
- 📖 [Master Finance & Risk Hub](../README.md)
- 📖 [Risk Domain Knowledge](03_domain-knowledge.md)
- 📖 [Risk Tools & Technical Stack](04_tools-and-technical.md)
- 📖 [Risk High-Yield Question Bank](06_question-bank.md)
- 📖 [Risk Practice Cases](07_practice-and-cases.md)
- 📖 [Risk Mock Assessment](12_mock-assessment.md)
- 📖 [General Finance Curriculum](../../finance/finance/README.md)
