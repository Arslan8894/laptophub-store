# -*- coding: utf-8 -*-
"""
Generator script for all 69 laptops in laptops-data.js.
Produces clean official model names, legacyName, shortSpecs, and 7-category fullSpecs.
"""

import json
import re
import sys

DATA_JS_PATH = 'laptops-data.js'

with open(DATA_JS_PATH, 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'const\s+LAPTOPS_INVENTORY\s*=\s*(\[.*?\]);', text, re.DOTALL)
if not m:
    print("Could not match LAPTOPS_INVENTORY")
    sys.exit(1)

existing_laptops = json.loads(m.group(1))
print(f"Loaded {len(existing_laptops)} existing laptops from laptops-data.js")

# Master database of clean names and comprehensive specs for all 69 models
MODELS = {
    1: {
        "name": "Lenovo ThinkPad T14 Gen 1",
        "brandName": "Lenovo",
        "series": "ThinkPad T14",
        "shortSpecs": {"cpuFamily": "Core i7", "generation": "10th Gen", "ramGb": 16, "storageGb": 512, "storageType": "NVMe SSD", "gpuType": "integrated", "isDedicatedGpu": False},
        "fullSpecs": {
            "performance": {"processor": "Intel Core i7-10610U vPro", "coresThreads": "4 Cores / 8 Threads", "clocks": "1.80 GHz Base, up to 4.90 GHz Boost", "cache": "8 MB Intel Smart Cache"},
            "memoryStorage": {"ramSize": "16 GB", "ramType": "DDR4", "ramSpeed": "3200 MHz", "ramSlots": "1 Soldered + 1 SO-DIMM (Upgradable)", "storageSize": "512 GB", "storageType": "NVMe SSD", "interface": "PCIe Gen3 x4 M.2 2280", "readSpeed": "Up to 3,500 MB/s (unverified)"},
            "display": {"size": "14.0\"", "resolution": "FHD (1920 x 1080)", "panelType": "IPS Anti-Glare", "refreshRate": "60 Hz", "touchAntiGlare": "Anti-Glare (Non-touch), 250 nits"},
            "graphics": {"gpuName": "Intel UHD Graphics 620", "type": "Integrated", "vram": "Shared System Memory"},
            "connectivityPorts": {"ports": "2x USB 3.2 Gen 1, 1x USB-C 3.2 Gen 1, 1x Thunderbolt 3, HDMI 1.4b, RJ-45 Ethernet, Headphone/mic combo, MicroSD", "wireless": "Intel Wi-Fi 6 AX201 (802.11ax) + Bluetooth 5.1"},
            "batteryBuild": {"battery": "50Wh Internal (Rapid Charge)", "weight": "1.55 kg (3.41 lbs)", "keyboard": "Spill-Resistant Backlit Keyboard with TrackPoint", "webcam": "720p HD with ThinkShutter", "os": "Windows 11 Pro 64-bit Licensed"},
            "conditionWarranty": {"condition": "Like New (10/10) · Certified Refurbished", "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"}
        }
    },
    2: {
        "name": "Microsoft Surface Pro 7",
        "brandName": "Microsoft",
        "series": "Surface Pro 7",
        "shortSpecs": {"cpuFamily": "Core i5", "generation": "10th Gen", "ramGb": 8, "storageGb": 256, "storageType": "NVMe SSD", "gpuType": "integrated", "isDedicatedGpu": False},
        "fullSpecs": {
            "performance": {"processor": "Intel Core i5-1035G4", "coresThreads": "4 Cores / 8 Threads", "clocks": "1.10 GHz Base, up to 3.70 GHz Boost", "cache": "6 MB Intel Smart Cache"},
            "memoryStorage": {"ramSize": "8 GB", "ramType": "LPDDR4x", "ramSpeed": "3733 MHz", "ramSlots": "Soldered (Non-upgradable)", "storageSize": "256 GB", "storageType": "NVMe SSD", "interface": "PCIe NVMe M.2 2230", "readSpeed": "Up to 2,200 MB/s (unverified)"},
            "display": {"size": "12.3\"", "resolution": "2.7K (2736 x 1824)", "panelType": "PixelSense 3:2 Aspect Ratio", "refreshRate": "60 Hz", "touchAntiGlare": "10-Point Multi-Touch Glass with Surface Pen Support"},
            "graphics": {"gpuName": "Intel Iris Plus Graphics", "type": "Integrated", "vram": "Shared System Memory"},
            "connectivityPorts": {"ports": "1x USB-C 3.1, 1x USB-A 3.1, 3.5mm Headphone Jack, Surface Connect Port, MicroSDXC Card Reader", "wireless": "Wi-Fi 6 (802.11ax) + Bluetooth 5.0"},
            "batteryBuild": {"battery": "43.2Wh Battery (Up to 10.5 hours use)", "weight": "775 g (1.70 lbs) Tablet Body", "keyboard": "Surface Signature Type Cover (Detachable Backlit)", "webcam": "5.0MP Front 1080p with Windows Hello + 8.0MP Rear", "os": "Windows 11 Pro 64-bit Licensed"},
            "conditionWarranty": {"condition": "Pristine Like New (10/10) · Open Box", "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"}
        }
    },
    3: {
        "name": "HP EliteBook 840 G9",
        "brandName": "HP",
        "series": "EliteBook 840 G9",
        "shortSpecs": {"cpuFamily": "Core i7", "generation": "12th Gen", "ramGb": 16, "storageGb": 512, "storageType": "NVMe SSD", "gpuType": "integrated", "isDedicatedGpu": False},
        "fullSpecs": {
            "performance": {"processor": "Intel Core i7-1255U", "coresThreads": "10 Cores (2P + 8E) / 12 Threads", "clocks": "1.70 GHz Base, up to 4.70 GHz Turbo", "cache": "12 MB Intel Smart Cache"},
            "memoryStorage": {"ramSize": "16 GB", "ramType": "DDR5", "ramSpeed": "4800 MHz", "ramSlots": "2x SO-DIMM Slots (Upgradable)", "storageSize": "512 GB", "storageType": "NVMe SSD", "interface": "PCIe Gen4 x4 NVMe M.2 2280", "readSpeed": "Up to 4,800 MB/s"},
            "display": {"size": "14.0\"", "resolution": "WUXGA (1920 x 1200) 16:10", "panelType": "IPS Anti-Glare", "refreshRate": "60 Hz", "touchAntiGlare": "Anti-Glare 400 nits Low Power"},
            "graphics": {"gpuName": "Intel Iris Xe Graphics", "type": "Integrated", "vram": "Shared System Memory"},
            "connectivityPorts": {"ports": "2x Thunderbolt 4 USB-C, 2x USB-A 3.2 Gen 1, 1x HDMI 2.0, Headphone/mic combo", "wireless": "Intel Wi-Fi 6E AX211 + Bluetooth 5.3"},
            "batteryBuild": {"battery": "51Wh HP Long Life Fast Charge (50% in 30 mins)", "weight": "1.36 kg (2.99 lbs)", "keyboard": "HP Premium Spill-Resistant Backlit Keyboard", "webcam": "5MP Camera with HP Auto Frame & Dual Mics", "os": "Windows 11 Pro 64-bit Licensed"},
            "conditionWarranty": {"condition": "Grade A+ Like New · Verified Refurbished", "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"}
        }
    },
    4: {
        "name": "Lenovo ThinkPad X1 Yoga Gen 7",
        "brandName": "Lenovo",
        "series": "ThinkPad X1 Yoga",
        "shortSpecs": {"cpuFamily": "Core i5", "generation": "12th Gen", "ramGb": 16, "storageGb": 512, "storageType": "NVMe SSD", "gpuType": "integrated", "isDedicatedGpu": False},
        "fullSpecs": {
            "performance": {"processor": "Intel Core i5-1240P", "coresThreads": "12 Cores (4P + 8E) / 16 Threads", "clocks": "1.70 GHz Base, up to 4.40 GHz Boost", "cache": "12 MB Intel Smart Cache"},
            "memoryStorage": {"ramSize": "16 GB", "ramType": "LPDDR5", "ramSpeed": "5200 MHz", "ramSlots": "Soldered Dual-Channel (Non-upgradable)", "storageSize": "512 GB", "storageType": "NVMe SSD", "interface": "PCIe Gen4 x4 NVMe M.2 2280", "readSpeed": "Up to 5,000 MB/s"},
            "display": {"size": "14.0\"", "resolution": "WUXGA (1920 x 1200) 16:10", "panelType": "IPS Touchscreen 360°", "refreshRate": "60 Hz", "touchAntiGlare": "Anti-Reflection Touch with ThinkPad Pen Pro, 400 nits"},
            "graphics": {"gpuName": "Intel Iris Xe Graphics", "type": "Integrated", "vram": "Shared System Memory"},
            "connectivityPorts": {"ports": "2x Thunderbolt 4 USB-C, 2x USB-A 3.2 Gen 1, 1x HDMI 2.0b, Headphone/mic combo", "wireless": "Intel Wi-Fi 6E AX211 + Bluetooth 5.1"},
            "batteryBuild": {"battery": "57Wh Rapid Charge (80% in 60 mins)", "weight": "1.38 kg (3.04 lbs)", "keyboard": "Backlit Spill-Resistant Keyboard with TrackPoint", "webcam": "FHD 1080p IR Camera with Privacy Shutter", "os": "Windows 11 Pro 64-bit Licensed"},
            "conditionWarranty": {"condition": "Pristine Like New (10/10) · Certified Refurbished", "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"}
        }
    },
    5: {
        "name": "Lenovo ThinkPad X13 Gen 1",
        "brandName": "Lenovo",
        "series": "ThinkPad X13",
        "shortSpecs": {"cpuFamily": "Core i5", "generation": "10th Gen", "ramGb": 8, "storageGb": 256, "storageType": "NVMe SSD", "gpuType": "integrated", "isDedicatedGpu": False},
        "fullSpecs": {
            "performance": {"processor": "Intel Core i5-10210U", "coresThreads": "4 Cores / 8 Threads", "clocks": "1.60 GHz Base, up to 4.20 GHz Boost", "cache": "6 MB Intel Smart Cache"},
            "memoryStorage": {"ramSize": "8 GB", "ramType": "DDR4", "ramSpeed": "2666 MHz", "ramSlots": "Soldered (Non-upgradable)", "storageSize": "256 GB", "storageType": "NVMe SSD", "interface": "PCIe Gen3 x4 M.2 2280", "readSpeed": "Up to 2,400 MB/s"},
            "display": {"size": "13.3\"", "resolution": "FHD (1920 x 1080)", "panelType": "IPS Anti-Glare", "refreshRate": "60 Hz", "touchAntiGlare": "Anti-Glare (Non-touch), 300 nits"},
            "graphics": {"gpuName": "Intel UHD Graphics", "type": "Integrated", "vram": "Shared System Memory"},
            "connectivityPorts": {"ports": "2x USB-A 3.2 Gen 1, 1x USB-C 3.2 Gen 1, 1x Thunderbolt 3, HDMI 1.4b, Headphone combo, MicroSD", "wireless": "Intel Wi-Fi 6 AX201 + Bluetooth 5.1"},
            "batteryBuild": {"battery": "48Wh Internal Battery", "weight": "1.22 kg (2.69 lbs)", "keyboard": "Spill-Resistant Backlit Keyboard with TrackPoint", "webcam": "720p HD with ThinkShutter", "os": "Windows 11 Pro 64-bit Licensed"},
            "conditionWarranty": {"condition": "Like New (10/10) · Certified Refurbished", "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"}
        }
    },
    6: {
        "name": "Lenovo ThinkPad T14 Gen 1",
        "brandName": "Lenovo",
        "series": "ThinkPad T14",
        "shortSpecs": {"cpuFamily": "Ryzen 7", "generation": "4000 Series", "ramGb": 16, "storageGb": 512, "storageType": "NVMe SSD", "gpuType": "integrated", "isDedicatedGpu": False},
        "fullSpecs": {
            "performance": {"processor": "AMD Ryzen 7 PRO 4750U", "coresThreads": "8 Cores / 16 Threads", "clocks": "1.70 GHz Base, up to 4.10 GHz Boost", "cache": "8 MB L3 Cache"},
            "memoryStorage": {"ramSize": "16 GB", "ramType": "DDR4", "ramSpeed": "3200 MHz", "ramSlots": "1 Soldered + 1 SO-DIMM Slot (Upgradable)", "storageSize": "512 GB", "storageType": "NVMe SSD", "interface": "PCIe Gen3 x4 M.2 2280", "readSpeed": "Up to 3,400 MB/s"},
            "display": {"size": "14.0\"", "resolution": "FHD (1920 x 1080)", "panelType": "IPS Anti-Glare", "refreshRate": "60 Hz", "touchAntiGlare": "Anti-Glare (Non-touch), 250 nits"},
            "graphics": {"gpuName": "AMD Radeon Graphics Vega 7", "type": "Integrated", "vram": "Shared System Memory"},
            "connectivityPorts": {"ports": "2x USB-A 3.2 Gen 1, 2x USB-C 3.2 Gen 2 (DisplayPort/PD), HDMI 2.0, RJ-45 Gigabit, Audio combo, MicroSD", "wireless": "Wi-Fi 6 (802.11ax) + Bluetooth 5.1"},
            "batteryBuild": {"battery": "50Wh Internal Rapid Charge Battery", "weight": "1.55 kg (3.41 lbs)", "keyboard": "Spill-Resistant Backlit Keyboard with TrackPoint", "webcam": "720p HD with ThinkShutter Privacy Cover", "os": "Windows 11 Pro 64-bit Licensed"},
            "conditionWarranty": {"condition": "Like New (10/10) · Certified Refurbished", "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"}
        }
    },
    7: {
        "name": "Lenovo ThinkPad 13 Gen 1",
        "brandName": "Lenovo",
        "series": "ThinkPad 13",
        "shortSpecs": {"cpuFamily": "Core i5", "generation": "6th Gen", "ramGb": 8, "storageGb": 256, "storageType": "SATA SSD", "gpuType": "integrated", "isDedicatedGpu": False},
        "fullSpecs": {
            "performance": {"processor": "Intel Core i5-6200U", "coresThreads": "2 Cores / 4 Threads", "clocks": "2.30 GHz Base, up to 2.80 GHz Boost", "cache": "3 MB Intel Smart Cache"},
            "memoryStorage": {"ramSize": "8 GB", "ramType": "DDR4", "ramSpeed": "2133 MHz", "ramSlots": "2x SO-DIMM Slots (Upgradable)", "storageSize": "256 GB", "storageType": "SATA M.2 SSD", "interface": "M.2 SATA III", "readSpeed": "Up to 550 MB/s"},
            "display": {"size": "13.3\"", "resolution": "FHD (1920 x 1080)", "panelType": "IPS Anti-Glare", "refreshRate": "60 Hz", "touchAntiGlare": "Anti-Glare (Non-touch)"},
            "graphics": {"gpuName": "Intel HD Graphics 520", "type": "Integrated", "vram": "Shared System Memory"},
            "connectivityPorts": {"ports": "3x USB 3.0, 1x USB-C, 1x HDMI, 4-in-1 Card Reader, Audio Jack", "wireless": "Intel Dual Band Wireless-AC 8260 + Bluetooth 4.2"},
            "batteryBuild": {"battery": "42Wh 3-Cell Li-Ion Battery", "weight": "1.44 kg (3.17 lbs)", "keyboard": "ThinkPad Precision Keyboard with TrackPoint", "webcam": "720p HD Webcam", "os": "Windows 10 Pro 64-bit Licensed"},
            "conditionWarranty": {"condition": "Clean Condition (9/10) · Fully Tested", "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"}
        }
    },
    8: {
        "name": "Dell XPS 15 9550",
        "brandName": "Dell",
        "series": "XPS 15",
        "shortSpecs": {"cpuFamily": "Core i7", "generation": "6th Gen", "ramGb": 16, "storageGb": 512, "storageType": "NVMe SSD", "gpuType": "discrete", "isDedicatedGpu": True},
        "fullSpecs": {
            "performance": {"processor": "Intel Core i7-6700HQ (45W)", "coresThreads": "4 Cores / 8 Threads", "clocks": "2.60 GHz Base, up to 3.50 GHz Turbo", "cache": "6 MB Intel Smart Cache"},
            "memoryStorage": {"ramSize": "16 GB", "ramType": "DDR4", "ramSpeed": "2133 MHz", "ramSlots": "2x SO-DIMM Slots (Upgradable)", "storageSize": "512 GB", "storageType": "NVMe SSD", "interface": "PCIe Gen3 x4 M.2 2280", "readSpeed": "Up to 2,200 MB/s"},
            "display": {"size": "15.6\"", "resolution": "4K UHD (3840 x 2160) Touch / FHD", "panelType": "IGZO IPS UltraSharp", "refreshRate": "60 Hz", "touchAntiGlare": "Touchscreen / InfinityEdge, 400 nits"},
            "graphics": {"gpuName": "NVIDIA GeForce GTX 960M", "type": "Dedicated", "vram": "2 GB GDDR5 Dedicated"},
            "connectivityPorts": {"ports": "1x Thunderbolt 3 (USB-C), 2x USB 3.0 with PowerShare, 1x HDMI, SD Card Slot, Audio jack", "wireless": "Dell Wireless 1830 802.11ac + Bluetooth 4.1"},
            "batteryBuild": {"battery": "84Wh / 56Wh Lithium-Ion Battery", "weight": "2.00 kg (4.4 lbs)", "keyboard": "Full-size Backlit Keyboard with Carbon Fiber Palmrest", "webcam": "Widescreen HD (720p) Webcam with Dual Array Digital Microphones", "os": "Windows 11 Pro 64-bit Licensed"},
            "conditionWarranty": {"condition": "Excellent Condition (9.5/10) · Creator Ready", "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"}
        }
    },
    9: {
        "name": "Dell Latitude 5310",
        "brandName": "Dell",
        "series": "Latitude 5310",
        "shortSpecs": {"cpuFamily": "Core i5", "generation": "10th Gen", "ramGb": 8, "storageGb": 256, "storageType": "NVMe SSD", "gpuType": "integrated", "isDedicatedGpu": False},
        "fullSpecs": {
            "performance": {"processor": "Intel Core i5-10210U", "coresThreads": "4 Cores / 8 Threads", "clocks": "1.60 GHz Base, up to 4.20 GHz Boost", "cache": "6 MB Intel Smart Cache"},
            "memoryStorage": {"ramSize": "8 GB", "ramType": "DDR4", "ramSpeed": "2666 MHz", "ramSlots": "2x SO-DIMM Slots (Upgradable to 32GB)", "storageSize": "256 GB", "storageType": "NVMe SSD", "interface": "PCIe Gen3 x4 M.2 2280", "readSpeed": "Up to 2,400 MB/s"},
            "display": {"size": "13.3\"", "resolution": "FHD (1920 x 1080)", "panelType": "WVA IPS Anti-Glare", "refreshRate": "60 Hz", "touchAntiGlare": "Anti-Glare (Non-touch), 300 nits"},
            "graphics": {"gpuName": "Intel UHD Graphics", "type": "Integrated", "vram": "Shared System Memory"},
            "connectivityPorts": {"ports": "1x USB-C 3.2 Gen 2 (DisplayPort/PD), 2x USB-A 3.2 Gen 1 (1 with PowerShare), 1x HDMI 1.4b, RJ-45, MicroSD, Audio Jack", "wireless": "Intel Wi-Fi 6 AX201 (802.11ax) + Bluetooth 5.1"},
            "batteryBuild": {"battery": "42Wh / 51Wh ExpressCharge Capable", "weight": "1.24 kg (2.73 lbs)", "keyboard": "Backlit Spill-Resistant Keyboard", "webcam": "HD RGB Camera with Privacy Shutter", "os": "Windows 11 Pro 64-bit Licensed"},
            "conditionWarranty": {"condition": "Grade A+ Like New · Enterprise Refurbished", "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"}
        }
    },
    10: {
        "name": "HP EliteBook x360 1030 G8",
        "brandName": "HP",
        "series": "EliteBook x360 1030",
        "shortSpecs": {"cpuFamily": "Core i7", "generation": "11th Gen", "ramGb": 16, "storageGb": 512, "storageType": "NVMe SSD", "gpuType": "integrated", "isDedicatedGpu": False},
        "fullSpecs": {
            "performance": {"processor": "Intel Core i7-1165G7", "coresThreads": "4 Cores / 8 Threads", "clocks": "2.80 GHz Base, up to 4.70 GHz Turbo", "cache": "12 MB Intel Smart Cache"},
            "memoryStorage": {"ramSize": "16 GB", "ramType": "LPDDR4x", "ramSpeed": "4266 MHz", "ramSlots": "Soldered Dual-Channel (Non-upgradable)", "storageSize": "512 GB", "storageType": "NVMe SSD", "interface": "PCIe Gen3 x4 NVMe M.2 TLC", "readSpeed": "Up to 3,500 MB/s"},
            "display": {"size": "13.3\"", "resolution": "FHD (1920 x 1080)", "panelType": "IPS BrightView Touchscreen 360°", "refreshRate": "60 Hz", "touchAntiGlare": "Corning Gorilla Glass 5 Touch with Pen Support, 400 nits"},
            "graphics": {"gpuName": "Intel Iris Xe Graphics", "type": "Integrated", "vram": "Shared System Memory"},
            "connectivityPorts": {"ports": "2x Thunderbolt 4 USB-C (Power Delivery, DisplayPort 1.4), 2x USB-A 3.2 Gen 1 (1 charging), 1x HDMI 2.0, Headphone/mic combo", "wireless": "Intel Wi-Fi 6 AX201 (2x2) + Bluetooth 5.0"},
            "batteryBuild": {"battery": "54Wh HP Long Life Fast Charge (50% in 30 mins)", "weight": "1.21 kg (2.68 lbs) CNC Aluminum", "keyboard": "HP Premium Quiet Backlit Spill-Resistant Keyboard", "webcam": "720p HD Camera with IR Facial Recognition Windows Hello", "os": "Windows 11 Pro 64-bit Licensed"},
            "conditionWarranty": {"condition": "Pristine Like New (10/10) · Executive 2-in-1", "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"}
        }
    },
    11: {
        "name": "Dell Latitude 5320",
        "brandName": "Dell",
        "series": "Latitude 5320",
        "shortSpecs": {"cpuFamily": "Core i5", "generation": "11th Gen", "ramGb": 16, "storageGb": 256, "storageType": "NVMe SSD", "gpuType": "integrated", "isDedicatedGpu": False},
        "fullSpecs": {
            "performance": {"processor": "Intel Core i5-1145G7 vPro", "coresThreads": "4 Cores / 8 Threads", "clocks": "2.60 GHz Base, up to 4.40 GHz Turbo", "cache": "8 MB Intel Smart Cache"},
            "memoryStorage": {"ramSize": "16 GB", "ramType": "DDR4", "ramSpeed": "3200 MHz", "ramSlots": "Soldered Dual-Channel (Non-upgradable)", "storageSize": "256 GB", "storageType": "NVMe SSD", "interface": "PCIe Gen3 x4 M.2 2280", "readSpeed": "Up to 2,400 MB/s"},
            "display": {"size": "13.3\"", "resolution": "FHD (1920 x 1080)", "panelType": "IPS Anti-Glare", "refreshRate": "60 Hz", "touchAntiGlare": "Anti-Glare (Non-touch), 300 nits"},
            "graphics": {"gpuName": "Intel Iris Xe Graphics", "type": "Integrated", "vram": "Shared System Memory"},
            "connectivityPorts": {"ports": "2x Thunderbolt 4 USB-C (Power Delivery/DisplayPort), 2x USB-A 3.2 Gen 1 (1 with PowerShare), 1x HDMI 2.0, MicroSD, Audio Jack", "wireless": "Intel Wi-Fi 6 AX201 + Bluetooth 5.1"},
            "batteryBuild": {"battery": "63Wh / 42Wh ExpressCharge Capable", "weight": "1.20 kg (2.65 lbs)", "keyboard": "Backlit Spill-Resistant Keyboard", "webcam": "720p HD with Camera Shutter & IR Hello", "os": "Windows 11 Pro 64-bit Licensed"},
            "conditionWarranty": {"condition": "Grade A+ Like New · Corporate Clean", "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"}
        }
    },
    12: {
        "name": "HP EliteBook x360 1030 G2",
        "brandName": "HP",
        "series": "EliteBook x360 1030",
        "shortSpecs": {"cpuFamily": "Core i5", "generation": "7th Gen", "ramGb": 8, "storageGb": 256, "storageType": "NVMe SSD", "gpuType": "integrated", "isDedicatedGpu": False},
        "fullSpecs": {
            "performance": {"processor": "Intel Core i5-7200U", "coresThreads": "2 Cores / 4 Threads", "clocks": "2.50 GHz Base, up to 3.10 GHz Boost", "cache": "3 MB Intel Smart Cache"},
            "memoryStorage": {"ramSize": "8 GB", "ramType": "DDR4", "ramSpeed": "2133 MHz", "ramSlots": "Soldered Dual-Channel (Non-upgradable)", "storageSize": "256 GB", "storageType": "NVMe SSD", "interface": "PCIe Gen3 x4 M.2 2280", "readSpeed": "Up to 1,800 MB/s"},
            "display": {"size": "13.3\"", "resolution": "FHD (1920 x 1080)", "panelType": "IPS Touchscreen 360°", "refreshRate": "60 Hz", "touchAntiGlare": "Corning Gorilla Glass Touch Convertible"},
            "graphics": {"gpuName": "Intel HD Graphics 620", "type": "Integrated", "vram": "Shared System Memory"},
            "connectivityPorts": {"ports": "1x USB-C (Thunderbolt), 2x USB 3.1 Gen 1 (1 charging), 1x HDMI 1.4, MicroSD, Audio Jack", "wireless": "Intel 802.11a/b/g/n/ac (2x2) + Bluetooth 4.2"},
            "batteryBuild": {"battery": "57Wh HP Long Life 3-cell Li-ion", "weight": "1.28 kg (2.82 lbs) CNC Aluminum", "keyboard": "HP Premium Collaboration Backlit Keyboard", "webcam": "720p HD with IR Camera for Windows Hello", "os": "Windows 10/11 Pro 64-bit Licensed"},
            "conditionWarranty": {"condition": "Like New (10/10) · Certified Refurbished", "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"}
        }
    },
    13: {
        "name": "Dell Latitude 5430",
        "brandName": "Dell",
        "series": "Latitude 5430",
        "shortSpecs": {"cpuFamily": "Core i5", "generation": "12th Gen", "ramGb": 16, "storageGb": 512, "storageType": "NVMe SSD", "gpuType": "integrated", "isDedicatedGpu": False},
        "fullSpecs": {
            "performance": {"processor": "Intel Core i5-1235U", "coresThreads": "10 Cores (2P + 8E) / 12 Threads", "clocks": "1.30 GHz Base, up to 4.40 GHz Turbo", "cache": "12 MB Intel Smart Cache"},
            "memoryStorage": {"ramSize": "16 GB", "ramType": "DDR4", "ramSpeed": "3200 MHz", "ramSlots": "2x SO-DIMM Slots (Upgradable to 64GB)", "storageSize": "512 GB", "storageType": "NVMe SSD", "interface": "PCIe Gen4 x4 NVMe M.2 2280", "readSpeed": "Up to 4,200 MB/s"},
            "display": {"size": "14.0\"", "resolution": "FHD (1920 x 1080)", "panelType": "IPS Anti-Glare", "refreshRate": "60 Hz", "touchAntiGlare": "Anti-Glare 250 nits (Non-touch)"},
            "graphics": {"gpuName": "Intel Iris Xe Graphics", "type": "Integrated", "vram": "Shared System Memory"},
            "connectivityPorts": {"ports": "2x Thunderbolt 4 with Power Delivery & DisplayPort, 2x USB 3.2 Gen 1 (1 PowerShare), 1x HDMI 2.0, RJ-45 Gigabit, MicroSD, Audio Jack", "wireless": "Intel Wi-Fi 6E AX211 + Bluetooth 5.2"},
            "batteryBuild": {"battery": "58Wh ExpressCharge Boost Capable", "weight": "1.36 kg (3.01 lbs)", "keyboard": "Backlit Spill-Resistant Keyboard", "webcam": "1080p FHD RGB-IR with Camera Privacy Shutter", "os": "Windows 11 Pro 64-bit Licensed"},
            "conditionWarranty": {"condition": "Grade A+ Like New · Business Workhorse", "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"}
        }
    },
    14: {
        "name": "Dell Latitude 7420",
        "brandName": "Dell",
        "series": "Latitude 7420",
        "shortSpecs": {"cpuFamily": "Core i5", "generation": "11th Gen", "ramGb": 16, "storageGb": 512, "storageType": "NVMe SSD", "gpuType": "integrated", "isDedicatedGpu": False},
        "fullSpecs": {
            "performance": {"processor": "Intel Core i5-1145G7 vPro", "coresThreads": "4 Cores / 8 Threads", "clocks": "2.60 GHz Base, up to 4.40 GHz Turbo", "cache": "8 MB Intel Smart Cache"},
            "memoryStorage": {"ramSize": "16 GB", "ramType": "LPDDR4x", "ramSpeed": "4266 MHz", "ramSlots": "Soldered Dual-Channel (Non-upgradable)", "storageSize": "512 GB", "storageType": "NVMe SSD", "interface": "PCIe Gen3 x4 M.2 2280", "readSpeed": "Up to 3,200 MB/s"},
            "display": {"size": "14.0\"", "resolution": "FHD (1920 x 1080)", "panelType": "IPS Anti-Glare", "refreshRate": "60 Hz", "touchAntiGlare": "Super Low Power Anti-Glare, 400 nits ComfortView Plus"},
            "graphics": {"gpuName": "Intel Iris Xe Graphics", "type": "Integrated", "vram": "Shared System Memory"},
            "connectivityPorts": {"ports": "2x Thunderbolt 4 USB-C (Power Delivery/DisplayPort), 1x USB-A 3.2 Gen 1 (PowerShare), 1x HDMI 2.0, MicroSD 4.0, Audio Jack", "wireless": "Intel Wi-Fi 6 AX201 + Bluetooth 5.1"},
            "batteryBuild": {"battery": "63Wh ExpressCharge Capable", "weight": "1.22 kg (2.69 lbs) Carbon Fiber", "keyboard": "Backlit Spill-Resistant Keyboard", "webcam": "FHD IR Camera with ExpressSign-in & Privacy Shutter", "os": "Windows 11 Pro 64-bit Licensed"},
            "conditionWarranty": {"condition": "Grade A+ Like New · Carbon Fiber Flagship", "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"}
        }
    },
    15: {
        "name": "HP ProBook 640 G1",
        "brandName": "HP",
        "series": "ProBook 640 G1",
        "shortSpecs": {"cpuFamily": "Core i5", "generation": "4th Gen", "ramGb": 8, "storageGb": 256, "storageType": "SATA SSD", "gpuType": "integrated", "isDedicatedGpu": False},
        "fullSpecs": {
            "performance": {"processor": "Intel Core i5-4200M (Socketed)", "coresThreads": "2 Cores / 4 Threads", "clocks": "2.50 GHz Base, up to 3.10 GHz Boost", "cache": "3 MB Intel Smart Cache"},
            "memoryStorage": {"ramSize": "8 GB", "ramType": "DDR3L", "ramSpeed": "1600 MHz", "ramSlots": "2x SO-DIMM Slots (Upgradable to 16GB)", "storageSize": "256 GB", "storageType": "SATA SSD", "interface": "2.5\" SATA III SSD", "readSpeed": "Up to 520 MB/s"},
            "display": {"size": "14.0\"", "resolution": "HD / HD+ (1366 x 768 / 1600 x 900)", "panelType": "Anti-Glare LED-backlit", "refreshRate": "60 Hz", "touchAntiGlare": "Anti-Glare (Non-touch)"},
            "graphics": {"gpuName": "Intel HD Graphics 4600", "type": "Integrated", "vram": "Shared System Memory"},
            "connectivityPorts": {"ports": "4x USB 3.0, 1x VGA, 1x DisplayPort, 1x RJ-45 Ethernet, SD Card Reader, Headphone/Mic combo", "wireless": "Intel Dual Band Wireless-AC 7260 + Bluetooth 4.0"},
            "batteryBuild": {"battery": "55Wh 6-cell Lithium-Ion (Removable)", "weight": "2.00 kg (4.4 lbs)", "keyboard": "Spill-Resistant Keyboard with Drain", "webcam": "720p HD Webcam", "os": "Windows 10 Pro 64-bit Licensed"},
            "conditionWarranty": {"condition": "Clean Used (9/10) · Durable Classic", "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"}
        }
    },
    16: {
        "name": "HP ProBook 630 G9",
        "brandName": "HP",
        "series": "ProBook 630 G9",
        "shortSpecs": {"cpuFamily": "Core i3", "generation": "12th Gen", "ramGb": 8, "storageGb": 256, "storageType": "NVMe SSD", "gpuType": "integrated", "isDedicatedGpu": False},
        "fullSpecs": {
            "performance": {"processor": "Intel Core i3-1215U", "coresThreads": "6 Cores (2P + 4E) / 8 Threads", "clocks": "1.20 GHz Base, up to 4.40 GHz Turbo", "cache": "10 MB Intel Smart Cache"},
            "memoryStorage": {"ramSize": "8 GB", "ramType": "DDR4", "ramSpeed": "3200 MHz", "ramSlots": "2x SO-DIMM Slots (Upgradable to 32GB)", "storageSize": "256 GB", "storageType": "NVMe SSD", "interface": "PCIe NVMe M.2 2280", "readSpeed": "Up to 2,400 MB/s"},
            "display": {"size": "13.3\"", "resolution": "FHD (1920 x 1080)", "panelType": "IPS Anti-Glare", "refreshRate": "60 Hz", "touchAntiGlare": "Anti-Glare (Non-touch), 250 nits"},
            "graphics": {"gpuName": "Intel UHD Graphics", "type": "Integrated", "vram": "Shared System Memory"},
            "connectivityPorts": {"ports": "1x USB Type-C (USB Power Delivery, DisplayPort 1.4), 2x USB Type-A (1 charging), 1x HDMI 2.0, Headphone/mic combo", "wireless": "Intel Wi-Fi 6E AX211 + Bluetooth 5.3"},
            "batteryBuild": {"battery": "42.75Wh / 51Wh HP Long Life Fast Charge", "weight": "1.28 kg (2.81 lbs)", "keyboard": "HP Premium Spill-Resistant Backlit Keyboard", "webcam": "720p HD Privacy Camera", "os": "Windows 11 Pro 64-bit Licensed"},
            "conditionWarranty": {"condition": "Grade A+ Like New · Modern Compact", "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"}
        }
    },
    17: {
        "name": "Lenovo ThinkPad T480s",
        "brandName": "Lenovo",
        "series": "ThinkPad T480s",
        "shortSpecs": {"cpuFamily": "Core i5", "generation": "8th Gen", "ramGb": 8, "storageGb": 256, "storageType": "NVMe SSD", "gpuType": "integrated", "isDedicatedGpu": False},
        "fullSpecs": {
            "performance": {"processor": "Intel Core i5-8350U vPro Quad Core", "coresThreads": "4 Cores / 8 Threads", "clocks": "1.70 GHz Base, up to 3.60 GHz Boost", "cache": "6 MB Intel Smart Cache"},
            "memoryStorage": {"ramSize": "8 GB", "ramType": "DDR4", "ramSpeed": "2400 MHz", "ramSlots": "8GB Soldered + 1 SO-DIMM Slot (Upgradable to 24GB/40GB)", "storageSize": "256 GB", "storageType": "NVMe SSD", "interface": "PCIe Gen3 x4 M.2 2280", "readSpeed": "Up to 2,500 MB/s"},
            "display": {"size": "14.0\"", "resolution": "FHD (1920 x 1080)", "panelType": "IPS Anti-Glare", "refreshRate": "60 Hz", "touchAntiGlare": "Anti-Glare (Non-touch), 250 nits"},
            "graphics": {"gpuName": "Intel UHD Graphics 620", "type": "Integrated", "vram": "Shared System Memory"},
            "connectivityPorts": {"ports": "2x USB 3.1 Gen 1 (1 Always On), 1x USB-C 3.1 Gen 1, 1x Thunderbolt 3, HDMI 1.4b, RJ-45 Gigabit, 4-in-1 Card Reader, Audio Jack", "wireless": "Intel Dual Band Wireless-AC 8265 + Bluetooth 4.2"},
            "batteryBuild": {"battery": "57Wh Internal Li-Ion (Rapid Charge 80% in 1 hr)", "weight": "1.32 kg (2.90 lbs) Slim Magnesium Chassis", "keyboard": "Legendary Spill-Resistant Backlit Keyboard with TrackPoint", "webcam": "720p HD with ThinkShutter Privacy Cover", "os": "Windows 11 Pro 64-bit Licensed"},
            "conditionWarranty": {"condition": "Grade A Like New · Legendary Slim Workhorse", "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"}
        }
    },
    18: {
        "name": "HP EliteBook Folio 9480m",
        "brandName": "HP",
        "series": "EliteBook Folio 9480m",
        "shortSpecs": {"cpuFamily": "Core i5", "generation": "4th Gen", "ramGb": 8, "storageGb": 256, "storageType": "SATA SSD", "gpuType": "integrated", "isDedicatedGpu": False},
        "fullSpecs": {
            "performance": {"processor": "Intel Core i5-4310U", "coresThreads": "2 Cores / 4 Threads", "clocks": "2.00 GHz Base, up to 3.00 GHz Boost", "cache": "3 MB Intel Smart Cache"},
            "memoryStorage": {"ramSize": "8 GB", "ramType": "DDR3L", "ramSpeed": "1600 MHz", "ramSlots": "2x SO-DIMM Slots (Upgradable to 16GB)", "storageSize": "256 GB", "storageType": "SATA SSD", "interface": "2.5\" SATA III SSD / mSATA", "readSpeed": "Up to 520 MB/s"},
            "display": {"size": "14.0\"", "resolution": "HD+ (1600 x 900)", "panelType": "Anti-Glare LED-backlit", "refreshRate": "60 Hz", "touchAntiGlare": "Anti-Glare (Non-touch)"},
            "graphics": {"gpuName": "Intel HD Graphics 4400", "type": "Integrated", "vram": "Shared System Memory"},
            "connectivityPorts": {"ports": "3x USB 3.0 (1 charging), 1x DisplayPort 1.2a, 1x VGA, RJ-45 Ethernet, SD/MMC slot, Headphone/Mic combo", "wireless": "Intel Dual Band Wireless-AC 7260 + Bluetooth 4.0"},
            "batteryBuild": {"battery": "52Wh 4-Cell Long Life Polymer", "weight": "1.61 kg (3.56 lbs) Slim Silver Magnesium/Aluminum", "keyboard": "Spill-Resistant Backlit Keyboard with Dual Point", "webcam": "720p HD Webcam", "os": "Windows 10/11 Pro 64-bit Licensed"},
            "conditionWarranty": {"condition": "Clean Used (9/10) · Durable Metal Ultrabook", "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"}
        }
    },
    19: {
        "name": "HP ProBook 640 G2",
        "brandName": "HP",
        "series": "ProBook 640 G2",
        "shortSpecs": {"cpuFamily": "Core i3", "generation": "6th Gen", "ramGb": 8, "storageGb": 256, "storageType": "SATA SSD", "gpuType": "integrated", "isDedicatedGpu": False},
        "fullSpecs": {
            "performance": {"processor": "Intel Core i3-6100U", "coresThreads": "2 Cores / 4 Threads", "clocks": "2.30 GHz Base", "cache": "3 MB Intel Smart Cache"},
            "memoryStorage": {"ramSize": "8 GB", "ramType": "DDR4", "ramSpeed": "2133 MHz", "ramSlots": "2x SO-DIMM Slots (Upgradable to 16GB/32GB)", "storageSize": "256 GB", "storageType": "SATA SSD", "interface": "2.5\" SATA III SSD / M.2", "readSpeed": "Up to 530 MB/s"},
            "display": {"size": "14.0\"", "resolution": "FHD (1920 x 1080) / HD", "panelType": "Anti-Glare Slim LED", "refreshRate": "60 Hz", "touchAntiGlare": "Anti-Glare (Non-touch)"},
            "graphics": {"gpuName": "Intel HD Graphics 520", "type": "Integrated", "vram": "Shared System Memory"},
            "connectivityPorts": {"ports": "1x USB-C, 2x USB 3.0 (1 charging), 1x DisplayPort, 1x VGA, RJ-45, SD Card Reader, Audio Jack", "wireless": "Intel 802.11a/b/g/n/ac + Bluetooth 4.2"},
            "batteryBuild": {"battery": "46Wh 3-Cell HP Long Life Prismatic", "weight": "1.95 kg (4.30 lbs)", "keyboard": "HP Spill-Resistant Keyboard", "webcam": "720p HD Webcam", "os": "Windows 10/11 Pro 64-bit Licensed"},
            "conditionWarranty": {"condition": "Good Condition (9/10) · Reliable Budget Laptop", "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"}
        }
    },
    20: {
        "name": "Microsoft Surface Laptop 3",
        "brandName": "Microsoft",
        "series": "Surface Laptop 3",
        "shortSpecs": {"cpuFamily": "Core i5", "generation": "10th Gen", "ramGb": 8, "storageGb": 256, "storageType": "NVMe SSD", "gpuType": "integrated", "isDedicatedGpu": False},
        "fullSpecs": {
            "performance": {"processor": "Intel Core i5-1035G7", "coresThreads": "4 Cores / 8 Threads", "clocks": "1.20 GHz Base, up to 3.70 GHz Boost", "cache": "6 MB Intel Smart Cache"},
            "memoryStorage": {"ramSize": "8 GB", "ramType": "LPDDR4x", "ramSpeed": "3733 MHz", "ramSlots": "Soldered (Non-upgradable)", "storageSize": "256 GB", "storageType": "NVMe SSD", "interface": "Removable M.2 2230 NVMe SSD", "readSpeed": "Up to 2,200 MB/s"},
            "display": {"size": "13.5\"", "resolution": "2.2K (2256 x 1504) 3:2", "panelType": "PixelSense Touchscreen", "refreshRate": "60 Hz", "touchAntiGlare": "10-Point Multi-Touch with Surface Pen Support, Gorilla Glass 3"},
            "graphics": {"gpuName": "Intel Iris Plus Graphics", "type": "Integrated", "vram": "Shared System Memory"},
            "connectivityPorts": {"ports": "1x USB-C 3.1, 1x USB-A 3.1, 3.5mm Headphone Jack, Surface Connect Port", "wireless": "Wi-Fi 6 (802.11ax) + Bluetooth 5.0"},
            "batteryBuild": {"battery": "45Wh Fast Charging (80% in about 1 hour)", "weight": "1.26 kg (2.79 lbs) Aluminum Chassis", "keyboard": "Backlit Keyboard with Large Glass Trackpad", "webcam": "720p HD f/2.0 with Windows Hello Facial Authentication", "os": "Windows 11 Pro 64-bit Licensed"},
            "conditionWarranty": {"condition": "Pristine Like New (10/10) · Minimalist Premium", "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"}
        }
    },
    21: {
        "name": "Lenovo ThinkPad X1 Extreme Gen 2",
        "brandName": "Lenovo",
        "series": "ThinkPad X1 Extreme",
        "shortSpecs": {"cpuFamily": "Core i7", "generation": "9th Gen", "ramGb": 16, "storageGb": 512, "storageType": "NVMe SSD", "gpuType": "discrete", "isDedicatedGpu": True},
        "fullSpecs": {
            "performance": {"processor": "Intel Core i7-9750H (45W High-Power)", "coresThreads": "6 Cores / 12 Threads", "clocks": "2.60 GHz Base, up to 4.50 GHz Turbo", "cache": "12 MB Intel Smart Cache"},
            "memoryStorage": {"ramSize": "16 GB", "ramType": "DDR4", "ramSpeed": "2666 MHz", "ramSlots": "2x SO-DIMM Slots (Upgradable to 64GB)", "storageSize": "512 GB", "storageType": "NVMe SSD", "interface": "Dual M.2 PCIe Gen3 x4 NVMe (2 Slots)", "readSpeed": "Up to 3,500 MB/s"},
            "display": {"size": "15.6\"", "resolution": "FHD (1920 x 1080) 500 nits HDR400 IPS / 4K OLED", "panelType": "IPS Anti-Glare 500 nits Dolby Vision HDR", "refreshRate": "60 Hz", "touchAntiGlare": "Anti-Glare (Non-touch)"},
            "graphics": {"gpuName": "NVIDIA GeForce GTX 1650 Max-Q", "type": "Dedicated", "vram": "4 GB GDDR5 Dedicated"},
            "connectivityPorts": {"ports": "2x Thunderbolt 3, 2x USB 3.1 Gen 1, 1x HDMI 2.0, SD Card Reader, Audio combo, Network extension", "wireless": "Intel Wi-Fi 6 AX200 + Bluetooth 5.1"},
            "batteryBuild": {"battery": "80Wh Rapid Charge (80% in 1 hr)", "weight": "1.70 kg (3.75 lbs) Carbon-Fiber & Magnesium", "keyboard": "ThinkPad Precision Backlit Keyboard with TrackPoint", "webcam": "720p HD with ThinkShutter & IR Windows Hello", "os": "Windows 11 Pro 64-bit Licensed"},
            "conditionWarranty": {"condition": "Grade A+ Like New · High-Performance Workstation", "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"}
        }
    },
    22: {
        "name": "Dell Latitude 7320 2-in-1",
        "brandName": "Dell",
        "series": "Latitude 7320",
        "shortSpecs": {"cpuFamily": "Core i5", "generation": "11th Gen", "ramGb": 16, "storageGb": 512, "storageType": "NVMe SSD", "gpuType": "integrated", "isDedicatedGpu": False},
        "fullSpecs": {
            "performance": {"processor": "Intel Core i5-1145G7 vPro", "coresThreads": "4 Cores / 8 Threads", "clocks": "2.60 GHz Base, up to 4.40 GHz Turbo", "cache": "8 MB Intel Smart Cache"},
            "memoryStorage": {"ramSize": "16 GB", "ramType": "LPDDR4x", "ramSpeed": "4266 MHz", "ramSlots": "Soldered Dual-Channel (Non-upgradable)", "storageSize": "512 GB", "storageType": "NVMe SSD", "interface": "PCIe Gen3 x4 M.2 2280", "readSpeed": "Up to 3,200 MB/s"},
            "display": {"size": "13.3\"", "resolution": "FHD (1920 x 1080) 16:9", "panelType": "IPS Touchscreen 360° Convertible", "refreshRate": "60 Hz", "touchAntiGlare": "Corning Gorilla Glass 6 DX Touch with Active Pen Support, 300 nits"},
            "graphics": {"gpuName": "Intel Iris Xe Graphics", "type": "Integrated", "vram": "Shared System Memory"},
            "connectivityPorts": {"ports": "2x Thunderbolt 4 with Power Delivery & DisplayPort, 1x USB-A 3.2 Gen 1 with PowerShare, 1x HDMI 2.0, MicroSD, Audio Jack", "wireless": "Intel Wi-Fi 6 AX201 + Bluetooth 5.1"},
            "batteryBuild": {"battery": "63Wh ExpressCharge Capable", "weight": "1.39 kg (3.06 lbs) CNC Aluminum", "keyboard": "Backlit Spill-Resistant Keyboard", "webcam": "FHD IR Camera with Proximity Sensor & ExpressSign-in", "os": "Windows 11 Pro 64-bit Licensed"},
            "conditionWarranty": {"condition": "Grade A+ Like New · Executive 2-in-1", "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"}
        }
    },
    23: {
        "name": "HP EliteBook 840 G8",
        "brandName": "HP",
        "series": "EliteBook 840 G8",
        "shortSpecs": {"cpuFamily": "Core i5", "generation": "11th Gen", "ramGb": 16, "storageGb": 512, "storageType": "NVMe SSD", "gpuType": "integrated", "isDedicatedGpu": False},
        "fullSpecs": {
            "performance": {"processor": "Intel Core i5-1135G7", "coresThreads": "4 Cores / 8 Threads", "clocks": "2.40 GHz Base, up to 4.20 GHz Turbo", "cache": "8 MB Intel Smart Cache"},
            "memoryStorage": {"ramSize": "16 GB", "ramType": "DDR4", "ramSpeed": "3200 MHz", "ramSlots": "2x SO-DIMM Slots (Upgradable to 64GB)", "storageSize": "512 GB", "storageType": "NVMe SSD", "interface": "PCIe Gen3 x4 NVMe M.2 2280", "readSpeed": "Up to 3,200 MB/s"},
            "display": {"size": "14.0\"", "resolution": "FHD (1920 x 1080)", "panelType": "IPS Anti-Glare", "refreshRate": "60 Hz", "touchAntiGlare": "Anti-Glare 400 nits Low Power HP Sure View or sRGB"},
            "graphics": {"gpuName": "Intel Iris Xe Graphics", "type": "Integrated", "vram": "Shared System Memory"},
            "connectivityPorts": {"ports": "2x Thunderbolt 4 USB-C, 2x USB-A 3.2 Gen 1 (1 charging), 1x HDMI 2.0b, Headphone/mic combo", "wireless": "Intel Wi-Fi 6 AX201 (2x2) + Bluetooth 5.0"},
            "batteryBuild": {"battery": "53Wh HP Long Life Fast Charge (50% in 30 mins)", "weight": "1.32 kg (2.9 lbs) All-Metal Aluminum", "keyboard": "HP Premium Spill-Resistant Backlit Keyboard", "webcam": "720p HD IR Camera with Windows Hello & Privacy Shutter", "os": "Windows 11 Pro 64-bit Licensed"},
            "conditionWarranty": {"condition": "Grade A+ Like New · Executive Business Ultrabook", "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"}
        }
    },
    24: {
        "name": "HP EliteBook 840 G7",
        "brandName": "HP",
        "series": "EliteBook 840 G7",
        "shortSpecs": {"cpuFamily": "Core i5", "generation": "10th Gen", "ramGb": 16, "storageGb": 512, "storageType": "NVMe SSD", "gpuType": "integrated", "isDedicatedGpu": False},
        "fullSpecs": {
            "performance": {"processor": "Intel Core i5-10310U vPro", "coresThreads": "4 Cores / 8 Threads", "clocks": "1.70 GHz Base, up to 4.40 GHz Boost", "cache": "6 MB Intel Smart Cache"},
            "memoryStorage": {"ramSize": "16 GB", "ramType": "DDR4", "ramSpeed": "2666 MHz", "ramSlots": "2x SO-DIMM Slots (Upgradable to 64GB)", "storageSize": "512 GB", "storageType": "NVMe SSD", "interface": "PCIe Gen3 x4 NVMe M.2 2280", "readSpeed": "Up to 2,800 MB/s"},
            "display": {"size": "14.0\"", "resolution": "FHD (1920 x 1080)", "panelType": "IPS Anti-Glare", "refreshRate": "60 Hz", "touchAntiGlare": "Anti-Glare 250 nits / 400 nits Low Power"},
            "graphics": {"gpuName": "Intel UHD Graphics 620", "type": "Integrated", "vram": "Shared System Memory"},
            "connectivityPorts": {"ports": "2x USB-C (Thunderbolt 3), 2x USB-A 3.1 Gen 1 (1 charging), 1x HDMI 1.4b, Headphone/mic combo", "wireless": "Intel Wi-Fi 6 AX201 + Bluetooth 5.0"},
            "batteryBuild": {"battery": "53Wh HP Long Life Fast Charge", "weight": "1.33 kg (2.93 lbs) Sleek Silver Aluminum", "keyboard": "HP Premium Spill-Resistant Backlit Keyboard", "webcam": "720p HD with Integrated Privacy Shutter", "os": "Windows 11 Pro 64-bit Licensed"},
            "conditionWarranty": {"condition": "Grade A+ Like New · Certified Refurbished", "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"}
        }
    },
    25: {
        "name": "Dell Precision 5560",
        "brandName": "Dell",
        "series": "Precision 5560",
        "shortSpecs": {"cpuFamily": "Core i9", "generation": "11th Gen", "ramGb": 32, "storageGb": 1000, "storageType": "NVMe SSD", "gpuType": "rtx", "isDedicatedGpu": True},
        "fullSpecs": {
            "performance": {"processor": "Intel Core i9-11950H vPro (45W Workstation)", "coresThreads": "8 Cores / 16 Threads", "clocks": "2.60 GHz Base, up to 5.00 GHz Max Turbo", "cache": "24 MB Intel Smart Cache"},
            "memoryStorage": {"ramSize": "32 GB", "ramType": "DDR4", "ramSpeed": "3200 MHz", "ramSlots": "2x SO-DIMM Slots (Upgradable to 64GB)", "storageSize": "1 TB", "storageType": "NVMe SSD", "interface": "Dual M.2 PCIe Gen4 x4 NVMe Slots", "readSpeed": "Up to 6,900 MB/s"},
            "display": {"size": "15.6\"", "resolution": "FHD+ (1920 x 1200) 16:10 500 nits / 4K UHD+ Touch", "panelType": "IPS UltraSharp 100% sRGB", "refreshRate": "60 Hz", "touchAntiGlare": "Anti-Glare 500 nits InfinityEdge"},
            "graphics": {"gpuName": "NVIDIA RTX A2000 Laptop GPU", "type": "Dedicated", "vram": "4 GB GDDR6 Dedicated Workstation"},
            "connectivityPorts": {"ports": "2x Thunderbolt 4 USB-C (DisplayPort/PD), 1x USB-C 3.2 Gen 2, Full-size SD Card Slot, Audio Jack", "wireless": "Intel Wi-Fi 6 AX201 + Bluetooth 5.2"},
            "batteryBuild": {"battery": "86Wh 6-cell Lithium-Ion ExpressCharge", "weight": "1.84 kg (4.06 lbs) CNC Aluminum & Carbon Fiber", "keyboard": "Backlit Keyboard with Large Glass Touchpad", "webcam": "720p HD IR Camera with Windows Hello Proximity Sensor", "os": "Windows 11 Pro for Workstations Licensed"},
            "conditionWarranty": {"condition": "Pristine Grade A+ · Mobile Workstation Beast", "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"}
        }
    },
    26: {
        "name": "Dell XPS 15 9575 2-in-1",
        "brandName": "Dell",
        "series": "XPS 15",
        "shortSpecs": {"cpuFamily": "Core i7", "generation": "8th Gen", "ramGb": 16, "storageGb": 512, "storageType": "NVMe SSD", "gpuType": "discrete", "isDedicatedGpu": True},
        "fullSpecs": {
            "performance": {"processor": "Intel Core i7-8705G with Radeon RX Vega M GL", "coresThreads": "4 Cores / 8 Threads (65W Kaby Lake-G)", "clocks": "3.10 GHz Base, up to 4.10 GHz Turbo", "cache": "8 MB Intel Smart Cache"},
            "memoryStorage": {"ramSize": "16 GB", "ramType": "DDR4", "ramSpeed": "2400 MHz", "ramSlots": "Soldered Dual-Channel (Non-upgradable)", "storageSize": "512 GB", "storageType": "NVMe SSD", "interface": "PCIe Gen3 x4 M.2 2280", "readSpeed": "Up to 3,000 MB/s"},
            "display": {"size": "15.6\"", "resolution": "4K UHD (3840 x 2160) Touch / FHD Touch", "panelType": "IPS InfinityEdge 100% AdobeRGB", "refreshRate": "60 Hz", "touchAntiGlare": "Corning Gorilla Glass 4 360° Touch with Dell Premium Pen Support"},
            "graphics": {"gpuName": "Radeon RX Vega M GL Graphics", "type": "Dedicated", "vram": "4 GB HBM2 High-Bandwidth Dedicated"},
            "connectivityPorts": {"ports": "2x Thunderbolt 3 with Power Delivery & DisplayPort, 2x USB-C 3.1 with Power Delivery, MicroSD, Audio Jack", "wireless": "Killer 1435 802.11ac 2x2 + Bluetooth 4.1"},
            "batteryBuild": {"battery": "75Wh 6-Cell Lithium-Ion Battery", "weight": "2.00 kg (4.41 lbs) Ultra-thin MagLev Body", "keyboard": "MagLev Keyboard (Magnetic Levitation Keys)", "webcam": "720p HD Webcam with Windows Hello IR Facial Recognition", "os": "Windows 11 Pro 64-bit Licensed"},
            "conditionWarranty": {"condition": "Pristine Grade A+ · Rare Powerful Convertible", "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"}
        }
    },
    27: {
        "name": "HP EliteBook x360 1030 G4",
        "brandName": "HP",
        "series": "EliteBook x360 1030",
        "shortSpecs": {"cpuFamily": "Core i5", "generation": "8th Gen", "ramGb": 16, "storageGb": 512, "storageType": "NVMe SSD", "gpuType": "integrated", "isDedicatedGpu": False},
        "fullSpecs": {
            "performance": {"processor": "Intel Core i5-8365U vPro Quad Core", "coresThreads": "4 Cores / 8 Threads", "clocks": "1.60 GHz Base, up to 4.10 GHz Boost", "cache": "6 MB Intel Smart Cache"},
            "memoryStorage": {"ramSize": "16 GB", "ramType": "LPDDR3", "ramSpeed": "2133 MHz", "ramSlots": "Soldered Dual-Channel (Non-upgradable)", "storageSize": "512 GB", "storageType": "NVMe SSD", "interface": "PCIe Gen3 x4 M.2 2280", "readSpeed": "Up to 3,000 MB/s"},
            "display": {"size": "13.3\"", "resolution": "FHD (1920 x 1080) BrightView", "panelType": "IPS Touchscreen 360° Convertible", "refreshRate": "60 Hz", "touchAntiGlare": "Corning Gorilla Glass 5 Touch with Active Pen Support, 400 nits"},
            "graphics": {"gpuName": "Intel UHD Graphics 620", "type": "Integrated", "vram": "Shared System Memory"},
            "connectivityPorts": {"ports": "2x Thunderbolt 3 (USB-C), 1x USB 3.1 Gen 1 (charging), 1x HDMI 1.4, Headphone/mic combo", "wireless": "Intel Wi-Fi 6 AX200 + Bluetooth 5.0"},
            "batteryBuild": {"battery": "56.2Wh HP Long Life Fast Charge", "weight": "1.25 kg (2.76 lbs) Precision CNC Aluminum", "keyboard": "HP Premium Collaboration Backlit Spill-Resistant", "webcam": "1080p FHD IR Camera with HP Privacy Shutter", "os": "Windows 11 Pro 64-bit Licensed"},
            "conditionWarranty": {"condition": "Grade A+ Like New · Business 2-in-1", "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"}
        }
    },
    28: {
        "name": "Lenovo ThinkPad X13 Gen 4",
        "brandName": "Lenovo",
        "series": "ThinkPad X13",
        "shortSpecs": {"cpuFamily": "Core i7", "generation": "13th Gen", "ramGb": 16, "storageGb": 512, "storageType": "NVMe SSD", "gpuType": "integrated", "isDedicatedGpu": False},
        "fullSpecs": {
            "performance": {"processor": "Intel Core i7-1355U", "coresThreads": "10 Cores (2P + 8E) / 12 Threads", "clocks": "1.70 GHz Base, up to 5.00 GHz Turbo", "cache": "12 MB Intel Smart Cache"},
            "memoryStorage": {"ramSize": "16 GB", "ramType": "LPDDR5", "ramSpeed": "4800 MHz", "ramSlots": "Soldered Dual-Channel (Non-upgradable)", "storageSize": "512 GB", "storageType": "NVMe SSD", "interface": "PCIe Gen4 x4 NVMe M.2 2280", "readSpeed": "Up to 5,000 MB/s"},
            "display": {"size": "13.3\"", "resolution": "WUXGA (1920 x 1200) 16:10", "panelType": "IPS Anti-Glare 100% sRGB", "refreshRate": "60 Hz", "touchAntiGlare": "Anti-Glare 300 nits (Non-touch)"},
            "graphics": {"gpuName": "Intel Iris Xe Graphics", "type": "Integrated", "vram": "Shared System Memory"},
            "connectivityPorts": {"ports": "2x Thunderbolt 4 USB-C, 2x USB-A 3.2 Gen 1 (1 Always On), 1x HDMI 2.1, Audio combo jack", "wireless": "Intel Wi-Fi 6E AX211 + Bluetooth 5.1"},
            "batteryBuild": {"battery": "54.7Wh Rapid Charge Battery", "weight": "1.09 kg (2.41 lbs) Ultra-Lightweight Carbon/Magnesium", "keyboard": "Backlit Spill-Resistant Keyboard with TrackPoint", "webcam": "FHD 1080p + IR Hybrid with Privacy Shutter", "os": "Windows 11 Pro 64-bit Licensed"},
            "conditionWarranty": {"condition": "Pristine Like New (10/10) · Latest Generation Ultrabook", "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"}
        }
    },
    29: {
        "name": "Dell Vostro 5490",
        "brandName": "Dell",
        "series": "Vostro 5490",
        "shortSpecs": {"cpuFamily": "Core i5", "generation": "10th Gen", "ramGb": 8, "storageGb": 256, "storageType": "NVMe SSD", "gpuType": "integrated", "isDedicatedGpu": False},
        "fullSpecs": {
            "performance": {"processor": "Intel Core i5-10210U", "coresThreads": "4 Cores / 8 Threads", "clocks": "1.60 GHz Base, up to 4.20 GHz Boost", "cache": "6 MB Intel Smart Cache"},
            "memoryStorage": {"ramSize": "8 GB", "ramType": "DDR4", "ramSpeed": "2666 MHz", "ramSlots": "1 Soldered + 1 SO-DIMM Slot (Upgradable to 24GB)", "storageSize": "256 GB", "storageType": "NVMe SSD", "interface": "PCIe Gen3 x4 M.2 2280", "readSpeed": "Up to 2,200 MB/s"},
            "display": {"size": "14.0\"", "resolution": "FHD (1920 x 1080)", "panelType": "IPS Anti-Glare LED-Backlit", "refreshRate": "60 Hz", "touchAntiGlare": "Anti-Glare (Non-touch)"},
            "graphics": {"gpuName": "Intel UHD Graphics", "type": "Integrated", "vram": "Shared System Memory"},
            "connectivityPorts": {"ports": "1x USB-C 3.1 Gen 1 (DisplayPort/PD), 2x USB-A 3.1 Gen 1, 1x USB 2.0, 1x HDMI 1.4b, RJ-45, MicroSD, Audio Jack", "wireless": "802.11ac 1x1 Wi-Fi + Bluetooth 5.0"},
            "batteryBuild": {"battery": "42Wh 3-Cell Lithium-Ion", "weight": "1.49 kg (3.28 lbs) Aluminum Cover", "keyboard": "Backlit Spill-Resistant Keyboard", "webcam": "720p HD Webcam", "os": "Windows 11 Pro 64-bit Licensed"},
            "conditionWarranty": {"condition": "Grade A+ Like New · Business Essential", "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"}
        }
    },
    30: {
        "name": "Dell Latitude 7490",
        "brandName": "Dell",
        "series": "Latitude 7490",
        "shortSpecs": {"cpuFamily": "Core i7", "generation": "8th Gen", "ramGb": 16, "storageGb": 512, "storageType": "NVMe SSD", "gpuType": "integrated", "isDedicatedGpu": False},
        "fullSpecs": {
            "performance": {"processor": "Intel Core i7-8650U vPro Quad Core", "coresThreads": "4 Cores / 8 Threads", "clocks": "1.90 GHz Base, up to 4.20 GHz Boost", "cache": "8 MB Intel Smart Cache"},
            "memoryStorage": {"ramSize": "16 GB", "ramType": "DDR4", "ramSpeed": "2400 MHz", "ramSlots": "2x SO-DIMM Slots (Upgradable to 32GB)", "storageSize": "512 GB", "storageType": "NVMe SSD", "interface": "PCIe Gen3 x4 M.2 2280", "readSpeed": "Up to 3,000 MB/s"},
            "display": {"size": "14.0\"", "resolution": "FHD (1920 x 1080)", "panelType": "WVA IPS Anti-Glare", "refreshRate": "60 Hz", "touchAntiGlare": "Anti-Glare 300 nits (Non-touch)"},
            "graphics": {"gpuName": "Intel UHD Graphics 620", "type": "Integrated", "vram": "Shared System Memory"},
            "connectivityPorts": {"ports": "1x USB-C (DisplayPort/Thunderbolt 3), 3x USB 3.1 Gen 1 (1 PowerShare), 1x HDMI 1.4, RJ-45, MicroSD, Audio Jack", "wireless": "Intel Dual-Band Wireless-AC 8265 + Bluetooth 4.2"},
            "batteryBuild": {"battery": "60Wh ExpressCharge 4-Cell Battery", "weight": "1.40 kg (3.11 lbs) Carbon Fiber/Magnesium", "keyboard": "Backlit Spill-Resistant Keyboard with Dual Pointing", "webcam": "HD Camera with Privacy Shutter", "os": "Windows 11 Pro 64-bit Licensed"},
            "conditionWarranty": {"condition": "Grade A+ Like New · High Durability Corporate", "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"}
        }
    },
    31: {
        "name": "Dell Latitude 3310 2-in-1",
        "brandName": "Dell",
        "series": "Latitude 3310",
        "shortSpecs": {"cpuFamily": "Core i5", "generation": "10th Gen", "ramGb": 8, "storageGb": 256, "storageType": "NVMe SSD", "gpuType": "integrated", "isDedicatedGpu": False},
        "fullSpecs": {
            "performance": {"processor": "Intel Core i5-10210U", "coresThreads": "4 Cores / 8 Threads", "clocks": "1.60 GHz Base, up to 4.20 GHz Boost", "cache": "6 MB Intel Smart Cache"},
            "memoryStorage": {"ramSize": "8 GB", "ramType": "DDR4", "ramSpeed": "2666 MHz", "ramSlots": "1x SO-DIMM Slot (Upgradable to 16GB)", "storageSize": "256 GB", "storageType": "NVMe SSD", "interface": "PCIe Gen3 x4 M.2 2280", "readSpeed": "Up to 2,200 MB/s"},
            "display": {"size": "13.3\"", "resolution": "FHD (1920 x 1080) 16:9", "panelType": "IPS Touchscreen 360° Convertible", "refreshRate": "60 Hz", "touchAntiGlare": "Corning Gorilla Glass Touch with Active Stylus Support"},
            "graphics": {"gpuName": "Intel UHD Graphics", "type": "Integrated", "vram": "Shared System Memory"},
            "connectivityPorts": {"ports": "1x USB-C (DisplayPort/PD), 2x USB 3.1 Gen 1, 1x HDMI 1.4a, MicroSD Card Reader, Audio Jack", "wireless": "Intel Wi-Fi 6 AX201 + Bluetooth 5.1"},
            "batteryBuild": {"battery": "53Wh 4-Cell ExpressCharge", "weight": "1.56 kg (3.44 lbs) Ruggedized Rubberized Edges", "keyboard": "Sealed Spill-Resistant Keyboard", "webcam": "HD Webcam with Dual Digital Mics", "os": "Windows 11 Pro 64-bit Licensed"},
            "conditionWarranty": {"condition": "Grade A Like New · Durable Student / Teacher 2-in-1", "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"}
        }
    },
    32: {
        "name": "Dell Latitude E7270",
        "brandName": "Dell",
        "series": "Latitude E7270",
        "shortSpecs": {"cpuFamily": "Core i5", "generation": "6th Gen", "ramGb": 8, "storageGb": 256, "storageType": "SATA SSD", "gpuType": "integrated", "isDedicatedGpu": False},
        "fullSpecs": {
            "performance": {"processor": "Intel Core i5-6300U vPro", "coresThreads": "2 Cores / 4 Threads", "clocks": "2.40 GHz Base, up to 3.00 GHz Boost", "cache": "3 MB Intel Smart Cache"},
            "memoryStorage": {"ramSize": "8 GB", "ramType": "DDR4", "ramSpeed": "2133 MHz", "ramSlots": "2x SO-DIMM Slots (Upgradable to 16GB)", "storageSize": "256 GB", "storageType": "SATA SSD", "interface": "M.2 SATA III SSD", "readSpeed": "Up to 540 MB/s"},
            "display": {"size": "12.5\"", "resolution": "FHD (1920 x 1080) / HD", "panelType": "Anti-Glare IPS Display", "refreshRate": "60 Hz", "touchAntiGlare": "Anti-Glare (Non-touch)"},
            "graphics": {"gpuName": "Intel HD Graphics 520", "type": "Integrated", "vram": "Shared System Memory"},
            "connectivityPorts": {"ports": "3x USB 3.0 (1 with PowerShare), 1x HDMI, 1x Mini DisplayPort, RJ-45 Ethernet, SD Card Reader, Audio Jack", "wireless": "Intel Dual-Band Wireless-AC 8260 + Bluetooth 4.2"},
            "batteryBuild": {"battery": "55Wh 4-Cell Lithium Polymer", "weight": "1.26 kg (2.77 lbs) Magnesium Alloy", "keyboard": "Backlit Spill-Resistant Keyboard", "webcam": "720p HD Webcam", "os": "Windows 10/11 Pro 64-bit Licensed"},
            "conditionWarranty": {"condition": "Clean Used (9/10) · Ultra-Portable Compact", "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"}
        }
    },
    33: {
        "name": "Dell Latitude 5320",
        "brandName": "Dell",
        "series": "Latitude 5320",
        "shortSpecs": {"cpuFamily": "Core i5", "generation": "11th Gen", "ramGb": 16, "storageGb": 512, "storageType": "NVMe SSD", "gpuType": "integrated", "isDedicatedGpu": False},
        "fullSpecs": {
            "performance": {"processor": "Intel Core i5-1145G7 vPro", "coresThreads": "4 Cores / 8 Threads", "clocks": "2.60 GHz Base, up to 4.40 GHz Turbo", "cache": "8 MB Intel Smart Cache"},
            "memoryStorage": {"ramSize": "16 GB", "ramType": "DDR4", "ramSpeed": "3200 MHz", "ramSlots": "Soldered Dual-Channel (Non-upgradable)", "storageSize": "512 GB", "storageType": "NVMe SSD", "interface": "PCIe Gen3 x4 M.2 2280", "readSpeed": "Up to 3,200 MB/s"},
            "display": {"size": "13.3\"", "resolution": "FHD (1920 x 1080)", "panelType": "IPS Anti-Glare", "refreshRate": "60 Hz", "touchAntiGlare": "Anti-Glare 300 nits ComfortView Plus"},
            "graphics": {"gpuName": "Intel Iris Xe Graphics", "type": "Integrated", "vram": "Shared System Memory"},
            "connectivityPorts": {"ports": "2x Thunderbolt 4 USB-C, 2x USB-A 3.2 Gen 1 (1 PowerShare), 1x HDMI 2.0, MicroSD, Audio Jack", "wireless": "Intel Wi-Fi 6 AX201 + Bluetooth 5.1"},
            "batteryBuild": {"battery": "63Wh ExpressCharge Capable", "weight": "1.20 kg (2.65 lbs)", "keyboard": "Backlit Spill-Resistant Keyboard", "webcam": "720p HD with Privacy Shutter", "os": "Windows 11 Pro 64-bit Licensed"},
            "conditionWarranty": {"condition": "Grade A+ Like New · Certified Refurbished", "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"}
        }
    },
    34: {
        "name": "Lenovo ThinkPad E14 Gen 1",
        "brandName": "Lenovo",
        "series": "ThinkPad E14",
        "shortSpecs": {"cpuFamily": "Core i3", "generation": "10th Gen", "ramGb": 8, "storageGb": 256, "storageType": "NVMe SSD", "gpuType": "integrated", "isDedicatedGpu": False},
        "fullSpecs": {
            "performance": {"processor": "Intel Core i3-10110U", "coresThreads": "2 Cores / 4 Threads", "clocks": "2.10 GHz Base, up to 4.10 GHz Boost", "cache": "4 MB Intel Smart Cache"},
            "memoryStorage": {"ramSize": "8 GB", "ramType": "DDR4", "ramSpeed": "2666 MHz", "ramSlots": "1x SO-DIMM Slot (Upgradable to 16GB/32GB)", "storageSize": "256 GB", "storageType": "NVMe SSD", "interface": "PCIe Gen3 x4 M.2 2280", "readSpeed": "Up to 2,200 MB/s"},
            "display": {"size": "14.0\"", "resolution": "FHD (1920 x 1080)", "panelType": "IPS Anti-Glare", "refreshRate": "60 Hz", "touchAntiGlare": "Anti-Glare (Non-touch), 250 nits"},
            "graphics": {"gpuName": "Intel UHD Graphics", "type": "Integrated", "vram": "Shared System Memory"},
            "connectivityPorts": {"ports": "1x USB-C 3.1 Gen 1 (DisplayPort/PD), 2x USB 3.1 Gen 1, 1x USB 2.0, 1x HDMI 1.4b, RJ-45 Gigabit, Audio Jack", "wireless": "Intel Wi-Fi 6 AX201 + Bluetooth 5.0"},
            "batteryBuild": {"battery": "45Wh Rapid Charge Battery", "weight": "1.69 kg (3.73 lbs) Aluminum Top Cover", "keyboard": "ThinkPad Precision Keyboard with TrackPoint", "webcam": "720p HD with ThinkShutter Privacy Cover", "os": "Windows 11 Pro 64-bit Licensed"},
            "conditionWarranty": {"condition": "Grade A+ Like New · Business Budget Favorite", "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"}
        }
    },
    35: {
        "name": "HP EliteBook x360 1030 G3",
        "brandName": "HP",
        "series": "EliteBook x360 1030",
        "shortSpecs": {"cpuFamily": "Core i5", "generation": "8th Gen", "ramGb": 16, "storageGb": 512, "storageType": "NVMe SSD", "gpuType": "integrated", "isDedicatedGpu": False},
        "fullSpecs": {
            "performance": {"processor": "Intel Core i5-8350U vPro Quad Core", "coresThreads": "4 Cores / 8 Threads", "clocks": "1.70 GHz Base, up to 3.60 GHz Boost", "cache": "6 MB Intel Smart Cache"},
            "memoryStorage": {"ramSize": "16 GB", "ramType": "LPDDR3", "ramSpeed": "2133 MHz", "ramSlots": "Soldered Dual-Channel (Non-upgradable)", "storageSize": "512 GB", "storageType": "NVMe SSD", "interface": "PCIe Gen3 x4 M.2 2280", "readSpeed": "Up to 3,000 MB/s"},
            "display": {"size": "13.3\"", "resolution": "FHD (1920 x 1080) BrightView", "panelType": "IPS Touchscreen 360° Convertible", "refreshRate": "60 Hz", "touchAntiGlare": "Corning Gorilla Glass 4 Touch, 400 nits, Active Pen Support"},
            "graphics": {"gpuName": "Intel UHD Graphics 620", "type": "Integrated", "vram": "Shared System Memory"},
            "connectivityPorts": {"ports": "2x Thunderbolt 3 (USB-C), 1x USB 3.1 Gen 1 (charging), 1x HDMI 1.4, Headphone/mic combo", "wireless": "Intel Dual-Band Wireless-AC 8265 + Bluetooth 4.2"},
            "batteryBuild": {"battery": "56.2Wh HP Long Life Fast Charge (50% in 30 mins)", "weight": "1.25 kg (2.76 lbs) CNC Machined Aluminum", "keyboard": "HP Premium Collaboration Backlit Spill-Resistant Keyboard", "webcam": "FHD 1080p Camera with IR Facial Recognition Windows Hello", "os": "Windows 11 Pro 64-bit Licensed"},
            "conditionWarranty": {"condition": "Pristine Like New (10/10) · CNC Aluminum 2-in-1", "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"}
        }
    },
    36: {
        "name": "Dell Alienware m15 R7",
        "brandName": "Dell",
        "series": "Alienware m15 R7",
        "shortSpecs": {"cpuFamily": "Ryzen 7", "generation": "6000 Series", "ramGb": 16, "storageGb": 1000, "storageType": "NVMe SSD", "gpuType": "rtx", "isDedicatedGpu": True},
        "fullSpecs": {
            "performance": {"processor": "AMD Ryzen 7 6800H", "coresThreads": "8 Cores / 16 Threads (45W Max Performance)", "clocks": "3.20 GHz Base, up to 4.70 GHz Max Boost", "cache": "16 MB L3 Cache"},
            "memoryStorage": {"ramSize": "16 GB", "ramType": "DDR5", "ramSpeed": "4800 MHz", "ramSlots": "2x SO-DIMM Slots (Upgradable to 64GB)", "storageSize": "1 TB", "storageType": "NVMe SSD", "interface": "Dual M.2 PCIe Gen4 x4 NVMe Slots", "readSpeed": "Up to 6,800 MB/s"},
            "display": {"size": "15.6\"", "resolution": "QHD (2560 x 1440) 240Hz 2ms", "panelType": "Fast IPS G-SYNC & Advanced Optimus", "refreshRate": "240 Hz", "touchAntiGlare": "Anti-Glare 400 nits, 99% DCI-P3, ComfortView Plus"},
            "graphics": {"gpuName": "NVIDIA GeForce RTX 3070 Ti", "type": "Dedicated", "vram": "8 GB GDDR6 Dedicated (150W TGP)"},
            "connectivityPorts": {"ports": "1x USB-C 3.2 Gen 2 (DisplayPort 1.4), 3x USB-A 3.2 Gen 1 (1 PowerShare), 1x HDMI 2.1, RJ-45 2.5Gbps Killer Ethernet, Headphone Jack", "wireless": "MediaTek Wi-Fi 6E RZ616 + Bluetooth 5.2"},
            "batteryBuild": {"battery": "86Wh 6-Cell Battery with 240W GaN Adapter", "weight": "2.42 kg (5.34 lbs) Cryo-tech Liquid Metal Cooled", "keyboard": "AlienFX Per-Key RGB Backlit Keyboard (1.8mm key travel)", "webcam": "720p HD with Dual-Array Digital Microphones and Windows Hello IR", "os": "Windows 11 Home/Pro 64-bit Licensed"},
            "conditionWarranty": {"condition": "Pristine Like New (10/10) · Elite Esports Gaming Beast", "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"}
        }
    },
    37: {
        "name": "HP 15-da Series",
        "brandName": "HP",
        "series": "HP 15 Laptop",
        "shortSpecs": {"cpuFamily": "Core i5", "generation": "8th Gen", "ramGb": 8, "storageGb": 256, "storageType": "NVMe SSD", "gpuType": "integrated", "isDedicatedGpu": False},
        "fullSpecs": {
            "performance": {"processor": "Intel Core i5-8250U Quad Core", "coresThreads": "4 Cores / 8 Threads", "clocks": "1.60 GHz Base, up to 3.40 GHz Boost", "cache": "6 MB Intel Smart Cache"},
            "memoryStorage": {"ramSize": "8 GB", "ramType": "DDR4", "ramSpeed": "2400 MHz", "ramSlots": "2x SO-DIMM Slots (Upgradable to 16GB)", "storageSize": "256 GB", "storageType": "NVMe SSD", "interface": "M.2 PCIe NVMe SSD + 2.5\" Bay", "readSpeed": "Up to 2,000 MB/s (unverified)"},
            "display": {"size": "15.6\"", "resolution": "FHD (1920 x 1080)", "panelType": "SVA Anti-Glare WLED-backlit", "refreshRate": "60 Hz", "touchAntiGlare": "Anti-Glare (Non-touch)"},
            "graphics": {"gpuName": "Intel UHD Graphics 620", "type": "Integrated", "vram": "Shared System Memory"},
            "connectivityPorts": {"ports": "2x USB 3.1 Gen 1, 1x USB 2.0, 1x HDMI 1.4b, RJ-45 Ethernet, SD Card Reader, Headphone/Mic combo", "wireless": "Realtek 802.11b/g/n/ac + Bluetooth 4.2"},
            "batteryBuild": {"battery": "41Wh 3-Cell Li-ion Battery", "weight": "1.77 kg (3.91 lbs)", "keyboard": "Full-size Keyboard with Integrated Numeric Keypad", "webcam": "HP TrueVision HD Camera with Digital Mic", "os": "Windows 11 Home/Pro 64-bit Licensed"},
            "conditionWarranty": {"condition": "Grade A Used · 15.6\" Everyday Workhorse", "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"}
        }
    },
    38: {
        "name": "HP Pavilion 15",
        "brandName": "HP",
        "series": "Pavilion 15",
        "shortSpecs": {"cpuFamily": "Core i5", "generation": "7th Gen", "ramGb": 8, "storageGb": 256, "storageType": "SATA SSD", "gpuType": "integrated", "isDedicatedGpu": False},
        "fullSpecs": {
            "performance": {"processor": "Intel Core i5-7200U", "coresThreads": "2 Cores / 4 Threads", "clocks": "2.50 GHz Base, up to 3.10 GHz Boost", "cache": "3 MB Intel Smart Cache"},
            "memoryStorage": {"ramSize": "8 GB", "ramType": "DDR4", "ramSpeed": "2133 MHz", "ramSlots": "2x SO-DIMM Slots (Upgradable to 16GB)", "storageSize": "256 GB", "storageType": "SATA SSD", "interface": "2.5\" SATA III SSD / M.2", "readSpeed": "Up to 540 MB/s"},
            "display": {"size": "15.6\"", "resolution": "FHD (1920 x 1080)", "panelType": "IPS BrightView WLED-backlit", "refreshRate": "60 Hz", "touchAntiGlare": "BrightView Glass (Non-touch / Touch config unverified)"},
            "graphics": {"gpuName": "Intel HD Graphics 620", "type": "Integrated", "vram": "Shared System Memory"},
            "connectivityPorts": {"ports": "1x USB-C 3.1 Gen 1, 2x USB 3.1 Gen 1, 1x HDMI, RJ-45, SD Card Slot, Audio Jack", "wireless": "Intel 802.11b/g/n/ac + Bluetooth 4.2"},
            "batteryBuild": {"battery": "41Wh Li-Ion Fast Charge", "weight": "1.92 kg (4.23 lbs)", "keyboard": "Full-size Backlit Keyboard with NumPad", "webcam": "HP Wide Vision HD Camera with B&O Play Audio", "os": "Windows 10/11 Pro 64-bit Licensed"},
            "conditionWarranty": {"condition": "Clean Used (9/10) · Home & Office 15.6\"", "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"}
        }
    },
    39: {
        "name": "Lenovo Yoga 6 13",
        "brandName": "Lenovo",
        "series": "Yoga 6",
        "shortSpecs": {"cpuFamily": "Ryzen 5", "generation": "7000 Series", "ramGb": 16, "storageGb": 512, "storageType": "NVMe SSD", "gpuType": "integrated", "isDedicatedGpu": False},
        "fullSpecs": {
            "performance": {"processor": "AMD Ryzen 5 7530U", "coresThreads": "6 Cores / 12 Threads", "clocks": "2.00 GHz Base, up to 4.50 GHz Max Boost", "cache": "16 MB L3 Cache"},
            "memoryStorage": {"ramSize": "16 GB", "ramType": "LPDDR4x", "ramSpeed": "4266 MHz", "ramSlots": "Soldered Dual-Channel (Non-upgradable)", "storageSize": "512 GB", "storageType": "NVMe SSD", "interface": "PCIe Gen4 x4 NVMe M.2 2242", "readSpeed": "Up to 4,000 MB/s"},
            "display": {"size": "13.3\"", "resolution": "WUXGA (1920 x 1200) 16:10", "panelType": "IPS Touchscreen 360° Convertible", "refreshRate": "60 Hz", "touchAntiGlare": "Glossy 100% sRGB Touch, 300 nits, Dolby Vision, Stylus Supported"},
            "graphics": {"gpuName": "AMD Radeon Graphics (Vega 7)", "type": "Integrated", "vram": "Shared System Memory"},
            "connectivityPorts": {"ports": "2x USB-C 3.2 Gen 1 (DisplayPort 1.4/PD 3.0), 2x USB-A 3.2 Gen 1, 1x HDMI 2.1, MicroSD, Audio Jack", "wireless": "Wi-Fi 6 (802.11ax 2x2) + Bluetooth 5.1"},
            "batteryBuild": {"battery": "59Wh Internal Battery (Up to 12.5 hrs)", "weight": "1.37 kg (3.02 lbs) Unique Dark Teal Fabric/Alloy", "keyboard": "Backlit Keyboard with Front-Facing Dolby Atmos Stereo Speakers", "webcam": "FHD 1080p with Privacy Shutter and IR Windows Hello", "os": "Windows 11 Pro 64-bit Licensed"},
            "conditionWarranty": {"condition": "Pristine Like New (10/10) · Stylish Fabric Cover 2-in-1", "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"}
        }
    },
    40: {
        "name": "HP ProBook 640 G7",
        "brandName": "HP",
        "series": "ProBook 640 G7",
        "shortSpecs": {"cpuFamily": "Core i5", "generation": "10th Gen", "ramGb": 16, "storageGb": 512, "storageType": "NVMe SSD", "gpuType": "integrated", "isDedicatedGpu": False},
        "fullSpecs": {
            "performance": {"processor": "Intel Core i5-10210U", "coresThreads": "4 Cores / 8 Threads", "clocks": "1.60 GHz Base, up to 4.20 GHz Boost", "cache": "6 MB Intel Smart Cache"},
            "memoryStorage": {"ramSize": "16 GB", "ramType": "DDR4", "ramSpeed": "2666 MHz", "ramSlots": "2x SO-DIMM Slots (Upgradable to 32GB/64GB)", "storageSize": "512 GB", "storageType": "NVMe SSD", "interface": "PCIe Gen3 x4 M.2 2280", "readSpeed": "Up to 2,800 MB/s"},
            "display": {"size": "14.0\"", "resolution": "FHD (1920 x 1080)", "panelType": "IPS Anti-Glare", "refreshRate": "60 Hz", "touchAntiGlare": "Anti-Glare 250 nits (Non-touch)"},
            "graphics": {"gpuName": "Intel UHD Graphics", "type": "Integrated", "vram": "Shared System Memory"},
            "connectivityPorts": {"ports": "1x USB-C 3.1 Gen 1, 3x USB 3.1 Gen 1 (1 charging), 1x HDMI 1.4b, RJ-45 Ethernet, MicroSD, Audio Jack", "wireless": "Intel Wi-Fi 6 AX201 + Bluetooth 5.0"},
            "batteryBuild": {"battery": "45Wh HP Long Life 3-Cell", "weight": "1.60 kg (3.53 lbs)", "keyboard": "HP Premium Spill-Resistant Backlit Keyboard", "webcam": "720p HD Privacy Camera", "os": "Windows 11 Pro 64-bit Licensed"},
            "conditionWarranty": {"condition": "Grade A+ Like New · Business Standard", "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"}
        }
    },
    41: {
        "name": "Lenovo Yoga 7i Gen 7",
        "brandName": "Lenovo",
        "series": "Yoga 7i",
        "shortSpecs": {"cpuFamily": "Core i7", "generation": "12th Gen", "ramGb": 16, "storageGb": 1000, "storageType": "NVMe SSD", "gpuType": "integrated", "isDedicatedGpu": False},
        "fullSpecs": {
            "performance": {"processor": "Intel Core i7-1260P", "coresThreads": "12 Cores (4P + 8E) / 16 Threads", "clocks": "2.10 GHz Base, up to 4.70 GHz Turbo", "cache": "18 MB Intel Smart Cache"},
            "memoryStorage": {"ramSize": "16 GB", "ramType": "LPDDR5", "ramSpeed": "4800 MHz", "ramSlots": "Soldered Dual-Channel (Non-upgradable)", "storageSize": "1 TB", "storageType": "NVMe SSD", "interface": "PCIe Gen4 x4 NVMe M.2 2280", "readSpeed": "Up to 5,500 MB/s"},
            "display": {"size": "14.0\"", "resolution": "2.8K (2880 x 1800) 16:10 90Hz OLED", "panelType": "OLED PureSight Touch 360°", "refreshRate": "90 Hz", "touchAntiGlare": "100% DCI-P3 400 nits Glossy Touch with Dolby Vision"},
            "graphics": {"gpuName": "Intel Iris Xe Graphics", "type": "Integrated", "vram": "Shared System Memory"},
            "connectivityPorts": {"ports": "2x Thunderbolt 4 USB-C, 1x USB-A 3.2 Gen 1 (Always On), 1x HDMI 2.0, MicroSD Card Reader, Audio Jack", "wireless": "Wi-Fi 6E AX211 + Bluetooth 5.2"},
            "batteryBuild": {"battery": "71Wh Rapid Charge Express (Up to 15 hours)", "weight": "1.42 kg (3.13 lbs) Comfort Edge CNC Aluminum", "keyboard": "Backlit Keyboard with Front Quad Speakers Dolby Atmos", "webcam": "1080p FHD IR Camera with Privacy Shutter", "os": "Windows 11 Pro 64-bit Licensed"},
            "conditionWarranty": {"condition": "Pristine Like New (10/10) · 2.8K OLED Convertible", "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"}
        }
    },
    42: {
        "name": "HP EliteBook 1040 G5",
        "brandName": "HP",
        "series": "EliteBook 1040",
        "shortSpecs": {"cpuFamily": "Core i7", "generation": "7th Gen", "ramGb": 16, "storageGb": 512, "storageType": "NVMe SSD", "gpuType": "integrated", "isDedicatedGpu": False},
        "fullSpecs": {
            "performance": {"processor": "Intel Core i7-7600U vPro", "coresThreads": "2 Cores / 4 Threads", "clocks": "2.80 GHz Base, up to 3.90 GHz Boost", "cache": "4 MB Intel Smart Cache"},
            "memoryStorage": {"ramSize": "16 GB", "ramType": "DDR4", "ramSpeed": "2133 MHz", "ramSlots": "Soldered Dual-Channel (Non-upgradable)", "storageSize": "512 GB", "storageType": "NVMe SSD", "interface": "PCIe Gen3 x4 M.2 2280", "readSpeed": "Up to 2,800 MB/s"},
            "display": {"size": "14.0\"", "resolution": "FHD (1920 x 1080)", "panelType": "IPS Anti-Glare Glass", "refreshRate": "60 Hz", "touchAntiGlare": "Anti-Glare 400 nits Ultra-Slim"},
            "graphics": {"gpuName": "Intel HD Graphics 620", "type": "Integrated", "vram": "Shared System Memory"},
            "connectivityPorts": {"ports": "2x Thunderbolt 3 (USB-C), 2x USB 3.1 Gen 1 (1 charging), 1x HDMI 1.4, Headphone/mic combo", "wireless": "Intel Dual Band Wireless-AC 8265 + Bluetooth 4.2"},
            "batteryBuild": {"battery": "67Wh 6-Cell Long Life Polymer", "weight": "1.35 kg (2.99 lbs) Precision CNC Unibody Aluminum", "keyboard": "HP Premium Collaboration Backlit Keyboard", "webcam": "720p HD with IR Facial Recognition Windows Hello & B&O Audio", "os": "Windows 11 Pro 64-bit Licensed"},
            "conditionWarranty": {"condition": "Grade A+ Like New · Ultra-Slim CNC Flagship", "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"}
        }
    },
    43: {
        "name": "Dell Latitude 5310",
        "brandName": "Dell",
        "series": "Latitude 5310",
        "shortSpecs": {"cpuFamily": "Core i5", "generation": "10th Gen", "ramGb": 16, "storageGb": 256, "storageType": "NVMe SSD", "gpuType": "integrated", "isDedicatedGpu": False},
        "fullSpecs": {
            "performance": {"processor": "Intel Core i5-10310U vPro", "coresThreads": "4 Cores / 8 Threads", "clocks": "1.70 GHz Base, up to 4.40 GHz Boost", "cache": "6 MB Intel Smart Cache"},
            "memoryStorage": {"ramSize": "16 GB", "ramType": "DDR4", "ramSpeed": "2666 MHz", "ramSlots": "2x SO-DIMM Slots (Upgradable to 32GB)", "storageSize": "256 GB", "storageType": "NVMe SSD", "interface": "PCIe Gen3 x4 M.2 2280", "readSpeed": "Up to 2,400 MB/s"},
            "display": {"size": "13.3\"", "resolution": "FHD (1920 x 1080)", "panelType": "IPS Anti-Glare", "refreshRate": "60 Hz", "touchAntiGlare": "Anti-Glare (Non-touch), 300 nits"},
            "graphics": {"gpuName": "Intel UHD Graphics", "type": "Integrated", "vram": "Shared System Memory"},
            "connectivityPorts": {"ports": "1x USB-C 3.2 Gen 2 (DisplayPort/PD), 2x USB-A 3.2 Gen 1 (1 PowerShare), 1x HDMI 1.4b, RJ-45, MicroSD, Audio Jack", "wireless": "Intel Wi-Fi 6 AX201 + Bluetooth 5.1"},
            "batteryBuild": {"battery": "51Wh ExpressCharge Capable", "weight": "1.24 kg (2.73 lbs)", "keyboard": "Backlit Spill-Resistant Keyboard", "webcam": "HD Camera with Privacy Shutter", "os": "Windows 11 Pro 64-bit Licensed"},
            "conditionWarranty": {"condition": "Grade A+ Like New · Certified Refurbished", "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"}
        }
    },
    44: {
        "name": "HP ProBook 430 G8",
        "brandName": "HP",
        "series": "ProBook 430 G8",
        "shortSpecs": {"cpuFamily": "Core i3", "generation": "11th Gen", "ramGb": 8, "storageGb": 256, "storageType": "NVMe SSD", "gpuType": "integrated", "isDedicatedGpu": False},
        "fullSpecs": {
            "performance": {"processor": "Intel Core i3-1115G4", "coresThreads": "2 Cores / 4 Threads", "clocks": "3.00 GHz Base, up to 4.10 GHz Turbo", "cache": "6 MB Intel Smart Cache"},
            "memoryStorage": {"ramSize": "8 GB", "ramType": "DDR4", "ramSpeed": "3200 MHz", "ramSlots": "2x SO-DIMM Slots (Upgradable to 32GB)", "storageSize": "256 GB", "storageType": "NVMe SSD", "interface": "PCIe NVMe M.2 2280", "readSpeed": "Up to 2,200 MB/s"},
            "display": {"size": "13.3\"", "resolution": "FHD (1920 x 1080)", "panelType": "IPS Anti-Glare", "refreshRate": "60 Hz", "touchAntiGlare": "Anti-Glare 250 nits (Non-touch)"},
            "graphics": {"gpuName": "Intel UHD Graphics", "type": "Integrated", "vram": "Shared System Memory"},
            "connectivityPorts": {"ports": "1x USB-C 3.2 Gen 2 (Power Delivery, DisplayPort 1.4), 2x USB-A 3.2 Gen 1 (1 charging), 1x HDMI 1.4b, MicroSD, Audio Jack", "wireless": "Intel Wi-Fi 6 AX201 + Bluetooth 5.0"},
            "batteryBuild": {"battery": "45Wh HP Long Life Fast Charge (50% in 30 mins)", "weight": "1.28 kg (2.81 lbs) Lightweight Aluminum", "keyboard": "HP Spill-Resistant Keyboard", "webcam": "720p HD Privacy Camera", "os": "Windows 11 Pro 64-bit Licensed"},
            "conditionWarranty": {"condition": "Grade A+ Like New · Compact Student / Office", "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"}
        }
    },
    45: {
        "name": "Dell Latitude 7320",
        "brandName": "Dell",
        "series": "Latitude 7320",
        "shortSpecs": {"cpuFamily": "Core i7", "generation": "11th Gen", "ramGb": 16, "storageGb": 512, "storageType": "NVMe SSD", "gpuType": "integrated", "isDedicatedGpu": False},
        "fullSpecs": {
            "performance": {"processor": "Intel Core i7-1185G7 vPro", "coresThreads": "4 Cores / 8 Threads", "clocks": "3.00 GHz Base, up to 4.80 GHz Turbo", "cache": "12 MB Intel Smart Cache"},
            "memoryStorage": {"ramSize": "16 GB", "ramType": "LPDDR4x", "ramSpeed": "4266 MHz", "ramSlots": "Soldered Dual-Channel (Non-upgradable)", "storageSize": "512 GB", "storageType": "NVMe SSD", "interface": "PCIe Gen3 x4 M.2 2280", "readSpeed": "Up to 3,500 MB/s"},
            "display": {"size": "13.3\"", "resolution": "FHD (1920 x 1080)", "panelType": "IPS Super Low Power Anti-Glare", "refreshRate": "60 Hz", "touchAntiGlare": "Anti-Glare 400 nits ComfortView Plus"},
            "graphics": {"gpuName": "Intel Iris Xe Graphics", "type": "Integrated", "vram": "Shared System Memory"},
            "connectivityPorts": {"ports": "2x Thunderbolt 4 USB-C, 1x USB-A 3.2 Gen 1 (PowerShare), 1x HDMI 2.0, MicroSD 4.0, Audio Jack", "wireless": "Intel Wi-Fi 6 AX201 + Bluetooth 5.1"},
            "batteryBuild": {"battery": "63Wh ExpressCharge 4-Cell", "weight": "1.12 kg (2.48 lbs) Carbon Fiber / Aluminum", "keyboard": "Backlit Spill-Resistant Keyboard", "webcam": "FHD IR Camera with Presence Detection & Privacy Shutter", "os": "Windows 11 Pro 64-bit Licensed"},
            "conditionWarranty": {"condition": "Pristine Like New (10/10) · Ultra-Light Executive Flagship", "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"}
        }
    },
    46: {
        "name": "HP EliteBook 845 G7",
        "brandName": "HP",
        "series": "EliteBook 845 G7",
        "shortSpecs": {"cpuFamily": "Ryzen 7", "generation": "4000 Series", "ramGb": 16, "storageGb": 512, "storageType": "NVMe SSD", "gpuType": "integrated", "isDedicatedGpu": False},
        "fullSpecs": {
            "performance": {"processor": "AMD Ryzen 7 PRO 4750U", "coresThreads": "8 Cores / 16 Threads", "clocks": "1.70 GHz Base, up to 4.10 GHz Boost", "cache": "8 MB L3 Cache"},
            "memoryStorage": {"ramSize": "16 GB", "ramType": "DDR4", "ramSpeed": "3200 MHz", "ramSlots": "2x SO-DIMM Slots (Upgradable to 64GB)", "storageSize": "512 GB", "storageType": "NVMe SSD", "interface": "PCIe Gen3 x4 NVMe M.2 2280", "readSpeed": "Up to 3,200 MB/s"},
            "display": {"size": "14.0\"", "resolution": "FHD (1920 x 1080)", "panelType": "IPS Anti-Glare", "refreshRate": "60 Hz", "touchAntiGlare": "Anti-Glare 250 nits / 400 nits Low Power"},
            "graphics": {"gpuName": "AMD Radeon Graphics Vega 7", "type": "Integrated", "vram": "Shared System Memory"},
            "connectivityPorts": {"ports": "2x USB-C 3.1 Gen 2 (DisplayPort/PD), 2x USB-A 3.1 Gen 1 (1 charging), 1x HDMI 2.0, Headphone/mic combo", "wireless": "Intel Wi-Fi 6 AX200 + Bluetooth 5.0"},
            "batteryBuild": {"battery": "53Wh HP Long Life Fast Charge", "weight": "1.33 kg (2.93 lbs) Aluminum Unibody", "keyboard": "HP Premium Spill-Resistant Backlit Keyboard", "webcam": "720p HD Camera with IR Face Recognition & Privacy Shutter", "os": "Windows 11 Pro 64-bit Licensed"},
            "conditionWarranty": {"condition": "Grade A+ Like New · 8-Core Powerhouse", "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"}
        }
    },
    47: {
        "name": "Apple MacBook Pro 14\" (2021)",
        "brandName": "Apple",
        "series": "MacBook Pro 14",
        "shortSpecs": {"cpuFamily": "M1 Pro", "generation": "2021", "ramGb": 16, "storageGb": 512, "storageType": "NVMe SSD", "gpuType": "apple_gpu", "isDedicatedGpu": False},
        "fullSpecs": {
            "performance": {"processor": "Apple M1 Pro Chip (8-Core CPU)", "coresThreads": "6 Performance Cores + 2 Efficiency Cores (8 Cores Total)", "clocks": "Up to 3.22 GHz High-Efficiency Unified Architecture", "cache": "16-Core Neural Engine 200GB/s Memory Bandwidth"},
            "memoryStorage": {"ramSize": "16 GB", "ramType": "Unified Memory", "ramSpeed": "200 GB/s Bandwidth", "ramSlots": "Apple Unified Memory Architecture (Non-upgradable)", "storageSize": "512 GB", "storageType": "Apple High-Speed SSD", "interface": "Custom Integrated Apple Controller", "readSpeed": "Up to 7,400 MB/s"},
            "display": {"size": "14.2\"", "resolution": "Liquid Retina XDR (3024 x 1964) 120Hz", "panelType": "Mini-LED ProMotion Display", "refreshRate": "120 Hz ProMotion", "touchAntiGlare": "1,000 nits sustained, 1,600 nits peak, 1,000,000:1 contrast, True Tone"},
            "graphics": {"gpuName": "Apple 14-Core GPU", "type": "Apple Silicon Integrated GPU", "vram": "Shared Unified Memory (Up to 16GB)"},
            "connectivityPorts": {"ports": "3x Thunderbolt 4 (USB-C), 1x HDMI, SDXC Card Slot, MagSafe 3 Port, 3.5mm Headphone Jack with High-Impedance Support", "wireless": "Wi-Fi 6 (802.11ax) + Bluetooth 5.0"},
            "batteryBuild": {"battery": "70Wh Lithium-Polymer (Up to 17 hours Apple TV playback)", "weight": "1.60 kg (3.5 lbs) 100% Recycled Aluminum Unibody", "keyboard": "Magic Keyboard with Touch ID & Full-Height Function Row", "webcam": "1080p FaceTime HD Camera with Advanced Image Signal Processor", "os": "macOS Sequoia / Sonoma Official Licensed"},
            "conditionWarranty": {"condition": "Pristine Like New (10/10) · 100% Battery Health Grade", "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"}
        }
    },
    48: {
        "name": "HP EliteBook Folio 1020 G1",
        "brandName": "HP",
        "series": "EliteBook Folio 1020",
        "shortSpecs": {"cpuFamily": "Core M", "generation": "5th Gen", "ramGb": 8, "storageGb": 256, "storageType": "SATA SSD", "gpuType": "integrated", "isDedicatedGpu": False},
        "fullSpecs": {
            "performance": {"processor": "Intel Core M-5Y71 Fanless Processor", "coresThreads": "2 Cores / 4 Threads (4.5W Ultra-Low Power)", "clocks": "1.20 GHz Base, up to 2.90 GHz Boost", "cache": "4 MB Intel Smart Cache"},
            "memoryStorage": {"ramSize": "8 GB", "ramType": "LPDDR3", "ramSpeed": "1866 MHz", "ramSlots": "Soldered Dual-Channel (Non-upgradable)", "storageSize": "256 GB", "storageType": "SATA SSD", "interface": "M.2 2280 SATA III SSD", "readSpeed": "Up to 530 MB/s"},
            "display": {"size": "12.5\"", "resolution": "FHD (1920 x 1080)", "panelType": "IPS Ultra-Slim Anti-Glare", "refreshRate": "60 Hz", "touchAntiGlare": "Anti-Glare (Non-touch)"},
            "graphics": {"gpuName": "Intel HD Graphics 5300", "type": "Integrated", "vram": "Shared System Memory"},
            "connectivityPorts": {"ports": "2x USB 3.0 (charging), 1x HDMI, 1x Side Docking Connector, MicroSD, Audio Jack", "wireless": "Intel Dual Band Wireless-AC 7265 + Bluetooth 4.0"},
            "batteryBuild": {"battery": "36Wh 4-Cell Long Life Li-ion (Fanless Zero Noise)", "weight": "1.20 kg (2.68 lbs) CNC Magnesium-Lithium Alloy", "keyboard": "HP Spill-Resistant Backlit Keyboard with ForcePad", "webcam": "720p HD Webcam with Dual-Array Mics", "os": "Windows 10/11 Pro 64-bit Licensed"},
            "conditionWarranty": {"condition": "Grade A Used · Ultra-Thin Fanless Silent", "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"}
        }
    },
    49: {
        "name": "HP EliteBook 630 G10",
        "brandName": "HP",
        "series": "EliteBook 630 G10",
        "shortSpecs": {"cpuFamily": "Core i5", "generation": "13th Gen", "ramGb": 16, "storageGb": 512, "storageType": "NVMe SSD", "gpuType": "integrated", "isDedicatedGpu": False},
        "fullSpecs": {
            "performance": {"processor": "Intel Core i5-1335U", "coresThreads": "10 Cores (2P + 8E) / 12 Threads", "clocks": "1.30 GHz Base, up to 4.60 GHz Turbo", "cache": "12 MB Intel Smart Cache"},
            "memoryStorage": {"ramSize": "16 GB", "ramType": "DDR4", "ramSpeed": "3200 MHz", "ramSlots": "2x SO-DIMM Slots (Upgradable to 64GB)", "storageSize": "512 GB", "storageType": "NVMe SSD", "interface": "PCIe Gen4 x4 NVMe M.2 2280", "readSpeed": "Up to 4,500 MB/s"},
            "display": {"size": "13.3\"", "resolution": "FHD (1920 x 1080)", "panelType": "IPS Anti-Glare", "refreshRate": "60 Hz", "touchAntiGlare": "Anti-Glare 250 nits / 400 nits Low Power"},
            "graphics": {"gpuName": "Intel Iris Xe Graphics", "type": "Integrated", "vram": "Shared System Memory"},
            "connectivityPorts": {"ports": "1x Thunderbolt 4 with USB4 Type-C, 2x USB Type-A 3.2 Gen 1 (1 charging), 1x HDMI 2.1, Headphone/mic combo", "wireless": "Intel Wi-Fi 6E AX211 (2x2) + Bluetooth 5.3"},
            "batteryBuild": {"battery": "51.3Wh HP Long Life Fast Charge (50% in 30 mins)", "weight": "1.22 kg (2.69 lbs) Silver Aluminum", "keyboard": "HP Premium Spill-Resistant Backlit Keyboard", "webcam": "720p HD Privacy Camera with Temporal Noise Reduction", "os": "Windows 11 Pro 64-bit Licensed"},
            "conditionWarranty": {"condition": "Grade A+ Like New · 13th Gen Modern Business", "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"}
        }
    },
    50: {
        "name": "Apple MacBook Pro 14\" (M4 Max)",
        "brandName": "Apple",
        "series": "MacBook Pro 14",
        "shortSpecs": {"cpuFamily": "M4 Max", "generation": "2024", "ramGb": 36, "storageGb": 1000, "storageType": "NVMe SSD", "gpuType": "apple_gpu", "isDedicatedGpu": False},
        "fullSpecs": {
            "performance": {"processor": "Apple M4 Max Chip (14-Core CPU)", "coresThreads": "10 Performance Cores + 4 Efficiency Cores (14 Cores Total)", "clocks": "Next-Gen 3nm Architecture with Hardware-Accelerated Ray Tracing", "cache": "16-Core Neural Engine 410GB/s Memory Bandwidth"},
            "memoryStorage": {"ramSize": "36 GB", "ramType": "Unified Memory", "ramSpeed": "410 GB/s Ultra-High Bandwidth", "ramSlots": "Unified Memory Architecture (Non-upgradable)", "storageSize": "1 TB", "storageType": "Apple Gen5 Class SSD", "interface": "Custom Integrated High-Performance Controller", "readSpeed": "Up to 7,800 MB/s"},
            "display": {"size": "14.2\"", "resolution": "Liquid Retina XDR (3024 x 1964) 120Hz ProMotion", "panelType": "Mini-LED Quantum Dot Nano-Texture Option", "refreshRate": "120 Hz ProMotion", "touchAntiGlare": "1,000 nits SDR, 1,600 nits peak HDR, 1,000,000:1 contrast ratio"},
            "graphics": {"gpuName": "Apple 32-Core GPU", "type": "Apple Silicon Flagship GPU with Ray Tracing", "vram": "Shared Unified Memory (Up to 36GB)"},
            "connectivityPorts": {"ports": "3x Thunderbolt 5 (USB-C up to 120Gbps), 1x HDMI (up to 8K), SDXC Card Slot, MagSafe 3 Port, 3.5mm Headphone Jack", "wireless": "Wi-Fi 6E (802.11ax) + Bluetooth 5.3"},
            "batteryBuild": {"battery": "72.4Wh Lithium-Polymer (Up to 18 hours battery life)", "weight": "1.62 kg (3.57 lbs) Space Black Anodized Aluminum", "keyboard": "Magic Keyboard with Touch ID & Ambient Light Sensor", "webcam": "12MP Center Stage Camera with Desk View Support", "os": "macOS Sequoia Licensed"},
            "conditionWarranty": {"condition": "Pristine Open Box / Brand New Condition (10/10)", "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"}
        }
    },
    51: {
        "name": "HP Envy x360 13",
        "brandName": "HP",
        "series": "Envy x360 13",
        "shortSpecs": {"cpuFamily": "Core i7", "generation": "8th Gen", "ramGb": 16, "storageGb": 512, "storageType": "NVMe SSD", "gpuType": "integrated", "isDedicatedGpu": False},
        "fullSpecs": {
            "performance": {"processor": "Intel Core i7-8550U Quad Core", "coresThreads": "4 Cores / 8 Threads", "clocks": "1.80 GHz Base, up to 4.00 GHz Boost", "cache": "8 MB Intel Smart Cache"},
            "memoryStorage": {"ramSize": "16 GB", "ramType": "LPDDR3", "ramSpeed": "2133 MHz", "ramSlots": "Soldered Dual-Channel (Non-upgradable)", "storageSize": "512 GB", "storageType": "NVMe SSD", "interface": "PCIe Gen3 x4 M.2 2280", "readSpeed": "Up to 2,800 MB/s"},
            "display": {"size": "13.3\"", "resolution": "FHD (1920 x 1080) IPS", "panelType": "Corning Gorilla Glass Touch 360°", "refreshRate": "60 Hz", "touchAntiGlare": "BrightView Glass Touch with Active Stylus Support"},
            "graphics": {"gpuName": "Intel UHD Graphics 620", "type": "Integrated", "vram": "Shared System Memory"},
            "connectivityPorts": {"ports": "1x USB-C 3.1 Gen 1 (DisplayPort/PD), 2x USB 3.1 Gen 1 (1 HP Sleep and Charge), MicroSD, Audio Jack", "wireless": "Intel 802.11b/g/n/ac + Bluetooth 4.2"},
            "batteryBuild": {"battery": "53.2Wh HP Fast Charge (50% in 45 mins)", "weight": "1.30 kg (2.87 lbs) CNC Aluminum", "keyboard": "Full-size Island-style Backlit Keyboard", "webcam": "HP Wide Vision HD Camera with Bang & Olufsen Quad Speakers", "os": "Windows 11 Pro 64-bit Licensed"},
            "conditionWarranty": {"condition": "Grade A+ Like New · Sleek All-Metal Convertible", "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"}
        }
    },
    52: {
        "name": "HP Spectre x360 13",
        "brandName": "HP",
        "series": "Spectre x360 13",
        "shortSpecs": {"cpuFamily": "Core i7", "generation": "8th Gen", "ramGb": 16, "storageGb": 512, "storageType": "NVMe SSD", "gpuType": "integrated", "isDedicatedGpu": False},
        "fullSpecs": {
            "performance": {"processor": "Intel Core i7-8565U Quad Core (Whiskey Lake)", "coresThreads": "4 Cores / 8 Threads", "clocks": "1.80 GHz Base, up to 4.60 GHz Turbo Boost", "cache": "8 MB Intel Smart Cache"},
            "memoryStorage": {"ramSize": "16 GB", "ramType": "LPDDR3", "ramSpeed": "2133 MHz", "ramSlots": "Soldered Dual-Channel (Non-upgradable)", "storageSize": "512 GB", "storageType": "NVMe SSD", "interface": "PCIe Gen3 x4 M.2 2280", "readSpeed": "Up to 3,200 MB/s"},
            "display": {"size": "13.3\"", "resolution": "4K UHD (3840 x 2160) AMOLED / FHD IPS Touch", "panelType": "AMOLED / IPS BrightView Touchscreen 360°", "refreshRate": "60 Hz", "touchAntiGlare": "Corning Gorilla Glass NBT Touch with HP Tilt Pen Support"},
            "graphics": {"gpuName": "Intel UHD Graphics 620", "type": "Integrated", "vram": "Shared System Memory"},
            "connectivityPorts": {"ports": "2x Thunderbolt 3 (USB-C with Power Delivery), 1x USB-A 3.1 Gen 2 (HP Sleep and Charge), MicroSD, Headphone Jack", "wireless": "Intel Wireless-AC 9560 802.11ac + Bluetooth 5.0"},
            "batteryBuild": {"battery": "61Wh HP Long Life Fast Charge (50% in 30 mins)", "weight": "1.32 kg (2.91 lbs) Iconic Gem-Cut CNC Aluminum Chassis", "keyboard": "Edge-to-Edge Backlit Keyboard with Bang & Olufsen Quad Speakers", "webcam": "HP Wide Vision FHD IR Camera with Privacy Kill Switch", "os": "Windows 11 Pro 64-bit Licensed"},
            "conditionWarranty": {"condition": "Pristine Like New (10/10) · Luxury Gem-Cut Masterpiece", "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"}
        }
    },
    53: {
        "name": "Microsoft Surface Laptop Go",
        "brandName": "Microsoft",
        "series": "Surface Laptop Go",
        "shortSpecs": {"cpuFamily": "Core i5", "generation": "10th Gen", "ramGb": 8, "storageGb": 256, "storageType": "NVMe SSD", "gpuType": "integrated", "isDedicatedGpu": False},
        "fullSpecs": {
            "performance": {"processor": "Intel Core i5-1035G1", "coresThreads": "4 Cores / 8 Threads", "clocks": "1.00 GHz Base, up to 3.60 GHz Boost", "cache": "6 MB Intel Smart Cache"},
            "memoryStorage": {"ramSize": "8 GB", "ramType": "LPDDR4x", "ramSpeed": "3733 MHz", "ramSlots": "Soldered (Non-upgradable)", "storageSize": "256 GB", "storageType": "NVMe SSD", "interface": "PCIe NVMe M.2 2230", "readSpeed": "Up to 2,000 MB/s"},
            "display": {"size": "12.4\"", "resolution": "1.5K (1536 x 1024) 3:2 Aspect Ratio", "panelType": "PixelSense 10-Point Multi-Touch", "refreshRate": "60 Hz", "touchAntiGlare": "Corning Gorilla Glass Touch, 300 nits"},
            "graphics": {"gpuName": "Intel UHD Graphics", "type": "Integrated", "vram": "Shared System Memory"},
            "connectivityPorts": {"ports": "1x USB-C 3.1, 1x USB-A 3.1, 3.5mm Headphone Jack, Surface Connect Port", "wireless": "Wi-Fi 6 (802.11ax) + Bluetooth 5.0"},
            "batteryBuild": {"battery": "40Wh Fast Charging (80% in about 1 hour)", "weight": "1.11 kg (2.45 lbs) Ultra-Lightweight Aluminum/Resin", "keyboard": "Precision Keyboard with Fingerprint Power Button Windows Hello", "webcam": "720p HD f/2.0 Camera with Omnisonic Speakers & Dolby Audio", "os": "Windows 11 Pro 64-bit Licensed"},
            "conditionWarranty": {"condition": "Pristine Like New (10/10) · Featherlight Grab-and-Go", "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"}
        }
    },
    54: {
        "name": "Lenovo Yoga Slim 7 14",
        "brandName": "Lenovo",
        "series": "Yoga Slim 7",
        "shortSpecs": {"cpuFamily": "Core i7", "generation": "10th Gen", "ramGb": 16, "storageGb": 512, "storageType": "NVMe SSD", "gpuType": "integrated", "isDedicatedGpu": False},
        "fullSpecs": {
            "performance": {"processor": "Intel Core i7-1065G7 (Iris Plus G7)", "coresThreads": "4 Cores / 8 Threads", "clocks": "1.30 GHz Base, up to 3.90 GHz Boost", "cache": "8 MB Intel Smart Cache"},
            "memoryStorage": {"ramSize": "16 GB", "ramType": "LPDDR4x", "ramSpeed": "3200 MHz", "ramSlots": "Soldered Dual-Channel (Non-upgradable)", "storageSize": "512 GB", "storageType": "NVMe SSD", "interface": "PCIe Gen3 x4 M.2 2280", "readSpeed": "Up to 3,200 MB/s"},
            "display": {"size": "14.0\"", "resolution": "FHD (1920 x 1080) 100% sRGB", "panelType": "IPS Anti-Glare 300 nits", "refreshRate": "60 Hz", "touchAntiGlare": "Anti-Glare (Non-touch) / Dolby Vision"},
            "graphics": {"gpuName": "Intel Iris Plus Graphics", "type": "Integrated", "vram": "Shared System Memory"},
            "connectivityPorts": {"ports": "1x USB-C (Thunderbolt 3/PD/DisplayPort), 1x USB-C (Power Delivery), 2x USB-A 3.2 Gen 1, 1x HDMI 2.0b, MicroSD, Audio Jack", "wireless": "Wi-Fi 6 (802.11ax) + Bluetooth 5.0"},
            "batteryBuild": {"battery": "60.7Wh Rapid Charge Pro (Up to 14 hours)", "weight": "1.36 kg (2.99 lbs) Slim Slate Grey All-Metal", "keyboard": "Backlit Keyboard with Front-Facing Dolby Atmos Speakers", "webcam": "IR Camera with Time-of-Flight Presence Sensor & Windows Hello", "os": "Windows 11 Pro 64-bit Licensed"},
            "conditionWarranty": {"condition": "Grade A+ Like New · Premium Ultra-Slim", "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"}
        }
    },
    55: {
        "name": "HP Spectre x360 14 (2024)",
        "brandName": "HP",
        "series": "Spectre x360 14",
        "shortSpecs": {"cpuFamily": "Core Ultra 7", "generation": "Series 1 (AI PC)", "ramGb": 16, "storageGb": 1000, "storageType": "NVMe SSD", "gpuType": "integrated", "isDedicatedGpu": False},
        "fullSpecs": {
            "performance": {"processor": "Intel Core Ultra 7 155H (Meteor Lake AI PC)", "coresThreads": "16 Cores (6P + 8E + 2 Low-Power E) / 22 Threads", "clocks": "Up to 4.80 GHz Boost with Dedicated Intel AI Boost NPU", "cache": "24 MB Intel Smart Cache"},
            "memoryStorage": {"ramSize": "16 GB", "ramType": "LPDDR5x", "ramSpeed": "7467 MHz", "ramSlots": "Soldered Ultra-Fast (Non-upgradable)", "storageSize": "1 TB", "storageType": "NVMe SSD", "interface": "PCIe Gen4 x4 NVMe M.2 2280", "readSpeed": "Up to 6,800 MB/s"},
            "display": {"size": "14.0\"", "resolution": "2.8K (2880 x 1800) 120Hz OLED 16:10", "panelType": "OLED Touchscreen 360° Convertible (0.2ms)", "refreshRate": "120 Hz Variable (48-120Hz)", "touchAntiGlare": "Corning Gorilla Glass Touch with Active Rechargeable Tilt Pen, 500 nits HDR, 100% DCI-P3"},
            "graphics": {"gpuName": "Intel Arc Graphics (Built-in)", "type": "Integrated Arc Architecture", "vram": "Shared System Memory"},
            "connectivityPorts": {"ports": "2x Thunderbolt 4 USB-C (Power Delivery, DisplayPort 2.1), 1x USB-A 10Gbps (HP Sleep and Charge), Headphone/mic combo", "wireless": "Intel Wi-Fi 7 BE200 + Bluetooth 5.4"},
            "batteryBuild": {"battery": "68Wh HP Fast Charge (50% in 45 mins, up to 13 hrs)", "weight": "1.44 kg (3.19 lbs) CNC Nightfall Black / Slate Blue", "keyboard": "Backlit Keyboard with Poly Studio Quad Speakers", "webcam": "9MP AI IR Camera with Auto Frame & Hardware Shutter", "os": "Windows 11 Pro 64-bit Licensed"},
            "conditionWarranty": {"condition": "Pristine Like New (10/10) · Latest AI PC Flagship", "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"}
        }
    },
    56: {
        "name": "Dell XPS 13 9310",
        "brandName": "Dell",
        "series": "XPS 13",
        "shortSpecs": {"cpuFamily": "Core i5", "generation": "11th Gen", "ramGb": 16, "storageGb": 512, "storageType": "NVMe SSD", "gpuType": "integrated", "isDedicatedGpu": False},
        "fullSpecs": {
            "performance": {"processor": "Intel Core i5-1135G7", "coresThreads": "4 Cores / 8 Threads", "clocks": "2.40 GHz Base, up to 4.20 GHz Turbo", "cache": "8 MB Intel Smart Cache"},
            "memoryStorage": {"ramSize": "16 GB", "ramType": "LPDDR4x", "ramSpeed": "4267 MHz", "ramSlots": "Soldered Dual-Channel (Non-upgradable)", "storageSize": "512 GB", "storageType": "NVMe SSD", "interface": "PCIe Gen3 x4 M.2 2280", "readSpeed": "Up to 3,400 MB/s"},
            "display": {"size": "13.4\"", "resolution": "FHD+ (1920 x 1200) 16:10", "panelType": "InfinityEdge IPS Anti-Glare", "refreshRate": "60 Hz", "touchAntiGlare": "Anti-Glare 500 nits 100% sRGB (Non-touch)"},
            "graphics": {"gpuName": "Intel Iris Xe Graphics", "type": "Integrated", "vram": "Shared System Memory"},
            "connectivityPorts": {"ports": "2x Thunderbolt 4 USB-C (Power Delivery and DisplayPort), MicroSD Card Reader, 3.5mm Headphone Jack", "wireless": "Killer Wi-Fi 6 AX1650 (2x2) + Bluetooth 5.1"},
            "batteryBuild": {"battery": "52Wh Integrated Lithium-Ion", "weight": "1.20 kg (2.64 lbs) CNC Platinum Silver & Carbon Fiber", "keyboard": "Edge-to-Edge Backlit Keyboard with Glass Precision Touchpad", "webcam": "HD (720p) 2.25mm Camera with Windows Hello IR Facial Recognition", "os": "Windows 11 Pro 64-bit Licensed"},
            "conditionWarranty": {"condition": "Pristine Like New (10/10) · Ultra-Compact Bezel-less", "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"}
        }
    },
    57: {
        "name": "Lenovo ThinkPad L13 Gen 2",
        "brandName": "Lenovo",
        "series": "ThinkPad L13",
        "shortSpecs": {"cpuFamily": "Core i5", "generation": "11th Gen", "ramGb": 16, "storageGb": 512, "storageType": "NVMe SSD", "gpuType": "integrated", "isDedicatedGpu": False},
        "fullSpecs": {
            "performance": {"processor": "Intel Core i5-1135G7", "coresThreads": "4 Cores / 8 Threads", "clocks": "2.40 GHz Base, up to 4.20 GHz Turbo", "cache": "8 MB Intel Smart Cache"},
            "memoryStorage": {"ramSize": "16 GB", "ramType": "DDR4", "ramSpeed": "3200 MHz", "ramSlots": "Soldered Dual-Channel (Non-upgradable)", "storageSize": "512 GB", "storageType": "NVMe SSD", "interface": "PCIe Gen3 x4 M.2 2280", "readSpeed": "Up to 3,200 MB/s"},
            "display": {"size": "13.3\"", "resolution": "FHD (1920 x 1080)", "panelType": "IPS Anti-Glare", "refreshRate": "60 Hz", "touchAntiGlare": "Anti-Glare 250 nits (Non-touch)"},
            "graphics": {"gpuName": "Intel Iris Xe Graphics", "type": "Integrated", "vram": "Shared System Memory"},
            "connectivityPorts": {"ports": "1x Thunderbolt 4 USB-C, 1x USB-C 3.2 Gen 2, 2x USB-A 3.2 Gen 1 (1 Always On), 1x HDMI 2.0, MicroSD, Audio Jack", "wireless": "Intel Wi-Fi 6 AX201 + Bluetooth 5.1"},
            "batteryBuild": {"battery": "46Wh Rapid Charge (80% in 1 hr)", "weight": "1.39 kg (3.06 lbs)", "keyboard": "ThinkPad Spill-Resistant Backlit Keyboard with TrackPoint", "webcam": "720p HD with ThinkShutter Privacy Cover", "os": "Windows 11 Pro 64-bit Licensed"},
            "conditionWarranty": {"condition": "Grade A+ Like New · Certified Business Ultrabook", "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"}
        }
    },
    58: {
        "name": "Microsoft Surface Laptop 3 13.5\"",
        "brandName": "Microsoft",
        "series": "Surface Laptop 3",
        "shortSpecs": {"cpuFamily": "Core i5", "generation": "10th Gen", "ramGb": 8, "storageGb": 256, "storageType": "NVMe SSD", "gpuType": "integrated", "isDedicatedGpu": False},
        "fullSpecs": {
            "performance": {"processor": "Intel Core i5-1035G7", "coresThreads": "4 Cores / 8 Threads", "clocks": "1.20 GHz Base, up to 3.70 GHz Boost", "cache": "6 MB Intel Smart Cache"},
            "memoryStorage": {"ramSize": "8 GB", "ramType": "LPDDR4x", "ramSpeed": "3733 MHz", "ramSlots": "Soldered (Non-upgradable)", "storageSize": "256 GB", "storageType": "NVMe SSD", "interface": "Removable M.2 2230 NVMe SSD", "readSpeed": "Up to 2,200 MB/s"},
            "display": {"size": "13.5\"", "resolution": "2.2K (2256 x 1504) 3:2 Aspect Ratio", "panelType": "PixelSense 10-Point Multi-Touch", "refreshRate": "60 Hz", "touchAntiGlare": "Corning Gorilla Glass 3 Touch with Surface Pen Support"},
            "graphics": {"gpuName": "Intel Iris Plus Graphics", "type": "Integrated", "vram": "Shared System Memory"},
            "connectivityPorts": {"ports": "1x USB-C 3.1, 1x USB-A 3.1, 3.5mm Headphone Jack, Surface Connect Port", "wireless": "Wi-Fi 6 (802.11ax) + Bluetooth 5.0"},
            "batteryBuild": {"battery": "45Wh Fast Charging (80% in 1 hr)", "weight": "1.26 kg (2.79 lbs) Matte Black Metal Chassis", "keyboard": "Backlit Keyboard with Large Precision Glass Touchpad", "webcam": "720p HD f/2.0 with Windows Hello Face Sign-in", "os": "Windows 11 Pro 64-bit Licensed"},
            "conditionWarranty": {"condition": "Pristine Like New (10/10) · All-Metal Edition", "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"}
        }
    },
    59: {
        "name": "HP EliteBook 845 G7",
        "brandName": "HP",
        "series": "EliteBook 845 G7",
        "shortSpecs": {"cpuFamily": "Ryzen 5", "generation": "4000 Series", "ramGb": 16, "storageGb": 512, "storageType": "NVMe SSD", "gpuType": "integrated", "isDedicatedGpu": False},
        "fullSpecs": {
            "performance": {"processor": "AMD Ryzen 5 PRO 4650U", "coresThreads": "6 Cores / 12 Threads", "clocks": "2.10 GHz Base, up to 4.00 GHz Boost", "cache": "8 MB L3 Cache"},
            "memoryStorage": {"ramSize": "16 GB", "ramType": "DDR4", "ramSpeed": "3200 MHz", "ramSlots": "2x SO-DIMM Slots (Upgradable to 64GB)", "storageSize": "512 GB", "storageType": "NVMe SSD", "interface": "PCIe Gen3 x4 NVMe M.2 2280", "readSpeed": "Up to 3,200 MB/s"},
            "display": {"size": "14.0\"", "resolution": "FHD (1920 x 1080)", "panelType": "IPS Anti-Glare", "refreshRate": "60 Hz", "touchAntiGlare": "Anti-Glare 250 nits / 400 nits Low Power"},
            "graphics": {"gpuName": "AMD Radeon Vega 6 Graphics", "type": "Integrated", "vram": "Shared System Memory"},
            "connectivityPorts": {"ports": "2x USB-C 3.1 Gen 2 (DisplayPort/PD), 2x USB-A 3.1 Gen 1 (1 charging), 1x HDMI 2.0, Audio combo", "wireless": "Intel Wi-Fi 6 AX200 + Bluetooth 5.0"},
            "batteryBuild": {"battery": "53Wh HP Long Life Fast Charge (50% in 30 mins)", "weight": "1.33 kg (2.93 lbs) Aluminum Chassis", "keyboard": "HP Premium Spill-Resistant Backlit Keyboard", "webcam": "720p HD IR Camera with Bang & Olufsen Dual Stereo Speakers", "os": "Windows 11 Pro 64-bit Licensed"},
            "conditionWarranty": {"condition": "Grade A+ Like New · Certified Refurbished", "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"}
        }
    },
    60: {
        "name": "HP ProBook 640 G10",
        "brandName": "HP",
        "series": "ProBook 640 G10",
        "shortSpecs": {"cpuFamily": "Core i5", "generation": "13th Gen", "ramGb": 16, "storageGb": 512, "storageType": "NVMe SSD", "gpuType": "integrated", "isDedicatedGpu": False},
        "fullSpecs": {
            "performance": {"processor": "Intel Core i5-1335U", "coresThreads": "10 Cores (2P + 8E) / 12 Threads", "clocks": "1.30 GHz Base, up to 4.60 GHz Turbo", "cache": "12 MB Intel Smart Cache"},
            "memoryStorage": {"ramSize": "16 GB", "ramType": "DDR4", "ramSpeed": "3200 MHz", "ramSlots": "2x SO-DIMM Slots (Upgradable to 64GB)", "storageSize": "512 GB", "storageType": "NVMe SSD", "interface": "PCIe Gen4 x4 NVMe M.2 2280", "readSpeed": "Up to 4,800 MB/s"},
            "display": {"size": "14.0\"", "resolution": "FHD (1920 x 1080)", "panelType": "IPS Anti-Glare", "refreshRate": "60 Hz", "touchAntiGlare": "Anti-Glare 250 nits / 400 nits (Non-touch)"},
            "graphics": {"gpuName": "Intel Iris Xe Graphics", "type": "Integrated", "vram": "Shared System Memory"},
            "connectivityPorts": {"ports": "1x Thunderbolt 4 USB4 Type-C, 3x USB Type-A 3.2 Gen 1 (1 charging), 1x HDMI 2.1, RJ-45 Gigabit, Headphone/mic combo", "wireless": "Intel Wi-Fi 6E AX211 + Bluetooth 5.3"},
            "batteryBuild": {"battery": "51.3Wh HP Long Life Fast Charge (50% in 30 mins)", "weight": "1.37 kg (3.03 lbs) Silver Aluminum", "keyboard": "HP Premium Spill-Resistant Backlit Keyboard", "webcam": "720p HD Privacy Camera with Temporal Noise Reduction", "os": "Windows 11 Pro 64-bit Licensed"},
            "conditionWarranty": {"condition": "Grade A+ Like New · Current Generation Corporate", "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"}
        }
    },
    61: {
        "name": "Dell Latitude 5320",
        "brandName": "Dell",
        "series": "Latitude 5320",
        "shortSpecs": {"cpuFamily": "Core i3", "generation": "11th Gen", "ramGb": 8, "storageGb": 256, "storageType": "NVMe SSD", "gpuType": "integrated", "isDedicatedGpu": False},
        "fullSpecs": {
            "performance": {"processor": "Intel Core i3-1125G4", "coresThreads": "4 Cores / 8 Threads (Rare 4-Core i3)", "clocks": "2.00 GHz Base, up to 3.70 GHz Turbo", "cache": "8 MB Intel Smart Cache"},
            "memoryStorage": {"ramSize": "8 GB", "ramType": "DDR4", "ramSpeed": "3200 MHz", "ramSlots": "Soldered Dual-Channel (Non-upgradable)", "storageSize": "256 GB", "storageType": "NVMe SSD", "interface": "PCIe Gen3 x4 M.2 2280", "readSpeed": "Up to 2,400 MB/s"},
            "display": {"size": "13.3\"", "resolution": "FHD (1920 x 1080)", "panelType": "IPS Anti-Glare", "refreshRate": "60 Hz", "touchAntiGlare": "Anti-Glare (Non-touch), 250 nits"},
            "graphics": {"gpuName": "Intel UHD Graphics", "type": "Integrated", "vram": "Shared System Memory"},
            "connectivityPorts": {"ports": "2x Thunderbolt 4 USB-C (Power Delivery/DisplayPort), 2x USB-A 3.2 Gen 1 (1 PowerShare), 1x HDMI 2.0, MicroSD, Audio Jack", "wireless": "Intel Wi-Fi 6 AX201 + Bluetooth 5.1"},
            "batteryBuild": {"battery": "42Wh / 63Wh ExpressCharge Capable", "weight": "1.20 kg (2.65 lbs)", "keyboard": "Backlit Spill-Resistant Keyboard", "webcam": "720p HD with Privacy Shutter", "os": "Windows 11 Pro 64-bit Licensed"},
            "conditionWarranty": {"condition": "Grade A+ Like New · Fast Quad-Core Budget Ultrabook", "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"}
        }
    },
    62: {
        "name": "Microsoft Surface Laptop 4 13.5\"",
        "brandName": "Microsoft",
        "series": "Surface Laptop 4",
        "shortSpecs": {"cpuFamily": "Core i5", "generation": "11th Gen", "ramGb": 16, "storageGb": 512, "storageType": "NVMe SSD", "gpuType": "integrated", "isDedicatedGpu": False},
        "fullSpecs": {
            "performance": {"processor": "Intel Core i5-1135G7", "coresThreads": "4 Cores / 8 Threads", "clocks": "2.40 GHz Base, up to 4.20 GHz Turbo", "cache": "8 MB Intel Smart Cache"},
            "memoryStorage": {"ramSize": "16 GB", "ramType": "LPDDR4x", "ramSpeed": "4267 MHz", "ramSlots": "Soldered Dual-Channel (Non-upgradable)", "storageSize": "512 GB", "storageType": "NVMe SSD", "interface": "Removable M.2 2230 NVMe SSD", "readSpeed": "Up to 3,200 MB/s"},
            "display": {"size": "13.5\"", "resolution": "2.2K (2256 x 1504) 3:2 Aspect Ratio", "panelType": "PixelSense 10-Point Multi-Touch", "refreshRate": "60 Hz", "touchAntiGlare": "Corning Gorilla Glass 3 Touch with Surface Pen Support, 400 nits"},
            "graphics": {"gpuName": "Intel Iris Xe Graphics", "type": "Integrated", "vram": "Shared System Memory"},
            "connectivityPorts": {"ports": "1x USB-C 3.1 Gen 2, 1x USB-A 3.1 Gen 2, 3.5mm Headphone Jack, Surface Connect Port", "wireless": "Wi-Fi 6 (802.11ax) + Bluetooth 5.0"},
            "batteryBuild": {"battery": "47.4Wh Fast Charging (Up to 17 hours)", "weight": "1.28 kg (2.84 lbs) Matte Black Aluminum", "keyboard": "Backlit Keyboard with Large Precision Glass Trackpad", "webcam": "720p HD f/2.0 with Windows Hello & Omnisonic Speakers with Dolby Atmos", "os": "Windows 11 Pro 64-bit Licensed"},
            "conditionWarranty": {"condition": "Pristine Like New (10/10) · Premium Sleek Laptop", "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"}
        }
    },
    63: {
        "name": "Microsoft Surface Laptop 4 15\"",
        "brandName": "Microsoft",
        "series": "Surface Laptop 4",
        "shortSpecs": {"cpuFamily": "Core i7", "generation": "11th Gen", "ramGb": 16, "storageGb": 512, "storageType": "NVMe SSD", "gpuType": "integrated", "isDedicatedGpu": False},
        "fullSpecs": {
            "performance": {"processor": "Intel Core i7-1185G7", "coresThreads": "4 Cores / 8 Threads", "clocks": "3.00 GHz Base, up to 4.80 GHz Turbo", "cache": "12 MB Intel Smart Cache"},
            "memoryStorage": {"ramSize": "16 GB", "ramType": "LPDDR4x", "ramSpeed": "4267 MHz", "ramSlots": "Soldered Dual-Channel (Non-upgradable)", "storageSize": "512 GB", "storageType": "NVMe SSD", "interface": "Removable M.2 2230 NVMe SSD", "readSpeed": "Up to 3,500 MB/s"},
            "display": {"size": "15.0\"", "resolution": "2.5K (2496 x 1664) 3:2 Aspect Ratio", "panelType": "PixelSense 10-Point Multi-Touch", "refreshRate": "60 Hz", "touchAntiGlare": "Corning Gorilla Glass 3 Touch with Surface Pen Support, 400 nits"},
            "graphics": {"gpuName": "Intel Iris Xe Graphics", "type": "Integrated", "vram": "Shared System Memory"},
            "connectivityPorts": {"ports": "1x USB-C 3.1 Gen 2, 1x USB-A 3.1 Gen 2, 3.5mm Headphone Jack, Surface Connect Port", "wireless": "Wi-Fi 6 (802.11ax) + Bluetooth 5.0"},
            "batteryBuild": {"battery": "47.4Wh Fast Charging (Up to 16.5 hours)", "weight": "1.54 kg (3.40 lbs) Matte Black All-Metal Unibody", "keyboard": "Backlit Keyboard with Large Glass Touchpad", "webcam": "720p HD with Windows Hello Facial Authentication", "os": "Windows 11 Pro 64-bit Licensed"},
            "conditionWarranty": {"condition": "Pristine Like New (10/10) · Big Screen Premium Productivity", "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"}
        }
    },
    64: {
        "name": "Dell XPS 15 9500",
        "brandName": "Dell",
        "series": "XPS 15",
        "shortSpecs": {"cpuFamily": "Core i7", "generation": "10th Gen", "ramGb": 16, "storageGb": 512, "storageType": "NVMe SSD", "gpuType": "discrete", "isDedicatedGpu": True},
        "fullSpecs": {
            "performance": {"processor": "Intel Core i7-10750H (45W High-Performance)", "coresThreads": "6 Cores / 12 Threads", "clocks": "2.60 GHz Base, up to 5.00 GHz Max Turbo", "cache": "12 MB Intel Smart Cache"},
            "memoryStorage": {"ramSize": "16 GB", "ramType": "DDR4", "ramSpeed": "2933 MHz", "ramSlots": "2x SO-DIMM Slots (Upgradable to 64GB)", "storageSize": "512 GB", "storageType": "NVMe SSD", "interface": "Dual M.2 PCIe Gen3 x4 NVMe Slots", "readSpeed": "Up to 3,500 MB/s"},
            "display": {"size": "15.6\"", "resolution": "FHD+ (1920 x 1200) 16:10 500 nits InfinityEdge", "panelType": "IPS Anti-Glare 100% sRGB", "refreshRate": "60 Hz", "touchAntiGlare": "Anti-Glare 500 nits 4-sided InfinityEdge (Non-touch)"},
            "graphics": {"gpuName": "NVIDIA GeForce GTX 1650 Ti", "type": "Dedicated", "vram": "4 GB GDDR6 Dedicated"},
            "connectivityPorts": {"ports": "2x Thunderbolt 3 (Power Delivery and DisplayPort), 1x USB-C 3.1 (PD/DisplayPort), Full-size SD Card Reader v6.0, 3.5mm Headphone Jack", "wireless": "Killer Wi-Fi 6 AX1650 (2x2) + Bluetooth 5.1"},
            "batteryBuild": {"battery": "86Wh 6-Cell Lithium-Ion ExpressCharge", "weight": "1.83 kg (4.0 lbs) CNC Platinum Silver Aluminum with Carbon Fiber Palmrest", "keyboard": "Backlit Keyboard with Huge Glass Precision Touchpad", "webcam": "720p HD with Dual-Array Digital Mics & Windows Hello IR", "os": "Windows 11 Pro 64-bit Licensed"},
            "conditionWarranty": {"condition": "Pristine Like New (10/10) · Creator Flagship", "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"}
        }
    },
    65: {
        "name": "Lenovo ThinkPad T490s",
        "brandName": "Lenovo",
        "series": "ThinkPad T490s",
        "shortSpecs": {"cpuFamily": "Core i5", "generation": "8th Gen", "ramGb": 16, "storageGb": 512, "storageType": "NVMe SSD", "gpuType": "integrated", "isDedicatedGpu": False},
        "fullSpecs": {
            "performance": {"processor": "Intel Core i5-8365U vPro Quad Core", "coresThreads": "4 Cores / 8 Threads", "clocks": "1.60 GHz Base, up to 4.10 GHz Boost", "cache": "6 MB Intel Smart Cache"},
            "memoryStorage": {"ramSize": "16 GB", "ramType": "DDR4", "ramSpeed": "2400 MHz", "ramSlots": "Soldered Dual-Channel (Non-upgradable)", "storageSize": "512 GB", "storageType": "NVMe SSD", "interface": "PCIe Gen3 x4 M.2 2280", "readSpeed": "Up to 3,200 MB/s"},
            "display": {"size": "14.0\"", "resolution": "FHD (1920 x 1080) Low Power 400 nits", "panelType": "IPS Anti-Glare", "refreshRate": "60 Hz", "touchAntiGlare": "Anti-Glare (Non-touch), 400 nits Low Power 72% NTSC"},
            "graphics": {"gpuName": "Intel UHD Graphics 620", "type": "Integrated", "vram": "Shared System Memory"},
            "connectivityPorts": {"ports": "1x USB-C 3.1 Gen 1 (PD/DisplayPort), 1x Thunderbolt 3, 2x USB-A 3.1 Gen 1 (1 Always On), HDMI 1.4b, MicroSD, Audio Jack", "wireless": "Intel Wireless-AC 9560 802.11ac + Bluetooth 5.0"},
            "batteryBuild": {"battery": "57Wh Rapid Charge (80% in 1 hr)", "weight": "1.35 kg (2.98 lbs) Magnesium/Carbon-Fiber", "keyboard": "ThinkPad Precision Backlit Keyboard with TrackPoint", "webcam": "720p HD with ThinkShutter Privacy Cover", "os": "Windows 11 Pro 64-bit Licensed"},
            "conditionWarranty": {"condition": "Grade A+ Like New · 400 Nits Low-Power Display", "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"}
        }
    },
    66: {
        "name": "Apple MacBook Air 13\" (M2)",
        "brandName": "Apple",
        "series": "MacBook Air M2",
        "shortSpecs": {"cpuFamily": "M2", "generation": "2022", "ramGb": 16, "storageGb": 512, "storageType": "NVMe SSD", "gpuType": "apple_gpu", "isDedicatedGpu": False},
        "fullSpecs": {
            "performance": {"processor": "Apple M2 Chip (8-Core CPU)", "coresThreads": "4 Performance Cores + 4 Efficiency Cores (8 Cores Total)", "clocks": "Up to 3.49 GHz Next-Gen Apple Silicon", "cache": "16-Core Neural Engine 100GB/s Memory Bandwidth"},
            "memoryStorage": {"ramSize": "16 GB", "ramType": "Unified Memory", "ramSpeed": "100 GB/s Bandwidth", "ramSlots": "Unified Memory Architecture (Non-upgradable)", "storageSize": "512 GB", "storageType": "Apple High-Speed SSD", "interface": "Custom Integrated Apple Controller", "readSpeed": "Up to 3,500 MB/s"},
            "display": {"size": "13.6\"", "resolution": "Liquid Retina (2560 x 1664) 500 nits", "panelType": "Liquid Retina with P3 Wide Color", "refreshRate": "60 Hz", "touchAntiGlare": "500 nits Brightness with True Tone Technology"},
            "graphics": {"gpuName": "Apple 8-Core GPU", "type": "Apple Silicon Integrated GPU", "vram": "Shared Unified Memory (Up to 16GB)"},
            "connectivityPorts": {"ports": "MagSafe 3 Charging Port, 2x Thunderbolt / USB 4 Ports, 3.5mm Headphone Jack with High-Impedance Support", "wireless": "Wi-Fi 6 (802.11ax) + Bluetooth 5.3"},
            "batteryBuild": {"battery": "52.6Wh Lithium-Polymer (Up to 18 hours battery life, Fanless Zero Noise)", "weight": "1.24 kg (2.7 lbs) Ultra-Thin 11.3mm Aluminum Unibody", "keyboard": "Magic Keyboard with Touch ID & Ambient Light Sensor", "webcam": "1080p FaceTime HD Camera with Four-Speaker Sound System Spatial Audio", "os": "macOS Sequoia / Sonoma Official Licensed"},
            "conditionWarranty": {"condition": "Pristine Like New (10/10) · Fanless Silent Design", "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"}
        }
    },
    67: {
        "name": "Dell Latitude 7430",
        "brandName": "Dell",
        "series": "Latitude 7430",
        "shortSpecs": {"cpuFamily": "Core i7", "generation": "12th Gen", "ramGb": 16, "storageGb": 512, "storageType": "NVMe SSD", "gpuType": "integrated", "isDedicatedGpu": False},
        "fullSpecs": {
            "performance": {"processor": "Intel Core i7-1265U vPro", "coresThreads": "10 Cores (2P + 8E) / 12 Threads", "clocks": "1.80 GHz Base, up to 4.80 GHz Turbo", "cache": "12 MB Intel Smart Cache"},
            "memoryStorage": {"ramSize": "16 GB", "ramType": "DDR4", "ramSpeed": "3200 MHz", "ramSlots": "Soldered Dual-Channel (Non-upgradable)", "storageSize": "512 GB", "storageType": "NVMe SSD", "interface": "PCIe Gen4 x4 NVMe M.2 2280", "readSpeed": "Up to 4,800 MB/s"},
            "display": {"size": "14.0\"", "resolution": "FHD (1920 x 1080)", "panelType": "IPS Super Low Power Anti-Glare", "refreshRate": "60 Hz", "touchAntiGlare": "Anti-Glare 400 nits ComfortView Plus (Non-touch)"},
            "graphics": {"gpuName": "Intel Iris Xe Graphics", "type": "Integrated", "vram": "Shared System Memory"},
            "connectivityPorts": {"ports": "2x Thunderbolt 4 USB-C (Power Delivery and DisplayPort), 1x USB-A 3.2 Gen 1 (PowerShare), 1x HDMI 2.0, MicroSD 4.0, Audio Jack", "wireless": "Intel Wi-Fi 6E AX211 + Bluetooth 5.2"},
            "batteryBuild": {"battery": "58Wh ExpressCharge Capable", "weight": "1.22 kg (2.69 lbs) Carbon Fiber Unibody", "keyboard": "Backlit Spill-Resistant Keyboard", "webcam": "FHD IR Camera with Presence Detection & Privacy Shutter", "os": "Windows 11 Pro 64-bit Licensed"},
            "conditionWarranty": {"condition": "Pristine Like New (10/10) · 12th Gen Executive Carbon", "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"}
        }
    },
    68: {
        "name": "HP EliteBook 630 G11",
        "brandName": "HP",
        "series": "EliteBook 630 G11",
        "shortSpecs": {"cpuFamily": "Core Ultra 5", "generation": "Series 1 (AI PC)", "ramGb": 16, "storageGb": 512, "storageType": "NVMe SSD", "gpuType": "integrated", "isDedicatedGpu": False},
        "fullSpecs": {
            "performance": {"processor": "Intel Core Ultra 5 125U (AI Boost NPU)", "coresThreads": "12 Cores (2P + 8E + 2 Low-Power E) / 14 Threads", "clocks": "Up to 4.30 GHz Turbo with Dedicated Intel AI NPU", "cache": "12 MB Intel Smart Cache"},
            "memoryStorage": {"ramSize": "16 GB", "ramType": "DDR5", "ramSpeed": "5600 MHz", "ramSlots": "2x SO-DIMM Slots (Upgradable to 64GB)", "storageSize": "512 GB", "storageType": "NVMe SSD", "interface": "PCIe Gen4 x4 NVMe M.2 2280", "readSpeed": "Up to 5,000 MB/s"},
            "display": {"size": "13.3\"", "resolution": "WUXGA (1920 x 1200) 16:10", "panelType": "IPS Anti-Glare", "refreshRate": "60 Hz", "touchAntiGlare": "Anti-Glare 300 nits 16:10 Aspect Ratio (Non-touch)"},
            "graphics": {"gpuName": "Intel Graphics (Meteor Lake Architecture)", "type": "Integrated", "vram": "Shared System Memory"},
            "connectivityPorts": {"ports": "2x Thunderbolt 4 USB-C (40Gbps), 2x USB Type-A 3.2 Gen 1 (1 charging), 1x HDMI 2.1, Headphone/mic combo", "wireless": "Intel Wi-Fi 6E AX211 + Bluetooth 5.3"},
            "batteryBuild": {"battery": "54Wh HP Long Life Fast Charge", "weight": "1.23 kg (2.71 lbs) Premium Recycled Aluminum", "keyboard": "HP Premium Spill-Resistant Backlit Keyboard", "webcam": "FHD 1080p Camera with AI Noise Reduction & Privacy Shutter", "os": "Windows 11 Pro 64-bit Licensed"},
            "conditionWarranty": {"condition": "Open Box / Brand New Condition · Latest AI Generation", "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"}
        }
    },
    69: {
        "name": "Dell XPS 13 Plus 9320",
        "brandName": "Dell",
        "series": "XPS 13 Plus",
        "shortSpecs": {"cpuFamily": "Core i7", "generation": "12th Gen", "ramGb": 16, "storageGb": 512, "storageType": "NVMe SSD", "gpuType": "integrated", "isDedicatedGpu": False},
        "fullSpecs": {
            "performance": {"processor": "Intel Core i7-1280P (28W Performance)", "coresThreads": "14 Cores (6P + 8E) / 20 Threads", "clocks": "1.80 GHz Base, up to 4.80 GHz Turbo", "cache": "24 MB Intel Smart Cache"},
            "memoryStorage": {"ramSize": "16 GB", "ramType": "LPDDR5", "ramSpeed": "5200 MHz", "ramSlots": "Soldered Dual-Channel (Non-upgradable)", "storageSize": "512 GB", "storageType": "NVMe SSD", "interface": "PCIe Gen4 x4 NVMe M.2 2280", "readSpeed": "Up to 6,000 MB/s"},
            "display": {"size": "13.4\"", "resolution": "3.5K (3456 x 2160) OLED Touch / FHD+ 500 nits", "panelType": "OLED InfinityEdge / IPS", "refreshRate": "60 Hz", "touchAntiGlare": "Corning Gorilla Glass 7 Touch / Anti-Glare 500 nits"},
            "graphics": {"gpuName": "Intel Iris Xe Graphics", "type": "Integrated", "vram": "Shared System Memory"},
            "connectivityPorts": {"ports": "2x Thunderbolt 4 USB-C (Power Delivery and DisplayPort), USB-C to USB-A adapter included", "wireless": "Intel Killer Wi-Fi 6E 1675 (AX211) + Bluetooth 5.2"},
            "batteryBuild": {"battery": "55Wh ExpressCharge Capable", "weight": "1.24 kg (2.73 lbs) CNC Machined Aluminum", "keyboard": "Zero-Lattice Backlit Keyboard + Capacitive Touch Function Row + Seamless Glass Touchpad", "webcam": "720p HD RGB + 400p IR Camera with Windows Hello", "os": "Windows 11 Pro 64-bit Licensed"},
            "conditionWarranty": {"condition": "Open Box / Brand New Condition · Futuristic Flagship", "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"}
        }
    }
}

# Update all 69 laptops
updated_count = 0
for lap in existing_laptops:
    lid = lap['id']
    if lid in MODELS:
        m_info = MODELS[lid]
        
        # Save legacyName if not already set or preserve original
        if 'legacyName' not in lap:
            lap['legacyName'] = lap['name']
            
        lap['name'] = m_info['name']
        lap['brandName'] = m_info['brandName']
        lap['series'] = m_info['series']
        lap['shortSpecs'] = m_info['shortSpecs']
        lap['fullSpecs'] = m_info['fullSpecs']
        
        # Ensure compatibility fields match
        lap['ramGb'] = m_info['shortSpecs']['ramGb']
        lap['storageGb'] = m_info['shortSpecs']['storageGb']
        lap['isDedicatedGpu'] = m_info['shortSpecs']['isDedicatedGpu']
        lap['gpuType'] = m_info['shortSpecs']['gpuType']
        
        updated_count += 1

print(f"Successfully processed {updated_count} / {len(existing_laptops)} laptops.")

# Output updated dataset to laptops-data.js
js_content = f"// Complete {len(existing_laptops)}-Laptop Real Inventory Dataset\nconst LAPTOPS_INVENTORY = {json.dumps(existing_laptops, indent=2)};\n\nif (typeof module !== 'undefined') module.exports = LAPTOPS_INVENTORY;\n"

with open(DATA_JS_PATH, 'w', encoding='utf-8') as f:
    f.write(js_content)

print(f"Written updated dataset to {DATA_JS_PATH}!")
