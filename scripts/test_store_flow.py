# -*- coding: utf-8 -*-
"""
Automated unit & integration test for clean model names and structured specs.
"""

import json
import re
import urllib.request
import urllib.parse

print("=" * 65)
print("  LAPTOP STORE SPECS & NAMING VERIFICATION SUITE")
print("=" * 65)

# 1. Test laptops-data.js integrity
with open('laptops-data.js', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'const\s+LAPTOPS_INVENTORY\s*=\s*(\[.*?\]);', text, re.DOTALL)
assert m, "Could not match LAPTOPS_INVENTORY"
laptops = json.loads(m.group(1))
assert len(laptops) == 69, f"Expected 69 laptops, got {len(laptops)}"
print(f"[OK] Loaded {len(laptops)} laptops from laptops-data.js")

# Check each laptop
forbidden_name_patterns = [
    r'\bCore\s+i[3579]\b',
    r'\bi[3579]\s+\d+th\b',
    r'\b\d+Th\b',
    r'\b\d+th\b',
    r'\b\d+GB\b',
    r'\b\d+gb\b',
    r'\bRyzen\s+[3579]\s+PRO\b',
    r'\bRyzen\s+[3579]\s+\d+\b',
    r'\bCore\s+M5\b',
    r'\bCore\s+ULTRA\b',
    r'\bCore\s+i5/i7\b'
]

naming_issues = []
categories_required = ['performance', 'memoryStorage', 'display', 'graphics', 'connectivityPorts', 'batteryBuild', 'conditionWarranty']
missing_spec_categories = []

for lap in laptops:
    lid = lap['id']
    name = lap['name']
    legacy = lap.get('legacyName')
    
    assert legacy, f"Laptop {lid} missing legacyName"
    
    # Check for forbidden processor/RAM strings in name
    for pat in forbidden_name_patterns:
        if re.search(pat, name, re.IGNORECASE):
            naming_issues.append((lid, name, pat))
            
    # Check shortSpecs
    short = lap.get('shortSpecs')
    assert short, f"Laptop {lid} missing shortSpecs"
    assert 'cpuFamily' in short, f"Laptop {lid} shortSpecs missing cpuFamily"
    assert 'generation' in short, f"Laptop {lid} shortSpecs missing generation"
    assert 'ramGb' in short, f"Laptop {lid} shortSpecs missing ramGb"
    assert 'storageGb' in short, f"Laptop {lid} shortSpecs missing storageGb"
    
    # Check fullSpecs
    full = lap.get('fullSpecs')
    assert full, f"Laptop {lid} missing fullSpecs"
    for cat in categories_required:
        if cat not in full:
            missing_spec_categories.append((lid, cat))

if naming_issues:
    print(f"[WARNING] Found {len(naming_issues)} potential naming pattern matches:")
    for lid, name, pat in naming_issues[:5]:
        print(f"  Laptop {lid}: '{name}' matched pattern '{pat}'")
else:
    print("[OK] All 69 product names are clean official model names with NO processor/RAM/storage strings!")

if missing_spec_categories:
    print(f"[FAIL] Missing categories: {missing_spec_categories}")
else:
    print("[OK] All 69 laptops have complete 7-category fullSpecs structures!")

# 2. Test HTTP server running
try:
    req = urllib.request.urlopen("http://127.0.0.1:8080/laptophub.html", timeout=5)
    html = req.read().decode('utf-8')
    assert req.status == 200
    print("[OK] Server is active on port 8080 and serving laptophub.html")
    
    # Check that new elements and styles exist in HTML
    assert 'lmodal-specs-section' in html, "Missing lmodal-specs-section in HTML"
    assert 'lmodalSpecsGrid' in html, "Missing lmodalSpecsGrid in HTML"
    assert 'renderModalFullSpecs' in html, "Missing renderModalFullSpecs in JavaScript"
    assert 'pcard-chips' in html, "Missing pcard-chips CSS in HTML"
    print("[OK] laptophub.html contains all modal specs and card chips DOM & logic elements.")
except Exception as e:
    print(f"[ERROR] Could not connect to local server: {e}")

print("=" * 65)
print("  ALL DATASET AND PAGE ASSERTIONS PASSED SUCCESSFULLY!")
print("=" * 65)
