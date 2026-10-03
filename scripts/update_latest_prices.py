"""
Update all 69 laptops with the latest Pakistani market prices from Paklap, Mega.pk, and Hafeez Centre benchmarks.
"""
import os
import sys
import json
import sqlite3

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from server import load_inventory, save_inventory

# Map of ID to updated latest market price (in PKR)
LATEST_PRICES = {
    1: 92000,    # Lenovo ThinkPad T14 Gen 1 (i7-10610U 10th Gen, 16GB, 512GB)
    2: 84000,    # Microsoft Surface Pro 7 (i5-1035G4, 8GB, 256GB)
    3: 158000,   # HP EliteBook 840 G9 (i7-1255U 12th Gen 10-Core, 16GB, 512GB)
    4: 175000,   # Lenovo ThinkPad X1 Yoga Gen 7 (i5-1240P 12th Gen, 16GB, 512GB)
    5: 78000,    # Lenovo ThinkPad X13 Gen 1 (i5-10210U, 16GB, 256GB)
    6: 98000,    # Lenovo ThinkPad T14 Gen 1 (AMD Ryzen 7 PRO 4750U, 16GB, 512GB)
    7: 38000,    # Lenovo ThinkPad 13 Gen 1 (i5-6200U, 8GB, 256GB)
    8: 82000,    # Dell XPS 15 9550 (i7-6700HQ, 16GB, 512GB, GTX 960M)
    9: 72000,    # Dell Latitude 5310 (i5-10210U, 16GB, 256GB)
    10: 128000,  # HP EliteBook x360 1030 G8 (i7-1165G7, 16GB, 512GB)
    11: 88000,   # Dell Latitude 5320 (i5-1145G7 vPro, 16GB, 512GB)
    12: 52000,   # HP EliteBook x360 1030 G2 (i5-7200U, 8GB, 256GB)
    13: 128000,  # Dell Latitude 5430 (i5-1235U 12th Gen, 16GB, 512GB)
    14: 98000,   # Dell Latitude 7420 (i5-1145G7 vPro, 16GB, 512GB)
    15: 32000,   # HP ProBook 640 G1 (i5-4200M, 8GB, 256GB)
    16: 82000,   # HP ProBook 630 G9 (i3-1215U 12th Gen, 8GB, 256GB)
    17: 58000,   # Lenovo ThinkPad T480s (i5-8350U vPro, 16GB, 256GB)
    18: 34000,   # HP EliteBook Folio 9480m (i5-4310U, 8GB, 256GB)
    19: 35000,   # HP ProBook 640 G2 (i3-6100U, 8GB, 256GB)
    20: 98000,   # Microsoft Surface Laptop 3 (i5-1035G7, 8GB, 256GB)
    21: 152000,  # Lenovo ThinkPad X1 Extreme Gen 2 (i7-9750H, 16GB, 512GB, GTX 1650)
    22: 108000,  # Dell Latitude 7320 2-in-1 (i5-1145G7 vPro, 16GB, 512GB)
    23: 92000,   # HP EliteBook 840 G8 (i5-1135G7, 16GB, 512GB)
    24: 82000,   # HP EliteBook 840 G7 (i5-10310U, 16GB, 512GB)
    25: 265000,  # Dell Precision 5560 (i9-11950H, 32GB, 1TB, RTX A2000)
    26: 105000,  # Dell XPS 15 9575 2-in-1 (i7-8705G, 16GB, 512GB, Radeon RX Vega M)
    27: 76000,   # HP EliteBook x360 1030 G4 (i5-8365U, 16GB, 512GB)
    28: 228000,  # Lenovo ThinkPad X13 Gen 4 (i7-1355U 13th Gen, 16GB, 512GB)
    29: 72000,   # Dell Vostro 5490 (i5-10210U, 8GB, 256GB)
    30: 58000,   # Dell Latitude 7490 (i7-8650U vPro, 16GB, 512GB)
    31: 56000,   # Dell Latitude 3310 2-in-1 (i5-10210U, 8GB, 256GB)
    32: 38000,   # Dell Latitude E7270 (i5-6300U, 8GB, 256GB)
    33: 88000,   # Dell Latitude 5320 (i5-1145G7 vPro, 16GB, 512GB)
    34: 55000,   # Lenovo ThinkPad E14 Gen 1 (i3-10110U, 8GB, 256GB)
    35: 68000,   # HP EliteBook x360 1030 G3 (i5-8350U, 16GB, 512GB)
    36: 315000,  # Dell Alienware m15 R7 (Ryzen 7 6800H, 16GB, 1TB, RTX 3070 Ti)
    37: 52000,   # HP 15-da Series (i5-8250U, 8GB, 256GB)
    38: 48000,   # HP Pavilion 15 (i5-7200U, 8GB, 256GB)
    39: 125000,  # Lenovo Yoga 6 13 (Ryzen 5 7530U, 16GB, 512GB)
    40: 76000,   # HP ProBook 640 G7 (i5-10210U, 16GB, 512GB)
    41: 182000,  # Lenovo Yoga 7i Gen 7 (i7-1260P 12th Gen, 16GB, 1TB)
    42: 62000,   # HP EliteBook 1040 G5 (i7-7600U, 16GB, 512GB)
    43: 72000,   # Dell Latitude 5310 (i5-10310U vPro, 16GB, 256GB)
    44: 68000,   # HP ProBook 430 G8 (i3-1115G4, 8GB, 256GB)
    45: 115000,  # Dell Latitude 7320 (i7-1185G7 vPro, 16GB, 512GB)
    46: 108000,  # HP EliteBook 845 G7 (Ryzen 7 PRO 4750U 8-Core, 16GB, 512GB)
    47: 295000,  # Apple MacBook Pro 14" 2021 (M1 Pro 8-Core/14-Core GPU, 16GB, 512GB)
    48: 42000,   # HP EliteBook Folio 1020 G1 (Core M-5Y71, 8GB, 256GB)
    49: 162000,  # HP EliteBook 630 G10 (i5-1335U 13th Gen, 16GB, 512GB)
    50: 745000,  # Apple MacBook Pro 14" (M4 Max 14-Core CPU/32-Core GPU, 36GB, 1TB)
    51: 78000,   # HP Envy x360 13 (i7-8550U, 16GB, 512GB)
    52: 92000,   # HP Spectre x360 13 (i7-8565U, 16GB, 512GB, 4K)
    53: 76000,   # Microsoft Surface Laptop Go (i5-1035G1, 8GB, 256GB)
    54: 118000,  # Lenovo Yoga Slim 7 14 (i7-1065G7, 16GB, 512GB)
    55: 365000,  # HP Spectre x360 14 2024 (Intel Core Ultra 7 155H, 16GB, 1TB)
    56: 135000,  # Dell XPS 13 9310 (i5-1135G7, 16GB, 512GB)
    57: 86000,   # Lenovo ThinkPad L13 Gen 2 (i5-1135G7, 16GB, 512GB)
    58: 105000,  # Microsoft Surface Laptop 3 13.5" (i5-1035G7, 8GB, 256GB)
    59: 89000,   # HP EliteBook 845 G7 (Ryzen 5 PRO 4650U 6-Core, 16GB, 512GB)
    60: 162000,  # HP ProBook 640 G10 (i5-1335U 13th Gen, 16GB, 512GB)
    61: 68000,   # Dell Latitude 5320 (i3-1125G4, 8GB, 256GB)
    62: 135000,  # Microsoft Surface Laptop 4 13.5" (i5-1135G7, 16GB, 512GB)
    63: 158000,  # Microsoft Surface Laptop 4 15" (i7-1185G7, 16GB, 512GB)
    64: 182000,  # Dell XPS 15 9500 (i7-10750H, 16GB, 512GB, GTX 1650 Ti)
    65: 72000,   # Lenovo ThinkPad T490s (i5-8365U vPro, 16GB, 512GB)
    66: 268000,  # Apple MacBook Air 13" M2 (M2 8-Core, 16GB, 512GB)
    67: 142000,  # Dell Latitude 7430 (i7-1265U 12th Gen, 16GB, 512GB)
    68: 198000,  # HP EliteBook 630 G11 (Intel Core Ultra 5 125U AI NPU, 16GB, 512GB)
    69: 255000,  # Dell XPS 13 Plus 9320 (i7-1280P 14-Core, 16GB, 512GB)
}

def update_inventory_prices():
    laptops = load_inventory()
    updated_count = 0
    for lap in laptops:
        lid = lap['id']
        if lid in LATEST_PRICES:
            new_price = LATEST_PRICES[lid]
            old_price = lap.get('price', 0)
            if new_price != old_price:
                lap['price'] = new_price
                lap['priceFormatted'] = f"Rs {new_price:,}"
                lap['priceUsd'] = round(new_price / 278)
                updated_count += 1
                print(f"[{lid}] {lap['name']}: PKR {old_price:,} -> PKR {new_price:,}")
    
    save_inventory(laptops)
    print(f"\n[SUCCESS] Updated {updated_count} laptops in laptops-data.js")

if __name__ == '__main__':
    update_inventory_prices()
