import re
import sys

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

def audit_file(path):
    print(f"=== Auditing {path} ===")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Check for Playfair Display font references
    playfair_matches = re.findall(r"Playfair", content, re.IGNORECASE)
    if playfair_matches:
        print(f"  [WARN] Found {len(playfair_matches)} instances of 'Playfair'")
    else:
        print("  [OK] No 'Playfair' font references found (unified to modern font system).")

    # 2. Check for leftover problematic emojis mentioned in prompt: 🧠 💾 💬 🛒 📦 🎯 🔍
    emojis = ['🧠', '💾', '💬', '🛒', '📦', '🎯', '🔍']
    found_emojis = {}
    for em in emojis:
        count = len(re.findall(re.escape(em), content))
        if count > 0:
            found_emojis[em] = count
    if found_emojis:
        print(f"  [WARN] Found target emojis: {found_emojis}")
    else:
        print("  [OK] None of the target emojis (🧠 💾 💬 🛒 📦 🎯 🔍) found in UI.")

    # 3. Check for tabular-nums
    tabular_matches = re.findall(r"tabular-nums", content)
    print(f"  [INFO] 'tabular-nums' occurrences: {len(tabular_matches)}")

    # 4. Check tags balance
    for tag in ['div', 'button', 'section', 'main']:
        opens = len(re.findall(rf"<{tag}\b", content, re.IGNORECASE))
        closes = len(re.findall(rf"</{tag}>", content, re.IGNORECASE))
        if opens != closes:
            print(f"  [WARN] Tag mismatch <{tag}>: {opens} open, {closes} close")
        else:
            print(f"  [OK] Tag <{tag}> balanced ({opens}/{closes})")

    # 5. Check key functions exist
    scripts = "\n".join(re.findall(r"<script\b[^>]*>(.*?)</script>", content, re.DOTALL))
    if "laptophub.html" in path:
        req_funcs = [
            "openLaptopModal", "closeLaptopModal", "selectModalRam",
            "selectModalStorage", "updateModalPricingAndUI", "addModalItemToCart",
            "orderModalViaWhatsApp", "checkoutModalCOD"
        ]
        for fn in req_funcs:
            if re.search(rf"\b{fn}\b", scripts):
                print(f"  [OK] Modal function '{fn}' is defined.")
            else:
                print(f"  [ERROR] Modal function '{fn}' is MISSING!")
    elif "consult.html" in path:
        req_funcs = [
            "showStep", "jumpToStep", "syncStepUI", "goNext", "goPrev",
            "showResults", "editAnswers", "restart", "generateMatchReason"
        ]
        for fn in req_funcs:
            if re.search(rf"\b{fn}\b", scripts):
                print(f"  [OK] Consult function '{fn}' is defined.")
            else:
                print(f"  [ERROR] Consult function '{fn}' is MISSING!")

audit_file("laptophub.html")
audit_file("consult.html")
