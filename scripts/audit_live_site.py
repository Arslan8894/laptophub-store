import subprocess
import time
import json
import urllib.request
import socket
import base64
import os
import struct
import sys

CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
PORT = 9226
LIVE_URL = "https://arslan8894.github.io/laptophub-store/"

class SimpleWebSocket:
    def __init__(self, host, port, path):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.settimeout(15)
        self.sock.connect((host, port))
        
        key = base64.b64encode(os.urandom(16)).decode('utf-8')
        headers = [
            f"GET {path} HTTP/1.1",
            f"Host: {host}:{port}",
            "Upgrade: websocket",
            "Connection: Upgrade",
            f"Sec-WebSocket-Key: {key}",
            "Sec-WebSocket-Version: 13",
            "\r\n"
        ]
        self.sock.sendall("\r\n".join(headers).encode('utf-8'))
        
        resp = b""
        while b"\r\n\r\n" not in resp:
            resp += self.sock.recv(4096)
        
        if b"101" not in resp:
            raise RuntimeError(f"WebSocket upgrade failed: {resp.decode('utf-8', errors='ignore')}")

    def send(self, msg_str):
        data = msg_str.encode('utf-8')
        length = len(data)
        
        header = bytearray()
        header.append(0x81)
        
        mask_key = os.urandom(4)
        if length <= 125:
            header.append(0x80 | length)
        elif length <= 65535:
            header.append(0x80 | 126)
            header.extend(struct.pack("!H", length))
        else:
            header.append(0x80 | 127)
            header.extend(struct.pack("!Q", length))
            
        header.extend(mask_key)
        masked_data = bytearray(length)
        for i in range(length):
            masked_data[i] = data[i] ^ mask_key[i % 4]
            
        self.sock.sendall(header + masked_data)

    def recv(self):
        b1, b2 = self.sock.recv(2)
        opcode = b1 & 0x0F
        is_masked = (b2 & 0x80) != 0
        length = b2 & 0x7F
        
        if length == 126:
            length = struct.unpack("!H", self.sock.recv(2))[0]
        elif length == 127:
            length = struct.unpack("!Q", self.sock.recv(8))[0]
            
        mask = self.sock.recv(4) if is_masked else None
        
        payload = b""
        while len(payload) < length:
            chunk = self.sock.recv(length - len(payload))
            if not chunk:
                break
            payload += chunk
            
        if is_masked:
            unmasked = bytearray(len(payload))
            for i in range(len(payload)):
                unmasked[i] = payload[i] ^ mask[i % 4]
            return unmasked.decode('utf-8')
        return payload.decode('utf-8')

    def close(self):
        self.sock.close()

def audit_live_site():
    print("=" * 70)
    print("   LIVE GITHUB PAGES STORE AUDIT VIA CHROME HEADLESS CDP")
    print(f"   Target URL: {LIVE_URL}")
    print("=" * 70)

    proc = subprocess.Popen([
        CHROME_PATH,
        "--headless=new",
        f"--remote-debugging-port={PORT}",
        "--disable-gpu",
        "--no-first-run",
        "--no-default-browser-check",
        "--window-size=1280,900",
        LIVE_URL
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    time.sleep(4)
    ws = None
    try:
        req = urllib.request.urlopen(f"http://127.0.0.1:{PORT}/json")
        targets = json.loads(req.read().decode())
        page_target = next((t for t in targets if t.get("type") == "page"), None)
        assert page_target is not None, "Target page not found"
        
        ws_url = page_target["webSocketDebuggerUrl"]
        path = "/" + ws_url.split("/", 3)[3]
        ws = SimpleWebSocket("127.0.0.1", PORT, path)

        msg_id = 1
        def send_cmd(method, params=None):
            nonlocal msg_id
            curr_id = msg_id
            msg_id += 1
            payload = {"id": curr_id, "method": method, "params": params or {}}
            ws.send(json.dumps(payload))
            return curr_id

        # Enable Network, Page, Runtime, Log
        send_cmd("Network.enable")
        send_cmd("Page.enable")
        send_cmd("Runtime.enable")
        send_cmd("Log.enable")

        failed_requests = []
        console_messages = []
        page_loaded = False

        # Drain initial events
        start_time = time.time()
        while time.time() - start_time < 5:
            try:
                raw = ws.recv()
                ev = json.loads(raw)
                method = ev.get("method", "")
                params = ev.get("params", {})
                
                if method == "Network.responseReceived":
                    resp = params.get("response", {})
                    status = resp.get("status")
                    url = resp.get("url")
                    if status and status >= 400:
                        failed_requests.append({"url": url, "status": status})
                elif method == "Network.loadingFailed":
                    failed_requests.append({
                        "url": params.get("canceled", False),
                        "error": params.get("errorText")
                    })
                elif method == "Runtime.consoleAPICalled":
                    t = params.get("type")
                    args = " ".join([str(a.get("value", a.get("description", ""))) for a in params.get("args", [])])
                    console_messages.append({"type": t, "text": args})
                elif method == "Runtime.exceptionThrown":
                    details = params.get("exceptionDetails", {})
                    text = details.get("text", "")
                    ex = details.get("exception", {}).get("description", "")
                    console_messages.append({"type": "exception", "text": f"{text}: {ex}"})
            except Exception:
                break

        print("\n--- 1. Live Homepage Audit ---")
        def eval_js(expression):
            cid = send_cmd("Runtime.evaluate", {
                "expression": expression,
                "returnByValue": True,
                "awaitPromise": True
            })
            start_wait = time.time()
            while time.time() - start_wait < 5:
                raw = ws.recv()
                ev = json.loads(raw)
                if ev.get("id") == cid:
                    res = ev.get("result", {}).get("result", {})
                    return res.get("value")
            return None

        current_url = eval_js("window.location.href")
        page_title = eval_js("document.title")
        laptop_count = eval_js("document.querySelectorAll('.pcard').length")
        has_nav = eval_js("document.querySelector('nav') !== null || document.querySelector('.main-nav') !== null")
        print(f"  Current URL: {current_url}")
        print(f"  Page Title: {page_title}")
        print(f"  Rendered Laptop Cards (.pcard): {laptop_count}")

        # Check console messages
        print(f"\n--- 2. Console Logs & Errors on Live Homepage ({len(console_messages)} events) ---")
        errors = [c for c in console_messages if c["type"] in ("error", "exception")]
        if errors:
            for err in errors:
                print(f"  [ERROR] {err['type']}: {err['text']}")
        else:
            print("  [OK] Zero console errors on live homepage load.")

        print(f"\n--- 3. Failed Network Requests ({len(failed_requests)} events) ---")
        if failed_requests:
            for fr in failed_requests:
                print(f"  [FAIL] {fr}")
        else:
            print("  [OK] Zero 4xx/5xx network failures.")

        # Test search
        print("\n--- 4. Testing Search Filter on Live Homepage ---")
        search_res = eval_js("""
            (() => {
                const searchInput = document.getElementById('searchInput') || document.querySelector('input[type="search"]');
                if (!searchInput) return { found: false };
                searchInput.value = 'ThinkPad';
                searchInput.dispatchEvent(new Event('input', { bubbles: true }));
                const visible = Array.from(document.querySelectorAll('.pcard')).filter(c => c.offsetParent !== null).length;
                return { found: true, visibleCount: visible };
            })()
        """)
        print(f"  Search for 'ThinkPad': {search_res}")

        # Test brand filter
        print("\n--- 5. Testing Brand Filter Pills ---")
        brand_res = eval_js("""
            (() => {
                const dellBtn = Array.from(document.querySelectorAll('.filter-btn, button')).find(b => b.textContent.trim().toLowerCase() === 'dell');
                if (!dellBtn) return { found: false };
                dellBtn.click();
                const visible = Array.from(document.querySelectorAll('.pcard')).filter(c => c.offsetParent !== null).length;
                return { found: true, visibleDell: visible };
            })()
        """)
        print(f"  Click 'Dell' filter: {brand_res}")

        # Test Cart drawer
        print("\n--- 6. Testing Cart Drawer & Checkout ---")
        cart_res = eval_js("""
            (() => {
                const addBtns = document.querySelectorAll('.btn-add-cart, button[onclick*="addToCart"]');
                const firstAdd = addBtns[0];
                if (!firstAdd) return { addBtnFound: false };
                firstAdd.click();
                const drawer = document.getElementById('cartDrawer');
                const isOpen = drawer ? drawer.classList.contains('open') : false;
                const itemsCount = document.querySelectorAll('.cart-item').length;
                const badgeText = document.getElementById('cartCount') ? document.getElementById('cartCount').textContent : '';
                return { addBtnFound: true, drawerOpen: isOpen, itemsInCart: itemsCount, badge: badgeText };
            })()
        """)
        print(f"  Add to Cart Interaction: {cart_res}")

        # Test WhatsApp Floating Link
        print("\n--- 7. Testing WhatsApp Links ---")
        wa_res = eval_js("""
            (() => {
                const waLinks = Array.from(document.querySelectorAll('a[href*="wa.me"]')).map(a => a.href);
                return { count: waLinks.length, sample: waLinks[0] };
            })()
        """)
        print(f"  WhatsApp Links: {wa_res}")

        # Navigate to product page
        print("\n--- 8. Testing Product Page (product.html?id=1) ---")
        prod_url = LIVE_URL.rstrip('/') + "/product.html?id=1"
        eval_js(f"window.location.href = '{prod_url}'")
        time.sleep(3)
        prod_res = eval_js("""
            (() => {
                const title = document.querySelector('h1') ? document.querySelector('h1').textContent : '';
                const price = document.querySelector('.price, .product-price') ? document.querySelector('.price, .product-price').textContent : '';
                const images = document.querySelectorAll('.gallery-main img, #mainProductImg, img').length;
                const specs = document.querySelectorAll('.spec-row, table tr').length;
                return { title, price, images, specs, url: window.location.href };
            })()
        """)
        print(f"  Product Page Load: {prod_res}")

        # Navigate to consult page
        print("\n--- 9. Testing Consult Page (consult.html) ---")
        consult_url = LIVE_URL.rstrip('/') + "/consult.html"
        eval_js(f"window.location.href = '{consult_url}'")
        time.sleep(3)
        consult_res = eval_js("""
            (() => {
                const title = document.title;
                const step1 = document.querySelector('.step-card, .quiz-step, .question-card');
                const options = document.querySelectorAll('.quiz-option, .usecase-card, .option-btn').length;
                return { title, hasStep1: step1 !== null, optionsCount: options, url: window.location.href };
            })()
        """)
        print(f"  Consult Page Load: {consult_res}")

        # Navigate to admin login page
        print("\n--- 10. Testing Admin Login Page (admin/login.html) ---")
        admin_url = LIVE_URL.rstrip('/') + "/admin/login.html"
        eval_js(f"window.location.href = '{admin_url}'")
        time.sleep(3)
        admin_res = eval_js("""
            (() => {
                const title = document.title;
                const emailInput = document.querySelector('input[type="email"]');
                const passInput = document.querySelector('input[type="password"]');
                return { title, hasInputs: (emailInput !== null && passInput !== null), url: window.location.href };
            })()
        """)
        print(f"  Admin Login Page Load: {admin_res}")

    finally:
        if ws:
            ws.close()
        proc.terminate()
        proc.wait()

if __name__ == '__main__':
    audit_live_site()
