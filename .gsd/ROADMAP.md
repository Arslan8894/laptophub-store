# ROADMAP.md — LaptopHUB Project Roadmap

## Milestone 1: Platform Foundation & Core Catalog (Completed)
- [x] Phase 1.1: 69-model verified inventory dataset (`laptops-data.js`).
- [x] Phase 1.2: Flagship storefront UI (`laptophub.html`) with brand & spec filters.
- [x] Phase 1.3: High-res photography processing and image blending.
- [x] Phase 1.4: Interactive consultation quiz (`consult.html`, `consult-matcher.js`).

## Milestone 2: Backend Architecture & Auth Security (Completed)
- [x] Phase 2.1: SQLite database schema and initialization (`db/laptophub.db`, `db/schema.sql`).
- [x] Phase 2.2: Scrypt password hashing, session tokens, and sliding-window rate limiting.
- [x] Phase 2.3: Cash on Delivery (COD) checkout modal and customer order tracking.
- [x] Phase 2.4: Dedicated admin authentication and control center (`/admin/`, `admin/login.html`).

## Milestone 3: Modular Pricing Engine & UI Refinements (Current)
- [x] Phase 3.1: Cumulative RAM tier table matrix for DDR4 (`store-config.js`, `db/ram_pricing.json`).
- [x] Phase 3.2: Relative RAM delta calculations in modal, cart, COD, and WhatsApp orders.
- [x] Phase 3.3: Soldered memory detection and graceful UI fallback.
- [x] Phase 3.4: Admin RAM Pricing Tier Editor with real-time math previews.
- [x] Phase 3.5: Modular header stylesheet (`css/header.css`) with 3-column grid (`1fr auto 1fr`), 40px action buttons, and responsive collapse.
- [x] Phase 3.6: Removal of legacy Volts / custom laptop switcher in favor of seamless storefront navigation.

## Milestone 4: Tooling & Extension Integrations (Active)
- [x] Phase 4.1: CodeRabbit static analysis & PR review rules (`.coderabbit.yaml`).
- [x] Phase 4.2: Roo Code custom modes and project rules (`.roomodes`, `.clinerules`, `.roorules`).
- [x] Phase 4.3: GSD methodology integration (`.gsd/SPEC.md`, `.gsd/ROADMAP.md`, `.gsd/STATE.md`, `.gsd/DECISIONS.md`).
- [x] Phase 4.4: Ralph Loop autonomous runner integration (`.ralph/PRD.md`, `.ralph/PROMPT.md`, `.ralph/ralph.ps1`).
