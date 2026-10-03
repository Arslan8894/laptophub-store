import subprocess
import time
import json
import urllib.request
import socket
import base64
import os
import struct

CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
PORT = 9225

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


def audit_page(url):
    print(f"\n==========================================")
    print(f"Auditing: {url}")
    print(f"==========================================")
    proc = subprocess.Popen([
        CHROME_PATH,
        "--headless=new",
        f"--remote-debugging-port={PORT}",
        "--disable-gpu",
        "--no-first-run",
        "--no-default-browser-check",
        "--window-size=1280,900",
        url
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    time.sleep(2.5)
    errors = []
    failed_requests = []
    
    try:
        req = urllib.request.urlopen(f"http://127.0.0.1:{PORT}/json")
        tabs = json.loads(req.read().decode())
        target = next((t for t in tabs if t.get("type") == "page"), None)
        assert target is not None, "Target page not found"
        
        ws_url = target["webSocketDebuggerUrl"]
        path = "/" + ws_url.split("/", 3)[3]
        ws = SimpleWebSocket("127.0.0.1", PORT, path)
        
        cmd_id = 0
        def cdp(method, params=None):
            nonlocal cmd_id
            cmd_id += 1
            payload = {"id": cmd_id, "method": method, "params": params or {}}
            ws.send(json.dumps(payload))
            while True:
                resp = json.loads(ws.recv())
                if resp.get("id") == cmd_id:
                    return resp.get("result", {})

        cdp("Runtime.enable")
        cdp("Log.enable")
        cdp("Network.enable")

        # Check DOM state and errors
        res = cdp("Runtime.evaluate", {
            "expression": """
            (() => {
                const nav = document.querySelector('nav.liquid-glass-nav');
                const images = Array.from(document.querySelectorAll('img')).map(img => ({
                    src: img.src,
                    complete: img.complete,
                    naturalWidth: img.naturalWidth
                }));
                const brokenImages = images.filter(i => i.complete && i.naturalWidth === 0);

                return {
                    title: document.title,
                    hasLiquidGlassNav: !!nav,
                    totalImages: images.length,
                    brokenImagesCount: brokenImages.length,
                    brokenImages: brokenImages.slice(0, 5)
                };
            })()
            """,
            "returnByValue": True
        })

        info = res.get("result", {}).get("value", {})
        print(f"Title: {info.get('title')}")
        print(f"Liquid Glass Nav: {info.get('hasLiquidGlassNav')}")
        print(f"Images: {info.get('totalImages')} total, {info.get('brokenImagesCount')} broken")
        if info.get('brokenImagesCount') > 0:
            print("Broken images sample:", info.get('brokenImages'))

        ws.close()
    finally:
        proc.terminate()
        proc.wait()

def main():
    pages = [
        "http://127.0.0.1:8080/laptophub.html",
        "http://127.0.0.1:8080/product.html?id=12",
        "http://127.0.0.1:8080/consult.html",
        "http://127.0.0.1:8080/index.html",
    ]
    for p in pages:
        audit_page(p)

if __name__ == "__main__":
    main()
