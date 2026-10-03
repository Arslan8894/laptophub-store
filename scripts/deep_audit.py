import os
import re
import sys
import json
sys.stdout.reconfigure(encoding='utf-8')

def check_all():
    print("=== DEEP AUDIT OF LAPTOP STORE CODEBASE ===")
    
    # -------------------------------------------------------------
    # 1. IMAGE ASSETS AUDIT
    # -------------------------------------------------------------
    print("\n--- 1. Image Assets & Data References ---")
    with open('laptops-data.js', 'r', encoding='utf-8') as f:
        data_text = f.read()
    
    # Extract all img: "..." and processedImg: "..."
    img_matches = re.findall(r'"img":\s*"([^"]+)"', data_text)
    proc_matches = re.findall(r'"processedImg":\s*"([^"]+)"', data_text)
    print(f"Total inventory items checked: {len(img_matches)}")
    missing_imgs = [img for img in img_matches if not os.path.exists(img)]
    missing_proc = [p for p in proc_matches if not os.path.exists(p)]
    print(f"Missing primary images: {len(missing_imgs)} -> {missing_imgs}")
    print(f"Missing processed images: {len(missing_proc)} -> {missing_proc}")

    # Check images referenced in HTML
    for html_file in ['laptophub.html', 'product.html', 'consult.html', 'inventory.html', 'admin/index.html']:
        if not os.path.exists(html_file): continue
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        raw_imgs = re.findall(r'src=["\'](images/[^"\']+)["\']', content)
        for ri in raw_imgs:
            if not os.path.exists(ri):
                print(f"[{html_file}] Missing direct image reference: {ri}")

    # -------------------------------------------------------------
    # 2. JAVASCRIPT & LOGIC AUDIT
    # -------------------------------------------------------------
    print("\n--- 2. JS / Logic Audit ---")
    # Check consult.html
    if os.path.exists('consult.html'):
        with open('consult.html', 'r', encoding='utf-8') as f:
            c_text = f.read()
        # Check if consult has COD references
        cod_in_consult = re.findall(r'\b(?:cash\s+on\s+delivery|cod)\b', c_text, re.I)
        print(f"consult.html: COD references = {len(cod_in_consult)}")
        # Check if consult links to modal or product.html
        if 'openLaptopModal' in c_text:
            print("consult.html: calls openLaptopModal (should be product.html?id=ID)")
        if 'product.html' in c_text:
            print("consult.html: links to product.html")

    # Check product.html edge cases
    with open('product.html', 'r', encoding='utf-8') as f:
        p_text = f.read()
    
    # Check undefined vars or handlers in product.html
    onclicks = re.findall(r'onclick=["\']([a-zA-Z0-9_]+)\(', p_text)
    for fn in set(onclicks):
        if f'function {fn}' not in p_text and f'{fn} =' not in p_text and fn not in ['switchAuthTab']:
            # Check if in store-config.js
            with open('store-config.js', 'r', encoding='utf-8') as sc:
                sc_text = sc.read()
            if f'function {fn}' not in sc_text:
                print(f"product.html: Potentially undefined handler called by onclick: {fn}()")

    # Check laptophub.html onclick handlers
    with open('laptophub.html', 'r', encoding='utf-8') as f:
        l_text = f.read()
    onclicks_lh = re.findall(r'onclick=["\']([a-zA-Z0-9_]+)\(', l_text)
    for fn in set(onclicks_lh):
        if f'function {fn}' not in l_text and f'{fn} =' not in l_text and fn not in ['switchAuthTab']:
            with open('store-config.js', 'r', encoding='utf-8') as sc:
                sc_text = sc.read()
            if f'function {fn}' not in sc_text:
                print(f"laptophub.html: Potentially undefined handler called by onclick: {fn}()")

    # -------------------------------------------------------------
    # 3. CSS & RESPONSIVENESS AUDIT
    # -------------------------------------------------------------
    print("\n--- 3. CSS & Responsiveness Audit ---")
    css_files = ['css/header.css', 'css/product.css', 'css/theme.css']
    for cf in css_files:
        with open(cf, 'r', encoding='utf-8') as f:
            css = f.read()
        print(f"{cf}: {len(css.splitlines())} lines, {len(css)} bytes")
        # Check media queries
        mqs = re.findall(r'@media[^{]+', css)
        print(f"  Media queries in {cf}: {len(mqs)}")
        for m in mqs:
            print(f"    {m.strip()}")

    # -------------------------------------------------------------
    # 4. SERVER.PY SECURITY AUDIT
    # -------------------------------------------------------------
    print("\n--- 4. Server & Backend Security ---")
    with open('server.py', 'r', encoding='utf-8') as f:
        srv_text = f.read()
    endpoints = re.findall(r'path == [\'"]([^\'"]+)[\'"]', srv_text)
    print(f"Total API endpoints in server.py: {len(endpoints)}")
    for ep in sorted(set(endpoints)):
        print(f"  {ep}")

if __name__ == '__main__':
    check_all()
