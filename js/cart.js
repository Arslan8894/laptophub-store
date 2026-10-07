/**
 * LaptopHUB - Unified Cart System (js/cart.js)
 * Clean, modular cart management with full persistence, touch accessibility,
 * z-index layering, and synchronized WhatsApp / COD checkout flows.
 */

(function(window) {
  'use strict';

  const STORAGE_KEY = 'lh_cart_items';
  let cart = [];

  function loadCart() {
    try {
      const saved = localStorage.getItem(STORAGE_KEY);
      cart = saved ? JSON.parse(saved) : [];
      if (!Array.isArray(cart)) cart = [];
    } catch (_) {
      cart = [];
    }
    return cart;
  }

  function saveCart() {
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(cart));
    } catch (_) {}
    updateCartUI();
  }

  function getCart() {
    return cart;
  }

  function getCartSubtotal() {
    return cart.reduce((sum, item) => sum + (Number(item.price) || 0) * (Number(item.qty) || 1), 0);
  }

  function getCartTotalCount() {
    return cart.reduce((sum, item) => sum + (Number(item.qty) || 1), 0);
  }

  /**
   * Add a laptop item to cart with custom or default configurations
   */
  function addToCart(laptopOrId, options = {}) {
    let lap = laptopOrId;
    if (typeof laptopOrId === 'number' || typeof laptopOrId === 'string') {
      const inv = window.inventory || (typeof LAPTOPS_INVENTORY !== 'undefined' ? LAPTOPS_INVENTORY : []);
      lap = inv.find(l => String(l.id) === String(laptopOrId));
    }
    if (!lap) return false;

    // Check stock
    const curStock = lap.stock !== undefined ? lap.stock : 1;
    if (curStock <= 0) {
      if (typeof window.showToast === 'function') {
        window.showToast(`Sorry, ${lap.name} is currently out of stock!`);
      }
      return false;
    }

    const ram = options.ram !== undefined ? options.ram : lap.ram;
    const ramType = options.ramType || lap.ramType || lap.fullSpecs?.memoryStorage?.ramType || 'DDR4';
    const storage = options.storage !== undefined ? options.storage : lap.storage;
    const storageType = options.storageType || lap.storageType || lap.fullSpecs?.memoryStorage?.storageType || 'NVMe SSD';
    const price = options.price !== undefined ? options.price : lap.price;
    const comment = options.comment || '';

    // Create unique key per configuration
    const itemKey = `${lap.id}-${ram}-${storage}`;
    const existing = cart.find(i => (i.itemKey ? i.itemKey === itemKey : i.id === lap.id));

    if (existing) {
      if (existing.qty + 1 > curStock) {
        if (typeof window.showToast === 'function') {
          window.showToast(`Only ${curStock} units available for ${lap.name}`);
        }
        return false;
      }
      existing.qty = (existing.qty || 1) + 1;
    } else {
      cart.push({
        id: lap.id,
        itemKey: itemKey,
        name: lap.name,
        brand: lap.brandName || lap.brand,
        price: Number(price),
        priceFormatted: `Rs ${Number(price).toLocaleString('en-PK')}`,
        img: lap.img,
        ram: Number(ram),
        ramType: ramType,
        ramLabel: `${ram} GB ${ramType}`,
        storage: Number(storage),
        storageType: storageType,
        storageLabel: (storage >= 1000 ? (storage / 1000) + ' TB' : storage + ' GB') + ' ' + storageType,
        comment: comment,
        qty: 1
      });
    }

    saveCart();
    if (typeof window.showToast === 'function') {
      window.showToast(`✓ Added ${lap.name} to cart!`);
    }
    return true;
  }

  function removeFromCart(keyOrId) {
    cart = cart.filter(i => (i.itemKey ? i.itemKey !== String(keyOrId) : String(i.id) !== String(keyOrId)));
    saveCart();
    if (typeof window.showToast === 'function') {
      window.showToast('Item removed from cart');
    }
  }

  function updateCartQty(keyOrId, delta) {
    const item = cart.find(i => (i.itemKey ? i.itemKey === String(keyOrId) : String(i.id) === String(keyOrId)));
    if (!item) return;

    // Check stock limit if increasing
    if (delta > 0) {
      const inv = window.inventory || (typeof LAPTOPS_INVENTORY !== 'undefined' ? LAPTOPS_INVENTORY : []);
      const lap = inv.find(l => String(l.id) === String(item.id));
      if (lap && lap.stock !== undefined && item.qty + delta > lap.stock) {
        if (typeof window.showToast === 'function') {
          window.showToast(`Only ${lap.stock} units available in stock.`);
        }
        return;
      }
    }

    item.qty = (item.qty || 1) + delta;
    if (item.qty <= 0) {
      removeFromCart(keyOrId);
      return;
    }
    saveCart();
  }

  function openCart() {
    updateCartUI();
    const overlay = document.getElementById('cartOverlay') || document.querySelector('.cart-drawer-overlay');
    const drawer = document.getElementById('cartDrawer') || document.querySelector('.cart-drawer');
    if (overlay) overlay.classList.add('open');
    if (drawer) drawer.classList.add('open');
    document.body.classList.add('cart-open');
  }

  function closeCart() {
    const overlay = document.getElementById('cartOverlay') || document.querySelector('.cart-drawer-overlay');
    const drawer = document.getElementById('cartDrawer') || document.querySelector('.cart-drawer');
    if (overlay) overlay.classList.remove('open');
    if (drawer) drawer.classList.remove('open');
    document.body.classList.remove('cart-open');
  }

  function updateCartUI() {
    const totalCount = getCartTotalCount();
    const subtotal = getCartSubtotal();

    // Update Badges
    document.querySelectorAll('.cart-badge-count, #cartBadge, #navCartBadge, #drawerCartBadge').forEach(el => {
      el.textContent = totalCount;
      el.style.display = totalCount > 0 ? 'inline-flex' : (el.id === 'drawerCartBadge' ? 'inline-flex' : 'none');
    });

    // Subtotal
    document.querySelectorAll('#drawerSubtotal, .subtotal-val').forEach(el => {
      el.textContent = `Rs ${subtotal.toLocaleString('en-PK')}`;
    });

    // Drawer Items List
    const container = document.getElementById('drawerItemsList') || document.getElementById('cartDrawerItems');
    if (!container) return;

    if (cart.length === 0) {
      container.innerHTML = `
        <div class="drawer-empty" style="text-align:center;padding:3rem 1.5rem;color:var(--muted,#94a3b8)">
          <div class="drawer-empty-icon" style="font-size:3rem;margin-bottom:0.75rem">🛒</div>
          <p style="font-weight:700;font-size:1.1rem;color:var(--heading,#fff);margin-bottom:0.35rem">Your Cart is Empty</p>
          <p style="font-size:0.85rem">Explore our laptops and add one to your cart!</p>
        </div>
      `;
      return;
    }

    container.innerHTML = cart.map(item => {
      const key = item.itemKey || item.id;
      const lineTotal = (item.price || 0) * (item.qty || 1);
      const storText = item.storage ? (item.storage >= 1000 ? (item.storage / 1000) + ' TB' : item.storage + ' GB') : '';
      const ramText = item.ram ? `${item.ram} GB` : '';
      const specTag = [ramText, storText].filter(Boolean).join(' · ');

      return `
        <div class="cart-item" style="display:flex;gap:12px;padding:12px 14px;background:var(--s2,rgba(255,255,255,0.04));border:1px solid var(--border-subtle,rgba(255,255,255,0.08));border-radius:12px;margin-bottom:10px;align-items:center;">
          <img src="${item.img || 'images/logo-icon.png'}" alt="${item.name}" style="width:58px;height:44px;object-fit:contain;background:var(--s1,rgba(0,0,0,0.2));border-radius:8px;padding:4px;flex-shrink:0;">
          <div style="flex:1;min-width:0;">
            <div style="font-size:0.88rem;font-weight:700;color:var(--heading,#fff);white-space:nowrap;overflow:hidden;text-overflow:ellipsis;">${item.name}</div>
            <div style="font-size:0.75rem;color:var(--muted,#94a3b8);margin-top:2px;">${specTag}</div>
            <div style="font-size:0.85rem;font-weight:800;color:var(--blue,#4c7cff);margin-top:4px;">Rs ${lineTotal.toLocaleString('en-PK')}</div>
          </div>
          <div style="display:flex;align-items:center;gap:6px;flex-shrink:0;">
            <button type="button" class="cart-qty-btn" onclick="window.updateCartQty('${key}', -1)" aria-label="Decrease quantity" style="width:28px;height:28px;border-radius:6px;border:1px solid var(--border,rgba(255,255,255,0.15));background:transparent;color:var(--text,#fff);cursor:pointer;font-weight:700;">-</button>
            <span style="font-size:0.85rem;font-weight:700;min-width:18px;text-align:center;">${item.qty}</span>
            <button type="button" class="cart-qty-btn" onclick="window.updateCartQty('${key}', 1)" aria-label="Increase quantity" style="width:28px;height:28px;border-radius:6px;border:1px solid var(--border,rgba(255,255,255,0.15));background:transparent;color:var(--text,#fff);cursor:pointer;font-weight:700;">+</button>
            <button type="button" class="cart-del-btn" onclick="window.removeFromCart('${key}')" aria-label="Remove item" style="background:transparent;border:none;color:#ef4444;cursor:pointer;padding:4px 6px;margin-left:4px;" title="Remove">🗑️</button>
          </div>
        </div>
      `;
    }).join('');
  }

  /**
   * Order via WhatsApp with complete configuration detail
   */
  function checkoutWhatsApp() {
    if (cart.length === 0) {
      if (typeof window.showToast === 'function') window.showToast('Your cart is empty!');
      return;
    }

    const user = window.currentUser || JSON.parse(localStorage.getItem('lh_user') || 'null');
    if (!user || !user.loggedIn) {
      // Close cart drawer first, then prompt login
      closeCart();
      if (typeof window.openLoginModal === 'function') {
        window.pendingBuyAction = { type: 'cart_whatsapp' };
        window.openLoginModal('Please sign in to confirm your WhatsApp order');
      }
      return;
    }

    let subtotal = 0;
    const itemsText = cart.map((i, idx) => {
      const lineTotal = i.price * i.qty;
      subtotal += lineTotal;
      const storStr = i.storage ? (i.storage >= 1000 ? (i.storage / 1000) + 'TB' : i.storage + 'GB') : '';
      let line = `${idx + 1}. *${i.name}* (x${i.qty})%0A   Specs: ${i.ram}GB RAM / ${storStr}%0A   Price: Rs ${lineTotal.toLocaleString('en-PK')}`;
      if (i.comment) line += `%0A   Note: "${encodeURIComponent(i.comment)}"`;
      return line;
    }).join('%0A%0A');

    let msg = `*🛒 NEW ORDER — LaptopHUB Pakistan*%0A`;
    msg += `------------------------------------------%0A`;
    if (user.name) msg += `*Customer:* ${encodeURIComponent(user.name)}%0A`;
    if (user.phone) msg += `*Contact:* ${encodeURIComponent(user.phone)}%0A`;
    if (user.city) msg += `*City:* ${encodeURIComponent(user.city)}%0A`;
    if (user.address) msg += `*Delivery Address:* ${encodeURIComponent(user.address)}%0A`;
    msg += `------------------------------------------%0A`;
    msg += `*Items Ordered:*%0A${itemsText}%0A`;
    msg += `------------------------------------------%0A`;
    msg += `*Total Amount:* Rs ${subtotal.toLocaleString('en-PK')}%0A`;
    msg += `*Payment:* Cash on Delivery (COD) / IBFT%0A`;
    msg += `*Shipping:* Insured Express Dispatch across Pakistan%0A%0A`;
    msg += `Please confirm my order and dispatch timeline!`;

    window.open(`https://wa.me/923261398594?text=${msg}`, '_blank');
  }

  // Initialize
  loadCart();

  // Export to window
  window.cart = cart;
  window.loadCart = loadCart;
  window.saveCart = saveCart;
  window.getCart = getCart;
  window.getCartSubtotal = getCartSubtotal;
  window.getCartTotalCount = getCartTotalCount;
  window.addToCart = addToCart;
  window.removeFromCart = removeFromCart;
  window.updateCartQty = updateCartQty;
  window.openCart = openCart;
  window.closeCart = closeCart;
  window.updateCartUI = updateCartUI;
  window.checkoutWhatsApp = checkoutWhatsApp;

  document.addEventListener('DOMContentLoaded', () => {
    loadCart();
    updateCartUI();
  });
})(window);
