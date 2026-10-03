import sys
import os
import json
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from server import load_inventory

laptops = load_inventory()
with open('scripts/all_laptops_dump.json', 'w', encoding='utf-8') as f:
    json.dump([{
        'id': l['id'],
        'brand': l['brand'],
        'name': l['name'],
        'cpu': l.get('cpu', ''),
        'ram': l.get('ram', 0),
        'storage': l.get('storage', 0),
        'gpu': l.get('gpu', ''),
        'price': l.get('price', 0),
        'badge': l.get('badge', '')
    } for l in laptops], f, indent=2)

print(f"Dumped {len(laptops)} laptops to scripts/all_laptops_dump.json")
