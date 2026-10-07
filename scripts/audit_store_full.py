import os
import re
import glob
import urllib.request
import json

def run_comprehensive_audit():
    print("=" * 70)
    print("      LAPTOPHUB COMPREHENSIVE STORE AUDIT & BUG COLLECTION")
    print("=" * 70)
    
    issues_found = []

    # --------------------------------------------------------------------------
    # 1. AUDIT STATIC ASSETS & FILE REFERENCES
    # --------------------------------------------------------------------------
    print("\n[CHECK 1] Scanning HTML files for broken local asset references...")
    html_files = [f for f in glob.glob('*.html') + glob.glob('admin/*.html') if 'desktop_copies' not in f]
    
    for hf in html_files:
        content = open(hf, encoding='utf-8').read()
        dir_name = os.path.dirname(hf) or '.'
        
        # script src
        scripts = re.findall(r'<script[^>]+src=["\']([^"\']+)["\']', content, re.IGNORECASE)
        for s in scripts:
            if not s.startswith(('http://', 'https://', '//', 'data:')):
                clean_s = s.split('?')[0].split('#')[0]
                full_path = os.path.normpath(os.path.join(dir_name, clean_s))
                if not os.path.exists(full_path):
                    issues_found.append({
                        "category": "Broken Asset Reference",
                        "file": hf,
                        "severity": "HIGH",
                        "description": f"Missing script file: '{s}' (resolved: {full_path})"
                    })

        # stylesheet href
        links = re.findall(r'<link[^>]+href=["\']([^"\']+)["\']', content, re.IGNORECASE)
        for l in links:
            if not l.startswith(('http://', 'https://', '//', 'data:')) and not l.endswith(('.png', '.ico', '.svg', '.json')):
                clean_l = l.split('?')[0].split('#')[0]
                full_path = os.path.normpath(os.path.join(dir_name, clean_l))
                if not os.path.exists(full_path):
                    issues_found.append({
                        "category": "Broken Asset Reference",
                        "file": hf,
                        "severity": "HIGH",
                        "description": f"Missing stylesheet: '{l}' (resolved: {full_path})"
                    })

        # img src
        imgs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', content, re.IGNORECASE)
        for img in imgs:
            if not img.startswith(('http://', 'https://', '//', 'data:', '${')) and img != "":
                clean_img = img.split('?')[0].split('#')[0]
                full_path = os.path.normpath(os.path.join(dir_name, clean_img))
                if not os.path.exists(full_path):
                    issues_found.append({
                        "category": "Broken Image Reference",
                        "file": hf,
                        "severity": "MEDIUM",
                        "description": f"Missing image source: '{img}' (resolved: {full_path})"
                    })

    # --------------------------------------------------------------------------
    # 2. AUDIT INVENTORY IMAGES IN laptops-data.js
    # --------------------------------------------------------------------------
    print("\n[CHECK 2] Auditing inventory images in laptops-data.js...")
    ldata = open('laptops-data.js', encoding='utf-8').read()
    m = re.search(r'const LAPTOPS_INVENTORY = (\[.*?\]);', ldata, re.DOTALL)
    if not m:
        issues_found.append({
            "category": "Data Syntax",
            "file": "laptops-data.js",
            "severity": "CRITICAL",
            "description": "Could not parse LAPTOPS_INVENTORY JSON array"
        })
    else:
        try:
            laps = json.loads(m.group(1))
            print(f"  Parsed {len(laps)} laptops from laptops-data.js")
            missing_imgs = 0
            for lap in laps:
                lid = lap.get('id')
                img = lap.get('img')
                pimg = lap.get('processedImg')
                images = lap.get('images', [])
                
                if img and not os.path.exists(img):
                    issues_found.append({
                        "category": "Missing Inventory Image",
                        "file": "laptops-data.js",
                        "severity": "MEDIUM",
                        "description": f"Laptop ID {lid} ({lap.get('name')}) primary img missing: {img}"
                    })
                    missing_imgs += 1
                if pimg and not os.path.exists(pimg):
                    issues_found.append({
                        "category": "Missing Inventory Image",
                        "file": "laptops-data.js",
                        "severity": "LOW",
                        "description": f"Laptop ID {lid} processed cutout missing: {pimg}"
                    })
                for idx, simg in enumerate(images):
                    if simg and not os.path.exists(simg):
                        issues_found.append({
                            "category": "Missing Inventory Image",
                            "file": "laptops-data.js",
                            "severity": "MEDIUM",
                            "description": f"Laptop ID {lid} gallery image [{idx}] missing: {simg}"
                        })
            if missing_imgs == 0:
                print("  All primary inventory images exist on disk!")
        except Exception as e:
            issues_found.append({
                "category": "Data Syntax",
                "file": "laptops-data.js",
                "severity": "CRITICAL",
                "description": f"Error parsing JSON: {str(e)}"
            })

    # --------------------------------------------------------------------------
    # 3. AUDIT PERFORMANCE: EVENT LISTENERS & SCROLL PASSIVITY
    # --------------------------------------------------------------------------
    print("\n[CHECK 3] Auditing JavaScript files for scroll/wheel passivity & memory leaks...")
    js_files = glob.glob('js/**/*.js', recursive=True) + ['laptophub.html', 'consult.html', 'product.html']
    
    for jf in js_files:
        if 'desktop_copies' in jf: continue
        content = open(jf, encoding='utf-8').read()
        
        # Check non-passive scroll or wheel listeners by finding addEventListener calls
        for m in re.finditer(r'addEventListener\(\s*[\'"](scroll|wheel)[\'"]\s*,([\s\S]*?)\)', content):
            ev_name = m.group(1)
            call_body = m.group(2)
            if 'passive: true' not in call_body and 'passive:true' not in call_body:
                issues_found.append({
                    "category": "Performance: Passive Listener",
                    "file": jf,
                    "severity": "LOW",
                    "description": f"Scroll listener without {{ passive: true }}: addEventListener('{ev_name}', ...)"
                })
    print("  All scroll and wheel event listeners audited!")

    # --------------------------------------------------------------------------
    # 4. AUDIT BACKEND SERVER ENDPOINTS (server.py)
    # --------------------------------------------------------------------------
    print("\n[CHECK 4] Testing live HTTP server endpoints...")
    endpoints_to_test = [
        ("GET", "http://localhost:8080/laptophub.html", 200),
        ("GET", "http://localhost:8080/consult.html", 200),
        ("GET", "http://localhost:8080/product.html?id=1", 200),
        ("GET", "http://localhost:8080/css/global.css", 200),
        ("GET", "http://localhost:8080/js/cursor.js", 200),
        ("GET", "http://localhost:8080/css/hover-expand.css", 200),
        ("GET", "http://localhost:8080/js/hover-expand.js", 200),
        ("GET", "http://localhost:8080/api/auth/me", 200),
        ("GET", "http://localhost:8080/api/inventory", 200),
    ]

    for method, url, expected_code in endpoints_to_test:
        try:
            req = urllib.request.Request(url, method=method)
            with urllib.request.urlopen(req, timeout=3) as resp:
                code = resp.getcode()
                if code != expected_code:
                    issues_found.append({
                        "category": "Backend Endpoint",
                        "file": "server.py",
                        "severity": "HIGH",
                        "description": f"{url} returned HTTP {code}, expected {expected_code}"
                    })
                else:
                    print(f"  [OK] {url} -> HTTP {code}")
        except Exception as e:
            issues_found.append({
                "category": "Backend Endpoint",
                "file": "server.py",
                "severity": "HIGH",
                "description": f"{url} failed: {str(e)}"
            })

    # --------------------------------------------------------------------------
    # 5. AUDIT COMMON JAVASCRIPT BUGS & UNDEFINED SELECTORS
    # --------------------------------------------------------------------------
    print("\n[CHECK 5] Checking for missing DOM targets in scripts...")
    for target_html in ['laptophub.html', 'consult.html', 'product.html']:
        content = open(target_html, encoding='utf-8').read()
        js_ids = set(re.findall(r'document\.getElementById\(["\']([a-zA-Z0-9_\-]+)["\']\)', content))
        dom_ids = set(re.findall(r'id=["\']([a-zA-Z0-9_\-]+)["\']', content))
        
        missing = js_ids - dom_ids
        allowed = {
            'hoverExpandOverlay', 'hoverExpandCard', 'hoverExpandCloseBtn', 
            'hexBrand', 'hexTitle', 'hexPrice', 'hexTopBadges', 'hexStockBadge',
            'hexSlidesTrack', 'hexArrowPrev', 'hexArrowNext', 'hexDots',
            'hexSpecsGrid', 'hexBtnAddToCart', 'hexBtnCod', 'hexBtnWhatsApp',
            'hexBtnDetails', 'cursor-dot', 'cursor-ring', 'hexBadges', 'hexImgWrap',
            'hexImg', 'hexReviewsCount', 'hexGallery', 'hexSlideshowContainer',
            'mobileAdminLink', 'toast', 'toastMsg'
        }
        real_missing = missing - allowed
        if real_missing:
            for uid in real_missing:
                issues_found.append({
                    "category": "Missing DOM Element",
                    "file": target_html,
                    "severity": "MEDIUM",
                    "description": f"document.getElementById('{uid}') is called in script but element id does not exist in DOM"
                })
        else:
            print(f"  [OK] {target_html}: All referenced DOM IDs exist!")

    # --------------------------------------------------------------------------
    # REPORT SUMMARY
    # --------------------------------------------------------------------------
    print("\n" + "=" * 70)
    print(f"AUDIT COMPLETE: Found {len(issues_found)} potential issues")
    print("=" * 70)
    for idx, iss in enumerate(issues_found, 1):
        print(f"{idx}. [{iss['severity']}] {iss['category']} in {iss['file']}:")
        print(f"   {iss['description']}")

    with open('audit_results.json', 'w', encoding='utf-8') as f:
        json.dump(issues_found, f, indent=2)

if __name__ == '__main__':
    run_comprehensive_audit()
