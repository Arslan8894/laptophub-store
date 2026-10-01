# -*- coding: utf-8 -*-
"""
Script to apply clean model names and structured spec displays to laptophub.html
"""

import sys

with open('laptophub.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Card CSS (.pcard-title and .pcard-chips)
old_card_css = """.pcard-title {
    font-family: var(--font-display);
    font-size: 1.05rem;
    font-weight: var(--fw-semibold);
    color: var(--heading);
    line-height: 1.3;
    margin-bottom: 0.4rem;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    transition: color 0.2s;
  }

  .pcard-specs-line {
    font-size: 0.78rem;
    color: var(--muted);
    line-height: 1.4;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    margin-bottom: 1.1rem;
    display: flex;
    align-items: center;
    gap: 6px;
  }
  .spec-dot {
    color: var(--border2);
    font-size: 0.7rem;
  }"""

new_card_css = """.pcard-title {
    font-family: var(--font-display);
    font-size: 1.05rem;
    font-weight: var(--fw-semibold);
    color: var(--heading);
    line-height: 1.35;
    margin-bottom: 0.5rem;
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
    overflow: hidden;
    text-overflow: ellipsis;
    min-height: 2.8em;
    transition: color 0.2s;
  }

  .pcard-chips {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    gap: 6px;
    margin-bottom: 1.1rem;
    min-height: 28px;
  }

  .pcard-chip {
    font-size: 0.72rem;
    font-weight: var(--fw-medium);
    padding: 3px 8px;
    background: var(--s2);
    border: 1px solid var(--border);
    border-radius: 6px;
    color: var(--text);
    white-space: nowrap;
    display: inline-flex;
    align-items: center;
    line-height: 1.3;
  }

  .pcard-chip.gpu-chip {
    background: rgba(168, 85, 247, 0.12);
    color: #c084fc;
    border-color: rgba(168, 85, 247, 0.3);
    font-weight: var(--fw-semibold);
  }
  [data-theme="light"] .pcard-chip.gpu-chip {
    background: rgba(147, 51, 234, 0.1);
    color: #7e22ce;
    border-color: rgba(147, 51, 234, 0.3);
  }"""

if old_card_css in content:
    content = content.replace(old_card_css, new_card_css, 1)
    print("Updated pcard CSS.")
else:
    print("Could not match old_card_css directly. Checking fallback.")

# 2. Add Modal Specifications CSS
old_modal_comment_css = """.modal-comment-box:focus { border-color: var(--blue); }"""

new_modal_specs_css = """.modal-comment-box:focus { border-color: var(--blue); }

  /* FULL SPECIFICATIONS 7-CATEGORY SECTION */
  .lmodal-specs-section {
    display: flex;
    flex-direction: column;
    gap: 10px;
    margin-top: 0.6rem;
    padding-top: 1.1rem;
    border-top: 1px solid var(--border);
  }
  .lmodal-specs-title {
    font-size: 0.95rem;
    font-weight: 700;
    color: var(--heading);
    display: inline-flex;
    align-items: center;
    gap: 8px;
    letter-spacing: -0.01em;
  }
  .lmodal-specs-title svg {
    color: var(--blue);
  }
  .lmodal-specs-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 10px;
  }
  @media (max-width: 768px) {
    .lmodal-specs-grid {
      grid-template-columns: 1fr;
    }
  }
  .spec-cat-block {
    background: var(--s2);
    border: 1px solid var(--border);
    border-radius: 9px;
    padding: 10px 12px;
    display: flex;
    flex-direction: column;
    gap: 7px;
  }
  .spec-cat-header {
    display: flex;
    align-items: center;
    gap: 7px;
    font-size: 0.74rem;
    font-weight: 700;
    color: var(--blue);
    text-transform: uppercase;
    letter-spacing: 0.05em;
    padding-bottom: 5px;
    border-bottom: 1px solid var(--border2);
  }
  .spec-cat-header svg {
    flex-shrink: 0;
  }
  .spec-rows-list {
    display: flex;
    flex-direction: column;
    gap: 5px;
  }
  .spec-row {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    font-size: 0.75rem;
    line-height: 1.35;
    gap: 10px;
  }
  .spec-key {
    color: var(--muted);
    font-weight: 500;
    flex-shrink: 0;
  }
  .spec-val {
    color: var(--heading);
    font-weight: 600;
    text-align: right;
    word-break: break-word;
  }
  .spec-val.unverified-val {
    color: var(--subtle);
    font-style: italic;
    font-weight: normal;
  }
  .spec-val.highlight-spec {
    color: var(--blue);
    font-weight: 700;
  }"""

if old_modal_comment_css in content:
    content = content.replace(old_modal_comment_css, new_modal_specs_css, 1)
    print("Added Modal Specs CSS.")

# 3. Add Modal Specs HTML in .lmodal-content
old_comment_html = """          <!-- CLIENT COMMENTS / DESIRED REQUEST SECTION -->
          <div class="spec-picker-section">
            <div class="spec-picker-header">
              <span class="spec-picker-title">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>
                Desired Specs / Custom Requests
              </span>
              <span style="font-size:0.72rem;color:var(--muted)">Optional</span>
            </div>
            <textarea class="modal-comment-box" id="lmodalComment" rows="2" placeholder="Tell us your desired additions (e.g. install Windows 11 Pro, apply fresh Arctic thermal paste, need Type-C hub, deliver on weekend)..."></textarea>
          </div>
        </div>"""

new_comment_with_specs_html = """          <!-- CLIENT COMMENTS / DESIRED REQUEST SECTION -->
          <div class="spec-picker-section">
            <div class="spec-picker-header">
              <span class="spec-picker-title">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>
                Desired Specs / Custom Requests
              </span>
              <span style="font-size:0.72rem;color:var(--muted)">Optional</span>
            </div>
            <textarea class="modal-comment-box" id="lmodalComment" rows="2" placeholder="Tell us your desired additions (e.g. install Windows 11 Pro, apply fresh Arctic thermal paste, need Type-C hub, deliver on weekend)..."></textarea>
          </div>

          <!-- FULL 7-CATEGORY SPECIFICATIONS SECTION -->
          <div class="lmodal-specs-section">
            <h4 class="lmodal-specs-title">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/><polyline points="10 9 9 9 8 9"/></svg>
              Full Specifications
            </h4>
            <div class="lmodal-specs-grid" id="lmodalSpecsGrid">
              <!-- Dynamically populated with 7 categories -->
            </div>
          </div>
        </div>"""

if old_comment_html in content:
    content = content.replace(old_comment_html, new_comment_with_specs_html, 1)
    print("Added Modal Specs HTML container.")
else:
    print("Could not match old_comment_html directly. Checking alternate.")

# 4. Update renderProducts() search and card generation
old_search_logic = """      // Search query
      if (searchQuery) {
        const q = searchQuery.toLowerCase();
        const haystack = (lap.name + ' ' + lap.brandName + ' ' + lap.cpu + ' ' + lap.display + ' ' + lap.gpu + ' ' + lap.category).toLowerCase();
        if (!haystack.includes(q)) return false;
      }"""

new_search_logic = """      // Search query (multi-token search matching clean name, legacy name, brand, processor, RAM, and SSD)
      if (searchQuery) {
        const q = searchQuery.toLowerCase().trim();
        const tokens = q.split(/\\s+/).filter(Boolean);
        const shortCpu = lap.shortSpecs ? `${lap.shortSpecs.cpuFamily} ${lap.shortSpecs.generation}` : '';
        const haystack = [
          lap.name,
          lap.legacyName || '',
          lap.brandName || lap.brand,
          lap.cpu || '',
          shortCpu,
          lap.fullSpecs?.performance?.processor || '',
          lap.display || '',
          lap.gpu || '',
          lap.category || '',
          lap.series || '',
          `${lap.ram}gb`,
          `${lap.ram} gb`,
          `${lap.storage}gb`,
          `${lap.storage} gb`,
          lap.storage >= 1000 ? '1tb 1 tb' : ''
        ].join(' ').toLowerCase();

        const matchesAll = tokens.every(tok => haystack.includes(tok));
        if (!matchesAll) return false;
      }"""

if old_search_logic in content:
    content = content.replace(old_search_logic, new_search_logic, 1)
    print("Updated search logic in renderProducts.")

old_card_gen = """    grid.innerHTML = filtered.map(lap => {
      const waMsg = encodeURIComponent(`Hi LaptopHUB! I am interested in purchasing the ${lap.name} (${lap.priceFormatted}). Please confirm availability!`);
      const cleanCpu = formatCardCpu(lap);
      const storText = lap.storage >= 1000 ? (lap.storage/1000)+' TB' : lap.storage+' GB';
      const condBadge = lap.condition ? lap.condition.split('·')[0].trim() : 'Like New (10/10)';
      return `
        <div class="pcard" data-brand="${lap.brand}" onclick="openLaptopModal(${lap.id}, event)" tabindex="0" onkeydown="handleCardKey(event, ${lap.id})" role="button" aria-label="View details for ${escapeHtml(lap.name)}">
          <div class="pcard-photo-wrap">
            <span class="pcard-cond-badge">${escapeHtml(condBadge)}</span>
            <img src="${lap.img}" alt="${escapeHtml(lap.name)}" class="pcard-photo" loading="lazy">
          </div>
          <div class="pcard-brand">${escapeHtml(lap.brandName || lap.brand)}</div>
          <h3 class="pcard-title" title="${escapeHtml(lap.name)}">${escapeHtml(lap.name)}</h3>
          <div class="pcard-specs-line">
            <span>${escapeHtml(cleanCpu)}</span>
            <span class="spec-dot">•</span>
            <span>${lap.ram} GB</span>
            <span class="spec-dot">•</span>
            <span>${storText}</span>
          </div>
          <div class="pcard-footer">"""

new_card_gen = """    grid.innerHTML = filtered.map(lap => {
      const waMsg = encodeURIComponent(`Hi LaptopHUB! I am interested in purchasing the ${lap.name} (${lap.priceFormatted}). Please confirm availability!`);
      const condBadge = lap.condition ? lap.condition.split('·')[0].trim() : 'Like New (10/10)';
      
      const cpuChip = (lap.shortSpecs && lap.shortSpecs.cpuFamily && lap.shortSpecs.generation)
        ? `${lap.shortSpecs.cpuFamily} · ${lap.shortSpecs.generation}`
        : formatCardCpu(lap);
      const ramGb = (lap.shortSpecs && lap.shortSpecs.ramGb) ? lap.shortSpecs.ramGb : lap.ram;
      const storGb = (lap.shortSpecs && lap.shortSpecs.storageGb) ? lap.shortSpecs.storageGb : lap.storage;
      const storChip = (storGb >= 1000 ? (storGb/1000) + ' TB' : storGb + ' GB') + ' SSD';
      const isDedGpu = lap.isDedicatedGpu || (lap.shortSpecs && lap.shortSpecs.isDedicatedGpu);

      return `
        <div class="pcard" data-brand="${lap.brand}" onclick="openLaptopModal(${lap.id}, event)" tabindex="0" onkeydown="handleCardKey(event, ${lap.id})" role="button" aria-label="View details for ${escapeHtml(lap.name)}">
          <div class="pcard-photo-wrap">
            <span class="pcard-cond-badge">${escapeHtml(condBadge)}</span>
            <img src="${lap.img}" alt="${escapeHtml(lap.name)}" class="pcard-photo" loading="lazy">
          </div>
          <div class="pcard-brand">${escapeHtml(lap.brandName || lap.brand)}</div>
          <h3 class="pcard-title" title="${escapeHtml(lap.name)}">${escapeHtml(lap.name)}</h3>
          <div class="pcard-chips">
            <span class="pcard-chip cpu-chip">${escapeHtml(cpuChip)}</span>
            <span class="pcard-chip ram-chip">${ramGb} GB RAM</span>
            <span class="pcard-chip stor-chip">${escapeHtml(storChip)}</span>
            ${isDedGpu ? `<span class="pcard-chip gpu-chip">Dedicated GPU</span>` : ''}
          </div>
          <div class="pcard-footer">"""

if old_card_gen in content:
    content = content.replace(old_card_gen, new_card_gen, 1)
    print("Updated card rendering with clean model name and 3-4 short spec chips.")

# 5. Add renderModalFullSpecs() and update updateModalPricingAndUI()
old_update_modal = """  function updateModalPricingAndUI() {
    if (!activeModalLaptop) return;
    const basePrice = activeModalLaptop.price;
    const baseRam = activeModalLaptop.ram;
    const baseStorage = activeModalLaptop.storage;

    const ramDelta = getRamDelta(modalSelectedRam, baseRam);
    const storageDelta = getStorageDelta(modalSelectedStorage, baseStorage);

    modalCalculatedPrice = Math.max(25000, basePrice + ramDelta + storageDelta);

    document.getElementById('lmodalPrice').textContent = `Rs ${modalCalculatedPrice.toLocaleString('en-PK')}`;
    document.getElementById('lblSelectedRam').textContent = `${modalSelectedRam} GB DDR4/DDR5`;
    const storText = modalSelectedStorage >= 1000 ? '1 TB NVMe' : `${modalSelectedStorage} GB NVMe`;
    document.getElementById('lblSelectedStorage').textContent = storText;"""

new_update_modal = """  function renderModalFullSpecs(lap, selectedRam, selectedStorage) {
    const container = document.getElementById('lmodalSpecsGrid');
    if (!container || !lap) return;

    const full = lap.fullSpecs || {};
    const perf = full.performance || {};
    const mem = full.memoryStorage || {};
    const disp = full.display || {};
    const graph = full.graphics || {};
    const conn = full.connectivityPorts || {};
    const build = full.batteryBuild || {};
    const cond = full.conditionWarranty || {};

    const curRam = selectedRam || lap.ram;
    const curStorage = selectedStorage || lap.storage;
    const storFormatted = curStorage >= 1000 ? '1 TB' : `${curStorage} GB`;

    const ramDisplay = `${curRam} GB ${mem.ramType || 'DDR4'}${mem.ramSpeed ? ' ' + mem.ramSpeed : ''}`;
    const storDisplay = `${storFormatted} ${mem.storageType || 'NVMe SSD'}`;

    const categories = [
      {
        title: "Performance",
        icon: `<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="4" width="16" height="16" rx="2"/><rect x="9" y="9" width="6" height="6"/><path d="M9 1v3M15 1v3M9 20v3M15 20v3M20 9h3M20 14h3M1 9h3M1 14h3"/></svg>`,
        rows: [
          { key: "Processor", val: perf.processor || lap.cpu },
          { key: "Cores & Threads", val: perf.coresThreads },
          { key: "Clock Speeds", val: perf.clocks },
          { key: "Cache", val: perf.cache }
        ]
      },
      {
        title: "Memory & Storage",
        icon: `<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="22" y1="12" x2="2" y2="12"/><path d="M5.45 5.11 2 12v6a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2v-6l-3.45-6.89A2 2 0 0 0 16.76 4H7.24a2 2 0 0 0-1.79 1.11z"/><line x1="6" y1="16" x2="6.01" y2="16"/><line x1="10" y1="16" x2="10.01" y2="16"/></svg>`,
        rows: [
          { key: "RAM (Selected)", val: ramDisplay, highlight: true },
          { key: "RAM Expansion", val: mem.ramSlots || (lap.isRamUpgradable ? 'Upgradable' : 'Soldered (Non-upgradable)') },
          { key: "Storage (Selected)", val: storDisplay, highlight: true },
          { key: "Drive Interface", val: mem.interface || lap.storageType },
          { key: "Transfer Speed", val: mem.readSpeed }
        ]
      },
      {
        title: "Display",
        icon: `<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="3" width="20" height="14" rx="2" ry="2"/><line x1="8" y1="21" x2="16" y2="21"/><line x1="12" y1="17" x2="12" y2="21"/></svg>`,
        rows: [
          { key: "Screen Size", val: disp.size },
          { key: "Resolution", val: disp.resolution },
          { key: "Panel Technology", val: disp.panelType },
          { key: "Refresh Rate", val: disp.refreshRate },
          { key: "Touch / Surface", val: disp.touchAntiGlare }
        ]
      },
      {
        title: "Graphics",
        icon: `<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m12 3-1.912 5.813a2 2 0 0 1-1.275 1.275L3 12l5.813 1.912a2 2 0 0 1 1.275 1.275L12 21l1.912-5.813a2 2 0 0 1 1.275-1.275L21 12l-5.813-1.912a2 2 0 0 1-1.275-1.275L12 3Z"/></svg>`,
        rows: [
          { key: "Graphics Model", val: graph.gpuName || lap.gpu },
          { key: "Architecture", val: graph.type || (lap.isDedicatedGpu ? 'Dedicated' : 'Integrated') },
          { key: "Dedicated VRAM", val: graph.vram }
        ]
      },
      {
        title: "Connectivity & Ports",
        icon: `<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></svg>`,
        rows: [
          { key: "External Ports", val: conn.ports },
          { key: "Wireless", val: conn.wireless }
        ]
      },
      {
        title: "Battery & Build",
        icon: `<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="1" y="6" width="18" height="12" rx="2"/><line x1="23" y1="11" x2="23" y2="13"/></svg>`,
        rows: [
          { key: "Battery", val: build.battery },
          { key: "Weight", val: build.weight },
          { key: "Keyboard", val: build.keyboard },
          { key: "Webcam & Mics", val: build.webcam },
          { key: "Operating System", val: build.os }
        ]
      },
      {
        title: "Condition & Warranty",
        icon: `<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>`,
        rows: [
          { key: "Condition Grade", val: cond.condition || lap.condition },
          { key: "Store Warranty", val: cond.warranty || lap.warranty }
        ]
      }
    ];

    container.innerHTML = categories.map(cat => {
      const validRows = cat.rows.filter(r => r.val && String(r.val).trim() !== '' && String(r.val).trim() !== '-');
      if (validRows.length === 0) return '';
      
      const rowsHtml = validRows.map(r => {
        const isUnverified = String(r.val).toLowerCase().includes('unverified');
        let valClass = isUnverified ? 'spec-val unverified-val' : 'spec-val';
        if (r.highlight) valClass += ' highlight-spec';
        return `
          <div class="spec-row">
            <span class="spec-key">${escapeHtml(r.key)}</span>
            <span class="${valClass}">${escapeHtml(r.val)}</span>
          </div>`;
      }).join('');

      return `
        <div class="spec-cat-block">
          <div class="spec-cat-header">
            ${cat.icon}
            <span>${escapeHtml(cat.title)}</span>
          </div>
          <div class="spec-rows-list">
            ${rowsHtml}
          </div>
        </div>`;
    }).join('');
  }

  function updateModalPricingAndUI() {
    if (!activeModalLaptop) return;
    const basePrice = activeModalLaptop.price;
    const baseRam = activeModalLaptop.ram;
    const baseStorage = activeModalLaptop.storage;

    const ramDelta = getRamDelta(modalSelectedRam, baseRam);
    const storageDelta = getStorageDelta(modalSelectedStorage, baseStorage);

    modalCalculatedPrice = Math.max(25000, basePrice + ramDelta + storageDelta);

    document.getElementById('lmodalPrice').textContent = `Rs ${modalCalculatedPrice.toLocaleString('en-PK')}`;
    const ramType = activeModalLaptop.fullSpecs?.memoryStorage?.ramType || 'DDR4';
    document.getElementById('lblSelectedRam').textContent = `${modalSelectedRam} GB ${ramType}`;
    const storType = activeModalLaptop.fullSpecs?.memoryStorage?.storageType || 'NVMe';
    const storText = modalSelectedStorage >= 1000 ? `1 TB ${storType}` : `${modalSelectedStorage} GB ${storType}`;
    document.getElementById('lblSelectedStorage').textContent = storText;

    // Dynamically update full specifications section to reflect selected upgrades
    renderModalFullSpecs(activeModalLaptop, modalSelectedRam, modalSelectedStorage);"""

if old_update_modal in content:
    content = content.replace(old_update_modal, new_update_modal, 1)
    print("Updated updateModalPricingAndUI with dynamic spec rendering.")

# 6. Update addModalItemToCart and orderModalViaWhatsApp to pass clean model name and exact configured specs
old_modal_cart = """    const storText = modalSelectedStorage >= 1000 ? '1TB' : `${modalSelectedStorage}GB`;

    // Add unique item entry or increment if identical specs exist
    const existing = cart.find(i => i.id === activeModalLaptop.id && i.ram === modalSelectedRam && i.storage === modalSelectedStorage && i.comment === comment);
    if (existing) {
      existing.qty++;
    } else {
      cart.push({
        id: activeModalLaptop.id,
        name: activeModalLaptop.name,
        price: modalCalculatedPrice,
        basePrice: activeModalLaptop.price,
        cpu: activeModalLaptop.cpu,
        ram: modalSelectedRam,
        storage: modalSelectedStorage,
        storageLabel: storText,
        comment: comment,
        img: activeModalLaptop.img,
        qty: 1
      });
    }

    saveCart();
    closeLaptopModal();
    showToast(`Added ${activeModalLaptop.name} (${modalSelectedRam}GB / ${storText}) to cart!`);"""

new_modal_cart = """    const storText = modalSelectedStorage >= 1000 ? '1 TB NVMe SSD' : `${modalSelectedStorage} GB NVMe SSD`;
    const ramText = `${modalSelectedRam} GB ${activeModalLaptop.fullSpecs?.memoryStorage?.ramType || 'RAM'}`;
    const cpuName = activeModalLaptop.fullSpecs?.performance?.processor || activeModalLaptop.cpu;

    // Add unique item entry or increment if identical specs exist
    const existing = cart.find(i => i.id === activeModalLaptop.id && i.ram === modalSelectedRam && i.storage === modalSelectedStorage && i.comment === comment);
    if (existing) {
      existing.qty++;
    } else {
      cart.push({
        id: activeModalLaptop.id,
        name: activeModalLaptop.name,
        price: modalCalculatedPrice,
        basePrice: activeModalLaptop.price,
        cpu: cpuName,
        ram: modalSelectedRam,
        ramLabel: ramText,
        storage: modalSelectedStorage,
        storageLabel: storText,
        comment: comment,
        img: activeModalLaptop.img,
        qty: 1
      });
    }

    saveCart();
    closeLaptopModal();
    showToast(`Added ${activeModalLaptop.name} (${ramText} / ${storText}) to cart!`);"""

if old_modal_cart in content:
    content = content.replace(old_modal_cart, new_modal_cart, 1)
    print("Updated addModalItemToCart.")

old_modal_wa = """  function orderModalViaWhatsApp() {
    if (!activeModalLaptop) return;
    const comment = document.getElementById('lmodalComment').value.trim();
    const storText = modalSelectedStorage >= 1000 ? '1TB NVMe' : `${modalSelectedStorage}GB NVMe`;

    let msg = `*Custom Laptop Inquiry — LaptopHUB Pakistan*%0A`;
    msg += `------------------------------------------%0A`;
    msg += `*Model:* ${encodeURIComponent(activeModalLaptop.name)}%0A`;
    msg += `*Processor:* ${encodeURIComponent(activeModalLaptop.cpu)}%0A`;
    msg += `*Selected RAM:* ${modalSelectedRam}GB%0A`;
    msg += `*Selected Storage:* ${storText}%0A`;
    msg += `*Configured Price:* Rs ${modalCalculatedPrice.toLocaleString('en-PK')}%0A`;
    msg += `*Condition:* ${encodeURIComponent(activeModalLaptop.condition)}%0A`;"""

new_modal_wa = """  function orderModalViaWhatsApp() {
    if (!activeModalLaptop) return;
    const comment = document.getElementById('lmodalComment').value.trim();
    const storText = modalSelectedStorage >= 1000 ? '1 TB NVMe SSD' : `${modalSelectedStorage} GB NVMe SSD`;
    const ramText = `${modalSelectedRam} GB ${activeModalLaptop.fullSpecs?.memoryStorage?.ramType || 'RAM'}`;
    const cpuName = activeModalLaptop.fullSpecs?.performance?.processor || activeModalLaptop.cpu;

    let msg = `*Custom Laptop Order — LaptopHUB Pakistan*%0A`;
    msg += `------------------------------------------%0A`;
    msg += `*Model:* ${encodeURIComponent(activeModalLaptop.name)}%0A`;
    msg += `*Processor:* ${encodeURIComponent(cpuName)}%0A`;
    msg += `*Selected RAM:* ${encodeURIComponent(ramText)}%0A`;
    msg += `*Selected Storage:* ${encodeURIComponent(storText)}%0A`;
    msg += `*Display:* ${encodeURIComponent(activeModalLaptop.display)}%0A`;
    msg += `*Graphics:* ${encodeURIComponent(activeModalLaptop.gpu)}%0A`;
    msg += `*Configured Cash Price:* Rs ${modalCalculatedPrice.toLocaleString('en-PK')}%0A`;
    msg += `*Condition:* ${encodeURIComponent(activeModalLaptop.condition)}%0A`;"""

if old_modal_wa in content:
    content = content.replace(old_modal_wa, new_modal_wa, 1)
    print("Updated orderModalViaWhatsApp.")

with open('laptophub.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Saved updated laptophub.html!")
