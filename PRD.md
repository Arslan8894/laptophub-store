# Product Requirements Document (PRD) — LaptopHUB

## Project Status: ACTIVE
- **Storefront**: `laptophub.html`
- **Backend**: `server.py` (Port 8080)
- **Database**: `db/laptophub.db`
- **Test Command**: `python scripts/test_fixes.py`

---

## Completed Tasks [VERIFIED]
- [x] **TASK-001**: 69 verified laptop models with photography and specs schema (`laptops-data.js`).
- [x] **TASK-002**: Customer authentication with scrypt hashing, rate limiting, and HttpOnly session cookies.
- [x] **TASK-003**: COD Checkout Modal with address collection and persistent SQLite order record.
- [x] **TASK-004**: Administrative Dashboard at `/admin/` with unlinked `/admin/login.html` authentication.
- [x] **TASK-005**: RAM upgrade cumulative pricing matrix for DDR4 (`8GB: 0`, `16GB: 8000`, `32GB: 23000`).
- [x] **TASK-006**: Relative RAM delta calculation for Upgradable laptops with Soldered RAM fixed badge fallback.
- [x] **TASK-007**: Admin panel RAM Pricing Tier Editor with live delta math previews and JSON persistence.
- [x] **TASK-008**: Modular header CSS (`css/header.css`) with 3-column grid (`1fr auto 1fr`), 40px action buttons, and responsive collapse.
- [x] **TASK-009**: Clean redirect of legacy Volts and custom configurator links to `laptophub.html`.
- [x] **TASK-010**: Automated test suite `scripts/test_fixes.py` verifying header CSS, API contracts, admin login, and RAM math.

---

## Active & Upcoming Backlog Tasks

- [ ] **TASK-011**: **DDR5 Pricing Tier Matrix Refinement**
  - **Scope**: When the user provides the final DDR5 tier formula, update `STORE_CONFIG.ramPricingTiers.DDR5` and `db/ram_pricing.json`.
  - **Models affected**: ID 3 (HP EliteBook 840 G9), ID 36 (Dell Alienware m15 R7), ID 68 (HP EliteBook 630 G11).
  - **Verification**: Run `python scripts/test_fixes.py`.

- [ ] **TASK-012**: **Automated Daily Database Backups**
  - **Scope**: Add scheduled or CLI backup command to `server.py` / `run.py` to snapshot `db/laptophub.db` into `db/backups/`.
  - **Verification**: Run backup command and assert non-empty `.sqlite` file is created.

- [ ] **TASK-013**: **Email & SMS Order Notifications for COD**
  - **Scope**: Integrate SMTP / WhatsApp Webhook notification dispatch on new order placement.
  - **Verification**: Dispatch test order and check log event.

- [ ] **TASK-014**: **Customer Order History View**
  - **Scope**: Add "My Orders" modal/section in `laptophub.html` displaying the logged-in customer's orders fetched from `GET /api/orders/mine`.
  - **Verification**: Place order, open customer dropdown, view order card with status.
