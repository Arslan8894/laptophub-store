import re

file_path = r"c:\Users\Arslan\.antigravity-ide\laptop-store\laptophub.html"
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add script tag in head if not present
if '<script src="laptops-data.js"></script>' not in content:
    content = content.replace('</head>', '<script src="laptops-data.js"></script>\n</head>')

# 2. Add Cart Drawer CSS before </style>
cart_drawer_css = '''
  /* CART DRAWER & OVERLAY */
  #cartOverlay {
    position: fixed; inset: 0;
    background: rgba(0,0,0,0.6);
    backdrop-filter: blur(8px);
    z-index: 10000;
    opacity: 0; pointer-events: none;
    transition: opacity 0.3s ease;
  }
  #cartOverlay.open {
    opacity: 1; pointer-events: auto;
  }
  #cartDrawer {
    position: fixed; top: 0; right: 0; bottom: 0;
    width: min(460px, 100vw);
    background: var(--s1);
    border-left: 1px solid var(--border2);
    box-shadow: -10px 0 45px rgba(0,0,0,0.4);
    z-index: 10001;
    display: flex; flex-direction: column;
    transform: translateX(100%);
    transition: transform 0.35s cubic-bezier(0.16, 1, 0.3, 1);
  }
  #cartDrawer.open {
    transform: translateX(0);
  }
  .drawer-head {
    padding: 1.3rem 1.6rem;
    border-bottom: 1px solid var(--border);
    display: flex; align-items: center; justify-content: space-between;
    background: var(--s2);
  }
  .drawer-title {
    font-size: 1.15rem; font-weight: 800; color: var(--heading);
    display: flex; align-items: center; gap: 8px;
    font-family: 'Playfair Display', serif;
  }
  .drawer-close {
    background: none; border: 1px solid var(--border2);
    color: var(--muted); width: 34px; height: 34px;
    border-radius: 50%; font-size: 1.1rem;
    display: flex; align-items: center; justify-content: center;
    cursor: pointer; transition: all 0.2s;
  }
  .drawer-close:hover { color: var(--heading); border-color: var(--blue); }
  
  .drawer-items {
    flex-grow: 1; overflow-y: auto; padding: 1.2rem 1.6rem;
    display: flex; flex-direction: column; gap: 1rem;
  }
  .drawer-empty {
    text-align: center; padding: 3rem 1rem; color: var(--muted);
  }
  .drawer-empty-icon { font-size: 3rem; margin-bottom: 0.8rem; }
  
  .cart-item {
    display: flex; gap: 12px; background: var(--s2);
    border: 1px solid var(--border); border-radius: 10px;
    padding: 12px; align-items: center;
    transition: border-color 0.2s;
  }
  .cart-item:hover { border-color: var(--border2); }
  .cart-item-img {
    width: 65px; height: 55px; object-fit: contain;
    background: var(--photo-bg); border-radius: 6px; padding: 4px;
    flex-shrink: 0;
  }
  .cart-item-info { flex-grow: 1; min-width: 0; }
  .cart-item-name {
    font-size: 0.86rem; font-weight: 700; color: var(--heading);
    white-space: nowrap; overflow: hidden; text-overflow: ellipsis;
  }
  .cart-item-specs { font-size: 0.72rem; color: var(--muted); margin: 2px 0 5px; }
  .cart-item-price { font-size: 0.88rem; font-weight: 800; color: var(--blue); }
  
  .cart-item-qty {
    display: flex; align-items: center; gap: 6px;
    background: var(--s1); border: 1px solid var(--border2);
    border-radius: 6px; padding: 2px 6px;
  }
  .qty-btn {
    background: none; border: none; color: var(--heading);
    font-size: 0.9rem; font-weight: 800; cursor: pointer;
    padding: 0 4px; line-height: 1;
  }
  .qty-num { font-size: 0.8rem; font-weight: 700; min-width: 14px; text-align: center; }
  .cart-item-del {
    background: none; border: none; color: #ef4444;
    cursor: pointer; font-size: 0.95rem; padding: 4px;
    opacity: 0.7; transition: opacity 0.2s;
  }
  .cart-item-del:hover { opacity: 1; }

  .drawer-footer {
    border-top: 1px solid var(--border); padding: 1.4rem 1.6rem;
    background: var(--s2);
  }
  .subtotal-row {
    display: flex; justify-content: space-between; align-items: center;
    margin-bottom: 0.6rem;
  }
  .subtotal-label { font-size: 0.85rem; color: var(--muted); font-weight: 600; }
  .subtotal-val { font-size: 1.4rem; font-weight: 800; color: var(--heading); font-family: 'Playfair Display', serif; }
  .shipping-badge {
    background: rgba(16,185,129,0.12); color: var(--green);
    border: 1px solid rgba(16,185,129,0.25); border-radius: 6px;
    padding: 4px 10px; font-size: 0.74rem; font-weight: 700;
    display: flex; align-items: center; gap: 6px; margin-bottom: 1rem;
  }

  .drawer-btn-wa {
    width: 100%; background: #25d366; color: #fff;
    border: none; padding: 0.85rem; border-radius: 8px;
    font-family: inherit; font-size: 0.9rem; font-weight: 700;
    cursor: pointer; display: flex; align-items: center; justify-content: center;
    gap: 8px; box-shadow: 0 4px 16px rgba(37,211,102,0.3);
    text-decoration: none; margin-bottom: 0.6rem;
    transition: transform 0.2s, box-shadow 0.2s;
  }
  .drawer-btn-wa:hover { transform: translateY(-1px); box-shadow: 0 6px 22px rgba(37,211,102,0.45); }
  
  .drawer-btn-checkout {
    width: 100%; background: var(--blue); color: #fff;
    border: none; padding: 0.85rem; border-radius: 8px;
    font-family: inherit; font-size: 0.9rem; font-weight: 700;
    cursor: pointer; display: flex; align-items: center; justify-content: center;
    gap: 8px; box-shadow: 0 4px 16px rgba(76,124,255,0.3);
    transition: transform 0.2s, background 0.2s;
  }
  .drawer-btn-checkout:hover { background: var(--blue-hover); transform: translateY(-1px); }

  /* CHECKOUT MODAL */
  #checkoutModal {
    position: fixed; inset: 0; background: rgba(0,0,0,0.7);
    backdrop-filter: blur(10px); z-index: 10002;
    display: none; align-items: center; justify-content: center;
    padding: 1.5rem;
  }
  #checkoutModal.open { display: flex; }
  .checkout-card {
    background: var(--s1); border: 1px solid var(--border2);
    border-radius: 16px; width: min(500px, 100%);
    box-shadow: 0 25px 60px rgba(0,0,0,0.6);
    overflow: hidden;
  }
  .checkout-header {
    background: var(--s2); padding: 1.2rem 1.6rem;
    display: flex; justify-content: space-between; align-items: center;
    border-bottom: 1px solid var(--border);
  }
  .checkout-form { padding: 1.6rem; display: flex; flex-direction: column; gap: 0.9rem; }
  .form-group { display: flex; flex-direction: column; gap: 4px; }
  .form-label { font-size: 0.78rem; font-weight: 700; color: var(--subtle); text-transform: uppercase; letter-spacing: 0.04em; }
  .form-input, .form-select {
    background: var(--input-bg); border: 1px solid var(--border2);
    color: var(--heading); padding: 0.65rem 0.9rem; border-radius: 7px;
    font-family: inherit; font-size: 0.88rem; outline: none;
    transition: border-color 0.2s;
  }
  .form-input:focus, .form-select:focus { border-color: var(--blue); }
  
  /* ORDER CONFIRMATION MODAL */
  #orderConfirmModal {
    position: fixed; inset: 0; background: rgba(0,0,0,0.75);
    backdrop-filter: blur(12px); z-index: 10003;
    display: none; align-items: center; justify-content: center;
    padding: 1.5rem;
  }
  #orderConfirmModal.open { display: flex; }
  .confirm-card {
    background: var(--s1); border: 1.5px solid var(--green);
    border-radius: 20px; width: min(480px, 100%);
    box-shadow: 0 25px 60px rgba(0,0,0,0.6); padding: 2.5rem 2rem;
    text-align: center;
  }
  .confirm-icon {
    width: 64px; height: 64px; border-radius: 50%;
    background: rgba(16,185,129,0.15); color: var(--green);
    display: flex; align-items: center; justify-content: center;
    font-size: 2rem; margin: 0 auto 1.2rem;
    box-shadow: 0 0 25px rgba(16,185,129,0.25);
  }

  /* TOOLBAR EXPANSIONS */
  .toolbar-row2 {
    max-width: 1400px; margin: -1.8rem auto 2.5rem; padding: 0 3rem;
    display: flex; justify-content: space-between; align-items: center;
    gap: 1rem; flex-wrap: wrap;
  }
  .filter-pills { display: flex; gap: 6px; flex-wrap: wrap; }
  .pill-filter {
    background: var(--s2); border: 1px solid var(--border);
    color: var(--muted); padding: 0.35rem 0.85rem; border-radius: 100px;
    font-size: 0.76rem; font-weight: 600; cursor: pointer;
    transition: all 0.2s;
  }
  .pill-filter:hover { color: var(--heading); border-color: var(--border2); }
  .pill-filter.active { background: var(--blue-dim); color: var(--blue); border-color: var(--blue); }
  
  .sort-select {
    background: var(--s1); border: 1px solid var(--border2);
    color: var(--heading); padding: 0.45rem 1rem; border-radius: 7px;
    font-family: inherit; font-size: 0.82rem; font-weight: 600;
    outline: none; cursor: pointer;
  }
  .count-indicator { font-size: 0.82rem; color: var(--muted); font-weight: 600; }
  .count-indicator strong { color: var(--heading); }

  /* CARD ACTION ROW */
  .card-action-row {
    display: flex; gap: 8px; align-items: center;
  }
  .btn-wa-card {
    background: rgba(37,211,102,0.12); color: #1ebe5d;
    border: 1px solid rgba(37,211,102,0.3); border-radius: 6px;
    padding: 0.65rem 0.85rem; font-size: 0.82rem; font-weight: 700;
    text-decoration: none; display: flex; align-items: center; justify-content: center;
    gap: 4px; transition: all 0.2s;
  }
  .btn-wa-card:hover { background: rgba(37,211,102,0.22); transform: translateY(-2px); }

  /* BADGE TYPES */
  .b-game { background: rgba(6,182,212,0.14); color: #06b6d4; border: 1px solid rgba(6,182,212,0.3); }
  .b-touch { background: rgba(236,72,153,0.14); color: #ec4899; border: 1px solid rgba(236,72,153,0.3); }
'''

if '#cartDrawer {' not in content:
    content = content.replace('</style>', cart_drawer_css + '\n</style>')

# 3. Replace Hero Count and Text
content = content.replace('Explore All 7 Models', 'Explore All 69 Laptops')
content = content.replace('7 Verified Models Ready', '69 In-Stock Models Ready')
content = content.replace('Dual Mode (Light & Dark) · 7 Laptop Models', '69 Models In-Stock · Lenovo, Dell, HP, Apple, Surface')

# 4. Replace Catalog Toolbar and Grid Section
new_toolbar_and_grid = '''<!-- CATALOG TOOLBAR -->
<div class="catalog-toolbar" id="inventory">
  <div class="filter-tabs">
    <button class="filter-btn active" onclick="filterBrand('all', this)">All Laptops (69)</button>
    <button class="filter-btn" onclick="filterBrand('lenovo', this)">Lenovo (15)</button>
    <button class="filter-btn" onclick="filterBrand('dell', this)">Dell (19)</button>
    <button class="filter-btn" onclick="filterBrand('hp', this)">HP (22)</button>
    <button class="filter-btn" onclick="filterBrand('apple', this)">Apple (3)</button>
    <button class="filter-btn" onclick="filterBrand('microsoft', this)">Microsoft (7)</button>
    <button class="filter-btn" onclick="filterBrand('gaming', this)">Gaming / RTX (4)</button>
  </div>
  <div class="search-box">
    <span class="search-icon">🔍</span>
    <input type="text" class="search-input" id="laptopSearch" placeholder="Search 69 models: T14, XPS, Alienware, i7..." oninput="handleSearch()">
  </div>
</div>

<!-- SUB-FILTER ROW (Price & Category Filters) -->
<div class="toolbar-row2">
  <div class="filter-pills">
    <button class="pill-filter active" onclick="filterPill('all', this)">All Specs</button>
    <button class="pill-filter" onclick="filterPill('under-100k', this)">Under Rs 100k</button>
    <button class="pill-filter" onclick="filterPill('100k-200k', this)">Rs 100k – 200k</button>
    <button class="pill-filter" onclick="filterPill('200k-plus', this)">Rs 200k+ Flagship</button>
    <button class="pill-filter" onclick="filterPill('touch', this)">Touch / 360°</button>
    <button class="pill-filter" onclick="filterPill('core-i7', this)">Core i7 / i9 / Ryzen 7</button>
  </div>

  <div style="display:flex; align-items:center; gap:12px;">
    <span class="count-indicator">Showing <strong id="visibleCount">69</strong> of <strong>69</strong> laptops</span>
    <select class="sort-select" id="sortSelect" onchange="handleSort(this.value)">
      <option value="default">Sort: Most Popular</option>
      <option value="price-asc">Price: Low to High</option>
      <option value="price-desc">Price: High to Low</option>
      <option value="name-asc">Model Name (A-Z)</option>
    </select>
  </div>
</div>

<!-- DYNAMIC LAPTOP PRODUCTS GRID -->
<section class="sec" style="padding-top:0">
  <div class="pgrid" id="productGrid">
    <!-- Rendered dynamically by JavaScript with all 69 models -->
  </div>
</section>'''

# Replace from CATALOG TOOLBAR to </section> before STATS
catalog_pattern = re.compile(r'<!-- CATALOG TOOLBAR -->.*?</section>', re.DOTALL)
content = catalog_pattern.sub(new_toolbar_and_grid, content, count=1)

# 5. Insert Cart Drawer & Modals HTML right before <footer>
cart_modals_html = '''
<!-- CART OVERLAY & SLIDE-OVER DRAWER -->
<div id="cartOverlay" onclick="closeCart()"></div>
<aside id="cartDrawer" aria-label="Shopping Cart">
  <div class="drawer-head">
    <div class="drawer-title">
      <span>🛍️ Your Cart</span>
      <span class="cart-badge-count" id="drawerCartBadge">0</span>
    </div>
    <button class="drawer-close" onclick="closeCart()" aria-label="Close cart">✕</button>
  </div>

  <div class="drawer-items" id="drawerItemsList">
    <!-- Rendered by renderCart() -->
  </div>

  <div class="drawer-footer">
    <div class="shipping-badge">
      <span>🚚</span> FREE Express Dispatch across Pakistan · Cash on Delivery
    </div>
    <div class="subtotal-row">
      <span class="subtotal-label">Subtotal:</span>
      <span class="subtotal-val" id="drawerSubtotal">Rs 0</span>
    </div>
    <button class="drawer-btn-wa" onclick="checkoutWhatsApp()">
      <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>
      Order / Confirm on WhatsApp
    </button>
    <button class="drawer-btn-checkout" onclick="openCheckoutModal()">
      <span>📦</span> Cash on Delivery Checkout
    </button>
  </div>
</aside>

<!-- QUICK CASH ON DELIVERY CHECKOUT MODAL -->
<div id="checkoutModal">
  <div class="checkout-card">
    <div class="checkout-header">
      <h3 style="font-size:1.1rem;font-weight:800;color:var(--heading)">📦 Cash on Delivery Order</h3>
      <button class="drawer-close" onclick="closeCheckoutModal()">✕</button>
    </div>
    <form class="checkout-form" onsubmit="handlePlaceOrder(event)">
      <div class="form-group">
        <label class="form-label">Full Name *</label>
        <input class="form-input" id="custName" type="text" placeholder="e.g. Muhammad Ali" required>
      </div>
      <div class="form-group">
        <label class="form-label">Phone / WhatsApp Number *</label>
        <input class="form-input" id="custPhone" type="tel" placeholder="e.g. 0300 1234567" required>
      </div>
      <div class="form-group">
        <label class="form-label">City *</label>
        <select class="form-select" id="custCity" required>
          <option value="">Select City</option>
          <option value="Lahore">Lahore (Same Day Dispatch)</option>
          <option value="Karachi">Karachi (24h Express)</option>
          <option value="Islamabad">Islamabad (24h Express)</option>
          <option value="Rawalpindi">Rawalpindi</option>
          <option value="Faisalabad">Faisalabad</option>
          <option value="Multan">Multan</option>
          <option value="Peshawar">Peshawar</option>
          <option value="Quetta">Quetta</option>
          <option value="Other">Other City</option>
        </select>
      </div>
      <div class="form-group">
        <label class="form-label">Delivery Address *</label>
        <input class="form-input" id="custAddress" type="text" placeholder="House / Office #, Street, Area" required>
      </div>
      <div style="background:var(--s2);padding:10px;border-radius:8px;font-size:0.8rem;color:var(--muted)">
        Order Total: <strong id="modalOrderTotal" style="color:var(--blue)">Rs 0</strong> · Payment on delivery via Cash
      </div>
      <button type="submit" class="drawer-btn-checkout" style="margin-top:4px">
        Confirm & Place COD Order
      </button>
    </form>
  </div>
</div>

<!-- ORDER CONFIRMATION MODAL -->
<div id="orderConfirmModal">
  <div class="confirm-card">
    <div class="confirm-icon">✓</div>
    <h2 style="font-family:'Playfair Display',serif;font-size:1.8rem;font-weight:800;color:var(--heading);margin-bottom:0.5rem">Order Confirmed!</h2>
    <p style="color:var(--muted);font-size:0.88rem;margin-bottom:1.5rem">Thank you for ordering with LaptopHUB. Our team is packing your laptop with warranty documentation and diagnostic report.</p>
    <div style="background:var(--s2);padding:1rem;border-radius:10px;margin-bottom:1.5rem;text-align:left;font-size:0.85rem">
      <div style="margin-bottom:6px"><strong>Order ID:</strong> <span id="confirmOrderId" style="color:var(--blue)">#LH-9842</span></div>
      <div style="margin-bottom:6px"><strong>Customer:</strong> <span id="confirmCustomer">Muhammad Ali</span></div>
      <div><strong>Payment:</strong> Cash on Delivery</div>
    </div>
    <button class="drawer-btn-checkout" onclick="closeConfirmModal()">Continue Shopping</button>
  </div>
</div>
'''

if '#cartDrawer' not in content:
    content = content.replace('<footer>', cart_modals_html + '\n<footer>')

# 6. Replace Nav Cart Click Handler
content = content.replace('onclick="openCartToast()"', 'onclick="openCart()"')

# 7. Write complete updated JavaScript logic into <script>
js_code = '''
<script>
  // COMPLETE 69 LAPTOP STORE LOGIC
  
  // State
  let currentBrand = 'all';
  let currentPill = 'all';
  let searchQuery = '';
  let currentSort = 'default';
  let cart = JSON.parse(localStorage.getItem('lh_cart_items') || '[]');

  // Check if LAPTOPS_INVENTORY loaded
  const inventory = (typeof LAPTOPS_INVENTORY !== 'undefined') ? LAPTOPS_INVENTORY : [];

  // Theme
  function initTheme() {
    const saved = localStorage.getItem('laptophub_theme') || 
      (window.matchMedia('(prefers-color-scheme: light)').matches ? 'light' : 'dark');
    applyTheme(saved);
  }

  function applyTheme(theme) {
    document.documentElement.setAttribute('data-theme', theme);
    localStorage.setItem('laptophub_theme', theme);
    const icon = document.getElementById('themeIcon');
    const label = document.getElementById('themeLabel');
    if (icon && label) {
      if (theme === 'light') {
        icon.textContent = '🌙'; label.textContent = 'Dark';
      } else {
        icon.textContent = '☀️'; label.textContent = 'Light';
      }
    }
  }

  function toggleTheme() {
    const cur = document.documentElement.getAttribute('data-theme') || 'dark';
    const next = cur === 'dark' ? 'light' : 'dark';
    applyTheme(next);
    showToast(`Switched to ${next.toUpperCase()} mode`);
  }

  initTheme();
  window.addEventListener('message', (e) => {
    if (e.data && e.data.type === 'SET_THEME' && e.data.theme) {
      applyTheme(e.data.theme);
    }
  });

  // Render Products Grid
  function renderProducts() {
    const grid = document.getElementById('productGrid');
    if (!grid) return;

    let filtered = inventory.filter(lap => {
      // Brand filter
      if (currentBrand === 'gaming') {
        if (lap.gpuType !== 'rtx' && lap.gpuType !== 'discrete') return false;
      } else if (currentBrand !== 'all') {
        if (lap.brand !== currentBrand) return false;
      }

      // Pill filter
      if (currentPill === 'under-100k' && lap.price >= 100000) return false;
      if (currentPill === '100k-200k' && (lap.price < 100000 || lap.price > 200000)) return false;
      if (currentPill === '200k-plus' && lap.price <= 200000) return false;
      if (currentPill === 'touch' && !lap.display.toLowerCase().includes('touch')) return false;
      if (currentPill === 'core-i7' && !(lap.cpu.toLowerCase().includes('i7') || lap.cpu.toLowerCase().includes('i9') || lap.cpu.toLowerCase().includes('ryzen 7'))) return false;

      // Search query
      if (searchQuery) {
        const q = searchQuery.toLowerCase();
        const haystack = (lap.name + ' ' + lap.brandName + ' ' + lap.cpu + ' ' + lap.display + ' ' + lap.gpu + ' ' + lap.category).toLowerCase();
        if (!haystack.includes(q)) return false;
      }

      return true;
    });

    // Sort
    if (currentSort === 'price-asc') {
      filtered.sort((a, b) => a.price - b.price);
    } else if (currentSort === 'price-desc') {
      filtered.sort((a, b) => b.price - a.price);
    } else if (currentSort === 'name-asc') {
      filtered.sort((a, b) => a.name.localeCompare(b.name));
    }

    const countEl = document.getElementById('visibleCount');
    if (countEl) countEl.textContent = filtered.length;

    if (filtered.length === 0) {
      grid.innerHTML = `
        <div style="grid-column:1/-1;text-align:center;padding:4rem 1rem;background:var(--s1);border:1px solid var(--border);border-radius:12px">
          <div style="font-size:3rem;margin-bottom:0.5rem">🔍</div>
          <h3 style="font-size:1.3rem;font-weight:700;color:var(--heading);margin-bottom:0.5rem">No matching laptops found</h3>
          <p style="color:var(--muted);font-size:0.9rem">Try clearing search filters or selecting "All Laptops".</p>
        </div>`;
      return;
    }

    grid.innerHTML = filtered.map(lap => {
      const waMsg = encodeURIComponent(`Hi LaptopHUB! I am interested in purchasing the ${lap.name} (${lap.priceFormatted}). Please confirm availability!`);
      return `
        <div class="pcard" data-brand="${lap.brand}">
          <div class="pcard-top">
            <span class="pcard-badge ${lap.badgeType || 'b-corp'}">${lap.badge}</span>
            <span class="brand-chip">${lap.brandName}</span>
          </div>
          <div class="pcard-photo-wrap">
            <img src="${lap.img}" alt="${lap.name}" class="pcard-photo" loading="lazy">
          </div>
          <h3 class="pcard-title">${lap.name}</h3>
          <p class="pcard-specs">${lap.category} · ${lap.condition}</p>
          <div class="spec-tags">
            <span class="spec-pill">${lap.cpu}</span>
            <span class="spec-pill">${lap.ram}GB RAM</span>
            <span class="spec-pill">${lap.storage >= 1000 ? (lap.storage/1000)+'TB' : lap.storage+'GB'} NVMe</span>
            <span class="spec-pill">${lap.display}</span>
            <span class="spec-pill">${lap.gpu}</span>
          </div>
          <div class="pcard-footer">
            <div class="price-col">
              <span class="price-label">Cash Price</span>
              <span class="pcard-price">${lap.priceFormatted}</span>
            </div>
            <div class="card-action-row">
              <a href="https://wa.me/923001234567?text=${waMsg}" target="_blank" class="btn-wa-card" title="Chat on WhatsApp">💬</a>
              <button class="btn-card-add" onclick="addToCartById(${lap.id})">+ Cart</button>
            </div>
          </div>
        </div>`;
    }).join('');
  }

  // Filter actions
  function filterBrand(brand, btn) {
    currentBrand = brand;
    if (btn) {
      document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
    }
    renderProducts();
  }

  function filterPill(pill, btn) {
    currentPill = pill;
    if (btn) {
      document.querySelectorAll('.pill-filter').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
    }
    renderProducts();
  }

  function handleSearch() {
    searchQuery = document.getElementById('laptopSearch').value.trim();
    renderProducts();
  }

  function handleSort(val) {
    currentSort = val;
    renderProducts();
  }

  // CART LOGIC
  function saveCart() {
    localStorage.setItem('lh_cart_items', JSON.stringify(cart));
    updateCartUI();
  }

  function updateCartUI() {
    const totalCount = cart.reduce((sum, item) => sum + item.qty, 0);
    const cartCountEl = document.getElementById('cartCount');
    const drawerBadge = document.getElementById('drawerCartBadge');
    if (cartCountEl) cartCountEl.textContent = totalCount;
    if (drawerBadge) drawerBadge.textContent = totalCount;

    const itemsContainer = document.getElementById('drawerItemsList');
    const subtotalEl = document.getElementById('drawerSubtotal');
    if (!itemsContainer || !subtotalEl) return;

    if (cart.length === 0) {
      itemsContainer.innerHTML = `
        <div class="drawer-empty">
          <div class="drawer-empty-icon">🛒</div>
          <p>Your cart is empty.</p>
          <span style="font-size:0.8rem;color:var(--muted)">Select any of our 69 premium laptops to begin!</span>
        </div>`;
      subtotalEl.textContent = 'Rs 0';
      return;
    }

    let subtotal = 0;
    itemsContainer.innerHTML = cart.map(item => {
      const itemTotal = item.price * item.qty;
      subtotal += itemTotal;
      return `
        <div class="cart-item">
          <img src="${item.img}" alt="${item.name}" class="cart-item-img">
          <div class="cart-item-info">
            <div class="cart-item-name">${item.name}</div>
            <div class="cart-item-specs">${item.cpu} · ${item.ram}GB RAM</div>
            <div class="cart-item-price">Rs ${itemTotal.toLocaleString('en-PK')}</div>
          </div>
          <div class="cart-item-qty">
            <button class="qty-btn" onclick="changeQty(${item.id}, -1)">−</button>
            <span class="qty-num">${item.qty}</span>
            <button class="qty-btn" onclick="changeQty(${item.id}, 1)">+</button>
          </div>
          <button class="cart-item-del" onclick="removeFromCart(${item.id})" title="Remove">🗑️</button>
        </div>`;
    }).join('');

    subtotalEl.textContent = `Rs ${subtotal.toLocaleString('en-PK')}`;
    const modalTotal = document.getElementById('modalOrderTotal');
    if (modalTotal) modalTotal.textContent = `Rs ${subtotal.toLocaleString('en-PK')}`;
  }

  function addToCartById(id) {
    const lap = inventory.find(l => l.id === id);
    if (!lap) return;
    const existing = cart.find(i => i.id === id);
    if (existing) {
      existing.qty++;
    } else {
      cart.push({
        id: lap.id,
        name: lap.name,
        price: lap.price,
        cpu: lap.cpu,
        ram: lap.ram,
        img: lap.img,
        qty: 1
      });
    }
    saveCart();
    showToast(`Added ${lap.name} to cart!`);
  }

  function changeQty(id, delta) {
    const item = cart.find(i => i.id === id);
    if (!item) return;
    item.qty += delta;
    if (item.qty <= 0) {
      cart = cart.filter(i => i.id !== id);
    }
    saveCart();
  }

  function removeFromCart(id) {
    cart = cart.filter(i => i.id !== id);
    saveCart();
    showToast('Item removed from cart');
  }

  function openCart() {
    updateCartUI();
    document.getElementById('cartOverlay').classList.add('open');
    document.getElementById('cartDrawer').classList.add('open');
  }

  function closeCart() {
    document.getElementById('cartOverlay').classList.remove('open');
    document.getElementById('cartDrawer').classList.remove('open');
  }

  function checkoutWhatsApp() {
    if (cart.length === 0) {
      showToast('Your cart is empty!');
      return;
    }
    let subtotal = 0;
    let itemsText = cart.map((i, idx) => {
      const lineTotal = i.price * i.qty;
      subtotal += lineTotal;
      return `${idx+1}. ${i.name} (x${i.qty}) - Rs ${lineTotal.toLocaleString('en-PK')}`;
    }).join('%0A');

    const msg = `*New Laptop Order - LaptopHUB Pakistan*%0A%0A*Items:*%0A${itemsText}%0A%0A*Subtotal:* Rs ${subtotal.toLocaleString('en-PK')}%0A*Delivery:* Free Cash on Delivery%0A%0APlease confirm my order!`;
    window.open(`https://wa.me/923001234567?text=${msg}`, '_blank');
  }

  function openCheckoutModal() {
    if (cart.length === 0) {
      showToast('Please add items to cart first!');
      return;
    }
    closeCart();
    document.getElementById('checkoutModal').classList.add('open');
  }

  function closeCheckoutModal() {
    document.getElementById('checkoutModal').classList.remove('open');
  }

  function handlePlaceOrder(e) {
    e.preventDefault();
    const name = document.getElementById('custName').value.trim();
    const phone = document.getElementById('custPhone').value.trim();
    const city = document.getElementById('custCity').value;
    const address = document.getElementById('custAddress').value.trim();

    const orderId = '#LH-' + Math.floor(1000 + Math.random() * 9000);
    document.getElementById('confirmOrderId').textContent = orderId;
    document.getElementById('confirmCustomer').textContent = `${name} (${city})`;

    // Reset cart
    cart = [];
    saveCart();
    closeCheckoutModal();
    document.getElementById('orderConfirmModal').classList.add('open');
  }

  function closeConfirmModal() {
    document.getElementById('orderConfirmModal').classList.remove('open');
  }

  // Toast
  let toastTimer;
  function showToast(msg) {
    const toast = document.getElementById('toast');
    if (!toast) return;
    document.getElementById('toastMsg').textContent = msg;
    toast.classList.add('show');
    clearTimeout(toastTimer);
    toastTimer = setTimeout(() => toast.classList.remove('show'), 3000);
  }

  function handleSubscribe(e) {
    e.preventDefault();
    const email = document.getElementById('subEmail').value;
    showToast(`Subscribed ${email} to weekly stock drops!`);
    document.getElementById('subEmail').value = '';
  }

  // FAQ Accordion
  document.querySelectorAll('.faq-q').forEach(btn => {
    btn.addEventListener('click', () => {
      const item = btn.parentElement;
      const wasOpen = item.classList.contains('open');
      document.querySelectorAll('.faq-item').forEach(i => i.classList.remove('open'));
      if (!wasOpen) item.classList.add('open');
    });
  });

  // Init
  renderProducts();
  updateCartUI();
</script>
'''

# Replace script block
script_pattern = re.compile(r'<script>.*?</script>', re.DOTALL)
content = script_pattern.sub(js_code, content, count=1)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated laptophub.html successfully!")
