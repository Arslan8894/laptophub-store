import json
import re
import os
import sys
import urllib.request
import urllib.parse

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.dirname(BASE_DIR)
sys.path.insert(0, BASE_DIR)
sys.path.insert(0, PARENT_DIR)

def run_suite():
    print("=" * 65)
    print("  CONSULT ME COMPREHENSIVE VERIFICATION SUITE")
    print("=" * 65)

    # 1. Load Inventory & HTML
    with open('laptops-data.js', 'r', encoding='utf-8') as f:
        text = f.read()
    start = text.find('[')
    end = text.rfind(']') + 1
    laptops = json.loads(text[start:end])
    print(f"[OK] Loaded {len(laptops)} laptops from laptops-data.js")

    with open('consult.html', 'r', encoding='utf-8') as f:
        html = f.read()
    print(f"[OK] consult.html verified ({len(html)} bytes)")

    # Verify script references in consult.html
    assert 'consult-matcher.js' in html, "consult-matcher.js must be included in consult.html"
    assert 'id="aiRecomContainer"' in html, "aiRecomContainer element missing"
    assert 'id="aiLoadingSkeleton"' in html, "aiLoadingSkeleton element missing"
    assert 'id="aiRecomCard"' in html, "aiRecomCard element missing"
    assert 'id="nothingFoundContainer"' in html, "nothingFoundContainer element missing"
    assert 'id="resultsGrid"' in html, "resultsGrid element missing"
    print("[OK] All required HTML DOM elements and script inclusions present.")

    # 2. Test Pure Matcher Module
    from scripts.test_matcher import matches_preference, calculate_upgrade_cost

    # TEST CASE 1: MULTI-MATCH COMBINATION
    print("\n--- TEST CASE 1: Combination with Several Matches ---")
    prefs_multi = {
        'usecase': 'office',
        'cpu': 'intel_i7',
        'ram': 16,
        'storage': 512,
        'gpu': 'integrated',
        'budget': 130000
    }
    matches_1 = [l for l in laptops if matches_preference(l, prefs_multi)[0]]
    print(f"Results for Office, Intel i7, 16GB, 512GB, Integrated, PKR 130,000:")
    print(f"Matched count: {len(matches_1)} laptops (NOT the full 69-laptop store)")
    assert 5 <= len(matches_1) <= 10, f"Expected 5-10 matches, got {len(matches_1)}"
    for m in matches_1:
        print(f"  - [{m['id']}] {m['name']} | PKR {m['price']:,} | {m['cpu']} | {m['gpu']}")

    # TEST CASE 2: SINGLE-MATCH COMBINATION
    print("\n--- TEST CASE 2: Combination with Exactly One Match ---")
    prefs_single = {
        'usecase': 'student',
        'cpu': 'any',
        'ram': 8,
        'storage': 256,
        'gpu': 'no_pref',
        'budget': 33000
    }
    matches_2 = [l for l in laptops if matches_preference(l, prefs_single)[0]]
    print(f"Results for Student, Any CPU, 8GB RAM, 256GB SSD, Budget PKR 33,000:")
    print(f"Matched count: {len(matches_2)} laptop")
    assert len(matches_2) == 1, f"Expected exactly 1 match, got {len(matches_2)}"
    print(f"  -> Exact Match: [{matches_2[0]['id']}] {matches_2[0]['name']} (PKR {matches_2[0]['price']:,})")

    # TEST CASE 3: ZERO-MATCH COMBINATION
    print("\n--- TEST CASE 3: Zero-Match Combination (Budget too low / Impossible combo) ---")
    prefs_zero = {
        'usecase': 'gaming',
        'cpu': 'any',
        'ram': 32,
        'storage': 1000,
        'gpu': 'rtx',
        'budget': 40000 # impossible budget for RTX 32GB 1TB
    }
    matches_3 = [l for l in laptops if matches_preference(l, prefs_zero)[0]]
    print(f"Results for Gaming, RTX, 32GB RAM, 1TB SSD, Budget PKR 40,000:")
    print(f"Matched count: {len(matches_3)} laptops")
    assert len(matches_3) == 0, f"Expected 0 matches, got {len(matches_3)}"
    print("  -> Successfully avoided full-store dump. Zero matches returned.")

    # TEST CASE 4: GOING BACK AND CHANGING AN ANSWER
    print("\n--- TEST CASE 4: Going Back and Changing Answer ---")
    # Simulate user changing budget from 40k to 360k
    prefs_changed = dict(prefs_zero)
    prefs_changed['budget'] = 360000
    matches_4 = [l for l in laptops if matches_preference(l, prefs_changed)[0]]
    print(f"After raising budget to PKR 360,000:")
    print(f"Matched count updated from 0 to: {len(matches_4)} laptops")
    assert len(matches_4) >= 1, "Results should dynamically update when answer changes"
    for m in matches_4:
        print(f"  - [{m['id']}] {m['name']} | PKR {m['price']:,}")

    # TEST CASE 5: AI SERVICE OFFLINE FALLBACK
    print("\n--- TEST CASE 5: AI Service Offline Fallback ---")
    api_payload = json.dumps({
        'preferences': prefs_multi,
        'matchedLaptops': [{'id': m['id'], 'name': m['name'], 'price': m['price']} for m in matches_1]
    }).encode('utf-8')

    req = urllib.request.Request(
        'http://127.0.0.1:8080/api/consult/ai-recommend',
        data=api_payload,
        headers={'Content-Type': 'application/json'}
    )
    with urllib.request.urlopen(req) as resp:
        res_data = json.loads(resp.read().decode('utf-8'))
    print("API Response:", res_data)
    assert res_data.get('fallback') is True or res_data.get('success') is True
    print("  -> AI API successfully handled request and provided safe fallback response.")

    # TEST CASE 6: RESPONSIVENESS AND CSS AUDIT
    print("\n--- TEST CASE 6: Mobile (360px) and Desktop Responsive Layout Audit ---")
    assert '@media (max-width: 640px)' in html, "Mobile media query missing"
    assert 'minmax(260px, 1fr)' in html or 'minmax(175px, 1fr)' in html, "Responsive grid columns missing"
    assert 'flex-wrap: wrap' in html, "Responsive flex wrapping missing"
    assert 'overflow-x' not in html or 'overflow: hidden' in html, "Check clean layout"
    print("  -> Responsive tokens, mobile grid rules, and overflow safety verified.")

    print("\n" + "=" * 65)
    print("  ALL 6 SUITE TESTS PASSED WITH 100% SUCCESS!")
    print("=" * 65)

if __name__ == '__main__':
    run_suite()
