// Complete 69-Laptop Real Inventory Dataset
const LAPTOPS_INVENTORY = [
  {
    "id": 1,
    "name": "Lenovo ThinkPad T14 Gen 1",
    "brand": "lenovo",
    "brandName": "Lenovo",
    "series": "ThinkPad T14",
    "cpu": "Intel Core i7-10610U 10th Gen",
    "cpuTag": "intel_i7",
    "gen": "10th",
    "ram": 16,
    "storage": 512,
    "display": "14\" FHD IPS Anti-Glare",
    "gpu": "Intel UHD Graphics 620",
    "gpuType": "integrated",
    "category": "Corporate Ultrabook",
    "badge": "Best Seller",
    "badgeType": "b-corp",
    "price": 98000,
    "priceFormatted": "Rs 98,000",
    "priceUsd": 350,
    "img": "images/laptop-1-lenovo-thinkpad-t14-1.jpg",
    "condition": "Like New (10/10) \u00b7 Certified Refurbished",
    "warranty": "1 Year Local Warranty + 7 Days Checking",
    "useCases": [
      "office",
      "programming",
      "student"
    ],
    "ramGb": 16,
    "storageGb": 512,
    "storageType": "NVMe SSD",
    "cpuBrand": "Intel",
    "cpuTier": "Core i7",
    "cpuGen": 10,
    "gpuCategory": "integrated",
    "isDedicatedGpu": false,
    "gpuModel": "Intel UHD Graphics 620",
    "isRamUpgradable": true,
    "ramUpgradeOptions": [
      16,
      32
    ],
    "storageUpgradeOptions": [
      512,
      1000
    ],
    "legacyName": "LENOVO T14G1 Core i7 10Th",
    "shortSpecs": {
      "cpuFamily": "Core i7",
      "generation": "10th Gen",
      "ramGb": 16,
      "storageGb": 512,
      "storageType": "NVMe SSD",
      "gpuType": "integrated",
      "isDedicatedGpu": false
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
        "ramSlots": "1 Soldered + 1 SO-DIMM (Upgradable)",
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
        "battery": "50Wh Internal (Rapid Charge)",
        "weight": "1.55 kg (3.41 lbs)",
        "keyboard": "Spill-Resistant Backlit Keyboard with TrackPoint",
        "webcam": "720p HD with ThinkShutter",
        "os": "Windows 11 Pro 64-bit Licensed"
      },
      "conditionWarranty": {
        "condition": "Like New (10/10) \u00b7 Certified Refurbished",
        "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"
      }
    },
    "bgTone": "white",
    "bgColor": "rgb(255, 255, 255)",
    "tintColor": "rgba(76, 124, 255, 0.04)",
    "processedImg": "images/processed/laptop-1-cutout.webp",
    "stock": 3
  },
  {
    "id": 2,
    "name": "Microsoft Surface Pro 7",
    "brand": "microsoft",
    "brandName": "Microsoft",
    "series": "Surface Pro 7",
    "cpu": "Intel Core i5-1035G4 10th Gen",
    "cpuTag": "intel_i5",
    "gen": "10th",
    "ram": 8,
    "storage": 256,
    "display": "12.3\" PixelSense (2736x1824) Touch",
    "gpu": "Intel Iris Plus Graphics",
    "gpuType": "integrated",
    "category": "2-in-1 Tablet PC",
    "badge": "Touch & Pen",
    "badgeType": "b-val",
    "price": 88000,
    "priceFormatted": "Rs 88,000",
    "priceUsd": 315,
    "img": "images/laptop-2-microsoft-surface-pro-7-2.jpg",
    "condition": "Like New (10/10) \u00b7 Certified Refurbished",
    "warranty": "1 Year Local Warranty + 7 Days Checking",
    "useCases": [
      "office",
      "student",
      "creator"
    ],
    "ramGb": 8,
    "storageGb": 256,
    "storageType": "NVMe SSD",
    "cpuBrand": "Intel",
    "cpuTier": "Core i5",
    "cpuGen": 10,
    "gpuCategory": "integrated",
    "isDedicatedGpu": false,
    "gpuModel": "Intel Iris Plus Graphics",
    "isRamUpgradable": false,
    "ramUpgradeOptions": [
      8
    ],
    "storageUpgradeOptions": [
      256,
      512,
      1000
    ],
    "legacyName": "Surface Tab 1866 Core i5 10th",
    "shortSpecs": {
      "cpuFamily": "Core i5",
      "generation": "10th Gen",
      "ramGb": 8,
      "storageGb": 256,
      "storageType": "NVMe SSD",
      "gpuType": "integrated",
      "isDedicatedGpu": false
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
        "ports": "1x USB-C 3.1, 1x USB-A 3.1, 3.5mm Headphone Jack, Surface Connect Port, MicroSDXC Card Reader",
        "wireless": "Wi-Fi 6 (802.11ax) + Bluetooth 5.0"
      },
      "batteryBuild": {
        "battery": "43.2Wh Battery (Up to 10.5 hours use)",
        "weight": "775 g (1.70 lbs) Tablet Body",
        "keyboard": "Surface Signature Type Cover (Detachable Backlit)",
        "webcam": "5.0MP Front 1080p with Windows Hello + 8.0MP Rear",
        "os": "Windows 11 Pro 64-bit Licensed"
      },
      "conditionWarranty": {
        "condition": "Pristine Like New (10/10) \u00b7 Open Box",
        "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"
      }
    },
    "bgTone": "colorful",
    "bgColor": "rgb(183, 158, 138)",
    "tintColor": "rgba(183, 158, 138, 0.15)",
    "processedImg": "images/laptop-2-microsoft-surface-pro-7-2.jpg",
    "stock": 3
  },
  {
    "id": 3,
    "name": "HP EliteBook 840 G9",
    "brand": "hp",
    "brandName": "HP",
    "series": "EliteBook 840 G9",
    "cpu": "Intel Core i7-1255U 12th Gen (10-Core)",
    "cpuTag": "intel_i7",
    "gen": "12th",
    "ram": 16,
    "storage": 512,
    "display": "14\" WUXGA 16:10 IPS 400 nits",
    "gpu": "Intel Iris Xe Graphics",
    "gpuType": "integrated",
    "category": "Executive Ultrabook",
    "badge": "Newer Gen",
    "badgeType": "b-gen",
    "price": 165000,
    "priceFormatted": "Rs 165,000",
    "priceUsd": 590,
    "img": "images/laptop-3-hp-elitebook-840-g9-3.jpg",
    "condition": "Like New (10/10) \u00b7 Certified Refurbished",
    "warranty": "1 Year Local Warranty + 7 Days Checking",
    "useCases": [
      "office",
      "programming",
      "creator"
    ],
    "ramGb": 16,
    "storageGb": 512,
    "storageType": "NVMe SSD",
    "cpuBrand": "Intel",
    "cpuTier": "Core i7",
    "cpuGen": 12,
    "gpuCategory": "integrated",
    "isDedicatedGpu": false,
    "gpuModel": "Intel Iris Xe Graphics",
    "isRamUpgradable": true,
    "ramUpgradeOptions": [
      16,
      32
    ],
    "storageUpgradeOptions": [
      512,
      1000
    ],
    "legacyName": "HP EliteBook 840G9 Core i5/i7 12th",
    "shortSpecs": {
      "cpuFamily": "Core i7",
      "generation": "12th Gen",
      "ramGb": 16,
      "storageGb": 512,
      "storageType": "NVMe SSD",
      "gpuType": "integrated",
      "isDedicatedGpu": false
    },
    "fullSpecs": {
      "performance": {
        "processor": "Intel Core i7-1255U",
        "coresThreads": "10 Cores (2P + 8E) / 12 Threads",
        "clocks": "1.70 GHz Base, up to 4.70 GHz Turbo",
        "cache": "12 MB Intel Smart Cache"
      },
      "memoryStorage": {
        "ramSize": "16 GB",
        "ramType": "DDR5",
        "ramSpeed": "4800 MHz",
        "ramSlots": "2x SO-DIMM Slots (Upgradable)",
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
        "touchAntiGlare": "Anti-Glare 400 nits Low Power"
      },
      "graphics": {
        "gpuName": "Intel Iris Xe Graphics",
        "type": "Integrated",
        "vram": "Shared System Memory"
      },
      "connectivityPorts": {
        "ports": "2x Thunderbolt 4 USB-C, 2x USB-A 3.2 Gen 1, 1x HDMI 2.0, Headphone/mic combo",
        "wireless": "Intel Wi-Fi 6E AX211 + Bluetooth 5.3"
      },
      "batteryBuild": {
        "battery": "51Wh HP Long Life Fast Charge (50% in 30 mins)",
        "weight": "1.36 kg (2.99 lbs)",
        "keyboard": "HP Premium Spill-Resistant Backlit Keyboard",
        "webcam": "5MP Camera with HP Auto Frame & Dual Mics",
        "os": "Windows 11 Pro 64-bit Licensed"
      },
      "conditionWarranty": {
        "condition": "Grade A+ Like New \u00b7 Verified Refurbished",
        "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"
      }
    },
    "bgTone": "colorful",
    "bgColor": "rgb(20, 82, 127)",
    "tintColor": "rgba(20, 82, 127, 0.15)",
    "processedImg": "images/laptop-3-hp-elitebook-840-g9-3.jpg",
    "stock": 3
  },
  {
    "id": 4,
    "name": "Lenovo ThinkPad X1 Yoga Gen 7",
    "brand": "lenovo",
    "brandName": "Lenovo",
    "series": "ThinkPad X1 Yoga",
    "cpu": "Intel Core i5-1240P 12th Gen (12-Core)",
    "cpuTag": "intel_i5",
    "gen": "12th",
    "ram": 16,
    "storage": 512,
    "display": "14\" WUXGA Touch 360\u00b0 with Stylus",
    "gpu": "Intel Iris Xe Graphics",
    "gpuType": "integrated",
    "category": "Flagship 2-in-1",
    "badge": "360\u00b0 Touch",
    "badgeType": "b-val",
    "price": 185000,
    "priceFormatted": "Rs 185,000",
    "priceUsd": 660,
    "img": "images/laptop-4-lenovo-thinkpad-x1-yoga-gen-7-4.jpg",
    "condition": "Like New (10/10) \u00b7 Certified Refurbished",
    "warranty": "1 Year Local Warranty + 7 Days Checking",
    "useCases": [
      "office",
      "creator",
      "programming"
    ],
    "ramGb": 16,
    "storageGb": 512,
    "storageType": "NVMe SSD",
    "cpuBrand": "Intel",
    "cpuTier": "Core i5",
    "cpuGen": 12,
    "gpuCategory": "integrated",
    "isDedicatedGpu": false,
    "gpuModel": "Intel Iris Xe Graphics",
    "isRamUpgradable": false,
    "ramUpgradeOptions": [
      16
    ],
    "storageUpgradeOptions": [
      512,
      1000
    ],
    "legacyName": "Lenovo X1 Yoga Core i5 12th",
    "shortSpecs": {
      "cpuFamily": "Core i5",
      "generation": "12th Gen",
      "ramGb": 16,
      "storageGb": 512,
      "storageType": "NVMe SSD",
      "gpuType": "integrated",
      "isDedicatedGpu": false
    },
    "fullSpecs": {
      "performance": {
        "processor": "Intel Core i5-1240P",
        "coresThreads": "12 Cores (4P + 8E) / 16 Threads",
        "clocks": "1.70 GHz Base, up to 4.40 GHz Boost",
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
        "panelType": "IPS Touchscreen 360\u00b0",
        "refreshRate": "60 Hz",
        "touchAntiGlare": "Anti-Reflection Touch with ThinkPad Pen Pro, 400 nits"
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
        "webcam": "FHD 1080p IR Camera with Privacy Shutter",
        "os": "Windows 11 Pro 64-bit Licensed"
      },
      "conditionWarranty": {
        "condition": "Pristine Like New (10/10) \u00b7 Certified Refurbished",
        "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"
      }
    },
    "bgTone": "white",
    "bgColor": "rgb(255, 255, 255)",
    "tintColor": "rgba(76, 124, 255, 0.04)",
    "processedImg": "images/processed/laptop-4-cutout.webp",
    "stock": 3
  },
  {
    "id": 5,
    "name": "Lenovo ThinkPad X13 Gen 1",
    "brand": "lenovo",
    "brandName": "Lenovo",
    "series": "ThinkPad X13",
    "cpu": "Intel Core i5-10210U 10th Gen",
    "cpuTag": "intel_i5",
    "gen": "10th",
    "ram": 16,
    "storage": 256,
    "display": "13.3\" FHD IPS Anti-Glare",
    "gpu": "Intel UHD Graphics",
    "gpuType": "integrated",
    "category": "Ultra-Portable Business",
    "badge": "Compact",
    "badgeType": "b-corp",
    "price": 82000,
    "priceFormatted": "Rs 82,000",
    "priceUsd": 295,
    "img": "images/laptop-5-lenovo-thinkpad-x13-gen-1-5.jpg",
    "condition": "Like New (10/10) \u00b7 Certified Refurbished",
    "warranty": "1 Year Local Warranty + 7 Days Checking",
    "useCases": [
      "office",
      "student"
    ],
    "ramGb": 8,
    "storageGb": 256,
    "storageType": "NVMe SSD",
    "cpuBrand": "Intel",
    "cpuTier": "Core i5",
    "cpuGen": 10,
    "gpuCategory": "integrated",
    "isDedicatedGpu": false,
    "gpuModel": "Intel UHD Graphics",
    "isRamUpgradable": false,
    "ramUpgradeOptions": [
      16
    ],
    "storageUpgradeOptions": [
      256,
      512,
      1000
    ],
    "legacyName": "Lenovo X13 Core i5 10th",
    "shortSpecs": {
      "cpuFamily": "Core i5",
      "generation": "10th Gen",
      "ramGb": 8,
      "storageGb": 256,
      "storageType": "NVMe SSD",
      "gpuType": "integrated",
      "isDedicatedGpu": false
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
        "condition": "Like New (10/10) \u00b7 Certified Refurbished",
        "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"
      }
    },
    "bgTone": "white",
    "bgColor": "rgb(255, 255, 255)",
    "tintColor": "rgba(76, 124, 255, 0.04)",
    "processedImg": "images/processed/laptop-5-cutout.webp",
    "stock": 3
  },
  {
    "id": 6,
    "name": "Lenovo ThinkPad T14 Gen 1",
    "brand": "lenovo",
    "brandName": "Lenovo",
    "series": "ThinkPad T14",
    "cpu": "AMD Ryzen 7 PRO 4750U 8-Core/16-Thread",
    "cpuTag": "amd",
    "gen": "Ryzen 4000",
    "ram": 16,
    "storage": 512,
    "display": "14\" FHD IPS Anti-Glare",
    "gpu": "AMD Radeon Vega 7",
    "gpuType": "integrated",
    "category": "8-Core Workhorse",
    "badge": "Heavy Dev",
    "badgeType": "b-corp",
    "price": 105000,
    "priceFormatted": "Rs 105,000",
    "priceUsd": 375,
    "img": "images/laptop-6-lenovo-thinkpad-t14-gen-1-6.jpg",
    "condition": "Like New (10/10) \u00b7 Certified Refurbished",
    "warranty": "1 Year Local Warranty + 7 Days Checking",
    "useCases": [
      "programming",
      "office",
      "student"
    ],
    "ramGb": 16,
    "storageGb": 512,
    "storageType": "NVMe SSD",
    "cpuBrand": "AMD",
    "cpuTier": "Ryzen 7",
    "cpuGen": 4000,
    "gpuCategory": "integrated",
    "isDedicatedGpu": false,
    "gpuModel": "AMD Radeon Vega 7",
    "isRamUpgradable": true,
    "ramUpgradeOptions": [
      16,
      32
    ],
    "storageUpgradeOptions": [
      512,
      1000
    ],
    "legacyName": "Lenovo T14G1 Ryzen 7 Pro",
    "shortSpecs": {
      "cpuFamily": "Ryzen 7",
      "generation": "4000 Series",
      "ramGb": 16,
      "storageGb": 512,
      "storageType": "NVMe SSD",
      "gpuType": "integrated",
      "isDedicatedGpu": false
    },
    "fullSpecs": {
      "performance": {
        "processor": "AMD Ryzen 7 PRO 4750U",
        "coresThreads": "8 Cores / 16 Threads",
        "clocks": "1.70 GHz Base, up to 4.10 GHz Boost",
        "cache": "8 MB L3 Cache"
      },
      "memoryStorage": {
        "ramSize": "16 GB",
        "ramType": "DDR4",
        "ramSpeed": "3200 MHz",
        "ramSlots": "1 Soldered + 1 SO-DIMM Slot (Upgradable)",
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
        "ports": "2x USB-A 3.2 Gen 1, 2x USB-C 3.2 Gen 2 (DisplayPort/PD), HDMI 2.0, RJ-45 Gigabit, Audio combo, MicroSD",
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
        "condition": "Like New (10/10) \u00b7 Certified Refurbished",
        "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"
      }
    },
    "bgTone": "white",
    "bgColor": "rgb(253, 253, 253)",
    "tintColor": "rgba(76, 124, 255, 0.04)",
    "processedImg": "images/processed/laptop-6-cutout.webp",
    "stock": 3
  },
  {
    "id": 7,
    "name": "Lenovo ThinkPad 13 Gen 1",
    "brand": "lenovo",
    "brandName": "Lenovo",
    "series": "ThinkPad 13",
    "cpu": "Intel Core i5-6200U 6th Gen",
    "cpuTag": "intel_i5",
    "gen": "6th",
    "ram": 8,
    "storage": 256,
    "display": "13.3\" HD Anti-Glare",
    "gpu": "Intel HD Graphics 520",
    "gpuType": "integrated",
    "category": "Budget Student",
    "badge": "Under 50k",
    "badgeType": "b-val",
    "price": 44000,
    "priceFormatted": "Rs 44,000",
    "priceUsd": 160,
    "img": "images/laptop-7-lenovo-thinkpad-13-gen-1-7.jpg",
    "condition": "Like New (10/10) \u00b7 Certified Refurbished",
    "warranty": "1 Year Local Warranty + 7 Days Checking",
    "useCases": [
      "student",
      "office"
    ],
    "ramGb": 8,
    "storageGb": 256,
    "storageType": "NVMe SSD",
    "cpuBrand": "Intel",
    "cpuTier": "Core i5",
    "cpuGen": 6,
    "gpuCategory": "integrated",
    "isDedicatedGpu": false,
    "gpuModel": "Intel HD Graphics 520",
    "isRamUpgradable": true,
    "ramUpgradeOptions": [
      8,
      16,
      32
    ],
    "storageUpgradeOptions": [
      256,
      512,
      1000
    ],
    "legacyName": "Lenovo 13 Core i5 6th",
    "shortSpecs": {
      "cpuFamily": "Core i5",
      "generation": "6th Gen",
      "ramGb": 8,
      "storageGb": 256,
      "storageType": "SATA SSD",
      "gpuType": "integrated",
      "isDedicatedGpu": false
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
        "ramSlots": "2x SO-DIMM Slots (Upgradable)",
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
        "condition": "Clean Condition (9/10) \u00b7 Fully Tested",
        "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"
      }
    },
    "bgTone": "white",
    "bgColor": "rgb(255, 255, 255)",
    "tintColor": "rgba(76, 124, 255, 0.04)",
    "processedImg": "images/processed/laptop-7-cutout.webp",
    "stock": 3
  },
  {
    "id": 8,
    "name": "Dell XPS 15 9550",
    "brand": "dell",
    "brandName": "Dell",
    "series": "XPS 15",
    "cpu": "Intel Core i7-6700HQ Quad Core 45W",
    "cpuTag": "intel_i7",
    "gen": "6th",
    "ram": 16,
    "storage": 512,
    "display": "15.6\" 4K UHD Touch InfinityEdge",
    "gpu": "NVIDIA GeForce GTX 960M 2GB",
    "gpuType": "discrete",
    "category": "Studio Performance",
    "badge": "4K Touch",
    "badgeType": "b-val",
    "price": 88000,
    "priceFormatted": "Rs 88,000",
    "priceUsd": 315,
    "img": "images/laptop-8-dell-xps-15-9550-8.jpg",
    "condition": "Like New (10/10) \u00b7 Certified Refurbished",
    "warranty": "1 Year Local Warranty + 7 Days Checking",
    "useCases": [
      "creator",
      "programming",
      "gaming"
    ],
    "ramGb": 16,
    "storageGb": 512,
    "storageType": "NVMe SSD",
    "cpuBrand": "Intel",
    "cpuTier": "Core i7",
    "cpuGen": 6,
    "gpuCategory": "dedicated",
    "isDedicatedGpu": true,
    "gpuModel": "NVIDIA GeForce GTX 960M 2GB",
    "isRamUpgradable": true,
    "ramUpgradeOptions": [
      16,
      32
    ],
    "storageUpgradeOptions": [
      512,
      1000
    ],
    "legacyName": "Dell XPS 15 Core i7 6th",
    "shortSpecs": {
      "cpuFamily": "Core i7",
      "generation": "6th Gen",
      "ramGb": 16,
      "storageGb": 512,
      "storageType": "NVMe SSD",
      "gpuType": "discrete",
      "isDedicatedGpu": true
    },
    "fullSpecs": {
      "performance": {
        "processor": "Intel Core i7-6700HQ (45W)",
        "coresThreads": "4 Cores / 8 Threads",
        "clocks": "2.60 GHz Base, up to 3.50 GHz Turbo",
        "cache": "6 MB Intel Smart Cache"
      },
      "memoryStorage": {
        "ramSize": "16 GB",
        "ramType": "DDR4",
        "ramSpeed": "2133 MHz",
        "ramSlots": "2x SO-DIMM Slots (Upgradable)",
        "storageSize": "512 GB",
        "storageType": "NVMe SSD",
        "interface": "PCIe Gen3 x4 M.2 2280",
        "readSpeed": "Up to 2,200 MB/s"
      },
      "display": {
        "size": "15.6\"",
        "resolution": "4K UHD (3840 x 2160) Touch / FHD",
        "panelType": "IGZO IPS UltraSharp",
        "refreshRate": "60 Hz",
        "touchAntiGlare": "Touchscreen / InfinityEdge, 400 nits"
      },
      "graphics": {
        "gpuName": "NVIDIA GeForce GTX 960M",
        "type": "Dedicated",
        "vram": "2 GB GDDR5 Dedicated"
      },
      "connectivityPorts": {
        "ports": "1x Thunderbolt 3 (USB-C), 2x USB 3.0 with PowerShare, 1x HDMI, SD Card Slot, Audio jack",
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
        "condition": "Excellent Condition (9.5/10) \u00b7 Creator Ready",
        "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"
      }
    },
    "bgTone": "white",
    "bgColor": "rgb(255, 255, 255)",
    "tintColor": "rgba(76, 124, 255, 0.04)",
    "processedImg": "images/processed/laptop-8-cutout.webp",
    "stock": 3
  },
  {
    "id": 9,
    "name": "Dell Latitude 5310",
    "brand": "dell",
    "brandName": "Dell",
    "series": "Latitude 5310",
    "cpu": "Intel Core i5-10210U 10th Gen",
    "cpuTag": "intel_i5",
    "gen": "10th",
    "ram": 16,
    "storage": 256,
    "display": "13.3\" FHD IPS Anti-Glare",
    "gpu": "Intel UHD Graphics",
    "gpuType": "integrated",
    "category": "Compact Business",
    "badge": "Popular",
    "badgeType": "b-corp",
    "price": 78000,
    "priceFormatted": "Rs 78,000",
    "priceUsd": 280,
    "img": "images/laptop-9-dell-latitude-5310-9.jpg",
    "condition": "Like New (10/10) \u00b7 Certified Refurbished",
    "warranty": "1 Year Local Warranty + 7 Days Checking",
    "useCases": [
      "office",
      "student"
    ],
    "ramGb": 8,
    "storageGb": 256,
    "storageType": "NVMe SSD",
    "cpuBrand": "Intel",
    "cpuTier": "Core i5",
    "cpuGen": 10,
    "gpuCategory": "integrated",
    "isDedicatedGpu": false,
    "gpuModel": "Intel UHD Graphics",
    "isRamUpgradable": true,
    "ramUpgradeOptions": [
      16,
      32
    ],
    "storageUpgradeOptions": [
      256,
      512,
      1000
    ],
    "legacyName": "Dell 5310 Core i5 10th",
    "shortSpecs": {
      "cpuFamily": "Core i5",
      "generation": "10th Gen",
      "ramGb": 8,
      "storageGb": 256,
      "storageType": "NVMe SSD",
      "gpuType": "integrated",
      "isDedicatedGpu": false
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
        "condition": "Grade A+ Like New \u00b7 Enterprise Refurbished",
        "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"
      }
    },
    "bgTone": "colorful",
    "bgColor": "rgb(172, 177, 183)",
    "tintColor": "rgba(172, 177, 183, 0.15)",
    "processedImg": "images/laptop-9-dell-latitude-5310-9.jpg",
    "stock": 3
  },
  {
    "id": 10,
    "name": "HP EliteBook x360 1030 G8",
    "brand": "hp",
    "brandName": "HP",
    "series": "EliteBook x360 1030",
    "cpu": "Intel Core i7-1165G7 11th Gen",
    "cpuTag": "intel_i7",
    "gen": "11th",
    "ram": 16,
    "storage": 512,
    "display": "13.3\" FHD IPS Touch 360\u00b0 SureView",
    "gpu": "Intel Iris Xe Graphics",
    "gpuType": "integrated",
    "category": "Executive 2-in-1",
    "badge": "Premium Touch",
    "badgeType": "b-gen",
    "price": 138000,
    "priceFormatted": "Rs 138,000",
    "priceUsd": 495,
    "img": "images/laptop-10-hp-elitebook-x360-1030-g8-10.jpg",
    "condition": "Like New (10/10) \u00b7 Certified Refurbished",
    "warranty": "1 Year Local Warranty + 7 Days Checking",
    "useCases": [
      "office",
      "creator",
      "programming"
    ],
    "ramGb": 16,
    "storageGb": 512,
    "storageType": "NVMe SSD",
    "cpuBrand": "Intel",
    "cpuTier": "Core i7",
    "cpuGen": 11,
    "gpuCategory": "integrated",
    "isDedicatedGpu": false,
    "gpuModel": "Intel Iris Xe Graphics",
    "isRamUpgradable": true,
    "ramUpgradeOptions": [
      16,
      32
    ],
    "storageUpgradeOptions": [
      512,
      1000
    ],
    "legacyName": "HP 1030G8 Core i7 11th",
    "shortSpecs": {
      "cpuFamily": "Core i7",
      "generation": "11th Gen",
      "ramGb": 16,
      "storageGb": 512,
      "storageType": "NVMe SSD",
      "gpuType": "integrated",
      "isDedicatedGpu": false
    },
    "fullSpecs": {
      "performance": {
        "processor": "Intel Core i7-1165G7",
        "coresThreads": "4 Cores / 8 Threads",
        "clocks": "2.80 GHz Base, up to 4.70 GHz Turbo",
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
        "panelType": "IPS BrightView Touchscreen 360\u00b0",
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
        "condition": "Pristine Like New (10/10) \u00b7 Executive 2-in-1",
        "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"
      }
    },
    "bgTone": "white",
    "bgColor": "rgb(255, 255, 255)",
    "tintColor": "rgba(76, 124, 255, 0.04)",
    "processedImg": "images/processed/laptop-10-cutout.webp",
    "stock": 3
  },
  {
    "id": 11,
    "name": "Dell Latitude 5320",
    "brand": "dell",
    "brandName": "Dell",
    "series": "Latitude 5320",
    "cpu": "Intel Core i5-1145G7 vPro 11th Gen",
    "cpuTag": "intel_i5",
    "gen": "11th",
    "ram": 16,
    "storage": 512,
    "display": "13.3\" FHD IPS Anti-Glare",
    "gpu": "Intel Iris Xe Graphics",
    "gpuType": "integrated",
    "category": "Corporate Ultrabook",
    "badge": "Top Value",
    "badgeType": "b-corp",
    "price": 92000,
    "priceFormatted": "Rs 92,000",
    "priceUsd": 330,
    "img": "images/laptop-11-dell-latitude-5320-11.jpg",
    "condition": "Like New (10/10) \u00b7 Certified Refurbished",
    "warranty": "1 Year Local Warranty + 7 Days Checking",
    "useCases": [
      "office",
      "programming",
      "student"
    ],
    "ramGb": 16,
    "storageGb": 256,
    "storageType": "NVMe SSD",
    "cpuBrand": "Intel",
    "cpuTier": "Core i5",
    "cpuGen": 11,
    "gpuCategory": "integrated",
    "isDedicatedGpu": false,
    "gpuModel": "Intel Iris Xe Graphics",
    "isRamUpgradable": true,
    "ramUpgradeOptions": [
      16,
      32
    ],
    "storageUpgradeOptions": [
      512,
      1000
    ],
    "legacyName": "Dell 5320 Core i5 11th",
    "shortSpecs": {
      "cpuFamily": "Core i5",
      "generation": "11th Gen",
      "ramGb": 16,
      "storageGb": 256,
      "storageType": "NVMe SSD",
      "gpuType": "integrated",
      "isDedicatedGpu": false
    },
    "fullSpecs": {
      "performance": {
        "processor": "Intel Core i5-1145G7 vPro",
        "coresThreads": "4 Cores / 8 Threads",
        "clocks": "2.60 GHz Base, up to 4.40 GHz Turbo",
        "cache": "8 MB Intel Smart Cache"
      },
      "memoryStorage": {
        "ramSize": "16 GB",
        "ramType": "DDR4",
        "ramSpeed": "3200 MHz",
        "ramSlots": "Soldered Dual-Channel (Non-upgradable)",
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
        "gpuName": "Intel Iris Xe Graphics",
        "type": "Integrated",
        "vram": "Shared System Memory"
      },
      "connectivityPorts": {
        "ports": "2x Thunderbolt 4 USB-C (Power Delivery/DisplayPort), 2x USB-A 3.2 Gen 1 (1 with PowerShare), 1x HDMI 2.0, MicroSD, Audio Jack",
        "wireless": "Intel Wi-Fi 6 AX201 + Bluetooth 5.1"
      },
      "batteryBuild": {
        "battery": "63Wh / 42Wh ExpressCharge Capable",
        "weight": "1.20 kg (2.65 lbs)",
        "keyboard": "Backlit Spill-Resistant Keyboard",
        "webcam": "720p HD with Camera Shutter & IR Hello",
        "os": "Windows 11 Pro 64-bit Licensed"
      },
      "conditionWarranty": {
        "condition": "Grade A+ Like New \u00b7 Corporate Clean",
        "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"
      }
    },
    "bgTone": "white",
    "bgColor": "rgb(255, 255, 255)",
    "tintColor": "rgba(76, 124, 255, 0.04)",
    "processedImg": "images/processed/laptop-11-cutout.webp",
    "stock": 3
  },
  {
    "id": 12,
    "name": "HP EliteBook x360 1030 G2",
    "brand": "hp",
    "brandName": "HP",
    "series": "EliteBook x360 1030",
    "cpu": "Intel Core i5-7200U 7th Gen",
    "cpuTag": "intel_i5",
    "gen": "7th",
    "ram": 8,
    "storage": 256,
    "display": "13.3\" FHD Touch 360\u00b0 Aluminum",
    "gpu": "Intel HD Graphics 620",
    "gpuType": "integrated",
    "category": "Budget 2-in-1",
    "badge": "Touch 360\u00b0",
    "badgeType": "b-val",
    "price": 58000,
    "priceFormatted": "Rs 58,000",
    "priceUsd": 210,
    "img": "images/laptop-12-hp-elitebook-x360-1030-g2-12.jpg",
    "condition": "Like New (10/10) \u00b7 Certified Refurbished",
    "warranty": "1 Year Local Warranty + 7 Days Checking",
    "useCases": [
      "student",
      "office"
    ],
    "ramGb": 8,
    "storageGb": 256,
    "storageType": "NVMe SSD",
    "cpuBrand": "Intel",
    "cpuTier": "Core i5",
    "cpuGen": 7,
    "gpuCategory": "integrated",
    "isDedicatedGpu": false,
    "gpuModel": "Intel HD Graphics 620",
    "isRamUpgradable": true,
    "ramUpgradeOptions": [
      8,
      16,
      32
    ],
    "storageUpgradeOptions": [
      256,
      512,
      1000
    ],
    "legacyName": "HP EliteBook 1030G2 Core i5 7th",
    "shortSpecs": {
      "cpuFamily": "Core i5",
      "generation": "7th Gen",
      "ramGb": 8,
      "storageGb": 256,
      "storageType": "NVMe SSD",
      "gpuType": "integrated",
      "isDedicatedGpu": false
    },
    "fullSpecs": {
      "performance": {
        "processor": "Intel Core i5-7200U",
        "coresThreads": "2 Cores / 4 Threads",
        "clocks": "2.50 GHz Base, up to 3.10 GHz Boost",
        "cache": "3 MB Intel Smart Cache"
      },
      "memoryStorage": {
        "ramSize": "8 GB",
        "ramType": "DDR4",
        "ramSpeed": "2133 MHz",
        "ramSlots": "Soldered Dual-Channel (Non-upgradable)",
        "storageSize": "256 GB",
        "storageType": "NVMe SSD",
        "interface": "PCIe Gen3 x4 M.2 2280",
        "readSpeed": "Up to 1,800 MB/s"
      },
      "display": {
        "size": "13.3\"",
        "resolution": "FHD (1920 x 1080)",
        "panelType": "IPS Touchscreen 360\u00b0",
        "refreshRate": "60 Hz",
        "touchAntiGlare": "Corning Gorilla Glass Touch Convertible"
      },
      "graphics": {
        "gpuName": "Intel HD Graphics 620",
        "type": "Integrated",
        "vram": "Shared System Memory"
      },
      "connectivityPorts": {
        "ports": "1x USB-C (Thunderbolt), 2x USB 3.1 Gen 1 (1 charging), 1x HDMI 1.4, MicroSD, Audio Jack",
        "wireless": "Intel 802.11a/b/g/n/ac (2x2) + Bluetooth 4.2"
      },
      "batteryBuild": {
        "battery": "57Wh HP Long Life 3-cell Li-ion",
        "weight": "1.28 kg (2.82 lbs) CNC Aluminum",
        "keyboard": "HP Premium Collaboration Backlit Keyboard",
        "webcam": "720p HD with IR Camera for Windows Hello",
        "os": "Windows 10/11 Pro 64-bit Licensed"
      },
      "conditionWarranty": {
        "condition": "Like New (10/10) \u00b7 Certified Refurbished",
        "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"
      }
    },
    "bgTone": "white",
    "bgColor": "rgb(255, 255, 255)",
    "tintColor": "rgba(76, 124, 255, 0.04)",
    "processedImg": "images/processed/laptop-12-cutout.webp",
    "stock": 3
  },
  {
    "id": 13,
    "name": "Dell Latitude 5430",
    "brand": "dell",
    "brandName": "Dell",
    "series": "Latitude 5430",
    "cpu": "Intel Core i5-1235U 12th Gen (10-Core)",
    "cpuTag": "intel_i5",
    "gen": "12th",
    "ram": 16,
    "storage": 512,
    "display": "14\" FHD IPS Anti-Glare",
    "gpu": "Intel Iris Xe Graphics",
    "gpuType": "integrated",
    "category": "Modern Business",
    "badge": "12th Gen Fast",
    "badgeType": "b-corp",
    "price": 135000,
    "priceFormatted": "Rs 135,000",
    "priceUsd": 485,
    "img": "images/laptop-13-dell-latitude-5430-13.jpg",
    "condition": "Like New (10/10) \u00b7 Certified Refurbished",
    "warranty": "1 Year Local Warranty + 7 Days Checking",
    "useCases": [
      "office",
      "programming"
    ],
    "ramGb": 16,
    "storageGb": 512,
    "storageType": "NVMe SSD",
    "cpuBrand": "Intel",
    "cpuTier": "Core i5",
    "cpuGen": 12,
    "gpuCategory": "integrated",
    "isDedicatedGpu": false,
    "gpuModel": "Intel Iris Xe Graphics",
    "isRamUpgradable": true,
    "ramUpgradeOptions": [
      16,
      32
    ],
    "storageUpgradeOptions": [
      512,
      1000
    ],
    "legacyName": "Dell 5430 Core i5 12th",
    "shortSpecs": {
      "cpuFamily": "Core i5",
      "generation": "12th Gen",
      "ramGb": 16,
      "storageGb": 512,
      "storageType": "NVMe SSD",
      "gpuType": "integrated",
      "isDedicatedGpu": false
    },
    "fullSpecs": {
      "performance": {
        "processor": "Intel Core i5-1235U",
        "coresThreads": "10 Cores (2P + 8E) / 12 Threads",
        "clocks": "1.30 GHz Base, up to 4.40 GHz Turbo",
        "cache": "12 MB Intel Smart Cache"
      },
      "memoryStorage": {
        "ramSize": "16 GB",
        "ramType": "DDR4",
        "ramSpeed": "3200 MHz",
        "ramSlots": "2x SO-DIMM Slots (Upgradable to 64GB)",
        "storageSize": "512 GB",
        "storageType": "NVMe SSD",
        "interface": "PCIe Gen4 x4 NVMe M.2 2280",
        "readSpeed": "Up to 4,200 MB/s"
      },
      "display": {
        "size": "14.0\"",
        "resolution": "FHD (1920 x 1080)",
        "panelType": "IPS Anti-Glare",
        "refreshRate": "60 Hz",
        "touchAntiGlare": "Anti-Glare 250 nits (Non-touch)"
      },
      "graphics": {
        "gpuName": "Intel Iris Xe Graphics",
        "type": "Integrated",
        "vram": "Shared System Memory"
      },
      "connectivityPorts": {
        "ports": "2x Thunderbolt 4 with Power Delivery & DisplayPort, 2x USB 3.2 Gen 1 (1 PowerShare), 1x HDMI 2.0, RJ-45 Gigabit, MicroSD, Audio Jack",
        "wireless": "Intel Wi-Fi 6E AX211 + Bluetooth 5.2"
      },
      "batteryBuild": {
        "battery": "58Wh ExpressCharge Boost Capable",
        "weight": "1.36 kg (3.01 lbs)",
        "keyboard": "Backlit Spill-Resistant Keyboard",
        "webcam": "1080p FHD RGB-IR with Camera Privacy Shutter",
        "os": "Windows 11 Pro 64-bit Licensed"
      },
      "conditionWarranty": {
        "condition": "Grade A+ Like New \u00b7 Business Workhorse",
        "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"
      }
    },
    "bgTone": "white",
    "bgColor": "rgb(253, 253, 253)",
    "tintColor": "rgba(76, 124, 255, 0.04)",
    "processedImg": "images/processed/laptop-13-cutout.webp",
    "stock": 3
  },
  {
    "id": 14,
    "name": "Dell Latitude 7420",
    "brand": "dell",
    "brandName": "Dell",
    "series": "Latitude 7420",
    "cpu": "Intel Core i5-1145G7 vPro 11th Gen",
    "cpuTag": "intel_i5",
    "gen": "11th",
    "ram": 16,
    "storage": 512,
    "display": "14\" FHD IPS Carbon Chassis",
    "gpu": "Intel Iris Xe Graphics",
    "gpuType": "integrated",
    "category": "Carbon Ultrabook",
    "badge": "Hot Seller",
    "badgeType": "b-corp",
    "price": 105000,
    "priceFormatted": "Rs 105,000",
    "priceUsd": 375,
    "img": "images/laptop-14-dell-latitude-7420-carbon-14.jpg",
    "condition": "Like New (10/10) \u00b7 Certified Refurbished",
    "warranty": "1 Year Local Warranty + 7 Days Checking",
    "useCases": [
      "office",
      "programming",
      "student"
    ],
    "ramGb": 16,
    "storageGb": 512,
    "storageType": "NVMe SSD",
    "cpuBrand": "Intel",
    "cpuTier": "Core i5",
    "cpuGen": 11,
    "gpuCategory": "integrated",
    "isDedicatedGpu": false,
    "gpuModel": "Intel Iris Xe Graphics",
    "isRamUpgradable": true,
    "ramUpgradeOptions": [
      16,
      32
    ],
    "storageUpgradeOptions": [
      512,
      1000
    ],
    "legacyName": "Dell 7420 Core i5 11th",
    "shortSpecs": {
      "cpuFamily": "Core i5",
      "generation": "11th Gen",
      "ramGb": 16,
      "storageGb": 512,
      "storageType": "NVMe SSD",
      "gpuType": "integrated",
      "isDedicatedGpu": false
    },
    "fullSpecs": {
      "performance": {
        "processor": "Intel Core i5-1145G7 vPro",
        "coresThreads": "4 Cores / 8 Threads",
        "clocks": "2.60 GHz Base, up to 4.40 GHz Turbo",
        "cache": "8 MB Intel Smart Cache"
      },
      "memoryStorage": {
        "ramSize": "16 GB",
        "ramType": "LPDDR4x",
        "ramSpeed": "4266 MHz",
        "ramSlots": "Soldered Dual-Channel (Non-upgradable)",
        "storageSize": "512 GB",
        "storageType": "NVMe SSD",
        "interface": "PCIe Gen3 x4 M.2 2280",
        "readSpeed": "Up to 3,200 MB/s"
      },
      "display": {
        "size": "14.0\"",
        "resolution": "FHD (1920 x 1080)",
        "panelType": "IPS Anti-Glare",
        "refreshRate": "60 Hz",
        "touchAntiGlare": "Super Low Power Anti-Glare, 400 nits ComfortView Plus"
      },
      "graphics": {
        "gpuName": "Intel Iris Xe Graphics",
        "type": "Integrated",
        "vram": "Shared System Memory"
      },
      "connectivityPorts": {
        "ports": "2x Thunderbolt 4 USB-C (Power Delivery/DisplayPort), 1x USB-A 3.2 Gen 1 (PowerShare), 1x HDMI 2.0, MicroSD 4.0, Audio Jack",
        "wireless": "Intel Wi-Fi 6 AX201 + Bluetooth 5.1"
      },
      "batteryBuild": {
        "battery": "63Wh ExpressCharge Capable",
        "weight": "1.22 kg (2.69 lbs) Carbon Fiber",
        "keyboard": "Backlit Spill-Resistant Keyboard",
        "webcam": "FHD IR Camera with ExpressSign-in & Privacy Shutter",
        "os": "Windows 11 Pro 64-bit Licensed"
      },
      "conditionWarranty": {
        "condition": "Grade A+ Like New \u00b7 Carbon Fiber Flagship",
        "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"
      }
    },
    "bgTone": "white",
    "bgColor": "rgb(255, 255, 255)",
    "tintColor": "rgba(76, 124, 255, 0.04)",
    "processedImg": "images/processed/laptop-14-cutout.webp",
    "stock": 3
  },
  {
    "id": 15,
    "name": "HP ProBook 640 G1",
    "brand": "hp",
    "brandName": "HP",
    "series": "ProBook 640 G1",
    "cpu": "Intel Core i5-4200M 4th Gen",
    "cpuTag": "intel_i5",
    "gen": "4th",
    "ram": 8,
    "storage": 256,
    "display": "14\" HD Anti-Glare",
    "gpu": "Intel HD Graphics 4600",
    "gpuType": "integrated",
    "category": "Entry Budget",
    "badge": "Super Budget",
    "badgeType": "b-val",
    "price": 36000,
    "priceFormatted": "Rs 36,000",
    "priceUsd": 130,
    "img": "images/laptop-15-hp-probook-640-g1-15.jpg",
    "condition": "Like New (10/10) \u00b7 Certified Refurbished",
    "warranty": "1 Year Local Warranty + 7 Days Checking",
    "useCases": [
      "student",
      "office"
    ],
    "ramGb": 8,
    "storageGb": 256,
    "storageType": "NVMe SSD",
    "cpuBrand": "Intel",
    "cpuTier": "Core i5",
    "cpuGen": 4,
    "gpuCategory": "integrated",
    "isDedicatedGpu": false,
    "gpuModel": "Intel HD Graphics 4600",
    "isRamUpgradable": true,
    "ramUpgradeOptions": [
      8,
      16,
      32
    ],
    "storageUpgradeOptions": [
      256,
      512,
      1000
    ],
    "legacyName": "HP 640G1 Core i5 4th",
    "shortSpecs": {
      "cpuFamily": "Core i5",
      "generation": "4th Gen",
      "ramGb": 8,
      "storageGb": 256,
      "storageType": "SATA SSD",
      "gpuType": "integrated",
      "isDedicatedGpu": false
    },
    "fullSpecs": {
      "performance": {
        "processor": "Intel Core i5-4200M (Socketed)",
        "coresThreads": "2 Cores / 4 Threads",
        "clocks": "2.50 GHz Base, up to 3.10 GHz Boost",
        "cache": "3 MB Intel Smart Cache"
      },
      "memoryStorage": {
        "ramSize": "8 GB",
        "ramType": "DDR3L",
        "ramSpeed": "1600 MHz",
        "ramSlots": "2x SO-DIMM Slots (Upgradable to 16GB)",
        "storageSize": "256 GB",
        "storageType": "SATA SSD",
        "interface": "2.5\" SATA III SSD",
        "readSpeed": "Up to 520 MB/s"
      },
      "display": {
        "size": "14.0\"",
        "resolution": "HD / HD+ (1366 x 768 / 1600 x 900)",
        "panelType": "Anti-Glare LED-backlit",
        "refreshRate": "60 Hz",
        "touchAntiGlare": "Anti-Glare (Non-touch)"
      },
      "graphics": {
        "gpuName": "Intel HD Graphics 4600",
        "type": "Integrated",
        "vram": "Shared System Memory"
      },
      "connectivityPorts": {
        "ports": "4x USB 3.0, 1x VGA, 1x DisplayPort, 1x RJ-45 Ethernet, SD Card Reader, Headphone/Mic combo",
        "wireless": "Intel Dual Band Wireless-AC 7260 + Bluetooth 4.0"
      },
      "batteryBuild": {
        "battery": "55Wh 6-cell Lithium-Ion (Removable)",
        "weight": "2.00 kg (4.4 lbs)",
        "keyboard": "Spill-Resistant Keyboard with Drain",
        "webcam": "720p HD Webcam",
        "os": "Windows 10 Pro 64-bit Licensed"
      },
      "conditionWarranty": {
        "condition": "Clean Used (9/10) \u00b7 Durable Classic",
        "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"
      }
    },
    "bgTone": "white",
    "bgColor": "rgb(242, 242, 242)",
    "tintColor": "rgba(76, 124, 255, 0.04)",
    "processedImg": "images/processed/laptop-15-cutout.webp",
    "stock": 3
  },
  {
    "id": 16,
    "name": "HP ProBook 630 G9",
    "brand": "hp",
    "brandName": "HP",
    "series": "ProBook 630 G9",
    "cpu": "Intel Core i3-1215U 12th Gen (6-Core)",
    "cpuTag": "intel_i3",
    "gen": "12th",
    "ram": 8,
    "storage": 256,
    "display": "13.3\" FHD IPS Anti-Glare",
    "gpu": "Intel UHD Graphics",
    "gpuType": "integrated",
    "category": "Modern Budget",
    "badge": "6-Core i3",
    "badgeType": "b-gen",
    "price": 88000,
    "priceFormatted": "Rs 88,000",
    "priceUsd": 315,
    "img": "images/laptop-16-hp-probook-630-g9-16.jpg",
    "condition": "Like New (10/10) \u00b7 Certified Refurbished",
    "warranty": "1 Year Local Warranty + 7 Days Checking",
    "useCases": [
      "office",
      "student"
    ],
    "ramGb": 8,
    "storageGb": 256,
    "storageType": "NVMe SSD",
    "cpuBrand": "Intel",
    "cpuTier": "Core i3",
    "cpuGen": 12,
    "gpuCategory": "integrated",
    "isDedicatedGpu": false,
    "gpuModel": "Intel UHD Graphics",
    "isRamUpgradable": true,
    "ramUpgradeOptions": [
      8,
      16,
      32
    ],
    "storageUpgradeOptions": [
      256,
      512,
      1000
    ],
    "legacyName": "HP 630G9 Core i3 12th",
    "shortSpecs": {
      "cpuFamily": "Core i3",
      "generation": "12th Gen",
      "ramGb": 8,
      "storageGb": 256,
      "storageType": "NVMe SSD",
      "gpuType": "integrated",
      "isDedicatedGpu": false
    },
    "fullSpecs": {
      "performance": {
        "processor": "Intel Core i3-1215U",
        "coresThreads": "6 Cores (2P + 4E) / 8 Threads",
        "clocks": "1.20 GHz Base, up to 4.40 GHz Turbo",
        "cache": "10 MB Intel Smart Cache"
      },
      "memoryStorage": {
        "ramSize": "8 GB",
        "ramType": "DDR4",
        "ramSpeed": "3200 MHz",
        "ramSlots": "2x SO-DIMM Slots (Upgradable to 32GB)",
        "storageSize": "256 GB",
        "storageType": "NVMe SSD",
        "interface": "PCIe NVMe M.2 2280",
        "readSpeed": "Up to 2,400 MB/s"
      },
      "display": {
        "size": "13.3\"",
        "resolution": "FHD (1920 x 1080)",
        "panelType": "IPS Anti-Glare",
        "refreshRate": "60 Hz",
        "touchAntiGlare": "Anti-Glare (Non-touch), 250 nits"
      },
      "graphics": {
        "gpuName": "Intel UHD Graphics",
        "type": "Integrated",
        "vram": "Shared System Memory"
      },
      "connectivityPorts": {
        "ports": "1x USB Type-C (USB Power Delivery, DisplayPort 1.4), 2x USB Type-A (1 charging), 1x HDMI 2.0, Headphone/mic combo",
        "wireless": "Intel Wi-Fi 6E AX211 + Bluetooth 5.3"
      },
      "batteryBuild": {
        "battery": "42.75Wh / 51Wh HP Long Life Fast Charge",
        "weight": "1.28 kg (2.81 lbs)",
        "keyboard": "HP Premium Spill-Resistant Backlit Keyboard",
        "webcam": "720p HD Privacy Camera",
        "os": "Windows 11 Pro 64-bit Licensed"
      },
      "conditionWarranty": {
        "condition": "Grade A+ Like New \u00b7 Modern Compact",
        "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"
      }
    },
    "bgTone": "white",
    "bgColor": "rgb(254, 254, 254)",
    "tintColor": "rgba(76, 124, 255, 0.04)",
    "processedImg": "images/processed/laptop-16-cutout.webp",
    "stock": 3
  },
  {
    "id": 17,
    "name": "Lenovo ThinkPad T480s",
    "brand": "lenovo",
    "brandName": "Lenovo",
    "series": "ThinkPad T480s",
    "cpu": "Intel Core i5-8350U Quad-Core vPro",
    "cpuTag": "intel_i5",
    "gen": "8th",
    "ram": 16,
    "storage": 256,
    "display": "14\" FHD IPS Anti-Glare",
    "gpu": "Intel UHD Graphics 620",
    "gpuType": "integrated",
    "category": "Legendary Slim",
    "badge": "Cult Classic",
    "badgeType": "b-corp",
    "price": 68000,
    "priceFormatted": "Rs 68,000",
    "priceUsd": 245,
    "img": "images/laptop-17-lenovo-thinkpad-t480s-17.jpg",
    "condition": "Like New (10/10) \u00b7 Certified Refurbished",
    "warranty": "1 Year Local Warranty + 7 Days Checking",
    "useCases": [
      "programming",
      "office",
      "student"
    ],
    "ramGb": 8,
    "storageGb": 256,
    "storageType": "NVMe SSD",
    "cpuBrand": "Intel",
    "cpuTier": "Core i5",
    "cpuGen": 8,
    "gpuCategory": "integrated",
    "isDedicatedGpu": false,
    "gpuModel": "Intel UHD Graphics 620",
    "isRamUpgradable": true,
    "ramUpgradeOptions": [
      16,
      32
    ],
    "storageUpgradeOptions": [
      256,
      512,
      1000
    ],
    "legacyName": "Lenovo T480s Core i5 8th",
    "shortSpecs": {
      "cpuFamily": "Core i5",
      "generation": "8th Gen",
      "ramGb": 8,
      "storageGb": 256,
      "storageType": "NVMe SSD",
      "gpuType": "integrated",
      "isDedicatedGpu": false
    },
    "fullSpecs": {
      "performance": {
        "processor": "Intel Core i5-8350U vPro Quad Core",
        "coresThreads": "4 Cores / 8 Threads",
        "clocks": "1.70 GHz Base, up to 3.60 GHz Boost",
        "cache": "6 MB Intel Smart Cache"
      },
      "memoryStorage": {
        "ramSize": "8 GB",
        "ramType": "DDR4",
        "ramSpeed": "2400 MHz",
        "ramSlots": "8GB Soldered + 1 SO-DIMM Slot (Upgradable to 24GB/40GB)",
        "storageSize": "256 GB",
        "storageType": "NVMe SSD",
        "interface": "PCIe Gen3 x4 M.2 2280",
        "readSpeed": "Up to 2,500 MB/s"
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
        "ports": "2x USB 3.1 Gen 1 (1 Always On), 1x USB-C 3.1 Gen 1, 1x Thunderbolt 3, HDMI 1.4b, RJ-45 Gigabit, 4-in-1 Card Reader, Audio Jack",
        "wireless": "Intel Dual Band Wireless-AC 8265 + Bluetooth 4.2"
      },
      "batteryBuild": {
        "battery": "57Wh Internal Li-Ion (Rapid Charge 80% in 1 hr)",
        "weight": "1.32 kg (2.90 lbs) Slim Magnesium Chassis",
        "keyboard": "Legendary Spill-Resistant Backlit Keyboard with TrackPoint",
        "webcam": "720p HD with ThinkShutter Privacy Cover",
        "os": "Windows 11 Pro 64-bit Licensed"
      },
      "conditionWarranty": {
        "condition": "Grade A Like New \u00b7 Legendary Slim Workhorse",
        "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"
      }
    },
    "bgTone": "white",
    "bgColor": "rgb(249, 247, 247)",
    "tintColor": "rgba(76, 124, 255, 0.04)",
    "processedImg": "images/processed/laptop-17-cutout.webp",
    "stock": 3
  },
  {
    "id": 18,
    "name": "HP EliteBook Folio 9480m",
    "brand": "hp",
    "brandName": "HP",
    "series": "EliteBook Folio 9480m",
    "cpu": "Intel Core i5-4310U 4th Gen",
    "cpuTag": "intel_i5",
    "gen": "4th",
    "ram": 8,
    "storage": 256,
    "display": "14\" HD+ (1600x900) Aluminum",
    "gpu": "Intel HD Graphics 4400",
    "gpuType": "integrated",
    "category": "Aluminum Slim",
    "badge": "Budget",
    "badgeType": "b-val",
    "price": 38000,
    "priceFormatted": "Rs 38,000",
    "priceUsd": 135,
    "img": "images/laptop-18-hp-elitebook-folio-9480m-18.jpg",
    "condition": "Like New (10/10) \u00b7 Certified Refurbished",
    "warranty": "1 Year Local Warranty + 7 Days Checking",
    "useCases": [
      "student",
      "office"
    ],
    "ramGb": 8,
    "storageGb": 256,
    "storageType": "NVMe SSD",
    "cpuBrand": "Intel",
    "cpuTier": "Core i5",
    "cpuGen": 4,
    "gpuCategory": "integrated",
    "isDedicatedGpu": false,
    "gpuModel": "Intel HD Graphics 4400",
    "isRamUpgradable": false,
    "ramUpgradeOptions": [
      8
    ],
    "storageUpgradeOptions": [
      256,
      512,
      1000
    ],
    "legacyName": "HP 9480 Core i5 4th",
    "shortSpecs": {
      "cpuFamily": "Core i5",
      "generation": "4th Gen",
      "ramGb": 8,
      "storageGb": 256,
      "storageType": "SATA SSD",
      "gpuType": "integrated",
      "isDedicatedGpu": false
    },
    "fullSpecs": {
      "performance": {
        "processor": "Intel Core i5-4310U",
        "coresThreads": "2 Cores / 4 Threads",
        "clocks": "2.00 GHz Base, up to 3.00 GHz Boost",
        "cache": "3 MB Intel Smart Cache"
      },
      "memoryStorage": {
        "ramSize": "8 GB",
        "ramType": "DDR3L",
        "ramSpeed": "1600 MHz",
        "ramSlots": "2x SO-DIMM Slots (Upgradable to 16GB)",
        "storageSize": "256 GB",
        "storageType": "SATA SSD",
        "interface": "2.5\" SATA III SSD / mSATA",
        "readSpeed": "Up to 520 MB/s"
      },
      "display": {
        "size": "14.0\"",
        "resolution": "HD+ (1600 x 900)",
        "panelType": "Anti-Glare LED-backlit",
        "refreshRate": "60 Hz",
        "touchAntiGlare": "Anti-Glare (Non-touch)"
      },
      "graphics": {
        "gpuName": "Intel HD Graphics 4400",
        "type": "Integrated",
        "vram": "Shared System Memory"
      },
      "connectivityPorts": {
        "ports": "3x USB 3.0 (1 charging), 1x DisplayPort 1.2a, 1x VGA, RJ-45 Ethernet, SD/MMC slot, Headphone/Mic combo",
        "wireless": "Intel Dual Band Wireless-AC 7260 + Bluetooth 4.0"
      },
      "batteryBuild": {
        "battery": "52Wh 4-Cell Long Life Polymer",
        "weight": "1.61 kg (3.56 lbs) Slim Silver Magnesium/Aluminum",
        "keyboard": "Spill-Resistant Backlit Keyboard with Dual Point",
        "webcam": "720p HD Webcam",
        "os": "Windows 10/11 Pro 64-bit Licensed"
      },
      "conditionWarranty": {
        "condition": "Clean Used (9/10) \u00b7 Durable Metal Ultrabook",
        "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"
      }
    },
    "bgTone": "white",
    "bgColor": "rgb(249, 249, 249)",
    "tintColor": "rgba(76, 124, 255, 0.04)",
    "processedImg": "images/processed/laptop-18-cutout.webp",
    "stock": 3
  },
  {
    "id": 19,
    "name": "HP ProBook 640 G2",
    "brand": "hp",
    "brandName": "HP",
    "series": "ProBook 640 G2",
    "cpu": "Intel Core i3-6100U 6th Gen",
    "cpuTag": "intel_i3",
    "gen": "6th",
    "ram": 8,
    "storage": 256,
    "display": "14\" HD Anti-Glare",
    "gpu": "Intel HD Graphics 520",
    "gpuType": "integrated",
    "category": "Everyday Office",
    "badge": "Under 40k",
    "badgeType": "b-val",
    "price": 39000,
    "priceFormatted": "Rs 39,000",
    "priceUsd": 140,
    "img": "images/laptop-19-hp-probook-640-g2-19.jpg",
    "condition": "Like New (10/10) \u00b7 Certified Refurbished",
    "warranty": "1 Year Local Warranty + 7 Days Checking",
    "useCases": [
      "student",
      "office"
    ],
    "ramGb": 8,
    "storageGb": 256,
    "storageType": "NVMe SSD",
    "cpuBrand": "Intel",
    "cpuTier": "Core i3",
    "cpuGen": 6,
    "gpuCategory": "integrated",
    "isDedicatedGpu": false,
    "gpuModel": "Intel HD Graphics 520",
    "isRamUpgradable": true,
    "ramUpgradeOptions": [
      8,
      16,
      32
    ],
    "storageUpgradeOptions": [
      256,
      512,
      1000
    ],
    "legacyName": "HP 640G2 Core i3 6th",
    "shortSpecs": {
      "cpuFamily": "Core i3",
      "generation": "6th Gen",
      "ramGb": 8,
      "storageGb": 256,
      "storageType": "SATA SSD",
      "gpuType": "integrated",
      "isDedicatedGpu": false
    },
    "fullSpecs": {
      "performance": {
        "processor": "Intel Core i3-6100U",
        "coresThreads": "2 Cores / 4 Threads",
        "clocks": "2.30 GHz Base",
        "cache": "3 MB Intel Smart Cache"
      },
      "memoryStorage": {
        "ramSize": "8 GB",
        "ramType": "DDR4",
        "ramSpeed": "2133 MHz",
        "ramSlots": "2x SO-DIMM Slots (Upgradable to 16GB/32GB)",
        "storageSize": "256 GB",
        "storageType": "SATA SSD",
        "interface": "2.5\" SATA III SSD / M.2",
        "readSpeed": "Up to 530 MB/s"
      },
      "display": {
        "size": "14.0\"",
        "resolution": "FHD (1920 x 1080) / HD",
        "panelType": "Anti-Glare Slim LED",
        "refreshRate": "60 Hz",
        "touchAntiGlare": "Anti-Glare (Non-touch)"
      },
      "graphics": {
        "gpuName": "Intel HD Graphics 520",
        "type": "Integrated",
        "vram": "Shared System Memory"
      },
      "connectivityPorts": {
        "ports": "1x USB-C, 2x USB 3.0 (1 charging), 1x DisplayPort, 1x VGA, RJ-45, SD Card Reader, Audio Jack",
        "wireless": "Intel 802.11a/b/g/n/ac + Bluetooth 4.2"
      },
      "batteryBuild": {
        "battery": "46Wh 3-Cell HP Long Life Prismatic",
        "weight": "1.95 kg (4.30 lbs)",
        "keyboard": "HP Spill-Resistant Keyboard",
        "webcam": "720p HD Webcam",
        "os": "Windows 10/11 Pro 64-bit Licensed"
      },
      "conditionWarranty": {
        "condition": "Good Condition (9/10) \u00b7 Reliable Budget Laptop",
        "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"
      }
    },
    "bgTone": "white",
    "bgColor": "rgb(255, 255, 255)",
    "tintColor": "rgba(76, 124, 255, 0.04)",
    "processedImg": "images/processed/laptop-19-cutout.webp",
    "stock": 3
  },
  {
    "id": 20,
    "name": "Microsoft Surface Laptop 3",
    "brand": "microsoft",
    "brandName": "Microsoft",
    "series": "Surface Laptop 3",
    "cpu": "Intel Core i5-1035G7 10th Gen",
    "cpuTag": "intel_i5",
    "gen": "10th",
    "ram": 8,
    "storage": 256,
    "display": "13.5\" PixelSense 2256x1504 Touch (3:2)",
    "gpu": "Intel Iris Plus Graphics",
    "gpuType": "integrated",
    "category": "Designer Ultrabook",
    "badge": "3:2 Aspect",
    "badgeType": "b-val",
    "price": 115000,
    "priceFormatted": "Rs 115,000",
    "priceUsd": 415,
    "img": "images/laptop-20-microsoft-surface-laptop-3-20.jpg",
    "condition": "Like New (10/10) \u00b7 Certified Refurbished",
    "warranty": "1 Year Local Warranty + 7 Days Checking",
    "useCases": [
      "office",
      "student",
      "creator"
    ],
    "ramGb": 8,
    "storageGb": 256,
    "storageType": "NVMe SSD",
    "cpuBrand": "Intel",
    "cpuTier": "Core i5",
    "cpuGen": 10,
    "gpuCategory": "integrated",
    "isDedicatedGpu": false,
    "gpuModel": "Intel Iris Plus Graphics",
    "isRamUpgradable": false,
    "ramUpgradeOptions": [
      8
    ],
    "storageUpgradeOptions": [
      256,
      512,
      1000
    ],
    "legacyName": "Microsoft Surface Laptop Core i5 10th",
    "shortSpecs": {
      "cpuFamily": "Core i5",
      "generation": "10th Gen",
      "ramGb": 8,
      "storageGb": 256,
      "storageType": "NVMe SSD",
      "gpuType": "integrated",
      "isDedicatedGpu": false
    },
    "fullSpecs": {
      "performance": {
        "processor": "Intel Core i5-1035G7",
        "coresThreads": "4 Cores / 8 Threads",
        "clocks": "1.20 GHz Base, up to 3.70 GHz Boost",
        "cache": "6 MB Intel Smart Cache"
      },
      "memoryStorage": {
        "ramSize": "8 GB",
        "ramType": "LPDDR4x",
        "ramSpeed": "3733 MHz",
        "ramSlots": "Soldered (Non-upgradable)",
        "storageSize": "256 GB",
        "storageType": "NVMe SSD",
        "interface": "Removable M.2 2230 NVMe SSD",
        "readSpeed": "Up to 2,200 MB/s"
      },
      "display": {
        "size": "13.5\"",
        "resolution": "2.2K (2256 x 1504) 3:2",
        "panelType": "PixelSense Touchscreen",
        "refreshRate": "60 Hz",
        "touchAntiGlare": "10-Point Multi-Touch with Surface Pen Support, Gorilla Glass 3"
      },
      "graphics": {
        "gpuName": "Intel Iris Plus Graphics",
        "type": "Integrated",
        "vram": "Shared System Memory"
      },
      "connectivityPorts": {
        "ports": "1x USB-C 3.1, 1x USB-A 3.1, 3.5mm Headphone Jack, Surface Connect Port",
        "wireless": "Wi-Fi 6 (802.11ax) + Bluetooth 5.0"
      },
      "batteryBuild": {
        "battery": "45Wh Fast Charging (80% in about 1 hour)",
        "weight": "1.26 kg (2.79 lbs) Aluminum Chassis",
        "keyboard": "Backlit Keyboard with Large Glass Trackpad",
        "webcam": "720p HD f/2.0 with Windows Hello Facial Authentication",
        "os": "Windows 11 Pro 64-bit Licensed"
      },
      "conditionWarranty": {
        "condition": "Pristine Like New (10/10) \u00b7 Minimalist Premium",
        "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"
      }
    },
    "bgTone": "white",
    "bgColor": "rgb(254, 254, 254)",
    "tintColor": "rgba(76, 124, 255, 0.04)",
    "processedImg": "images/processed/laptop-20-cutout.webp",
    "stock": 3
  },
  {
    "id": 21,
    "name": "Lenovo ThinkPad X1 Extreme Gen 2",
    "brand": "lenovo",
    "brandName": "Lenovo",
    "series": "ThinkPad X1 Extreme",
    "cpu": "Intel Core i7-9750H (6-Core/12-Thread 45W)",
    "cpuTag": "intel_i7",
    "gen": "9th",
    "ram": 16,
    "storage": 512,
    "display": "15.6\" FHD IPS 500 nits HDR",
    "gpu": "NVIDIA GeForce GTX 1650 Max-Q 4GB",
    "gpuType": "discrete",
    "category": "Performance / Dev",
    "badge": "Dedicated GPU",
    "badgeType": "b-corp",
    "price": 165000,
    "priceFormatted": "Rs 165,000",
    "priceUsd": 590,
    "img": "images/laptop-21-lenovo-thinkpad-x1-extreme-gen-2-21.jpg",
    "condition": "Like New (10/10) \u00b7 Certified Refurbished",
    "warranty": "1 Year Local Warranty + 7 Days Checking",
    "useCases": [
      "programming",
      "creator",
      "gaming"
    ],
    "ramGb": 16,
    "storageGb": 512,
    "storageType": "NVMe SSD",
    "cpuBrand": "Intel",
    "cpuTier": "Core i7",
    "cpuGen": 9,
    "gpuCategory": "dedicated",
    "isDedicatedGpu": true,
    "gpuModel": "NVIDIA GeForce GTX 1650 Max-Q 4GB",
    "isRamUpgradable": true,
    "ramUpgradeOptions": [
      16,
      32
    ],
    "storageUpgradeOptions": [
      512,
      1000
    ],
    "legacyName": "Lenovo X1 Extreme Gen 2 Core i7 9th",
    "shortSpecs": {
      "cpuFamily": "Core i7",
      "generation": "9th Gen",
      "ramGb": 16,
      "storageGb": 512,
      "storageType": "NVMe SSD",
      "gpuType": "discrete",
      "isDedicatedGpu": true
    },
    "fullSpecs": {
      "performance": {
        "processor": "Intel Core i7-9750H (45W High-Power)",
        "coresThreads": "6 Cores / 12 Threads",
        "clocks": "2.60 GHz Base, up to 4.50 GHz Turbo",
        "cache": "12 MB Intel Smart Cache"
      },
      "memoryStorage": {
        "ramSize": "16 GB",
        "ramType": "DDR4",
        "ramSpeed": "2666 MHz",
        "ramSlots": "2x SO-DIMM Slots (Upgradable to 64GB)",
        "storageSize": "512 GB",
        "storageType": "NVMe SSD",
        "interface": "Dual M.2 PCIe Gen3 x4 NVMe (2 Slots)",
        "readSpeed": "Up to 3,500 MB/s"
      },
      "display": {
        "size": "15.6\"",
        "resolution": "FHD (1920 x 1080) 500 nits HDR400 IPS / 4K OLED",
        "panelType": "IPS Anti-Glare 500 nits Dolby Vision HDR",
        "refreshRate": "60 Hz",
        "touchAntiGlare": "Anti-Glare (Non-touch)"
      },
      "graphics": {
        "gpuName": "NVIDIA GeForce GTX 1650 Max-Q",
        "type": "Dedicated",
        "vram": "4 GB GDDR5 Dedicated"
      },
      "connectivityPorts": {
        "ports": "2x Thunderbolt 3, 2x USB 3.1 Gen 1, 1x HDMI 2.0, SD Card Reader, Audio combo, Network extension",
        "wireless": "Intel Wi-Fi 6 AX200 + Bluetooth 5.1"
      },
      "batteryBuild": {
        "battery": "80Wh Rapid Charge (80% in 1 hr)",
        "weight": "1.70 kg (3.75 lbs) Carbon-Fiber & Magnesium",
        "keyboard": "ThinkPad Precision Backlit Keyboard with TrackPoint",
        "webcam": "720p HD with ThinkShutter & IR Windows Hello",
        "os": "Windows 11 Pro 64-bit Licensed"
      },
      "conditionWarranty": {
        "condition": "Grade A+ Like New \u00b7 High-Performance Workstation",
        "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"
      }
    },
    "bgTone": "white",
    "bgColor": "rgb(253, 253, 253)",
    "tintColor": "rgba(76, 124, 255, 0.04)",
    "processedImg": "images/processed/laptop-21-cutout.webp",
    "stock": 3
  },
  {
    "id": 22,
    "name": "Dell Latitude 7320 2-in-1",
    "brand": "dell",
    "brandName": "Dell",
    "series": "Latitude 7320",
    "cpu": "Intel Core i5-1145G7 vPro 11th Gen",
    "cpuTag": "intel_i5",
    "gen": "11th",
    "ram": 16,
    "storage": 512,
    "display": "13.3\" FHD Touch 360\u00b0 Gorilla Glass",
    "gpu": "Intel Iris Xe Graphics",
    "gpuType": "integrated",
    "category": "2-in-1 Convertible",
    "badge": "Touch 360\u00b0",
    "badgeType": "b-corp",
    "price": 115000,
    "priceFormatted": "Rs 115,000",
    "priceUsd": 415,
    "img": "images/laptop-22-dell-latitude-7320-2-in-1-22.jpg",
    "condition": "Like New (10/10) \u00b7 Certified Refurbished",
    "warranty": "1 Year Local Warranty + 7 Days Checking",
    "useCases": [
      "office",
      "creator",
      "student"
    ],
    "ramGb": 16,
    "storageGb": 512,
    "storageType": "NVMe SSD",
    "cpuBrand": "Intel",
    "cpuTier": "Core i5",
    "cpuGen": 11,
    "gpuCategory": "integrated",
    "isDedicatedGpu": false,
    "gpuModel": "Intel Iris Xe Graphics",
    "isRamUpgradable": true,
    "ramUpgradeOptions": [
      16,
      32
    ],
    "storageUpgradeOptions": [
      512,
      1000
    ],
    "legacyName": "Dell Latitude 7320(2 in 1) Core i5 11th",
    "shortSpecs": {
      "cpuFamily": "Core i5",
      "generation": "11th Gen",
      "ramGb": 16,
      "storageGb": 512,
      "storageType": "NVMe SSD",
      "gpuType": "integrated",
      "isDedicatedGpu": false
    },
    "fullSpecs": {
      "performance": {
        "processor": "Intel Core i5-1145G7 vPro",
        "coresThreads": "4 Cores / 8 Threads",
        "clocks": "2.60 GHz Base, up to 4.40 GHz Turbo",
        "cache": "8 MB Intel Smart Cache"
      },
      "memoryStorage": {
        "ramSize": "16 GB",
        "ramType": "LPDDR4x",
        "ramSpeed": "4266 MHz",
        "ramSlots": "Soldered Dual-Channel (Non-upgradable)",
        "storageSize": "512 GB",
        "storageType": "NVMe SSD",
        "interface": "PCIe Gen3 x4 M.2 2280",
        "readSpeed": "Up to 3,200 MB/s"
      },
      "display": {
        "size": "13.3\"",
        "resolution": "FHD (1920 x 1080) 16:9",
        "panelType": "IPS Touchscreen 360\u00b0 Convertible",
        "refreshRate": "60 Hz",
        "touchAntiGlare": "Corning Gorilla Glass 6 DX Touch with Active Pen Support, 300 nits"
      },
      "graphics": {
        "gpuName": "Intel Iris Xe Graphics",
        "type": "Integrated",
        "vram": "Shared System Memory"
      },
      "connectivityPorts": {
        "ports": "2x Thunderbolt 4 with Power Delivery & DisplayPort, 1x USB-A 3.2 Gen 1 with PowerShare, 1x HDMI 2.0, MicroSD, Audio Jack",
        "wireless": "Intel Wi-Fi 6 AX201 + Bluetooth 5.1"
      },
      "batteryBuild": {
        "battery": "63Wh ExpressCharge Capable",
        "weight": "1.39 kg (3.06 lbs) CNC Aluminum",
        "keyboard": "Backlit Spill-Resistant Keyboard",
        "webcam": "FHD IR Camera with Proximity Sensor & ExpressSign-in",
        "os": "Windows 11 Pro 64-bit Licensed"
      },
      "conditionWarranty": {
        "condition": "Grade A+ Like New \u00b7 Executive 2-in-1",
        "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"
      }
    },
    "bgTone": "white",
    "bgColor": "rgb(255, 255, 255)",
    "tintColor": "rgba(76, 124, 255, 0.04)",
    "processedImg": "images/processed/laptop-22-cutout.webp",
    "stock": 3
  },
  {
    "id": 23,
    "name": "HP EliteBook 840 G8",
    "brand": "hp",
    "brandName": "HP",
    "series": "EliteBook 840 G8",
    "cpu": "Intel Core i5-1135G7 11th Gen",
    "cpuTag": "intel_i5",
    "gen": "11th",
    "ram": 16,
    "storage": 512,
    "display": "14\" FHD IPS Aluminum Chassis",
    "gpu": "Intel Iris Xe Graphics",
    "gpuType": "integrated",
    "category": "Corporate Ultrabook",
    "badge": "Best Seller",
    "badgeType": "b-corp",
    "price": 105000,
    "priceFormatted": "Rs 105,000",
    "priceUsd": 375,
    "img": "images/laptop-23-hp-elitebook-840-g8-23.jpg",
    "condition": "Like New (10/10) \u00b7 Certified Refurbished",
    "warranty": "1 Year Local Warranty + 7 Days Checking",
    "useCases": [
      "office",
      "programming",
      "student"
    ],
    "ramGb": 16,
    "storageGb": 512,
    "storageType": "NVMe SSD",
    "cpuBrand": "Intel",
    "cpuTier": "Core i5",
    "cpuGen": 11,
    "gpuCategory": "integrated",
    "isDedicatedGpu": false,
    "gpuModel": "Intel Iris Xe Graphics",
    "isRamUpgradable": true,
    "ramUpgradeOptions": [
      16,
      32
    ],
    "storageUpgradeOptions": [
      512,
      1000
    ],
    "legacyName": "HP EliteBook 840G8 Core i5 11th",
    "shortSpecs": {
      "cpuFamily": "Core i5",
      "generation": "11th Gen",
      "ramGb": 16,
      "storageGb": 512,
      "storageType": "NVMe SSD",
      "gpuType": "integrated",
      "isDedicatedGpu": false
    },
    "fullSpecs": {
      "performance": {
        "processor": "Intel Core i5-1135G7",
        "coresThreads": "4 Cores / 8 Threads",
        "clocks": "2.40 GHz Base, up to 4.20 GHz Turbo",
        "cache": "8 MB Intel Smart Cache"
      },
      "memoryStorage": {
        "ramSize": "16 GB",
        "ramType": "DDR4",
        "ramSpeed": "3200 MHz",
        "ramSlots": "2x SO-DIMM Slots (Upgradable to 64GB)",
        "storageSize": "512 GB",
        "storageType": "NVMe SSD",
        "interface": "PCIe Gen3 x4 NVMe M.2 2280",
        "readSpeed": "Up to 3,200 MB/s"
      },
      "display": {
        "size": "14.0\"",
        "resolution": "FHD (1920 x 1080)",
        "panelType": "IPS Anti-Glare",
        "refreshRate": "60 Hz",
        "touchAntiGlare": "Anti-Glare 400 nits Low Power HP Sure View or sRGB"
      },
      "graphics": {
        "gpuName": "Intel Iris Xe Graphics",
        "type": "Integrated",
        "vram": "Shared System Memory"
      },
      "connectivityPorts": {
        "ports": "2x Thunderbolt 4 USB-C, 2x USB-A 3.2 Gen 1 (1 charging), 1x HDMI 2.0b, Headphone/mic combo",
        "wireless": "Intel Wi-Fi 6 AX201 (2x2) + Bluetooth 5.0"
      },
      "batteryBuild": {
        "battery": "53Wh HP Long Life Fast Charge (50% in 30 mins)",
        "weight": "1.32 kg (2.9 lbs) All-Metal Aluminum",
        "keyboard": "HP Premium Spill-Resistant Backlit Keyboard",
        "webcam": "720p HD IR Camera with Windows Hello & Privacy Shutter",
        "os": "Windows 11 Pro 64-bit Licensed"
      },
      "conditionWarranty": {
        "condition": "Grade A+ Like New \u00b7 Executive Business Ultrabook",
        "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"
      }
    },
    "bgTone": "white",
    "bgColor": "rgb(255, 255, 255)",
    "tintColor": "rgba(76, 124, 255, 0.04)",
    "processedImg": "images/processed/laptop-23-cutout.webp",
    "stock": 3
  },
  {
    "id": 24,
    "name": "HP EliteBook 840 G7",
    "brand": "hp",
    "brandName": "HP",
    "series": "EliteBook 840 G7",
    "cpu": "Intel Core i5-10310U 10th Gen",
    "cpuTag": "intel_i5",
    "gen": "10th",
    "ram": 16,
    "storage": 512,
    "display": "14\" FHD IPS Anti-Glare B&O Audio",
    "gpu": "Intel UHD Graphics",
    "gpuType": "integrated",
    "category": "All-Aluminum Classic",
    "badge": "In Demand",
    "badgeType": "b-corp",
    "price": 88000,
    "priceFormatted": "Rs 88,000",
    "priceUsd": 315,
    "img": "images/laptop-24-hp-elitebook-840-g7-24.jpg",
    "condition": "Like New (10/10) \u00b7 Certified Refurbished",
    "warranty": "1 Year Local Warranty + 7 Days Checking",
    "useCases": [
      "office",
      "student",
      "programming"
    ],
    "ramGb": 16,
    "storageGb": 512,
    "storageType": "NVMe SSD",
    "cpuBrand": "Intel",
    "cpuTier": "Core i5",
    "cpuGen": 10,
    "gpuCategory": "integrated",
    "isDedicatedGpu": false,
    "gpuModel": "Intel UHD Graphics",
    "isRamUpgradable": true,
    "ramUpgradeOptions": [
      16,
      32
    ],
    "storageUpgradeOptions": [
      512,
      1000
    ],
    "legacyName": "HP EliteBook 840G7 Core i5 10th",
    "shortSpecs": {
      "cpuFamily": "Core i5",
      "generation": "10th Gen",
      "ramGb": 16,
      "storageGb": 512,
      "storageType": "NVMe SSD",
      "gpuType": "integrated",
      "isDedicatedGpu": false
    },
    "fullSpecs": {
      "performance": {
        "processor": "Intel Core i5-10310U vPro",
        "coresThreads": "4 Cores / 8 Threads",
        "clocks": "1.70 GHz Base, up to 4.40 GHz Boost",
        "cache": "6 MB Intel Smart Cache"
      },
      "memoryStorage": {
        "ramSize": "16 GB",
        "ramType": "DDR4",
        "ramSpeed": "2666 MHz",
        "ramSlots": "2x SO-DIMM Slots (Upgradable to 64GB)",
        "storageSize": "512 GB",
        "storageType": "NVMe SSD",
        "interface": "PCIe Gen3 x4 NVMe M.2 2280",
        "readSpeed": "Up to 2,800 MB/s"
      },
      "display": {
        "size": "14.0\"",
        "resolution": "FHD (1920 x 1080)",
        "panelType": "IPS Anti-Glare",
        "refreshRate": "60 Hz",
        "touchAntiGlare": "Anti-Glare 250 nits / 400 nits Low Power"
      },
      "graphics": {
        "gpuName": "Intel UHD Graphics 620",
        "type": "Integrated",
        "vram": "Shared System Memory"
      },
      "connectivityPorts": {
        "ports": "2x USB-C (Thunderbolt 3), 2x USB-A 3.1 Gen 1 (1 charging), 1x HDMI 1.4b, Headphone/mic combo",
        "wireless": "Intel Wi-Fi 6 AX201 + Bluetooth 5.0"
      },
      "batteryBuild": {
        "battery": "53Wh HP Long Life Fast Charge",
        "weight": "1.33 kg (2.93 lbs) Sleek Silver Aluminum",
        "keyboard": "HP Premium Spill-Resistant Backlit Keyboard",
        "webcam": "720p HD with Integrated Privacy Shutter",
        "os": "Windows 11 Pro 64-bit Licensed"
      },
      "conditionWarranty": {
        "condition": "Grade A+ Like New \u00b7 Certified Refurbished",
        "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"
      }
    },
    "bgTone": "white",
    "bgColor": "rgb(255, 255, 255)",
    "tintColor": "rgba(76, 124, 255, 0.04)",
    "processedImg": "images/processed/laptop-24-cutout.webp",
    "stock": 3
  },
  {
    "id": 25,
    "name": "Dell Precision 5560",
    "brand": "dell",
    "brandName": "Dell",
    "series": "Precision 5560",
    "cpu": "Intel Core i9-11950H (8-Core/16-Thread up to 5.0GHz)",
    "cpuTag": "intel_i9",
    "gen": "11th",
    "ram": 32,
    "storage": 1000,
    "display": "15.6\" UHD+ 4K (3840x2400) 500-nit Touch",
    "gpu": "NVIDIA RTX A2000 4GB GDDR6",
    "gpuType": "rtx",
    "category": "Heavy Workstation",
    "badge": "Core i9 Beast",
    "badgeType": "b-game",
    "price": 285000,
    "priceFormatted": "Rs 285,000",
    "priceUsd": 1020,
    "img": "images/laptop-25-dell-precision-5560-workstation-25.jpg",
    "condition": "Open Box / Brand New Condition",
    "warranty": "1 Year Local Warranty + 7 Days Checking",
    "useCases": [
      "creator",
      "programming",
      "gaming"
    ],
    "ramGb": 32,
    "storageGb": 1000,
    "storageType": "NVMe SSD",
    "cpuBrand": "Intel",
    "cpuTier": "Core i9",
    "cpuGen": 11,
    "gpuCategory": "dedicated",
    "isDedicatedGpu": true,
    "gpuModel": "NVIDIA RTX A2000 4GB GDDR6",
    "isRamUpgradable": true,
    "ramUpgradeOptions": [
      16,
      32
    ],
    "storageUpgradeOptions": [
      512,
      1000
    ],
    "legacyName": "Dell Precision 5560 Core i9 11th",
    "shortSpecs": {
      "cpuFamily": "Core i9",
      "generation": "11th Gen",
      "ramGb": 32,
      "storageGb": 1000,
      "storageType": "NVMe SSD",
      "gpuType": "rtx",
      "isDedicatedGpu": true
    },
    "fullSpecs": {
      "performance": {
        "processor": "Intel Core i9-11950H vPro (45W Workstation)",
        "coresThreads": "8 Cores / 16 Threads",
        "clocks": "2.60 GHz Base, up to 5.00 GHz Max Turbo",
        "cache": "24 MB Intel Smart Cache"
      },
      "memoryStorage": {
        "ramSize": "32 GB",
        "ramType": "DDR4",
        "ramSpeed": "3200 MHz",
        "ramSlots": "2x SO-DIMM Slots (Upgradable to 64GB)",
        "storageSize": "1 TB",
        "storageType": "NVMe SSD",
        "interface": "Dual M.2 PCIe Gen4 x4 NVMe Slots",
        "readSpeed": "Up to 6,900 MB/s"
      },
      "display": {
        "size": "15.6\"",
        "resolution": "FHD+ (1920 x 1200) 16:10 500 nits / 4K UHD+ Touch",
        "panelType": "IPS UltraSharp 100% sRGB",
        "refreshRate": "60 Hz",
        "touchAntiGlare": "Anti-Glare 500 nits InfinityEdge"
      },
      "graphics": {
        "gpuName": "NVIDIA RTX A2000 Laptop GPU",
        "type": "Dedicated",
        "vram": "4 GB GDDR6 Dedicated Workstation"
      },
      "connectivityPorts": {
        "ports": "2x Thunderbolt 4 USB-C (DisplayPort/PD), 1x USB-C 3.2 Gen 2, Full-size SD Card Slot, Audio Jack",
        "wireless": "Intel Wi-Fi 6 AX201 + Bluetooth 5.2"
      },
      "batteryBuild": {
        "battery": "86Wh 6-cell Lithium-Ion ExpressCharge",
        "weight": "1.84 kg (4.06 lbs) CNC Aluminum & Carbon Fiber",
        "keyboard": "Backlit Keyboard with Large Glass Touchpad",
        "webcam": "720p HD IR Camera with Windows Hello Proximity Sensor",
        "os": "Windows 11 Pro for Workstations Licensed"
      },
      "conditionWarranty": {
        "condition": "Pristine Grade A+ \u00b7 Mobile Workstation Beast",
        "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"
      }
    },
    "bgTone": "white",
    "bgColor": "rgb(254, 254, 254)",
    "tintColor": "rgba(76, 124, 255, 0.04)",
    "processedImg": "images/processed/laptop-25-cutout.webp",
    "stock": 3
  },
  {
    "id": 26,
    "name": "Dell XPS 15 9575 2-in-1",
    "brand": "dell",
    "brandName": "Dell",
    "series": "XPS 15",
    "cpu": "Intel Core i7-8705G with Radeon RX Vega M",
    "cpuTag": "intel_i7",
    "gen": "8th",
    "ram": 16,
    "storage": 512,
    "display": "15.6\" 4K UHD Touch 360\u00b0 Convertible",
    "gpu": "Radeon RX Vega M GL 4GB HBM2",
    "gpuType": "discrete",
    "category": "Creator 2-in-1",
    "badge": "Rare 4K 360\u00b0",
    "badgeType": "b-val",
    "price": 115000,
    "priceFormatted": "Rs 115,000",
    "priceUsd": 415,
    "img": "images/laptop-26-dell-xps-15-9575-2-in-1-26.jpg",
    "condition": "Like New (10/10) \u00b7 Certified Refurbished",
    "warranty": "1 Year Local Warranty + 7 Days Checking",
    "useCases": [
      "creator",
      "gaming",
      "office"
    ],
    "ramGb": 16,
    "storageGb": 512,
    "storageType": "NVMe SSD",
    "cpuBrand": "Intel",
    "cpuTier": "Core i7",
    "cpuGen": 8,
    "gpuCategory": "dedicated",
    "isDedicatedGpu": true,
    "gpuModel": "Radeon RX Vega M GL 4GB HBM2",
    "isRamUpgradable": true,
    "ramUpgradeOptions": [
      16,
      32
    ],
    "storageUpgradeOptions": [
      512,
      1000
    ],
    "legacyName": "Dell XPS 15 9575 Core i7 8th",
    "shortSpecs": {
      "cpuFamily": "Core i7",
      "generation": "8th Gen",
      "ramGb": 16,
      "storageGb": 512,
      "storageType": "NVMe SSD",
      "gpuType": "discrete",
      "isDedicatedGpu": true
    },
    "fullSpecs": {
      "performance": {
        "processor": "Intel Core i7-8705G with Radeon RX Vega M GL",
        "coresThreads": "4 Cores / 8 Threads (65W Kaby Lake-G)",
        "clocks": "3.10 GHz Base, up to 4.10 GHz Turbo",
        "cache": "8 MB Intel Smart Cache"
      },
      "memoryStorage": {
        "ramSize": "16 GB",
        "ramType": "DDR4",
        "ramSpeed": "2400 MHz",
        "ramSlots": "Soldered Dual-Channel (Non-upgradable)",
        "storageSize": "512 GB",
        "storageType": "NVMe SSD",
        "interface": "PCIe Gen3 x4 M.2 2280",
        "readSpeed": "Up to 3,000 MB/s"
      },
      "display": {
        "size": "15.6\"",
        "resolution": "4K UHD (3840 x 2160) Touch / FHD Touch",
        "panelType": "IPS InfinityEdge 100% AdobeRGB",
        "refreshRate": "60 Hz",
        "touchAntiGlare": "Corning Gorilla Glass 4 360\u00b0 Touch with Dell Premium Pen Support"
      },
      "graphics": {
        "gpuName": "Radeon RX Vega M GL Graphics",
        "type": "Dedicated",
        "vram": "4 GB HBM2 High-Bandwidth Dedicated"
      },
      "connectivityPorts": {
        "ports": "2x Thunderbolt 3 with Power Delivery & DisplayPort, 2x USB-C 3.1 with Power Delivery, MicroSD, Audio Jack",
        "wireless": "Killer 1435 802.11ac 2x2 + Bluetooth 4.1"
      },
      "batteryBuild": {
        "battery": "75Wh 6-Cell Lithium-Ion Battery",
        "weight": "2.00 kg (4.41 lbs) Ultra-thin MagLev Body",
        "keyboard": "MagLev Keyboard (Magnetic Levitation Keys)",
        "webcam": "720p HD Webcam with Windows Hello IR Facial Recognition",
        "os": "Windows 11 Pro 64-bit Licensed"
      },
      "conditionWarranty": {
        "condition": "Pristine Grade A+ \u00b7 Rare Powerful Convertible",
        "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"
      }
    },
    "bgTone": "white",
    "bgColor": "rgb(255, 255, 255)",
    "tintColor": "rgba(76, 124, 255, 0.04)",
    "processedImg": "images/processed/laptop-26-cutout.webp",
    "stock": 3
  },
  {
    "id": 27,
    "name": "HP EliteBook x360 1030 G4",
    "brand": "hp",
    "brandName": "HP",
    "series": "EliteBook x360 1030",
    "cpu": "Intel Core i5-8365U Quad Core",
    "cpuTag": "intel_i5",
    "gen": "8th",
    "ram": 16,
    "storage": 512,
    "display": "13.3\" FHD Touch 360\u00b0 Privacy Screen",
    "gpu": "Intel UHD Graphics 620",
    "gpuType": "integrated",
    "category": "Executive 2-in-1",
    "badge": "SureView Touch",
    "badgeType": "b-corp",
    "price": 82000,
    "priceFormatted": "Rs 82,000",
    "priceUsd": 295,
    "img": "images/laptop-27-hp-elitebook-x360-1030-g4-27.jpg",
    "condition": "Like New (10/10) \u00b7 Certified Refurbished",
    "warranty": "1 Year Local Warranty + 7 Days Checking",
    "useCases": [
      "office",
      "student"
    ],
    "ramGb": 16,
    "storageGb": 512,
    "storageType": "NVMe SSD",
    "cpuBrand": "Intel",
    "cpuTier": "Core i5",
    "cpuGen": 8,
    "gpuCategory": "integrated",
    "isDedicatedGpu": false,
    "gpuModel": "Intel UHD Graphics 620",
    "isRamUpgradable": true,
    "ramUpgradeOptions": [
      16,
      32
    ],
    "storageUpgradeOptions": [
      512,
      1000
    ],
    "legacyName": "HP EliteBook 1030G4 Core i5 8th",
    "shortSpecs": {
      "cpuFamily": "Core i5",
      "generation": "8th Gen",
      "ramGb": 16,
      "storageGb": 512,
      "storageType": "NVMe SSD",
      "gpuType": "integrated",
      "isDedicatedGpu": false
    },
    "fullSpecs": {
      "performance": {
        "processor": "Intel Core i5-8365U vPro Quad Core",
        "coresThreads": "4 Cores / 8 Threads",
        "clocks": "1.60 GHz Base, up to 4.10 GHz Boost",
        "cache": "6 MB Intel Smart Cache"
      },
      "memoryStorage": {
        "ramSize": "16 GB",
        "ramType": "LPDDR3",
        "ramSpeed": "2133 MHz",
        "ramSlots": "Soldered Dual-Channel (Non-upgradable)",
        "storageSize": "512 GB",
        "storageType": "NVMe SSD",
        "interface": "PCIe Gen3 x4 M.2 2280",
        "readSpeed": "Up to 3,000 MB/s"
      },
      "display": {
        "size": "13.3\"",
        "resolution": "FHD (1920 x 1080) BrightView",
        "panelType": "IPS Touchscreen 360\u00b0 Convertible",
        "refreshRate": "60 Hz",
        "touchAntiGlare": "Corning Gorilla Glass 5 Touch with Active Pen Support, 400 nits"
      },
      "graphics": {
        "gpuName": "Intel UHD Graphics 620",
        "type": "Integrated",
        "vram": "Shared System Memory"
      },
      "connectivityPorts": {
        "ports": "2x Thunderbolt 3 (USB-C), 1x USB 3.1 Gen 1 (charging), 1x HDMI 1.4, Headphone/mic combo",
        "wireless": "Intel Wi-Fi 6 AX200 + Bluetooth 5.0"
      },
      "batteryBuild": {
        "battery": "56.2Wh HP Long Life Fast Charge",
        "weight": "1.25 kg (2.76 lbs) Precision CNC Aluminum",
        "keyboard": "HP Premium Collaboration Backlit Spill-Resistant",
        "webcam": "1080p FHD IR Camera with HP Privacy Shutter",
        "os": "Windows 11 Pro 64-bit Licensed"
      },
      "conditionWarranty": {
        "condition": "Grade A+ Like New \u00b7 Business 2-in-1",
        "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"
      }
    },
    "bgTone": "white",
    "bgColor": "rgb(255, 255, 255)",
    "tintColor": "rgba(76, 124, 255, 0.04)",
    "processedImg": "images/processed/laptop-27-cutout.webp",
    "stock": 3
  },
  {
    "id": 28,
    "name": "Lenovo ThinkPad X13 Gen 4",
    "brand": "lenovo",
    "brandName": "Lenovo",
    "series": "ThinkPad X13",
    "cpu": "Intel Core i7-1355U 13th Gen (10-Core)",
    "cpuTag": "intel_i7",
    "gen": "13th",
    "ram": 16,
    "storage": 512,
    "display": "13.3\" WUXGA 16:10 IPS 400 nits",
    "gpu": "Intel Iris Xe Graphics",
    "gpuType": "integrated",
    "category": "Modern Compact",
    "badge": "13th Gen Pro",
    "badgeType": "b-corp",
    "price": 245000,
    "priceFormatted": "Rs 245,000",
    "priceUsd": 880,
    "img": "images/laptop-28-lenovo-thinkpad-x13-gen-4-28.jpg",
    "condition": "Like New (10/10) \u00b7 Certified Refurbished",
    "warranty": "1 Year Local Warranty + 7 Days Checking",
    "useCases": [
      "office",
      "programming",
      "creator"
    ],
    "ramGb": 16,
    "storageGb": 512,
    "storageType": "NVMe SSD",
    "cpuBrand": "Intel",
    "cpuTier": "Core i7",
    "cpuGen": 13,
    "gpuCategory": "integrated",
    "isDedicatedGpu": false,
    "gpuModel": "Intel Iris Xe Graphics",
    "isRamUpgradable": false,
    "ramUpgradeOptions": [
      16
    ],
    "storageUpgradeOptions": [
      512,
      1000
    ],
    "legacyName": "Lenovo X13 Gen 4 Core i7 13th",
    "shortSpecs": {
      "cpuFamily": "Core i7",
      "generation": "13th Gen",
      "ramGb": 16,
      "storageGb": 512,
      "storageType": "NVMe SSD",
      "gpuType": "integrated",
      "isDedicatedGpu": false
    },
    "fullSpecs": {
      "performance": {
        "processor": "Intel Core i7-1355U",
        "coresThreads": "10 Cores (2P + 8E) / 12 Threads",
        "clocks": "1.70 GHz Base, up to 5.00 GHz Turbo",
        "cache": "12 MB Intel Smart Cache"
      },
      "memoryStorage": {
        "ramSize": "16 GB",
        "ramType": "LPDDR5",
        "ramSpeed": "4800 MHz",
        "ramSlots": "Soldered Dual-Channel (Non-upgradable)",
        "storageSize": "512 GB",
        "storageType": "NVMe SSD",
        "interface": "PCIe Gen4 x4 NVMe M.2 2280",
        "readSpeed": "Up to 5,000 MB/s"
      },
      "display": {
        "size": "13.3\"",
        "resolution": "WUXGA (1920 x 1200) 16:10",
        "panelType": "IPS Anti-Glare 100% sRGB",
        "refreshRate": "60 Hz",
        "touchAntiGlare": "Anti-Glare 300 nits (Non-touch)"
      },
      "graphics": {
        "gpuName": "Intel Iris Xe Graphics",
        "type": "Integrated",
        "vram": "Shared System Memory"
      },
      "connectivityPorts": {
        "ports": "2x Thunderbolt 4 USB-C, 2x USB-A 3.2 Gen 1 (1 Always On), 1x HDMI 2.1, Audio combo jack",
        "wireless": "Intel Wi-Fi 6E AX211 + Bluetooth 5.1"
      },
      "batteryBuild": {
        "battery": "54.7Wh Rapid Charge Battery",
        "weight": "1.09 kg (2.41 lbs) Ultra-Lightweight Carbon/Magnesium",
        "keyboard": "Backlit Spill-Resistant Keyboard with TrackPoint",
        "webcam": "FHD 1080p + IR Hybrid with Privacy Shutter",
        "os": "Windows 11 Pro 64-bit Licensed"
      },
      "conditionWarranty": {
        "condition": "Pristine Like New (10/10) \u00b7 Latest Generation Ultrabook",
        "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"
      }
    },
    "bgTone": "white",
    "bgColor": "rgb(255, 255, 255)",
    "tintColor": "rgba(76, 124, 255, 0.04)",
    "processedImg": "images/processed/laptop-28-cutout.webp",
    "stock": 3
  },
  {
    "id": 29,
    "name": "Dell Vostro 5490",
    "brand": "dell",
    "brandName": "Dell",
    "series": "Vostro 5490",
    "cpu": "Intel Core i5-10210U 10th Gen",
    "cpuTag": "intel_i5",
    "gen": "10th",
    "ram": 8,
    "storage": 256,
    "display": "14\" FHD Anti-Glare LED",
    "gpu": "Intel UHD Graphics",
    "gpuType": "integrated",
    "category": "Business Essential",
    "badge": "Reliable",
    "badgeType": "b-corp",
    "price": 78000,
    "priceFormatted": "Rs 78,000",
    "priceUsd": 280,
    "img": "images/laptop-29-dell-vostro-5490-29.jpg",
    "condition": "Like New (10/10) \u00b7 Certified Refurbished",
    "warranty": "1 Year Local Warranty + 7 Days Checking",
    "useCases": [
      "office",
      "student"
    ],
    "ramGb": 8,
    "storageGb": 256,
    "storageType": "NVMe SSD",
    "cpuBrand": "Intel",
    "cpuTier": "Core i5",
    "cpuGen": 10,
    "gpuCategory": "integrated",
    "isDedicatedGpu": false,
    "gpuModel": "Intel UHD Graphics",
    "isRamUpgradable": true,
    "ramUpgradeOptions": [
      8,
      16,
      32
    ],
    "storageUpgradeOptions": [
      256,
      512,
      1000
    ],
    "legacyName": "Dell VOSTRO 5490 Core i5 10th",
    "shortSpecs": {
      "cpuFamily": "Core i5",
      "generation": "10th Gen",
      "ramGb": 8,
      "storageGb": 256,
      "storageType": "NVMe SSD",
      "gpuType": "integrated",
      "isDedicatedGpu": false
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
        "ramSlots": "1 Soldered + 1 SO-DIMM Slot (Upgradable to 24GB)",
        "storageSize": "256 GB",
        "storageType": "NVMe SSD",
        "interface": "PCIe Gen3 x4 M.2 2280",
        "readSpeed": "Up to 2,200 MB/s"
      },
      "display": {
        "size": "14.0\"",
        "resolution": "FHD (1920 x 1080)",
        "panelType": "IPS Anti-Glare LED-Backlit",
        "refreshRate": "60 Hz",
        "touchAntiGlare": "Anti-Glare (Non-touch)"
      },
      "graphics": {
        "gpuName": "Intel UHD Graphics",
        "type": "Integrated",
        "vram": "Shared System Memory"
      },
      "connectivityPorts": {
        "ports": "1x USB-C 3.1 Gen 1 (DisplayPort/PD), 2x USB-A 3.1 Gen 1, 1x USB 2.0, 1x HDMI 1.4b, RJ-45, MicroSD, Audio Jack",
        "wireless": "802.11ac 1x1 Wi-Fi + Bluetooth 5.0"
      },
      "batteryBuild": {
        "battery": "42Wh 3-Cell Lithium-Ion",
        "weight": "1.49 kg (3.28 lbs) Aluminum Cover",
        "keyboard": "Backlit Spill-Resistant Keyboard",
        "webcam": "720p HD Webcam",
        "os": "Windows 11 Pro 64-bit Licensed"
      },
      "conditionWarranty": {
        "condition": "Grade A+ Like New \u00b7 Business Essential",
        "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"
      }
    },
    "bgTone": "white",
    "bgColor": "rgb(255, 255, 255)",
    "tintColor": "rgba(76, 124, 255, 0.04)",
    "processedImg": "images/processed/laptop-29-cutout.webp",
    "stock": 3
  },
  {
    "id": 30,
    "name": "Dell Latitude 7490",
    "brand": "dell",
    "brandName": "Dell",
    "series": "Latitude 7490",
    "cpu": "Intel Core i7-8650U Quad-Core vPro",
    "cpuTag": "intel_i7",
    "gen": "8th",
    "ram": 16,
    "storage": 512,
    "display": "14\" FHD IPS Anti-Glare",
    "gpu": "Intel UHD Graphics 620",
    "gpuType": "integrated",
    "category": "Durable Workhorse",
    "badge": "Top Reliability",
    "badgeType": "b-corp",
    "price": 68000,
    "priceFormatted": "Rs 68,000",
    "priceUsd": 245,
    "img": "images/laptop-30-dell-latitude-7490-30.jpg",
    "condition": "Like New (10/10) \u00b7 Certified Refurbished",
    "warranty": "1 Year Local Warranty + 7 Days Checking",
    "useCases": [
      "office",
      "programming",
      "student"
    ],
    "ramGb": 16,
    "storageGb": 512,
    "storageType": "NVMe SSD",
    "cpuBrand": "Intel",
    "cpuTier": "Core i7",
    "cpuGen": 8,
    "gpuCategory": "integrated",
    "isDedicatedGpu": false,
    "gpuModel": "Intel UHD Graphics 620",
    "isRamUpgradable": true,
    "ramUpgradeOptions": [
      16,
      32
    ],
    "storageUpgradeOptions": [
      512,
      1000
    ],
    "legacyName": "Dell 7490 Core i7 8th",
    "shortSpecs": {
      "cpuFamily": "Core i7",
      "generation": "8th Gen",
      "ramGb": 16,
      "storageGb": 512,
      "storageType": "NVMe SSD",
      "gpuType": "integrated",
      "isDedicatedGpu": false
    },
    "fullSpecs": {
      "performance": {
        "processor": "Intel Core i7-8650U vPro Quad Core",
        "coresThreads": "4 Cores / 8 Threads",
        "clocks": "1.90 GHz Base, up to 4.20 GHz Boost",
        "cache": "8 MB Intel Smart Cache"
      },
      "memoryStorage": {
        "ramSize": "16 GB",
        "ramType": "DDR4",
        "ramSpeed": "2400 MHz",
        "ramSlots": "2x SO-DIMM Slots (Upgradable to 32GB)",
        "storageSize": "512 GB",
        "storageType": "NVMe SSD",
        "interface": "PCIe Gen3 x4 M.2 2280",
        "readSpeed": "Up to 3,000 MB/s"
      },
      "display": {
        "size": "14.0\"",
        "resolution": "FHD (1920 x 1080)",
        "panelType": "WVA IPS Anti-Glare",
        "refreshRate": "60 Hz",
        "touchAntiGlare": "Anti-Glare 300 nits (Non-touch)"
      },
      "graphics": {
        "gpuName": "Intel UHD Graphics 620",
        "type": "Integrated",
        "vram": "Shared System Memory"
      },
      "connectivityPorts": {
        "ports": "1x USB-C (DisplayPort/Thunderbolt 3), 3x USB 3.1 Gen 1 (1 PowerShare), 1x HDMI 1.4, RJ-45, MicroSD, Audio Jack",
        "wireless": "Intel Dual-Band Wireless-AC 8265 + Bluetooth 4.2"
      },
      "batteryBuild": {
        "battery": "60Wh ExpressCharge 4-Cell Battery",
        "weight": "1.40 kg (3.11 lbs) Carbon Fiber/Magnesium",
        "keyboard": "Backlit Spill-Resistant Keyboard with Dual Pointing",
        "webcam": "HD Camera with Privacy Shutter",
        "os": "Windows 11 Pro 64-bit Licensed"
      },
      "conditionWarranty": {
        "condition": "Grade A+ Like New \u00b7 High Durability Corporate",
        "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"
      }
    },
    "bgTone": "white",
    "bgColor": "rgb(255, 255, 255)",
    "tintColor": "rgba(76, 124, 255, 0.04)",
    "processedImg": "images/processed/laptop-30-cutout.webp",
    "stock": 3
  },
  {
    "id": 31,
    "name": "Dell Latitude 3310 2-in-1",
    "brand": "dell",
    "brandName": "Dell",
    "series": "Latitude 3310",
    "cpu": "Intel Core i5-10210U 10th Gen",
    "cpuTag": "intel_i5",
    "gen": "10th",
    "ram": 8,
    "storage": 256,
    "display": "13.3\" FHD Touch 360\u00b0 Rubberized",
    "gpu": "Intel UHD Graphics",
    "gpuType": "integrated",
    "category": "Rugged 2-in-1",
    "badge": "Drop Resistant",
    "badgeType": "b-val",
    "price": 62000,
    "priceFormatted": "Rs 62,000",
    "priceUsd": 220,
    "img": "images/laptop-31-dell-latitude-3310-2-in-1-31.jpg",
    "condition": "Like New (10/10) \u00b7 Certified Refurbished",
    "warranty": "1 Year Local Warranty + 7 Days Checking",
    "useCases": [
      "student",
      "office"
    ],
    "ramGb": 8,
    "storageGb": 256,
    "storageType": "NVMe SSD",
    "cpuBrand": "Intel",
    "cpuTier": "Core i5",
    "cpuGen": 10,
    "gpuCategory": "integrated",
    "isDedicatedGpu": false,
    "gpuModel": "Intel UHD Graphics",
    "isRamUpgradable": true,
    "ramUpgradeOptions": [
      8,
      16,
      32
    ],
    "storageUpgradeOptions": [
      256,
      512,
      1000
    ],
    "legacyName": "Dell 3310(2 in 1) Core i5 10th",
    "shortSpecs": {
      "cpuFamily": "Core i5",
      "generation": "10th Gen",
      "ramGb": 8,
      "storageGb": 256,
      "storageType": "NVMe SSD",
      "gpuType": "integrated",
      "isDedicatedGpu": false
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
        "ramSlots": "1x SO-DIMM Slot (Upgradable to 16GB)",
        "storageSize": "256 GB",
        "storageType": "NVMe SSD",
        "interface": "PCIe Gen3 x4 M.2 2280",
        "readSpeed": "Up to 2,200 MB/s"
      },
      "display": {
        "size": "13.3\"",
        "resolution": "FHD (1920 x 1080) 16:9",
        "panelType": "IPS Touchscreen 360\u00b0 Convertible",
        "refreshRate": "60 Hz",
        "touchAntiGlare": "Corning Gorilla Glass Touch with Active Stylus Support"
      },
      "graphics": {
        "gpuName": "Intel UHD Graphics",
        "type": "Integrated",
        "vram": "Shared System Memory"
      },
      "connectivityPorts": {
        "ports": "1x USB-C (DisplayPort/PD), 2x USB 3.1 Gen 1, 1x HDMI 1.4a, MicroSD Card Reader, Audio Jack",
        "wireless": "Intel Wi-Fi 6 AX201 + Bluetooth 5.1"
      },
      "batteryBuild": {
        "battery": "53Wh 4-Cell ExpressCharge",
        "weight": "1.56 kg (3.44 lbs) Ruggedized Rubberized Edges",
        "keyboard": "Sealed Spill-Resistant Keyboard",
        "webcam": "HD Webcam with Dual Digital Mics",
        "os": "Windows 11 Pro 64-bit Licensed"
      },
      "conditionWarranty": {
        "condition": "Grade A Like New \u00b7 Durable Student / Teacher 2-in-1",
        "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"
      }
    },
    "bgTone": "white",
    "bgColor": "rgb(255, 255, 255)",
    "tintColor": "rgba(76, 124, 255, 0.04)",
    "processedImg": "images/processed/laptop-31-cutout.webp",
    "stock": 3
  },
  {
    "id": 32,
    "name": "Dell Latitude E7270",
    "brand": "dell",
    "brandName": "Dell",
    "series": "Latitude E7270",
    "cpu": "Intel Core i5-6300U 6th Gen",
    "cpuTag": "intel_i5",
    "gen": "6th",
    "ram": 8,
    "storage": 256,
    "display": "12.5\" HD Anti-Glare Ultra-Portable",
    "gpu": "Intel HD Graphics 520",
    "gpuType": "integrated",
    "category": "Budget Portable",
    "badge": "Under 45k",
    "badgeType": "b-val",
    "price": 42000,
    "priceFormatted": "Rs 42,000",
    "priceUsd": 150,
    "img": "images/laptop-32-dell-latitude-e7270-32.jpg",
    "condition": "Like New (10/10) \u00b7 Certified Refurbished",
    "warranty": "1 Year Local Warranty + 7 Days Checking",
    "useCases": [
      "student",
      "office"
    ],
    "ramGb": 8,
    "storageGb": 256,
    "storageType": "NVMe SSD",
    "cpuBrand": "Intel",
    "cpuTier": "Core i5",
    "cpuGen": 6,
    "gpuCategory": "integrated",
    "isDedicatedGpu": false,
    "gpuModel": "Intel HD Graphics 520",
    "isRamUpgradable": true,
    "ramUpgradeOptions": [
      8,
      16,
      32
    ],
    "storageUpgradeOptions": [
      256,
      512,
      1000
    ],
    "legacyName": "Dell 7270 Core i5 6th",
    "shortSpecs": {
      "cpuFamily": "Core i5",
      "generation": "6th Gen",
      "ramGb": 8,
      "storageGb": 256,
      "storageType": "SATA SSD",
      "gpuType": "integrated",
      "isDedicatedGpu": false
    },
    "fullSpecs": {
      "performance": {
        "processor": "Intel Core i5-6300U vPro",
        "coresThreads": "2 Cores / 4 Threads",
        "clocks": "2.40 GHz Base, up to 3.00 GHz Boost",
        "cache": "3 MB Intel Smart Cache"
      },
      "memoryStorage": {
        "ramSize": "8 GB",
        "ramType": "DDR4",
        "ramSpeed": "2133 MHz",
        "ramSlots": "2x SO-DIMM Slots (Upgradable to 16GB)",
        "storageSize": "256 GB",
        "storageType": "SATA SSD",
        "interface": "M.2 SATA III SSD",
        "readSpeed": "Up to 540 MB/s"
      },
      "display": {
        "size": "12.5\"",
        "resolution": "FHD (1920 x 1080) / HD",
        "panelType": "Anti-Glare IPS Display",
        "refreshRate": "60 Hz",
        "touchAntiGlare": "Anti-Glare (Non-touch)"
      },
      "graphics": {
        "gpuName": "Intel HD Graphics 520",
        "type": "Integrated",
        "vram": "Shared System Memory"
      },
      "connectivityPorts": {
        "ports": "3x USB 3.0 (1 with PowerShare), 1x HDMI, 1x Mini DisplayPort, RJ-45 Ethernet, SD Card Reader, Audio Jack",
        "wireless": "Intel Dual-Band Wireless-AC 8260 + Bluetooth 4.2"
      },
      "batteryBuild": {
        "battery": "55Wh 4-Cell Lithium Polymer",
        "weight": "1.26 kg (2.77 lbs) Magnesium Alloy",
        "keyboard": "Backlit Spill-Resistant Keyboard",
        "webcam": "720p HD Webcam",
        "os": "Windows 10/11 Pro 64-bit Licensed"
      },
      "conditionWarranty": {
        "condition": "Clean Used (9/10) \u00b7 Ultra-Portable Compact",
        "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"
      }
    },
    "bgTone": "white",
    "bgColor": "rgb(255, 255, 255)",
    "tintColor": "rgba(76, 124, 255, 0.04)",
    "processedImg": "images/processed/laptop-32-cutout.webp",
    "stock": 3
  },
  {
    "id": 33,
    "name": "Dell Latitude 5320",
    "brand": "dell",
    "brandName": "Dell",
    "series": "Latitude 5320",
    "cpu": "Intel Core i5-1145G7 vPro 11th Gen",
    "cpuTag": "intel_i5",
    "gen": "11th",
    "ram": 16,
    "storage": 512,
    "display": "13.3\" FHD IPS 400 nits Anti-Glare",
    "gpu": "Intel Iris Xe Graphics",
    "gpuType": "integrated",
    "category": "Corporate Ultrabook",
    "badge": "High Demand",
    "badgeType": "b-corp",
    "price": 92000,
    "priceFormatted": "Rs 92,000",
    "priceUsd": 330,
    "img": "images/laptop-33-dell-latitude-5320-33.jpg",
    "condition": "Like New (10/10) \u00b7 Certified Refurbished",
    "warranty": "1 Year Local Warranty + 7 Days Checking",
    "useCases": [
      "office",
      "programming",
      "student"
    ],
    "ramGb": 16,
    "storageGb": 512,
    "storageType": "NVMe SSD",
    "cpuBrand": "Intel",
    "cpuTier": "Core i5",
    "cpuGen": 11,
    "gpuCategory": "integrated",
    "isDedicatedGpu": false,
    "gpuModel": "Intel Iris Xe Graphics",
    "isRamUpgradable": true,
    "ramUpgradeOptions": [
      16,
      32
    ],
    "storageUpgradeOptions": [
      512,
      1000
    ],
    "legacyName": "Dell Latitude 5320 Core i5 11th",
    "shortSpecs": {
      "cpuFamily": "Core i5",
      "generation": "11th Gen",
      "ramGb": 16,
      "storageGb": 512,
      "storageType": "NVMe SSD",
      "gpuType": "integrated",
      "isDedicatedGpu": false
    },
    "fullSpecs": {
      "performance": {
        "processor": "Intel Core i5-1145G7 vPro",
        "coresThreads": "4 Cores / 8 Threads",
        "clocks": "2.60 GHz Base, up to 4.40 GHz Turbo",
        "cache": "8 MB Intel Smart Cache"
      },
      "memoryStorage": {
        "ramSize": "16 GB",
        "ramType": "DDR4",
        "ramSpeed": "3200 MHz",
        "ramSlots": "Soldered Dual-Channel (Non-upgradable)",
        "storageSize": "512 GB",
        "storageType": "NVMe SSD",
        "interface": "PCIe Gen3 x4 M.2 2280",
        "readSpeed": "Up to 3,200 MB/s"
      },
      "display": {
        "size": "13.3\"",
        "resolution": "FHD (1920 x 1080)",
        "panelType": "IPS Anti-Glare",
        "refreshRate": "60 Hz",
        "touchAntiGlare": "Anti-Glare 300 nits ComfortView Plus"
      },
      "graphics": {
        "gpuName": "Intel Iris Xe Graphics",
        "type": "Integrated",
        "vram": "Shared System Memory"
      },
      "connectivityPorts": {
        "ports": "2x Thunderbolt 4 USB-C, 2x USB-A 3.2 Gen 1 (1 PowerShare), 1x HDMI 2.0, MicroSD, Audio Jack",
        "wireless": "Intel Wi-Fi 6 AX201 + Bluetooth 5.1"
      },
      "batteryBuild": {
        "battery": "63Wh ExpressCharge Capable",
        "weight": "1.20 kg (2.65 lbs)",
        "keyboard": "Backlit Spill-Resistant Keyboard",
        "webcam": "720p HD with Privacy Shutter",
        "os": "Windows 11 Pro 64-bit Licensed"
      },
      "conditionWarranty": {
        "condition": "Grade A+ Like New \u00b7 Certified Refurbished",
        "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"
      }
    },
    "bgTone": "white",
    "bgColor": "rgb(255, 255, 255)",
    "tintColor": "rgba(76, 124, 255, 0.04)",
    "processedImg": "images/processed/laptop-33-cutout.webp",
    "stock": 3
  },
  {
    "id": 34,
    "name": "Lenovo ThinkPad E14 Gen 1",
    "brand": "lenovo",
    "brandName": "Lenovo",
    "series": "ThinkPad E14",
    "cpu": "Intel Core i3-10110U 10th Gen",
    "cpuTag": "intel_i3",
    "gen": "10th",
    "ram": 8,
    "storage": 256,
    "display": "14\" FHD Anti-Glare",
    "gpu": "Intel UHD Graphics",
    "gpuType": "integrated",
    "category": "Budget ThinkPad",
    "badge": "Great Value",
    "badgeType": "b-val",
    "price": 62000,
    "priceFormatted": "Rs 62,000",
    "priceUsd": 220,
    "img": "images/laptop-34-lenovo-thinkpad-e14-gen-1-34.jpg",
    "condition": "Like New (10/10) \u00b7 Certified Refurbished",
    "warranty": "1 Year Local Warranty + 7 Days Checking",
    "useCases": [
      "student",
      "office"
    ],
    "ramGb": 8,
    "storageGb": 256,
    "storageType": "NVMe SSD",
    "cpuBrand": "Intel",
    "cpuTier": "Core i3",
    "cpuGen": 10,
    "gpuCategory": "integrated",
    "isDedicatedGpu": false,
    "gpuModel": "Intel UHD Graphics",
    "isRamUpgradable": true,
    "ramUpgradeOptions": [
      8,
      16,
      32
    ],
    "storageUpgradeOptions": [
      256,
      512,
      1000
    ],
    "legacyName": "Lenovo E14 Core i3 10th",
    "shortSpecs": {
      "cpuFamily": "Core i3",
      "generation": "10th Gen",
      "ramGb": 8,
      "storageGb": 256,
      "storageType": "NVMe SSD",
      "gpuType": "integrated",
      "isDedicatedGpu": false
    },
    "fullSpecs": {
      "performance": {
        "processor": "Intel Core i3-10110U",
        "coresThreads": "2 Cores / 4 Threads",
        "clocks": "2.10 GHz Base, up to 4.10 GHz Boost",
        "cache": "4 MB Intel Smart Cache"
      },
      "memoryStorage": {
        "ramSize": "8 GB",
        "ramType": "DDR4",
        "ramSpeed": "2666 MHz",
        "ramSlots": "1x SO-DIMM Slot (Upgradable to 16GB/32GB)",
        "storageSize": "256 GB",
        "storageType": "NVMe SSD",
        "interface": "PCIe Gen3 x4 M.2 2280",
        "readSpeed": "Up to 2,200 MB/s"
      },
      "display": {
        "size": "14.0\"",
        "resolution": "FHD (1920 x 1080)",
        "panelType": "IPS Anti-Glare",
        "refreshRate": "60 Hz",
        "touchAntiGlare": "Anti-Glare (Non-touch), 250 nits"
      },
      "graphics": {
        "gpuName": "Intel UHD Graphics",
        "type": "Integrated",
        "vram": "Shared System Memory"
      },
      "connectivityPorts": {
        "ports": "1x USB-C 3.1 Gen 1 (DisplayPort/PD), 2x USB 3.1 Gen 1, 1x USB 2.0, 1x HDMI 1.4b, RJ-45 Gigabit, Audio Jack",
        "wireless": "Intel Wi-Fi 6 AX201 + Bluetooth 5.0"
      },
      "batteryBuild": {
        "battery": "45Wh Rapid Charge Battery",
        "weight": "1.69 kg (3.73 lbs) Aluminum Top Cover",
        "keyboard": "ThinkPad Precision Keyboard with TrackPoint",
        "webcam": "720p HD with ThinkShutter Privacy Cover",
        "os": "Windows 11 Pro 64-bit Licensed"
      },
      "conditionWarranty": {
        "condition": "Grade A+ Like New \u00b7 Business Budget Favorite",
        "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"
      }
    },
    "bgTone": "white",
    "bgColor": "rgb(255, 255, 255)",
    "tintColor": "rgba(76, 124, 255, 0.04)",
    "processedImg": "images/processed/laptop-34-cutout.webp",
    "stock": 3
  },
  {
    "id": 35,
    "name": "HP EliteBook x360 1030 G3",
    "brand": "hp",
    "brandName": "HP",
    "series": "EliteBook x360 1030",
    "cpu": "Intel Core i5-8350U Quad Core",
    "cpuTag": "intel_i5",
    "gen": "8th",
    "ram": 16,
    "storage": 512,
    "display": "13.3\" FHD IPS Touch 360\u00b0 CNC Aluminum",
    "gpu": "Intel UHD Graphics 620",
    "gpuType": "integrated",
    "category": "Sleek 2-in-1",
    "badge": "B&O Audio",
    "badgeType": "b-val",
    "price": 75000,
    "priceFormatted": "Rs 75,000",
    "priceUsd": 270,
    "img": "images/laptop-35-hp-elitebook-x360-1030-g3-35.jpg",
    "condition": "Like New (10/10) \u00b7 Certified Refurbished",
    "warranty": "1 Year Local Warranty + 7 Days Checking",
    "useCases": [
      "office",
      "student",
      "creator"
    ],
    "ramGb": 16,
    "storageGb": 512,
    "storageType": "NVMe SSD",
    "cpuBrand": "Intel",
    "cpuTier": "Core i5",
    "cpuGen": 8,
    "gpuCategory": "integrated",
    "isDedicatedGpu": false,
    "gpuModel": "Intel UHD Graphics 620",
    "isRamUpgradable": true,
    "ramUpgradeOptions": [
      16,
      32
    ],
    "storageUpgradeOptions": [
      512,
      1000
    ],
    "legacyName": "HP EliteBook 1030G3 Core i5 8th",
    "shortSpecs": {
      "cpuFamily": "Core i5",
      "generation": "8th Gen",
      "ramGb": 16,
      "storageGb": 512,
      "storageType": "NVMe SSD",
      "gpuType": "integrated",
      "isDedicatedGpu": false
    },
    "fullSpecs": {
      "performance": {
        "processor": "Intel Core i5-8350U vPro Quad Core",
        "coresThreads": "4 Cores / 8 Threads",
        "clocks": "1.70 GHz Base, up to 3.60 GHz Boost",
        "cache": "6 MB Intel Smart Cache"
      },
      "memoryStorage": {
        "ramSize": "16 GB",
        "ramType": "LPDDR3",
        "ramSpeed": "2133 MHz",
        "ramSlots": "Soldered Dual-Channel (Non-upgradable)",
        "storageSize": "512 GB",
        "storageType": "NVMe SSD",
        "interface": "PCIe Gen3 x4 M.2 2280",
        "readSpeed": "Up to 3,000 MB/s"
      },
      "display": {
        "size": "13.3\"",
        "resolution": "FHD (1920 x 1080) BrightView",
        "panelType": "IPS Touchscreen 360\u00b0 Convertible",
        "refreshRate": "60 Hz",
        "touchAntiGlare": "Corning Gorilla Glass 4 Touch, 400 nits, Active Pen Support"
      },
      "graphics": {
        "gpuName": "Intel UHD Graphics 620",
        "type": "Integrated",
        "vram": "Shared System Memory"
      },
      "connectivityPorts": {
        "ports": "2x Thunderbolt 3 (USB-C), 1x USB 3.1 Gen 1 (charging), 1x HDMI 1.4, Headphone/mic combo",
        "wireless": "Intel Dual-Band Wireless-AC 8265 + Bluetooth 4.2"
      },
      "batteryBuild": {
        "battery": "56.2Wh HP Long Life Fast Charge (50% in 30 mins)",
        "weight": "1.25 kg (2.76 lbs) CNC Machined Aluminum",
        "keyboard": "HP Premium Collaboration Backlit Spill-Resistant Keyboard",
        "webcam": "FHD 1080p Camera with IR Facial Recognition Windows Hello",
        "os": "Windows 11 Pro 64-bit Licensed"
      },
      "conditionWarranty": {
        "condition": "Pristine Like New (10/10) \u00b7 CNC Aluminum 2-in-1",
        "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"
      }
    },
    "bgTone": "white",
    "bgColor": "rgb(255, 255, 255)",
    "tintColor": "rgba(76, 124, 255, 0.04)",
    "processedImg": "images/processed/laptop-35-cutout.webp",
    "stock": 3
  },
  {
    "id": 36,
    "name": "Dell Alienware m15 R7",
    "brand": "dell",
    "brandName": "Dell",
    "series": "Alienware m15 R7",
    "cpu": "AMD Ryzen 7 6800H (8-Core/16-Thread 4.7GHz)",
    "cpuTag": "amd",
    "gen": "Ryzen 6000",
    "ram": 16,
    "storage": 1000,
    "display": "15.6\" QHD 240Hz 2ms G-SYNC",
    "gpu": "NVIDIA GeForce RTX 3070 Ti 8GB (150W)",
    "gpuType": "rtx",
    "category": "Extreme Gaming",
    "badge": "RTX 3070 Ti",
    "badgeType": "b-game",
    "price": 340000,
    "priceFormatted": "Rs 340,000",
    "priceUsd": 1220,
    "img": "images/laptop-36-dell-alienware-m15-r7-36.jpg",
    "condition": "Open Box / Brand New Condition",
    "warranty": "1 Year Local Warranty + 7 Days Checking",
    "useCases": [
      "gaming",
      "creator",
      "programming"
    ],
    "ramGb": 16,
    "storageGb": 1000,
    "storageType": "NVMe SSD",
    "cpuBrand": "AMD",
    "cpuTier": "Ryzen 7",
    "cpuGen": 6000,
    "gpuCategory": "dedicated",
    "isDedicatedGpu": true,
    "gpuModel": "NVIDIA GeForce RTX 3070 Ti 8GB (150W)",
    "isRamUpgradable": true,
    "ramUpgradeOptions": [
      16,
      32
    ],
    "storageUpgradeOptions": [
      512,
      1000
    ],
    "legacyName": "Dell Alienware M15 R7 Ryzen 7 6800H",
    "shortSpecs": {
      "cpuFamily": "Ryzen 7",
      "generation": "6000 Series",
      "ramGb": 16,
      "storageGb": 1000,
      "storageType": "NVMe SSD",
      "gpuType": "rtx",
      "isDedicatedGpu": true
    },
    "fullSpecs": {
      "performance": {
        "processor": "AMD Ryzen 7 6800H",
        "coresThreads": "8 Cores / 16 Threads (45W Max Performance)",
        "clocks": "3.20 GHz Base, up to 4.70 GHz Max Boost",
        "cache": "16 MB L3 Cache"
      },
      "memoryStorage": {
        "ramSize": "16 GB",
        "ramType": "DDR5",
        "ramSpeed": "4800 MHz",
        "ramSlots": "2x SO-DIMM Slots (Upgradable to 64GB)",
        "storageSize": "1 TB",
        "storageType": "NVMe SSD",
        "interface": "Dual M.2 PCIe Gen4 x4 NVMe Slots",
        "readSpeed": "Up to 6,800 MB/s"
      },
      "display": {
        "size": "15.6\"",
        "resolution": "QHD (2560 x 1440) 240Hz 2ms",
        "panelType": "Fast IPS G-SYNC & Advanced Optimus",
        "refreshRate": "240 Hz",
        "touchAntiGlare": "Anti-Glare 400 nits, 99% DCI-P3, ComfortView Plus"
      },
      "graphics": {
        "gpuName": "NVIDIA GeForce RTX 3070 Ti",
        "type": "Dedicated",
        "vram": "8 GB GDDR6 Dedicated (150W TGP)"
      },
      "connectivityPorts": {
        "ports": "1x USB-C 3.2 Gen 2 (DisplayPort 1.4), 3x USB-A 3.2 Gen 1 (1 PowerShare), 1x HDMI 2.1, RJ-45 2.5Gbps Killer Ethernet, Headphone Jack",
        "wireless": "MediaTek Wi-Fi 6E RZ616 + Bluetooth 5.2"
      },
      "batteryBuild": {
        "battery": "86Wh 6-Cell Battery with 240W GaN Adapter",
        "weight": "2.42 kg (5.34 lbs) Cryo-tech Liquid Metal Cooled",
        "keyboard": "AlienFX Per-Key RGB Backlit Keyboard (1.8mm key travel)",
        "webcam": "720p HD with Dual-Array Digital Microphones and Windows Hello IR",
        "os": "Windows 11 Home/Pro 64-bit Licensed"
      },
      "conditionWarranty": {
        "condition": "Pristine Like New (10/10) \u00b7 Elite Esports Gaming Beast",
        "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"
      }
    },
    "bgTone": "white",
    "bgColor": "rgb(255, 255, 255)",
    "tintColor": "rgba(76, 124, 255, 0.04)",
    "processedImg": "images/processed/laptop-36-cutout.webp",
    "stock": 3
  },
  {
    "id": 37,
    "name": "HP 15-da Series",
    "brand": "hp",
    "brandName": "HP",
    "series": "HP 15 Laptop",
    "cpu": "Intel Core i5-8250U Quad Core",
    "cpuTag": "intel_i5",
    "gen": "8th",
    "ram": 8,
    "storage": 256,
    "display": "15.6\" FHD Display with Full NumPad",
    "gpu": "Intel UHD Graphics 620",
    "gpuType": "integrated",
    "category": "Everyday 15.6\"",
    "badge": "Full Numpad",
    "badgeType": "b-val",
    "price": 58000,
    "priceFormatted": "Rs 58,000",
    "priceUsd": 210,
    "img": "images/laptop-37-hp-hp-15-da-series-37.jpg",
    "condition": "Like New (10/10) \u00b7 Certified Refurbished",
    "warranty": "1 Year Local Warranty + 7 Days Checking",
    "useCases": [
      "office",
      "student"
    ],
    "ramGb": 8,
    "storageGb": 256,
    "storageType": "NVMe SSD",
    "cpuBrand": "Intel",
    "cpuTier": "Core i5",
    "cpuGen": 8,
    "gpuCategory": "integrated",
    "isDedicatedGpu": false,
    "gpuModel": "Intel UHD Graphics 620",
    "isRamUpgradable": true,
    "ramUpgradeOptions": [
      8,
      16,
      32
    ],
    "storageUpgradeOptions": [
      256,
      512,
      1000
    ],
    "legacyName": "HP Notebook 15 Core i5 8th",
    "shortSpecs": {
      "cpuFamily": "Core i5",
      "generation": "8th Gen",
      "ramGb": 8,
      "storageGb": 256,
      "storageType": "NVMe SSD",
      "gpuType": "integrated",
      "isDedicatedGpu": false
    },
    "fullSpecs": {
      "performance": {
        "processor": "Intel Core i5-8250U Quad Core",
        "coresThreads": "4 Cores / 8 Threads",
        "clocks": "1.60 GHz Base, up to 3.40 GHz Boost",
        "cache": "6 MB Intel Smart Cache"
      },
      "memoryStorage": {
        "ramSize": "8 GB",
        "ramType": "DDR4",
        "ramSpeed": "2400 MHz",
        "ramSlots": "2x SO-DIMM Slots (Upgradable to 16GB)",
        "storageSize": "256 GB",
        "storageType": "NVMe SSD",
        "interface": "M.2 PCIe NVMe SSD + 2.5\" Bay",
        "readSpeed": "Up to 2,000 MB/s (unverified)"
      },
      "display": {
        "size": "15.6\"",
        "resolution": "FHD (1920 x 1080)",
        "panelType": "SVA Anti-Glare WLED-backlit",
        "refreshRate": "60 Hz",
        "touchAntiGlare": "Anti-Glare (Non-touch)"
      },
      "graphics": {
        "gpuName": "Intel UHD Graphics 620",
        "type": "Integrated",
        "vram": "Shared System Memory"
      },
      "connectivityPorts": {
        "ports": "2x USB 3.1 Gen 1, 1x USB 2.0, 1x HDMI 1.4b, RJ-45 Ethernet, SD Card Reader, Headphone/Mic combo",
        "wireless": "Realtek 802.11b/g/n/ac + Bluetooth 4.2"
      },
      "batteryBuild": {
        "battery": "41Wh 3-Cell Li-ion Battery",
        "weight": "1.77 kg (3.91 lbs)",
        "keyboard": "Full-size Keyboard with Integrated Numeric Keypad",
        "webcam": "HP TrueVision HD Camera with Digital Mic",
        "os": "Windows 11 Home/Pro 64-bit Licensed"
      },
      "conditionWarranty": {
        "condition": "Grade A Used \u00b7 15.6\" Everyday Workhorse",
        "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"
      }
    },
    "bgTone": "white",
    "bgColor": "rgb(255, 255, 255)",
    "tintColor": "rgba(76, 124, 255, 0.04)",
    "processedImg": "images/processed/laptop-37-cutout.webp",
    "stock": 3
  },
  {
    "id": 38,
    "name": "HP Pavilion 15",
    "brand": "hp",
    "brandName": "HP",
    "series": "Pavilion 15",
    "cpu": "Intel Core i5-7200U 7th Gen",
    "cpuTag": "intel_i5",
    "gen": "7th",
    "ram": 8,
    "storage": 256,
    "display": "15.6\" FHD IPS B&O Play Audio",
    "gpu": "Intel HD Graphics 620",
    "gpuType": "integrated",
    "category": "Multimedia 15\"",
    "badge": "Affordable",
    "badgeType": "b-val",
    "price": 55000,
    "priceFormatted": "Rs 55,000",
    "priceUsd": 195,
    "img": "images/laptop-38-hp-pavilion-15-38.jpg",
    "condition": "Like New (10/10) \u00b7 Certified Refurbished",
    "warranty": "1 Year Local Warranty + 7 Days Checking",
    "useCases": [
      "student",
      "office"
    ],
    "ramGb": 8,
    "storageGb": 256,
    "storageType": "NVMe SSD",
    "cpuBrand": "Intel",
    "cpuTier": "Core i5",
    "cpuGen": 7,
    "gpuCategory": "integrated",
    "isDedicatedGpu": false,
    "gpuModel": "Intel HD Graphics 620",
    "isRamUpgradable": true,
    "ramUpgradeOptions": [
      8,
      16,
      32
    ],
    "storageUpgradeOptions": [
      256,
      512,
      1000
    ],
    "legacyName": "HP Pavilion Core i5 7th",
    "shortSpecs": {
      "cpuFamily": "Core i5",
      "generation": "7th Gen",
      "ramGb": 8,
      "storageGb": 256,
      "storageType": "SATA SSD",
      "gpuType": "integrated",
      "isDedicatedGpu": false
    },
    "fullSpecs": {
      "performance": {
        "processor": "Intel Core i5-7200U",
        "coresThreads": "2 Cores / 4 Threads",
        "clocks": "2.50 GHz Base, up to 3.10 GHz Boost",
        "cache": "3 MB Intel Smart Cache"
      },
      "memoryStorage": {
        "ramSize": "8 GB",
        "ramType": "DDR4",
        "ramSpeed": "2133 MHz",
        "ramSlots": "2x SO-DIMM Slots (Upgradable to 16GB)",
        "storageSize": "256 GB",
        "storageType": "SATA SSD",
        "interface": "2.5\" SATA III SSD / M.2",
        "readSpeed": "Up to 540 MB/s"
      },
      "display": {
        "size": "15.6\"",
        "resolution": "FHD (1920 x 1080)",
        "panelType": "IPS BrightView WLED-backlit",
        "refreshRate": "60 Hz",
        "touchAntiGlare": "BrightView Glass (Non-touch / Touch config unverified)"
      },
      "graphics": {
        "gpuName": "Intel HD Graphics 620",
        "type": "Integrated",
        "vram": "Shared System Memory"
      },
      "connectivityPorts": {
        "ports": "1x USB-C 3.1 Gen 1, 2x USB 3.1 Gen 1, 1x HDMI, RJ-45, SD Card Slot, Audio Jack",
        "wireless": "Intel 802.11b/g/n/ac + Bluetooth 4.2"
      },
      "batteryBuild": {
        "battery": "41Wh Li-Ion Fast Charge",
        "weight": "1.92 kg (4.23 lbs)",
        "keyboard": "Full-size Backlit Keyboard with NumPad",
        "webcam": "HP Wide Vision HD Camera with B&O Play Audio",
        "os": "Windows 10/11 Pro 64-bit Licensed"
      },
      "conditionWarranty": {
        "condition": "Clean Used (9/10) \u00b7 Home & Office 15.6\"",
        "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"
      }
    },
    "bgTone": "colorful",
    "bgColor": "rgb(92, 92, 92)",
    "tintColor": "rgba(92, 92, 92, 0.15)",
    "processedImg": "images/laptop-38-hp-pavilion-15-38.jpg",
    "stock": 3
  },
  {
    "id": 39,
    "name": "Lenovo Yoga 6 13",
    "brand": "lenovo",
    "brandName": "Lenovo",
    "series": "Yoga 6",
    "cpu": "AMD Ryzen 5 7530U / 7350 (6-Core/12-Thread)",
    "cpuTag": "amd",
    "gen": "Ryzen 7000",
    "ram": 16,
    "storage": 512,
    "display": "13.3\" WUXGA 16:10 Touch 360\u00b0 Denim Fabric",
    "gpu": "AMD Radeon Graphics",
    "gpuType": "integrated",
    "category": "Fabric Luxury 2-in-1",
    "badge": "Denim Cover",
    "badgeType": "b-val",
    "price": 135000,
    "priceFormatted": "Rs 135,000",
    "priceUsd": 485,
    "img": "images/laptop-39-lenovo-yoga-6-13-3-39.jpg",
    "condition": "Like New (10/10) \u00b7 Certified Refurbished",
    "warranty": "1 Year Local Warranty + 7 Days Checking",
    "useCases": [
      "creator",
      "office",
      "student"
    ],
    "ramGb": 16,
    "storageGb": 512,
    "storageType": "NVMe SSD",
    "cpuBrand": "AMD",
    "cpuTier": "Ryzen 5",
    "cpuGen": 7000,
    "gpuCategory": "integrated",
    "isDedicatedGpu": false,
    "gpuModel": "AMD Radeon Graphics",
    "isRamUpgradable": true,
    "ramUpgradeOptions": [
      16,
      32
    ],
    "storageUpgradeOptions": [
      512,
      1000
    ],
    "legacyName": "Lenovo YOGA 6 Ryzen 5 7350",
    "shortSpecs": {
      "cpuFamily": "Ryzen 5",
      "generation": "7000 Series",
      "ramGb": 16,
      "storageGb": 512,
      "storageType": "NVMe SSD",
      "gpuType": "integrated",
      "isDedicatedGpu": false
    },
    "fullSpecs": {
      "performance": {
        "processor": "AMD Ryzen 5 7530U",
        "coresThreads": "6 Cores / 12 Threads",
        "clocks": "2.00 GHz Base, up to 4.50 GHz Max Boost",
        "cache": "16 MB L3 Cache"
      },
      "memoryStorage": {
        "ramSize": "16 GB",
        "ramType": "LPDDR4x",
        "ramSpeed": "4266 MHz",
        "ramSlots": "Soldered Dual-Channel (Non-upgradable)",
        "storageSize": "512 GB",
        "storageType": "NVMe SSD",
        "interface": "PCIe Gen4 x4 NVMe M.2 2242",
        "readSpeed": "Up to 4,000 MB/s"
      },
      "display": {
        "size": "13.3\"",
        "resolution": "WUXGA (1920 x 1200) 16:10",
        "panelType": "IPS Touchscreen 360\u00b0 Convertible",
        "refreshRate": "60 Hz",
        "touchAntiGlare": "Glossy 100% sRGB Touch, 300 nits, Dolby Vision, Stylus Supported"
      },
      "graphics": {
        "gpuName": "AMD Radeon Graphics (Vega 7)",
        "type": "Integrated",
        "vram": "Shared System Memory"
      },
      "connectivityPorts": {
        "ports": "2x USB-C 3.2 Gen 1 (DisplayPort 1.4/PD 3.0), 2x USB-A 3.2 Gen 1, 1x HDMI 2.1, MicroSD, Audio Jack",
        "wireless": "Wi-Fi 6 (802.11ax 2x2) + Bluetooth 5.1"
      },
      "batteryBuild": {
        "battery": "59Wh Internal Battery (Up to 12.5 hrs)",
        "weight": "1.37 kg (3.02 lbs) Unique Dark Teal Fabric/Alloy",
        "keyboard": "Backlit Keyboard with Front-Facing Dolby Atmos Stereo Speakers",
        "webcam": "FHD 1080p with Privacy Shutter and IR Windows Hello",
        "os": "Windows 11 Pro 64-bit Licensed"
      },
      "conditionWarranty": {
        "condition": "Pristine Like New (10/10) \u00b7 Stylish Fabric Cover 2-in-1",
        "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"
      }
    },
    "bgTone": "white",
    "bgColor": "rgb(255, 255, 255)",
    "tintColor": "rgba(76, 124, 255, 0.04)",
    "processedImg": "images/processed/laptop-39-cutout.webp",
    "stock": 3
  },
  {
    "id": 40,
    "name": "HP ProBook 640 G7",
    "brand": "hp",
    "brandName": "HP",
    "series": "ProBook 640 G7",
    "cpu": "Intel Core i5-10210U 10th Gen",
    "cpuTag": "intel_i5",
    "gen": "10th",
    "ram": 16,
    "storage": 512,
    "display": "14\" FHD IPS Anti-Glare",
    "gpu": "Intel UHD Graphics",
    "gpuType": "integrated",
    "category": "Tough Enterprise",
    "badge": "Reliable",
    "badgeType": "b-corp",
    "price": 82000,
    "priceFormatted": "Rs 82,000",
    "priceUsd": 295,
    "img": "images/laptop-40-hp-probook-640-g7-40.jpg",
    "condition": "Like New (10/10) \u00b7 Certified Refurbished",
    "warranty": "1 Year Local Warranty + 7 Days Checking",
    "useCases": [
      "office",
      "student"
    ],
    "ramGb": 16,
    "storageGb": 512,
    "storageType": "NVMe SSD",
    "cpuBrand": "Intel",
    "cpuTier": "Core i5",
    "cpuGen": 10,
    "gpuCategory": "integrated",
    "isDedicatedGpu": false,
    "gpuModel": "Intel UHD Graphics",
    "isRamUpgradable": true,
    "ramUpgradeOptions": [
      16,
      32
    ],
    "storageUpgradeOptions": [
      512,
      1000
    ],
    "legacyName": "HP ProBook 640G7 Core i5 10th",
    "shortSpecs": {
      "cpuFamily": "Core i5",
      "generation": "10th Gen",
      "ramGb": 16,
      "storageGb": 512,
      "storageType": "NVMe SSD",
      "gpuType": "integrated",
      "isDedicatedGpu": false
    },
    "fullSpecs": {
      "performance": {
        "processor": "Intel Core i5-10210U",
        "coresThreads": "4 Cores / 8 Threads",
        "clocks": "1.60 GHz Base, up to 4.20 GHz Boost",
        "cache": "6 MB Intel Smart Cache"
      },
      "memoryStorage": {
        "ramSize": "16 GB",
        "ramType": "DDR4",
        "ramSpeed": "2666 MHz",
        "ramSlots": "2x SO-DIMM Slots (Upgradable to 32GB/64GB)",
        "storageSize": "512 GB",
        "storageType": "NVMe SSD",
        "interface": "PCIe Gen3 x4 M.2 2280",
        "readSpeed": "Up to 2,800 MB/s"
      },
      "display": {
        "size": "14.0\"",
        "resolution": "FHD (1920 x 1080)",
        "panelType": "IPS Anti-Glare",
        "refreshRate": "60 Hz",
        "touchAntiGlare": "Anti-Glare 250 nits (Non-touch)"
      },
      "graphics": {
        "gpuName": "Intel UHD Graphics",
        "type": "Integrated",
        "vram": "Shared System Memory"
      },
      "connectivityPorts": {
        "ports": "1x USB-C 3.1 Gen 1, 3x USB 3.1 Gen 1 (1 charging), 1x HDMI 1.4b, RJ-45 Ethernet, MicroSD, Audio Jack",
        "wireless": "Intel Wi-Fi 6 AX201 + Bluetooth 5.0"
      },
      "batteryBuild": {
        "battery": "45Wh HP Long Life 3-Cell",
        "weight": "1.60 kg (3.53 lbs)",
        "keyboard": "HP Premium Spill-Resistant Backlit Keyboard",
        "webcam": "720p HD Privacy Camera",
        "os": "Windows 11 Pro 64-bit Licensed"
      },
      "conditionWarranty": {
        "condition": "Grade A+ Like New \u00b7 Business Standard",
        "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"
      }
    },
    "bgTone": "white",
    "bgColor": "rgb(255, 255, 255)",
    "tintColor": "rgba(76, 124, 255, 0.04)",
    "processedImg": "images/processed/laptop-40-cutout.webp",
    "stock": 3
  },
  {
    "id": 41,
    "name": "Lenovo Yoga 7i Gen 7",
    "brand": "lenovo",
    "brandName": "Lenovo",
    "series": "Yoga 7i",
    "cpu": "Intel Core i7-1260P 12th Gen (12-Core)",
    "cpuTag": "intel_i7",
    "gen": "12th",
    "ram": 16,
    "storage": 1000,
    "display": "14\" 2.8K 90Hz OLED Touch 360\u00b0",
    "gpu": "Intel Iris Xe Graphics",
    "gpuType": "integrated",
    "category": "Luxury OLED 2-in-1",
    "badge": "2.8K OLED",
    "badgeType": "b-gen",
    "price": 195000,
    "priceFormatted": "Rs 195,000",
    "priceUsd": 700,
    "img": "images/laptop-41-lenovo-yoga-7i-gen-7-41.jpg",
    "condition": "Like New (10/10) \u00b7 Certified Refurbished",
    "warranty": "1 Year Local Warranty + 7 Days Checking",
    "useCases": [
      "creator",
      "office",
      "programming"
    ],
    "ramGb": 16,
    "storageGb": 1000,
    "storageType": "NVMe SSD",
    "cpuBrand": "Intel",
    "cpuTier": "Core i7",
    "cpuGen": 12,
    "gpuCategory": "integrated",
    "isDedicatedGpu": false,
    "gpuModel": "Intel Iris Xe Graphics",
    "isRamUpgradable": true,
    "ramUpgradeOptions": [
      16,
      32
    ],
    "storageUpgradeOptions": [
      512,
      1000
    ],
    "legacyName": "Lenovo YOGA Core i7 12th",
    "shortSpecs": {
      "cpuFamily": "Core i7",
      "generation": "12th Gen",
      "ramGb": 16,
      "storageGb": 1000,
      "storageType": "NVMe SSD",
      "gpuType": "integrated",
      "isDedicatedGpu": false
    },
    "fullSpecs": {
      "performance": {
        "processor": "Intel Core i7-1260P",
        "coresThreads": "12 Cores (4P + 8E) / 16 Threads",
        "clocks": "2.10 GHz Base, up to 4.70 GHz Turbo",
        "cache": "18 MB Intel Smart Cache"
      },
      "memoryStorage": {
        "ramSize": "16 GB",
        "ramType": "LPDDR5",
        "ramSpeed": "4800 MHz",
        "ramSlots": "Soldered Dual-Channel (Non-upgradable)",
        "storageSize": "1 TB",
        "storageType": "NVMe SSD",
        "interface": "PCIe Gen4 x4 NVMe M.2 2280",
        "readSpeed": "Up to 5,500 MB/s"
      },
      "display": {
        "size": "14.0\"",
        "resolution": "2.8K (2880 x 1800) 16:10 90Hz OLED",
        "panelType": "OLED PureSight Touch 360\u00b0",
        "refreshRate": "90 Hz",
        "touchAntiGlare": "100% DCI-P3 400 nits Glossy Touch with Dolby Vision"
      },
      "graphics": {
        "gpuName": "Intel Iris Xe Graphics",
        "type": "Integrated",
        "vram": "Shared System Memory"
      },
      "connectivityPorts": {
        "ports": "2x Thunderbolt 4 USB-C, 1x USB-A 3.2 Gen 1 (Always On), 1x HDMI 2.0, MicroSD Card Reader, Audio Jack",
        "wireless": "Wi-Fi 6E AX211 + Bluetooth 5.2"
      },
      "batteryBuild": {
        "battery": "71Wh Rapid Charge Express (Up to 15 hours)",
        "weight": "1.42 kg (3.13 lbs) Comfort Edge CNC Aluminum",
        "keyboard": "Backlit Keyboard with Front Quad Speakers Dolby Atmos",
        "webcam": "1080p FHD IR Camera with Privacy Shutter",
        "os": "Windows 11 Pro 64-bit Licensed"
      },
      "conditionWarranty": {
        "condition": "Pristine Like New (10/10) \u00b7 2.8K OLED Convertible",
        "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"
      }
    },
    "bgTone": "white",
    "bgColor": "rgb(255, 255, 255)",
    "tintColor": "rgba(76, 124, 255, 0.04)",
    "processedImg": "images/processed/laptop-41-cutout.webp",
    "stock": 3
  },
  {
    "id": 42,
    "name": "HP EliteBook 1040 G5",
    "brand": "hp",
    "brandName": "HP",
    "series": "EliteBook 1040",
    "cpu": "Intel Core i7-7600U 7th Gen",
    "cpuTag": "intel_i7",
    "gen": "7th",
    "ram": 16,
    "storage": 512,
    "display": "14\" FHD IPS Glass B&O Audio",
    "gpu": "Intel HD Graphics 620",
    "gpuType": "integrated",
    "category": "Executive Slim",
    "badge": "Premium Glass",
    "badgeType": "b-corp",
    "price": 68000,
    "priceFormatted": "Rs 68,000",
    "priceUsd": 245,
    "img": "images/laptop-42-hp-elitebook-1040-g5-42.jpg",
    "condition": "Like New (10/10) \u00b7 Certified Refurbished",
    "warranty": "1 Year Local Warranty + 7 Days Checking",
    "useCases": [
      "office",
      "student"
    ],
    "ramGb": 16,
    "storageGb": 512,
    "storageType": "NVMe SSD",
    "cpuBrand": "Intel",
    "cpuTier": "Core i7",
    "cpuGen": 7,
    "gpuCategory": "integrated",
    "isDedicatedGpu": false,
    "gpuModel": "Intel HD Graphics 620",
    "isRamUpgradable": true,
    "ramUpgradeOptions": [
      16,
      32
    ],
    "storageUpgradeOptions": [
      512,
      1000
    ],
    "legacyName": "HP EliteBook 1040G5 Core i7 7th",
    "shortSpecs": {
      "cpuFamily": "Core i7",
      "generation": "7th Gen",
      "ramGb": 16,
      "storageGb": 512,
      "storageType": "NVMe SSD",
      "gpuType": "integrated",
      "isDedicatedGpu": false
    },
    "fullSpecs": {
      "performance": {
        "processor": "Intel Core i7-7600U vPro",
        "coresThreads": "2 Cores / 4 Threads",
        "clocks": "2.80 GHz Base, up to 3.90 GHz Boost",
        "cache": "4 MB Intel Smart Cache"
      },
      "memoryStorage": {
        "ramSize": "16 GB",
        "ramType": "DDR4",
        "ramSpeed": "2133 MHz",
        "ramSlots": "Soldered Dual-Channel (Non-upgradable)",
        "storageSize": "512 GB",
        "storageType": "NVMe SSD",
        "interface": "PCIe Gen3 x4 M.2 2280",
        "readSpeed": "Up to 2,800 MB/s"
      },
      "display": {
        "size": "14.0\"",
        "resolution": "FHD (1920 x 1080)",
        "panelType": "IPS Anti-Glare Glass",
        "refreshRate": "60 Hz",
        "touchAntiGlare": "Anti-Glare 400 nits Ultra-Slim"
      },
      "graphics": {
        "gpuName": "Intel HD Graphics 620",
        "type": "Integrated",
        "vram": "Shared System Memory"
      },
      "connectivityPorts": {
        "ports": "2x Thunderbolt 3 (USB-C), 2x USB 3.1 Gen 1 (1 charging), 1x HDMI 1.4, Headphone/mic combo",
        "wireless": "Intel Dual Band Wireless-AC 8265 + Bluetooth 4.2"
      },
      "batteryBuild": {
        "battery": "67Wh 6-Cell Long Life Polymer",
        "weight": "1.35 kg (2.99 lbs) Precision CNC Unibody Aluminum",
        "keyboard": "HP Premium Collaboration Backlit Keyboard",
        "webcam": "720p HD with IR Facial Recognition Windows Hello & B&O Audio",
        "os": "Windows 11 Pro 64-bit Licensed"
      },
      "conditionWarranty": {
        "condition": "Grade A+ Like New \u00b7 Ultra-Slim CNC Flagship",
        "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"
      }
    },
    "bgTone": "white",
    "bgColor": "rgb(255, 255, 255)",
    "tintColor": "rgba(76, 124, 255, 0.04)",
    "processedImg": "images/processed/laptop-42-cutout.webp",
    "stock": 3
  },
  {
    "id": 43,
    "name": "Dell Latitude 5310",
    "brand": "dell",
    "brandName": "Dell",
    "series": "Latitude 5310",
    "cpu": "Intel Core i5-10310U vPro 10th Gen",
    "cpuTag": "intel_i5",
    "gen": "10th",
    "ram": 16,
    "storage": 256,
    "display": "13.3\" FHD IPS Anti-Glare",
    "gpu": "Intel UHD Graphics",
    "gpuType": "integrated",
    "category": "Compact Business",
    "badge": "vPro Secure",
    "badgeType": "b-corp",
    "price": 78000,
    "priceFormatted": "Rs 78,000",
    "priceUsd": 280,
    "img": "images/laptop-43-dell-latitude-5310-vpro-43.jpg",
    "condition": "Like New (10/10) \u00b7 Certified Refurbished",
    "warranty": "1 Year Local Warranty + 7 Days Checking",
    "useCases": [
      "office",
      "student"
    ],
    "ramGb": 16,
    "storageGb": 256,
    "storageType": "NVMe SSD",
    "cpuBrand": "Intel",
    "cpuTier": "Core i5",
    "cpuGen": 10,
    "gpuCategory": "integrated",
    "isDedicatedGpu": false,
    "gpuModel": "Intel UHD Graphics",
    "isRamUpgradable": true,
    "ramUpgradeOptions": [
      16,
      32
    ],
    "storageUpgradeOptions": [
      256,
      512,
      1000
    ],
    "legacyName": "Dell Latitude 5310 Core i5 10th",
    "shortSpecs": {
      "cpuFamily": "Core i5",
      "generation": "10th Gen",
      "ramGb": 16,
      "storageGb": 256,
      "storageType": "NVMe SSD",
      "gpuType": "integrated",
      "isDedicatedGpu": false
    },
    "fullSpecs": {
      "performance": {
        "processor": "Intel Core i5-10310U vPro",
        "coresThreads": "4 Cores / 8 Threads",
        "clocks": "1.70 GHz Base, up to 4.40 GHz Boost",
        "cache": "6 MB Intel Smart Cache"
      },
      "memoryStorage": {
        "ramSize": "16 GB",
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
        "ports": "1x USB-C 3.2 Gen 2 (DisplayPort/PD), 2x USB-A 3.2 Gen 1 (1 PowerShare), 1x HDMI 1.4b, RJ-45, MicroSD, Audio Jack",
        "wireless": "Intel Wi-Fi 6 AX201 + Bluetooth 5.1"
      },
      "batteryBuild": {
        "battery": "51Wh ExpressCharge Capable",
        "weight": "1.24 kg (2.73 lbs)",
        "keyboard": "Backlit Spill-Resistant Keyboard",
        "webcam": "HD Camera with Privacy Shutter",
        "os": "Windows 11 Pro 64-bit Licensed"
      },
      "conditionWarranty": {
        "condition": "Grade A+ Like New \u00b7 Certified Refurbished",
        "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"
      }
    },
    "bgTone": "white",
    "bgColor": "rgb(254, 254, 254)",
    "tintColor": "rgba(76, 124, 255, 0.04)",
    "processedImg": "images/processed/laptop-43-cutout.webp",
    "stock": 3
  },
  {
    "id": 44,
    "name": "HP ProBook 430 G8",
    "brand": "hp",
    "brandName": "HP",
    "series": "ProBook 430 G8",
    "cpu": "Intel Core i3-1115G4 11th Gen",
    "cpuTag": "intel_i3",
    "gen": "11th",
    "ram": 8,
    "storage": 256,
    "display": "13.3\" FHD IPS Ultra-Light",
    "gpu": "Intel UHD Graphics",
    "gpuType": "integrated",
    "category": "Ultra-Light Business",
    "badge": "1.28kg Light",
    "badgeType": "b-val",
    "price": 74000,
    "priceFormatted": "Rs 74,000",
    "priceUsd": 265,
    "img": "images/laptop-44-hp-probook-430-g8-44.jpg",
    "condition": "Like New (10/10) \u00b7 Certified Refurbished",
    "warranty": "1 Year Local Warranty + 7 Days Checking",
    "useCases": [
      "office",
      "student"
    ],
    "ramGb": 8,
    "storageGb": 256,
    "storageType": "NVMe SSD",
    "cpuBrand": "Intel",
    "cpuTier": "Core i3",
    "cpuGen": 11,
    "gpuCategory": "integrated",
    "isDedicatedGpu": false,
    "gpuModel": "Intel UHD Graphics",
    "isRamUpgradable": true,
    "ramUpgradeOptions": [
      8,
      16,
      32
    ],
    "storageUpgradeOptions": [
      256,
      512,
      1000
    ],
    "legacyName": "HP EliteBook 430G8 Core i3 11th",
    "shortSpecs": {
      "cpuFamily": "Core i3",
      "generation": "11th Gen",
      "ramGb": 8,
      "storageGb": 256,
      "storageType": "NVMe SSD",
      "gpuType": "integrated",
      "isDedicatedGpu": false
    },
    "fullSpecs": {
      "performance": {
        "processor": "Intel Core i3-1115G4",
        "coresThreads": "2 Cores / 4 Threads",
        "clocks": "3.00 GHz Base, up to 4.10 GHz Turbo",
        "cache": "6 MB Intel Smart Cache"
      },
      "memoryStorage": {
        "ramSize": "8 GB",
        "ramType": "DDR4",
        "ramSpeed": "3200 MHz",
        "ramSlots": "2x SO-DIMM Slots (Upgradable to 32GB)",
        "storageSize": "256 GB",
        "storageType": "NVMe SSD",
        "interface": "PCIe NVMe M.2 2280",
        "readSpeed": "Up to 2,200 MB/s"
      },
      "display": {
        "size": "13.3\"",
        "resolution": "FHD (1920 x 1080)",
        "panelType": "IPS Anti-Glare",
        "refreshRate": "60 Hz",
        "touchAntiGlare": "Anti-Glare 250 nits (Non-touch)"
      },
      "graphics": {
        "gpuName": "Intel UHD Graphics",
        "type": "Integrated",
        "vram": "Shared System Memory"
      },
      "connectivityPorts": {
        "ports": "1x USB-C 3.2 Gen 2 (Power Delivery, DisplayPort 1.4), 2x USB-A 3.2 Gen 1 (1 charging), 1x HDMI 1.4b, MicroSD, Audio Jack",
        "wireless": "Intel Wi-Fi 6 AX201 + Bluetooth 5.0"
      },
      "batteryBuild": {
        "battery": "45Wh HP Long Life Fast Charge (50% in 30 mins)",
        "weight": "1.28 kg (2.81 lbs) Lightweight Aluminum",
        "keyboard": "HP Spill-Resistant Keyboard",
        "webcam": "720p HD Privacy Camera",
        "os": "Windows 11 Pro 64-bit Licensed"
      },
      "conditionWarranty": {
        "condition": "Grade A+ Like New \u00b7 Compact Student / Office",
        "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"
      }
    },
    "bgTone": "white",
    "bgColor": "rgb(255, 255, 255)",
    "tintColor": "rgba(76, 124, 255, 0.04)",
    "processedImg": "images/processed/laptop-44-cutout.webp",
    "stock": 3
  },
  {
    "id": 45,
    "name": "Dell Latitude 7320",
    "brand": "dell",
    "brandName": "Dell",
    "series": "Latitude 7320",
    "cpu": "Intel Core i7-1185G7 vPro (up to 4.8GHz)",
    "cpuTag": "intel_i7",
    "gen": "11th",
    "ram": 16,
    "storage": 512,
    "display": "13.3\" FHD Super Low Power 400 nits",
    "gpu": "Intel Iris Xe Graphics",
    "gpuType": "integrated",
    "category": "Carbon Ultralight",
    "badge": "Top i7 11th",
    "badgeType": "b-corp",
    "price": 125000,
    "priceFormatted": "Rs 125,000",
    "priceUsd": 450,
    "img": "images/laptop-45-dell-latitude-7320-45.jpg",
    "condition": "Like New (10/10) \u00b7 Certified Refurbished",
    "warranty": "1 Year Local Warranty + 7 Days Checking",
    "useCases": [
      "office",
      "programming",
      "student"
    ],
    "ramGb": 16,
    "storageGb": 512,
    "storageType": "NVMe SSD",
    "cpuBrand": "Intel",
    "cpuTier": "Core i7",
    "cpuGen": 11,
    "gpuCategory": "integrated",
    "isDedicatedGpu": false,
    "gpuModel": "Intel Iris Xe Graphics",
    "isRamUpgradable": true,
    "ramUpgradeOptions": [
      16,
      32
    ],
    "storageUpgradeOptions": [
      512,
      1000
    ],
    "legacyName": "Dell Latitude 7320 Core i7 11th",
    "shortSpecs": {
      "cpuFamily": "Core i7",
      "generation": "11th Gen",
      "ramGb": 16,
      "storageGb": 512,
      "storageType": "NVMe SSD",
      "gpuType": "integrated",
      "isDedicatedGpu": false
    },
    "fullSpecs": {
      "performance": {
        "processor": "Intel Core i7-1185G7 vPro",
        "coresThreads": "4 Cores / 8 Threads",
        "clocks": "3.00 GHz Base, up to 4.80 GHz Turbo",
        "cache": "12 MB Intel Smart Cache"
      },
      "memoryStorage": {
        "ramSize": "16 GB",
        "ramType": "LPDDR4x",
        "ramSpeed": "4266 MHz",
        "ramSlots": "Soldered Dual-Channel (Non-upgradable)",
        "storageSize": "512 GB",
        "storageType": "NVMe SSD",
        "interface": "PCIe Gen3 x4 M.2 2280",
        "readSpeed": "Up to 3,500 MB/s"
      },
      "display": {
        "size": "13.3\"",
        "resolution": "FHD (1920 x 1080)",
        "panelType": "IPS Super Low Power Anti-Glare",
        "refreshRate": "60 Hz",
        "touchAntiGlare": "Anti-Glare 400 nits ComfortView Plus"
      },
      "graphics": {
        "gpuName": "Intel Iris Xe Graphics",
        "type": "Integrated",
        "vram": "Shared System Memory"
      },
      "connectivityPorts": {
        "ports": "2x Thunderbolt 4 USB-C, 1x USB-A 3.2 Gen 1 (PowerShare), 1x HDMI 2.0, MicroSD 4.0, Audio Jack",
        "wireless": "Intel Wi-Fi 6 AX201 + Bluetooth 5.1"
      },
      "batteryBuild": {
        "battery": "63Wh ExpressCharge 4-Cell",
        "weight": "1.12 kg (2.48 lbs) Carbon Fiber / Aluminum",
        "keyboard": "Backlit Spill-Resistant Keyboard",
        "webcam": "FHD IR Camera with Presence Detection & Privacy Shutter",
        "os": "Windows 11 Pro 64-bit Licensed"
      },
      "conditionWarranty": {
        "condition": "Pristine Like New (10/10) \u00b7 Ultra-Light Executive Flagship",
        "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"
      }
    },
    "bgTone": "white",
    "bgColor": "rgb(255, 255, 255)",
    "tintColor": "rgba(76, 124, 255, 0.04)",
    "processedImg": "images/processed/laptop-45-cutout.webp",
    "stock": 3
  },
  {
    "id": 46,
    "name": "HP EliteBook 845 G7",
    "brand": "hp",
    "brandName": "HP",
    "series": "EliteBook 845 G7",
    "cpu": "AMD Ryzen 7 PRO 4750U 8-Core/16-Thread",
    "cpuTag": "amd",
    "gen": "Ryzen 4000",
    "ram": 16,
    "storage": 512,
    "display": "14\" FHD IPS Anti-Glare B&O Sound",
    "gpu": "AMD Radeon Vega 7",
    "gpuType": "integrated",
    "category": "8-Core Value Beast",
    "badge": "Verified Stock",
    "badgeType": "b-corp",
    "price": 118000,
    "priceFormatted": "Rs 118,000",
    "priceUsd": 425,
    "img": "images/laptop-46-hp-elitebook-845-g7-46.jpg",
    "condition": "Like New (10/10) \u00b7 Certified Refurbished",
    "warranty": "1 Year Local Warranty + 7 Days Checking",
    "useCases": [
      "office",
      "programming",
      "student"
    ],
    "ramGb": 16,
    "storageGb": 512,
    "storageType": "NVMe SSD",
    "cpuBrand": "AMD",
    "cpuTier": "Ryzen 7",
    "cpuGen": 4000,
    "gpuCategory": "integrated",
    "isDedicatedGpu": false,
    "gpuModel": "AMD Radeon Vega 7",
    "isRamUpgradable": true,
    "ramUpgradeOptions": [
      16,
      32
    ],
    "storageUpgradeOptions": [
      512,
      1000
    ],
    "legacyName": "HP EliteBook 845G7 Ryzen 7 Pro",
    "shortSpecs": {
      "cpuFamily": "Ryzen 7",
      "generation": "4000 Series",
      "ramGb": 16,
      "storageGb": 512,
      "storageType": "NVMe SSD",
      "gpuType": "integrated",
      "isDedicatedGpu": false
    },
    "fullSpecs": {
      "performance": {
        "processor": "AMD Ryzen 7 PRO 4750U",
        "coresThreads": "8 Cores / 16 Threads",
        "clocks": "1.70 GHz Base, up to 4.10 GHz Boost",
        "cache": "8 MB L3 Cache"
      },
      "memoryStorage": {
        "ramSize": "16 GB",
        "ramType": "DDR4",
        "ramSpeed": "3200 MHz",
        "ramSlots": "2x SO-DIMM Slots (Upgradable to 64GB)",
        "storageSize": "512 GB",
        "storageType": "NVMe SSD",
        "interface": "PCIe Gen3 x4 NVMe M.2 2280",
        "readSpeed": "Up to 3,200 MB/s"
      },
      "display": {
        "size": "14.0\"",
        "resolution": "FHD (1920 x 1080)",
        "panelType": "IPS Anti-Glare",
        "refreshRate": "60 Hz",
        "touchAntiGlare": "Anti-Glare 250 nits / 400 nits Low Power"
      },
      "graphics": {
        "gpuName": "AMD Radeon Graphics Vega 7",
        "type": "Integrated",
        "vram": "Shared System Memory"
      },
      "connectivityPorts": {
        "ports": "2x USB-C 3.1 Gen 2 (DisplayPort/PD), 2x USB-A 3.1 Gen 1 (1 charging), 1x HDMI 2.0, Headphone/mic combo",
        "wireless": "Intel Wi-Fi 6 AX200 + Bluetooth 5.0"
      },
      "batteryBuild": {
        "battery": "53Wh HP Long Life Fast Charge",
        "weight": "1.33 kg (2.93 lbs) Aluminum Unibody",
        "keyboard": "HP Premium Spill-Resistant Backlit Keyboard",
        "webcam": "720p HD Camera with IR Face Recognition & Privacy Shutter",
        "os": "Windows 11 Pro 64-bit Licensed"
      },
      "conditionWarranty": {
        "condition": "Grade A+ Like New \u00b7 8-Core Powerhouse",
        "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"
      }
    },
    "bgTone": "colorful",
    "bgColor": "rgb(177, 173, 165)",
    "tintColor": "rgba(177, 173, 165, 0.15)",
    "processedImg": "images/laptop-46-hp-elitebook-845-g7-46.jpg",
    "stock": 3
  },
  {
    "id": 47,
    "name": "Apple MacBook Pro 14\" (2021)",
    "brand": "apple",
    "brandName": "Apple",
    "series": "MacBook Pro 14",
    "cpu": "Apple M1 Pro (8-Core CPU / 14-Core GPU)",
    "cpuTag": "apple",
    "gen": "M1 Pro",
    "ram": 16,
    "storage": 512,
    "display": "14.2\" Liquid Retina XDR 120Hz ProMotion",
    "gpu": "Apple 14-Core GPU",
    "gpuType": "apple_gpu",
    "category": "Pro Silicon Creator",
    "badge": "Liquid Retina",
    "badgeType": "b-apple",
    "price": 320000,
    "priceFormatted": "Rs 320,000",
    "priceUsd": 1150,
    "img": "images/laptop-47-apple-macbook-pro-14-2021-47.jpg",
    "condition": "Open Box / Brand New Condition",
    "warranty": "1 Year Local Warranty + 7 Days Checking",
    "useCases": [
      "creator",
      "programming",
      "office"
    ],
    "ramGb": 16,
    "storageGb": 512,
    "storageType": "NVMe SSD",
    "cpuBrand": "Apple",
    "cpuTier": "M1 Pro",
    "cpuGen": 1,
    "gpuCategory": "apple",
    "isDedicatedGpu": false,
    "gpuModel": "Apple 14-Core GPU",
    "isRamUpgradable": false,
    "ramUpgradeOptions": [
      16
    ],
    "storageUpgradeOptions": [
      512,
      1000
    ],
    "legacyName": "APPLE MACBOOK M1 PRO 2021",
    "shortSpecs": {
      "cpuFamily": "M1 Pro",
      "generation": "2021",
      "ramGb": 16,
      "storageGb": 512,
      "storageType": "NVMe SSD",
      "gpuType": "apple_gpu",
      "isDedicatedGpu": false
    },
    "fullSpecs": {
      "performance": {
        "processor": "Apple M1 Pro Chip (8-Core CPU)",
        "coresThreads": "6 Performance Cores + 2 Efficiency Cores (8 Cores Total)",
        "clocks": "Up to 3.22 GHz High-Efficiency Unified Architecture",
        "cache": "16-Core Neural Engine 200GB/s Memory Bandwidth"
      },
      "memoryStorage": {
        "ramSize": "16 GB",
        "ramType": "Unified Memory",
        "ramSpeed": "200 GB/s Bandwidth",
        "ramSlots": "Apple Unified Memory Architecture (Non-upgradable)",
        "storageSize": "512 GB",
        "storageType": "Apple High-Speed SSD",
        "interface": "Custom Integrated Apple Controller",
        "readSpeed": "Up to 7,400 MB/s"
      },
      "display": {
        "size": "14.2\"",
        "resolution": "Liquid Retina XDR (3024 x 1964) 120Hz",
        "panelType": "Mini-LED ProMotion Display",
        "refreshRate": "120 Hz ProMotion",
        "touchAntiGlare": "1,000 nits sustained, 1,600 nits peak, 1,000,000:1 contrast, True Tone"
      },
      "graphics": {
        "gpuName": "Apple 14-Core GPU",
        "type": "Apple Silicon Integrated GPU",
        "vram": "Shared Unified Memory (Up to 16GB)"
      },
      "connectivityPorts": {
        "ports": "3x Thunderbolt 4 (USB-C), 1x HDMI, SDXC Card Slot, MagSafe 3 Port, 3.5mm Headphone Jack with High-Impedance Support",
        "wireless": "Wi-Fi 6 (802.11ax) + Bluetooth 5.0"
      },
      "batteryBuild": {
        "battery": "70Wh Lithium-Polymer (Up to 17 hours Apple TV playback)",
        "weight": "1.60 kg (3.5 lbs) 100% Recycled Aluminum Unibody",
        "keyboard": "Magic Keyboard with Touch ID & Full-Height Function Row",
        "webcam": "1080p FaceTime HD Camera with Advanced Image Signal Processor",
        "os": "macOS Sequoia / Sonoma Official Licensed"
      },
      "conditionWarranty": {
        "condition": "Pristine Like New (10/10) \u00b7 100% Battery Health Grade",
        "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"
      }
    },
    "bgTone": "white",
    "bgColor": "rgb(255, 255, 255)",
    "tintColor": "rgba(76, 124, 255, 0.04)",
    "processedImg": "images/processed/laptop-47-cutout.webp",
    "stock": 3
  },
  {
    "id": 48,
    "name": "HP EliteBook Folio 1020 G1",
    "brand": "hp",
    "brandName": "HP",
    "series": "EliteBook Folio 1020",
    "cpu": "Intel Core M-5Y71 Fanless Ultra-Slim",
    "cpuTag": "intel_i5",
    "gen": "Fanless",
    "ram": 8,
    "storage": 256,
    "display": "12.5\" FHD IPS Aluminum Unibody",
    "gpu": "Intel HD Graphics 5300",
    "gpuType": "integrated",
    "category": "Razor Thin Fanless",
    "badge": "Featherweight",
    "badgeType": "b-val",
    "price": 46000,
    "priceFormatted": "Rs 46,000",
    "priceUsd": 165,
    "img": "images/laptop-48-hp-elitebook-folio-1040-48.jpg",
    "condition": "Like New (10/10) \u00b7 Certified Refurbished",
    "warranty": "1 Year Local Warranty + 7 Days Checking",
    "useCases": [
      "student",
      "office"
    ],
    "ramGb": 8,
    "storageGb": 256,
    "storageType": "NVMe SSD",
    "cpuBrand": "Intel",
    "cpuTier": "Core M",
    "cpuGen": 5,
    "gpuCategory": "integrated",
    "isDedicatedGpu": false,
    "gpuModel": "Intel HD Graphics 5300",
    "isRamUpgradable": false,
    "ramUpgradeOptions": [
      8
    ],
    "storageUpgradeOptions": [
      256,
      512,
      1000
    ],
    "legacyName": "HP 1040G1 FOLIO Series Core M5",
    "shortSpecs": {
      "cpuFamily": "Core M",
      "generation": "5th Gen",
      "ramGb": 8,
      "storageGb": 256,
      "storageType": "SATA SSD",
      "gpuType": "integrated",
      "isDedicatedGpu": false
    },
    "fullSpecs": {
      "performance": {
        "processor": "Intel Core M-5Y71 Fanless Processor",
        "coresThreads": "2 Cores / 4 Threads (4.5W Ultra-Low Power)",
        "clocks": "1.20 GHz Base, up to 2.90 GHz Boost",
        "cache": "4 MB Intel Smart Cache"
      },
      "memoryStorage": {
        "ramSize": "8 GB",
        "ramType": "LPDDR3",
        "ramSpeed": "1866 MHz",
        "ramSlots": "Soldered Dual-Channel (Non-upgradable)",
        "storageSize": "256 GB",
        "storageType": "SATA SSD",
        "interface": "M.2 2280 SATA III SSD",
        "readSpeed": "Up to 530 MB/s"
      },
      "display": {
        "size": "12.5\"",
        "resolution": "FHD (1920 x 1080)",
        "panelType": "IPS Ultra-Slim Anti-Glare",
        "refreshRate": "60 Hz",
        "touchAntiGlare": "Anti-Glare (Non-touch)"
      },
      "graphics": {
        "gpuName": "Intel HD Graphics 5300",
        "type": "Integrated",
        "vram": "Shared System Memory"
      },
      "connectivityPorts": {
        "ports": "2x USB 3.0 (charging), 1x HDMI, 1x Side Docking Connector, MicroSD, Audio Jack",
        "wireless": "Intel Dual Band Wireless-AC 7265 + Bluetooth 4.0"
      },
      "batteryBuild": {
        "battery": "36Wh 4-Cell Long Life Li-ion (Fanless Zero Noise)",
        "weight": "1.20 kg (2.68 lbs) CNC Magnesium-Lithium Alloy",
        "keyboard": "HP Spill-Resistant Backlit Keyboard with ForcePad",
        "webcam": "720p HD Webcam with Dual-Array Mics",
        "os": "Windows 10/11 Pro 64-bit Licensed"
      },
      "conditionWarranty": {
        "condition": "Grade A Used \u00b7 Ultra-Thin Fanless Silent",
        "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"
      }
    },
    "bgTone": "white",
    "bgColor": "rgb(255, 255, 255)",
    "tintColor": "rgba(76, 124, 255, 0.04)",
    "processedImg": "images/processed/laptop-48-cutout.webp",
    "stock": 3
  },
  {
    "id": 49,
    "name": "HP EliteBook 630 G10",
    "brand": "hp",
    "brandName": "HP",
    "series": "EliteBook 630 G10",
    "cpu": "Intel Core i5-1335U 13th Gen (10-Core)",
    "cpuTag": "intel_i5",
    "gen": "13th",
    "ram": 16,
    "storage": 512,
    "display": "13.3\" FHD IPS Anti-Glare Gen 4 NVMe",
    "gpu": "Intel Iris Xe Graphics",
    "gpuType": "integrated",
    "category": "13th Gen Executive",
    "badge": "Gen4 NVMe",
    "badgeType": "b-gen",
    "price": 175000,
    "priceFormatted": "Rs 175,000",
    "priceUsd": 625,
    "img": "images/laptop-49-hp-elitebook-630-g10-49.jpg",
    "condition": "Like New (10/10) \u00b7 Certified Refurbished",
    "warranty": "1 Year Local Warranty + 7 Days Checking",
    "useCases": [
      "office",
      "programming"
    ],
    "ramGb": 16,
    "storageGb": 512,
    "storageType": "NVMe SSD",
    "cpuBrand": "Intel",
    "cpuTier": "Core i5",
    "cpuGen": 13,
    "gpuCategory": "integrated",
    "isDedicatedGpu": false,
    "gpuModel": "Intel Iris Xe Graphics",
    "isRamUpgradable": true,
    "ramUpgradeOptions": [
      16,
      32
    ],
    "storageUpgradeOptions": [
      512,
      1000
    ],
    "legacyName": "HP EliteBook 630G10 Core i5 13th",
    "shortSpecs": {
      "cpuFamily": "Core i5",
      "generation": "13th Gen",
      "ramGb": 16,
      "storageGb": 512,
      "storageType": "NVMe SSD",
      "gpuType": "integrated",
      "isDedicatedGpu": false
    },
    "fullSpecs": {
      "performance": {
        "processor": "Intel Core i5-1335U",
        "coresThreads": "10 Cores (2P + 8E) / 12 Threads",
        "clocks": "1.30 GHz Base, up to 4.60 GHz Turbo",
        "cache": "12 MB Intel Smart Cache"
      },
      "memoryStorage": {
        "ramSize": "16 GB",
        "ramType": "DDR4",
        "ramSpeed": "3200 MHz",
        "ramSlots": "2x SO-DIMM Slots (Upgradable to 64GB)",
        "storageSize": "512 GB",
        "storageType": "NVMe SSD",
        "interface": "PCIe Gen4 x4 NVMe M.2 2280",
        "readSpeed": "Up to 4,500 MB/s"
      },
      "display": {
        "size": "13.3\"",
        "resolution": "FHD (1920 x 1080)",
        "panelType": "IPS Anti-Glare",
        "refreshRate": "60 Hz",
        "touchAntiGlare": "Anti-Glare 250 nits / 400 nits Low Power"
      },
      "graphics": {
        "gpuName": "Intel Iris Xe Graphics",
        "type": "Integrated",
        "vram": "Shared System Memory"
      },
      "connectivityPorts": {
        "ports": "1x Thunderbolt 4 with USB4 Type-C, 2x USB Type-A 3.2 Gen 1 (1 charging), 1x HDMI 2.1, Headphone/mic combo",
        "wireless": "Intel Wi-Fi 6E AX211 (2x2) + Bluetooth 5.3"
      },
      "batteryBuild": {
        "battery": "51.3Wh HP Long Life Fast Charge (50% in 30 mins)",
        "weight": "1.22 kg (2.69 lbs) Silver Aluminum",
        "keyboard": "HP Premium Spill-Resistant Backlit Keyboard",
        "webcam": "720p HD Privacy Camera with Temporal Noise Reduction",
        "os": "Windows 11 Pro 64-bit Licensed"
      },
      "conditionWarranty": {
        "condition": "Grade A+ Like New \u00b7 13th Gen Modern Business",
        "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"
      }
    },
    "bgTone": "white",
    "bgColor": "rgb(254, 254, 254)",
    "tintColor": "rgba(76, 124, 255, 0.04)",
    "processedImg": "images/processed/laptop-49-cutout.webp",
    "stock": 3
  },
  {
    "id": 50,
    "name": "Apple MacBook Pro 14\" (M4 Max)",
    "brand": "apple",
    "brandName": "Apple",
    "series": "MacBook Pro 14",
    "cpu": "Apple M4 Max (14-Core CPU / 32-Core GPU)",
    "cpuTag": "apple",
    "gen": "M4 Max",
    "ram": 36,
    "storage": 1000,
    "display": "14.2\" Liquid Retina XDR 1600 nits Nano",
    "gpu": "Apple 32-Core GPU with Ray Tracing",
    "gpuType": "apple_gpu",
    "category": "Ultimate Computing Beast",
    "badge": "Ultra Flagship",
    "badgeType": "b-apple",
    "price": 780000,
    "priceFormatted": "Rs 780,000",
    "priceUsd": 2800,
    "img": "images/laptop-50-apple-macbook-pro-14-m4-max-50.jpg",
    "condition": "Open Box / Brand New Condition",
    "warranty": "1 Year Local Warranty + 7 Days Checking",
    "useCases": [
      "creator",
      "programming",
      "gaming"
    ],
    "ramGb": 36,
    "storageGb": 1000,
    "storageType": "NVMe SSD",
    "cpuBrand": "Apple",
    "cpuTier": "M4 Max",
    "cpuGen": 4,
    "gpuCategory": "apple",
    "isDedicatedGpu": false,
    "gpuModel": "Apple 32-Core GPU with Ray Tracing",
    "isRamUpgradable": false,
    "ramUpgradeOptions": [
      36
    ],
    "storageUpgradeOptions": [
      512,
      1000
    ],
    "legacyName": "APPLE MACBOOK PRO 14\" M4 MAX",
    "shortSpecs": {
      "cpuFamily": "M4 Max",
      "generation": "2024",
      "ramGb": 36,
      "storageGb": 1000,
      "storageType": "NVMe SSD",
      "gpuType": "apple_gpu",
      "isDedicatedGpu": false
    },
    "fullSpecs": {
      "performance": {
        "processor": "Apple M4 Max Chip (14-Core CPU)",
        "coresThreads": "10 Performance Cores + 4 Efficiency Cores (14 Cores Total)",
        "clocks": "Next-Gen 3nm Architecture with Hardware-Accelerated Ray Tracing",
        "cache": "16-Core Neural Engine 410GB/s Memory Bandwidth"
      },
      "memoryStorage": {
        "ramSize": "36 GB",
        "ramType": "Unified Memory",
        "ramSpeed": "410 GB/s Ultra-High Bandwidth",
        "ramSlots": "Unified Memory Architecture (Non-upgradable)",
        "storageSize": "1 TB",
        "storageType": "Apple Gen5 Class SSD",
        "interface": "Custom Integrated High-Performance Controller",
        "readSpeed": "Up to 7,800 MB/s"
      },
      "display": {
        "size": "14.2\"",
        "resolution": "Liquid Retina XDR (3024 x 1964) 120Hz ProMotion",
        "panelType": "Mini-LED Quantum Dot Nano-Texture Option",
        "refreshRate": "120 Hz ProMotion",
        "touchAntiGlare": "1,000 nits SDR, 1,600 nits peak HDR, 1,000,000:1 contrast ratio"
      },
      "graphics": {
        "gpuName": "Apple 32-Core GPU",
        "type": "Apple Silicon Flagship GPU with Ray Tracing",
        "vram": "Shared Unified Memory (Up to 36GB)"
      },
      "connectivityPorts": {
        "ports": "3x Thunderbolt 5 (USB-C up to 120Gbps), 1x HDMI (up to 8K), SDXC Card Slot, MagSafe 3 Port, 3.5mm Headphone Jack",
        "wireless": "Wi-Fi 6E (802.11ax) + Bluetooth 5.3"
      },
      "batteryBuild": {
        "battery": "72.4Wh Lithium-Polymer (Up to 18 hours battery life)",
        "weight": "1.62 kg (3.57 lbs) Space Black Anodized Aluminum",
        "keyboard": "Magic Keyboard with Touch ID & Ambient Light Sensor",
        "webcam": "12MP Center Stage Camera with Desk View Support",
        "os": "macOS Sequoia Licensed"
      },
      "conditionWarranty": {
        "condition": "Pristine Open Box / Brand New Condition (10/10)",
        "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"
      }
    },
    "bgTone": "white",
    "bgColor": "rgb(255, 255, 255)",
    "tintColor": "rgba(76, 124, 255, 0.04)",
    "processedImg": "images/processed/laptop-50-cutout.webp",
    "stock": 3
  },
  {
    "id": 51,
    "name": "HP Envy x360 13",
    "brand": "hp",
    "brandName": "HP",
    "series": "Envy x360 13",
    "cpu": "Intel Core i7-8550U Quad Core",
    "cpuTag": "intel_i7",
    "gen": "8th",
    "ram": 16,
    "storage": 512,
    "display": "13.3\" FHD IPS Touch 360\u00b0 Convertible",
    "gpu": "Intel UHD Graphics 620",
    "gpuType": "integrated",
    "category": "Touch 360\u00b0",
    "badge": "Versatile",
    "badgeType": "b-val",
    "price": 85000,
    "priceFormatted": "Rs 85,000",
    "priceUsd": 305,
    "img": "images/laptop-51-hp-envy-x360-13-51.jpg",
    "condition": "Like New (10/10) \u00b7 Certified Refurbished",
    "warranty": "1 Year Local Warranty + 7 Days Checking",
    "useCases": [
      "office",
      "student",
      "creator"
    ],
    "ramGb": 16,
    "storageGb": 512,
    "storageType": "NVMe SSD",
    "cpuBrand": "Intel",
    "cpuTier": "Core i7",
    "cpuGen": 8,
    "gpuCategory": "integrated",
    "isDedicatedGpu": false,
    "gpuModel": "Intel UHD Graphics 620",
    "isRamUpgradable": true,
    "ramUpgradeOptions": [
      16,
      32
    ],
    "storageUpgradeOptions": [
      512,
      1000
    ],
    "legacyName": "HP X360 Core i7 8th",
    "shortSpecs": {
      "cpuFamily": "Core i7",
      "generation": "8th Gen",
      "ramGb": 16,
      "storageGb": 512,
      "storageType": "NVMe SSD",
      "gpuType": "integrated",
      "isDedicatedGpu": false
    },
    "fullSpecs": {
      "performance": {
        "processor": "Intel Core i7-8550U Quad Core",
        "coresThreads": "4 Cores / 8 Threads",
        "clocks": "1.80 GHz Base, up to 4.00 GHz Boost",
        "cache": "8 MB Intel Smart Cache"
      },
      "memoryStorage": {
        "ramSize": "16 GB",
        "ramType": "LPDDR3",
        "ramSpeed": "2133 MHz",
        "ramSlots": "Soldered Dual-Channel (Non-upgradable)",
        "storageSize": "512 GB",
        "storageType": "NVMe SSD",
        "interface": "PCIe Gen3 x4 M.2 2280",
        "readSpeed": "Up to 2,800 MB/s"
      },
      "display": {
        "size": "13.3\"",
        "resolution": "FHD (1920 x 1080) IPS",
        "panelType": "Corning Gorilla Glass Touch 360\u00b0",
        "refreshRate": "60 Hz",
        "touchAntiGlare": "BrightView Glass Touch with Active Stylus Support"
      },
      "graphics": {
        "gpuName": "Intel UHD Graphics 620",
        "type": "Integrated",
        "vram": "Shared System Memory"
      },
      "connectivityPorts": {
        "ports": "1x USB-C 3.1 Gen 1 (DisplayPort/PD), 2x USB 3.1 Gen 1 (1 HP Sleep and Charge), MicroSD, Audio Jack",
        "wireless": "Intel 802.11b/g/n/ac + Bluetooth 4.2"
      },
      "batteryBuild": {
        "battery": "53.2Wh HP Fast Charge (50% in 45 mins)",
        "weight": "1.30 kg (2.87 lbs) CNC Aluminum",
        "keyboard": "Full-size Island-style Backlit Keyboard",
        "webcam": "HP Wide Vision HD Camera with Bang & Olufsen Quad Speakers",
        "os": "Windows 11 Pro 64-bit Licensed"
      },
      "conditionWarranty": {
        "condition": "Grade A+ Like New \u00b7 Sleek All-Metal Convertible",
        "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"
      }
    },
    "bgTone": "white",
    "bgColor": "rgb(255, 255, 255)",
    "tintColor": "rgba(76, 124, 255, 0.04)",
    "processedImg": "images/processed/laptop-51-cutout.webp",
    "stock": 3
  },
  {
    "id": 52,
    "name": "HP Spectre x360 13",
    "brand": "hp",
    "brandName": "HP",
    "series": "Spectre x360 13",
    "cpu": "Intel Core i7-8565U Quad Core (up to 4.6GHz)",
    "cpuTag": "intel_i7",
    "gen": "8th",
    "ram": 16,
    "storage": 512,
    "display": "13.3\" 4K UHD OLED Touch 360\u00b0",
    "gpu": "Intel UHD Graphics 620",
    "gpuType": "integrated",
    "category": "Gem-Cut Luxury",
    "badge": "4K OLED Touch",
    "badgeType": "b-val",
    "price": 98000,
    "priceFormatted": "Rs 98,000",
    "priceUsd": 350,
    "img": "images/laptop-52-hp-spectre-x360-13-gem-cut-52.jpg",
    "condition": "Like New (10/10) \u00b7 Certified Refurbished",
    "warranty": "1 Year Local Warranty + 7 Days Checking",
    "useCases": [
      "creator",
      "office",
      "student"
    ],
    "ramGb": 16,
    "storageGb": 512,
    "storageType": "NVMe SSD",
    "cpuBrand": "Intel",
    "cpuTier": "Core i7",
    "cpuGen": 8,
    "gpuCategory": "integrated",
    "isDedicatedGpu": false,
    "gpuModel": "Intel UHD Graphics 620",
    "isRamUpgradable": true,
    "ramUpgradeOptions": [
      16,
      32
    ],
    "storageUpgradeOptions": [
      512,
      1000
    ],
    "legacyName": "HP Spectre X360 Core i7 8th",
    "shortSpecs": {
      "cpuFamily": "Core i7",
      "generation": "8th Gen",
      "ramGb": 16,
      "storageGb": 512,
      "storageType": "NVMe SSD",
      "gpuType": "integrated",
      "isDedicatedGpu": false
    },
    "fullSpecs": {
      "performance": {
        "processor": "Intel Core i7-8565U Quad Core (Whiskey Lake)",
        "coresThreads": "4 Cores / 8 Threads",
        "clocks": "1.80 GHz Base, up to 4.60 GHz Turbo Boost",
        "cache": "8 MB Intel Smart Cache"
      },
      "memoryStorage": {
        "ramSize": "16 GB",
        "ramType": "LPDDR3",
        "ramSpeed": "2133 MHz",
        "ramSlots": "Soldered Dual-Channel (Non-upgradable)",
        "storageSize": "512 GB",
        "storageType": "NVMe SSD",
        "interface": "PCIe Gen3 x4 M.2 2280",
        "readSpeed": "Up to 3,200 MB/s"
      },
      "display": {
        "size": "13.3\"",
        "resolution": "4K UHD (3840 x 2160) AMOLED / FHD IPS Touch",
        "panelType": "AMOLED / IPS BrightView Touchscreen 360\u00b0",
        "refreshRate": "60 Hz",
        "touchAntiGlare": "Corning Gorilla Glass NBT Touch with HP Tilt Pen Support"
      },
      "graphics": {
        "gpuName": "Intel UHD Graphics 620",
        "type": "Integrated",
        "vram": "Shared System Memory"
      },
      "connectivityPorts": {
        "ports": "2x Thunderbolt 3 (USB-C with Power Delivery), 1x USB-A 3.1 Gen 2 (HP Sleep and Charge), MicroSD, Headphone Jack",
        "wireless": "Intel Wireless-AC 9560 802.11ac + Bluetooth 5.0"
      },
      "batteryBuild": {
        "battery": "61Wh HP Long Life Fast Charge (50% in 30 mins)",
        "weight": "1.32 kg (2.91 lbs) Iconic Gem-Cut CNC Aluminum Chassis",
        "keyboard": "Edge-to-Edge Backlit Keyboard with Bang & Olufsen Quad Speakers",
        "webcam": "HP Wide Vision FHD IR Camera with Privacy Kill Switch",
        "os": "Windows 11 Pro 64-bit Licensed"
      },
      "conditionWarranty": {
        "condition": "Pristine Like New (10/10) \u00b7 Luxury Gem-Cut Masterpiece",
        "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"
      }
    },
    "bgTone": "white",
    "bgColor": "rgb(255, 255, 255)",
    "tintColor": "rgba(76, 124, 255, 0.04)",
    "processedImg": "images/processed/laptop-52-cutout.webp",
    "stock": 3
  },
  {
    "id": 53,
    "name": "Microsoft Surface Laptop Go",
    "brand": "microsoft",
    "brandName": "Microsoft",
    "series": "Surface Laptop Go",
    "cpu": "Intel Core i5-1035G1 10th Gen",
    "cpuTag": "intel_i5",
    "gen": "10th",
    "ram": 8,
    "storage": 256,
    "display": "12.4\" PixelSense Touch (3:2) 1.1kg",
    "gpu": "Intel UHD Graphics",
    "gpuType": "integrated",
    "category": "Featherweight Touch",
    "badge": "1.1kg Light",
    "badgeType": "b-val",
    "price": 82000,
    "priceFormatted": "Rs 82,000",
    "priceUsd": 295,
    "img": "images/laptop-53-microsoft-surface-laptop-go-1943-53.jpg",
    "condition": "Like New (10/10) \u00b7 Certified Refurbished",
    "warranty": "1 Year Local Warranty + 7 Days Checking",
    "useCases": [
      "student",
      "office"
    ],
    "ramGb": 8,
    "storageGb": 256,
    "storageType": "NVMe SSD",
    "cpuBrand": "Intel",
    "cpuTier": "Core i5",
    "cpuGen": 10,
    "gpuCategory": "integrated",
    "isDedicatedGpu": false,
    "gpuModel": "Intel UHD Graphics",
    "isRamUpgradable": false,
    "ramUpgradeOptions": [
      8
    ],
    "storageUpgradeOptions": [
      256,
      512,
      1000
    ],
    "legacyName": "Microsoft Surface Laptop GO 1943 Core i5 10th",
    "shortSpecs": {
      "cpuFamily": "Core i5",
      "generation": "10th Gen",
      "ramGb": 8,
      "storageGb": 256,
      "storageType": "NVMe SSD",
      "gpuType": "integrated",
      "isDedicatedGpu": false
    },
    "fullSpecs": {
      "performance": {
        "processor": "Intel Core i5-1035G1",
        "coresThreads": "4 Cores / 8 Threads",
        "clocks": "1.00 GHz Base, up to 3.60 GHz Boost",
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
        "readSpeed": "Up to 2,000 MB/s"
      },
      "display": {
        "size": "12.4\"",
        "resolution": "1.5K (1536 x 1024) 3:2 Aspect Ratio",
        "panelType": "PixelSense 10-Point Multi-Touch",
        "refreshRate": "60 Hz",
        "touchAntiGlare": "Corning Gorilla Glass Touch, 300 nits"
      },
      "graphics": {
        "gpuName": "Intel UHD Graphics",
        "type": "Integrated",
        "vram": "Shared System Memory"
      },
      "connectivityPorts": {
        "ports": "1x USB-C 3.1, 1x USB-A 3.1, 3.5mm Headphone Jack, Surface Connect Port",
        "wireless": "Wi-Fi 6 (802.11ax) + Bluetooth 5.0"
      },
      "batteryBuild": {
        "battery": "40Wh Fast Charging (80% in about 1 hour)",
        "weight": "1.11 kg (2.45 lbs) Ultra-Lightweight Aluminum/Resin",
        "keyboard": "Precision Keyboard with Fingerprint Power Button Windows Hello",
        "webcam": "720p HD f/2.0 Camera with Omnisonic Speakers & Dolby Audio",
        "os": "Windows 11 Pro 64-bit Licensed"
      },
      "conditionWarranty": {
        "condition": "Pristine Like New (10/10) \u00b7 Featherlight Grab-and-Go",
        "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"
      }
    },
    "bgTone": "white",
    "bgColor": "rgb(254, 254, 254)",
    "tintColor": "rgba(76, 124, 255, 0.04)",
    "processedImg": "images/processed/laptop-53-cutout.webp",
    "stock": 3
  },
  {
    "id": 54,
    "name": "Lenovo Yoga Slim 7 14",
    "brand": "lenovo",
    "brandName": "Lenovo",
    "series": "Yoga Slim 7",
    "cpu": "Intel Core i7-1065G7 10th Gen (Iris Plus G7)",
    "cpuTag": "intel_i7",
    "gen": "10th",
    "ram": 16,
    "storage": 512,
    "display": "14\" FHD IPS 100% sRGB 300 nits",
    "gpu": "Intel Iris Plus Graphics",
    "gpuType": "integrated",
    "category": "All-Metal Slim",
    "badge": "100% sRGB",
    "badgeType": "b-corp",
    "price": 125000,
    "priceFormatted": "Rs 125,000",
    "priceUsd": 450,
    "img": "images/laptop-54-lenovo-yoga-slim-7-14-54.jpg",
    "condition": "Like New (10/10) \u00b7 Certified Refurbished",
    "warranty": "1 Year Local Warranty + 7 Days Checking",
    "useCases": [
      "creator",
      "office",
      "student"
    ],
    "ramGb": 16,
    "storageGb": 512,
    "storageType": "NVMe SSD",
    "cpuBrand": "Intel",
    "cpuTier": "Core i7",
    "cpuGen": 10,
    "gpuCategory": "integrated",
    "isDedicatedGpu": false,
    "gpuModel": "Intel Iris Plus Graphics",
    "isRamUpgradable": false,
    "ramUpgradeOptions": [
      16
    ],
    "storageUpgradeOptions": [
      512,
      1000
    ],
    "legacyName": "Lenovo YOGA Slim 7 Core i7 10th",
    "shortSpecs": {
      "cpuFamily": "Core i7",
      "generation": "10th Gen",
      "ramGb": 16,
      "storageGb": 512,
      "storageType": "NVMe SSD",
      "gpuType": "integrated",
      "isDedicatedGpu": false
    },
    "fullSpecs": {
      "performance": {
        "processor": "Intel Core i7-1065G7 (Iris Plus G7)",
        "coresThreads": "4 Cores / 8 Threads",
        "clocks": "1.30 GHz Base, up to 3.90 GHz Boost",
        "cache": "8 MB Intel Smart Cache"
      },
      "memoryStorage": {
        "ramSize": "16 GB",
        "ramType": "LPDDR4x",
        "ramSpeed": "3200 MHz",
        "ramSlots": "Soldered Dual-Channel (Non-upgradable)",
        "storageSize": "512 GB",
        "storageType": "NVMe SSD",
        "interface": "PCIe Gen3 x4 M.2 2280",
        "readSpeed": "Up to 3,200 MB/s"
      },
      "display": {
        "size": "14.0\"",
        "resolution": "FHD (1920 x 1080) 100% sRGB",
        "panelType": "IPS Anti-Glare 300 nits",
        "refreshRate": "60 Hz",
        "touchAntiGlare": "Anti-Glare (Non-touch) / Dolby Vision"
      },
      "graphics": {
        "gpuName": "Intel Iris Plus Graphics",
        "type": "Integrated",
        "vram": "Shared System Memory"
      },
      "connectivityPorts": {
        "ports": "1x USB-C (Thunderbolt 3/PD/DisplayPort), 1x USB-C (Power Delivery), 2x USB-A 3.2 Gen 1, 1x HDMI 2.0b, MicroSD, Audio Jack",
        "wireless": "Wi-Fi 6 (802.11ax) + Bluetooth 5.0"
      },
      "batteryBuild": {
        "battery": "60.7Wh Rapid Charge Pro (Up to 14 hours)",
        "weight": "1.36 kg (2.99 lbs) Slim Slate Grey All-Metal",
        "keyboard": "Backlit Keyboard with Front-Facing Dolby Atmos Speakers",
        "webcam": "IR Camera with Time-of-Flight Presence Sensor & Windows Hello",
        "os": "Windows 11 Pro 64-bit Licensed"
      },
      "conditionWarranty": {
        "condition": "Grade A+ Like New \u00b7 Premium Ultra-Slim",
        "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"
      }
    },
    "bgTone": "white",
    "bgColor": "rgb(247, 247, 247)",
    "tintColor": "rgba(76, 124, 255, 0.04)",
    "processedImg": "images/processed/laptop-54-cutout.webp",
    "stock": 3
  },
  {
    "id": 55,
    "name": "HP Spectre x360 14 (2024)",
    "brand": "hp",
    "brandName": "HP",
    "series": "Spectre x360 14",
    "cpu": "Intel Core Ultra 7 155H (16-Core/22-Thread AI NPU)",
    "cpuTag": "intel_ultra",
    "gen": "Core Ultra",
    "ram": 16,
    "storage": 1000,
    "display": "14\" 2.8K 120Hz OLED Touch 360\u00b0",
    "gpu": "Intel Arc Graphics (Built-in)",
    "gpuType": "integrated",
    "category": "Next-Gen AI Flagship",
    "badge": "Intel Ultra 7",
    "badgeType": "b-gen",
    "price": 395000,
    "priceFormatted": "Rs 395,000",
    "priceUsd": 1420,
    "img": "images/laptop-55-hp-spectre-x360-14-ai-pc-55.jpg",
    "condition": "Open Box / Brand New Condition",
    "warranty": "1 Year Local Warranty + 7 Days Checking",
    "useCases": [
      "creator",
      "programming",
      "office"
    ],
    "ramGb": 16,
    "storageGb": 1000,
    "storageType": "NVMe SSD",
    "cpuBrand": "Intel",
    "cpuTier": "Core Ultra 7",
    "cpuGen": 14,
    "gpuCategory": "integrated",
    "isDedicatedGpu": false,
    "gpuModel": "Intel Arc Graphics (Built-in)",
    "isRamUpgradable": true,
    "ramUpgradeOptions": [
      16,
      32
    ],
    "storageUpgradeOptions": [
      512,
      1000
    ],
    "legacyName": "HP Spectre X360 Core ULTRA 7",
    "shortSpecs": {
      "cpuFamily": "Core Ultra 7",
      "generation": "Series 1 (AI PC)",
      "ramGb": 16,
      "storageGb": 1000,
      "storageType": "NVMe SSD",
      "gpuType": "integrated",
      "isDedicatedGpu": false
    },
    "fullSpecs": {
      "performance": {
        "processor": "Intel Core Ultra 7 155H (Meteor Lake AI PC)",
        "coresThreads": "16 Cores (6P + 8E + 2 Low-Power E) / 22 Threads",
        "clocks": "Up to 4.80 GHz Boost with Dedicated Intel AI Boost NPU",
        "cache": "24 MB Intel Smart Cache"
      },
      "memoryStorage": {
        "ramSize": "16 GB",
        "ramType": "LPDDR5x",
        "ramSpeed": "7467 MHz",
        "ramSlots": "Soldered Ultra-Fast (Non-upgradable)",
        "storageSize": "1 TB",
        "storageType": "NVMe SSD",
        "interface": "PCIe Gen4 x4 NVMe M.2 2280",
        "readSpeed": "Up to 6,800 MB/s"
      },
      "display": {
        "size": "14.0\"",
        "resolution": "2.8K (2880 x 1800) 120Hz OLED 16:10",
        "panelType": "OLED Touchscreen 360\u00b0 Convertible (0.2ms)",
        "refreshRate": "120 Hz Variable (48-120Hz)",
        "touchAntiGlare": "Corning Gorilla Glass Touch with Active Rechargeable Tilt Pen, 500 nits HDR, 100% DCI-P3"
      },
      "graphics": {
        "gpuName": "Intel Arc Graphics (Built-in)",
        "type": "Integrated Arc Architecture",
        "vram": "Shared System Memory"
      },
      "connectivityPorts": {
        "ports": "2x Thunderbolt 4 USB-C (Power Delivery, DisplayPort 2.1), 1x USB-A 10Gbps (HP Sleep and Charge), Headphone/mic combo",
        "wireless": "Intel Wi-Fi 7 BE200 + Bluetooth 5.4"
      },
      "batteryBuild": {
        "battery": "68Wh HP Fast Charge (50% in 45 mins, up to 13 hrs)",
        "weight": "1.44 kg (3.19 lbs) CNC Nightfall Black / Slate Blue",
        "keyboard": "Backlit Keyboard with Poly Studio Quad Speakers",
        "webcam": "9MP AI IR Camera with Auto Frame & Hardware Shutter",
        "os": "Windows 11 Pro 64-bit Licensed"
      },
      "conditionWarranty": {
        "condition": "Pristine Like New (10/10) \u00b7 Latest AI PC Flagship",
        "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"
      }
    },
    "bgTone": "dark",
    "bgColor": "rgb(0, 0, 0)",
    "tintColor": "rgba(45, 45, 60, 0.06)",
    "processedImg": "images/laptop-55-hp-spectre-x360-14-ai-pc-55.jpg",
    "stock": 3
  },
  {
    "id": 56,
    "name": "Dell XPS 13 9310",
    "brand": "dell",
    "brandName": "Dell",
    "series": "XPS 13",
    "cpu": "Intel Core i5-1135G7 11th Gen",
    "cpuTag": "intel_i5",
    "gen": "11th",
    "ram": 16,
    "storage": 512,
    "display": "13.4\" FHD+ 16:10 (1920x1200) 500 nits",
    "gpu": "Intel Iris Xe Graphics",
    "gpuType": "integrated",
    "category": "CNC Aluminum Icon",
    "badge": "500 nits 16:10",
    "badgeType": "b-corp",
    "price": 155000,
    "priceFormatted": "Rs 155,000",
    "priceUsd": 555,
    "img": "images/laptop-56-dell-xps-13-9310-56.jpg",
    "condition": "Like New (10/10) \u00b7 Certified Refurbished",
    "warranty": "1 Year Local Warranty + 7 Days Checking",
    "useCases": [
      "office",
      "programming",
      "creator"
    ],
    "ramGb": 16,
    "storageGb": 512,
    "storageType": "NVMe SSD",
    "cpuBrand": "Intel",
    "cpuTier": "Core i5",
    "cpuGen": 11,
    "gpuCategory": "integrated",
    "isDedicatedGpu": false,
    "gpuModel": "Intel Iris Xe Graphics",
    "isRamUpgradable": false,
    "ramUpgradeOptions": [
      16
    ],
    "storageUpgradeOptions": [
      512,
      1000
    ],
    "legacyName": "Dell XPS 13 9310 Core i5 11th",
    "shortSpecs": {
      "cpuFamily": "Core i5",
      "generation": "11th Gen",
      "ramGb": 16,
      "storageGb": 512,
      "storageType": "NVMe SSD",
      "gpuType": "integrated",
      "isDedicatedGpu": false
    },
    "fullSpecs": {
      "performance": {
        "processor": "Intel Core i5-1135G7",
        "coresThreads": "4 Cores / 8 Threads",
        "clocks": "2.40 GHz Base, up to 4.20 GHz Turbo",
        "cache": "8 MB Intel Smart Cache"
      },
      "memoryStorage": {
        "ramSize": "16 GB",
        "ramType": "LPDDR4x",
        "ramSpeed": "4267 MHz",
        "ramSlots": "Soldered Dual-Channel (Non-upgradable)",
        "storageSize": "512 GB",
        "storageType": "NVMe SSD",
        "interface": "PCIe Gen3 x4 M.2 2280",
        "readSpeed": "Up to 3,400 MB/s"
      },
      "display": {
        "size": "13.4\"",
        "resolution": "FHD+ (1920 x 1200) 16:10",
        "panelType": "InfinityEdge IPS Anti-Glare",
        "refreshRate": "60 Hz",
        "touchAntiGlare": "Anti-Glare 500 nits 100% sRGB (Non-touch)"
      },
      "graphics": {
        "gpuName": "Intel Iris Xe Graphics",
        "type": "Integrated",
        "vram": "Shared System Memory"
      },
      "connectivityPorts": {
        "ports": "2x Thunderbolt 4 USB-C (Power Delivery and DisplayPort), MicroSD Card Reader, 3.5mm Headphone Jack",
        "wireless": "Killer Wi-Fi 6 AX1650 (2x2) + Bluetooth 5.1"
      },
      "batteryBuild": {
        "battery": "52Wh Integrated Lithium-Ion",
        "weight": "1.20 kg (2.64 lbs) CNC Platinum Silver & Carbon Fiber",
        "keyboard": "Edge-to-Edge Backlit Keyboard with Glass Precision Touchpad",
        "webcam": "HD (720p) 2.25mm Camera with Windows Hello IR Facial Recognition",
        "os": "Windows 11 Pro 64-bit Licensed"
      },
      "conditionWarranty": {
        "condition": "Pristine Like New (10/10) \u00b7 Ultra-Compact Bezel-less",
        "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"
      }
    },
    "bgTone": "white",
    "bgColor": "rgb(255, 255, 255)",
    "tintColor": "rgba(76, 124, 255, 0.04)",
    "processedImg": "images/processed/laptop-56-cutout.webp",
    "stock": 3
  },
  {
    "id": 57,
    "name": "Lenovo ThinkPad L13 Gen 2",
    "brand": "lenovo",
    "brandName": "Lenovo",
    "series": "ThinkPad L13",
    "cpu": "Intel Core i5-1135G7 11th Gen",
    "cpuTag": "intel_i5",
    "gen": "11th",
    "ram": 16,
    "storage": 512,
    "display": "13.3\" FHD IPS Anti-Glare Spill-Resistant",
    "gpu": "Intel Iris Xe Graphics",
    "gpuType": "integrated",
    "category": "Rugged Enterprise",
    "badge": "Best Value",
    "badgeType": "b-corp",
    "price": 92000,
    "priceFormatted": "Rs 92,000",
    "priceUsd": 330,
    "img": "images/laptop-57-lenovo-thinkpad-l13-gen-2-57.jpg",
    "condition": "Like New (10/10) \u00b7 Certified Refurbished",
    "warranty": "1 Year Local Warranty + 7 Days Checking",
    "useCases": [
      "office",
      "programming",
      "student"
    ],
    "ramGb": 16,
    "storageGb": 512,
    "storageType": "NVMe SSD",
    "cpuBrand": "Intel",
    "cpuTier": "Core i5",
    "cpuGen": 11,
    "gpuCategory": "integrated",
    "isDedicatedGpu": false,
    "gpuModel": "Intel Iris Xe Graphics",
    "isRamUpgradable": true,
    "ramUpgradeOptions": [
      16,
      32
    ],
    "storageUpgradeOptions": [
      512,
      1000
    ],
    "legacyName": "Lenovo ThinkPad L13 Gen 2 Core i5 11th",
    "shortSpecs": {
      "cpuFamily": "Core i5",
      "generation": "11th Gen",
      "ramGb": 16,
      "storageGb": 512,
      "storageType": "NVMe SSD",
      "gpuType": "integrated",
      "isDedicatedGpu": false
    },
    "fullSpecs": {
      "performance": {
        "processor": "Intel Core i5-1135G7",
        "coresThreads": "4 Cores / 8 Threads",
        "clocks": "2.40 GHz Base, up to 4.20 GHz Turbo",
        "cache": "8 MB Intel Smart Cache"
      },
      "memoryStorage": {
        "ramSize": "16 GB",
        "ramType": "DDR4",
        "ramSpeed": "3200 MHz",
        "ramSlots": "Soldered Dual-Channel (Non-upgradable)",
        "storageSize": "512 GB",
        "storageType": "NVMe SSD",
        "interface": "PCIe Gen3 x4 M.2 2280",
        "readSpeed": "Up to 3,200 MB/s"
      },
      "display": {
        "size": "13.3\"",
        "resolution": "FHD (1920 x 1080)",
        "panelType": "IPS Anti-Glare",
        "refreshRate": "60 Hz",
        "touchAntiGlare": "Anti-Glare 250 nits (Non-touch)"
      },
      "graphics": {
        "gpuName": "Intel Iris Xe Graphics",
        "type": "Integrated",
        "vram": "Shared System Memory"
      },
      "connectivityPorts": {
        "ports": "1x Thunderbolt 4 USB-C, 1x USB-C 3.2 Gen 2, 2x USB-A 3.2 Gen 1 (1 Always On), 1x HDMI 2.0, MicroSD, Audio Jack",
        "wireless": "Intel Wi-Fi 6 AX201 + Bluetooth 5.1"
      },
      "batteryBuild": {
        "battery": "46Wh Rapid Charge (80% in 1 hr)",
        "weight": "1.39 kg (3.06 lbs)",
        "keyboard": "ThinkPad Spill-Resistant Backlit Keyboard with TrackPoint",
        "webcam": "720p HD with ThinkShutter Privacy Cover",
        "os": "Windows 11 Pro 64-bit Licensed"
      },
      "conditionWarranty": {
        "condition": "Grade A+ Like New \u00b7 Certified Business Ultrabook",
        "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"
      }
    },
    "bgTone": "white",
    "bgColor": "rgb(255, 255, 255)",
    "tintColor": "rgba(76, 124, 255, 0.04)",
    "processedImg": "images/processed/laptop-57-cutout.webp",
    "stock": 3
  },
  {
    "id": 58,
    "name": "Microsoft Surface Laptop 3 13.5\"",
    "brand": "microsoft",
    "brandName": "Microsoft",
    "series": "Surface Laptop 3",
    "cpu": "Intel Core i5-1035G7 10th Gen",
    "cpuTag": "intel_i5",
    "gen": "10th",
    "ram": 8,
    "storage": 256,
    "display": "13.5\" PixelSense 2256x1504 Touch",
    "gpu": "Intel Iris Plus Graphics",
    "gpuType": "integrated",
    "category": "Alcantara Signature",
    "badge": "PixelSense 3:2",
    "badgeType": "b-val",
    "price": 118000,
    "priceFormatted": "Rs 118,000",
    "priceUsd": 425,
    "img": "images/laptop-58-microsoft-surface-laptop-3-1872-58.jpg",
    "condition": "Like New (10/10) \u00b7 Certified Refurbished",
    "warranty": "1 Year Local Warranty + 7 Days Checking",
    "useCases": [
      "office",
      "student",
      "creator"
    ],
    "ramGb": 8,
    "storageGb": 256,
    "storageType": "NVMe SSD",
    "cpuBrand": "Intel",
    "cpuTier": "Core i5",
    "cpuGen": 10,
    "gpuCategory": "integrated",
    "isDedicatedGpu": false,
    "gpuModel": "Intel Iris Plus Graphics",
    "isRamUpgradable": false,
    "ramUpgradeOptions": [
      8
    ],
    "storageUpgradeOptions": [
      256,
      512,
      1000
    ],
    "legacyName": "Microsoft Surface Laptop 1872 Core i5 10th",
    "shortSpecs": {
      "cpuFamily": "Core i5",
      "generation": "10th Gen",
      "ramGb": 8,
      "storageGb": 256,
      "storageType": "NVMe SSD",
      "gpuType": "integrated",
      "isDedicatedGpu": false
    },
    "fullSpecs": {
      "performance": {
        "processor": "Intel Core i5-1035G7",
        "coresThreads": "4 Cores / 8 Threads",
        "clocks": "1.20 GHz Base, up to 3.70 GHz Boost",
        "cache": "6 MB Intel Smart Cache"
      },
      "memoryStorage": {
        "ramSize": "8 GB",
        "ramType": "LPDDR4x",
        "ramSpeed": "3733 MHz",
        "ramSlots": "Soldered (Non-upgradable)",
        "storageSize": "256 GB",
        "storageType": "NVMe SSD",
        "interface": "Removable M.2 2230 NVMe SSD",
        "readSpeed": "Up to 2,200 MB/s"
      },
      "display": {
        "size": "13.5\"",
        "resolution": "2.2K (2256 x 1504) 3:2 Aspect Ratio",
        "panelType": "PixelSense 10-Point Multi-Touch",
        "refreshRate": "60 Hz",
        "touchAntiGlare": "Corning Gorilla Glass 3 Touch with Surface Pen Support"
      },
      "graphics": {
        "gpuName": "Intel Iris Plus Graphics",
        "type": "Integrated",
        "vram": "Shared System Memory"
      },
      "connectivityPorts": {
        "ports": "1x USB-C 3.1, 1x USB-A 3.1, 3.5mm Headphone Jack, Surface Connect Port",
        "wireless": "Wi-Fi 6 (802.11ax) + Bluetooth 5.0"
      },
      "batteryBuild": {
        "battery": "45Wh Fast Charging (80% in 1 hr)",
        "weight": "1.26 kg (2.79 lbs) Matte Black Metal Chassis",
        "keyboard": "Backlit Keyboard with Large Precision Glass Touchpad",
        "webcam": "720p HD f/2.0 with Windows Hello Face Sign-in",
        "os": "Windows 11 Pro 64-bit Licensed"
      },
      "conditionWarranty": {
        "condition": "Pristine Like New (10/10) \u00b7 All-Metal Edition",
        "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"
      }
    },
    "bgTone": "white",
    "bgColor": "rgb(253, 253, 253)",
    "tintColor": "rgba(76, 124, 255, 0.04)",
    "processedImg": "images/processed/laptop-58-cutout.webp",
    "stock": 3
  },
  {
    "id": 59,
    "name": "HP EliteBook 845 G7",
    "brand": "hp",
    "brandName": "HP",
    "series": "EliteBook 845 G7",
    "cpu": "AMD Ryzen 5 PRO 4650U (6-Core/12-Thread)",
    "cpuTag": "amd",
    "gen": "Ryzen 4000",
    "ram": 16,
    "storage": 512,
    "display": "14\" FHD IPS Anti-Glare B&O Sound",
    "gpu": "AMD Radeon Vega 6",
    "gpuType": "integrated",
    "category": "6-Core Business",
    "badge": "Top Value",
    "badgeType": "b-corp",
    "price": 98000,
    "priceFormatted": "Rs 98,000",
    "priceUsd": 350,
    "img": "images/laptop-59-hp-elitebook-845-g7-59.jpg",
    "condition": "Like New (10/10) \u00b7 Certified Refurbished",
    "warranty": "1 Year Local Warranty + 7 Days Checking",
    "useCases": [
      "office",
      "programming",
      "student"
    ],
    "ramGb": 16,
    "storageGb": 512,
    "storageType": "NVMe SSD",
    "cpuBrand": "AMD",
    "cpuTier": "Ryzen 5",
    "cpuGen": 4000,
    "gpuCategory": "integrated",
    "isDedicatedGpu": false,
    "gpuModel": "AMD Radeon Vega 6",
    "isRamUpgradable": true,
    "ramUpgradeOptions": [
      16,
      32
    ],
    "storageUpgradeOptions": [
      512,
      1000
    ],
    "legacyName": "HP EliteBook 845G7 Ryzen 5",
    "shortSpecs": {
      "cpuFamily": "Ryzen 5",
      "generation": "4000 Series",
      "ramGb": 16,
      "storageGb": 512,
      "storageType": "NVMe SSD",
      "gpuType": "integrated",
      "isDedicatedGpu": false
    },
    "fullSpecs": {
      "performance": {
        "processor": "AMD Ryzen 5 PRO 4650U",
        "coresThreads": "6 Cores / 12 Threads",
        "clocks": "2.10 GHz Base, up to 4.00 GHz Boost",
        "cache": "8 MB L3 Cache"
      },
      "memoryStorage": {
        "ramSize": "16 GB",
        "ramType": "DDR4",
        "ramSpeed": "3200 MHz",
        "ramSlots": "2x SO-DIMM Slots (Upgradable to 64GB)",
        "storageSize": "512 GB",
        "storageType": "NVMe SSD",
        "interface": "PCIe Gen3 x4 NVMe M.2 2280",
        "readSpeed": "Up to 3,200 MB/s"
      },
      "display": {
        "size": "14.0\"",
        "resolution": "FHD (1920 x 1080)",
        "panelType": "IPS Anti-Glare",
        "refreshRate": "60 Hz",
        "touchAntiGlare": "Anti-Glare 250 nits / 400 nits Low Power"
      },
      "graphics": {
        "gpuName": "AMD Radeon Vega 6 Graphics",
        "type": "Integrated",
        "vram": "Shared System Memory"
      },
      "connectivityPorts": {
        "ports": "2x USB-C 3.1 Gen 2 (DisplayPort/PD), 2x USB-A 3.1 Gen 1 (1 charging), 1x HDMI 2.0, Audio combo",
        "wireless": "Intel Wi-Fi 6 AX200 + Bluetooth 5.0"
      },
      "batteryBuild": {
        "battery": "53Wh HP Long Life Fast Charge (50% in 30 mins)",
        "weight": "1.33 kg (2.93 lbs) Aluminum Chassis",
        "keyboard": "HP Premium Spill-Resistant Backlit Keyboard",
        "webcam": "720p HD IR Camera with Bang & Olufsen Dual Stereo Speakers",
        "os": "Windows 11 Pro 64-bit Licensed"
      },
      "conditionWarranty": {
        "condition": "Grade A+ Like New \u00b7 Certified Refurbished",
        "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"
      }
    },
    "bgTone": "colorful",
    "bgColor": "rgb(177, 173, 165)",
    "tintColor": "rgba(177, 173, 165, 0.15)",
    "processedImg": "images/laptop-59-hp-elitebook-845-g7-59.jpg",
    "stock": 3
  },
  {
    "id": 60,
    "name": "HP ProBook 640 G10",
    "brand": "hp",
    "brandName": "HP",
    "series": "ProBook 640 G10",
    "cpu": "Intel Core i5-1335U 13th Gen (10-Core)",
    "cpuTag": "intel_i5",
    "gen": "13th",
    "ram": 16,
    "storage": 512,
    "display": "14\" FHD IPS Anti-Glare Gen 4 NVMe",
    "gpu": "Intel Iris Xe Graphics",
    "gpuType": "integrated",
    "category": "Enterprise Workhorse",
    "badge": "13th Gen",
    "badgeType": "b-gen",
    "price": 174000,
    "priceFormatted": "Rs 174,000",
    "priceUsd": 625,
    "img": "images/laptop-60-hp-probook-640-g10-60.jpg",
    "condition": "Like New (10/10) \u00b7 Certified Refurbished",
    "warranty": "1 Year Local Warranty + 7 Days Checking",
    "useCases": [
      "office",
      "programming"
    ],
    "ramGb": 16,
    "storageGb": 512,
    "storageType": "NVMe SSD",
    "cpuBrand": "Intel",
    "cpuTier": "Core i5",
    "cpuGen": 13,
    "gpuCategory": "integrated",
    "isDedicatedGpu": false,
    "gpuModel": "Intel Iris Xe Graphics",
    "isRamUpgradable": true,
    "ramUpgradeOptions": [
      16,
      32
    ],
    "storageUpgradeOptions": [
      512,
      1000
    ],
    "legacyName": "HP ProBook 640G10 Core i5 13th",
    "shortSpecs": {
      "cpuFamily": "Core i5",
      "generation": "13th Gen",
      "ramGb": 16,
      "storageGb": 512,
      "storageType": "NVMe SSD",
      "gpuType": "integrated",
      "isDedicatedGpu": false
    },
    "fullSpecs": {
      "performance": {
        "processor": "Intel Core i5-1335U",
        "coresThreads": "10 Cores (2P + 8E) / 12 Threads",
        "clocks": "1.30 GHz Base, up to 4.60 GHz Turbo",
        "cache": "12 MB Intel Smart Cache"
      },
      "memoryStorage": {
        "ramSize": "16 GB",
        "ramType": "DDR4",
        "ramSpeed": "3200 MHz",
        "ramSlots": "2x SO-DIMM Slots (Upgradable to 64GB)",
        "storageSize": "512 GB",
        "storageType": "NVMe SSD",
        "interface": "PCIe Gen4 x4 NVMe M.2 2280",
        "readSpeed": "Up to 4,800 MB/s"
      },
      "display": {
        "size": "14.0\"",
        "resolution": "FHD (1920 x 1080)",
        "panelType": "IPS Anti-Glare",
        "refreshRate": "60 Hz",
        "touchAntiGlare": "Anti-Glare 250 nits / 400 nits (Non-touch)"
      },
      "graphics": {
        "gpuName": "Intel Iris Xe Graphics",
        "type": "Integrated",
        "vram": "Shared System Memory"
      },
      "connectivityPorts": {
        "ports": "1x Thunderbolt 4 USB4 Type-C, 3x USB Type-A 3.2 Gen 1 (1 charging), 1x HDMI 2.1, RJ-45 Gigabit, Headphone/mic combo",
        "wireless": "Intel Wi-Fi 6E AX211 + Bluetooth 5.3"
      },
      "batteryBuild": {
        "battery": "51.3Wh HP Long Life Fast Charge (50% in 30 mins)",
        "weight": "1.37 kg (3.03 lbs) Silver Aluminum",
        "keyboard": "HP Premium Spill-Resistant Backlit Keyboard",
        "webcam": "720p HD Privacy Camera with Temporal Noise Reduction",
        "os": "Windows 11 Pro 64-bit Licensed"
      },
      "conditionWarranty": {
        "condition": "Grade A+ Like New \u00b7 Current Generation Corporate",
        "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"
      }
    },
    "bgTone": "white",
    "bgColor": "rgb(254, 254, 254)",
    "tintColor": "rgba(76, 124, 255, 0.04)",
    "processedImg": "images/processed/laptop-60-cutout.webp",
    "stock": 3
  },
  {
    "id": 61,
    "name": "Dell Latitude 5320",
    "brand": "dell",
    "brandName": "Dell",
    "series": "Latitude 5320",
    "cpu": "Intel Core i3-1125G4 11th Gen (4-Core/8-Thread)",
    "cpuTag": "intel_i3",
    "gen": "11th",
    "ram": 8,
    "storage": 256,
    "display": "13.3\" FHD IPS Anti-Glare",
    "gpu": "Intel UHD Graphics",
    "gpuType": "integrated",
    "category": "Affordable Corporate",
    "badge": "4-Core i3",
    "badgeType": "b-val",
    "price": 75000,
    "priceFormatted": "Rs 75,000",
    "priceUsd": 270,
    "img": "images/laptop-61-dell-latitude-5320-61.jpg",
    "condition": "Like New (10/10) \u00b7 Certified Refurbished",
    "warranty": "1 Year Local Warranty + 7 Days Checking",
    "useCases": [
      "office",
      "student"
    ],
    "ramGb": 8,
    "storageGb": 256,
    "storageType": "NVMe SSD",
    "cpuBrand": "Intel",
    "cpuTier": "Core i3",
    "cpuGen": 11,
    "gpuCategory": "integrated",
    "isDedicatedGpu": false,
    "gpuModel": "Intel UHD Graphics",
    "isRamUpgradable": true,
    "ramUpgradeOptions": [
      8,
      16,
      32
    ],
    "storageUpgradeOptions": [
      256,
      512,
      1000
    ],
    "legacyName": "Dell Latitude 5320 Core i3 11th",
    "shortSpecs": {
      "cpuFamily": "Core i3",
      "generation": "11th Gen",
      "ramGb": 8,
      "storageGb": 256,
      "storageType": "NVMe SSD",
      "gpuType": "integrated",
      "isDedicatedGpu": false
    },
    "fullSpecs": {
      "performance": {
        "processor": "Intel Core i3-1125G4",
        "coresThreads": "4 Cores / 8 Threads (Rare 4-Core i3)",
        "clocks": "2.00 GHz Base, up to 3.70 GHz Turbo",
        "cache": "8 MB Intel Smart Cache"
      },
      "memoryStorage": {
        "ramSize": "8 GB",
        "ramType": "DDR4",
        "ramSpeed": "3200 MHz",
        "ramSlots": "Soldered Dual-Channel (Non-upgradable)",
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
        "touchAntiGlare": "Anti-Glare (Non-touch), 250 nits"
      },
      "graphics": {
        "gpuName": "Intel UHD Graphics",
        "type": "Integrated",
        "vram": "Shared System Memory"
      },
      "connectivityPorts": {
        "ports": "2x Thunderbolt 4 USB-C (Power Delivery/DisplayPort), 2x USB-A 3.2 Gen 1 (1 PowerShare), 1x HDMI 2.0, MicroSD, Audio Jack",
        "wireless": "Intel Wi-Fi 6 AX201 + Bluetooth 5.1"
      },
      "batteryBuild": {
        "battery": "42Wh / 63Wh ExpressCharge Capable",
        "weight": "1.20 kg (2.65 lbs)",
        "keyboard": "Backlit Spill-Resistant Keyboard",
        "webcam": "720p HD with Privacy Shutter",
        "os": "Windows 11 Pro 64-bit Licensed"
      },
      "conditionWarranty": {
        "condition": "Grade A+ Like New \u00b7 Fast Quad-Core Budget Ultrabook",
        "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"
      }
    },
    "bgTone": "white",
    "bgColor": "rgb(255, 255, 255)",
    "tintColor": "rgba(76, 124, 255, 0.04)",
    "processedImg": "images/processed/laptop-61-cutout.webp",
    "stock": 3
  },
  {
    "id": 62,
    "name": "Microsoft Surface Laptop 4 13.5\"",
    "brand": "microsoft",
    "brandName": "Microsoft",
    "series": "Surface Laptop 4",
    "cpu": "Intel Core i5-1135G7 11th Gen",
    "cpuTag": "intel_i5",
    "gen": "11th",
    "ram": 16,
    "storage": 512,
    "display": "13.5\" PixelSense 2256x1504 Touch (3:2)",
    "gpu": "Intel Iris Xe Graphics",
    "gpuType": "integrated",
    "category": "Modern Surface",
    "badge": "Omnisonic Audio",
    "badgeType": "b-val",
    "price": 145000,
    "priceFormatted": "Rs 145,000",
    "priceUsd": 520,
    "img": "images/laptop-62-microsoft-surface-laptop-4-1950-62.jpg",
    "condition": "Like New (10/10) \u00b7 Certified Refurbished",
    "warranty": "1 Year Local Warranty + 7 Days Checking",
    "useCases": [
      "office",
      "creator",
      "student"
    ],
    "ramGb": 16,
    "storageGb": 512,
    "storageType": "NVMe SSD",
    "cpuBrand": "Intel",
    "cpuTier": "Core i5",
    "cpuGen": 11,
    "gpuCategory": "integrated",
    "isDedicatedGpu": false,
    "gpuModel": "Intel Iris Xe Graphics",
    "isRamUpgradable": false,
    "ramUpgradeOptions": [
      16
    ],
    "storageUpgradeOptions": [
      512,
      1000
    ],
    "legacyName": "Microsoft Surface Laptop 4 1950 Core i5 11th",
    "shortSpecs": {
      "cpuFamily": "Core i5",
      "generation": "11th Gen",
      "ramGb": 16,
      "storageGb": 512,
      "storageType": "NVMe SSD",
      "gpuType": "integrated",
      "isDedicatedGpu": false
    },
    "fullSpecs": {
      "performance": {
        "processor": "Intel Core i5-1135G7",
        "coresThreads": "4 Cores / 8 Threads",
        "clocks": "2.40 GHz Base, up to 4.20 GHz Turbo",
        "cache": "8 MB Intel Smart Cache"
      },
      "memoryStorage": {
        "ramSize": "16 GB",
        "ramType": "LPDDR4x",
        "ramSpeed": "4267 MHz",
        "ramSlots": "Soldered Dual-Channel (Non-upgradable)",
        "storageSize": "512 GB",
        "storageType": "NVMe SSD",
        "interface": "Removable M.2 2230 NVMe SSD",
        "readSpeed": "Up to 3,200 MB/s"
      },
      "display": {
        "size": "13.5\"",
        "resolution": "2.2K (2256 x 1504) 3:2 Aspect Ratio",
        "panelType": "PixelSense 10-Point Multi-Touch",
        "refreshRate": "60 Hz",
        "touchAntiGlare": "Corning Gorilla Glass 3 Touch with Surface Pen Support, 400 nits"
      },
      "graphics": {
        "gpuName": "Intel Iris Xe Graphics",
        "type": "Integrated",
        "vram": "Shared System Memory"
      },
      "connectivityPorts": {
        "ports": "1x USB-C 3.1 Gen 2, 1x USB-A 3.1 Gen 2, 3.5mm Headphone Jack, Surface Connect Port",
        "wireless": "Wi-Fi 6 (802.11ax) + Bluetooth 5.0"
      },
      "batteryBuild": {
        "battery": "47.4Wh Fast Charging (Up to 17 hours)",
        "weight": "1.28 kg (2.84 lbs) Matte Black Aluminum",
        "keyboard": "Backlit Keyboard with Large Precision Glass Trackpad",
        "webcam": "720p HD f/2.0 with Windows Hello & Omnisonic Speakers with Dolby Atmos",
        "os": "Windows 11 Pro 64-bit Licensed"
      },
      "conditionWarranty": {
        "condition": "Pristine Like New (10/10) \u00b7 Premium Sleek Laptop",
        "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"
      }
    },
    "bgTone": "white",
    "bgColor": "rgb(255, 255, 255)",
    "tintColor": "rgba(76, 124, 255, 0.04)",
    "processedImg": "images/processed/laptop-62-cutout.webp",
    "stock": 3
  },
  {
    "id": 63,
    "name": "Microsoft Surface Laptop 4 15\"",
    "brand": "microsoft",
    "brandName": "Microsoft",
    "series": "Surface Laptop 4",
    "cpu": "Intel Core i7-1185G7 11th Gen",
    "cpuTag": "intel_i7",
    "gen": "11th",
    "ram": 16,
    "storage": 512,
    "display": "13.5\" PixelSense Touch Dolby Atmos",
    "gpu": "Intel Iris Xe Graphics",
    "gpuType": "integrated",
    "category": "Executive Surface",
    "badge": "Core i7 Touch",
    "badgeType": "b-val",
    "price": 175000,
    "priceFormatted": "Rs 175,000",
    "priceUsd": 630,
    "img": "images/laptop-63-microsoft-surface-laptop-4-1979-63.jpg",
    "condition": "Like New (10/10) \u00b7 Certified Refurbished",
    "warranty": "1 Year Local Warranty + 7 Days Checking",
    "useCases": [
      "office",
      "creator",
      "student"
    ],
    "ramGb": 16,
    "storageGb": 512,
    "storageType": "NVMe SSD",
    "cpuBrand": "Intel",
    "cpuTier": "Core i7",
    "cpuGen": 11,
    "gpuCategory": "integrated",
    "isDedicatedGpu": false,
    "gpuModel": "Intel Iris Xe Graphics",
    "isRamUpgradable": false,
    "ramUpgradeOptions": [
      16
    ],
    "storageUpgradeOptions": [
      512,
      1000
    ],
    "legacyName": "Microsoft Surface Laptop 4 1979 Core i7 11th",
    "shortSpecs": {
      "cpuFamily": "Core i7",
      "generation": "11th Gen",
      "ramGb": 16,
      "storageGb": 512,
      "storageType": "NVMe SSD",
      "gpuType": "integrated",
      "isDedicatedGpu": false
    },
    "fullSpecs": {
      "performance": {
        "processor": "Intel Core i7-1185G7",
        "coresThreads": "4 Cores / 8 Threads",
        "clocks": "3.00 GHz Base, up to 4.80 GHz Turbo",
        "cache": "12 MB Intel Smart Cache"
      },
      "memoryStorage": {
        "ramSize": "16 GB",
        "ramType": "LPDDR4x",
        "ramSpeed": "4267 MHz",
        "ramSlots": "Soldered Dual-Channel (Non-upgradable)",
        "storageSize": "512 GB",
        "storageType": "NVMe SSD",
        "interface": "Removable M.2 2230 NVMe SSD",
        "readSpeed": "Up to 3,500 MB/s"
      },
      "display": {
        "size": "15.0\"",
        "resolution": "2.5K (2496 x 1664) 3:2 Aspect Ratio",
        "panelType": "PixelSense 10-Point Multi-Touch",
        "refreshRate": "60 Hz",
        "touchAntiGlare": "Corning Gorilla Glass 3 Touch with Surface Pen Support, 400 nits"
      },
      "graphics": {
        "gpuName": "Intel Iris Xe Graphics",
        "type": "Integrated",
        "vram": "Shared System Memory"
      },
      "connectivityPorts": {
        "ports": "1x USB-C 3.1 Gen 2, 1x USB-A 3.1 Gen 2, 3.5mm Headphone Jack, Surface Connect Port",
        "wireless": "Wi-Fi 6 (802.11ax) + Bluetooth 5.0"
      },
      "batteryBuild": {
        "battery": "47.4Wh Fast Charging (Up to 16.5 hours)",
        "weight": "1.54 kg (3.40 lbs) Matte Black All-Metal Unibody",
        "keyboard": "Backlit Keyboard with Large Glass Touchpad",
        "webcam": "720p HD with Windows Hello Facial Authentication",
        "os": "Windows 11 Pro 64-bit Licensed"
      },
      "conditionWarranty": {
        "condition": "Pristine Like New (10/10) \u00b7 Big Screen Premium Productivity",
        "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"
      }
    },
    "bgTone": "white",
    "bgColor": "rgb(251, 251, 251)",
    "tintColor": "rgba(76, 124, 255, 0.04)",
    "processedImg": "images/processed/laptop-63-cutout.webp",
    "stock": 3
  },
  {
    "id": 64,
    "name": "Dell XPS 15 9500",
    "brand": "dell",
    "brandName": "Dell",
    "series": "XPS 15",
    "cpu": "Intel Core i7-10750H (6-Core/12-Thread 45W)",
    "cpuTag": "intel_i7",
    "gen": "10th",
    "ram": 16,
    "storage": 512,
    "display": "15.6\" FHD+ 16:10 (1920x1200) 500 nits",
    "gpu": "NVIDIA GeForce GTX 1650 Ti 4GB GDDR6",
    "gpuType": "discrete",
    "category": "Creator Studio 15",
    "badge": "GTX 1650 Ti",
    "badgeType": "b-corp",
    "price": 195000,
    "priceFormatted": "Rs 195,000",
    "priceUsd": 700,
    "img": "images/laptop-64-dell-xps-15-9500-64.jpg",
    "condition": "Like New (10/10) \u00b7 Certified Refurbished",
    "warranty": "1 Year Local Warranty + 7 Days Checking",
    "useCases": [
      "creator",
      "gaming",
      "programming"
    ],
    "ramGb": 16,
    "storageGb": 512,
    "storageType": "NVMe SSD",
    "cpuBrand": "Intel",
    "cpuTier": "Core i7",
    "cpuGen": 10,
    "gpuCategory": "dedicated",
    "isDedicatedGpu": true,
    "gpuModel": "NVIDIA GeForce GTX 1650 Ti 4GB GDDR6",
    "isRamUpgradable": true,
    "ramUpgradeOptions": [
      16,
      32
    ],
    "storageUpgradeOptions": [
      512,
      1000
    ],
    "legacyName": "Dell XPS 15 9500 Core i7 10th",
    "shortSpecs": {
      "cpuFamily": "Core i7",
      "generation": "10th Gen",
      "ramGb": 16,
      "storageGb": 512,
      "storageType": "NVMe SSD",
      "gpuType": "discrete",
      "isDedicatedGpu": true
    },
    "fullSpecs": {
      "performance": {
        "processor": "Intel Core i7-10750H (45W High-Performance)",
        "coresThreads": "6 Cores / 12 Threads",
        "clocks": "2.60 GHz Base, up to 5.00 GHz Max Turbo",
        "cache": "12 MB Intel Smart Cache"
      },
      "memoryStorage": {
        "ramSize": "16 GB",
        "ramType": "DDR4",
        "ramSpeed": "2933 MHz",
        "ramSlots": "2x SO-DIMM Slots (Upgradable to 64GB)",
        "storageSize": "512 GB",
        "storageType": "NVMe SSD",
        "interface": "Dual M.2 PCIe Gen3 x4 NVMe Slots",
        "readSpeed": "Up to 3,500 MB/s"
      },
      "display": {
        "size": "15.6\"",
        "resolution": "FHD+ (1920 x 1200) 16:10 500 nits InfinityEdge",
        "panelType": "IPS Anti-Glare 100% sRGB",
        "refreshRate": "60 Hz",
        "touchAntiGlare": "Anti-Glare 500 nits 4-sided InfinityEdge (Non-touch)"
      },
      "graphics": {
        "gpuName": "NVIDIA GeForce GTX 1650 Ti",
        "type": "Dedicated",
        "vram": "4 GB GDDR6 Dedicated"
      },
      "connectivityPorts": {
        "ports": "2x Thunderbolt 3 (Power Delivery and DisplayPort), 1x USB-C 3.1 (PD/DisplayPort), Full-size SD Card Reader v6.0, 3.5mm Headphone Jack",
        "wireless": "Killer Wi-Fi 6 AX1650 (2x2) + Bluetooth 5.1"
      },
      "batteryBuild": {
        "battery": "86Wh 6-Cell Lithium-Ion ExpressCharge",
        "weight": "1.83 kg (4.0 lbs) CNC Platinum Silver Aluminum with Carbon Fiber Palmrest",
        "keyboard": "Backlit Keyboard with Huge Glass Precision Touchpad",
        "webcam": "720p HD with Dual-Array Digital Mics & Windows Hello IR",
        "os": "Windows 11 Pro 64-bit Licensed"
      },
      "conditionWarranty": {
        "condition": "Pristine Like New (10/10) \u00b7 Creator Flagship",
        "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"
      }
    },
    "bgTone": "white",
    "bgColor": "rgb(255, 255, 255)",
    "tintColor": "rgba(76, 124, 255, 0.04)",
    "processedImg": "images/processed/laptop-64-cutout.webp",
    "stock": 3
  },
  {
    "id": 65,
    "name": "Lenovo ThinkPad T490s",
    "brand": "lenovo",
    "brandName": "Lenovo",
    "series": "ThinkPad T490s",
    "cpu": "Intel Core i5-8365U vPro Quad Core",
    "cpuTag": "intel_i5",
    "gen": "8th",
    "ram": 16,
    "storage": 512,
    "display": "14\" FHD IPS Low Power 400 nits",
    "gpu": "Intel UHD Graphics 620",
    "gpuType": "integrated",
    "category": "Slim Executive",
    "badge": "400 nits Panel",
    "badgeType": "b-corp",
    "price": 78000,
    "priceFormatted": "Rs 78,000",
    "priceUsd": 280,
    "img": "images/laptop-65-lenovo-thinkpad-t490s-65.jpg",
    "condition": "Like New (10/10) \u00b7 Certified Refurbished",
    "warranty": "1 Year Local Warranty + 7 Days Checking",
    "useCases": [
      "office",
      "programming",
      "student"
    ],
    "ramGb": 16,
    "storageGb": 512,
    "storageType": "NVMe SSD",
    "cpuBrand": "Intel",
    "cpuTier": "Core i5",
    "cpuGen": 8,
    "gpuCategory": "integrated",
    "isDedicatedGpu": false,
    "gpuModel": "Intel UHD Graphics 620",
    "isRamUpgradable": true,
    "ramUpgradeOptions": [
      16,
      32
    ],
    "storageUpgradeOptions": [
      512,
      1000
    ],
    "legacyName": "Lenovo Thinkpad T490s Core i5 8th",
    "shortSpecs": {
      "cpuFamily": "Core i5",
      "generation": "8th Gen",
      "ramGb": 16,
      "storageGb": 512,
      "storageType": "NVMe SSD",
      "gpuType": "integrated",
      "isDedicatedGpu": false
    },
    "fullSpecs": {
      "performance": {
        "processor": "Intel Core i5-8365U vPro Quad Core",
        "coresThreads": "4 Cores / 8 Threads",
        "clocks": "1.60 GHz Base, up to 4.10 GHz Boost",
        "cache": "6 MB Intel Smart Cache"
      },
      "memoryStorage": {
        "ramSize": "16 GB",
        "ramType": "DDR4",
        "ramSpeed": "2400 MHz",
        "ramSlots": "Soldered Dual-Channel (Non-upgradable)",
        "storageSize": "512 GB",
        "storageType": "NVMe SSD",
        "interface": "PCIe Gen3 x4 M.2 2280",
        "readSpeed": "Up to 3,200 MB/s"
      },
      "display": {
        "size": "14.0\"",
        "resolution": "FHD (1920 x 1080) Low Power 400 nits",
        "panelType": "IPS Anti-Glare",
        "refreshRate": "60 Hz",
        "touchAntiGlare": "Anti-Glare (Non-touch), 400 nits Low Power 72% NTSC"
      },
      "graphics": {
        "gpuName": "Intel UHD Graphics 620",
        "type": "Integrated",
        "vram": "Shared System Memory"
      },
      "connectivityPorts": {
        "ports": "1x USB-C 3.1 Gen 1 (PD/DisplayPort), 1x Thunderbolt 3, 2x USB-A 3.1 Gen 1 (1 Always On), HDMI 1.4b, MicroSD, Audio Jack",
        "wireless": "Intel Wireless-AC 9560 802.11ac + Bluetooth 5.0"
      },
      "batteryBuild": {
        "battery": "57Wh Rapid Charge (80% in 1 hr)",
        "weight": "1.35 kg (2.98 lbs) Magnesium/Carbon-Fiber",
        "keyboard": "ThinkPad Precision Backlit Keyboard with TrackPoint",
        "webcam": "720p HD with ThinkShutter Privacy Cover",
        "os": "Windows 11 Pro 64-bit Licensed"
      },
      "conditionWarranty": {
        "condition": "Grade A+ Like New \u00b7 400 Nits Low-Power Display",
        "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"
      }
    },
    "bgTone": "white",
    "bgColor": "rgb(255, 255, 255)",
    "tintColor": "rgba(76, 124, 255, 0.04)",
    "processedImg": "images/processed/laptop-65-cutout.webp",
    "stock": 3
  },
  {
    "id": 66,
    "name": "Apple MacBook Air 13\" (M2)",
    "brand": "apple",
    "brandName": "Apple",
    "series": "MacBook Air M2",
    "cpu": "Apple M2 (8-Core CPU / 8-Core GPU)",
    "cpuTag": "apple",
    "gen": "M2",
    "ram": 16,
    "storage": 512,
    "display": "13.6\" Liquid Retina Display 500 nits",
    "gpu": "Apple 8-Core GPU",
    "gpuType": "apple_gpu",
    "category": "MagSafe Ultra-Thin",
    "badge": "Midnight M2",
    "badgeType": "b-apple",
    "price": 285000,
    "priceFormatted": "Rs 285,000",
    "priceUsd": 1025,
    "img": "images/laptop-66-apple-macbook-air-m2-66.jpg",
    "condition": "Open Box / Brand New Condition",
    "warranty": "1 Year Local Warranty + 7 Days Checking",
    "useCases": [
      "creator",
      "office",
      "student",
      "programming"
    ],
    "ramGb": 16,
    "storageGb": 512,
    "storageType": "NVMe SSD",
    "cpuBrand": "Apple",
    "cpuTier": "M2",
    "cpuGen": 2,
    "gpuCategory": "apple",
    "isDedicatedGpu": false,
    "gpuModel": "Apple 8-Core GPU",
    "isRamUpgradable": false,
    "ramUpgradeOptions": [
      16
    ],
    "storageUpgradeOptions": [
      512,
      1000
    ],
    "legacyName": "APPLE MACBOOK M2 AIR",
    "shortSpecs": {
      "cpuFamily": "M2",
      "generation": "2022",
      "ramGb": 16,
      "storageGb": 512,
      "storageType": "NVMe SSD",
      "gpuType": "apple_gpu",
      "isDedicatedGpu": false
    },
    "fullSpecs": {
      "performance": {
        "processor": "Apple M2 Chip (8-Core CPU)",
        "coresThreads": "4 Performance Cores + 4 Efficiency Cores (8 Cores Total)",
        "clocks": "Up to 3.49 GHz Next-Gen Apple Silicon",
        "cache": "16-Core Neural Engine 100GB/s Memory Bandwidth"
      },
      "memoryStorage": {
        "ramSize": "16 GB",
        "ramType": "Unified Memory",
        "ramSpeed": "100 GB/s Bandwidth",
        "ramSlots": "Unified Memory Architecture (Non-upgradable)",
        "storageSize": "512 GB",
        "storageType": "Apple High-Speed SSD",
        "interface": "Custom Integrated Apple Controller",
        "readSpeed": "Up to 3,500 MB/s"
      },
      "display": {
        "size": "13.6\"",
        "resolution": "Liquid Retina (2560 x 1664) 500 nits",
        "panelType": "Liquid Retina with P3 Wide Color",
        "refreshRate": "60 Hz",
        "touchAntiGlare": "500 nits Brightness with True Tone Technology"
      },
      "graphics": {
        "gpuName": "Apple 8-Core GPU",
        "type": "Apple Silicon Integrated GPU",
        "vram": "Shared Unified Memory (Up to 16GB)"
      },
      "connectivityPorts": {
        "ports": "MagSafe 3 Charging Port, 2x Thunderbolt / USB 4 Ports, 3.5mm Headphone Jack with High-Impedance Support",
        "wireless": "Wi-Fi 6 (802.11ax) + Bluetooth 5.3"
      },
      "batteryBuild": {
        "battery": "52.6Wh Lithium-Polymer (Up to 18 hours battery life, Fanless Zero Noise)",
        "weight": "1.24 kg (2.7 lbs) Ultra-Thin 11.3mm Aluminum Unibody",
        "keyboard": "Magic Keyboard with Touch ID & Ambient Light Sensor",
        "webcam": "1080p FaceTime HD Camera with Four-Speaker Sound System Spatial Audio",
        "os": "macOS Sequoia / Sonoma Official Licensed"
      },
      "conditionWarranty": {
        "condition": "Pristine Like New (10/10) \u00b7 Fanless Silent Design",
        "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"
      }
    },
    "bgTone": "white",
    "bgColor": "rgb(246, 246, 246)",
    "tintColor": "rgba(76, 124, 255, 0.04)",
    "processedImg": "images/processed/laptop-66-cutout.webp",
    "stock": 3
  },
  {
    "id": 67,
    "name": "Dell Latitude 7430",
    "brand": "dell",
    "brandName": "Dell",
    "series": "Latitude 7430",
    "cpu": "Intel Core i7-1265U 12th Gen (10-Core)",
    "cpuTag": "intel_i7",
    "gen": "12th",
    "ram": 16,
    "storage": 512,
    "display": "14\" FHD IPS Anti-Glare Carbon",
    "gpu": "Intel Iris Xe Graphics",
    "gpuType": "integrated",
    "category": "Corporate Ultrabook",
    "badge": "Verified Stock",
    "badgeType": "b-corp",
    "price": 154000,
    "priceFormatted": "Rs 154,000",
    "priceUsd": 550,
    "img": "images/laptop-67-dell-latitude-7430-67.jpg",
    "condition": "Like New (10/10) \u00b7 Certified Refurbished",
    "warranty": "1 Year Local Warranty + 7 Days Checking",
    "useCases": [
      "office",
      "programming"
    ],
    "ramGb": 16,
    "storageGb": 512,
    "storageType": "NVMe SSD",
    "cpuBrand": "Intel",
    "cpuTier": "Core i7",
    "cpuGen": 12,
    "gpuCategory": "integrated",
    "isDedicatedGpu": false,
    "gpuModel": "Intel Iris Xe Graphics",
    "isRamUpgradable": true,
    "ramUpgradeOptions": [
      16,
      32
    ],
    "storageUpgradeOptions": [
      512,
      1000
    ],
    "legacyName": "Dell Latitude 7430 Core i7 12th",
    "shortSpecs": {
      "cpuFamily": "Core i7",
      "generation": "12th Gen",
      "ramGb": 16,
      "storageGb": 512,
      "storageType": "NVMe SSD",
      "gpuType": "integrated",
      "isDedicatedGpu": false
    },
    "fullSpecs": {
      "performance": {
        "processor": "Intel Core i7-1265U vPro",
        "coresThreads": "10 Cores (2P + 8E) / 12 Threads",
        "clocks": "1.80 GHz Base, up to 4.80 GHz Turbo",
        "cache": "12 MB Intel Smart Cache"
      },
      "memoryStorage": {
        "ramSize": "16 GB",
        "ramType": "DDR4",
        "ramSpeed": "3200 MHz",
        "ramSlots": "Soldered Dual-Channel (Non-upgradable)",
        "storageSize": "512 GB",
        "storageType": "NVMe SSD",
        "interface": "PCIe Gen4 x4 NVMe M.2 2280",
        "readSpeed": "Up to 4,800 MB/s"
      },
      "display": {
        "size": "14.0\"",
        "resolution": "FHD (1920 x 1080)",
        "panelType": "IPS Super Low Power Anti-Glare",
        "refreshRate": "60 Hz",
        "touchAntiGlare": "Anti-Glare 400 nits ComfortView Plus (Non-touch)"
      },
      "graphics": {
        "gpuName": "Intel Iris Xe Graphics",
        "type": "Integrated",
        "vram": "Shared System Memory"
      },
      "connectivityPorts": {
        "ports": "2x Thunderbolt 4 USB-C (Power Delivery and DisplayPort), 1x USB-A 3.2 Gen 1 (PowerShare), 1x HDMI 2.0, MicroSD 4.0, Audio Jack",
        "wireless": "Intel Wi-Fi 6E AX211 + Bluetooth 5.2"
      },
      "batteryBuild": {
        "battery": "58Wh ExpressCharge Capable",
        "weight": "1.22 kg (2.69 lbs) Carbon Fiber Unibody",
        "keyboard": "Backlit Spill-Resistant Keyboard",
        "webcam": "FHD IR Camera with Presence Detection & Privacy Shutter",
        "os": "Windows 11 Pro 64-bit Licensed"
      },
      "conditionWarranty": {
        "condition": "Pristine Like New (10/10) \u00b7 12th Gen Executive Carbon",
        "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"
      }
    },
    "bgTone": "white",
    "bgColor": "rgb(253, 253, 253)",
    "tintColor": "rgba(76, 124, 255, 0.04)",
    "processedImg": "images/processed/laptop-67-cutout.webp",
    "stock": 3
  },
  {
    "id": 68,
    "name": "HP EliteBook 630 G11",
    "brand": "hp",
    "brandName": "HP",
    "series": "EliteBook 630 G11",
    "cpu": "Intel Core Ultra 5 125U (AI Boost NPU)",
    "cpuTag": "intel_ultra",
    "gen": "Core Ultra",
    "ram": 16,
    "storage": 512,
    "display": "13.3\" WUXGA 16:10 IPS Anti-Glare",
    "gpu": "Intel Graphics",
    "gpuType": "integrated",
    "category": "AI Ultra Workhorse",
    "badge": "Intel Ultra AI",
    "badgeType": "b-gen",
    "price": 215000,
    "priceFormatted": "Rs 215,000",
    "priceUsd": 770,
    "img": "images/laptop-68-hp-elitebook-630-g11-68.jpg",
    "condition": "Like New (10/10) \u00b7 Certified Refurbished",
    "warranty": "1 Year Local Warranty + 7 Days Checking",
    "useCases": [
      "office",
      "programming",
      "creator"
    ],
    "ramGb": 16,
    "storageGb": 512,
    "storageType": "NVMe SSD",
    "cpuBrand": "Intel",
    "cpuTier": "Core Ultra 5",
    "cpuGen": 14,
    "gpuCategory": "integrated",
    "isDedicatedGpu": false,
    "gpuModel": "Intel Graphics",
    "isRamUpgradable": true,
    "ramUpgradeOptions": [
      16,
      32
    ],
    "storageUpgradeOptions": [
      512,
      1000
    ],
    "legacyName": "HP EliteBook 630G11 Core ULTA 5",
    "shortSpecs": {
      "cpuFamily": "Core Ultra 5",
      "generation": "Series 1 (AI PC)",
      "ramGb": 16,
      "storageGb": 512,
      "storageType": "NVMe SSD",
      "gpuType": "integrated",
      "isDedicatedGpu": false
    },
    "fullSpecs": {
      "performance": {
        "processor": "Intel Core Ultra 5 125U (AI Boost NPU)",
        "coresThreads": "12 Cores (2P + 8E + 2 Low-Power E) / 14 Threads",
        "clocks": "Up to 4.30 GHz Turbo with Dedicated Intel AI NPU",
        "cache": "12 MB Intel Smart Cache"
      },
      "memoryStorage": {
        "ramSize": "16 GB",
        "ramType": "DDR5",
        "ramSpeed": "5600 MHz",
        "ramSlots": "2x SO-DIMM Slots (Upgradable to 64GB)",
        "storageSize": "512 GB",
        "storageType": "NVMe SSD",
        "interface": "PCIe Gen4 x4 NVMe M.2 2280",
        "readSpeed": "Up to 5,000 MB/s"
      },
      "display": {
        "size": "13.3\"",
        "resolution": "WUXGA (1920 x 1200) 16:10",
        "panelType": "IPS Anti-Glare",
        "refreshRate": "60 Hz",
        "touchAntiGlare": "Anti-Glare 300 nits 16:10 Aspect Ratio (Non-touch)"
      },
      "graphics": {
        "gpuName": "Intel Graphics (Meteor Lake Architecture)",
        "type": "Integrated",
        "vram": "Shared System Memory"
      },
      "connectivityPorts": {
        "ports": "2x Thunderbolt 4 USB-C (40Gbps), 2x USB Type-A 3.2 Gen 1 (1 charging), 1x HDMI 2.1, Headphone/mic combo",
        "wireless": "Intel Wi-Fi 6E AX211 + Bluetooth 5.3"
      },
      "batteryBuild": {
        "battery": "54Wh HP Long Life Fast Charge",
        "weight": "1.23 kg (2.71 lbs) Premium Recycled Aluminum",
        "keyboard": "HP Premium Spill-Resistant Backlit Keyboard",
        "webcam": "FHD 1080p Camera with AI Noise Reduction & Privacy Shutter",
        "os": "Windows 11 Pro 64-bit Licensed"
      },
      "conditionWarranty": {
        "condition": "Open Box / Brand New Condition \u00b7 Latest AI Generation",
        "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"
      }
    },
    "bgTone": "white",
    "bgColor": "rgb(255, 255, 255)",
    "tintColor": "rgba(76, 124, 255, 0.04)",
    "processedImg": "images/processed/laptop-68-cutout.webp",
    "stock": 3
  },
  {
    "id": 69,
    "name": "Dell XPS 13 Plus 9320",
    "brand": "dell",
    "brandName": "Dell",
    "series": "XPS 13 Plus",
    "cpu": "Intel Core i7-1280P (14-Core/20-Thread 28W)",
    "cpuTag": "intel_i7",
    "gen": "12th",
    "ram": 16,
    "storage": 512,
    "display": "13.4\" 3.5K OLED Touch or FHD+ 500 nits",
    "gpu": "Intel Iris Xe Graphics",
    "gpuType": "integrated",
    "category": "Invisible Glass Touchpad",
    "badge": "XPS Plus Flagship",
    "badgeType": "b-gen",
    "price": 275000,
    "priceFormatted": "Rs 275,000",
    "priceUsd": 990,
    "img": "images/laptop-69-dell-xps-13-plus-9320-69.jpg",
    "condition": "Open Box / Brand New Condition",
    "warranty": "1 Year Local Warranty + 7 Days Checking",
    "useCases": [
      "creator",
      "programming",
      "office"
    ],
    "ramGb": 16,
    "storageGb": 512,
    "storageType": "NVMe SSD",
    "cpuBrand": "Intel",
    "cpuTier": "Core i7",
    "cpuGen": 12,
    "gpuCategory": "integrated",
    "isDedicatedGpu": false,
    "gpuModel": "Intel Iris Xe Graphics",
    "isRamUpgradable": false,
    "ramUpgradeOptions": [
      16
    ],
    "storageUpgradeOptions": [
      512,
      1000
    ],
    "legacyName": "Dell XPS 9320 Core i7 12th",
    "shortSpecs": {
      "cpuFamily": "Core i7",
      "generation": "12th Gen",
      "ramGb": 16,
      "storageGb": 512,
      "storageType": "NVMe SSD",
      "gpuType": "integrated",
      "isDedicatedGpu": false
    },
    "fullSpecs": {
      "performance": {
        "processor": "Intel Core i7-1280P (28W Performance)",
        "coresThreads": "14 Cores (6P + 8E) / 20 Threads",
        "clocks": "1.80 GHz Base, up to 4.80 GHz Turbo",
        "cache": "24 MB Intel Smart Cache"
      },
      "memoryStorage": {
        "ramSize": "16 GB",
        "ramType": "LPDDR5",
        "ramSpeed": "5200 MHz",
        "ramSlots": "Soldered Dual-Channel (Non-upgradable)",
        "storageSize": "512 GB",
        "storageType": "NVMe SSD",
        "interface": "PCIe Gen4 x4 NVMe M.2 2280",
        "readSpeed": "Up to 6,000 MB/s"
      },
      "display": {
        "size": "13.4\"",
        "resolution": "3.5K (3456 x 2160) OLED Touch / FHD+ 500 nits",
        "panelType": "OLED InfinityEdge / IPS",
        "refreshRate": "60 Hz",
        "touchAntiGlare": "Corning Gorilla Glass 7 Touch / Anti-Glare 500 nits"
      },
      "graphics": {
        "gpuName": "Intel Iris Xe Graphics",
        "type": "Integrated",
        "vram": "Shared System Memory"
      },
      "connectivityPorts": {
        "ports": "2x Thunderbolt 4 USB-C (Power Delivery and DisplayPort), USB-C to USB-A adapter included",
        "wireless": "Intel Killer Wi-Fi 6E 1675 (AX211) + Bluetooth 5.2"
      },
      "batteryBuild": {
        "battery": "55Wh ExpressCharge Capable",
        "weight": "1.24 kg (2.73 lbs) CNC Machined Aluminum",
        "keyboard": "Zero-Lattice Backlit Keyboard + Capacitive Touch Function Row + Seamless Glass Touchpad",
        "webcam": "720p HD RGB + 400p IR Camera with Windows Hello",
        "os": "Windows 11 Pro 64-bit Licensed"
      },
      "conditionWarranty": {
        "condition": "Open Box / Brand New Condition \u00b7 Futuristic Flagship",
        "warranty": "1 Year Local Warranty + 7 Days Checking Guarantee"
      }
    },
    "bgTone": "white",
    "bgColor": "rgb(254, 253, 253)",
    "tintColor": "rgba(76, 124, 255, 0.04)",
    "processedImg": "images/processed/laptop-69-cutout.webp",
    "stock": 3
  }
];

if (typeof module !== 'undefined') module.exports = LAPTOPS_INVENTORY;
