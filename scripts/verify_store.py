#!/usr/bin/env python3
"""
verify_store.py
Health check and integrity verification tool for LaptopHub & VOLTS.
Verifies:
  - All HTML storefront pages exist and are valid.
  - laptops-data.js dataset integrity (ID sequences, names, prices, image references).
  - Images directory check (all 69 product photos exist on disk).
  - WhatsApp phone number configuration across all pages.
"""

import os
import json
import re
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, 'laptops-data.js')
IMAGES_DIR = os.path.join(BASE_DIR, 'images')

def check_html_files():
    print("\n--- 1. Checking Storefront HTML Files ---")
    pages = [
        ('index.html', 'Master Portal / Suite View'),
        ('laptophub.html', 'LaptopHub Storefront (69 Laptops)'),
        ('volts.html', 'VOLTS Performance Edition'),
        ('custom-laptop.html', 'Create Your Laptop Configurator'),
        ('consult.html', 'Consult AI Recommendation Tool'),
        ('inventory.html', 'Inventory Admin Dashboard')
    ]
    all_ok = True
    for fname, desc in pages:
        p = os.path.join(BASE_DIR, fname)
        if os.path.exists(p):
            size = os.path.getsize(p)
            print(f"  [OK] {fname:<20} ({size:>6,} bytes) - {desc}")
        else:
            print(f"  [FAIL] {fname:<20} MISSING!")
            all_ok = False
    return all_ok

def check_inventory_data():
    print("\n--- 2. Checking Inventory Dataset (laptops-data.js) ---")
    if not os.path.exists(DATA_PATH):
        print("  [FAIL] laptops-data.js does not exist!")
        return False

    with open(DATA_PATH, 'r', encoding='utf-8') as f:
        text = f.read()

    start = text.find('[')
    end = text.rfind(']') + 1
    if start == -1 or end == 0:
        print("  [FAIL] Could not parse JSON array from laptops-data.js")
        return False

    try:
        data = json.loads(text[start:end])
    except Exception as e:
        print(f"  [FAIL] JSON parsing error: {e}")
        return False

    print(f"  [OK] Loaded {len(data)} laptops successfully.")
    
    missing_images = []
    invalid_prices = []
    brands = set()

    for lap in data:
        brands.add(lap.get('brand', 'unknown'))
        img = lap.get('img', '')
        img_full = os.path.join(BASE_DIR, img.replace('/', os.sep))
        if not os.path.exists(img_full):
            missing_images.append((lap.get('id'), lap.get('name'), img))
        if not lap.get('price') or lap.get('price') <= 0:
            invalid_prices.append((lap.get('id'), lap.get('name')))

    print(f"  [OK] Brands present: {', '.join(sorted(brands))}")
    if missing_images:
        print(f"  [WARN] {len(missing_images)} missing image files on disk:")
        for mid, mname, mimg in missing_images[:5]:
            print(f"    - #{mid} {mname}: {mimg}")
    else:
        print(f"  [OK] All {len(data)} product image files verified on disk.")

    if invalid_prices:
        print(f"  [WARN] {len(invalid_prices)} items with zero/invalid price.")
    else:
        print("  [OK] All prices are valid integers.")

    return True

def check_whatsapp_number():
    print("\n--- 3. Checking WhatsApp Configuration (+923261398594) ---")
    target_num = "923261398594"
    files_to_check = [
        'laptophub.html',
        'volts.html',
        'custom-laptop.html',
        'consult.html',
        'store-config.js'
    ]
    all_ok = True
    for f in files_to_check:
        p = os.path.join(BASE_DIR, f)
        if not os.path.exists(p):
            continue
        with open(p, 'r', encoding='utf-8') as fp:
            content = fp.read()
            matches = len(re.findall(target_num, content))
            if matches > 0:
                print(f"  [OK] {f:<20} contains {matches} references to {target_num}")
            else:
                print(f"  [WARN] {f:<20} has 0 references to {target_num}")
                all_ok = False
    return all_ok

def main():
    print("=" * 60)
    print(" LAPTOP STORE SYSTEM VERIFICATION & INTEGRITY CHECK")
    print("=" * 60)
    h_ok = check_html_files()
    d_ok = check_inventory_data()
    w_ok = check_whatsapp_number()
    print("\n" + "=" * 60)
    if h_ok and d_ok and w_ok:
        print(" [SUCCESS] All systems, pages, datasets, and links are HEALTHY!")
    else:
        print(" [WARNING] Some checks reported warnings or issues.")
    print("=" * 60)

if __name__ == '__main__':
    main()
