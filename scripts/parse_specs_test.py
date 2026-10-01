import json
import re

with open('laptops-data.js', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'const\s+LAPTOPS_INVENTORY\s*=\s*(\[.*?\]);', text, re.DOTALL)
data = json.loads(m.group(1))

print(f"Total laptops: {len(data)}")

for lap in data:
    cpu = lap.get('cpu', '')
    gpu = lap.get('gpu', '')
    gpuType = lap.get('gpuType', '')
    brand = lap.get('brand', '')
    
    # Check CPU details
    print(f"[{lap['id']:02d}] {lap['name']} | CPU: {cpu} | GPU: {gpu} ({gpuType})")
