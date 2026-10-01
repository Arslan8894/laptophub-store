import json

with open("laptops-data.js", "r", encoding="utf-8") as f:
    text = f.read()

start = text.find("[")
end = text.rfind("]") + 1
laptops = json.loads(text[start:end])

print(f"Total laptops: {len(laptops)}")
print("-" * 80)

ddr4_upgradable = []
ddr5_upgradable = []
soldered_or_fixed = []

for l in laptops:
    mem = l.get("fullSpecs", {}).get("memoryStorage", {})
    ram_type = mem.get("ramType", "").strip().upper()
    ram_slots = str(mem.get("ramSlots", "")).strip()
    is_up = l.get("isRamUpgradable", True)

    # If isRamUpgradable is False or ramSlots says soldered/non-upgradable
    # Note: check if 1 soldered + 1 so-dimm slot (upgradable)
    is_soldered_fixed = (
        not is_up 
        or "non-upgradable" in ram_slots.lower() 
        or "soldered dual-channel" in ram_slots.lower()
        or ("soldered" in ram_slots.lower() and "upgradable" not in ram_slots.lower())
        or "unified memory" in ram_type.lower()
    )

    if is_soldered_fixed:
        soldered_or_fixed.append((l["id"], l["name"], l.get("ram", 0), ram_type, ram_slots))
    elif "DDR5" in ram_type:
        ddr5_upgradable.append((l["id"], l["name"], l.get("ram", 0), ram_type, ram_slots))
    else:
        ddr4_upgradable.append((l["id"], l["name"], l.get("ram", 0), ram_type, ram_slots))

print(f"\n=== DDR4 UPGRADABLE ({len(ddr4_upgradable)}) ===")
for item in ddr4_upgradable:
    print(f"ID {item[0]:2d}: {item[1]:<35} | Base: {item[2]}GB | {item[3]:<10} | {item[4]}")

print(f"\n=== DDR5 UPGRADABLE ({len(ddr5_upgradable)}) ===")
for item in ddr5_upgradable:
    print(f"ID {item[0]:2d}: {item[1]:<35} | Base: {item[2]}GB | {item[3]:<10} | {item[4]}")

print(f"\n=== SOLDERED / NON-UPGRADABLE ({len(soldered_or_fixed)}) ===")
for item in soldered_or_fixed:
    print(f"ID {item[0]:2d}: {item[1]:<35} | Base: {item[2]}GB | {item[3]:<10} | {item[4]}")
