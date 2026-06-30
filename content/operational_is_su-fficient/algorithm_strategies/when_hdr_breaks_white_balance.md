# When HDR breaks White Balance

*Yeah, I know there is no WB word in the picture on main page.*

It’s about linear signal sysyem

White Balance (WB) determines the color temperature by analyzing "qualified" statistics grids (stats grids) across the image. A grid is deemed "qualified" only if its luma (brightness) falls within a specific threshold. Consequently, any module that alters image brightness fundamentally shifts this statistical baseline—including Auto Exposure (AE), its sibling in the 3A algorithms.

I have always opposed boxing 3A into a fixed block within standard ISP pipeline diagrams. 3A algorithms do not belong to a single stage; they control the very source—the lens and the sensor. It’s not that they aren't important; rather, their influence is so overarching that confining them to a specific "territory" in the data flow is a misrepresentation of the system architecture.

WB relies on stable exposure to converge properly. Modules that drastically manipulate signal intensity, such as HDR or DCG (Dual Conversion Gain), severely disrupt the statistical foundation of WB. Imagine a stats grid that was initially rejected for being under-exposed; after HDR blending, it suddenly becomes "qualified." This introduces massive skew in the color temperature estimation.

To mitigate this, standard practice applies a preliminary White Balance (Pre-WB) to the source frames before the HDR/blending module, followed by a second WB pass (Post-WB) after blending. However, this post-blending WB is mathematically valid **only if**:

1. The blending module correctly propagates the applied gain values down the pipeline.
2. The blending logic operates strictly within the **linear domain**.

If the signal passes through **non-linear modules**—such as Local Tone Mapping (LTM) or adaptive histogram equalization (like CLAHE)—the data is mapped onto a curve, effectively moving into a gamma-compressed space. Attempting to calculate or correct linear WB gains on non-linear data is not only mathematically flawed, but also computationally expensive and overwhelmingly complex to reconstruct.

Extend:

[Failure Log 00 | Architectural Overreach: From Non-Linear WDR-LTM to Grid-Based Linear Pipeline](/operational_is_su-fficient/algorithm_strategies/../failure_logs/failure_log_00_architectural_overreach_from_non-li.md)