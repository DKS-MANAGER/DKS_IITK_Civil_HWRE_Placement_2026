# Module 08: Energy Dissipation Systems — Basins, Flip Buckets & Roller Buckets

> **Document Focus**: Hydraulic Energy Dissipation, USBR Stilling Basins, Trajectory (Flip) Buckets, Roller Buckets, Jet Throw Mechanics, and Scour Prediction  
> **Target Role**: Hydraulics Engineer (AFRY India)  
> **Evidentiary Status**: `[TIER 4 / STATUTORY & ENGINEERING CODES — USBR MONOGRAPH 25, IS 4997, IS 7365, PETERKA]`  

---

## 1. Fundamentals of Hydraulic Energy Dissipation

Water spilling over a high dam acquires immense kinetic energy. At the base of a $60\text{ m}$ high dam, flow velocities exceed $30\text{ to } 35\text{ m/s}$. Discharging high-velocity jets directly into an unlined alluvial or fractured rock riverbed produces severe undermining of the dam foundation, destruction of powerhouses, and catastrophic slope failures.

The engineering challenge is to safely convert kinetic energy ($v^2/2g$) into heat and turbulent eddies before the water enters the natural river downstream. The choice of dissipator is governed by the incoming Froude number ($Fr_1$), tailwater depth ($y_{tw}$), and the geological competence of the downstream riverbed:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    ENERGY DISSIPATOR SELECTION MATRIX                       │
├─────────────────────┬───────────────────────────┬───────────────────────────┤
│ DISSIPATOR TYPE     │ HYDRAULIC & TAILWATER FIT │ FOUNDATION REQUIREMENT    │
├─────────────────────┼───────────────────────────┼───────────────────────────┤
│ **Stilling Basin**  │ $y_{tw} \approx y_2$      │ Any foundation (alluvium, │
│ (USBR Type II/III)  │ Jump forms inside basin;  │ soft rock, hard rock);    │
│                     │ tranquil outflow ($Fr < 1$)│ requires concrete floor   │
├─────────────────────┼───────────────────────────┼───────────────────────────┤
│ **Trajectory Bucket**│ $y_{tw} \ll y_2$         │ Sound, non-erodible bed-  │
│ (Flip / Ski-Jump)   │ Launches jet far away     │ rock (granite, massive    │
│                     │ into deep plunge pool     │ basalt, competent gneiss) │
├─────────────────────┼───────────────────────────┼───────────────────────────┤
│ **Roller Bucket**   │ $y_{tw} \gg y_2$         │ Medium to sound rock;     │
│ (Solid / Slotted)   │ Drowned roller action;    │ cannot be founded on      │
│                     │ surface & ground rollers  │ erodible alluvial soils   │
└─────────────────────┴───────────────────────────┴───────────────────────────┘
```

---

## 2. Hydraulic Jump Stilling Basins (USBR Types)

Stilling basins dissipate energy through a forced hydraulic jump contained entirely on a horizontal or sloping concrete apron.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       USBR TYPE II STILLING BASIN                           │
│                                                                             │
│               Supercritical Chute                                           │
│               ─────────────────\                                            │
│                                 \   Chute Blocks                            │
│                                  \   ┌─┐             Dentated End Sill      │
│                                   \  │ │             ┌─┐   ┌─┐              │
│               ═════════════════════╧═╧═╧═════════════╧═╧═══╧═╧═══════════   │
│               ◄────────────────── Basin Length L_II ──────────────────►     │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 2.1 Tailwater Rating Curve (TWC) vs. Jump Rating Curve (JRC)
Proper stilling basin performance requires comparing the natural river **Tailwater Rating Curve ($TWC$)** with the required **Jump Conjugate Depth Curve ($JRC = y_2$)**:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           TWC vs. JRC RELATIONSHIPS                         │
│       Stage                                                                 │
│         ▲                                                                   │
│         │              Case 2: JRC > TWC (Jump sweeps out of basin)         │
│         │           ┌────────────────────────────► JRC                      │
│         │          /                                                        │
│         │         /   Case 1: JRC = TWC (Ideal jump at toe)                 │
│         │        /                                                          │
│         │       /     Case 3: TWC > JRC (Jump drowned at toe)               │
│         │      /   ┌─────────────────────────────► TWC                      │
│         │     /   /                                                         │
│         └────┴───┴─────────────────────────────────────────► Discharge Q     │
└─────────────────────────────────────────────────────────────────────────────┘
```
1. **Case 1 ($TWC = JRC$)**: The tailwater depth matches the conjugate depth across all discharges. The jump stays positioned at the basin entrance. (Extremely rare in nature).
2. **Case 2 ($TWC < JRC$)**: Tailwater depth is lower than required conjugate depth. The jump sweeps downstream off the concrete apron onto the unprotected riverbed. **Remedy**: Depress the basin floor below riverbed level ($d = y_2 - y_{tw}$).
3. **Case 3 ($TWC > JRC$)**: Tailwater depth exceeds conjugate depth. The jump is drowned at the spillway toe, forming a high-velocity bottom jet that travels across the floor without full dissipation. **Remedy**: Use a sloping apron or roller bucket.

### 2.2 Standard USBR Stilling Basin Classifications (Bureau of Reclamation)
* **USBR Type I**: Plain horizontal rectangular apron without accessories. Requires full natural jump length $L_I \approx 6.0 y_2$. Unused for high dams due to excessive concrete cost.
* **USBR Type II (High-Head / Large Dams — $Fr_1 > 4.5, v_1 > 15\text{ m/s}$)**:
  * Designed for high dam spillways where velocities would cavitate intermediate baffle piers.
  * **Accessories**: Chute blocks at the entrance, and a **dentated end sill** at the exit. Intermediate baffle piers are strictly **omitted**.
  * **Basin Length**: Reduced by $33\%$ compared to plain basins:
    $$\boxed{L_{II} \approx 4.3 \times y_2}$$
* **USBR Type III (Low to Medium Head — $Fr_1 > 4.5, v_1 \le 18\text{ m/s}$)**:
  * Designed for canals, barrages, and low-head dams where inflow velocity does not exceed the cavitation threshold ($18\text{ m/s}$).
  * **Accessories**: Chute blocks, **intermediate baffle piers (impact blocks)**, and a solid end sill.
  * **Basin Length**: Reduced by $60\%$:
    $$\boxed{L_{III} \approx 2.7 \times y_2}$$
* **USBR Type IV (Oscillating Jump Regime — $2.5 \le Fr_1 \le 4.5$)**:
  * Employs large, deflecting chute blocks spaced along the floor to stabilize wave oscillation.

---

## 3. Trajectory Buckets (Flip Buckets / Ski-Jump)

When the tailwater depth is much lower than the conjugate depth ($y_{tw} \ll y_2$) and the riverbed consists of sound, unweathered rock, constructing a concrete stilling basin is uneconomical. A **Trajectory (Flip) Bucket** terminates the spillway chute in an upward circular curve, launching the high-velocity jet into the atmosphere.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                     TRAJECTORY FLIP BUCKET DYNAMICS                         │
│                                                                             │
│                                           Parabolic Jet Trajectory          │
│                                           . - - - - .                       │
│     Spillway Chute                      /             \                     │
│     ──────────────\                    /               \                    │
│                    \     Trajectory   /                 \                   │
│                     \   ┌────────────/                   ▼ Plunge Pool      │
│                      \_/ Bucket Lip (θ)                   (Scour Depth d_s) │
│                      ◄─ R ─►                              ═══════════════   │
│                      ◄────────────── Throw Distance X_t ────────────────►   │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 3.1 Jet Throw Distance Derivation ($X_t$)
Let the bucket lip have an exit angle $\theta$ to the horizontal, radius $R$, lip elevation $y_0$ above tailwater level, and launch velocity $v_0$.
The initial velocity components are:
$$v_{x0} = v_0 \cos\theta, \quad v_{y0} = v_0 \sin\theta$$
Applying equations of projectile kinematics in air:
$$x(t) = (v_0 \cos\theta) t$$
$$y(t) = y_0 + (v_0 \sin\theta) t - \frac{1}{2}g t^2$$
At impact with the tailwater pool ($y = 0$):
$$\frac{1}{2}g t^2 - (v_0 \sin\theta) t - y_0 = 0$$
Solving for time of flight $t$:
$$t = \frac{v_0 \sin\theta + \sqrt{v_0^2 \sin^2\theta + 2 g y_0}}{g}$$
The horizontal **throw distance ($X_t$)** is:
$$X_t = (v_0 \cos\theta) t = \frac{v_0^2 \sin\theta \cos\theta}{g} \left[ 1 + \sqrt{1 + \frac{2 g y_0}{v_0^2 \sin^2\theta}} \right]$$
$$\boxed{X_t = \frac{v_0^2 \sin 2\theta}{2g} \left[ 1 + \sqrt{1 + \frac{2 g y_0}{v_0^2 \sin^2\theta}} \right]} \quad \blacksquare$$
* If the bucket lip is at the tailwater surface ($y_0 = 0$):
  $$X_t = \frac{v_0^2 \sin 2\theta}{g}$$
  Maximum throw distance occurs at lip angle **$\theta = 45^\circ$** ($\sin 2\theta = 1$). In practice, lip angles of $\theta = 30^\circ \text{ to } 35^\circ$ are commonly adopted to achieve maximum throw distance while minimizing jet wind drift.

### 3.2 Plunge Pool Maximum Scour Depth Prediction
The falling jet impacts the riverbed, excavating a localized plunge pool until an equilibrium depth is reached. The empirical **Veronese formula** (verified by USBR, CWC, and international standards) predicts maximum scour depth $d_s$ below the tailwater surface:
$$\boxed{d_s = 1.90 H_t^{0.225} q^{0.54} - d_{tw}}$$
where:
* $d_s$: Scour hole depth below the riverbed (m).
* $H_t$: Total drop from upstream reservoir level to downstream tailwater pool (m).
* $q$: Discharge per unit width ($Q / B$, in $\text{m}^3\text{/s/m}$).
* $d_{tw}$: Tailwater depth above original riverbed (m).
* $1.90$: Empirical SI unit coefficient for massive competent bedrock. (For fractured rock, factor increases to $2.10 \text{ to } 2.40$).

---

## 4. Roller Buckets (Solid versus Slotted)

When the tailwater depth is substantially greater than the conjugate depth ($y_{tw} > 1.1 \text{ to } 1.2 y_2$), a hydraulic jump cannot form. A **Roller Bucket** consists of a circular concave curve located below riverbed level that establishes two circular rollers:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          SOLID ROLLER BUCKET DYNAMICS                       │
│                                                                             │
│                                    Surface Roller                           │
│                                    (Counter-Clockwise)                      │
│                                     ┌───◄───┐                               │
│     Spillway Chute                 │   ▼   │                               │
│     ──────────────\                └───►───┘  Downstream Tailwater Pool     │
│                    \   Solid Bucket Lip       ~~~~~~~~~~~~~~~~~~~~~~~~~~~~  │
│                     \      ┌───┐                  ┌───►───┐                 │
│                      \____/    │                  │   ▲   │ Ground Roller   │
│                      ◄── R ───►                   └───◄───┘ (Clockwise)     │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 4.1 Two-Roller Energy Dissipation Mechanism
1. **Surface Roller**: A violent counter-clockwise roller forms directly above the bucket, dissipating jet kinetic energy through internal fluid shear and turbulence.
2. **Ground Roller**: A clockwise ground roller forms on the riverbed immediately downstream of the bucket lip.
   * *Critical Engineering Feature*: The ground roller moves **upstream toward the bucket lip** along the channel bed, pulling sediment and bed material *against* the bucket toe rather than washing it downstream. This protects the dam toe from scouring!

### 4.2 Solid versus Slotted Roller Buckets
* **Solid Roller Bucket**: The continuous cylindrical apron generates a heavy, violent surface boil. The ground roller can pull massive river rocks into the bucket, where the churning jet grinds them against the concrete floor like a ball mill, causing severe abrasion erosion.
* **Slotted Roller Bucket (IS 7365 / USBR)**: The lip has alternating teeth and slots. Part of the jet passes through the slots, breaking the jet into smaller filaments. This softens the surface boil, allows bed sediment to be washed out, and operates over a much wider range of tailwater levels.

---

## 5. Solved Engineering Problem: Dissipator Sizing & Selection

**Statement**: A spillway on a concrete gravity dam discharges a design flood of $Q = 1,800\text{ m}^3\text{/s}$ across a total chute width of $B = 30.0\text{ m}$ ($q = 60.0\text{ m}^3\text{/s/m}$).
* Reservoir full pool level: $480.0\text{ m}$.
* Downstream riverbed elevation: $410.0\text{ m}$ (Gross head drop $H_0 = 70.0\text{ m}$).
* The chute friction loss is estimated at $h_f = 5.0\text{ m}$, leaving net effective head $H_{\text{net}} = 65.0\text{ m}$.
* Natural river tailwater rating shows that at $Q = 1,800\text{ m}^3\text{/s}$, tailwater depth is $y_{tw} = 8.0\text{ m}$ (Water surface elevation $418.0\text{ m}$).
* Competent sound basalt bedrock exists at the site.
1. Calculate the supercritical velocity $v_1$, flow depth $y_1$, and Froude number $Fr_1$ at the chute toe.
2. Calculate the theoretical conjugate depth $y_2$ required for a hydraulic jump stilling basin.
3. Demonstrate why a conventional stilling basin is hydraulically unfeasible without massive excavation.
4. Design a Trajectory Flip Bucket (lip angle $\theta = 35^\circ$, lip elevation $414.0\text{ m}$, radius $R$). Compute the jet throw distance $X_t$ and estimate maximum scour depth in the plunge pool using the Veronese formula.

**Solution**:
1. **Supercritical Inflow Parameters ($y_1, v_1, Fr_1$)**:
   $$\frac{v_1^2}{2g} = H_{\text{net}} = 65.0\text{ m} \implies v_1 = \sqrt{2 \times 9.81 \times 65.0} = \sqrt{1,275.3} = \mathbf{35.71\text{ m/s}}$$
   Supercritical depth:
   $$y_1 = \frac{q}{v_1} = \frac{60.0\text{ m}^3\text{/s/m}}{35.71\text{ m/s}} = \mathbf{1.680\text{ m}}$$
   Inflow Froude number:
   $$Fr_1 = \frac{v_1}{\sqrt{g y_1}} = \frac{35.71}{\sqrt{9.81 \times 1.680}} = \frac{35.71}{\sqrt{16.481}} = \frac{35.71}{4.060} = \mathbf{8.796}$$

2. **Required Conjugate Depth ($y_2$)**:
   Applying the Bélanger equation:
   $$y_2 = \frac{y_1}{2}\left(\sqrt{1 + 8 Fr_1^2} - 1\right) = \frac{1.680}{2}\left(\sqrt{1 + 8(8.796)^2} - 1\right)$$
   $$8(8.796)^2 = 8 \times 77.37 = 618.96 \implies \sqrt{619.96} = 24.90$$
   $$y_2 = 0.840 \times (24.90 - 1) = 0.840 \times 23.90 = \mathbf{20.08\text{ m}}$$

3. **Hydraulic Unfeasibility of Stilling Basin**:
   * Required conjugate depth: $y_2 = 20.08\text{ m}$.
   * Available natural tailwater depth: $y_{tw} = 8.0\text{ m}$.
   * Discrepancy: $y_{tw} \ll y_2$ ($8.0\text{ m} \ll 20.08\text{ m}$).
   * If a stilling basin were placed at riverbed level, the jump would instantly sweep downstream off the apron, destroying the riverbed.
   * To force a hydraulic jump, the basin floor would have to be excavated downward by:
     $$d_{\text{excavation}} = y_2 - y_{tw} = 20.08 - 8.0 = \mathbf{12.08\text{ m}}$$
     Excavating a $30\text{ m} \times 85\text{ m}$ basin $12.1\text{ m}$ deep into solid rock is economically prohibitive. Therefore, a **Trajectory Flip Bucket** is the optimum solution.

4. **Trajectory Flip Bucket Design**:
   * Bucket Radius ($R$):
     $$R = 0.6 \text{ to } 0.8 \sqrt{H_d \cdot P} \approx 0.7 \sqrt{8.0 \times 70.0} = 0.7 \sqrt{560} = 0.7(23.66) = \mathbf{16.5\text{ m}} \implies \text{Adopt } R = 18.0\text{ m}$$
   * Lip parameters:
     * Lip angle: $\theta = 35^\circ \implies \sin 35^\circ = 0.5736, \cos 35^\circ = 0.8192, \sin 70^\circ = 0.9397$.
     * Lip elevation $= 414.0\text{ m}$.
     * Tailwater elevation $= 418.0\text{ m} \implies y_0 = 414.0 - 418.0 = -4.0\text{ m}$ (lip is $4.0\text{ m}$ submerged) OR if lip is above tailwater, say tailwater is $410 + 4 = 414\text{ m} \implies y_0 = 0.0\text{ m}$.
     * For lip above low tailwater ($y_0 = 2.0\text{ m}$ above pool):
       $$X_t = \frac{v_0^2 \sin 2\theta}{2g} \left[ 1 + \sqrt{1 + \frac{2 g y_0}{v_0^2 \sin^2\theta}} \right]$$
       With $v_0 = 35.71\text{ m/s} \implies v_0^2 = 1,275.3$:
       $$\frac{v_0^2 \sin 70^\circ}{2g} = \frac{1,275.3 \times 0.9397}{19.62} = \frac{1,198.4}{19.62} = 61.08\text{ m}$$
       $$\frac{2 g y_0}{v_0^2 \sin^2 35^\circ} = \frac{19.62 \times 2.0}{1,275.3 \times (0.5736)^2} = \frac{39.24}{419.6} = 0.0935$$
       $$\sqrt{1 + 0.0935} = 1.0457$$
       $$X_t = 61.08 \times (1 + 1.0457) = 61.08 \times 2.0457 = \mathbf{124.95\text{ m}}$$
       The jet is thrown **125 meters away from the dam toe** into the center of the river channel!

5. **Plunge Pool Scour Depth Estimation (Veronese)**:
   Total head drop from reservoir ($480.0\text{ m}$) to tailwater ($418.0\text{ m}$): $H_t = 480.0 - 418.0 = 62.0\text{ m}$.
   Unit discharge: $q = 60.0\text{ m}^3\text{/s/m}$.
   $$d_s = 1.90 H_t^{0.225} q^{0.54} - d_{tw}$$
   $$H_t^{0.225} = (62.0)^{0.225} = 2.528$$
   $$q^{0.54} = (60.0)^{0.54} = 9.091$$
   $$d_s = 1.90 \times 2.528 \times 9.091 - 8.0 = 43.66 - 8.0 = \mathbf{35.66\text{ m}}$$
   Maximum equilibrium scour depth will reach $35.7\text{ m}$ below riverbed at the impact point 125 m downstream. The dam toe remains 100% protected.

