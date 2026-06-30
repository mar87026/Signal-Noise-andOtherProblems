# Failure Log 06 | AWB with Dual-Cameras

## Symptom:

Both sensors initially observe a yellow wall, then one sensor suddenly turns toward the blue sky while the other points at green vegetation. The AWB algorithm immediately updated the gain based on only one sensor, causing the estimated illuminant to shift dramatically. This occasionally produced visually unacceptable colors, such as unnatural violet or lemon-yellow casts—colors that rarely occur in natural scenes and are highly noticeable to users.

## ROOT CAUSE:

Under normal operation, AWB estimated the white balance gain primarily from one sensor, while the second sensor was largely ignored. This worked well when both sensors observed similar content.

However, problems occurred during rapid scene changes, and also, the color performance could’t violate the Planckian Locus.

![image.png](/operational_is_su-fficient/failure_logs/failure_log_06_awb_with_dual-cameras/image.png)

## AWB Pipeline:

1. Estimate the current illuminant and white balance target within effective grids.
2. Compare the result with the **previous frames** and the Planckian locus stability region.
3. If the change is small, continue normal temporal adaptation.
4. If the change exceeds the threshold, cross-check the second sensor.
5. If the two sensors disagree significantly, treat the scene as unstable and temporarily freeze the white balance update.
6. What ever the former step was, keep the result into **previous frames sequence.**
7. If both sensors indicate a consistent change, verify that the new gain will not produce predefined perceptually unacceptable colors. Apply the value with predefined gain ratio, it might to be called “Custermized”.
8. If all validation conditions are satisfied, gradually update the gain using the existing step-length mechanism.

Also a stability region around the Planckian locus so that minor fluctuations would not trigger unnecessary white balance adjustments. This improves temporal stability while avoiding excessive oscillation.

The key idea is that white balance should not react immediately to every measurement. Every ISP Module which control whole frame coefficients doens’t. Instead, updates should be driven by confidence. Cross-sensor validation is only activated when a significant change is detected, minimizing computational overhead while substantially improving robustness during challenging scene transitions.

#### Extension:

[When HDR breaks White Balance](/operational_is_su-fficient/failure_logs/../algorithm_strategies/when_hdr_breaks_white_balance.md)