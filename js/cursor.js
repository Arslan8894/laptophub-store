/**
 * LaptopHUB — Universal Custom Cursor System (js/cursor.js)
 * Loaded globally across all pages (Home, Consult Me, Product, Admin, Modals)
 * - Trailing ring + pinpoint dot
 * - 0% idle CPU (sleeps when stationary)
 * - Auto-detects hover targets on interactive elements
 * - Completely disabled on mobile and touch devices
 * - Preserves state across modal dialogs, overlays, and drawer interactions
 */

(function(window) {
  'use strict';

  // Only initialize on desktop devices with a fine pointer (not touch)
  const isFineDesktop = () => {
    return window.matchMedia &&
           window.matchMedia('(hover: hover) and (pointer: fine)').matches &&
           !('ontouchstart' in window) &&
           (!navigator.maxTouchPoints || navigator.maxTouchPoints === 0);
  };

  if (!isFineDesktop()) return;

  function initCursor() {
    let dot = document.getElementById('cursor-dot');
    let ring = document.getElementById('cursor-ring');

    if (!dot) {
      dot = document.createElement('div');
      dot.id = 'cursor-dot';
      dot.setAttribute('aria-hidden', 'true');
      document.body.appendChild(dot);
    }

    if (!ring) {
      ring = document.createElement('div');
      ring.id = 'cursor-ring';
      ring.setAttribute('aria-hidden', 'true');
      document.body.appendChild(ring);
    }

    let mouseX = -100, mouseY = -100;
    let ringX = -100, ringY = -100;
    let hasMoved = false;
    let isVisible = false;
    let ringRaf = null;

    function showCursor() {
      if (!hasMoved) return;
      dot.style.opacity = '1';
      ring.style.opacity = '0.6';
      isVisible = true;
    }

    function hideCursor() {
      dot.style.opacity = '0';
      ring.style.opacity = '0';
      isVisible = false;
    }

    function stepRing() {
      if (!hasMoved) {
        ringRaf = null;
        return;
      }
      const dx = mouseX - ringX;
      const dy = mouseY - ringY;
      if (Math.abs(dx) > 0.2 || Math.abs(dy) > 0.2) {
        ringX += dx * 0.45;
        ringY += dy * 0.45;
        ring.style.transform = `translate3d(${ringX.toFixed(1)}px, ${ringY.toFixed(1)}px, 0)`;
        ringRaf = requestAnimationFrame(stepRing);
      } else {
        ringX = mouseX;
        ringY = mouseY;
        ring.style.transform = `translate3d(${ringX}px, ${ringY}px, 0)`;
        ringRaf = null; // Sleep when stationary! Zero CPU drain
      }
    }

    window.addEventListener('mousemove', e => {
      mouseX = e.clientX;
      mouseY = e.clientY;
      if (!hasMoved) {
        hasMoved = true;
        ringX = mouseX;
        ringY = mouseY;
        document.body.classList.add('custom-cursor-active');
        showCursor();
      }
      dot.style.transform = `translate3d(${mouseX}px, ${mouseY}px, 0)`;
      if (!isVisible) showCursor();
      if (!ringRaf) {
        ringRaf = requestAnimationFrame(stepRing);
      }
    }, { passive: true });

    document.addEventListener('mouseleave', () => {
      hideCursor();
    }, { passive: true });

    document.addEventListener('mouseenter', () => {
      if (hasMoved) showCursor();
    }, { passive: true });

    const hoverSelectors = [
      'a',
      'button',
      '[role="button"]',
      'input',
      'select',
      'textarea',
      'label',
      '.pcard',
      '.hex-btn',
      '.btn-p',
      '.btn-s',
      '.btn-wa',
      '.btn-cod',
      '.nav-btn',
      '.glass-circle-btn',
      '.option-tile',
      '.filter-btn',
      '.pill-filter',
      '.cart-item',
      '.thumb-btn',
      '.faq-item',
      '.support-btn',
      '.theme-toggle-btn',
      '.step-label',
      '.clickable',
      '.auth-tab',
      '[onclick]'
    ].join(', ');

    let isHovering = false;

    document.addEventListener('mouseover', e => {
      if (e.target && e.target.closest && e.target.closest(hoverSelectors)) {
        if (!isHovering) {
          isHovering = true;
          dot.classList.add('hovering');
          ring.classList.add('hovering');
        }
      }
    }, { passive: true });

    document.addEventListener('mouseout', e => {
      if (e.target && e.target.closest && e.target.closest(hoverSelectors)) {
        if (e.relatedTarget && e.relatedTarget.closest && e.relatedTarget.closest(hoverSelectors)) return;
        if (isHovering) {
          isHovering = false;
          dot.classList.remove('hovering');
          ring.classList.remove('hovering');
        }
      }
    }, { passive: true });

    document.addEventListener('mousedown', () => {
      dot.classList.add('clicking');
      ring.classList.add('clicking');
    }, { passive: true });

    document.addEventListener('mouseup', () => {
      dot.classList.remove('clicking');
      ring.classList.remove('clicking');
    }, { passive: true });

    window.LHCursor = {
      show: showCursor,
      hide: hideCursor
    };
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initCursor);
  } else {
    initCursor();
  }
})(window);
