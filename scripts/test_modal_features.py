import re
import sys

def test_file(filename, modal_id, ram_pills_id, storage_pills_id, comment_id, price_id):
    print(f"--- Checking {filename} ---")
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Modal container check
    assert f'id="{modal_id}"' in content, f"Missing #{modal_id} in {filename}"
    print(f"  [OK] Modal #{modal_id} container found")

    # 2. RAM pills
    for ram in [8, 16, 32]:
        assert f'data-ram="{ram}"' in content, f"Missing data-ram={ram} in {filename}"
    print(f"  [OK] RAM pills (8, 16, 32 GB) found")

    # 3. Storage pills
    for stor in [128, 256, 512, 1000]:
        assert f'data-storage="{stor}"' in content, f"Missing data-storage={stor} in {filename}"
    print(f"  [OK] Storage pills (128, 256, 512, 1TB) found")

    # 4. Comments box
    assert f'id="{comment_id}"' in content, f"Missing #{comment_id} in {filename}"
    print(f"  [OK] Comment textarea #{comment_id} found")

    # 5. Price element
    assert f'id="{price_id}"' in content, f"Missing #{price_id} in {filename}"
    print(f"  [OK] Live price display #{price_id} found")

    # 6. Smooth transition styles
    assert 'cubic-bezier' in content, f"Missing cubic-bezier animation in {filename}"
    assert 'backdrop-filter' in content, f"Missing backdrop-filter blur in {filename}"
    print(f"  [OK] Smooth animation & backdrop blur verified")

    # 7. Check WhatsApp number
    assert "923261398594" in content, f"Missing WhatsApp +923261398594 in {filename}"
    print(f"  [OK] WhatsApp number +923261398594 verified")

if __name__ == "__main__":
    test_file("laptophub.html", "laptopModal", "ramPillsContainer", "storagePillsContainer", "lmodalComment", "lmodalPrice")
    test_file("volts.html", "voltsModal", "voltsRamPills", "voltsStoragePills", "vmodalComment", "vmodalPrice")
    print("\n========================================================")
    print("ALL LAPTOP CARD MODAL & CUSTOMIZER CHECKS PASSED (100%)")
    print("========================================================")
