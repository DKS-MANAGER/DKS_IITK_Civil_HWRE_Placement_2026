# Module 14: Secondary Desk Research & Evidence Triangulation

> **Document Status**: Authoritative Research Methodology `[TIER 1 / PROFORMA REQUIREMENT & TIER 4 / RESEARCH STANDARDS]`  
> **Core Focus**: Secondary Desk Research Protocols, Regulatory Database Mining (SEC 10-K, FDA, ClinicalTrials.gov), Source Evaluation Framework, and Triangulation  
> **Target Role**: Associate Consultant (Commercial Strategy Consulting)  

---

## 1. What is Secondary Desk Research in Strategy Consulting?

In commercial strategy engagements, consultants cannot always commission multi-month primary field surveys with hundreds of physicians. Clients hire IQVIA because strategy consultants can rapidly synthesize disparate public and proprietary databases into definitive commercial conclusions:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    THE FIVE-TIER SECONDARY EVIDENCE HIERARCHY               │
├────────────────────┬────────────────────────────────────────────────────────┤
│ Evidence Tier      │ Primary Authoritative Sources                          │
├────────────────────┼────────────────────────────────────────────────────────┤
│ **Tier 1: Statutory**│ • SEC Form 10-K / 10-Q filings (Audited company sales) │
│ **& Regulatory**   │ • FDA Drugs@FDA approval labels & Medical Reviews      │
│                    │ • EMA European Public Assessment Reports (EPAR)        │
│                    │ • ClinicalTrials.gov (Registered Phase I–III protocols)│
├────────────────────┼────────────────────────────────────────────────────────┤
│ **Tier 2: Clinical**│ • Peer-reviewed journals (NEJM, The Lancet, JAMA)      │
│ **Literature**     │ • Medical congress abstracts (ASCO, ESMO, AHA, ADA)    │
├────────────────────┼────────────────────────────────────────────────────────┤
│ **Tier 3: Health** │ • National cancer registries (NIH / NCI SEER database) │
│ **Registries**     │ • CDC WONDER, WHO Global Health Observatory            │
│                    │ • CMS Medicare public utilization files                │
├────────────────────┼────────────────────────────────────────────────────────┤
│ **Tier 4: Investor**│ • J.P. Morgan Healthcare Conference slide decks        │
│ **Disclosures**    │ • Quarterly earnings call transcripts (SeekingAlpha)   │
├────────────────────┼────────────────────────────────────────────────────────┤
│ **Tier 5: Industry**│ • IQVIA Institute for Human Data Science reports       │
│ **Audits**         │ • EvaluatePharma, Clarivate Cortellis databases        │
└────────────────────┴────────────────────────────────────────────────────────┘
```

---

## 2. Source Evaluation & Credibility Framework

Before any numerical figure (prevalence, market size, price) is entered into a client slide deck, it must pass a rigorous evaluation audit:

| Evaluation Dimension | Quality Benchmark | Immediate Red Flag |
| :--- | :--- | :--- |
| **1. Authority & Independence** | Official statutory filings (SEC 10-K, FDA label, peer-reviewed journals). | Unverified blog posts, sponsored PR wire news releases, Wikipedia. |
| **2. Recency & Timeliness** | Published within the last 12 to 24 months. | Market reports older than 4 years in rapidly evolving therapeutic classes. |
| **3. Methodological Rigor** | Explicitly documented sample size, statistical bounds, and clinical criteria. | Round unsourced market sizing estimates without methodology. |
| **4. Geographic Relevance** | Matched specifically to client target market (US vs EU vs Japan). | Applying US epidemiological rates directly to Asian populations. |

---

## 3. Data Triangulation: Reconciling Discrepancies

When researching ambiguous metrics (such as the addressable patient population for a rare genetic disease), different public sources frequently provide conflicting estimates:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       THE DATA TRIANGULATION PROTOCOL                       │
│                                                                             │
│ [ SOURCE A: Clinical Literature ]  ──► States 35,000 US patients             │
│ [ SOURCE B: Patient Advocacy Org ] ──► States 60,000 US patients             │
│ [ SOURCE C: Competitor SEC 10-K ]  ──► States 28,000 addressable patients    │
│                               ▼                                             │
│ TRIANGULATION ANALYSIS:                                                     │
│ • Source B includes undiagnosed / mild asymptomatic individuals.            │
│ • Source A represents total diagnosed epidemiological prevalence.           │
│ • Source C represents biomarker-confirmed, drug-eligible patients.          │
│                               ▼                                             │
│ SYNTHESIZED BASELINE FOR CLIENT MODEL:                                      │
│ Use 28,000 to 35,000 as the commercial base case, citing definitions.       │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 4. Where to Find Specific Commercial Data (Cheat Sheet)

* **Finding Competitor Historical Sales**: SEC Form 10-K Item 7 (Management's Discussion & Analysis / Product Revenue Breakdown).
* **Finding Phase III Clinical Trial Completion Dates**: Search `ClinicalTrials.gov` by NCT ID $\to$ Check "Estimated Primary Completion Date".
* **Finding FDA Approved Dosing & Side Effects**: Search `Drugs@FDA` $\to$ Download official PDF package insert $\to$ Section 2 (Dosage) and Section 6 (Adverse Reactions).
* **Finding Epidemiological Incidence & Staging**: National Cancer Institute SEER Cancer Statistics Explorer (`seer.cancer.gov`).

