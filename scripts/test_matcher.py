import json
import re

with open('laptops-data.js', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'const\s+LAPTOPS_INVENTORY\s*=\s*(\[.*?\]);', text, re.DOTALL)
laptops = json.loads(m.group(1))

def calculate_upgrade_cost(lap, target_ram, target_storage):
    ram_cost = 0
    base_ram = lap.get('ramGb', lap.get('ram', 16))
    if base_ram < target_ram:
        if not lap.get('isRamUpgradable', True):
            return None, "RAM not upgradable"
        if base_ram == 8 and target_ram == 16: ram_cost = 6000
        elif base_ram == 16 and target_ram == 32: ram_cost = 14000
        elif base_ram == 8 and target_ram == 32: ram_cost = 20000
        elif target_ram == 64: ram_cost = 35000
        else: ram_cost = 10000
        
    storage_cost = 0
    base_storage = lap.get('storageGb', lap.get('storage', 512))
    if base_storage < target_storage:
        if base_storage == 256 and target_storage == 512: storage_cost = 2000
        elif base_storage == 512 and target_storage == 1000: storage_cost = 12000
        elif base_storage == 256 and target_storage == 1000: storage_cost = 14000
        elif target_storage == 2000: storage_cost = 25000
        else: storage_cost = 12000
        
    final_price = lap['price'] + ram_cost + storage_cost
    return {
        'ram_cost': ram_cost,
        'storage_cost': storage_cost,
        'final_price': final_price,
        'needed_ram_upgrade': ram_cost > 0,
        'needed_storage_upgrade': storage_cost > 0
    }, None

def matches_preference(lap, prefs):
    failures = []
    
    # 1. Use case
    uc = prefs.get('usecase')
    if uc and uc != 'any':
        if uc not in lap.get('useCases', []):
            failures.append(f"usecase ({uc} not in {lap.get('useCases')})")
        if uc == 'gaming':
            if not lap.get('isDedicatedGpu'):
                failures.append("gaming requires dedicated GPU")
        elif uc == 'creator':
            if lap.get('ramGb', 16) < 16 and not lap.get('isRamUpgradable'):
                failures.append("creator requires 16GB+ RAM")
        elif uc == 'programming':
            if lap.get('ramGb', 16) < 16 and not lap.get('isRamUpgradable'):
                failures.append("programming requires 16GB+ RAM")
                
    # 2. CPU
    cpu = prefs.get('cpu')
    if cpu and cpu != 'any':
        brand = lap.get('cpuBrand', '')
        tier = lap.get('cpuTier', '')
        tag = lap.get('cpuTag', '')
        if cpu == 'intel_i5':
            if brand != 'Intel' or ('i5' not in tier and 'Ultra 5' not in tier and tag != 'intel_i5'):
                failures.append(f"cpu not i5 ({tier})")
        elif cpu == 'intel_i7':
            if brand != 'Intel' or ('i7' not in tier and 'Ultra 7' not in tier and 'i9' not in tier and tag != 'intel_i7' and tag != 'intel_i9'):
                failures.append(f"cpu not i7 ({tier})")
        elif cpu == 'intel_ultra':
            if 'Ultra' not in tier and tag != 'intel_ultra':
                failures.append(f"cpu not Ultra ({tier})")
        elif cpu == 'amd':
            if brand != 'AMD' and tag != 'amd':
                failures.append(f"cpu not AMD ({brand})")
        elif cpu == 'apple':
            if brand != 'Apple' and tag != 'apple':
                failures.append(f"cpu not Apple ({brand})")
                
    # 3. RAM & Storage Upgrades
    target_ram = prefs.get('ram', 16)
    target_storage = prefs.get('storage', 512)
    upgrade_info, err = calculate_upgrade_cost(lap, target_ram, target_storage)
    if err:
        failures.append(err)
        effective_price = lap['price']
    else:
        effective_price = upgrade_info['final_price']
        
    # 4. GPU
    gpu = prefs.get('gpu')
    if gpu and gpu != 'no_pref':
        is_dedicated = lap.get('isDedicatedGpu', False)
        gpu_cat = lap.get('gpuCategory', '')
        gpu_type = lap.get('gpuType', '')
        gpu_model = lap.get('gpuModel', '').lower()
        if gpu == 'integrated':
            if is_dedicated:
                failures.append("requested integrated, laptop has dedicated")
        elif gpu == 'any_discrete':
            if not is_dedicated:
                failures.append("requested dedicated GPU, laptop has integrated")
        elif gpu == 'rtx':
            if 'rtx' not in gpu_type and 'rtx' not in gpu_model:
                failures.append("requested RTX, laptop does not have RTX")
        elif gpu == 'apple_gpu':
            if gpu_cat != 'apple' and lap.get('brand') != 'apple':
                failures.append("requested Apple GPU, laptop is not Apple")
                
    # 5. Budget
    budget = prefs.get('budget', 130000)
    if effective_price > budget:
        failures.append(f"over budget (Rs {effective_price:,} > Rs {budget:,})")
        
    return len(failures) == 0, failures, effective_price, upgrade_info

print("--- TEST CASES ---")

test_cases = [
    {
        "name": "Case 1: Office, Intel i7, 16GB, 512GB, Integrated, 130k Budget",
        "prefs": {"usecase": "office", "cpu": "intel_i7", "ram": 16, "storage": 512, "gpu": "integrated", "budget": 130000}
    },
    {
        "name": "Case 2: Gaming, Any CPU, 16GB, 512GB, Dedicated GPU, 200k Budget",
        "prefs": {"usecase": "gaming", "cpu": "any", "ram": 16, "storage": 512, "gpu": "any_discrete", "budget": 200000}
    },
    {
        "name": "Case 3: Apple M-Series, 16GB, 512GB, 350k Budget",
        "prefs": {"usecase": "any", "cpu": "apple", "ram": 16, "storage": 512, "gpu": "apple_gpu", "budget": 350000}
    },
    {
        "name": "Case 4: Impossible budget: Gaming RTX with 50k Budget (Zero match expected)",
        "prefs": {"usecase": "gaming", "cpu": "any", "ram": 16, "storage": 512, "gpu": "rtx", "budget": 50000}
    }
]

for tc in test_cases:
    print(f"\n{tc['name']}:")
    matches = []
    for lap in laptops:
        ok, fails, price, upg = matches_preference(lap, tc['prefs'])
        if ok:
            matches.append((lap, price, upg))
    print(f"  Total exact matches: {len(matches)}")
    for lap, price, upg in matches[:5]:
        print(f"    -> ID {lap['id']} ({lap['brand']}): {lap['name']} | Price: Rs {price:,} | CPU: {lap['cpuTier']} | GPU: {lap['gpu']}")
