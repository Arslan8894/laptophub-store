import re

file_path = r"c:\Users\Arslan\.antigravity-ide\laptop-store\consult.html"
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add script tag in head if not present
if '<script src="laptops-data.js"></script>' not in content:
    content = content.replace('</head>', '<script src="laptops-data.js"></script>\n</head>')

# 2. Adjust budget slider range to cover 35k to 800k
content = content.replace(
    'min="50000" max="500000" value="130000" step="5000"',
    'min="35000" max="800000" value="130000" step="5000"'
)
content = content.replace(
    '<span>50K</span><span>150K</span><span>300K</span><span>500K</span>',
    '<span>35K</span><span>100K</span><span>250K</span><span>500K</span><span>800K</span>'
)

# 3. Replace inventory database in script
new_inventory_code = '''  // ── LAPTOP DATABASE (Connected to all 69 models from laptops-data.js) ────────
  let inventory = [];
  if (typeof LAPTOPS_INVENTORY !== 'undefined') {
    inventory = LAPTOPS_INVENTORY.map(lap => ({
      name: lap.name,
      brand: lap.brand,
      cpu: lap.cpu,
      cpuTags: [lap.cpuTag, 'any', lap.brand],
      ram: lap.ram,
      storage: lap.storage,
      gpu: lap.gpuType,
      gpuTags: [lap.gpuType, (lap.gpuType === 'rtx' || lap.gpuType === 'discrete') ? 'any_discrete' : 'integrated', 'no_pref'],
      price: lap.price,
      useCaseTags: [...lap.useCases, 'any'],
      img: lap.img,
      highlight: `${lap.category} · ${lap.display} · ${lap.gpu}`
    }));
  } else {
    // Fallback if standalone
    inventory = [
      { name: 'Dell Latitude 7430', cpu: 'Intel Core i7-1265U', cpuTags: ['intel_i7','any'], ram: 16, storage: 512, gpu: 'integrated', gpuTags: ['integrated','no_pref'], price: 154000, useCaseTags: ['office','programming','any'], img: 'images/dell-latitude-7430.png', highlight: 'Enterprise Ultrabook · 14" FHD IPS' }
    ];
  }
'''

# Replace from const inventory = [ ... to // ── RESULTS ENGINE
inv_pattern = re.compile(r'// ── LAPTOP DATABASE.*?(?=// ── RESULTS ENGINE)', re.DOTALL)
content = inv_pattern.sub(new_inventory_code, content, count=1)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated consult.html successfully!")
