import urllib.request
import urllib.parse
import json
import re
import sys
sys.stdout.reconfigure(encoding='utf-8')
import http.cookiejar

BASE_URL = 'http://localhost:8080'

def test_static_files():
    print('--> Testing static files and routes...')
    # product.html
    req = urllib.request.urlopen(f'{BASE_URL}/product.html?id=1')
    assert req.status == 200, f'Expected 200, got {req.status}'
    content = req.read().decode('utf-8')
    assert 'product.css' in content
    assert 'laptops-data.js' in content
    assert 'store-config.js' in content
    assert 'id="specsGridLayout"' in content
    assert 'id="reviewsList"' in content
    assert 'id="ramPillsContainer"' in content
    assert 'id="storagePillsContainer"' in content
    assert 'id="productLivePrice"' in content
    print('  ✓ product.html served correctly with required elements')

    # css/product.css
    req_css = urllib.request.urlopen(f'{BASE_URL}/css/product.css')
    assert req_css.status == 200
    css_content = req_css.read().decode('utf-8')
    assert '.product-hero-grid' in css_content
    assert '.spec-category-card' in css_content
    assert '.product-reviews-section' in css_content
    assert '@media (max-width: 900px)' in css_content
    print('  ✓ css/product.css served correctly with responsive styles')

    # laptophub.html
    req_hub = urllib.request.urlopen(f'{BASE_URL}/laptophub.html')
    assert req_hub.status == 200
    hub_content = req_hub.read().decode('utf-8')
    assert 'openProductPage' in hub_content
    assert 'openLaptopModal' not in hub_content
    assert 'id="laptopModal"' not in hub_content
    assert 'laptophub_scroll_pos' in hub_content
    print('  ✓ laptophub.html refactored to openProductPage with scroll preservation and old modal removed')

def test_cod_removal():
    print('--> Testing COD removal across files...')
    files_to_check = ['laptophub.html', 'product.html', 'store-config.js', 'admin/index.html']
    for file_path in files_to_check:
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()
        matches = re.findall(r'\b(?:cash\s+on\s+delivery|cod)\b', text, re.I)
        assert len(matches) == 0, f'Found {len(matches)} COD occurrences in {file_path}: {matches}'
        print(f'  ✓ 0 COD references in {file_path}')

def test_reviews_api():
    print('--> Testing Reviews API...')
    # 1. GET reviews
    req = urllib.request.urlopen(f'{BASE_URL}/api/reviews?laptop_id=1')
    assert req.status == 200
    data = json.loads(req.read().decode('utf-8'))
    assert 'reviews' in data
    assert 'average' in data
    assert 'count' in data
    print(f'  ✓ GET /api/reviews?laptop_id=1: {data["count"]} reviews, average {data["average"]}')

    # 2. POST review without login -> expect 401
    post_data = json.dumps({'laptop_id': 1, 'rating': 5, 'body': 'Test unauthenticated review'}).encode('utf-8')
    req_unauth = urllib.request.Request(f'{BASE_URL}/api/reviews', data=post_data, headers={'Content-Type': 'application/json'})
    try:
        urllib.request.urlopen(req_unauth)
        assert False, 'Expected 401 Unauthorized for guest review submission'
    except urllib.error.HTTPError as e:
        assert e.code == 401
        print('  ✓ Guest review submission correctly rejected with 401')

    # 3. Login as customer and post review
    cj = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))

    login_data = json.dumps({'email': 'arslan@laptophub.pk', 'password': 'Password123!'}).encode('utf-8')
    login_req = urllib.request.Request(f'{BASE_URL}/api/auth/login', data=login_data, headers={'Content-Type': 'application/json'})
    login_resp = opener.open(login_req)
    assert login_resp.status == 200
    login_json = json.loads(login_resp.read().decode('utf-8'))
    print(f'  ✓ Customer logged in: {login_json["user"]["name"]}')

    # Submit review
    review_body = 'Incredible build quality and battery life! Arrived via express insured dispatch in pristine condition.'
    post_rev = json.dumps({'laptop_id': 2, 'rating': 5, 'body': review_body}).encode('utf-8')
    rev_req = urllib.request.Request(f'{BASE_URL}/api/reviews', data=post_rev, headers={'Content-Type': 'application/json'})
    rev_resp = opener.open(rev_req)
    assert rev_resp.status == 201
    rev_json = json.loads(rev_resp.read().decode('utf-8'))
    created_id = rev_json['review']['id']
    print(f'  ✓ Review posted successfully with ID {created_id}')

    # Verify review shows up
    verify_req = urllib.request.urlopen(f'{BASE_URL}/api/reviews?laptop_id=2')
    v_data = json.loads(verify_req.read().decode('utf-8'))
    found = any(r['id'] == created_id for r in v_data['reviews'])
    assert found, 'Newly posted review not found in listing'
    print('  ✓ Newly posted review verified in GET /api/reviews')

    # 4. Admin deletes review
    # Customer deletes own review
    del_data = json.dumps({'id': created_id}).encode('utf-8')
    del_req = urllib.request.Request(f'{BASE_URL}/api/reviews/delete', data=del_data, headers={'Content-Type': 'application/json'})
    del_resp = opener.open(del_req)
    assert del_resp.status == 200
    print('  ✓ Review deletion verified')

def main():
    print('====================================================')
    print('RUNNING AMAZON-STYLE PRODUCT PAGE VERIFICATION SUITE')
    print('====================================================')
    test_static_files()
    test_cod_removal()
    test_reviews_api()
    print('\n====================================================')
    print('ALL AMAZON-STYLE PRODUCT PAGE TESTS PASSED!')
    print('====================================================')

if __name__ == '__main__':
    main()
