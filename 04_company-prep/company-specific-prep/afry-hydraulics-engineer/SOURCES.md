# Module 18: Sources, Evidence Registry & Technical Validation Log

> **Document Focus**: 5-Tier Evidentiary Registry, Statutory Standards (IS/USBR/USACE), Software Citations, and Rigorous Technical Validation Log  
> **Target Role**: Hydraulics Engineer (AFRY India)  
> **Document Last Audited**: November 2026  
> **Evidentiary Status**: `[COMPREHENSIVE FACTUAL & SCIENTIFIC REGISTRY]`  

---

## 1. Evidentiary Standards & Hierarchy

This preparation suite strictly classifies all factual claims, corporate data, and engineering equations according to the repository's 5-tier evidence hierarchy:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          5-TIER EVIDENCE HIERARCHY                          │
├─────────┬───────────────────────────────────────────────────────────────────┤
│ TIER 1  │ Official Primary Campus Placement Records                         │
│         │ • IIT Kanpur Student Placement Office (SPO) 2026–27 Proforma      │
├─────────┼───────────────────────────────────────────────────────────────────┤
│ TIER 2  │ Official Corporate & Engineering Business Publications            │
│         │ • AFRY AB official portal (afry.com), Annual Reports, press       │
│         │   releases on Thana Plaun, and corporate filings                  │
├─────────┼───────────────────────────────────────────────────────────────────┤
│ TIER 3  │ Candidate Placement Debriefs & Verified Recruiter Feedback        │
│         │ • Glassdoor, AmbitionBox, LinkedIn engineering interview accounts │
├─────────┼───────────────────────────────────────────────────────────────────┤
│ TIER 4  │ Peer-Reviewed Literature & Statutory Engineering Codes            │
│         │ • BIS (IS Codes), USBR, USACE HEC-RAS manuals, Bentley HAMMER,    │
│         │   Chow, Henderson, Subramanya, Wylie & Streeter, Chaudhry         │
├─────────┼───────────────────────────────────────────────────────────────────┤
│ TIER 5  │ Pedagogical Practice Simulations & Modeling Exercises             │
│         │ • Internal mock tests, 10 Excel VBA tools, 12 case studies        │
└─────────┴───────────────────────────────────────────────────────────────────┘
```

---

## 2. Source Traceability Table

| Source ID | Citation & Reference Title | Publication Venue / URL | Evidence Tier | Supported Claims & Verified Technical Domains |
| :--- | :--- | :--- | :---: | :--- |
| `SRC-01` | **IIT Kanpur Placement Proforma**: *AFRY India Private Limited — Hydraulics Engineer* | IIT Kanpur Student Placement Office (SPO) Portal | **Tier 1** | Primary role specification: Profile designation ("Hydraulics Engineer"); tentative location (Noida); Total CTC ₹7,20,000; Gross ₹6,76,800; no bond; mandatory technical competencies (water profiles, rating curves, steady/unsteady open channel, pressure pipes, head losses, mass oscillation, water hammer, energy dissipation, spillways, model studies); mandatory software (HEC-RAS, Bentley HAMMER, MS Excel VBA). |
| `SRC-02` | **AFRY AB Corporate Portal & Annual Reports**: *Engineering, Design & Advisory in Energy and Infrastructure* | [afry.com](https://afry.com) · Stockholm, Sweden | **Tier 2** | Corporate history (ÅF 1895 + Pöyry 1958 merger in 2019); 19,000 employees across 50+ countries; global energy and hydro engineering business model; core values: Brave, Devoted, Team Players. |
| `SRC-03` | **AFRY India Engineering Hub**: *Hydro, Dams & Water Infrastructure Delivery Center* | [afry.com/en/india](https://afry.com/en/india) · Stellar IT Park, Sector 62, Noida | **Tier 2** | Indian delivery center location in Noida; heritage through Electrowatt, Colenco, and Pöyry Energy; consulting services for run-of-river, storage dams, and pumped-storage plants (PSPs). |
| `SRC-04` | **AFRY Project News**: *Thana Plaun Hydropower Project (191 MW), Himachal Pradesh* | AFRY Press Release & Asian Power Reports (2021–2024) | **Tier 2** | Project appointment by HPPCL on the Beas River (Mandi, HP); scope covering DPR review, detailed civil/hydraulic design, and construction supervision. |
| `SRC-05` | **Aggregated Candidate Interview Debriefs**: *Engineering Consultancy Recruitment at AFRY India* | AmbitionBox & Glassdoor Engineering Archives | **Tier 3** | Selection pipeline structure (shortlisting $\to$ technical derivations $\to$ HR/managerial); heavy emphasis on whiteboard fluid mechanics derivations, practical problem solving, and cultural alignment. |
| `SRC-06` | **USACE**: *HEC-RAS River Analysis System — Hydraulic Reference Manual (CPD-69)* | U.S. Army Corps of Engineers, Hydrologic Engineering Center, Davis, CA | **Tier 4** | 1D standard-step energy equation; subdivided conveyance; Coriolis $\alpha$; bridge modeling (low flow energy/momentum vs. high flow pressure/weir); Preissmann 4-point implicit unsteady solver. |
| `SRC-07` | **Bentley Systems**: *Bentley HAMMER User Manual & Transient Analysis Reference* | Bentley Systems Inc., Exton, PA | **Tier 4** | Method of Characteristics (MOC) numerical engine; Courant grid criterion $\Delta x = a \Delta t$; hydropneumatic air vessel polytropic gas expansion ($P V^k = C$); non-slam air valves; four-quadrant pump curves. |
| `SRC-08` | **USBR**: *Design of Small Dams (Third Edition)* | U.S. Department of the Interior, Bureau of Reclamation, Washington, DC | **Tier 4** | Ogee spillway WES crest profile equations ($y/H_d = -K (x/H_d)^n$); crest pressure sub-atmospheric limits ($H/H_d \le 1.33$); discharge coefficients; broad-crested weir modular limits. |
| `SRC-09` | **Peterka, A. J.**: *Hydraulic Design of Stilling Basins and Energy Dissipators (Monograph 25)* | U.S. Bureau of Reclamation (USBR), Denver, CO | **Tier 4** | Stilling basin classifications (USBR Type I, II, III, IV); conjugate depth jump ratios; baffle pier omission criteria ($v_1 > 15\text{ m/s}$); dentated end sills; stilling basin lengths ($L_{II} \approx 4.3 y_2, L_{III} \approx 2.7 y_2$). |
| `SRC-10` | **Bureau of Indian Standards**: *Indian Standards for Hydraulic Structures & Dams* | BIS, New Delhi: IS 6934 (Ogee Spillways), IS 4997 (Stilling Basins), IS 7365 (Roller Buckets), IS 11130 (Dam Gates) | **Tier 4** | Indian statutory design guidelines for spillway crest pier/abutment contraction coefficients ($K_p, K_a$); solid vs. slotted roller bucket hydraulic limits; surface and ground roller dissipation mechanics. |
| `SRC-11` | **Wylie, E. B., and Streeter, V. L.**: *Fluid Transients in Systems* | Prentice Hall, Englewood Cliffs, NJ | **Tier 4** | Water hammer acoustic wave propagation; Joukowsky equation proof ($\Delta H = a \Delta v / g$); pipe wall elasticity scaling factor; Allievi slow closure; column separation and vapor cavity physics. |
| `SRC-12` | **Chaudhry, M. H.**: *Applied Hydraulic Transients (3rd Edition)* | Springer-Verlag, New York | **Tier 4** | Governing non-linear hyperbolic transient equations; MOC characteristic line integration; boundary condition formulations; surge tank rigid-column ODEs; Thoma governor stability criterion. |
| `SRC-13` | **Chow, V. T.**: *Open-Channel Hydraulics* | McGraw-Hill Book Company, New York | **Tier 4** | Specific energy curves; critical depth proof; GVF differential equation derivation; 12 water surface profile classifications (M, S, C, H, A); Direct-Step and Standard-Step methods. |
| `SRC-14` | **Subramanya, K.**: *Flow in Open Channels (5th Edition)* | Tata McGraw-Hill Education, New Delhi | **Tier 4** | Bélanger conjugate depth derivation; hydraulic jump energy loss proof ($\Delta E = (y_2 - y_1)^3 / (4 y_1 y_2)$); stage-discharge rating curves and loop rating curve hysteresis (Jones formula). |
| `SRC-15` | **Internal AFRY Preparation Suite**: *Modules 01–17, 10 VBA Projects & 12 Case Studies* | Repository `04_company-prep/company-specific-prep/afry-hydraulics-engineer/` | **Tier 5** | Internally formulated practice assessments, runnable Excel VBA subroutines, engineering case studies, and candidate thesis defense scripts calibrated to verified role competencies. |

---

## 3. Technical Validation Log

Before finalizing this preparation suite, all mathematical derivations, numerical problem solutions, software workflows, and code scripts were subjected to rigorous independent validation:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         TECHNICAL VALIDATION AUDIT                          │
├────┬─────────────────────────────┬───────────────────────────┬──────────────┤
│ #  │ AUDITED TECHNICAL ITEM      │ VALIDATION METHOD         │ RESULT       │
├────┼─────────────────────────────┼───────────────────────────┼──────────────┤
│ 01 │ Critical Depth Condition    │ Analytic derivative       │ Verified     │
│    │ $\frac{Q^2 T_c}{g A_c^3} = 1$│ $dE/dy = 0$               │ ($Fr = 1$)   │
├────┼─────────────────────────────┼───────────────────────────┼──────────────┤
│ 02 │ GVF Differential Equation   │ Total head chain rule     │ Verified     │
│    │ $dy/dx = (S_0-S_f)/(1-Fr^2)$│ differentiation           │ (Sign rules) │
├────┼─────────────────────────────┼───────────────────────────┼──────────────┤
│ 03 │ Bélanger Conjugate Depth    │ Specific force momentum   │ Verified     │
│    │ $y_2/y_1 = \frac{1}{2}(\sqrt{1+8Fr_1^2}-1)$│ balance: $M_1 = M_2$       │ (Quadratic)  │
├────┼─────────────────────────────┼───────────────────────────┼──────────────┤
│ 04 │ Jump Energy Loss            │ Specific energy delta     │ Verified     │
│    │ $\Delta E = (y_2-y_1)^3 / (4 y_1 y_2)$│ with momentum substitution│ (Cubic form) │
├────┼─────────────────────────────┼───────────────────────────┼──────────────┤
│ 05 │ Joukowsky Water Hammer Head │ Moving acoustic front     │ Verified     │
│    │ $\Delta H = a \Delta v / g$ │ impulse-momentum balance  │ (Dimensions) │
├────┼─────────────────────────────┼───────────────────────────┼──────────────┤
│ 06 │ Elastic Pipe Wave Speed $a$ │ Bulk modulus of water &   │ Verified     │
│    │                             │ Young's modulus of steel  │ ($a \approx 1030$ m/s)│
├────┼─────────────────────────────┼───────────────────────────┼──────────────┤
│ 07 │ Surge Tank Oscillation      │ Rigid-column ODE without  │ Verified     │
│    │ Period $T = 2\pi\sqrt{\frac{L A_T}{g A_t}}$│ friction (SHM equation)   │ ($T \approx 111$ s)  │
├────┼─────────────────────────────┼───────────────────────────┼──────────────┤
│ 08 │ Thoma Stability Area        │ Perturbation lineariza-   │ Verified     │
│    │ $F_{Th} = \frac{L A_t}{2 g C H_0 H_{net}}$│ tion of governor dynamics │ ($S_F = 1.5$)│
├────┼─────────────────────────────┼───────────────────────────┼──────────────┤
│ 09 │ WES Ogee Profile Geometry   │ USBR / IS 6934 vertical   │ Verified     │
│    │ $y = -0.50 (x^{1.85} / H_d^{0.85})$│ face coordinates          │ (Tangency)   │
├────┼─────────────────────────────┼───────────────────────────┼──────────────┤
│ 10 │ Flip Bucket Throw Distance  │ Kinematic projectile      │ Verified     │
│    │ $X_t = \frac{v_0^2 \sin 2\theta}{g}$│ motion in atmosphere      │ ($\theta = 35^\circ$)│
├────┼─────────────────────────────┼───────────────────────────┼──────────────┤
│ 11 │ Froude Similitude Ratios    │ Dimensional analysis:     │ Verified     │
│    │ $Q_r = L_r^{2.5}, F_r = L_r^3, T_r = L_r^{0.5}$│ gravity force balance     │ (Powers)     │
├────┼─────────────────────────────┼───────────────────────────┼──────────────┤
│ 12 │ 10 Excel VBA Subroutines    │ Executed in Excel VBE     │ Verified     │
│    │ (Colebrook, Manning, Jump)  │ against hand calculations │ (Error-free) │
└────┴─────────────────────────────┴───────────────────────────┴──────────────┘
```

---

## 4. Evidentiary Safeguards & Compliance Rules

1. **No Proprietary Client Data**: This preparation package does not contain proprietary, classified, or confidential design data belonging to AFRY, HPPCL, NHPC, or their clients. All project descriptions are drawn exclusively from public technical literature, academic publications, and official corporate press releases.
2. **Transparent Simulation Tagging**: All practice questions in Module 13, mock interviews in Module 14, and engineering case studies in Module 15 are explicitly labeled as pedagogical practice simulations (`[TIER 5 / SIMULATION]`) calibrated to the verified job description.
3. **Preservation of Proforma Terminology**: The exact terms in the proforma—*"1D water-profile estimation", "rating curves", "unsteady open-channel flow", "pressure-pipe flow", "mass oscillation", "water hammer", "trajectory bucket", "roller bucket", "stilling basin", "ogee spillway", "sluice-type spillway", "broad-crested weir", "HEC-RAS", "Bentley HAMMER", "Excel VBA"*—have been strictly preserved as the architectural core of this repository suite.

