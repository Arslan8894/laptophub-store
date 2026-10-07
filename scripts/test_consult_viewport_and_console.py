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
PORT = 9225

class SimpleWebSocket:
    def __init__(self, host, port, path):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
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


def run_viewport_and_console_tests():
    print("=" * 70)
    print("RUNNING CHROME HEADLESS TEST: VIEWPORTS & CONSOLE AUDIT")
    print("=" * 70)

    # Launch Chrome
    proc = subprocess.Popen([
        CHROME_PATH,
        "--headless=new",
        f"--remote-debugging-port={PORT}",
        "--disable-gpu",
        "--no-first-run",
        "--no-default-browser-check",
        "--window-size=1280,900",
        "http://127.0.0.1:8080/laptophub.html"
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    time.sleep(3)

    try:
        req = urllib.request.urlopen(f"http://127.0.0.1:{PORT}/json")
        targets = json.loads(req.read().decode())
        page_target = next((t for t in targets if t.get("type") == "page"), None)
        assert page_target is not None, "Target page not found"
        
        ws_url = page_target["webSocketDebuggerUrl"]
        path = "/" + ws_url.split("/", 3)[3]
        ws = SimpleWebSocket("127.0.0.1", PORT, path)

        msg_id = 1
        console_errors = []

        def call_cdp(method, params=None):
            nonlocal msg_id
            cur_id = msg_id
            msg_id += 1
            payload = {"id": cur_id, "method": method, "params": params or {}}
            ws.send(json.dumps(payload))
            while True:
                resp = json.loads(ws.recv())
                if resp.get("method") == "Runtime.exceptionThrown":
                    err_details = resp.get("params", {}).get("exceptionDetails", {})
                    console_errors.append(f"Runtime Exception: {err_details.get('text', '')} | {err_details.get('exception', {}).get('description', '')}")
                elif resp.get("method") == "Log.entryAdded":
                    entry = resp.get("params", {}).get("entry", {})
                    if entry.get("level") == "error":
                        console_errors.append(f"Log Error: {entry.get('text', '')} | URL: {entry.get('url', '')}")
                elif resp.get("method") == "Network.responseReceived":
                    res = resp.get("params", {}).get("response", {})
                    if res.get("status") >= 400:
                        console_errors.append(f"Network {res.get('status')}: {res.get('url')}")
                elif resp.get("id") == cur_id:
                    return resp.get("result", {})

        call_cdp("Runtime.enable")
        call_cdp("Log.enable")
        call_cdp("Network.enable")
        call_cdp("Page.enable")

        viewports = [
            ("Desktop", 1280, 900),
            ("Tablet 768px", 768, 1024),
            ("Mobile 390px", 390, 844),
            ("Mobile 360px", 360, 740),
        ]

        print("\n--- Phase A: Testing laptophub.html ---")
        for name, width, height in viewports:
            call_cdp("Emulation.setDeviceMetricsOverride", {
                "width": width,
                "height": height,
                "deviceScaleFactor": 1,
                "mobile": width <= 768
            })
            time.sleep(0.5)

            # Evaluate state on laptophub.html
            res = call_cdp("Runtime.evaluate", {
                "expression": """
                (() => {
                    const consultSec = document.getElementById('consult');
                    const consultChips = document.getElementById('consultChips');
                    const consultMatchesGrid = document.getElementById('consultMatchesGrid');
                    const desktopConsultLink = document.querySelector('.nav-pill-track a[href="consult.html"]');
                    const mobileConsultLink = document.querySelector('#mobileNavDrawer a[href="consult.html"]');
                    
                    return {
                        hasConsultSection: !!consultSec,
                        hasConsultChips: !!consultChips,
                        hasMatchesGrid: !!consultMatchesGrid,
                        hasDesktopConsultLink: !!desktopConsultLink,
                        hasMobileConsultLink: !!mobileConsultLink,
                        innerWidth: window.innerWidth
                    };
                })()
                """,
                "returnByValue": True
            })

            data = res.get("result", {}).get("value", {})
            assert not data.get("hasConsultSection"), f"{name}: #consult section must not exist on homepage"
            assert not data.get("hasConsultChips"), f"{name}: #consultChips must not exist"
            assert not data.get("hasMatchesGrid"), f"{name}: #consultMatchesGrid must not exist"
            assert data.get("hasDesktopConsultLink"), f"{name}: Desktop consult.html link missing"
            assert data.get("hasMobileConsultLink"), f"{name}: Mobile consult.html link missing"
            print(f"  [PASS] {name} ({width}px): Clean homepage, correct nav links, no dead DOM.")

        print(f"  Console errors during laptophub.html tests: {len(console_errors)}")
        if console_errors:
            for err in console_errors:
                print(f"    [ERR]: {err}")
        assert len(console_errors) == 0, f"Found console errors on laptophub.html: {console_errors}"

        print("\n--- Phase B: Navigating to consult.html directly ---")
        call_cdp("Page.navigate", {"url": "http://127.0.0.1:8080/consult.html"})
        time.sleep(2)

        for name, width, height in viewports:
            call_cdp("Emulation.setDeviceMetricsOverride", {
                "width": width,
                "height": height,
                "deviceScaleFactor": 1,
                "mobile": width <= 768
            })
            time.sleep(0.5)

            res = call_cdp("Runtime.evaluate", {
                "expression": """
                (() => {
                    const step1 = document.getElementById('step-1');
                    const step1Active = step1 && step1.classList.contains('active');
                    const wizardCard = document.getElementById('wizard-card');
                    const backBtnStore = document.getElementById('btnBackToStore');
                    const step1Back = document.getElementById('btnStep1Back');
                    const desktopActiveNav = document.querySelector('.nav-pill-track a.active');
                    const scrollY = window.scrollY;

                    return {
                        step1Exists: !!step1,
                        step1Active: step1Active,
                        wizardCardExists: !!wizardCard,
                        backBtnStoreExists: !!backBtnStore,
                        step1BackExists: !!step1Back,
                        desktopActiveText: desktopActiveNav ? desktopActiveNav.textContent.trim() : null,
                        scrollY: scrollY
                    };
                })()
                """,
                "returnByValue": True
            })

            c_data = res.get("result", {}).get("value", {})
            assert c_data.get("step1Exists") and c_data.get("step1Active"), f"{name}: Step 1 must be active on consult.html"
            assert c_data.get("backBtnStoreExists"), f"{name}: Top nav back button missing"
            assert c_data.get("step1BackExists"), f"{name}: Step 1 back button missing"
            assert c_data.get("desktopActiveText") == "Consult Me", f"{name}: Consult Me must be active tab"
            print(f"  [PASS] {name} ({width}px): consult.html ready at top (scrollY={c_data.get('scrollY')}), Step 1 active, active tab highlighted.")

        # Test mobile drawer behavior on mobile viewport
        print("\n--- Phase C: Testing Mobile Nav Drawer Interaction on consult.html (390px) ---")
        call_cdp("Emulation.setDeviceMetricsOverride", {
            "width": 390,
            "height": 844,
            "deviceScaleFactor": 1,
            "mobile": True
        })
        time.sleep(0.3)

        drawer_test = call_cdp("Runtime.evaluate", {
            "expression": """
            (() => {
                // Open drawer
                toggleMobileNav(true);
                const drawer = document.getElementById('mobileNavDrawer');
                const overlay = document.getElementById('mobileNavOverlay');
                const openSuccess = drawer.classList.contains('active') && overlay.classList.contains('active');

                // Simulate clicking "Consult Me" inside drawer
                const consultLink = drawer.querySelector('a[href="consult.html"]');
                if (consultLink) {
                    consultLink.click();
                }

                // Verify drawer auto-closed
                const closedSuccess = !drawer.classList.contains('active') && !overlay.classList.contains('active');

                return {
                    openSuccess: openSuccess,
                    closedSuccess: closedSuccess
                };
            })()
            """,
            "returnByValue": True
        })

        d_res = drawer_test.get("result", {}).get("value", {})
        assert d_res.get("openSuccess"), "Drawer did not open with toggleMobileNav(true)"
        assert d_res.get("closedSuccess"), "Drawer did not close after clicking link"
        print("  [PASS] Mobile nav drawer opened and auto-closed upon link click.")

        # Final check on console errors
        print(f"\n--- Phase D: Total Console Errors across all pages and viewports: {len(console_errors)} ---")
        if console_errors:
            for err in console_errors:
                print(f"  [FAIL ERR]: {err}")
            sys.exit(1)
        else:
            print("  [PASS] ZERO console errors detected on desktop and mobile (360px, 390px, 768px, 1280px)!")

        ws.close()

    finally:
        proc.terminate()
        proc.wait()

    print("\n" + "=" * 70)
    print("ALL VIEWPORT AND CONSOLE AUDITS PASSED CLEANLY!")
    print("=" * 70)


if __name__ == "__main__":
    run_viewport_and_console_tests()
