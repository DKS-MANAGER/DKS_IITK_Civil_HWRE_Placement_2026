# Electric Vehicle (EV) Architecture & Vehicle Systems
**Target Role:** Graduate Engineer Trainee (GET) — Product Engineering & Advanced Manufacturing  
**Company:** Ola Electric Mobility Limited  
**Standard:** Two-Wheeler Vehicle Dynamics, Powertrain Packaging & NVH  

---

## 1. EV Scooter & Motorcycle Platform Architectures

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                        OLA ELECTRIC PLATFORM EVOLUTION ARCHITECTURE                    │
├─────────────────────┬──────────────────────────┬───────────────────────────────────────┤
│ Architecture        │ S1 Pro (Gen 2 Platform)  │ Roadster Series (Gen 3 Motorcycle)    │
├─────────────────────┼──────────────────────────┼───────────────────────────────────────┤
│ Frame Architecture  │ Single-piece tubular HSS │ Double-cradle steel tubular frame     │
│                     │ spine with floor battery │ with structural battery integration   │
├─────────────────────┼──────────────────────────┼───────────────────────────────────────┤
│ Powertrain Layout   │ Mid-drive IPMSM motor    │ Mid-drive liquid-cooled PMSM motor    │
│                     │ with planetary reduction │ with final chain drive                │
├─────────────────────┼──────────────────────────┼───────────────────────────────────────┤
│ Front Suspension    │ Dual telescopic forks    │ Upside-down (USD) telescopic forks    │
├─────────────────────┼──────────────────────────┼───────────────────────────────────────┤
│ Rear Suspension     │ Die-cast hybrid swingarm │ Dual-sided extruded/cast swingarm with│
│                     │ with offset monoshock    │ link-type mono-shock absorber         │
├─────────────────────┼──────────────────────────┼───────────────────────────────────────┤
│ Battery Packaging   │ 4 kWh under floorboard   │ 2.5 – 16 kWh structural monocoque     │
│                     │ (IP67 aluminum pack)     │ casing using 4680 Bharat Cells        │
└─────────────────────┴──────────────────────────┴───────────────────────────────────────┘
```

---

## 2. Chassis Geometry & Vehicle Dynamics Fundamentals

Vehicle handling, high-speed stability, and low-speed agility are governed by front-end steering geometry:

```
                  STEERING HEAD GEOMETRY & TRAIL
                  
                   \ Steering Axis
                    \ 
                     \ 
                      \  Rake Angle (θ)
                       \
                        \
                         \ 
    ──────────────────────\───────────────── Ground Level
                          │\
             Ground Contact│ \ Pivot Ground Intercept
                           │  \
                           └───┘
                           TRAIL
```

1. **Rake Angle (Caster Angle, $\theta$):**  
   The acute angle between the steering axis (steering head tube) and the vertical ground normal.  
   - Typical scooter rake: $24^\circ - 26^\circ$.  
   - Higher rake ($> 28^\circ$): Increases high-speed straight-line stability, but causes sluggish low-speed turning.
2. **Trail ($T$):**  
   The horizontal distance on the ground between the forward steering axis ground intercept and the center of the front tire contact patch:
   $$T = \frac{R_w \sin \theta - O_{\text{fork}}}{\cos \theta}$$
   where $R_w$ is front tire radius, $\theta$ is rake angle, and $O_{\text{fork}}$ is triple-clamp fork offset.
   - **Castor Effect:** Trail acts like a shopping-cart castor wheel, generating a restoring steering moment ($M_{\text{restoring}} = F_{\text{lateral}} \times T$) that pulls the front wheel straight when disturbed by wind or potholes.
   - S1 Pro Gen 2 trail is tuned to **$\approx 85 - 95\text{ mm}$**, balancing flickable city traffic maneuvering with stable $120\text{ km/h}$ highway cruising.

---

## 3. Front Suspension Engineering: Single-Fork vs Dual-Telescopic

The technical evolution of Ola’s front suspension represents a textbook automotive case study in **stress concentration and fatigue elimination**:

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                        FRONT SUSPENSION COMPARATIVE ANALYSIS                           │
├───────────────────────────────┬────────────────────────────────────────────────────────┤
│ Gen 1: Single-Sided Fork      │ Gen 2: Conventional Dual Telescopic Forks              │
├───────────────────────────────┼────────────────────────────────────────────────────────┤
│ • Asymmetric cantilevered load│ • Symmetric dual load paths                            │
│ • Massive bending moments at  │ • Bending moment partitioned 50:50 between two stanchion│
│   the single steer-tube neck  │   tubes under hard braking ($1.0g$)                    │
│ • High stress concentration Kt│ • Low stress concentration; widely understood tolerances│
│ • Prone to fatigue shear failure│• Superior lateral stiffness; high bump compliance    │
│ • Higher casting complexity   │ • Cost-effective; proven automotive tier-1 supply base│
└───────────────────────────────┴────────────────────────────────────────────────────────┘
```

---

## 4. Powertrain Packaging: Mid-Drive IPMSM vs Hub Motor

Electric two-wheelers deploy two contrasting motor layouts:

### 4.1 Interior Permanent Magnet Synchronous Motor (IPMSM — Mid-Drive)
*Used on Ola S1 Pro Gen 2 and Roadster:*
- Motor is mounted securely to the sprung chassis frame, protected from road shocks.
- Features high peak power density ($11\text{ kW}$ peak, $120\text{ km/h}$).
- Torque is multiplied through a compact **planetary reduction gearbox (ratio $\approx 6:1 - 7:1$)** before driving the rear wheel via a carbon-reinforced toothed belt or chain.
- **Dynamic Advantage:** Low unsprung mass $\implies$ rear suspension reacts instantaneously to bumps, delivering superior ride comfort and road grip.

### 4.2 Direct-Drive Hub Motor
*Used on Ola S1 Air and S1 X:*
- Motor is built directly inside the rear wheel rim, eliminating the gearbox, drive belt, and swingarm pivot tensioners.
- Reduces bill-of-materials (BOM) cost and eliminates belt maintenance.
- **Dynamic Drawback:** High unsprung mass ($+8 - 12\text{ kg}$ on the rear wheel) increases impact harshness over sharp road bumps and subjects motor electronics to severe mechanical vibration ($> 15g$).

---

## 5. Noise, Vibration and Harshness (NVH) Engineering

Because electric vehicles lack an internal combustion engine to mask background sounds, mechanical and electro-acoustic noises become acutely noticeable to customers:
1. **Electromagnetic Motor Whine & Cogging Torque:**  
   Caused by the harmonic magnetic attraction between rotor permanent magnets and stator iron teeth as the rotor spins.  
   - *Mitigation:* Skewing the stator slots or rotor magnets by one slot pitch; implementing Space Vector Pulse Width Modulation (SVPWM) with Field-Oriented Control (FOC) to inject pure sinusoidal currents, eliminating 5th and 7th harmonic radial forces.
2. **Planetary Gearbox Whine:**  
   Meshing gear teeth generate acoustic excitation at the Tooth Passing Frequency ($TPF = \text{RPM} \times Z / 60$).  
   - *Mitigation:* Shifting from straight spur gears to helical gears with high contact ratio ($\varepsilon_\alpha > 2.0$), micro-crowning tooth profiles, and structural ribbing on the aluminum die-cast casing to attenuate acoustic radiation.
3. **Chassis Resonance Isolation:**  
   Ensuring the first structural bending and torsional natural frequencies of the frame ($> 28\text{ Hz}$) remain decoupled from motor operational frequencies across the $0 - 6000\text{ RPM}$ band.

---

## 6. Vehicle Durability & Accelerated Endurance Testing

Before series production release, prototype vehicles undergo brutal physical endurance testing:
1. **Four-Poster Hydraulic Shaker Rig Testing:**  
   Actuators reproduce digitized road profile telemetry recorded from rough Indian rural roads, cycling the frame and battery mounts through $2.5g - 3.5g$ vertical shock pulses for 500 hours (simulating $100,000\text{ km}$ of customer life).
2. **Pave & Belgian Cobblestone Track Testing:**  
   High-frequency impact testing evaluating fastener torque retention, weld toe crack inception, and plastic latch integrity.
3. **Environmental Testing:**  
   - Mud slurry spray testing.
   - Water wading: Riding through a $300\text{ mm}$ deep water trough at $20\text{ km/h}$ to verify IP67 seal integrity.
   - Extreme thermal soak (cycling between $-10^\circ\text{C}$ and $+55^\circ\text{C}$ in an environmental climatic chamber).

---
*End of EV Architecture & Vehicle Systems.*
