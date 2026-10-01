import urllib.request
import os
import json

os.makedirs('images', exist_ok=True)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

# 1. Direct CDN targets
urls = {
    'dell-latitude-7430.png': 'https://i.dell.com/is/image/DellContent/content/dam/ss2/product-images/dell-client-products/notebooks/latitude-notebooks/14-7430/media-gallery/notebook-latitude-14-7430-t-gray-gallery-2.psd?fmt=png-alpha&wid=800',
    'hp-elitebook-845-g7.png': 'https://hp.widen.net/content/buo6k5yyls/png/buo6k5yyls.png?w=800&h=800&dpi=72&color=ffffff00',
    'hp-probook-640-g10.png': 'https://hp.widen.net/content/klbvdsg77q/png/klbvdsg77q.png?w=800&h=800&dpi=72&color=ffffff00',
    'hp-630-g11.png': 'https://hp.widen.net/content/ltfrrklrar/png/ltfrrklrar.png?w=800&h=800&dpi=72&color=ffffff00',
}

for name, url in urls.items():
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = resp.read()
            target_path = os.path.join('images', name)
            with open(target_path, 'wb') as f:
                f.write(data)
            print(f'Downloaded {name}: {len(data)} bytes')
    except Exception as e:
        print(f'Error downloading {name}: {e}')

# 2. Get Wikimedia direct URLs via MediaWiki API
wiki_files = {
    'macbook-pro-m2.jpg': 'Apple_MacBook_Pro_16"_M2_Max.jpg',
    'hp-spectre-x360.jpg': 'Hp_Spectre_x360_13t.jpg',
    'surface-laptop.jpg': 'Microsoft_Surface_Laptop_7.jpg'
}

for local_name, title in wiki_files.items():
    api_url = f'https://en.wikipedia.org/w/api.php?action=query&titles=File:{urllib.parse.quote(title)}&prop=imageinfo&iiprop=url&format=json'
    try:
        req = urllib.request.Request(api_url, headers=headers)
        with urllib.request.urlopen(req, timeout=15) as resp:
            res = json.loads(resp.read().decode('utf-8'))
            pages = res['query']['pages']
            page = next(iter(pages.values()))
            image_url = page['imageinfo'][0]['url']
            print(f'Found URL for {title}: {image_url}')
            
            img_req = urllib.request.Request(image_url, headers=headers)
            with urllib.request.urlopen(img_req, timeout=20) as img_resp:
                img_data = img_resp.read()
                with open(os.path.join('images', local_name), 'wb') as f:
                    f.write(img_data)
                print(f'Downloaded {local_name}: {len(img_data)} bytes')
    except Exception as e:
        print(f'Error processing {title}: {e}')
