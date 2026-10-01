import os

images_dir = r"c:\Users\Arslan\.antigravity-ide\laptop-store\images"
os.makedirs(images_dir, exist_ok=True)

# 1. ThinkPad SVG
thinkpad_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 320" width="100%" height="100%">
  <defs>
    <linearGradient id="tp_lid" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#242629"/>
      <stop offset="60%" stop-color="#18191c"/>
      <stop offset="100%" stop-color="#121315"/>
    </linearGradient>
    <linearGradient id="tp_screen" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f1118"/>
      <stop offset="100%" stop-color="#05070a"/>
    </linearGradient>
    <linearGradient id="tp_base" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#222427"/>
      <stop offset="100%" stop-color="#141517"/>
    </linearGradient>
    <filter id="tp_drop" x="-10%" y="-10%" width="120%" height="130%">
      <feDropShadow dx="0" dy="16" stdDeviation="14" flood-color="#000" flood-opacity="0.5"/>
    </filter>
  </defs>

  <g filter="url(#tp_drop)">
    <!-- Base bottom plate -->
    <path d="M 40 240 L 460 240 L 475 258 C 475 264 470 268 462 268 L 38 268 C 30 268 25 264 25 258 Z" fill="url(#tp_base)"/>
    <!-- Base top keyboard deck -->
    <path d="M 50 200 L 450 200 L 465 240 L 35 240 Z" fill="#1b1c20" stroke="#33373d" stroke-width="1"/>
    
    <!-- Keyboard & TrackPoint -->
    <rect x="80" y="206" width="340" height="24" rx="3" fill="#111215" stroke="#25272c"/>
    <!-- Red Trackpoint dot -->
    <circle cx="250" cy="218" r="3.5" fill="#e11d48"/>
    <!-- Trackpad & red accent buttons -->
    <rect x="220" y="244" width="60" height="18" rx="2" fill="#17181c" stroke="#2b2d33"/>
    <line x1="228" y1="243" x2="272" y2="243" stroke="#e11d48" stroke-width="1.8"/>

    <!-- Screen Lid (open at perspective) -->
    <path d="M 68 36 L 432 36 C 438 36 443 41 443 47 L 450 200 L 50 200 L 57 47 C 57 41 62 36 68 36 Z" fill="url(#tp_lid)" stroke="#383c44" stroke-width="1.5"/>
    
    <!-- Screen Bezel & Panel -->
    <rect x="74" y="48" width="352" height="142" rx="4" fill="url(#tp_screen)"/>
    
    <!-- ThinkPad wallpaper code / display glow -->
    <circle cx="250" cy="119" r="45" fill="none" stroke="#e11d48" stroke-width="1.5" opacity="0.35"/>
    <text x="250" y="115" font-family="'Plus Jakarta Sans', system-ui, sans-serif" font-weight="800" font-size="14" fill="#ffffff" text-anchor="middle" letter-spacing="1">ThinkPad</text>
    <text x="250" y="132" font-family="monospace" font-size="9" fill="#94a3b8" text-anchor="middle">MIL-STD 810H TOUGH</text>

    <!-- ThinkPad Corner Logo with glowing red dot on 'i' -->
    <text x="408" y="190" font-family="sans-serif" font-weight="700" font-style="italic" font-size="9" fill="#9ca3af">ThinkPad</text>
    <circle cx="414" cy="183.5" r="1.5" fill="#ef4444"/>
    
    <!-- Webcam -->
    <circle cx="250" cy="42" r="2" fill="#38bdf8"/>
  </g>
</svg>'''

# 2. Dell XPS SVG
dell_xps_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 320" width="100%" height="100%">
  <defs>
    <linearGradient id="xps_lid" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#e2e8f0"/>
      <stop offset="40%" stop-color="#cbd5e1"/>
      <stop offset="100%" stop-color="#94a3b8"/>
    </linearGradient>
    <linearGradient id="xps_screen" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#020617"/>
      <stop offset="50%" stop-color="#0f172a"/>
      <stop offset="100%" stop-color="#1e1b4b"/>
    </linearGradient>
    <filter id="xps_shadow" x="-10%" y="-10%" width="120%" height="130%">
      <feDropShadow dx="0" dy="16" stdDeviation="15" flood-color="#000" flood-opacity="0.45"/>
    </filter>
  </defs>

  <g filter="url(#xps_shadow)">
    <!-- Base bottom -->
    <path d="M 40 240 L 460 240 L 476 256 C 476 262 470 266 462 266 L 38 266 C 30 266 24 262 24 256 Z" fill="#64748b"/>
    <!-- Base keyboard deck (Carbon Fiber weave) -->
    <path d="M 48 198 L 452 198 L 464 240 L 36 240 Z" fill="#1e293b" stroke="#475569" stroke-width="1"/>
    
    <!-- Keyboard -->
    <rect x="75" y="204" width="350" height="24" rx="2" fill="#0f172a" stroke="#334155"/>
    <!-- Invisible glass trackpad -->
    <rect x="205" y="243" width="90" height="19" rx="3" fill="#334155" opacity="0.4"/>

    <!-- Screen Lid (Ultra thin InfinityEdge) -->
    <path d="M 64 34 L 436 34 C 440 34 444 38 444 42 L 452 198 L 48 198 L 56 42 C 56 38 60 34 64 34 Z" fill="url(#xps_lid)" stroke="#94a3b8" stroke-width="1"/>
    
    <!-- InfinityEdge Display (Virtually 0 bezel) -->
    <rect x="58" y="38" width="384" height="156" rx="2" fill="url(#xps_screen)"/>
    
    <!-- Screen visuals -->
    <circle cx="250" cy="116" r="42" fill="none" stroke="#38bdf8" stroke-width="2" opacity="0.5"/>
    <text x="250" y="112" font-family="'Playfair Display', serif" font-weight="700" font-size="16" fill="#f8fafc" text-anchor="middle">DELL XPS</text>
    <text x="250" y="130" font-family="sans-serif" font-weight="600" font-size="9" fill="#38bdf8" text-anchor="middle" letter-spacing="2">INFINITYEDGE 500 NITS</text>
  </g>
</svg>'''

# 3. Alienware Gaming SVG
alienware_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 320" width="100%" height="100%">
  <defs>
    <linearGradient id="aw_bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="60%" stop-color="#020617"/>
      <stop offset="100%" stop-color="#000000"/>
    </linearGradient>
    <linearGradient id="aw_screen" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#18002e"/>
      <stop offset="50%" stop-color="#0a0017"/>
      <stop offset="100%" stop-color="#001824"/>
    </linearGradient>
    <filter id="aw_glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="8" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
  </defs>

  <!-- Cybernetic Tron Light Ring at the rear exhaust -->
  <ellipse cx="250" cy="195" rx="210" ry="12" fill="none" stroke="#06b6d4" stroke-width="4" filter="url(#aw_glow)"/>

  <!-- Base with rear shelf -->
  <path d="M 35 240 L 465 240 L 485 264 C 485 272 478 276 468 276 L 32 276 C 22 276 15 272 15 264 Z" fill="#0f172a" stroke="#1e293b"/>
  <!-- Keyboard deck -->
  <path d="M 45 195 L 455 195 L 470 240 L 30 240 Z" fill="#090d16" stroke="#334155"/>
  <!-- Per-key RGB Keyboard representation -->
  <rect x="70" y="202" width="360" height="26" rx="3" fill="#030712" stroke="#06b6d4" stroke-width="0.8"/>
  <line x1="80" y1="215" x2="420" y2="215" stroke="#ec4899" stroke-width="2" opacity="0.6"/>

  <!-- Screen Lid -->
  <path d="M 60 28 L 440 28 C 446 28 450 32 450 38 L 455 195 L 45 195 L 50 38 C 50 32 54 28 60 28 Z" fill="#0b0f19" stroke="#06b6d4" stroke-width="1.2"/>
  <rect x="64" y="36" width="372" height="152" rx="3" fill="url(#aw_screen)"/>

  <!-- Alienware Alien Head Logo glowing -->
  <g transform="translate(250, 105) scale(1.3)" filter="url(#aw_glow)">
    <path d="M 0 -18 C -11 -18 -18 -8 -16 6 C -14 18 -6 22 0 22 C 6 22 14 18 16 6 C 18 -8 11 -18 0 -18 Z" fill="#06b6d4"/>
    <ellipse cx="-5" cy="0" rx="3.5" ry="6" fill="#000" transform="rotate(20 -5 0)"/>
    <ellipse cx="5" cy="0" rx="3.5" ry="6" fill="#000" transform="rotate(-20 5 0)"/>
  </g>
  <text x="250" y="152" font-family="'Syne', sans-serif" font-weight="800" font-size="14" fill="#06b6d4" text-anchor="middle" letter-spacing="3">ALIENWARE M15 R7</text>
  <text x="250" y="168" font-family="monospace" font-size="9" fill="#ec4899" text-anchor="middle" letter-spacing="1">RYZEN 7 6800H · RTX 3070 Ti 240Hz</text>
</svg>'''

# 4. Surface Tablet 2-in-1 SVG
surface_tab_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 320" width="100%" height="100%">
  <defs>
    <linearGradient id="sf_lid" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#f1f5f9"/>
      <stop offset="100%" stop-color="#cbd5e1"/>
    </linearGradient>
    <linearGradient id="sf_screen" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0284c7"/>
      <stop offset="40%" stop-color="#2563eb"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <filter id="sf_drop" x="-10%" y="-10%" width="120%" height="130%">
      <feDropShadow dx="0" dy="12" stdDeviation="12" flood-color="#000" flood-opacity="0.3"/>
    </filter>
  </defs>

  <g filter="url(#sf_drop)">
    <!-- Type Cover Keyboard (tilted forward) -->
    <path d="M 60 215 L 440 215 L 460 262 C 460 266 455 270 448 270 L 52 270 C 45 270 40 266 40 262 Z" fill="#334155" stroke="#475569"/>
    <!-- Keys on type cover -->
    <rect x="75" y="222" width="350" height="24" rx="2" fill="#1e293b"/>
    <rect x="220" y="249" width="60" height="16" rx="2" fill="#475569" opacity="0.6"/>

    <!-- Kickstand at the back -->
    <polygon points="120,170 380,170 410,215 90,215" fill="#94a3b8" opacity="0.7"/>

    <!-- Tablet Body (3:2 Aspect Ratio) -->
    <rect x="90" y="32" width="320" height="185" rx="10" fill="url(#sf_lid)" stroke="#94a3b8" stroke-width="1.5"/>
    <rect x="100" y="42" width="300" height="165" rx="6" fill="url(#sf_screen)"/>

    <!-- Windows 11 Fluent Flower Bloom Artwork -->
    <circle cx="250" cy="115" r="34" fill="#38bdf8" opacity="0.4"/>
    <circle cx="236" cy="106" r="28" fill="#818cf8" opacity="0.5"/>
    <circle cx="264" cy="120" r="30" fill="#60a5fa" opacity="0.6"/>
    
    <text x="250" y="118" font-family="'Plus Jakarta Sans', sans-serif" font-weight="700" font-size="13" fill="#ffffff" text-anchor="middle">Surface Pro 1866</text>
    <text x="250" y="134" font-family="sans-serif" font-size="9" fill="#e0f2fe" text-anchor="middle" letter-spacing="1">PixelSense 3:2 Touch</text>
  </g>
</svg>'''

# 5. MacBook Air M2 SVG
macbook_air_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 320" width="100%" height="100%">
  <defs>
    <linearGradient id="mba_lid" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1e293b"/>
      <stop offset="50%" stop-color="#0f172a"/>
      <stop offset="100%" stop-color="#020617"/>
    </linearGradient>
    <linearGradient id="mba_screen" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#020617"/>
      <stop offset="60%" stop-color="#0f172a"/>
      <stop offset="100%" stop-color="#1e1b4b"/>
    </linearGradient>
    <filter id="mba_drop" x="-10%" y="-10%" width="120%" height="130%">
      <feDropShadow dx="0" dy="14" stdDeviation="14" flood-color="#000" flood-opacity="0.4"/>
    </filter>
  </defs>

  <g filter="url(#mba_drop)">
    <!-- Bottom base wedge shape -->
    <path d="M 40 240 L 460 240 L 476 254 C 476 260 470 264 460 264 L 40 264 C 30 264 24 260 24 254 Z" fill="#0f172a"/>
    <!-- Top deck -->
    <path d="M 50 198 L 450 198 L 464 240 L 36 240 Z" fill="#1e293b" stroke="#334155" stroke-width="1"/>
    <!-- Magic keyboard -->
    <rect x="80" y="204" width="340" height="24" rx="3" fill="#020617"/>
    <!-- Force touch trackpad -->
    <rect x="200" y="242" width="100" height="19" rx="3" fill="#0f172a" stroke="#334155" stroke-width="0.8"/>

    <!-- Screen Lid (Midnight with camera notch) -->
    <path d="M 65 35 L 435 35 C 440 35 444 39 444 44 L 450 198 L 50 198 L 56 44 C 56 39 60 35 65 35 Z" fill="url(#mba_lid)" stroke="#334155"/>
    <rect x="62" y="42" width="376" height="150" rx="4" fill="url(#mba_screen)"/>

    <!-- Camera notch -->
    <path d="M 235 42 L 265 42 C 267 42 268 44 268 46 L 268 50 C 268 53 266 55 263 55 L 237 55 C 234 55 232 53 232 50 L 232 46 C 232 44 233 42 235 42 Z" fill="#020617"/>

    <!-- Apple Wallpaper Glow -->
    <circle cx="250" cy="120" r="45" fill="none" stroke="#60a5fa" stroke-width="2.5" opacity="0.6"/>
    <text x="250" y="116" font-family="-apple-system, BlinkMacSystemFont, 'Plus Jakarta Sans', sans-serif" font-weight="700" font-size="16" fill="#ffffff" text-anchor="middle">MacBook Air M2</text>
    <text x="250" y="134" font-family="sans-serif" font-size="10" fill="#93c5fd" text-anchor="middle" letter-spacing="1.5">Liquid Retina · Midnight Finish</text>
  </g>
</svg>'''

files = {
    'lenovo-thinkpad.svg': thinkpad_svg,
    'dell-xps.svg': dell_xps_svg,
    'alienware.svg': alienware_svg,
    'surface-tab.svg': surface_tab_svg,
    'macbook-air.svg': macbook_air_svg
}

for name, content in files.items():
    p = os.path.join(images_dir, name)
    with open(p, 'w', encoding='utf-8') as f:
        f.write(content.strip())
    print(f"Created SVG: {p}")
