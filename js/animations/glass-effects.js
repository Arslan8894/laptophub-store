/**
 * LaptopHUB - Interactive Liquid Glass Effects (js/animations/glass-effects.js)
 * Step 5: Specular light follower across glass surfaces, subtle button squish,
 * and pure CSS lightweight glass depth. Zero scroll lag, 100% native performance.
 */

(function () {
  'use strict';

  function initGlassEffects() {
    // Only on fine pointers (desktop mouse)
    const isPointerFine = window.matchMedia('(hover: hover) and (pointer: fine)').matches;
    if (!isPointerFine) return;

    // Specular radial light follower on glass elements
    const glassTargets = document.querySelectorAll(
      '.liquid-glass-nav, .consult-glass-card, .glass-pill, .glass-circle-btn, .pcard'
    );

    glassTargets.forEach(el => {
      el.addEventListener('pointermove', (e) => {
        const rect = el.getBoundingClientRect();
        const x = ((e.clientX - rect.left) / rect.width) * 100;
        const y = ((e.clientY - rect.top) / rect.height) * 100;
        el.style.setProperty('--glass-glare-x', `${x.toFixed(1)}%`);
        el.style.setProperty('--glass-glare-y', `${y.toFixed(1)}%`);
      }, { passive: true });

      el.addEventListener('pointerleave', () => {
        el.style.setProperty('--glass-glare-x', '50%');
        el.style.setProperty('--glass-glare-y', '20%');
      }, { passive: true });
    });

    // Subtle press squish micro-interactions for buttons
    const interactiveButtons = document.querySelectorAll(
      '.btn-p, .btn-s, .glass-circle-btn, .btn-launch-wizard, .consult-chip, .filter-btn, .pill-filter'
    );

    interactiveButtons.forEach(btn => {
      btn.classList.add('glass-squish');
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initGlassEffects);
  } else {
    initGlassEffects();
  }
})();
