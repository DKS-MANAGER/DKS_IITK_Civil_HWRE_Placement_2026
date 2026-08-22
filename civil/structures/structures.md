# Structures

## Scope

Structural engineering for civil placements covers the analysis and design of load-carrying systems. Breadth knowledge in strength of materials, reinforced concrete, steel structures, and structural analysis is expected for core design roles.

## Strength of Materials (Solid Mechanics)

### Stress & Strain
- Normal stress, shear stress, and stress transformation
- Strain: Normal strain, shear strain, and thermal strain
- Hooke's law: σ = Eε (uniaxial), τ = Gγ (shear)

### Bending of Beams
- Flexure formula: M = f × Z (f = stress, Z = section modulus)
- Shear stress distribution: τ = VQ/Ib
- Deflection: Double integration method, moment-area method, conjugate beam method
- Slope-deflection equations for indeterminate beams

### Shear & Torsion
- Shear center for open and closed sections
- Torsion of circular sections: T/J = τ/r = Gθ/L
- Warping torsion for non-circular open sections

### Energy Methods
- Strain energy in axial, bending, shear, and torsional loading
- Castigliano's theorems: First theorem for displacement, second theorem for redundant reactions
- Unit load method for deflection calculation

### Columns & Buckling
- Euler's critical load: Pcr = π²EI / (KL)²
- Effective length factor K for different end conditions
- Rankine-Gordon formula for combined crushing and buckling
- Slenderness ratio and column classification

## Structural Analysis

### Methods
- **Force method (Flexibility):** Compatibility of displacements for statically indeterminate structures
- **Displacement method (Stiffness):** Equilibrium of forces using member stiffness matrices
- **Moment distribution (Hardy Cross):** Iterative method for beams and frames
- **Matrix methods:** Stiffness matrix formulation for frames and trusses

### Influence Lines
- Müller-Breslau principle for qualitative influence lines
- Influence lines for beams, trusses, and arches
- Applications: Maximum shear, maximum moment, and absolute maximum moment

## Reinforced Cement Concrete (RCC)

### IS 456: 2000 Provisions
- Limit state method: Limit state of collapse (strength) and limit state of serviceability (deflection, cracking)
- Grades of concrete (M20, M25, M30, etc.) and steel (Fe415, Fe500, Fe550)
- Modular ratio: m = Es/Ec ≈ 280/σcbc (for working stress method)

### Beam Design
- Singly reinforced: Balanced, under-reinforced, over-reinforced sections
- Doubly reinforced: Additional steel in compression zone
- Shear reinforcement: Stirrups and bent-up bars; design shear stress τc and τv
- Torsional reinforcement: Additional longitudinal and transverse steel

### Slabs
- One-way vs. two-way slabs
- Span-to-depth ratio and deflection check
- Minimum and maximum steel requirements

### Columns
- Short column versus long column behavior
- Eccentric loading and uniaxial/biaxial bending
- Spiral and tied columns

### Footings
- Isolated, combined, strap, and mat foundations
- Soil pressure distribution and moment transfer

## Steel Structures

### IS 800: 2007 Provisions
- Limit state method for steel structures
- Grades: E250, E350, E410, E450, E550
- Types of steel: Mild steel and high-strength deformed (HSD) bars

### Connections
- Riveted, bolted, and welded connections
- Bolt types: Black bolt, turned bolt, high-strength bolt (friction type and bearing type)
- Weld types: Butt weld, fillet weld, plug weld, slot weld

### Tension Members
- Net area and effective net area
- Design strength: Tdn = 0.9 × An × fu / γm

### Compression Members
- Slenderness ratio and buckling class
- Design strength: Pd = (Aeff × fcd) / γm₀
- Lacings and battening for built-up columns

### Beams
- Plate girders and built-up sections
- Shear lag and effective width
- Lateral torsional buckling

## Structural Software

| Tool | Application |
|------|-------------|
| SAP2000 | General-purpose structural analysis and design |
| ETABS | Building analysis and design |
| STAAD.Pro | Structural analysis and design |
| Tekla Structures | Steel and concrete detailing |
| midas Civil | Bridge and civil structural analysis |
| RISA-3D | 3D structural analysis for buildings and bridges |
| Dlubal RFEM | 3D finite element structural analysis |
| OpenSees | Open-source nonlinear structural and geotechnical simulation |

## Design Codes & Standards
- IS 456: Plain and reinforced concrete
- IS 800: General construction in steel
- IS 1893: Earthquake resistant design
- IS 3370: Concrete structures for storage of liquids
- IS 456:2000 and SP 16: Design aids for RCC

## Further expansion needed
- Prestressed concrete fundamentals
- Advanced analysis of indeterminate structures
- Structural dynamics and seismic design
- Wind load computation and tall building behavior

## References

* [Civil_Placement_IITK](https://github.com/DKS-MANAGER/Civil_Placement_IITK)
* [awesome-civil-engineering](https://github.com/awesome-civil-engineering/awesome-civil-engineering)