# Quality Engineering, SPC & Six Sigma Assessment Question Bank

## Overview and Role Alignment
This question bank provides **35 technically rigorous, fully worked questions** on Statistical Process Control (SPC), Process Capability Indices ($C_p, C_{pk}, P_p, P_{pk}$), AIAG-VDA Failure Mode and Effects Analysis (FMEA), 8D Problem Solving, Root Cause Analysis (Ishikawa 6M / 5-Whys), DMAIC Six Sigma, and Lean Manufacturing Operations (Takt Time, OEE, Line Balancing). These concepts form the operational core of high-volume quality engineering at **Ola Electric's Futurefactory** and **Gigafactory**.

---

### Question 1: Process Capability Index ($C_p$ vs $C_{pk}$)
**Question:** The cylindrical outside diameter of a high-precision rotor shaft for an EV traction motor has a design specification of $45.000 \pm 0.030\text{ mm}$ ($\text{USL} = 45.030\text{ mm}$, $\text{LSL} = 44.970\text{ mm}$). A capability study of 150 consecutive parts machined in a stable CNC turning cell indicates a sample mean $\bar{\bar{X}} = 45.012\text{ mm}$ and an estimated within-subgroup standard deviation $\hat{\sigma}_{\text{within}} = 0.005\text{ mm}$.
Calculate the process potential index ($C_p$) and the process capability index ($C_{pk}$). Is the process capable according to standard automotive OEM standards ($C_{pk} \ge 1.33$)?
- A) $C_p = 2.00$, $C_{pk} = 1.20$; Not capable
- B) $C_p = 1.67$, $C_{pk} = 1.33$; Marginally capable
- C) $C_p = 2.00$, $C_{pk} = 1.50$; Capable
- D) $C_p = 1.50$, $C_{pk} = 1.20$; Not capable

**Correct Answer:** A) $C_p = 2.00$, $C_{pk} = 1.20$; Not capable

**Detailed Solution & Mathematical Derivation:**
1. Specification Width:
   $$\text{USL} - \text{LSL} = 45.030 - 44.970 = 0.060\text{ mm}$$
2. Process Potential Index ($C_p$):
   $$C_p = \frac{\text{USL} - \text{LSL}}{6\hat{\sigma}} = \frac{0.060}{6 \times 0.005} = \frac{0.060}{0.030} = 2.00$$
3. Upper and Lower Capability Indices ($C_{pu}$ and $C_{pl}$):
   $$C_{pu} = \frac{\text{USL} - \mu}{3\hat{\sigma}} = \frac{45.030 - 45.012}{3 \times 0.005} = \frac{0.018}{0.015} = 1.20$$
   $$C_{pl} = \frac{\mu - \text{LSL}}{3\hat{\sigma}} = \frac{45.012 - 44.970}{3 \times 0.005} = \frac{0.042}{0.015} = 2.80$$
4. Overall Capability Index ($C_{pk}$):
   $$C_{pk} = \min(C_{pu}, C_{pl}) = \min(1.20, 2.80) = 1.20$$
5. Assessment:
   While the inherent process spread is narrow ($C_p = 2.00$, capable of Six Sigma), the process mean is shifted to the right ($\bar{X} = 45.012\text{ mm}$ vs nominal $45.000\text{ mm}$). Because $C_{pk} = 1.20 < 1.33$ (the minimum automotive threshold, often $1.67$ for critical safety dimensions), the process is **not capable** due to decentering. Tool offset adjustment is immediately required to re-center the mean.

---

### Question 2: Expected Defect Rate (PPM) from Capability
**Question:** If the rotor shaft process in Question 1 continues running with $C_{pk} = 1.20$ (with normal distribution of dimensions), what is the expected non-conformance rate in Parts Per Million (PPM) exceeding the Upper Specification Limit? (Given standard normal cumulative probabilities: $\Phi(3.60) = 0.999841$, $\Phi(3.00) = 0.99865$, $\Phi(1.20) = 0.8849$).
- A) $159\text{ PPM}$
- B) $1,350\text{ PPM}$
- C) $3.4\text{ PPM}$
- D) $2,700\text{ PPM}$

**Correct Answer:** A) $159\text{ PPM}$

**Detailed Solution & Mathematical Derivation:**
1. The $Z$-score for the Upper Specification Limit:
   $$Z_{\text{USL}} = \frac{\text{USL} - \mu}{\hat{\sigma}} = \frac{45.030 - 45.012}{0.005} = \frac{0.018}{0.005} = 3.60$$
   *(Note that $Z_{\text{USL}} = 3 \times C_{pu} = 3 \times 1.20 = 3.60$)*.
2. The probability of parts exceeding USL:
   $$P(X > \text{USL}) = 1 - \Phi(Z_{\text{USL}}) = 1 - \Phi(3.60) = 1 - 0.999841 = 0.000159$$
3. Non-conformance in PPM:
   $$\text{PPM} = P(X > \text{USL}) \times 10^6 = 0.000159 \times 1,000,000 = 159\text{ PPM}$$
   *(The lower specification limit non-conformance is at $Z_{\text{LSL}} = 3 \times 2.80 = 8.40\sigma$, which contributes $\approx 0\text{ PPM}$)*.

---

### Question 3: $\bar{X}-R$ Control Chart Limit Calculations
**Question:** Quality technicians monitor the thickness of coated cathode electrodes at the Gigafactory using an $\bar{X}$ and $R$ control chart. Subgroups of size $n = 5$ are sampled every 30 minutes. Across 25 in-control subgroups, the grand mean is $\bar{\bar{X}} = 142.5\text{ }\mu\text{m}$ and the average subgroup range is $\bar{R} = 6.2\text{ }\mu\text{m}$.
Given standard SPC constants for $n = 5$: $A_2 = 0.577$, $D_3 = 0$, $D_4 = 2.114$, $d_2 = 2.326$.
What are the Upper and Lower Control Limits for the $\bar{X}$ chart ($\text{UCL}_{\bar{X}}, \text{LCL}_{\bar{X}}$) and the estimated population standard deviation ($\hat{\sigma}$)?
- A) $\text{UCL}_{\bar{X}} = 146.08\text{ }\mu\text{m}$, $\text{LCL}_{\bar{X}} = 138.92\text{ }\mu\text{m}$, $\hat{\sigma} = 2.67\text{ }\mu\text{m}$
- B) $\text{UCL}_{\bar{X}} = 148.70\text{ }\mu\text{m}$, $\text{LCL}_{\bar{X}} = 136.30\text{ }\mu\text{m}$, $\hat{\sigma} = 3.10\text{ }\mu\text{m}$
- C) $\text{UCL}_{\bar{X}} = 145.20\text{ }\mu\text{m}$, $\text{LCL}_{\bar{X}} = 139.80\text{ }\mu\text{m}$, $\hat{\sigma} = 1.85\text{ }\mu\text{m}$
- D) $\text{UCL}_{\bar{X}} = 146.08\text{ }\mu\text{m}$, $\text{LCL}_{\bar{X}} = 138.92\text{ }\mu\text{m}$, $\hat{\sigma} = 3.58\text{ }\mu\text{m}$

**Correct Answer:** A) $\text{UCL}_{\bar{X}} = 146.08\text{ }\mu\text{m}$, $\text{LCL}_{\bar{X}} = 138.92\text{ }\mu\text{m}$, $\hat{\sigma} = 2.67\text{ }\mu\text{m}$

**Detailed Solution & Mathematical Derivation:**
1. Control limits for $\bar{X}$ chart:
   $$\text{UCL}_{\bar{X}} = \bar{\bar{X}} + A_2 \bar{R} = 142.5 + (0.577 \times 6.2) = 142.5 + 3.5774 = 146.077\text{ }\mu\text{m} \approx 146.08\text{ }\mu\text{m}$$
   $$\text{LCL}_{\bar{X}} = \bar{\bar{X}} - A_2 \bar{R} = 142.5 - (0.577 \times 6.2) = 142.5 - 3.5774 = 138.923\text{ }\mu\text{m} \approx 138.92\text{ }\mu\text{m}$$
2. Control limits for $R$ chart:
   $$\text{UCL}_R = D_4 \bar{R} = 2.114 \times 6.2 = 13.11\text{ }\mu\text{m}$$
   $$\text{LCL}_R = D_3 \bar{R} = 0 \times 6.2 = 0\text{ }\mu\text{m}$$
3. Population standard deviation estimation ($\hat{\sigma}$):
   $$\hat{\sigma} = \frac{\bar{R}}{d_2} = \frac{6.2\text{ }\mu\text{m}}{2.326} \approx 2.6655\text{ }\mu\text{m} \approx 2.67\text{ }\mu\text{m}$$

---

### Question 4: Western Electric Rules and Out-of-Control Signals
**Question:** On the $\bar{X}$ chart of an automated robotic laser welding station, 8 consecutive subgroup averages fall on one side of the center line (all above $\bar{\bar{X}}$), but none breach the $3\sigma$ Upper Control Limit. According to Western Electric Rule 2 / Nelson Rule 2:
- A) The process is perfectly normal and shows superior performance.
- B) An out-of-control condition is signaled due to a systematic mean shift or tool bias; immediate investigation is required.
- C) The sample size $n$ should be reduced to 2 to hide the variance.
- D) The control limits should be manually expanded to encompass the shift.

**Correct Answer:** B) An out-of-control condition is signaled due to a systematic mean shift or tool bias; immediate investigation is required.

**Detailed Solution & Mathematical Derivation:**
- Under a purely random normal process, the probability of any single point falling above the mean is $p = 0.5$.
- The probability of 8 consecutive independent points falling on the same side of the mean is:
  $$P(\text{8 consecutive above}) = (0.5)^8 = \frac{1}{256} \approx 0.0039\text{ }(0.39\%)$$
- Because this probability is less than $0.5\%$, it indicates an assignable cause (e.g., optical cover slide spatter on the laser, lens thermal focus drift, or a new batch of wire feed).

---

### Question 5: $p$-Chart (Fraction Nonconforming) Limits
**Question:** At the final functional testing of battery management system (BMS) PCBA boards, lots of $N = 400$ boards are inspected daily. Over 30 days, 240 boards were rejected in total.
What is the average defect fraction ($\bar{p}$) and the $3\sigma$ Upper Control Limit ($\text{UCL}_p$) for this $p$-chart?
- A) $\bar{p} = 0.020$, $\text{UCL}_p = 0.041$
- B) $\bar{p} = 0.020$, $\text{UCL}_p = 0.035$
- C) $\bar{p} = 0.050$, $\text{UCL}_p = 0.083$
- D) $\bar{p} = 0.020$, $\text{UCL}_p = 0.052$

**Correct Answer:** A) $\bar{p} = 0.020$, $\text{UCL}_p = 0.041$

**Detailed Solution & Mathematical Derivation:**
1. Total inspected: $30 \times 400 = 12,000\text{ boards}$. Total rejected: $240$.
2. Centerline ($\bar{p}$):
   $$\bar{p} = \frac{240}{12,000} = 0.020\text{ (i.e., } 2.0\%)$$
3. Standard error of fraction nonconforming ($\sigma_p$):
   $$\sigma_p = \sqrt{\frac{\bar{p}(1 - \bar{p})}{n}} = \sqrt{\frac{0.020 \times 0.980}{400}} = \sqrt{\frac{0.0196}{400}} = \sqrt{0.000049} = 0.007$$
4. Upper Control Limit ($\text{UCL}_p$):
   $$\text{UCL}_p = \bar{p} + 3\sigma_p = 0.020 + 3(0.007) = 0.020 + 0.021 = 0.041\text{ (i.e., } 4.1\%)$$
5. Lower Control Limit ($\text{LCL}_p$):
   $$\text{LCL}_p = \max(0, \bar{p} - 3\sigma_p) = \max(0, 0.020 - 0.021) = 0$$

---

### Question 6: Overall Equipment Effectiveness (OEE) Calculation
**Question:** An automated stator winding machine on the motor line at Futurefactory operates on an 8-hour shift ($480\text{ minutes}$).
The operating record reveals:
- Planned maintenance and tea breaks: $30\text{ minutes}$ (Planned operating time $= 450\text{ minutes}$)
- Unplanned downtime (jam clearing, wire spool changeover): $45\text{ minutes}$
- Ideal cycle time: $1.2\text{ minutes per stator}$
- Total stators produced: $300\text{ units}$
- Defective stators rejected during surge testing: $15\text{ units}$
Calculate Availability ($A$), Performance ($P$), Quality ($Q$), and the total OEE of the work cell.
- A) $A = 90.0\%$, $P = 88.9\%$, $Q = 95.0\%$, $\text{OEE} = 76.0\%$
- B) $A = 85.0\%$, $P = 92.0\%$, $Q = 96.0\%$, $\text{OEE} = 75.1\%$
- C) $A = 90.0\%$, $P = 80.0\%$, $Q = 95.0\%$, $\text{OEE} = 68.4\%$
- D) $A = 93.3\%$, $P = 88.9\%$, $Q = 95.0\%$, $\text{OEE} = 78.8\%$

**Correct Answer:** A) $A = 90.0\%$, $P = 88.9\%$, $Q = 95.0\%$, $\text{OEE} = 76.0\%$

**Detailed Solution & Mathematical Derivation:**
1. Availability ($A$):
   - Planned Operating Time: $480 - 30 = 450\text{ minutes}$.
   - Actual Operating Time (Run Time): $450 - 45 = 405\text{ minutes}$.
   $$A = \frac{\text{Operating Time}}{\text{Planned Production Time}} = \frac{405}{450} = 0.900 = 90.0\%$$
2. Performance ($P$):
   - Ideal Time for Produced Parts: $300\text{ units} \times 1.2\text{ min/unit} = 360\text{ minutes}$.
   $$P = \frac{\text{Ideal Cycle Time} \times \text{Total Count}}{\text{Operating Time}} = \frac{360\text{ min}}{405\text{ min}} \approx 0.8889 = 88.89\%$$
3. Quality ($Q$):
   - Good Parts: $300 - 15 = 285\text{ units}$.
   $$Q = \frac{\text{Good Count}}{\text{Total Count}} = \frac{285}{300} = 0.950 = 95.0\%$$
4. Total OEE:
   $$\text{OEE} = A \times P \times Q = 0.900 \times 0.8889 \times 0.950 \approx 0.7600 = 76.0\%$$

---

### Question 7: Takt Time and Line Balancing
**Question:** Ola Futurefactory targets producing $2,400$ electric scooters per day operating across three shifts of $8\text{ hours}$ each. Total planned breaks, shift handovers, and cleanings amount to $60\text{ minutes}$ per shift.
What is the required Takt Time in seconds per scooter?
- A) $25.0\text{ seconds}$
- B) $31.5\text{ seconds}$
- C) $36.0\text{ seconds}$
- D) $42.0\text{ seconds}$

**Correct Answer:** B) $31.5\text{ seconds}$

**Detailed Solution & Mathematical Derivation:**
1. Available working time per shift:
   $$480\text{ min} - 60\text{ min} = 420\text{ minutes}$$
2. Total available operating time per day across 3 shifts:
   $$\text{Time}_{\text{total}} = 3 \times 420\text{ min} = 1,260\text{ minutes} = 1,260 \times 60\text{ seconds} = 75,600\text{ seconds}$$
3. Customer demand: $2,400\text{ scooters/day}$.
4. Takt Time ($T_t$):
   $$T_t = \frac{\text{Net Available Operating Time}}{\text{Customer Demand}} = \frac{75,600\text{ s}}{2,400\text{ units}} = 31.5\text{ seconds/scooter}$$
   Every assembly station on the main line must complete its standard work sequence within $31.5\text{ seconds}$ to meet the daily schedule.

---

### Question 8: AIAG-VDA FMEA — Risk Assessment Methodology
**Question:** In the updated AIAG-VDA Failure Mode and Effects Analysis (FMEA) 1st Edition standard, what major methodology replaced the traditional Risk Priority Number ($\text{RPN} = S \times O \times D$) for prioritizing corrective actions, and why?
- A) Pareto $80/20$ sorting; because RPN was too complicated to multiply.
- B) Action Priority (AP) tables (High, Medium, Low); because the traditional RPN gave equal mathematical weight to Severity, Occurrence, and Detection, often masking high-severity safety risks behind low detection scores.
- C) Simple voting by the quality committee.
- D) Cost-of-Quality monetary index (COQ).

**Correct Answer:** B) Action Priority (AP) tables (High, Medium, Low); because the traditional RPN gave equal mathematical weight to Severity, Occurrence, and Detection, often masking high-severity safety risks behind low detection scores.

**Detailed Solution & Mathematical Derivation:**
- Under the old RPN system, two failure modes could have the same score:
  - Mode 1: $S=10$ (Battery fire/death), $O=2$, $D=2 \implies \text{RPN} = 40$.
  - Mode 2: $S=2$ (Minor scratch), $O=5$, $D=4 \implies \text{RPN} = 40$.
  Engineers frequently ignored Mode 1 because an arbitrary cutoff (e.g., $\text{RPN} > 100$) was not triggered, despite a potential vehicle fire hazard.
- The AIAG-VDA Action Priority (AP) standard evaluates the logic combinations of $S$, $O$, and $D$ via multi-dimensional look-up tables:
  - If $S \ge 9$ (Safety/Regulatory violation), AP is assigned **High (H)** regardless of detection, legally mandating an engineering design change (fail-safe mechanism).

---

### Question 9: 8D Problem Solving Methodology
**Question:** A sudden spike in customer field complaints reports sudden power loss in S1 scooters due to an open circuit in the main power contactor. Place the following 8D Problem Solving steps in their mandatory sequence:
1. Define Root Cause & Escape Point (D4)
2. Develop Interim Containment Action (ICA) (D3)
3. Implement & Validate Permanent Corrective Actions (PCA) (D5)
4. Establish the Team (D1)
5. Prevent Recurrence (D7)
6. Describe the Problem (D2)
- A) 4 $\to$ 6 $\to$ 2 $\to$ 1 $\to$ 3 $\to$ 5
- B) 6 $\to$ 4 $\to$ 1 $\to$ 2 $\to$ 3 $\to$ 5
- C) 2 $\to$ 4 $\to$ 6 $\to$ 1 $\to$ 3 $\to$ 5
- D) 4 $\to$ 2 $\to$ 6 $\to$ 1 $\to$ 5 $\to$ 3

**Correct Answer:** A) 4 $\to$ 6 $\to$ 2 $\to$ 1 $\to$ 3 $\to$ 5

**Detailed Solution & Mathematical Derivation:**
The standard Global 8D (Eight Disciplines) sequence:
- **D0**: Prepare / Plan emergency response.
- **D1**: Form multi-disciplinary team.
- **D2**: Describe problem using $5\text{W}2\text{H}$ (Who, What, Where, When, Why, How, How many).
- **D3**: Develop & verify Interim Containment Actions (ICA) (quarantine warehouse stock, stop shipment).
- **D4**: Identify and verify Root Cause and Escape Point (5-Whys, Fishbone, DOE).
- **D5**: Select and verify Permanent Corrective Action (PCA).
- **D6**: Implement and validate PCA (control plan update, line trials).
- **D7**: Prevent recurrence (update DFMEA, PFMEA, design rules, standard work).
- **D8**: Recognize team contributions.

---

### Question 10: Fishbone (Ishikawa) 6M Analysis
**Question:** In root cause investigation of high scrap rate due to paint peeling on injection molded body panels, an engineer categorizes potential causes under the "6M" framework. Which of the following matches correctly?
- A) Machine: Oven temperature controller thermocouple decalibrated; Material: Inadequate flame treatment surface tension ($< 38\text{ dynes/cm}$); Method: Robot spray gun pass overlap percentage incorrect.
- B) Machine: Polypropylene resin batch change; Material: Conveyor chain speed fluctuation; Measurement: Ambient humidity.
- C) Man: Robot program velocity; Milieu (Environment): Operator fatigue.
- D) Method: Mold steel grade; Material: Shift handover duration.

**Correct Answer:** A) Machine: Oven temperature controller thermocouple decalibrated; Material: Inadequate flame treatment surface tension ($< 38\text{ dynes/cm}$); Method: Robot spray gun pass overlap percentage incorrect.

**Detailed Solution & Mathematical Derivation:**
The standard automotive manufacturing 6M categories:
1. **Machine**: Equipment, tooling, robots, spray guns, temperature controllers, chillers.
2. **Material**: Raw polymers, solvent purity, surface tension, virgin-to-regrind ratio.
3. **Method**: Process parameters, spray overlap, curing time, transfer speed, standard operating procedures.
4. **Measurement**: DFT gauge calibration, gloss meter, cross-hatch cutter wear.
5. **Milieu (Environment)**: Humidity, cleanroom airborne particle count, booth ambient temperature.
6. **Man (People)**: Operator training, technique, inspection compliance.

---

### Questions 11–35: Rapid Technical Quality Mastery

#### Question 11: Little's Law in Line Balancing
**Question:** An automated pack assembly buffer contains an average Work-in-Progress ($WIP$) of $60$ battery packs. The line throughput is $120$ packs per hour. By Little's Law ($WIP = \text{Throughput} \times \text{Flow Time}$), what is the average flow time of a pack through this buffer?
- A) $30\text{ seconds}$
- B) $30\text{ minutes}$
- C) $2\text{ hours}$
- D) $15\text{ minutes}$
*Answer:* B. $\text{Flow Time} = WIP / \text{Throughput} = 60 / 120\text{ hr} = 0.5\text{ hr} = 30\text{ minutes}$.

#### Question 12: $P_p / P_{pk}$ vs $C_p / C_{pk}$
**Question:** What is the fundamental mathematical and operational difference between $C_{pk}$ and $P_{pk}$ in automotive PPAP (Production Part Approval Process)?
- A) $C_{pk}$ uses long-term overall standard deviation ($\sigma_{\text{overall}} = s$); $P_{pk}$ uses short-term within-subgroup variation ($\bar{R}/d_2$).
- B) $C_{pk}$ evaluates short-term inherent process capability using within-subgroup variation ($\hat{\sigma}_{\text{within}} = \bar{R}/d_2$ or $\bar{s}/c_4$); $P_{pk}$ evaluates overall long-term process performance using sample standard deviation ($s_{\text{overall}}$) including shift-to-shift and lot-to-lot variation.
- C) $P_{pk}$ is only used for non-metallic parts.
- D) $C_{pk}$ can only be calculated when the process has zero defects.
*Answer:* B. Automotive standard: $P_{pk} \ge 1.67$ for initial PPAP sampling; $C_{pk} \ge 1.33$ for regular production.

#### Question 13: Type I vs Type II Error in SPC
**Question:** On a Shewhart control chart, a "Type I error" ($\alpha$) occurs when:
- A) An out-of-control condition is missed.
- B) A point falls outside the $3\sigma$ control limits purely by random chance, causing engineers to look for an assignable cause when the process is actually in statistical control (False Alarm, $\alpha = 0.27\%$).
- C) The machine breaks down.
- D) The gauge is dropped on the floor.
*Answer:* B. For $3\sigma$ limits, $\alpha = 2 \times (1 - \Phi(3)) = 0.0027 = 0.27\%$.

#### Question 14: Poka-Yoke (Mistake Proofing) Classification
**Question:** An assembly station for battery terminal bolts uses a torque wrench linked to a PLC. If the operator attempts to advance the conveyor without torqueing all 12 bolts to exactly $9.5 \pm 0.5\text{ N}\cdot\text{m}$, the pneumatic pallet clamp refuses to release and sounds an alarm. What level of Poka-yoke is this?
- A) Warning-only Poka-yoke
- B) Control / Shut-out Poka-yoke (Level 1: prevents nonconforming product from being produced or passed to the next station)
- C) Visual inspection checklist
- D) Sampling audit
*Answer:* B. Interlocking physical/electrical systems that prevent progression are fail-safe control Poka-yokes.

#### Question 15: Gauge R&R (Measurement System Analysis)
**Question:** In an automotive MSA study of a digital bore gauge measuring rotor bearing diameters:
- $\%GRR < 10\%$: Measurement system is fully acceptable.
- $10\% \le \%GRR \le 30\%$: Acceptable based on application criticality and cost.
- $\%GRR > 30\%$: Unacceptable; gauge system must be redesigned or recalibrated.
If a gauge study yields $\%GRR = 42\%$, what does this mean?
- A) $42\%$ of parts are scrap.
- B) The measurement system accounts for $42\%$ of total observed process variation, rendering the data unreliable for process control.
- C) The tool is $42\%$ faster than manual calipers.
- D) Machine accuracy is $99.58\%$.
*Answer:* B. Excessive gauge variation masks real process variation.

#### Question 16: $u$-Chart vs $c$-Chart
**Question:** When counting the total number of paint surface defects (blemishes, dirt seeds, runs) on scooter chassis panels where the surface area inspected varies significantly from sub-assembly to sub-assembly, which control chart must be used?
- A) $c$-chart
- B) $u$-chart (defects per unit area with variable inspection unit size)
- C) $p$-chart
- D) $\bar{X}-S$ chart
*Answer:* B. $c$-chart requires constant inspection sample size; $u$-chart handles varying inspection sample size.

#### Question 17: DMAIC — "Measure" vs "Analyze" Phase Deliverable
**Question:** In a Six Sigma DMAIC project to reduce battery pack enclosure leak failures:
- A) Measure delivers Root Cause; Analyze delivers Control Plan.
- B) Measure delivers Baseline Process Capability and Gauge R&R validation; Analyze delivers statistically proven Vital Few Root Causes ($X$'s) using hypothesis testing/ANOVA.
- C) Measure delivers permanent mechanical drawings.
- D) Analyze executes production line shutdowns.
*Answer:* B. Measure establishes baseline and measurement validity; Analyze isolates critical inputs ($X$'s).

#### Question 18: Pareto 80/20 Rule
**Question:** In analyzing 1,000 recorded defects across the S1 assembly line, 820 defects belong to just two categories: "harness pin unseated" and "torque mark missing". A Pareto analysis directs engineering to:
- A) Spend equal time on all 18 defect categories.
- B) Prioritize resources exclusively on the "vital few" two root causes that drive $82\%$ of total losses.
- C) Re-label defects as acceptable.
- D) Discontinue recording data.
*Answer:* B. Focus on the vital few rather than the trivial many.

#### Question 19: Single Minute Exchange of Die (SMED)
**Question:** In Shigeo Shingo's SMED methodology for rapid press stamping tool changeovers:
- A) All tooling setup must be done after the press is stopped.
- B) "Internal setup" operations (done only while the press is stopped) are converted into "External setup" operations (prepared while the press is still running).
- C) Stamping speeds are increased by $10\times$.
- D) Operators work without safety interlocks.
*Answer:* B. Pre-staging dies, preheating tools, and standardized clamping hardware slash changeover from hours to under 10 minutes.

#### Question 20: Andon System
**Question:** On an automated scooter final assembly conveyor, an operator pulls the Andon cord when a wire harness connector will not latch. What is the immediate lean protocol?
- A) The operator is penalized for stopping the line.
- B) The line leader is alerted immediately via audible chime/board; if not resolved within takt time cycle, the line stops to prevent passing a defective vehicle downstream.
- C) The part is bypassed and ignored.
- D) The conveyor speed is doubled.
*Answer:* B. Jidoka / Autonomation principles mandate stopping the line to fix defects immediately at the source.

#### Question 21: Six Sigma Shift Assumption
**Question:** In classical Motorola Six Sigma theory, a $6\sigma$ process with a standard $1.5\sigma$ long-term mean shift yields how many defects per million opportunities (DPMO)?
- A) $0.001\text{ DPMO}$
- B) $3.4\text{ DPMO}$
- C) $66,807\text{ DPMO}$
- D) $2,700\text{ DPMO}$
*Answer:* B. $\Phi(6 - 1.5) = \Phi(4.5) \implies 1 - 0.9999966 = 3.4\text{ PPM}$.

#### Question 22: FMEA — Severity Ranking of 10
**Question:** In an automotive DFMEA for an electric scooter powertrain, what failure consequence strictly receives a Severity ($S$) ranking of 10?
- A) Vehicle color mismatch visible only under direct sunlight.
- B) Failure to meet customer cosmetic expectations with dealer rework.
- C) Catastrophic loss of primary steering or uncontrolled acceleration/fire violating federal safety standards without prior warning to the rider.
- D) Radio volume knob loose.
*Answer:* C. Severity 10 is reserved for safety and regulatory non-compliance without warning.

#### Question 23: Hypothesis Testing — ANOVA (Analysis of Variance)
**Question:** A manufacturing engineer wants to compare the mean tensile shear strength of laser welds across 3 different laser power settings ($2.5\text{ kW}, 3.0\text{ kW}, 3.5\text{ kW}$). Which statistical test is appropriate?
- A) 1-sample $Z$-test
- B) One-Way ANOVA (testing $H_0: \mu_1 = \mu_2 = \mu_3$ vs $H_1:$ at least one mean differs)
- C) Chi-Square test of independence
- D) Mann-Whitney U test
*Answer:* B. ANOVA tests equality of means across three or more treatment groups using $F$-statistic.

#### Question 24: $p$-value Interpretation
**Question:** In regression analysis evaluating the effect of injection mold temperature on battery box warpage, the calculated $p$-value for the temperature coefficient is $0.002$. At an $\alpha = 0.05$ significance level:
- A) Reject the null hypothesis; mold temperature has a statistically significant effect on warpage.
- B) Fail to reject the null hypothesis; temperature is irrelevant.
- C) The model has a $99.8\%$ error rate.
- D) Mold temperature should be ignored.
*Answer:* A. $p = 0.002 < 0.05 \implies$ statistically significant evidence against $H_0$.

#### Question 25: 5-Whys Methodology Pitfall
**Question:** What is the primary common error when conducting a "5-Whys" root cause analysis in a manufacturing plant?
- A) Asking why too many times.
- B) Stopping at human error ("operator was careless") instead of drilling down into systemic process, training, or mistake-proofing (Poka-yoke) failures.
- C) Involving machine operators.
- D) Writing down the findings.
*Answer:* B. "Human error" is never the root cause; lack of ergonomic design, unclear visual standards, or absence of mistake-proofing is the systemic root cause.

#### Question 26: Gemba Walk
**Question:** What is the fundamental objective of an operations leader conducting a "Gemba" walk at Futurefactory?
- A) To sit in the executive office and review Excel reports.
- B) To go to the actual workplace ("the real place"), observe the value-adding process firsthand, engage with operators, and identify waste and safety risks directly.
- C) To conduct formal disciplinary hearings.
- D) To inspect the cafeteria food.
*Answer:* B. Lean principle: Go see, ask why, show respect.

#### Question 27: 7 Wastes (Muda)
**Question:** An assembly cell has finished sub-assemblies piled up between Station 3 and Station 4 waiting for the next operation because Station 4 is slower. Under Toyota Production System (TPS) Muda classification, this waste is:
- A) Overprocessing
- B) Work-in-Progress (WIP) Inventory / Waiting
- C) Motion
- D) Transportation
*Answer:* B. Excess inventory ties up working capital, risks transit damage, and hides upstream quality defects.

#### Question 28: Kan-ban Principle
**Question:** In a pull production system supplying battery modules to the vehicle assembly line, what does an empty physical or electronic Kanban card authorize?
- A) Authorized overtime for the line supervisor.
- B) Authorization to the upstream workstation to produce or move exactly one replenishment container of parts.
- C) Immediate shutdown of the entire factory.
- D) Discarding scrap parts.
*Answer:* B. Kanban prevents overproduction by only authorizing production upon downstream consumption.

#### Question 29: $C_p$ with One-Sided Specification
**Question:** For a weld tensile pull test where only a Lower Specification Limit exists ($\text{LSL} = 12.0\text{ kN}$, no upper limit):
- A) $C_p$ cannot be defined, and capability is evaluated solely by $C_{pk} = C_{pl} = (\mu - \text{LSL})/(3\sigma)$.
- B) $C_p$ is assumed to be infinity.
- C) The test is invalid.
- D) $C_p = 0$.
*Answer:* A. For single-sided tolerances, capability is evaluated via $C_{pu}$ or $C_{pl}$.

#### Question 30: Common Cause vs Special Cause Variation
**Question:** Dr. W. Edwards Deming demonstrated that attempting to adjust a machine in response to "common cause" (inherent random) variation:
- A) Eliminates all variation.
- B) Increases total process variation (tampering / over-adjustment) and degrades capability.
- C) Triples the machine speed.
- D) Is standard Six Sigma practice.
*Answer:* B. Tampering with an in-control stable process increases variance; process redesign is required to reduce common-cause variation.

#### Question 31: Run Chart Trend Rule
**Question:** On an SPC run chart, how many consecutive increasing or decreasing points constitute a statistically significant "trend"?
- A) 3 points
- B) 6 or 7 consecutive points continuously rising or falling
- C) 20 points
- D) 2 points
*Answer:* B. A continuous monotonic run of 6 or 7 points indicates a tool wear or thermal drift trend.

#### Question 32: Design of Experiments (DOE) — Orthogonal Arrays
**Question:** Why does an advanced manufacturing engineer use Taguchi Orthogonal Arrays ($L_8, L_9, L_{16}$) instead of One-Factor-At-A-Time (OFAT) testing?
- A) DOE tests factors in fewer total runs while identifying interaction effects between process variables.
- B) Taguchi arrays do not require physical testing.
- C) OFAT is illegal under ISO 9001.
- D) Taguchi testing only works on plastics.
*Answer:* A. Efficient exploration of multi-factor parameter space and factor interactions.

#### Question 33: Kaizen Principle
**Question:** "Kaizen" in the context of Ola Electric manufacturing operations refers to:
- A) A one-time multi-million dollar capital expenditure project.
- B) Continuous, incremental improvement involving all employees from shop-floor associates to plant directors.
- C) Complete automation without human labor.
- D) Outsourcing manufacturing to third parties.
*Answer:* B. Incremental, relentless elimination of waste and friction.

#### Question 34: Standard Operating Procedure (SOP) Visual Standards
**Question:** Why are visual One-Point Lessons (OPLs) and photo-based SOPs mounted directly at assembly stations?
- A) To decorate the station.
- B) To ensure process reproducibility across shifts, standardize takt-time execution, and provide clear "Good vs No-Good" visual boundary samples.
- C) To pass audits without reading.
- D) To replace automated sensors.
*Answer:* B. Visual management establishes unequivocal operational standards.

#### Question 35: Cost of Poor Quality (COPQ)
**Question:** In financial quality management, which category represents the highest unit cost and severe brand equity erosion?
- A) Prevention Costs (DFMEA, training)
- B) Appraisal Costs (CMM inspection, lab testing)
- C) Internal Failure Costs (in-plant scrap and rework)
- D) External Failure Costs (field recalls, CCPA warranty litigation, customer roadside breakdowns)
*Answer:* D. External failures cost $10\text{--}100\times$ more than catching defects internally.

