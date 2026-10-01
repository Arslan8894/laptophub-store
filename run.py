#!/usr/bin/env python3
"""
run.py — Master Launcher & Control Center for LaptopHUB & VOLTS
Provides a clean, unified command-line interface to run the server,
verify assets, manage inventory, and fetch photos.

Usage:
  python run.py server           # Start local HTTP store server & REST API (default: 8080)
  python run.py verify           # Verify health of all pages, images, and data
  python run.py list             # List all 69 inventory laptops in terminal
  python run.py fetch-photos     # Download real laptop photos from internet
  python run.py backup           # Create timestamped backup of inventory dataset
"""

import sys
import os
import argparse
import json
import shutil
import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SCRIPTS_DIR = os.path.join(BASE_DIR, 'scripts')
DATA_PATH = os.path.join(BASE_DIR, 'laptops-data.js')
BACKUPS_DIR = os.path.join(BASE_DIR, 'backups')

def cmd_server(args):
    port = args.port or 8080
    print(f"\n🚀 Launching Laptop Store Server & Admin API on http://localhost:{port} ...")
    print(f"👉 Main Portal:     http://localhost:{port}/index.html")
    print(f"👉 LaptopHub Store: http://localhost:{port}/laptophub.html")
    print(f"👉 Custom Builder:  http://localhost:{port}/custom-laptop.html")
    print(f"👉 VOLTS Store:     http://localhost:{port}/volts.html")
    print(f"👉 Consult AI:      http://localhost:{port}/consult.html")
    print(f"👉 Admin Dashboard: http://localhost:{port}/inventory.html")
    print("\nPress Ctrl+C to stop the server.\n")

    manage_script = os.path.join(BASE_DIR, 'manage_inventory.py')
    os.system(f'python "{manage_script}" --port {port}')

def cmd_verify(args):
    verify_script = os.path.join(SCRIPTS_DIR, 'verify_store.py')
    os.system(f'python "{verify_script}"')

def cmd_list(args):
    if not os.path.exists(DATA_PATH):
        print("Error: laptops-data.js not found.")
        return
    with open(DATA_PATH, 'r', encoding='utf-8') as f:
        text = f.read()
    start = text.find('[')
    end = text.rfind(']') + 1
    data = json.loads(text[start:end])

    print(f"\n{'ID':<4} {'Brand':<10} {'Name':<34} {'RAM':<6} {'Price (PKR)':<14} {'Status'}")
    print("-" * 75)
    for lap in data:
        lid = lap.get('id', '-')
        brand = lap.get('brandName', lap.get('brand', ''))
        name = (lap.get('name', '')[:32] + '..') if len(lap.get('name', '')) > 34 else lap.get('name', '')
        ram = f"{lap.get('ram', '')}GB"
        price = lap.get('priceFormatted', f"Rs {lap.get('price', 0):,}")
        status = "In Stock" if lap.get('inStock', True) else "Out of Stock"
        print(f"#{lid:<3} {brand:<10} {name:<34} {ram:<6} {price:<14} {status}")
    print("-" * 75)
    print(f"Total: {len(data)} verified models\n")

def cmd_backup(args):
    os.makedirs(BACKUPS_DIR, exist_ok=True)
    timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_file = os.path.join(BACKUPS_DIR, f'laptops_backup_{timestamp}.js')
    shutil.copy2(DATA_PATH, backup_file)
    print(f"✅ Created inventory backup: {backup_file}")

def cmd_fetch_photos(args):
    fetch_script = os.path.join(SCRIPTS_DIR, 'retrieve_laptop_photos.py')
    if os.path.exists(fetch_script):
        os.system(f'python "{fetch_script}"')
    else:
        manage_script = os.path.join(BASE_DIR, 'manage_inventory.py')
        os.system(f'python "{manage_script}" --fetch-photos')

def main():
    parser = argparse.ArgumentParser(
        description="LaptopHUB & VOLTS Master Store Control Center",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python run.py server          Start local dev server on port 8080
  python run.py verify          Run full integrity & health checks
  python run.py list            Display formatted inventory table
  python run.py backup          Backup current inventory dataset
  python run.py fetch-photos    Download real product photos from internet
        """
    )
    subparsers = parser.add_subparsers(dest='command', help='Command to run')

    # server
    p_server = subparsers.add_parser('server', help='Start local store HTTP server & API')
    p_server.add_argument('--port', type=int, default=8080, help='Port to bind (default: 8080)')

    # verify
    subparsers.add_parser('verify', help='Run comprehensive system health check')

    # list
    subparsers.add_parser('list', help='List all 69 inventory laptops')

    # backup
    subparsers.add_parser('backup', help='Create timestamped backup of laptops-data.js')

    # fetch-photos
    subparsers.add_parser('fetch-photos', help='Retrieve laptop photos from internet')

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        print("\n💡 Quick Start: Run 'python run.py verify' or 'python run.py server'")
        return

    commands = {
        'server': cmd_server,
        'verify': cmd_verify,
        'list': cmd_list,
        'backup': cmd_backup,
        'fetch-photos': cmd_fetch_photos
    }

    if args.command in commands:
        commands[args.command](args)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
