# Sources, Economic Baselines & Verification Standards

> **Document Type**: Authoritative Demographic & Economic Reference Repository
> **Scope**: Official baseline data, demographic segmentations, and mathematical validation standards for consulting guesstimates and market sizing.

---

## 1. Evidentiary Standards & Tagging Taxonomy

All statements, statistics, and figures in this curriculum adhere strictly to standardized evidentiary labels:

* `[OFFICIAL DEMOGRAPHIC SOURCE]` — Directly verified from official governmental statistics (e.g., Census of India, National Family Health Survey NFHS-5, Ministry of Statistics and Programme Implementation MOSPI).
* `[REGULATORY / CENTRAL BANK SOURCE]` — Supported by official standards issued by statutory regulators (e.g., Reserve Bank of India, TRAI, NITI Aayog).
* `[OFFICIAL COMPANY SOURCE]` — Confirmed from official company investor presentations, annual reports, or regulatory filings.
* `[HISTORICAL PLACEMENT SOURCE]` — Documented interview debriefs from past IIT Kanpur recruitment cycles.
* `[PRACTICE ASSUMPTION]` — Stylized, simplified, or hypothetical numbers explicitly formulated for case drills.
* `[PREPARATION HEURISTIC]` — Practical rule-of-thumb or pedagogical guideline.

---

## 2. Authoritative Demographic & Economic Baselines (India & Global)

### India Macro & Demographic Profile (2024–2026 Reference)

| Metric | Canonical Baseline Value | Primary Official Source | Use in Case Interviews |
| :--- | :--- | :--- | :--- |
| **Total Population** | **1,420 Million (~1.42 Billion)** | UN World Population Prospects / MoSPI | Standard denominator for all per-capita estimations. Round to **1.4 Billion** for clean interview mental math. |
| **Average Household Size** | **4.2 persons / household** | NFHS-5 / Census of India | Divide population by **4.0** to estimate total households $\approx$ **350 Million Households**. |
| **Urban vs. Rural Split** | **35% Urban / 65% Rural** | MoSPI / World Bank | Urban $\approx$ **500M people (~120M households)**; Rural $\approx$ **920M people (~230M households)**. |
| **Age Demographics** | - $0–14$ yrs: **25% (~355M)**<br>- $15–24$ yrs: **18% (~255M)**<br>- $25–59$ yrs: **47% (~670M)**<br>- $60+$ yrs: **10% (~140M)** | Census Projection / NITI Aayog | Critical for workforce, education, and consumer tech sizing. Working-age population ($15–59$) $\approx$ **65% (~925M)**. |
| **Income Segmentation (Households)** | - Affluent / High: **10% (~35M)**<br>- Middle / Aspiring: **30% (~105M)**<br>- Lower Middle: **40% (~140M)**<br>- Low / Subsistence: **20% (~70M)** | NITI Aayog / ICE 360 Survey | Fundamental for purchasing power, premium consumer goods, and credit card market sizing. |
| **Internet / Smartphone Penetration**| - Internet Users: **~850–900 Million**<br>- Smartphone Users: **~650–700 Million** | TRAI Telecom Reports / IAMAI | Essential for digital platforms, e-commerce, fintech, and app market sizing. |
| **Two-Wheeler vs Four-Wheeler Base**| - Two-wheelers: **~220–250 Million**<br>- Four-wheelers (Cars): **~40–45 Million** | MoRTH / SIAM | Household penetration: Cars $\approx 10–12\%$; 2-wheelers $\approx 60–65\%$. |

---

### Global & City Macro Baselines

| Geography | Population | Household Size | Total Households | Key Case Sizing Application |
| :--- | :---: | :---: | :---: | :--- |
| **Metro Tier 1 (Delhi NCR, Mumbai)** | **~25–30 Million** | 4.0 | ~6.5–7.5 Million | Ride-hailing, food delivery, metro transit sizing. |
| **Tier 1 Tech Hub (Bengaluru, Hyd)** | **~12–15 Million** | 3.5 | ~3.5–4.2 Million | Quick commerce, co-living, high-tech B2C platforms. |
| **United States** | **~340 Million** | 2.5 | ~135 Million | Global SaaS, enterprise software, pharma cases. |
| **European Union** | **~450 Million** | 2.3 | ~195 Million | Cross-border trade, renewable energy cases. |

---

## 3. Mathematical & Arithmetic Validation Standards

To ensure zero computational errors across all exercises:
1. **Compounding Limits**: The Rule of 72 approximation $\left(\text{Years to double} \approx \frac{72}{r\%}\right)$ is accurate to within $\pm 1\%$ for rates between $4\%$ and $12\%$. At rates above $15\%$, the exact formula $t = \frac{\ln(2)}{\ln(1 + r)}$ must be stated alongside the approximation.
2. **Sanity Checking Protocols**:
   - *Per-capita reality check*: Total annual market divided by relevant population must yield a sensible per-person consumption figure (e.g., if annual toothpaste tubes sold exceeds 50 per person, the assumption is invalid).
   - *Capacity / Time check*: Daily volume divided by operating hours must not exceed physical machine/worker throughput limits.
