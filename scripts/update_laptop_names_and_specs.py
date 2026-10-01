# -*- coding: utf-8 -*-
"""
Master script to update laptops-data.js with:
- Clean official model names (Brand + Product Line + Model + Gen, no CPU/RAM/SSD)
- legacyName field preserving the exact previous name
- shortSpecs: cpuFamily, generation, ramGb, storageGb, storageType, gpuType, isDedicatedGpu
- fullSpecs: 7 grouped categories (Performance, Memory & Storage, Display, Graphics, Connectivity & Ports, Battery & Build, Condition & Warranty)
"""

import json
import re
import os

DATA_JS_PATH = 'laptops-data.js'

with open(DATA_JS_PATH, 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'const\s+LAPTOPS_INVENTORY\s*=\s*(\[.*?\]);', text, re.DOTALL)
if not m:
    print("Could not match LAPTOPS_INVENTORY in laptops-data.js")
    exit(1)

laptops = json.loads(m.group(1))
print(f"Loaded {len(laptops)} laptops.")

# Full authoritative dictionary of model names and specs for all 69 laptops
# Keyed by laptop ID (1..69)
SPECS_DB = {
    1: {
        "name": "Lenovo ThinkPad T14 Gen 1",
        "brandName": "Lenovo",
        "series": "ThinkPad T14",
        "shortSpecs": {
            "cpuFamily": "Core i7",
            "generation": "10th Gen",
            "ramGb": 16,
            "storageGb": 512,
            "storageType": "NVMe SSD",
            "gpuType": "integrated",
            "isDedicatedGpu": False
        },
        "fullSpecs": {
            "performance": {
                "processor": "Intel Core i7-10610U vPro",
                "coresThreads": "4 Cores / 8 Threads",
                "clocks": "1.80 GHz Base, up to 4.90 GHz Boost",
                "cache": "8 MB Intel Smart Cache"
            },
            "memoryStorage": {
                "ramSize": "16 GB",
                "ramType": "DDR4",
                "ramSpeed": "3200 MHz",
                "ramSlots": "1 Soldered + 1 SO-DIMM Slot (Upgradable to 32GB)",
                "storageSize": "512 GB",
                "storageType": "NVMe SSD",
                "interface": "PCIe Gen3 x4 M.2 2280",
                "readSpeed": "Up to 3,500 MB/s (unverified)"
            },
            "display": {
                "size": "14.0\"",
                "resolution": "FHD (1920 x 1080)",
                "panelType": "IPS Anti-Glare",
                "refreshRate": "60 Hz",
                "touchAntiGlare": "Anti-Glare (Non-touch), 250 nits"
            },
            "graphics": {
                "gpuName": "Intel UHD Graphics 620",
                "type": "Integrated",
                "vram": "Shared System Memory"
            },
            "connectivityPorts": {
                "ports": "2x USB 3.2 Gen 1, 1x USB-C 3.2 Gen 1, 1x Thunderbolt 3, HDMI 1.4b, RJ-45 Ethernet, Headphone/mic combo, MicroSD",
                "wireless": "Intel Wi-Fi 6 AX201 (802.11ax) + Bluetooth 5.1"
            },
            "batteryBuild": {
                "battery": "50Wh Internal (Supports Rapid Charge 80% in 1 hr)",
                "weight": "1.55 kg (3.41 lbs)",
                "keyboard": "Spill-Resistant Backlit Keyboard with TrackPoint",
                "webcam": "720p HD with ThinkShutter Privacy Cover",
                "os": "Windows 11 Pro 64-bit Licensed"
            },
            "conditionWarranty": {
                "condition": "Like New (10/10) · Certified Refurbished",
                "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"
            }
        }
    },
    2: {
        "name": "Microsoft Surface Pro 7",
        "brandName": "Microsoft",
        "series": "Surface Pro 7",
        "shortSpecs": {
            "cpuFamily": "Core i5",
            "generation": "10th Gen",
            "ramGb": 8,
            "storageGb": 256,
            "storageType": "NVMe SSD",
            "gpuType": "integrated",
            "isDedicatedGpu": False
        },
        "fullSpecs": {
            "performance": {
                "processor": "Intel Core i5-1035G4",
                "coresThreads": "4 Cores / 8 Threads",
                "clocks": "1.10 GHz Base, up to 3.70 GHz Boost",
                "cache": "6 MB Intel Smart Cache"
            },
            "memoryStorage": {
                "ramSize": "8 GB",
                "ramType": "LPDDR4x",
                "ramSpeed": "3733 MHz",
                "ramSlots": "Soldered (Non-upgradable)",
                "storageSize": "256 GB",
                "storageType": "NVMe SSD",
                "interface": "PCIe NVMe M.2 2230",
                "readSpeed": "Up to 2,200 MB/s (unverified)"
            },
            "display": {
                "size": "12.3\"",
                "resolution": "2.7K (2736 x 1824)",
                "panelType": "PixelSense 3:2 Aspect Ratio",
                "refreshRate": "60 Hz",
                "touchAntiGlare": "10-Point Multi-Touch Glass with Surface Pen Support"
            },
            "graphics": {
                "gpuName": "Intel Iris Plus Graphics",
                "type": "Integrated",
                "vram": "Shared System Memory"
            },
            "connectivityPorts": {
                "ports": "1x USB-C 3.1 Gen 2, 1x USB-A 3.1 Gen 1, 3.5mm Headphone Jack, Surface Connect Port, MicroSDXC Card Reader",
                "wireless": "Wi-Fi 6 (802.11ax) + Bluetooth 5.0"
            },
            "batteryBuild": {
                "battery": "43.2Wh Battery (Up to 10.5 hours typical use)",
                "weight": "775 g (1.70 lbs) Tablet Body",
                "keyboard": "Surface Signature Type Cover (Detachable Backlit)",
                "webcam": "5.0MP Front 1080p with Windows Hello + 8.0MP Rear Autofocus",
                "os": "Windows 11 Pro 64-bit Licensed"
            },
            "conditionWarranty": {
                "condition": "Pristine Like New (10/10) · Open Box",
                "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"
            }
        }
    },
    3: {
        "name": "HP EliteBook 840 G9",
        "brandName": "HP",
        "series": "EliteBook 840 G9",
        "shortSpecs": {
            "cpuFamily": "Core i7",
            "generation": "12th Gen",
            "ramGb": 16,
            "storageGb": 512,
            "storageType": "NVMe SSD",
            "gpuType": "integrated",
            "isDedicatedGpu": False
        },
        "fullSpecs": {
            "performance": {
                "processor": "Intel Core i7-1255U",
                "coresThreads": "10 Cores (2P + 8E) / 12 Threads",
                "clocks": "1.70 GHz Base, up to 4.70 GHz Turbo Boost",
                "cache": "12 MB Intel Smart Cache"
            },
            "memoryStorage": {
                "ramSize": "16 GB",
                "ramType": "DDR5",
                "ramSpeed": "4800 MHz",
                "ramSlots": "2x SO-DIMM Slots (Dual-Channel Upgradable to 32GB/64GB)",
                "storageSize": "512 GB",
                "storageType": "NVMe SSD",
                "interface": "PCIe Gen4 x4 NVMe M.2 2280",
                "readSpeed": "Up to 4,800 MB/s"
            },
            "display": {
                "size": "14.0\"",
                "resolution": "WUXGA (1920 x 1200) 16:10",
                "panelType": "IPS Anti-Glare",
                "refreshRate": "60 Hz",
                "touchAntiGlare": "Anti-Glare 400 nits Low Power (Non-touch)"
            },
            "graphics": {
                "gpuName": "Intel Iris Xe Graphics",
                "type": "Integrated",
                "vram": "Shared System Memory"
            },
            "connectivityPorts": {
                "ports": "2x Thunderbolt 4 USB-C (40Gbps), 2x USB-A 3.2 Gen 1 (1 charging), 1x HDMI 2.0, Headphone/mic combo",
                "wireless": "Intel Wi-Fi 6E AX211 (802.11ax) + Bluetooth 5.3"
            },
            "batteryBuild": {
                "battery": "51Wh HP Long Life Fast Charge (50% in 30 mins)",
                "weight": "1.36 kg (2.99 lbs)",
                "keyboard": "HP Premium Spill-Resistant Backlit Keyboard",
                "webcam": "5MP Camera with HP Auto Frame & Dual Mics",
                "os": "Windows 11 Pro 64-bit Licensed"
            },
            "conditionWarranty": {
                "condition": "Grade A+ Like New · Verified Refurbished",
                "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"
            }
        }
    },
    4: {
        "name": "Lenovo ThinkPad X1 Yoga Gen 7",
        "brandName": "Lenovo",
        "series": "ThinkPad X1 Yoga",
        "shortSpecs": {
            "cpuFamily": "Core i5",
            "generation": "12th Gen",
            "ramGb": 16,
            "storageGb": 512,
            "storageType": "NVMe SSD",
            "gpuType": "integrated",
            "isDedicatedGpu": False
        },
        "fullSpecs": {
            "performance": {
                "processor": "Intel Core i5-1240P",
                "coresThreads": "12 Cores (4P + 8E) / 16 Threads",
                "clocks": "1.70 GHz Base, up to 4.40 GHz Turbo Boost",
                "cache": "12 MB Intel Smart Cache"
            },
            "memoryStorage": {
                "ramSize": "16 GB",
                "ramType": "LPDDR5",
                "ramSpeed": "5200 MHz",
                "ramSlots": "Soldered Dual-Channel (Non-upgradable)",
                "storageSize": "512 GB",
                "storageType": "NVMe SSD",
                "interface": "PCIe Gen4 x4 NVMe M.2 2280",
                "readSpeed": "Up to 5,000 MB/s"
            },
            "display": {
                "size": "14.0\"",
                "resolution": "WUXGA (1920 x 1200) 16:10",
                "panelType": "IPS Touchscreen 360° Convertible",
                "refreshRate": "60 Hz",
                "touchAntiGlare": "Anti-Reflection Touch with Garaged ThinkPad Pen Pro, 400 nits"
            },
            "graphics": {
                "gpuName": "Intel Iris Xe Graphics",
                "type": "Integrated",
                "vram": "Shared System Memory"
            },
            "connectivityPorts": {
                "ports": "2x Thunderbolt 4 USB-C, 2x USB-A 3.2 Gen 1, 1x HDMI 2.0b, Headphone/mic combo",
                "wireless": "Intel Wi-Fi 6E AX211 + Bluetooth 5.1"
            },
            "batteryBuild": {
                "battery": "57Wh Rapid Charge (80% in 60 mins)",
                "weight": "1.38 kg (3.04 lbs)",
                "keyboard": "Backlit Spill-Resistant Keyboard with TrackPoint",
                "webcam": "FHD 1080p IR Hybrid Camera with Privacy Shutter",
                "os": "Windows 11 Pro 64-bit Licensed"
            },
            "conditionWarranty": {
                "condition": "Pristine Like New (10/10) · Certified Refurbished",
                "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"
            }
        }
    },
    5: {
        "name": "Lenovo ThinkPad X13 Gen 1",
        "brandName": "Lenovo",
        "series": "ThinkPad X13",
        "shortSpecs": {
            "cpuFamily": "Core i5",
            "generation": "10th Gen",
            "ramGb": 8,
            "storageGb": 256,
            "storageType": "NVMe SSD",
            "gpuType": "integrated",
            "isDedicatedGpu": False
        },
        "fullSpecs": {
            "performance": {
                "processor": "Intel Core i5-10210U",
                "coresThreads": "4 Cores / 8 Threads",
                "clocks": "1.60 GHz Base, up to 4.20 GHz Boost",
                "cache": "6 MB Intel Smart Cache"
            },
            "memoryStorage": {
                "ramSize": "8 GB",
                "ramType": "DDR4",
                "ramSpeed": "2666 MHz",
                "ramSlots": "Soldered (Non-upgradable)",
                "storageSize": "256 GB",
                "storageType": "NVMe SSD",
                "interface": "PCIe Gen3 x4 M.2 2280",
                "readSpeed": "Up to 2,400 MB/s"
            },
            "display": {
                "size": "13.3\"",
                "resolution": "FHD (1920 x 1080)",
                "panelType": "IPS Anti-Glare",
                "refreshRate": "60 Hz",
                "touchAntiGlare": "Anti-Glare (Non-touch), 300 nits"
            },
            "graphics": {
                "gpuName": "Intel UHD Graphics",
                "type": "Integrated",
                "vram": "Shared System Memory"
            },
            "connectivityPorts": {
                "ports": "2x USB-A 3.2 Gen 1, 1x USB-C 3.2 Gen 1, 1x Thunderbolt 3, HDMI 1.4b, Headphone combo, MicroSD",
                "wireless": "Intel Wi-Fi 6 AX201 + Bluetooth 5.1"
            },
            "batteryBuild": {
                "battery": "48Wh Internal Battery",
                "weight": "1.22 kg (2.69 lbs)",
                "keyboard": "Spill-Resistant Backlit Keyboard with TrackPoint",
                "webcam": "720p HD with ThinkShutter",
                "os": "Windows 11 Pro 64-bit Licensed"
            },
            "conditionWarranty": {
                "condition": "Like New (10/10) · Certified Refurbished",
                "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"
            }
        }
    },
    6: {
        "name": "Lenovo ThinkPad T14 Gen 1",
        "brandName": "Lenovo",
        "series": "ThinkPad T14",
        "shortSpecs": {
            "cpuFamily": "Ryzen 7",
            "generation": "4000 Series",
            "ramGb": 16,
            "storageGb": 512,
            "storageType": "NVMe SSD",
            "gpuType": "integrated",
            "isDedicatedGpu": False
        },
        "fullSpecs": {
            "performance": {
                "processor": "AMD Ryzen 7 PRO 4750U",
                "coresThreads": "8 Cores / 16 Threads",
                "clocks": "1.70 GHz Base, up to 4.10 GHz Max Boost",
                "cache": "8 MB L3 Cache"
            },
            "memoryStorage": {
                "ramSize": "16 GB",
                "ramType": "DDR4",
                "ramSpeed": "3200 MHz",
                "ramSlots": "1 Soldered + 1 SO-DIMM Slot (Upgradable to 32GB)",
                "storageSize": "512 GB",
                "storageType": "NVMe SSD",
                "interface": "PCIe Gen3 x4 M.2 2280",
                "readSpeed": "Up to 3,400 MB/s"
            },
            "display": {
                "size": "14.0\"",
                "resolution": "FHD (1920 x 1080)",
                "panelType": "IPS Anti-Glare",
                "refreshRate": "60 Hz",
                "touchAntiGlare": "Anti-Glare (Non-touch), 250 nits"
            },
            "graphics": {
                "gpuName": "AMD Radeon Graphics Vega 7",
                "type": "Integrated",
                "vram": "Shared System Memory"
            },
            "connectivityPorts": {
                "ports": "2x USB-A 3.2 Gen 1, 2x USB-C 3.2 Gen 2 (DisplayPort/PD), HDMI 2.0, RJ-45 Gigabit Ethernet, Audio combo, MicroSD",
                "wireless": "Wi-Fi 6 (802.11ax) + Bluetooth 5.1"
            },
            "batteryBuild": {
                "battery": "50Wh Internal Rapid Charge Battery",
                "weight": "1.55 kg (3.41 lbs)",
                "keyboard": "Spill-Resistant Backlit Keyboard with TrackPoint",
                "webcam": "720p HD with ThinkShutter Privacy Cover",
                "os": "Windows 11 Pro 64-bit Licensed"
            },
            "conditionWarranty": {
                "condition": "Like New (10/10) · Certified Refurbished",
                "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"
            }
        }
    },
    7: {
        "name": "Lenovo ThinkPad 13 Gen 1",
        "brandName": "Lenovo",
        "series": "ThinkPad 13",
        "shortSpecs": {
            "cpuFamily": "Core i5",
            "generation": "6th Gen",
            "ramGb": 8,
            "storageGb": 256,
            "storageType": "NVMe SSD",
            "gpuType": "integrated",
            "isDedicatedGpu": False
        },
        "fullSpecs": {
            "performance": {
                "processor": "Intel Core i5-6200U",
                "coresThreads": "2 Cores / 4 Threads",
                "clocks": "2.30 GHz Base, up to 2.80 GHz Boost",
                "cache": "3 MB Intel Smart Cache"
            },
            "memoryStorage": {
                "ramSize": "8 GB",
                "ramType": "DDR4",
                "ramSpeed": "2133 MHz",
                "ramSlots": "2x SO-DIMM Slots (Upgradable to 16GB)",
                "storageSize": "256 GB",
                "storageType": "SATA M.2 SSD",
                "interface": "M.2 SATA III",
                "readSpeed": "Up to 550 MB/s"
            },
            "display": {
                "size": "13.3\"",
                "resolution": "FHD (1920 x 1080)",
                "panelType": "IPS Anti-Glare",
                "refreshRate": "60 Hz",
                "touchAntiGlare": "Anti-Glare (Non-touch)"
            },
            "graphics": {
                "gpuName": "Intel HD Graphics 520",
                "type": "Integrated",
                "vram": "Shared System Memory"
            },
            "connectivityPorts": {
                "ports": "3x USB 3.0, 1x USB-C, 1x HDMI, 4-in-1 Card Reader, Audio Jack",
                "wireless": "Intel Dual Band Wireless-AC 8260 + Bluetooth 4.2"
            },
            "batteryBuild": {
                "battery": "42Wh 3-Cell Li-Ion Battery",
                "weight": "1.44 kg (3.17 lbs)",
                "keyboard": "ThinkPad Precision Keyboard with TrackPoint",
                "webcam": "720p HD Webcam",
                "os": "Windows 10 Pro 64-bit Licensed"
            },
            "conditionWarranty": {
                "condition": "Clean Condition (9/10) · Fully Tested",
                "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"
            }
        }
    },
    8: {
        "name": "Dell XPS 15 9550",
        "brandName": "Dell",
        "series": "XPS 15",
        "shortSpecs": {
            "cpuFamily": "Core i7",
            "generation": "6th Gen",
            "ramGb": 16,
            "storageGb": 512,
            "storageType": "NVMe SSD",
            "gpuType": "discrete",
            "isDedicatedGpu": True
        },
        "fullSpecs": {
            "performance": {
                "processor": "Intel Core i7-6700HQ",
                "coresThreads": "4 Cores / 8 Threads (45W High-Performance)",
                "clocks": "2.60 GHz Base, up to 3.50 GHz Turbo",
                "cache": "6 MB Intel Smart Cache"
            },
            "memoryStorage": {
                "ramSize": "16 GB",
                "ramType": "DDR4",
                "ramSpeed": "2133 MHz",
                "ramSlots": "2x SO-DIMM Slots (Upgradable to 32GB)",
                "storageSize": "512 GB",
                "storageType": "NVMe SSD",
                "interface": "PCIe Gen3 x4 M.2 2280",
                "readSpeed": "Up to 2,200 MB/s"
            },
            "display": {
                "size": "15.6\"",
                "resolution": "4K UHD (3840 x 2160) InfinityEdge Touch / FHD IPS",
                "panelType": "IGZO IPS UltraSharp",
                "refreshRate": "60 Hz",
                "touchAntiGlare": "100% AdobeRGB Touchscreen with Corning Gorilla Glass NBT"
            },
            "graphics": {
                "gpuName": "NVIDIA GeForce GTX 960M",
                "type": "Dedicated",
                "vram": "2 GB GDDR5 Dedicated"
            },
            "connectivityPorts": {
                "ports": "1x Thunderbolt 3 (USB-C), 2x USB 3.0 with PowerShare, 1x HDMI, Full-size SD Card Reader, Headphone Jack",
                "wireless": "Dell Wireless 1830 802.11ac + Bluetooth 4.1"
            },
            "batteryBuild": {
                "battery": "84Wh / 56Wh Lithium-Ion Battery",
                "weight": "2.00 kg (4.4 lbs)",
                "keyboard": "Full-size Backlit Keyboard with Carbon Fiber Palmrest",
                "webcam": "Widescreen HD (720p) Webcam with Dual Array Digital Microphones",
                "os": "Windows 11 Pro 64-bit Licensed"
            },
            "conditionWarranty": {
                "condition": "Excellent Condition (9.5/10) · Creator Ready",
                "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"
            }
        }
    },
    9: {
        "name": "Dell Latitude 5310",
        "brandName": "Dell",
        "series": "Latitude 5310",
        "shortSpecs": {
            "cpuFamily": "Core i5",
            "generation": "10th Gen",
            "ramGb": 8,
            "storageGb": 256,
            "storageType": "NVMe SSD",
            "gpuType": "integrated",
            "isDedicatedGpu": False
        },
        "fullSpecs": {
            "performance": {
                "processor": "Intel Core i5-10210U",
                "coresThreads": "4 Cores / 8 Threads",
                "clocks": "1.60 GHz Base, up to 4.20 GHz Boost",
                "cache": "6 MB Intel Smart Cache"
            },
            "memoryStorage": {
                "ramSize": "8 GB",
                "ramType": "DDR4",
                "ramSpeed": "2666 MHz",
                "ramSlots": "2x SO-DIMM Slots (Upgradable to 32GB)",
                "storageSize": "256 GB",
                "storageType": "NVMe SSD",
                "interface": "PCIe Gen3 x4 M.2 2280",
                "readSpeed": "Up to 2,400 MB/s"
            },
            "display": {
                "size": "13.3\"",
                "resolution": "FHD (1920 x 1080)",
                "panelType": "WVA IPS Anti-Glare",
                "refreshRate": "60 Hz",
                "touchAntiGlare": "Anti-Glare (Non-touch), 300 nits"
            },
            "graphics": {
                "gpuName": "Intel UHD Graphics",
                "type": "Integrated",
                "vram": "Shared System Memory"
            },
            "connectivityPorts": {
                "ports": "1x USB-C 3.2 Gen 2 (DisplayPort/PD), 2x USB-A 3.2 Gen 1 (1 with PowerShare), 1x HDMI 1.4b, RJ-45, MicroSD, Audio Jack",
                "wireless": "Intel Wi-Fi 6 AX201 (802.11ax) + Bluetooth 5.1"
            },
            "batteryBuild": {
                "battery": "42Wh / 51Wh ExpressCharge Capable",
                "weight": "1.24 kg (2.73 lbs)",
                "keyboard": "Backlit Spill-Resistant Keyboard",
                "webcam": "HD RGB Camera with Privacy Shutter",
                "os": "Windows 11 Pro 64-bit Licensed"
            },
            "conditionWarranty": {
                "condition": "Grade A+ Like New · Enterprise Refurbished",
                "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"
            }
        }
    },
    10: {
        "name": "HP EliteBook x360 1030 G8",
        "brandName": "HP",
        "series": "EliteBook x360 1030",
        "shortSpecs": {
            "cpuFamily": "Core i7",
            "generation": "11th Gen",
            "ramGb": 16,
            "storageGb": 512,
            "storageType": "NVMe SSD",
            "gpuType": "integrated",
            "isDedicatedGpu": False
        },
        "fullSpecs": {
            "performance": {
                "processor": "Intel Core i7-1165G7",
                "coresThreads": "4 Cores / 8 Threads",
                "clocks": "2.80 GHz Base, up to 4.70 GHz Turbo Boost",
                "cache": "12 MB Intel Smart Cache"
            },
            "memoryStorage": {
                "ramSize": "16 GB",
                "ramType": "LPDDR4x",
                "ramSpeed": "4266 MHz",
                "ramSlots": "Soldered Dual-Channel (Non-upgradable)",
                "storageSize": "512 GB",
                "storageType": "NVMe SSD",
                "interface": "PCIe Gen3 x4 NVMe M.2 TLC",
                "readSpeed": "Up to 3,500 MB/s"
            },
            "display": {
                "size": "13.3\"",
                "resolution": "FHD (1920 x 1080)",
                "panelType": "IPS BrightView Touchscreen 360°",
                "refreshRate": "60 Hz",
                "touchAntiGlare": "Corning Gorilla Glass 5 Touch with Pen Support, 400 nits"
            },
            "graphics": {
                "gpuName": "Intel Iris Xe Graphics",
                "type": "Integrated",
                "vram": "Shared System Memory"
            },
            "connectivityPorts": {
                "ports": "2x Thunderbolt 4 USB-C (Power Delivery, DisplayPort 1.4), 2x USB-A 3.2 Gen 1 (1 charging), 1x HDMI 2.0, Headphone/mic combo",
                "wireless": "Intel Wi-Fi 6 AX201 (2x2) + Bluetooth 5.0"
            },
            "batteryBuild": {
                "battery": "54Wh HP Long Life Fast Charge (50% in 30 mins)",
                "weight": "1.21 kg (2.68 lbs) CNC Aluminum",
                "keyboard": "HP Premium Quiet Backlit Spill-Resistant Keyboard",
                "webcam": "720p HD Camera with IR Facial Recognition Windows Hello",
                "os": "Windows 11 Pro 64-bit Licensed"
            },
            "conditionWarranty": {
                "condition": "Pristine Like New (10/10) · Executive 2-in-1",
                "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"
            }
        }
    }
}

print(f"Defined prototype specs for IDs 1-10.")
