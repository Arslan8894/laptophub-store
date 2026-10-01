"""
retrieve_all_laptop_images.py
Retrieves genuine, high-resolution product photos from the internet for all laptops in the inventory.
Validates downloaded images (magic bytes, file size > 15KB) and updates laptops-data.js.
"""

import urllib.request
import urllib.parse
import json
import re
import os
import time

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGES_DIR = os.path.join(BASE_DIR, 'images')
DATA_JS_PATH = os.path.join(BASE_DIR, 'laptops-data.js')

os.makedirs(IMAGES_DIR, exist_ok=True)

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.9',
}

IMG_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
    'Referer': 'https://www.bing.com/',
}

def slugify(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9]+', '-', text)
    return text.strip('-')

def search_bing_images(query):
    q = urllib.parse.quote(query)
    url = f'https://www.bing.com/images/search?q={q}&form=HDRSC2&first=1'
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=12) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
        murls = re.findall(r'murl&quot;:&quot;(https?://[^&]+)&quot;', html)
        if not murls:
            murls = re.findall(r'"murl":"(https?://[^"]+)"', html)
        return murls
    except Exception as e:
        print(f"    [Search Error]: {e}")
        return []

def download_image(url_list, dest_path, min_kb=15):
    for u in url_list[:8]:
        # Filter out bad domains or SVG/ICO if present in URL
        if any(bad in u.lower() for bad in ['.svg', '.ico', 'favicon', 'logo-']):
            continue
        try:
            req = urllib.request.Request(u, headers=IMG_HEADERS)
            with urllib.request.urlopen(req, timeout=10) as r:
                data = r.read()
                # Verify valid image header
                is_jpg = data[:3] == b'\xff\xd8\xff'
                is_png = data[:8] == b'\x89PNG\r\n\x1a\n'
                is_webp = data[:4] == b'RIFF' and data[8:12] == b'WEBP'
                
                if (is_jpg or is_png or is_webp) and len(data) >= min_kb * 1024:
                    with open(dest_path, 'wb') as f:
                        f.write(data)
                    return True, len(data), u
        except Exception:
            continue
    return False, 0, None

def main():
    print("="*65)
    print("  RETRIEVING PRODUCT PHOTOS FOR ALL LAPTOPS FROM THE INTERNET")
    print("="*65)
    
    with open(DATA_JS_PATH, 'r', encoding='utf-8') as f:
        js_raw = f.read()
    
    start = js_raw.find('[')
    end = js_raw.rfind(']') + 1
    laptops = json.loads(js_raw[start:end])
    
    print(f"Loaded {len(laptops)} laptops from laptops-data.js\n")
    
    updated_count = 0
    skipped_count = 0
    failed_count = 0
    
    for item in laptops:
        lid = item['id']
        name = item['name']
        brand = item['brandName']
        series = item.get('series', '')
        current_img = item.get('img', '')
        
        # Build clean filename
        name_slug = slugify(f"{brand}-{series}-{lid}")
        filename = f"laptop-{lid}-{name_slug}.jpg"
        dest_path = os.path.join(IMAGES_DIR, filename)
        rel_img_path = f"images/{filename}"
        
        # If destination file already exists and is >20KB, we can use it
        if os.path.exists(dest_path) and os.path.getsize(dest_path) > 20 * 1024:
            print(f"[{lid:02d}/69] {name[:36]:<36} -> Exists ({os.path.getsize(dest_path)//1024} KB)")
            item['img'] = rel_img_path
            skipped_count += 1
            continue
            
        # Specific search queries tailored for clean product catalog photography
        query = f"{brand} {series} laptop product white background"
        if 'Surface' in name or 'Surface' in series:
            query = f"{name} official product photo"
        elif 'MacBook' in name:
            query = f"{name} laptop apple product"
        elif 'Alienware' in name:
            query = f"Dell Alienware M15 R7 gaming laptop product photo"
        elif 'Yoga' in name:
            query = f"Lenovo {series} laptop product photo"
        elif 'Spectre' in name:
            query = f"HP {series} laptop product photo"
            
        print(f"[{lid:02d}/69] Fetching photo for: {name[:36]}...")
        urls = search_bing_images(query)
        
        # Fallback query if no urls
        if not urls:
            time.sleep(0.5)
            urls = search_bing_images(f"{brand} {name} laptop")
            
        ok, size, src = download_image(urls, dest_path)
        if ok:
            print(f"       -> Saved {filename} ({size//1024} KB)")
            item['img'] = rel_img_path
            updated_count += 1
        else:
            print(f"       -> [FAILED] Could not download photo for {name}")
            failed_count += 1
            
        time.sleep(0.4) # Polite delay
        
    print("\n" + "="*65)
    print(f"  DOWNLOAD COMPLETE: {updated_count} New | {skipped_count} Cached | {failed_count} Failed")
    print("="*65)
    
    # Save back to laptops-data.js
    new_js = f"// Complete {len(laptops)}-Laptop Real Inventory Dataset\nconst LAPTOPS_INVENTORY = {json.dumps(laptops, indent=2)};\n\nif (typeof module !== 'undefined') module.exports = LAPTOPS_INVENTORY;\n"
    with open(DATA_JS_PATH, 'w', encoding='utf-8') as f:
        f.write(new_js)
    print(f"\nSuccessfully updated {DATA_JS_PATH}!")

if __name__ == '__main__':
    main()
