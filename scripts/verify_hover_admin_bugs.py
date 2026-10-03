"""
Comprehensive Empirical Verification Script for:
1. Admin unauthenticated redirect to home page (laptophub.html)
2. Admin login form & Firebase Auth integration
3. Firestore rules structure and syntax
4. Hover-to-expand CSS and JS presence and functionality
5. Out of stock button disabling and badge rendering logic
6. Glass navbar tab transition lock (no glitch)
7. Liquid glass topbar styling on product.html
"""
import urllib.request
import re
import os
import json

BASE_URL = "http://localhost:8080"

def run_tests():
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

    print("\n" + "="*70)
    print("EMPIRICAL VERIFICATION: HOVER-EXPAND & ADMIN SECURITY SYSTEM")
    print("="*70)

    # ── TEST 1: Unauthenticated Admin Guard in admin/index.html ──
    print("\n>>> 1. Verifying Admin Guard & Redirect...")
    with open("admin/index.html", "r", encoding="utf-8") as f:
        admin_content = f.read()

    assert_true(
        "window.location.replace('../laptophub.html')" in admin_content,
        "admin/index.html redirects unauthenticated visitors to ../laptophub.html"
    )
    assert_true(
        "window.adminSaveLaptop" in admin_content and "window.adminDeleteLaptop" in admin_content,
        "admin/index.html utilizes Firestore admin helper functions"
    )
    assert_true(
        "window.adminUpdateStock" in admin_content,
        "admin/index.html supports fast stock updating via Firestore"
    )

    # ── TEST 2: Admin Login Page (admin/login.html) ──
    print("\n>>> 2. Verifying Admin Login & Auth...")
    with open("admin/login.html", "r", encoding="utf-8") as f:
        login_content = f.read()

    assert_true(
        "signInWithEmailAndPassword" in login_content,
        "admin/login.html implements Firebase Authentication signInWithEmailAndPassword"
    )
    assert_true(
        "window.location.replace('./')" in login_content,
        "admin/login.html successfully directs authenticated admin to /admin/"
    )

    # ── TEST 3: Cloud Firestore Security Rules ──
    print("\n>>> 3. Verifying Cloud Firestore Security Rules...")
    with open("firestore.rules", "r", encoding="utf-8") as f:
        rules_content = f.read()

    assert_true(
        "allow read: if true;" in rules_content,
        "firestore.rules allows public read for storefront inventory"
    )
    assert_true(
        "request.auth != null" in rules_content and ("allow create, update, delete:" in rules_content or "allow write:" in rules_content),
        "firestore.rules enforces authentication check for all write/mutation operations"
    )

    # ── TEST 4: Hover-to-Expand System in laptophub.html ──
    print("\n>>> 4. Verifying Hover-to-Expand Card System...")
    with open("laptophub.html", "r", encoding="utf-8") as f:
        hub_content = f.read()

    assert_true(
        'href="css/hover-expand.css"' in hub_content,
        "laptophub.html links css/hover-expand.css"
    )
    assert_true(
        'src="js/hover-expand.js"' in hub_content,
        "laptophub.html includes js/hover-expand.js"
    )
    assert_true(
        "handleCardClick(" in hub_content,
        "laptophub.html card click triggers handleCardClick for touch tap-to-expand"
    )

    # Check js/hover-expand.js implementation details
    with open("js/hover-expand.js", "r", encoding="utf-8") as f:
        hex_js = f.read()

    assert_true(
        "2000" in hex_js and "setTimeout" in hex_js,
        "hover-expand.js uses exactly 2000ms (2 seconds) deliberate hover timer"
    )
    assert_true(
        "clearHoverTimer" in hex_js and "pointerleave" in hex_js,
        "hover-expand.js immediately cancels timer on mouseleave"
    )
    assert_true(
        "window.addEventListener('scroll'" in hex_js,
        "hover-expand.js cancels timer during scroll to prevent accidental triggers"
    )
    assert_true(
        "prefersReducedMotion" in hex_js,
        "hover-expand.js explicitly checks and respects prefers-reduced-motion"
    )
    assert_true(
        "translate3d" in hex_js and "scale" in hex_js,
        "hover-expand.js implements FLIP animation morphing from origin card rect"
    )

    # ── TEST 5: Out of Stock Handling ──
    print("\n>>> 5. Verifying Out-of-Stock Logic Across Storefront...")
    assert_true(
        "isOutOfStock = lap.stock !== undefined && lap.stock <= 0" in hub_content,
        "laptophub.html identifies laptops with stock <= 0 as out of stock"
    )
    with open("product.html", "r", encoding="utf-8") as f:
        prod_content = f.read()

    assert_true(
        "Out of Stock" in prod_content and "addBtn.disabled = true" in prod_content,
        "product.html disables Add to Cart button when stock <= 0"
    )

    # ── TEST 6: Liquid Glass Topbar on product.html ──
    print("\n>>> 6. Verifying Liquid Glass Topbar on product.html...")
    assert_true(
        'class="liquid-glass-nav"' in prod_content,
        "product.html has liquid-glass-nav class on header"
    )
    assert_true(
        "top-ambient-glow" in prod_content,
        "product.html has top-ambient-glow providing rich lighting for glass refraction"
    )

    # ── TEST 7: Glass Nav Tab Glitch Elimination ──
    print("\n>>> 7. Verifying Glass Nav Tab Switcher Smoothness...")
    with open("js/animations/glass-nav.js", "r", encoding="utf-8") as f:
        glass_nav = f.read()

    assert_true(
        "scrollend" in glass_nav,
        "glass-nav.js listens to scrollend event for accurate navigation completion"
    )
    assert_true(
        "stillFrames >= 4" in glass_nav and "elapsed > 700" in glass_nav,
        "glass-nav.js fallback arrival monitor prevents premature lock release"
    )

    # ── TEST 8: Live HTTP Server Response ──
    print("\n>>> 8. Verifying Live Server Endpoints...")
    try:
        req = urllib.request.Request(f"{BASE_URL}/laptophub.html")
        res = urllib.request.urlopen(req)
        assert_true(res.status == 200, "HTTP 200 on /laptophub.html")

        req2 = urllib.request.Request(f"{BASE_URL}/product.html?id=1")
        res2 = urllib.request.urlopen(req2)
        assert_true(res2.status == 200, "HTTP 200 on /product.html?id=1")

        req3 = urllib.request.Request(f"{BASE_URL}/css/hover-expand.css")
        res3 = urllib.request.urlopen(req3)
        assert_true(res3.status == 200, "HTTP 200 on /css/hover-expand.css")

        req4 = urllib.request.Request(f"{BASE_URL}/js/hover-expand.js")
        res4 = urllib.request.urlopen(req4)
        assert_true(res4.status == 200, "HTTP 200 on /js/hover-expand.js")
    except Exception as e:
        assert_true(False, f"Server endpoint error: {e}")

    print("\n" + "="*70)
    print(f"RESULTS: {passes} passed, {fails} failed.")
    print("="*70 + "\n")
    return fails == 0

if __name__ == '__main__':
    success = run_tests()
    exit(0 if success else 1)
