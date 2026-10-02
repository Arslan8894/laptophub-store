import re
import json

with open('laptops-data.js', 'r', encoding='utf-8') as f:
    content = f.read()

m = re.search(r'const LAPTOPS_INVENTORY = (\[.*?\]);', content, re.DOTALL)
if m:
    data = json.loads(m.group(1))
    ddr4 = []
    ddr5 = []
    soldered = []

    for l in data:
        lid = l.get('id')
        name = l.get('name')
        base_ram = l.get('ramGb', l.get('ram'))
        mem = l.get('fullSpecs', {}).get('memoryStorage', {})
        ram_type = mem.get('ramType', 'DDR4')
        slots = mem.get('ramSlots', '')
        upgradable = l.get('isRamUpgradable', True)

        is_soldered = (
            ('soldered' in slots.lower() and 'upgradable' not in slots.lower())
            or ('non-upgradable' in slots.lower())
            or (not upgradable)
            or ('lpddr' in ram_type.lower())
            or ('unified' in ram_type.lower())
        )
        is_ddr5 = ('ddr5' in ram_type.lower()) and not is_soldered

        item = {
            'id': lid,
            'name': name,
            'baseRam': base_ram,
            'ramType': ram_type,
            'slots': slots
        }

        if is_soldered:
            soldered.append(item)
        elif is_ddr5:
            ddr5.append(item)
        else:
            ddr4.append(item)

    print(f"Total Laptops: {len(data)}")
    print(f"DDR4 Upgradable Count: {len(ddr4)}")
    print(f"DDR5 Upgradable Count: {len(ddr5)}")
    print(f"Soldered / Non-Upgradable Count: {len(soldered)}")

    print("\n================== DDR5 MODELS ==================")
    for x in ddr5:
        print(f"• ID #{x['id']}: {x['name']} (Base: {x['baseRam']}GB | {x['ramType']} | {x['slots']})")

    print("\n========== SOLDERED / NON-UPGRADABLE MODELS ==========")
    for x in soldered:
        print(f"• ID #{x['id']}: {x['name']} (Base: {x['baseRam']}GB | {x['ramType']} | {x['slots']})")
