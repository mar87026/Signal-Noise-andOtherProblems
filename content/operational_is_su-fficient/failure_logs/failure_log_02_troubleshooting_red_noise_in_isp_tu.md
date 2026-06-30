# Failure Log 02 | Troubleshooting Red Noise in ISP Tuning: Sensor QE, Crosstalk, and Chromatic Aberration Correction

*Troubleshooting withch colorchecker Patch 15*

## **Hypotheses & Root Cause Analysis:**

#### 1. **Sensor Nature (Low Red-CFA SNR):**

Red light has a longer wavelength (lower frequency) and lower photon energy (E=hv ), allowing it to penetrate deeper into the Silicon wafer. Consequently, red photons often bypass the effective photosensitive layer of the photodiode, getting absorbed deep within the substrate or drifting into adjacent pixels. This induces **optical crosstalk**, which is the fundamental physical cause of poor red Quantum Efficiency (QE) and a high noise floor. If this is sensor-inherent, White Balance (WB) gains for Red will be disproportionately high. Noise will persist across the entire grayscale spectrum (though slightly attenuated) and must be mitigated via Color Correction Matrix (CCM) tuning.

#### 2. **Aggressive WB/CC Gains:**

The noise is amplified by excessive gains applied during White Balance or Color Correction. If the noise subsides in a grayscale environment, this is the most manageable scenario to tune.

#### 3. **CAC (Chromatic Aberration Correction) Anomaly:**

Lens dispersion compensation gone wrong. However, CAC artifacts are spatially dependent (worse at corners). If the noise occurs regardless of where the ColorChecker is placed, CAC can be ruled out.

#### 4. **Color Transform (Corner Cases):**

The worst-case scenario involving non-linearities in strict linear transformations. Typically caused by fixed-point overflow, rounding errors, or bit-depth truncation. This requires a Firmware patch/clamping protection. This type of noise usually disappears entirely in grayscale.

## **Step-by-Step Troubleshooting Pipeline:**

#### • **Step 1 (Isolate Sensor/CAC):**

Turn off saturation (render the image in grayscale). If the noise disappears, rule out Sensor Nature and CAC → Go to **Step 2**. If noise persists → Go to **Step 3**.

#### • **Step 2 (Isolate CCM vs. CT):**

With saturation enabled, set the CCM to an Identity Matrix and WB gains to 1.0. If the noise disappears, CCM tuning is the culprit. If it persists, it is a Color Transform (CT) overflow issue; inspect bit-depth and clamping logic.

#### • **Step 3 (Isolate Sensor vs. CAC):**

Move a red object from the image center to the boundaries. If the noise intensity correlates with spatial positioning (amplified at the corners), it is a CAC issue. If the noise remains spatially uniform, it is sensor-inherent; leverage CCM parameters to suppress the red-channel noise floor.