# Advanced Manufacturing Processes: Automotive & Gigafactory Engineering
**Target Role:** Graduate Engineer Trainee (GET) — Product Engineering & Advanced Manufacturing  
**Company:** Ola Electric Mobility Limited  
**Focus:** Futurefactory Shop Floor Operations, Gigafactory Battery Assembly & Tooling  

---

## 1. High-Pressure Die-Casting (HPDC) & Foundry Technology

In the Ola S1 Gen 2 and electric motorcycle platforms, the rear swingarm, motor casing, and transmission planetary housing are manufactured via **High-Pressure Die-Casting (HPDC)** using aluminum-silicon alloys (A380, A383, or AlSi9Cu3).

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                        COLD-CHAMBER HPDC OPERATIONAL CYCLE                             │
└────────────────────────────────────────────────────────────────────────────────────────┘
  1. Molten Al Pouring: Ladle pours liquid metal (650°C - 680°C) into cold shot sleeve.
  2. Slow Shot Phase: Piston moves forward at low speed (0.2 - 0.4 m/s) to push metal 
     past the pour hole without air entrapment.
  3. Fast Shot Phase: Piston accelerates (2.0 - 5.0 m/s), injecting liquid metal into 
     hardened tool steel die cavities in 20 to 60 milliseconds.
  4. Intensification Phase: Hydraulic booster spikes pressure to 80 - 120 MPa, forcing 
     liquid metal into microscopic dendritic voids as solidification initiates.
  5. Solidification & Ejection: Water-cooled die opens; hydraulic ejector pins push part out.
```

### 1.1 Casting Defect Taxonomy & Remediation
- **Gas Porosity (Smooth, spherical internal bubbles):**  
  *Root Cause:* Entrapment of air in the shot sleeve during high-velocity transition or thermal decomposition of oil-based die lubricants.  
  *Remediation:* Implement high-vacuum evacuation ($P_{\text{cavity}} < 50\text{ mbar}$) before shot injection; optimize slow-to-fast shot switch point.
- **Shrinkage Porosity (Jagged, irregular internal cavities):**  
  *Root Cause:* Volumetric contraction of aluminum ($\approx 6 - 7\%$) as it solidifies from liquid to solid phase, occurring in isolated thick sections.  
  *Remediation:* Maintain uniform wall thickness ($2.5 - 4.0\text{ mm}$); apply squeeze pins (local hydraulic squeeze cores) to feed liquid metal during freezing.
- **Cold Shuts / Misruns (Visible seam lines or incomplete fill):**  
  *Root Cause:* Two converging liquid metal flow fronts meet after premature freezing without coalescing.  
  *Remediation:* Increase die preheat temperature ($200 - 250^\circ\text{C}$); increase fast shot velocity; enlarge gate cross-sectional area.
- **Blistering (Surface bubble expansion after heat treatment):**  
  *Root Cause:* Sub-surface entrapped gas expanding during post-casting solution heat treatment ($> 450^\circ\text{C}$).  
  *Rule:* Standard HPDC parts cannot undergo T6 heat treatment unless cast under **ultra-high vacuum**.

---

## 2. Precision Sheet Metal Stamping & Tube Hydroforming

The Futurefactory press shop forms the main structural tubular spine, battery tray underbody, and reinforcement gussets using progressive stamping dies and automated robotic transfer lines.

### 2.1 Mechanics of Shearing, Blanking & Piercing
- **Clearance ($c$):** The per-side clearance between the hardened steel punch and die:
  $$c = 0.05 \text{ to } 0.10 \times t \quad (\text{where } t \text{ is sheet thickness})$$
  - Insufficient clearance ($c < 3\% t$): Causes double-shear burrs and severe punch wear.
  - Excessive clearance ($c > 12\% t$): Causes heavy edge rollover, large burrs, and tear fracture.
- **Cutting Force Equation:**
  $$F_{\text{blank}} = L_{\text{perimeter}} \times t \times \tau_{\text{shear}}$$
  where $\tau_{\text{shear}} \approx 0.70 - 0.80 \times S_{ut}$. Providing shear angles on the punch face reduces peak instantaneous tonnage by spreading the cut over time.

### 2.2 Sheet Bending, Springback & Forming Limit Diagrams (FLD)
- **Bend Allowance (BA) & Neutral Axis Shift:**  
  During bending, outer fibers stretch in tension while inner fibers compress. The neutral axis shifts inward by factor $K$:
  $$BA = \frac{\pi}{180} \cdot \alpha \cdot (R + K \cdot t)$$
  where $K \approx 0.33$ for $R < 2t$; $K \approx 0.50$ for $R > 2t$.
- **Springback Mechanics:**  
  When the forming punch retracts, elastic strain energy recovers, causing the bend angle to open up ($\Delta \alpha$) and the bend radius to increase ($\Delta R$):
  $$\frac{R_i}{R_f} = 4\left(\frac{R_i \sigma_y}{E t}\right)^3 - 3\left(\frac{R_i \sigma_y}{E t}\right) + 1$$
  - **High-Strength Steel Springback:** Modern Advanced High-Strength Steels (AHSS) have high yield-to-modulus ratios ($S_y / E$), resulting in $3 - 5\times$ more springback than mild steel!
  - **Mitigation Techniques:** Bottoming / coining dies, over-bending (bending to $86^\circ$ to achieve $90^\circ$), stretch-bending, and localized stiffening beads.

---

## 3. Robotic Welding & Joining Technologies

The Body-in-White (BIW) line at the Futurefactory deploys hundreds of 6-axis ABB industrial robots for frame welding.

### 3.1 Gas Metal Arc Welding (GMAW / MIG-MAG)
- **Shielding Gas Mixture:** $80\% \text{ Argon} / 20\% \text{ CO}_2$ for tubular steel frames. Argon provides arc stability and finger-like deep penetration; $\text{CO}_2$ provides wide bead wetting and reduces cost.
- **Welding Modes:** Pulsed MIG welding is standard on automated lines, cycling between high peak current (droplet spray transfer) and low background current, minimizing heat input and preventing burn-through on thin-walled ($1.5 - 2.0\text{ mm}$) tubes.
- **Heat-Affected Zone (HAZ) Metallurgy:**  
  Adjacent to the fusion zone, parent metal reaches temperatures below melting but above austenitizing temperature ($A_3$). Rapid conductive cooling by the cold steel tube creates a brittle **martensitic HAZ**, prone to cold cracking unless preheated or welded with low-hydrogen wire.

### 3.2 Automated Laser Welding in Battery Pack Assembly
- **Application:** Micro-joining of copper and aluminum busbars to 4680 cell terminals in the battery pack cleanroom.
- **Why Laser Welding?** Laser welding (Fiber / Blue laser, $\lambda = 450 - 1070\text{ nm}$) delivers high energy density ($> 10^6\text{ W/cm}^2$) in millisecond pulses, creating strong metallurgical bonds without transferring damaging heat into the active lithium-ion cell jelly roll ($T_{\text{cell}} < 60^\circ\text{C}$ during welding).
- **Copper vs Aluminum Laser Challenges:** Copper has high optical reflectivity ($> 95\%$ for standard infrared lasers) and extreme thermal conductivity. Ola utilizes green/blue laser wavelengths where copper absorption jumps to $> 40\%$, ensuring spatter-free joints.

---

## 4. Polymer Injection Molding for Body Panels

Ola S1 Pro and S1 X exterior body panels (front apron, side panels, floorboard trim) are manufactured via automated plastic injection molding from high-impact **Polypropylene (PP)** and **Acrylonitrile Butadiene Styrene (ABS)**.

### 4.1 Process Parameters & PVT Behavior
The injection molding cycle consists of:
1. **Plastication:** Reciprocating screw melts polymer granules via barrel heater bands and mechanical shear friction ($200 - 240^\circ\text{C}$).
2. **Injection (Filling):** Screw drives forward as a ram, injecting molten polymer into the cooled steel mold under high pressure ($80 - 150\text{ MPa}$).
3. **Holding / Packing:** Extra molten polymer is packed into the cavity to compensate for volumetric thermal shrinkage ($\approx 1 - 2\%$).
4. **Cooling:** Represents $\approx 60 - 70\%$ of total cycle time. Conformal water cooling channels rapidly solidify the part.
5. **Ejection:** Mold opens; ejector pins strip the part.

### 4.2 Injection Molding Defects & Root-Cause Elimination
- **Sink Marks (Local surface depressions above internal ribs):**  
  *Cause:* Thick rib intersections solidify slower than the outer wall; volumetric shrinkage pulls the surface inward.  
  *Design Rule:* Rib base thickness must be restricted to **$\le 50 - 60\%$ of nominal wall thickness** ($t_{\text{rib}} \le 0.60 \cdot t_{\text{wall}}$).
- **Weld / Knit Lines (Visible weak lines where split flow fronts rejoin):**  
  *Cause:* Polymer melt flows around a core pin or door handle hole and meets cold.  
  *Remediation:* Relocate injection gates; increase mold temperature and injection velocity to ensure flow fronts fuse above melt temperature.
- **Flash (Thin excess plastic creeping between parting surfaces):**  
  *Cause:* Injection hydraulic force exceeds machine clamping tonnage, forcing die halves apart.  
  *Remediation:* Increase machine clamp tonnage; reduce peak injection pressure.

---

## 5. Surface Finishing & Automated Paint Shop

The Futurefactory operates a fully automated paint shop designed by Dürr:
1. **Pretreatment & Zinc Phosphating:** High-pressure spray cleaning and degreasing removes rolling oils and drawing lubricants, followed by zinc phosphate conversion coating for corrosion adhesion.
2. **Cathodic Electro-Deposition (CED / E-Coat):**  
   The entire steel chassis is submerged in a 20,000-liter water-borne primer bath. The frame acts as a cathode ($-$), attracting positively charged paint polymer particles. This guarantees complete primer coverage inside hollow tubes and hidden crevices.
3. **Baking Oven:** Cures CED primer at $170 - 180^\circ\text{C}$ for 20 minutes.
4. **Robotic Topcoat & Clearcoat Application:**  
   High-speed rotating bells (electrostatic atomizers spinning at $40,000\text{ RPM}$) charge paint droplets to $-60\text{ kV}$, creating an electrostatic attraction to the grounded chassis that minimizes paint overspray waste ($> 85\%$ transfer efficiency).

---

## 6. Gigafactory Lithium-Ion Cell Assembly Operations

Inside the Ola Gigafactory cleanrooms, the **4680 cylindrical Bharat Cell** is produced through a sequential multi-stage chemical and mechanical manufacturing pipeline:

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                        4680 BHARAT CELL MANUFACTURING SEQUENCE                         │
└────────────────────────────────────────────────────────────────────────────────────────┘
  [ELECTRODE PREPARATION]
  1. Slurry Mixing: High-shear vacuum mixing of active materials, PVDF, and NMP solvent.
  2. Slot-Die Coating: Continuous high-speed roll-to-roll coating onto Al (cathode) and Cu (anode) foils.
  3. Calendering: Heavy heated steel rollers compress electrode porosity to exact target density (g/cc).
  4. Slitting: Precision laser or rotary knives slice master rolls into 80 mm wide ribbon strips.
      │
      ▼
  [CELL ASSEMBLY IN ULTRA-DRY ROOM (Dew Point < -40°C)]
  5. Tabless Notch Forming: High-speed laser cutting forms continuous shingled edge foil contacts.
  6. Jelly-Roll Winding: Continuous automated winding of cathode, separator, and anode ribbons.
  7. Can Insertion: Jelly roll inserted into nickel-plated steel cylindrical can (46 mm dia).
  8. Laser Terminal Welding: Tabless shingled foil ends are laser-welded directly to the can bottom.
  9. Grooving & Insulating: Mechanical necking creates a seat for the top seal.
  10. Electrolyte Filling: Vacuum injection of organic liquid electrolyte (LiPF6 in EC/DMC).
  11. Top Cap Sealing: Hermetic crimping or laser-sealing of the safety vent cap.
      │
      ▼
  [FORMATION, AGING & QUALITY SCREENING]
  12. Formation Cycling: Automated charging/discharging racks create the protective SEI layer.
  13. High-Temperature Aging: Stored for 7 to 14 days at 45°C to detect internal micro-shorts.
  14. End-of-Line Screening: Open Circuit Voltage (OCV) and AC Internal Resistance (ACIR) grading.
```

---
*End of Manufacturing Processes & Plant Operations.*
