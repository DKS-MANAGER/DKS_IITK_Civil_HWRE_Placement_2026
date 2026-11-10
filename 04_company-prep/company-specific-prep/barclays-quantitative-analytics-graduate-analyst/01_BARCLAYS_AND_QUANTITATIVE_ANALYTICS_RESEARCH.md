# Module 01 — Barclays, Quantitative Analytics & Model Monitoring Research

## 1. Corporate Profile: Barclays PLC

Founded in 1690 in London, **Barclays PLC** is one of the world's oldest and most prestigious transatlantic universal financial institutions, operating across 40+ countries with over 85,000 employees.

```
┌────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                   BARCLAYS PLC: AT A GLANCE                                            │
├───────────────────────────────────┬───────────────────────────────────┬────────────────────────────────┤
│ Founded                           │ 1690 (London, United Kingdom)     │ C.S. Venkatakrishnan (Group CEO│
├───────────────────────────────────┼───────────────────────────────────┼────────────────────────────────┤
│ Group Balance Sheet Assets        │ ~£1.5 Trillion GBP                │ High-quality liquid assets     │
├───────────────────────────────────┼───────────────────────────────────┼────────────────────────────────┤
│ Primary Operating Divisions       │ • Barclays UK (Retail/SME/Cards)  │ • Barclays International (CIB/ │
│                                   │ • Consumer, Cards & Payments (CCP)│   Wholesale/Corporate Banking) │
├───────────────────────────────────┼───────────────────────────────────┼────────────────────────────────┤
│ Global Risk & Analytics Hubs      │ London (HQ), New York, Whippany,  │ Noida (Advant/Candor), Pune,   │
│                                   │ Singapore, Hong Kong              │ Chennai (Barclays GSC India)   │
├───────────────────────────────────┼───────────────────────────────────┼────────────────────────────────┤
│ Regulatory Supervisions           │ Bank of England (Prudential       │ US Federal Reserve, OCC, EBA,  │
│                                   │ Regulation Authority - PRA / FCA) │ ECB, RBI (India operations)    │
└───────────────────────────────────┴───────────────────────────────────┴────────────────────────────────┘
```

---

## 2. The Quantitative Analytics (QA) Organization

Within Barclays, the **Quantitative Analytics (QA)** organization represents the bank’s central mathematical and modeling powerhouse. 

Historically famous for pioneering exotic derivatives pricing in Barclays Capital, QA today has expanded into a comprehensive global institution covering both valuation and balance-sheet risk:

```
┌────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                              BARCLAYS QUANTITATIVE ANALYTICS (QA) DIVISIONS                            │
├───────────────────────────────────┬───────────────────────────────────┬────────────────────────────────┤
│      1. Front Office QA           │       2. Risk QA (Credit Risk)    │    3. Treasury & Capital QA    │
├───────────────────────────────────┼───────────────────────────────────┼────────────────────────────────┤
│ • Derivatives pricing models      │ • Probability of Default (PD)     │ • Asset-Liability Management   │
│ • Volatility surface modeling     │ • Loss Given Default (LGD)        │ • Net Interest Income (NII)    │
│ • Algorithmic execution (e-FX/e-EQ│ • Exposure at Default (EAD)       │ • Stress testing & CCAR / PRA  │
│ • Counterparty credit risk (XVA)  │ • IFRS 9 Impairment & ECL models  │ • Economic capital allocation  │
└───────────────────────────────────┴───────────────────────────────────┴────────────────────────────────┘
```

---

## 3. The Dedicated Role of QA Model Monitoring

The position being recruited at IIT Kanpur sits inside **QA Model Monitoring** within **Risk QA**, based at the **Barclays Global Service Centre in Noida, India**.

### 3.1 Why Model Monitoring is Essential in Regulated Banking
Once a credit risk model (such as a mortgage scorecard or corporate rating system) is approved by regulators (PRA/EBA/Fed) and deployed into production, it cannot be left unattended:
- Macroeconomic conditions shift (inflation surges, interest rates climb, unemployment spikes).
- Borrower behavior evolves (credit card repayment patterns change, buy-now-pay-later usage expands).
- Lending policies change (underwriting criteria tighten or expand).

**If a model becomes miscalibrated or unstable without detection, the bank faces severe regulatory fines, inadequate capital reserves, or unexpected balance-sheet loan losses.**

### 3.2 The Lifecycle Distinction: Development vs. Validation vs. Monitoring vs. Governance

Candidates frequently confuse these banking risk functions during technical interviews. You must articulate the differences effortlessly:

```
┌────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                   THE 4 PILLARS OF MODEL RISK MANAGEMENT                               │
├─────────────────────┬───────────────────┬───────────────────────────────┬──────────────────────────────┤
│      Function       │  Organizational   │          Primary Focus        │       Key Deliverables       │
│                     │       Line        │                               │                              │
├─────────────────────┼───────────────────┼───────────────────────────────┼──────────────────────────────┤
│ 1. Model Development│ 1st Line of       │ Builds the mathematical model │ Initial development paper,   │
│    (Quant Dev)      │ Defense (QA)      │ from historical data.         │ feature selection, training. │
├─────────────────────┼───────────────────┼───────────────────────────────┼──────────────────────────────┤
│ 2. Model Validation │ 2nd Line of       │ Independent audit of model    │ Pre-implementation approval, │
│    (IMR / MRM)      │ Defense (Risk)    │ theory, math, code, and flaws.│ validation report, overlays. │
├─────────────────────┼───────────────────┼───────────────────────────────┼──────────────────────────────┤
│ 3. Model Monitoring │ 1st Line of       │ Ongoing tracking of model     │ Periodic Model Monitoring    │
│    (THIS ROLE)      │ Defense (Risk QA) │ health, drift, back-testing.  │ Packs (MMP), trigger alerts. │
├─────────────────────┼───────────────────┼───────────────────────────────┼──────────────────────────────┤
│ 4. Model Governance │ Oversight /       │ Policy compliance, committee  │ Model Inventory, approval    │
│    & Audit          │ Internal Audit    │ approvals, regulatory sign-off│ logs, audit remediation.     │
└─────────────────────┴───────────────────┴───────────────────────────────┴──────────────────────────────┘
```

---

## 4. Portfolios Monitored by the Noida QA Team

The Noida QA Model Monitoring department oversees both **Retail** and **Wholesale** portfolios across the UK, US, and European franchises:

```
┌─────────────────────────────────┬─────────────────────────────────┬─────────────────────────────────┐
│        Banking Portfolio        │        Typical Loan Types       │       Core Risk Characteristics │
├─────────────────────────────────┼─────────────────────────────────┼─────────────────────────────────┤
│ UK Retail Mortgages             │ Residential home loans, Buy-to- │ Low default rates (<1%), high   │
│                                 │ Let (BTL) mortgages             │ collateral backing (LTV < 70%). │
├─────────────────────────────────┼─────────────────────────────────┼─────────────────────────────────┤
│ Barclaycard (UK & US)           │ Unsecured revolving consumer    │ High default rates (3–6%), rapid│
│                                 │ credit card debt                │ balance fluctuations, zero coll.│
├─────────────────────────────────┼─────────────────────────────────┼─────────────────────────────────┤
│ Consumer & Personal Loans       │ Fixed-term unsecured loans,     │ Medium default rates, amortizing│
│                                 │ auto financing                  │ fixed repayment schedules.      │
├─────────────────────────────────┼─────────────────────────────────┼─────────────────────────────────┤
│ Business Banking & SME Lending  │ Small-and-medium enterprise     │ Hybrid scoring (owner credit +  │
│                                 │ working capital facilities      │ business cash flows).           │
├─────────────────────────────────┼─────────────────────────────────┼─────────────────────────────────┤
│ Large Corporate & Wholesale     │ Term loans, syndicated debt,    │ Low default volume, high dollar │
│                                 │ revolving credit facilities     │ exposure (EAD), rating agencies.│
└─────────────────────────────────┴─────────────────────────────────┴─────────────────────────────────┘
```

---

## 5. Career Progression for BA4 Graduate Analysts

```
Graduate Analyst (BA4)
  │ (18 – 24 months of rigorous model monitoring, Python automation, back-testing)
  ▼
Analyst (BA3)
  │ (Deep domain ownership of specific portfolios, e.g. Barclaycard or Wholesale PD)
  ▼
Assistant Vice President (AVP / BA2)
  │ (Leading monitoring workstreams, designing new monitoring methodologies, committee presentations)
  ▼
Vice President (VP)
  │ (Accountable Model Owner / Monitoring Lead, direct interactions with PRA/EBA regulators)
  ▼
Director (D) & Managing Director (MD)
  │ (Global Head of Risk Quantitative Analytics / Model Risk)
```

