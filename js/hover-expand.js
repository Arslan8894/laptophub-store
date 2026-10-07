/**
 * LaptopHUB - Upgraded Hover-to-Expand Card System (js/hover-expand.js)
 * Fully Modular & Independent:
 * - Desktop only: 1.0 second deliberate hover trigger
 * - Cancel if cursor leaves before 1s, never loop/re-trigger while open
 * - Auto-photo slideshow at top:
 *   - Cycles every 2.0s with smooth fade
 *   - Dot indicators & manual Prev/Next arrows
 *   - Pauses on user interaction, resumes automatically
 *   - Static 1-photo mode if only 1 photo available
 *   - Complete timer cleanup on card close (zero memory leaks)
 * - Internal specs ONLY (Exact CPU, Gen, RAM + DDR, Storage + drive type/speed, Display, GPU, Battery, Ports, Weight, Condition)
 * - Working buttons: Add to Cart, Cash on Delivery, WhatsApp Order, View Full Details
 * - Zero horizontal overflow, vertical-only scroll with max-height 85vh
 */

(function(window) {
  'use strict';

  const HOVER_DELAY_MS = 1000; // 1.0 second deliberate hover
  const SLIDESHOW_INTERVAL_MS = 2000; // 2.0s photo transition

  let hoverTimer = null;
  let activeCard = null;
  let originCardRect = null;
  let isOverlayOpen = false;
  let closeTimeout = null;

  // Slideshow state
  let currentLapPhotos = [];
  let currentSlideIndex = 0;
  let slideshowTimer = null;
  let slideshowResumeTimer = null;
  let isInteractingSlideshow = false;

  const isFineDesktop = () => {
    return window.matchMedia &&
           window.matchMedia('(hover: hover) and (pointer: fine)').matches &&
           !('ontouchstart' in window) &&
           (!navigator.maxTouchPoints || navigator.maxTouchPoints === 0);
  };

  const prefersReducedMotion = () => {
    return window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  };

  // ── 1. MODAL DOM INJECTION ──────────────────────────────────────────────────
  function ensureOverlayExists() {
    let overlay = document.getElementById('hoverExpandOverlay');
    if (overlay) return overlay;

    overlay = document.createElement('div');
    overlay.id = 'hoverExpandOverlay';
    overlay.className = 'hover-expand-overlay';
    overlay.setAttribute('role', 'dialog');
    overlay.setAttribute('aria-modal', 'true');
    overlay.setAttribute('aria-label', 'Laptop Full Specifications Preview');

    overlay.innerHTML = `
      <div class="hover-expand-card" id="hoverExpandCard">
        <!-- Close Button (Fixed at top right) -->
        <button class="hover-expand-close" id="hoverExpandCloseBtn" aria-label="Close preview" type="button">✕</button>

        <!-- TOP: Photo Slideshow Container -->
        <div class="hex-slideshow-container" id="hexSlideshowContainer">
          <!-- Top Badges -->
          <div class="hex-top-badges" id="hexTopBadges"></div>

          <!-- Slide Track -->
          <div class="hex-slides-track" id="hexSlidesTrack"></div>

          <!-- Prev/Next Navigation Arrows -->
          <button type="button" class="hex-nav-arrow hex-arrow-prev" id="hexArrowPrev" aria-label="Previous image">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="15 18 9 12 15 6"></polyline></svg>
          </button>
          <button type="button" class="hex-nav-arrow hex-arrow-next" id="hexArrowNext" aria-label="Next image">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="9 18 15 12 9 6"></polyline></svg>
          </button>

          <!-- Dot Indicators -->
          <div class="hex-dots" id="hexDots" role="tablist"></div>
        </div>

        <!-- BOTTOM: Internal Specs & Action Buttons -->
        <div class="hover-expand-content">
          <!-- Header Meta -->
          <div class="hex-header-meta">
            <div class="hex-brand" id="hexBrand"></div>
            <h2 class="hex-title" id="hexTitle"></h2>
            
            <div class="hex-meta-row">
              <span class="hex-stars">★★★★★</span>
              <span style="font-weight:700;color:var(--heading,#fff);font-size:0.85rem">4.8</span>
              <span class="hex-reviews-count" id="hexReviewsCount">(24 Verified Reviews)</span>
              <span style="margin-left:auto" id="hexStockBadge"></span>
            </div>

            <div class="hex-price-wrap">
              <span class="hex-price-val" id="hexPrice"></span>
              <span class="hex-price-label">Cash Price</span>
            </div>
          </div>

          <!-- Internal Specs Grid (Internal Specs ONLY) -->
          <div class="hover-expand-specs-grid" id="hexSpecsGrid">
            <!-- 10 Internal Specs injected dynamically -->
          </div>

          <!-- Action Buttons -->
          <div class="hover-expand-actions">
            <div class="hex-btn-grid">
              <button type="button" class="hex-btn hex-btn-cart" id="hexBtnAddToCart">
                <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><circle cx="9" cy="21" r="1"/><circle cx="20" cy="21" r="1"/><path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"/></svg>
                <span>Add to Cart</span>
              </button>
              <button type="button" class="hex-btn hex-btn-cod" id="hexBtnCod">
                <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><rect x="1" y="4" width="22" height="16" rx="2" ry="2"/><line x1="1" y1="10" x2="23" y2="10"/></svg>
                <span>Cash on Delivery</span>
              </button>
              <button type="button" class="hex-btn hex-btn-wa" id="hexBtnWhatsApp">
                <svg width="15" height="15" viewBox="0 0 24 24" fill="currentColor"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>
                <span>WhatsApp</span>
              </button>
            </div>
            <a href="#" class="hex-btn-details" id="hexBtnDetails">
              <span>View Full Details & Custom Upgrades →</span>
            </a>
          </div>
        </div>
      </div>
    `;

    document.body.appendChild(overlay);

    // Event Listeners for Dismissal
    document.getElementById('hoverExpandCloseBtn').addEventListener('click', (e) => {
      e.stopPropagation();
      closeExpandedCard();
    });

    overlay.addEventListener('click', (e) => {
      // Click outside card closes overlay
      if (e.target === overlay) {
        closeExpandedCard();
      }
    });

    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && isOverlayOpen) {
        e.preventDefault();
        closeExpandedCard();
      }
    });

    // Close on mouse leaving the overlay card
    const cardEl = document.getElementById('hoverExpandCard');
    cardEl.addEventListener('mouseleave', () => {
      if (!isOverlayOpen) return;
      closeTimeout = setTimeout(() => {
        closeExpandedCard();
      }, 250);
    });

    cardEl.addEventListener('mouseenter', () => {
      if (closeTimeout) {
        clearTimeout(closeTimeout);
        closeTimeout = null;
      }
    });

    // Slideshow control button interactions
    const prevBtn = document.getElementById('hexArrowPrev');
    const nextBtn = document.getElementById('hexArrowNext');

    prevBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      navigateSlideshow(-1);
      pauseAndResumeSlideshow();
    });

    nextBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      navigateSlideshow(1);
      pauseAndResumeSlideshow();
    });

    // Pause on hovering the slideshow
    const slideBox = document.getElementById('hexSlideshowContainer');
    slideBox.addEventListener('mouseenter', () => {
      isInteractingSlideshow = true;
      stopSlideshowTimer();
    });

    slideBox.addEventListener('mouseleave', () => {
      isInteractingSlideshow = false;
      if (isOverlayOpen && currentLapPhotos.length > 1) {
        startSlideshowTimer();
      }
    });

    return overlay;
  }

  // ── 2. CARD HOVER DETECTION (DESKTOP ONLY, 1.0 SECOND DELIBERATE HOVER) ────
  function attachHoverListeners() {
    if (!isFineDesktop()) return;

    const cards = document.querySelectorAll('.pcard');
    cards.forEach(card => {
      if (card._hexAttached) return;
      card._hexAttached = true;

      // Ensure progress ring
      let progress = card.querySelector('.pcard-hover-progress');
      if (!progress) {
        progress = document.createElement('div');
        progress.className = 'pcard-hover-progress';
        progress.setAttribute('aria-hidden', 'true');
        progress.innerHTML = `
          <svg width="22" height="22" viewBox="0 0 24 24">
            <circle class="bg" cx="12" cy="12" r="9" fill="none" stroke-width="2.5"></circle>
            <circle class="meter" cx="12" cy="12" r="9" fill="none" stroke-width="2.5"></circle>
          </svg>
        `;
        card.appendChild(progress);
      }

      // Pointer enter: start 1.0s timer
      card.addEventListener('pointerenter', (e) => {
        if (e.pointerType !== 'mouse') return;
        if (!isFineDesktop()) return;
        if (isOverlayOpen) return; // Never loop or re-trigger while open

        clearHoverTimer();
        activeCard = card;
        card.classList.add('is-hovering');

        // Extract ID
        const lapId = card.dataset.laptopId || card.getAttribute('data-laptop-id') || (function() {
          const match = (card.getAttribute('onclick') || '').match(/\((\d+)/);
          return match ? match[1] : null;
        })();
        if (!lapId) return;

        hoverTimer = setTimeout(() => {
          card.classList.remove('is-hovering');
          openExpandedCard(lapId, card);
        }, HOVER_DELAY_MS);
      });

      // Pointer leave: cancel timer immediately
      card.addEventListener('pointerleave', () => {
        clearHoverTimer();
      });

      // Click on card: cancel timer immediately
      card.addEventListener('click', () => {
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

  // Cancel immediately on scroll or wheel
  window.addEventListener('scroll', clearHoverTimer, { passive: true });
  window.addEventListener('wheel', clearHoverTimer, { passive: true });

  // ── 3. OPEN EXPANDED CARD ──────────────────────────────────────────────────
  function openExpandedCard(lapId, cardElement) {
    if (!isFineDesktop()) return;

    const inv = window.inventory || (typeof LAPTOPS_INVENTORY !== 'undefined' ? LAPTOPS_INVENTORY : []);
    const lap = inv.find(l => String(l.id) === String(lapId));
    if (!lap) return;

    const overlay = ensureOverlayExists();
    const modal = document.getElementById('hoverExpandCard');
    if (!modal) return;

    // Reset card scroll position to top
    modal.scrollTop = 0;

    // Populate Data & Slideshow
    populateModalData(lap);

    originCardRect = cardElement ? cardElement.getBoundingClientRect() : null;

    overlay.classList.add('active');
    isOverlayOpen = true;

    // Smooth entrance animation
    if (!prefersReducedMotion() && originCardRect) {
      const targetRect = modal.getBoundingClientRect();
      const scaleX = Math.min(1, originCardRect.width / Math.max(targetRect.width, 300));
      const scaleY = Math.min(1, originCardRect.height / Math.max(targetRect.height, 400));
      const translateX = (originCardRect.left + originCardRect.width / 2) - (targetRect.left + targetRect.width / 2);
      const translateY = (originCardRect.top + originCardRect.height / 2) - (targetRect.top + targetRect.height / 2);

      modal.style.transition = 'none';
      modal.style.transform = `translate3d(${translateX.toFixed(1)}px, ${translateY.toFixed(1)}px, 0) scale(${scaleX.toFixed(4)}, ${scaleY.toFixed(4)})`;
      modal.style.opacity = '0.9';

      requestAnimationFrame(() => {
        requestAnimationFrame(() => {
          modal.style.transition = 'transform 0.38s cubic-bezier(0.16, 1, 0.3, 1), opacity 0.28s ease';
          modal.style.transform = 'translate3d(0, 0, 0) scale(1, 1)';
          modal.style.opacity = '1';
        });
      });
    } else {
      modal.style.transform = 'none';
      modal.style.opacity = '1';
    }
  }

  // ── 4. POPULATE MODAL DATA & SLIDESHOW ──────────────────────────────────────
  function populateModalData(lap) {
    const isOutOfStock = lap.stock !== undefined && lap.stock <= 0;
    const isLowStock = lap.stock !== undefined && lap.stock > 0 && lap.stock <= 2;
    const stockCount = lap.stock !== undefined ? lap.stock : 1;

    // Header info
    document.getElementById('hexBrand').textContent = (lap.brandName || lap.brand || 'LAPTOP').toUpperCase();
    document.getElementById('hexTitle').textContent = lap.name;
    document.getElementById('hexPrice').textContent = lap.priceFormatted || `Rs ${Number(lap.price || 0).toLocaleString('en-PK')}`;

    // Badges inside slideshow
    const badgesContainer = document.getElementById('hexTopBadges');
    badgesContainer.innerHTML = '';
    if (lap.badge) {
      const b = document.createElement('span');
      b.className = 'hex-badge hex-badge-custom';
      b.textContent = lap.badge;
      badgesContainer.appendChild(b);
    }
    const condBadge = document.createElement('span');
    condBadge.className = 'hex-badge hex-badge-cond';
    condBadge.textContent = lap.condition ? lap.condition.split('·')[0].trim() : 'Like New (10/10)';
    badgesContainer.appendChild(condBadge);

    // Stock Badge
    const stockEl = document.getElementById('hexStockBadge');
    if (isOutOfStock) {
      stockEl.innerHTML = `<span class="hex-badge hex-badge-stock-out">✕ Out of Stock</span>`;
    } else if (isLowStock) {
      stockEl.innerHTML = `<span class="hex-badge hex-badge-stock-low">⚡ Only ${stockCount} Left</span>`;
    } else {
      stockEl.innerHTML = `<span class="hex-badge hex-badge-stock-in">✓ In Stock (${stockCount})</span>`;
    }

    // ── PHOTO SLIDESHOW SETUP ────────────────────────────────────────────────
    setupPhotoSlideshow(lap);

    // ── INTERNAL SPECS ONLY (NO MODIFIERS) ──────────────────────────────────
    const exactCpu = lap.exactCpu || lap.fullSpecs?.performance?.processor || lap.cpu;
    const cpuGen = lap.gen ? (String(lap.gen).includes('Gen') ? lap.gen : `${lap.gen} Gen`) : (lap.shortSpecs?.generation || 'Current Architecture');
    const ramType = lap.ramType || lap.fullSpecs?.memoryStorage?.ramType || 'DDR4';
    const storType = lap.storageType || lap.fullSpecs?.memoryStorage?.storageType || 'NVMe SSD';
    const storText = lap.storage >= 1000 ? `${lap.storage / 1000} TB` : `${lap.storage} GB`;
    const display = lap.display || lap.fullSpecs?.display?.panel || '14.0" FHD IPS Anti-Glare';
    const gpu = lap.gpu || lap.fullSpecs?.performance?.graphics || 'Intel Integrated Graphics';
    const battery = lap.battery || lap.fullSpecs?.battery?.capacity || 'Up to 8-10 Hours (Fast Charge)';
    const ports = lap.ports || lap.fullSpecs?.connectivity?.ports || 'Thunderbolt / USB-C, USB 3.2, HDMI';
    const weight = lap.weight || lap.fullSpecs?.build?.weight || '1.36 kg (Lightweight Ultrabook)';
    const condition = lap.condition || 'Like New (10/10) · Grade A+ Certified';

    const specsGrid = document.getElementById('hexSpecsGrid');
    specsGrid.innerHTML = `
      <div class="hex-spec-item" title="Exact CPU: ${escapeHtml(exactCpu)}">
        <span class="hex-spec-k">⚡ Exact CPU Model</span>
        <span class="hex-spec-v">${escapeHtml(exactCpu)}</span>
      </div>
      <div class="hex-spec-item" title="Generation: ${escapeHtml(cpuGen)}">
        <span class="hex-spec-k">🏷️ Generation</span>
        <span class="hex-spec-v">${escapeHtml(cpuGen)}</span>
      </div>
      <div class="hex-spec-item" title="RAM: ${lap.ram} GB ${escapeHtml(ramType)}">
        <span class="hex-spec-k">🧠 RAM Size & Type</span>
        <span class="hex-spec-v">${lap.ram} GB ${escapeHtml(ramType)}</span>
      </div>
      <div class="hex-spec-item" title="Storage: ${storText} ${escapeHtml(storType)}">
        <span class="hex-spec-k">💾 Storage & Type</span>
        <span class="hex-spec-v">${storText} ${escapeHtml(storType)}</span>
      </div>
      <div class="hex-spec-item" title="Display: ${escapeHtml(display)}">
        <span class="hex-spec-k">🖥️ Display Panel</span>
        <span class="hex-spec-v">${escapeHtml(display)}</span>
      </div>
      <div class="hex-spec-item" title="Graphics: ${escapeHtml(gpu)}">
        <span class="hex-spec-k">🎮 Graphics (GPU)</span>
        <span class="hex-spec-v">${escapeHtml(gpu)}</span>
      </div>
      <div class="hex-spec-item" title="Battery: ${escapeHtml(battery)}">
        <span class="hex-spec-k">🔋 Battery Runtime</span>
        <span class="hex-spec-v">${escapeHtml(battery)}</span>
      </div>
      <div class="hex-spec-item" title="Ports: ${escapeHtml(ports)}">
        <span class="hex-spec-k">🔌 Ports & Expansion</span>
        <span class="hex-spec-v">${escapeHtml(ports)}</span>
      </div>
      <div class="hex-spec-item" title="Weight: ${escapeHtml(weight)}">
        <span class="hex-spec-k">⚖️ Weight & Form</span>
        <span class="hex-spec-v">${escapeHtml(weight)}</span>
      </div>
      <div class="hex-spec-item" title="Condition: ${escapeHtml(condition)}">
        <span class="hex-spec-k">✨ Certified Condition</span>
        <span class="hex-spec-v">${escapeHtml(condition)}</span>
      </div>
    `;

    // ── BUTTON ACTIONS ────────────────────────────────────────────────────────
    const addBtn = document.getElementById('hexBtnAddToCart');
    const codBtn = document.getElementById('hexBtnCod');
    const waBtn = document.getElementById('hexBtnWhatsApp');
    const detailsBtn = document.getElementById('hexBtnDetails');

    if (isOutOfStock) {
      addBtn.disabled = true;
      addBtn.innerHTML = '<span>Out of Stock</span>';
      codBtn.disabled = true;
      codBtn.innerHTML = '<span>Out of Stock</span>';
    } else {
      addBtn.disabled = false;
      addBtn.innerHTML = `
        <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><circle cx="9" cy="21" r="1"/><circle cx="20" cy="21" r="1"/><path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"/></svg>
        <span>Add to Cart</span>
      `;
      addBtn.onclick = () => {
        if (typeof window.addToCart === 'function') {
          window.addToCart(lap.id);
        }
        closeExpandedCard();
      };

      codBtn.disabled = false;
      codBtn.innerHTML = `
        <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><rect x="1" y="4" width="22" height="16" rx="2" ry="2"/><line x1="1" y1="10" x2="23" y2="10"/></svg>
        <span>Cash on Delivery</span>
      `;
      codBtn.onclick = () => {
        if (typeof window.addToCart === 'function') {
          window.addToCart(lap.id);
        }
        closeExpandedCard();
        if (typeof window.openCheckoutModal === 'function') {
          window.openCheckoutModal();
        }
      };
    }

    // WhatsApp Action
    waBtn.onclick = () => {
      const msg = encodeURIComponent(
        `Hi LaptopHUB! I want to order the following laptop with exact specifications:%0A` +
        `• Model: ${lap.name}%0A` +
        `• Price: ${lap.priceFormatted || 'Rs ' + lap.price}%0A` +
        `• Processor: ${exactCpu}%0A` +
        `• Memory: ${lap.ram}GB ${ramType}%0A` +
        `• Storage: ${storText} ${storType}%0A` +
        `• Condition: ${condition}%0A%0A` +
        `Please confirm availability and express shipping details!`
      );
      window.open(`https://wa.me/923261398594?text=${msg}`, '_blank');
    };

    // View Full Details Button
    detailsBtn.href = `product.html?id=${lap.id}`;
    detailsBtn.onclick = () => {
      closeExpandedCard();
    };
  }

  // ── 5. PHOTO SLIDESHOW ENGINE ──────────────────────────────────────────────
  function setupPhotoSlideshow(lap) {
    stopSlideshowTimer();
    if (slideshowResumeTimer) {
      clearTimeout(slideshowResumeTimer);
      slideshowResumeTimer = null;
    }

    // Determine photo list
    let photos = [];
    if (Array.isArray(lap.images) && lap.images.length > 0) {
      photos = [...lap.images];
    } else if (Array.isArray(lap.gallery) && lap.gallery.length > 0) {
      photos = [...lap.gallery];
    } else {
      if (lap.processedImg) photos.push(lap.processedImg);
      if (lap.img && !photos.includes(lap.img)) photos.push(lap.img);
      if (photos.length === 0) photos.push('images/placeholder.svg');
    }

    currentLapPhotos = photos;
    currentSlideIndex = 0;

    const track = document.getElementById('hexSlidesTrack');
    const dotsWrap = document.getElementById('hexDots');
    const prevArrow = document.getElementById('hexArrowPrev');
    const nextArrow = document.getElementById('hexArrowNext');

    track.innerHTML = '';
    dotsWrap.innerHTML = '';

    // Render slide elements
    currentLapPhotos.forEach((src, idx) => {
      const slide = document.createElement('div');
      slide.className = `hex-slide ${idx === 0 ? 'active' : ''}`;
      slide.dataset.slideIndex = String(idx);

      const img = document.createElement('img');
      img.src = src;
      img.alt = `${lap.name} photo ${idx + 1}`;
      img.className = 'hex-slide-img';
      img.loading = 'lazy';
      img.onerror = function() {
        this.src = 'images/placeholder.svg';
      };

      slide.appendChild(img);
      track.appendChild(slide);

      // Render dot
      if (currentLapPhotos.length > 1) {
        const dot = document.createElement('button');
        dot.type = 'button';
        dot.className = `hex-dot ${idx === 0 ? 'active' : ''}`;
        dot.setAttribute('aria-label', `Show photo ${idx + 1}`);
        dot.addEventListener('click', (e) => {
          e.stopPropagation();
          goToSlide(idx);
          pauseAndResumeSlideshow();
        });
        dotsWrap.appendChild(dot);
      }
    });

    // If only 1 photo: hide arrows and dots, do not auto-slide
    if (currentLapPhotos.length <= 1) {
      prevArrow.style.display = 'none';
      nextArrow.style.display = 'none';
      dotsWrap.style.display = 'none';
    } else {
      prevArrow.style.display = 'flex';
      nextArrow.style.display = 'flex';
      dotsWrap.style.display = 'flex';
      startSlideshowTimer();
    }
  }

  function goToSlide(targetIndex) {
    if (!currentLapPhotos || currentLapPhotos.length <= 1) return;
    const track = document.getElementById('hexSlidesTrack');
    const dotsWrap = document.getElementById('hexDots');
    if (!track) return;

    const slides = track.querySelectorAll('.hex-slide');
    const dots = dotsWrap ? dotsWrap.querySelectorAll('.hex-dot') : [];

    slides.forEach((s, idx) => {
      if (idx === targetIndex) {
        s.classList.add('active');
      } else {
        s.classList.remove('active');
      }
    });

    dots.forEach((d, idx) => {
      if (idx === targetIndex) {
        d.classList.add('active');
      } else {
        d.classList.remove('active');
      }
    });

    currentSlideIndex = targetIndex;
  }

  function navigateSlideshow(direction) {
    if (!currentLapPhotos || currentLapPhotos.length <= 1) return;
    const newIndex = (currentSlideIndex + direction + currentLapPhotos.length) % currentLapPhotos.length;
    goToSlide(newIndex);
  }

  function startSlideshowTimer() {
    stopSlideshowTimer();
    if (currentLapPhotos.length <= 1) return;

    slideshowTimer = setInterval(() => {
      if (!isOverlayOpen || isInteractingSlideshow) return;
      navigateSlideshow(1);
    }, SLIDESHOW_INTERVAL_MS);
  }

  function stopSlideshowTimer() {
    if (slideshowTimer) {
      clearInterval(slideshowTimer);
      slideshowTimer = null;
    }
  }

  function pauseAndResumeSlideshow() {
    stopSlideshowTimer();
    if (slideshowResumeTimer) {
      clearTimeout(slideshowResumeTimer);
    }
    // Resume after 2s of inactivity
    slideshowResumeTimer = setTimeout(() => {
      if (isOverlayOpen && !isInteractingSlideshow && currentLapPhotos.length > 1) {
        startSlideshowTimer();
      }
    }, SLIDESHOW_INTERVAL_MS);
  }

  // ── 6. CLOSE EXPANDED CARD ─────────────────────────────────────────────────
  function closeExpandedCard() {
    const overlay = document.getElementById('hoverExpandOverlay');
    const modal = document.getElementById('hoverExpandCard');
    if (!overlay || !isOverlayOpen) return;

    // Clean up slideshow timer immediately
    stopSlideshowTimer();
    if (slideshowResumeTimer) {
      clearTimeout(slideshowResumeTimer);
      slideshowResumeTimer = null;
    }

    if (!prefersReducedMotion() && originCardRect && modal) {
      const targetRect = modal.getBoundingClientRect();
      const scaleX = Math.min(1, originCardRect.width / Math.max(targetRect.width, 300));
      const scaleY = Math.min(1, originCardRect.height / Math.max(targetRect.height, 400));
      const translateX = (originCardRect.left + originCardRect.width / 2) - (targetRect.left + targetRect.width / 2);
      const translateY = (originCardRect.top + originCardRect.height / 2) - (targetRect.top + targetRect.height / 2);

      modal.style.transition = 'transform 0.3s cubic-bezier(0.16, 1, 0.3, 1), opacity 0.22s ease';
      modal.style.transform = `translate3d(${translateX.toFixed(1)}px, ${translateY.toFixed(1)}px, 0) scale(${scaleX.toFixed(4)}, ${scaleY.toFixed(4)})`;
      modal.style.opacity = '0';
      overlay.style.transition = 'opacity 0.26s ease, visibility 0.26s ease';
      overlay.classList.remove('active');

      setTimeout(() => {
        cleanupClose();
      }, 300);
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
      modal.style.opacity = '';
      modal.scrollTop = 0;
    }
    isOverlayOpen = false;
    originCardRect = null;
    isInteractingSlideshow = false;
    if (closeTimeout) {
      clearTimeout(closeTimeout);
      closeTimeout = null;
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

  // ── 7. INITIALIZATION & DYNAMIC RE-ATTACH ───────────────────────────────────
  function initHoverExpand() {
    if (!isFineDesktop()) return;
    attachHoverListeners();

    const grid = document.getElementById('productGrid');
    if (grid && window.MutationObserver) {
      if (!grid._hexObserver) {
        grid._hexObserver = new MutationObserver(() => {
          attachHoverListeners();
        });
        grid._hexObserver.observe(grid, { childList: true });
      }
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
})(window);
