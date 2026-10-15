# Consulting Formula Reference Sheet

> **Document Type**: High-Density Quantitative Formula Reference for Live Case Interviews.  
> **Usage**: Rapid formula lookup and test-eve review.

---

## 1. Profitability & Unit Economics

| Metric | Exact Formula | Notes & Traps |
| :--- | :--- | :--- |
| **Gross Margin %** | $\frac{P - VC_{\text{unit}}}{P} \times 100\%$ | Based on selling price ($P$), NOT cost ($C$). |
| **Markup %** | $\frac{P - C}{C} \times 100\%$ | Based on unit cost ($C$). $\text{Margin} = \frac{\text{Markup}}{1 + \text{Markup}}$. |
| **EBIT Margin %** | $\frac{\text{Operating Profit}}{\text{Revenue}} \times 100\%$ | Measures core operational earning power. |
| **EBITDA** | $\text{EBIT} + \text{Depreciation} + \text{Amortization}$ | Operating cash profitability proxy. |
| **Contribution Margin ($CM$)**| $P - VC_{\text{unit}}$ | Dollars available to cover fixed overhead. |
| **Break-Even Volume ($Q^*$)** | $\frac{\text{Fixed Overhead}}{P - VC_{\text{unit}}}$ | In units produced and sold. |
| **Operating Leverage (DOL)**| $\frac{\% \Delta \text{EBIT}}{\% \Delta \text{Revenue}} = \frac{Q \times CM}{\text{EBIT}}$ | High fixed costs amplify profit sensitivity. |

---

## 2. Growth, Compounding & Estimation

| Metric | Formula | Heuristic / Boundary Limit |
| :--- | :--- | :--- |
| **CAGR** | $\left(\frac{V_{\text{final}}}{V_{\text{initial}}}\right)^{1/n} - 1$ | Use Rule of 72 for doublings. |
| **Rule of 72** | $\text{Doubling Years} \approx \frac{72}{\text{Growth Rate \%}}$ | Accurate for rates between $4\%$ and $18\%$. |
| **Price Elasticity ($E_d$)** | $\frac{\% \Delta Q}{\% \Delta P}$ | If $|E_d| < 1$, raise price to expand revenue. |
| **Volume Effect** | $(Q_2 - Q_1) \times \bar{P}_1$ | Change in volume at baseline weighted price. |
| **Price Effect** | $\sum Q_{i, 2} \times (P_{i, 2} - P_{i, 1})$ | Change in price on actual new volumes. |
| **Mix Effect** | $Q_2 \times \sum P_{i, 1} \times (\text{Mix}_{i, 2} - \text{Mix}_{i, 1})$ | Customer migration between product tiers. |

---

## 3. Operations & Queueing Economics

| Concept | Mathematical Equation | Application Context |
| :--- | :--- | :--- |
| **Little's Law** | $L = \lambda \times W$ | $L = \text{WIP/Inventory}$, $\lambda = \text{Throughput}$, $W = \text{Cycle Time}$. |
| **Overall Equipment Effectiveness (OEE)**| $\text{Availability} \times \text{Performance} \times \text{Quality}$ | World-class benchmark is $\ge 85\%$. |
| **Economic Order Quantity (EOQ)**| $\sqrt{\frac{2 \times D \times S}{H}}$ | $D = \text{Demand}$, $S = \text{Order Cost}$, $H = \text{Holding Cost}$. |
| **Safety Stock ($SS$)** | $Z \times \sqrt{\bar{L}\sigma_D^2 + \bar{D}^2\sigma_L^2}$ | Incorporates both demand and lead-time variance. |
| **Cash Conversion Cycle (CCC)** | $DSO + DIO - DPO$ | Days cash is tied up in operating working capital. |

---

## 4. Valuation, Finance & LTV

| Metric | Mathematical Equation | Benchmark |
| :--- | :--- | :--- |
| **Customer Lifetime Value (LTV)** | $\frac{\text{Annual Contribution} \times (1 - \text{Churn})}{d + \text{Churn}}$ | Include discount rate $d$ for enterprise contracts. |
| **LTV / CAC Ratio** | $\frac{\text{LTV}}{\text{CAC}}$ | Target $\ge 3.0\times$ for venture/growth stage. |
| **CAC Payback Period** | $\frac{\text{CAC}}{\text{Monthly Gross Margin per Account}}$ | Target $\le 12\text{ months}$. |
| **Economic Value Added (EVA)** | $\text{Invested Capital} \times (\text{ROIC} - \text{WACC})$ | Value created above cost of capital hurdle. |
| **DuPont Identity (ROE)** | $\text{Net Profit Margin} \times \text{Asset Turnover} \times \text{Financial Leverage}$ | Deconstructs drivers of Return on Equity. |
