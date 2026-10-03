import os
import re
import json
import urllib.request
import urllib.error

def audit():
    print("=== STARTING COMPREHENSIVE PROJECT AUDIT ===")
    issues = []

    # 1. Inspect Broken Links & Assets
    print("-> Checking HTML files for asset links and references...")
    html_files = [
        'index.html', 'laptophub.html', 'product.html', 'volts.html', 
        'custom-laptop.html', 'consult.html', 'inventory.html',
        'admin/index.html', 'admin/login.html'
    ]
    
    for hf in html_files:
        if not os.path.exists(hf):
            issues.append({'sev': 'Critical', 'cat': 'Broken Link', 'loc': hf, 'msg': f"File does not exist: {hf}"})
            continue
        with open(hf, 'r', encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()
        
        base_dir = os.path.dirname(hf)
        for i, line in enumerate(lines):
            # Check img src
            for m in re.finditer(r'<img[^>]+src=["\']([^"\']+)["\']', line):
                src = m.group(1)
                if not src.startswith(('http://', 'https://', 'data:', '{{', '{', '<%')):
                    # check relative path
                    target = os.path.normpath(os.path.join(base_dir, src.split('?')[0].split('#')[0]))
                    if not os.path.exists(target) and not src.startswith('images/laptop-'):
                        issues.append({'sev': 'Major', 'cat': 'Broken Asset', 'loc': f"{hf}:{i+1}", 'msg': f"Image not found: {src} (resolved {target})"})
            
            # Check script src
            for m in re.finditer(r'<script[^>]+src=["\']([^"\']+)["\']', line):
                src = m.group(1)
                if not src.startswith(('http://', 'https://')):
                    target = os.path.normpath(os.path.join(base_dir, src.split('?')[0]))
                    if not os.path.exists(target):
                        issues.append({'sev': 'Major', 'cat': 'Broken Asset', 'loc': f"{hf}:{i+1}", 'msg': f"Script file not found: {src}"})

            # Check css link href
            for m in re.finditer(r'<link[^>]+rel=["\']stylesheet["\'][^>]+href=["\']([^"\']+)["\']', line):
                href = m.group(1)
                if not href.startswith(('http://', 'https://')):
                    target = os.path.normpath(os.path.join(base_dir, href.split('?')[0]))
                    if not os.path.exists(target):
                        issues.append({'sev': 'Major', 'cat': 'Broken Asset', 'loc': f"{hf}:{i+1}", 'msg': f"Stylesheet not found: {href}"})

    # 2. Check COD references across the whole repository
    print("-> Checking for any remaining COD references...")
    for root, dirs, fnames in os.walk('.'):
        dirs[:] = [d for d in dirs if d not in ['.git', '__pycache__', '.gemini', 'node_modules', 'scripts']]
        for fn in fnames:
            if fn.endswith(('.html', '.js', '.py')):
                p = os.path.normpath(os.path.join(root, fn))
                with open(p, 'r', encoding='utf-8', errors='ignore') as f:
                    for i, l in enumerate(f):
                        if re.search(r'\b(?:cash\s+on\s+delivery|cod)\b', l, re.I):
                            # Ignore comments or desktop copies if any
                            if 'desktop_copies' not in p and 'raw-combined' not in p and not l.strip().startswith('//') and not l.strip().startswith('<!--'):
                                issues.append({'sev': 'Major', 'cat': 'COD Remnant', 'loc': f"{p}:{i+1}", 'msg': f"Remaining COD reference: {l.strip()[:80]}"})

    # 3. Check for XSS and dangerous innerHTML
    print("-> Checking innerHTML usage and sanitization...")
    for hf in ['laptophub.html', 'product.html', 'volts.html', 'custom-laptop.html', 'consult.html', 'inventory.html', 'admin/index.html']:
        if not os.path.exists(hf): continue
        with open(hf, 'r', encoding='utf-8', errors='ignore') as f:
            for i, l in enumerate(f):
                if '.innerHTML =' in l:
                    # check if uses variable without escapeHtml or sanitize
                    if any(v in l for v in ['val', 'name', 'reviewer', 'body', 'comment', 'input', 'query', 'search']) and 'escapeHtml' not in l:
                        issues.append({'sev': 'Major', 'cat': 'Potential XSS', 'loc': f"{hf}:{i+1}", 'msg': f"innerHTML assignment without explicit escapeHtml: {l.strip()[:80]}"})

    # 4. Check for undefined function calls or duplicate IDs
    print("-> Checking DOM IDs in HTML files...")
    for hf in ['laptophub.html', 'product.html']:
        with open(hf, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        ids = re.findall(r'\bid=["\']([^"\']+)["\']', content)
        seen = set()
        dups = set()
        for dom_id in ids:
            if dom_id in seen:
                dups.add(dom_id)
            seen.add(dom_id)
        if dups:
            issues.append({'sev': 'Major', 'cat': 'Duplicate DOM ID', 'loc': hf, 'msg': f"Duplicate IDs found: {list(dups)[:5]}"})

    print(f"Audit completed. Found {len(issues)} candidate issues.")
    for iss in issues:
        print(f"[{iss['sev']}] {iss['cat']} at {iss['loc']}: {iss['msg']}")

if __name__ == '__main__':
    audit()
