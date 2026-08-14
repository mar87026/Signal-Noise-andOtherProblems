# Power-On to Pipeline

*Before the ISP processes its first pixel, dozens of hardware and firmware components have already synchornized. Understanding this initialization sequence explains why many image quality bugs cannot be solved by tuning alone.*

## Power on

This step is focusing on the wake the sensors up, and sync all of them. Especially while there are multiple streams in.

![image.png](/operational_is_su-fficient/power-on_to_pipeline/image.png)

| PMIC | Power Management IC | Control Power within droping down or elevate the root. |
| --- | --- | --- |
| GPIO | General-purpose input/output | The root, not a special action, merely an item/technology that tranmit the signal between device. |
| OSC | Oscillator | Control the working cycle time Be the synchronization basic here. |
| AVDD/DVDD | Analog/Digital Device | provid power to the analog/digic circuits in the sensor. |

### Transmission Detail:

[I2C,SPI,USB,DVP,MIPI](/operational_is_su-fficient/power-on_to_pipeline/i2c,spi,usb,dvp,mipi.md)

## Streaming In

After booted up sensor with synchronization, it start to collect the light energy and transmit it within line by line. Transmitting it within MIPI **protocol mostly and save it in RAM within DMA, memory control.**

 

![image.png](/operational_is_su-fficient/power-on_to_pipeline/image_1.png)

### Memory Detail

[Memory](/operational_is_su-fficient/power-on_to_pipeline/memory.md)

### Sensor Type

[Sensor Type](/operational_is_su-fficient/power-on_to_pipeline/sensor_type.md)

## Before 1st Frame

Before first frame input, apply first parameters from .cfg or .bin in flash

![image.png](/operational_is_su-fficient/power-on_to_pipeline/image_2.png)

### Extend:

[Fast Root Cause Isolation for Image Quality Issues](/operational_is_su-fficient/picture_quality_engineering/fast_root_cause_isolation_for_image_quality_issues.md)

## Module On

All data wrote in and marked the same timestamp or Frame ID. Load data from RAM, processed it in ISP module, saved in another uint of RAM.

![image.png](/operational_is_su-fficient/power-on_to_pipeline/image_3.png)

## Module Run

Processor produced statistics and record in RAM.

![image.png](/operational_is_su-fficient/power-on_to_pipeline/image_4.png)