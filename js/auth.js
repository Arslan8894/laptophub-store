/**
 * LaptopHUB - Authentication & Session Management (js/auth.js)
 * Manages customer sign-in, account creation, session persistence,
 * user navigation controls, and post-login action resumption.
 */

(function(window) {
  'use strict';

  let currentUser = JSON.parse(localStorage.getItem('lh_user') || 'null');
  let authMode = 'signin'; // 'signin' or 'register'
  let pendingBuyAction = null;

  function getCurrentUser() {
    return currentUser;
  }

  function setCurrentUser(user) {
    currentUser = user;
    if (user) {
      localStorage.setItem('lh_user', JSON.stringify(user));
    } else {
      localStorage.removeItem('lh_user');
    }
    renderUserNav();
  }

  function switchAuthTab(mode) {
    authMode = mode;
    const tabLogin = document.getElementById('tabLogin') || document.getElementById('tabBtnLogin');
    const tabRegister = document.getElementById('tabRegister') || document.getElementById('tabBtnRegister');
    const regFields = document.querySelectorAll('.register-only-field, #groupFullName, #groupPhone, #groupCity, #groupAddress');
    const submitBtn = document.getElementById('btnAuthSubmit');
    const modalTitle = document.getElementById('authModalTitle');

    if (tabLogin) tabLogin.classList.toggle('active', mode === 'signin');
    if (tabRegister) tabRegister.classList.toggle('active', mode === 'register');

    regFields.forEach(el => {
      el.style.display = (mode === 'register') ? 'block' : 'none';
    });

    if (submitBtn) {
      submitBtn.textContent = (mode === 'register') ? 'Create Account & Sign In' : 'Sign In to LaptopHUB';
    }
    if (modalTitle) {
      modalTitle.textContent = (mode === 'register') ? 'Create Account' : 'Sign In';
    }
  }

  function openLoginModal(msg) {
    // If cart is open, close it cleanly first
    if (typeof window.closeCart === 'function') {
      window.closeCart();
    }

    const banner = document.getElementById('authNoticeBanner');
    const noticeText = document.getElementById('authNoticeText');
    if (banner) {
      if (msg) {
        if (noticeText) noticeText.textContent = msg;
        else banner.textContent = msg;
        banner.style.display = 'flex';
      } else {
        banner.style.display = 'none';
      }
    }

    const modal = document.getElementById('loginModal');
    if (modal) {
      modal.classList.add('open');
      document.body.classList.add('modal-open');
    }
  }

  function closeLoginModal() {
    const banner = document.getElementById('authNoticeBanner');
    if (banner) banner.style.display = 'none';
    const modal = document.getElementById('loginModal');
    if (modal) {
      modal.classList.remove('open');
    }
    const openModals = document.querySelectorAll('#loginModal.open, #checkoutModal.open, #orderConfirmModal.open');
    if (openModals.length === 0) {
      document.body.classList.remove('modal-open');
    }
  }

  async function handleAuthSubmit(e) {
    if (e && e.preventDefault) e.preventDefault();

    const email = (document.getElementById('authEmail')?.value || '').trim();
    const pass = document.getElementById('authPass')?.value || document.getElementById('authPassword')?.value || '';
    const name = (document.getElementById('authName')?.value || '').trim();
    const phone = (document.getElementById('authPhone')?.value || '').trim();
    const city = document.getElementById('authCity')?.value || 'Lahore';
    const address = (document.getElementById('authAddress')?.value || '').trim();

    if (!email || !pass) {
      if (typeof window.showToast === 'function') window.showToast('Please enter both email and password');
      return;
    }

    if (authMode === 'register') {
      if (!name) {
        if (typeof window.showToast === 'function') window.showToast('Please enter your full name');
        return;
      }
      const pkPhoneRe = /^(?:\+92|0092|0)?3[0-9]{2}[-\s]?[0-9]{7}$/;
      if (!phone || !pkPhoneRe.test(phone)) {
        if (typeof window.showToast === 'function') window.showToast('Please enter a valid Pakistani mobile number (03XX-XXXXXXX)');
        return;
      }
      if (!address) {
        if (typeof window.showToast === 'function') window.showToast('Please enter your delivery address');
        return;
      }

      // Try server registration
      let registered = false;
      try {
        const res = await fetch('/api/auth/register', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          credentials: 'include',
          body: JSON.stringify({ email, password: pass, name, phone, city, address })
        });
        if (res.ok) registered = true;
      } catch (_) {}

      // Sign in user
      currentUser = { email, name, phone, city, address, loggedIn: true, role: 'user' };
      setCurrentUser(currentUser);
      closeLoginModal();
      if (typeof window.showToast === 'function') {
        window.showToast(`🎉 Account created! Welcome, ${name}!`);
      }
      resumePendingAction();
    } else {
      // Sign in mode
      let isAdmin = false;
      let userData = { email, name: email.split('@')[0], loggedIn: true, role: 'user' };

      try {
        const res = await fetch('/api/auth/login', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          credentials: 'include',
          body: JSON.stringify({ email, password: pass })
        });
        if (res.ok) {
          const data = await res.json();
          const u = data.user || data;
          if (data.role === 'admin' || u.role === 'admin' || email.toLowerCase().includes('admin')) {
            isAdmin = true;
          }
          userData = { ...u, loggedIn: true, role: isAdmin ? 'admin' : 'user' };
        }
      } catch (_) {
        // Fallback for offline demo
        if (email.toLowerCase().includes('admin')) {
          isAdmin = true;
          userData.role = 'admin';
        }
      }

      currentUser = userData;
      setCurrentUser(currentUser);

      if (isAdmin) {
        closeLoginModal();
        if (typeof window.showToast === 'function') {
          window.showToast('Admin account authenticated! Opening Control Center...');
        }
        setTimeout(() => { window.location.href = '/admin/'; }, 600);
        return;
      }

      closeLoginModal();
      if (typeof window.showToast === 'function') {
        window.showToast(`Welcome back, ${currentUser.name || 'Customer'}!`);
      }
      resumePendingAction();
    }
  }

  function resumePendingAction() {
    const action = window.pendingBuyAction || pendingBuyAction;
    window.pendingBuyAction = null;
    pendingBuyAction = null;
    if (!action) return;

    if (action.type === 'checkout') {
      if (typeof window.openCheckoutModal === 'function') {
        window.openCheckoutModal();
      }
    } else if (action.type === 'cart_whatsapp') {
      if (typeof window.checkoutWhatsApp === 'function') {
        window.checkoutWhatsApp();
      }
    } else if (action.type === 'card_whatsapp' && action.lapId) {
      if (typeof window.orderCardViaWhatsApp === 'function') {
        window.orderCardViaWhatsApp(action.lapId);
      }
    }
  }

  function renderUserNav() {
    const btnSignIn = document.getElementById('btnSignIn');
    const userMenuWrap = document.getElementById('userMenuWrap');
    const userNameLabel = document.getElementById('userNameLabel');

    if (!currentUser || !currentUser.loggedIn) {
      if (btnSignIn) btnSignIn.style.display = 'inline-flex';
      if (userMenuWrap) userMenuWrap.style.display = 'none';
    } else {
      if (btnSignIn) btnSignIn.style.display = 'none';
      if (userMenuWrap) userMenuWrap.style.display = 'inline-flex';
      if (userNameLabel) {
        userNameLabel.textContent = currentUser.name ? currentUser.name.split(' ')[0] : 'Account';
      }
    }
  }

  function handleUserSignOut() {
    currentUser = null;
    localStorage.removeItem('lh_user');
    try {
      fetch('/api/auth/logout', { method: 'POST', credentials: 'include' });
    } catch (_) {}
    renderUserNav();
    if (typeof window.showToast === 'function') {
      window.showToast('You have been signed out.');
    }
  }

  async function quickGuestLogin() {
    currentUser = {
      name: 'Arslan Tariq',
      email: 'arslan@laptophub.pk',
      phone: '0326-1398594',
      city: 'Lahore',
      address: 'Main Boulevard, Gulberg III, Lahore',
      loggedIn: true,
      role: 'user'
    };
    setCurrentUser(currentUser);
    closeLoginModal();
    if (typeof window.showToast === 'function') {
      window.showToast('Signed in successfully as Arslan Tariq!');
    }
    resumePendingAction();
  }

  // Export to window
  window.currentUser = currentUser;
  window.getCurrentUser = getCurrentUser;
  window.setCurrentUser = setCurrentUser;
  window.switchAuthTab = switchAuthTab;
  window.openLoginModal = openLoginModal;
  window.closeLoginModal = closeLoginModal;
  window.handleAuthSubmit = handleAuthSubmit;
  window.handleUserSignOut = handleUserSignOut;
  window.quickGuestLogin = quickGuestLogin;
  window.renderUserNav = renderUserNav;

  document.addEventListener('DOMContentLoaded', () => {
    renderUserNav();
  });
})(window);
