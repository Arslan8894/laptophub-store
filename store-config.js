/**
 * store-config.js
 * Central Configuration & Utilities for LaptopHUB
 *
 * Single source of truth for:
 * - Owner contact numbers (WhatsApp / Calls)
 * - Store identity & metadata
 * - Cart & User session state helpers
 * - Message formatting for WhatsApp orders
 */

const STORE_CONFIG = {
  storeName: "LaptopHUB Pakistan",
  tagline: "Premium Laptops. Every Spec. Honest Prices.",

  // PRIMARY OWNER CONTACT (Used across all stores, carts, and configurators)
  contact: {
    whatsapp: "923261398594",
    phoneDisplay: "+92 326 1398594",
    phoneTel: "+923261398594",
    email: "contact.laptophubofficial@gmail.com",
    businessHours: "Mon – Sat (10:00 AM – 8:00 PM PKT)",
    address: "Lahore / Karachi / Islamabad Dispatch Centers, Pakistan"
  },

  // SHIPPING & GUARANTEE
  delivery: {
    freeShipping: true,
    policy: "Free Express Insured Dispatch Across Pakistan",
    timelines: {
      lahore: "Same Day / 24 Hours",
      karachi: "24 to 48 Hours via Express Courier",
      islamabad: "24 to 48 Hours via Express Courier",
      other: "2 to 4 Business Days"
    },
    warranty: "7-Day Checking & Replacement Guarantee + Up to 3 Years Official Manufacturer Warranty"
  },

  // LOCAL STORAGE STATE KEYS
  storageKeys: {
    cart: "lh_cart_items",
    user: "lh_user",
    orders: "lh_orders",
    theme: "laptophub_theme"
  },

  // NAVIGATION ROUTES
  routes: {
    home: "laptophub.html",
    consult: "consult.html",
    admin: "admin/index.html"
  },

  // UPGRADE PRICING TIERS
  // Cumulative price per RAM size (cumulative: 8GB=0, 16GB=8000, 32GB=23000)
  // Per pricing rule: 8GB to 16GB = +Rs 8,000; 16GB to 32GB = +Rs 15,000
  ramPricingTiers: {
    DDR4: {
      8: 0,
      16: 8000,
      32: 23000
    },
    DDR5: {
      8: 0,
      16: 10000,
      32: 28000
    }
  },
  storagePricingTiers: {
    128: 0,
    256: 4000,
    512: 9000,
    1000: 21000
  }
};

// ============================================================================
// STORE UTILITY FUNCTIONS
// ============================================================================

/**
 * Retrieve current active RAM tier table
 * Checks in-memory cache, localStorage, or falls back to STORE_CONFIG
 * @param {string} ramType - "DDR4" or "DDR5"
 * @returns {Object}
 */
function getRamTierTable(ramType = 'DDR4') {
  const isDdr5 = String(ramType).toUpperCase().includes('DDR5');
  const typeKey = isDdr5 ? 'DDR5' : 'DDR4';
  
  if (typeof window !== 'undefined' && window.LH_RAM_TIERS && window.LH_RAM_TIERS[typeKey]) {
    return window.LH_RAM_TIERS[typeKey];
  }
  try {
    const cached = JSON.parse(localStorage.getItem('lh_ram_pricing') || 'null');
    if (cached && cached[typeKey]) return cached[typeKey];
  } catch (_) {}

  return (STORE_CONFIG.ramPricingTiers && STORE_CONFIG.ramPricingTiers[typeKey]) 
    || (isDdr5 ? { 8: 0, 16: 10000, 32: 28000 } : { 8: 0, 16: 8000, 32: 23000 });
}

/**
 * Calculate RAM price difference relative to laptop's base RAM
 * @param {number} targetRam - e.g. 8, 16, 32
 * @param {number} baseRam - e.g. 8, 16, 32
 * @param {string} ramType - "DDR4" or "DDR5"
 * @param {boolean} isUpgradable - false if soldered/non-upgradable
 * @returns {number} difference in PKR (positive, 0, or negative)
 */
function getRamDelta(targetRam, baseRam, ramType = 'DDR4', isUpgradable = true) {
  if (!isUpgradable || targetRam === baseRam) return 0;
  const table = getRamTierTable(ramType);
  const targetVal = Number(table[targetRam] ?? (table[String(targetRam)] ?? 0));
  const baseVal = Number(table[baseRam] ?? (table[String(baseRam)] ?? 0));
  return targetVal - baseVal;
}

/**
 * Calculate Storage price difference relative to laptop's base storage
 * @param {number} targetStorage - e.g. 128, 256, 512, 1000
 * @param {number} baseStorage - e.g. 128, 256, 512, 1000
 * @returns {number} difference in PKR
 */
function getStorageDelta(targetStorage, baseStorage) {
  if (targetStorage === baseStorage) return 0;
  let table = null;
  if (typeof window !== 'undefined' && window.LH_STORAGE_TIERS) {
    table = window.LH_STORAGE_TIERS;
  } else {
    try {
      table = JSON.parse(localStorage.getItem('lh_storage_pricing') || 'null');
    } catch (_) {}
  }
  if (!table) {
    table = STORE_CONFIG.storagePricingTiers || { 128: 0, 256: 4000, 512: 9000, 1000: 21000 };
  }
  const targetVal = Number(table[targetStorage] ?? (table[String(targetStorage)] ?? 9000));
  const baseVal = Number(table[baseStorage] ?? (table[String(baseStorage)] ?? 9000));
  return targetVal - baseVal;
}

/**
 * Fetch dynamic RAM & Storage pricing tiers from server on initialization
 */
async function loadDynamicRamPricing() {
  if (typeof fetch === 'undefined') return;
  // If running on static host (GitHub Pages, file://, etc.) where /api endpoints do not exist, use default tiers without 404 network waste
  if (typeof window !== 'undefined' && window.location) {
    const host = window.location.hostname || '';
    const proto = window.location.protocol || '';
    if (proto === 'file:' || host.endsWith('github.io') || host.endsWith('pages.dev')) {
      return;
    }
  }
  try {
    const res = await fetch('/api/config/ram-pricing');
    if (res.ok) {
      const data = await res.json();
      if (typeof window !== 'undefined') {
        window.LH_RAM_TIERS = data;
        localStorage.setItem('lh_ram_pricing', JSON.stringify(data));
      }
    }
  } catch (_) {}
  try {
    const resStor = await fetch('/api/config/storage-pricing');
    if (resStor.ok) {
      const dataStor = await resStor.json();
      if (typeof window !== 'undefined') {
        window.LH_STORAGE_TIERS = dataStor;
        localStorage.setItem('lh_storage_pricing', JSON.stringify(dataStor));
      }
    }
  } catch (_) {}
}
if (typeof window !== 'undefined') {
  loadDynamicRamPricing();
}

/**
 * Generate direct WhatsApp deep-link with pre-filled message
 * @param {string} text - Message text to encode
 * @returns {string} WhatsApp URL
 */
function getWhatsAppUrl(text) {
  const number = STORE_CONFIG.contact.whatsapp;
  if (!text) return `https://wa.me/${number}`;
  return `https://wa.me/${number}?text=${encodeURIComponent(text)}`;
}

/**
 * Format raw number to PKR Currency format
 * @param {number} amount - Numeric price
 * @returns {string} Formatted price e.g. "Rs 154,000"
 */
function formatPKR(amount) {
  if (typeof amount !== 'number') return 'Rs 0';
  return `Rs ${amount.toLocaleString('en-PK')}`;
}

/**
 * Load cart items from localStorage
 * @returns {Array} Array of cart item objects
 */
function getLocalCart() {
  try {
    return JSON.parse(localStorage.getItem(STORE_CONFIG.storageKeys.cart) || '[]');
  } catch (e) {
    return [];
  }
}

/**
 * Save cart items to localStorage
 * @param {Array} cart - Array of cart item objects
 */
function saveLocalCart(cart) {
  try {
    localStorage.setItem(STORE_CONFIG.storageKeys.cart, JSON.stringify(cart));
  } catch (e) {
    console.error("Failed to save cart to localStorage", e);
  }
}

/**
 * Get active user session from localStorage
 * NOTE: With the new server-side session system this is only used as a
 * UI-only cache for display name / email. Role and auth are always
 * verified against /api/auth/me on page load.
 * @returns {Object|null} User session or null
 */
function getActiveUser() {
  try {
    return JSON.parse(localStorage.getItem(STORE_CONFIG.storageKeys.user) || 'null');
  } catch (e) {
    return null;
  }
}

/**
 * Save user session to localStorage (display cache only)
 * @param {Object} user - User session object
 */
function saveActiveUser(user) {
  try {
    localStorage.setItem(STORE_CONFIG.storageKeys.user, JSON.stringify(user));
  } catch (e) {
    console.error("Failed to save user session", e);
  }
}

/**
 * Build WhatsApp checkout message for shopping cart
 * @param {Array} cart - Cart items
 * @param {Object} customer - Customer details { name, phone, city, address }
 * @returns {string} Plaintext formatted message
 */
function formatCartWhatsAppMessage(cart, customer = {}) {
  let subtotal = 0;
  const itemsText = cart.map((item, idx) => {
    const lineTotal = (item.price || 0) * (item.qty || 1);
    subtotal += lineTotal;
    return `${idx + 1}. ${item.name} (x${item.qty}) — Rs ${lineTotal.toLocaleString('en-PK')}`;
  }).join('\n');

  let msg = `*🛒 NEW LAPTOP ORDER — ${STORE_CONFIG.storeName}*\n`;
  msg += `------------------------------------------\n`;
  if (customer.name) msg += `*Customer:* ${customer.name}\n`;
  if (customer.phone) msg += `*Contact:* ${customer.phone}\n`;
  if (customer.city) msg += `*City:* ${customer.city}\n`;
  if (customer.address) msg += `*Address:* ${customer.address}\n`;
  msg += `------------------------------------------\n`;
  msg += `*Order Items:*\n${itemsText}\n`;
  msg += `------------------------------------------\n`;
  msg += `*Subtotal:* Rs ${subtotal.toLocaleString('en-PK')}\n`;
  msg += `*Payment:* Direct Bank Transfer / Raast (IBFT)\n`;
  msg += `*Shipping:* Free Express Dispatch\n\n`;
  msg += `Please confirm availability and dispatch time!`;

  return msg;
}

// Export for Node/CommonJS environments if required
if (typeof module !== 'undefined' && module.exports) {
  module.exports = {
    STORE_CONFIG,
    getWhatsAppUrl,
    formatPKR,
    getLocalCart,
    saveLocalCart,
    getActiveUser,
    saveActiveUser,
    formatCartWhatsAppMessage
  };
}
