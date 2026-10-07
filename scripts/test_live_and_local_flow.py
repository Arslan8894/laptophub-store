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
PORT = 9228

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
        length = b2 & 0x7F
        if length == 126:
            length = struct.unpack("!H", self.sock.recv(2))[0]
        elif length == 127:
            length = struct.unpack("!Q", self.sock.recv(8))[0]
        mask = self.sock.recv(4) if (b2 & 0x80) != 0 else None
        payload = b""
        while len(payload) < length:
            chunk = self.sock.recv(length - len(payload))
            if not chunk: break
            payload += chunk
        if mask:
            unmasked = bytearray(len(payload))
            for i in range(len(payload)):
                unmasked[i] = payload[i] ^ mask[i % 4]
            return unmasked.decode('utf-8')
        return payload.decode('utf-8')

    def close(self):
        self.sock.close()

def run_tests_on_target(target_base, is_live=False):
    label = "LIVE GITHUB PAGES" if is_live else "LOCAL SERVER (localhost:8080)"
    print("\n" + "=" * 70)
    print(f"  TESTING {label}")
    print(f"  Base URL: {target_base}")
    print("=" * 70)

    start_url = target_base + "/laptophub.html" if not target_base.endswith('/') else target_base + "laptophub.html"
    proc = subprocess.Popen([
        CHROME_PATH,
        "--headless=new",
        f"--remote-debugging-port={PORT}",
        "--disable-gpu",
        "--no-first-run",
        "--no-default-browser-check",
        "--window-size=1280,900",
        start_url
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

        # ── Test 1: laptophub.html search with debounce ──
        print("\n[TEST 1] Testing Search Filter...")
        s_res = eval_js("""
            new Promise(resolve => {
                const input = document.getElementById('laptopSearch');
                if (!input) return resolve({ error: 'laptopSearch element missing' });
                input.value = 'ThinkPad';
                input.dispatchEvent(new Event('input', { bubbles: true }));
                setTimeout(() => {
                    const cards = Array.from(document.querySelectorAll('.pcard'));
                    const visible = cards.filter(c => c.offsetParent !== null);
                    resolve({ totalCards: cards.length, visibleCards: visible.length, sampleName: visible[0]?.querySelector('.pcard-title')?.textContent });
                }, 350);
            })
        """)
        print(f"  Search result: {s_res}")

        # ── Test 2: Brand filter pills ──
        print("\n[TEST 2] Testing Brand Filter (Dell)...")
        b_res = eval_js("""
            (() => {
                const input = document.getElementById('laptopSearch');
                if (input) { input.value = ''; input.dispatchEvent(new Event('input', { bubbles: true })); }
                const dellBtn = Array.from(document.querySelectorAll('.brand-btn, .filter-btn')).find(b => b.textContent.trim().toLowerCase() === 'dell');
                if (!dellBtn) return { error: 'Dell filter button not found' };
                dellBtn.click();
                const visible = Array.from(document.querySelectorAll('.pcard')).filter(c => c.offsetParent !== null);
                const brands = Array.from(new Set(visible.map(c => c.getAttribute('data-brand'))));
                return { visibleCount: visible.length, brands };
            })()
        """)
        print(f"  Dell filter result: {b_res}")

        # ── Test 3: Hover-to-expand card ──
        print("\n[TEST 3] Testing Hover-to-Expand Card System...")
        h_res = eval_js("""
            (() => {
                const hexOverlay = document.getElementById('hoverExpandOverlay');
                const hexCard = document.getElementById('hoverExpandCard');
                const firstCard = document.querySelector('.pcard');
                const hasHandler = firstCard ? (typeof handleCardClick === 'function' || firstCard.onclick !== null) : false;
                const hasHexInit = typeof window.initHoverExpand === 'function';
                return {
                    hasOverlay: hexOverlay !== null,
                    hasHexCard: hexCard !== null,
                    hasHexInit,
                    hasCardClickHandler: hasHandler
                };
            })()
        """)
        print(f"  Hover-to-expand DOM check: {h_res}")

        # ── Test 4: Navigation to product.html ──
        print("\n[TEST 4] Testing product.html?id=1...")
        prod_target = (target_base.rstrip('/') + '/product.html?id=1')
        eval_js(f"window.location.href = '{prod_target}'")
        time.sleep(3)
        p_res = eval_js("""
            (() => {
                const title = document.querySelector('.product-title, h1')?.textContent?.trim();
                const price = document.querySelector('#productPrice, .prod-price, .price')?.textContent?.trim();
                const btnAdd = document.getElementById('btnAddToCart');
                const btnCod = document.getElementById('btnOrderCod');
                const ramSel = document.getElementById('ramSelect');
                const storSel = document.getElementById('storageSelect');
                
                // Try clicking Add to Cart
                let cartDrawerOpened = false;
                if (btnAdd) {
                    btnAdd.click();
                    const drawer = document.getElementById('cartDrawer');
                    cartDrawerOpened = drawer ? drawer.classList.contains('open') : false;
                }
                
                return {
                    title,
                    price,
                    hasAddBtn: btnAdd !== null,
                    hasCodBtn: btnCod !== null,
                    hasRamSelect: ramSel !== null,
                    hasStorageSelect: storSel !== null,
                    cartDrawerOpenedAfterAdd: cartDrawerOpened
                };
            })()
        """)
        print(f"  product.html test result: {p_res}")

        # ── Test 5: Consult Wizard flow ──
        print("\n[TEST 5] Testing Consult Wizard Flow (consult.html)...")
        consult_target = (target_base.rstrip('/') + '/consult.html')
        eval_js(f"window.location.href = '{consult_target}'")
        time.sleep(3)
        c_res = eval_js("""
            (() => {
                const stepPanels = document.querySelectorAll('.step-panel');
                const activePanel = document.querySelector('.step-panel.active');
                const options = activePanel ? activePanel.querySelectorAll('.option-tile, .usecase-card, [onclick*="select"]') : [];
                
                // Select first option
                let selectedOption = null;
                if (options.length > 0) {
                    options[0].click();
                    selectedOption = options[0].textContent.trim().slice(0, 30);
                }
                
                const nextBtn = document.querySelector('.btn-next, [onclick*="nextStep"], #nextBtn');
                let nextClicked = false;
                if (nextBtn) {
                    nextBtn.click();
                    nextClicked = true;
                }
                
                const newActivePanel = document.querySelector('.step-panel.active');
                
                return {
                    totalStepPanels: stepPanels.length,
                    initialActivePanelId: activePanel?.id,
                    optionsInStep1: options.length,
                    selectedOption,
                    nextBtnFound: nextBtn !== null,
                    newActivePanelId: newActivePanel?.id
                };
            })()
        """)
        print(f"  consult.html wizard step 1->2 result: {c_res}")

        # ── Test 6: Complete Consult Wizard to Results ──
        print("\n[TEST 6] Completing Consult Wizard to Recommendations...")
        rec_res = eval_js("""
            new Promise(resolve => {
                try {
                    // Step 2: Budget
                    const p2 = document.querySelector('.step-panel.active');
                    const bOpts = p2 ? p2.querySelectorAll('.option-tile, [onclick*="select"]') : [];
                    if (bOpts.length > 0) bOpts[0].click();
                    const n2 = document.querySelector('.btn-next, [onclick*="nextStep"], #nextBtn');
                    if (n2) n2.click();

                    setTimeout(() => {
                        // Step 3: Preferences
                        const p3 = document.querySelector('.step-panel.active');
                        const pOpts = p3 ? p3.querySelectorAll('.option-tile, [onclick*="select"]') : [];
                        if (pOpts.length > 0) pOpts[0].click();
                        const n3 = document.querySelector('.btn-next, [onclick*="nextStep"], #nextBtn');
                        if (n3) n3.click();

                        setTimeout(() => {
                            // Step 4: Finalize / Submit
                            const p4 = document.querySelector('.step-panel.active');
                            const subBtn = document.querySelector('.btn-submit, [onclick*="generate"], [onclick*="submit"], .btn-next');
                            if (subBtn) subBtn.click();

                            setTimeout(() => {
                                const resView = document.getElementById('resultsView') || document.querySelector('.results-container, .recommendations');
                                const matchCards = document.querySelectorAll('.rec-card, .match-card, .pcard');
                                resolve({
                                    hasResults: resView !== null,
                                    matchCardsCount: matchCards.length
                                });
                            }, 500);
                        }, 300);
                    }, 300);
                } catch(e) {
                    resolve({ error: e.toString() });
                }
            })
        """)
        print(f"  Consult recommendations result: {rec_res}")

        # ── Test 7: Admin Login page ──
        print("\n[TEST 7] Testing Admin Login Page (admin/login.html)...")
        admin_target = (target_base.rstrip('/') + '/admin/login.html')
        eval_js(f"window.location.href = '{admin_target}'")
        time.sleep(3)
        a_res = eval_js("""
            (() => {
                const emailInp = document.getElementById('adminEmail') || document.querySelector('input[type="email"]');
                const passInp = document.getElementById('adminPass') || document.querySelector('input[type="password"]');
                const submitBtn = document.querySelector('button[type="submit"], .btn-login');
                const hasFirebaseAuth = typeof firebase !== 'undefined' || typeof window.firebaseAuth !== 'undefined';
                return {
                    hasEmailInput: emailInp !== null,
                    hasPassInput: passInp !== null,
                    hasSubmitBtn: submitBtn !== null,
                    hasFirebaseSDK: hasFirebaseAuth
                };
            })()
        """)
        print(f"  admin/login.html test result: {a_res}")

    finally:
        if ws: ws.close()
        proc.terminate()
        proc.wait()

if __name__ == '__main__':
    # Test Live Site
    run_tests_on_target("https://arslan8894.github.io/laptophub-store/", is_live=True)
    # Test Local Site
    run_tests_on_target("http://localhost:8080", is_live=False)
