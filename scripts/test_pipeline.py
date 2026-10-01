import os
import json
import re
from PIL import Image, ImageDraw, ImageFilter

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.makedirs(os.path.join(BASE_DIR, 'images', 'processed'), exist_ok=True)

DATA_JS = os.path.join(BASE_DIR, 'laptops-data.js')
with open(DATA_JS, 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'const\s+LAPTOPS_INVENTORY\s*=\s*(\[\s*\{.*\}\s*\]);', text, re.DOTALL)
data = json.loads(m.group(1))

for lap in data[:8]:
    img_path = os.path.join(BASE_DIR, lap['img'])
    if not os.path.exists(img_path):
        continue
    im = Image.open(img_path).convert('RGB')
    w, h = im.size
    gray = im.convert('L')
    bin_img = gray.point(lambda p: 255 if p >= 244 else 0)
    
    pix = bin_img.load()
    step_x = max(1, w // 40)
    step_y = max(1, h // 40)
    for x in range(0, w, step_x):
        if pix[x, 0] == 255: ImageDraw.floodfill(bin_img, (x, 0), 128)
        if pix[x, h-1] == 255: ImageDraw.floodfill(bin_img, (x, h-1), 128)
    for y in range(0, h, step_y):
        if pix[0, y] == 255: ImageDraw.floodfill(bin_img, (0, y), 128)
        if pix[w-1, y] == 255: ImageDraw.floodfill(bin_img, (w-1, y), 128)
        
    alpha = bin_img.point(lambda p: 0 if p == 128 else 255)
    hist = alpha.histogram()
    keep_px = sum(hist[1:])
    ratio = keep_px / (w * h)
    
    alpha_smooth = alpha.filter(ImageFilter.GaussianBlur(0.8))
    out_rgba = im.convert('RGBA')
    out_rgba.putalpha(alpha_smooth)
    
    out_name = f"laptop-{lap['id']}-cutout.webp"
    out_path = os.path.join(BASE_DIR, 'images', 'processed', out_name)
    out_rgba.save(out_path, 'WEBP', quality=90)
    print(f"ID {lap['id']} | {lap['name']} | Keep ratio: {ratio*100:.1f}% | Saved: {out_name}")
