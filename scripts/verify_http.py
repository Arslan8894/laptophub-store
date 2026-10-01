import urllib.request

urls = [
    'http://127.0.0.1:8080/index.html',
    'http://127.0.0.1:8080/laptophub.html',
    'http://127.0.0.1:8080/volts.html',
    'http://127.0.0.1:8080/custom-laptop.html',
    'http://127.0.0.1:8080/consult.html',
    'http://127.0.0.1:8080/inventory.html',
    'http://127.0.0.1:8080/laptops-data.js'
]

for u in urls:
    resp = urllib.request.urlopen(u, timeout=5)
    name = u.split('/')[-1]
    print(f"[OK] {resp.status} - {name} ({len(resp.read())} bytes)")

print("\nAll 7 storefront endpoints verified running and healthy.")
