/**
 * LaptopHUB Side-by-Side Comparison System
 * Allows selecting up to 3 laptops from catalog and comparing specs side-by-side.
 */

(function() {
  let compareList = [];
  try {
    compareList = JSON.parse(sessionStorage.getItem('lh_compare_list') || '[]');
  } catch (_) {
    compareList = [];
  }

  function saveCompare() {
    try {
      sessionStorage.setItem('lh_compare_list', JSON.stringify(compareList));
    } catch (_) {}
  }

  function getInventory() {
    return window.inventory || (typeof LAPTOPS_INVENTORY !== 'undefined' ? LAPTOPS_INVENTORY : []);
  }

  window.toggleCompare = function(lapId, event) {
    if (event) {
      event.preventDefault();
      event.stopPropagation();
    }
    const inv = getInventory();
    const lap = inv.find(l => l.id === lapId);
    if (!lap) return;

    const idx = compareList.indexOf(lapId);
    if (idx > -1) {
      compareList.splice(idx, 1);
      if (typeof showToast === 'function') {
        showToast(`Removed ${lap.name} from comparison`);
      }
    } else {
      if (compareList.length >= 3) {
        if (typeof showToast === 'function') {
          showToast('You can compare up to 3 laptops at a time.');
        }
        return;
      }
      compareList.push(lapId);
      if (typeof showToast === 'function') {
        showToast(`Added ${lap.name} to comparison!`);
      }
    }

    saveCompare();
    updateCompareUI();
  };

  window.removeFromCompare = function(lapId, event) {
    if (event) {
      event.preventDefault();
      event.stopPropagation();
    }
    const idx = compareList.indexOf(lapId);
    if (idx > -1) {
      compareList.splice(idx, 1);
      saveCompare();
      updateCompareUI();
      // If modal is open, re-render modal or close if empty
      const modal = document.getElementById('compareModal');
      if (modal && modal.classList.contains('open')) {
        if (compareList.length >= 2) {
          renderCompareMatrix();
        } else {
          closeCompareModal();
        }
      }
    }
  };

  window.clearCompare = function() {
    compareList = [];
    saveCompare();
    updateCompareUI();
    closeCompareModal();
    if (typeof showToast === 'function') {
      showToast('Comparison cleared');
    }
  };

  window.updateCompareUI = function() {
    const dock = document.getElementById('compareDock');
    const itemsWrap = document.getElementById('compareDockItems');
    const badge = document.getElementById('compareCountBadge');
    if (!dock || !itemsWrap) return;

    const inv = getInventory();
    const count = compareList.length;

    // Update buttons in catalog
    document.querySelectorAll('.btn-card-compare').forEach(btn => {
      const card = btn.closest('.pcard');
      if (card) {
        const id = parseInt(card.getAttribute('data-laptop-id'), 10);
        if (compareList.includes(id)) {
          btn.classList.add('active');
          btn.setAttribute('title', 'Remove from comparison');
        } else {
          btn.classList.remove('active');
          btn.setAttribute('title', 'Compare laptop');
        }
      }
    });

    if (badge) {
      badge.textContent = `${count}/3`;
    }

    if (count === 0) {
      dock.classList.remove('visible');
      itemsWrap.innerHTML = '';
      return;
    }

    dock.classList.add('visible');

    itemsWrap.innerHTML = compareList.map(id => {
      const lap = inv.find(l => l.id === id);
      if (!lap) return '';
      const img = lap.processedImg || lap.img;
      return `
        <div class="compare-chip">
          <img src="${img}" alt="${escapeHtml(lap.name)}" class="compare-chip-img" loading="lazy">
          <span class="compare-chip-name" title="${escapeHtml(lap.name)}">${escapeHtml(lap.name)}</span>
          <span class="compare-chip-price">${lap.priceFormatted}</span>
          <button type="button" class="compare-chip-remove" onclick="removeFromCompare(${lap.id}, event)" title="Remove">✕</button>
        </div>
      `;
    }).join('');
  };

  window.openCompareModal = function() {
    if (compareList.length < 2) {
      if (typeof showToast === 'function') {
        showToast('Please select at least 2 laptops to compare!');
      }
      return;
    }
    renderCompareMatrix();
    const modal = document.getElementById('compareModal');
    if (modal) {
      modal.classList.add('open');
      document.body.classList.add('modal-open');
    }
  };

  window.closeCompareModal = function() {
    const modal = document.getElementById('compareModal');
    if (modal) {
      modal.classList.remove('open');
      const openModals = document.querySelectorAll('#loginModal.open, #checkoutModal.open, #orderConfirmModal.open, #myOrdersModal.open, #profileModal.open');
      if (openModals.length === 0) {
        document.body.classList.remove('modal-open');
        document.body.style.overflow = '';
      }
    }
  };

  function renderCompareMatrix() {
    const tableWrap = document.getElementById('compareTableContainer');
    if (!tableWrap) return;

    const inv = getInventory();
    const laps = compareList.map(id => inv.find(l => l.id === id)).filter(Boolean);
    if (laps.length === 0) return;

    const formatCpu = (lap) => {
      if (lap.shortSpecs && lap.shortSpecs.cpuFamily && lap.shortSpecs.generation) {
        return `${lap.shortSpecs.cpuFamily} · ${lap.shortSpecs.generation}`;
      }
      return lap.cpu || 'Multi-Core Processor';
    };

    const formatRam = (lap) => {
      const base = `${lap.ram} GB`;
      if (lap.isRamUpgradable && lap.ramUpgradeOptions && lap.ramUpgradeOptions.length) {
        const maxRam = Math.max(...lap.ramUpgradeOptions);
        return `<span class="compare-spec-highlight">${base}</span> (Upgradable to ${maxRam} GB)`;
      }
      return `${base} (High-Speed LPDDR)`;
    };

    const formatStorage = (lap) => {
      const stor = lap.storage >= 1000 ? `${lap.storage/1000} TB` : `${lap.storage} GB`;
      const type = lap.storageType || 'NVMe PCIe SSD';
      return `<span class="compare-spec-highlight">${stor}</span> ${type}`;
    };

    const formatGpu = (lap) => {
      if (lap.isDedicatedGpu || lap.gpuType === 'rtx' || lap.gpuType === 'discrete') {
        return `<span class="compare-badge-pill compare-badge-green">Dedicated ${escapeHtml(lap.gpuModel || lap.gpu || 'GPU')}</span>`;
      }
      return `<span class="compare-badge-pill">${escapeHtml(lap.gpuModel || lap.gpu || 'Integrated Graphics')}</span>`;
    };

    const html = `
      <table class="compare-table">
        <thead>
          <tr>
            <th class="feature-label">Model</th>
            ${laps.map(lap => `
              <th class="compare-hero-col">
                <div class="compare-hero-img-wrap">
                  <img src="${lap.processedImg || lap.img}" alt="${escapeHtml(lap.name)}" class="compare-hero-img">
                </div>
                <div class="compare-hero-name">${escapeHtml(lap.name)}</div>
                <div class="compare-hero-price">${lap.priceFormatted}</div>
                <div class="compare-hero-actions">
                  <button type="button" class="btn-card-view" onclick="openProductPage(${lap.id}, event)" style="padding:0.45rem 0.8rem;font-size:0.8rem">
                    <span>Details</span>
                  </button>
                  <button type="button" class="btn-card-wa" onclick="orderCardViaWhatsApp(${lap.id}, event)" title="Order on WhatsApp" style="width:32px;height:32px">
                    <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>
                  </button>
                  <button type="button" class="compare-chip-remove" onclick="removeFromCompare(${lap.id}, event)" title="Remove from compare" style="margin-left:4px">✕</button>
                </div>
              </th>
            `).join('')}
          </tr>
        </thead>
        <tbody>
          <tr>
            <th class="feature-label">Brand & Category</th>
            ${laps.map(lap => `<td class="feature-val"><strong>${escapeHtml(lap.brandName || lap.brand)}</strong> · ${escapeHtml(lap.category || 'Ultrabook')}</td>`).join('')}
          </tr>
          <tr>
            <th class="feature-label">Processor (CPU)</th>
            ${laps.map(lap => `<td class="feature-val">${escapeHtml(formatCpu(lap))}<br><small style="color:var(--muted)">${escapeHtml(lap.cpu || '')}</small></td>`).join('')}
          </tr>
          <tr>
            <th class="feature-label">Generation</th>
            ${laps.map(lap => `<td class="feature-val"><span class="compare-spec-highlight">${escapeHtml(lap.gen || 'Standard')}</span> Generation</td>`).join('')}
          </tr>
          <tr>
            <th class="feature-label">RAM Memory</th>
            ${laps.map(lap => `<td class="feature-val">${formatRam(lap)}</td>`).join('')}
          </tr>
          <tr>
            <th class="feature-label">Storage Drive</th>
            ${laps.map(lap => `<td class="feature-val">${formatStorage(lap)}</td>`).join('')}
          </tr>
          <tr>
            <th class="feature-label">Display & Screen</th>
            ${laps.map(lap => `<td class="feature-val">${escapeHtml(lap.display || 'FHD IPS')}</td>`).join('')}
          </tr>
          <tr>
            <th class="feature-label">Graphics (GPU)</th>
            ${laps.map(lap => `<td class="feature-val">${formatGpu(lap)}</td>`).join('')}
          </tr>
          <tr>
            <th class="feature-label">Condition Rating</th>
            ${laps.map(lap => `<td class="feature-val">${escapeHtml(lap.condition || 'Like New (10/10) · Certified')}</td>`).join('')}
          </tr>
          <tr>
            <th class="feature-label">Warranty Support</th>
            ${laps.map(lap => `<td class="feature-val">🛡️ ${escapeHtml(lap.warranty || '1 Year Local + 7 Days Checking')}</td>`).join('')}
          </tr>
        </tbody>
      </table>
    `;

    tableWrap.innerHTML = html;
  }

  function escapeHtml(str) {
    if (!str) return '';
    return String(str)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#39;');
  }

  // Keyboard and click outside handling
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
      const modal = document.getElementById('compareModal');
      if (modal && modal.classList.contains('open')) {
        closeCompareModal();
      }
    }
  });

  document.addEventListener('click', (e) => {
    const modal = document.getElementById('compareModal');
    if (modal && modal.classList.contains('open') && e.target === modal) {
      closeCompareModal();
    }
  });

  // Global initialization hook
  window.initCompareSystem = function() {
    updateCompareUI();
  };

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', updateCompareUI);
  } else {
    updateCompareUI();
  }
})();
