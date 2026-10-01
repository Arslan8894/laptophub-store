/**
 * store-config.js
 * Central Configuration & Utilities for LaptopHUB & VOLTS Stores
 * 
 * Single source of truth for:
 * - Owner contact numbers (WhatsApp / Calls)
 * - Store identity & metadata
 * - Cart & User session state helpers
 * - Message formatting for WhatsApp orders & custom specs
 */

const STORE_CONFIG = {
  storeName: "LaptopHUB Pakistan",
  editionVolts: "VOLTS Performance Arsenal",
  tagline: "Premium Laptops. Every Spec. Honest Prices.",
  
  // PRIMARY OWNER CONTACT (Used across all stores, carts, and configurators)
  contact: {
    whatsapp: "923261398594",
    phoneDisplay: "+92 326 1398594",
    phoneTel: "+923261398594",
    email: "support@laptophub.pk",
    businessHours: "Mon – Sat (10:00 AM – 8:00 PM PKT)",
    address: "Lahore / Karachi / Islamabad Dispatch Centers, Pakistan"
  },

  // SHIPPING & GUARANTEE
  delivery: {
    freeShipping: true,
    policy: "Free Express Cash on Delivery Across Pakistan",
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
    customRequests: "lh_custom_requests",
    theme: "laptophub_theme"
  },

  // NAVIGATION ROUTES
  routes: {
    home: "laptophub.html",
    createLaptop: "custom-laptop.html",
    consult: "consult.html",
    volts: "volts.html",
    inventory: "inventory.html",
    suitePortal: "index.html"
  }
};

// ============================================================================
// STORE UTILITY FUNCTIONS
// ============================================================================

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
 * Save user session to localStorage
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
  msg += `*Payment:* Cash on Delivery (COD)\n`;
  msg += `*Shipping:* Free Express Dispatch\n\n`;
  msg += `Please confirm availability and dispatch time!`;

  return msg;
}

/**
 * Build WhatsApp quotation message for custom laptop configurator
 * @param {Object} specs - Configured laptop specs
 * @param {Object} client - Client contact info
 * @returns {string} Plaintext formatted message
 */
function formatCustomSpecWhatsAppMessage(specs, client = {}) {
  let msg = `*🛠️ CUSTOM LAPTOP SPECIFICATION REQUEST*\n`;
  msg += `*${STORE_CONFIG.storeName} — Custom Build Desk*\n`;
  msg += `------------------------------------------\n`;
  if (client.name) msg += `*Client Name:* ${client.name}\n`;
  if (client.phone) msg += `*Phone / WhatsApp:* ${client.phone}\n`;
  if (client.city) msg += `*City:* ${client.city}\n`;
  if (client.timeline) msg += `*Timeline:* ${client.timeline}\n`;
  msg += `------------------------------------------\n`;
  if (specs.brand) msg += `*Brand:* ${specs.brand}\n`;
  if (specs.formFactor) msg += `*Chassis:* ${specs.formFactor}\n`;
  if (specs.cpu) msg += `*Processor (CPU):* ${specs.cpu}\n`;
  if (specs.gpu) msg += `*Graphics (GPU):* ${specs.gpu}\n`;
  if (specs.ram) msg += `*Memory (RAM):* ${specs.ram}\n`;
  if (specs.storage) msg += `*Storage (SSD):* ${specs.storage}\n`;
  if (specs.display) msg += `*Display:* ${specs.display}\n`;
  if (specs.condition) msg += `*Condition:* ${specs.condition}\n`;
  if (specs.budget) msg += `*Target Budget:* Rs ${Number(specs.budget).toLocaleString('en-PK')}\n`;
  if (specs.useCases && specs.useCases.length) msg += `*Use Cases:* ${specs.useCases.join(', ')}\n`;
  if (specs.features && specs.features.length) msg += `*Features:* ${specs.features.join(', ')}\n`;
  if (client.notes) msg += `*Notes:* ${client.notes}\n`;
  msg += `------------------------------------------\n`;
  msg += `Please send available matching inventory and best cash price!`;

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
    formatCartWhatsAppMessage,
    formatCustomSpecWhatsAppMessage
  };
}
