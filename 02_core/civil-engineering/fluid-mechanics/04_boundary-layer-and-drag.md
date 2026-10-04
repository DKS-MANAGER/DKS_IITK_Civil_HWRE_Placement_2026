# 04 — Boundary Layer Theory, Separation & Drag

> **Discipline**: Fundamental Fluid Mechanics  
> **Key Exam / Interview Topics**: Prandtl boundary layer equations, Boundary layer thickness ($\delta, \delta^*, \theta$), von Karman momentum integral equation, Laminar vs turbulent boundary layer, Flow separation and control, Form drag vs skin friction drag.

---

## 1. Boundary Layer Definitions

As fluid flows past a solid body, viscosity is significant only within a thin layer adjacent to the surface where velocity rises from zero (no-slip condition) to $99\%$ of the free stream velocity ($U_\infty$).

```text
U_inf ──────────────────────►
         δ(x) ┌───────────────────────────┐  Velocity u(y)
      ════════╪═══════════════════════════╧═══════════► Flat plate (y = 0)
```

### 1. Nominal Thickness ($\delta$):
Distance $y$ where $u = 0.99 U_\infty$.

### 2. Displacement Thickness ($\delta^*$):
The distance by which the external inviscid streamlines are displaced outward due to the boundary layer velocity deficit:
$$\delta^* = \int_0^\delta \left(1 - \frac{u}{U}\right) dy$$

### 3. Momentum Thickness ($\theta$):
The distance by which the physical boundary would have to be shifted to account for the total momentum deficit in the fluid layer:
$$\theta = \int_0^\delta \frac{u}{U}\left(1 - \frac{u}{U}\right) dy$$

### 4. Shape Factor ($H$):
$$H = \frac{\delta^*}{\theta}$$
* For laminar boundary layer: $H \approx 2.59$.
* For turbulent boundary layer: $H \approx 1.3\text{--}1.4$. (Lower shape factor indicates fuller velocity profile and greater resistance to separation).

---

## 2. Laminar vs Turbulent Boundary Layer over Flat Plate

| Parameter | Laminar Boundary Layer ($Re_x < 5 \times 10^5$) | Turbulent Boundary Layer ($Re_x > 5 \times 10^5$) |
| :--- | :--- | :--- |
| **Velocity Profile** | Blasius solution: $\frac{u}{U} \approx \frac{3}{2}\frac{y}{\delta} - \frac{1}{2}\left(\frac{y}{\delta}\right)^3$ | $1/7\text{th}$ Power Law: $\frac{u}{U} = \left(\frac{y}{\delta}\right)^{1/7}$ |
| **Boundary Layer Growth ($\delta$)**| $\delta = \frac{5.0 x}{\sqrt{Re_x}} \propto x^{0.5}$ | $\delta = \frac{0.37 x}{Re_x^{0.2}} \propto x^{0.8}$ |
| **Displacement Thickness ($\delta^*$)**| $\delta^* = \frac{1.72 x}{\sqrt{Re_x}} \approx \frac{\delta}{3}$ | $\delta^* = \frac{0.046 x}{Re_x^{0.2}} \approx \frac{\delta}{8}$ |
| **Momentum Thickness ($\theta$)** | $\theta = \frac{0.664 x}{\sqrt{Re_x}}$ | $\theta = \frac{0.036 x}{Re_x^{0.2}} \approx \frac{7}{72}\delta$ |
| **Local Skin Friction ($C_{fx}$)** | $C_{fx} = \frac{0.664}{\sqrt{Re_x}}$ | $C_{fx} = \frac{0.059}{Re_x^{0.2}}$ |
| **Total Drag Coefficient ($C_D$)** | $C_D = \frac{1.328}{\sqrt{Re_L}}$ | $C_D = \frac{0.074}{Re_L^{0.2}}$ |

---

## 3. Boundary Layer Separation & Control

### 1. Physical Mechanism of Separation:
Flow separation occurs under an **adverse pressure gradient** ($\frac{dp}{dx} > 0$, fluid decelerating in divergent channel or around rear of cylinder). Viscous friction removes fluid kinetic energy near the wall until fluid particles come to rest and reverse direction.

$$\left.\frac{\partial u}{\partial y}\right|_{y=0} > 0 \implies \text{Attached Flow}$$
$$\left.\frac{\partial u}{\partial y}\right|_{y=0} = 0 \implies \text{Point of Imminent Separation}$$
$$\left.\frac{\partial u}{\partial y}\right|_{y=0} < 0 \implies \text{Separated Flow (Backflow \& Eddy Shedding)}$$

### 2. Separation Control Methods:
1. Streamlining the body shape (reducing adverse pressure gradient).
2. Boundary layer suction (sucking decelerated fluid through porous wall).
3. Boundary layer blowing / energizing (injecting high-momentum fluid tangential to wall).
4. Vortex generators (inducing turbulence to mix high-speed outer fluid into boundary layer).
