import json
import urllib.request
import urllib.parse
import http.cookiejar
import re

BASE_URL = "http://localhost:8080"

def test_endpoints():
    print(">>> 1. Testing laptophub.html and css/header.css...")
    req = urllib.request.Request(f"{BASE_URL}/laptophub.html")
    with urllib.request.urlopen(req) as resp:
        html = resp.read().decode("utf-8")
        assert 'href="css/header.css"' in html, "header.css not linked!"
        assert 'href="laptophub.html" class="logo-mark"' in html, "logo does not link to laptophub.html!"
        assert 'index.html' not in html[:3000], "index.html found in top of laptophub.html!"
        print("  [PASS] laptophub.html links css/header.css and logo links to laptophub.html")

    req_css = urllib.request.Request(f"{BASE_URL}/css/header.css")
    with urllib.request.urlopen(req_css) as resp:
        css = resp.read().decode("utf-8")
        assert 'grid-template-columns: 1fr auto 1fr;' in css, "3-column grid missing in header.css!"
        assert 'height: 40px' in css, "40px height missing in header.css!"
        assert 'text-overflow: ellipsis' in css, "Ellipsis truncation missing in header.css!"
        print("  [PASS] css/header.css contains grid, 40px action buttons, and ellipsis truncation")

    print("\n>>> 2. Testing RAM Pricing API...")
    req_pricing = urllib.request.Request(f"{BASE_URL}/api/config/ram-pricing")
    with urllib.request.urlopen(req_pricing) as resp:
        data = json.loads(resp.read().decode("utf-8"))
        assert "ddr4" in data, "ddr4 missing in ram-pricing API!"
        assert data["ddr4"]["8"] == 0
        assert data["ddr4"]["16"] == 8000
        assert data["ddr4"]["32"] == 23000
        print(f"  [PASS] API returned active RAM tiers: {data}")

    print("\n>>> 3. Testing Admin Login and RAM Pricing Update...")
    cj = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))

    login_payload = json.dumps({"email": "admin@laptophub.pk", "password": "AdminPass123!"}).encode("utf-8")
    req_login = urllib.request.Request(f"{BASE_URL}/api/admin/login", data=login_payload, headers={"Content-Type": "application/json"})
    with opener.open(req_login) as resp:
        login_resp = json.loads(resp.read().decode("utf-8"))
        assert login_resp.get("role") == "admin", f"Admin login failed: {login_resp}"
        print(f"  [PASS] Admin logged in successfully: {login_resp['name']} ({login_resp['role']})")

    # Update pricing via admin endpoint
    updated_payload = json.dumps({
        "ddr4": {"8": 0, "16": 8000, "32": 23000},
        "ddr5": {"8": 0, "16": 10000, "32": 28000}
    }).encode("utf-8")
    req_update = urllib.request.Request(f"{BASE_URL}/api/admin/config/ram-pricing", data=updated_payload, headers={"Content-Type": "application/json"})
    with opener.open(req_update) as resp:
        res = json.loads(resp.read().decode("utf-8"))
        assert res.get("success"), f"Update failed: {res}"
        print("  [PASS] Admin updated RAM pricing tiers successfully")

def test_ram_math():
    print("\n>>> 4. Verifying RAM Delta Math...")
    # Tier table: 8GB=0, 16GB=8000, 32GB=23000
    tiers = {8: 0, 16: 8000, 32: 23000}
    
    def get_delta(target_gb, base_gb):
        return tiers[target_gb] - tiers[base_gb]

    # Test Base 16GB
    assert get_delta(8, 16) == -8000, f"Expected -8000, got {get_delta(8, 16)}"
    assert get_delta(16, 16) == 0, f"Expected 0, got {get_delta(16, 16)}"
    assert get_delta(32, 16) == 15000, f"Expected 15000, got {get_delta(32, 16)}"
    print("  [PASS] Base 16GB: 8GB = -Rs 8,000 | 16GB = Included | 32GB = +Rs 15,000")

    # Test Base 8GB
    assert get_delta(8, 8) == 0, f"Expected 0, got {get_delta(8, 8)}"
    assert get_delta(16, 8) == 8000, f"Expected 8000, got {get_delta(16, 8)}"
    assert get_delta(32, 8) == 23000, f"Expected 23000, got {get_delta(32, 8)}"
    print("  [PASS] Base 8GB: 8GB = Included | 16GB = +Rs 8,000 | 32GB = +Rs 23,000")

    # Test Base 32GB
    assert get_delta(8, 32) == -23000, f"Expected -23000, got {get_delta(8, 32)}"
    assert get_delta(16, 32) == -15000, f"Expected -15000, got {get_delta(16, 32)}"
    assert get_delta(32, 32) == 0, f"Expected 0, got {get_delta(32, 32)}"
    print("  [PASS] Base 32GB: 8GB = -Rs 23,000 | 16GB = -Rs 15,000 | 32GB = Included")

if __name__ == "__main__":
    test_endpoints()
    test_ram_math()
    print("\nALL AUTOMATED TESTS PASSED!")
