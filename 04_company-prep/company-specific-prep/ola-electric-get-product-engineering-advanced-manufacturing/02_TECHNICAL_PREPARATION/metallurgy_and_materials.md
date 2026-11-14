# Metallurgy & Advanced Materials: Automotive EV Applications
**Target Role:** Graduate Engineer Trainee (GET) — Product Engineering & Advanced Manufacturing  
**Company:** Ola Electric Mobility Limited  
**Standard:** Materials Science, Physical Metallurgy & Failure Analysis  

---

## 1. Crystal Structures, Slip Systems & Strengthening Mechanisms

### 1.1 Atomic Lattice Architectures in Automotive Metals
- **Face-Centered Cubic (FCC):**  
  *Examples:* Aluminum, Austenitic Stainless Steel, Copper.  
  *Characteristics:* 12 slip systems ($\{111\}\langle 110 \rangle$). Closely packed planes allow high dislocation mobility. Highly ductile, excellent formability (ideal for deep-drawn battery cans), and **retains ductility at cryogenic temperatures without a Ductile-to-Brittle Transition Temperature (DBTT)**.
- **Body-Centered Cubic (BCC):**  
  *Examples:* Ferritic / Structural Carbon Steel at room temperature ($\alpha$-iron).  
  *Characteristics:* 48 slip systems, but lacking close-packed planes. Higher yield strength, but exhibits a pronounced **Ductile-to-Brittle Transition Temperature (DBTT)** under cold climates and dynamic impact.
- **Hexagonal Close-Packed (HCP):**  
  *Examples:* Titanium, Magnesium, Zinc.  
  *Characteristics:* Only 3 primary basal slip systems at room temperature. Low room-temperature ductility; requires hot forming.

### 1.2 The Four Core Strengthening Mechanisms
1. **Grain Boundary Strengthening (Hall-Petch Relationship):**  
   Grain boundaries act as pin barriers to dislocation glide:
   $$\sigma_y = \sigma_0 + \frac{k_y}{\sqrt{d}}$$
   where $d$ is the average grain diameter. Refining grain size is the **only strengthening mechanism that simultaneously increases yield strength AND fracture toughness**!
2. **Solid Solution Strengthening:**  
   Solute atoms of differing atomic radii (e.g., carbon in interstitial steel lattice, or magnesium in substitutional aluminum lattice) create localized strain fields that interact with dislocations, resisting shear glide.
3. **Strain Hardening / Work Hardening (Dislocation Multiplication):**  
   Cold rolling or sheet stamping multiplies dislocation density ($\rho \approx 10^8 \to 10^{12}\text{ cm}^{-2}$). Dislocation tangles form locks (Lomer-Cottrell barriers), increasing yield strength at the expense of ductility:
   $$\sigma = K \varepsilon^n \quad (\text{Hollomon's Equation, where } n \text{ is the strain hardening exponent})$$
4. **Precipitation Hardening (Age Hardening — Basis of Al 6061-T6):**  
   Coherent microscopic intermetallic precipitates (e.g., $Mg_2Si$ in aluminum alloys) pin moving dislocations, forcing them to either shear through or bow around the particles (Orowan looping mechanism):
   $$\tau_0 \propto \frac{G b}{L_{\text{precipitate}}}$$

---

## 2. Phase Diagrams: Iron-Carbon (Fe-C) & Aluminum-Silicon (Al-Si)

### 2.1 The Iron-Carbon Phase Diagram (Chassis Steels)
- **Ferrite ($\alpha$-iron, BCC):** Stable below $912^\circ\text{C}$. Maximum carbon solubility is only $0.022\text{ wt\%}$ at $727^\circ\text{C}$. Soft, magnetic, ductile.
- **Austenite ($\gamma$-iron, FCC):** Stable between $912^\circ\text{C}$ and $1394^\circ\text{C}$. High carbon solubility up to $2.14\text{ wt\%}$. Non-magnetic, highly formable.
- **Cementite ($Fe_3C$):** Intermetallic iron carbide with fixed $6.67\text{ wt\% C}$. Extremely hard, brittle.
- **Eutectoid Reaction (at $727^\circ\text{C}, 0.76\text{ wt\% C}$):**
  $$\text{Austenite } (\gamma, 0.76\% C) \xrightarrow{\text{Slow Cooling}} \text{Ferrite } (\alpha, 0.022\% C) + \text{Cementite } (Fe_3C, 6.67\% C) \implies \mathbf{Pearlite}$$
  Pearlite is a lamellar (alternating plate) microstructure balancing tensile strength and ductility.

### 2.2 Non-Equilibrium Transformation: Martensite Formation
When austenite ($\gamma$) is rapidly quenched in water or oil, carbon atoms lack time to diffuse out of the lattice. The FCC lattice shears into a distorted **Body-Centered Tetragonal (BCT)** crystal structure supersaturated with carbon: **Martensite**.
- Martensite is extremely hard and brittle.
- **Tempering (Sub-critical reheating to $200 - 600^\circ\text{C}$):** Relieves internal quenching stresses and precipitates fine carbides, yielding **Tempered Martensite** with optimal automotive impact toughness.

### 2.3 The Aluminum-Silicon (Al-Si) Phase Diagram (Die-Castings)
In HPDC alloys like A380 ($8.5\% \text{ Si}$) and A383 ($10.5\% \text{ Si}$):
- Eutectic composition occurs at **$12.6\text{ wt\% Si}$ at $577^\circ\text{C}$**.
- High silicon content imparts **exceptional fluidity** to liquid aluminum, allowing it to flow through intricate $2.5\text{ mm}$ die cavities without premature freezing.
- Eutectic silicon naturally solidifies as coarse, needle-like acicular plates that act as internal stress concentrators. **Modification with tiny additions of Strontium (Sr, 100–200 PPM)** transforms brittle acicular silicon needles into fine fibrous coral-like globules, boosting elongation from $1.5\%$ to $> 5\%$.

---

## 3. Heat Treatment of Automotive Steels & Aluminum Alloys

### 3.1 Heat Treatment of Steels
- **Annealing:** Heating above $A_3$, soaking, and furnace cooling at slow rate. Yields soft, stress-free coarse pearlite for cold stamping.
- **Normalizing:** Air cooling from above $A_3$. Yields fine pearlite with higher yield strength.
- **Quenching & Tempering (Q&T):** Produces tough tempered martensite for high-strength suspension bolts (Grade 10.9).

### 3.2 T6 Heat Treatment of Aluminum Alloys (Solutionizing + Aging)
The T6 temper cycle for structural alloys (e.g., Al 6061 battery crash rails):
1. **Solution Heat Treatment ($530^\circ\text{C}$ for 1–2 hours):** Dissolves all alloying elements (Mg, Si) into a homogeneous solid solution $\alpha$.
2. **Rapid Water Quench ($< 10\text{ seconds}$ delay):** Freezes a supersaturated solid solution (SSSS) at room temperature.
3. **Artificial Aging ($160 - 180^\circ\text{C}$ for 6–10 hours):** Controlled precipitation of coherent $\beta''$ needle-like $Mg_2Si$ nanometer-scale precipitates that maximize dislocation pinning, boosting yield strength from $110\text{ MPa}$ to $> 275\text{ MPa}$.

---

## 4. Automotive Steel Grades & Aluminum Alloys

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                        AUTOMOTIVE STRUCTURAL MATERIALS SPECTRUM                        │
├───────────────────┬──────────────┬──────────────┬──────────────────────────────────────┤
│ Material Grade    │ Yield (MPa)  │ Tensile (MPa)│ Typical EV Application               │
├───────────────────┼──────────────┼──────────────┼──────────────────────────────────────┤
│ CRCA (IS 513)     │ 140 – 240    │ 270 – 370    │ Deep-drawn brackets, battery trays   │
│ HSLA 350 / 420    │ 350 – 420    │ 450 – 520    │ Gen 2 tubular chassis main spine     │
│ DP600 (Dual Phase)│ 350 – 400    │ 600 – 700    │ High energy-absorbing crash members  │
│ Al 6061-T6        │ 275          │ 310          │ Extruded battery enclosure rails     │
│ Al A380 (As Cast) │ 160          │ 325          │ Die-cast swingarm, motor housing     │
│ Nickel-Plated Steel│ 220         │ 350          │ 4680 cylindrical cell can casings    │
└───────────────────┴──────────────┴──────────────┴──────────────────────────────────────┘
```

---

## 5. Mechanical Testing & Material Characterization

### 5.1 Uniaxial Tensile Testing
- **Engineering Stress vs True Stress:**
  $$\sigma_{\text{eng}} = \frac{F}{A_0}, \quad \sigma_{\text{true}} = \frac{F}{A} = \sigma_{\text{eng}}(1 + \varepsilon_{\text{eng}})$$
  $$\varepsilon_{\text{eng}} = \frac{\Delta L}{L_0}, \quad \varepsilon_{\text{true}} = \ln\left(\frac{L}{L_0}\right) = \ln(1 + \varepsilon_{\text{eng}})$$
  *(True stress accounts for instantaneous cross-sectional area necking; valid up to ductile fracture).*
- **0.2% Offset Yield Strength ($R_{p0.2}$):** For metals lacking an upper/lower yield point (such as aluminum alloys and high-strength steels), yield strength is defined by drawing a line parallel to the linear elastic slope starting at $\varepsilon = 0.002$ ($0.2\%$ plastic strain).

### 5.2 Hardness Testing Scales
- **Brinell (HBW):** Hardened tungsten carbide ball ($10\text{ mm}$ dia, $3000\text{ kg}$ load). Measures bulk hardness; ideal for inhomogeneous castings.
- **Rockwell (HRC / HRB):** Diamond spheroconical indenter (HRC, $150\text{ kg}$) for hardened steels; $1/16''$ steel ball (HRB, $100\text{ kg}$) for aluminum and mild steels. Direct dial readout of indentation depth.
- **Vickers (HV):** Square-based pyramid diamond ($136^\circ$ face angle). Micro-hardness profiling across weld heat-affected zones (HAZ).

### 5.3 Charpy V-Notch Impact Testing & DBTT
Measures dynamic fracture energy absorption ($J$). BCC steels show a steep drop in toughness at low temperatures (Ductile-to-Brittle Transition Temperature — DBTT). Aluminum alloys and austenitic steels (FCC) do not exhibit DBTT, maintaining high impact toughness in sub-zero winter conditions.

---

## 6. Corrosion Mechanisms & Surface Passivation

In Indian road environments (monsoon water-logging, road mud, coastal salt spray in Mumbai/Chennai):
1. **Galvanic Corrosion (Bimetallic Cell):**  
   Occurs when dissimilar metals are in direct electrical contact in the presence of an electrolyte:
   - *Automotive Trap:* Bolting a steel bracket directly to an aluminum die-cast swingarm. Aluminum is more active (anodic) than steel (cathodic); the aluminum corrodes rapidly around the bolt hole.
   - *Mitigation:* Isolate metals with non-conductive zinc-flake coatings (Geomet / Dacromet), nylon washers, or E-coat primer.
2. **Crevice & Pitting Corrosion:**  
   Occurs in stagnant micro-gaps under battery enclosure gaskets or spot-welded overlapping sheet joints where dissolved oxygen depletes, creating localized acidic micro-anodes.
3. **ASTM B117 Neutral Salt Spray (NSS) Testing:**  
   Automotive benchmark: Chassis CED primer must survive **1,000 hours of 5% NaCl mist at 35°C** with zero blistering and red rust creep $< 1\text{ mm}$ from a cross-hatch scribe mark.

---
*End of Metallurgy & Advanced Materials.*
