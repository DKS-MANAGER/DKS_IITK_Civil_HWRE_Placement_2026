# Module 04 — Banking & Credit Risk Fundamentals

Credit risk represents the single largest risk on a commercial bank's balance sheet. In Quantitative Analytics at Barclays, understanding how credit risk is defined, structured, and quantified across retail and wholesale portfolios is the fundamental prerequisite for all model monitoring activities.

---

## 1. Defining Credit Risk, Delinquency & Default

**Credit Risk** is the risk of financial loss arising from a borrower or counterparty failing to meet contractual debt obligations (interest payments, principal amortization) in accordance with agreed terms.

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                              THE DELINQUENCY-TO-DEFAULT TIMELINE                       │
├───────────────┬─────────────────┬─────────────────┬──────────────────┬─────────────────┤
│ Current (0 DPD│ 30 Days Past    │ 60 Days Past    │ 90+ Days Past    │ Charge-Off /    │
│ Performing)   │ Due (1–30 DPD)  │ Due (31–60 DPD) │ Due (DEFAULT)    │ Recovery        │
├───────────────┼─────────────────┼─────────────────┼──────────────────┼─────────────────┤
│ Performing    │ Early-stage     │ Mid-stage       │ Regulatory       │ Uncollectible;  │
│ Stage 1       │ delinquency     │ delinquency     │ Default (Stage 3)│ debt sale / legal│
│ 12-Month ECL  │ Stage 2 (SICR)  │ Stage 2 (SICR)  │ Lifetime ECL     │ recovery workout│
└───────────────┴─────────────────┴─────────────────┴──────────────────┴─────────────────┘
```

### 1.1 The Regulatory Definition of Default (Article 178 CRR / Basel)
Under Basel III and IFRS 9, a credit obligation is deemed in **Default** when either (or both) of the following events has occurred:
1. **The 90 Days Past Due (DPD) Objective Trigger**: The obligor is past due more than 90 consecutive days on any material credit obligation.
2. **The Unlikeliness to Pay (UTP) Subjective Trigger**: The bank considers that the obligor is unlikely to pay its credit obligations in full without recourse to actions such as realizing collateral. UTP triggers include:
   - The bank puts the credit obligation on non-accrued status.
   - The bank makes a specific credit impairment provision.
   - The bank sells the credit obligation at a material credit-related economic loss.
   - The bank consents to a distressed restructuring of the credit obligation.
   - The obligor files for bankruptcy or corporate administration.

---

## 2. The Core Expected Loss Framework

The mathematical cornerstone of modern credit risk management is the **Expected Loss (EL)** equation:

$$\mathbf{EL = PD \times LGD \times EAD}$$

```
┌───────────────────────┬────────────────────────────────────────────────────────────────────────┐
│       Component       │                              Definition                                │
├──────────────────────┼────────────────────────────────────────────────────────────────────────┤
│ Probability of        │ The statistical likelihood that an obligor will default within a given │
│ Default (PD)          │ time horizon (typically 12 months for Basel / IFRS 9 Stage 1).         │
│                       │ Measured as a percentage: $0\% \le \text{PD} \le 100\%$.               │
├──────────────────────┼────────────────────────────────────────────────────────────────────────┤
│ Loss Given Default    │ The economic loss percentage incurred if default occurs, net of all    │
│ (LGD)                 │ recovery proceeds and legal workout costs, discounted to default date. │
│                       │ Measured as a percentage: $0\% \le \text{LGD} \le 100\%$.              │
│                       │ Related to Recovery Rate: $\text{LGD} = 1 - \text{Recovery Rate}$.     │
├──────────────────────┼────────────────────────────────────────────────────────────────────────┤
│ Exposure at Default   │ The gross dollar/sterling amount the bank is exposed to at the moment  │
│ (EAD)                 │ of default (drawn balance + proportion of undrawn commitments).        │
│                       │ Measured in currency units (e.g., £ GBP or $ USD).                     │
└──────────────────────┴────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Expected Loss (EL) vs. Unexpected Loss (UL)

Understanding the distinction between EL and UL explains why banks maintain both **Impairment Provisions** and **Regulatory Capital Reserves**:

```
     Probability
      Density
         │
         │         Expected Loss (EL)
         │        ┌───────┴───────┐
         │        │               │         Unexpected Loss (UL)
         │        │               │     ┌─────────────┴─────────────┐
         │        │               │     │                           │
         │       ▲│               │     │                           │
         │      ╱ │╲              │     │                           │
         │     ╱  │ ╲             │     │                           │
         │    ╱   │  ╲            │     │                           │
         │   ╱    │   ╲           │     │                           │
         │  ╱     │    ╲          │     │                           │
         │ ╱      │     ╲         │     │                           │
         │╱       │      ╲        │     │                           │
         └────────┴───────┴───────┴─────┴───────────────────────────┴────── Credit Loss ($)
                 Mean Loss               99.9% VaR Threshold         Catastrophic
              (Covered by P&L             (Covered by Tier 1          Tail Risk
                Provisions)                 Equity Capital)         (Risk Appetite)
```

```
┌─────────────────────────────────┬─────────────────────────────────┬─────────────────────────────────┐
│        Comparison Dimension     │        Expected Loss (EL)       │       Unexpected Loss (UL)      │
├─────────────────────────────────┼─────────────────────────────────┼─────────────────────────────────┤
│ Statistical Definition          │ Mean (average) loss of portfolio│ Volatility / standard deviation │
│                                 │ over a 1-year horizon: $\mu$    │ of loss around the mean: $\sigma$│
├─────────────────────────────────┼─────────────────────────────────┼─────────────────────────────────┤
│ Financial Interpretation        │ Foreseeable "cost of doing      │ Extreme tail-risk losses during │
│                                 │ business" in lending.           │ severe macroeconomic crises.    │
├─────────────────────────────────┼─────────────────────────────────┼─────────────────────────────────┤
│ Balance Sheet Treatment         │ Covered by **Impairment Reserves│ Covered by **Regulatory Capital │
│                                 │ / Provisions** on the P&L       │ (CET1 / Tier 1 Capital)** on    │
│                                 │ (IFRS 9 Expected Credit Loss).  │ the Balance Sheet (Basel RWA).  │
├─────────────────────────────────┼─────────────────────────────────┼─────────────────────────────────┤
│ Confidence Level                │ 50th percentile (central mean)  │ **99.9th percentile** over a    │
│                                 │                                 │ 1-year horizon (Basel VaR).     │
└─────────────────────────────────┴─────────────────────────────────┴─────────────────────────────────┘
```

---

## 4. Retail vs. Wholesale Credit Risk

Barclays divides its credit risk architecture into two radically different operating worlds:

```
┌─────────────────────────────────┬─────────────────────────────────┬─────────────────────────────────┐
│        Operating Dimension      │          Retail Banking         │        Wholesale Banking        │
├─────────────────────────────────┼─────────────────────────────────┼─────────────────────────────────┤
│ Core Products                   │ Residential mortgages, credit   │ Corporate loans, syndicated debt│
│                                 │ cards (Barclaycard), auto loans │ revolving lines, project finance│
├─────────────────────────────────┼─────────────────────────────────┼─────────────────────────────────┤
│ Portfolio Structure             │ Millions of accounts, small     │ Thousands of obligors, large    │
│                                 │ balances (£500 – £350,000)      │ balances (£5M – £500M+)         │
├─────────────────────────────────┼─────────────────────────────────┼─────────────────────────────────┤
│ Homogeneity                     │ Highly homogeneous; pooled into │ Highly heterogeneous; individual│
│                                 │ risk segments / score bands     │ financial statement analysis    │
├─────────────────────────────────┼─────────────────────────────────┼─────────────────────────────────┤
│ Modeling Methodology            │ Empirical statistical scorecards│ Expert judgment + quantitative  │
│                                 │ (Logistic regression, XGBoost)  │ shadow rating agency models     │
├─────────────────────────────────┼─────────────────────────────────┼─────────────────────────────────┤
│ Default Frequency               │ High default count (thousands); │ Low default count (rare events);│
│                                 │ robust statistical estimation   │ low-default portfolio (LDP) trap│
├─────────────────────────────────┼─────────────────────────────────┼─────────────────────────────────┤
│ Key Risk Drivers                │ Bureau score, DTI, LTV, past    │ Debt/EBITDA, interest coverage  │
│                                 │ payment delinquencies, tenure   │ DSCR, liquidity, industry trend │
└─────────────────────────────────┴─────────────────────────────────┴─────────────────────────────────┘
```

---

## 5. Secured vs. Unsecured Lending Dynamics

```
┌─────────────────────────────────┬─────────────────────────────────────────────────────────────┐
│         Secured Lending         │                      Unsecured Lending                      │
├─────────────────────────────────┼─────────────────────────────────────────────────────────────┤
│ Collateral Backed (e.g., Home)  │ Zero Collateral Backed (e.g., Credit Card)                  │
│ LGD is heavily driven by **LTV**│ LGD is high and relatively constant (typically 70% – 90%).  │
│ (Loan-to-Value) and house prices│ If borrower defaults, recovery is limited to debt collection│
│ If borrower defaults, bank      │ agencies, charge-off sales (at 5–15p on the pound), or      │
│ repossesses and liquidates home.│ legal wage garnishments.                                    │
│ Low LGD (typically 10% – 25%).  │ LGD model monitors charge-off curves and collection decays. │
└─────────────────────────────────┴─────────────────────────────────────────────────────────────┘
```

---

## 6. Credit Migration & Markov Transition Matrices

Credit risk models track how borrowers transition across internal rating grades over a 1-year monitoring horizon. 

Consider a simplified 4-grade master rating scale (Grade 1 = Prime, Grade 2 = Standard, Grade 3 = Subprime, Grade D = Default):

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                             1-YEAR CREDIT MIGRATION MATRIX                             │
├───────────────────┬───────────────┬───────────────┬───────────────┬────────────────────┤
│ Initial Grade     │ Grade 1 (End) │ Grade 2 (End) │ Grade 3 (End) │  Default (D) (End) │
├───────────────────┼───────────────┼───────────────┼───────────────┼────────────────────┤
│ Grade 1 (Prime)   │     92.0%     │      6.5%     │      1.2%     │       0.3%         │
├───────────────────┼───────────────┼───────────────┼───────────────┼────────────────────┤
│ Grade 2 (Standard)│      5.0%     │     82.0%     │     10.5%     │       2.5%         │
├───────────────────┼───────────────┼───────────────┼───────────────┼────────────────────┤
│ Grade 3 (Subprime)│      1.0%     │      8.0%     │     76.0%     │      15.0%         │
├───────────────────┼───────────────┼───────────────┼───────────────┼────────────────────┤
│ Default (D)       │      0.0%     │      0.0%     │      0.0%     │     100.0%         │
└───────────────────┴───────────────┴───────────────┴───────────────┴────────────────────┘
```
- **Absorbing State**: Default (D) is an absorbing state in Basel modeling ($P(D \rightarrow D) = 1.0$), meaning once a facility defaults, it remains in default for regulatory capital tracking until resolved.
- **Credit Deterioration Tracking**: In QA Model Monitoring, analysts check whether migration off-diagonals (downgrades) are accelerating compared to development benchmarks, acting as a critical **early warning indicator** of credit stress.

---

## 7. Comprehensive Worked Numerical Portfolio Calculations

### Case 1: UK Residential Mortgage Portfolio (Secured)
- **Portfolio Parameters**:
  - Total Outstanding Balance: £500,000,000 (1,000 mortgages, average £500,000).
  - 1-Year Predicted Probability of Default (PD): 0.80% ($0.008$).
  - Average Loan-to-Value (LTV): 65%.
  - House Price Index (HPI) downturn haircut: 20%.
  - Legal workout and repossession cost: £25,000 per property.
- **LGD Calculation**:
  1. Average Property Valuation = $£500,000 / 0.65 = £769,231$.
  2. Stressed Liquidation Value = $£769,231 \times (1 - 0.20) = £615,385$.
  3. Net Recoveries after £25k legal fees = $£615,385 - £25,000 = £590,385$.
  4. Since net recovery (£590,385) exceeds loan balance (£500,000), economic loss is zero on average, but accounting for conservative downturn floor: regulatory $\text{LGD} = 12.0\%$.
- **Expected Loss Calculation**:
  $$\text{EL} = \text{PD} \times \text{LGD} \times \text{EAD} = 0.008 \times 0.12 \times £500,000,000 = \mathbf{£480,000}$$
  *(Notice that despite a £500M balance, EL is only £480k due to strong collateralization).*

---

### Case 2: Barclaycard Revolving Credit Card Portfolio (Unsecured)
- **Portfolio Parameters**:
  - 100,000 active credit card accounts.
  - Total Current Drawn Balance: £200,000,000 (Average drawn £2,000).
  - Total Undrawn Available Credit Limits: £300,000,000 (Average undrawn limit £3,000).
  - Credit Conversion Factor (CCF) on undrawn lines: 60% ($0.60$).
  - 1-Year Average PD: 4.5% ($0.045$).
  - Unsecured Recovery Rate: 20% ($\text{LGD} = 1 - 0.20 = 80.0\%$).
- **EAD Calculation**:
  $$\text{EAD} = \text{Drawn Balance} + (\text{CCF} \times \text{Undrawn Limit})$$
  $$\text{EAD} = £200,000,000 + (0.60 \times £300,000,000) = £200,000,000 + £180,000,000 = \mathbf{£380,000,000}$$
- **Expected Loss Calculation**:
  $$\text{EL} = \text{PD} \times \text{LGD} \times \text{EAD}$$
  $$\text{EL} = 0.045 \times 0.80 \times £380,000,000 = \mathbf{£13,680,000}$$
  *(Unsecured credit produces an Expected Loss of £13.68M on £380M EAD—over 28× higher loss density than mortgages).*

---

### Case 3: Large Corporate Wholesale Syndicated Facility
- **Facility Parameters**:
  - Corporate Client: FTSE-100 Industrial Conglomerate.
  - Drawn Term Loan: £40,000,000.
  - Undrawn Revolving Credit Facility (RCF): £20,000,000 (CCF = 50%).
  - Internal Rating Grade: BBB- equivalent ($\text{PD} = 0.40\%$).
  - Senior Unsecured Claim (Historical senior debt recovery = 45% $\rightarrow \text{LGD} = 55\%$).
- **Calculations**:
  $$\text{EAD} = £40,000,000 + (0.50 \times £20,000,000) = £50,000,000$$
  $$\text{EL} = 0.004 \times 0.55 \times £50,000,000 = \mathbf{£110,000}$$

