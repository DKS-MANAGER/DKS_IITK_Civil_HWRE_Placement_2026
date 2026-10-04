# 01 — Fluid Properties & Hydrostatics

> **Discipline**: Fundamental Fluid Mechanics  
> **Key Exam / Interview Topics**: Newton's law of viscosity, Bulk modulus, Surface tension, Pressure intensity, Hydrostatic forces on planar and curved surfaces, Center of pressure, Buoyancy & Metacentric height.

---

## 1. Core Fluid Properties

### 1. Newton's Law of Viscosity
$$\tau = \mu \frac{du}{dy}$$
Where $\tau$ is shear stress ($\text{N/m}^2$), $\mu$ is dynamic viscosity ($\text{Pa}\cdot\text{s}$ or $\text{Poise}$, $1\text{ Pa}\cdot\text{s} = 10\text{ Poise}$), and $\frac{du}{dy}$ is velocity gradient or rate of shear strain.
* **Kinematic Viscosity ($\nu$)**: $\nu = \frac{\mu}{\rho}$ ($\text{m}^2/\text{s}$ or $\text{Stokes}$, $1\text{ Stoke} = 10^{-4}\text{ m}^2/\text{s}$).
* **Temperature Effect**: Viscosity of liquids **decreases** with increasing temperature (cohesive forces dominate); viscosity of gases **increases** with temperature (molecular momentum transfer dominates).

### 2. Compressibility & Bulk Modulus ($K$)
$$K = -\frac{dp}{dV/V} = \rho \frac{dp}{d\rho}$$
* Speed of sound in a fluid medium: $c = \sqrt{\frac{K}{\rho}}$. For water, $K \approx 2.2\text{ GPa}$, $c \approx 1,480\text{ m/s}$.

### 3. Surface Tension ($\sigma$) & Capillarity ($h$)
* Pressure difference inside a spherical droplet: $\Delta P = \frac{4\sigma}{d}$.
* Pressure difference inside a soap bubble: $\Delta P = \frac{8\sigma}{d}$.
* Capillary rise/depression in a tube of diameter $d$:
  $$h = \frac{4\sigma \cos \theta}{\rho g d}$$
  Where $\theta = 0^\circ$ for clean water on glass, and $\theta \approx 130^\circ$ for mercury on glass (capillary depression).

---

## 2. Hydrostatic Forces on Submerged Surfaces

### 1. Total Force on Plane Submerged Surface
$$F = \rho g \bar{h} A$$
Where $\bar{h}$ is the vertical depth of the centroid of area $A$ below the free surface.

### 2. Center of Pressure ($h^*$)
The point of application of the resultant hydrostatic force always lies **below** the centroid:
$$h^* = \bar{h} + \frac{I_{G} \sin^2 \theta}{A \bar{h}}$$
Where $I_G$ is the second moment of area about the horizontal centroidal axis, and $\theta$ is the angle of inclination of the plane with the horizontal.
* For vertical plane ($\theta = 90^\circ$): $h^* = \bar{h} + \frac{I_G}{A \bar{h}}$.
* For horizontal plane ($\theta = 0^\circ$): $h^* = \bar{h}$.

### 3. Hydrostatic Force on Curved Surfaces
* Horizontal Component ($F_H$): Total hydrostatic force on the **vertical projection** of the curved surface: $F_H = \rho g \bar{h}_{proj} A_{proj}$, acting at the center of pressure of the projected area.
* Vertical Component ($F_V$): Weight of the liquid column vertically above the curved surface extending up to the free surface: $F_V = \rho g V_{column}$.
* Resultant Force: $F_R = \sqrt{F_H^2 + F_V^2}$, acting at angle $\alpha = \tan^{-1}\left(\frac{F_V}{F_H}\right)$.

---

## 3. Buoyancy, Floatation & Stability

### 1. Archimedes' Principle
$$\text{Buoyant Force } F_B = \text{Weight of displaced liquid} = \rho_f g V_{submerged}$$
Acts through the **Center of Buoyancy ($B$)**, which is the centroid of the displaced liquid volume.

### 2. Metacentric Height ($GM$) for Floating Bodies
The Metacenter ($M$) is the point of intersection of the line of action of the buoyant force when the body is tilted through a small angle with the normal vertical axis of the body.
$$GM = BM - BG$$
$$BM = \frac{I_{min}}{V_{displaced}}$$
Where $I_{min}$ is the second moment of area of the water-plane section about the longitudinal tilt axis, and $BG$ is the distance between Center of Gravity ($G$) and Center of Buoyancy ($B$).

| Condition | Position of $M$ relative to $G$ | Metacentric Height ($GM$) | Stability State |
| :--- | :--- | :--- | :--- |
| **Stable Equilibrium** | $M$ is **above** $G$ | $GM > 0$ | Restoring couple acts to right the body. |
| **Neutral Equilibrium** | $M$ coincides with $G$ | $GM = 0$ | Body remains in tilted position. |
| **Unstable Equilibrium** | $M$ is **below** $G$ | $GM < 0$ | Overturning couple accelerates capsizing. |

* Time Period of Oscillation (Rolling): $T = 2\pi \sqrt{\frac{k^2}{g \cdot GM}}$ (where $k$ is radius of gyration).
