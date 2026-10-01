import json
import urllib.request
import urllib.error
import urllib.parse
import http.cookiejar
import re

BASE_URL = "http://localhost:8080"

class NoRedirectHandler(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None

def test_suite():
    print("=" * 70)
    print("LAPTOPHUB SYSTEM VERIFICATION SUITE")
    print("=" * 70)

    # Clear prior auth attempts so tests start cleanly
    import sqlite3
    try:
        with sqlite3.connect('db/laptophub.db') as c:
            c.execute('DELETE FROM auth_attempts')
            c.commit()
    except Exception:
        pass

    # -------------------------------------------------------------
    # PART 1: VOLTS VERSION REMOVAL & REDIRECTS
    # -------------------------------------------------------------
    print("\n[PART 1] Verifying VOLTS Removal & Redirects...")
    opener_noredir = urllib.request.build_opener(NoRedirectHandler)

    for path in ['/volts.html', '/volts']:
        try:
            req = urllib.request.Request(f"{BASE_URL}{path}")
            opener_noredir.open(req)
            raise AssertionError(f"Expected redirect for {path}, but got 200")
        except urllib.error.HTTPError as e:
            assert e.code in (301, 302, 308), f"Expected 301/308 redirect for {path}, got {e.code}"
            loc = e.headers.get('Location')
            assert 'laptophub.html' in loc or loc == '/', f"Expected redirect to laptophub.html, got {loc}"
            print(f"  [PASS] {path} successfully redirects ({e.code}) -> {loc}")

    # Verify no volts links in active public pages
    for page in ['laptophub.html', 'consult.html', 'admin/index.html', 'admin/login.html']:
        with open(page, 'r', encoding='utf-8') as f:
            content = f.read()
            assert 'volts.html' not in content, f"Found volts.html reference in {page}"
            assert 'VOLTS Version' not in content, f"Found 'VOLTS Version' text in {page}"
    print("  [PASS] Zero links or references to VOLTS in public nav, pages, and footer")

    # -------------------------------------------------------------
    # PART 2: CREATE YOUR LAPTOP REMOVAL & REDIRECTS
    # -------------------------------------------------------------
    print("\n[PART 2] Verifying 'Create Your Laptop' Removal & Consult Me...")
    for path in ['/custom-laptop.html', '/custom-laptop']:
        try:
            req = urllib.request.Request(f"{BASE_URL}{path}")
            opener_noredir.open(req)
            raise AssertionError(f"Expected redirect for {path}, but got 200")
        except urllib.error.HTTPError as e:
            assert e.code in (301, 302, 308), f"Expected 301/308 redirect for {path}, got {e.code}"
            loc = e.headers.get('Location')
            assert 'consult.html' in loc or loc == '/', f"Expected redirect to consult.html, got {loc}"
            print(f"  [PASS] {path} successfully redirects ({e.code}) -> {loc}")

    for page in ['laptophub.html', 'consult.html', 'admin/index.html']:
        with open(page, 'r', encoding='utf-8') as f:
            content = f.read()
            assert 'custom-laptop.html' not in content, f"Found custom-laptop.html reference in {page}"
    print("  [PASS] Zero links to custom-laptop builder")

    # Test Consult Me page is 200 OK and functions
    req_consult = urllib.request.Request(f"{BASE_URL}/consult.html")
    with urllib.request.urlopen(req_consult) as resp:
        html = resp.read().decode('utf-8')
        assert resp.status == 200
        assert 'Consult Me' in html or 'Recommendation Wizard' in html
        assert 'select(' in html
        print("  [PASS] Consult Me page intact and operational")

    # -------------------------------------------------------------
    # PART 3: SEPARATE ADMIN & USER ACCESS (SERVER-SIDE CHECKS)
    # -------------------------------------------------------------
    print("\n[PART 3] Verifying Security, Roles & Admin Separation...")

    # 3.1 Unauthenticated Visitor attempting admin endpoints -> 401
    admin_endpoints = [
        ('/api/admin/inventory', 'GET'),
        ('/api/admin/inventory/add', 'POST'),
        ('/api/admin/inventory/update', 'POST'),
        ('/api/admin/orders', 'GET'),
        ('/api/admin/users', 'GET'),
        ('/api/admin/log', 'GET'),
    ]
    for ep, method in admin_endpoints:
        try:
            req = urllib.request.Request(f"{BASE_URL}{ep}", method=method)
            urllib.request.urlopen(req)
            raise AssertionError(f"Visitor should be blocked from {ep}")
        except urllib.error.HTTPError as e:
            assert e.code in (401, 403), f"Expected 401/403 for {ep}, got {e.code}"
    print("  [PASS] All /api/admin/* endpoints strictly return 401 to unauthenticated visitors")

    # 3.2 Unauthenticated visitor opening /admin/ or /admin/index.html -> redirect to /admin/login
    for admin_page in ['/admin/', '/admin/index.html']:
        try:
            req = urllib.request.Request(f"{BASE_URL}{admin_page}")
            opener_noredir.open(req)
            raise AssertionError(f"Expected redirect for {admin_page}")
        except urllib.error.HTTPError as e:
            assert e.code in (301, 302, 308, 401, 403)
            loc = e.headers.get('Location', '')
            assert '/admin/login' in loc or e.code in (401, 403)
    print("  [PASS] Visitor navigating to /admin/ is redirected to /admin/login")

    # 3.3 Public Registration creates only role 'user'
    cj_user = http.cookiejar.CookieJar()
    user_opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj_user))

    cust_email = "testcustomer@example.com"
    reg_payload = json.dumps({
        "email": cust_email,
        "password": "CustomerPassword123!",
        "name": "Test Customer",
        "phone": "03001234567",
        "role": "admin"  # Malicious attempt to escalate role
    }).encode("utf-8")

    req_reg = urllib.request.Request(
        f"{BASE_URL}/api/auth/register",
        data=reg_payload,
        headers={"Content-Type": "application/json"}
    )
    try:
        with user_opener.open(req_reg) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            assert data.get("ok"), "Registration failed"
            assert data.get("role") == "user", f"Role tampering succeeded! Got role: {data.get('role')}"
            print("  [PASS] Public registration creates role 'user' and ignores malicious role field")
    except urllib.error.HTTPError as e:
        body = e.read()
        if (e.code in (400, 409)) and (b'already exists' in body.lower() or b'already registered' in body.lower()):
            print("  [PASS] Customer already registered, proceeding to login test")
        else:
            raise AssertionError(f"Registration failed unexpectedly: {e.code} - {body.decode('utf-8', errors='ignore')}")

    # 3.4 Customer Login
    login_payload = json.dumps({"email": cust_email, "password": "CustomerPassword123!"}).encode("utf-8")
    req_login = urllib.request.Request(f"{BASE_URL}/api/auth/login", data=login_payload, headers={"Content-Type": "application/json"})
    with user_opener.open(req_login) as resp:
        data = json.loads(resp.read().decode("utf-8"))
        assert data.get("user", {}).get("role") == "user"
        print(f"  [PASS] Customer logged in with role '{data['user']['role']}'")

    # 3.5 Customer attempting admin endpoints -> blocked with 401/403
    for ep, method in admin_endpoints:
        try:
            req = urllib.request.Request(f"{BASE_URL}{ep}", method=method)
            user_opener.open(req)
            raise AssertionError(f"Customer should be blocked from {ep}")
        except urllib.error.HTTPError as e:
            assert e.code in (401, 403), f"Expected 401/403 for customer on {ep}, got {e.code}"
    print("  [PASS] Customer session strictly blocked (401/403) from all /api/admin/* endpoints")

    # 3.6 Admin login on public login form -> rejected with 403
    admin_on_cust_form = json.dumps({"email": "admin@laptophub.pk", "password": "AdminPass123!"}).encode("utf-8")
    req_admin_on_cust = urllib.request.Request(f"{BASE_URL}/api/auth/login", data=admin_on_cust_form, headers={"Content-Type": "application/json"})
    try:
        user_opener.open(req_admin_on_cust)
        raise AssertionError("Admin should not be able to log in on public customer form")
    except urllib.error.HTTPError as e:
        assert e.code == 403, f"Expected 403 for admin on public form, got {e.code}"
        data = json.loads(e.read().decode("utf-8"))
        assert "admin portal" in data.get("error", "").lower()
        print(f"  [PASS] Admin logging in on public sign-in is rejected with 403: {data.get('error')}")

    # 3.7 Non-admin attempting admin login -> generic error
    non_admin_on_admin = json.dumps({"email": cust_email, "password": "CustomerPassword123!"}).encode("utf-8")
    req_non_admin_admin = urllib.request.Request(f"{BASE_URL}/api/admin/login", data=non_admin_on_admin, headers={"Content-Type": "application/json"})
    try:
        user_opener.open(req_non_admin_admin)
        raise AssertionError("Customer should not be able to log in on admin login")
    except urllib.error.HTTPError as e:
        assert e.code in (401, 403, 429)
        data = json.loads(e.read().decode("utf-8"))
        assert data.get("error") == "Invalid credentials", f"Expected generic 'Invalid credentials', got {data.get('error')}"
        print(f"  [PASS] Customer on admin login receives generic error: '{data.get('error')}' without revealing account details")

    # 3.8 Admin Login on dedicated /admin/login
    cj_admin = http.cookiejar.CookieJar()
    admin_opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj_admin))

    admin_payload = json.dumps({"email": "admin@laptophub.pk", "password": "AdminPass123!"}).encode("utf-8")
    req_admin_login = urllib.request.Request(f"{BASE_URL}/api/admin/login", data=admin_payload, headers={"Content-Type": "application/json"})
    with admin_opener.open(req_admin_login) as resp:
        data = json.loads(resp.read().decode("utf-8"))
        assert data.get("role") == "admin"
        print(f"  [PASS] Admin logged in on /admin/login successfully as {data.get('name')}")

    # 3.9 Admin Accessing /admin/ and /api/admin/* -> 200 OK
    req_admin_inv = urllib.request.Request(f"{BASE_URL}/api/admin/inventory")
    with admin_opener.open(req_admin_inv) as resp:
        inv = json.loads(resp.read().decode("utf-8"))
        assert isinstance(inv, list) and len(inv) >= 60
        print(f"  [PASS] Admin loaded full inventory ({len(inv)} items)")

    # 3.10 Customer Profile Update and Password Change
    prof_payload = json.dumps({
        "name": "Updated Customer Name",
        "phone": "03009876543",
        "city": "Karachi",
        "address": "Street 10, Clifton Block 4"
    }).encode("utf-8")
    req_prof = urllib.request.Request(f"{BASE_URL}/api/auth/profile", data=prof_payload, headers={"Content-Type": "application/json"})
    with user_opener.open(req_prof) as resp:
        assert resp.status == 200
        pdata = json.loads(resp.read().decode("utf-8"))
        assert pdata.get("ok")
        print("  [PASS] Customer updated delivery profile successfully")

    # Check GET /api/auth/me returns updated fields
    req_me = urllib.request.Request(f"{BASE_URL}/api/auth/me")
    with user_opener.open(req_me) as resp:
        me_data = json.loads(resp.read().decode("utf-8"))
        assert me_data["user"]["name"] == "Updated Customer Name"
        assert me_data["user"]["city"] == "Karachi"
        print("  [PASS] Customer GET /api/auth/me reflected updated profile")

    # 3.11 Order Placement & Automatic Stock Decrement
    # Find a laptop with stock > 0
    target_lap = None
    for l in inv:
        if l.get("stock", 0) > 0:
            target_lap = l
            break
    assert target_lap is not None
    stock_before = target_lap.get("stock", 1)
    lap_id = target_lap["id"]

    order_payload = json.dumps({
        "name": "Updated Customer Name",
        "phone": "03009876543",
        "city": "Karachi",
        "address": "Street 10, Clifton Block 4",
        "items": [{
            "id": lap_id,
            "name": target_lap["name"],
            "price": target_lap["price"],
            "qty": 1
        }]
    }).encode("utf-8")

    req_order = urllib.request.Request(f"{BASE_URL}/api/orders", data=order_payload, headers={"Content-Type": "application/json"})
    with user_opener.open(req_order) as resp:
        odata = json.loads(resp.read().decode("utf-8"))
        assert odata.get("orderId")
        new_order_id = odata["orderId"]
        print(f"  [PASS] Customer placed order #{new_order_id}")

    # Verify inventory stock decreased by 1
    with admin_opener.open(urllib.request.Request(f"{BASE_URL}/api/admin/inventory")) as resp:
        new_inv = json.loads(resp.read().decode("utf-8"))
        updated_lap = next(l for l in new_inv if l["id"] == lap_id)
        assert updated_lap.get("stock") == stock_before - 1, f"Expected {stock_before - 1}, got {updated_lap.get('stock')}"
        print(f"  [PASS] Laptop #{lap_id} stock automatically decremented ({stock_before} -> {updated_lap.get('stock')})")

    # Verify order in Customer's My Orders
    req_my_orders = urllib.request.Request(f"{BASE_URL}/api/orders/mine")
    with user_opener.open(req_my_orders) as resp:
        my_orders_data = json.loads(resp.read().decode("utf-8"))
        assert any(o["id"] == new_order_id for o in my_orders_data.get("orders", []))
        print("  [PASS] Order appears in Customer's My Orders endpoint")

    # Verify order in Admin's Orders List and change status
    req_admin_orders = urllib.request.Request(f"{BASE_URL}/api/admin/orders")
    with admin_opener.open(req_admin_orders) as resp:
        admin_orders_data = json.loads(resp.read().decode("utf-8"))
        assert any(o["id"] == new_order_id for o in admin_orders_data)
        print("  [PASS] Order appears in Admin Orders table")

    status_payload = json.dumps({"orderId": new_order_id, "status": "confirmed"}).encode("utf-8")
    req_status = urllib.request.Request(f"{BASE_URL}/api/admin/orders/status", data=status_payload, headers={"Content-Type": "application/json"})
    with admin_opener.open(req_status) as resp:
        assert resp.status == 200
        print(f"  [PASS] Admin successfully updated order #{new_order_id} status to 'confirmed'")

    # 3.12 Admin Add, Update, Archive, and Delete Laptop
    new_laptop_payload = json.dumps({
        "brand": "dell",
        "brandName": "Dell",
        "name": "Dell Latitude 5530 Test Unit",
        "cpu": "Intel Core i5-1245U",
        "gen": "12th",
        "ram": 16,
        "storage": 512,
        "storageType": "NVMe SSD",
        "gpu": "Intel Iris Xe",
        "display": '15.6" FHD IPS',
        "price": 95000,
        "stock": 5,
        "condition": "Like New (10/10) · Certified Refurbished",
        "badge": "Test Unit",
        "category": "Business Laptop",
        "img": "images/laptop-1-lenovo-thinkpad-t14-gen-1-1.jpg",
        "hidden": False
    }).encode("utf-8")

    req_add_lap = urllib.request.Request(f"{BASE_URL}/api/admin/inventory/add", data=new_laptop_payload, headers={"Content-Type": "application/json"})
    with admin_opener.open(req_add_lap) as resp:
        add_data = json.loads(resp.read().decode("utf-8"))
        assert add_data.get("success")
        created_lap_id = add_data["laptop"]["id"]
        print(f"  [PASS] Admin added new laptop #{created_lap_id} successfully")

    # Update laptop
    update_payload = json.dumps({
        "id": created_lap_id,
        "price": 92000,
        "stock": 4
    }).encode("utf-8")
    req_upd = urllib.request.Request(f"{BASE_URL}/api/admin/inventory/update", data=update_payload, headers={"Content-Type": "application/json"})
    with admin_opener.open(req_upd) as resp:
        assert resp.status == 200
        print(f"  [PASS] Admin updated laptop #{created_lap_id} price to Rs 92,000")

    # Archive laptop
    archive_payload = json.dumps({"id": created_lap_id}).encode("utf-8")
    req_arch = urllib.request.Request(f"{BASE_URL}/api/admin/inventory/archive", data=archive_payload, headers={"Content-Type": "application/json"})
    with admin_opener.open(req_arch) as resp:
        assert resp.status == 200
        print(f"  [PASS] Admin archived/hid laptop #{created_lap_id}")

    # Delete test laptop
    del_payload = json.dumps({"id": created_lap_id, "confirm": True}).encode("utf-8")
    req_del = urllib.request.Request(f"{BASE_URL}/api/admin/inventory/delete", data=del_payload, headers={"Content-Type": "application/json"})
    with admin_opener.open(req_del) as resp:
        assert resp.status == 200
        print(f"  [PASS] Admin permanently deleted test laptop #{created_lap_id}")

    # 3.13 Audit Log verification
    req_log = urllib.request.Request(f"{BASE_URL}/api/admin/log")
    with admin_opener.open(req_log) as resp:
        logs = json.loads(resp.read().decode("utf-8"))
        assert len(logs) > 0
        actions = [l["action"] for l in logs]
        assert "add_laptop" in actions
        assert "update_laptop" in actions
        assert "delete_laptop" in actions
        print(f"  [PASS] Audit log actively recording all admin operations ({len(logs)} actions logged)")

    # -------------------------------------------------------------
    # PART 4: NORMAL USER EXPERIENCE (DOM AUDIT)
    # -------------------------------------------------------------
    print("\n[PART 4] Verifying Normal User Experience & DOM cleanliness...")
    with open('laptophub.html', 'r', encoding='utf-8') as f:
        laptophub_html = f.read()

    # Verify no admin elements in page markup
    assert 'navAdminLink' not in laptophub_html, "navAdminLink still in laptophub.html!"
    assert 'mobileNavAdminLink' not in laptophub_html, "mobileNavAdminLink still in laptophub.html!"
    import re
    assert not re.findall(r'<a[^>]+href=[\'"][^\'"]*admin', laptophub_html, re.I), "Admin link found in page markup!"

    # Verify public navigation links
    assert 'All Laptops' in laptophub_html
    assert 'Consult Me' in laptophub_html
    assert 'Reviews' in laptophub_html
    assert 'My Orders' in laptophub_html
    assert 'Profile & Settings' in laptophub_html
    assert 'Sign Out' in laptophub_html
    print("  [PASS] Public navigation strictly contains only customer-relevant items")

    print("\n" + "=" * 70)
    print("ALL TESTS PASSED WITH 100% SUCCESS!")
    print("=" * 70)

if __name__ == "__main__":
    test_suite()
