# Environmental Engineering

## Scope

Environmental engineering applies engineering principles to protect and restore the natural environment — covering water and air pollution control, solid and hazardous waste management, environmental impact assessment, climate resilience, and sustainability. Core competency for PSU roles (CPCB, SPCB, NEERI, CPHEEO) and consulting positions.

> **Related topics:** [`water-supply.md`](../hwre/water_supply/water-supply.md) · [`wastewater-engineering.md`](../hwre/wastewater/wastewater-engineering.md) · [`water-resources-engineering.md`](../hwre/water_resources/water-resources-engineering.md) · [`geotechnical.md`](../geotechnical/geotechnical.md)

---

## 1. Water Pollution & Quality Engineering

### Water Quality Parameters

| Parameter | Symbol | Unit | Significance |
|-----------|--------|------|--------------|
| pH | pH | — | Acidity/alkalinity (6.5–8.5 drinking) |
| Dissolved Oxygen | DO | mg/L | Aquatic life health (≥ 5 mg/L) |
| BOD (5-day, 20°C) | BOD₅ | mg/L | Biodegradable organic load |
| Chemical Oxygen Demand | COD | mg/L | Total oxidizable matter |
| Total Dissolved Solids | TDS | mg/L | Mineralization (≤ 500 mg/L drinking) |
| Turbidity | NTU | NTU | Suspended particles (≤ 1 NTU drinking) |
| Hardness | — | mg/L as CaCO₃ | ≤ 200 mg/L desirable |
| Chloride | Cl⁻ | mg/L | ≤ 250 mg/L (IS 10500) |
| Fluoride | F⁻ | mg/L | 0.6–1.2 mg/L optimal |
| Coliforms | MPN | MPN/100 mL | Zero for drinking water |

### BOD Kinetics

**First-order BOD reaction:**
$$\frac{dL}{dt} = -k_1 L$$

$$L_t = L_0 \, e^{-k_1 t}$$

$$y_t = L_0 \left(1 - e^{-k_1 t}\right)$$

Where:
- $L_0$ = initial BOD (ultimate carbonaceous BOD)
- $L_t$ = BOD remaining at time $t$
- $y_t$ = BOD exerted at time $t$
- $k_1$ = reaction rate constant (base $e$, per day at 20°C)

**Temperature correction:**
$$k_{T} = k_{20} \cdot \theta^{(T - 20)}$$

Where $\theta = 1.047$ for BOD.

**Standard BOD test:**
- Incubation: 5 days at 20°C in dark
- $\text{BOD}_5 = (D_1 - D_2) - (B_1 - B_2) \times \text{dilution factor}$
- $D_1$ = initial DO of diluted sample, $D_2$ = final DO
- $B_1, B_2$ = DO of blank

### DO Sag Curve (Streeter-Phelps)

$$\frac{dD}{dt} = k_1 L - k_2 D$$

$$D_t = \frac{k_1 L_0}{k_2 - k_1}\left(e^{-k_1 t} - e^{-k_2 t}\right) + D_0 \, e^{-k_2 t}$$

**Critical deficit:**
$$D_c = \frac{k_1 L_0}{k_2} \, e^{-k_1 t_c}$$

**Time to critical deficit:**
$$t_c = \frac{1}{k_2 - k_1} \ln \left[\frac{k_2}{k_1}\left(1 - \frac{D_0(k_2 - k_1)}{k_1 L_0}\right)\right]$$

Where:
- $D$ = oxygen deficit (mg/L)
- $k_1$ = deoxygenation rate constant
- $k_2$ = reaeration rate constant
- $D_0$ = initial DO deficit

**Typical $k_2$ values (base $e$, 20°C):**

| Stream Condition | $k_2$ (day⁻¹) |
|------------------|----------------|
| Slow-moving, deep | 0.1–0.5 |
| Moderate | 0.5–1.5 |
| Rapid, turbulent | 1.5–5.0 |

### Coagulation & Flocculation

**Coagulants:**

| Coagulant | Formula | Optimal pH |
|-----------|---------|------------|
| Alum | Al₂(SO₄)₃·18H₂O | 6.0–7.5 |
| Ferric chloride | FeCl₃ | 6.0–11.0 |
| Ferrous sulfate | FeSO₄ | 8.5–11.0 |
| PAC (poly-aluminium chloride) | Al₂(OH)ₙCl₍₆₋ₙ₎ | 5.0–9.0 |

**Dosing:** For alum + bicarbonate alkalinity:
$$\text{Alum dose} + \text{Alkalinity consumed} \approx \frac{9 \times \text{Alum dose}}{1}$$

Every 1 mg/L of alum consumes approximately 0.5 mg/L alkalinity as CaCO₃.

**Flocculation:**
- Velocity gradient: $G = \sqrt{\frac{P}{\mu V}}$
- $GT$ value: 30,000–60,000 (typical for water treatment)
- Detention time: 20–40 minutes

### Sedimentation

**Surface loading rate (overflow rate):**
$$v_s = \frac{Q}{A}$$

**Stokes' Law (discrete particle settling):**
$$v_s = \frac{g(\rho_s - \rho_w) d^2}{18 \mu}$$

**Settling zones:**

| Zone | Description |
|------|-------------|
| Inlet zone | Flow distribution, energy dissipation |
| Settling zone | Main settling volume |
| Outlet zone | Clarified water collection |
| Sludge zone | Sludge storage and removal |

### Filtration

**Rapid sand filtration:**

| Parameter | Value |
|-----------|-------|
| Loading rate | 3,000–6,000 L/hr/m² |
| Media | Sand (0.45–0.70 mm), gravel base |
| Backwash rate | 15–25 m/hr |
| Run time | 24–72 hours |
| Head loss | 1.5–3.0 m |

**Slow sand filtration:**

| Parameter | Value |
|-----------|-------|
| Loading rate | 100–400 L/hr/m² |
| Media | Fine sand (0.15–0.35 mm) |
| Schmutzdecke | Biological layer on top |
| Removal | 90–99% bacteria |

### Disinfection

**Chlorination:**

$$\text{Breakpoint chlorination curve:}}$$

| Phase | Dose | Reaction |
|-------|------|----------|
| Zone 1 | 0–0.1 mg/L | Oxidation of Fe²⁺, Mn²⁺, H₂S |
| Zone 2 | 0.1–0.5 mg/L | Reaction with organics |
| Zone 3 | 0.5–1.0 mg/L | Combined residual builds |
| Zone 4 | Above breakpoint | Free residual appears |

**CT concept:**
$$\text{Inactivation} = f(\text{Concentration} \times \text{Contact time})$$

For 4-log Giardia removal at pH 7, 15°C: CT ≈ 100 mg·min/L

**Chlorine demand = Applied chlorine − Free chlorine residual**

### Advanced Treatment

| Process | Target | Mechanism |
|---------|--------|-----------|
| Activated carbon (GAC/PAC) | Organics, taste, odor | Adsorption |
| Membrane (UF/NF/RO) | TDS, pathogens, micropollutants | Size exclusion / solution-diffusion |
| UV disinfection | Pathogens | DNA damage (254 nm) |
| Ozonation | Pathogens, organics, color | Oxidation (O₃) |
| Ion exchange | Hardness, nitrate, fluoride | Ion replacement |
| Advanced oxidation (AOPs) | Recalcitrant organics | OH• radical generation |

---

## 2. Wastewater Treatment Engineering

### Treatment Levels

| Level | Process | Target |
|-------|---------|--------|
| Preliminary | Screening, grit removal | Large solids, grit |
| Primary | Sedimentation | 50–70% SS, 25–40% BOD |
| Secondary (biological) | Activated sludge, trickling filter | 85–95% BOD removal |
| Tertiary / Advanced | Filtration, nutrient removal | < 10 mg/L BOD, nutrient limits |
| Sludge treatment | Thickening, digestion, dewatering | Volume reduction, stabilization |

### Activated Sludge Process (ASP)

**Food to Microorganism ratio:**
$$F/M = \frac{Q \cdot S_0}{V \cdot X}$$

Where:
- $Q$ = influent flow (m³/d)
- $S_0$ = influent BOD (mg/L)
- $V$ = aeration tank volume (m³)
- $X$ = MLSS (mg/L)

**Typical ranges:**

| Parameter | Conventional | Extended Aeration |
|-----------|-------------|-------------------|
| F/M | 0.2–0.6 | 0.05–0.15 |
| MLSS (mg/L) | 1500–3000 | 3000–6000 |
| SRT (days) | 5–15 | 20–40 |
| HRT (hours) | 4–8 | 18–36 |
| DO (mg/L) | 1.5–2.5 | 1.5–2.5 |

**Solids Retention Time (SRT / sludge age):**
$$\theta_c = \frac{V \cdot X}{Q_w \cdot X_r + (Q - Q_w) \cdot X_e}$$

**BOD removal efficiency:**
$$\eta = \frac{S_0 - S_e}{S_0} \times 100\%$$

**Monod kinetics for biological growth:**
$$\mu = \mu_{max} \frac{S}{K_s + S}$$

Where:
- $\mu$ = specific growth rate
- $\mu_{max}$ = maximum specific growth rate
- $K_s$ = half-saturation constant
- $S$ = substrate concentration

### Trickling Filters

| Type | Depth | Media Size | BOD Loading |
|------|-------|-----------|-------------|
| Low-rate | 1.5–2.5 m | 25–100 mm | 0.08–0.4 kg/m³/d |
| High-rate | 1.5–2.5 m | 25–100 mm | 0.4–4.8 kg/m³/d |
| Roughing | 3–12 m | 25–100 mm | 0.6–7.2 kg/m³/d |

**NRC formula:**
$$E = \frac{100}{1 + 0.4432 \sqrt{\frac{W}{V \cdot F}}}$$

### Nutrient Removal

**Nitrogen removal (nitrification-denitrification):**

| Step | Reaction | Conditions |
|------|----------|------------|
| Nitrification | NH₄⁺ → NO₂⁻ → NO₃⁻ | Aerobic, autotrophs |
| Denitrification | NO₃⁻ → NO₂⁻ → N₂ | Anoxic, heterotrophs |

**Nitrification oxygen requirement:**
$$\text{O}_2 = 4.57 \, \text{NH}_4\text{-N oxidized (mg/L)}$$

**Denitrification carbon requirement:**
$$\text{BOD}_5 = 2.87 \, \text{NO}_3\text{-N reduced (mg/L)}$$

**Phosphorus removal:**
- Chemical: Al³⁺ or Fe³⁺ precipitation
  - Alum P removal: 1 mol Al removes 1 mol P
  - Dose (as Al₂(SO₄)₃): ~2 mol per mol P removed
- Biological (EBPR): Anaerobic selector → PAOs release P, then uptake excess P in aerobic zone

### Sludge Treatment

| Process | Purpose | Key Parameter |
|---------|---------|---------------|
| Gravity thickening | Concentrate primary sludge | Overflow rate 30–50 m³/m²/d |
| Anaerobic digestion | Stabilize, produce biogas | 35°C (mesophilic), 15–20 days SRT |
| Aerobic digestion | Stabilize (small plants) | 15–25 days |
| Belt press dewatering | Reduce water content | Cake solids 18–35% |
| Centrifuge dewatering | Rapid dewatering | Cake solids 20–35% |

**Biogas composition:** ~60–65% CH₄, ~35–40% CO₂

**Methane production:**
$$\text{CH}_4 = 0.35 \times \text{VS destroyed (kg)}$$

---

## 3. Air Pollution & Control Engineering

### Air Quality Standards

**NAAQS (National Ambient Air Quality Standards, India):**

| Pollutant | Averaging Time | Residential (µg/m³) |
|-----------|---------------|---------------------|
| PM₂.₅ | Annual | 40 |
| PM₂.₅ | 24-hour | 60 |
| PM₁₀ | Annual | 60 |
| PM₁₀ | 24-hour | 100 |
| SO₂ | Annual | 50 |
| SO₂ | 24-hour | 80 |
| NO₂ | Annual | 40 |
| NO₂ | 24-hour | 80 |
| CO | 8-hour | 4000 |
| CO | 1-hour | — |
| O₃ | 8-hour | 100 |
| Lead | Annual | 0.5 |

### Pollutant Formation Mechanisms

| Type | Formation |
|------|-----------|
| **Primary** | Emitted directly (CO, SO₂, PM, VOCs) |
| **Secondary** | Formed by atmospheric reactions (O₃, PAN, H₂SO₄, NH₄NO₃) |

**Photochemical smog:**
$$\text{NO}_2 + h\nu \rightarrow \text{NO} + \text{O}$$
$$\text{O} + \text{O}_2 \rightarrow \text{O}_3$$
$$\text{O}_3 + \text{NO} \rightarrow \text{NO}_2 + \text{O}_2 \quad \text{(without VOCs)}$$

With VOCs: VOCs react with OH• and NO to shift the photostationary state, causing O₃ accumulation.

### Stack Design & Dispersion

**Plume rise (Briggs equation, neutral):**
$$\Delta h = \frac{1.6 F^{1/3} x^{2/3}}{\bar{u}}$$

Where:
- $F$ = buoyancy flux = $g v_s d_s^2 \frac{T_s - T_a}{4 T_s}$
- $x$ = downwind distance
- $\bar{u}$ = mean wind speed at stack top
- $d_s$ = stack exit diameter

**Gaussian dispersion model:**
$$C(x, y, 0) = \frac{Q}{2\pi \bar{u} \sigma_y \sigma_z} \exp\left(-\frac{y^2}{2\sigma_y^2}\right) \left[\exp\left(-\frac{(z-H)^2}{2\sigma_z^2}\right) + \exp\left(-\frac{(z+H)^2}{2\sigma_z^2}\right)\right]$$

Where:
- $C$ = concentration at (x, y, z)
- $Q$ = emission rate (g/s)
- $\sigma_y, \sigma_z$ = dispersion coefficients (functions of stability class and downwind distance)
- $H$ = effective stack height ($H = h_s + \Delta h$)

**Atmospheric Stability Classes (Pasquill-Gifford):**

| Class | Condition | $\sigma_y$ | $\sigma_z$ |
|-------|-----------|-----------|-----------|
| A | Strong instability | Large | Very large |
| B | Moderate instability | Large | Large |
| C | Slight instability | Medium | Medium |
| D | Neutral | Small | Small |
| E | Slight stability | Very small | Very small |
| F | Moderate stability | Very small | Very small |

**Ground-level maximum concentration occurs at:** $x = \left(\frac{H}{\sigma_z}\right) \cdot \frac{dx}{d\sigma_z}$

### Air Pollution Control Devices

| Device | Target | Mechanism | Efficiency |
|--------|--------|-----------|------------|
| Cyclone separator | Coarse PM (> 10 µm) | Centrifugal separation | 70–90% |
| ESP | Fine PM (0.01–10 µm) | Electrostatic precipitation | 95–99% |
| Baghouse (fabric filter) | Fine PM | Filtration | 99–99.9% |
| Wet scrubber | PM + some gases | Impaction + absorption | 90–99% |
| Venturi scrubber | Fine PM | High-energy impaction | 95–99% |
| Packed bed scrubber | Gases (SO₂, HCl) | Absorption | 90–99% |
| Selective catalytic reduction (SCR) | NOₓ | NH₃ + NOₓ → N₂ + H₂O | 80–90% |
| Activated carbon injection | Hg, dioxins | Adsorption | 90–99% |

**Cyclone cut-size:**
$$d_{50} = \sqrt{\frac{9 \mu W}{2\pi N \rho_p V_i}}$$

Where:
- $W$ = cyclone body width
- $N$ = number of turns (typically 5)
- $V_i$ = inlet velocity (typically 15–20 m/s)

**ESP design equation:**
$$\eta = 1 - e^{-wA/Q}$$

Where:
- $w$ = drift velocity
- $A$ = collecting plate area
- $Q$ = gas flow rate

---

## 4. Solid & Hazardous Waste Management

### Solid Waste Classification

| Category | Source | Examples |
|----------|--------|----------|
| Municipal (MSW) | Domestic, commercial | Food, paper, plastics |
| Industrial | Manufacturing | Slag, fly ash, chemical waste |
| Hazardous | Chemical processes | Solvents, heavy metals, radioactive |
| Biomedical | Healthcare | Infectious, sharps, pathological |
| E-waste | Electronics | PCBs, CRTs, batteries |
| Construction & Demolition | Building activities | Concrete, bricks, wood |

### Waste Characterization

**Moisture content:**
$$MC = \frac{W_{wet} - W_{dry}}{W_{wet}} \times 100\%$$

**Volatile solids / combustible fraction:**
$$VS = \frac{W_{dry} - W_{ash}}{W_{dry}} \times 100\%$$

**Calorific value (Dulong's formula):**
$$CV = 337C + 1419(H - O/8) + 93S \quad (\text{kJ/kg})$$

**Landfill gas generation:**
$$\text{CH}_4 = 0.5 \times (MC + VS_{dm}) \times L_0 \times (1 - e^{-kt})$$

Where $L_0$ = methane generation potential, $k$ = decay rate.

### Sanitary Landfill Design

| Component | Design Criteria |
|-----------|----------------|
| Bottom liner | HDPE (1.5–2.0 mm) + compacted clay (≤ 10⁻⁷ cm/s) |
| Leachate collection | Gravel drainage layer (30 cm) + perforated pipes |
| Leachate quality | BOD 100–60,000 mg/L; COD 200–800,000 mg/L |
| Landfill gas | 50–70% CH₄; can be recovered for energy |
| Daily cover | 15 cm soil or alternative daily cover |
| Final cover | Soil + geomembrane + topsoil |
| Cell height | 2–3 m per lift |

**Landfill gas composition:** CH₄ (45–60%), CO₂ (40–55%), N₂, O₂, trace H₂S

**Methane oxidation in cover:** 10–40% of generated methane oxidized in cover soil

### Hazardous Waste

**RCRA classification (US) / Hazardous Waste Management Rules (India, 2016):**

| Characteristic | Test | Threshold |
|----------------|------|-----------|
| Ignitability | Flash point | < 60°C |
| Corrosivity | pH | ≤ 2 or ≥ 12.5 |
| Reactivity | Various | Unstable under normal conditions |
| Toxicity | TCLP | Leachate limits for 40 metals/organics |

**TCLP (Toxicity Characteristic Leaching Procedure):**
- Extract with acetic acid (pH ~2.88 or ~4.93)
- Analyze leachate for heavy metals and organics

---

## 5. Environmental Impact Assessment (EIA)

### EIA Process Steps

| Step | Activity |
|------|----------|
| 1 | Screening — Determine if EIA is required |
| 2 | Scoping — Identify key environmental issues |
| 3 | Baseline data collection | 
| 4 | Impact prediction (quantitative models) |
| 5 | Mitigation measures and alternatives |
| 6 | Environmental Management Plan (EMP) |
| 7 | Public hearing and consultation |
| 8 | Decision-making by regulatory authority |
| 9 | Post-project monitoring |

### Noise Assessment

| Area | Daytime Limit dB(A) | Nighttime Limit dB(A) |
|------|---------------------|-----------------------|
| Industrial | 75 | 70 |
| Commercial | 65 | 55 |
| Residential | 55 | 45 |
| Silence zone | 50 | 40 |

**Noise level from point source (inverse square law):**
$$L_p = L_w - 20 \log_{10}(r) - 11$$

**Combined noise level:**
$$L_{total} = 10 \log_{10}\left(\sum 10^{L_i/10}\right)$$

---

## 6. Climate Change & Sustainability in Civil Engineering

### Carbon Footprint Estimation

| Material | CO₂ Emission (kg CO₂/kg) |
|----------|--------------------------|
| Cement (Portland) | 0.9 |
| Steel (virgin) | 1.8 |
| Steel (recycled) | 0.4 |
| Aluminium | 8.0 |
| Concrete (typical) | 0.13 per kg |
| Timber | -1.6 (sequestration) |

### Green Building & Rating

| System | Country | Key Credits |
|--------|---------|-------------|
| LEED | USA | Energy, water, materials, indoor quality |
| GRIHA | India | Energy, water, waste, biodiversity |
| BREEAM | UK | Energy, transport, materials, pollution |
| IGBC | India | Indian Green Building Council |

### Stormwater & Sustainable Urban Drainage (SUDS)

| Practice | Benefit |
|----------|---------|
| Permeable pavement | Reduce runoff, recharge groundwater |
| Bioswale / rain garden | Filter and detain runoff |
| Green roof | Reduce peak flow, insulation |
| Rainwater harvesting | Water conservation, flood mitigation |
| Detention basin | Peak flow reduction |

---

## 7. Interview Quick-Reference

### Most Asked Questions

| # | Question | Key Points |
|---|----------|------------|
| 1 | What is BOD and COD? Difference? | BOD = biodegradable (5 days, 20°C); COD = total oxidizable |
| 2 | Explain Streeter-Phelps DO sag | Deoxygenation + reaeration → critical deficit point |
| 3 | How does an activated sludge plant work? | Aeration tank (biological) → secondary clarifier → return sludge |
| 4 | What is F/M ratio? Typical values? | 0.2–0.6 conventional, 0.05–0.15 extended aeration |
| 5 | Explain nitrification and denitrification | NH₄⁺→NO₃⁻ (aerobic), NO₃⁻→N₂ (anoxic) |
| 6 | Design a sedimentation tank | Surface overflow rate, detention time, weir loading rate |
| 7 | What is the Gaussian plume model? | C(x,y,z) = f(Q, u, σy, σz, H) — stability classes |
| 8 | ESP efficiency? | η = 1 - exp(-wA/Q); 95–99% for PM |
| 9 | What are primary, secondary, tertiary treatment? | Physical → Biological → Advanced (nutrient/chemical) |
| 10 | EIA process steps? | Screening → Scoping → Baseline → Impact → Mitigation → EMP → Public hearing → Decision → Monitoring |
| 11 | Landfill leachate — composition and management? | BOD 100–60k mg/L, collection + treatment |
| 12 | How is chlorine dose determined? | Breakpoint curve, CT concept, coliform testing |
| 13 | What is the turnover ratio in ASP? | Recirculation ratio = Q_r/Q; typically 0.25–0.50 |
| 14 | Difference between BOD and TOC? | BOD = biological oxidation time; TOC = total carbon (instant measurement) |
| 15 | Explain activated carbon adsorption | Freundlich / Langmuir isotherms, breakthrough curve |

### Key Formulas Summary

| Formula | Use |
|---------|-----|
| $y_t = L_0(1-e^{-k_1 t})$ | BOD exerted at time t |
| $D_t = \frac{k_1 L_0}{k_2 - k_1}(e^{-k_1 t} - e^{-k_2 t}) + D_0 e^{-k_2 t}$ | DO deficit (Streeter-Phelps) |
| $F/M = \frac{Q \cdot S_0}{V \cdot X}$ | Food to microorganism ratio |
| $\eta = 1 - e^{-wA/Q}$ | ESP efficiency |
| $C = \frac{Q}{2\pi \bar{u}\sigma_y\sigma_z} \exp(...)$ | Gaussian plume concentration |
| $G = \sqrt{\frac{P}{\mu V}}$ | Velocity gradient (flocculation) |
| $CT = \frac{D_1 - D_2}{D_0 - D_c}$ | Chlorine contact time for inactivation |

### Numerical Practice Problems

**Problem 1 — BOD Calculation:**
A wastewater sample has 5-day BOD of 180 mg/L at 20°C. The reaction rate constant $k_1 = 0.23$ day⁻¹ (base $e$). Find the ultimate BOD and the 3-day BOD at 25°C.

> **Solution:** $L_0 = \frac{180}{1 - e^{-0.23 \times 5}} = \frac{180}{1 - 0.317} = 264$ mg/L. At 25°C: $k_{25} = 0.23 \times 1.047^5 = 0.289$ day⁻¹. $y_3 = 264(1 - e^{-0.289 \times 3}) = 264 \times 0.578 = 152.6$ mg/L.

**Problem 2 — DO Sag:**
A river receives wastewater discharge. The initial deficit is $D_0 = 2$ mg/L, $L_0 = 200$ mg/L, $k_1 = 0.3$ day⁻¹, $k_2 = 0.8$ day⁻¹. Find the time and magnitude of critical deficit.

> **Solution:** $t_c = \frac{1}{0.8 - 0.3} \ln\left[\frac{0.8}{0.3}\left(1 - \frac{2(0.8 - 0.3)}{0.3 \times 200}\right)\right] = 2 \ln\left[2.667 \times 0.9833\right] = 2 \times 0.974 = 1.95$ days. $D_c = \frac{0.3 \times 200}{0.8} e^{-0.3 \times 1.95} = 75 \times 0.557 = 41.8$ mg/L.

**Problem 3 — ESP Efficiency:**
An ESP has a plate area of 5000 m², gas flow of 50 m³/s, and drift velocity of 0.05 m/s. Find collection efficiency.

> **Solution:** $\eta = 1 - e^{-0.05 \times 5000/50} = 1 - e^{-5} = 1 - 0.0067 = 99.3\%$

---

## 🗺️ Subject Roadmap

```
Beginner                    Intermediate                   Advanced                      Interview
─────────────────────────────────────────────────────────────────────────────────────────────────────
Water quality params  →  BOD kinetics/Streeter-Phelps →  Advanced oxidation           →  BOD vs COD interpretation
Treatment basics      →  Coagulation-flocculation      →  Membrane bioreactors        →  Treatment train logic
Air pollution basics  →  Gaussian plume model          →  Carbon capture              →  CPCB standards
Solid waste          →  landfill design               →  Waste-to-energy             →  3R principles
```

> **Priority:** `P0 — Must Know` · **Tags:** `ENVIRONMENTAL` `HWRE`

---

## ❓ Question Bank (Selected)

### A. Basic Concept
1. What are the key water quality parameters?
2. Explain the Streeter-Phelps DO sag curve.
3. What is BOD and how does it differ from COD?

### B. WHY Questions
1. **Why** is the DO sag curve important for wastewater discharge design?
   - It predicts the minimum dissolved oxygen downstream of a discharge point, ensuring aquatic life is protected.

2. **Why** is the BOD test done at 20°C for 5 days?
   - 20°C approximates average river temperature; 5 days captures ~65–70% of ultimate BOD, balancing test duration and information.

3. **Why** is coagulation needed before sedimentation?
   - Colloidal particles have negative charges preventing settling. Coagulants neutralize these charges, enabling flocculation.

---

## 🎤 Interview Answer Format

### High-Value Q: "Explain the Streeter-Phelps equation."

**30-second answer:**
"The Streeter-Phelps equation models the oxygen sag in a river downstream of a wastewater discharge. It balances deoxygenation (BOD decay) against reaeration from the atmosphere. The critical deficit occurs at time $t_c$ where the rate of deoxygenation equals reaeration."

**Key equation:**
$D_t = \frac{k_1 L_0}{k_2 - k_1}(e^{-k_1 t} - e^{-k_2 t}) + D_0 e^{-k_2 t}$

---

## 🔗 Cross-Links

- [`water-supply.md`](../../core/hwre/water_supply/water-supply.md) — Water treatment
- [`wastewater-engineering.md`](../../core/hwre/wastewater/wastewater-engineering.md) — WW treatment
- [`hydrology.md`](../../core/hwre/hydrology/hydrology.md) — Urban hydrology, SWMM

---

## 8. Key References

| Resource | Use |
|----------|-----|
| Peavy, Rowe & Tchobanoglous — *Environmental Engineering* | Comprehensive textbook |
| Metcalf & Eddy — *Wastewater Engineering* | Wastewater treatment bible |
| CPHEEO Manual (India) | Indian water supply & sanitation standards |
| CPCB Guidelines | Emission/effluent standards |
| IS 10500:2012 | Drinking water quality standards |
| CSE 2014 Air Quality Standards | National ambient air quality |

---

> **Last Updated:** 2026-09-03
> **Maintained by:** DKS IITK Civil/HWRE Placement 2026
> **Version:** 1.0 — Comprehensive Environmental Engineering Guide
