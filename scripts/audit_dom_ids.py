import re

pages = ['laptophub.html', 'volts.html', 'custom-laptop.html', 'consult.html', 'inventory.html', 'index.html']

for page in pages:
    with open(page, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract all getElementById calls
    get_ids = set(re.findall(r"getElementById\(['\"]([^'\"]+)['\"]\)", content))
    # Extract querySelector('#id') calls
    qs_ids = set(re.findall(r"querySelector\(['\"]#([^'\"\s,\.\[\]:]+)['\"]\)", content))
    all_referenced_ids = get_ids.union(qs_ids)

    # Find all declared id="..." in HTML
    declared_ids = set(re.findall(r"\bid=['\"]([^'\"]+)['\"]", content))

    missing = []
    for ref_id in sorted(all_referenced_ids):
        # Ignore dynamically constructed IDs if any
        if ref_id not in declared_ids:
            # Check if dynamically created or template
            if not any(f'id="{ref_id}' in content or f'id=\'{ref_id}' in content for _ in [1]):
                missing.append(ref_id)

    print(f"\n=== {page} ===")
    print(f"  Referenced DOM IDs: {len(all_referenced_ids)}")
    print(f"  Declared DOM IDs: {len(declared_ids)}")
    if missing:
        print(f"  [MISSING DOM IDs ({len(missing)})]:")
        for m in missing:
            print(f"    - #{m}")
    else:
        print("  [OK] All referenced DOM IDs exist in HTML!")
