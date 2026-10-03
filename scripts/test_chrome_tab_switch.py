"""
Comprehensive Chrome DevTools Protocol tester for LaptopHUB tab switching.
Connects directly to Chrome headless via lightweight WebSocket client.
"""
import subprocess
import time
import json
import urllib.request
import socket
import base64
import os
import struct

CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

class SimpleWebSocket:
    def __init__(self, host, port, path):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))
        
        # Handshake
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
        
        # Read handshake response
        resp = b""
        while b"\r\n\r\n" not in resp:
            resp += self.sock.recv(4096)
        
        if b"101" not in resp:
            raise RuntimeError(f"WebSocket upgrade failed: {resp.decode('utf-8', errors='ignore')}")

    def send(self, msg_str):
        data = msg_str.encode('utf-8')
        length = len(data)
        
        # Client must mask data
        header = bytearray()
        header.append(0x81) # FIN + text opcode
        
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
        # Read frame
        head = self.sock.recv(2)
        if not head:
            return None
        length = head[1] & 0x7f
        if length == 126:
            length = struct.unpack("!H", self.sock.recv(2))[0]
        elif length == 127:
            length = struct.unpack("!Q", self.sock.recv(8))[0]
            
        is_masked = bool(head[1] & 0x80)
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


def test_tab_switching():
    print("[1] Launching Chrome in headless mode...")
    proc = subprocess.Popen([
        CHROME_PATH,
        "--headless=new",
        "--remote-debugging-port=9222",
        "--disable-gpu",
        "--no-first-run",
        "--no-default-browser-check",
        "--window-size=1280,800",
        "http://localhost:8080/laptophub.html"
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    ws = None
    try:
        # Give Chrome time to initialize and render
        time.sleep(2.5)
        req = urllib.request.urlopen("http://127.0.0.1:9222/json")
        targets = json.loads(req.read().decode())
        page_target = next((t for t in targets if t.get("type") == "page"), None)
        assert page_target is not None, "Target page not found"
        
        ws_url = page_target["webSocketDebuggerUrl"]
        # parse ws_url e.g. ws://127.0.0.1:9222/devtools/page/XYZ
        path = "/" + ws_url.split("/", 3)[3]
        ws = SimpleWebSocket("127.0.0.1", 9222, path)

        msg_id = 1
        def call_cdp(method, params=None):
            nonlocal msg_id
            cur_id = msg_id
            msg_id += 1
            payload = {"id": cur_id, "method": method, "params": params or {}}
            ws.send(json.dumps(payload))
            while True:
                resp = json.loads(ws.recv())
                if resp.get("id") == cur_id:
                    return resp.get("result", {})

        # Enable Runtime
        call_cdp("Runtime.enable")

        def evaluate(js_code):
            res = call_cdp("Runtime.evaluate", {"expression": js_code, "returnByValue": True})
            return res.get("result", {}).get("value")

        print("[2] Page loaded. Checking initial active nav link & lens...")
        initial_state = evaluate("""
            (() => {
                const activeA = document.querySelector('.nav-pill-track a.active');
                const lens = document.querySelector('.glass-lens-highlight');
                return {
                    activeText: activeA ? activeA.innerText.trim() : null,
                    activeHref: activeA ? activeA.getAttribute('href') : null,
                    lensTransform: lens ? lens.style.transform : null,
                    lensWidth: lens ? lens.style.width : null,
                    scrollY: window.scrollY
                };
            })()
        """)
        print("  Initial state:", initial_state)
        assert initial_state["activeHref"] == "#inventory", "Default active link should be #inventory"

        print("\n[3] Clicking 'Consult Me' tab and tracking bubble positions during smooth scroll...")
        # Start tracking lens changes and click Consult Me
        evaluate("""
            (() => {
                window.__lensLog = [];
                const lens = document.querySelector('.glass-lens-highlight');
                const track = document.querySelector('.nav-pill-track');
                const consultLink = Array.from(track.querySelectorAll('a')).find(a => a.getAttribute('href') === '#consult');
                
                // Track every frame
                const interval = setInterval(() => {
                    const activeA = document.querySelector('.nav-pill-track a.active');
                    window.__lensLog.push({
                        time: Date.now(),
                        activeHref: activeA ? activeA.getAttribute('href') : null,
                        lensTransform: lens.style.transform,
                        scrollY: Math.round(window.scrollY)
                    });
                }, 50);
                window.__trackInterval = interval;
                
                // Dispatch click
                consultLink.click();
            })()
        """)

        # Wait 1.5 seconds for smooth scroll to finish
        time.sleep(1.8)

        # Stop tracking and fetch log
        lens_log = evaluate("""
            (() => {
                clearInterval(window.__trackInterval);
                return {
                    log: window.__lensLog,
                    finalScrollY: Math.round(window.scrollY),
                    activeHref: document.querySelector('.nav-pill-track a.active').getAttribute('href'),
                    lensTransform: document.querySelector('.glass-lens-highlight').style.transform
                };
            })()
        """)

        print(f"  After clicking 'Consult Me':")
        print(f"    Final ScrollY: {lens_log['finalScrollY']}px")
        print(f"    Active Tab: {lens_log['activeHref']}")
        print(f"    Lens Transform: {lens_log['lensTransform']}")

        # Verify that during the entire transition, activeHref stayed on #consult and NEVER reverted to #inventory!
        tab_history = [entry['activeHref'] for entry in lens_log['log']]
        print(f"    Tab history samples ({len(tab_history)} samples):", tab_history[::4])
        
        # Check for glitch: Did it ever revert to #inventory while scrolling?
        reverted = any(h == '#inventory' for h in tab_history[2:]) # allow first frame before click
        if reverted:
            print("  [FAIL] GLITCH DETECTED! Active tab reverted to #inventory during scroll!")
            raise AssertionError("Glitch detected: tab reverted during scroll")
        else:
            print("  [PASS] ZERO GLITCHES! Active tab remained solidly on #consult throughout!")

        print("\n[4] Clicking 'All Laptops' tab to scroll back up...")
        evaluate("""
            (() => {
                window.__lensLog = [];
                const lens = document.querySelector('.glass-lens-highlight');
                const track = document.querySelector('.nav-pill-track');
                const inventoryLink = Array.from(track.querySelectorAll('a')).find(a => a.getAttribute('href') === '#inventory');
                
                const interval = setInterval(() => {
                    const activeA = document.querySelector('.nav-pill-track a.active');
                    window.__lensLog.push({
                        time: Date.now(),
                        activeHref: activeA ? activeA.getAttribute('href') : null,
                        lensTransform: lens.style.transform,
                        scrollY: Math.round(window.scrollY)
                    });
                }, 50);
                window.__trackInterval = interval;
                
                inventoryLink.click();
            })()
        """)

        time.sleep(1.8)

        lens_log_up = evaluate("""
            (() => {
                clearInterval(window.__trackInterval);
                return {
                    log: window.__lensLog,
                    finalScrollY: Math.round(window.scrollY),
                    activeHref: document.querySelector('.nav-pill-track a.active').getAttribute('href'),
                    lensTransform: document.querySelector('.glass-lens-highlight').style.transform
                };
            })()
        """)

        print(f"  After clicking 'All Laptops':")
        print(f"    Final ScrollY: {lens_log_up['finalScrollY']}px")
        print(f"    Active Tab: {lens_log_up['activeHref']}")
        print(f"    Lens Transform: {lens_log_up['lensTransform']}")

        tab_history_up = [entry['activeHref'] for entry in lens_log_up['log']]
        print(f"    Tab history samples ({len(tab_history_up)} samples):", tab_history_up[::4])

        reverted_up = any(h == '#consult' for h in tab_history_up[2:])
        if reverted_up:
            print("  [FAIL] GLITCH DETECTED! Active tab reverted to #consult while scrolling back up!")
            raise AssertionError("Glitch detected: tab reverted during scroll up")
        else:
            print("  [PASS] ZERO GLITCHES! Active tab remained solidly on #inventory throughout scroll up!")

        print("\n[5] Rapid tab switching test (Consult Me -> All Laptops -> Consult Me in quick succession)...")
        rapid_result = evaluate("""
            (() => {
                const track = document.querySelector('.nav-pill-track');
                const links = Array.from(track.querySelectorAll('a'));
                const consult = links.find(a => a.getAttribute('href') === '#consult');
                const inv = links.find(a => a.getAttribute('href') === '#inventory');

                consult.click();
                setTimeout(() => inv.click(), 100);
                setTimeout(() => consult.click(), 200);

                return true;
            })()
        """)
        time.sleep(2.0)

        final_rapid = evaluate("""
            (() => {
                const activeA = document.querySelector('.nav-pill-track a.active');
                return {
                    activeHref: activeA ? activeA.getAttribute('href') : null,
                    lensTransform: document.querySelector('.glass-lens-highlight').style.transform,
                    scrollY: Math.round(window.scrollY)
                };
            })()
        """)
        print("  Rapid switch settled state:", final_rapid)
        assert final_rapid["activeHref"] == "#consult", "Should settle on last clicked tab (#consult)"
        print("  [PASS] Rapid switching handled cleanly without locking or freezing!")

        print("\n==========================================")
        print(" ALL TAB SWITCH & BUBBLE TESTS PASSED 100%!")
        print("==========================================")

    finally:
        if ws:
            try:
                ws.close()
            except Exception:
                pass
        proc.terminate()
        try:
            proc.wait(timeout=2)
        except Exception:
            proc.kill()

if __name__ == '__main__':
    test_tab_switching()
