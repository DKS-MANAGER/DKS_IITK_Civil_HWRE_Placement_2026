# Transportation Engineering

## Scope

Transportation engineering covers the planning, design, operation, and management of facilities for all modes of transportation — highways, railways, airports, and harbours. Core competency for PSU roles (NHAI, IRCON, Airport Authority, Railways), consulting firms, and urban planning.

> **Related topics:** [`structures.md`](../structures/structures.md) · [`geotechnical.md`](../geotechnical/geotechnical.md) · [`infrastructure-engineering-management.md`](../infrastructure/infrastructure-engineering-management.md) · [`geoinformatics.md`](../geoinformatics/geoinformatics.md)

---

## 1. Highway Engineering

### Highway Classification (IRC / MoRTH)

| Class | Description | Design Speed (km/h) | Carriageway Width (m) |
|-------|-------------|---------------------|----------------------|
| NH / Expressway | National highways, expressways | 100–120 | 7.0 (2-lane), 14.0 (4-lane) |
| SH | State highways | 80 | 7.0 |
| MDR | Major district roads | 65 | 7.0 |
| ODR | Other district roads | 50 | 6.0 |
| VR | Village roads | 30 | 3.75 |

### Geometric Design Standards (IRC)

#### Horizontal Curve Design

**Minimum radius:**
$$R_{min} = \frac{V^2}{127(e + f)}$$

Where:
- $V$ = design speed (km/h)
- $e$ = superelevation (decimal)
- $f$ = coefficient of lateral friction (0.15 for V ≤ 80 km/h, decreasing for higher speeds)

**IRC recommended values:**

| Design Speed (km/h) | $f$ | $e_{max}$ (plain) | $e_{max}$ (hilly) |
|---------------------|-----|---------------------|---------------------|
| 30 | 0.17 | 0.07 | 0.07 |
| 50 | 0.16 | 0.07 | 0.07 |
| 80 | 0.15 | 0.07 | 0.07 |
| 100 | 0.13 | 0.06 | — |
| 120 | 0.12 | 0.06 | — |

**Superelevation runoff:**
$$L_d = \frac{w \cdot n \cdot e \cdot b}{\Delta}$$

Where $w$ = width of lane, $n$ = number of lanes rotated, $b$ = extra widening, $\Delta$ = rate of rotation.

#### Vertical Curve Design

**Summit curve (parabolic):**
$$L = \frac{N \cdot V^2}{46.7}$$

Where:
- $N$ = algebraic difference of grades (%) = $|G_1 - G_2|$
- $L$ = length of vertical curve (m) — sight distance dependent

**For SSD ≥ L:**
$$L = \frac{N \cdot S^2}{4.4}$$

**For SSD < L:**
$$L = 2S - \frac{4.4}{N}$$

**Kearney's formula (sight distance):**
$$SSD = 0.278 \cdot V \cdot t + \frac{V^2}{254(f \pm G)}$$

Where:
- $t$ = reaction time (2.5 s IRC)
- $G$ = gradient (positive for uphill)
- $f$ = longitudinal friction coefficient

**SSD values (IRC):**

| Design Speed (km/h) | SSD (m) |
|---------------------|---------|
| 30 | 24 |
| 50 | 48 |
| 80 | 120 |
| 100 | 185 |
| 120 | 260 |

#### Sight Distance

| Type | Definition | Use |
|------|-----------|-----|
| **SSD (Stopping)** | Distance to see object, brake, stop | Curve design, summit curve |
| **OSD (Overtaking)** | Distance to safely overtake | Valley curve, horizontal curve |
| **Intermediate SSD** | 2× SSD | Meeting traffic on 2-lane road |

**Overtaking sight distance:**
$$OSD = d_1 + d_2 + d_3$$

- $d_1 = 0.278 \cdot V_b \cdot t$ (distance during reaction)
- $d_2 = 0.278 \cdot V_b \cdot t + \frac{a \cdot t^2}{2}$ (distance during overtaking)
- $d_3 = 0.278 \cdot V \cdot T$ (distance of oncoming vehicle)

### Highway Capacity (IRC 102)

| Lanes | Category | Capacity (pcu/hr) |
|-------|----------|-------------------|
| 2-lane, 2-way | Rolling | 3,500–4,000 |
| 4-lane divided | Rolling | 8,000–10,000 |
| 6-lane divided | Rolling | 12,000–15,000 |
| 8-lane expressway | Rolling | 16,000–20,000 |

**Passenger Car Unit (PCU) factors (IRC):**

| Vehicle Type | PCU Factor (Rolling) |
|-------------|---------------------|
| Car / Jeep | 1.0 |
| Two-wheeler | 0.5 |
| Auto-rickshaw | 0.75 |
| Bus / Truck | 3.0 |
| Trailer | 3.5–4.0 |
| Cycle | 0.5 |
| Cycle-rickshaw | 1.5 |

**Level of Service (LOS) for Indian conditions:**

| LOS | Description | Speed / Capacity |
|-----|-------------|-----------------|
| A | Free flow | < 35% capacity |
| B | Stable, slight delay | 35–55% capacity |
| C | Stable, acceptable delay | 55–75% capacity |
| D | Approaching unstable | 75–90% capacity |
| E | Unstable, significant delay | 90–100% capacity |
| F | Forced flow | > 100% capacity |

### Traffic Engineering

**Fundamental traffic flow equation:**
$$q = k \cdot v$$

Where:
- $q$ = flow (vehicles/hr)
- $k$ = density (vehicles/km)
- $v$ = space mean speed (km/hr)

**Greenshields model (speed-density relationship):**
$$v = v_f \left(1 - \frac{k}{k_j}\right)$$

- $v_f$ = free-flow speed
- $k_j$ = jam density

**Maximum flow (capacity):**
$$q_{max} = \frac{v_f \cdot k_j}{4}$$

**Optimal speed at capacity:** $v_{opt} = v_f/2$

**Optimal density at capacity:** $k_{opt} = k_j/2`

**Time headway vs space headway:**
$$h_t = \frac{1}{q}, \quad h_s = \frac{1}{k}$$

**Flow-density diagram (Greenshields):**
- Parabolic relationship between flow and density
- Peak at $q_{max} = v_f k_j / 4$

**Speed-flow diagram:**
- Parabolic shape
- Unstable region above $q_{max}$

### Traffic Studies

| Study | Method | Application |
|-------|--------|-------------|
| Speed study | Radar gun, GPS, video | Speed limits, enforcement |
| Volume study | Tube counters, video | Capacity, signal design |
| Origin-Destination | License plate, questionnaire | Route planning |
| Parking study | Field survey | Parking design |
| Accidents study | Police records | Safety analysis |

**Speed studies:**

| Measure | Formula | Description |
|---------|---------|-------------|
| Time mean speed | $\bar{v_t} = \frac{1}{n}\sum v_i$ | Arithmetic mean of spot speeds |
| Space mean speed | $\bar{v_s} = \frac{n}{\sum(1/v_i)}$ | Harmonic mean of spot speeds |
| 85th percentile speed | From cumulative frequency | Speed limit basis |

### Traffic Signal Design

**Webster's optimal cycle length:**
$$C_o = \frac{1.5L + 5}{1 - \sum Y_i}$$

Where:
- $L$ = total lost time per cycle (s)
- $Y_i = y_i / s_i$ = flow ratio for phase $i$ ($y_i$ = flow, $s_i$ = saturation flow)

**Effective green time:**
$$g_i = \frac{Y_i}{\sum Y_j}(C - L)$$

**Saturation flow:**
$$s = 525 \cdot w_h$$

Where $w_h$ = effective width of carriageway (m), for Indian conditions (IRC SP:88).

**Degree of saturation:**
$$X_i = \frac{q_i}{s_i \cdot (g_i/C)}$$

Design target: $X_i ≤ 0.85–0.90$

**All-red time (clearance):**
$$AR = \frac{W + L_v}{v}$$

Where $W$ = width of intersection, $L_v$ = vehicle length, $v$ = approach speed.

---

## 2. Pavement Design

### Flexible Pavement (IRC:37)

**Layer structure:**

| Layer | Material | Function |
|-------|----------|----------|
| Surface course | Bituminous concrete (BC) | Wear resistance, smooth ride |
| Binder course | Dense Bituminous Macadam (DBM) | Load distribution |
| Base | Water Bound Macadam (WBM) or Wet Mix Macadam (WMM) | Structural support |
| Sub-base | Granular sub-base (GSB) | Drainage, frost protection |
| Subgrade | Compacted soil | Foundation |

**CBR method (IRC:37-2018):**

Total pavement thickness = f(CBR, traffic)

| CBR (%) | Total Thickness for 10 msa (mm) | For 100 msa (mm) |
|---------|----------------------------------|-------------------|
| 2 | 520 | 780 |
| 3 | 440 | 670 |
| 5 | 350 | 550 |
| 10 | 240 | 400 |
| 15 | 190 | 330 |

(msa = million standard axles)

**IRC layer coefficients:**

| Layer | Material | Thickness Coefficient |
|-------|----------|----------------------|
| Surface (BC) | Asphalt concrete | 0.35 |
| Binder (DBM) | Dense bituminous macadam | 0.25 |
| Base (WMM) | Wet mix macadam | 0.15 |
| Sub-base (GSB) | Granular | 0.08 |

### Rigid Pavement (IRC:58)

**Westergaard's analysis:**

| Stress | Formula | Loading |
|--------|---------|---------|
| Interior stress | $\sigma_i = \frac{0.316 P}{h^2}\left[4\log_{10}\left(\frac{l}{b}\right) + 1.069\right]$ | Interior |
| Edge stress | $\sigma_e = \frac{0.572 P}{h^2}\left[4\log_{10}\left(\frac{l}{b}\right) + 0.359\right]$ | Edge |
| Corner stress | $\sigma_c = \frac{3P}{h^2}\left[1 - \left(\frac{a\sqrt{2}}{l}\right)^{0.6}\right]$ | Corner |

Where:
- $P$ = wheel load (kN)
- $h$ = slab thickness (mm)
- $l$ = radius of relative stiffness = $\sqrt[4]{\frac{Eh^3}{12(1-\mu^2)k}}$
- $b$ = equivalent radius of loading area
- $a$ = actual contact radius
- $E$ = modulus of elasticity, $k$ = modulus of subgrade reaction

**Radius of relative stiffness:**
$$l = \left(\frac{Eh^3}{12(1-\mu^2)k}\right)^{0.25}$$

**Typical values:**
- $l$ = 800–1500 mm (depending on slab thickness and subgrade)
- $k$ = 20–100 N/mm³

**Joint types:**

| Joint | Purpose | Detailing |
|-------|---------|-----------|
| Expansion | Allow thermal expansion | 20–25 mm gap, sealant |
| Contraction | Control shrinkage cracks | 1/4 to 1/3 of slab thickness |
| Construction | Phased construction | Dowel bars |
| Longitudinal | Lane construction | Tie bars (deformed steel) |

**Dowel bars:** Transfer load across joints; diameter 25–32 mm, length 450 mm, spacing 150–300 mm.

**Tie bars:** Hold slabs together; 12–16 mm diameter, 0.6–0.8% of slab area.

### Pavement Distress Types

| Distress | Flexible | Rigid |
|----------|----------|-------|
| Cracking | Fatigue, reflective, block | Transverse, corner, longitudinal |
| Deformation | Rutting, shoving, corrugation | Pumping, faulting |
| Surface | Bleeding, polishing, potholes | Surface erosion, scaling |
| Drainage | Stripping, moisture damage | Joint seal deterioration |

---

## 3. Railway Engineering

### Track Components

| Component | Function | Specification |
|-----------|----------|---------------|
| Rails | Support wheels, guide | 60 kg/m (BIS), 52 kg/m |
| Sleepers | Hold gauge, distribute load | Prestressed concrete (IRC standard) |
| Ballast | Drainage, stability | 25–50 mm crushed stone |
| Fishplate | Joint connection | 4-bolt / 6-bolt |
| Rail fastening | Secure rail to sleeper | Pandrol clips |

### Track Geometry

| Parameter | Standard Broad Gauge |
|-----------|---------------------|
| Gauge | 1676 mm |
| Rail weight | 60 kg/m (new), 52 kg/m |
| Sleeper spacing | 275–300 mm (c/c) |
| Ballast depth | 200–300 mm |
| Superelevation (max) | 165 mm (on curves) |
| Cant deficiency (max) | 75 mm |
| Cant excess (max) | 75 mm |

**Superelevation:**
$$e = \frac{G \cdot V^2}{127 \cdot R}$$

Where:
- $G$ = track gauge (m)
- $V$ = speed (km/h)
- $R$ = radius of curve (m)

**Cant deficiency:** When actual superelevation < equilibrium superelevation for the ruling speed.

**Equilibrium speed:** Speed at which superelevation equals cant for zero lateral thrust.

### Train Resistance

**Davis formula:**
$$R = A + BV + CV^2$$

Where:
- $A$ = journal resistance + track resistance (constant)
- $B$ = flange resistance (linear term)
- $C$ = aerodynamic resistance (speed-dependent)
- Typical: $R = 0.0016W + 0.00008WV + 0.000002WV^2$ (N per tonne)

### Gradient & Ruling Gradient

| Type | Gradient |
|------|----------|
| Ruling gradient (plain) | 1 in 150 (0.67%) |
| Ruling gradient (hilly) | 1 in 100 to 1 in 150 |
| Maximum (helper) | 1 in 37 |
| Station yard | 1 in 400 to 1 in 600 |

### Signalling

| System | Description |
|--------|-------------|
| Absolute block | Only one train per block section |
| Automatic block | Signals controlled by track circuits |
| Centralized traffic control (CTC) | Centralized signal control |
| ATP (Automatic Train Protection) | Speed control + braking |
| ETCS (European Train Control System) | Standardized train control |

---

## 4. Airport Engineering

### Airport Classification (ICAO / DGCA)

| Code | Wingspan (m) | Reference Field Length (m) |
|------|-------------|---------------------------|
| 1 | < 15 | < 800 |
| 2 | 15–24 | 800–1200 |
| 3A | 24–36 | 1200–1500 |
| 3B | 24–36 | 1500–1800 |
| 4A | 36–52 | 1800–2300 |
| 4B | 36–52 | 2300–2800 |
| 4E | 52–80 | ≥ 1800 |
| 4F | ≥ 65 | ≥ 1800 |

### Runway Design

**Runway length (ICAO Annex 14 / DGCA CAR):**
$$L_{required} = \frac{1}{2} \left(\frac{V^2}{2a} + \frac{V}{g \cdot T/S}\right)$$

Simplified empirical (DGCA):
$$L = \frac{V^2}{30\left(\frac{a}{g} \pm G\right)}$$

Where:
- $V$ = approach speed (km/h)
- $a$ = deceleration (m/s²)
- $G$ = effective gradient (uphill positive)
- $T/S$ = thrust-to-weight ratio

**Correction factors:**
- Elevation: +7% per 300 m above MSL
- Temperature: +1% per 1°C above standard temp
- Wet/contaminated: +15%
- Gradient: +20% per 1% gradient

**Runway orientation:**
- Oriented into wind (≥ 95% of wind operations)
- Wind rose analysis
- Crosswind component ≤ 37 km/h (Class 3+ airports)

**Runway width:**

| Code | Width (m) |
|------|-----------|
| 1 | 18 |
| 2 | 23 |
| 3 | 30 |
| 4A | 45 |
| 4B | 45 |
| 4E | 45 |
| 4F | 60 |

### Terminal Design

**Passenger building sizing:**
$$A = N_{peak} \times S_{per\_pax}$$

Where $S_{per\_pax}$ = 0.6–1.2 m²/passenger (terminal dependent).

**Aerodrome Reference Code:**

| Element 1 | Element 2 |
|-----------|-----------|
| Wingspan | Reference field length |

### Pavement Design (Airport)

| Parameter | Description |
|-----------|-------------|
| CBR method | Similar to highways but with aircraft loads |
| Airport CBR design | Based on gear configuration and tire pressure |
| Rigid pavement | Westergaard's method, adapted for aircraft |
| Aircraft loading | Gear configurations (single, dual, tandem, triple) |

### Airport Drainage

| System | Purpose |
|--------|---------|
| Surface drainage | Remove rainwater from runways/taxiways |
| Subsurface drainage | Prevent water table rise, remove seepage |
| Stormwater management | Detention/retention basins |

---

## 5. Harbour & Dock Engineering (Brief)

### Port Components

| Component | Description |
|-----------|-------------|
| Quay wall | Structure along berth for mooring |
| Jetty/Berth | Platform for loading/unloading |
| Breakwater | Wave protection |
| Harbour basin | Sheltered water area |
| Turning circle | For vessel manoeuvre |
| Approach channel | Deep-water navigation path |

### Wave Force (Morison Equation for slender structures)
$$F = \frac{1}{2} C_D \rho D |u| u + C_M \rho \frac{\pi D^2}{4} \frac{du}{dt}$$

Where $C_D$ = drag coefficient, $C_M$ = inertia coefficient, $u$ = water particle velocity.

### Breakwater Design

| Type | Material | Application |
|------|----------|-------------|
| Rubble mound | Stone, armor units | Most common |
| Vertical wall | Concrete caisson | Deep water, small space |
| Composite | Vertical on rubble | Mixed conditions |
| AI (Accropode, Tetrapod) | Concrete armor | Wave dissipation |

---

## 6. Transportation Software & Tools

| Software | Application |
|----------|-------------|
| **PTV Vissim** | Microscopic traffic simulation |
| **PTV Visum** | Macroscopic traffic planning |
| **Aimsun Next** | Multi-modal traffic simulation |
| **TransCAD** | GIS-based transportation planning |
| **Synchro / SimTraffic** | Signal timing optimization |
| **SIDRA INTERSECTION** | Intersection capacity analysis |
| **HEC-RAS** | Hydraulic modeling (culvert design) |
| **OpenRoads Designer** | Highway geometric design |
| **MX Roads** | Road alignment and design |
| **HPDS (IRC)** | Pavement design software |
| **KMONY / KENLAYER** | Rigid / flexible pavement analysis |
| **SAP2000 / MIDAS** | Bridge structural analysis |
| **Civil 3D** | Corridor modeling, grading |
| **GIS (QGIS / ArcGIS)** | Transportation network analysis |
| **SUMO / MATSim** | Open-source traffic simulation |

---

## 7. Interview Quick-Reference

### Most Asked Questions

| # | Question | Key Points |
|---|----------|------------|
| 1 | What is superelevation? How is it calculated? | $e = GV^2/(127R)$; banking of road on curves |
| 2 | Difference between SSD and OSD? | SSD = stopping; OSD = overtaking (includes oncoming) |
| 3 | What is PCU? | Passenger Car Unit; converts mixed traffic to equivalent |
| 4 | What is CBR? How is it used in pavement design? | California Bearing Ratio; strength of subgrade; thickness design |
| 5 | What is Westergaard's method? | Rigid pavement stress: interior, edge, corner conditions |
| 6 | What is Greenshields' model? | $v = v_f(1-k/k_j)$; linear speed-density |
| 7 | What is Webster's signal timing? | $C_o = (1.5L+5)/(1-\sum Y_i)$; optimal cycle length |
| 8 | How is runway length determined? | Based on approach speed, elevation, temperature, gradient |
| 9 | What is the difference between flexible and rigid pavement? | Flexible: layer system; Rigid: slab action |
| 10 | What is cant deficiency? | Difference between equilibrium cant and actual cant on curves |
| 11 | What is the 100% rule in WBS? | Child elements sum to 100% of parent scope |
| 12 | Explain horizontal curve design | Radius, superelevation, extra widening |
| 13 | What is IRC? Key codes? | Indian Roads Congress; IRC:37 (flexible), IRC:58 (rigid) |
| 14 | What is pavement distress? Types? | Rutting, fatigue cracking, bleeding (flexible); corner cracking, faulting (rigid) |
| 15 | What is the difference between traffic volume and capacity? | Volume = actual flow; Capacity = max sustainable flow |

### Key Formulas Summary

| Formula | Use |
|---------|-----|
| $R_{min} = V^2/(127(e+f))$ | Horizontal curve radius |
| $SSD = 0.278Vt + V^2/(254(f \pm G))$ | Stopping sight distance |
| $L = NV^2/46.7$ | Summit curve length |
| $q = kv$ | Fundamental traffic flow |
| $v = v_f(1-k/k_j)$ | Greenshields speed-density |
| $C_o = (1.5L+5)/(1-\sum Y_i)$ | Webster's optimal cycle |
| $e = GV^2/(127R)$ | Superelevation |
| $\sigma_c = (3P/h^2)[1-(a\sqrt{2}/l)^{0.6}]$ | Westergaard corner stress |
| $l = (Eh^3/[12(1-\mu^2)k])^{0.25}$ | Radius of relative stiffness |
| $R = A + BV + CV^2$ | Train resistance (Davis) |

### Numerical Practice Problems

**Problem 1 — Horizontal Curve:**
Design speed 80 km/h, max superelevation 7%, friction 0.15. Find minimum radius.

> **Solution:** $R_{min} = 80^2 / (127(0.07 + 0.15)) = 6400 / (127 × 0.22) = 6400 / 27.94 = 229$ m.

**Problem 2 — SSD:**
Design speed 100 km/h, f = 0.35, grade +2%. Find SSD.

> **Solution:** $SSD = 0.278 \times 100 \times 2.5 + 100^2 / (254 \times (0.35 + 0.02)) = 69.5 + 10000/93.98 = 69.5 + 106.4 = 175.9$ m ≈ 176 m.

**Problem 3 — Signal Timing:**
Total lost time L = 12 s, sum of flow ratios = 0.6. Find optimal cycle.

> **Solution:** $C_o = (1.5 \times 12 + 5)/(1 - 0.6) = 23/0.4 = 57.5$ s. Use C = 60 s.

**Problem 4 — Superelevation:**
Track gauge 1676 mm, speed 100 km/h, radius 500 m. Find equilibrium superelevation.

> **Solution:** $e = 1.676 \times 100^2 / (127 \times 500) = 16760 / 63500 = 0.264$ m = 264 mm. This exceeds max (165 mm), so cant deficiency must be provided.

---

## 8. Key References

| Resource | Use |
|----------|-----|
| IRC:37-2018 | Flexible pavement design |
| IRC:58-2015 | Rigid pavement design |
| IRC:73-1980 | Geometric design (rural roads) |
| IRC:SP:73-2015 | Geometric design (highways) |
| IRC:102-2015 | Highway capacity |
| MoRTH Specifications | Road construction standards |
| Khanna & Justo — *Highway Engineering* | Comprehensive textbook |
| Garber & Hoel — *Traffic & Highway Engineering* | Traffic + pavement |
| Saxena & Arora — *Railway Engineering* | Railway concepts |
| ICARO / DGCA CAR | Airport design standards |
| PTV Vissim / Visum Manual | Software-based analysis |

---

> **Last Updated:** 2026-09-03
> **Maintained by:** DKS IITK Civil/HWRE Placement 2026
> **Version:** 2.0 — Comprehensive Transportation Engineering Guide (replaces software-only v1.0)
