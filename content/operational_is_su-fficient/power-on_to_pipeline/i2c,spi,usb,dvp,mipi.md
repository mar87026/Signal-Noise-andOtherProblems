# I2C,SPI,USB,DVP,MIPI

*First step to debug*

| Abbreviation | Full Name | Lines number | Advantage | Defect | Speed Limit |
| --- | --- | --- | --- | --- | --- |
| I2C | Inter-Integrated Circuit | 2
clock
data | only 2 pins
simple | read can’t synced with write | about 3.4M
usually 400kps |
| Wake up sensors, change the registers’ value. |  |  |  |  |  |
| SPI | Serial Peripheral Interface | 4
clock
Master Out Slave In
Master In Slave out
Chip Select | read and write in same time. | Add any item, add one CS line for transmission | usually 50M |
| transmit OSD inform which shown on screen and return IMU inform |  |  |  |  | p |
| USB(2.0) | **U**niversal **S**erial **B**us | 4
power
D+
D-
GND | support 
Hot-Plugging
Plug and Play
Power Delivery | Protocol Overhead
Master CPU cost
short transmission distance | 480M in theory
320M in practice |
| Transmitted the IR inform |  |  |  |  |  |
| DVP(parallel) | Digital Video Port | 8-12
HSYNC and VSYNC | Easy to follow | Low
sure to support 4K frame, but EMI would ruin everything. | < 150 Mbps |
| simple MCU, toy camera |  |  |  |  |  |
| MIPI(D-PHY) | Mobile Industry Processor Interface | 1+N
clock
N pairs of data | dominate | be careful of clock sync | 2.5G to 4.5G |
| transmit 4K video, 1080p60 frames and multi-sensor inform |  |  |  |  |  |
| MIPI(C-PHY) | Mobile Industry Processor Interface | 3
no clock, hiding clock in path | really really high speed | expensive
high complexity | 80Msp to 8.0Gsps |
| Deploy above 100MP resolution |  |  |  |  |  |
| PCle | Peripheral Component Interconnect Express | 4x, depends on version | could support edge computing while connecting with AI recognition | super expensive | **PCIe 4.0** 16 GT/s32 GB/s ~7,500 MB/s |
| Server, Computer, game console and high level UAV. |  |  |  |  |  |