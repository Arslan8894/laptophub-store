import json
import re
import sys

DATA_JS_PATH = 'laptops-data.js'

with open(DATA_JS_PATH, 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'const\s+LAPTOPS_INVENTORY\s*=\s*(\[.*?\]);', text, re.DOTALL)
if not m:
    print('Failed to match LAPTOPS_INVENTORY')
    sys.exit(1)

laptops = json.loads(m.group(1))
print(f"Loaded {len(laptops)} laptops.")

non_upgradable_series = ['surface', 'macbook', 'xps 13', 'x1 yoga', 'x13', 'yoga slim', 'folio']

for lap in laptops:
    cpu = lap.get('cpu', '')
    gpu = lap.get('gpu', '')
    brand = lap.get('brand', '').lower()
    series = lap.get('series', '').lower()
    name = lap.get('name', '').lower()
    gen = str(lap.get('gen', '')).lower()
    
    # 1. ramGb & storageGb
    ramGb = int(lap.get('ram', 16))
    storageGb = int(lap.get('storage', 512))
    storageType = "NVMe SSD"
    
    # 2. cpuBrand
    if brand == 'apple' or 'apple' in cpu.lower() or 'm1' in cpu.lower() or 'm2' in cpu.lower() or 'm4' in cpu.lower():
        cpuBrand = 'Apple'
    elif 'amd' in cpu.lower() or 'ryzen' in cpu.lower():
        cpuBrand = 'AMD'
    else:
        cpuBrand = 'Intel'
        
    # 3. cpuTier
    if cpuBrand == 'Apple':
        if 'm4 max' in cpu.lower(): cpuTier = 'M4 Max'
        elif 'm1 pro' in cpu.lower(): cpuTier = 'M1 Pro'
        elif 'm2' in cpu.lower(): cpuTier = 'M2'
        else: cpuTier = 'Apple Silicon'
    elif cpuBrand == 'AMD':
        if 'ryzen 7' in cpu.lower(): cpuTier = 'Ryzen 7'
        elif 'ryzen 5' in cpu.lower(): cpuTier = 'Ryzen 5'
        elif 'ryzen 9' in cpu.lower(): cpuTier = 'Ryzen 9'
        else: cpuTier = 'Ryzen'
    else:
        if 'core ultra 7' in cpu.lower(): cpuTier = 'Core Ultra 7'
        elif 'core ultra 5' in cpu.lower() or 'core ulta 5' in cpu.lower(): cpuTier = 'Core Ultra 5'
        elif 'core i9' in cpu.lower(): cpuTier = 'Core i9'
        elif 'core i7' in cpu.lower(): cpuTier = 'Core i7'
        elif 'core i5' in cpu.lower(): cpuTier = 'Core i5'
        elif 'core i3' in cpu.lower(): cpuTier = 'Core i3'
        elif 'core m' in cpu.lower(): cpuTier = 'Core M'
        else: cpuTier = 'Core i5'
        
    # 4. cpuGen
    if cpuBrand == 'Apple':
        if 'm1' in cpuTier.lower(): cpuGen = 1
        elif 'm2' in cpuTier.lower(): cpuGen = 2
        elif 'm4' in cpuTier.lower(): cpuGen = 4
        else: cpuGen = 1
    elif cpuBrand == 'AMD':
        if '7530' in cpu or '7350' in cpu: cpuGen = 7000
        elif '6800' in cpu: cpuGen = 6000
        elif '4750' in cpu or '4650' in cpu: cpuGen = 4000
        else: cpuGen = 5000
    else:
        if 'ultra' in cpuTier.lower(): cpuGen = 14
        elif '13th' in cpu or '13' in gen: cpuGen = 13
        elif '12th' in cpu or '12' in gen: cpuGen = 12
        elif '11th' in cpu or '11' in gen: cpuGen = 11
        elif '10th' in cpu or '10' in gen: cpuGen = 10
        elif '9th' in cpu or '9' in gen: cpuGen = 9
        elif '8th' in cpu or '8' in gen: cpuGen = 8
        elif '7th' in cpu or '7' in gen: cpuGen = 7
        elif '6th' in cpu or '6' in gen: cpuGen = 6
        elif '4th' in cpu or '4' in gen: cpuGen = 4
        elif '5y71' in cpu.lower(): cpuGen = 5
        else: cpuGen = 10
        
    # 5. gpuCategory & isDedicatedGpu
    if cpuBrand == 'Apple':
        gpuCategory = 'apple'
        isDedicatedGpu = False
    elif any(d in gpu.lower() for d in ['geforce', 'nvidia', 'rtx', 'gtx', 'radeon rx vega m']):
        gpuCategory = 'dedicated'
        isDedicatedGpu = True
    else:
        gpuCategory = 'integrated'
        isDedicatedGpu = False
        
    # 6. upgradability
    soldered = any(s in series or s in name for s in non_upgradable_series) or (brand == 'apple')
    isRamUpgradable = not soldered
    
    if isRamUpgradable:
        ramUpgradeOptions = sorted(list(set([ramGb, 16, 32])))
    else:
        ramUpgradeOptions = [ramGb]
        
    storageUpgradeOptions = sorted(list(set([storageGb, 512, 1000])))
    
    # Update laptop object with structured normalized fields
    lap['ramGb'] = ramGb
    lap['storageGb'] = storageGb
    lap['storageType'] = storageType
    lap['cpuBrand'] = cpuBrand
    lap['cpuTier'] = cpuTier
    lap['cpuGen'] = cpuGen
    lap['gpuCategory'] = gpuCategory
    lap['isDedicatedGpu'] = isDedicatedGpu
    lap['gpuModel'] = gpu
    lap['isRamUpgradable'] = isRamUpgradable
    lap['ramUpgradeOptions'] = ramUpgradeOptions
    lap['storageUpgradeOptions'] = storageUpgradeOptions

# Write back to laptops-data.js
js_content = f"// Complete {len(laptops)}-Laptop Real Inventory Dataset\nconst LAPTOPS_INVENTORY = {json.dumps(laptops, indent=2)};\n\nif (typeof module !== 'undefined') module.exports = LAPTOPS_INVENTORY;\n"

with open(DATA_JS_PATH, 'w', encoding='utf-8') as f:
    f.write(js_content)

print(f"Successfully normalized and saved {len(laptops)} laptops to {DATA_JS_PATH}!")
