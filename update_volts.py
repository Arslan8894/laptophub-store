import re

file_path = r"c:\Users\Arslan\.antigravity-ide\laptop-store\volts.html"
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add script tag in head if not present
if '<script src="laptops-data.js"></script>' not in content:
    content = content.replace('</head>', '<script src="laptops-data.js"></script>\n</head>')

# 2. Update hero
content = content.replace('View 7 Laptops', 'Explore All 69 Laptops')

# 3. Add search and filter toolbar to volts.html
volts_toolbar_css = '''
  .volts-filter-row {
    display: flex; justify-content: space-between; align-items: center;
    gap: 1rem; margin-bottom: 2.5rem; flex-wrap: wrap;
  }
  .v-filter-tabs { display: flex; gap: 6px; flex-wrap: wrap; }
  .v-filter-btn {
    background: var(--surface); border: 1px solid var(--border);
    color: var(--muted); padding: 0.5rem 1.1rem; border-radius: 6px;
    font-family: inherit; font-size: 0.8rem; font-weight: 700;
    cursor: pointer; transition: all 0.2s;
  }
  .v-filter-btn:hover { color: #fff; border-color: var(--accent); }
  .v-filter-btn.active {
    background: var(--accent); color: #000; border-color: var(--accent);
    box-shadow: 0 0 15px var(--accent-glow);
  }
  .v-search {
    background: var(--surface); border: 1px solid var(--border);
    color: #fff; padding: 0.55rem 1.2rem; border-radius: 6px;
    font-family: inherit; font-size: 0.85rem; outline: none; width: 280px;
    transition: border-color 0.2s;
  }
  .v-search:focus { border-color: var(--accent); }
'''
if '.volts-filter-row' not in content:
    content = content.replace('</style>', volts_toolbar_css + '\n</style>')

# 4. Replace products grid section
new_products_section = '''<!-- PRODUCTS -->
<section class="section" id="models">
  <div class="section-header">
    <div>
      <p class="section-label">Verified Inventory</p>
      <h2 class="section-title">Hardware Lineup (69 Models)</h2>
    </div>
  </div>

  <div class="volts-filter-row">
    <div class="v-filter-tabs">
      <button class="v-filter-btn active" onclick="vFilter('all', this)">All (69)</button>
      <button class="v-filter-btn" onclick="vFilter('lenovo', this)">Lenovo (15)</button>
      <button class="v-filter-btn" onclick="vFilter('dell', this)">Dell (19)</button>
      <button class="v-filter-btn" onclick="vFilter('hp', this)">HP (22)</button>
      <button class="v-filter-btn" onclick="vFilter('apple', this)">Apple (3)</button>
      <button class="v-filter-btn" onclick="vFilter('microsoft', this)">Surface (7)</button>
      <button class="v-filter-btn" onclick="vFilter('gaming', this)">Gaming (4)</button>
    </div>
    <input type="text" class="v-search" id="voltsSearch" placeholder="Search 69 models..." oninput="vSearch()">
  </div>

  <div class="products-grid" id="voltsProductsGrid">
    <!-- Rendered dynamically from laptops-data.js -->
  </div>
</section>'''

# Replace products section
prod_pattern = re.compile(r'<!-- PRODUCTS -->.*?</section>', re.DOTALL)
content = prod_pattern.sub(new_products_section, content, count=1)

# 5. Update script in volts.html
volts_script = '''
<script>
  let cartTotal = 0;
  let vCurrentBrand = 'all';
  let vSearchQuery = '';

  const inventory = (typeof LAPTOPS_INVENTORY !== 'undefined') ? LAPTOPS_INVENTORY : [];

  function renderVoltsProducts() {
    const grid = document.getElementById('voltsProductsGrid');
    if (!grid) return;

    let filtered = inventory.filter(lap => {
      if (vCurrentBrand === 'gaming') {
        if (lap.gpuType !== 'rtx' && lap.gpuType !== 'discrete') return false;
      } else if (vCurrentBrand !== 'all') {
        if (lap.brand !== vCurrentBrand) return false;
      }

      if (vSearchQuery) {
        const q = vSearchQuery.toLowerCase();
        const haystack = (lap.name + ' ' + lap.brandName + ' ' + lap.cpu + ' ' + lap.gpu).toLowerCase();
        if (!haystack.includes(q)) return false;
      }

      return true;
    });

    if (filtered.length === 0) {
      grid.innerHTML = '<div style="grid-column:1/-1;text-align:center;padding:3rem;color:var(--muted)">No models matched your search query.</div>';
      return;
    }

    grid.innerHTML = filtered.map(lap => {
      const badgeClass = lap.gpuType === 'rtx' ? 'badge-hot' : (lap.brand === 'apple' ? 'badge-pro' : 'badge-new');
      return `
        <div class="product-card">
          <div class="card-top">
            <span class="card-badge ${badgeClass}">${lap.badge}</span>
            <span style="font-size:0.75rem;color:var(--muted);text-transform:uppercase;font-weight:700">${lap.brandName}</span>
          </div>
          <div class="photo-box">
            <img src="${lap.img}" alt="${lap.name}" class="laptop-img" loading="lazy">
          </div>
          <h3 class="card-name">${lap.name}</h3>
          <p class="card-specs">${lap.category} · ${lap.condition}</p>
          <div class="tag-row">
            <span class="tag">${lap.cpu}</span>
            <span class="tag">${lap.ram}GB RAM</span>
            <span class="tag">${lap.storage >= 1000 ? (lap.storage/1000)+'TB' : lap.storage+'GB'} SSD</span>
            <span class="tag">${lap.display}</span>
          </div>
          <div class="card-price-row">
            <span class="card-price">$${lap.priceUsd} <small style="font-size:0.75rem;color:var(--muted)">(${lap.priceFormatted})</small></span>
            <button class="btn-buy-card" onclick="addToCart('${lap.name}', '$${lap.priceUsd}')">+ Cart</button>
          </div>
        </div>`;
    }).join('');
  }

  function vFilter(brand, btn) {
    vCurrentBrand = brand;
    if (btn) {
      document.querySelectorAll('.v-filter-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
    }
    renderVoltsProducts();
  }

  function vSearch() {
    vSearchQuery = document.getElementById('voltsSearch').value.trim();
    renderVoltsProducts();
  }

  function addToCart(name, price) {
    cartTotal++;
    const countEl = document.getElementById('cartCount');
    if (countEl) countEl.textContent = cartTotal;
    showToast(`Added ${name} (${price}) to cart!`);
  }

  function openCartToast() {
    showToast(`Your cart has ${cartTotal} item(s).`);
  }

  let toastTimer;
  function showToast(msg) {
    const toast = document.getElementById('toast');
    if (!toast) return;
    document.getElementById('toastMsg').textContent = msg;
    toast.classList.add('show');
    clearTimeout(toastTimer);
    toastTimer = setTimeout(() => toast.classList.remove('show'), 3000);
  }

  renderVoltsProducts();
</script>
'''

content = re.sub(r'<script>.*?</script>', volts_script, content, flags=re.DOTALL)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated volts.html successfully!")
