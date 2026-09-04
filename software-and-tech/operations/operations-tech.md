# ⚙️ Operations / Supply Chain Technology

> **Target:** Operations Analyst, Supply Chain Analyst, Planning, Procurement, Project Controls, Business Operations
> **Covers Excel, Power BI, SQL, Python, optimization, simulation, ERP concepts, and quantitative modelling.**

---

## Priority Stack

| Tool | Tag | Level | Purpose |
|:-----|:----|:------|:--------|
| Excel | `[MUST LEARN]` | L3 | Data analysis, modelling, optimization |
| Power BI | `[HIGH ROI]` | L2–L3 | Dashboards, KPI reporting |
| SQL | `[HIGH ROI]` | L2–L3 | Querying operational data |
| Python | `[ROLE DEPENDENT]` | L2 | Advanced analysis, optimization |
| ERP concepts | `[ROLE DEPENDENT]` | L1–L2 | Understanding SAP, Oracle ERP |
| Project management tools | `[ROLE DEPENDENT]` | L2 | Jira, Asana, MS Project |

---

## Role Mapping

### Operations Analyst

| Tool | Tag | Level | Purpose |
|:-----|:----|:------|:--------|
| Excel | `[MUST LEARN]` | L3 | Process analysis, KPIs |
| Power BI | `[MUST LEARN]` | L2–L3 | Dashboards, reporting |
| SQL | `[HIGH ROI]` | L2 | Querying operational data |
| Python | `[ROLE DEPENDENT]` | L2 | Process optimization |

### Supply Chain Analyst

| Tool | Tag | Level | Purpose |
|:-----|:----|:------|:--------|
| Excel | `[MUST LEARN]` | L3 | Inventory, demand forecasting |
| SQL | `[MUST LEARN]` | L2–L3 | Supply chain data |
| Power BI | `[HIGH ROI]` | L2 | Supply chain dashboards |
| Python | `[ROLE DEPENDENT]` | L2 | Forecasting, optimization |
| ERP (SAP) | `[ROLE DEPENDENT]` | L1–L2 | Understanding ERP workflows |

### Planning / Procurement

| Tool | Tag | Level | Purpose |
|:-----|:----|:------|:--------|
| Excel | `[MUST LEARN]` | L3 | Planning, forecasting |
| ERP (SAP) | `[ROLE DEPENDENT]` | L1–L2 | Procurement workflows |
| Power BI | `[HIGH ROI]` | L2 | Spend analysis, dashboards |

### Project Controls

| Tool | Tag | Level | Purpose |
|:-----|:----|:------|:--------|
| Excel | `[MUST LEARN]` | L3 | Earned value, cost analysis |
| Primavera P6 | `[ROLE DEPENDENT]` | L2 | Scheduling |
| Power BI | `[HIGH ROI]` | L2 | KPI dashboards |

### Business Operations

| Tool | Tag | Level | Purpose |
|:-----|:----|:------|:--------|
| Excel | `[MUST LEARN]` | L3 | Business analysis |
| SQL | `[HIGH ROI]` | L2 | Data querying |
| Power BI | `[HIGH ROI]` | L2 | Reporting |
| Python | `[ROLE DEPENDENT]` | L2 | Automation, analysis |

---

## Quantitative Modelling

### Inventory Management

```
EOQ (Economic Order Quantity):
    EOQ = √(2DS/H)
    where D = annual demand, S = ordering cost, H = holding cost

Safety Stock:
    SS = Z × σ_d × √L
    where Z = service level factor, σ_d = demand std dev, L = lead time

Reorder Point:
    ROP = d × L + SS
    where d = daily demand, L = lead time
```

### Demand Forecasting

```
Moving Average:  MA = (Σ demand over n periods) / n
Exponential Smoothing:
    F(t+1) = α·D(t) + (1-α)·F(t)
    where α = smoothing constant (0 < α < 1)

Linear Regression:  y = a + bx (trend forecasting)
```

### Optimization

```
Linear Programming (Excel Solver):
    Maximize: Z = c₁x₁ + c₂x₂ + ...
    Subject to: constraints (resource limits, demand)

Transportation Problem:
    Minimize total shipping cost
    Subject to: supply and demand constraints
```

### Simulation

```
Monte Carlo Simulation:
    1. Define uncertain variables and distributions
    2. Generate random samples
    3. Run model many times
    4. Analyze distribution of outcomes

Use case: Demand uncertainty, lead time variability, risk analysis
```

---

## ERP Concepts

```
What is ERP?
    Enterprise Resource Planning — integrated software for managing
    business processes (finance, HR, supply chain, manufacturing)

Key modules:
    - Finance / Accounting
    - Supply Chain / Procurement
    - Manufacturing / Production
    - HR / Payroll
    - Sales / CRM

Common ERP systems:
    - SAP (most common in large companies)
    - Oracle ERP
    - Microsoft Dynamics
    - NetSuite

Why it matters:
    - Operations roles interact with ERP daily
    - Understanding ERP workflows is a differentiator
    - You don't need to be an expert — just understand the concepts
```

---

## Example Project: Supply Chain Dashboard

```
Project: Inventory Optimization Dashboard
Objective: Analyze inventory data, identify slow-moving items, optimize stock levels
Tools: SQL + Excel + Power BI
Workflow:
    1. SQL: Query inventory, sales, supplier data
    2. Excel: Compute EOQ, safety stock, turnover
    3. Power BI: Build interactive dashboard
    4. Insights: Recommend stock level adjustments
Expected Output: Dashboard + optimization recommendations
Resume value: High
```

---

## Interview Questions

### Basic (101)
- What is EOQ? How do you calculate it?
- Explain the difference between supply chain and operations.
- What is a KPI? Give examples for operations.

### Practical (201)
- How do you forecast demand for a product?
- Walk me through an inventory optimization analysis.
- How do you build a KPI dashboard?

### Technical (301)
- Explain safety stock and reorder point.
- How do you handle demand uncertainty?
- What is linear programming? Give an operations example.

### Project Defense
- Show me your supply chain analysis.
- How did you validate your forecast?
- What data quality issues did you encounter?

---

## Cross-Links

| Related Section | Link |
|:----------------|:-----|
| Data/Analytics Stack | [`data/`](../data/data-analytics-stack.md) |
| SQL | [`programming/sql.md`](../programming/sql.md) |
| Non-Core Operations | [`non-core/operations/`](../../non-core/operations/operations-overview.md) |
| Non-Core Supply Chain | [`non-core/supply-chain/`](../../non-core/supply-chain/supply-chain-overview.md) |

---

*See also: [`data-analytics-stack.md`](../data/data-analytics-stack.md) for the full data stack.*
