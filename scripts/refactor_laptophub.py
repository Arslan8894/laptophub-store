import sys

def run():
    with open('laptophub.html', 'r', encoding='utf-8') as f:
        text = f.read()

    # 1. Update meta description
    old_meta = '<meta name="description" content="Pakistan\'s premier laptop store offering certified business & creator laptops from Dell, HP, Apple, and Lenovo with Cash on Delivery and warranty.">'
    new_meta = '<meta name="description" content="Pakistan\'s premier laptop store offering certified business & creator laptops from Dell, HP, Apple, and Lenovo with verified specs, express insured delivery, and warranty.">'
    assert old_meta in text, "old_meta not found"
    text = text.replace(old_meta, new_meta)

    # 2. Update CSS: remove lines from /* LAPTOP QUICK-VIEW & CUSTOM SPEC MODAL to #laptopModal button, #laptopModal a { cursor: pointer !important; }
    start_css = '  /* LAPTOP QUICK-VIEW & CUSTOM SPEC MODAL (NON-OVERLAPPING STICKY FOOTER) */'
    end_css = '  #laptopModal button, #laptopModal a { cursor: pointer !important; }'
    idx1 = text.find(start_css)
    idx2 = text.find(end_css)
    assert idx1 != -1 and idx2 != -1, "CSS block not found"
    text = text[:idx1] + '  /* Laptop modal styles migrated to css/product.css for Amazon-style product page */\n' + text[idx2 + len(end_css):]

    # 3. Update FAQ button and text
    assert '<a href="#faq" class="btn-s">COD & Warranty Info</a>' in text
    text = text.replace('<a href="#faq" class="btn-s">COD & Warranty Info</a>', '<a href="#faq" class="btn-s">Payment & Warranty Info</a>')

    old_testim = '"Got the MacBook Pro M2 delivered via COD in Karachi. Verified serial number on Apple\'s coverage site immediately. 100% authentic."'
    new_testim = '"Got the MacBook Pro M2 delivered via insured courier in Karachi. Verified serial number on Apple\'s coverage site immediately. 100% authentic."'
    assert old_testim in text
    text = text.replace(old_testim, new_testim)

    old_faq = '<button class="faq-q"><span>Do you offer Cash on Delivery (COD)?</span><div class="faq-icon">+</div></button>\n      <div class="faq-ans"><p>Yes — COD is available across all major cities including Lahore, Karachi, Islamabad, Rawalpindi, Faisalabad, and Multan with zero extra handling fees.</p></div>'
    new_faq = '<button class="faq-q"><span>What payment methods do you accept?</span><div class="faq-icon">+</div></button>\n      <div class="faq-ans"><p>We accept Direct Bank Transfer / Raast (IBFT) and advance payment verification. Every shipment is fully insured with express tracking across Lahore, Karachi, Islamabad, Rawalpindi, Faisalabad, Multan, and nationwide destinations.</p></div>'
    assert old_faq in text
    text = text.replace(old_faq, new_faq)

    # 4. Cart drawer text
    assert 'FREE Express Dispatch across Pakistan · Cash on Delivery' in text
    text = text.replace(
        'FREE Express Dispatch across Pakistan · Cash on Delivery',
        'FREE Express Insured Dispatch across Pakistan'
    )
    assert 'Cash on Delivery Checkout' in text
    text = text.replace(
        'Cash on Delivery Checkout',
        'Proceed to Order Checkout'
    )

    # 5. Remove #laptopModal HTML block
    start_html = '<!-- LAPTOP QUICK-VIEW & CUSTOM SPEC MODAL -->'
    end_html = '<!-- QUICK CASH ON DELIVERY CHECKOUT MODAL -->'
    idx1 = text.find(start_html)
    idx2 = text.find(end_html)
    assert idx1 != -1 and idx2 != -1, "Modal HTML block not found"
    text = text[:idx1] + text[idx2:]

    # 6. Checkout modal & confirm modal text
    text = text.replace('<!-- QUICK CASH ON DELIVERY CHECKOUT MODAL -->', '<!-- ORDER CHECKOUT MODAL -->')
    text = text.replace('Cash on Delivery Order', 'Secure Order Checkout')
    old_tot = 'Order Total: <strong id="modalOrderTotal" style="color:var(--blue)">Rs 0</strong> · Payment on delivery via Cash'
    new_tot = 'Order Total: <strong id="modalOrderTotal" style="color:var(--blue)">Rs 0</strong> · Payment: Direct Bank Transfer / Raast (IBFT)'
    assert old_tot in text
    text = text.replace(old_tot, new_tot)
    assert 'Confirm & Place COD Order' in text
    text = text.replace('Confirm & Place COD Order', 'Confirm & Place Order')
    assert '<div><strong>Payment:</strong> Cash on Delivery</div>' in text
    text = text.replace('<div><strong>Payment:</strong> Cash on Delivery</div>', '<div><strong>Payment:</strong> Direct Bank Transfer / Raast (IBFT)</div>')

    # 7. Update JS: handleCardKey & renderProducts
    old_hkey = """  function handleCardKey(e, id) {
    if (e.key === 'Enter' || e.key === ' ') {
      e.preventDefault();
      openLaptopModal(id);
    }
  }"""
    new_hkey = """  function handleCardKey(e, id) {
    if (e.key === 'Enter' || e.key === ' ') {
      e.preventDefault();
      openProductPage(id);
    }
  }"""
    assert old_hkey in text
    text = text.replace(old_hkey, new_hkey)

    assert 'onclick="openLaptopModal(${lap.id}, event)"' in text
    text = text.replace(
        'onclick="openLaptopModal(${lap.id}, event)"',
        'onclick="openProductPage(${lap.id}, event)"'
    )


    old_atc = """  function addToCartById(id) {
    openLaptopModal(id);
  }"""
    new_atc = """  function addToCartById(id) {
    openProductPage(id);
  }"""
    assert old_atc in text
    text = text.replace(old_atc, new_atc)

    # 8. Remove modal JS functions
    start_js = '  // =========================================================================\n  // LAPTOP MODAL CUSTOMIZER & SPEC SELECTOR\n  // ========================================================================='
    end_js = '  function openCheckoutModal() {'
    idx1 = text.find(start_js)
    idx2 = text.find(end_js)
    assert idx1 != -1 and idx2 != -1, "Modal JS block not found"

    modal_replacement = """  // =========================================================================
  // STANDALONE PRODUCT PAGE NAVIGATION & SCROLL RESTORATION
  // =========================================================================
  function openProductPage(id, e) {
    if (e && e.target && e.target.closest && e.target.closest('.btn-card-wa')) return;
    try {
      sessionStorage.setItem('laptophub_scroll_pos', window.scrollY.toString());
    } catch (_) {}
    window.location.href = `product.html?id=${id}`;
  }

  // Restore scroll position when returning from product page
  window.addEventListener('DOMContentLoaded', () => {
    try {
      const savedScroll = sessionStorage.getItem('laptophub_scroll_pos');
      if (savedScroll !== null) {
        sessionStorage.removeItem('laptophub_scroll_pos');
        requestAnimationFrame(() => {
          window.scrollTo({ top: parseInt(savedScroll, 10), behavior: 'instant' });
        });
      }
    } catch (_) {}
  });

"""
    text = text[:idx1] + modal_replacement + text[idx2:]

    # 9. Clean up pendingBuyAction and Escape handler
    text = text.replace("pendingBuyAction = { type: 'cod_checkout' };", "pendingBuyAction = { type: 'checkout' };")
    text = text.replace("else if (action.type === 'cod_checkout') {", "else if (action.type === 'checkout' || action.type === 'cod_checkout') {")
    text = text.replace("    } else if (action.type === 'modal_whatsapp') {\n      orderModalViaWhatsApp();", "")
    text = text.replace("      closeLaptopModal();\n", "")

    with open('laptophub.html', 'w', encoding='utf-8') as f:
        f.write(text)

    print('Successfully updated laptophub.html!')

    # Update admin/index.html
    with open('admin/index.html', 'r', encoding='utf-8') as f:
        admin_text = f.read()

    old_admin_h2 = '<h2 class="card-title">🛒 Customer Orders (Cash on Delivery)</h2>'
    if old_admin_h2 in admin_text:
        admin_text = admin_text.replace(old_admin_h2, '<h2 class="card-title">🛒 Customer Orders</h2>')
        with open('admin/index.html', 'w', encoding='utf-8') as f:
            f.write(admin_text)
        print('Successfully updated admin/index.html!')

if __name__ == '__main__':
    run()
