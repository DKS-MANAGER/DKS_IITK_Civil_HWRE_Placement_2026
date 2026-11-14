# Root-Cause Error Journal & High-Frequency Traps

## 1. The 4-Category Error Classification Framework
Every mistake in test and interview practice must be cataloged into one of four root causes:
- **Type A (Conceptual Deficiency):** Did not understand the underlying physics or standard (e.g., confusing $C_p$ with $C_{pk}$, or forgetting that Euler formula is invalid below critical slenderness $\lambda_c$).
- **Type B (Mathematical / Arithmetic Slip):** Set up the equation correctly but made an arithmetic calculation error (e.g., misplacing a decimal in $10^{-6}\text{ m}^2$ or forgetting that $1\text{ cycle} = 20\text{ ms}$ at $50\text{ Hz}$).
- **Type C (Misreading / Unit Mismatch):** Did not read question constraints carefully (e.g., diameter vs radius, meters vs millimeters, minutes vs seconds, percentage vs fraction).
- **Type D (Time Pressure / Panic):** Rushed through the problem in the last 5 minutes without sanity-checking the order of magnitude.

---

## 2. High-Frequency Trap Checklist

| Topic | Common Candidate Trap | First-Principles Reality / Safe Rule |
|:---|:---|:---|
| **HPDC Clamping Force** | Calculating projected area based solely on part 3D volume or cavity geometry. | **Always add runner, biscuit, and overflow areas** ($+20\text{--}30\%$), and multiply by safety factor ($1.15\text{--}1.25$). |
| **Process Capability ($C_{pk}$)** | Assuming high $C_p$ ($> 2.0$) means zero defects. | $C_p$ measures spread only. If the mean is shifted ($k > 0$), $C_{pk}$ can be $< 1.0$, producing heavy out-of-spec scrap. **Always check both $C_p$ and $C_{pk}$**. |
| **Euler Buckling** | Applying $P_{\text{cr}} = \pi^2 E I / L^2$ blindly to all compressive members. | **Check slenderness ratio $\lambda$ against $\lambda_c$ first**. If $\lambda < \lambda_c$, Euler formula is invalid; use Johnson's parabolic column formula. |
| **Bolted Joints** | Believing a bolt carries 100% of the external separating load. | Because clamped parts are stiffer than the bolt, the bolt carries only $C \cdot P_e \approx 15\text{--}25\%$ of the load. **Preload protects the bolt from cyclic fatigue**. |
| **Battery Fast Charging** | Assuming cold batteries are safe to charge because "heat causes fires". | Cold charging ($< 0^\circ\text{C}$) drives negative anode overpotentials, depositing **dendritic metallic lithium plating** that pierces the separator. |
| **AIS-156 Compliance** | Quoting the pre-warning alarm as 1 minute or 10 minutes. | **MoRTH legally mandates at least 5 minutes** audio-visual warning before external thermal event breakout. |
| **Resistance Spot Welding** | Setting weld time directly in seconds on AC lines. | Standard timers specify **cycles** at $50\text{ Hz}$ line frequency: $1\text{ cycle} = 1/50\text{ s} = 0.020\text{ s} = 20\text{ ms}$. |

---

## 3. Logged Remediation Journal

### Entry 1: Sheet Metal Bend Allowance Calculation
- *Error:* Used $K$-factor directly as the neutral axis radius instead of neutral axis offset ($R + K \cdot t$).
- *Root Cause:* Type C (Formula syntax misread).
- *Remediation Rule:* $BA = \frac{\pi \theta}{180} (R + K \cdot t)$. Memorize: $K$ is the dimensionless ratio of neutral axis distance to sheet thickness ($y/t$).

### Entry 2: OEE Availability Factor
- *Error:* Divided actual operating time by total shift duration ($480\text{ min}$) instead of planned production time ($480 - \text{planned breaks}$).
- *Root Cause:* Type A (OEE definition boundary).
- *Remediation Rule:* Planned tea breaks and preventive maintenance are excluded from planned time; only *unplanned* downtime penalizes Availability.

### Entry 3: Normal Distribution PPM Tail Area
- *Error:* Looked up $Z$-score for $C_{pk} = 1.33$ as $1.33\sigma$ instead of $3 \times C_{pk} = 4.0\sigma$.
- *Root Cause:* Type A (Relation between $Z$-score and capability).
- *Remediation Rule:* $Z = 3 \times C_{pu}$. A $C_{pk}$ of $1.33$ corresponds to $Z = 4.0\sigma$ ($31.7\text{ PPM}$).

