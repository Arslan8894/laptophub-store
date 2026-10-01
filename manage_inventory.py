#!/usr/bin/env python3
"""
manage_inventory.py
Complete inventory management backend and CLI for LaptopHub & VOLTS laptop store.
Provides:
  - Local HTTP & REST API server for live browser-based inventory management (Add/Edit/Remove/Photo search).
  - CLI commands for direct terminal manipulation (list, add, remove, fetch-photos).
  - Automatic synchronization with laptops-data.js and build_inventory.py.
"""

import sys
import os
import json
import re
import argparse
import time
import urllib.request
import urllib.parse
from http.server import HTTPServer, SimpleHTTPRequestHandler

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_JS_PATH = os.path.join(BASE_DIR, 'laptops-data.js')
BUILD_PY_PATH = os.path.join(BASE_DIR, 'build_inventory.py')
IMAGES_DIR = os.path.join(BASE_DIR, 'images')

os.makedirs(IMAGES_DIR, exist_ok=True)

# ---------------------------------------------------------------------------
# DATA LOAD / SAVE HELPERS
# ---------------------------------------------------------------------------
def load_inventory():
    if not os.path.exists(DATA_JS_PATH):
        return []
    with open(DATA_JS_PATH, 'r', encoding='utf-8') as f:
        text = f.read()
    start = text.find('[')
    end = text.rfind(']') + 1
    if start != -1 and end != 0:
        return json.loads(text[start:end])
    return []

def save_inventory(laptops):
    # Ensure sequential IDs and formatted prices
    for idx, lap in enumerate(laptops, start=1):
        if 'id' not in lap or not lap['id']:
            lap['id'] = idx
        if 'price' in lap and isinstance(lap['price'], (int, float)):
            lap['priceFormatted'] = f"Rs {int(lap['price']):,}"
            if 'priceUsd' not in lap or not lap['priceUsd']:
                lap['priceUsd'] = round(int(lap['price']) / 278)
        if 'brand' in lap and 'brandName' not in lap:
            lap['brandName'] = lap['brand'].capitalize()
            
    js_content = f"// Complete {len(laptops)}-Laptop Real Inventory Dataset\nconst LAPTOPS_INVENTORY = {json.dumps(laptops, indent=2)};\n\nif (typeof module !== 'undefined') module.exports = LAPTOPS_INVENTORY;\n"
    with open(DATA_JS_PATH, 'w', encoding='utf-8') as f:
        f.write(js_content)
    return True

# ---------------------------------------------------------------------------
# INTERNET PHOTO RETRIEVAL HELPER
# ---------------------------------------------------------------------------
def fetch_photo_for_laptop(query, dest_filename):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    }
    img_headers = {
        'User-Agent': headers['User-Agent'],
        'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
        'Referer': 'https://www.bing.com/',
    }
    q = urllib.parse.quote(query)
    url = f'https://www.bing.com/images/search?q={q}&form=HDRSC2&first=1'
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
        murls = re.findall(r'murl&quot;:&quot;(https?://[^&]+)&quot;', html)
        if not murls:
            murls = re.findall(r'"murl":"(https?://[^"]+)"', html)
            
        dest_path = os.path.join(IMAGES_DIR, dest_filename)
        for u in murls[:8]:
            if any(bad in u.lower() for bad in ['.svg', '.ico', 'favicon']):
                continue
            try:
                img_req = urllib.request.Request(u, headers=img_headers)
                with urllib.request.urlopen(img_req, timeout=10) as r:
                    data = r.read()
                    if len(data) >= 15 * 1024:
                        with open(dest_path, 'wb') as f:
                            f.write(data)
                        return f"images/{dest_filename}", len(data)
            except Exception:
                continue
    except Exception as e:
        print(f"Error fetching photo: {e}")
    return None, 0

# ---------------------------------------------------------------------------
# AI CONSULTATION RECOMMENDATION HELPER (GEMINI INTEGRATION)
# ---------------------------------------------------------------------------
RATE_LIMIT_CACHE = {}

def get_ai_recommendation(prefs, matched_laptops):
    valid_ids = {lap['id'] for lap in matched_laptops if 'id' in lap}
    if not valid_ids:
        return {'success': False, 'fallback': True, 'error': 'No valid laptop IDs'}

    api_key = os.environ.get('GEMINI_API_KEY') or os.environ.get('GOOGLE_API_KEY')
    
    # Check optional local .env file
    env_path = os.path.join(BASE_DIR, '.env')
    if not api_key and os.path.exists(env_path):
        try:
            with open(env_path, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if line.startswith('GEMINI_API_KEY=') or line.startswith('GOOGLE_API_KEY='):
                        api_key = line.split('=', 1)[1].strip().strip('"').strip("'")
                        break
        except Exception:
            pass

    if not api_key:
        return {
            'success': False,
            'fallback': True,
            'message': 'AI service offline: GEMINI_API_KEY is not configured in backend environment.'
        }

    # Format structured candidate list (strict minimization)
    candidate_summary = []
    for lap in matched_laptops[:8]:
        candidate_summary.append({
            'id': lap['id'],
            'name': lap.get('name'),
            'brand': lap.get('brand'),
            'cpu': lap.get('cpu'),
            'ramGb': lap.get('ramGb', lap.get('ram')),
            'storageGb': lap.get('storageGb', lap.get('storage')),
            'gpu': lap.get('gpu'),
            'price': lap.get('priceFormatted', f"Rs {lap.get('price', 0):,}"),
            'condition': lap.get('condition')
        })

    budget_val = prefs.get('budget', 130000)
    budget_formatted = f"Rs {int(budget_val):,}" if isinstance(budget_val, (int, float)) else str(budget_val)

    prompt_text = (
        f"You are LaptopHUB's senior laptop hardware consultant in Pakistan.\n"
        f"User Preferences:\n"
        f"- Target Use Case: {prefs.get('usecase', 'General')}\n"
        f"- Preferred CPU: {prefs.get('cpu', 'Any')}\n"
        f"- Minimum RAM: {prefs.get('ram', 16)} GB\n"
        f"- Minimum SSD: {prefs.get('storage', 512)} GB\n"
        f"- GPU Requirement: {prefs.get('gpu', 'Any')}\n"
        f"- Maximum Budget: PKR {budget_formatted}\n\n"
        f"Matched Laptops in Stock (Select ONLY from this list):\n"
        f"{json.dumps(candidate_summary, indent=2)}\n\n"
        f"Instructions:\n"
        f"1. Select the single best laptop ID from the provided list that maximizes value for the user.\n"
        f"2. Explain why in 2-3 friendly, authoritative sentences.\n"
        f"3. Highlight tradeoffs comparing it to the other matches in 1-2 friendly sentences.\n"
        f"4. You MUST respond with JSON matching this schema: "
        f'{{"recommendedLaptopId": <int>, "reason": "<string>", "tradeoffs": "<string>"}}\n'
        f"5. NEVER recommend any laptop ID that is not in the list. Do not invent any specs."
    )

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
    req_body = {
        "contents": [{"parts": [{"text": prompt_text}]}],
        "generationConfig": {
            "temperature": 0.2,
            "responseMimeType": "application/json"
        }
    }

    try:
        data_bytes = json.dumps(req_body).encode('utf-8')
        req = urllib.request.Request(
            url,
            data=data_bytes,
            headers={'Content-Type': 'application/json'},
            method='POST'
        )
        with urllib.request.urlopen(req, timeout=7) as resp:
            resp_data = json.loads(resp.read().decode('utf-8'))
            
        candidates = resp_data.get('candidates', [])
        if candidates and 'content' in candidates[0]:
            parts = candidates[0]['content'].get('parts', [])
            if parts and 'text' in parts[0]:
                ai_json = json.loads(parts[0]['text'])
                rec_id = int(ai_json.get('recommendedLaptopId'))
                if rec_id in valid_ids:
                    return {
                        'success': True,
                        'recommendation': {
                            'recommendedLaptopId': rec_id,
                            'reason': ai_json.get('reason', '').strip(),
                            'tradeoffs': ai_json.get('tradeoffs', '').strip()
                        }
                    }
    except Exception as e:
        return {
            'success': False,
            'fallback': True,
            'error': str(e),
            'message': 'AI call failed or timed out. Falling back to deterministic matching.'
        }

    return {
        'success': False,
        'fallback': True,
        'message': 'AI recommendation could not be validated against candidate list.'
    }

# ---------------------------------------------------------------------------
# INVENTORY REST API REQUEST HANDLER
# ---------------------------------------------------------------------------
class InventoryAPIHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=BASE_DIR, **kwargs)

    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()

    def do_GET(self):
        if self.path == '/api/inventory':
            laptops = load_inventory()
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(laptops).encode('utf-8'))
            return
        elif self.path == '/' or self.path == '/inventory':
            self.path = '/inventory.html'
        return super().do_GET()

    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(content_length)
        payload = {}
        if body:
            try:
                payload = json.loads(body.decode('utf-8'))
            except Exception:
                pass

        if self.path == '/api/laptop/add':
            laptops = load_inventory()
            # Generate new unique ID
            new_id = max([lap.get('id', 0) for lap in laptops], default=0) + 1
            payload['id'] = new_id
            
            # Default fallback fields if missing
            payload.setdefault('brand', 'other')
            payload.setdefault('brandName', payload['brand'].capitalize())
            payload.setdefault('series', payload.get('name', 'Custom Laptop'))
            payload.setdefault('category', 'Ultrabook')
            payload.setdefault('badge', 'New Arrival')
            payload.setdefault('badgeType', 'b-corp')
            payload.setdefault('condition', 'Like New (10/10) · Certified Refurbished')
            payload.setdefault('warranty', '1 Year Local Warranty + 7 Days Checking')
            payload.setdefault('useCases', ['office', 'student'])
            payload.setdefault('img', 'images/lenovo-t14-g1.jpg')
            
            laptops.append(payload)
            save_inventory(laptops)
            
            self.send_response(201)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'success': True, 'laptop': payload}).encode('utf-8'))
            return

        elif self.path == '/api/laptop/update':
            target_id = payload.get('id')
            laptops = load_inventory()
            found = False
            for idx, lap in enumerate(laptops):
                if lap.get('id') == target_id:
                    laptops[idx].update(payload)
                    found = True
                    break
            if found:
                save_inventory(laptops)
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'success': True, 'id': target_id}).encode('utf-8'))
            else:
                self.send_response(404)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'error': 'Laptop not found'}).encode('utf-8'))
            return

        elif self.path == '/api/laptop/delete':
            target_id = payload.get('id')
            laptops = load_inventory()
            initial_len = len(laptops)
            laptops = [lap for lap in laptops if lap.get('id') != target_id]
            if len(laptops) < initial_len:
                save_inventory(laptops)
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'success': True, 'deletedId': target_id, 'remaining': len(laptops)}).encode('utf-8'))
            else:
                self.send_response(404)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'error': 'Laptop not found'}).encode('utf-8'))
            return

        elif self.path == '/api/fetch-photo':
            query = payload.get('query', '')
            laptop_id = payload.get('id', 'temp')
            slug = re.sub(r'[^a-z0-9]+', '-', query.lower()).strip('-')[:30]
            filename = f"laptop-{laptop_id}-{slug}.jpg"
            img_rel, size = fetch_photo_for_laptop(query, filename)
            if img_rel:
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'success': True, 'img': img_rel, 'sizeBytes': size}).encode('utf-8'))
            else:
                self.send_response(500)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'error': 'Could not retrieve photo'}).encode('utf-8'))
            return

        elif self.path == '/api/save-all':
            items = payload.get('laptops', [])
            if items:
                save_inventory(items)
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'success': True, 'count': len(items)}).encode('utf-8'))
                return

        elif self.path == '/api/consult/ai-recommend':
            client_ip = self.client_address[0]
            now = time.time()
            requests = RATE_LIMIT_CACHE.get(client_ip, [])
            requests = [t for t in requests if now - t < 60]
            if len(requests) >= 12:
                self.send_response(429)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({
                    'success': False,
                    'fallback': True,
                    'error': 'Rate limit exceeded (max 12 req/min). Please try again shortly.'
                }).encode('utf-8'))
                return

            requests.append(now)
            RATE_LIMIT_CACHE[client_ip] = requests

            prefs = payload.get('preferences', {})
            matched_laptops = payload.get('matchedLaptops', [])

            if not matched_laptops:
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({
                    'success': False,
                    'fallback': True,
                    'message': 'No matched laptops provided.'
                }).encode('utf-8'))
                return

            result = get_ai_recommendation(prefs, matched_laptops)
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(result).encode('utf-8'))
            return

        self.send_response(404)
        self.end_headers()

# ---------------------------------------------------------------------------
# CLI MODES
# ---------------------------------------------------------------------------
def run_cli_list():
    laptops = load_inventory()
    print(f"\n=======================================================")
    print(f"  CURRENT INVENTORY ({len(laptops)} Laptops)")
    print(f"=======================================================")
    for lap in laptops:
        lid = lap.get('id')
        name = lap.get('name', 'Unnamed')
        price = lap.get('priceFormatted', f"Rs {lap.get('price', 0):,}")
        ram = lap.get('ram', 0)
        ssd = lap.get('storage', 0)
        img = lap.get('img', 'no image')
        print(f"[{lid:>2}] {name:<38} | {price:>10} | {ram}GB/{ssd}GB | {img}")
    print("=======================================================\n")

def run_cli_remove(laptop_id):
    laptops = load_inventory()
    initial_len = len(laptops)
    laptops = [lap for lap in laptops if lap.get('id') != laptop_id]
    if len(laptops) < initial_len:
        save_inventory(laptops)
        print(f"Successfully removed laptop ID {laptop_id}. Remaining: {len(laptops)} laptops.")
    else:
        print(f"Error: Laptop with ID {laptop_id} not found.")

def run_server(port=8080):
    server_address = ('', port)
    httpd = HTTPServer(server_address, InventoryAPIHandler)
    print("=" * 65)
    print(f"  LAPTOP INVENTORY MANAGER SERVER STARTED")
    print(f"  URL: http://localhost:{port}/inventory.html")
    print(f"  Full Suite: http://localhost:{port}/index.html")
    print("=" * 65)
    print("Press Ctrl+C to stop.")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping server...")
        httpd.server_close()

# ---------------------------------------------------------------------------
# MAIN ENTRYPOINT
# ---------------------------------------------------------------------------
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Laptop Inventory Manager CLI & Server")
    parser.add_argument('action', nargs='?', default='serve', choices=['serve', 'list', 'remove', 'fetch-photos'],
                        help="Action to perform: 'serve' (web admin), 'list' (print inventory), 'remove' (delete item), 'fetch-photos'")
    parser.add_argument('--id', type=int, help="Laptop ID for removal")
    parser.add_argument('--port', type=int, default=8080, help="Port to run web server on (default: 8080)")

    args = parser.parse_args()

    if args.action == 'list':
        run_cli_list()
    elif args.action == 'remove':
        if not args.id:
            print("Please specify --id <laptop_id> to remove.")
            sys.exit(1)
        run_cli_remove(args.id)
    elif args.action == 'fetch-photos':
        import retrieve_all_laptop_images
        retrieve_all_laptop_images.main()
    else:
        run_server(args.port)
