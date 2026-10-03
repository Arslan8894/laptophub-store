/**
 * LaptopHUB - Liquid Glass Navbar Interactive Lens (js/animations/glass-nav.js)
 * Smooth sliding glass highlight with locked navigation transitions to prevent
 * jitter and flickering while smooth scrolling across page sections.
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

    let activeLink = links[0]; // Default to All Laptops
    let isNavigating = false;
    let navTimeout = null;

    // Determine initial active link based on URL hash
    const currentHash = window.location.hash;
    if (currentHash) {
      const match = links.find(l => l.getAttribute('href') === currentHash);
      if (match) activeLink = match;
    }

    function positionLens(targetEl, animate = true) {
      if (!targetEl || !lens) return;

      const trackRect = track.getBoundingClientRect();
      const targetRect = targetEl.getBoundingClientRect();

      const leftOffset = targetRect.left - trackRect.left;
      const targetWidth = targetRect.width;

      if (!animate || typeof gsap === 'undefined') {
        lens.style.transform = `translateX(${leftOffset}px)`;
        lens.style.width = `${targetWidth}px`;
        lens.style.opacity = '1';
      } else {
        gsap.to(lens, {
          x: leftOffset,
          width: targetWidth,
          opacity: 1,
          duration: 0.38,
          ease: 'elastic.out(1, 0.82)',
          overwrite: 'auto'
        });
      }
    }

    // Set initial active state
    links.forEach(l => l.classList.remove('active'));
    activeLink.classList.add('active');
    setTimeout(() => positionLens(activeLink, false), 60);

    // Hover interactions
    links.forEach(link => {
      link.addEventListener('mouseenter', () => {
        positionLens(link, true);
      });

      link.addEventListener('click', (e) => {
        const href = link.getAttribute('href');
        if (href && href.startsWith('#')) {
          const targetEl = document.querySelector(href);
          if (targetEl) {
            e.preventDefault();

            // Lock navigation to prevent scroll spy from jittering between tabs
            isNavigating = true;
            clearTimeout(navTimeout);

            links.forEach(l => l.classList.remove('active'));
            link.classList.add('active');
            activeLink = link;

            // Immediately animate lens to clicked link
            positionLens(activeLink, true);

            // Calculate precise destination scroll offset (accounting for floating header)
            const targetY = targetEl.getBoundingClientRect().top + window.scrollY - 80;
            window.scrollTo({
              top: Math.max(0, targetY),
              behavior: 'smooth'
            });

            // Unlock scroll spy once smooth scroll has settled
            navTimeout = setTimeout(() => {
              isNavigating = false;
            }, 850);
          }
        }
      });
    });

    track.addEventListener('mouseleave', () => {
      positionLens(activeLink, true);
    });

    window.addEventListener('resize', () => {
      positionLens(activeLink, false);
    });

    // Listen for modern scrollend if supported to promptly release lock
    if ('onscrollend' in window) {
      window.addEventListener('scrollend', () => {
        clearTimeout(navTimeout);
        isNavigating = false;
      }, { passive: true });
    }

    // Throttled Scroll-Spy for manual scrolling only
    let scrollRafId = null;
    window.addEventListener('scroll', () => {
      // If user just clicked a tab and the page is auto-scrolling, ignore scroll spy!
      if (isNavigating) return;

      if (scrollRafId) return;
      scrollRafId = requestAnimationFrame(() => {
        scrollRafId = null;
        if (isNavigating) return;

        const inventorySec = document.getElementById('inventory');
        const consultSec = document.getElementById('consult');
        const reviewsSec = document.getElementById('reviews');

        let currentSec = '#inventory';

        // When near the very top of the page, always stay on inventory
        if (window.scrollY < 260) {
          currentSec = '#inventory';
        } else {
          // Check from bottom to top
          if (reviewsSec && reviewsSec.getBoundingClientRect().top <= 200) {
            currentSec = '#reviews';
          } else if (consultSec && consultSec.getBoundingClientRect().top <= 200) {
            currentSec = '#consult';
          } else if (inventorySec && inventorySec.getBoundingClientRect().top <= 200) {
            currentSec = '#inventory';
          }
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
