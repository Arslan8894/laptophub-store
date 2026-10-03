import re
import os
import sys

def verify():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    js_path = os.path.join(base_dir, 'js', 'animations', 'tab-switcher.js')
    css_path = os.path.join(base_dir, 'css', 'glass.css')
    html_path = os.path.join(base_dir, 'laptophub.html')

    assert os.path.exists(js_path), "tab-switcher.js missing"
    assert os.path.exists(css_path), "glass.css missing"
    assert os.path.exists(html_path), "laptophub.html missing"

    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Verify tab switcher markup
    assert 'class="glass-tab-switcher"' in html, "Missing .glass-tab-switcher"
    assert 'id="glassTabIndicator"' in html, "Missing #glassTabIndicator"
    assert 'id="tab-inventory"' in html, "Missing #tab-inventory"
    assert 'id="tab-consult"' in html, "Missing #tab-consult"
    assert 'id="tab-reviews"' in html, "Missing #tab-reviews"
    assert 'id="tabpanel-inventory"' in html, "Missing #tabpanel-inventory"
    assert 'id="tabpanel-consult"' in html, "Missing #tabpanel-consult"
    assert 'id="tabpanel-reviews"' in html, "Missing #tabpanel-reviews"
    assert 'js/animations/tab-switcher.js' in html, "Missing script tag for tab-switcher.js"

    # Verify inventory and reviews are still present and intact inside panels
    assert 'id="inventory"' in html, "Missing #inventory"
    assert 'id="productGrid"' in html, "Missing #productGrid"
    assert 'id="reviews"' in html, "Missing #reviews"

    with open(css_path, 'r', encoding='utf-8') as f:
        css = f.read()

    assert '.glass-tab-switcher' in css, "Missing .glass-tab-switcher in css"
    assert '.glass-sliding-indicator' in css, "Missing .glass-sliding-indicator in css"
    assert '.glass-tab-btn' in css, "Missing .glass-tab-btn in css"
    assert '.main-tab-panel' in css, "Missing .main-tab-panel in css"
    assert 'prefers-reduced-motion' in css, "Missing prefers-reduced-motion in css"

    with open(js_path, 'r', encoding='utf-8') as f:
        js = f.read()

    assert 'initTabSwitcher' in js, "Missing initTabSwitcher"
    assert 'switchStoreTab' in js, "Missing switchStoreTab"
    assert 'updateIndicatorPosition' in js, "Missing updateIndicatorPosition"
    assert 'elastic.out' in js, "Missing elastic.out in js"
    assert 'prefers-reduced-motion' in js, "Missing prefers-reduced-motion in js"

    print("ALL VERIFICATIONS PASSED: Step 4 Liquid Glass Tab Switcher is fully wired and valid!")

if __name__ == '__main__':
    verify()
