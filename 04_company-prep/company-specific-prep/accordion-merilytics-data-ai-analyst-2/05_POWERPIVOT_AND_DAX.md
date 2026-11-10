# Module 05 — PowerPivot & DAX (Data Analysis Expressions)

## 1. PowerPivot Internal Architecture: The xVelocity Engine

When dataset volumes exceed standard Excel limits (1,048,576 rows) or require complex relational joins across multiple transaction tables, traditional Excel formulas (`VLOOKUP`, `SUMIFS`) cause workbook lag and memory crashes. 

**PowerPivot** solves this by embedding Microsoft's enterprise **xVelocity (VertiPaq) in-memory columnar database engine** directly inside Excel.

```
┌─────────────────────────────────┬─────────────────────────────────┐
│     Traditional Excel Grid      │       PowerPivot / VertiPaq     │
├─────────────────────────────────┼─────────────────────────────────┤
│ • Row-oriented storage          │ • Columnar storage engine       │
│ • Max 1,048,576 rows            │ • Handles 10M – 50M+ rows       │
│ • Full recalculation trees      │ • High in-memory compression    │
│ • Fragile VLOOKUP links         │ • Star-schema relational model  │
│ • Slow multi-condition math     │ • Dynamic DAX measure engine    │
└─────────────────────────────────┴─────────────────────────────────┘
```

### 1.1 How VertiPaq Compresses Millions of Records
1. **Columnar Storage**: Data is stored by column rather than by row. Because a single column (e.g., `Product_Category` or `Region`) contains many repeating values, compression efficiency reaches 80% to 95%.
2. **Dictionary Encoding**: Strings are replaced with compact integer keys (e.g., `"North America"` $\rightarrow 1$, `"Europe"` $\rightarrow 2$).
3. **Run-Length Encoding (RLE)**: Repeating adjacent values are stored as count pairs (e.g., twenty consecutive `1`s stored as `(1, 20)` rather than 20 separate memory addresses).

---

## 2. Dimensional Modeling & Relational Schema Design

PowerPivot models require a **Star Schema** architecture. Avoid messy spaghetti joins.

```
                         ┌───────────────────────┐
                         │      Dim_Customer     │
                         ├───────────────────────┤
                         │ Customer_ID (PK)      │
                         │ Customer_Name         │
                         │ Industry_Vertical     │
                         │ Tier_Segment          │
                         └───────────┬───────────┘
                                     │ 1
                                     │ 
                                     │ *
┌───────────────────────┐  *     ┌───┴───────────────────┐     *  ┌───────────────────────┐
│       Dim_Date        │───────►│       Fact_Sales      │◄───────│      Dim_Product      │
├───────────────────────┤        ├───────────────────────┤        ├───────────────────────┤
│ Date (PK)             │        │ Transaction_ID (PK)   │        │ Product_ID (PK)       │
│ Year                  │        │ Date (FK)             │        │ SKU_Name              │
│ Quarter               │        │ Customer_ID (FK)      │        │ Product_Category      │
│ Month_Name            │        │ Product_ID (FK)       │        │ Standard_Cost         │
│ Fiscal_Period         │        │ Units_Sold            │        │ List_Price            │
└───────────────────────┘        │ Revenue_Gross         │        └───────────────────────┘
                                 │ Discount_Amount       │
                                 └───────────────────────┘
```

### 2.1 Star Schema Best Practices
- **Fact Tables**: Contain numeric, additive measurements and foreign keys (FK). High row count (millions).
- **Dimension Tables**: Contain descriptive context, filtering attributes, and unique primary keys (PK). Lower row count (thousands).
- **Relationship Cardinality**: Relationships should always be **One-to-Many ($1:*$)** flowing from Dimension PK to Fact FK.
- **Cross-Filter Direction**: Maintain **Single-Direction** filtering (Dimension filters Fact). Avoid Bi-directional cross-filtering unless modeling complex many-to-many bridges, as bi-directional filters introduce calculation ambiguity and performance degradation.

---

## 3. Calculated Columns vs. DAX Measures

```
┌─────────────────────────────────┬─────────────────────────────────────────────────────────────┐
│        Calculated Column        │                         DAX Measure                         │
├─────────────────────────────────┼─────────────────────────────────────────────────────────────┤
│ Computed at row ingestion       │ Computed on the fly at query time                           │
│ Consumes permanent RAM storage  │ Consumes zero RAM until displayed in a PivotTable           │
│ Evaluated in Row Context        │ Evaluated in Filter Context                                 │
│ Static across filter slices     │ Dynamic: adapts instantly to slicers, rows, and columns     │
│ Example: Full_Name = [First] &  │ Example: Total_Revenue = SUM(Fact_Sales[Revenue_Gross])     │
│          " " & [Last]           │                                                             │
└─────────────────────────────────┴─────────────────────────────────────────────────────────────┘
```

> [!TIP]
> **Consulting Golden Rule**: Always prefer **DAX Measures** over Calculated Columns for numeric aggregations, profit margins, and ratios. Use Calculated Columns only when you need a new dimension to slice by in rows or columns.

---

## 4. Master DAX Functions & Common Design Patterns

### 4.1 Foundational Aggregations & Safe Division
```dax
// Total Gross Revenue
Total_Gross_Revenue := SUM(Fact_Sales[Revenue_Gross])

// Total Discount
Total_Discount := SUM(Fact_Sales[Discount_Amount])

// Net Revenue
Total_Net_Revenue := [Total_Gross_Revenue] - [Total_Discount]

// Safe Division (Prevents #DIV/0! errors when denominator is zero or blank)
Gross_Margin_Pct := DIVIDE([Total_Net_Revenue] - SUM(Fact_Sales[Total_COGS]), [Total_Net_Revenue], 0.0)
```

### 4.2 The CALCULATE Function (The Heart of DAX)
`CALCULATE` evaluates an expression in a modified filter context:

```dax
// Revenue for Enterprise Customer Segment Only
Enterprise_Revenue := 
CALCULATE(
    [Total_Net_Revenue],
    Dim_Customer[Tier_Segment] = "Enterprise"
)

// Percentage of Total Revenue (Ignoring Product Filters)
Product_Revenue_Share := 
DIVIDE(
    [Total_Net_Revenue],
    CALCULATE([Total_Net_Revenue], ALL(Dim_Product)),
    0.0
)
```

### 4.3 Iterator Functions (SUMX, AVERAGEX)
Iterators iterate through a table row-by-row, evaluate an expression, and aggregate the results:

```dax
// Computing Total Margin where Cost varies row-by-row
Total_Margin_Dollars := 
SUMX(
    Fact_Sales,
    Fact_Sales[Units_Sold] * (RELATED(Dim_Product[List_Price]) - RELATED(Dim_Product[Standard_Cost]))
)
```

---

## 5. Time Intelligence in DAX

Time intelligence functions allow private equity analysts to compute Year-over-Year (YoY) growth, Quarter-to-Date (QTD), and Year-to-Date (YTD) metrics.

> [!IMPORTANT]
> Time intelligence requires a **Dedicated Date Dimension (`Dim_Date`)** with contiguous dates, no gaps, spanning from January 1 to December 31.

```dax
// Year-to-Date Net Revenue
Revenue_YTD := 
TOTALYTD(
    [Total_Net_Revenue],
    Dim_Date[Date]
)

// Prior Year Revenue (Same Period Last Year)
Revenue_Prior_Year := 
CALCULATE(
    [Total_Net_Revenue],
    SAMEPERIODLASTYEAR(Dim_Date[Date])
)

// Year-over-Year (YoY) Revenue Growth %
YoY_Revenue_Growth_Pct := 
DIVIDE(
    [Total_Net_Revenue] - [Revenue_Prior_Year],
    [Revenue_Prior_Year],
    0.0
)

// Trailing Twelve Months (TTM) Revenue
Revenue_TTM := 
CALCULATE(
    [Total_Net_Revenue],
    DATESINPERIOD(Dim_Date[Date], MAX(Dim_Date[Date]), -12, MONTH)
)
```

---

## 6. End-to-End Case Study: SaaS Portco ARR & Churn Model

A private equity sponsor acquires a B2B SaaS company and requires monthly recurring revenue (MRR) tracking and cohort churn analysis.

### Model Setup
- `Fact_Subscriptions`: `Subscription_ID`, `Customer_ID`, `Start_Date`, `End_Date`, `Monthly_Rate`, `Churn_Flag`.
- `Dim_Customer`: `Customer_ID`, `Customer_Name`, `Acquisition_Channel`, `ARR_Tier`.
- `Dim_Date`: Standard Calendar.

### Key DAX Measures
```dax
// 1. Ending Active MRR
Active_MRR := 
CALCULATE(
    SUM(Fact_Subscriptions[Monthly_Rate]),
    Fact_Subscriptions[Start_Date] <= MAX(Dim_Date[Date]) &&
    (ISBLANK(Fact_Subscriptions[End_Date]) || Fact_Subscriptions[End_Date] > MAX(Dim_Date[Date]))
)

// 2. Churned MRR in Selected Period
Churned_MRR := 
CALCULATE(
    SUM(Fact_Subscriptions[Monthly_Rate]),
    Fact_Subscriptions[Churn_Flag] = 1,
    USERELATIONSHIP(Fact_Subscriptions[End_Date], Dim_Date[Date])
)

// 3. Monthly Net Revenue Retention (NRR) Rate
// Measures expansion vs churn across established customer cohort
NRR_Pct := 
DIVIDE(
    [Cohort_Current_MRR],
    [Cohort_Baseline_MRR],
    1.0
)
```

