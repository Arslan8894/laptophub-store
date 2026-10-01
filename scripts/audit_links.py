import re
import os

pages = ['index.html', 'laptophub.html', 'volts.html', 'custom-laptop.html', 'consult.html', 'inventory.html']
for p in pages:
    with open(p, 'r', encoding='utf-8') as f:
        html = f.read()
    links = re.findall(r'<a\s+[^>]*?href=[\'"](.*?)[\'"]', html, re.IGNORECASE)
    print(f"\n=== {p} ({len(links)} links found) ===")
    dead_hashes = 0
    for l in links:
        if l == '#' or l == '':
            dead_hashes += 1
            print(f"  [DEAD ANCHOR] href=\"{l}\"")
        elif l.startswith('#'):
            target_id = l[1:]
            found = f'id="{target_id}"' in html or f"id='{target_id}'" in html
            if not found:
                print(f"  [BROKEN IN-PAGE ANCHOR] href=\"{l}\" (no element with id=\"{target_id}\")")
        elif not l.startswith('http') and not l.startswith('mailto') and not l.startswith('tel') and not l.startswith('javascript:'):
            file_part = l.split('#')[0]
            if not os.path.exists(file_part):
                print(f"  [MISSING TARGET FILE] href=\"{l}\"")
    if dead_hashes:
        print(f"  -> Total dead '#' anchors in {p}: {dead_hashes}")
