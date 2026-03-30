#  Phase 2: Sentinel Hardware Interface
### *Custom 3D-Printed Security Console & Telemetry Bridge*

##  Project Overview
**The Sentinel** is a custom hardware peripheral designed to act as a physical "Gatekeeper" for the Hydra Cluster. This phase focuses on **Human-Machine Interface (HMI)** design and hardware-level security. 

Instead of an independent PC, the Sentinel leverages the processing power of the **Phase 1 Master Node**, functioning as a dedicated hardware security module and telemetry dashboard.

---

##  Hardware Integration & Logic

### 1. Host-Powered Architecture
To maximize efficiency, the Sentinel Console connects directly to the Master Node:
*   **Display:** Powered via HDMI, providing a dedicated 7-inch "Heads-Up Display" (HUD) for cluster metrics.
*   **Data Bridge:** The Raspberry Pi Pico communicates with the host OS over a **Serial-over-USB** interface.

### 2. The "Handshake" Security Protocol
The Pico runs a persistent MicroPython loop. It does not allow the Master Node to initiate Phase 3 GPU tasks until a **Hardware Handshake** is successful.
*   **Logic:** The host script waits for a "VALID_AUTH" string from the Pico.
*   **Security:** This ensures that even if the software is compromised, a physical presence is required to "arm" the system.

### 3. Custom 3D-Printed Enclosure
The entire unit is housed in a bespoke, 3D-printed chassis. 
*   **Material:** PLA (Polylactic Acid).
*   **Design Focus:** Integrated internal cable management to hide the HDMI and USB tethers, presenting a clean, professional "Control Center" aesthetic.
## Diagrams 
<img width="542" height="677" alt="image" src="https://github.com/user-attachments/assets/1e632e41-fa90-46d3-ae89-2c587a3a2ed6" />
<img width="579" height="337" alt="image" src="https://github.com/user-attachments/assets/24919cd0-02b4-490b-bb92-8dea6b1577d6" />


---

## 📊 Bill of Materials (BOM)


| Component | Model | Purpose | Price (GBP) |Link|
| :--- | :--- | :--- | :--- |:---|
| **Telemetry UI** | 7" HDMI IPS Touchscreen | System Monitoring & UI | £27.19 |[amazon](https://www.amazon.co.uk/FOLOSAFENAR-Capacitive-Touchscreen-Resolution-Compatible/dp/B0CDH6GTNQ/ref=asc_df_B0CDH6GTNQ?mcid=e164062c24763c7ba9a207d0167b5376&tag=googshopuk-21&linkCode=df0&hvadid=696386561242&hvpos=&hvnetw=g&hvrand=2629794622045856847&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9045084&hvtargid=pla-2430690427567&psc=1&hvocijid=2629794622045856847-B0CDH6GTNQ-&hvexpln=0&gad_source=1)|
| **Auth Hardware** | 2x RC522 RFID Modules | Dual-Key Physical Security | £6.24 |[amazon](https://www.amazon.co.uk/Hailege-2pcs-RFID-Reader-Module/dp/B0DRCRLJ8R/ref=sr_1_10?dib=eyJ2IjoiMSJ9.Kn2u2iQKKEHfDyFZJn_MgCEe7Rm0WL7ZjZTMjiconwhUJoS0hthr-EXKDWZ3FAfYP2B18TcTQ135YENgk0jXw4yPpyOGIQ4MyZeynwfDTBC7fsDPfMHwr9obMcKhUeUEdV27uVUDG-EgrfPlFQYxMnLsgNmMUPWL8HOLNLQLnCsfkyrdpaBOqyzgfQiSwC1VWeR1oHXib8Hsik41hFTcJP4LGh8GXqYRhRu_GgfgjDA.phazFojAh_IsXMwRtyMVmVXo3DPLdlfKub9O_sPXxDM&dib_tag=se&keywords=rc522&qid=1774820051&sr=8-10)|
|Festerness|16 mm Stainless Steel Screws M3|Componing mounting|£7.59|[amazon](https://www.amazon.co.uk/Stainless-Screws-Tapping-Hardware-Fasteners/dp/B0G1TVGBHY/ref=sr_1_7?crid=DB4C84C6JEJ&dib=eyJ2IjoiMSJ9.zaZwc9twDUWd0OSNe7QVOuZIXlvqVZ7g9zvxd1DYT9AqAaTNyJNjZlVNbmNtMYFfTYWy0imCNOT7MxCS00K3b82ueCQA1z01Zcs54Zr6IMSCvzaah7qa0939qmcfKOv2fXhEbOlO7w-qOx5ov2i2T-0ay5IiYfXKdfKrlREYxI4u6u5Xt4nze_gYvhk5e8kIKBnyb9nQkAZPgEKKDJQpbBTnEEZlVVK-W0pDigOKK0j1CjXkGQByoIIwme31U9e-LxC1uwsWv09Amti5gGprjw.SXItqV1Fh_lu3mkYWAd3UN2kC0reFtzCORfRcU7_Nwk&dib_tag=se&keywords=M3%2B(10-12мм)%2Bsharp%2Bend&qid=1774902143&refinements=p_36%3A-1000&rnid=118657031&sprefix=m3%2B10-12мм%2Bsharp%2Bend%2Caps%2C306&sr=8-7&th=1)|
|Festerness|Double Sided Tape Heavy Duty|Component mounting|£7.99|[amazon](https://www.amazon.co.uk/KICQOM-Mounting-Removable-Multipurpose-3mx2cmx2mm/dp/B0D9BXLYSC/ref=sr_1_5?crid=116I0TZBQ13CV&dib=eyJ2IjoiMSJ9.LyNQEMjvn6V2fJD5fh6O7gIBr_di3HM_f3Sx8SS_7fWc5rogxRkkaRplOTuIxUP82eQvJglnAmbgCeGU3qpmytIT26GAzGakpJ1-ToRxYgTSKgUZTf_rEa-N_JtgATn-bjS2LpnCZXc08cnKoG6bDsJ5nUeTi4oMTrhbU6aTGn6M_or2Jpld7Q6byldwC6tfY37VGlqm6543EpWWoVIvqkL8QO9sj7ZMeU1aWtKLSshtwcT8pgSJhAjvoevo97nsyUvzUKhYGwQnFqKH79SiVuduxyUUi0Qb2seSAQsDeDM.IKPRjRrzcHiyLYyfuSrZkVMVaJOjPKYq-dcDWWEPQpw&dib_tag=se&keywords=scotch%2Btwo%2Bside&qid=1774902312&sprefix=scoth%2Btwo%2Bside%2Caps%2C382&sr=8-5&th=1)
| **Logic Controller** | Raspberry Pi Pico (RP2040) | Hardware-to-OS Firmware | £11.39 |[amazon](https://www.amazon.co.uk/IBest-Pre-Soldered-Pico-Microcontroller-Board/dp/B091TLCNJD/ref=sr_1_2?crid=1HDURYW5ZBFO2&dib=eyJ2IjoiMSJ9.4d8ulAHF6e79yadSzoGsp8w5SUwYB3KPQ9fvxvHyv2ldJhmft0sdHHP_pxHFNBdqnESOLRpoTwnvPirowZFE-c0IMsi0PBu5Qfk4CnssscbI5L-zQ1ZZMJxXpIIc-7anPk1_3mj0MuyPYQSB_OXG4ro7zGa8saORApnmHbU9lkZtuIcexQlZey4P7YgPgafXso4eQ2hGSEQl7wyFP8XCwasWa6tHpf3wDZZRqOWeBe54N4IJTuWauS3ulZ9pz_s9W_0LARcPBpZGxs65l5pkMuskGPXFG_vakiSDe1eoIbM.1jU4gqdN2LbvKD0IO5pmrgLiWLYHMc942cMJayWK6Ws&dib_tag=se&keywords=Raspberry%2BPi%2BPico%2B(RP2040)&qid=1774820135&s=computers&sprefix=raspberry%2Bpi%2Bpico%2Brp2040%2B%2Ccomputers%2C296&sr=1-2&th=1)|
|Enclosure|	1kg PLA Filament(black)|	Custom 3D Printed Chassis	|£12.99|[amazon](https://www.amazon.co.uk/ELEGOO-Filament-Dimensional-Accuracy-Printers/dp/B0F4871GP4/ref=sr_1_3_sspa?crid=1NKTT1BY54FUU&dib=eyJ2IjoiMSJ9.U3iU3ZmAbqSbG37OAhI4Nnwu7cDqKQoLve0JaciSXui_pzpY1uXEVfywxPiccVc64h5H_nh-3BHs0R-FOkqa0mAXOVT7DCDXZw6oU8IVDXsXo6nRQFO55l01ZRLsL9845dQObb7WkmQ_HRydq8TJZCk51IINoHN23ws4lOESXunTWujWxQTNlzqM_Q0MbW8LdXvtcvF-bo1nl19-iSdS-LjLYbZnTnTKOdRCCZFxTO6V3Id0p1epNtGL8UaBtizT9-cE9CJL_q9CC7X7Jjepg0YascUQ7tnI9ynmw8Ss_cg.cGYMXedu9DjwZH4T8lmp6pHXxnqP6rsoIpnq2IPbMsM&dib_tag=se&keywords=3d%2Bpla&qid=1774901662&sprefix=3d%2Bpl%2Caps%2C312&sr=8-3-spons&aref=7NqVohaY7z&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1)|
|Cabling|	HDMI|  Cables	Data & Video Interconnect|	£6.92|[amazon](https://www.amazon.co.uk/Certified-Adauxter-HDCP2-2-Compatible-Soundbar/dp/B098T3LSY3/ref=sr_1_3_sspa?crid=3NSRPQKKNSOLS&dib=eyJ2IjoiMSJ9.nBiJHTgOZ85ll-lCUW2jXBmVWrCa7gIIVDl6QJHAn17Bu1P4HdsbYJlJG7GmLuqhllNb7YwVxmoSDfQrzGYLeZXR2EZSEQwCXAluX4NcLwFcP1x4GoNXHfFOHLv1CaLmxBa1Oo3LI6y7DZMNVNPw7Lp-NgxH3Wz7gYJo2-fJrMYnsrgbbGV_Ddi0feDYp2d5SUm55IFjBmFf63yKs4dQZpGecGquNkWYiflFIHSQUcfXupms6x7K_C1SqHuvm2f_EMczaHnP7qw_kOIoJrbViZe1di2o7e_dFRnVC_6nVwU.DIafcwIcdrc3S9PycV64EnhFhwkmxLX8LYk_bnF_Nk0&dib_tag=se&keywords=HDMI&qid=1774821084&s=industrial&sprefix=hdmi%2B%2Cindustrial%2C356&sr=1-3-spons&aref=6PiCvsNz8I&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1)|
|Cabling| HDMI(adapter)| Cables Data & Video Interconnect|£9.99|[amazon](https://www.amazon.co.uk/RIIEYOCA-Degree-Braided-0-56ft-Supports/dp/B0C4GJFGD6/ref=sr_1_5?crid=1PA6MIRX4TBUZ&dib=eyJ2IjoiMSJ9.ZVeuRBklX8SCZT2maKo6oQLyaVuZOeiwxzTl-SMdt5lGrJ_KxsYYae1PjxeDf4-fvPt7uz66L7QcCBsc7ij0XPrjF9Hn2jBUJ_7rgK83VLQvoZCVGX_b7GDQ1dBB_9c2S6Zb0ilM5tZpnsCmegFpxH52MlU4AXVmDYJ7uYIcXuuO1CLiiAu52zKntipvOeuzjccbVPV54GSkQQ1Y_X7XKPCheQlu3MvjCasjZHhrwn8.ePZNDATCna1waxt5Tcub5Ze0tp48hTF7AY2zUDqRQ4c&dib_tag=se&keywords=hdmi%2B90%2Bdegree%2Badapter&qid=1774901862&sprefix=HDMI%2B90%2B%2Caps%2C302&sr=8-5&th=1)|
|Sound|Buzzer, 3-24V Piezo Electronic Tone Buzzer Alarm Continuous Sound Cable|Sound that it worked|4.59|[amazon](https://www.amazon.co.uk/Electronic-Continuous-electronic-component-assortment/dp/B07YG9WQMX/ref=sr_1_12?dib=eyJ2IjoiMSJ9.7c6wBy1eaB9CTMn3kEHq49BbbuF60bqy-UgzmpHYH3xiAbL57Mv4KEivZh_FmlsJEUWRMgicUn5CibabYbTg4zLyg9BZTkF4-Elx0Uq4mygsC-TTlhpDCMWB-ziyMfvhqAp5V_YBrBH7kYQWVr3qAuZvfxdy7PrMXtxI9yNzusqd9q9Fo4Iy4qqJJPANOtkng-NOhBLVX9zD9BJ2az1KUkSt9X6EqqiaXZuqeHoX4i926pkcYQvrlF70KLLmnBylKSjODbtS1lzVEChR4GK18lgccy9dW6L9RmCOQrmTPKw.un1aNYNGvgURlsfnVrqfNUecezzOLfGbPCXXjpjkP_w&dib_tag=se&keywords=Active+Buzzer+%283.3V%29&qid=1774902519&sr=8-12)|
| **TOTAL** | | | **£94.89/$125,09** |

---

## 🛠️ Software & Firmware Stack
*   **MicroPython:** Polling RFID UIDs and controlling status LED indicators.
*   **Docker:** Containerization of monitoring services on the internal Micro-PC.
*   **MQTT/Serial:** Protocol for transmitting security status between the Console and the Cluster.

---
##  Wiring Diagram (Pinout)
| Component | Module Pin | Pico Pin (GPIO) | Physical Pin # | Signal Type |
| :--- | :--- | :--- | :--- | :--- |
| **RFID Reader L (Master)** | SDA (SS/CS) | **GP17** | 22 | SPI0 CS |
| | SCK | **GP18** | 24 | SPI0 SCK |
| | MOSI (TX) | **GP19** | 25 | SPI0 TX |
| | MISO (RX) | **GP16** | 21 | SPI0 RX |
| | RST | **GP20** | 26 | Reset |
| | 3.3V | **3.3V(OUT)** | 36 | Power |
| | GND | **GND** | 38 | Ground |
| **RFID Reader R (Slave)** | SDA (SS/CS) | **GP13** | 17 | SPI1 CS |
| | SCK | **GP10** | 14 | SPI1 SCK |
| | MOSI (TX) | **GP11** | 15 | SPI1 TX |
| | MISO (RX) | **GP8** | 11 | SPI1 RX |
| | RST | **GP9** | 12 | Reset |
| | 3.3V | **3.3V(OUT)** | 36 | Power |
| | GND | **GND** | 13 | Ground |
| **Active Buzzer** | (+) Positive | **GP15** | 20 | Digital Output |
| | (-) Negative | **GND** | 18 | Ground |
| **7" IPS Screen** | HDMI | **N/A** | External | Video Feed |
| | Micro-USB | **N/A** | External | Power / Touch |

---

## 🛠️ Assembly & Wiring Notes

### 1. SPI Bus Separation
The system uses **Dual-SPI architecture**. This prevents data collisions between the two RFID readers, allowing the Pico to poll both authentication slots simultaneously without lag.

### 2. Power Strategy
- **7" IPS Screen:** MUST be powered directly from the Master Node (PC) USB port. Do NOT power the screen via the Pico pins, as the current draw exceeds the Pico's limits.
- **RFID Modules:** Powered by the Pico's 3.3V(OUT) pin. For extra stability, add a 10µF capacitor between VCC and GND if you experience read errors.
- **Pico:** Powered via the Micro-USB cable, which also acts as the Data Bridge for the `Rolling Password` protocol.

### 3. Cable Management (No-Holder Build)
- Use **3M VHB Double-Sided Tape** to secure the RFID modules against the front panel.
- Ensure the **antenna side** (the loop on the PCB) of the RFID reader is facing the plastic wall (2.5mm thickness).
- Keep SPI jumper wires under **20cm** to avoid electromagnetic interference (EMI).

### 4. Buzzer Polarity
The Active Piezo Buzzer is polarity-sensitive:
- **Long Leg (+):** Connect to GP15.
- **Short Leg (-):** Connect to GND.




---

##  System Logic Flow (The "Sentinel" Protocol)

```mermaid
graph TD
    Start[Power On] --> Init[Init SPI0 & SPI1]
    Init --> Idle{Scanning Slots...}
    
    Idle -->|Card 1 Detected| Check2{Card 2 Present?}
    Check2 -->|No / Timeout| Error[Access Denied: Dual-Auth Required]
    Check2 -->|Yes| Validation{Check Whitelist}
    
    Validation -->|Match| Grant[Serial: AUTH_GRANTED]
    Validation -->|Mismatch| Alert[Serial: SECURITY_ALERT]
    
    Grant --> Monitor{Keep-Alive Loop}
    Monitor -->|Card Removed| Revoke[Serial: SESSION_TERMINATED]
    Revoke --> Idle
    Error --> Idle
