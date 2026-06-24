# Failure Log 00 | Architectural Overreach: From Non-Linear WDR-LTM to Grid-Based Linear Pipeline

### 1. The Genesis: The Radical Joint Architecture (Fusion 1)

- **Context:** The ISP in its early stages was in a state of "hardware deficiency"—the pipeline lacked an independent LTM (Local Tone Mapping) module and only featured globally adjusted WDR.
- **The Idea:** On edge devices with ultra-low power consumption and extremely constrained chip area, I made a bold architectural attempt: a **Joint WDR and Local Tone Mapping** approach. I tried to bind the "physical fusion of dynamic range" and "spatial local contrast enhancement" into a single module.
- **The Implementation:** Utilizing a Local Histogram for non-linear content analysis, I forcefully "pumped" out shadow details right at the front-end pipeline. Even without a back-end LTM, it brute-forced the output to maximize visual information.

---

### 2. The Dilemma: A Color Engineer's Compromise and the Hardware Cost Trap

- **Domain Knowledge Conflict:** With my background rooted in color algorithms, I knew exactly the price of breaking signal linearity at the front end: it would heavily burden downstream color calibration (CCM/AWB) and induce temporal flickering. But I compromised, because the immediate visual impact of non-linear fusion was undeniably far superior to pure linear fusion at that moment.
- **The "Sort" Illusion:** This was my biggest architectural misjudgment. During a discussion with the hardware engineers, their casual remark, "We already have the code for sorting," led me to a severe miscalculation.
- **Misplaced Focus:** All my mental bandwidth was consumed by dealing with the 5x5 window and frame sync, causing me to completely overlook the horrific cost of implementing Local Statistics and Sorting at the hardware front-end. When I finally saw the Area/Gate count after hardware synthesis, the regret was immense—the cost was unacceptably massive.

---

### 3. The Pivot: The Reluctant Return to Linearity and Full-Frame Operations (Fusion 2)

- **The Correction (The Linear  version):** After digesting this architectural disaster, I immediately axed the Statistics and Sort blocks, forcibly yanking Fusion 2 back to the industry-standard **"linear decoupled pipeline."**
- **The Compromise:** In pursuit of extreme stability, I practically abandoned the Line Buffer paradigm and retreated to a Full-frame operation mode.
- **The Dissatisfaction:** Although full-frame operations perfectly bypass the inconsistencies and boundary artifacts between grids, I fundamentally despise this solution. According to the dogmas of Edge AI and low-power silicon design, relying on entire frames to operate is inelegant and lacks scalability.

---

### 4. The Promise: Towards a Grid-Based Future (Fusion 2.5)

Since the current WDR also processes the entire frame, the refactoring needs to be done thoroughly all at once.

- **Current Research:** I am currently tearing down and auditing industry algorithms for Local Dimming and Defogging.
- **The Objective:** The next generation of the fusion pipeline must transition entirely from frame-based to **Grid-based operation**. The goal is to utilize grid-level processing without relying on massive full-frame memory, employing mathematical models to resolve the brightness discrepancy issues at partition boundaries.

<aside>
⚙️

*There will be a Fusion 2.5. This is an engineer's promise to the system architecture.*

</aside>