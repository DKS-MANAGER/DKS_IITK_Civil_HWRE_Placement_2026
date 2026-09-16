# Master Placement Mock System & Assessment Architecture

> **Domain:** Full-Scale Aptitude Examination & Corporate Placement Simulation · **Target:** IIT Kanpur Postgraduate Placements 2026  
> **Benchmark Standards:** McKinsey & Company, The Boston Consulting Group (BCG), Bain & Company, Goldman Sachs (Quant / Strats / IB), WorldQuant, Morgan Stanley, Google (PM / Strategy), and Core Engineering PSUs  
> **Mock Suite Inventory:** 7 Standardized Full Placement Mocks (360+ Placement Questions across Progressive Calibers)  
> **Assessment Philosophy:** Interleaved Testing (No in-test difficulty labels) · Strict Negative Marking ($-0.25$ / $-0.33$) · Sector-Specific Percentile Mapping · Comprehensive Distractor Audits

---

## 1. Executive Examination Protocol & Test Architecture

A genuine corporate placement mock test is not merely a collection of topic exercises; it is a **high-pressure cognitive diagnostic system** that evaluates speed, precision, constraint prioritization, and strategic elimination under tight temporal constraints.

```
+----------------------------------------------------------------------------------------------------+
|                                THE THREE-TIER PLACEMENT TESTING SYSTEM                             |
+--------------------------+------------------------------------------+------------------------------+
| Testing Tier             | Target Scope & Architecture              | Primary Pedagogical Function |
+--------------------------+------------------------------------------+------------------------------+
| Layer 1: Topic Tests     | 15–20 Questions per Topic                | Fine-grained skill diagnosis |
| (aptitude/tests/topic/)  | Cat-8 Cognitive Hierarchy                | and formula mastery.         |
+--------------------------+------------------------------------------+------------------------------+
| Layer 2: Sectional Tests | 25–30 Questions Timed (30–40 min)        | Speed pacing across broad    |
| (aptitude/tests/section/)| Quant, Reasoning, DI, Verbal             | domain categories.           |
+--------------------------+------------------------------------------+------------------------------+
| Layer 3: Full Mocks      | 50–60 Questions Timed (60–75 min)        | Exact corporate recruitment  |
| (aptitude/mocks/)        | Interleaved Multi-Domain Mock Suite      | simulation with negative mk. |
+--------------------------+------------------------------------------+------------------------------+
```

---

## 2. Progressive Mock Suite Inventory

| Mock File | Benchmark Caliber | Target Difficulty Distribution | Target Time & Qs | Primary Target Sector |
|:---|:---|:---|:---:|:---|
| [**Mock 01**](full-placement-mock-01.md) | Baseline Diagnostic | 20% Found, 40% Inter, 30% Hard, 10% V.Hard | 60 min · 50 Qs | Universal Diagnostic / Initial Screening |
| [**Mock 02**](full-placement-mock-02.md) | Standard Corporate | 10% Found, 30% Inter, 40% Hard, 20% V.Hard | 60 min · 50 Qs | Big Tech (Google/Amazon), Analytics MNCs |
| [**Mock 03**](full-placement-mock-03.md) | Competitive Placement | 10% Inter, 40% Hard, 35% V.Hard, 15% Expert | 60 min · 50 Qs | Management Consulting (Bain/Kearney) |
| [**Mock 04**](full-placement-mock-04.md) | IITK High-Bar Flagship | 30% Hard, 45% V.Hard, 20% Expert, 5% Trap | 60 min · 50 Qs | Elite Strategy (McKinsey, BCG, GS Strats) |
| [**Mock 05**](full-placement-mock-05.md) | Expert Mixed Suite | 20% Hard, 40% V.Hard, 30% Expert, 10% Extreme | 60 min · 50 Qs | Quant Finance & Proprietary Trading Desks |
| [**Hard Mock 01**](hard-placement-mock-01.md) | High-Pressure Selective | 25% Hard, 45% V.Hard, 25% Expert, 5% Trap | 75 min · 60 Qs | Day-1 Shortlisting (Goldman/WorldQuant) |
| [**Expert Mock 01**](expert-placement-mock-01.md) | Extreme Multi-Caselets | 20% V.Hard, 50% Expert, 30% Industrial Caselet | 60 min · 50 Qs | Senior Quant / Executive Strategy Caselets |

---

## 3. Standardized Scoring Rubric & Negative Marking Rules

Every mock in this repository utilizes standardized institutional scoring:
- **Correct Answer:** $+1.00$ Mark
- **Incorrect Answer:** $-0.25$ Mark (Standard) or $-0.33$ Mark (High-Selectivity)
- **Unattempted Question:** $0.00$ Marks

### Raw Score to IIT Kanpur Percentile Translation Matrix

For a standard **50-Question / 60-Minute Mock Test**:

```
+-----------------------------------------------------------------------------------+
| RAW SCORE (Out of 50) | PERCENTILE BRACKET | TARGET CORPORATE SHORTLISTING TIER   |
+-----------------------+--------------------+--------------------------------------+
| 42.50 – 50.00         | 99.5th+ Percentile | Goldman Sachs Quant, WorldQuant,     |
|                       |                    | McKinsey & Co., BCG Senior Associate |
+-----------------------+--------------------+--------------------------------------+
| 36.00 – 42.25         | 95.0th – 99.0th    | Bain & Co., Google PM, Morgan Stanley|
|                       |                    | Tier-1 Analytics, ITC Management     |
+-----------------------+--------------------+--------------------------------------+
| 30.00 – 35.75         | 85.0th – 94.0th    | Amazon SDE/BI, Unilever Commercial,  |
|                       |                    | Core PSUs (IOCL, ONGC, HPCL)         |
+-----------------------+--------------------+--------------------------------------+
| 22.00 – 29.75         | 70.0th – 84.0th    | Standard Tech MNCs & Large IT Ops    |
+-----------------------+--------------------+--------------------------------------+
| < 22.00               | Below 70th         | Critical Gap: Diagnostic Remediate   |
+-----------------------+--------------------+--------------------------------------+
```

---

## 4. Cognitive Error Classification Framework

After completing any mock test, classify every missed mark into one of four fatal error categories:

```
+-----------------------------------------------------------------------------------+
|                        THE 4-QUADRANT ERROR DIAGNOSTIC MATRIX                     |
+-----------------------------------------------------------------------------------+
| 1. Conceptual Gap (Type C)  : Did not know the governing formula, theorem, or    |
|                              structural grammar rule.                             |
| 2. Calculation Slip (Type A): Formulated the correct algebraic equation but made  |
|                              an arithmetic or sign error during evaluation.       |
| 3. Strategic Trap (Type T)  : Fell for an engineered distractor (e.g., base       |
|                              inversion, scope shift, unstated assumption).        |
| 4. Temporal Panic (Type P)  : Rushed under the final 10-minute clock or mismanaged|
|                              time on a multi-variable time sink.                  |
+-----------------------------------------------------------------------------------+
```

---

## 5. Strategic Test Pacing Heuristics (The 3-Pass Strategy)

```
Pass 1 (0 to 25 min)  : Sweep the test. Solve all direct 30-45 sec questions 
                        (Percentages, Direct Syllogisms, Grammar, Direct Series).
                        Target: 22-25 questions banked with 100% accuracy.

Pass 2 (25 to 50 min) : Execute structured multi-step problems (Tabular DI, 
                        Multi-constraint Seating Arrangements, Critical Reasoning,
                        Partnership Waterfalls, Permutations).
                        Target: 15-18 questions banked.

Pass 3 (50 to 60 min) : Tackle high-yield caselets or verify high-risk borderline 
                        attempts. Strictly avoid blind guessing under -0.25 penalty.
```
