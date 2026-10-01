import json
import urllib.request
import urllib.parse
import os
import time

RATE_LIMIT_CACHE = {}

def get_ai_recommendation(prefs, matched_laptops):
    valid_ids = {lap['id'] for lap in matched_laptops if 'id' in lap}
    if not valid_ids:
        return {'success': False, 'fallback': True, 'error': 'No valid laptop IDs'}

    api_key = os.environ.get('GEMINI_API_KEY') or os.environ.get('GOOGLE_API_KEY')
    
    # Also check local .env file
    env_path = os.path.join(os.path.dirname(__file__), '..', '.env')
    if not api_key and os.path.exists(env_path):
        try:
            with open(env_path, 'r', encoding='utf-8') as f:
                for line in f:
                    if line.startswith('GEMINI_API_KEY=') or line.startswith('GOOGLE_API_KEY='):
                        api_key = line.split('=', 1)[1].strip()
                        break
        except Exception:
            pass

    if not api_key:
        return {
            'success': False,
            'fallback': True,
            'message': 'AI service offline: GEMINI_API_KEY is not configured in backend environment.'
        }

    # Format structured candidate list
    candidate_summary = []
    for lap in matched_laptops[:8]:
        candidate_summary.append({
            'id': lap['id'],
            'name': lap.get('name'),
            'brand': lap.get('brand'),
            'cpu': lap.get('cpu'),
            'ramGb': lap.get('ramGb', lap.get('ram')),
            'storageGb': lap.get('storageGb', lap.get('storage')),
            'gpu': lap.get('gpu'),
            'price': lap.get('priceFormatted', f"Rs {lap.get('price', 0):,}"),
            'condition': lap.get('condition')
        })

    prompt_text = (
        f"You are LaptopHUB's senior laptop hardware consultant in Pakistan.\n"
        f"User Preferences:\n"
        f"- Target Use Case: {prefs.get('usecase', 'General')}\n"
        f"- Preferred CPU: {prefs.get('cpu', 'Any')}\n"
        f"- Minimum RAM: {prefs.get('ram', 16)} GB\n"
        f"- Minimum SSD: {prefs.get('storage', 512)} GB\n"
        f"- GPU Requirement: {prefs.get('gpu', 'Any')}\n"
        f"- Maximum Budget: PKR {Number(prefs.get('budget', 130000)):,}\n\n"
        f"Matched Laptops in Stock (Select ONLY from this list):\n"
        f"{json.dumps(candidate_summary, indent=2)}\n\n"
        f"Instructions:\n"
        f"1. Select the single best laptop ID from the provided list that maximizes value for the user.\n"
        f"2. Explain why in 2-3 friendly, authoritative sentences.\n"
        f"3. Highlight tradeoffs comparing it to the other matches in 1-2 friendly sentences.\n"
        f"4. You MUST respond with JSON matching this schema: "
        f'{{"recommendedLaptopId": <int>, "reason": "<string>", "tradeoffs": "<string>"}}\n'
        f"5. NEVER recommend any laptop ID that is not in the list. Do not invent any specs."
    )

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
    req_body = {
        "contents": [{"parts": [{"text": prompt_text}]}],
        "generationConfig": {
            "temperature": 0.2,
            "responseMimeType": "application/json"
        }
    }

    try:
        data_bytes = json.dumps(req_body).encode('utf-8')
        req = urllib.request.Request(
            url,
            data=data_bytes,
            headers={'Content-Type': 'application/json'},
            method='POST'
        )
        with urllib.request.urlopen(req, timeout=7) as resp:
            resp_data = json.loads(resp.read().decode('utf-8'))
            
        candidates = resp_data.get('candidates', [])
        if candidates and 'content' in candidates[0]:
            parts = candidates[0]['content'].get('parts', [])
            if parts and 'text' in parts[0]:
                ai_json = json.loads(parts[0]['text'])
                rec_id = int(ai_json.get('recommendedLaptopId'))
                if rec_id in valid_ids:
                    return {
                        'success': True,
                        'recommendation': {
                            'recommendedLaptopId': rec_id,
                            'reason': ai_json.get('reason', ''),
                            'tradeoffs': ai_json.get('tradeoffs', '')
                        }
                    }
    except Exception as e:
        return {
            'success': False,
            'fallback': True,
            'error': str(e),
            'message': 'AI call failed or timed out. Falling back to deterministic matching.'
        }

    return {
        'success': False,
        'fallback': True,
        'message': 'AI recommendation could not be validated against candidate list.'
    }

print("Testing get_ai_recommendation with simulated laptops...")
dummy_laptops = [
    {"id": 1, "name": "Lenovo T14", "price": 98000, "ram": 16, "storage": 512},
    {"id": 3, "name": "HP EliteBook 840 G9", "price": 165000, "ram": 16, "storage": 512}
]
dummy_prefs = {"usecase": "office", "budget": 180000}

res = get_ai_recommendation(dummy_prefs, dummy_laptops)
print("Result with no key:", res)
assert res['fallback'] is True, "Should gracefully fall back when API key is not configured"
print("Test passed successfully!")
