# Failure Log 01 | Debugging ISP Video Stream Corruption: Hardware Failure vs. Auto Exposure (AE) Loop Runaway

*When AE Works, But the Image Fades Away.*

## **Root Cause:**

**Physical layer failure (damaged ribbon cable) caused silent data corruption in the input video stream.** The initial Y-channel values were consistently read as near-zero, leading the ISP’s Auto Exposure (AE) loop to incorrectly trigger a maximum-gain compensation.

## **Debugging & Diagnosis:**

The issue was initially masked by the system’s adaptive behavior; the AE algorithm continuously boosted gain in response to the perceived "underexposed" input, resulting in an exponentially brightening output. Attempts to trace the Firmware execution via interrupt monitoring were hindered by the system’s internal safety protection, which froze execution context upon detecting anomalies. By isolating the input source, we identified that the signal delivery from the sensor to the SoC was inconsistent, confirming a hardware-level integrity issue rather than a software logic error.

## Preventive Measures & Lessons Learned:

- **Logic Inconsistency Check:** Implemented a cross-domain validation layer in the post-ISP pipeline. The system now validates the correlation between environmental indicators (e.g., Dark Channel Prior) and color correction results (AWB). If a low-light state is detected alongside high-saturation color gains, the system triggers an anomaly flag to halt the gain-loop.
- **Temporal Stability Guard:** Added a change-rate threshold for gain adjustments. Any sudden, physically impossible convergence shifts are now flagged as signal-integrity failures, protecting the downstream pipeline from runaway gain accumulation.
- **Zero-Trust Input Policy:** Shifted toward a "Zero-Trust" architecture where ISP statistics are no longer accepted as valid if they violate fundamental physical consistency, regardless of the sensor's reported status.