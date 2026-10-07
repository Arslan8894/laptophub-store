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
PORT = 9227
LIVE_URL = "https://arslan8894.github.io/laptophub-store/laptophub.html"

class SimpleWebSocket:
    def __init__(self, host, port, path):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.settimeout(20)
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
        header = bytearray([0x81])
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
            if not chunk: break
            payload += chunk
        if is_masked:
            unmasked = bytearray(len(payload))
            for i in range(len(payload)):
                unmasked[i] = payload[i] ^ mask[i % 4]
            return unmasked.decode('utf-8')
        return payload.decode('utf-8')

    def close(self):
        self.sock.close()

def run_deep_test():
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
        ws_url = page_target["webSocketDebuggerUrl"]
        path = "/" + ws_url.split("/", 3)[3]
        ws = SimpleWebSocket("127.0.0.1", PORT, path)

        msg_id = 1
        def send_cmd(method, params=None):
            nonlocal msg_id
            curr_id = msg_id
            msg_id += 1
            ws.send(json.dumps({"id": curr_id, "method": method, "params": params or {}}))
            return curr_id

        send_cmd("Runtime.enable")
        send_cmd("Page.enable")
        time.sleep(2)

        def eval_js(expression):
            cid = send_cmd("Runtime.evaluate", {
                "expression": expression,
                "returnByValue": True,
                "awaitPromise": True
            })
            start_wait = time.time()
            while time.time() - start_wait < 10:
                raw = ws.recv()
                ev = json.loads(raw)
                if ev.get("id") == cid:
                    res = ev.get("result", {}).get("result", {})
                    return res.get("value")
            return None

        # 1. Test live search
        print("\n--- TEST 1: Live Search ---")
        res1 = eval_js("""
            (() => {
                const input = document.getElementById('laptopSearch');
                if (!input) return { error: 'laptopSearch not found' };
                input.value = 'T14';
                input.dispatchEvent(new Event('input', { bubbles: true }));
                const visible = Array.from(document.querySelectorAll('.pcard')).filter(c => c.offsetParent !== null);
                return { count: visible.length, firstTitle: visible[0] ? visible[0].querySelector('.pcard-title').textContent : null };
            })()
        """)
        print("Search result:", res1)

        # 2. Test brand filter
        print("\n--- TEST 2: Brand Filter Apple ---")
        res2 = eval_js("""
            (() => {
                // Clear search
                const input = document.getElementById('laptopSearch');
                input.value = '';
                input.dispatchEvent(new Event('input', { bubbles: true }));
                
                // Click Apple
                const appleBtn = Array.from(document.querySelectorAll('.brand-btn, .filter-btn, [onclick*="filterBrand"]')).find(b => b.textContent.includes('Apple'));
                if (!appleBtn) return { error: 'Apple button not found' };
                appleBtn.click();
                const visible = Array.from(document.querySelectorAll('.pcard')).filter(c => c.offsetParent !== null);
                return { count: visible.length, brands: Array.from(new Set(visible.map(c => c.getAttribute('data-brand')))) };
            })()
        """)
        print("Apple filter result:", res2)

        # 3. Test Cart Drawer Open & Close
        print("\n--- TEST 3: Cart Drawer ---")
        res3 = eval_js("""
            (() => {
                const cartBtn = document.querySelector('.nav-cart-btn, [onclick*="openCart"]');
                if (!cartBtn) return { error: 'Cart button in nav not found' };
                cartBtn.click();
                const drawer = document.getElementById('cartDrawer');
                const isOpen = drawer && drawer.classList.contains('open');
                const emptyMsg = drawer ? drawer.querySelector('.cart-empty, p')?.textContent : '';
                return { cartBtnFound: true, isOpen, emptyMsg };
            })()
        """)
        print("Cart Drawer result:", res3)

        # 4. Test Customer Auth Modal
        print("\n--- TEST 4: Customer Auth Modal ---")
        res4 = eval_js("""
            (() => {
                const loginBtn = document.querySelector('[onclick*="openLoginModal"], .nav-login-btn');
                if (!loginBtn) return { error: 'Login button not found in nav' };
                loginBtn.click();
                const modal = document.getElementById('loginModal');
                const isOpen = modal && modal.classList.contains('open');
                return { loginBtnFound: true, isOpen };
            })()
        """)
        print("Login Modal result:", res4)

        # 5. Test Live Checkout / COD on static site
        print("\n--- TEST 5: Order COD Flow on Live Site ---")
        res5 = eval_js("""
            (() => {
                // Check what submitOrder does
                return {
                    hasSubmitOrder: typeof submitOrder === 'function',
                    submitOrderStr: typeof submitOrder === 'function' ? submitOrder.toString().slice(0, 300) : 'none'
                };
            })()
        """)
        print("Submit Order implementation:", res5)

        # 6. Test product.html directly
        print("\n--- TEST 6: product.html on Live Site ---")
        eval_js("window.location.href = 'https://arslan8894.github.io/laptophub-store/product.html?id=1'")
        time.sleep(3)
        res6 = eval_js("""
            (() => {
                const title = document.querySelector('h1')?.textContent;
                const price = document.querySelector('#productPrice, .prod-price, .price')?.textContent;
                const addBtn = document.querySelector('#addToCartBtn, [onclick*="addToCart"]');
                const waBtn = document.querySelector('#buyWaBtn, [onclick*="whatsapp"]');
                
                // Click Add to Cart
                let cartUpdated = false;
                if (addBtn) {
                    addBtn.click();
                    const badge = document.querySelector('#cartCount, .cart-badge')?.textContent;
                    cartUpdated = badge;
                }
                
                return {
                    title,
                    price,
                    hasAddBtn: addBtn !== null,
                    cartBadgeAfterClick: cartUpdated,
                    waHref: waBtn ? waBtn.href || waBtn.getAttribute('onclick') : null
                };
            })()
        """)
        print("Product page test result:", res6)

        # 7. Test consult.html on Live Site
        print("\n--- TEST 7: consult.html on Live Site ---")
        eval_js("window.location.href = 'https://arslan8894.github.io/laptophub-store/consult.html'")
        time.sleep(3)
        res7 = eval_js("""
            (() => {
                const step1Active = document.querySelector('.step-card.active, .quiz-step.active, #step1');
                const firstOption = document.querySelector('.quiz-option, .usecase-option, [data-usecase]');
                let nextStepWorked = false;
                if (firstOption) {
                    firstOption.click();
                    const nextBtn = document.querySelector('.btn-next, #nextBtn, [onclick*="nextStep"]');
                    if (nextBtn) {
                        nextBtn.click();
                        nextStepWorked = true;
                    }
                }
                return {
                    title: document.title,
                    hasStep1: step1Active !== null,
                    step1Tag: step1Active ? step1Active.className : 'not found',
                    firstOptionFound: firstOption !== null,
                    nextStepWorked
                };
            })()
        """)
        print("Consult page test result:", res7)

    finally:
        if ws: ws.close()
        proc.terminate()
        proc.wait()

if __name__ == '__main__':
    run_deep_test()
