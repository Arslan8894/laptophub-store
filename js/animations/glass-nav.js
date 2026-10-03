/**
 * LaptopHUB - Liquid Glass Navbar Interactive Lens
 * Handles the springy sliding glass highlight between navigation items.
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

    let activeLink = links[0]; // Default to first (All Laptops)

    // Check URL or hash to select active item
    const currentHash = window.location.hash;
    const currentPath = window.location.pathname;

    links.forEach(link => {
      const href = link.getAttribute('href');
      if (href && (href === currentHash || currentPath.endsWith(href))) {
        activeLink = link;
      }
    });

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
          duration: 0.42,
          ease: 'elastic.out(1, 0.75)',
          overwrite: 'auto'
        });
      }
    }

    // Set initial active state
    links.forEach(l => l.classList.remove('active'));
    activeLink.classList.add('active');
    setTimeout(() => positionLens(activeLink, false), 50);

    // Hover interactions
    links.forEach(link => {
      link.addEventListener('mouseenter', () => {
        positionLens(link, true);
      });

      link.addEventListener('click', () => {
        links.forEach(l => l.classList.remove('active'));
        link.classList.add('active');
        activeLink = link;
        positionLens(activeLink, true);
      });
    });

    track.addEventListener('mouseleave', () => {
      positionLens(activeLink, true);
    });

    window.addEventListener('resize', () => {
      positionLens(activeLink, false);
      updateOffsets();
    });

    // Cache offsets to avoid layout thrashing
    let cachedReviewsOffset = 0;
    let cachedInventoryOffset = 0;

    function updateOffsets() {
      const reviewsSec = document.getElementById('reviews');
      const inventorySec = document.getElementById('inventory');
      if (reviewsSec) cachedReviewsOffset = reviewsSec.offsetTop;
      if (inventorySec) cachedInventoryOffset = inventorySec.offsetTop;
    }
    setTimeout(updateOffsets, 200);

    // Update active tab on scroll throttled via requestAnimationFrame
    let scrollRafId = null;
    window.addEventListener('scroll', () => {
      if (scrollRafId) return;
      scrollRafId = requestAnimationFrame(() => {
        scrollRafId = null;
        const scrollPos = window.scrollY + 120;

        let currentSec = null;
        if (cachedReviewsOffset && scrollPos >= cachedReviewsOffset) {
          currentSec = '#reviews';
        } else if (cachedInventoryOffset && scrollPos >= cachedInventoryOffset - 80) {
          currentSec = '#inventory';
        }

        if (currentSec) {
          const matchingLink = links.find(l => l.getAttribute('href') === currentSec);
          if (matchingLink && matchingLink !== activeLink) {
            links.forEach(l => l.classList.remove('active'));
            matchingLink.classList.add('active');
            activeLink = matchingLink;
            positionLens(activeLink, true);
          }
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
