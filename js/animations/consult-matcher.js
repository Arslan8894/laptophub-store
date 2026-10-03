/**
 * LaptopHUB - Hardware Matcher / Quick Consultation (js/animations/consult-matcher.js)
 * High-performance, lightweight hardware matching from LAPTOPS_INVENTORY.
 */

(function () {
  'use strict';

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
      matches = inventory.filter(l => (l.gpu && (l.gpu.includes('RTX') || l.gpu.includes('GTX')) || l.badge === 'Gaming Flagship' || (l.useCases && l.useCases.includes('gaming')))).slice(0, 4);
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
            <button class="glass-pill" style="padding:5px 14px;font-size:0.8rem;font-weight:600;font-family:inherit;background:var(--blue-dim);color:var(--blue);border:1px solid var(--border2);cursor:pointer;" onclick="event.stopPropagation();openProductPage(${l.id})">
              Details →
            </button>
          </div>
        </div>
      `;
    }).join('');
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initConsultChips);
  } else {
    initConsultChips();
  }
})();
