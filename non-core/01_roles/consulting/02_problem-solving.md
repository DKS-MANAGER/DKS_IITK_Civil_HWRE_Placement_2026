# Block 1 — Structured Problem Solving, MECE & Issue Trees

> **Document Purpose**: Core methodology for consulting problem solving.  
> **Structure**: Concept → Framework → Step-by-Step Workflow → 2 Fully Worked Examples → Common Mistakes.

---

## 1. The 7-Step Consulting Problem Solving Workflow

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│                   7-STEP PROBLEM SOLVING WORKFLOW                           │
├─────────────────────────────────────────────────────────────────────────────┤
│ Step 1: Clarify & Define Objective  ──► What exact goal must client reach? │
│ Step 2: Deconstruct Problem (MECE)  ──► Build Issue Tree (No gaps/overlaps)│
│ Step 3: Formulate Hypothesis       ──► What is the likely root cause?      │
│ Step 4: Prioritize Branches        ──► 80/20 rule (Focus on high-impact)  │
│ Step 5: Gather & Analyze Data       ──► Verify hypothesis with numbers    │
│ Step 6: Synthesize Findings        ──► Translate analysis into insights    │
│ Step 7: Formulate Recommendation   ──► Clear action plan with next steps  │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Concept: MECE (Mutually Exclusive, Collectively Exhaustive)

### What is MECE?
* **Mutually Exclusive**: Branches do not overlap with each other.
* **Collectively Exhaustive**: All branches together cover 100% of possibilities.

```text
               ┌───────────────────────────────────────────────┐
               │                NON-MECE BREAKDOWN             │
               │   (Bad: Overlaps & Missing Segments)          │
               │   • Online Sales                              │
               │   • Retail Store Sales                        │
               │   • Customers over 30 years old               │ ◄── Overlaps!
               └───────────────────────────────────────────────┘

               ┌───────────────────────────────────────────────┐
               │                  MECE BREAKDOWN               │
               │   (Good: Clear Disjoint Segmentation)        │
               │   • Direct Channels (Online, Flagship Stores) │
               │   • Indirect Channels (Distributors, Wholesalers)│
               └───────────────────────────────────────────────┘
```

---

## 3. Issue Trees — How to Build Them

An **Issue Tree** breaks down a complex problem into smaller, logical sub-components.

### Common MECE Breakdown Structures:
1. **Mathematical Deconstruction**: Revenue = Units Sold × Price per Unit.
2. **Process / Value Chain**: Inbound Logistics → Manufacturing → Distribution → Sales → After-Sales.
3. **Internal vs External**: Company Internal Factors vs Macro Market Factors.
4. **Customer Journey**: Awareness → Consideration → Purchase → Retention.

---

## 4. Worked Example 1: E-Commerce Client Revenue Drop

### Case Prompt:
Our client, an online fashion retailer in India, experienced a **15% drop in total quarterly revenue**. Diagnose the root cause and recommend actions.

---

### Step 1: Clarify Objective
* **Objective**: Identify why quarterly revenue fell by 15% and how to reverse it.
* **Scope**: India market, past 3 months.

---

### Step 2: Build MECE Issue Tree (Mathematical Deconstruction)

```text
                                [Total Revenue Drop]
                                         │
            ┌────────────────────────────┴────────────────────────────┐
            ▼                                                         ▼
[Number of Orders / Conversions]                           [Average Order Value (AOV)]
            │                                                         │
   ┌────────┴────────┐                                       ┌────────┴────────┐
   ▼                 ▼                                       ▼                 ▼
[Site Visitors] [Conversion Rate %]                      [Units per Order] [Price per Unit]
```

---

### Step 3: Hypothesis & Data Analysis Path
* **Interviewer Insight 1**: Site traffic grew by 5%, but overall revenue dropped. (Rules out Visitor count).
* **Interviewer Insight 2**: Average Order Value remained constant at ₹1,800. (Rules out AOV).
* **Interviewer Insight 3**: Conversion rate dropped from 3.2% to 2.1%.
* **Drill-down into Conversion Rate**:

```text
                          [Conversion Rate Drop]
                                     │
         ┌───────────────────────────┴───────────────────────────┐
         ▼                                                       ▼
[Checkout Funnel Drop-off]                               [Payment Failure Rate]
```

* **Data Finding**: Payment gateway failures spiked by 40% after a recent software deployment, leading to abandoned carts at the checkout page.

---

### Step 4: Recommendation & Action Plan
1. **Immediate Action**: Roll back the payment gateway update to restore checkout stability.
2. **Short-Term Action**: Send automated email/WhatsApp cart recovery links with discounts to affected customers.
3. **Long-Term Action**: Implement dual payment gateways (Razorpay + PayU) for automatic failover redundancy.

---

## 5. Worked Example 2: Manufacturing Operations Cost Spikes

### Case Prompt:
A commercial vehicle manufacturer in Pune sees a **12% increase in unit production costs** over 6 months despite steady production volume.

---

### Step 1: Build MECE Value Chain Tree

```text
                             [Unit Production Cost +12%]
                                         │
            ┌────────────────────────────┼────────────────────────────┐
            ▼                            ▼                            ▼
[Raw Material Costs]           [Factory Processing Costs]     [Logistics & Warehouse]
            │                            │                            │
  ┌─────────┴─────────┐        ┌─────────┴─────────┐        ┌─────────┴─────────┐
  ▼                   ▼        ▼                   ▼        ▼                   ▼
[Steel/Metal Price] [Scrap Rate] [Labor Overhead] [Power/Machine] [Inbound Freight] [Inventory Holding]
```

---

### Step 2: Analysis & Discovery
* **Steel Costs**: Contract prices fixed for 1 year (No change).
* **Labor**: Hourly rate stable (No change).
* **Power/Machine Efficiency**: Breakdown logs reveal machine calibration errors caused scrap/reject rate to jump from 2% to 7% of raw steel.

---

### Step 3: Recommendation
1. **Immediate**: Re-calibrate CNC machinery and institute automated daily sensor alignment checks.
2. **Impact**: Reduces scrap rate back to 2%, cutting unit production cost by 9.5%.

---

## 6. Common Candidate Errors in Problem Solving

| Mistake | Why It Fails | How to Correct It |
| :--- | :--- | :--- |
| **Jumping to Solutions Immediately** | *"They should launch an app!"* shows lack of analytical structure. | Always structure the issue tree first before proposing solutions. |
| **Non-MECE Categories** | Combining overlapping categories (e.g., "Online, Retail, Youth"). | Ensure categories are strictly disjoint and exhaustive. |
| **Ignoring Data Signals** | Continuing down a branch after the interviewer stated metrics are normal. | Prune branches immediately when data rules them out. |
