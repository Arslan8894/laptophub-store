# Agent Instructions: Antigravity Laptop Store Project (`AGENTS.md`)

> **CRITICAL DIRECTIVE**: **Preserve everything already built.** Only make modifications that are explicitly requested by the user. Do not break, replace, refactor, or delete existing features or architecture.

---

## 1. Prime Directive: Preserve, Don't Break

* **Preserve Working Features**: All existing store functionality (inventory browsing, specs modals, filters, search, comparison tools, currency toggles, consultation wizard, animations, and responsive layouts) must remain intact and functional.
* **No Unsolicited Refactoring**: Do not reorganize files, rewrite working logic, modernize syntax unnecessarily, or replace custom implementations with generic boilerplates unless explicitly commanded.
* **No Placeholders**: Never replace working code, styles, or data with `// TODO`, placeholders, or truncated snippets. Always maintain full, production-ready code.

---

## 2. Core Operating Rules

### Rule 1: Inspect Before Changing
* Before editing any file, inspect the existing code, dependencies, and structure.
* Understand the data flow, DOM element IDs, CSS variables, and event listeners before proposing or executing changes.
* Verify how helper scripts (e.g., Python build and update scripts) and client-side JavaScript (`laptops-data.js`) interact with the HTML pages.

### Rule 2: Reuse Existing Components, Styles, and Data Patterns
* **Design & Styles**: Reuse existing CSS variables (e.g., `--bg`, `--surface`, `--accent`, `--border`), classes, and typography (`Plus Jakarta Sans`, `Syne`, `DM Sans`, `JetBrains Mono`). Maintain dark/light mode compatibility where present.
* **Components**: Reuse existing UI patterns (cards, badges, modals, drawers, floating action buttons, search bars).
* **Data Schema**: Adhere strictly to the data schema established in `laptops-data.js` (e.g., `id`, `name`, `brand`, `cpu`, `ram`, `storage`, `gpu`, `price`, `priceFormatted`, `badge`, `useCases`, `img`).

### Rule 3: No Deleting or Rewriting Without Permission
* **Explicit Consent Required**: Never delete existing pages, functions, inventory items, scripts, or styles without explicit instructions from the user.
* If a requested feature conflicts with an existing one, stop and clarify with the user before overwriting or removing functionality.

### Rule 4: Minimal, Surgical Changes
* Make the smallest, most targeted change required to achieve the user's objective.
* Do not touch unrelated functions, styles, or markup.
* Keep git diffs focused and clean.

### Rule 5: Keep the Store Responsive and Production-Ready
* Ensure all pages remain fully responsive across mobile, tablet, and desktop viewports.
* Preserve smooth animations, micro-interactions, transitions, and custom cursor/interactive elements.
* Ensure all interactive elements retain unique IDs and accessible semantic attributes.

### Rule 6: Test and Verify Affected Functionality
* After making any change:
  - Check for syntax errors, broken paths, and missing references.
  - If a script was executed (e.g., Python inventory/image updater), verify that output files (`laptops-data.js`, HTML files) are intact and valid.
  - Ensure the browser can render the modified page without JavaScript runtime errors or styling regressions.

### Rule 7: Ask Before Major Architectural or UI Changes
* Do not introduce new heavy libraries, external frameworks (e.g., React, Vue, Tailwind CSS), or alter page architecture without explicit user approval.
* Consult with the user before redesigning UI layouts, altering color schemes, or restructuring navigation.

### Rule 8: Preserve Existing Data and Configurations
* Protect inventory datasets (`laptops-data.js`, `Laptops on TIKTOK.txt`), image assets (`images/`), and reference copies in `desktop_copies/`.
* Do not overwrite or regenerate assets unless explicitly requested.

---

## 3. Project Structure Reference

| Path / File | Purpose & Rule |
| :--- | :--- |
| `laptop-store/laptops-data.js` | Source of truth for all laptop inventory data (69 models). Preserve schema, format, and existing entries. |
| `laptop-store/store-config.js` | Central configuration for owner WhatsApp (+923261398594), phone, routes, and state helpers. |
| `laptop-store/STRUCTURE.md` | Master architectural guide and directory index for finding all components and scripts. |
| `laptop-store/laptophub.html` | Flagship LaptopHub storefront with filtering, search, cart drawer, COD checkout, and customer login. |
| `laptop-store/volts.html` | VOLTS cybernetic boutique store interface with synchronized cart and WhatsApp orders. |
| `laptop-store/custom-laptop.html` | "Create Your Laptop" configurator with live Pakistani market pricing and inventory match finder. |
| `laptop-store/consult.html` | Interactive consultation and recommendation flow. Preserve quiz logic and matching algorithms. |
| `laptop-store/inventory.html` | Full Admin Dashboard for adding/editing/deleting laptops and fetching internet photos. |
| `laptop-store/index.html` | Storefront showcase and architecture review portal (tab switcher). |
| `laptop-store/run.py` | Unified CLI controller: server, verify, list, backup, fetch-photos. |
| `laptop-store/scripts/` | Automated verification (`verify_store.py`) and photo retrieval tools. |
| `laptop-store/images/` | Product visuals (69 high-res photos) and SVGs. Preserve existing paths. |
| `laptop-store/desktop_copies/` | Reference/standalone designs. Do not delete or mutate without permission. |

---

## 4. Agent Execution Checklist

Before completing any task in this repository, verify:
- [ ] Did I review the existing code before modifying it?
- [ ] Are all pre-existing features, filters, modals, and scripts still working?
- [ ] Were modifications strictly scoped to the user's explicit request?
- [ ] Did I reuse existing CSS variables, classes, and UI components?
- [ ] Is the page layout responsive and free of runtime console errors?
- [ ] Are all data files and asset references intact?
