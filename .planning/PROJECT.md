# PROJECT.md — LaptopHUB Project Context (GSD)

See canonical specification in [.gsd/SPEC.md](file:///c:/Users/Arslan/.antigravity-ide/laptop-store/.gsd/SPEC.md).

## Key Architecture
- **Catalog**: 69 models defined in `laptops-data.js`.
- **Config & Pricing**: `store-config.js` (RAM tier tables & delta math).
- **Header**: `css/header.css` (3-column grid `1fr auto 1fr`, 40px buttons, 8px gap).
- **Backend**: `server.py` on port 8080 with SQLite `db/laptophub.db`.
- **Admin**: `admin/index.html` (authenticated via `admin/login.html`).
