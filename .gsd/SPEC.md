---
status: FINALIZED
created: 2026-10-01T10:00:00Z
finalized: 2026-10-01T15:00:00Z
project: LaptopHUB
version: 2.1.0
---

# SPEC.md — LaptopHUB Platform Specification

## Vision
LaptopHUB is Pakistan's premier specialized e-commerce platform for verified business and creator laptops (Dell Latitude/XPS, HP EliteBook/ProBook, Apple MacBook, Lenovo ThinkPad, Microsoft Surface). It pairs a high-performance storefront with an interactive consultation quiz, COD checkout, dynamic RAM/Storage upgrade pricing, and a full administrative suite.

---

## Architecture & Technology Stack
- **Frontend Core**: Vanilla JavaScript (ES6+), Semantic HTML5, CSS Custom Properties (`Plus Jakarta Sans`, `Syne`, `JetBrains Mono`).
- **Styling Architecture**: Modular CSS components:
  - `css/theme.css`: Core design system tokens (dark/light themes, elevation, surface colors).
  - `css/header.css`: 3-column balanced grid (`1fr auto 1fr`), unified 40px action buttons, 8px spacing, customer name truncation, responsive collapse.
- **Data Layer**:
  - `laptops-data.js`: Primary inventory dataset of 69 verified laptops with complete multi-tier specifications.
  - `store-config.js`: Centralized business rules, WhatsApp routing, and cumulative RAM/SSD pricing tier matrix.
- **Backend & Database**:
  - `server.py`: Lightweight Python HTTP service providing static asset delivery and REST APIs.
  - `db/laptophub.db`: SQLite database for customer accounts, orders, reviews, admin audit logs, and rate-limiting attempts.
  - `db/ram_pricing.json`: Persistent tier table for dynamic RAM pricing.
- **Security**:
  - Password Hashing: Scrypt with per-user unique salt (`hash_password` / `verify_password`).
  - Session Management: Secure HttpOnly SameSite=Strict session cookies (`lh_sess` for users, `lh_admin_sess` for admins).
  - SQL Injection Prevention: Exclusively parameterized SQLite queries.
  - Rate Limiting: DB-backed sliding window for authentication endpoints.

---

## Core Features & System Contracts

### 1. Storefront & Catalog (`laptophub.html`)
- 69 authentic laptop models with high-res photos and cutouts.
- Real-time search by model, brand, processor family, RAM size, and SSD capacity.
- Brand filtering (Lenovo, Dell, HP, Apple, Microsoft, Gaming/RTX) and spec filters (Under Rs 100k, Rs 100k-200k, 200k+ Flagship, Touch/360°, Core i7/Ryzen 7).
- Persistent cart drawer with quantity management, subtotal calculations, and free nationwide delivery badge.

### 2. RAM & Storage Upgrade Engine
- **Cumulative Tier Formula**: Delta relative to factory base RAM:
  $$\Delta_{\text{RAM}} = \text{Tier}(\text{Target RAM}) - \text{Tier}(\text{Base RAM})$$
- **DDR4 Tiers**: 8GB: 0 | 16GB: +Rs 8,000 | 32GB: +Rs 23,000.
- **DDR5 Tiers**: 8GB: 0 | 16GB: +Rs 10,000 | 32GB: +Rs 28,000 (configurable via Admin).
- **Soldered RAM**: Laptops with soldered memory display a `Soldered (Fixed)` indicator with upgrade options disabled.
- **Storage Deltas**: 128GB: -Rs 9,000 | 256GB: -Rs 5,000 | 512GB: Included | 1TB: +Rs 12,000 (relative to 512GB baseline).
- **Funnel Consistency**: Modal, Cart drawer, WhatsApp order message, and COD checkout carry identical computed pricing.

### 3. Header & Navigation (`css/header.css`)
- 3-column balanced grid (`1fr auto 1fr`):
  - Left: Logo mark linking to `laptophub.html`.
  - Center: Nav links (`All Laptops`, `Consult Me`, `Reviews`) perfectly centered across the entire viewport.
  - Right: Unified 40px action buttons (`Theme Toggle`, `Cart`, `User Button`).
- Truncates long user names with ellipsis (`max-width: 95px`).
- Responsive collapse at 992px to mobile hamburger menu with zero overlap or wrapping.

### 4. Admin Suite (`/admin/` & `admin/login.html`)
- Dedicated, unlinked administrative login endpoint.
- Live RAM Upgrade Pricing Matrix editor for DDR4 and DDR5 tiers.
- Live Inventory Management (add, update, archive/unarchive, stock adjustment).
- Order Management with status workflows (New, Confirmed, Shipped, Delivered, Cancelled).
- Customer Review moderation and Audit Log tracking.
