-- LaptopHUB Database Schema
-- SQLite3 · created by server.py on first run

PRAGMA journal_mode = WAL;
PRAGMA foreign_keys = ON;

-- ─────────────────────────────────────────────
-- USERS
-- ─────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS users (
  id          INTEGER PRIMARY KEY AUTOINCREMENT,
  email       TEXT UNIQUE NOT NULL COLLATE NOCASE,
  name        TEXT,
  phone       TEXT,          -- Pakistani format, e.g. 03XX-XXXXXXX
  address     TEXT,
  city        TEXT,
  role        TEXT NOT NULL DEFAULT 'user' CHECK(role IN ('user','admin')),
  pass_hash   TEXT NOT NULL, -- algo$salt_hex$hash_hex  (scrypt)
  is_active   INTEGER NOT NULL DEFAULT 1,
  created_at  TEXT NOT NULL DEFAULT (datetime('now','utc')),
  updated_at  TEXT NOT NULL DEFAULT (datetime('now','utc'))
);

-- ─────────────────────────────────────────────
-- SESSIONS (HTTP-only cookie, server-side store)
-- ─────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS sessions (
  token       TEXT PRIMARY KEY,          -- 32-byte hex (secrets.token_hex(32))
  user_id     INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
  created_at  TEXT NOT NULL DEFAULT (datetime('now','utc')),
  last_active TEXT NOT NULL DEFAULT (datetime('now','utc')),
  ip          TEXT,
  user_agent  TEXT
);
CREATE INDEX IF NOT EXISTS idx_sessions_user ON sessions(user_id);

-- ─────────────────────────────────────────────
-- ORDERS
-- ─────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS orders (
  id          INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id     INTEGER NOT NULL REFERENCES users(id),
  items       TEXT NOT NULL,             -- JSON [{laptop_id,name,qty,price,ram,storage}]
  total_pkr   INTEGER NOT NULL,
  cust_name   TEXT NOT NULL,             -- snapshot at order time
  cust_phone  TEXT NOT NULL,
  cust_city   TEXT NOT NULL,
  cust_address TEXT NOT NULL,
  status      TEXT NOT NULL DEFAULT 'new'
              CHECK(status IN ('new','confirmed','shipped','delivered','cancelled')),
  notes       TEXT,
  created_at  TEXT NOT NULL DEFAULT (datetime('now','utc')),
  updated_at  TEXT NOT NULL DEFAULT (datetime('now','utc'))
);
CREATE INDEX IF NOT EXISTS idx_orders_user   ON orders(user_id);
CREATE INDEX IF NOT EXISTS idx_orders_status ON orders(status);

-- ─────────────────────────────────────────────
-- REVIEWS
-- ─────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS reviews (
  id          INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id     INTEGER REFERENCES users(id) ON DELETE SET NULL,
  laptop_id   INTEGER,
  reviewer    TEXT NOT NULL,
  rating      INTEGER NOT NULL CHECK(rating BETWEEN 1 AND 5),
  body        TEXT NOT NULL,
  approved    INTEGER NOT NULL DEFAULT 0,
  created_at  TEXT NOT NULL DEFAULT (datetime('now','utc'))
);
CREATE INDEX IF NOT EXISTS idx_reviews_laptop   ON reviews(laptop_id);
CREATE INDEX IF NOT EXISTS idx_reviews_approved ON reviews(approved);

-- ─────────────────────────────────────────────
-- ADMIN ACTION LOG
-- ─────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS admin_log (
  id          INTEGER PRIMARY KEY AUTOINCREMENT,
  admin_id    INTEGER NOT NULL REFERENCES users(id),
  action      TEXT NOT NULL,
  target      TEXT,
  detail      TEXT,
  created_at  TEXT NOT NULL DEFAULT (datetime('now','utc'))
);

-- ─────────────────────────────────────────────
-- AUTH RATE-LIMIT TRACKING
-- ─────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS auth_attempts (
  id           INTEGER PRIMARY KEY AUTOINCREMENT,
  ip           TEXT NOT NULL,
  email        TEXT NOT NULL COLLATE NOCASE,
  attempted_at TEXT NOT NULL DEFAULT (datetime('now','utc'))
);
CREATE INDEX IF NOT EXISTS idx_auth_attempts ON auth_attempts(ip, email, attempted_at);
