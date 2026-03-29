# 🛡️ Phase 2: Sentinel Hardware Interface
### *Custom 3D-Printed Security Console & Telemetry Bridge*

## 📌 Project Overview
**The Sentinel** is a custom hardware peripheral designed to act as a physical "Gatekeeper" for the Hydra Cluster. This phase focuses on **Human-Machine Interface (HMI)** design and hardware-level security. 

Instead of an independent PC, the Sentinel leverages the processing power of the **Phase 1 Master Node**, functioning as a dedicated hardware security module and telemetry dashboard.

---

## 🏗️ Hardware Integration & Logic

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

---

## 📊 Bill of Materials (BOM)


| Component | Model | Purpose | Price (GBP) |Link|
| :--- | :--- | :--- | :--- |:---|
| **Telemetry UI** | 7" HDMI IPS Touchscreen | System Monitoring & UI | £27.19 |[amazon](https://www.amazon.co.uk/FOLOSAFENAR-Capacitive-Touchscreen-Resolution-Compatible/dp/B0CDH6GTNQ/ref=asc_df_B0CDH6GTNQ?mcid=e164062c24763c7ba9a207d0167b5376&tag=googshopuk-21&linkCode=df0&hvadid=696386561242&hvpos=&hvnetw=g&hvrand=2629794622045856847&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9045084&hvtargid=pla-2430690427567&psc=1&hvocijid=2629794622045856847-B0CDH6GTNQ-&hvexpln=0&gad_source=1)|
| **Auth Hardware** | 2x RC522 RFID Modules | Dual-Key Physical Security | £6.24 |[amazon](https://www.amazon.co.uk/Hailege-2pcs-RFID-Reader-Module/dp/B0DRCRLJ8R/ref=sr_1_10?dib=eyJ2IjoiMSJ9.Kn2u2iQKKEHfDyFZJn_MgCEe7Rm0WL7ZjZTMjiconwhUJoS0hthr-EXKDWZ3FAfYP2B18TcTQ135YENgk0jXw4yPpyOGIQ4MyZeynwfDTBC7fsDPfMHwr9obMcKhUeUEdV27uVUDG-EgrfPlFQYxMnLsgNmMUPWL8HOLNLQLnCsfkyrdpaBOqyzgfQiSwC1VWeR1oHXib8Hsik41hFTcJP4LGh8GXqYRhRu_GgfgjDA.phazFojAh_IsXMwRtyMVmVXo3DPLdlfKub9O_sPXxDM&dib_tag=se&keywords=rc522&qid=1774820051&sr=8-10)|
| **Logic Controller** | Raspberry Pi Pico (RP2040) | Hardware-to-OS Firmware | £11.39 |[amazon](https://www.amazon.co.uk/IBest-Pre-Soldered-Pico-Microcontroller-Board/dp/B091TLCNJD/ref=sr_1_2?crid=1HDURYW5ZBFO2&dib=eyJ2IjoiMSJ9.4d8ulAHF6e79yadSzoGsp8w5SUwYB3KPQ9fvxvHyv2ldJhmft0sdHHP_pxHFNBdqnESOLRpoTwnvPirowZFE-c0IMsi0PBu5Qfk4CnssscbI5L-zQ1ZZMJxXpIIc-7anPk1_3mj0MuyPYQSB_OXG4ro7zGa8saORApnmHbU9lkZtuIcexQlZey4P7YgPgafXso4eQ2hGSEQl7wyFP8XCwasWa6tHpf3wDZZRqOWeBe54N4IJTuWauS3ulZ9pz_s9W_0LARcPBpZGxs65l5pkMuskGPXFG_vakiSDe1eoIbM.1jU4gqdN2LbvKD0IO5pmrgLiWLYHMc942cMJayWK6Ws&dib_tag=se&keywords=Raspberry%2BPi%2BPico%2B(RP2040)&qid=1774820135&s=computers&sprefix=raspberry%2Bpi%2Bpico%2Brp2040%2B%2Ccomputers%2C296&sr=1-2&th=1)|
|Enclosure|	1kg PLA Filament(white)|	Custom 3D Printed Chassis	|£15.00|[amazon](https://www.amazon.co.uk/ELEGOO-Filament-Dimensional-Accuracy-Refilling/dp/B0F42W1K8Z/ref=sr_1_2_sspa?dib=eyJ2IjoiMSJ9.aa-S4e5IHtVzYX09L3lhAbpteRrpqUU-mgyMQIuAwT6FoS2nXHrHDaVxOrAKHB-UAqh72RO7sC1ChubSf8dpk-wkGjSn9uMfw_sUKZ4gok_UDTqLzaZ1aFrHjoWqZVI2ZkAdc5Brd1SoR69OAfLstKORsCMDR-O542SDclHHWm_F2UUAj10EaLrPRik_rLPEfEIJgkVmKBHUTHjuo8NmYk-WzAaLpCBZnLUQtwwQm1fAA6gZpSoyam9knAAokTwPoolQX9QBMMzzN7avmI8SQFfEciVW55WgvGIXk3ghZJI.RgCRl-lLP_K0D9V1D1zxaE73i8E7e5eRnHUW_NO8s24&dib_tag=se&keywords=1kg%2BPLA%2BFilament&qid=1774820830&refinements=p_36%3A1000-1500&rnid=118657031&sr=8-2-spons&aref=tkWP8wr3on&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1)|
|Fasteners|	M3 Bolt & Standoff Set(10 pcs)|	Component Mounting|	£5.00|[amazon](https://www.amazon.co.uk/PATIKIL-Stainless-Extension-Quadcopter-Assortment/dp/B0DX786YB1/ref=sxin_15_pa_sp_search_thematic_sspa?content-id=amzn1.sym.39f3f322-e4f4-475f-ab3a-16807016655d%3Aamzn1.sym.39f3f322-e4f4-475f-ab3a-16807016655d&crid=5IMMQB3K4VBB&cv_ct_cx=M3%2BBolt%2B%26%2BStandoff%2BSet&keywords=M3%2BBolt%2B%26%2BStandoff%2BSet&pd_rd_i=B0DX786YB1&pd_rd_r=498d1117-b5be-40ad-9003-f6a8e96769f8&pd_rd_w=0EYTl&pd_rd_wg=mwSG5&pf_rd_p=39f3f322-e4f4-475f-ab3a-16807016655d&pf_rd_r=68YA2C359E75TW51ZTM9&qid=1774821017&sbo=RZvfv%2F%2FHxDF%2BO5021pAnSA%3D%3D&sprefix=%2Caps%2C322&sr=1-4-ad3222ed-9545-4dc8-8dd8-6b2cb5278509-spons&aref=VwgEZ6Ok6i&sp_csd=d2lkZ2V0TmFtZT1zcF9zZWFyY2hfdGhlbWF0aWM&th=1)|
|Cabling|	HDMI|  Cables	Data & Video Interconnect|	£6.92|[amazon](https://www.amazon.co.uk/Certified-Adauxter-HDCP2-2-Compatible-Soundbar/dp/B098T3LSY3/ref=sr_1_3_sspa?crid=3NSRPQKKNSOLS&dib=eyJ2IjoiMSJ9.nBiJHTgOZ85ll-lCUW2jXBmVWrCa7gIIVDl6QJHAn17Bu1P4HdsbYJlJG7GmLuqhllNb7YwVxmoSDfQrzGYLeZXR2EZSEQwCXAluX4NcLwFcP1x4GoNXHfFOHLv1CaLmxBa1Oo3LI6y7DZMNVNPw7Lp-NgxH3Wz7gYJo2-fJrMYnsrgbbGV_Ddi0feDYp2d5SUm55IFjBmFf63yKs4dQZpGecGquNkWYiflFIHSQUcfXupms6x7K_C1SqHuvm2f_EMczaHnP7qw_kOIoJrbViZe1di2o7e_dFRnVC_6nVwU.DIafcwIcdrc3S9PycV64EnhFhwkmxLX8LYk_bnF_Nk0&dib_tag=se&keywords=HDMI&qid=1774821084&s=industrial&sprefix=hdmi%2B%2Cindustrial%2C356&sr=1-3-spons&aref=6PiCvsNz8I&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1)|
| **TOTAL** | | | **£71.74/$95,16** |

---

## 🛠️ Software & Firmware Stack
*   **MicroPython:** Polling RFID UIDs and controlling status LED indicators.
*   **Docker:** Containerization of monitoring services on the internal Micro-PC.
*   **MQTT/Serial:** Protocol for transmitting security status between the Console and the Cluster.

---

## 📁 Repository Contents
*   `/CAD_Models`: `.STL` and `.STEP` files for 3D printing or CNC cutting.
*   `/Firmware_Pico`: Source code for the Raspberry Pi Pico controller.
*   `/Assets`: Wiring diagrams and electrical schematics.
