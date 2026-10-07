import asyncio
import sys
from playwright.async_api import async_playwright

async def run_tests():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(viewport={'width': 1280, 'height': 800})
        page = await context.new_page()

        console_errors = []
        page.on("console", lambda msg: console_errors.append(f"[{msg.type}] {msg.text}") if msg.type in ["error"] else None)
        page.on("pageerror", lambda err: console_errors.append(f"[pageerror] {str(err)}"))

        print("=== 1. AUDIT GLOBAL CURSOR & DESIGN TOKENS ACROSS ALL PAGES ===")
        pages_to_check = [
            ("Home / LaptopHUB", "http://localhost:8080/laptophub.html"),
            ("Consult Me", "http://localhost:8080/consult.html"),
            ("Product Page", "http://localhost:8080/product.html?id=1"),
            ("Admin Login", "http://localhost:8080/admin/login.html")
        ]

        for name, url in pages_to_check:
            console_errors.clear()
            print(f"\nChecking: {name} ({url})")
            await page.goto(url, wait_until="networkidle")
            await page.wait_for_timeout(500)

            # Check cursor elements
            dot_count = await page.locator("#cursor-dot").count()
            ring_count = await page.locator("#cursor-ring").count()
            print(f"  [Cursor elements] #cursor-dot: {dot_count}, #cursor-ring: {ring_count}")
            assert dot_count == 1, f"Missing #cursor-dot on {name}"
            assert ring_count == 1, f"Missing #cursor-ring on {name}"

            # Check global font token
            font_family = await page.evaluate("getComputedStyle(document.body).fontFamily")
            print(f"  [Font Family] {font_family}")
            assert "Plus Jakarta Sans" in font_family, f"Expected Plus Jakarta Sans on {name}, got {font_family}"

            # Check mouse movement activates cursor
            await page.mouse.move(200, 200)
            has_cursor_active = await page.evaluate("document.body.classList.contains('custom-cursor-active')")
            print(f"  [Cursor activated on mousemove] {has_cursor_active}")
            assert has_cursor_active, f"Cursor did not activate on mousemove on {name}"

            # Check console errors
            filtered_errors = [e for e in console_errors if "favicon" not in e.lower()]
            if filtered_errors:
                print(f"  [WARNING/ERROR] Console errors on {name}: {filtered_errors}")
            else:
                print(f"  [OK] Zero console errors on {name}")

        print("\n=== 2. TEST HOVER CARD ON LAPTOPHUB ===")
        await page.goto("http://localhost:8080/laptophub.html", wait_until="networkidle")
        await page.wait_for_timeout(1000)

        # Find first product card (Laptop 1: Lenovo ThinkPad T14, 3 photos)
        card1 = page.locator('.pcard[data-laptop-id="1"]')
        box1 = await card1.bounding_box()
        assert box1 is not None, "Laptop card 1 not found"

        # Test early leave (<1000ms): should NOT open
        print("\nTest 2a: Hover < 1.0s (early leave, 400ms)")
        await page.mouse.move(box1['x'] + 50, box1['y'] + 50)
        await page.wait_for_timeout(400)
        # Move away
        await page.mouse.move(10, 10)
        await page.wait_for_timeout(800)
        is_open = await page.locator("#hoverExpandOverlay.active").count()
        print(f"  Hover card open after early leave? {is_open > 0} (Expected: False)")
        assert is_open == 0, "Hover card opened after early cursor leave!"

        # Test deliberate hover >= 1.0s: should OPEN
        print("\nTest 2b: Deliberate hover >= 1.0s (1200ms) on Laptop 1 (3 photos)")
        await page.mouse.move(box1['x'] + 50, box1['y'] + 50)
        await page.wait_for_timeout(1300)
        is_open = await page.locator("#hoverExpandOverlay.active").count()
        print(f"  Hover card open after 1.2s hover? {is_open > 0} (Expected: True)")
        assert is_open == 1, "Hover card did not open after 1.2s deliberate hover!"

        # Check Horizontal Scrolling (overflow-x)
        card_el = page.locator("#hoverExpandCard")
        scroll_info = await card_el.evaluate("""el => ({
            scrollWidth: el.scrollWidth,
            clientWidth: el.clientWidth,
            scrollHeight: el.scrollHeight,
            clientHeight: el.clientHeight,
            hasHorizontalScroll: el.scrollWidth > el.clientWidth
        })""")
        print(f"  [Card Dimensions] scrollWidth: {scroll_info['scrollWidth']}, clientWidth: {scroll_info['clientWidth']}, hasHorizontalScroll: {scroll_info['hasHorizontalScroll']}")
        assert not scroll_info['hasHorizontalScroll'], f"Horizontal scroll detected on hover card! {scroll_info}"
        print("  [OK] ZERO horizontal scroll!")

        # Check Slideshow on Laptop 1 (3 photos)
        slides_count = await page.locator("#hexSlidesTrack .hex-slide").count()
        dots_count = await page.locator("#hexDots .hex-dot").count()
        print(f"  [Slideshow Laptop 1] Slides: {slides_count}, Dots: {dots_count}")
        assert slides_count == 3, f"Expected 3 slides for Laptop 1, got {slides_count}"
        assert dots_count == 3, f"Expected 3 dots for Laptop 1, got {dots_count}"

        # Check auto-slideshow progression (2s interval)
        active_slide_0 = await page.locator("#hexSlidesTrack .hex-slide.active").get_attribute("data-slide-index")
        print(f"  Initial active slide index: {active_slide_0}")
        await page.wait_for_timeout(2200)
        active_slide_1 = await page.locator("#hexSlidesTrack .hex-slide.active").get_attribute("data-slide-index")
        print(f"  Active slide index after 2.2s: {active_slide_1}")
        assert active_slide_1 != active_slide_0, "Auto-slideshow did not advance after 2 seconds!"

        # Test Prev/Next Arrows
        print("  Testing Prev/Next Arrow navigation...")
        await page.click("#hexArrowNext")
        active_slide_2 = await page.locator("#hexSlidesTrack .hex-slide.active").get_attribute("data-slide-index")
        print(f"  Active slide index after clicking Next: {active_slide_2}")

        # Check 10 Internal Specs
        spec_items = await page.locator("#hexSpecsGrid .hex-spec-item").count()
        print(f"  [Internal Specs Count] {spec_items} (Expected: 10)")
        assert spec_items == 10, f"Expected 10 internal specs items, got {spec_items}"

        # Check buttons exist
        btn_cart = await page.locator("#hexBtnAddToCart").count()
        btn_cod = await page.locator("#hexBtnCod").count()
        btn_wa = await page.locator("#hexBtnWhatsApp").count()
        btn_details = await page.locator("#hexBtnDetails").count()
        print(f"  [Action Buttons] AddToCart: {btn_cart}, COD: {btn_cod}, WhatsApp: {btn_wa}, Details: {btn_details}")
        assert btn_cart == 1 and btn_cod == 1 and btn_wa == 1 and btn_details == 1

        # Close via Escape key
        print("\nTest 2c: Close via Escape key")
        await page.keyboard.press("Escape")
        await page.wait_for_timeout(400)
        is_open = await page.locator("#hoverExpandOverlay.active").count()
        print(f"  Hover card open after Escape? {is_open > 0} (Expected: False)")
        assert is_open == 0, "Card failed to close on Escape key"

        # Test Laptop 2 (5+ photos: Microsoft Surface Pro 7)
        print("\nTest 2d: Deliberate hover on Laptop 2 (5 photos)")
        card2 = page.locator('.pcard[data-laptop-id="2"]')
        box2 = await card2.bounding_box()
        await page.mouse.move(box2['x'] + 50, box2['y'] + 50)
        await page.wait_for_timeout(1300)

        slides_count_2 = await page.locator("#hexSlidesTrack .hex-slide").count()
        dots_count_2 = await page.locator("#hexDots .hex-dot").count()
        print(f"  [Slideshow Laptop 2] Slides: {slides_count_2}, Dots: {dots_count_2}")
        assert slides_count_2 == 5, f"Expected 5 slides for Laptop 2, got {slides_count_2}"
        assert dots_count_2 == 5, f"Expected 5 dots for Laptop 2, got {dots_count_2}"

        # Check horizontal scroll on Laptop 2
        scroll_info_2 = await card_el.evaluate("""el => ({
            scrollWidth: el.scrollWidth,
            clientWidth: el.clientWidth,
            hasHorizontalScroll: el.scrollWidth > el.clientWidth
        })""")
        print(f"  [Card Dimensions Laptop 2] scrollWidth: {scroll_info_2['scrollWidth']}, clientWidth: {scroll_info_2['clientWidth']}")
        assert not scroll_info_2['hasHorizontalScroll'], "Horizontal scroll detected on Laptop 2 hover card!"

        # Close via Close button (✕)
        print("  Closing via X button...")
        await page.click("#hoverExpandCloseBtn")
        await page.wait_for_timeout(400)
        is_open = await page.locator("#hoverExpandOverlay.active").count()
        assert is_open == 0, "Card failed to close on X button"

        # Test Laptop 3 (1 photo: Dell Latitude 7400)
        print("\nTest 2e: Deliberate hover on Laptop 3 (1 photo)")
        card3 = page.locator('.pcard[data-laptop-id="3"]')
        box3 = await card3.bounding_box()
        await page.mouse.move(box3['x'] + 50, box3['y'] + 50)
        await page.wait_for_timeout(1300)

        slides_count_3 = await page.locator("#hexSlidesTrack .hex-slide").count()
        prev_arrow_visible = await page.locator("#hexArrowPrev").is_visible()
        dots_visible = await page.locator("#hexDots").is_visible()
        print(f"  [Slideshow Laptop 3] Slides: {slides_count_3}, Arrows Visible: {prev_arrow_visible}, Dots Visible: {dots_visible}")
        assert slides_count_3 == 1, f"Expected 1 slide, got {slides_count_3}"
        assert not prev_arrow_visible, "Arrows should be hidden for 1 photo!"
        assert not dots_visible, "Dots should be hidden for 1 photo!"

        # Close via click outside
        print("  Closing via click outside overlay...")
        await page.mouse.click(15, 15)
        await page.wait_for_timeout(400)
        is_open = await page.locator("#hoverExpandOverlay.active").count()
        assert is_open == 0, "Card failed to close on click outside"

        print("\n=== ALL TESTS PASSED SUCCESSFULLY! ===")
        await browser.close()

asyncio.run(run_tests())
