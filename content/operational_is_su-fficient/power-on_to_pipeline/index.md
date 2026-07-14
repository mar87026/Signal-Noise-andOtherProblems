# Power-On to Pipeline

*Once upon a time, a register was written, and the pixels began to flow.*

## Power on

This step is focusing on the wake the sensors up, and sync all of them. Especially while there are multiple streams in.

![image.png](/operational_is_su-fficient/power-on_to_pipeline/image.png)

| PMIC | Power Management IC |  |
| --- | --- | --- |
| GPIO | General-purpose input/output | The root, not a special action, merely an item/technology that tranmit the signal between device. |
| OSC | Oscillator | Control the working cycle time “CLOCK”, the basic of sync. |
| AVDD/DVDD | Analog Digital Device |  |

### Transmission Detail:

[I2C,SPI,USB,DVP,MIPI](/operational_is_su-fficient/power-on_to_pipeline/i2c,spi,usb,dvp,mipi.md)

## Streaming In

After booted up sensor, it start to collect the light energy and transmit it within line by line. This action called “rolling shutter”.

 

![image.png](/operational_is_su-fficient/power-on_to_pipeline/image_1.png)

| Photodiode |  |  |
| --- | --- | --- |
| DMA | Direct Memory Access |  |
| DDR, RAM, ROM | [Introduction](https://app.notion.com/p/memory-2f827c1a893c80409e27f40c068d4e30?pvs=21) |  |
| Memory Control |  |  |

## Module On

1. Apply first parameters

![image.png](/operational_is_su-fficient/power-on_to_pipeline/image_2.png)

1. All data wrote in and marked the same timestamp or Frame ID. Load data from RAM, processed it in ISP module, saved in another uint of RAM.

![image.png](/operational_is_su-fficient/power-on_to_pipeline/image_3.png)

1. Processor produced statistics and record in RAM.

![image.png](/operational_is_su-fficient/power-on_to_pipeline/image_4.png)

Extend:

[Fast Root Cause Isolation for Image Quality Issues](/operational_is_su-fficient/picture_quality_engineering/fast_root_cause_isolation_for_image_quality_issues.md)