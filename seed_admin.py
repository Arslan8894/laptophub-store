#!/usr/bin/env python3
"""
seed_admin.py — Create the first admin account for LaptopHUB
=============================================================
Run once after setting up the server. Idempotent: running again
with the same email updates the password but does not duplicate the user.

Usage:
    python seed_admin.py --email admin@example.com --password "StrongPass123!"

Or via environment variables (safer for CI):
    ADMIN_EMAIL=admin@example.com ADMIN_PASSWORD=StrongPass123! python seed_admin.py
"""

import os
import sys
import hashlib
import hmac
import secrets
import sqlite3
import argparse
import getpass

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH  = os.path.join(BASE_DIR, 'db', 'laptophub.db')


def hash_password(password: str) -> str:
    salt = secrets.token_hex(32)
    dk = hashlib.scrypt(password.encode('utf-8'), salt=bytes.fromhex(salt),
                        n=16384, r=8, p=1, dklen=64)
    return f"scrypt${salt}${dk.hex()}"


def seed(email: str, password: str, name: str = 'Admin'):
    if not os.path.exists(DB_PATH):
        print(f"[ERROR] Database not found at {DB_PATH}")
        print("       Run 'python server.py' at least once to initialize the DB, then run this script.")
        sys.exit(1)

    if len(password) < 8:
        print("[ERROR] Password must be at least 8 characters.")
        sys.exit(1)

    email = email.strip().lower()
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys=ON")

    existing = conn.execute("SELECT id, role FROM users WHERE email=?", (email,)).fetchone()
    if existing:
        # Update existing to admin + refresh password
        conn.execute(
            "UPDATE users SET role='admin', pass_hash=?, is_active=1, name=?, "
            "updated_at=datetime('now','utc') WHERE email=?",
            (hash_password(password), name, email))
        conn.commit()
        uid = existing[0]
        print(f"\n[OK] Existing account updated to admin role.")
        print(f"   ID:    {uid}")
        print(f"   Email: {email}")
    else:
        conn.execute(
            "INSERT INTO users(email, name, pass_hash, role) VALUES(?,?,?,'admin')",
            (email, name, hash_password(password)))
        conn.commit()
        uid = conn.execute("SELECT last_insert_rowid()").fetchone()[0]
        print(f"\n[OK] Admin account created.")
        print(f"   ID:    {uid}")
        print(f"   Email: {email}")
        print(f"   Name:  {name}")

    conn.close()
    print(f"\n   Admin login URL: http://localhost:8080/admin/login")
    print(f"   [NOTE] This URL is NOT linked from the public site.\n")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Create LaptopHUB admin account')
    parser.add_argument('--email',    default=os.environ.get('ADMIN_EMAIL', ''),
                        help='Admin email address')
    parser.add_argument('--password', default=os.environ.get('ADMIN_PASSWORD', ''),
                        help='Admin password (min 8 chars). Omit to prompt securely.')
    parser.add_argument('--name',     default='Admin', help='Display name (default: Admin)')
    args = parser.parse_args()

    if not args.email:
        args.email = input('Admin email: ').strip()
    if not args.password:
        args.password = getpass.getpass('Admin password (hidden): ')

    seed(args.email, args.password, args.name)
