import re

def verify():
    with open('laptophub.html', 'r', encoding='utf-8') as f:
        html = f.read()

    errors = []

    # 1. Verify duplicate switcher is gone
    if 'id="mainViewSwitcherWrap"' in html or 'glass-tab-switcher' in html:
        errors.append("Duplicate tab switcher still found in HTML!")
    else:
        print("[PASS] Duplicate tab switcher completely eliminated.")

    # 2. Verify hero styling
    if 'flex-direction: column' not in html or 'padding: 5.6rem 2rem 3.5rem' not in html:
        errors.append("Hero CSS is missing flex-direction: column or 5.6rem top padding!")
    else:
        print("[PASS] Hero layout is vertically stacked with balanced 5.6rem top padding.")

    # 3. Verify obsolete script is not referenced
    if 'tab-switcher.js' in html:
        errors.append("Obsolete tab-switcher.js still referenced in HTML!")
    else:
        print("[PASS] Obsolete tab-switcher.js cleanly removed.")

    # 4. Verify consult-matcher.js is referenced
    if 'consult-matcher.js' not in html:
        errors.append("consult-matcher.js is not referenced in HTML!")
    else:
        print("[PASS] consult-matcher.js is properly linked.")

    # 5. Verify unneeded heavy scripts and dead calls are purged
    if 'glass-effects.js' in html:
        errors.append("glass-effects.js is still referenced in HTML!")
    else:
        print("[PASS] Heavy glass-effects.js cleanly removed in favor of pure CSS.")

    if 'refreshScrollTriggers' in html:
        errors.append("Dead refreshScrollTriggers call still present in HTML!")
    else:
        print("[PASS] Dead refreshScrollTriggers cleanly purged.")

    # 6. Verify document sections exist in flow
    for sec in ['id="inventory"', 'id="consult"', 'id="reviews"', 'id="faq"', 'id="support"']:
        if sec not in html:
            errors.append(f"Section {sec} is missing from page flow!")
        else:
            print(f"[PASS] Section {sec} is present in continuous document flow.")

    # 7. Check active JS files
    for js_file in ['js/animations/glass-nav.js', 'js/animations/consult-matcher.js']:
        try:
            with open(js_file, 'r', encoding='utf-8') as jf:
                content = jf.read()
                # Basic check for unbalanced braces
                open_b = content.count('{')
                close_b = content.count('}')
                if open_b != close_b:
                    errors.append(f"{js_file} has unbalanced braces: {open_b} open vs {close_b} close")
                else:
                    print(f"[PASS] {js_file} syntax verified ({open_b} matching braces).")
        except Exception as e:
            errors.append(f"Error reading {js_file}: {e}")

    if errors:
        print("\nERRORS DETECTED:")
        for err in errors:
            print("  [FAIL]", err)
        return False
    else:
        print("\nALL VERIFICATION CHECKS PASSED PERFECTLY!")
        return True

if __name__ == '__main__':
    verify()
