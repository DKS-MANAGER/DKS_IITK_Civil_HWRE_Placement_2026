# Practical Engineering Scenarios & Troubleshooting Playbook

## Overview and Role Alignment
During Ola Electric technical interview rounds for Product Engineering & Advanced Manufacturing, candidates are evaluated on their ability to resolve **real-world, open-ended plant and product engineering crises**. 

These 8 scenarios evaluate your first-principles physics grounding, structured root-cause analysis (8D / 5-Whys / Fishbone), manufacturing diagnostics, and cross-functional decision-making.

---

### Scenario 1: Suspension Component Fatigue Fracture Under Real-World Rough-Road Usage
**Scenario:**
Three months post-launch, customer field telemetry and service centers report micro-cracks and three isolated brittle fractures at the upper steering-arm mounting boss of an electric scooter during high-speed pothole impacts in Tier-2 Indian cities. The original component passed 100,000 cycles on the lab multi-axis shaker rig without failure. As the GET in chassis engineering, how do you investigate and solve this crisis?

**Structured Resolution Approach:**
1. **Immediate Containment (D3):**
   - Issue a technical service bulletin to inspect all vehicles undergoing service using non-destructive dye penetrant inspection (DPI) around the mounting boss.
   - Quarantine warehouse sub-assemblies and freeze production lot shipments pending metallurgical sign-off.
2. **Root Cause Analysis (D4) — Lab vs Field Discrepancy:**
   - *SEM Fractography:* Section the failed field part and examine under Scanning Electron Microscopy. Observe striation marks indicating high-cycle fatigue initiating from a sharp machining notch at the fillet radius, transitioning to rapid cleavage failure.
   - *Road Load Data Acquisition (RLDA):* Mount tri-axial strain gauges and accelerometers onto test scooters driven across actual rough rural Indian roads. Discrepancy identified: The lab shaker rig applied pure vertical sinusoidal vibration ($F_z$), whereas rough-road pothole impacts create severe **multi-axial combined torsional ($T_x$) and longitudinal brake-impact shock loads ($F_y$) with shock acceleration spikes up to $5.5g$** (vs $2.5g$ modeled in lab).
   - *Casting Inspection:* Metallurgical cross-section reveals coarse eutectic silicon needles and gas porosity concentrated at the thick mounting boss due to delayed solidification.
3. **Engineering Redesign & Permanent Corrective Action (D5/D6):**
   - *Geometry:* Increase fillet radius from $R = 1.5\text{ mm}$ to $R = 4.0\text{ mm}$ to reduce the geometric stress concentration factor from $K_t = 2.4$ down to $K_t = 1.35$.
   - *Casting Tooling:* Add a conformal copper chill pin in the HPDC die to accelerate local heat extraction at the boss, eliminating shrinkage porosity. Specify Strontium ($Sr$) eutectic modification ($180\text{ ppm}$) to ensure fibrous ductile silicon morphology.
   - *Surface Treatment:* Introduce shot-peening on the fillet radius to impart surface compressive residual stress ($-300\text{ MPa}$), pushing fatigue endurance comfortably above peak rough-road stress cycles.

---

### Scenario 2: HPDC Motor Housing Porosity Causing Transmission Oil Leakage
**Scenario:**
At the motor assembly plant, $8.5\%$ of die-cast aluminum reduction gearbox motor housings fail the end-of-line pressurized air-decay leak test ($2.0\text{ bar}$ pneumatic pressure drop $> 0.05\text{ bar/min}$), indicating through-wall porosity. Scrapping these fully machined housings costs ₹12 Lakhs weekly. How do you eliminate this defect?

**Structured Resolution Approach:**
1. **Defect Characterization:**
   - Cut sections through leaking housings and perform Industrial CT scanning.
   - Distinguish whether leak paths are caused by **Gas Porosity** (smooth, round bubbles from air/steam entrainment) or **Shrinkage Porosity** (jagged, sponge-like voids between dendrites).
   - *Finding:* Smooth spherical voids are found concentrated along the runner entry and mating face, alongside micro-shrinkage at the thick bearing boss.
2. **Process Diagnostics & Parameter Optimization:**
   - *Shot Sleeve Filling Ratio:* The shot sleeve is only filled to $38\%$ by volume before plunger advance. The slow shot plunger creates a breaking wave that rolls over, trapping large volumes of air in the melt before entering the runner.
   - *Solution:* Increase sleeve fill ratio to $65\%$ by sizing a smaller diameter sleeve or increasing ladle pour volume. Optimize the slow-shot velocity profile ($v_1 = 0.18\text{ m/s}$) to push a smooth, unbroken meniscus up to the runner gate.
   - *Vacuum-Assist System:* Check die vacuum pulling system. Found that vacuum valve filters were clogged with die lubricant residue, resulting in cavity pressure of $250\text{ mbar}$ instead of the mandated $< 50\text{ mbar}$. Overhaul vacuum lines and implement automated vacuum pressure sensor logging on every shot.
   - *Rotary Degassing:* Verify hydrogen content in the central melting furnace using reduced pressure test (RPT). Hydrogen density was $0.28\text{ cm}^3/100\text{g}$; optimize rotary nitrogen impeller degassing with fluxing to bring dissolved hydrogen strictly below $0.12\text{ cm}^3/100\text{g}$.
3. **Verification:**
   - Post-implementation production run of 500 consecutive housings shows leak-test rejection rate drops from $8.5\%$ to $0.15\%$, achieving Six Sigma process stability.

---

### Scenario 3: Spot-Welded Chassis Joint Fatigue Failure Under Cyclic Shock
**Scenario:**
During a 15,000 km accelerated durability test of a newly designed steel battery cradle sub-assembly, robotic resistance spot welds (RSW) between two $1.5\text{ mm}$ CRCA steel gusset plates fail via weld nugget pull-out. The welding robot program has not changed. Why did this happen, and what is your engineering countermeasure?

**Structured Resolution Approach:**
1. **Immediate Inspection & Root Cause:**
   - Measure actual weld nugget diameter via chisel testing and metallographic peel testing.
   - Standard minimum automotive nugget diameter: $d_{\min} = 4\sqrt{t} = 4\sqrt{1.5} \approx 4.9\text{ mm}$.
   - *Observation:* Field failure nuggets measure only $3.2\text{ mm}$ with severe interfacial expulsion flash around the weld perimeter.
   - *Root Cause 1 (Electrode Mushrooming):* The copper-chromium-zirconium (CuCrZr) welding electrode tips have deformed and flattened ("mushroomed") after 1,800 welds without tip dressing. The contact tip diameter expanded from $6\text{ mm}$ to $8.8\text{ mm}$, lowering the effective welding current density ($J = I / A$) by $53\%$.
   - *Root Cause 2 (Part Fit-up Gap):* A stamped gusset sheet metal tolerance drift created a $1.2\text{ mm}$ air gap between sheets prior to welding. Substantial electrode force was wasted purely bending the sheets together, reducing effective interfacial clamping pressure and causing violent liquid metal expulsion.
2. **Permanent Engineering Countermeasures:**
   - *Automated Tip Dresser:* Install an in-cell pneumatic robotic tip dresser programed to redress electrode geometry every 250 weld cycles.
   - *Adaptive Weld Controller:* Upgrade weld timers to constant current controllers with dynamic resistance feedback ($R_{\text{dyn}}$); if sheet gap or tip wear changes resistance, the controller automatically adjusts current and weld cycle time in real time.
   - *Stamping Die Correction:* Recalibrate the progressive stamping die to eliminate springback, ensuring sheet-to-sheet mating gap is strictly $< 0.3\text{ mm}$.

---

### Scenario 4: Cosmetic Injection Molded Cowl Panel Warpage and Sink Marks
**Scenario:**
The front painted handlebar cowl made of injection-molded PC/ABS exhibits two severe quality defects upon demolding: (1) Out-of-flatness warpage of $3.5\text{ mm}$ (drawing allows $\pm 1.0\text{ mm}$), preventing flush snap-fit assembly with the headlight; and (2) Noticeable localized surface depressions (sink marks) on the high-gloss exterior directly opposite internal clip-mounting ribs.

**Structured Resolution Approach:**
1. **Root-Cause Analysis — Sink Marks:**
   - *DFM Violation:* 3D CAD inspection reveals that the internal clip-mounting rib has a base thickness of $t_{\text{rib}} = 2.2\text{ mm}$, while the nominal cosmetic outer wall is $t_{\text{wall}} = 2.5\text{ mm}$ ($t_{\text{rib}} / t_{\text{wall}} = 88\%$).
   - *Physics:* The intersection forms a thick localized thermal core. As the outer skin solidifies, the slower-cooling molten interior contracts, pulling the soft exterior skin inward to create a visible depression.
   - *Corrective Action:* Modify mold tooling core inserts to reduce rib base thickness to $1.1\text{ mm}$ ($44\%$ of nominal wall), adding a $1.5^\circ$ draft angle and small $0.5\text{ mm}$ root fillet.
2. **Root-Cause Analysis — Warpage:**
   - *Differential Cooling:* Thermal imaging of the mold tool reveals that the core half is running at $75^\circ\text{C}$ while the cavity half is running at $45^\circ\text{C}$ due to a clogged cooling baffle.
   - *Physics:* The hotter side cools slower and undergoes higher volumetric shrinkage, creating an asymmetric bending moment that curls the part upon ejection.
   - *Corrective Action:* Clean and descale the cooling channels; balance water chiller manifold flow rates so core and cavity temperatures are within $\pm 2^\circ\text{C}$ ($55^\circ\text{C}$ target). Increase holding pressure from $35\text{ MPa}$ to $50\text{ MPa}$ and holding time by $2.0\text{ seconds}$ to compensate for volumetric shrinkage before gate freeze-off.

---

### Scenario 5: Assembly Line Bottleneck Producing a 20% Output Deficit
**Scenario:**
The S1 final assembly line at Futurefactory has a daily production target of 1,600 vehicles across two shifts (Takt time $= 32.6\text{ seconds}$). However, the line is capped at 1,280 vehicles/day ($20\%$ deficit). Station 4 (Motor & Drivetrain Mounting) has an observed cycle time of $41.0\text{ seconds}$, starving downstream stations and causing upstream buffer line jams. How do you optimize this line without capital equipment purchase?

**Structured Resolution Approach:**
1. **Time & Motion Study (MOST / Maynard Operation Sequence Technique):**
   - Dissect the $41.0\text{ second}$ work sequence at Station 4 into micro-tasks:
     - Task 4a: Retrieve motor from supply tote: $5.0\text{ s}$
     - Task 4b: Align motor onto chassis dowel pins: $6.0\text{ s}$
     - Task 4c: Manually hand-thread 4 mounting bolts: $11.0\text{ s}$
     - Task 4d: Use DC electric torque tool to tighten 4 bolts to $28\text{ N}\cdot\text{m}$: $14.0\text{ s}$
     - Task 4e: Visual inspection & torque paint-pen marking: $5.0\text{ s}$
2. **Kaizen & Line Rebalancing Actions:**
   - *Eliminate Hand-Threading (Save $7\text{ s}$):* Replace standard hex bolts with "dog-point" pilot lead bolts and provide magnetic multi-spindle socket heads, allowing operators to power-drive bolts directly without pre-hand-threading.
   - *Kitting / Sub-Assembly Offload (Save $5\text{ s}$):* Pre-stage the motor on an automated guided vehicle (AGV) with fasteners pre-located in a kitting tray at ergonomic waist height, eliminating reaching motion.
   - *Task Offloading to Starved Adjacent Stations (Save $5\text{ s}$):* Move Task 4e (visual inspection and torque marking) to Station 5 (Suspension Mount), which currently has an idle cycle time of only $22.0\text{ seconds}$.
3. **Outcome:**
   - Station 4 cycle time is reduced from $41.0\text{ seconds}$ down to **$29.0\text{ seconds}$** ($< \text{Takt time of } 32.6\text{ s}$).
   - Line balancing efficiency jumps from $79.5\%$ to $94.2\%$, unlocking plant capacity to produce $1,650\text{ units/day}$ and completely eliminating the $20\%$ deficit.

---

### Scenario 6: Discrepancy Between FEA Simulation ($120\text{ MPa}$) and Physical Test ($210\text{ MPa}$)
**Scenario:**
Finite Element Analysis (FEA) of an aluminum battery mounting bracket predicted a maximum Von Mises stress of $120\text{ MPa}$ under a $3g$ vertical shock load. However, physical testing on a prototype frame fitted with a 3-axis rosette strain gauge measures an actual peak stress of $210\text{ MPa}$—exceeding the yield strength and causing plastic yielding. Why does this discrepancy exist, and how do you resolve it?

**Structured Resolution Approach:**
1. **Audit FEA Assumptions vs Physical Reality:**
   - *Boundary Conditions (The #1 Source of Error):* In the FEA model, the mounting bracket holes were modeled as "rigidly fixed" ($U_x = U_y = U_z = 0$). In physical reality, the tubular frame onto which the bracket is bolted is compliant and deflects under load, inducing unintended secondary prying moments and torsion into the bracket.
   - *Bolt Modeling:* The FEA model merged the bracket to the frame with shared nodes (idealized continuous bond). The real bracket is clamped with an M8 bolt with clearance hole ($9\text{ mm}$ hole in bracket). Under load, micro-slip occurred until the bolt shank contacted the hole edge, generating concentrated bearing and prying stresses.
   - *Mesh Discretization:* The FEA used coarse 1st-order tetrahedral solid elements (C3D4) with only 1 element through the thickness, artificially suppressing bending stress due to volumetric/shear locking.
2. **Corrective Modeling & Validation Protocol:**
   - Re-mesh the bracket using quadratic elements (C3D10 or 2nd-order shell elements S8R) with at least 3 elements through the thickness.
   - Model the bolted connection explicitly with contact surfaces, bolt preload ($F_i = 18\text{ kN}$), and frictional contact ($\mu = 0.25$).
   - Include the surrounding tubular frame in the FEA assembly to capture realistic compliance.
3. **Convergence:**
   - The updated FEA model predicts peak stress of $204\text{ MPa}$, correlating within $3\%$ of the physical strain-gauge reading ($210\text{ MPa}$).
   - *Engineering Solution:* Add a $2.0\text{ mm}$ stamped gusset rib to the bracket to increase section modulus $Z$, reducing physical stress to $115\text{ MPa}$ ($SF = 2.4$).

---

### Scenario 7: High Process Capability ($C_p = 2.1$) But Unacceptable Performance ($C_{pk} = 0.95$)
**Scenario:**
An automated CNC turning lathe machines the bearing seat diameter of traction motor shafts ($\text{Specification: } 35.000 \pm 0.020\text{ mm}$). Statistical analysis of 100 consecutive shafts yields $C_p = 2.10$, but $C_{pk} = 0.95$. What is happening physically on the shop floor, and what is your immediate corrective intervention?

**Structured Resolution Approach:**
1. **Mathematical Interpretation:**
   - $C_p = \frac{\text{USL} - \text{LSL}}{6\hat{\sigma}} = \frac{0.040}{6\hat{\sigma}} = 2.10 \implies \hat{\sigma} = \frac{0.040}{12.6} \approx 0.00317\text{ mm}$.
   - The inherent process variation is exceptionally small ($6\sigma = 0.019\text{ mm} < \text{Tolerance } 0.040\text{ mm}$). The machine is capable of Six Sigma precision!
   - However, $C_{pk} = \min(C_{pu}, C_{pl}) = 0.95$.
   - Since $C_{pk} = C_p (1 - k)$:
     $$1 - k = \frac{0.95}{2.10} \approx 0.452 \implies k = 0.548$$
   - The process mean is heavily shifted off-center by:
     $$\Delta \mu = k \times \frac{\text{Tolerance}}{2} = 0.548 \times 0.020 = 0.011\text{ mm}$$
   - The actual mean is running at $\bar{X} \approx 35.011\text{ mm}$ (near the USL).
2. **Shop Floor Investigation:**
   - *Root Cause 1 (Thermal Spindle Growth):* The CNC lathe spindle warms up during continuous operation, causing axial and radial thermal expansion of the spindle bearings, pushing the turning insert away from the part.
   - *Root Cause 2 (Tool Wear Offset Error):* The machinist entered a tool geometry wear offset compensation incorrectly during the morning shift changeover.
3. **Corrective Intervention:**
   - Stop production and inspect the tool offset register on the Fanuc/Siemens CNC controller.
   - Apply a negative radial tool offset of $\Delta X = -0.011\text{ mm}$ to re-center the mean precisely at nominal $35.000\text{ mm}$.
   - Enable the CNC machine's automated thermal compensation macro or program a 15-minute spindle warm-up cycle prior to production startup.
   - *Result:* Post-adjustment verification yields $\bar{X} = 35.001\text{ mm}$, elevating $C_{pk}$ to $2.01$, eliminating all out-of-tolerance scrap.

---

### Scenario 8: Complex Trade-off — Lightweighting vs Crash Intrusion vs Cost in Battery Enclosures
**Scenario:**
Ola’s product management targets reducing the curb weight of the S1 scooter by $4.0\text{ kg}$ to boost certified range by $7\text{ km}$. The design team proposes replacing the current $2.5\text{ mm}$ cast aluminum (AlSi10Mg) battery bottom enclosure tray with a $1.8\text{ mm}$ stampable glass-fiber reinforced polypropylene composite (GF-PP) or thinner aluminum. However, the enclosure must withstand AIS-156 mechanical drop and curb-strike puncture tests without cell intrusion. As the GET, how do you structure this multi-variable engineering trade-off?

**Structured Decision-Making Matrix:**

| Evaluation Metric | Option A: Current Cast Al (AlSi10Mg, 2.5 mm) | Option B: Thin Cast Al with Ribs (1.8 mm + Stiffeners) | Option C: Thermoplastic Composite (GF-PP 30%) | Option D: Hybrid Al Base + Composite Lid |
|:---|:---:|:---:|:---:|:---:|
| **Mass Reduction** | Baseline ($0.0\text{ kg}$) | **$-1.8\text{ kg}$** | **$-3.6\text{ kg}$** | **$-2.4\text{ kg}$** |
| **Tooling CapEx** | ₹0 (Existing Die) | ₹45 Lakhs (Die rework) | ₹1.2 Crores (New compression mold) | ₹65 Lakhs |
| **Piece Cost (BOM)** | Baseline | $-8\%$ (less alloy) | $+35\%$ (expensive resin) | $+12\%$ |
| **Puncture Resistance (AIS-156)** | High (Ductile yield) | High (Tested with ribs) | Low (Risk of localized fiber shear) | High |
| **Thermal Conductivity ($\kappa$)** | High ($140\text{ W/m}\cdot\text{K}$) | High ($140\text{ W/m}\cdot\text{K}$) | Terrible ($0.3\text{ W/m}\cdot\text{K}$ — traps heat!) | Bottom cooling intact |
| **IP67 Sealing Stability** | Superior (Stiff flange) | Excellent | Creep under bolt torque ($T_g$) | Excellent |

**Engineering Recommendation:**
1. **Reject Option C (Pure Composite):** While it achieves the $4\text{ kg}$ weight target, its near-zero thermal conductivity ($\kappa = 0.3\text{ W/m}\cdot\text{K}$) prevents bottom liquid/conductive heat dissipation, leading to cell overheating. Furthermore, polymer creep under bolt preloads over 3 years causes gasket relaxation and water ingress (violating IP67).
2. **Adopt Option D (Hybrid Architecture):**
   - Retain the **aluminum bottom plate** (thinned to $2.0\text{ mm}$ with FEA-optimized topology stiffening ribs), maintaining high crash puncture protection and battery cold-plate heat transfer.
   - Replace the heavy cast aluminum **top lid cover** with lightweight injection-molded flame-retardant polyamide/polypropylene (PA66-GF30 with UL-94 V-0 rating), as the top lid carries zero ground impact loads.
   - *Result:* Delivers **$2.5\text{ kg}$ net weight reduction**, maintains 100% AIS-156 crash and thermal compliance, preserves IP67 hermeticity with metal compression limiters, and fits within existing assembly line cycle times.

