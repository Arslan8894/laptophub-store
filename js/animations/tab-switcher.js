/**
 * LaptopHUB - Liquid Glass Tab Switcher (js/animations/tab-switcher.js)
 * Step 4: Fluid sliding indicator with dynamic stretching and shape morphing,
 * combined with content panel cross-fade/slide transitions.
 */

(function () {
  'use strict';

  let currentTabKey = 'inventory';
  let isTransitioning = false;

  // Cache DOM nodes
  let switcherTrack = null;
  let indicator = null;
  let tabButtons = [];
  let panels = {};

  function initTabSwitcher() {
    switcherTrack = document.querySelector('.glass-tab-switcher');
    if (!switcherTrack) return;

    indicator = document.getElementById('glassTabIndicator');
    tabButtons = Array.from(switcherTrack.querySelectorAll('.glass-tab-btn'));

    panels = {
      inventory: document.getElementById('tabpanel-inventory'),
      consult: document.getElementById('tabpanel-consult'),
      reviews: document.getElementById('tabpanel-reviews')
    };

    if (!tabButtons.length) return;

    // Check if initial hash matches a tab
    const hash = window.location.hash.replace('#', '');
    let initialKey = 'inventory';
    if (hash === 'reviews' || hash === 'consult') {
      initialKey = hash;
    }

    // Set initial position without animation
    const initialBtn = tabButtons.find(b => b.dataset.tab === initialKey) || tabButtons[0];
    setInitialPosition(initialBtn);

    // Bind click events on tab buttons
    tabButtons.forEach(btn => {
      btn.addEventListener('click', (e) => {
        e.preventDefault();
        const tabKey = btn.dataset.tab;
        switchStoreTab(tabKey, btn);
      });
    });

    // Resize handler
    window.addEventListener('resize', debounce(() => {
      const activeBtn = tabButtons.find(b => b.classList.contains('active'));
      if (activeBtn) updateIndicatorPosition(activeBtn, false);
    }, 100));

    // Handle hash change
    window.addEventListener('hashchange', () => {
      const newHash = window.location.hash.replace('#', '');
      if (['inventory', 'consult', 'reviews'].includes(newHash) && newHash !== currentTabKey) {
        const targetBtn = tabButtons.find(b => b.dataset.tab === newHash);
        if (targetBtn) switchStoreTab(newHash, targetBtn, false);
      }
    });

    // Initialize interactive consult chips
    initConsultChips();

    // Hook navbar links to sync with tab switcher
    wireNavbarToTabSwitcher();
  }

  function setInitialPosition(targetBtn) {
    if (!targetBtn || !indicator || !switcherTrack) return;

    const trackRect = switcherTrack.getBoundingClientRect();
    const btnRect = targetBtn.getBoundingClientRect();
    const leftOffset = btnRect.left - trackRect.left;
    const btnWidth = btnRect.width;

    tabButtons.forEach(b => {
      const isActive = b === targetBtn;
      b.classList.toggle('active', isActive);
      b.setAttribute('aria-selected', isActive ? 'true' : 'false');
    });

    currentTabKey = targetBtn.dataset.tab || 'inventory';

    // Show initial panel, hide others
    Object.keys(panels).forEach(key => {
      const panel = panels[key];
      if (panel) {
        if (key === currentTabKey) {
          panel.classList.remove('hidden-tab');
          panel.classList.add('active-tab');
          panel.style.opacity = '1';
          panel.style.transform = 'translateY(0)';
        } else {
          panel.classList.remove('active-tab');
          panel.classList.add('hidden-tab');
          panel.style.opacity = '0';
        }
      }
    });

    indicator.style.transform = `translateX(${leftOffset}px)`;
    indicator.style.width = `${btnWidth}px`;
    indicator.style.opacity = '1';
    indicator.dataset.currentLeft = leftOffset;
    indicator.dataset.currentWidth = btnWidth;
  }

  function updateIndicatorPosition(targetBtn, animate = true) {
    if (!targetBtn || !indicator || !switcherTrack) return;

    const trackRect = switcherTrack.getBoundingClientRect();
    const btnRect = targetBtn.getBoundingClientRect();
    const targetLeft = btnRect.left - trackRect.left;
    const targetWidth = btnRect.width;

    const currentLeft = parseFloat(indicator.dataset.currentLeft || targetLeft);
    const deltaX = targetLeft - currentLeft;
    const direction = deltaX >= 0 ? 1 : -1;
    const distance = Math.abs(deltaX);

    const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    if (!animate || typeof gsap === 'undefined' || prefersReducedMotion) {
      indicator.style.transform = `translateX(${targetLeft}px)`;
      indicator.style.width = `${targetWidth}px`;
      indicator.style.borderRadius = '9999px';
      indicator.dataset.currentLeft = targetLeft;
      indicator.dataset.currentWidth = targetWidth;
      return;
    }

    // Dynamic liquid stretch & morph calculation:
    // When moving right: right edge stretches forward first, pill bulges horizontally
    // When moving left: left edge stretches backwards first
    const stretchExpansion = Math.min(distance * 0.32, 50);
    const midWidth = targetWidth + stretchExpansion;
    const midLeft = direction > 0 ? currentLeft : (targetLeft - stretchExpansion);

    // Kill any existing animations on indicator
    gsap.killTweensOf(indicator);

    const tl = gsap.timeline({
      onComplete: () => {
        indicator.dataset.currentLeft = targetLeft;
        indicator.dataset.currentWidth = targetWidth;
      }
    });

    // Phase 1: Fluid stretch & shape morph while in transit
    tl.to(indicator, {
      x: midLeft + (direction > 0 ? stretchExpansion * 0.4 : 0),
      width: midWidth,
      borderRadius: direction > 0 ? '16px 30px 30px 16px' : '30px 16px 16px 30px',
      duration: 0.16,
      ease: 'power2.inOut'
    })
    // Phase 2: Snap and elastic contract to exact destination with springy settle
    .to(indicator, {
      x: targetLeft,
      width: targetWidth,
      borderRadius: '9999px',
      duration: 0.36,
      ease: 'elastic.out(1, 0.72)'
    }, '-=0.03');
  }

  function switchStoreTab(tabKey, targetBtn, shouldScroll = true) {
    if (!targetBtn) {
      targetBtn = tabButtons.find(b => b.dataset.tab === tabKey);
    }
    if (!targetBtn || tabKey === currentTabKey && panels[tabKey] && panels[tabKey].classList.contains('active-tab')) {
      return;
    }

    const prevKey = currentTabKey;
    currentTabKey = tabKey;

    // Update button states
    tabButtons.forEach(b => {
      const isActive = b === targetBtn;
      b.classList.toggle('active', isActive);
      b.setAttribute('aria-selected', isActive ? 'true' : 'false');
    });

    // Move & morph the indicator
    updateIndicatorPosition(targetBtn, true);

    // Cross-fade & slide panels
    const currentPanel = panels[prevKey];
    const targetPanel = panels[tabKey];

    const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    const direction = getTabOrder(tabKey) > getTabOrder(prevKey) ? 1 : -1;

    if (currentPanel && targetPanel) {
      if (prefersReducedMotion || typeof gsap === 'undefined') {
        currentPanel.classList.remove('active-tab');
        currentPanel.classList.add('hidden-tab');
        targetPanel.classList.remove('hidden-tab');
        targetPanel.classList.add('active-tab');
        targetPanel.style.opacity = '1';
        targetPanel.style.transform = 'translateY(0)';
      } else {
        isTransitioning = true;
        gsap.killTweensOf([currentPanel, targetPanel]);

        // Outgoing panel slide & fade
        gsap.to(currentPanel, {
          opacity: 0,
          y: -14 * direction,
          duration: 0.22,
          ease: 'power2.in',
          onComplete: () => {
            currentPanel.classList.remove('active-tab');
            currentPanel.classList.add('hidden-tab');

            // Incoming panel slide & fade in
            targetPanel.classList.remove('hidden-tab');
            targetPanel.classList.add('active-tab');

            gsap.fromTo(targetPanel,
              { opacity: 0, y: 18 * direction },
              {
                opacity: 1,
                y: 0,
                duration: 0.35,
                ease: 'power2.out',
                onComplete: () => {
                  isTransitioning = false;
                  // Refresh Lenis / ScrollTrigger if present
                  if (typeof ScrollTrigger !== 'undefined') {
                    ScrollTrigger.refresh();
                  }
                }
              }
            );
          }
        });
      }
    }

    // Update URL hash without harsh jumping
    if (history.replaceState) {
      history.replaceState(null, '', `#${tabKey}`);
    }

    // Synchronize navbar active lens
    syncNavbarWithTab(tabKey);

    // Optional smooth scroll to tab area if user was far below
    if (shouldScroll && switcherTrack) {
      const switcherRect = switcherTrack.getBoundingClientRect();
      if (switcherRect.top < 60 || switcherRect.top > window.innerHeight * 0.7) {
        const targetScroll = window.scrollY + switcherRect.top - 100;
        window.scrollTo({ top: Math.max(0, targetScroll), behavior: 'smooth' });
      }
    }
  }

  function getTabOrder(key) {
    const order = { inventory: 0, consult: 1, reviews: 2 };
    return order[key] !== undefined ? order[key] : 0;
  }

  function syncNavbarWithTab(tabKey) {
    const navTrack = document.querySelector('.nav-pill-track');
    if (!navTrack) return;

    const navLinks = Array.from(navTrack.querySelectorAll('a'));
    let matchHref = '#inventory';
    if (tabKey === 'consult') matchHref = 'consult';
    if (tabKey === 'reviews') matchHref = '#reviews';

    navLinks.forEach(link => {
      const href = link.getAttribute('href') || '';
      const isMatch = (matchHref === 'consult' && href.includes('consult')) || href === matchHref;
      link.classList.toggle('active', isMatch);
    });

    // Trigger lens reposition in glass-nav
    const activeNavLink = navLinks.find(l => l.classList.contains('active'));
    const lens = navTrack.querySelector('.glass-lens-highlight');
    if (activeNavLink && lens && typeof gsap !== 'undefined') {
      const trackRect = navTrack.getBoundingClientRect();
      const targetRect = activeNavLink.getBoundingClientRect();
      gsap.to(lens, {
        x: targetRect.left - trackRect.left,
        width: targetRect.width,
        opacity: 1,
        duration: 0.35,
        ease: 'elastic.out(1, 0.75)',
        overwrite: 'auto'
      });
    }
  }

  function wireNavbarToTabSwitcher() {
    // Intercept navbar link clicks on the same page
    const navTrack = document.querySelector('.nav-pill-track');
    if (!navTrack) return;

    navTrack.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', (e) => {
        const href = link.getAttribute('href');
        if (href === '#inventory') {
          e.preventDefault();
          switchStoreTab('inventory', null, true);
        } else if (href === '#reviews') {
          e.preventDefault();
          switchStoreTab('reviews', null, true);
        } else if (href === 'consult.html') {
          // If clicked normally, switch to embedded Consult tab with option to open full page
          e.preventDefault();
          switchStoreTab('consult', null, true);
        }
      });
    });

    // Also wire mobile drawer links
    const mobileDrawer = document.getElementById('mobileNavOverlay');
    if (mobileDrawer) {
      document.querySelectorAll('.mobile-drawer a').forEach(link => {
        link.addEventListener('click', (e) => {
          const href = link.getAttribute('href');
          if (href === '#inventory') {
            e.preventDefault();
            switchStoreTab('inventory', null, true);
          } else if (href === '#reviews') {
            e.preventDefault();
            switchStoreTab('reviews', null, true);
          } else if (href === 'consult.html') {
            e.preventDefault();
            switchStoreTab('consult', null, true);
          }
        });
      });
    }
  }

  // Quick Consult Interactive Matching Feature
  function initConsultChips() {
    const chipsContainer = document.getElementById('consultChips');
    if (!chipsContainer) return;

    const chips = chipsContainer.querySelectorAll('.consult-chip');
    chips.forEach(chip => {
      chip.addEventListener('click', () => {
        chips.forEach(c => c.classList.remove('active'));
        chip.classList.add('active');
        const filterType = chip.dataset.filter;
        renderConsultMatches(filterType);
      });
    });

    // Initial render
    renderConsultMatches('coding');
  }

  function renderConsultMatches(filterType) {
    const grid = document.getElementById('consultMatchesGrid');
    if (!grid) return;

    const inventory = (typeof LAPTOPS_INVENTORY !== 'undefined') ? LAPTOPS_INVENTORY : [];
    if (!inventory.length) {
      grid.innerHTML = '<p style="color:var(--muted);text-align:center;grid-column:1/-1;">Loading recommendations...</p>';
      return;
    }

    let matches = [];
    if (filterType === 'coding') {
      matches = inventory.filter(l => (l.ram >= 16 || l.cpu.toLowerCase().includes('i7') || l.cpu.toLowerCase().includes('ryzen 7'))).slice(0, 4);
    } else if (filterType === 'design') {
      matches = inventory.filter(l => (l.gpu && !l.gpu.toLowerCase().includes('intel') || l.screen && l.screen.toLowerCase().includes('oled') || l.name.includes('MacBook') || l.name.includes('Spectre'))).slice(0, 4);
    } else if (filterType === 'executive') {
      matches = inventory.filter(l => (l.name.includes('XPS') || l.name.includes('Latitude') || l.name.includes('EliteBook') || l.name.includes('Surface'))).slice(0, 4);
    } else if (filterType === 'budget') {
      matches = inventory.filter(l => l.price && l.price <= 120000).slice(0, 4);
    } else if (filterType === 'gaming') {
      matches = inventory.filter(l => (l.gpu && (l.gpu.includes('RTX') || l.gpu.includes('GTX')) || l.badge === 'Gaming Flagship' || l.useCases.includes('gaming'))).slice(0, 4);
    }

    if (!matches.length) {
      matches = inventory.slice(0, 4);
    }

    grid.innerHTML = matches.map(l => {
      const priceStr = l.priceFormatted || `Rs ${Number(l.price).toLocaleString('en-PK')}`;
      const badgeHtml = l.badge ? `<span style="position:absolute;top:10px;right:10px;background:var(--badge-bg);color:var(--badge-text);font-size:0.7rem;font-weight:700;padding:2px 8px;border-radius:9999px;border:1px solid var(--badge-border);">${l.badge}</span>` : '';
      return `
        <div class="consult-match-card glass-squish" onclick="openProductPage(${l.id}, event)">
          ${badgeHtml}
          <div class="consult-match-img-wrap">
            <img src="${l.img}" alt="${l.name}" loading="lazy">
          </div>
          <div style="font-size:0.75rem;font-weight:700;color:var(--blue);text-transform:uppercase;letter-spacing:0.04em;margin-bottom:4px;">${l.brand.toUpperCase()}</div>
          <h4 style="font-size:1.05rem;font-weight:700;color:var(--heading);margin-bottom:6px;line-height:1.3;">${l.name}</h4>
          <div style="font-size:0.82rem;color:var(--muted);margin-bottom:12px;">${l.cpu} • ${l.ram}GB RAM • ${l.storage}</div>
          <div style="margin-top:auto;display:flex;align-items:center;justify-content:space-between;border-top:1px solid var(--border);padding-top:10px;">
            <div style="font-size:1.15rem;font-weight:800;color:var(--heading);">${priceStr}</div>
            <button class="glass-pill" style="padding:5px 14px;font-size:0.8rem;font-weight:600;background:var(--blue-dim);color:var(--blue);border:1px solid var(--border2);cursor:pointer;" onclick="event.stopPropagation();openProductPage(${l.id})">
              Details →
            </button>
          </div>
        </div>
      `;
    }).join('');
  }

  function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
      const later = () => {
        clearTimeout(timeout);
        func(...args);
      };
      clearTimeout(timeout);
      timeout = setTimeout(later, wait);
    };
  }

  // Expose global switcher
  window.switchStoreTab = switchStoreTab;

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initTabSwitcher);
  } else {
    initTabSwitcher();
  }
})();
