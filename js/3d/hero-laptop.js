/**
 * LaptopHUB - 3D Interactive Hero Laptop
 * Powered by Three.js
 * Features: Procedural high-detail metallic laptop, screen emissive texture,
 * mouse tracking with damping, idle floating, scroll tilt, touch drag, and performance culling.
 */

(function () {
  'use strict';

  // Check prefers-reduced-motion
  const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  function initHeroLaptop() {
    const container = document.getElementById('hero3dContainer');
    if (!container) return;

    // Check WebGL availability
    const canvas = document.createElement('canvas');
    const gl = canvas.getContext('webgl') || canvas.getContext('experimental-webgl');
    if (!gl) {
      container.classList.add('no-webgl-fallback');
      return;
    }

    const width = container.clientWidth || 540;
    const height = container.clientHeight || 460;

    // Scene, Camera, Renderer
    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(40, width / height, 0.1, 100);
    camera.position.set(0, 1.4, 5.2);

    const renderer = new THREE.WebGLRenderer({
      antialias: true,
      alpha: true,
      powerPreference: 'high-performance'
    });
    renderer.setSize(width, height);
    renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 2));
    renderer.toneMapping = THREE.ACESFilmicToneMapping;
    renderer.toneMappingExposure = 1.15;
    renderer.shadowMap.enabled = true;
    renderer.shadowMap.type = THREE.PCFSoftShadowMap;

    renderer.domElement.id = 'heroLaptopCanvas';
    renderer.domElement.style.width = '100%';
    renderer.domElement.style.height = '100%';
    renderer.domElement.style.display = 'block';
    container.innerHTML = '';
    container.appendChild(renderer.domElement);

    // Lighting
    const ambientLight = new THREE.AmbientLight(0xffffff, 0.7);
    scene.add(ambientLight);

    const dirLight = new THREE.DirectionalLight(0xffffff, 1.3);
    dirLight.position.set(4, 6, 4);
    dirLight.castShadow = true;
    dirLight.shadow.mapSize.width = 1024;
    dirLight.shadow.mapSize.height = 1024;
    dirLight.shadow.camera.near = 0.5;
    dirLight.shadow.camera.far = 15;
    dirLight.shadow.bias = -0.0005;
    scene.add(dirLight);

    // Accent Rim Light (matches brand --blue / #4c7cff)
    const rimLight = new THREE.DirectionalLight(0x4c7cff, 2.0);
    rimLight.position.set(-5, 3, -2);
    scene.add(rimLight);

    // Soft Front Fill
    const fillLight = new THREE.DirectionalLight(0x8da7ff, 0.6);
    fillLight.position.set(0, -2, 4);
    scene.add(fillLight);

    // Master Laptop Group
    const laptopGroup = new THREE.Group();
    laptopGroup.position.set(0, -0.2, 0);
    laptopGroup.rotation.y = -0.35; // Default aesthetic 3/4 turn
    laptopGroup.rotation.x = 0.15;
    scene.add(laptopGroup);

    // Materials
    // Aluminum body matching site theme: dark anodized titanium / space grey
    const bodyMaterial = new THREE.MeshStandardMaterial({
      color: 0x1b1e2a,
      metalness: 0.88,
      roughness: 0.22,
      envMapIntensity: 1.0
    });

    const bodyAccentMaterial = new THREE.MeshStandardMaterial({
      color: 0x0f1118,
      metalness: 0.7,
      roughness: 0.4
    });

    const chromeMaterial = new THREE.MeshStandardMaterial({
      color: 0xdde0ed,
      metalness: 0.95,
      roughness: 0.1
    });

    // 1. BASE CHASSIS
    const baseW = 3.2;
    const baseD = 2.15;
    const baseH = 0.11;
    const baseGeo = new THREE.BoxGeometry(baseW, baseH, baseD);
    const baseMesh = new THREE.Mesh(baseGeo, bodyMaterial);
    baseMesh.position.y = -baseH / 2;
    baseMesh.castShadow = true;
    baseMesh.receiveShadow = true;
    laptopGroup.add(baseMesh);

    // Keyboard well indent
    const wellW = 2.8;
    const wellD = 1.15;
    const wellH = 0.015;
    const wellGeo = new THREE.BoxGeometry(wellW, wellH, wellD);
    const wellMesh = new THREE.Mesh(wellGeo, bodyAccentMaterial);
    wellMesh.position.set(0, 0.005, -0.32);
    wellMesh.receiveShadow = true;
    laptopGroup.add(wellMesh);

    // Procedural Keyboard Keys (create a unified texture on canvas for high perf & glowing backlit legend)
    const kbCanvas = document.createElement('canvas');
    kbCanvas.width = 1024;
    kbCanvas.height = 512;
    const kbCtx = kbCanvas.getContext('2d');

    // KB Background
    kbCtx.fillStyle = '#0a0c12';
    kbCtx.fillRect(0, 0, 1024, 512);

    // Draw keyboard keys grid
    const rows = 6;
    const cols = 15;
    const keyPadX = 14;
    const keyPadY = 12;
    const keyW = (1024 - (cols + 1) * keyPadX) / cols;
    const keyH = (512 - (rows + 1) * keyPadY) / rows;

    for (let r = 0; r < rows; r++) {
      for (let c = 0; c < cols; c++) {
        // Spacebar and special keys layout variation
        let kw = keyW;
        let x = keyPadX + c * (keyW + keyPadX);
        let y = keyPadY + r * (keyH + keyPadY);

        if (r === 5 && c === 4) {
          kw = keyW * 5 + keyPadX * 4;
          c += 4;
        }

        // Keycap gradient
        const kg = kbCtx.createLinearGradient(x, y, x, y + keyH);
        kg.addColorStop(0, '#1c1f2d');
        kg.addColorStop(1, '#11131c');
        kbCtx.fillStyle = kg;

        // Rounded keycaps
        kbCtx.beginPath();
        const rad = 6;
        kbCtx.roundRect ? kbCtx.roundRect(x, y, kw, keyH, rad) : kbCtx.rect(x, y, kw, keyH);
        kbCtx.fill();

        // Keycap subtle border / glow
        kbCtx.strokeStyle = 'rgba(76, 124, 255, 0.22)';
        kbCtx.lineWidth = 1.5;
        kbCtx.stroke();
      }
    }

    const kbTexture = new THREE.CanvasTexture(kbCanvas);
    const kbPlaneGeo = new THREE.PlaneGeometry(wellW * 0.98, wellD * 0.96);
    const kbMaterial = new THREE.MeshStandardMaterial({
      map: kbTexture,
      roughness: 0.5,
      metalness: 0.4
    });
    const kbMesh = new THREE.Mesh(kbPlaneGeo, kbMaterial);
    kbMesh.rotation.x = -Math.PI / 2;
    kbMesh.position.set(0, 0.015, -0.32);
    laptopGroup.add(kbMesh);

    // Trackpad
    const padW = 1.15;
    const padD = 0.72;
    const padGeo = new THREE.BoxGeometry(padW, 0.008, padD);
    const padMaterial = new THREE.MeshStandardMaterial({
      color: 0x1f2334,
      metalness: 0.8,
      roughness: 0.25
    });
    const padMesh = new THREE.Mesh(padGeo, padMaterial);
    padMesh.position.set(0, 0.006, 0.58);
    laptopGroup.add(padMesh);

    // Trackpad border highlight
    const padEdges = new THREE.EdgesGeometry(padGeo);
    const padLine = new THREE.LineSegments(padEdges, new THREE.LineBasicMaterial({ color: 0x3a4260 }));
    padMesh.add(padLine);

    // Hinge
    const hingeGeo = new THREE.CylinderGeometry(0.045, 0.045, 2.4, 32);
    const hingeMesh = new THREE.Mesh(hingeGeo, chromeMaterial);
    hingeMesh.rotation.z = Math.PI / 2;
    hingeMesh.position.set(0, 0.02, -baseD / 2 + 0.04);
    laptopGroup.add(hingeMesh);

    // Rubber feet under chassis
    const footGeo = new THREE.CylinderGeometry(0.06, 0.06, 0.02, 16);
    const footMat = new THREE.MeshBasicMaterial({ color: 0x050608 });
    [
      [-baseW / 2 + 0.2, baseD / 2 - 0.2],
      [baseW / 2 - 0.2, baseD / 2 - 0.2],
      [-baseW / 2 + 0.2, -baseD / 2 + 0.2],
      [baseW / 2 - 0.2, -baseD / 2 + 0.2]
    ].forEach(([fx, fz]) => {
      const foot = new THREE.Mesh(footGeo, footMat);
      foot.position.set(fx, -baseH - 0.01, fz);
      laptopGroup.add(foot);
    });

    // 2. LID / SCREEN ASSEMBLY (Pivot at hinge)
    const screenHingeGroup = new THREE.Group();
    screenHingeGroup.position.set(0, 0.035, -baseD / 2 + 0.04);
    laptopGroup.add(screenHingeGroup);

    // Default opened angle: ~110 degrees
    const openAngle = Math.PI * 0.61;
    screenHingeGroup.rotation.x = openAngle;

    // Screen Lid Back
    const lidW = baseW;
    const lidH = baseD;
    const lidD = 0.06;
    const lidGeo = new THREE.BoxGeometry(lidW, lidH, lidD);
    const lidMesh = new THREE.Mesh(lidGeo, bodyMaterial);
    lidMesh.position.set(0, lidH / 2, -lidD / 2);
    lidMesh.castShadow = true;
    screenHingeGroup.add(lidMesh);

    // LaptopHUB Logo on back of lid
    const logoPlateGeo = new THREE.BoxGeometry(0.5, 0.5, 0.005);
    const logoPlateMat = new THREE.MeshStandardMaterial({
      color: 0x4c7cff,
      emissive: 0x3a6bf5,
      emissiveIntensity: 0.8,
      metalness: 0.9,
      roughness: 0.1
    });
    const logoPlate = new THREE.Mesh(logoPlateGeo, logoPlateMat);
    logoPlate.position.set(0, lidH / 2, -lidD - 0.001);
    screenHingeGroup.add(logoPlate);

    // Screen Bezel (Front)
    const bezelGeo = new THREE.BoxGeometry(lidW * 0.98, lidH * 0.98, 0.01);
    const bezelMat = new THREE.MeshBasicMaterial({ color: 0x050608 });
    const bezelMesh = new THREE.Mesh(bezelGeo, bezelMat);
    bezelMesh.position.set(0, lidH / 2, 0.005);
    screenHingeGroup.add(bezelMesh);

    // Screen Glass Display Canvas Texture
    const screenCanvas = document.createElement('canvas');
    screenCanvas.width = 1200;
    screenCanvas.height = 800;
    const sCtx = screenCanvas.getContext('2d');

    function drawScreenContent() {
      // Dark cyber background
      const grad = sCtx.createLinearGradient(0, 0, 1200, 800);
      grad.addColorStop(0, '#05070e');
      grad.addColorStop(0.5, '#090d1b');
      grad.addColorStop(1, '#070b16');
      sCtx.fillStyle = grad;
      sCtx.fillRect(0, 0, 1200, 800);

      // Grid lines
      sCtx.strokeStyle = 'rgba(76, 124, 255, 0.08)';
      sCtx.lineWidth = 1;
      for (let x = 0; x < 1200; x += 40) {
        sCtx.beginPath();
        sCtx.moveTo(x, 0);
        sCtx.lineTo(x, 800);
        sCtx.stroke();
      }
      for (let y = 0; y < 800; y += 40) {
        sCtx.beginPath();
        sCtx.moveTo(0, y);
        sCtx.lineTo(1200, y);
        sCtx.stroke();
      }

      // Ambient radial glow behind central hero
      const glow = sCtx.createRadialGradient(600, 360, 40, 600, 360, 420);
      glow.addColorStop(0, 'rgba(76, 124, 255, 0.35)');
      glow.addColorStop(0.6, 'rgba(16, 185, 129, 0.12)');
      glow.addColorStop(1, 'rgba(0, 0, 0, 0)');
      sCtx.fillStyle = glow;
      sCtx.fillRect(0, 0, 1200, 800);

      // Top Glass Bar
      sCtx.fillStyle = 'rgba(255, 255, 255, 0.06)';
      sCtx.fillRect(40, 30, 1120, 52);
      sCtx.strokeStyle = 'rgba(255, 255, 255, 0.12)';
      sCtx.lineWidth = 1.5;
      sCtx.strokeRect(40, 30, 1120, 52);

      // Window dots
      sCtx.fillStyle = '#ff5f56';
      sCtx.beginPath(); sCtx.arc(68, 56, 7, 0, Math.PI * 2); sCtx.fill();
      sCtx.fillStyle = '#ffbd2e';
      sCtx.beginPath(); sCtx.arc(92, 56, 7, 0, Math.PI * 2); sCtx.fill();
      sCtx.fillStyle = '#27c93f';
      sCtx.beginPath(); sCtx.arc(116, 56, 7, 0, Math.PI * 2); sCtx.fill();

      // Top bar title
      sCtx.font = '600 20px "Plus Jakarta Sans", sans-serif';
      sCtx.fillStyle = '#dde0ed';
      sCtx.fillText('LaptopHUB — Flagship Hardware Matrix', 150, 63);

      // Brand Chip
      sCtx.fillStyle = 'rgba(76, 124, 255, 0.25)';
      sCtx.fillRect(1000, 42, 140, 28);
      sCtx.strokeStyle = '#4c7cff';
      sCtx.strokeRect(1000, 42, 140, 28);
      sCtx.font = '700 13px "Plus Jakarta Sans", sans-serif';
      sCtx.fillStyle = '#60a5fa';
      sCtx.fillText('VERIFIED 100%', 1020, 61);

      // Main Feature Graphic Card
      sCtx.fillStyle = 'rgba(15, 20, 35, 0.85)';
      sCtx.fillRect(80, 120, 1040, 480);
      sCtx.strokeStyle = 'rgba(76, 124, 255, 0.35)';
      sCtx.lineWidth = 2;
      sCtx.strokeRect(80, 120, 1040, 480);

      // Title on Screen
      sCtx.font = '800 48px "Plus Jakarta Sans", sans-serif';
      sCtx.fillStyle = '#ffffff';
      sCtx.fillText('CERTIFIED ENTERPRISE', 130, 210);

      sCtx.font = '800 48px "Plus Jakarta Sans", sans-serif';
      const blueGrad = sCtx.createLinearGradient(130, 0, 750, 0);
      blueGrad.addColorStop(0, '#4c7cff');
      blueGrad.addColorStop(1, '#38bdf8');
      sCtx.fillStyle = blueGrad;
      sCtx.fillText('POWER & PRECISION', 130, 270);

      // Spec Chips
      const specs = [
        '⚡ Intel Core Ultra 9 / Ryzen 7 PRO',
        '💾 64GB DDR5 Dual-Channel',
        '🚀 2TB PCIe Gen4 NVMe 7000MB/s',
        '✨ 3.2K OLED 120Hz Calibrated',
        '🛡️ 1-Year Local Replacement Warranty'
      ];

      sCtx.font = '600 20px "Plus Jakarta Sans", sans-serif';
      specs.forEach((sp, i) => {
        const chipY = 320 + i * 44;
        sCtx.fillStyle = 'rgba(76, 124, 255, 0.12)';
        sCtx.fillRect(130, chipY - 26, 680, 36);
        sCtx.strokeStyle = 'rgba(76, 124, 255, 0.3)';
        sCtx.strokeRect(130, chipY - 26, 680, 36);

        sCtx.fillStyle = '#e2e8f0';
        sCtx.fillText(sp, 150, chipY - 2);
      });

      // Holographic Ring on Right
      sCtx.save();
      sCtx.translate(940, 360);
      sCtx.strokeStyle = '#4c7cff';
      sCtx.lineWidth = 4;
      sCtx.beginPath();
      sCtx.arc(0, 0, 100, 0, Math.PI * 1.5);
      sCtx.stroke();

      sCtx.strokeStyle = '#10b981';
      sCtx.lineWidth = 2;
      sCtx.beginPath();
      sCtx.arc(0, 0, 115, 0.5, Math.PI * 1.8);
      sCtx.stroke();

      sCtx.font = '800 36px "Plus Jakarta Sans", sans-serif';
      sCtx.fillStyle = '#ffffff';
      sCtx.textAlign = 'center';
      sCtx.fillText('69', 0, 5);
      sCtx.font = '600 15px "Plus Jakarta Sans", sans-serif';
      sCtx.fillStyle = '#94a3b8';
      sCtx.fillText('MODELS IN STOCK', 0, 32);
      sCtx.restore();

      // Bottom Status bar
      sCtx.fillStyle = 'rgba(255, 255, 255, 0.04)';
      sCtx.fillRect(40, 670, 1120, 50);
      sCtx.font = '600 16px "Plus Jakarta Sans", sans-serif';
      sCtx.fillStyle = '#10b981';
      sCtx.fillText('● Express Insured Delivery to Karachi, Lahore, Islamabad & Nationwide', 70, 702);
    }

    drawScreenContent();

    const screenTexture = new THREE.CanvasTexture(screenCanvas);
    screenTexture.generateMipmaps = true;
    screenTexture.minFilter = THREE.LinearMipmapLinearFilter;

    const screenMat = new THREE.MeshStandardMaterial({
      map: screenTexture,
      emissive: 0x4c7cff,
      emissiveMap: screenTexture,
      emissiveIntensity: 0.42,
      roughness: 0.12,
      metalness: 0.1
    });

    const screenGeo = new THREE.PlaneGeometry(lidW * 0.94, lidH * 0.94);
    const screenMesh = new THREE.Mesh(screenGeo, screenMat);
    screenMesh.position.set(0, lidH / 2, 0.012);
    screenHingeGroup.add(screenMesh);

    // Screen light casting soft illumination onto keyboard
    const screenGlowLight = new THREE.PointLight(0x4c7cff, 1.2, 3.5);
    screenGlowLight.position.set(0, lidH * 0.4, 0.4);
    screenHingeGroup.add(screenGlowLight);

    // Ground Shadow (Circular soft gradient)
    const shadowGeo = new THREE.PlaneGeometry(4.5, 3.5);
    const shadowCanvas = document.createElement('canvas');
    shadowCanvas.width = 256;
    shadowCanvas.height = 256;
    const shadowCtx = shadowCanvas.getContext('2d');
    const shadowGrad = shadowCtx.createRadialGradient(128, 128, 10, 128, 128, 120);
    shadowGrad.addColorStop(0, 'rgba(0, 0, 0, 0.65)');
    shadowGrad.addColorStop(0.5, 'rgba(0, 0, 0, 0.25)');
    shadowGrad.addColorStop(1, 'rgba(0, 0, 0, 0)');
    shadowCtx.fillStyle = shadowGrad;
    shadowCtx.fillRect(0, 0, 256, 256);

    const shadowTex = new THREE.CanvasTexture(shadowCanvas);
    const shadowMat = new THREE.MeshBasicMaterial({
      map: shadowTex,
      transparent: true,
      depthWrite: false
    });
    const shadowMesh = new THREE.Mesh(shadowGeo, shadowMat);
    shadowMesh.rotation.x = -Math.PI / 2;
    shadowMesh.position.set(0, -baseH - 0.05, 0.1);
    scene.add(shadowMesh);

    // Interaction & Animation State
    const mouse = { x: 0, y: 0, targetX: 0, targetY: 0 };
    let scrollTilt = 0;
    let isDragging = false;
    let dragStartX = 0;
    let dragStartY = 0;
    let dragRotY = 0;
    let dragRotX = 0;
    let isVisible = true;

    // Track mouse over hero section and window
    function onMouseMove(e) {
      if (prefersReducedMotion) return;
      const rect = container.getBoundingClientRect();
      // Normalized between -1 and 1
      const cx = rect.left + rect.width / 2;
      const cy = rect.top + rect.height / 2;
      mouse.targetX = (e.clientX - cx) / (window.innerWidth * 0.5);
      mouse.targetY = (e.clientY - cy) / (window.innerHeight * 0.5);
    }
    window.addEventListener('mousemove', onMouseMove, { passive: true });

    // Touch & Mouse Drag to inspect laptop
    container.addEventListener('mousedown', (e) => {
      isDragging = true;
      dragStartX = e.clientX;
      dragStartY = e.clientY;
      dragRotY = laptopGroup.rotation.y;
      dragRotX = laptopGroup.rotation.x;
      container.style.cursor = 'grabbing';
    });

    window.addEventListener('mouseup', () => {
      if (isDragging) {
        isDragging = false;
        container.style.cursor = 'grab';
      }
    });

    window.addEventListener('mousemove', (e) => {
      if (!isDragging) return;
      const dx = (e.clientX - dragStartX) * 0.008;
      const dy = (e.clientY - dragStartY) * 0.008;
      laptopGroup.rotation.y = dragRotY + dx;
      laptopGroup.rotation.x = THREE.MathUtils.clamp(dragRotX + dy, -0.4, 0.6);
    });

    // Touch support for mobile
    let touchStartX = 0;
    let touchStartY = 0;
    container.addEventListener('touchstart', (e) => {
      if (e.touches.length === 1) {
        touchStartX = e.touches[0].clientX;
        touchStartY = e.touches[0].clientY;
        dragRotY = laptopGroup.rotation.y;
        dragRotX = laptopGroup.rotation.x;
      }
    }, { passive: true });

    container.addEventListener('touchmove', (e) => {
      if (e.touches.length === 1) {
        const dx = (e.touches[0].clientX - touchStartX) * 0.01;
        const dy = (e.touches[0].clientY - touchStartY) * 0.01;
        laptopGroup.rotation.y = dragRotY + dx;
        laptopGroup.rotation.x = THREE.MathUtils.clamp(dragRotX + dy, -0.4, 0.6);
      }
    }, { passive: true });

    // Scroll Tilt calculation
    function onScroll() {
      const scrollY = window.scrollY || window.pageYOffset;
      const heroHeight = container.closest('.hero') ? container.closest('.hero').offsetHeight : 600;
      const progress = Math.min(scrollY / heroHeight, 1.5);
      scrollTilt = progress * 0.35; // Tilt upwards smoothly
    }
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();

    // Resize Handler
    function onResize() {
      const w = container.clientWidth || 540;
      const h = container.clientHeight || 460;
      camera.aspect = w / h;
      camera.updateProjectionMatrix();
      renderer.setSize(w, h);
    }
    window.addEventListener('resize', onResize);

    // Performance Culling via IntersectionObserver (pause rendering when scrolled offscreen)
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        isVisible = entry.isIntersecting;
      });
    }, { threshold: 0.05 });
    observer.observe(container);

    // Animation Loop
    let clock = new THREE.Clock();

    function animate() {
      requestAnimationFrame(animate);

      if (!isVisible) return; // Save GPU/CPU cycles when offscreen

      const delta = clock.getDelta();
      const elapsed = clock.getElapsedTime();

      if (!isDragging) {
        // Smooth lerp mouse target
        mouse.x += (mouse.targetX - mouse.x) * 0.06;
        mouse.y += (mouse.targetY - mouse.y) * 0.06;

        if (!prefersReducedMotion) {
          // Slow aesthetic idle floating rotation
          const idleY = -0.35 + Math.sin(elapsed * 0.75) * 0.08;
          const idleX = 0.16 + Math.cos(elapsed * 0.6) * 0.04;
          const idleZ = Math.sin(elapsed * 0.5) * 0.02;

          laptopGroup.rotation.y += (idleY + mouse.x * 0.45 - laptopGroup.rotation.y) * 0.08;
          laptopGroup.rotation.x += (idleX - mouse.y * 0.35 + scrollTilt - laptopGroup.rotation.x) * 0.08;
          laptopGroup.rotation.z += (idleZ - mouse.x * 0.15 - laptopGroup.rotation.z) * 0.08;

          // Subtle floating height
          laptopGroup.position.y = -0.18 + Math.sin(elapsed * 1.2) * 0.04;
        } else {
          laptopGroup.rotation.y = -0.35;
          laptopGroup.rotation.x = 0.16;
        }
      }

      renderer.render(scene, camera);
    }

    container.style.cursor = 'grab';
    animate();
  }

  // Auto-init on DOMContentLoaded or immediate if ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initHeroLaptop);
  } else {
    initHeroLaptop();
  }
})();
