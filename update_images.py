import re

with open('laptops-data.js', 'r', encoding='utf-8') as f:
    content = f.read()

id_map = {
    1:  'images/lenovo-t14-g1.jpg',
    6:  'images/lenovo-t14-g1.jpg',
    4:  'images/lenovo-x1-yoga.jpg',
    5:  'images/lenovo-x13.jpg',
    28: 'images/lenovo-x13.jpg',
    17: 'images/lenovo-t14-g1.jpg',
    7:  'images/lenovo-t14-g1.jpg',
    34: 'images/lenovo-t14-g1.jpg',
    21: 'images/lenovo-x1-yoga.jpg',
    3:  'images/hp-elitebook-840g9.jpg',
    23: 'images/hp-elitebook-840g9.jpg',
    24: 'images/hp-elitebook-840g7.jpg',
    10: 'images/hp-elitebook-840g9.jpg',
    12: 'images/hp-elitebook-840g9.jpg',
    27: 'images/hp-elitebook-840g9.jpg',
    35: 'images/hp-elitebook-840g9.jpg',
    15: 'images/hp-elitebook-840g7.jpg',
    19: 'images/hp-elitebook-840g7.jpg',
    16: 'images/hp-elitebook-840g9.jpg',
    18: 'images/hp-elitebook-840g7.jpg',
    9:  'images/dell-5320.jpg',
    11: 'images/dell-5320.jpg',
    13: 'images/dell-5320.jpg',
    33: 'images/dell-5320.jpg',
    14: 'images/dell-5320.jpg',
    30: 'images/dell-5320.jpg',
    32: 'images/dell-5320.jpg',
    22: 'images/lenovo-x1-yoga.jpg',
    31: 'images/lenovo-x1-yoga.jpg',
    25: 'images/dell-5320.jpg',
    29: 'images/dell-5320.jpg',
    2:  'images/surface-tab.svg',
    20: 'images/surface-tab.svg',
    8:  'images/dell-xps.svg',
    26: 'images/dell-xps.svg',
    36: 'images/alienware.svg',
}

def replace_img(content, laptop_id, new_img):
    pattern = (
        r'("id"\s*:\s*' + str(laptop_id) + r'\b'
        r'(?:(?!"id"\s*:).)*?)'
        r'("img"\s*:\s*)"[^"]*"'
    )
    repl = r'\g<1>\g<2>"' + new_img + '"'
    new_content, n = re.subn(pattern, repl, content, count=1, flags=re.DOTALL)
    return new_content, n

changes = 0
for lid, img in sorted(id_map.items()):
    content, n = replace_img(content, lid, img)
    if n:
        changes += 1
        print(f'  ID {lid:>2} -> {img}')
    else:
        print(f'  ID {lid:>2} NOT FOUND')

with open('laptops-data.js', 'w', encoding='utf-8') as f:
    f.write(content)

print(f'\nDone: {changes} IDs updated')
