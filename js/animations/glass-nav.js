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
    let navLockTimeout = null;
    let scrollDebounceTimeout = null;

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
    links.forEach(l => l.classList.remove('active'));
    activeLink.classList.add('active');

    // Run positioning once fonts / layout are ready
    setTimeout(() => positionLens(activeLink, false), 50);
    if (document.fonts && document.fonts.ready) {
      document.fonts.ready.then(() => positionLens(activeLink, false));
    }

    // CLICK HANDLER
    links.forEach(link => {
      // Hover preview - ONLY when NOT navigating
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

            // Set programmatic navigation lock
            isNavigating = true;
            clearTimeout(navLockTimeout);
            clearTimeout(scrollDebounceTimeout);

            // Update active link immediately
            links.forEach(l => l.classList.remove('active'));
            link.classList.add('active');
            activeLink = link;

            // Slide lens to the clicked link immediately and lock it there
            positionLens(activeLink, true);

            // Calculate exact target scroll position using live document coordinates
            const targetY = href === '#inventory'
              ? Math.max(0, targetEl.getBoundingClientRect().top + window.scrollY - 75)
              : Math.max(0, targetEl.getBoundingClientRect().top + window.scrollY - 75);

            window.scrollTo({
              top: targetY,
              behavior: 'smooth'
            });

            // Keep navigation lock engaged for the full duration of smooth scroll
            navLockTimeout = setTimeout(() => {
              isNavigating = false;
              positionLens(activeLink, true);
            }, 1200);
          }
        }
      });
    });

    // When mouse leaves the track, always return lens to activeLink
    track.addEventListener('mouseleave', () => {
      positionLens(activeLink, true);
    });

    // Reposition without transition on window resize
    window.addEventListener('resize', () => {
      positionLens(activeLink, false);
    });

    // When scroll finishes natively, release navigation lock safely
    window.addEventListener('scrollend', () => {
      if (isNavigating) {
        clearTimeout(navLockTimeout);
        isNavigating = false;
        positionLens(activeLink, true);
      }
    });

    // SCROLL SPY - Runs ONLY during genuine manual scrolling
    let scrollRafId = null;
    window.addEventListener('scroll', () => {
      // If page doesn't have inventory section (e.g. consult.html), do not run scroll spy
      if (!document.getElementById('inventory')) return;

      // If user clicked a tab and smooth scroll is ongoing, do NOT let scroll spy run!
      if (isNavigating) {
        clearTimeout(scrollDebounceTimeout);
        scrollDebounceTimeout = setTimeout(() => {
          // If no scroll events fired for 200ms, smooth scroll has finished
          isNavigating = false;
          positionLens(activeLink, true);
        }, 200);
        return;
      }

      if (scrollRafId) return;
      scrollRafId = requestAnimationFrame(() => {
        scrollRafId = null;
        if (isNavigating) return;

        const consultSec = document.getElementById('consult');
        const reviewsSec = document.getElementById('reviews');

        const scrollY = window.scrollY;
        // Compute real-time element tops in document coordinates
        const consultTop = consultSec ? (consultSec.getBoundingClientRect().top + scrollY - 200) : 999999;
        const reviewsTop = reviewsSec ? (reviewsSec.getBoundingClientRect().top + scrollY - 200) : 999999;

        let currentSec = '#inventory';
        if (scrollY >= reviewsTop) {
          currentSec = '#reviews';
        } else if (scrollY >= consultTop) {
          currentSec = '#consult';
        } else {
          currentSec = '#inventory';
        }

        const matchingLink = links.find(l => l.getAttribute('href') === currentSec);
        if (matchingLink && matchingLink !== activeLink) {
          links.forEach(l => l.classList.remove('active'));
          matchingLink.classList.add('active');
          activeLink = matchingLink;
          positionLens(activeLink, true);
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
