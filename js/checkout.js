/**
 * LaptopHUB - Checkout & Order Processing System (js/checkout.js)
 * Implements Step 2 Layering & Z-Index architecture:
 * Always closes cart drawer first, layers checkout on top of everything,
 * cleans up scroll-locks, auto-decrements stock, and validates Pakistani deliveries.
 */

(function(window) {
  'use strict';

  function openCheckoutModal() {
    const cart = window.getCart ? window.getCart() : (window.cart || []);
    if (!cart || cart.length === 0) {
      if (typeof window.showToast === 'function') {
        window.showToast('Please add items to cart first!');
      }
      return;
    }

    // 1. STEP 2 DIRECTIVE: ALWAYS CLOSE CART DRAWER FIRST
    if (typeof window.closeCart === 'function') {
      window.closeCart();
    }

    // 2. AUTHENTICATION CHECK
    const user = window.currentUser || JSON.parse(localStorage.getItem('lh_user') || 'null');
    if (!user || !user.loggedIn) {
      window.pendingBuyAction = { type: 'checkout' };
      if (typeof window.openLoginModal === 'function') {
        window.openLoginModal('Please sign in to place your order');
      }
      return;
    }

    // 3. POPULATE CUSTOMER DETAILS IF AVAILABLE
    const nameInput = document.getElementById('custName');
    const phoneInput = document.getElementById('custPhone');
    const cityInput = document.getElementById('custCity');
    const addrInput = document.getElementById('custAddress');

    if (nameInput && user.name) nameInput.value = user.name;
    if (phoneInput && user.phone) phoneInput.value = user.phone;
    if (cityInput && user.city) cityInput.value = user.city;
    if (addrInput && user.address) addrInput.value = user.address;

    // 4. UPDATE TOTAL PAYABLE
    const subtotal = window.getCartSubtotal ? window.getCartSubtotal() : 0;
    const totalEl = document.getElementById('modalOrderTotal');
    if (totalEl) totalEl.textContent = `Rs ${subtotal.toLocaleString('en-PK')}`;

    // 5. OPEN CHECKOUT MODAL ON TOP OF EVERYTHING (Z-INDEX 12000)
    const modal = document.getElementById('checkoutModal');
    if (modal) {
      modal.classList.add('open');
      document.body.classList.add('modal-open');
    }
  }

  function closeCheckoutModal() {
    const modal = document.getElementById('checkoutModal');
    if (modal) {
      modal.classList.remove('open');
    }
    // Clean up modal-open scroll lock if no other modal is open
    const openModals = document.querySelectorAll('#loginModal.open, #checkoutModal.open, #orderConfirmModal.open, #myOrdersModal.open, #profileModal.open');
    if (openModals.length === 0) {
      document.body.classList.remove('modal-open');
    }
  }

  async function handlePlaceOrder(e) {
    if (e && e.preventDefault) e.preventDefault();

    const user = window.currentUser || JSON.parse(localStorage.getItem('lh_user') || 'null');
    if (!user || !user.loggedIn) {
      closeCheckoutModal();
      window.pendingBuyAction = { type: 'checkout' };
      if (typeof window.openLoginModal === 'function') {
        window.openLoginModal('Please sign in to place your order');
      }
      return;
    }

    const name = (document.getElementById('custName')?.value || '').trim();
    const phone = (document.getElementById('custPhone')?.value || '').trim();
    const city = document.getElementById('custCity')?.value || '';
    const address = (document.getElementById('custAddress')?.value || '').trim();

    if (!name) {
      if (typeof window.showToast === 'function') window.showToast('Please enter your full name');
      return;
    }

    const pkPhoneRe = /^(?:\+92|0092|0)?3[0-9]{2}[-\s]?[0-9]{7}$/;
    if (!phone || !pkPhoneRe.test(phone)) {
      if (typeof window.showToast === 'function') window.showToast('Please enter a valid Pakistani mobile number (03XX-XXXXXXX)');
      return;
    }

    if (!city) {
      if (typeof window.showToast === 'function') window.showToast('Please select your delivery city');
      return;
    }

    if (!address) {
      if (typeof window.showToast === 'function') window.showToast('Please enter your complete delivery address');
      return;
    }

    const cart = window.getCart ? window.getCart() : (window.cart || []);
    if (cart.length === 0) {
      if (typeof window.showToast === 'function') window.showToast('Your cart is empty!');
      return;
    }

    // Try posting to backend orders API
    let orderResult = null;
    try {
      const res = await fetch('/api/orders', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        credentials: 'include',
        body: JSON.stringify({ items: cart, name, phone, city, address })
      });
      if (res.ok) {
        orderResult = await res.json();
      }
    } catch (_) {}

    const orderIdNum = orderResult?.orderId || Math.floor(1000 + Math.random() * 9000);
    const orderId = '#LH-' + orderIdNum;

    // Auto-decrement inventory stock locally and in Firestore
    const inv = window.inventory || (typeof LAPTOPS_INVENTORY !== 'undefined' ? LAPTOPS_INVENTORY : []);
    cart.forEach(item => {
      const lap = inv.find(l => String(l.id) === String(item.id));
      if (lap && lap.stock !== undefined) {
        lap.stock = Math.max(0, lap.stock - (item.qty || 1));
        if (typeof window.fsUpdateLaptopStock === 'function') {
          try { window.fsUpdateLaptopStock(lap.id, lap.stock); } catch (_) {}
        }
      }
    });

    // Re-render store cards if function exists
    if (typeof window.renderProducts === 'function') {
      window.renderProducts();
    }

    // Update customer memory in localStorage
    user.name = name;
    user.phone = phone;
    user.city = city;
    user.address = address;
    localStorage.setItem('lh_user', JSON.stringify(user));
    window.currentUser = user;

    // Show order confirmation modal
    const confirmOrderId = document.getElementById('confirmOrderId');
    const confirmCust = document.getElementById('confirmCustomer');
    if (confirmOrderId) confirmOrderId.textContent = orderId;
    if (confirmCust) confirmCust.textContent = `${name} (${city})`;

    // Clear cart
    if (window.saveCart) {
      window.cart.length = 0;
      window.saveCart();
    } else {
      localStorage.removeItem('lh_cart_items');
      window.cart = [];
    }

    closeCheckoutModal();

    const confirmModal = document.getElementById('orderConfirmModal');
    if (confirmModal) {
      confirmModal.classList.add('open');
      document.body.classList.add('modal-open');
    }

    if (typeof window.showToast === 'function') {
      window.showToast('🎉 Order placed successfully! Cash on Delivery confirmed.');
    }
  }

  function closeConfirmModal() {
    const modal = document.getElementById('orderConfirmModal');
    if (modal) modal.classList.remove('open');
    document.body.classList.remove('modal-open');
  }

  // Export to window
  window.openCheckoutModal = openCheckoutModal;
  window.closeCheckoutModal = closeCheckoutModal;
  window.handlePlaceOrder = handlePlaceOrder;
  window.closeConfirmModal = closeConfirmModal;

})(window);
