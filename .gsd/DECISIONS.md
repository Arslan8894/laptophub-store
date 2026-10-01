# DECISIONS.md — Architectural Decision Records (ADR)

## ADR-001: Vanilla Stack Over Heavy Frameworks
- **Decision**: Retain Vanilla JavaScript, semantic HTML5, and CSS Custom Properties instead of migrating to React, Vue, or Tailwind.
- **Rationale**: Instant sub-second page loads without bundling overhead, zero build dependencies for frontend assets, and maximum longevity.

## ADR-002: Cumulative RAM Pricing Tier Matrix
- **Decision**: Store RAM upgrade pricing once as cumulative costs (`8GB: 0`, `16GB: 8000`, `32GB: 23000`) rather than hardcoding per-laptop deltas.
- **Rationale**: Any target RAM difference relative to any base RAM is derived with a single formula: $\text{Delta} = \text{Tier}(\text{Target}) - \text{Tier}(\text{Base})$. Upgrades, downgrades, and admin updates stay consistent across the entire funnel.

## ADR-003: Modular Header Component (`css/header.css`)
- **Decision**: Isolate navigation, actions, and header responsive rules into `css/header.css`.
- **Rationale**: Prevents cascade conflicts with catalog and modal styles. Guarantees true 3-column centering (`1fr auto 1fr`) regardless of logo width or action button text length.

## ADR-004: Server-Side Authentication & Session Cookies
- **Decision**: Use scrypt hashing with per-user salt and HttpOnly SameSite=Strict cookies (`lh_sess` and `lh_admin_sess`).
- **Rationale**: Protects against XSS session theft, ensures separation of customer and administrative privileges, and prevents role spoofing in localStorage.
