import json
import re

with open('laptops-data.js', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'const\s+LAPTOPS_INVENTORY\s*=\s*(\[.*?\]);', text, re.DOTALL)
laptops = json.loads(m.group(1))

for l in laptops:
    print(f"ID {l['id']}: '{l['name']}' | Brand: {l.get('brand')} | Series: {l.get('series')} | CPU: {l.get('cpu')} | RAM: {l.get('ram')} | Storage: {l.get('storage')} | Display: {l.get('display')} | GPU: {l.get('gpu')}")
