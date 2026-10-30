# Module 07: Pharmacokinetics (PK) & Pharmacodynamics (PD)

> **Track**: Pharmacometrics, Target-Mediated Disposition & Exposure-Response Modeling  
> **Role Level**: Scientist – Modeler (Scientist 1 / Scientist 2 Standard)  
> **Target Entity**: Vantage Research  
> **Evidentiary Standard**: `[PEER-REVIEWED PHARMACOMETRICS & FDA/EMA MIDD STANDARDS]`  

---

## 1. Executive Summary & Core Pharmacological Principles

Pharmacokinetics (PK) describes **what the body does to the drug** (Absorption, Distribution, Metabolism, Excretion — ADME). Pharmacodynamics (PD) describes **what the drug does to the body** (biological effect, biomarker dynamics, receptor occupancy, toxicity).

Coupling PK and PD via mechanistic differential equations is the core bread-and-butter of Vantage Research's commercial projects. This module details:
1. **1-Compartment PK**: IV bolus, 1st-order oral absorption, the Bateman function, analytical derivations of $C_{max}, T_{max}, AUC, CL, V_d$, and the flip-flop phenomenon.
2. **2-Compartment PK**: Micro-rate constants ($k_{10}, k_{12}, k_{21}$), hybrid macro-constants ($\alpha, \beta, A, B$), and biphasic plasma concentration profiles.
3. **Target-Mediated Drug Disposition (TMDD)**: Full system of non-linear ODEs for monoclonal antibodies, rapid binding approximations, and target saturation kinetics.
4. **Multiple Dosing & Steady-State Accumulation**: Superposition principle, accumulation factor $R$, peak-to-trough fluctuations, and loading dose design.
5. **Pharmacodynamics (PD)**: $E_{max}$ and sigmoidal Hill models, inhibitory $I_{max}$ models, and the four classic Dayneka-Jusko Indirect Response models (Types I–IV).
6. **PK/PD Coupling & Hysteresis**: The effect-compartment model ($k_{e0}$) resolving temporal distribution delays between blood and biophase.

---

## 2. One-Compartment Pharmacokinetics

### 2.1 Intravenous (IV) Bolus Administration
In an IV bolus, drug dose $D$ enters the central blood circulation instantaneously at $t = 0$:
$$\frac{dC}{dt} = -k_e C, \quad C(0) = C_0 = \frac{D}{V_d}$$
where:
* $C(t)$ is drug concentration [$\text{mg/L}$ or $\mu\text{g/mL}$].
* $V_d$ is the apparent volume of distribution [$\text{L}$].
* $k_e$ is the first-order elimination rate constant [$\text{h}^{-1}$].

#### Analytical Solution:
$$C(t) = C_0 e^{-k_e t} = \frac{D}{V_d} e^{-\frac{CL}{V_d} t}$$

#### Fundamental PK Relationships:
1. **Clearance ($CL$)**: Volume of plasma completely cleared of drug per unit time:
   $$CL = k_e \cdot V_d \quad [\text{L/h}]$$
2. **Elimination Half-Life ($t_{1/2}$)**: Time required for concentration to decrease by 50%:
   $$C(t_{1/2}) = \frac{C_0}{2} = C_0 e^{-k_e t_{1/2}} \implies t_{1/2} = \frac{\ln 2}{k_e} = \frac{0.693 \cdot V_d}{CL} \quad [\text{h}]$$
3. **Area Under the Curve ($AUC_{0-\infty}$)**: Total systemic drug exposure over all time:
   $$AUC_{0-\infty} = \int_0^\infty C(t) dt = \int_0^\infty \frac{D}{V_d} e^{-k_e t} dt = \frac{D}{V_d} \left[ -\frac{e^{-k_e t}}{k_e} \right]_0^\infty = \frac{D}{V_d k_e} = \mathbf{\frac{D}{CL}}$$
   *Scientist 2 Principle*: Total exposure ($AUC$) depends **strictly on Clearance and Dose**, and is completely **independent of the volume of distribution ($V_d$)**!

---

### 2.2 First-Order Oral Administration (Bateman Function)
For an oral pill, drug amount in the gut $A_{gut}$ is absorbed into the central plasma compartment with absorption rate constant $k_a$ and fractional bioavailability $F \in [0, 1]$:
$$\frac{dA_{gut}}{dt} = -k_a A_{gut}, \quad A_{gut}(0) = F \cdot D$$
$$V_d \frac{dC}{dt} = k_a A_{gut} - CL \cdot C, \quad C(0) = 0$$

#### Analytical Solution (The Bateman Equation):
From equation 1: $A_{gut}(t) = F \cdot D \cdot e^{-k_a t}$. Substitute into equation 2:
$$\frac{dC}{dt} + k_e C = \frac{F \cdot D \cdot k_a}{V_d} e^{-k_a t}$$

Using integrating factor $I(t) = e^{k_e t}$:
$$\frac{d}{dt}\left( C e^{k_e t} \right) = \frac{F \cdot D \cdot k_a}{V_d} e^{(k_e - k_a) t}$$
Integrating with initial condition $C(0) = 0$ (assuming $k_a \ne k_e$):
$$C(t) = \mathbf{\frac{F \cdot D \cdot k_a}{V_d (k_a - k_e)} \left( e^{-k_e t} - e^{-k_a t} \right)}$$

#### Derivation of Peak Time ($T_{max}$) and Peak Concentration ($C_{max}$):
At the peak, $\frac{dC}{dt} = 0$:
$$\frac{dC}{dt} = \frac{F \cdot D \cdot k_a}{V_d (k_a - k_e)} \left( -k_e e^{-k_e T_{max}} + k_a e^{-k_a T_{max}} \right) = 0$$
$$k_e e^{-k_e T_{max}} = k_a e^{-k_a T_{max}} \implies \frac{k_a}{k_e} = \frac{e^{-k_e T_{max}}}{e^{-k_a T_{max}}} = e^{(k_a - k_e) T_{max}}$$

Taking natural logarithms:
$$\ln\left(\frac{k_a}{k_e}\right) = (k_a - k_e) T_{max} \implies \mathbf{T_{max} = \frac{\ln(k_a / k_e)}{k_a - k_e}}$$

Substitute $T_{max}$ back into the Bateman equation to find $C_{max}$:
$$C_{max} = \frac{F \cdot D}{V_d} \left(\frac{k_a}{k_e}\right)^{-\frac{k_e}{k_a - k_e}}$$

#### The Flip-Flop Kinetics Phenomenon:
* **Normal Kinetics ($k_a \gg k_e$)**: Absorption is rapid; the terminal slope of $\ln C(t)$ reflects the elimination rate constant $k_e$.
* **Flip-Flop Kinetics ($k_a \ll k_e$)**: Occurs in sustained-release formulations or subcutaneous depot injections. Absorption is much slower than elimination! The terminal slope reflects **$k_a$**, while the early slope reflects $k_e$! Misinterpreting this causes erroneous clearance calculations.

---

## 3. Two-Compartment Pharmacokinetics

Drugs that distribute slowly into highly perfused vs poorly perfused tissues follow 2-compartment kinetics:
$$\frac{dC_1}{dt} = -\left( \frac{CL}{V_1} + \frac{Q}{V_1} \right) C_1 + \frac{Q}{V_1} C_2 + \frac{\text{Input}(t)}{V_1}$$
$$\frac{dC_2}{dt} = \frac{Q}{V_2} C_1 - \frac{Q}{V_2} C_2$$
where:
* $V_1, V_2$: Central and peripheral distribution volumes [$\text{L}$].
* $CL$: Systemic elimination clearance from central compartment [$\text{L/h}$].
* $Q$: Inter-compartmental distribution clearance [$\text{L/h}$].

### Micro-Constants:
$$k_{10} = \frac{CL}{V_1}, \quad k_{12} = \frac{Q}{V_1}, \quad k_{21} = \frac{Q}{V_2}$$

### Biphasic Analytical Solution (IV Bolus):
$$C_1(t) = A e^{-\alpha t} + B e^{-\beta t}$$
where:
* $\alpha, \beta$: Hybrid rate constants representing rapid distribution ($\alpha$) and terminal elimination ($\beta$).
  $$\alpha + \beta = k_{10} + k_{12} + k_{21}, \quad \alpha \beta = k_{10} k_{21}$$
  $$\alpha, \beta = \frac{(k_{10} + k_{12} + k_{21}) \pm \sqrt{(k_{10} + k_{12} + k_{21})^2 - 4 k_{10} k_{21}}}{2}$$
* Zero-time intercepts: $A = \frac{D(\alpha - k_{21})}{V_1(\alpha - \beta)}, \quad B = \frac{D(k_{21} - \beta)}{V_1(\alpha - \beta)}$, with $C_0 = A + B = \frac{D}{V_1}$.

---

## 4. Target-Mediated Drug Disposition (TMDD)

Therapeutic biologics (e.g., monoclonal antibodies targeting PD-1, HER2, or PCSK9) bind with high affinity to pharmacological targets. When the target receptor concentration is comparable to drug concentration, target binding and subsequent target-drug complex internalization clear a significant fraction of the drug:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          FULL TMDD SYSTEM OF ODEs                           │
├─────────────────────────────────────────────────────────────────────────────┤
│ 1. Free Drug Concentration C:                                               │
│    dC/dt = Input/V1 - (CL/V1)*C - kon*C*R + koff*RC                         │
│                                                                             │
│ 2. Free Target Receptor Density R:                                          │
│    dR/dt = ksyn - kdeg*R - kon*C*R + koff*RC                                │
│                                                                             │
│ 3. Target-Drug Complex RC:                                                  │
│    d(RC)/dt = kon*C*R - koff*RC - kint*RC                                   │
└─────────────────────────────────────────────────────────────────────────────┘
```
where:
* $k_{syn}$: Baseline target receptor zero-order synthesis rate.
* $k_{deg}$: Free target receptor first-order degradation rate ($R_0 = k_{syn} / k_{deg}$).
* $k_{int}$: Target-mediated internalization and degradation of the complex.

### Clinical Impact: Concentration-Dependent Non-Linear Clearance:
* **At Low Drug Doses ($C \ll R$)**: Target binding sites are abundant. Complex internalization dominates elimination $\implies$ Rapid apparent clearance!
* **At High Drug Doses ($C \gg R$)**: Receptors become 100% saturated ($RO \approx 1.0$). TMDD elimination saturates, leaving only non-specific linear clearance ($CL$) $\implies$ Clearance drops, causing disproportionate non-linear jumps in exposure!

---

## 5. Multiple Dosing & Steady-State Accumulation

When a drug is administered repeatedly with dosing interval $\tau$ (e.g., every 24 hours):
At steady state ($t \to \infty$), the concentration profile exactly repeats each cycle.

### The Accumulation Factor ($R$):
For a 1-compartment IV bolus:
$$R = \frac{C_{max, ss}}{C_{max, 1}} = \frac{1}{1 - e^{-k_e \tau}}$$
* **Steady-State Peak**: $C_{max, ss} = \frac{D}{V_d} \left( \frac{1}{1 - e^{-k_e \tau}} \right)$
* **Steady-State Trough**: $C_{min, ss} = C_{max, ss} e^{-k_e \tau} = \frac{D}{V_d} \left( \frac{e^{-k_e \tau}}{1 - e^{-k_e \tau}} \right)$
* **Steady-State Average Concentration**:
  $$C_{avg, ss} = \frac{AUC_\tau}{\tau} = \frac{D}{CL \cdot \tau}$$
* **Loading Dose ($D_L$) Calculation**: To reach steady state immediately on dose 1:
  $$D_L = D \cdot R = \frac{D}{1 - e^{-k_e \tau}} = C_{target} \cdot V_d$$

---

## 6. Pharmacodynamics (PD) & Indirect Response Models

### 6.1 Direct $E_{max}$ Models
When drug concentration in blood is in instantaneous equilibrium with the pharmacological effect:
$$E(C) = \frac{E_{max} \cdot C^\gamma}{EC_{50}^\gamma + C^\gamma}$$
where:
* $E_{max}$: Maximum achievable pharmacological effect.
* $EC_{50}$: Drug concentration producing 50% of $E_{max}$.
* $\gamma$: Hill coefficient (steepness of the dose-response curve).
  * If $\gamma = 1$: Standard hyperbolic Michaelis-Menten profile.
  * If $\gamma > 1$: Sigmoidal switch-like behavior.

### 6.2 Indirect Response Models (Dayneka-Jusko Types I–IV)
Most drugs do not directly produce clinical effects; they stimulate or inhibit the natural synthesis ($k_{in}$) or degradation ($k_{out}$) of an endogenous biomarker or cell population $R$:
$$\frac{dR}{dt} = k_{in} - k_{out} R, \quad \text{Baseline: } R_0 = \frac{k_{in}}{k_{out}}$$

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                 DAYNEKA-JUSKO INDIRECT RESPONSE TAXONOMY                    │
├───────┬───────────────────────────────┬─────────────────────────────────────┤
│ TYPE  │ MECHANISM                     │ GOVERNING DIFFERENTIAL EQUATION     │
├───────┼───────────────────────────────┼─────────────────────────────────────┤
│ I     │ Inhibition of Production kin  │ dR/dt = kin * (1 - I(C)) - kout * R │
│       │ (e.g., NSAIDs, Statins)       │ where I(C) = Imax*C / (IC50 + C)    │
├───────┼───────────────────────────────┼─────────────────────────────────────┤
│ II    │ Inhibition of Dissipation kout│ dR/dt = kin - kout * (1 - I(C)) * R │
│       │ (e.g., ACE inhibitors)        │                                     │
├───────┼───────────────────────────────┼─────────────────────────────────────┤
│ III   │ Stimulation of Production kin │ dR/dt = kin * (1 + S(C)) - kout * R │
│       │ (e.g., Erythropoietin / EPO)  │ where S(C) = Smax*C / (SC50 + C)    │
├───────┼───────────────────────────────┼─────────────────────────────────────┤
│ IV    │ Stimulation of Dissipation    │ dR/dt = kin - kout * (1 + S(C)) * R │
│       │ (e.g., Chemotherapy on WBCs)  │                                     │
└───────┴───────────────────────────────┴─────────────────────────────────────┘
```

---

## 7. Worked Mathematical Problems

### Problem 7.1: Analytical Derivation of $T_{max}$ and $C_{max}$ for Oral Dosing
**Question**: An antibiotic has oral bioavailability $F = 0.80$, absorption rate constant $k_a = 1.5\text{ h}^{-1}$, elimination rate constant $k_e = 0.15\text{ h}^{-1}$, and volume of distribution $V_d = 20.0\text{ L}$.
For an oral dose of $D = 500\text{ mg}$:
1. Compute the time of peak concentration $T_{max}$.
2. Compute the maximum plasma concentration $C_{max}$.
3. Calculate the total exposure $AUC_{0-\infty}$.

#### Solution:
**Step 1: Peak Time $T_{max}$**
$$T_{max} = \frac{\ln(k_a / k_e)}{k_a - k_e} = \frac{\ln(1.5 / 0.15)}{1.5 - 0.15} = \frac{\ln(10.0)}{1.35} = \frac{2.3026}{1.35} = \mathbf{1.7056\text{ hours}}$$

**Step 2: Peak Concentration $C_{max}$**
Substitute $T_{max} = 1.7056\text{ h}$ into the Bateman equation:
$$C(t) = \frac{F \cdot D \cdot k_a}{V_d (k_a - k_e)} \left( e^{-k_e t} - e^{-k_a t} \right)$$
$$\text{Pre-factor} = \frac{0.80 \times 500 \times 1.5}{20.0 \times (1.5 - 0.15)} = \frac{600.0}{20.0 \times 1.35} = \frac{600.0}{27.0} = 22.222\text{ mg/L}$$

Evaluate exponentials at $t = 1.7056\text{ h}$:
$$e^{-k_e T_{max}} = e^{-0.15 \times 1.7056} = e^{-0.25584} = 0.77427$$
$$e^{-k_a T_{max}} = e^{-1.5 \times 1.7056} = e^{-2.5584} = 0.07743$$

$$C_{max} = 22.222 \times (0.77427 - 0.07743) = 22.222 \times 0.69684 = \mathbf{15.485\text{ mg/L}}$$

**Step 3: Total Systemic Exposure $AUC_{0-\infty}$**
$$CL = k_e \cdot V_d = 0.15\text{ h}^{-1} \times 20.0\text{ L} = 3.0\text{ L/h}$$
$$AUC_{0-\infty} = \frac{F \cdot D}{CL} = \frac{0.80 \times 500\text{ mg}}{3.0\text{ L/h}} = \frac{400.0}{3.0} = \mathbf{133.33\text{ mg}\cdot\text{h/L}}$$

---

### Problem 7.2: Loading Dose & Accumulation in Multiple Dosing
**Question**: An intensive care patient requires an anticoagulant with target trough concentration $C_{target} \ge 2.0\text{ mg/L}$ and peak concentration below toxic threshold $C_{tox} \le 10.0\text{ mg/L}$.
Parameters: $V_d = 15.0\text{ L}$, clearance $CL = 1.5\text{ L/h}$, dosing interval $\tau = 12\text{ hours}$.
1. Compute the elimination rate $k_e$ and half-life $t_{1/2}$.
2. Determine the steady-state accumulation factor $R$.
3. Calculate the required maintenance IV bolus dose $D$ to ensure trough concentration $C_{min, ss} = 2.0\text{ mg/L}$.
4. Check if peak concentration exceeds $C_{tox}$.
5. Calculate the initial loading dose $D_L$.

#### Solution:
**Step 1: Basic Parameters**
$$k_e = \frac{CL}{V_d} = \frac{1.5}{15.0} = 0.10\text{ h}^{-1}$$
$$t_{1/2} = \frac{\ln 2}{0.10} = \mathbf{6.93\text{ hours}}$$

**Step 2: Accumulation Factor $R$**
$$R = \frac{1}{1 - e^{-k_e \tau}} = \frac{1}{1 - e^{-0.10 \times 12}} = \frac{1}{1 - e^{-1.2}} = \frac{1}{1 - 0.30119} = \frac{1}{0.69881} = \mathbf{1.4310}$$

**Step 3: Maintenance Dose $D$**
At steady-state trough:
$$C_{min, ss} = \frac{D}{V_d} \left( \frac{e^{-k_e \tau}}{1 - e^{-k_e \tau}} \right) = \frac{D}{15.0} \left( \frac{0.30119}{0.69881} \right) = \frac{D}{15.0} \times 0.43101 = 0.028734 D$$
Setting $C_{min, ss} = 2.0\text{ mg/L}$:
$$D = \frac{2.0}{0.028734} = \mathbf{69.60\text{ mg}} \approx \mathbf{70.0\text{ mg}}$$

**Step 4: Peak Concentration Check**
$$C_{max, ss} = \frac{D}{V_d} \cdot R = \frac{69.60}{15.0} \times 1.4310 = 4.640 \times 1.4310 = \mathbf{6.64\text{ mg/L}}$$
Since $C_{max, ss} = 6.64\text{ mg/L} < 10.0\text{ mg/L}$, the regimen is therapeutically safe and non-toxic.

**Step 5: Initial Loading Dose $D_L$**
$$D_L = D \cdot R = 69.60 \times 1.4310 = \mathbf{99.6\text{ mg}} \approx \mathbf{100.0\text{ mg}}$$
Administering $100\text{ mg}$ at $t = 0$ immediately establishes the target steady-state peak ($C_0 = 100/15 = 6.67\text{ mg/L}$) without waiting 4–5 half-lives for gradual drug accumulation!
