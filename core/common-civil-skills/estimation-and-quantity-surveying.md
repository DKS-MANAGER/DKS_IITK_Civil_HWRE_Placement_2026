# Estimation & Quantity Surveying

> Track: Core Civil Professional Skills  
> Domain: Quantity Surveying & Cost Estimation  
> Level: Advanced Placement / Professional Execution  

---

## 1. Overview & Fundamentals

Quantity Surveying (QS) and Estimation form the financial backbone of any construction project. An estimator predicts the cost of a project prior to construction, while a quantity surveyor measures quantities from drawings, prepares Bill of Quantities (BOQ), manages contracts, and values work done for contractor billing.

---

## 2. Bill of Quantities (BOQ) & Measurement Rules (IS 1200)

### Standard Units of Measurement
| Item | Unit | Measurement Rule (IS 1200) |
|:-----|:-----|:---------------------------|
| **Earthwork** | $m^3$ | Measured in stages of $1.5\text{ m}$ lift and $30\text{ m}$ lead. |
| **Concrete (RCC/PCC)** | $m^3$ | No deduction for reinforcement, small openings $< 0.1\text{ m}^2$, or ends of beams/joists $< 0.05\text{ m}^2$. |
| **Formwork** | $m^2$ | Contact area between concrete and shuttering. |
| **Reinforcement** | $MT$ or $kg$ | Measured by weight based on BBS. Laps, chairs, and spacers included. |
| **Brickwork** | $m^3$ | Full brick walls. Deductions for openings $> 0.1\text{ m}^2$. |
| **Plastering** | $m^2$ | Deductions for openings: No deduction for $< 0.5\text{ m}^2$; half deduction for $0.5 - 3\text{ m}^2$; full deduction for $> 3\text{ m}^2$. |

---

## 3. Worked Example: Concrete & Steel Estimation

### Problem: Estimate concrete and steel for a $3\text{ m} \times 4\text{ m}$ RCC slab, $150\text{ mm}$ thick, with $12\text{ mm}$ bars @ $150\text{ mm}$ c/c both ways.

#### Step 1: Concrete Volume
$$\text{Volume} = L \times B \times T = 3.0 \times 4.0 \times 0.15 = 1.8\text{ m}^3$$

#### Step 2: Reinforcement (BBS)
- **Bars along 3m span:** $\text{Number} = \frac{4000}{150} + 1 = 27.6 \approx 28\text{ bars}$. Length = $3.0\text{ m}$.
- **Bars along 4m span:** $\text{Number} = \frac{3000}{150} + 1 = 21\text{ bars}$. Length = $4.0\text{ m}$.
- **Total Length:** $(28 \times 3.0) + (21 \times 4.0) = 84 + 84 = 168\text{ m}$.
- **Unit Weight ($12\text{ mm}$):** $0.888\text{ kg/m}$.
- **Total Weight:** $168 \times 0.888 = 149.18\text{ kg} \approx 0.15\text{ MT}$.

---

## 4. Rate Analysis: M20 Concrete ($1:1.5:3$)

### Material Requirement for $1\text{ m}^3$ Wet Concrete:
- **Dry Volume:** $1.54 \times \text{Wet Volume} = 1.54\text{ m}^3$.
- **Cement:** $\frac{1}{1+1.5+3} \times 1.54 = 0.28\text{ m}^3 \approx 8.1\text{ bags}$ (since $1\text{ bag} = 0.0347\text{ m}^3$).
- **Sand:** $1.5 \times 0.28 = 0.42\text{ m}^3$.
- **Coarse Aggregate:** $3 \times 0.28 = 0.84\text{ m}^3$.

### Costing (Illustrative):
| Item | Quantity | Rate | Amount |
|:-----|:---------|:-----|:-------|
| Cement | $8.1\text{ bags}$ | $₹400$ | $₹3,240$ |
| Sand | $0.42\text{ m}^3$ | $₹1,500$ | $₹630$ |
| Aggregate | $0.84\text{ m}^3$ | $₹1,200$ | $₹1,008$ |
| Labor | $1\text{ unit}$ | $₹800$ | $₹800$ |
| **Total Direct Cost** | | | **$₹5,678$** |
| CP&O (15%) | | | $₹852$ |
| **Final Rate per $m^3$** | | | **$₹6,530$** |

---

## 5. Interview Questions & Rapid Revision

- **Q: What is the difference between Plinth Area and Carpet Area?**  
  *A:* Plinth area is the total built-up area including walls. Carpet area is the net usable area where a carpet can be laid (excludes wall thickness, balconies, etc.).
- **Q: How do you calculate the weight of a steel bar?**  
  *A:* $\text{Weight (kg/m)} = D^2 / 162.2$.
- **Q: What is a 'Lead' and 'Lift' in earthwork?**  
  *A:* Lead is the horizontal distance of transport (standard $30\text{ m}$). Lift is the vertical distance of transport (standard $1.5\text{ m}$).

---

## Related Topics
- [`contracts-and-tendering.md`](contracts-and-tendering.md)
- [`practical-site-execution.md`](practical-site-execution.md)
- [`README.md`](README.md)
