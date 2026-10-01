import os
import json
import re
from PIL import Image, ImageDraw, ImageFilter

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_JS = os.path.join(BASE_DIR, 'laptops-data.js')

with open(DATA_JS, 'r', encoding='utf-8') as f:
    text = f.read()
m = re.search(r'const\s+LAPTOPS_INVENTORY\s*=\s*(\[\s*\{.*\}\s*\]);', text, re.DOTALL)
data = json.loads(m.group(1))

laps_by_id = {lap['id']: lap for lap in data}
test_ids = [8, 14, 20, 23, 26, 47, 50, 66]

for tid in test_ids:
    lap = laps_by_id[tid]
    img_path = os.path.join(BASE_DIR, lap['img'])
    im = Image.open(img_path).convert('RGB')
    w, h = im.size
    gray = im.convert('L')
    bin_img = gray.point(lambda p: 255 if p >= 242 else 0)
    
    pix = bin_img.load()
    for x in range(0, w, 15):
        if pix[x, 0] == 255: ImageDraw.floodfill(bin_img, (x, 0), 128)
        if pix[x, h-1] == 255: ImageDraw.floodfill(bin_img, (x, h-1), 128)
    for y in range(0, h, 15):
        if pix[0, y] == 255: ImageDraw.floodfill(bin_img, (0, y), 128)
        if pix[w-1, y] == 255: ImageDraw.floodfill(bin_img, (w-1, y), 128)
        
    alpha = bin_img.point(lambda p: 0 if p == 128 else 255)
    hist = alpha.histogram()
    bg_count = hist[0]
    laptop_count = sum(hist[1:])
    ratio = laptop_count / (w * h)
    name = lap['name']
    print(f"ID {tid:2d} | {name:30s} | {w}x{h} | Laptop area: {ratio*100:4.1f}% | Keep px: {laptop_count}")
