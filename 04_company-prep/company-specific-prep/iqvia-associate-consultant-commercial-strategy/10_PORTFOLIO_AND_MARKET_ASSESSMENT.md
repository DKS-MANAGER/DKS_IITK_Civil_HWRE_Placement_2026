# Module 10: Portfolio Strategy & Market Assessment

> **Document Status**: Authoritative Strategy Reference `[TIER 1 / PROFORMA REQUIREMENT & TIER 2 / IQVIA CONSULTING PRACTICE]`  
> **Core Focus**: Multi-Criteria Decision Analysis (MCDA), Expected Net Present Value (eNPV), Probability of Technical Success (PTRS), and 4-Asset Pipeline Prioritization Case  
> **Target Role**: Associate Consultant (Commercial Strategy Consulting)  

---

## 1. What is Portfolio Strategy in Biopharma?

Biopharmaceutical executives manage complex pipelines of therapeutic assets spanning multiple disease indications. Because clinical development and global commercialization require immense capital (\$1B+ per Phase III launch), leadership cannot fund every internal project.

**Portfolio Strategy & Market Assessment** is the disciplined evaluation of where a company should allocate its capital, R&D resources, and commercial footprint to maximize long-term shareholder value and clinical impact:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    THE STRATEGIC PORTFOLIO EVALUATION MATRIX                │
│                                                                             │
│ Strategic Fit &    ▲                                                        │
│ Commercial Feasib. │   [ PRIORITY 2: SELECTIVE ]   [ PRIORITY 1: CORE BETS ]│
│                    │   • High capability, but      │   • Large unmet need;  │
│               High │     modest market size        │     uncontested market │
│                    │   • Niche orphan therapies    │   • Transformational   │
│                    ├───────────────────────────────┼────────────────────────┤
│                    │   [ PRIORITY 4: DIVEST / KILL]│   [ PRIORITY 3: SEED ] │
│                Low │   • Crowded market, no        │   • Massive market, but│
│                    │     clinical differentiation  │     unproven science   │
│                    │   • Low commercial return     │   • High-risk oncology │
│                    └───────────────────────────────┴────────────────────────►
│                                 Low                          High           │
│                                      Market Attractiveness                  │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Quantitative Portfolio Scoring: MCDA & Risk-Adjusted Valuation

To eliminate subjective executive bias, IQVIA consultants evaluate pipeline assets using two quantitative tools: **Multi-Criteria Decision Analysis (MCDA)** and **Expected Net Present Value (eNPV)**.

### 2.1 Multi-Criteria Decision Analysis (MCDA) Scoring Dimensions
1. **Market Attractiveness (50% Weight)**:
   * Addressable Patient Pool & 5-Year Market CAGR.
   * Magnitude of Unmet Clinical Need (Lack of effective existing standard-of-care).
   * Competitive Crowdedness & Timing of Pipeline Rivals.
   * Pricing Flexibility & Payer Access Friendliness.
2. **Internal Feasibility & Strategic Synergy (50% Weight)**:
   * **Probability of Technical & Regulatory Success (PTRS)**.
   * Commercial Sales-Force Synergy (Can our existing reps detail this drug?).
   * Manufacturing Feasibility & Cost of Goods Sold (COGS).
   * Intellectual Property (IP) Exclusivity Runway ($> 12\text{ years}$ vs $< 8\text{ years}$).

### 2.2 Expected Net Present Value (eNPV)
In drug development, future cash flows must be discounted not only by the financial cost of capital ($r$), but by the cumulative clinical probability of passing Phase III trials and FDA review:
$$\text{eNPV} = \sum_{t=0}^{T} \frac{\text{PTRS} \times \text{Net Cash Flow}_t}{(1 + r)^t} - \text{Cumulative R\&D Cost}$$
* *Benchmark PTRS Rates*: Phase II asset $\approx 15\text{–}25\%$; Phase III asset $\approx 55\text{–}65\%$; Post-filing NDA/BLA $\approx 85\text{–}90\%$.

---

## 3. End-to-End Case Study: Prioritizing a \$300M Biopharma Pipeline

### 3.1 Client Context
A mid-sized biopharma client with a **fixed \$300M capital budget** must prioritize which assets to advance into Phase III registrational trials:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       PIPELINE CANDIDATE BENCHMARKS                         │
├───────┬──────────────────────┬─────────────┬──────────┬──────────┬──────────┤
│ Asset │ Therapeutic Area     │ Phase III   │ Peak Rev │ PTRS     │ eNPV     │
│ ID    │                      │ Trial Cost  │ (Annual) │ Rate     │ (10% WACC│
├───────┼──────────────────────┼─────────────┼──────────┼──────────┼──────────┤
│ **A** │ Rare Kidney Disease  │ $75M        │ $350M    │ 70%      │ **$420M**│
│ **B** │ Type-2 Diabetes      │ $160M       │ $1,800M  │ 40%      │ **$380M**│
│ **C** │ Solid Tumor Oncology │ $140M       │ $650M    │ 55%      │ **$290M**│
│ **D** │ Rheumatoid Arthritis │ $120M       │ $400M    │ 50%      │ **$95M** │
└───────┴──────────────────────┴─────────────┴──────────┴──────────┴──────────┘
```

### 3.2 Strategic Portfolio Analysis & Recommendations
1. **Asset A (Rare Kidney Disease — Highest Strategic Priority)**:
   * *Rationale*: Exceptional capital efficiency (\$75M trial cost) and high regulatory probability ($70\%$). High pricing power (\$150k/year) in orphan disease yields the highest risk-adjusted return ($\text{eNPV} = \$420\text{M}$). **Mandatory Fund.**
2. **Asset B vs Asset C (The Capital Constraint Dilemma)**:
   * Remaining Budget after Asset A $= \$300\text{M} - \$75\text{M} = \mathbf{\$225\text{M}}$.
   * Client cannot fund both Asset B (\$160M) and Asset C (\$140M) because $\$160\text{M} + \$140\text{M} = \$300\text{M} > \$225\text{M}$.
   * *Evaluation*: While Asset B has massive peak potential (\$1.8B), diabetes is dominated by giants (Novo Nordisk, Eli Lilly), requiring a massive 500-person primary care sales force. Asset C has lower peak sales, but high oncology synergy with the client's existing hospital infrastructure.
3. **Strategic Portfolio Verdict to Board of Directors**:
   * **Fully Fund Asset A (\$75M)**: Build dedicated rare-disease franchise.
   * **Fully Fund Asset C (\$140M)**: Consolidate leadership in solid tumor oncology. Total direct spend $= \$75\text{M} + \$140\text{M} = \mathbf{\$215\text{M}}$ (within \$300M cap).
   * **Out-License / Partner Asset B**: Partner Asset B with a global pharma major in exchange for a \$150M upfront milestone and $18\%$ royalty, offloading Phase III execution costs while preserving commercial upside.
   * **Divest / Terminate Asset D**: RA market is oversaturated with cheap biosimilars; $\text{eNPV} = \$95\text{M}$ does not justify Phase III risk.

