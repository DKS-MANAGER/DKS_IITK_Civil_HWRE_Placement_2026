# Worked Case 05: Multi-Specialty Hospital Capacity & OR Yield Optimization

> **Case Type**: Operations Bottlenecks & Capacity Optimization
> **Industry**: Healthcare Services

---

## Case 4: Private Multi-Specialty Hospital Capacity & Margin Turnaround

### Problem Statement & Candidate Brief
> *“A 400-bed private multi-specialty tertiary care hospital in Hyderabad saw EBITDA decline 18% over the past two years despite bed occupancy remaining high at 88%. The Managing Director has hired us to explain why high occupancy is producing lower profit and how to restore margins.”*

### Step 1: Clarification & Structural Decomposition
- **Candidate**: *“Has the payer mix changed (e.g., government insurance vs. self-pay), or has the clinical case mix shifted between medical admissions and surgical procedures?”*  
  **Interviewer**: *“Excellent inquiry. Payer mix is stable (70% private insurance, 30% self-pay). However, the clinical case mix has shifted significantly toward general medicine admissions, while cardiac and orthopedic surgeries have declined.”*

### Step 2: Clinical Throughput & Capacity Bottleneck Analysis

| Department / Case Type | Bed Allocation | Average Length of Stay (ALOS) | Daily Revenue per Bed | Contribution Margin % | Daily Contribution per Bed |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **General Internal Medicine** | 220 beds | **7.0 days** | ₹12,000 | 25% | **₹3,000 / day** |
| **Elective Surgeries (Cardio/Ortho)** | 180 beds | **3.5 days** | ₹45,000 | 45% | **₹20,250 / day** |

#### Key Operational Insights:
1. **Capacity Blockage**: General medicine patients generate only **₹3,000/day** in contribution margin, but tie up beds for an extended **7.0 days**.
2. **Surgical Queue Cancellations**: Surgeons report having to postpone or turn away 15 elective surgical patients weekly because step-down ICU and surgical ward beds are full of lingering general medicine patients.
3. **Discharge Delay Bottleneck**: Internal audit reveals that 35% of general medicine discharge delays are caused by delayed morning lab test approvals and insurance billing paperwork, keeping patients in beds 24–36 hours longer than clinically necessary.

### Step 3: Financial Sizing of Discharge Acceleration
If the hospital implements rapid clinical discharge protocols and reduces General Medicine ALOS from **7.0 days to 4.5 days**:
- General medicine bed capacity freed = $\frac{7.0 - 4.5}{7.0} = \mathbf{35.7\% \text{ bed capacity released}}$.
- This frees up: $220\text{ beds} \times 35.7\% \approx \mathbf{78\text{ available beds}}$.
- Re-allocate 40 of these freed beds to capture the lost 15 surgical patients per week:
  - 15 incremental surgical patients/week $\times 52\text{ weeks} = \mathbf{780\text{ surgical cases / year}}$.
  - Average revenue per surgical admission = $3.5\text{ days} \times ₹45,000 = \mathbf{₹157,500}$.
  - Contribution per surgery = $₹157,500 \times 45\% \approx \mathbf{₹70,875}$.
  - **Incremental Annual Contribution**:
    $$\text{Annual EBITDA Expansion} = 780\text{ cases} \times ₹70,875 \approx \mathbf{+₹5.53\text{ Crore INR}}$$

### Step 4: Executive Recommendation
1. **Institute 11:00 AM Discharge Protocol**: Streamline insurance billing and lab report sign-offs to complete discharges before noon, freeing beds for afternoon surgical admissions.
2. **Re-Designate 40 Beds as Dedicated Surgical Units**: Ring-fence surgical beds so general medicine patients cannot block high-margin surgical throughput.
3. **Align Physician Incentives**: Introduce performance incentives for surgical suite utilization and on-time starts.