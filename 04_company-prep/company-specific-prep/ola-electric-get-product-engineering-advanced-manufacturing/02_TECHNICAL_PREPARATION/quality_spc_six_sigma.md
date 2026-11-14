# Quality Engineering, SPC & Six Sigma: Industrial Manufacturing Excellence
**Target Role:** Graduate Engineer Trainee (GET) — Product Engineering & Advanced Manufacturing  
**Company:** Ola Electric Mobility Limited  
**Standard:** Statistical Process Control (SPC), Six Sigma DMAIC & Quality Management  

---

## 1. Quality Assurance (QA) vs Quality Control (QC)

In advanced gigawatt-scale manufacturing at Ola Electric:
- **Quality Control (QC — Product-Focused / Reactive):**  
  Operational techniques and inspection activities performed to verify that finished parts or sub-assemblies satisfy specified dimensional, mechanical, and electrical tolerances (e.g., CMM dimensional checks on swingarms, End-of-Line dyno testing, battery pack Hi-Pot dielectric insulation checks). QC detects defects *after* they are manufactured.
- **Quality Assurance (QA — Process-Focused / Proactive):**  
  The systematic planning, procedural governance, and statistical monitoring of manufacturing processes to guarantee that defects are prevented from occurring in the first place (e.g., SPC monitoring of die-casting melt temperatures, robotic weld calibration logs, FMEA risk prevention, supplier PPAP qualification).

---

## 2. Statistical Process Control (SPC) & Control Charts

Statistical Process Control monitors process stability over time, distinguishing **Common Cause Variation** (inherent random noise) from **Special Cause Variation** (assignable anomalies: tool wear, incorrect raw material batch, operator error).

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                        ANATOMY OF A SHEWHART CONTROL CHART                             │
└────────────────────────────────────────────────────────────────────────────────────────┘
  Upper Control Limit (UCL) = μ + 3σ  -------------------------------------------------
                                           *           *
  Center Line (CL)          = μ       -------*-------*-------*-------*-----------------
                                                 *               *
  Lower Control Limit (LCL) = μ - 3σ  -------------------------------------------------
  
  * Note: Control Limits (UCL/LCL) are calculated from PROCESS DATA (±3σ).
  * Specification Limits (USL/LSL) are defined by ENGINEERING DRAWINGS / DESIGN.
```

### 2.1 Variable Control Charts ($\bar{X}-R$ and $\bar{X}-S$)
Used for continuous dimensional metrics (e.g., chassis tube wall thickness, swingarm bore diameter):
- Subgroup sample size $n$ (typically $n = 4$ to $5$ consecutive parts measured every hour).
- **$\bar{X}$-Chart (Measures Process Centering / Mean):**
  $$\bar{\bar{X}} = \frac{1}{m}\sum_{i=1}^m \bar{X}_i$$
  $$UCL_{\bar{X}} = \bar{\bar{X}} + A_2 \bar{R}, \quad LCL_{\bar{X}} = \bar{\bar{X}} - A_2 \bar{R}$$
- **$R$-Chart (Measures Process Dispersion / Variability):**
  $$\bar{R} = \frac{1}{m}\sum_{i=1}^m R_i \quad (\text{where } R_i = X_{\max} - X_{\min})$$
  $$UCL_R = D_4 \bar{R}, \quad LCL_R = D_3 \bar{R}$$
  *(For $n = 5$: $A_2 = 0.577, D_3 = 0, D_4 = 2.114$).*

### 2.2 Western Electric Out-of-Control Rules
A manufacturing process is declared statistically **out of control** (requiring immediate line investigation) if any of the following occur:
1. **Rule 1 (Single Point Spike):** 1 point falls beyond Zone A ($> 3\sigma$ from center line).
2. **Rule 2 (Zone A Bias):** 2 out of 3 consecutive points fall in Zone A or beyond ($> 2\sigma$ on the same side).
3. **Rule 3 (Zone B Trend):** 4 out of 5 consecutive points fall in Zone B or beyond ($> 1\sigma$ on the same side).
4. **Rule 4 (Run of Eight):** 8 consecutive points fall on the same side of the center line (indicates process mean shift).
5. **Rule 5 (Linear Drift):** 6 consecutive points steadily increasing or steadily decreasing (tool wear indicator).

---

## 3. Process Capability Analysis ($C_p, C_{pk}$ vs $P_p, P_{pk}$)

Process capability evaluates whether a statistically stable process can reliably produce parts within customer design engineering specifications ($LSL$ to $USL$).

```
                      PROCESS SPREAD (6σ) VS SPECIFICATION WIDTH
                      
       LSL                                Target                               USL
        │                                   │                                   │
        ▼                                   ▼                                   ▼
        ├───────────────────────────────────┼───────────────────────────────────┤
                    ┌───────────────────────┴───────────────────────┐
                    │               PROCESS SPREAD (6σ)             │
                    └───────────────────────────────────────────────┘
```

### 3.1 Mathematical Derivations & Formulas
- **Potential Capability Index ($C_p$ — Independent of Centering):**
  $$C_p = \frac{\text{Voice of Customer}}{\text{Voice of Process}} = \frac{USL - LSL}{6\hat{\sigma}}$$
  where estimated process standard deviation $\hat{\sigma} = \frac{\bar{R}}{d_2}$ (within-subgroup short-term variation).
  - $C_p$ measures the inherent precision of the tooling/machine, assuming the process is perfectly centered on target.
- **Actual Capability Index ($C_{pk}$ — Accounts for Centering Shift):**
  $$C_{pk} = \min\left( \frac{USL - \mu}{3\hat{\sigma}}, \frac{\mu - LSL}{3\hat{\sigma}} \right) = C_p (1 - k)$$
  where $k = \frac{|\text{Target} - \mu|}{(USL - LSL)/2}$ is the process off-center factor.

### 3.2 Interpreting $C_p$ vs $C_{pk}$ Discrepancies
- **Case 1: $C_p = C_{pk} \ge 1.33$:** The process is capable and perfectly centered on the nominal design target.
- **Case 2: $C_p \ge 1.67$, but $C_{pk} = 0.85$:**  
  *Diagnostic Insight:* The machine has exceptional inherent precision (very low spread $6\sigma$), but the process mean $\mu$ has drifted significantly towards one specification limit!  
  *Remediation:* Do NOT replace the tooling or machine. Simply adjust the machine tool offset, cutter datum, or die clamping stop to re-center the mean.
- **Case 3: $C_p = C_{pk} \le 0.90$:**  
  *Diagnostic Insight:* The process is centered, but the inherent machine spread is too wide for the tolerance band. Tooling redesign or tighter temperature/pressure controls are required.

### 3.3 $C_{pk}$ vs $P_{pk}$ (Short-Term vs Long-Term Performance)
- $C_{pk}$ uses short-term within-subgroup variation ($\hat{\sigma} = \bar{R}/d_2$), reflecting best-case machine capability.
- $P_{pk}$ (Process Performance Index) uses overall sample standard deviation ($s = \sqrt{\frac{\sum (X - \bar{X})^2}{N - 1}}$) across days or weeks, capturing tool wear, shift changes, batch-to-batch material variations, and ambient temperature swings.

---

## 4. Failure Mode and Effects Analysis (FMEA)

In EV design and assembly, Design FMEA (DFMEA) and Process FMEA (PFMEA) prioritize failure modes by evaluating their **Risk Priority Number (RPN)**:

$$RPN = \text{Severity (S)} \times \text{Occurrence (O)} \times \text{Detection (D)}$$
- **Severity ($S$, 1–10):** How severe is the impact on customer safety or vehicle function? (e.g., Battery thermal runaway fire $= 10$; minor cosmetic panel scratch $= 2$).
- **Occurrence ($O$, 1–10):** What is the statistical frequency or probability of the failure mode occurring?
- **Detection ($D$, 1–10):** How likely is the current inspection/testing method to detect the defect *before* it leaves the factory? ($1 =$ Automated 100% vision detection; $10 =$ Undetectable until customer use).
- **Corrective Action Threshold:** Under modern AIAG & VDA standards, any failure mode with $S \ge 9$ (safety or regulatory hazard) mandates immediate redesign or error-proofing, regardless of overall RPN!

---

## 5. Root-Cause Problem Solving: 8D, Fishbone & 5 Whys

When an unexpected defect spike occurs on the Futurefactory line:

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                        THE 8D PROBLEM-SOLVING METHODOLOGY                              │
├─────────┬──────────────────────────┬───────────────────────────────────────────────────┤
│ Stage   │ Discipline Action        │ Engineering Execution                             │
├─────────┼──────────────────────────┼───────────────────────────────────────────────────┤
│ D1      │ Establish the Team       │ Cross-functional: Design, Mfg, Quality, Supplier  │
│ D2      │ Describe the Problem     │ Is / Is-Not matrix (What, Where, When, Extent)    │
│ D3      │ Interim Containment      │ Quarantining suspect chassis inventory at plant   │
│ D4      │ Root Cause Analysis      │ 5-Whys, Fishbone (6M), fault tree verification    │
│ D5      │ Permanent Corrective Act.│ Tooling redesign, robotic weld parameter lock     │
│ D6      │ Implement & Validate     │ Pilot run, confirm Cpk > 1.33 across 500 parts    │
│ D7      │ Prevent Recurrence       │ Update PFMEA, Control Plans, standard work SOP    │
│ D8      │ Congratulate Team        │ Knowledge sharing across platform teams           │
└─────────┴──────────────────────────┴───────────────────────────────────────────────────┘
```

### 5.1 The Ishikawa (Fishbone) Diagram (The 6Ms)
Categories used to brainstorm root causes:
1. **Machine:** Die wear, robotic torch alignment, hydraulic pump pressure fluctuations.
2. **Method:** Incorrect weld sequence causing thermal distortion, excessive stamping press speed.
3. **Material:** Aluminum batch silicon content out of spec, sheet metal yield strength variation.
4. **Man / Personnel:** Inadequate operator training on manual torque guns.
5. **Measurement:** Dial gauge out of calibration, CMM probing coordinate error.
6. **Milieu (Environment):** High ambient humidity in battery cleanroom, seasonal temperature swings.

---

## 6. Lean Manufacturing & Industrial Engineering Metrics

### 6.1 Takt Time & Line Balancing
- **Takt Time:** The allowable pace of production required to match customer demand:
  $$\text{Takt Time} = \frac{\text{Net Available Working Time per Shift}}{\text{Customer Demand per Shift}}$$
  *Example:* An 8-hour shift has $480\text{ minutes}$. Subtract two 15-minute tea breaks and a 30-minute lunch $\implies 420\text{ minutes} = 25,200\text{ seconds}$. If customer demand is 350 scooters per shift:
  $$\text{Takt Time} = \frac{25,200\text{ s}}{350\text{ units}} = \mathbf{72.0\text{ seconds/unit}}$$
- **Line Balancing:** Workstations along the conveyor are balanced such that cycle times at every station approach, but do not exceed, $72\text{ seconds}$. Any station exceeding $72\text{ s}$ is a **bottleneck**, dictating the maximum throughput of the entire plant.

### 6.2 Overall Equipment Effectiveness (OEE)
$$OEE = \text{Availability} \times \text{Performance} \times \text{Quality}$$
- **Availability ($A$):** Ratio of actual operating time to planned production time (penalized by machine breakdowns and die changeovers).
- **Performance ($P$):** Ratio of actual pieces produced to ideal design capacity speed (penalized by micro-stoppages and idling).
- **Quality ($Q$):** Ratio of good, defect-free parts to total parts produced (penalized by scrap and rework).
- *World-Class Benchmark:* $A \ge 90\%, P \ge 95\%, Q \ge 99.9\% \implies OEE \ge 85\%$.

### 6.3 Poka-Yoke (Mistake-Proofing)
Mechanical, electrical, or software mechanisms that physically prevent an error from occurring:
- **Contact Method:** Asymmetric alignment pins ensuring a battery module cannot be plugged in reverse polarity.
- **Fixed-Value Method:** An automated torque gun that will not release the pallet to the next conveyor station until all 12 chassis bolts have been torqued to $25\text{ Nm} \pm 1\text{ Nm}$.
- **Motion-Step Method:** Light-curtain sensors across parts bins that sound an alarm if an operator reaches for Part B before installing Part A.

---
*End of Quality Engineering, SPC & Six Sigma.*
