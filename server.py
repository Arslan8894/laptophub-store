#!/usr/bin/env python3
"""
server.py — LaptopHUB Complete Backend
=======================================
Replaces manage_inventory.py. Zero new pip dependencies.
Uses only Python stdlib: sqlite3, hashlib, hmac, secrets, json,
http.server, urllib, re, argparse, os, sys, time, logging.

Features:
  - SQLite-backed users, sessions, orders, reviews, admin_log
  - Two separate session cookies: lh_sess (customer) lh_admin_sess (admin)
  - scrypt password hashing
  - Server-side role enforcement on every admin endpoint
  - Rate limiting: 5/15min customers, 3/10min admins (+ lockout)
  - Cache-Control: no-store on all admin responses
  - Admin action logging
  - Redirect: /volts.html → /laptophub.html, /custom-laptop.html → /consult.html
  - Gemini AI consultation endpoint
"""

import sys
import os
import json
import re
import argparse
import time
import hashlib
import hmac
import secrets
import sqlite3
import logging
import urllib.request
import urllib.parse
from http.server import HTTPServer, BaseHTTPRequestHandler
from http.cookies import SimpleCookie
from datetime import datetime, timezone
import base64
import html

# ─────────────────────────────────────────────────────────────
# PATHS & CONSTANTS
# ─────────────────────────────────────────────────────────────
BASE_DIR    = os.path.dirname(os.path.abspath(__file__))
DATA_JS     = os.path.join(BASE_DIR, 'laptops-data.js')
DB_DIR      = os.path.join(BASE_DIR, 'db')
DB_PATH     = os.path.join(DB_DIR, 'laptophub.db')
SCHEMA_PATH = os.path.join(DB_DIR, 'schema.sql')
IMAGES_DIR  = os.path.join(BASE_DIR, 'images')
ADMIN_DIR   = os.path.join(BASE_DIR, 'admin')
RAM_PRICING_PATH = os.path.join(DB_DIR, 'ram_pricing.json')

os.makedirs(DB_DIR, exist_ok=True)
os.makedirs(IMAGES_DIR, exist_ok=True)
os.makedirs(ADMIN_DIR, exist_ok=True)

DEFAULT_RAM_TIERS = {
    "DDR4": { "8": 0, "16": 8000, "32": 23000 },
    "DDR5": { "8": 0, "16": 10000, "32": 28000 }
}

def load_ram_pricing() -> dict:
    if os.path.exists(RAM_PRICING_PATH):
        try:
            with open(RAM_PRICING_PATH, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            log.warning("Could not read ram_pricing.json: %s", e)
    return DEFAULT_RAM_TIERS

def save_ram_pricing(tiers: dict) -> bool:
    try:
        with open(RAM_PRICING_PATH, 'w', encoding='utf-8') as f:
            json.dump(tiers, f, indent=2)
        return True
    except Exception as e:
        log.error("Failed to save ram_pricing.json: %s", e)
        return False

# Cookie names
CUST_COOKIE  = 'lh_sess'
ADMIN_COOKIE = 'lh_admin_sess'

# Session lifetimes (seconds)
CUST_TTL  = 7 * 24 * 3600   # 7 days rolling
ADMIN_TTL = 30 * 60          # 30 min inactivity

# Rate limiting
CUST_MAX_ATTEMPTS  = 5
CUST_WINDOW_SECS   = 15 * 60
ADMIN_MAX_ATTEMPTS = 3
ADMIN_WINDOW_SECS  = 10 * 60

# Max upload size: 8 MB
MAX_UPLOAD_BYTES = 8 * 1024 * 1024

# Allowed image extensions
ALLOWED_IMG_EXTS = {'.jpg', '.jpeg', '.png', '.webp', '.gif'}

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')
log = logging.getLogger('laptophub')

# In-memory AI rate limit cache (per IP)
AI_RATE_CACHE: dict = {}

# ─────────────────────────────────────────────────────────────
# DATABASE INIT
# ─────────────────────────────────────────────────────────────
def get_db() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH, timeout=10)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA foreign_keys=ON")
    return conn


def init_db():
    """Create tables from schema.sql if they don't exist."""
    with get_db() as conn:
        if os.path.exists(SCHEMA_PATH):
            with open(SCHEMA_PATH, 'r', encoding='utf-8') as f:
                conn.executescript(f.read())
        else:
            # Inline fallback schema
            conn.executescript("""
                PRAGMA foreign_keys = ON;
                CREATE TABLE IF NOT EXISTS users (
                  id INTEGER PRIMARY KEY AUTOINCREMENT, email TEXT UNIQUE NOT NULL COLLATE NOCASE,
                  name TEXT, phone TEXT, address TEXT, city TEXT,
                  role TEXT NOT NULL DEFAULT 'user' CHECK(role IN ('user','admin')),
                  pass_hash TEXT NOT NULL, is_active INTEGER NOT NULL DEFAULT 1,
                  created_at TEXT NOT NULL DEFAULT (datetime('now','utc')),
                  updated_at TEXT NOT NULL DEFAULT (datetime('now','utc')));
                CREATE TABLE IF NOT EXISTS sessions (
                  token TEXT PRIMARY KEY, user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
                  created_at TEXT NOT NULL DEFAULT (datetime('now','utc')),
                  last_active TEXT NOT NULL DEFAULT (datetime('now','utc')),
                  ip TEXT, user_agent TEXT);
                CREATE TABLE IF NOT EXISTS orders (
                  id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER NOT NULL REFERENCES users(id),
                  items TEXT NOT NULL, total_pkr INTEGER NOT NULL,
                  cust_name TEXT NOT NULL, cust_phone TEXT NOT NULL,
                  cust_city TEXT NOT NULL, cust_address TEXT NOT NULL,
                  status TEXT NOT NULL DEFAULT 'new', notes TEXT,
                  created_at TEXT NOT NULL DEFAULT (datetime('now','utc')),
                  updated_at TEXT NOT NULL DEFAULT (datetime('now','utc')));
                CREATE TABLE IF NOT EXISTS reviews (
                  id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER REFERENCES users(id) ON DELETE SET NULL,
                  laptop_id INTEGER, reviewer TEXT NOT NULL, rating INTEGER NOT NULL CHECK(rating BETWEEN 1 AND 5),
                  body TEXT NOT NULL, approved INTEGER NOT NULL DEFAULT 0,
                  created_at TEXT NOT NULL DEFAULT (datetime('now','utc')));
                CREATE TABLE IF NOT EXISTS admin_log (
                  id INTEGER PRIMARY KEY AUTOINCREMENT, admin_id INTEGER NOT NULL REFERENCES users(id),
                  action TEXT NOT NULL, target TEXT, detail TEXT,
                  created_at TEXT NOT NULL DEFAULT (datetime('now','utc')));
                CREATE TABLE IF NOT EXISTS auth_attempts (
                  id INTEGER PRIMARY KEY AUTOINCREMENT, ip TEXT NOT NULL, email TEXT NOT NULL COLLATE NOCASE,
                  attempted_at TEXT NOT NULL DEFAULT (datetime('now','utc')));
            """)
    log.info("Database ready: %s", DB_PATH)


# ─────────────────────────────────────────────────────────────
# PASSWORD HASHING  (scrypt, stdlib only)
# ─────────────────────────────────────────────────────────────
def hash_password(password: str) -> str:
    salt = secrets.token_hex(32)
    dk = hashlib.scrypt(password.encode('utf-8'), salt=bytes.fromhex(salt),
                        n=16384, r=8, p=1, dklen=64)
    return f"scrypt${salt}${dk.hex()}"


def verify_password(password: str, stored: str) -> bool:
    try:
        algo, salt_hex, hash_hex = stored.split('$', 2)
        if algo != 'scrypt':
            return False
        dk = hashlib.scrypt(password.encode('utf-8'), salt=bytes.fromhex(salt_hex),
                            n=16384, r=8, p=1, dklen=64)
        return hmac.compare_digest(dk.hex(), hash_hex)
    except Exception:
        return False


# ─────────────────────────────────────────────────────────────
# SESSION HELPERS
# ─────────────────────────────────────────────────────────────
def create_session(user_id: int, ip: str, ua: str) -> str:
    token = secrets.token_hex(32)
    with get_db() as conn:
        conn.execute(
            "INSERT INTO sessions(token,user_id,ip,user_agent) VALUES(?,?,?,?)",
            (token, user_id, ip, ua))
    return token


def get_session_user(token: str, is_admin: bool = False) -> dict | None:
    """Validate session token and return user row, or None if invalid/expired."""
    if not token:
        return None
    ttl = ADMIN_TTL if is_admin else CUST_TTL
    with get_db() as conn:
        row = conn.execute(
            "SELECT s.token, s.last_active, u.id, u.email, u.name, u.role, u.is_active, "
            "u.phone, u.city, u.address "
            "FROM sessions s JOIN users u ON u.id=s.user_id WHERE s.token=?",
            (token,)).fetchone()
        if not row:
            return None
        if not row['is_active']:
            return None
        # Check role match
        if is_admin and row['role'] != 'admin':
            return None
        if not is_admin and row['role'] == 'admin':
            return None   # admin must use admin cookie, not customer cookie
        # Check inactivity (admin) or absolute TTL (customer)
        last = datetime.fromisoformat(row['last_active']).replace(tzinfo=timezone.utc)
        now  = datetime.now(timezone.utc)
        if (now - last).total_seconds() > ttl:
            conn.execute("DELETE FROM sessions WHERE token=?", (token,))
            return None
        # Refresh last_active
        conn.execute("UPDATE sessions SET last_active=datetime('now','utc') WHERE token=?", (token,))
        return dict(row)


def delete_session(token: str):
    with get_db() as conn:
        conn.execute("DELETE FROM sessions WHERE token=?", (token,))


# ─────────────────────────────────────────────────────────────
# RATE LIMITING (DB-backed for auth, in-memory for AI)
# ─────────────────────────────────────────────────────────────
def is_rate_limited(ip: str, email: str, max_attempts: int, window_secs: int) -> bool:
    cutoff = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S') # sqlite utc string
    with get_db() as conn:
        # Clean old records
        conn.execute(
            "DELETE FROM auth_attempts WHERE attempted_at < datetime('now','-' || ? || ' seconds')",
            (window_secs,))
        count = conn.execute(
            "SELECT COUNT(*) FROM auth_attempts WHERE ip=? AND email=? "
            "AND attempted_at >= datetime('now','-' || ? || ' seconds')",
            (ip, email.lower(), window_secs)).fetchone()[0]
        return count >= max_attempts


def record_attempt(ip: str, email: str):
    with get_db() as conn:
        conn.execute("INSERT INTO auth_attempts(ip,email) VALUES(?,?)", (ip, email.lower()))


# ─────────────────────────────────────────────────────────────
# VALIDATION HELPERS
# ─────────────────────────────────────────────────────────────
PK_PHONE_RE = re.compile(r'^(?:\+92|0092|0)3[0-9]{9}$')

def validate_pk_phone(phone: str) -> bool:
    return bool(PK_PHONE_RE.match(phone.replace('-', '').replace(' ', '')))

def validate_email(email: str) -> bool:
    return bool(re.match(r'^[^@\s]+@[^@\s]+\.[^@\s]+$', email))


# ─────────────────────────────────────────────────────────────
# INVENTORY HELPERS (JS file read/write — same as before)
# ─────────────────────────────────────────────────────────────
def load_inventory() -> list:
    if not os.path.exists(DATA_JS):
        return []
    with open(DATA_JS, 'r', encoding='utf-8') as f:
        text = f.read()
    start = text.find('[')
    end   = text.rfind(']') + 1
    if start != -1 and end > 0:
        laptops = json.loads(text[start:end])
        for lap in laptops:
            if 'stock' not in lap or lap.get('stock') is None:
                lap['stock'] = 3
        return laptops
    return []


def save_inventory(laptops: list) -> bool:
    for idx, lap in enumerate(laptops, start=1):
        if 'id' not in lap or not lap['id']:
            lap['id'] = idx
        if 'stock' not in lap or lap.get('stock') is None:
            lap['stock'] = 3
        if 'price' in lap and isinstance(lap['price'], (int, float)):
            lap['priceFormatted'] = f"Rs {int(lap['price']):,}"
            if 'priceUsd' not in lap or not lap['priceUsd']:
                lap['priceUsd'] = round(int(lap['price']) / 278)
        if 'brand' in lap and 'brandName' not in lap:
            lap['brandName'] = lap['brand'].capitalize()
    js = (f"// Complete {len(laptops)}-Laptop Real Inventory Dataset\n"
          f"const LAPTOPS_INVENTORY = {json.dumps(laptops, indent=2)};\n\n"
          f"if (typeof module !== 'undefined') module.exports = LAPTOPS_INVENTORY;\n")
    with open(DATA_JS, 'w', encoding='utf-8') as f:
        f.write(js)
    return True


def public_inventory(laptops: list) -> list:
    """Return only visible laptops for public API."""
    return [l for l in laptops if not l.get('hidden', False)]


# ─────────────────────────────────────────────────────────────
# ADMIN LOG
# ─────────────────────────────────────────────────────────────
def log_admin_action(admin_id: int, action: str, target: str = '', detail: str = ''):
    with get_db() as conn:
        conn.execute(
            "INSERT INTO admin_log(admin_id,action,target,detail) VALUES(?,?,?,?)",
            (admin_id, action, str(target), str(detail)))
    log.info("ADMIN[%s] %s target=%s", admin_id, action, target)


# ─────────────────────────────────────────────────────────────
# PHOTO FETCH (unchanged from manage_inventory.py)
# ─────────────────────────────────────────────────────────────
def fetch_photo_for_laptop(query: str, dest_filename: str):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
        'Accept': 'text/html,application/xhtml+xml,*/*;q=0.8',
    }
    img_headers = {**headers,
                   'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
                   'Referer': 'https://www.bing.com/'}
    q   = urllib.parse.quote(query)
    url = f'https://www.bing.com/images/search?q={q}&form=HDRSC2&first=1'
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
        murls = re.findall(r'murl&quot;:&quot;(https?://[^&]+)&quot;', html)
        if not murls:
            murls = re.findall(r'"murl":"(https?://[^"]+)"', html)
        dest = os.path.join(IMAGES_DIR, dest_filename)
        for u in murls[:8]:
            if any(bad in u.lower() for bad in ['.svg', '.ico', 'favicon']):
                continue
            try:
                r = urllib.request.Request(u, headers=img_headers)
                with urllib.request.urlopen(r, timeout=10) as rsp:
                    data = rsp.read()
                    if len(data) >= 15 * 1024:
                        with open(dest, 'wb') as f:
                            f.write(data)
                        return f"images/{dest_filename}", len(data)
            except Exception:
                continue
    except Exception as e:
        log.warning("Photo fetch error: %s", e)
    return None, 0


# ─────────────────────────────────────────────────────────────
# AI CONSULTATION  (Gemini — unchanged logic)
# ─────────────────────────────────────────────────────────────
def get_ai_recommendation(prefs: dict, matched: list) -> dict:
    valid_ids = {lap['id'] for lap in matched if 'id' in lap}
    if not valid_ids:
        return {'success': False, 'fallback': True, 'error': 'No valid laptop IDs'}

    api_key = os.environ.get('GEMINI_API_KEY') or os.environ.get('GOOGLE_API_KEY')
    env_path = os.path.join(BASE_DIR, '.env')
    if not api_key and os.path.exists(env_path):
        with open(env_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line.startswith(('GEMINI_API_KEY=', 'GOOGLE_API_KEY=')):
                    api_key = line.split('=', 1)[1].strip().strip('"\'')
                    break

    if not api_key:
        return {'success': False, 'fallback': True,
                'message': 'AI service offline: GEMINI_API_KEY not configured.'}

    candidates = [{
        'id': lap['id'], 'name': lap.get('name'), 'brand': lap.get('brand'),
        'cpu': lap.get('cpu'), 'ramGb': lap.get('ram'),
        'storageGb': lap.get('storage'), 'gpu': lap.get('gpu'),
        'price': lap.get('priceFormatted', f"Rs {lap.get('price', 0):,}"),
        'condition': lap.get('condition')
    } for lap in matched[:8]]

    budget_val = prefs.get('budget', 130000)
    prompt = (
        f"You are LaptopHUB's senior laptop consultant in Pakistan.\n"
        f"User Preferences: use case={prefs.get('usecase','General')}, "
        f"cpu={prefs.get('cpu','Any')}, ram≥{prefs.get('ram',16)}GB, "
        f"storage≥{prefs.get('storage',512)}GB, gpu={prefs.get('gpu','Any')}, "
        f"budget≤PKR {int(budget_val):,}\n"
        f"Matched laptops (choose ONLY from these IDs):\n{json.dumps(candidates,indent=2)}\n"
        f"Respond with JSON: {{\"recommendedLaptopId\":<int>,\"reason\":\"<str>\",\"tradeoffs\":\"<str>\"}}"
    )

    url = (f"https://generativelanguage.googleapis.com/v1beta/models/"
           f"gemini-1.5-flash:generateContent?key={api_key}")
    body = json.dumps({
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {"temperature": 0.2, "responseMimeType": "application/json"}
    }).encode()
    try:
        req = urllib.request.Request(url, data=body,
                                     headers={'Content-Type': 'application/json'}, method='POST')
        with urllib.request.urlopen(req, timeout=7) as resp:
            data = json.loads(resp.read())
        cands = data.get('candidates', [])
        if cands and 'content' in cands[0]:
            parts = cands[0]['content'].get('parts', [])
            if parts and 'text' in parts[0]:
                ai = json.loads(parts[0]['text'])
                rid = int(ai['recommendedLaptopId'])
                if rid in valid_ids:
                    return {'success': True, 'recommendation': {
                        'recommendedLaptopId': rid,
                        'reason': ai.get('reason', '').strip(),
                        'tradeoffs': ai.get('tradeoffs', '').strip()}}
    except Exception as e:
        return {'success': False, 'fallback': True, 'error': str(e),
                'message': 'AI call failed. Falling back to deterministic matching.'}
    return {'success': False, 'fallback': True,
            'message': 'AI recommendation could not be validated.'}


# ─────────────────────────────────────────────────────────────
# HTTP HANDLER
# ─────────────────────────────────────────────────────────────
class LaptopHubHandler(BaseHTTPRequestHandler):

    # ── request plumbing ──────────────────────────────────────
    def __init__(self, *args, **kwargs):
        self._body  = b''
        self._json  = None
        self._cookies: dict = {}
        super().__init__(*args, **kwargs)

    def log_message(self, fmt, *args):
        log.info("HTTP %s %s", self.command, self.path.split('?')[0])

    def _read_body(self):
        cl = int(self.headers.get('Content-Length', 0))
        if cl > MAX_UPLOAD_BYTES:
            self._send(413, {'error': 'Payload too large'})
            return False
        self._body = self.rfile.read(cl) if cl else b''
        if self._body:
            try:
                self._json = json.loads(self._body.decode('utf-8'))
            except Exception:
                self._json = {}
        else:
            self._json = {}
        return True

    def _parse_cookies(self):
        raw = self.headers.get('Cookie', '')
        c = SimpleCookie()
        c.load(raw)
        self._cookies = {k: v.value for k, v in c.items()}

    def _get_cust_user(self):
        self._parse_cookies()
        token = self._cookies.get(CUST_COOKIE, '')
        user = get_session_user(token, is_admin=False)
        if not user:
            admin_tok = self._cookies.get(ADMIN_COOKIE, '')
            if admin_tok:
                user = get_session_user(admin_tok, is_admin=True)
        return user

    def _get_admin_user(self):
        self._parse_cookies()
        token = self._cookies.get(ADMIN_COOKIE, '')
        return get_session_user(token, is_admin=True)

    def _require_admin(self):
        user = self._get_admin_user()
        if not user:
            self._send(401, {'error': 'Unauthorized'})
            return None
        return user

    def _require_customer(self):
        user = self._get_cust_user()
        if not user:
            self._send(401, {'error': 'Please sign in to place your order'})
            return None
        return user

    # ── response helpers ──────────────────────────────────────
    def _send(self, code: int, body=None, extra_headers: dict = None,
              no_cache: bool = False, set_cookie = None):
        self.send_response(code)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', self.headers.get('Origin', '*'))
        self.send_header('Access-Control-Allow-Credentials', 'true')
        self.send_header('Access-Control-Allow-Methods', 'GET,POST,PUT,DELETE,OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        if no_cache:
            self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')
            self.send_header('Pragma', 'no-cache')
            self.send_header('Expires', '0')
        if set_cookie:
            if isinstance(set_cookie, (list, tuple)):
                for ck in set_cookie:
                    self.send_header('Set-Cookie', ck)
            else:
                self.send_header('Set-Cookie', set_cookie)
        if extra_headers:
            for k, v in extra_headers.items():
                self.send_header(k, v)
        self.end_headers()
        if body is not None:
            self.wfile.write(json.dumps(body).encode('utf-8'))

    def _redirect(self, location: str, code: int = 302):
        self.send_response(code)
        self.send_header('Location', location)
        self.send_header('Content-Length', '0')
        self.end_headers()

    def _cookie_header(self, name: str, value: str, max_age: int,
                       path: str = '/') -> str:
        if max_age <= 0:
            return (f"{name}=; Path={path}; HttpOnly; SameSite=Strict; "
                    f"Max-Age=0; Expires=Thu, 01 Jan 1970 00:00:00 GMT")
        return f"{name}={value}; Path={path}; HttpOnly; SameSite=Strict; Max-Age={max_age}"

    # ── routing ───────────────────────────────────────────────
    def do_OPTIONS(self):
        self._send(200)

    def do_GET(self):
        parsed_url = urllib.parse.urlparse(self.path)
        path = parsed_url.path.rstrip('/')
        qs_params = urllib.parse.parse_qs(parsed_url.query)
        self._parse_cookies()

        # ── legacy redirects ─────────────────────────────────
        if path in ('/volts.html', '/volts'):
            return self._redirect('/laptophub.html')
        if path in ('/custom-laptop.html', '/custom-laptop'):
            return self._redirect('/consult.html')
        if path in ('/inventory', '/inventory.html'):
            return self._redirect('/admin/')

        # ── public inventory (visible items only) ────────────
        if path == '/api/inventory':
            laptops = public_inventory(load_inventory())
            self._send(200, laptops)
            return

        # ── public / admin: RAM pricing tiers ─────────────────
        if path == '/api/config/ram-pricing':
            tiers = load_ram_pricing()
            d4 = tiers.get('DDR4', tiers.get('ddr4', {}))
            d5 = tiers.get('DDR5', tiers.get('ddr5', {}))
            self._send(200, {
                'success': True,
                'DDR4': d4,
                'DDR5': d5,
                'ddr4': d4,
                'ddr5': d5,
                'tiers': {'DDR4': d4, 'DDR5': d5}
            }, no_cache=True)
            return

        # ── public: who am I? ────────────────────────────────
        if path == '/api/auth/me':
            user = self._get_cust_user()
            if not user:
                self._send(401, {'error': 'Not authenticated'}, no_cache=True)
                return
            u_info = {
                'id': user['id'], 'name': user['name'],
                'email': user['email'], 'role': user['role'],
                'phone': user.get('phone') or '',
                'city': user.get('city') or '',
                'address': user.get('address') or ''
            }
            self._send(200, {
                'ok': True,
                'user': u_info,
                **u_info
            }, no_cache=True)
            return

        # ── admin: who am I? ─────────────────────────────────
        if path == '/api/admin/me':
            user = self._get_admin_user()
            if not user:
                self._send(401, {'error': 'Unauthorized'}, no_cache=True)
                return
            self._send(200, {'id': user['id'], 'name': user['name'],
                             'email': user['email'], 'role': 'admin'}, no_cache=True)
            return

        # ── customer: my orders ──────────────────────────────
        if path == '/api/orders/mine':
            user = self._require_customer()
            if not user: return
            with get_db() as conn:
                rows = conn.execute(
                    "SELECT id,items,total_pkr,cust_name,cust_city,status,created_at "
                    "FROM orders WHERE user_id=? ORDER BY created_at DESC",
                    (user['id'],)).fetchall()
            orders = []
            for r in rows:
                o = dict(r)
                o['items'] = json.loads(o['items'])
                orders.append(o)
            self._send(200, {'ok': True, 'orders': orders}, no_cache=True)
            return

        # ── public: product reviews ──────────────────────────
        if path == '/api/reviews':
            laptop_id_vals = qs_params.get('laptop_id', [])
            laptop_id = laptop_id_vals[0] if laptop_id_vals else None
            with get_db() as conn:
                if laptop_id:
                    rows = conn.execute(
                        "SELECT id, user_id, laptop_id, reviewer, rating, body, created_at "
                        "FROM reviews WHERE laptop_id=? AND approved=1 ORDER BY id DESC",
                        (laptop_id,)).fetchall()
                    agg = conn.execute(
                        "SELECT COUNT(*), AVG(rating) FROM reviews WHERE laptop_id=? AND approved=1",
                        (laptop_id,)).fetchone()
                else:
                    rows = conn.execute(
                        "SELECT id, user_id, laptop_id, reviewer, rating, body, created_at "
                        "FROM reviews WHERE approved=1 ORDER BY id DESC LIMIT 50").fetchall()
                    agg = conn.execute("SELECT COUNT(*), AVG(rating) FROM reviews WHERE approved=1").fetchone()
            
            count = agg[0] if agg else 0
            avg_rating = round(agg[1], 1) if (agg and agg[1]) else 5.0
            reviews_list = [dict(r) for r in rows]
            self._send(200, {
                'ok': True,
                'count': count,
                'average': avg_rating,
                'reviews': reviews_list
            }, no_cache=True)
            return

        # ── admin: full inventory ─────────────────────────────
        if path == '/api/admin/inventory':
            if not self._require_admin(): return
            self._send(200, load_inventory(), no_cache=True)
            return

        # ── admin: all orders ─────────────────────────────────
        if path == '/api/admin/orders':
            if not self._require_admin(): return
            with get_db() as conn:
                rows = conn.execute(
                    "SELECT o.id, o.user_id, u.email, o.items, o.total_pkr, "
                    "o.cust_name, o.cust_phone, o.cust_city, o.cust_address, "
                    "o.status, o.notes, o.created_at, o.updated_at "
                    "FROM orders o JOIN users u ON u.id=o.user_id "
                    "ORDER BY o.created_at DESC").fetchall()
            orders = []
            for r in rows:
                o = dict(r)
                o['items'] = json.loads(o['items'])
                orders.append(o)
            self._send(200, orders, no_cache=True)
            return

        # ── admin: users list ─────────────────────────────────
        if path == '/api/admin/users':
            if not self._require_admin(): return
            with get_db() as conn:
                rows = conn.execute(
                    "SELECT id,email,name,phone,city,role,is_active,created_at FROM users "
                    "ORDER BY created_at DESC").fetchall()
            self._send(200, [dict(r) for r in rows], no_cache=True)
            return

        # ── admin: reviews ────────────────────────────────────
        if path == '/api/admin/reviews':
            if not self._require_admin(): return
            with get_db() as conn:
                rows = conn.execute(
                    "SELECT r.id,r.reviewer,r.laptop_id,r.rating,r.body,r.approved,r.created_at,"
                    "u.email as user_email FROM reviews r "
                    "LEFT JOIN users u ON u.id=r.user_id ORDER BY r.created_at DESC").fetchall()
            self._send(200, [dict(r) for r in rows], no_cache=True)
            return

        # ── admin: log ────────────────────────────────────────
        if path == '/api/admin/log':
            if not self._require_admin(): return
            with get_db() as conn:
                rows = conn.execute(
                    "SELECT l.*,u.email as admin_email FROM admin_log l "
                    "JOIN users u ON u.id=l.admin_id ORDER BY l.created_at DESC LIMIT 200"
                ).fetchall()
            self._send(200, [dict(r) for r in rows], no_cache=True)
            return

        # ── admin pages: serve SPA or redirect to login ───────
        if path == '/admin' or path.startswith('/admin/'):
            admin_user = self._get_admin_user()
            # /admin/login serves regardless
            if path in ('/admin/login', '/admin/login.html'):
                self._serve_file(os.path.join(ADMIN_DIR, 'login.html'))
                return
            if not admin_user:
                return self._redirect('/admin/login')
            # serve admin SPA
            spa = os.path.join(ADMIN_DIR, 'index.html')
            self._serve_file(spa, no_cache=True)
            return

        # ── static files ──────────────────────────────────────
        self._serve_static()

    def do_POST(self):
        path = self.path.split('?')[0]
        if not self._read_body():
            return
        payload = self._json or {}

        # ── customer signup / registration ─────────────────────
        if path in ('/api/auth/signup', '/api/auth/register'):
            email    = str(payload.get('email', '')).strip().lower()
            password = str(payload.get('password', ''))
            name     = str(payload.get('name', '')).strip()[:120]
            phone    = str(payload.get('phone', '')).strip()
            city     = str(payload.get('city', '')).strip()[:60]
            address  = str(payload.get('address', '')).strip()[:300]

            if not validate_email(email):
                return self._send(400, {'error': 'Invalid email address'})
            if len(password) < 8:
                return self._send(400, {'error': 'Password must be at least 8 characters'})
            if not name:
                return self._send(400, {'error': 'Name is required'})
            if phone and not validate_pk_phone(phone):
                return self._send(400, {'error': 'Please enter a valid Pakistani phone number (format: 03XX-XXXXXXX)'})

            with get_db() as conn:
                existing = conn.execute("SELECT id FROM users WHERE email=?", (email,)).fetchone()
                if existing:
                    return self._send(409, {'error': 'An account with this email already exists'})
                conn.execute(
                    "INSERT INTO users(email,name,phone,city,address,pass_hash,role) VALUES(?,?,?,?,?,?,'user')",
                    (email, name, phone, city, address, hash_password(password)))
                uid = conn.execute("SELECT last_insert_rowid()").fetchone()[0]

            ip = self.client_address[0]
            ua = self.headers.get('User-Agent', '')
            token = create_session(uid, ip, ua)
            cust_cookie = self._cookie_header(CUST_COOKIE, token, CUST_TTL)
            clear_admin = self._cookie_header(ADMIN_COOKIE, '', 0, path='/')
            u_info = {
                'id': uid, 'email': email, 'name': name,
                'phone': phone, 'city': city, 'address': address, 'role': 'user'
            }
            self._send(201, {
                'ok': True, 'id': uid, 'email': email, 'name': name,
                'phone': phone, 'city': city, 'address': address, 'role': 'user',
                'user': u_info
            }, set_cookie=[cust_cookie, clear_admin])
            return

        # ── customer login ────────────────────────────────────
        if path == '/api/auth/login':
            email    = str(payload.get('email', '')).strip().lower()
            password = str(payload.get('password', ''))
            ip       = self.client_address[0]

            if is_rate_limited(ip, email, CUST_MAX_ATTEMPTS, CUST_WINDOW_SECS):
                return self._send(429, {'error': 'Too many attempts. Try again in 15 minutes.'})

            with get_db() as conn:
                row = conn.execute(
                    "SELECT id,email,name,role,pass_hash,is_active,phone,city,address FROM users WHERE email=?",
                    (email,)).fetchone()

            valid = row and verify_password(password, row['pass_hash'])
            if not valid or not row['is_active']:
                record_attempt(ip, email)
                return self._send(401, {'error': 'Invalid credentials'})

            ua    = self.headers.get('User-Agent', '')
            token = create_session(row['id'], ip, ua)

            if row['role'] == 'admin':
                admin_cookie = self._cookie_header(ADMIN_COOKIE, token, ADMIN_TTL)
                cust_cookie  = self._cookie_header(CUST_COOKIE, token, ADMIN_TTL)
                u_info = {
                    'id': row['id'], 'email': row['email'], 'name': row['name'],
                    'role': 'admin', 'phone': row['phone'] or '',
                    'city': row['city'] or '', 'address': row['address'] or ''
                }
                self._send(200, {
                    'ok': True, 'id': row['id'], 'email': row['email'],
                    'name': row['name'], 'role': 'admin', 'redirect': '/admin/',
                    'user': u_info
                }, set_cookie=[admin_cookie, cust_cookie])
                return

            cust_cookie = self._cookie_header(CUST_COOKIE, token, CUST_TTL)
            clear_admin = self._cookie_header(ADMIN_COOKIE, '', 0, path='/')
            u_info = {
                'id': row['id'], 'email': row['email'], 'name': row['name'],
                'role': 'user', 'phone': row['phone'] or '',
                'city': row['city'] or '', 'address': row['address'] or ''
            }
            self._send(200, {
                'ok': True, 'id': row['id'], 'email': row['email'],
                'name': row['name'], 'role': 'user',
                'user': u_info
            }, set_cookie=[cust_cookie, clear_admin])
            return

        # ── customer logout ───────────────────────────────────
        if path == '/api/auth/logout':
            self._parse_cookies()
            ctoken = self._cookies.get(CUST_COOKIE, '')
            atoken = self._cookies.get(ADMIN_COOKIE, '')
            if ctoken:
                delete_session(ctoken)
            if atoken:
                delete_session(atoken)
            cookies = [
                self._cookie_header(CUST_COOKIE, '', 0, path='/'),
                self._cookie_header(ADMIN_COOKIE, '', 0, path='/')
            ]
            self._send(200, {'ok': True}, set_cookie=cookies, no_cache=True)
            return

        # ── customer update profile ───────────────────────────
        if path == '/api/auth/profile':
            user = self._require_customer()
            if not user: return

            name = str(payload.get('name', '')).strip()[:120]
            phone = str(payload.get('phone', '')).strip()
            city = str(payload.get('city', '')).strip()[:60]
            address = str(payload.get('address', '')).strip()[:300]

            if phone and not validate_pk_phone(phone):
                return self._send(400, {'error': 'Invalid Pakistani phone number (format: 03XX-XXXXXXX)'})

            with get_db() as conn:
                conn.execute(
                    "UPDATE users SET name=?, phone=?, city=?, address=?, updated_at=datetime('now','utc') "
                    "WHERE id=?",
                    (name or user['name'], phone, city, address, user['id']))

            self._send(200, {
                'ok': True,
                'success': True,
                'name': name or user['name'],
                'phone': phone,
                'city': city,
                'address': address
            }, no_cache=True)
            return

        # ── customer change password ──────────────────────────
        if path == '/api/auth/change-password':
            user = self._require_customer()
            if not user: return

            curr_pw = str(payload.get('current_password', ''))
            new_pw = str(payload.get('new_password', ''))

            if len(new_pw) < 8:
                return self._send(400, {'error': 'New password must be at least 8 characters'})

            with get_db() as conn:
                row = conn.execute("SELECT pass_hash FROM users WHERE id=?", (user['id'],)).fetchone()
                if not row or not verify_password(curr_pw, row['pass_hash']):
                    return self._send(401, {'error': 'Current password is incorrect'})

                conn.execute(
                    "UPDATE users SET pass_hash=?, updated_at=datetime('now','utc') WHERE id=?",
                    (hash_password(new_pw), user['id']))

            self._send(200, {'ok': True, 'success': True, 'message': 'Password changed successfully'}, no_cache=True)
            return

        # ── admin login ───────────────────────────────────────
        if path == '/api/admin/login':
            email    = str(payload.get('email', '')).strip().lower()
            password = str(payload.get('password', ''))
            ip       = self.client_address[0]

            if is_rate_limited(ip, email, ADMIN_MAX_ATTEMPTS, ADMIN_WINDOW_SECS):
                log.warning("Admin login rate-limited: ip=%s email=%s", ip, email)
                return self._send(429, {'error': 'Invalid credentials'})  # Generic message

            with get_db() as conn:
                row = conn.execute(
                    "SELECT id,email,name,role,pass_hash,is_active FROM users WHERE email=?",
                    (email,)).fetchone()

            valid = row and verify_password(password, row['pass_hash'])
            if not valid or not row or row['role'] != 'admin' or not row['is_active']:
                record_attempt(ip, email)
                log.warning("Failed admin login: email=%s ip=%s", email, ip)
                return self._send(401, {'error': 'Invalid credentials'})

            ua    = self.headers.get('User-Agent', '')
            token = create_session(row['id'], ip, ua)
            cookie = self._cookie_header(ADMIN_COOKIE, token, ADMIN_TTL, path='/')
            log.info("Admin login success: email=%s ip=%s", email, ip)
            self._send(200, {'id': row['id'], 'email': row['email'],
                             'name': row['name'], 'role': 'admin'},
                       set_cookie=cookie, no_cache=True)
            return

        # ── admin logout ──────────────────────────────────────
        if path == '/api/admin/logout':
            self._parse_cookies()
            ctoken = self._cookies.get(CUST_COOKIE, '')
            atoken = self._cookies.get(ADMIN_COOKIE, '')
            if ctoken:
                delete_session(ctoken)
            if atoken:
                delete_session(atoken)
            cookies = [
                self._cookie_header(ADMIN_COOKIE, '', 0, path='/'),
                self._cookie_header(CUST_COOKIE, '', 0, path='/')
            ]
            self._send(200, {'ok': True}, set_cookie=cookies, no_cache=True)
            return

        # ── place order (signed-in customer only) ──────────
        if path == '/api/orders':
            user = self._require_customer()
            if not user:
                return

            items    = payload.get('items', [])
            cust_name = str(payload.get('name', '')).strip()[:120]
            cust_phone= str(payload.get('phone', '')).strip()
            cust_city = str(payload.get('city', '')).strip()[:60]
            cust_addr = str(payload.get('address', '')).strip()[:300]

            if not items:
                return self._send(400, {'error': 'Cart is empty'})
            if not cust_name:
                return self._send(400, {'error': 'Name is required'})
            if not validate_pk_phone(cust_phone):
                return self._send(400, {'error': 'Please enter a valid Pakistani phone number (03XX-XXXXXXX)'})
            if not cust_city:
                return self._send(400, {'error': 'City is required'})
            if not cust_addr:
                return self._send(400, {'error': 'Delivery address is required'})

            # Stock validation against inventory
            laptops = load_inventory()
            for item in items:
                lid = item.get('id') or item.get('laptop_id')
                qty = item.get('qty', 1)
                for lap in laptops:
                    if lap.get('id') == lid:
                        cur_stock = lap.get('stock', 1)
                        if cur_stock <= 0:
                            return self._send(400, {'error': f"'{lap.get('name', 'Laptop')}' is currently out of stock."})
                        if qty > cur_stock:
                            return self._send(400, {'error': f"Only {cur_stock} units available for '{lap.get('name', 'Laptop')}'."})
                        break

            total = sum((i.get('price', 0) * i.get('qty', 1)) for i in items)
            items_json = json.dumps(items)

            with get_db() as conn:
                user_id = user['id']
                conn.execute(
                    "INSERT INTO orders(user_id,items,total_pkr,cust_name,cust_phone,cust_city,cust_address) "
                    "VALUES(?,?,?,?,?,?,?)",
                    (user_id, items_json, total, cust_name, cust_phone, cust_city, cust_addr))
                oid = conn.execute("SELECT last_insert_rowid()").fetchone()[0]

                # Update customer profile defaults in users table
                conn.execute(
                    "UPDATE users SET name=COALESCE(NULLIF(name,''), ?), "
                    "phone=COALESCE(NULLIF(phone,''), ?), "
                    "city=COALESCE(NULLIF(city,''), ?), "
                    "address=COALESCE(NULLIF(address,''), ?), "
                    "updated_at=datetime('now','utc') WHERE id=?",
                    (cust_name, cust_phone, cust_city, cust_addr, user['id']))

            # Automatically decrement inventory stock
            inv_changed = False
            for item in items:
                lid = item.get('id') or item.get('laptop_id')
                qty = item.get('qty', 1)
                for lap in laptops:
                    if lap.get('id') == lid:
                        lap['stock'] = max(0, lap.get('stock', 1) - qty)
                        inv_changed = True
                        break
            if inv_changed:
                save_inventory(laptops)

            self._send(201, {'orderId': oid, 'status': 'new', 'total': total})
            return

        # ── customer: post product review ─────────────────────
        if path == '/api/reviews':
            user = self._require_customer()
            if not user:
                return

            try:
                laptop_id = int(payload.get('laptop_id'))
            except (ValueError, TypeError):
                return self._send(400, {'error': 'Valid laptop_id is required'})

            try:
                rating = int(payload.get('rating', 5))
                if rating < 1 or rating > 5:
                    return self._send(400, {'error': 'Rating must be between 1 and 5'})
            except (ValueError, TypeError):
                return self._send(400, {'error': 'Rating must be an integer between 1 and 5'})

            raw_body = str(payload.get('body', '')).strip()
            if len(raw_body) < 3:
                return self._send(400, {'error': 'Review comment must be at least 3 characters'})
            if len(raw_body) > 2000:
                return self._send(400, {'error': 'Review comment cannot exceed 2000 characters'})

            safe_body = html.escape(raw_body)
            reviewer_name = user.get('name') or user.get('email', 'Verified Customer')

            with get_db() as conn:
                conn.execute(
                    "INSERT INTO reviews (user_id, laptop_id, reviewer, rating, body, approved) "
                    "VALUES (?, ?, ?, ?, ?, 1)",
                    (user['id'], laptop_id, reviewer_name, rating, safe_body))
                rid = conn.execute("SELECT last_insert_rowid()").fetchone()[0]

            self._send(201, {
                'ok': True,
                'success': True,
                'review': {
                    'id': rid,
                    'user_id': user['id'],
                    'laptop_id': laptop_id,
                    'reviewer': reviewer_name,
                    'rating': rating,
                    'body': safe_body,
                    'created_at': datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S')
                }
            }, no_cache=True)
            return

        # ── admin or customer: delete review ───────────────────
        if path == '/api/reviews/delete':
            admin = self._get_admin_user()
            cust = self._get_cust_user()
            if not admin and not cust:
                return self._send(401, {'error': 'Authentication required'})

            rid = payload.get('id') or payload.get('review_id')
            if not rid:
                return self._send(400, {'error': 'Review ID is required'})

            with get_db() as conn:
                if admin:
                    conn.execute("DELETE FROM reviews WHERE id=?", (rid,))
                    self._send(200, {'ok': True, 'message': 'Review deleted by admin'}, no_cache=True)
                else:
                    cur = conn.execute("DELETE FROM reviews WHERE id=? AND user_id=?", (rid, cust['id']))
                    if cur.rowcount == 0:
                        return self._send(403, {'error': 'You can only delete your own reviews'})
                    self._send(200, {'ok': True, 'message': 'Review deleted'}, no_cache=True)
            return

        # ── admin: add laptop ─────────────────────────────────
        if path == '/api/admin/inventory/add':
            admin = self._require_admin()
            if not admin: return
            laptops = load_inventory()
            new_id  = max((l.get('id', 0) for l in laptops), default=0) + 1
            payload['id'] = new_id
            payload.setdefault('brand', 'other')
            payload.setdefault('brandName', payload['brand'].capitalize())
            payload.setdefault('category', 'Ultrabook')
            payload.setdefault('badge', 'New Arrival')
            payload.setdefault('condition', 'Like New (10/10) · Certified Refurbished')
            payload.setdefault('warranty', '1 Year Local Warranty + 7 Days Checking')
            payload.setdefault('useCases', ['office', 'student'])
            payload.setdefault('img', 'images/lenovo-t14-g1.jpg')
            payload.setdefault('hidden', False)
            payload.setdefault('stock', 1)
            laptops.append(payload)
            save_inventory(laptops)
            log_admin_action(admin['id'], 'add_laptop', new_id, payload.get('name', ''))
            self._send(201, {'success': True, 'laptop': payload}, no_cache=True)
            return

        # ── admin: update laptop ──────────────────────────────
        if path == '/api/admin/inventory/update':
            admin = self._require_admin()
            if not admin: return
            tid = payload.get('id')
            if not tid:
                return self._send(400, {'error': 'id required'})
            laptops = load_inventory()
            found = False
            for i, l in enumerate(laptops):
                if l.get('id') == tid:
                    laptops[i].update(payload)
                    found = True
                    break
            if not found:
                return self._send(404, {'error': 'Laptop not found'})
            save_inventory(laptops)
            log_admin_action(admin['id'], 'update_laptop', tid, payload.get('name', ''))
            self._send(200, {'success': True}, no_cache=True)
            return

        # ── admin: save ram pricing tiers ─────────────────────
        if path == '/api/admin/config/ram-pricing':
            admin = self._require_admin()
            if not admin: return
            tiers_input = payload.get('tiers', payload)
            ddr4 = tiers_input.get('DDR4') or tiers_input.get('ddr4')
            ddr5 = tiers_input.get('DDR5') or tiers_input.get('ddr5')
            current = load_ram_pricing()
            if ddr4:
                current['DDR4'] = {str(k): int(v) for k, v in ddr4.items()}
            if ddr5:
                current['DDR5'] = {str(k): int(v) for k, v in ddr5.items()}
            save_ram_pricing(current)
            log_admin_action(admin['id'], 'update_ram_pricing', 'pricing_matrix', json.dumps(current))
            self._send(200, {
                'success': True,
                'tiers': current,
                'ddr4': current.get('DDR4', {}),
                'ddr5': current.get('DDR5', {})
            }, no_cache=True)
            return

        # ── admin: upload image ───────────────────────────────
        if path == '/api/admin/upload-image':
            admin = self._require_admin()
            if not admin: return

            filename = payload.get('filename', '')
            image_b64 = payload.get('data', '')

            if not filename or not image_b64:
                return self._send(400, {'error': 'filename and base64 data required'})

            clean_name = re.sub(r'[^a-zA-Z0-9_\-\.]', '', os.path.basename(filename)).lower()
            ext = os.path.splitext(clean_name)[1]
            if ext not in ('.jpg', '.jpeg', '.png', '.webp'):
                return self._send(400, {'error': 'Invalid file type. Allowed: jpg, jpeg, png, webp'})

            if ',' in image_b64:
                image_b64 = image_b64.split(',', 1)[1]

            try:
                raw_bytes = base64.b64decode(image_b64)
            except Exception:
                return self._send(400, {'error': 'Invalid base64 payload'})

            if len(raw_bytes) > MAX_UPLOAD_BYTES:
                return self._send(400, {'error': f'Image exceeds {MAX_UPLOAD_BYTES // (1024*1024)}MB limit'})

            dest_filename = f"{os.path.splitext(clean_name)[0]}_{int(time.time())}{ext}"
            dest_rel_path = f"images/{dest_filename}"
            dest_abs_path = os.path.join(BASE_DIR, 'images', dest_filename)

            with open(dest_abs_path, 'wb') as f:
                f.write(raw_bytes)

            bg_meta = {'bgTone': 'white', 'tintColor': 'rgba(76, 124, 255, 0.04)', 'processedImg': None}
            try:
                from scripts.process_image_blending import analyze_image_background
                analysis = analyze_image_background(dest_rel_path)
                bg_meta['bgTone'] = analysis.get('tone', 'white')
                bg_meta['tintColor'] = analysis.get('tint_color', '')
            except Exception as ex:
                log.warning("Image background analysis exception: %s", ex)

            log_admin_action(admin['id'], 'upload_image', None, dest_rel_path)
            self._send(200, {
                'success': True,
                'path': dest_rel_path,
                'bgTone': bg_meta['bgTone'],
                'tintColor': bg_meta['tintColor']
            }, no_cache=True)
            return

        # ── admin: archive (hide) laptop ──────────────────────
        if path == '/api/admin/inventory/archive':
            admin = self._require_admin()
            if not admin: return
            tid = payload.get('id')
            laptops = load_inventory()
            found = False
            for i, l in enumerate(laptops):
                if l.get('id') == tid:
                    laptops[i]['hidden'] = True
                    found = True
                    break
            if not found:
                return self._send(404, {'error': 'Laptop not found'})
            save_inventory(laptops)
            log_admin_action(admin['id'], 'archive_laptop', tid)
            self._send(200, {'success': True}, no_cache=True)
            return

        # ── admin: unarchive laptop ───────────────────────────
        if path == '/api/admin/inventory/unarchive':
            admin = self._require_admin()
            if not admin: return
            tid = payload.get('id')
            laptops = load_inventory()
            found = False
            for i, l in enumerate(laptops):
                if l.get('id') == tid:
                    laptops[i]['hidden'] = False
                    found = True
                    break
            if not found:
                return self._send(404, {'error': 'Laptop not found'})
            save_inventory(laptops)
            log_admin_action(admin['id'], 'unarchive_laptop', tid)
            self._send(200, {'success': True}, no_cache=True)
            return

        # ── admin: delete laptop (hard) ───────────────────────
        if path == '/api/admin/inventory/delete':
            admin = self._require_admin()
            if not admin: return
            tid = payload.get('id')
            confirm = payload.get('confirm', False)
            if not confirm:
                return self._send(400, {'error': 'Confirmation required for delete'})
            laptops = load_inventory()
            before = len(laptops)
            laptops = [l for l in laptops if l.get('id') != tid]
            if len(laptops) == before:
                return self._send(404, {'error': 'Laptop not found'})
            save_inventory(laptops)
            log_admin_action(admin['id'], 'delete_laptop', tid)
            self._send(200, {'success': True, 'remaining': len(laptops)}, no_cache=True)
            return

        # ── admin: update stock ───────────────────────────────
        if path == '/api/admin/inventory/stock':
            admin = self._require_admin()
            if not admin: return
            tid   = payload.get('id')
            stock = payload.get('stock')
            if stock is None or not isinstance(stock, int) or stock < 0:
                return self._send(400, {'error': 'Invalid stock value'})
            laptops = load_inventory()
            found = False
            for i, l in enumerate(laptops):
                if l.get('id') == tid:
                    laptops[i]['stock'] = stock
                    found = True
                    break
            if not found:
                return self._send(404, {'error': 'Laptop not found'})
            save_inventory(laptops)
            log_admin_action(admin['id'], 'update_stock', tid, f"stock={stock}")
            self._send(200, {'success': True}, no_cache=True)
            return

        # ── admin: update order status ────────────────────────
        if path == '/api/admin/orders/status':
            admin = self._require_admin()
            if not admin: return
            oid    = payload.get('orderId')
            status = payload.get('status', '')
            valid_statuses = ('new', 'confirmed', 'shipped', 'delivered', 'cancelled')
            if status not in valid_statuses:
                return self._send(400, {'error': f'Invalid status. Use: {", ".join(valid_statuses)}'})
            with get_db() as conn:
                r = conn.execute("SELECT id FROM orders WHERE id=?", (oid,)).fetchone()
                if not r:
                    return self._send(404, {'error': 'Order not found'})
                conn.execute(
                    "UPDATE orders SET status=?, updated_at=datetime('now','utc') WHERE id=?",
                    (status, oid))
            log_admin_action(admin['id'], 'update_order_status', oid, status)
            self._send(200, {'success': True}, no_cache=True)
            return

        # ── admin: disable user ───────────────────────────────
        if path == '/api/admin/users/disable':
            admin = self._require_admin()
            if not admin: return
            uid = payload.get('userId')
            with get_db() as conn:
                conn.execute("UPDATE users SET is_active=0 WHERE id=? AND role='user'", (uid,))
            log_admin_action(admin['id'], 'disable_user', uid)
            self._send(200, {'success': True}, no_cache=True)
            return

        # ── admin: approve review ─────────────────────────────
        if path == '/api/admin/reviews/approve':
            admin = self._require_admin()
            if not admin: return
            rid = payload.get('reviewId')
            with get_db() as conn:
                conn.execute("UPDATE reviews SET approved=1 WHERE id=?", (rid,))
            log_admin_action(admin['id'], 'approve_review', rid)
            self._send(200, {'success': True}, no_cache=True)
            return

        # ── admin: delete review ──────────────────────────────
        if path == '/api/admin/reviews/delete':
            admin = self._require_admin()
            if not admin: return
            rid = payload.get('reviewId')
            with get_db() as conn:
                conn.execute("DELETE FROM reviews WHERE id=?", (rid,))
            log_admin_action(admin['id'], 'delete_review', rid)
            self._send(200, {'success': True}, no_cache=True)
            return

        # ── admin: save full inventory (bulk) ────────────────
        if path == '/api/admin/save-all':
            admin = self._require_admin()
            if not admin: return
            items = payload.get('laptops', [])
            if items:
                save_inventory(items)
                log_admin_action(admin['id'], 'bulk_save', '', f"{len(items)} items")
            self._send(200, {'success': True, 'count': len(items)}, no_cache=True)
            return

        # ── admin: fetch photo ────────────────────────────────
        if path in ('/api/admin/fetch-photo', '/api/fetch-photo'):
            admin = self._require_admin()
            if not admin: return
            query     = str(payload.get('query', ''))
            laptop_id = str(payload.get('id', 'temp'))
            slug      = re.sub(r'[^a-z0-9]+', '-', query.lower()).strip('-')[:30]
            filename  = f"laptop-{laptop_id}-{slug}.jpg"
            img_rel, size = fetch_photo_for_laptop(query, filename)
            if img_rel:
                self._send(200, {'success': True, 'img': img_rel, 'sizeBytes': size}, no_cache=True)
            else:
                self._send(500, {'error': 'Could not retrieve photo'})
            return

        # ── admin: update RAM pricing tiers ───────────────────
        if path == '/api/admin/config/ram-pricing':
            admin = self._require_admin()
            if not admin: return
            if not isinstance(payload, dict):
                return self._send(400, {'error': 'Invalid tiers payload'})
            saved = save_ram_pricing(payload)
            if saved:
                log_admin_action(admin['id'], 'update_ram_pricing', '', json.dumps(payload))
                self._send(200, {'success': True, 'tiers': payload}, no_cache=True)
            else:
                self._send(500, {'error': 'Failed to save RAM pricing tiers'}, no_cache=True)
            return

        # ── AI consultation ───────────────────────────────────
        if path == '/api/consult/ai-recommend':
            ip   = self.client_address[0]
            now  = time.time()
            reqs = AI_RATE_CACHE.get(ip, [])
            reqs = [t for t in reqs if now - t < 60]
            if len(reqs) >= 12:
                return self._send(429, {'success': False, 'fallback': True,
                                        'error': 'Rate limit exceeded (max 12 req/min).'})
            reqs.append(now)
            AI_RATE_CACHE[ip] = reqs

            prefs   = payload.get('preferences', {})
            matched = payload.get('matchedLaptops', [])
            if not matched:
                return self._send(200, {'success': False, 'fallback': True,
                                        'message': 'No matched laptops provided.'})
            result = get_ai_recommendation(prefs, matched)
            self._send(200, result)
            return

        # ── legacy compat: /api/laptop/add etc. ──────────────
        if path == '/api/laptop/add':
            return self._redirect('/api/admin/inventory/add', 308)
        if path == '/api/laptop/update':
            return self._redirect('/api/admin/inventory/update', 308)
        if path == '/api/laptop/delete':
            return self._redirect('/api/admin/inventory/delete', 308)
        if path == '/api/save-all':
            return self._redirect('/api/admin/save-all', 308)

        self._send(404, {'error': 'Not found'})

    # ── static file serving ───────────────────────────────────
    MIME_MAP = {
        '.html': 'text/html; charset=utf-8',
        '.js':   'application/javascript',
        '.css':  'text/css',
        '.json': 'application/json',
        '.webp': 'image/webp',
        '.png':  'image/png',
        '.jpg':  'image/jpeg',
        '.jpeg': 'image/jpeg',
        '.gif':  'image/gif',
        '.svg':  'image/svg+xml',
        '.ico':  'image/x-icon',
        '.woff2':'font/woff2',
        '.woff': 'font/woff',
        '.ttf':  'font/ttf',
        '.txt':  'text/plain',
    }

    def _serve_file(self, fpath: str, no_cache: bool = False):
        if not os.path.isfile(fpath):
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'404 Not Found')
            return
        ext  = os.path.splitext(fpath)[1].lower()
        mime = self.MIME_MAP.get(ext, 'application/octet-stream')
        size = os.path.getsize(fpath)
        self.send_response(200)
        self.send_header('Content-Type', mime)
        self.send_header('Content-Length', str(size))
        if no_cache:
            self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')
            self.send_header('Pragma', 'no-cache')
            self.send_header('Expires', '0')
        else:
            self.send_header('Cache-Control', 'max-age=300')
        self.end_headers()
        with open(fpath, 'rb') as f:
            while chunk := f.read(65536):
                self.wfile.write(chunk)

    def _serve_static(self):
        url_path = self.path.split('?')[0]
        # Prevent path traversal
        safe = url_path.lstrip('/')
        if '..' in safe:
            self.send_response(403)
            self.end_headers()
            return
        # Root → laptophub.html
        if not safe or safe == 'index.html':
            return self._serve_file(os.path.join(BASE_DIR, 'laptophub.html'))
        fpath = os.path.join(BASE_DIR, safe)
        if os.path.isfile(fpath):
            return self._serve_file(fpath)
        self.send_response(404)
        self.end_headers()
        self.wfile.write(b'404 Not Found')


# ─────────────────────────────────────────────────────────────
# SERVER STARTUP
# ─────────────────────────────────────────────────────────────
def run_server(port: int = 8080):
    init_db()
    addr = ('', port)
    httpd = HTTPServer(addr, LaptopHubHandler)
    print("=" * 65)
    print(f"  LAPTOPHUB SERVER  ->  http://localhost:{port}/laptophub.html")
    print(f"  Admin login       ->  http://localhost:{port}/admin/login")
    print(f"  Consult Me        ->  http://localhost:{port}/consult.html")
    print("=" * 65)
    print("Press Ctrl+C to stop.")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping server...")
        httpd.server_close()


# ─────────────────────────────────────────────────────────────
# CLI
# ─────────────────────────────────────────────────────────────
def run_cli_list():
    laptops = load_inventory()
    print(f"\n{'='*65}\n  INVENTORY ({len(laptops)} laptops)\n{'='*65}")
    for l in laptops:
        h = ' [HIDDEN]' if l.get('hidden') else ''
        s = l.get('stock', '?')
        print(f"[{l.get('id'):>2}] {l.get('name','?'):<38} | {l.get('priceFormatted','?'):>10} | "
              f"stock={s}{h}")
    print()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='LaptopHUB Server')
    parser.add_argument('action', nargs='?', default='serve',
                        choices=['serve', 'list'],
                        help="'serve' to start web server, 'list' to print inventory")
    parser.add_argument('--port', type=int,
                        default=int(os.environ.get('PORT', 8080)))
    args = parser.parse_args()

    if args.action == 'list':
        run_cli_list()
    else:
        run_server(args.port)
