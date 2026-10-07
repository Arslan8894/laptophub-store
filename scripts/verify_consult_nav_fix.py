"""
Verification script for:
TASK: Fix the Consult Me navigation on LaptopHUB.
1. Homepage has no #consult section, no dead code, no gaps.
2. Desktop and mobile nav links point directly to consult.html.
3. consult.html has active tab styling, working back buttons, and mobile drawer.
4. Other tabs (All Laptops, Reviews) remain fully functional.
"""

import sys
import os
import re
import urllib.request

BASE_URL = "http://localhost:8080"

def test_consult_me_navigation():
    passes = 0
    fails = 0

    def assert_true(cond, msg):
        nonlocal passes, fails
        if cond:
            print(f"  [PASS] {msg}")
            passes += 1
        else:
            print(f"  [FAIL] {msg}")
            fails += 1
            raise AssertionError(msg)

    print("\n" + "="*70)
    print("VERIFICATION: CONSULT ME NAVIGATION & HOMEPAGE AUDIT")
    print("="*70)

    # 1. Homepage Audit (laptophub.html)
    print("\n>>> 1. Auditing laptophub.html...")
    with open("laptophub.html", "r", encoding="utf-8") as f:
        html = f.read()

    # Section #consult must be completely removed
    assert_true('id="consult"' not in html, "Homepage has zero sections with id='consult'")
    assert_true('id="consultChips"' not in html, "Homepage has zero elements with id='consultChips'")
    assert_true('id="consultMatchesGrid"' not in html, "Homepage has zero elements with id='consultMatchesGrid'")
    assert_true('btn-launch-wizard' not in html, "Homepage has zero 'Launch Complete 6-Step' buttons")
    assert_true('consult-matcher.js' not in html, "Homepage has no script tag for consult-matcher.js")

    # Navbar links must point directly to consult.html
    nav_match = re.search(r'<ul class="nav-pill-track">([\s\S]*?)</ul>', html)
    assert_true(nav_match is not None, "Desktop nav-pill-track exists")
    nav_content = nav_match.group(1)
    assert_true('href="consult.html"' in nav_content, "Desktop nav has href='consult.html' for Consult Me")
    assert_true('href="#consult"' not in nav_content, "Desktop nav has no href='#consult'")
    assert_true('href="#inventory"' in nav_content, "Desktop nav retains href='#inventory' for All Laptops")
    assert_true('href="#reviews"' in nav_content, "Desktop nav retains href='#reviews' for Reviews")

    # Mobile drawer links
    drawer_match = re.search(r'<ul class="mobile-nav-links">([\s\S]*?)</ul>', html)
    assert_true(drawer_match is not None, "Mobile nav drawer links exist")
    drawer_content = drawer_match.group(1)
    assert_true('href="consult.html"' in drawer_content and 'toggleMobileNav(false)' in drawer_content,
                "Mobile drawer Consult Me links to consult.html and closes drawer")
    assert_true('href="#consult"' not in drawer_content, "Mobile drawer has no href='#consult'")

    # 2. Consult Me Page Audit (consult.html)
    print("\n>>> 2. Auditing consult.html...")
    with open("consult.html", "r", encoding="utf-8") as f:
        consult_html = f.read()

    # Desktop nav in consult.html
    assert_true('href="laptophub.html#inventory"' in consult_html, "consult.html nav links to laptophub.html#inventory")
    assert_true('href="consult.html" class="active"' in consult_html or 'class="active" href="consult.html"' in consult_html,
                "consult.html marks Consult Me as active tab in desktop nav")
    assert_true('href="laptophub.html#reviews"' in consult_html, "consult.html nav links to laptophub.html#reviews")

    # Back buttons in consult.html
    assert_true('id="btnBackToStore"' in consult_html and 'returnToPreviousTab' in consult_html,
                "Top nav has functional '<- Store' back button with returnToPreviousTab handler")
    assert_true('id="btnStep1Back"' in consult_html and 'goPrev(1)' in consult_html,
                "Step 1 wizard has active '<- Back' button wired to goPrev(1)")
    assert_true('disabled' not in consult_html.split('id="btnStep1Back"')[0][-30:],
                "Step 1 Back button is NOT disabled")

    # Mobile drawer in consult.html
    assert_true('id="mobileNavBtn"' in consult_html, "consult.html has mobileNavBtn hamburger toggle")
    assert_true('id="mobileNavDrawer"' in consult_html, "consult.html has mobileNavDrawer")
    assert_true('id="mobileNavOverlay"' in consult_html, "consult.html has mobileNavOverlay")
    assert_true('toggleMobileNav' in consult_html, "consult.html implements toggleMobileNav")

    # 3. Glass Nav Script Audit (js/animations/glass-nav.js)
    print("\n>>> 3. Auditing glass-nav.js...")
    with open("js/animations/glass-nav.js", "r", encoding="utf-8") as f:
        glass_js = f.read()
    assert_true("consultSec" not in glass_js, "glass-nav.js scroll spy no longer monitors consultSec")
    assert_true("consult.html" in glass_js, "glass-nav.js recognizes consult.html path for active lens")

    # 4. CSS Audit (css/glass.css)
    print("\n>>> 4. Auditing css/glass.css...")
    with open("css/glass.css", "r", encoding="utf-8") as f:
        glass_css = f.read()
    assert_true(".consult-panel-container" not in glass_css, "css/glass.css has no dead .consult-panel-container rules")
    assert_true(".consult-glass-card" not in glass_css, "css/glass.css has no dead .consult-glass-card rules")

    # 5. Live Server HTTP Verification
    print("\n>>> 5. Testing HTTP status codes on live server...")
    req_hub = urllib.request.urlopen(f"{BASE_URL}/laptophub.html")
    assert_true(req_hub.status == 200, "HTTP 200 on /laptophub.html")

    req_consult = urllib.request.urlopen(f"{BASE_URL}/consult.html")
    assert_true(req_consult.status == 200, "HTTP 200 on /consult.html")

    print("\n" + "="*70)
    print(f"RESULTS: {passes} passed, {fails} failed.")
    print("="*70 + "\n")
    return fails == 0

if __name__ == "__main__":
    success = test_consult_me_navigation()
    sys.exit(0 if success else 1)
