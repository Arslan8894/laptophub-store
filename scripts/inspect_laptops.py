import json
import re

with open('laptops-data.js', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'const\s+LAPTOPS_INVENTORY\s*=\s*(\[.*?\]);', text, re.DOTALL)
if not m:
    print('Failed to match LAPTOPS_INVENTORY')
    exit(1)

data = json.loads(m.group(1))
print(f'Total laptops: {len(data)}')

gpu_types = set()
cpu_tags = set()
use_cases = set()
brands = set()
for lap in data:
    gpu_types.add(lap.get('gpuType'))
    cpu_tags.add(lap.get('cpuTag'))
    brands.add(lap.get('brand'))
    for u in lap.get('useCases', []):
        use_cases.add(u)

print('Brands:', sorted(list(brands)))
print('GPU types:', sorted(list(str(x) for x in gpu_types)))
print('CPU tags:', sorted(list(str(x) for x in cpu_tags)))
print('Use cases:', sorted(list(use_cases)))

print("\n--- SAMPLE LAPTOPS ---")
for lap in data:
    if lap.get('gpuType') in ['discrete', 'rtx'] or 'apple' in lap.get('brand', ''):
        print(f"ID {lap['id']} ({lap['brand']}): {lap['name']} | CPU: {lap['cpu']} | GPU: {lap['gpu']} ({lap.get('gpuType')}) | RAM: {lap['ram']} | Storage: {lap['storage']} | Price: {lap['price']}")
