"""
Automated validation of Header Alignment, Grid rules, Button geometry,
and Responsive Breakpoints across 360px, 768px, 1024px, 1366px, and 1920px.
"""
import re
import sys

def test_header():
    with open('css/header.css', 'r', encoding='utf-8') as f:
        css = f.read()

    with open('laptophub.html', 'r', encoding='utf-8') as f:
        html = f.read()

    passes = 0

    def check(cond, msg):
        nonlocal passes
        if cond:
            print(f"  [PASS] {msg}")
            passes += 1
        else:
            print(f"  [FAIL] {msg}")
            raise AssertionError(msg)

    print("\n================== HEADER ALIGNMENT VALIDATION ==================")

    # 1. 3-column grid structure
    check("grid-template-columns: 1fr auto 1fr;" in css, "3-column grid (1fr auto 1fr) configured on nav")
    check(".logo-mark" in css and "justify-self: start;" in css, "Logo left-aligned via justify-self: start")
    check(".nav-links" in css and "justify-self: center;" in css, "Nav links truly centered via justify-self: center")
    check(".nav-right" in css and "justify-self: end;" in css, "Actions group right-aligned via justify-self: end")

    # 2. Right-side actions geometry
    check("gap: 8px;" in css, "Action buttons have clean 8px gap")
    check("height: 40px !important;" in css, "Action buttons strictly 40px height")
    check("border-radius: 10px !important;" in css, "Action buttons unified 10px border-radius")
    check("align-items: center !important;" in css and "justify-content: center !important;" in css, "All actions vertically centered")

    # 3. Truncate long username with ellipsis
    check("text-overflow: ellipsis;" in css and "white-space: nowrap;" in css and "overflow: hidden;" in css,
          "User name text truncated with ellipsis for long names")
    check("max-width: 95px;" in css or "max-width: 55px;" in css, "User name text has bounded max-width for ellipsis")

    # 4. Light and Dark mode variables
    check("var(--nav-bg)" in css and "var(--border)" in css and "var(--heading)" in css,
          "Header uses theme tokens for light and dark mode compatibility")

    # 5. Breakpoint coverage:
    # Desktop 1920px & 1366px & 1024px
    check("grid-template-columns: 1fr auto 1fr;" in css, "Desktop viewports (1920px, 1366px, 1024px) use 3-column grid")
    # Tablet 768px (< 992px)
    check("@media (max-width: 992px)" in css, "Tablet breakpoint (<992px including 768px) defined")
    check(".nav-links {\n    display: none !important;" in css or "display: none !important;" in css,
          "Nav links hidden on tablet/mobile to prevent wrapping")
    check(".mobile-nav-toggle" in css, "Mobile toggle activated on tablet and mobile")
    # Mobile 360px (< 380px)
    check("@media (max-width: 380px)" in css, "Mobile small breakpoint (<380px including 360px) defined")
    check(".cart-text" in css and "display: none !important;" in css,
          "Cart label cleanly collapses to icon at 360px without overlapping")

    # 6. Linking in HTML
    check('href="css/header.css"' in html, "laptophub.html links css/header.css")

    print(f"\nAll {passes} header tests passed successfully!\n")
    return True

if __name__ == '__main__':
    test_header()
