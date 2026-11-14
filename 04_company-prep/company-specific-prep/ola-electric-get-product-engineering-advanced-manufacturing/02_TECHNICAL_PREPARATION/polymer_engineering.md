# Polymer Engineering & Composites: EV Battery & Body Applications
**Target Role:** Graduate Engineer Trainee (GET) — Product Engineering & Advanced Manufacturing  
**Company:** Ola Electric Mobility Limited  
**Standard:** Engineering Polymers, Reinforced Composites & Flame Retardancy  

---

## 1. Thermoplastics vs Thermosets: Molecular Architecture

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                        THERMOPLASTICS VS THERMOSETTING POLYMERS                        │
├─────────────────────┬──────────────────────────┬───────────────────────────────────────┤
│ Property            │ Thermoplastics           │ Thermosets                            │
├─────────────────────┼──────────────────────────┼───────────────────────────────────────┤
│ Molecular Structure │ Linear or branched chains│ Covalently cross-linked 3D network    │
│                     │ held by weak van der Waals│ chemical bonds (irreversible)         │
├─────────────────────┼──────────────────────────┼───────────────────────────────────────┤
│ Thermal Response    │ Softens & melts upon     │ Degrades/chars at high temp; cannot   │
│                     │ heating; can be re-molded│ be melted or reshaped                 │
├─────────────────────┼──────────────────────────┼───────────────────────────────────────┤
│ Recycling           │ 100% mechanically recycle│ Difficult / impossible to recycle     │
├─────────────────────┼──────────────────────────┼───────────────────────────────────────┤
│ Typical EV Examples │ S1 Pro/X body panels (PP,│ Epoxy structural resins, potting gels,│
│                     │ ABS), battery frames (PA)│ polyurethane foam cell encapsulation  │
└─────────────────────┴──────────────────────────┴───────────────────────────────────────┘
```

---

## 2. Viscoelasticity, Glass Transition ($T_g$) & Thermal Regimes

Unlike metals, polymers exhibit **viscoelastic behavior**—their mechanical properties are strongly dependent on both **operating temperature** and **strain rate (frequency)**:
- **Glass Transition Temperature ($T_g$):**  
  The temperature threshold where amorphous polymer regions transition from a rigid, glassy state to a rubbery, flexible state due to the onset of long-range segmental chain mobility.
  - *Engineering Rule:* For load-bearing structural parts (e.g., battery pack module brackets), the operating temperature range ($-10^\circ\text{C} \text{ to } +65^\circ\text{C}$) must remain **well below $T_g$** to prevent excessive creep deflection.
- **Creep (Time-Dependent Strain under Constant Load):**  
  A polymer component subjected to sustained bolt clamping force or battery pack dead weight experiences progressive strain over months:
  $$\varepsilon(t) = \varepsilon_0 + \beta t^m$$
  - *Design Mitigation:* Molded-in **brass or steel compression limiters** (collars) must be inserted into all bolted mounting holes. The bolt preload is absorbed entirely by the metal collar, preventing polymer creep relaxation and loss of clamping torque over time.

---

## 3. Engineering Polymers in Ola Electric Subsystems

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                        AUTOMOTIVE EV POLYMER APPLICATION MATRIX                        │
├───────────────────┬──────────────┬──────────────┬──────────────────────────────────────┤
│ Polymer Material  │ Modulus (GPa)│ Tensile (MPa)│ Primary Application at Ola Electric  │
├───────────────────┼──────────────┼──────────────┼──────────────────────────────────────┤
│ Polypropylene (PP)│ 1.2 – 1.6    │ 28 – 38      │ Under-seat storage bucket, inner trim│
│ (Impact Modified) │              │              │ Low cost, chemical/battery acid proof│
├───────────────────┼──────────────┼──────────────┼──────────────────────────────────────┤
│ ABS               │ 2.2 – 2.8    │ 40 – 50      │ S1 Pro painted exterior side panels  │
│                   │              │              │ Exceptional surface gloss, impact res│
├───────────────────┼──────────────┼──────────────┼──────────────────────────────────────┤
│ PA66-GF30         │ 8.5 – 10.0   │ 160 – 190    │ High-voltage battery pack cell module│
│ (30% Glass Fiber) │              │              │ brackets, motor terminal housings    │
├───────────────────┼──────────────┼──────────────┼──────────────────────────────────────┤
│ Polycarbonate (PC)│ 2.2 – 2.5    │ 60 – 72      │ Headlamp transparent lens cover      │
│                   │              │              │ Optical clarity, high impact shatter │
├───────────────────┼──────────────┼──────────────┼──────────────────────────────────────┤
│ Polyurethane (PU) │ 0.05 – 0.50  │ 5 – 25       │ Potting encapsulation between cells  │
│ Structural Foam   │              │              │ Vibration damping, thermal insulation│
└───────────────────┴──────────────┴──────────────┴──────────────────────────────────────┘
```

---

## 4. Fiber-Reinforced Composites (PA66-GF30)

Unreinforced nylon (PA66) has an elastic modulus of $\approx 2.8\text{ MPa}$ and softens significantly when absorbing moisture. Compounding with **$30\%$ chopped short glass fibers (PA66-GF30)** transforms the material:
1. **Modulus & Strength Multiplication:** Elastic modulus triples to $\approx 9.5\text{ GPa}$, while tensile strength increases to $> 175\text{ MPa}$.
2. **Fiber Orientation Anisotropy:**  
   During injection molding, molten polymer flow aligns glass fibers along the flow streamlines:
   - Longitudinal direction (parallel to flow): Maximum tensile stiffness ($E_\parallel \approx 9.5\text{ GPa}$).
   - Transverse direction (perpendicular to flow): Dominated by the polymer matrix ($E_\perp \approx 5.5\text{ GPa}$).
   - *Design Implication:* Injection mold gates must be oriented such that polymer flow aligns fibers along the primary service stress direction.

---

## 5. Battery Pack Flame Retardancy Standards (UL-94 V-0)

In EV battery enclosures, polymer covers and internal cell spacers must act as a firewall during thermal runaway:
- **The UL-94 Vertical Burning Test Standard:**
  - A vertical bar specimen is exposed to an open burner flame for 10 seconds.
  - **UL-94 V-0 (Mandatory for EV Battery Enclosures):**  
    1. Burning flame must extinguish within **$\le 10\text{ seconds}$** after each flame application.
    2. Total flaming combustion time for 5 specimens must not exceed $50\text{ seconds}$.
    3. Specimen must NOT drip burning particles that ignite dry surgical cotton placed $300\text{ mm}$ below.
  - *UL-94 V-1 / V-2:* Allows longer extinguishing times ($30\text{ s}$) or allows flaming drips (unacceptable for EV battery packs).
- **Halogen-Free Flame Retardant (HFFR) Additives:**  
  Older brominated flame retardants emit toxic, corrosive dioxin/furan fumes when ignited. Modern battery packs mandate halogen-free phosphorus/nitrogen additives (such as aluminum diethylphosphinate — AlPi) that promote surface **intumescent charring**, creating a thermal insulating foam layer that chokes oxygen from reaching the burning plastic.

---
*End of Polymer Engineering & Composites.*
