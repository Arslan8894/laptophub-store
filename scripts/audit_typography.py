import re

pages = ['laptophub.html', 'volts.html', 'custom-laptop.html', 'consult.html', 'inventory.html', 'index.html']

for p in pages:
    with open(p, 'r', encoding='utf-8') as f:
        text = f.read()

    weights = re.findall(r'font-weight:\s*(\d+|bold|bolder|normal);', text)
    counts = {}
    for w in weights:
        counts[w] = counts.get(w, 0) + 1

    print(f"\n=== Typography Weight Distribution in {p} ===")
    total = sum(counts.values())
    for k in sorted(counts.keys()):
        pct = (counts[k] / total) * 100 if total else 0
        print(f"  font-weight: {k:6} -> {counts[k]:3} occurrences ({pct:.1f}%)")

    # Check heavy bold usage (700, 800, bold, bolder)
    heavy = sum(counts.get(w, 0) for w in ['700', '800', 'bold', 'bolder'])
    regular = sum(counts.get(w, 0) for w in ['400', '500', 'normal'])
    print(f"  Heavy weights (700/800/bold): {heavy} ({heavy*100/total:.1f}%) vs Normal/Medium (400/500): {regular} ({regular*100/total:.1f}%)")
