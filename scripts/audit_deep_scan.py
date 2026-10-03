import os
import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

def scan():
    print("=== DEEP LINE-BY-LINE AUDIT ===")

    # -------------------------------------------------------------------
    # A. Check missing DOM element IDs in getElementById
    # -------------------------------------------------------------------
    files_to_check = ['laptophub.html', 'product.html', 'consult.html', 'inventory.html', 'admin/index.html']
    
    for fn in files_to_check:
        if not os.path.exists(fn): continue
        with open(fn, 'r', encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()
        
        full_text = "".join(lines)
        # Find all id="..." in HTML
        existing_ids = set(re.findall(r'\bid=["\']([^"\']+)["\']', full_text))
        
        # Check all document.getElementById('...')
        for line_no, line in enumerate(lines, start=1):
            for m in re.finditer(r'document\.getElementById\(["\']([^"\']+)["\']\)', line):
                target_id = m.group(1)
                # Ignore dynamically created element IDs like `rev-${rev.id}` or `card-${id}`
                if '${' in target_id or '+' in target_id:
                    continue
                if target_id not in existing_ids:
                    # Check if created in JS template literals
                    if f'id="{target_id}"' not in full_text and f"id='{target_id}'" not in full_text:
                        print(f"[BUG: Missing DOM ID] {fn}:{line_no} references getElementById('{target_id}') but #{target_id} is not defined in HTML")

    # -------------------------------------------------------------------
    # B. Check internal links href="#..."
    # -------------------------------------------------------------------
    for fn in ['laptophub.html', 'product.html', 'consult.html', 'admin/index.html']:
        if not os.path.exists(fn): continue
        with open(fn, 'r', encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()
        full_text = "".join(lines)
        existing_ids = set(re.findall(r'\bid=["\']([^"\']+)["\']', full_text))
        
        for line_no, line in enumerate(lines, start=1):
            for m in re.finditer(r'href=["\']#([a-zA-Z0-9_-]+)["\']', line):
                target_hash = m.group(1)
                if target_hash not in existing_ids:
                    print(f"[BUG: Broken Anchor Link] {fn}:{line_no} links to #{target_hash} which does not exist in the page")

    # -------------------------------------------------------------------
    # C. Check links to other pages
    # -------------------------------------------------------------------
    for fn in files_to_check:
        if not os.path.exists(fn): continue
        with open(fn, 'r', encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()
        for line_no, line in enumerate(lines, start=1):
            for m in re.finditer(r'href=["\']([^"\'#:]+\.html(?:\?[^"\']*)?)["\']', line):
                target_file = m.group(1).split('?')[0]
                base_dir = os.path.dirname(fn)
                target_path = os.path.normpath(os.path.join(base_dir, target_file))
                if not os.path.exists(target_path):
                    print(f"[BUG: Broken Page Link] {fn}:{line_no} links to {target_file} (path {target_path} does not exist)")

    # -------------------------------------------------------------------
    # D. Check for elements with fixed width > 360px (mobile overflow risk)
    # -------------------------------------------------------------------
    css_files = ['css/header.css', 'css/product.css', 'css/theme.css']
    for cf in css_files:
        with open(cf, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        for line_no, line in enumerate(lines, start=1):
            # match width: XXXpx where XXX > 360
            m = re.search(r'(?<!max-)(?<!min-)width:\s*([4-9]\d{2,}|[1-9]\d{3,})px', line)
            if m:
                print(f"[RESPONSIVE: Fixed Width > 360px] {cf}:{line_no} defines {m.group(0)} without max-width/fluidity")

    # -------------------------------------------------------------------
    # E. Check buttons without text or aria-label (Accessibility)
    # -------------------------------------------------------------------
    for fn in ['laptophub.html', 'product.html']:
        with open(fn, 'r', encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()
        for line_no, line in enumerate(lines, start=1):
            if '<button' in line and 'aria-label' not in line:
                # check if empty button or only contains svg
                if re.search(r'<button[^>]*>\s*<svg[^>]*>.*?</svg>\s*</button>', line):
                    print(f"[A11Y: Missing Button Label] {fn}:{line_no} icon-only button lacks aria-label")

if __name__ == '__main__':
    scan()
