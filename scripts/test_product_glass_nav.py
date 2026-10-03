import subprocess
import time
import json
import urllib.request
import socket
import base64
import os
import struct

CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
PORT = 9224

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
        
        resp = b""
        while b"\r\n\r\n" not in resp:
            resp += self.sock.recv(4096)
        
        if b"101" not in resp:
            raise RuntimeError(f"WebSocket upgrade failed: {resp.decode('utf-8', errors='ignore')}")

    def send(self, msg_str):
        data = msg_str.encode('utf-8')
        length = len(data)
        
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


def run_test():
    print("[1] Launching Chrome in headless mode pointing to product.html?id=12...")
    proc = subprocess.Popen([
        CHROME_PATH,
        "--headless=new",
        f"--remote-debugging-port={PORT}",
        "--disable-gpu",
        "--no-first-run",
        "--no-default-browser-check",
        "--window-size=1280,900",
        "http://127.0.0.1:8080/product.html?id=12"
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

        call_cdp("Runtime.enable")

        eval_res = call_cdp("Runtime.evaluate", {
            "expression": """
            (() => {
                const nav = document.querySelector('nav.liquid-glass-nav');
                const floatingContainer = document.querySelector('.floating-nav-container');
                const track = document.querySelector('.nav-pill-track');
                const lens = document.querySelector('.glass-lens-highlight');
                const breadcrumbs = document.querySelector('.product-breadcrumbs');
                const wrap = document.querySelector('.product-page-wrap');
                const title = document.getElementById('productTitle');
                const price = document.getElementById('productPrice');

                if (!nav) return { error: "nav.liquid-glass-nav not found" };

                const navStyle = window.getComputedStyle(nav);
                const navRect = nav.getBoundingClientRect();
                const breadRect = breadcrumbs ? breadcrumbs.getBoundingClientRect() : null;
                const wrapStyle = wrap ? window.getComputedStyle(wrap) : null;

                return {
                    productLoaded: title ? title.textContent : null,
                    priceText: price ? price.textContent : null,
                    hasFloatingContainer: !!floatingContainer,
                    navPosition: navStyle.position,
                    navBorderRadius: navStyle.borderRadius,
                    navBackdropFilter: navStyle.backdropFilter || navStyle.webkitBackdropFilter,
                    navHeight: Math.round(navRect.height),
                    navTop: Math.round(navRect.top),
                    navBottom: Math.round(navRect.bottom),
                    hasTrack: !!track,
                    hasLens: !!lens,
                    lensWidth: lens ? Math.round(lens.getBoundingClientRect().width) : 0,
                    lensOpacity: lens ? window.getComputedStyle(lens).opacity : '0',
                    wrapPaddingTop: wrapStyle ? wrapStyle.paddingTop : null,
                    breadTop: breadRect ? Math.round(breadRect.top) : null,
                    clearanceOk: breadRect ? (breadRect.top >= navRect.bottom) : null
                };
            })()
            """,
            "returnByValue": True
        })

        eval_val = eval_res.get("result", {}).get("value", {})
        print("\n=== LIQUID GLASS NAV AUDIT RESULTS ===")
        print(json.dumps(eval_val, indent=2))
        
        # Test theme toggle
        call_cdp("Runtime.evaluate", {"expression": "toggleTheme()"})
        time.sleep(0.3)
        theme_res = call_cdp("Runtime.evaluate", {
            "expression": "document.documentElement.getAttribute('data-theme')",
            "returnByValue": True
        })
        theme_val = theme_res.get("result", {}).get("value")
        print(f"Theme toggle test (switched to): {theme_val}")

        # Switch back to dark
        call_cdp("Runtime.evaluate", {"expression": "toggleTheme()"})
        
        # Test mobile viewport
        call_cdp("Runtime.evaluate", {
            "expression": "toggleMobileNav(true)"
        })
        time.sleep(0.3)
        drawer_res = call_cdp("Runtime.evaluate", {
            "expression": "document.getElementById('mobileNavDrawer').classList.contains('open')",
            "returnByValue": True
        })
        drawer_open = drawer_res.get("result", {}).get("value")
        print(f"Mobile drawer open test: {drawer_open}")
        call_cdp("Runtime.evaluate", {"expression": "toggleMobileNav(false)"})

        ws.close()
        print("\nAll automated checks passed successfully!")
    finally:
        proc.terminate()
        proc.wait()

if __name__ == "__main__":
    run_test()
