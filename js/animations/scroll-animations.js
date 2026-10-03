/**
 * LaptopHUB - Lenis Smooth Scroll & GSAP ScrollTrigger Orchestrator
 * Keeps all smooth scrolling and scroll reveals modularized in /js/animations/
 */

(function () {
  'use strict';

  const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  let lenisInstance = null;

  function initScrollAnimations() {
    // Ensure GSAP and ScrollTrigger are loaded
    if (typeof gsap === 'undefined' || typeof ScrollTrigger === 'undefined') {
      console.warn('LaptopHUB: GSAP or ScrollTrigger not loaded yet.');
      return;
    }

    gsap.registerPlugin(ScrollTrigger);

    // 1. Initialize Lenis Smooth Scroll if available and motion allowed
    if (typeof Lenis !== 'undefined' && !prefersReducedMotion) {
      try {
        lenisInstance = new Lenis({
          duration: 1.15,
          easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
          direction: 'vertical',
          gestureDirection: 'vertical',
          smooth: true,
          smoothTouch: false,
          touchMultiplier: 1.5
        });

        window.lenis = lenisInstance;

        // Synchronize Lenis with GSAP ScrollTrigger
        lenisInstance.on('scroll', ScrollTrigger.update);

        gsap.ticker.add((time) => {
          lenisInstance.raf(time * 1000);
        });

        gsap.ticker.lagSmoothing(0);

        // Prevent Lenis smooth scrolling inside modals, cart drawer, and select lists
        const stopScrollElements = document.querySelectorAll('#cartDrawer, #loginModal, #myOrdersModal, #profileModal, .modal-overlay, #modalOverlay');
        stopScrollElements.forEach(el => {
          el.setAttribute('data-lenis-prevent', 'true');
        });
      } catch (err) {
        console.warn('LaptopHUB Lenis init notice:', err);
      }
    }

    // 2. Headings & Section Reveals
    initSectionReveals();

    // 3. Product Cards Batch Reveal
    initCardReveals();
  }

  function initSectionReveals() {
    if (prefersReducedMotion) return;

    // Headings and section headers
    const sectionHeaders = document.querySelectorAll('.sec-head, .sec-pre, .sec-title, .faq-head, .cta-band, .stats-row');
    sectionHeaders.forEach((el) => {
      gsap.fromTo(el,
        {
          opacity: 0,
          y: 35,
          filter: 'blur(4px)'
        },
        {
          opacity: 1,
          y: 0,
          filter: 'blur(0px)',
          duration: 0.8,
          ease: 'power2.out',
          scrollTrigger: {
            trigger: el,
            start: 'top 88%',
            toggleActions: 'play none none none',
            once: true
          }
        }
      );
    });

    // Catalog Toolbar & Sub-filters
    const catalogToolbar = document.querySelector('.catalog-toolbar');
    if (catalogToolbar) {
      gsap.fromTo(catalogToolbar,
        { opacity: 0, y: 25 },
        {
          opacity: 1,
          y: 0,
          duration: 0.65,
          ease: 'power2.out',
          scrollTrigger: {
            trigger: catalogToolbar,
            start: 'top 90%',
            once: true
          }
        }
      );
    }
  }

  function initCardReveals() {
    if (prefersReducedMotion) return;

    // Batch reveal for product cards
    if (typeof ScrollTrigger.batch === 'function') {
      ScrollTrigger.batch('.pcard', {
        interval: 0.06,
        batchMax: 6,
        onEnter: (batch) => {
          gsap.fromTo(batch,
            {
              opacity: 0,
              y: 40,
              scale: 0.98
            },
            {
              opacity: 1,
              y: 0,
              scale: 1,
              duration: 0.6,
              ease: 'power2.out',
              stagger: 0.05,
              overwrite: 'auto'
            }
          );
        },
        once: true
      });
    }
  }

  // Global helper to refresh ScrollTrigger when inventory filters or tab switcher update
  window.refreshScrollTriggers = function () {
    if (typeof ScrollTrigger !== 'undefined') {
      setTimeout(() => {
        ScrollTrigger.refresh();
        initCardReveals();
      }, 50);
    }
  };

  // Run on DOM ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initScrollAnimations);
  } else {
    initScrollAnimations();
  }
})();
