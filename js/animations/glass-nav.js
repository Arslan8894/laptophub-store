/**
 * LaptopHUB - Liquid Glass Navbar Interactive Lens (js/animations/glass-nav.js)
 * High-performance sliding glass highlight with locked navigation transitions to prevent
 * jitter, flickering, and bouncing between tabs while scrolling across page sections.
 */

(function () {
  'use strict';

  function initGlassNav() {
    const track = document.querySelector('.nav-pill-track');
    if (!track) return;

    let lens = track.querySelector('.glass-lens-highlight');
    if (!lens) {
      lens = document.createElement('div');
      lens.className = 'glass-lens-highlight';
      track.prepend(lens);
    }

    const links = Array.from(track.querySelectorAll('a'));
    if (!links.length) return;

    let activeLink = track.querySelector('a.active') || links[0];
    let isNavigating = false;
    let navLockTimer = null;
    let scrollMonitorInterval = null;

    // Check if initial hash or current page matches a link
    const currentHash = window.location.hash;
    const currentPath = window.location.pathname;
    if (currentHash) {
      const match = links.find(l => l.getAttribute('href') === currentHash);
      if (match) activeLink = match;
    } else if (currentPath.includes('consult.html')) {
      const match = links.find(l => (l.getAttribute('href') || '').includes('consult.html'));
      if (match) activeLink = match;
    }

    function setActive(link, animate = true) {
      if (!link) return;
      activeLink = link;
      links.forEach(l => l.classList.toggle('active', l === activeLink));
      positionLens(activeLink, animate);
    }

    function positionLens(targetEl, animate = true) {
      if (!targetEl || !lens) return;

      const trackRect = track.getBoundingClientRect();
      const targetRect = targetEl.getBoundingClientRect();

      // Ensure dimensions are valid (avoid zero-width before layout)
      if (targetRect.width === 0) return;

      const leftOffset = targetRect.left - trackRect.left;
      const targetWidth = targetRect.width;

      if (!animate) {
        lens.style.transition = 'none';
        lens.style.transform = `translateX(${leftOffset}px)`;
        lens.style.width = `${targetWidth}px`;
        lens.style.opacity = '1';
        void lens.offsetWidth;
        lens.style.transition = '';
      } else {
        lens.style.transform = `translateX(${leftOffset}px)`;
        lens.style.width = `${targetWidth}px`;
        lens.style.opacity = '1';
      }
    }

    // Set initial active state
    setActive(activeLink, false);

    // Run positioning once fonts / layout are ready
    setTimeout(() => positionLens(activeLink, false), 50);
    if (document.fonts && document.fonts.ready) {
      document.fonts.ready.then(() => positionLens(activeLink, false));
    }

    // CLICK HANDLER WITH BULLETPROOF SMOOTH TRANSITION LOCK
    links.forEach(link => {
      // Hover preview - only when NOT actively programmatically scrolling
      link.addEventListener('mouseenter', () => {
        if (!isNavigating) {
          positionLens(link, true);
        }
      });

      link.addEventListener('click', (e) => {
        const href = link.getAttribute('href');
        if (href && href.startsWith('#')) {
          const targetEl = document.querySelector(href);
          if (targetEl) {
            e.preventDefault();

            // 1. Immediately engage navigation lock and clear any pending timers
            isNavigating = true;
            if (navLockTimer) clearTimeout(navLockTimer);
            if (scrollMonitorInterval) clearInterval(scrollMonitorInterval);

            // 2. Set active link immediately & smoothly glide lens to destination
            setActive(link, true);

            // 3. Compute exact target scroll coordinate (80px header clearance)
            const navOffset = 80;
            const targetScrollY = Math.max(0, targetEl.getBoundingClientRect().top + window.scrollY - navOffset);

            // 4. Smooth scroll to target section
            window.scrollTo({
              top: targetScrollY,
              behavior: 'smooth'
            });

            // 5. Release lock ONLY when scroll truly finishes (scrollend or verified arrival)
            const releaseLock = () => {
              if (scrollMonitorInterval) clearInterval(scrollMonitorInterval);
              scrollMonitorInterval = null;
              if (navLockTimer) clearTimeout(navLockTimer);
              navLockTimer = null;
              window.removeEventListener('scrollend', onScrollEnd);

              setTimeout(() => {
                isNavigating = false;
                positionLens(activeLink, false);
              }, 120);
            };

            const onScrollEnd = () => {
              releaseLock();
            };

            window.addEventListener('scrollend', onScrollEnd, { once: true });

            // Fallback monitor: never prematurely release midway through smooth scroll
            const startTime = Date.now();
            let lastY = window.scrollY;
            let stillFrames = 0;

            scrollMonitorInterval = setInterval(() => {
              const currentY = window.scrollY;
              const elapsed = Date.now() - startTime;
              const dist = Math.abs(currentY - targetScrollY);

              if (Math.abs(currentY - lastY) < 1.5) {
                stillFrames++;
              } else {
                stillFrames = 0;
              }
              lastY = currentY;

              if ((dist <= 12 && stillFrames >= 4) || (stillFrames >= 6 && elapsed > 700)) {
                releaseLock();
              }
            }, 50);

            // 6. Absolute failsafe timeout (1500ms max)
            navLockTimer = setTimeout(() => {
              releaseLock();
            }, 1500);
          }
        }
      });
    });

    // If user manually interrupts with wheel, release programmatic lock
    window.addEventListener('wheel', () => {
      if (isNavigating) {
        if (scrollMonitorInterval) clearInterval(scrollMonitorInterval);
        if (navLockTimer) clearTimeout(navLockTimer);
        isNavigating = false;
      }
    }, { passive: true });

    // When mouse leaves the track, always return lens to activeLink
    track.addEventListener('mouseleave', () => {
      positionLens(activeLink, true);
    });

    // Reposition without transition on window resize
    window.addEventListener('resize', () => {
      positionLens(activeLink, false);
    });

    // SCROLL SPY - Runs ONLY during genuine manual user scrolling
    let scrollRafId = null;
    window.addEventListener('scroll', () => {
      if (!document.getElementById('inventory')) return;

      // ABSOLUTELY DO NOT RUN SCROLL SPY WHILE PROGRAMMATICALLY SCROLLING!
      if (isNavigating) return;

      if (scrollRafId) return;
      scrollRafId = requestAnimationFrame(() => {
        scrollRafId = null;
        if (isNavigating) return;

        const reviewsSec = document.getElementById('reviews');

        // Reading probe zone: 35% of viewport height (max 220px)
        const probeY = Math.min(220, window.innerHeight * 0.35);

        let currentSec = '#inventory';

        if (reviewsSec && reviewsSec.getBoundingClientRect().top <= probeY) {
          currentSec = '#reviews';
        } else {
          currentSec = '#inventory';
        }

        const matchingLink = links.find(l => l.getAttribute('href') === currentSec);
        if (matchingLink && matchingLink !== activeLink) {
          setActive(matchingLink, true);
        }
      });
    }, { passive: true });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initGlassNav);
  } else {
    initGlassNav();
  }
})();
