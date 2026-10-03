/**
 * LaptopHUB - Lenis Smooth Scroll & GSAP ScrollTrigger Orchestrator
 * High-performance, zero-stutter configuration.
 */

(function () {
  'use strict';

  const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  let lenisInstance = null;

  function initScrollAnimations() {
    // Ensure GSAP and ScrollTrigger are loaded
    if (typeof gsap === 'undefined' || typeof ScrollTrigger === 'undefined') {
      return;
    }

    gsap.registerPlugin(ScrollTrigger);

    // 1. Initialize Lenis with lightweight, snappy configuration
    if (typeof Lenis !== 'undefined' && !prefersReducedMotion) {
      try {
        lenisInstance = new Lenis({
          duration: 0.8,
          easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
          orientation: 'vertical',
          gestureOrientation: 'vertical',
          smoothWheel: true,
          syncTouch: false,
          touchMultiplier: 1.0
        });

        window.lenis = lenisInstance;

        // Synchronize Lenis with GSAP ScrollTrigger
        lenisInstance.on('scroll', ScrollTrigger.update);

        gsap.ticker.add((time) => {
          lenisInstance.raf(time * 1000);
        });

        // Healthy lag smoothing prevents scroll freezing on frame drops
        gsap.ticker.lagSmoothing(500, 33);

        // Prevent Lenis smooth scrolling inside modals, drawers, and form dialogs
        const stopScrollElements = document.querySelectorAll(
          '#cartDrawer, #loginModal, #myOrdersModal, #profileModal, .modal-overlay, #modalOverlay'
        );
        stopScrollElements.forEach(el => {
          el.setAttribute('data-lenis-prevent', 'true');
        });
      } catch (err) {
        console.warn('LaptopHUB Lenis notice:', err);
      }
    }

    // 2. Headings & Section Reveals (pure opacity and transform, NO expensive filter:blur)
    initSectionReveals();

    // 3. Product Cards Batch Reveal
    initCardReveals();
  }

  function initSectionReveals() {
    if (prefersReducedMotion) return;

    // Headings and section headers - animate only opacity and translateY (GPU-composited)
    const sectionHeaders = document.querySelectorAll('.sec-head, .sec-pre, .sec-title, .faq-head, .cta-band, .stats-row');
    sectionHeaders.forEach((el) => {
      gsap.fromTo(el,
        {
          opacity: 0,
          y: 24
        },
        {
          opacity: 1,
          y: 0,
          duration: 0.55,
          ease: 'power2.out',
          clearProps: 'transform,opacity',
          scrollTrigger: {
            trigger: el,
            start: 'top 92%',
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
        { opacity: 0, y: 16 },
        {
          opacity: 1,
          y: 0,
          duration: 0.5,
          ease: 'power2.out',
          clearProps: 'transform,opacity',
          scrollTrigger: {
            trigger: catalogToolbar,
            start: 'top 94%',
            once: true
          }
        }
      );
    }
  }

  function initCardReveals() {
    if (prefersReducedMotion) return;

    // Fast, lightweight batch reveal for visible product cards
    if (typeof ScrollTrigger.batch === 'function') {
      ScrollTrigger.batch('.pcard', {
        interval: 0.04,
        batchMax: 6,
        onEnter: (batch) => {
          gsap.fromTo(batch,
            {
              opacity: 0,
              y: 20
            },
            {
              opacity: 1,
              y: 0,
              duration: 0.4,
              ease: 'power2.out',
              stagger: 0.04,
              clearProps: 'opacity,transform',
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
      requestAnimationFrame(() => {
        ScrollTrigger.refresh();
      });
    }
  };

  // Run on DOM ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initScrollAnimations);
  } else {
    initScrollAnimations();
  }
})();
