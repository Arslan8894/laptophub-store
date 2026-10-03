"""
Comprehensive automated test suite for PART 5 (Sign In Required to Buy)
and PART 6 (Admin Panel Visible Only to a Logged-In Admin).
"""
import sys
import os
import json
import re
import urllib.request
import urllib.parse
import http.cookiejar

BASE_URL = "http://localhost:8080"

class TestSuite:
    def __init__(self):
        self.passes = 0
        self.fails = 0

    def assert_true(self, condition, message):
        if condition:
            print(f"  [PASS] {message}")
            self.passes += 1
        else:
            print(f"  [FAIL] {message}")
            self.fails += 1
            raise AssertionError(message)

    def run_all(self):
        print("\n" + "="*70)
        print("TEST SUITE: PART 5 & PART 6 AUTOMATED VERIFICATION")
        print("="*70)

        self.test_1_signed_out_buying_actions()
        self.test_2_customer_registration_phone_and_order()
        self.test_3_normal_customer_zero_admin_access()
        self.test_4_admin_login_panel_and_signout()
        self.test_5_account_switching_no_leakage()
        self.test_6_immediate_role_revocation()
        self.test_7_dom_static_and_dynamic_inspection()

        print("\n" + "="*70)
        print(f"RESULTS: {self.passes} passed, {self.fails} failed.")
        print("="*70 + "\n")
        return self.fails == 0

    def make_opener(self):
        cj = http.cookiejar.CookieJar()
        return urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj)), cj

    # ─────────────────────────────────────────────────────────────
    # TEST 1: Signed-Out Visitor Buying Actions & Server 401
    # ─────────────────────────────────────────────────────────────
    def test_1_signed_out_buying_actions(self):
        print("\n>>> 1. Testing Signed-Out Visitor Buying Actions...")
        opener, _ = self.make_opener()

        # Direct POST /api/orders without session cookie
        payload = json.dumps({
            "items": [{"id": 1, "name": "ThinkPad T14", "price": 85000, "qty": 1}],
            "name": "Anonymous Guest",
            "phone": "03261398594",
            "city": "Lahore",
            "address": "Gulberg III"
        }).encode('utf-8')

        req = urllib.request.Request(
            f"{BASE_URL}/api/orders",
            data=payload,
            headers={"Content-Type": "application/json"},
            method="POST"
        )

        try:
            opener.open(req)
            self.assert_true(False, "Unauthenticated order should have failed with 401")
        except urllib.error.HTTPError as e:
            self.assert_true(e.code == 401, f"Direct order API returns HTTP 401 (got {e.code})")
            err_data = json.loads(e.read().decode())
            self.assert_true("Please sign in" in err_data.get("error", ""),
                             f"401 error message instructs sign-in: '{err_data.get('error')}'")

        # Verify client-side source contains proper auth checks on all buying entrypoints
        with open("laptophub.html", "r", encoding="utf-8") as f:
            html = f.read()

        self.assert_true("pendingBuyAction = { type: 'checkout' }" in html or "pendingBuyAction = { type: 'cod_checkout' }" in html,
                         "Checkout saves pendingBuyAction and prompts login")
        self.assert_true("pendingBuyAction = { type: 'card_whatsapp'" in html,
                         "Card WhatsApp order saves pendingBuyAction and prompts login")
        self.assert_true("pendingBuyAction = { type: 'cart_whatsapp' }" in html,
                         "Cart WhatsApp checkout saves pendingBuyAction and prompts login")
        self.assert_true("resumePendingBuyAction" in html,
                         "resumePendingBuyAction executes after successful sign-in")

    # ─────────────────────────────────────────────────────────────
    # TEST 2: Customer Registration, Phone Validation & Order Flow
    # ─────────────────────────────────────────────────────────────
    def test_2_customer_registration_phone_and_order(self):
        print("\n>>> 2. Testing Customer Registration, PK Phone Validation & Order...")
        opener, cj = self.make_opener()

        # Test invalid Pakistani phone rejection
        bad_reg = json.dumps({
            "email": "cust_test@laptophub.pk",
            "password": "Password123!",
            "name": "Test Customer",
            "phone": "12345678",  # Invalid PK phone
            "city": "Lahore",
            "address": "Street 4, DHA"
        }).encode('utf-8')

        req = urllib.request.Request(f"{BASE_URL}/api/auth/register", data=bad_reg,
                                     headers={"Content-Type": "application/json"}, method="POST")
        try:
            opener.open(req)
            self.assert_true(False, "Invalid phone number should be rejected")
        except urllib.error.HTTPError as e:
            self.assert_true(e.code == 400, f"Invalid phone rejected with HTTP 400 (got {e.code})")

        # Test valid Pakistani phone registration (03XX-XXXXXXX format)
        cust_email = f"customer_{os.getpid()}@laptophub.pk"
        good_reg = json.dumps({
            "email": cust_email,
            "password": "Password123!",
            "name": "Hamza Tariq",
            "phone": "0321-9876543",
            "city": "Karachi",
            "address": "Plot 12-B, Block 6, PECHS, Karachi"
        }).encode('utf-8')

        req = urllib.request.Request(f"{BASE_URL}/api/auth/register", data=good_reg,
                                     headers={"Content-Type": "application/json"}, method="POST")
        res = opener.open(req)
        self.assert_true(res.status == 201, f"Customer registered successfully with HTTP 201")
        reg_data = json.loads(res.read().decode())
        self.assert_true(reg_data.get("role") == "user", "Customer role is 'user'")

        # Verify session info via /api/auth/me
        me_res = opener.open(f"{BASE_URL}/api/auth/me")
        me_data = json.loads(me_res.read().decode())
        self.assert_true(me_data.get("role") == "user", "Session confirms customer role 'user'")
        self.assert_true(me_data.get("phone") == "0321-9876543", "Customer phone stored in profile")
        self.assert_true(me_data.get("address") == "Plot 12-B, Block 6, PECHS, Karachi",
                         "Customer address stored in profile")

        # Now place order as logged-in customer
        order_payload = json.dumps({
            "items": [{"id": 1, "name": "ThinkPad T14", "price": 85000, "qty": 1}],
            "name": "Hamza Tariq",
            "phone": "0321-9876543",
            "city": "Karachi",
            "address": "Plot 12-B, Block 6, PECHS, Karachi"
        }).encode('utf-8')

        order_req = urllib.request.Request(f"{BASE_URL}/api/orders", data=order_payload,
                                           headers={"Content-Type": "application/json"}, method="POST")
        try:
            order_res = opener.open(order_req)
        except urllib.error.HTTPError as e:
            print("ORDER ERROR RESPONSE:", e.code, e.read().decode())
            raise
        self.assert_true(order_res.status in (200, 201), f"Authenticated customer order placed successfully (HTTP {order_res.status})")
        order_info = json.loads(order_res.read().decode())
        self.assert_true("orderId" in order_info, f"Order created with ID #LH-{order_info.get('orderId')}")

        # Confirm order shows up in /api/orders/mine
        my_orders_res = opener.open(f"{BASE_URL}/api/orders/mine")
        my_orders_data = json.loads(my_orders_res.read().decode())
        orders = my_orders_data.get("orders", [])
        self.assert_true(len(orders) >= 1, "Order immediately appears in customer's My Orders")
        self.assert_true(orders[0]["cust_name"] == "Hamza Tariq", "Order linked correctly to customer")

    # ─────────────────────────────────────────────────────────────
    # TEST 3: Normal Customer Zero Admin Access
    # ─────────────────────────────────────────────────────────────
    def test_3_normal_customer_zero_admin_access(self):
        print("\n>>> 3. Testing Normal Customer Has Zero Admin Access...")
        opener, _ = self.make_opener()

        # Login as existing customer
        login_body = json.dumps({
            "email": "arslan@laptophub.pk",
            "password": "Password123!"
        }).encode('utf-8')

        req = urllib.request.Request(f"{BASE_URL}/api/auth/login", data=login_body,
                                     headers={"Content-Type": "application/json"}, method="POST")
        res = opener.open(req)
        self.assert_true(res.status == 200, "Logged in as customer arslan@laptophub.pk")

        # Try to access Admin API endpoints -> must return 401 Unauthorized
        admin_endpoints = [
            "/api/admin/inventory",
            "/api/admin/orders",
            "/api/admin/users",
            "/api/admin/log"
        ]
        for ep in admin_endpoints:
            try:
                opener.open(f"{BASE_URL}{ep}")
                self.assert_true(False, f"Customer should not be able to access {ep}")
            except urllib.error.HTTPError as e:
                self.assert_true(e.code == 401, f"Customer access to {ep} blocked with HTTP 401")

        # Try to access /admin/ direct URL -> must 302 redirect to /admin/login
        class NoRedirectHandler(urllib.request.HTTPRedirectHandler):
            def http_error_302(self, req, fp, code, msg, headers):
                return fp
        
        nr_opener, _ = self.make_opener()
        # login customer on nr_opener
        cust_req = urllib.request.Request(f"{BASE_URL}/api/auth/login", data=login_body,
                                          headers={"Content-Type": "application/json"}, method="POST")
        login_res = nr_opener.open(cust_req)
        try:
            admin_page_req = urllib.request.Request(f"{BASE_URL}/admin/")
            admin_page_res = nr_opener.open(admin_page_req)
            # Either redirect to /admin/login or redirected URL is /admin/login
            final_url = admin_page_res.geturl()
            self.assert_true("/admin/login" in final_url,
                             f"Customer accessing /admin/ is redirected to /admin/login (landed on {final_url})")
        except urllib.error.HTTPError as e:
            self.assert_true(e.code in (302, 401, 403), f"Customer accessing /admin/ returned {e.code}")

    # ─────────────────────────────────────────────────────────────
    # TEST 4: Admin Login, Panel Access, Inventory Features & Signout
    # ─────────────────────────────────────────────────────────────
    def test_4_admin_login_panel_and_signout(self):
        print("\n>>> 4. Testing Admin Login, Admin Panel, and Signout...")
        opener, cj = self.make_opener()

        # Admin login
        admin_login = json.dumps({
            "email": "admin@laptophub.pk",
            "password": "AdminPass123!"
        }).encode('utf-8')

        req = urllib.request.Request(f"{BASE_URL}/api/admin/login", data=admin_login,
                                     headers={"Content-Type": "application/json"}, method="POST")
        res = opener.open(req)
        self.assert_true(res.status == 200, "Admin logged in successfully (HTTP 200)")
        adm_data = json.loads(res.read().decode())
        self.assert_true(adm_data.get("role") == "admin", "Admin role confirmed by server")

        # Admin can access admin API
        inv_res = opener.open(f"{BASE_URL}/api/admin/inventory")
        self.assert_true(inv_res.status == 200, "Admin can access /api/admin/inventory (HTTP 200)")
        laptops = json.loads(inv_res.read().decode())
        self.assert_true(len(laptops) == 69, f"Admin inventory returns all 69 models (got {len(laptops)})")

        # Admin can access /admin/ HTML with no-cache headers
        admin_html_res = opener.open(f"{BASE_URL}/admin/")
        self.assert_true(admin_html_res.status == 200, "Admin can view /admin/ panel")
        headers = dict(admin_html_res.headers)
        cache_ctrl = headers.get("Cache-Control", "")
        self.assert_true("no-store" in cache_ctrl and "no-cache" in cache_ctrl,
                         f"Admin page served with no-cache headers: {cache_ctrl}")
        self.assert_true("no-cache" in headers.get("Pragma", ""), "Admin page served with Pragma: no-cache")

        # Admin signs out
        logout_req = urllib.request.Request(f"{BASE_URL}/api/admin/logout", data=b'{}',
                                            headers={"Content-Type": "application/json"}, method="POST")
        logout_res = opener.open(logout_req)
        self.assert_true(logout_res.status == 200, "Admin signed out successfully")

        # Verify admin session completely destroyed
        try:
            opener.open(f"{BASE_URL}/api/admin/inventory")
            self.assert_true(False, "Post-signout admin API access must fail")
        except urllib.error.HTTPError as e:
            self.assert_true(e.code == 401, f"Post-signout admin API returns HTTP 401 (got {e.code})")

    # ─────────────────────────────────────────────────────────────
    # TEST 5: Account Switching Between Customer & Admin (No Leakage)
    # ─────────────────────────────────────────────────────────────
    def test_5_account_switching_no_leakage(self):
        print("\n>>> 5. Testing Account Switching In Same Browser Session...")
        opener, cj = self.make_opener()

        # Step A: Log in as customer
        cust_payload = json.dumps({"email": "arslan@laptophub.pk", "password": "Password123!"}).encode()
        r1 = opener.open(urllib.request.Request(f"{BASE_URL}/api/auth/login", data=cust_payload,
                                                headers={"Content-Type": "application/json"}))
        self.assert_true(r1.status == 200, "Step A: Customer logged in")
        me1 = json.loads(opener.open(f"{BASE_URL}/api/auth/me").read().decode())
        self.assert_true(me1.get("role") == "user", "Step A: Current role is 'user'")

        # Verify customer CANNOT call admin API
        try:
            opener.open(f"{BASE_URL}/api/admin/orders")
            self.assert_true(False, "Customer should not access admin orders")
        except urllib.error.HTTPError as e:
            self.assert_true(e.code == 401, "Step A: Admin endpoint rejected customer with 401")

        # Step B: Log in as Admin in the SAME session / cookiejar
        admin_payload = json.dumps({"email": "admin@laptophub.pk", "password": "AdminPass123!"}).encode()
        r2 = opener.open(urllib.request.Request(f"{BASE_URL}/api/auth/login", data=admin_payload,
                                                headers={"Content-Type": "application/json"}))
        self.assert_true(r2.status == 200, "Step B: Admin logged in")
        me2 = json.loads(opener.open(f"{BASE_URL}/api/auth/me").read().decode())
        self.assert_true(me2.get("role") == "admin", "Step B: Current role elevated to 'admin'")
        adm_orders = opener.open(f"{BASE_URL}/api/admin/orders")
        self.assert_true(adm_orders.status == 200, "Step B: Admin can now access admin orders (HTTP 200)")

        # Step C: Sign out admin
        opener.open(urllib.request.Request(f"{BASE_URL}/api/auth/logout", data=b'{}',
                                           headers={"Content-Type": "application/json"}))
        try:
            opener.open(f"{BASE_URL}/api/auth/me")
            self.assert_true(False, "Session should be empty after logout")
        except urllib.error.HTTPError as e:
            self.assert_true(e.code == 401, "Step C: /api/auth/me returns 401 after logout")

        # Step D: Log back in as customer -> confirm completely isolated
        r4 = opener.open(urllib.request.Request(f"{BASE_URL}/api/auth/login", data=cust_payload,
                                                headers={"Content-Type": "application/json"}))
        self.assert_true(r4.status == 200, "Step D: Customer logged back in")
        me4 = json.loads(opener.open(f"{BASE_URL}/api/auth/me").read().decode())
        self.assert_true(me4.get("role") == "user", "Step D: Role is cleanly 'user', zero admin leakage")
        try:
            opener.open(f"{BASE_URL}/api/admin/orders")
            self.assert_true(False, "Customer still has zero admin access")
        except urllib.error.HTTPError as e:
            self.assert_true(e.code == 401, "Step D: Customer verified isolated from admin privileges")

    # ─────────────────────────────────────────────────────────────
    # TEST 6: Immediate Role Revocation on Server
    # ─────────────────────────────────────────────────────────────
    def test_6_immediate_role_revocation(self):
        print("\n>>> 6. Testing Immediate Role Revocation...")
        import sqlite3
        db_path = os.path.join("db", "laptophub.db")
        opener, _ = self.make_opener()

        # Login as admin
        admin_payload = json.dumps({"email": "admin@laptophub.pk", "password": "AdminPass123!"}).encode()
        opener.open(urllib.request.Request(f"{BASE_URL}/api/admin/login", data=admin_payload,
                                           headers={"Content-Type": "application/json"}))
        inv = opener.open(f"{BASE_URL}/api/admin/inventory")
        self.assert_true(inv.status == 200, "Admin logged in and accesses /api/admin/inventory")

        # Temporarily demote admin in SQLite DB
        conn = sqlite3.connect(db_path)
        conn.execute("UPDATE users SET role='user' WHERE email='admin@laptophub.pk'")
        conn.commit()
        conn.close()

        try:
            # Immediate next request must be rejected without server restart
            try:
                opener.open(f"{BASE_URL}/api/admin/inventory")
                self.assert_true(False, "Demoted admin should be rejected immediately")
            except urllib.error.HTTPError as e:
                self.assert_true(e.code == 401, f"Role demotion applies immediately on next call: HTTP {e.code}")

            # Also check /api/auth/me rejects with 401 or returns role != 'admin'
            try:
                me_res = opener.open(f"{BASE_URL}/api/auth/me")
                me_data = json.loads(me_res.read().decode())
                self.assert_true(me_data.get("role") != "admin",
                                 f"Admin role revoked on /api/auth/me (got {me_data.get('role')})")
            except urllib.error.HTTPError as e:
                self.assert_true(e.code == 401, f"Admin session immediately invalidated on /api/auth/me: HTTP {e.code}")
        finally:
            # Restore admin role
            conn = sqlite3.connect(db_path)
            conn.execute("UPDATE users SET role='admin' WHERE email='admin@laptophub.pk'")
            conn.commit()
            conn.close()
            print("  [INFO] Restored admin role in database")

    # ─────────────────────────────────────────────────────────────
    # TEST 7: Static & Dynamic DOM Inspection for Admin Elements
    # ─────────────────────────────────────────────────────────────
    def test_7_dom_static_and_dynamic_inspection(self):
        print("\n>>> 7. Testing Static HTML & Dynamic DOM Rules...")
        with open("laptophub.html", "r", encoding="utf-8") as f:
            html = f.read()

        # 1. Static HTML check: for visitors, no admin link or button in the public page
        # Extract body before script tag
        body_part = html[:html.find("<script>")]
        # Check nav and header
        nav_part = body_part[body_part.find("<nav"):body_part.find("</nav>")]
        self.assert_true("admin" not in nav_part.lower(),
                         "Static nav HTML contains zero admin links, buttons, or text")

        drawer_part = body_part[body_part.find('id="mobileNavDrawer"'):body_part.find('id="mobileNavDrawer"')+600]
        self.assert_true("admin" not in drawer_part.lower(),
                         "Mobile nav drawer static HTML contains zero admin links")

        # 2. Dynamic DOM injection check in script:
        # Verify renderUserNav injects admin link ONLY when currentUser.role === 'admin'
        self.assert_true("const isAdmin = currentUser.role === 'admin';" in html,
                         "renderUserNav strictly checks currentUser.role === 'admin'")
        self.assert_true("const adminDropdownItem = isAdmin ?" in html,
                         "Admin dropdown entry created conditionally via JS template")
        self.assert_true("existingMobileAdmin.remove();" in html,
                         "Non-admin or signed-out states remove mobile admin link from DOM")

        # 3. View Store link check in admin/index.html
        with open("admin/index.html", "r", encoding="utf-8") as f:
            admin_html = f.read()
        self.assert_true('View Store' in admin_html and 'href="../laptophub.html"' in admin_html,
                         "Admin dashboard has clear 'View Store' link back to storefront")
        self.assert_true('pageshow' in admin_html and 'window.location.reload()' in admin_html,
                         "Admin dashboard has bfcache back-button reload handler")


if __name__ == "__main__":
    suite = TestSuite()
    success = suite.run_all()
    sys.exit(0 if success else 1)
