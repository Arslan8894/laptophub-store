/**
 * LaptopHUB - Hover-to-Expand Card System (js/hover-expand.js)
 * Implements 2-second deliberate hover detection, FLIP morph animation,
 * full specifications preview, stock verification, and smooth dismissal.
 */

(function() {
  'use strict';

  let hoverTimer = null;
  let activeCard = null;
  let originCardRect = null;
  let isOverlayOpen = false;
  let lastFocusedElement = null;

  // Reduced motion preference
  const prefersReducedMotion = () => window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const isFinePointer = () => window.matchMedia && window.matchMedia('(hover: hover) and (pointer: fine)').matches;

  // ── 1. MODAL DOM INJECTION ──────────────────────────────────────────────────
  function ensureOverlayExists() {
    let overlay = document.getElementById('hoverExpandOverlay');
    if (overlay) return overlay;

    overlay = document.createElement('div');
    overlay.id = 'hoverExpandOverlay';
    overlay.className = 'hover-expand-overlay';
    overlay.setAttribute('role', 'dialog');
    overlay.setAttribute('aria-modal', 'true');
    overlay.setAttribute('aria-label', 'Laptop Quick Preview');

    overlay.innerHTML = `
      <div class="hover-expand-card" id="hoverExpandCard">
        <button class="hover-expand-close" id="hoverExpandCloseBtn" aria-label="Close preview">✕</button>
        
        <!-- Left: Image & Badges -->
        <div class="hover-expand-gallery" id="hexGallery">
          <div class="hover-expand-badges" id="hexBadges"></div>
          <div class="hover-expand-img-wrap" id="hexImgWrap">
            <img src="" alt="" class="hover-expand-img" id="hexImg" loading="lazy">
          </div>
        </div>

        <!-- Right: Specifications & Actions -->
        <div class="hover-expand-details">
          <div>
            <div class="hover-expand-brand" id="hexBrand"></div>
            <h2 class="hover-expand-title" id="hexTitle"></h2>
          </div>

          <div class="hover-expand-rating">
            <span class="hover-expand-stars">★★★★★</span>
            <span style="font-weight:700;color:var(--heading,#fff);font-size:0.85rem">4.8</span>
            <span style="color:var(--muted,#94a3b8);font-size:0.75rem" id="hexReviewsCount">(24 Verified Reviews)</span>
          </div>

          <!-- Price & Stock -->
          <div class="hover-expand-price-box">
            <div>
              <div class="hex-price-label">Cash Price</div>
              <div class="hex-price-val" id="hexPrice"></div>
            </div>
            <div id="hexStockBadge"></div>
          </div>

          <!-- Full Specifications Grid -->
          <div class="hover-expand-specs-grid" id="hexSpecsGrid"></div>

          <!-- Actions -->
          <div class="hover-expand-actions">
            <div class="hex-btn-row">
              <button type="button" class="hex-btn hex-btn-primary" id="hexBtnAddToCart">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><circle cx="9" cy="21" r="1"/><circle cx="20" cy="21" r="1"/><path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"/></svg>
                <span>Add to Cart</span>
              </button>
              <button type="button" class="hex-btn hex-btn-wa" id="hexBtnWhatsApp">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>
                <span>WhatsApp</span>
              </button>
            </div>
            <a href="#" class="hex-btn hex-btn-outline" id="hexBtnDetails">
              <span>View Full Specs, Benchmarks & Upgrades →</span>
            </a>
            <div class="hex-trust-bar">
              <span>🛡️ 1-Year Local Hardware Warranty</span>
              <span>·</span>
              <span>💵 COD Across Pakistan</span>
              <span>·</span>
              <span>🔄 7-Day Checking</span>
            </div>
          </div>
        </div>
      </div>
    `;

    document.body.appendChild(overlay);

    // Event listeners
    document.getElementById('hoverExpandCloseBtn').addEventListener('click', closeExpandedCard);
    overlay.addEventListener('click', (e) => {
      if (e.target === overlay) closeExpandedCard();
    });

    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && isOverlayOpen) {
        e.preventDefault();
        closeExpandedCard();
      }
    });

    return overlay;
  }

  // ── 2. CARD HOVER ATTACHMENT ────────────────────────────────────────────────
  function attachHoverListeners() {
    const cards = document.querySelectorAll('.pcard');
    cards.forEach(card => {
      if (card._hoverInit) return;
      card._hoverInit = true;

      // Inject hover progress ring
      let progress = card.querySelector('.pcard-hover-progress');
      if (!progress) {
        progress = document.createElement('div');
        progress.className = 'pcard-hover-progress';
        progress.innerHTML = `
          <svg width="20" height="20" viewBox="0 0 24 24">
            <circle class="bg" cx="12" cy="12" r="9" fill="none" stroke-width="2.5"></circle>
            <circle class="meter" cx="12" cy="12" r="9" fill="none" stroke-width="2.5"></circle>
          </svg>
        `;
        card.appendChild(progress);
      }

      // Mouseenter: start 2000ms timer on desktop
      card.addEventListener('pointerenter', (e) => {
        if (e.pointerType !== 'mouse') return;
        if (!isFinePointer()) return;
        if (isOverlayOpen) return;

        clearHoverTimer();
        activeCard = card;
        card.classList.add('is-hovering');

        // Extract ID
        const onclickAttr = card.getAttribute('onclick') || '';
        const match = onclickAttr.match(/openProductPage\((\d+)/);
        const lapId = match ? parseInt(match[1], 10) : null;
        if (!lapId) return;

        hoverTimer = setTimeout(() => {
          card.classList.remove('is-hovering');
          openExpandedCard(lapId, card);
        }, 2000);
      });

      // Mouseleave: cancel immediately!
      card.addEventListener('pointerleave', () => {
        clearHoverTimer();
      });
    });
  }

  function clearHoverTimer() {
    if (hoverTimer) {
      clearTimeout(hoverTimer);
      hoverTimer = null;
    }
    if (activeCard) {
      activeCard.classList.remove('is-hovering');
      activeCard = null;
    }
  }

  // Fast scroll cancellation: cancel hover immediately if user scrolls
  window.addEventListener('scroll', () => {
    clearHoverTimer();
  }, { passive: true });

  window.addEventListener('wheel', () => {
    clearHoverTimer();
  }, { passive: true });

  // ── 3. OPEN EXPANDED OVERLAY WITH FLIP ANIMATION ────────────────────────────
  function openExpandedCard(lapId, cardElement) {
    const inv = window.inventory || (typeof LAPTOPS_INVENTORY !== 'undefined' ? LAPTOPS_INVENTORY : []);
    const lap = inv.find(l => l.id == lapId);
    if (!lap) return;

    lastFocusedElement = cardElement || document.activeElement;
    const overlay = ensureOverlayExists();
    const modal = document.getElementById('hoverExpandCard');

    // Populate data
    populateModalData(lap);

    // Record origin rect
    originCardRect = cardElement ? cardElement.getBoundingClientRect() : null;

    // Display overlay
    overlay.classList.add('active');
    document.body.style.overflow = 'hidden';
    isOverlayOpen = true;

    if (!prefersReducedMotion() && originCardRect) {
      const targetRect = modal.getBoundingClientRect();
      const scaleX = originCardRect.width / targetRect.width;
      const scaleY = originCardRect.height / targetRect.height;
      const translateX = (originCardRect.left + originCardRect.width / 2) - (targetRect.left + targetRect.width / 2);
      const translateY = (originCardRect.top + originCardRect.height / 2) - (targetRect.top + targetRect.height / 2);

      // Invert
      modal.style.transition = 'none';
      modal.style.transform = `translate3d(${translateX}px, ${translateY}px, 0) scale(${scaleX}, ${scaleY})`;
      modal.style.borderRadius = '16px';

      // Play
      requestAnimationFrame(() => {
        modal.style.transition = 'transform 0.38s cubic-bezier(0.16, 1, 0.3, 1), border-radius 0.38s cubic-bezier(0.16, 1, 0.3, 1)';
        modal.style.transform = 'none';
        modal.style.borderRadius = '24px';
      });
    }

    // Accessibility focus
    const closeBtn = document.getElementById('hoverExpandCloseBtn');
    if (closeBtn) closeBtn.focus();
  }

  // ── 4. POPULATE MODAL DATA ──────────────────────────────────────────────────
  function populateModalData(lap) {
    const isOutOfStock = lap.stock !== undefined && lap.stock <= 0;
    const isLowStock = lap.stock !== undefined && lap.stock > 0 && lap.stock <= 2;
    const stockCount = lap.stock !== undefined ? lap.stock : 1;

    // Brand and Title
    document.getElementById('hexBrand').textContent = (lap.brandName || lap.brand || 'LAPTOP').toUpperCase();
    document.getElementById('hexTitle').textContent = lap.name;
    document.getElementById('hexPrice').textContent = lap.priceFormatted || `Rs ${Number(lap.price || 0).toLocaleString('en-PK')}`;

    // Badges
    const badgesContainer = document.getElementById('hexBadges');
    badgesContainer.innerHTML = '';

    if (lap.badge) {
      const b = document.createElement('span');
      b.className = 'hex-badge';
      b.style.background = 'var(--blue, #4c7cff)';
      b.style.color = '#ffffff';
      b.textContent = lap.badge;
      badgesContainer.appendChild(b);
    }

    const cond = document.createElement('span');
    cond.className = 'hex-badge hex-badge-cond';
    cond.textContent = lap.condition ? lap.condition.split('·')[0].trim() : 'Like New (10/10)';
    badgesContainer.appendChild(cond);

    // Stock Badge
    const stockBadge = document.getElementById('hexStockBadge');
    if (isOutOfStock) {
      stockBadge.innerHTML = `<span class="hex-badge hex-badge-stock-out">✕ Out of Stock</span>`;
    } else if (isLowStock) {
      stockBadge.innerHTML = `<span class="hex-badge hex-badge-stock-low">⚡ Only ${stockCount} Left</span>`;
    } else {
      stockBadge.innerHTML = `<span class="hex-badge hex-badge-stock-in">✓ In Stock (${stockCount})</span>`;
    }

    // Image Setup with Blending Tint
    const imgEl = document.getElementById('hexImg');
    const isWhite = lap.bgTone === 'white';
    imgEl.src = (isWhite && lap.processedImg) ? lap.processedImg : lap.img;
    imgEl.alt = lap.name;
    imgEl.className = `hover-expand-img ${isWhite ? 'blend-cutout' : 'blend-original'}`;

    const gallery = document.getElementById('hexGallery');
    if (lap.tintColor) {
      gallery.style.background = `radial-gradient(circle at center, ${lap.tintColor} 0%, transparent 70%)`;
    }

    // Specs Grid
    const specsGrid = document.getElementById('hexSpecsGrid');
    const exactCpu = lap.exactCpu || lap.fullSpecs?.performance?.processor || lap.cpu;
    const ramType = lap.ramType || lap.fullSpecs?.memoryStorage?.ramType || 'DDR4';
    const storType = lap.storageType || lap.fullSpecs?.memoryStorage?.storageType || 'NVMe PCIe SSD';
    const storText = (lap.storage >= 1000 ? (lap.storage/1000) + ' TB' : lap.storage + ' GB');
    const display = lap.display || '14.0" FHD IPS Display';
    const gpu = lap.gpu || 'Integrated Graphics';
    const condition = lap.condition || 'Like New (10/10) · Grade A+';

    specsGrid.innerHTML = `
      <div class="hex-spec-item">
        <span class="hex-spec-k">⚡ Processor (CPU)</span>
        <span class="hex-spec-v">${escapeHtml(exactCpu)}</span>
      </div>
      <div class="hex-spec-item">
        <span class="hex-spec-k">🧠 RAM & Architecture</span>
        <span class="hex-spec-v">${lap.ram} GB ${escapeHtml(ramType)}</span>
      </div>
      <div class="hex-spec-item">
        <span class="hex-spec-k">💾 High-Speed Storage</span>
        <span class="hex-spec-v">${storText} ${escapeHtml(storType)}</span>
      </div>
      <div class="hex-spec-item">
        <span class="hex-spec-k">🎮 Graphics (GPU)</span>
        <span class="hex-spec-v">${escapeHtml(gpu)}</span>
      </div>
      <div class="hex-spec-item">
        <span class="hex-spec-k">🖥️ Display Panel</span>
        <span class="hex-spec-v">${escapeHtml(display)}</span>
      </div>
      <div class="hex-spec-item">
        <span class="hex-spec-k">✨ Certified Condition</span>
        <span class="hex-spec-v">${escapeHtml(condition)}</span>
      </div>
    `;

    // Actions
    const addBtn = document.getElementById('hexBtnAddToCart');
    if (isOutOfStock) {
      addBtn.disabled = true;
      addBtn.innerHTML = '<span>Out of Stock</span>';
    } else {
      addBtn.disabled = false;
      addBtn.innerHTML = `
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><circle cx="9" cy="21" r="1"/><circle cx="20" cy="21" r="1"/><path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"/></svg>
        <span>Add to Cart</span>
      `;
      addBtn.onclick = () => {
        closeExpandedCard();
        if (typeof openProductPage === 'function') {
          openProductPage(lap.id);
        } else {
          window.location.href = `product.html?id=${lap.id}`;
        }
      };
    }

    // WhatsApp Action
    const waBtn = document.getElementById('hexBtnWhatsApp');
    waBtn.onclick = () => {
      const msg = encodeURIComponent(`Hi LaptopHUB! I am interested in purchasing ${lap.name} (${lap.priceFormatted || 'Rs ' + lap.price}). Please confirm availability!`);
      window.open(`https://wa.me/923261398594?text=${msg}`, '_blank');
    };

    // Details Link
    const detailsBtn = document.getElementById('hexBtnDetails');
    detailsBtn.href = `product.html?id=${lap.id}`;
    detailsBtn.onclick = () => {
      closeExpandedCard();
    };
  }

  // ── 5. CLOSE EXPANDED OVERLAY ───────────────────────────────────────────────
  function closeExpandedCard() {
    const overlay = document.getElementById('hoverExpandOverlay');
    const modal = document.getElementById('hoverExpandCard');
    if (!overlay || !isOverlayOpen) return;

    if (!prefersReducedMotion() && originCardRect && modal) {
      const targetRect = modal.getBoundingClientRect();
      const scaleX = originCardRect.width / targetRect.width;
      const scaleY = originCardRect.height / targetRect.height;
      const translateX = (originCardRect.left + originCardRect.width / 2) - (targetRect.left + targetRect.width / 2);
      const translateY = (originCardRect.top + originCardRect.height / 2) - (targetRect.top + targetRect.height / 2);

      modal.style.transition = 'transform 0.28s cubic-bezier(0.16, 1, 0.3, 1), border-radius 0.28s ease';
      modal.style.transform = `translate3d(${translateX}px, ${translateY}px, 0) scale(${scaleX}, ${scaleY})`;
      modal.style.borderRadius = '16px';
      overlay.style.transition = 'opacity 0.28s ease, visibility 0.28s ease';
      overlay.classList.remove('active');

      setTimeout(() => {
        cleanupClose();
      }, 290);
    } else {
      overlay.classList.remove('active');
      cleanupClose();
    }
  }

  function cleanupClose() {
    const modal = document.getElementById('hoverExpandCard');
    if (modal) {
      modal.style.transform = 'none';
      modal.style.transition = '';
    }
    document.body.style.overflow = '';
    isOverlayOpen = false;
    originCardRect = null;

    if (lastFocusedElement && typeof lastFocusedElement.focus === 'function') {
      lastFocusedElement.focus();
    }
  }

  function escapeHtml(str) {
    if (!str) return '';
    return String(str)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#039;');
  }

  // ── 6. INITIALIZATION & OBSERVERS ──────────────────────────────────────────
  function initHoverExpand() {
    attachHoverListeners();

    // Re-attach whenever product grid is updated
    const grid = document.getElementById('productGrid');
    if (grid && window.MutationObserver) {
      const observer = new MutationObserver(() => {
        attachHoverListeners();
      });
      observer.observe(grid, { childList: true });
    }
  }

  // Export functions to window
  window.openExpandedCard = openExpandedCard;
  window.closeExpandedCard = closeExpandedCard;
  window.initHoverExpand = initHoverExpand;

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initHoverExpand);
  } else {
    initHoverExpand();
  }
})();
