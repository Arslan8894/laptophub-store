import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

for fpath in ['product.html', 'laptophub.html']:
    with open(fpath, 'r', encoding='utf-8') as fp:
        text = fp.read()
    print(f'=== {fpath} ===')
    onclicks = re.findall(r'onclick=[\'"]([a-zA-Z0-9_]+)\(', text)
    for o in sorted(set(onclicks)):
        found = f'function {o}' in text or f'{o} =' in text
        if not found:
            print(f'  MISSING ONCLICK: {o}')
        else:
            # check if defined multiple times
            defs = len(re.findall(rf'function\s+{o}\b', text))
            if defs > 1:
                print(f'  DUPLICATE FUNCTION: {o} ({defs} times)')
