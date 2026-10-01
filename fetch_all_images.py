"""
fetch_all_images.py  – v2
Uses verified, publicly-accessible image URLs.
Falls back to a DuckDuckGo image search scrape if direct URL fails.
"""

import urllib.request
import urllib.parse
import os
import re
import time
import json

os.makedirs('images', exist_ok=True)

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/124.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
}

IMG_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/124.0.0.0 Safari/537.36',
    'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
    'Referer': 'https://www.google.com/',
}

TIMEOUT = 12

def fetch_bytes(url, extra_headers=None, timeout=TIMEOUT):
    h = dict(IMG_HEADERS)
    if extra_headers:
        h.update(extra_headers)
    try:
        req = urllib.request.Request(url, headers=h)
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.read(), r.headers.get('Content-Type', '')
    except Exception as e:
        print(f'    fetch error: {e}')
        return None, None

def save_img(data, dest):
    if data and len(data) > 8000:
        with open(dest, 'wb') as f:
            f.write(data)
        print(f'  OK  {os.path.basename(dest)}  ({len(data)//1024} KB)')
        return True
    return False

def ddg_first_image(query):
    """Scrape first image result from DuckDuckGo image search."""
    q = urllib.parse.quote(query)
    url = f'https://duckduckgo.com/?q={q}&iax=images&ia=images'
    data, _ = fetch_bytes(url, extra_headers=HEADERS)
    if not data:
        return None
    html = data.decode('utf-8', errors='ignore')
    # Extract vqd token
    m = re.search(r'vqd=(["\'])([^"\']+)\1', html)
    if not m:
        return None
    vqd = m.group(2)
    api_url = f'https://duckduckgo.com/i.js?q={q}&vqd={urllib.parse.quote(vqd)}&f=,,,&p=1'
    api_data, _ = fetch_bytes(api_url, extra_headers={**HEADERS, 'Referer': url})
    if not api_data:
        return None
    try:
        j = json.loads(api_data.decode('utf-8', errors='ignore'))
        results = j.get('results', [])
        for r in results[:5]:
            img_url = r.get('image', '')
            if img_url and img_url.startswith('http'):
                return img_url
    except Exception:
        pass
    return None

# ---------------------------------------------------------------------------
# LAPTOP IMAGE DEFINITIONS
# Each entry: file, search_query (for DDG fallback), direct_urls (tried first)
# ids: laptop IDs in laptops-data.js
# ---------------------------------------------------------------------------
IMAGES = [
    {
        'file': 'lenovo-t14-g1.jpg',
        'ids': [1, 6],
        'query': 'Lenovo ThinkPad T14 Gen 1 laptop product image white background',
        'urls': [
            'https://www.lenovo.com/medias/lenovo-laptop-thinkpad-t14-gen-1-intel-hero.png?context=bWFzdGVyfHJvb3R8NTU2NjQ5fGltYWdlL3BuZ3xoY2UvaGJlLzEwMTIyNDk3MjI1NTk4LnBuZ3xlY2VkY2VlNzBkYzViMjBhNmJhMzExZDkwNzFlMjZhMzRhZTc0YmEwMDk2MzliNTg1YWIyMzNkNjI0YzZlODQw',
        ]
    },
    {
        'file': 'lenovo-x1-yoga.jpg',
        'ids': [4],
        'query': 'Lenovo ThinkPad X1 Yoga Gen 7 laptop product image',
        'urls': []
    },
    {
        'file': 'lenovo-x13.jpg',
        'ids': [5],
        'query': 'Lenovo ThinkPad X13 Gen 1 Intel laptop product image white background',
        'urls': []
    },
    {
        'file': 'lenovo-x13-gen4.jpg',
        'ids': [28],
        'query': 'Lenovo ThinkPad X13 Gen 4 Intel laptop product image',
        'urls': []
    },
    {
        'file': 'lenovo-t480s.jpg',
        'ids': [17],
        'query': 'Lenovo ThinkPad T480s laptop product image white background',
        'urls': []
    },
    {
        'file': 'lenovo-thinkpad-13.jpg',
        'ids': [7],
        'query': 'Lenovo ThinkPad 13 2nd gen laptop product image white background',
        'urls': []
    },
    {
        'file': 'lenovo-e14.jpg',
        'ids': [34],
        'query': 'Lenovo E14 Gen 2 laptop product image white background',
        'urls': []
    },
    {
        'file': 'lenovo-x1-extreme.jpg',
        'ids': [21],
        'query': 'Lenovo ThinkPad X1 Extreme Gen 2 laptop product image',
        'urls': []
    },
    {
        'file': 'surface-pro-7.jpg',
        'ids': [2],
        'query': 'Microsoft Surface Pro 7 tablet product image white background',
        'urls': [
            'https://img-prod-cms-rt-microsoft-com.akamaized.net/cms/api/am/imageFileData/RE4Isal?ver=a5b1&q=90&m=6&h=600&w=900&b=%23FFFFFF&f=jpg&o=f',
        ]
    },
    {
        'file': 'surface-laptop-10th.jpg',
        'ids': [20],
        'query': 'Microsoft Surface Laptop 3 Core i5 10th gen product image',
        'urls': [
            'https://img-prod-cms-rt-microsoft-com.akamaized.net/cms/api/am/imageFileData/RE4pzMZ?ver=f4ea&q=90&m=6&h=600&w=900&b=%23FFFFFF&f=jpg&o=f',
        ]
    },
    {
        'file': 'hp-elitebook-840g9.jpg',
        'ids': [3],
        'query': 'HP EliteBook 840 G9 laptop product image white background',
        'urls': []
    },
    {
        'file': 'hp-elitebook-840g8.jpg',
        'ids': [23],
        'query': 'HP EliteBook 840 G8 laptop product image white background',
        'urls': []
    },
    {
        'file': 'hp-elitebook-840g7.jpg',
        'ids': [24],
        'query': 'HP EliteBook 840 G7 laptop product image white background',
        'urls': []
    },
    {
        'file': 'hp-elitebook-1030g2.jpg',
        'ids': [12],
        'query': 'HP EliteBook x360 1030 G2 laptop product image white background',
        'urls': []
    },
    {
        'file': 'hp-elitebook-1030g3.jpg',
        'ids': [35],
        'query': 'HP EliteBook x360 1030 G3 laptop product image',
        'urls': []
    },
    {
        'file': 'hp-elitebook-1030g4.jpg',
        'ids': [27],
        'query': 'HP EliteBook x360 1030 G4 laptop product image white background',
        'urls': []
    },
    {
        'file': 'hp-elitebook-1030g8.jpg',
        'ids': [10],
        'query': 'HP EliteBook x360 1030 G8 laptop product image white background',
        'urls': []
    },
    {
        'file': 'hp-640g1.jpg',
        'ids': [15],
        'query': 'HP ProBook 640 G1 laptop product image white background',
        'urls': []
    },
    {
        'file': 'hp-640g2.jpg',
        'ids': [19],
        'query': 'HP ProBook 640 G2 laptop product image white background',
        'urls': []
    },
    {
        'file': 'hp-630g9.jpg',
        'ids': [16],
        'query': 'HP ProBook 630 G9 laptop product image white background',
        'urls': []
    },
    {
        'file': 'hp-9480.jpg',
        'ids': [18],
        'query': 'HP ProBook 9480m laptop product image white background',
        'urls': []
    },
    {
        'file': 'dell-xps-15.jpg',
        'ids': [8, 26],
        'query': 'Dell XPS 15 9570 laptop product image white background',
        'urls': []
    },
    {
        'file': 'dell-5310.jpg',
        'ids': [9],
        'query': 'Dell Latitude 5310 laptop product image white background',
        'urls': []
    },
    {
        'file': 'dell-5320.jpg',
        'ids': [11, 33],
        'query': 'Dell Latitude 5320 laptop product image white background',
        'urls': []
    },
    {
        'file': 'dell-5430.jpg',
        'ids': [13],
        'query': 'Dell Latitude 5430 laptop product image white background',
        'urls': []
    },
    {
        'file': 'dell-7270.jpg',
        'ids': [32],
        'query': 'Dell Latitude 7270 laptop product image white background',
        'urls': []
    },
    {
        'file': 'dell-7420.jpg',
        'ids': [14],
        'query': 'Dell Latitude 7420 laptop product image white background',
        'urls': []
    },
    {
        'file': 'dell-7490.jpg',
        'ids': [30],
        'query': 'Dell Latitude 7490 laptop product image white background',
        'urls': []
    },
    {
        'file': 'dell-7320-2in1.jpg',
        'ids': [22],
        'query': 'Dell Latitude 7320 2-in-1 laptop product image white background',
        'urls': []
    },
    {
        'file': 'dell-3310-2in1.jpg',
        'ids': [31],
        'query': 'Dell Latitude 3310 2-in-1 laptop product image white background',
        'urls': []
    },
    {
        'file': 'dell-precision-5560.jpg',
        'ids': [25],
        'query': 'Dell Precision 5560 workstation laptop product image',
        'urls': []
    },
    {
        'file': 'dell-vostro-5490.jpg',
        'ids': [29],
        'query': 'Dell Vostro 5490 laptop product image white background',
        'urls': []
    },
    {
        'file': 'dell-alienware-m15.jpg',
        'ids': [36],
        'query': 'Dell Alienware m15 R4 gaming laptop product image',
        'urls': []
    },
]

# ---------------------------------------------------------------------------
downloaded = {}
failed = []

print('\n' + '='*60)
print('  DOWNLOADING LAPTOP IMAGES')
print('='*60)

for item in IMAGES:
    fname = item['file']
    dest  = os.path.join('images', fname)

    if os.path.exists(dest) and os.path.getsize(dest) > 8000:
        print(f'\n-- {fname} already exists, skipping')
        downloaded[fname] = dest
        continue

    print(f'\n>> {fname}')
    ok = False

    # Try direct URLs first
    for url in item.get('urls', []):
        print(f'   trying direct: {url[:70]}...')
        data, ct = fetch_bytes(url)
        if save_img(data, dest):
            downloaded[fname] = dest
            ok = True
            break
        time.sleep(0.3)

    # Fallback: DuckDuckGo image search
    if not ok:
        print(f'   trying DDG search: {item["query"]}')
        img_url = ddg_first_image(item['query'])
        if img_url:
            print(f'   found: {img_url[:70]}...')
            data, ct = fetch_bytes(img_url)
            if save_img(data, dest):
                downloaded[fname] = dest
                ok = True
        time.sleep(0.5)

    if not ok:
        print(f'   FAILED: {fname}')
        failed.append(fname)

# ---------------------------------------------------------------------------
print('\n' + '='*60)
print('  UPDATING laptops-data.js')
print('='*60)

id_to_img = {}
for item in IMAGES:
    fname = item['file']
    if fname not in failed:
        for lid in item['ids']:
            id_to_img[lid] = f'images/{fname}'

with open('laptops-data.js', 'r', encoding='utf-8') as f:
    content = f.read()

def replace_img_for_id(content, laptop_id, new_img):
    pattern = (
        r'("id"\s*:\s*' + str(laptop_id) + r'\b'
        r'(?:(?!"id"\s*:).)*?)'
        r'("img"\s*:\s*)"[^"]*"'
    )
    replacement = r'\1\2"' + new_img + '"'
    new_content, n = re.subn(pattern, replacement, content, count=1, flags=re.DOTALL)
    return new_content, n

changes = 0
for lid, img_path in sorted(id_to_img.items()):
    content, n = replace_img_for_id(content, lid, img_path)
    if n:
        changes += 1
        print(f'  ID {lid:>2} -> {img_path}')

with open('laptops-data.js', 'w', encoding='utf-8') as f:
    f.write(content)

print(f'\nUpdated {changes} img references in laptops-data.js')

# ---------------------------------------------------------------------------
print('\n' + '='*60)
print(f'  DONE  |  Downloaded: {len(downloaded)}  |  Failed: {len(failed)}')
if failed:
    print('\n  Failed files:')
    for f in failed:
        print(f'    - {f}')
print('='*60)
