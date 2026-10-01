# 🏛️ LaptopHUB & VOLTS — Project Architecture & Structure Map

> **Purpose**: This document provides a complete, structured directory map and architectural guide for the entire laptop store workspace. Everything is cataloged so you never have to search for files, features, data structures, or endpoints again.

---

## 📂 1. Directory Tree & File Inventory

```
c:/Users/Arslan/.antigravity-ide/laptop-store/
│
├── 🌐 STOREFRONT PAGES (HTML)
│   ├── index.html                  # Master Suite Portal & Tab Switcher (Iframe hub)
│   ├── laptophub.html              # Flagship LaptopHUB Storefront (69 models, filtering, cart, login)
│   ├── volts.html                  # Cyber-Minimalist VOLTS Performance Edition (69 models)
│   ├── custom-laptop.html          # "Create Your Laptop" Interactive Customizer & Quoting Studio
│   ├── consult.html                # Consult AI Interactive Quiz & Recommendation Engine
│   └── inventory.html              # Admin Dashboard (Add/Edit/Delete laptops & web photo search)
│
├── 📊 DATA & SHARED CONFIGURATION
│   ├── laptops-data.js             # Source of truth: JSON array with 69 verified laptops
│   ├── store-config.js             # Single source of truth for WhatsApp, phone, delivery & routes
│   └── Laptops on TIKTOK.txt       # Raw source TikTok inventory reference sheet
│
├── ⚡ MASTER CLI & AUTOMATION
│   ├── run.py                      # Master command center: server, verify, list, backup, fetch-photos
│   ├── manage_inventory.py         # Local HTTP & REST API server (port 8080) for live updates
│   └── build_inventory.py          # Python inventory builder & normalizer
│
├── 🛠️ SCRIPTS DIRECTORY (laptop-store/scripts/)
│   ├── verify_store.py             # Automated health & integrity checker for all pages & data
│   ├── retrieve_laptop_photos.py   # High-resolution internet image retrieval engine
│   ├── generate_svgs.py            # SVG fallback badge/laptop visual generator
│   └── build_inventory.py          # Standalone inventory generator
│
├── 🖼️ ASSETS & MEDIA
│   └── images/                     # 69 verified laptop photos + SVG visual fallbacks
│       ├── laptop-1-*.jpg          # Lenovo T14 Gen 1 photo
│       ├── laptop-2-*.jpg          # Surface Tab photo
│       └── ... (All 69 models)
│
└── 📁 REFERENCE DESIGNS & BACKUPS
    ├── desktop_copies/             # Standalone 3D and standalone reference designs
    └── backups/                    # Auto-generated timestamped backups of inventory
```

---

## 📱 2. Core Contact & WhatsApp Configuration

All customer communication is unified to:
* **WhatsApp Number**: `+923261398594` (`https://wa.me/923261398594`)
* **Phone Call Line**: `+92 326 1398594` (`tel:+923261398594`)
* **Support Email**: `support@laptophub.pk`
* **Single Configuration File**: [`store-config.js`](file:///c:/Users/Arslan/.antigravity-ide/laptop-store/store-config.js)

Whenever the contact number needs updating, change it in `store-config.js` to propagate across all modules.

---

## 🛒 3. E-Commerce State Management & LocalStorage

The storefront operates entirely client-side with full persistence via `localStorage`:

| Key | Purpose | Used In |
| :--- | :--- | :--- |
| `lh_cart_items` | Shopping cart items `[{id, name, price, cpu, ram, img, qty}]` | `laptophub.html`, `volts.html`, `store-config.js` |
| `lh_user` | Logged-in customer session `[{name, email, phone, loggedIn}]` | `laptophub.html`, `custom-laptop.html` |
| `lh_orders` | Local Cash on Delivery order history `[{id, date, items, ...}]` | `laptophub.html` |
| `lh_custom_requests` | Custom laptop quotation tickets `[{id, brand, cpu, ...}]` | `custom-laptop.html` |
| `laptophub_theme` | Theme preference (`dark` or `light`) | All storefront pages |

---

## 🛠️ 4. Feature Index: Where to Find Everything

### A. Shopping Cart & Drawer
* **LaptopHUB**: Search `#cartDrawer`, `#cartOverlay`, and `updateCartUI()` in `laptophub.html`.
* **VOLTS**: Search `#cartDrawer`, `openCartDrawer()`, and `addToCartById()` in `volts.html`.
* **Checkout Flow**: Handled by `#checkoutModal` (Cash on Delivery) and `checkoutWhatsApp()` (direct WhatsApp invoice).

### B. Customer Login & Registration
* **Modal Markup**: `#loginModal` in `laptophub.html`.
* **Session Manager**: `initUserSession()`, `quickGuestLogin()`, `signOutUser()`.
* **Dropdown**: `#userAccountSection` in the top navbar.

### C. "Create Your Laptop" Custom Configurator
* **File**: [`custom-laptop.html`](file:///c:/Users/Arslan/.antigravity-ide/laptop-store/custom-laptop.html).
* **Specs Customizer**:
  1. Brand & Form Factor (Lenovo, Dell, HP, Apple, Surface, Asus, Custom).
  2. Processor / CPU (Core i5, i7, i9, Core Ultra, Ryzen 5, 7, 9, M-series, or custom text).
  3. Graphics / GPU (Iris Xe/Radeon, RTX 3050-4070, Workstation Quadro, Apple Neural).
  4. RAM / Memory (8GB to 128GB DDR5).
  5. Storage / NVMe SSD (256GB to 4TB).
  6. Display (FHD IPS, 144Hz Gaming, 2.5K/2.8K OLED 120Hz, 4K UHD Touch).
  7. Workloads & Use Cases (Multi-select chips).
  8. Budget (Interactive slider in PKR from Rs 50k to Rs 650k+).
  9. Special Features (Backlit, Thunderbolt 4, Fingerprint, Ultralight).
  10. Client Contact Information (Name, WhatsApp, City).
* **Dynamic Features**:
  * Live Pakistani market estimate (`updateSummaryUI()`).
  * Live In-Stock matching against `LAPTOPS_INVENTORY` (`findStockMatches()`).
  * WhatsApp quotation dispatcher (`submitToWhatsApp()`).
  * Custom order ticket submission (`submitCustomTicket()`).

### D. Inventory Management & Photo Retrieval
* **Web UI**: [`inventory.html`](file:///c:/Users/Arslan/.antigravity-ide/laptop-store/inventory.html)
* **REST API**: [`manage_inventory.py`](file:///c:/Users/Arslan/.antigravity-ide/laptop-store/manage_inventory.py)
  * `GET /api/laptops`: Fetch all laptops.
  * `POST /api/laptops`: Add new laptop.
  * `PUT /api/laptops/<id>`: Update laptop.
  * `DELETE /api/laptops/<id>`: Delete laptop.
  * `POST /api/fetch-photo`: Retrieve image URL from internet search.
* **CLI Engine**: `python run.py fetch-photos` or `python run.py list`.

---

## 🚀 5. Command Reference (`run.py`)

Run all store management commands from `c:/Users/Arslan/.antigravity-ide/laptop-store/`:

| Command | Action |
| :--- | :--- |
| `python run.py server` | Start the local server & REST API on port `8080` |
| `python run.py verify` | Run comprehensive health check on HTML files, dataset, and WhatsApp numbers |
| `python run.py list` | Print a clean, formatted inventory table of all 69 models |
| `python run.py backup` | Save a timestamped copy of `laptops-data.js` to `backups/` |
| `python run.py fetch-photos` | Search and download real product photos from the web |

---

## 🔒 6. Safe Modification Rules

1. **Do Not Mutate Inventory Schema**: All items must contain `id`, `name`, `brand`, `cpu`, `ram`, `storage`, `gpu`, `price`, `priceFormatted`, `badge`, and `img`.
2. **Contact Centralization**: Use `STORE_CONFIG.contact.whatsapp` (`923261398594`) whenever adding new WhatsApp triggers.
3. **Responsive Aesthetics**: Preserve dark/light mode toggles (`laptophub_theme`) and typography (`Plus Jakarta Sans`, `Syne`, `JetBrains Mono`).
