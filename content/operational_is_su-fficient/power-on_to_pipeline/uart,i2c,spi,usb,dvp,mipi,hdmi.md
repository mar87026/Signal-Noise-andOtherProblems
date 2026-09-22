# UART,I2C,SPI,USB,DVP,MIPI,HDMI

*First step to debug*

Note:
640*480 30FPS 8bits: 73,728,000 approximately equal to 74M bps

1080p 30FPS 12bits: 746,496,000 approximately equal to 750M bps

#### Speed:

UART(115.2k) < I2C(3.4M) < SPI(50M) < DVP(<150M) <USB <PCle<HDMI(10-48G) <DP(21-80G)

#### Ages:

UART(1970s) < I2C(1980s) ≈ SPI(1980s) < USB(1996) < DVP(2000s) ≈ HDMI(2000s) < DP(2006)

| Abbreviation | Full Name | Lines number | Advantage | Defect | Speed Limit |
| --- | --- | --- | --- | --- | --- |
| I2C | Inter-Integrated Circuit | 2 <br> clock <br> data | 2 pins only <br> | read can’t synced with write | about 3.4M <br> usually 400kps |
| Wake up sensors, change the registers’ value. |  |  |  |  |  |
| SPI | Serial Peripheral Interface | 4 <br> clock <br> Master Out Slave In <br> Master In Slave out <br> Chip Select | read and write in same time. | Add any item, add one CS line for transmission | usually 50M |
| transmit OSD inform which shown on screen and return IMU inform |  |  |  |  | p |
| UART | Universal Asynchronous Receiver-Transmitter | 3 <br> **NO CLOCK** | 3 line only | Slow <br> One to one <br> Easy to be affected by electromagnetic | usually 115.2Kbps |
| Connection with MCU. Usually deploying at engineer debug mode. |  |  |  |  |  |
| USB | **U**niversal **S**erial **B**us | 4 <br> power <br> D+ <br> D- <br> GND | support <br> Hot-Plugging <br> Plug and Play <br> Power Delivery | Protocol Overhead <br> Master CPU cost <br> short transmission distance | USB(2.0) <br> 480M in theory <br> 320M in practice <br> USB(3.1) <br> 5Gbps |
| Transmitted the IR inform |  |  |  |  |  |
| DVP(parallel) | Digital Video Port | 8-12 <br> HSYNC and VSYNC | Easy to follow | Low <br> sure to support 4K frame, but EMI would ruin everything. | < 150 Mbps |
| simple MCU, toy camera |  |  |  |  |  |
| MIPI(D-PHY) | Mobile Industry Processor Interface | 1+N <br> clock <br> N pairs of data | dominate | be careful of clock sync | 2.5G to 4.5G |
| transmit 4K video, 1080p60 frames and multi-sensor inform |  |  |  |  |  |
| MIPI(C-PHY) | Mobile Industry Processor Interface | 3 <br> no clock, hiding clock in path | really really high speed | expensive <br> high complexity | 80Msp to 8.0Gsps |
| Deploy above 100MP resolution |  |  |  |  |  |
| DP | DisplayPort  | Packet-based, so good in extension | Support High fresh framerate <br> Support USB type C <br> No patent fee <br> One wire offer several screens at same time but display separately. | wire required under 1.8M <br> Low support Ratio | 21~80Gbps |
| Used in Multi-screen user. |  |  |  |  |  |
| HDMI | High-Definition Multimedia Interface |  |  | Patent fee, so the vender tend to provide DP. | 10~48Gbps |
| Used in all visual products. |  |  |  |  |  |
| PCle | Peripheral Component Interconnect Express | 4x, depends on version | could support edge computing while connecting with AI recognition | super expensive | **PCIe 4.0** 16 GT/s32 GB/s ~7,500 MB/s |
| Server, Computer, game console and high level UAV. |  |  |  |  |  |