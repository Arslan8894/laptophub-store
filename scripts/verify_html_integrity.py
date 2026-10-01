# Verify script tags and structural sanity
import re

files = ['laptophub.html', 'admin/index.html', 'admin/login.html', 'consult.html']
for fname in files:
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()
    open_s = len(re.findall(r'<script', content, re.I))
    close_s = len(re.findall(r'</script>', content, re.I))
    open_d = content.count('<div')
    close_d = content.count('</div>')
    print(f"{fname}: len={len(content)}, scripts={open_s}/{close_s}, divs={open_d}/{close_d}")
