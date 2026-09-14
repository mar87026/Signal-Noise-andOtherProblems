# PQ - Parking Lot Surveillance

*Designing an objective Picture Quality validation workflow*

## Requirement

The camera was installed at the entrance of an airport parking lot, facing strong backlight during the daytime. Vehicles slowed down approximately four meters in front of the camera for license plate recognition before turning into the parking area.

![image.png](/operational_is_su-fficient/picture_quality_engineering/pq_-_parking_lot_surveillance/image.png)

Due to security requirements, both the automatic license plate recognition(LPR system) and security personnel had to identify the license plate and vehicle type during this short turning interval.

The scene was particularly challenging because direct sunlight, vehicle headlights, and reflections from queued cars significantly reduced local contrast and obscured fine details.

## Problem Definition

Do not violate the PQ standard at our side, and statify consumer’s requirement.

## Lab Reproduction

Since real license plates were unavailable, I recreated the enviornment inside our laboratory. Commercial decorative metal license plates were purchased to mimic reflective characteristics.
Adiitional painted aluminum samples and irregular metallic objects were introduced to reproduce specular highlights and challenging reflections.

## PQ Strategy

Initial evaluation showed that most characters were correctly recognized. However, visually similar characters such as “3” and “8”, as well as “R” and “B”, frequently failed under strong highlights.

HDR was primarily used preserve long-exposure shadow information.
Excessive gamma enhancement increased edge contrast but also amplified local discontinuities, creating block artifacts that reduced OCR stability.

Increasing color saturation further improved plate readability. Although this could increase chroma noise on lower-cost sensors, the target deployment used high-end industrial cameras, making this trade-off acceptable.

## Benchmark

Finally, the customer requested a direct comparison against a competitor’s SoC using the identical input signal. Our solution consistently achieved better readability under this specific scenario, although performance varied across different environments. Performance depended on scene characteristics and optimization priorities.