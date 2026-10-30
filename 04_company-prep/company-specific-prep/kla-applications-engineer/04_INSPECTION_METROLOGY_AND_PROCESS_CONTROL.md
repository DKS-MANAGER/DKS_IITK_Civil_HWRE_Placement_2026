# Module 04: Inspection, Metrology & Process Control
## Optical Physics, Defect Detection Algorithms, Metrology Systems & Statistical Process Control (SPC)

> **Document Status**: Authoritative Technical Syllabus  
> **Relevant Business Units**: Wafer Inspection Group (WIN), Patterning Division, Klarity Analytics  
> **Target Role**: Customer Applications Engineer (CAE)  
> **Placement Cycle**: IIT Kanpur Placement Season 2026–27 | Phase 1  

---

## 1. Physical Principles of Optical Wafer Inspection

KLA's market leadership rests on optical inspection systems (e.g., 29xx, 39xx, Surfscan) that scan 300 mm wafers at high speed while resolving defects smaller than 20 nanometers.

### 1.1 Brightfield vs. Darkfield Inspection Architecture

```
       BRIGHTFIELD (BF) OPTICS                    DARKFIELD (DF) OPTICS
       ───────────────────────                    ─────────────────────
           Light Source                                Light Source
                │ (Normal)                                  \ (Oblique Angle)
                ▼                                            \
       ┌─────────────────┐                                    ▼
       │ Polarizer / N.A.│                               ┌───────────────┐
       └────────┬────────┘                               │ Wafer Surface │
                │                                        └───────┬───────┘
                ▼                                                │ (Scattered
       ┌─────────────────┐                                       │  Light Only)
       │ Wafer Surface   │                                       ▼
       └────────┬────────┘                               ┌───────────────┐
                │ (Specular Reflection)                  │ Off-Axis Lens │
                ▼                                        └───────┬───────┘
       ┌─────────────────┐                                       ▼
       │ Detector / CCD  │                               ┌───────────────┐
       └─────────────────┘                               │ Photomultiplier
                                                         └───────────────┘
```

| Parameter | Brightfield (BF) Inspection | Darkfield (DF) Inspection |
| :--- | :--- | :--- |
| **Illumination Angle** | Normal (perpendicular) or near-normal to wafer surface. | Oblique, grazing angle ($\sim 10^\circ - 30^\circ$ from surface). |
| **Collected Light** | Direct **specular reflection** and low-order diffracted light. | Only **scattered light** from defects; specular beam is blocked. |
| **Background Appearance** | Flat surfaces appear bright/luminous; patterns create contrast. | Flat clean surface appears completely black (zero background). |
| **Sensitivity Profile** | Superior for **complex patterned features**, film thickness variations, subtle color shifts, and micro-bridges. | Superior for **isolated particles, surface scratches, and pits** due to near-infinite contrast on flat zones. |
| **Dominant Physics** | Wave interference, diffraction gratings, point spread function. | Rayleigh scattering ($I \propto d^6 / \lambda^4$) and Mie scattering. |
| **Typical Tools** | KLA 29xx / 39xx Broadband Plasma Optical (BPO) series. | KLA Surfscan SP7 (Unpatterned/Patterned Laser Scatterometry). |

---

### 1.2 Ray & Wave Optics Formulations
1. **Rayleigh Scattering Regime ($d \ll \lambda$)**:
   For particles much smaller than the illumination wavelength (e.g., a $15\text{ nm}$ particle illuminated by $193\text{ nm}$ laser):
   $$I_{\text{scattered}} \propto I_0 \cdot \frac{1 + \cos^2\theta}{R^2} \cdot \left(\frac{2\pi}{\lambda}\right)^4 \cdot \left(\frac{n^2 - 1}{n^2 + 2}\right)^2 \cdot \left(\frac{d}{2}\right)^6$$
   *Key takeaway for Applications Engineers*: Scattering intensity scales with the **sixth power of particle diameter ($d^6$)** and **inversely with the fourth power of wavelength ($\lambda^{-4}$)**. Shifting from DUV ($266\text{ nm}$) to broadband vacuum ultraviolet (VUV $<190\text{ nm}$) yields an immense physical surge in scatter signal from sub-20nm killer particles.

2. **Point Spread Function (PSF) & Spatial Filtering**:
   An optical imaging system acts as a low-pass spatial frequency filter. In patterned wafer inspection, Fourier optical filtering is employed in the back focal plane to block periodic diffraction spikes from repetitive memory arrays (SRAM, DRAM), allowing only aperiodic defect signatures to reach the sensor.

---

## 2. Image Processing & Defect Detection Algorithms

### 2.1 Die-to-Die (D2D) and Cell-to-Cell (C2C) Comparison
Because semiconductor wafers consist of hundreds of identical printed dice, defect detection relies on differential image subtraction:

```
Test Die Image:       Reference Die Image:      Difference Image (|Test - Ref|):
┌──────────────┐      ┌──────────────┐         ┌──────────────┐
│  ┌──┐        │      │  ┌──┐        │         │              │
│  └──┘   ●    │  —   │  └──┘        │    =    │         ★    │ (Defect Detected!)
│        (Defect)     │              │         │              │
└──────────────┘      └──────────────┘         └──────────────┘
```

1. **Sub-Pixel Image Registration**: The test die image $I_{\text{test}}(x, y)$ and reference die image $I_{\text{ref}}(x, y)$ are aligned using normalized cross-correlation (NCC) to sub-pixel accuracy ($<0.05\text{ pixels}$).
2. **Difference Image Computation**:
   $$\Delta I(x, y) = |I_{\text{test}}(x, y) - I_{\text{ref}}(x, y)|$$
3. **Thresholding & Signal-to-Noise Ratio (SNR)**:
   A defect candidate is flagged if the local difference intensity exceeds an adaptive noise threshold $T(x, y)$:
   $$\Delta I(x, y) \ge T(x, y) = \mu_{\text{noise}} + k \cdot \sigma_{\text{noise}}$$
   * High $k$ (e.g., $k=6$): Suppresses nuisance noise but misses subtle killer defects (**High False Negatives**).
   * Low $k$ (e.g., $k=3$): Captures all killer defects but causes a nuisance explosion (**High False Positives**).
   * **Receiver Operating Characteristic (ROC)** curve tuning is a daily task for a KLA Applications Engineer.

---

## 3. Metrology: Overlay & Critical Dimension (CD)

Metrology tools quantify physical dimensions rather than searching for random anomalies.

### 3.1 Overlay Metrology (KLA Archer Series)
Overlay error measures the positional displacement vector $(\Delta x, \Delta y)$ between two successively patterned lithography layers:
$$\vec{\delta}_{\text{overlay}} = \vec{r}_{\text{current\_layer}} - \vec{r}_{\text{previous\_layer}}$$
* **Image-Based Overlay (IBO)**: Targets like "Box-in-Box" or "Frame-in-Frame" where optical microscopy measures the geometric centroid offset between inner and outer targets.
* **Diffraction-Based Overlay (DBO)**: Overlapping diffraction gratings where asymmetric scatterometry measures overlay error via intensity differences in positive and negative diffraction orders ($I_{+1} - I_{-1}$).
* **Allowable Overlay Budget**: On modern 3nm nodes, the allowable overlay error is under **$1.5\text{ to }2.0\text{ nanometers}$**.

### 3.2 Optical Critical Dimension (OCD — SpectraShape Series)
* Uses **Spectroscopic Ellipsometry (SE)** to measure the change in light polarization upon reflection:
  $$\rho = \tan\Psi \cdot e^{i\Delta}$$
* Solves the inverse optical problem using **Rigorous Coupled-Wave Analysis (RCWA)** to reconstruct 3D gate profiles, sidewall angles, and trench depths non-destructively.

---

## 4. Statistical Process Control (SPC) Fundamentals

Statistical Process Control ensures that a manufacturing step operates consistently around its target mean without unexpected shifts in variation.

### 4.1 Shewhart Control Charts ($\bar{X}-R$ and $\bar{X}-S$)
Subgroups of size $n$ are sampled over time $t$:
* **Subgroup Mean ($\bar{X}$)**:
  $$\bar{X} = \frac{1}{n} \sum_{i=1}^n X_i, \quad \bar{\bar{X}} = \frac{1}{m} \sum_{j=1}^m \bar{X}_j$$
* **Control Limits for $\bar{X}$ Chart**:
  $$UCL = \bar{\bar{X}} + 3 \frac{\sigma}{\sqrt{n}} = \bar{\bar{X}} + A_2 \bar{R}$$
  $$CL = \bar{\bar{X}}$$
  $$LCL = \bar{\bar{X}} - 3 \frac{\sigma}{\sqrt{n}} = \bar{\bar{X}} - A_2 \bar{R}$$
* **Control Limits for Range ($R$) Chart**:
  $$UCL_R = D_4 \bar{R}, \quad LCL_R = D_3 \bar{R}$$

### 4.2 Western Electric Rules for Process Excursions
A process is deemed **out of statistical control** if any of the following occur:
1. **Rule 1 (Gross Excursion)**: One single point falls beyond either $3\sigma$ control limit ($> UCL$ or $< LCL$).
2. **Rule 2 (Zone A Drift)**: Two out of three consecutive points fall beyond the $2\sigma$ warning limit on the same side of the center line.
3. **Rule 3 (Zone B Run)**: Four out of five consecutive points fall beyond the $1\sigma$ limit on the same side.
4. **Rule 4 (Systematic Bias)**: Eight consecutive points fall on the same side of the center line.

---

## 5. Process Capability Indices: $C_p$ vs. $C_{pk}$

Process capability quantifies the ability of an in-control process to manufacture parts within engineering specifications:
* **Upper Specification Limit ($USL$)** & **Lower Specification Limit ($LSL$)** defined by chip design rules.
* **Process Spread**: Natural process tolerance is $6\sigma$.

### 5.1 Formulation:
1. **Process Potential ($C_p$)**:
   $$C_p = \frac{USL - LSL}{6\sigma}$$
   *Measures the inherent process spread relative to specification width. Ignores process centering!*

2. **Actual Process Capability ($C_{pk}$)**:
   $$C_{pk} = \min\left(C_{pu}, C_{pl}\right) = \min\left(\frac{USL - \mu}{3\sigma}, \frac{\mu - LSL}{3\sigma}\right)$$
   *Accounts for both process spread and mean shift.*

3. **Relationship**:
   $$C_{pk} = C_p (1 - k), \quad \text{where } k = \frac{|\text{Target} - \mu|}{\frac{USL - LSL}{2}}$$
   * Always $C_{pk} \le C_p$.
   * $C_{pk} = C_p$ if and only if the process is perfectly centered on the target mean.
   * Semiconductor Six Sigma Benchmark: $C_{pk} \ge 1.67$ (less than 1 part per billion defect rate).

```
Process Centering and Capability Visualization:
─────────────────────────────────────────────────────────────
Case A: Perfectly Centered (Cp = 1.67, Cpk = 1.67)
           LSL                      Mean                     USL
            │                        ▼                        │
            │                  ╭───────────╮                  │
            │             ╭────╯           ╰────╮             │
────────────┴─────────────┴─────────────────────┴─────────────┴────────────
                      |◄────── 6 Sigma Spread ──────►|

Case B: Shifted Mean (Cp = 1.67, Cpk = 0.83) -> OUT OF SPEC DEFECTS!
           LSL                               Mean            USL
            │                                 ▼               │
            │                           ╭───────────╮         │
            │                      ╭────╯           ╰────╮   ░░░░ (Scrap)
────────────┴──────────────────────┴─────────────────────┴────░░░░─────────
```

---

## 6. Root-Cause Analysis (RCA) Frameworks

When a customer fab experiences an out-of-control defect excursion, KLA Applications Engineers lead structured investigations:

### 6.1 The 5-Whys Sequence (CMP Micro-Scratch Excursion Example)
1. *Why did wafer defect count spike by 400% post-CMP?*  
   $\rightarrow$ Multiple linear micro-scratches were detected on the copper surface.
2. *Why are micro-scratches forming during polish?*  
   $\rightarrow$ Large agglomerated abrasive particles ($>2\text{ }\mu\text{m}$) were dragged across the wafer.
3. *Why did the slurry contain agglomerated particles?*  
   $\rightarrow$ The Point-of-Use (POU) slurry filtration cartridge experienced breakthrough.
4. *Why did the filter cartridge experience breakthrough?*  
   $\rightarrow$ The differential pressure ($\Delta P$) across the filter exceeded 2.5 bar without triggering an alarm.
5. *Why was there no alarm?*  
   $\rightarrow$ The pressure sensor calibration had drifted and maintenance had not updated the preventive limit.

### 6.2 Ishikawa (Fishbone) Diagram for Semiconductor Defect RCA
```
  EQUIPMENT (MACHINE)                  PROCESS (METHOD)
  Pad conditioner wear ──┐             ┌── Slurry flow rate drift
  Spindle vibration ─────┤             ├── Polish head downforce profile
                         └───┐     ┌───┘
                             │     │
                             ▼     ▼
                        YIELD DEFECT EXCURSION
                             ▲     ▲
                             │     │
  Slurry agglomerates ───┘     └─── Filter pore degradation
  Incoming wafer bow ────┘         └── Cleanroom ambient humidity shift
  MATERIALS                            ENVIRONMENT / MEASUREMENT
```

---

## 7. Worked Numerical Example: $C_p$ and $C_{pk}$ Derivation

### Problem Statement:
In a 7nm gate-etch manufacturing step, the Critical Dimension (CD) of the polysilicon gate has specification limits:
* $\text{Nominal Target} = 45.0\text{ nm}$
* $USL = 48.0\text{ nm}, \quad LSL = 42.0\text{ nm}$

Metrology data gathered from 100 consecutive wafers on a KLA SpectraShape tool yields:
* Sample mean $\bar{X} = 46.2\text{ nm}$
* Sample standard deviation $\sigma = 0.80\text{ nm}$

1. Calculate the inherent process potential $C_p$.
2. Calculate the actual process capability $C_{pk}$.
3. What fraction of manufactured gates fall above the upper specification limit ($USL$), assuming a normal distribution?
4. What action should the Applications Engineer recommend to the fab team?

### Step-by-Step Solution:

#### Step 1: Inherent Process Capability ($C_p$)
$$C_p = \frac{USL - LSL}{6\sigma} = \frac{48.0 - 42.0}{6 \times 0.80} = \frac{6.0}{4.80} = \mathbf{1.25}$$

#### Step 2: Actual Process Capability ($C_{pk}$)
Calculate upper and lower capability:
$$C_{pu} = \frac{USL - \mu}{3\sigma} = \frac{48.0 - 46.2}{3 \times 0.80} = \frac{1.80}{2.40} = \mathbf{0.75}$$
$$C_{pl} = \frac{\mu - LSL}{3\sigma} = \frac{46.2 - 42.0}{3 \times 0.80} = \frac{4.20}{2.40} = \mathbf{1.75}$$
$$C_{pk} = \min(C_{pu}, C_{pl}) = \min(0.75, 1.75) = \mathbf{0.75}$$

#### Step 3: Defect Rate Calculation (Fraction Above $USL$)
Calculate the standard normal variable $Z$ at the upper limit:
$$Z = \frac{USL - \mu}{\sigma} = \frac{48.0 - 46.2}{0.80} = \frac{1.80}{0.80} = +2.25$$
Using the standard normal cumulative distribution table $\Phi(2.25) \approx 0.9878$:
$$P(X > USL) = 1 - \Phi(2.25) = 1 - 0.9878 = 0.0122 = \mathbf{1.22\%}$$
Approximately **$12,200\text{ parts per million (ppm)}$** are being manufactured out-of-spec!

#### Step 4: Engineering Diagnosis & Action
* **Diagnosis**: Notice that $C_p = 1.25$ indicates the process variation is sufficiently narrow to yield acceptable results if centered, but $C_{pk} = 0.75$ reveals a severe **mean centering error** ($+1.2\text{ nm}$ positive drift toward $USL$).
* **Recommended Action**: Do *not* re-engineer the etch chamber hardware or gas chemistry (which controls $\sigma$). Instead, **adjust the lithography exposure dose or etch over-etch duration** to shift the process mean from $46.2\text{ nm}$ back to the target $45.0\text{ nm}$. Centering the process will instantly raise $C_{pk}$ to $1.25$ and drop the scrap rate from $1.22\%$ to $0.018\%$.
