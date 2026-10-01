import json
import os
import re
from PIL import Image

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_JS = os.path.join(BASE_DIR, 'laptops-data.js')

with open(DATA_JS, 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'const\s+LAPTOPS_INVENTORY\s*=\s*(\[\s*\{.*\}\s*\]);', text, re.DOTALL)
if not m:
    m = re.search(r'LAPTOPS_INVENTORY\s*=\s*(\[.*?\])\s*;?\s*$', text, re.DOTALL)

data = json.loads(m.group(1))

results = []

for lap in data:
    img_path = os.path.join(BASE_DIR, lap['img'])
    if not os.path.exists(img_path):
        results.append({'id': lap['id'], 'name': lap['name'], 'error': 'not found'})
        continue

    with Image.open(img_path) as im:
        w, h = im.size
        im_rgb = im.convert('RGB')
        
        # Sample edge border (outer 4-6 pixels)
        edge_pixels = []
        # top and bottom strips
        for y in range(0, min(5, h)):
            for x in range(0, w, 2):
                edge_pixels.append(im_rgb.getpixel((x, y)))
        for y in range(max(0, h - 5), h):
            for x in range(0, w, 2):
                edge_pixels.append(im_rgb.getpixel((x, y)))
        # left and right strips
        for x in range(0, min(5, w)):
            for y in range(0, h, 2):
                edge_pixels.append(im_rgb.getpixel((x, y)))
        for x in range(max(0, w - 5), w):
            for y in range(0, h, 2):
                edge_pixels.append(im_rgb.getpixel((x, y)))
        
        avg_r = sum(p[0] for p in edge_pixels) / len(edge_pixels)
        avg_g = sum(p[1] for p in edge_pixels) / len(edge_pixels)
        avg_b = sum(p[2] for p in edge_pixels) / len(edge_pixels)
        
        lum = 0.2126 * avg_r + 0.7152 * avg_g + 0.0722 * avg_b
        max_c = max(avg_r, avg_g, avg_b)
        min_c = min(avg_r, avg_g, avg_b)
        sat = (max_c - min_c) / max_c if max_c > 0 else 0
        
        # Classification
        # If very bright and low saturation -> white / near-white
        if lum >= 225 and sat < 0.15:
            tone = 'white'
        elif lum < 70:
            tone = 'dark'
        else:
            tone = 'colorful'
            
        results.append({
            'id': lap['id'],
            'name': lap['name'],
            'brand': lap['brand'],
            'img': lap['img'],
            'size': f'{w}x{h}',
            'lum': round(lum, 1),
            'sat': round(sat, 2),
            'avg_rgb': (round(avg_r), round(avg_g), round(avg_b)),
            'tone': tone
        })

# Print summary
tone_counts = {'white': 0, 'colorful': 0, 'dark': 0}
for r in results:
    tone_counts[r['tone']] += 1

print(f"Total analyzed: {len(results)}")
print(f"Tone counts: {tone_counts}")
print("\nSample items across categories:")
for t in ['white', 'colorful', 'dark']:
    print(f"\n--- {t.upper()} TONE SAMPLES ---")
    items = [r for r in results if r['tone'] == t]
    for it in items[:6]:
        print(f"ID {it['id']:2d} | {it['name']:32s} | RGB={it['avg_rgb']} | lum={it['lum']} sat={it['sat']}")
