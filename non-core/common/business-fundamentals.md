# Business Fundamentals

> The language of business — definitions, formulas, intuition, examples, and interview questions for every core concept.

---

## Why You Need This

Non-core interviews assume basic business literacy. If you don't know what EBITDA means or can't explain unit economics, you'll struggle — regardless of your technical skills.

This is your **business vocabulary cheat sheet**.

---

## Revenue & Growth

### Revenue
**Definition:** Total income from sales of goods or services.
**Formula:** Revenue = Price × Quantity
**Intuition:** The "top line" — how much money comes in before any costs.

### Revenue Streams
| Type | Example | Civil Context |
|:-----|:--------|:--------------|
| Product sales | Selling software licenses | Selling precast components |
| Subscription | Monthly SaaS fees | Maintenance contracts |
| Service fees | Consulting hourly rate | Project-based consulting |
| Advertising | Google AdSense | — |
| Licensing | Patent licensing | Technology transfer |

### CAGR (Compound Annual Growth Rate)
**Formula:** CAGR = (Ending Value / Beginning Value)^(1/n) - 1
**Example:** Revenue grew from ₹100Cr to ₹200Cr in 4 years → CAGR = (200/100)^(1/4) - 1 = 18.9%
**Interview question:** "This company grew revenue from ₹50Cr to ₹200Cr in 3 years. What's the CAGR?"

### Market Share
**Formula:** Market Share = Company Revenue / Total Market Revenue × 100
**Interview question:** "How would you estimate the market share of [company]?"

---

## Profitability

### Gross Profit
**Formula:** Gross Profit = Revenue - Cost of Goods Sold (COGS)
**Gross Margin:** Gross Profit / Revenue × 100

### Operating Profit (EBIT)
**Formula:** Operating Profit = Revenue - COGS - Operating Expenses
**Operating Margin:** Operating Profit / Revenue × 100

### EBITDA
**Formula:** EBITDA = Earnings Before Interest, Taxes, Depreciation, Amortization
**Intuition:** A proxy for cash flow from operations — removes accounting and financing effects.
**Why it matters:** Lets you compare companies with different capital structures.

### Net Profit (Bottom Line)
**Formula:** Net Profit = Operating Profit - Interest - Taxes
**Net Margin:** Net Profit / Revenue × 100

### Profitability Framework
```
Revenue = Price × Volume
Costs = Fixed Costs + Variable Costs
Profit = Revenue - Costs

To improve profit:
├── Increase Revenue
│   ├── Increase price (if demand allows)
│   ├── Increase volume (more customers/sales)
│   └── New revenue streams
├── Decrease Costs
│   ├── Reduce fixed costs (rent, salaries)
│   ├── Reduce variable costs (materials, logistics)
│   └── Improve efficiency
└── Optimize Mix
    ├── Higher-margin products
    └── Better customer segments
```

---

## Cost Structure

### Fixed Costs
**Definition:** Costs that don't change with production volume.
**Examples:** Rent, salaries, insurance, equipment
**Interview context:** High fixed costs = need volume to be profitable (operating leverage)

### Variable Costs
**Definition:** Costs that scale with production volume.
**Examples:** Raw materials, shipping, hourly labor
**Interview context:** Low variable costs = high contribution margin per unit

### Break-Even Point
**Formula:** Break-Even Units = Fixed Costs / (Price - Variable Cost per Unit)
**Example:** Fixed costs = ₹10 lakh, Price = ₹500, Variable cost = ₹300 → Break-even = 10,00,000 / 200 = 5,000 units
**Interview question:** "How many units must we sell to break even?"

### Contribution Margin
**Formula:** Contribution Margin = Price - Variable Cost per Unit
**Intuition:** How much each unit contributes to covering fixed costs and generating profit.

---

## Unit Economics

### CAC (Customer Acquisition Cost)
**Formula:** CAC = Total Sales & Marketing Spend / Number of New Customers
**Example:** Spent ₹10 lakh on marketing, acquired 1,000 customers → CAC = ₹1,000/customer

### LTV (Customer Lifetime Value)
**Formula:** LTV = Average Revenue per Customer × Average Customer Lifespan
**Simple:** LTV = (Average Monthly Revenue × Gross Margin) / Monthly Churn Rate
**Example:** Monthly revenue = ₹500, Gross margin = 60%, Monthly churn = 5% → LTV = 500 × 0.6 / 0.05 = ₹6,000

### LTV:CAC Ratio
| Ratio | Meaning |
|:------|:--------|
| < 1:1 | Losing money on every customer |
| 1:1 - 3:1 | Unsustainable — not enough margin |
| 3:1 - 5:1 | Healthy — industry standard |
| > 5:1 | Very profitable — or under-investing in growth |

**Interview question:** "A company has CAC of ₹2,000 and LTV of ₹8,000. Is this healthy?"

### Payback Period
**Formula:** Payback Period = CAC / (Monthly Revenue per Customer × Gross Margin)
**Example:** CAC = ₹2,000, Monthly revenue = ₹500, Margin = 60% → Payback = 2,000 / 300 = 6.7 months

---

## Growth Metrics

### Retention Rate
**Formula:** Retention Rate = (Customers at End - New Customers) / Customers at Start × 100
**Example:** Started with 1,000, acquired 200, ended with 1,100 → Retention = (1,100 - 200) / 1,000 = 90%

### Churn Rate
**Formula:** Churn Rate = Customers Lost / Customers at Start × 100
**Example:** Started with 1,000, lost 100 → Churn = 10%
**Inverse of retention:** If retention is 90%, churn is 10%

### DAU / MAU (Daily/Monthly Active Users)
**Stickiness Ratio:** DAU / MAU
**Example:** DAU = 50,000, MAU = 200,000 → Stickiness = 25% (good for social media)

### Conversion Rate
**Formula:** Conversion Rate = Conversions / Total Visitors × 100
**Example:** 500 purchases from 10,000 visitors → Conversion = 5%

### Funnel Metrics
```
Awareness → Interest → Consideration → Purchase → Retention → Advocacy
   100%       60%         30%           10%         8%          3%

Key: Where is the biggest drop-off? That's where to focus.
```

---

## Pricing

### Cost-Plus Pricing
**Formula:** Price = Cost + (Cost × Markup %)
**Simple but ignores demand and competition**

### Value-Based Pricing
**Formula:** Price = Perceived Value to Customer
**Requires understanding customer willingness to pay**

### Dynamic Pricing
**Definition:** Adjusting prices based on demand, time, or customer segment
**Example:** Airlines, ride-sharing, e-commerce sales

### Price Elasticity
**Formula:** Elasticity = % Change in Quantity Demanded / % Change in Price
**|Elasticity| > 1:** Elastic (price-sensitive) — lowering price increases revenue
**|Elasticity| < 1:** Inelastic (price-insensitive) — raising price increases revenue

---

## Market Analysis

### TAM / SAM / SOM
| Term | Definition | Example (Coffee Shop) |
|:-----|:-----------|:----------------------|
| **TAM** | Total Addressable Market | All coffee consumed globally |
| **SAM** | Serviceable Addressable Market | Coffee consumed in your city |
| **SOM** | Serviceable Obtainable Market | Customers you can actually capture |

### Porter's Five Forces
1. **Threat of new entrants** — How easy is it to start competing?
2. **Bargaining power of suppliers** — Can suppliers raise prices?
3. **Bargaining power of buyers** — Can customers demand lower prices?
4. **Threat of substitutes** — Can something else replace your product?
5. **Competitive rivalry** — How intense is existing competition?

### SWOT Analysis
| | Helpful | Harmful |
|:---------|:--------|:--------|
| **Internal** | Strengths | Weaknesses |
| **External** | Opportunities | Threats |

---

## Financial Statements (Simplified)

### Income Statement (P&L)
```
Revenue
- COGS
= Gross Profit
- Operating Expenses (SG&A, R&D)
= Operating Profit (EBIT)
- Interest
- Taxes
= Net Profit
```

### Balance Sheet
```
Assets = Liabilities + Equity

Assets: What the company owns (cash, equipment, inventory)
Liabilities: What the company owes (loans, payables)
Equity: What belongs to shareholders (invested capital + retained earnings)
```

### Cash Flow Statement
```
Operating Activities: Cash from core business
Investing Activities: Cash spent on/received from investments
Financing Activities: Cash from/debt repayment to investors

Free Cash Flow = Operating Cash Flow - Capital Expenditures
```

---

## Interview Questions

### Basic
1. What is revenue? How is it different from profit?
2. What is EBITDA and why do we use it?
3. What are fixed vs variable costs?
4. Explain break-even analysis.
5. What is a balance sheet?

### Intermediate
6. How would you calculate CAC for a new product?
7. What LTV:CAC ratio would you consider healthy?
8. How does pricing strategy affect market share?
9. Explain operating leverage.
10. What's the difference between gross margin and net margin?

### Advanced
11. A company's revenue is growing but profits are declining. Why?
12. How would you value a company with no profits?
13. Two products have same revenue but different margins. Which should you invest in?
14. A SaaS company has 5% monthly churn. Is this good? How would you improve it?
15. Explain the relationship between pricing power and brand strength.

---

## Quick Reference Card

| Concept | Formula | Intuition |
|:--------|:--------|:----------|
| Revenue | Price × Quantity | Top line |
| Gross Profit | Revenue - COGS | Before operating costs |
| EBITDA | Earnings before I, T, D, A | Cash proxy |
| Break-Even | Fixed Costs / Contribution Margin | When profit = 0 |
| CAC | Marketing Spend / New Customers | Cost to acquire one customer |
| LTV | Revenue × Lifespan / Churn | Total value of one customer |
| Conversion | Conversions / Visitors | Funnel efficiency |
| CAGR | (End/Start)^(1/n) - 1 | Smoothed annual growth |

---

## Cross-Links

| Resource | Link |
|:---------|:-----|
| Role Selector (what skills you need) | [role-selector.md](../role-selector.md) |
| Consulting Case Frameworks | [case-frameworks.md](../consulting/case-frameworks.md) |
| Finance Basics | [finance-overview.md](../finance/finance-overview.md) |
| Aptitude Bridge | [aptitude-bridge.md](aptitude-bridge.md) |

---

*You don't need an MBA to understand business. You need to understand how money works.*
