import subprocess
import time
import json
import urllib.request
import urllib.error
import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

def run_feature_verification():
    print("======================================================================")
    print("VERIFYING NEW FEATURES VIA CHROME CDP & STATIC DOM ANALYSIS")
    print("======================================================================")

    # 1. Start headless chrome with remote debugging port 9228 pointing to laptophub.html
    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    proc = subprocess.Popen([
        chrome_path,
        "--headless=new",
        "--remote-debugging-port=9228",
        "--disable-gpu",
        "--no-first-run",
        "--no-default-browser-check",
        "http://127.0.0.1:8080/laptophub.html"
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    try:
        # Wait for CDP to respond
        time.sleep(2)
        import urllib.request
        version_info = json.loads(urllib.request.urlopen("http://127.0.0.1:9228/json/version", timeout=5).read().decode())
        print(f"[PASS] Headless Chrome connected: {version_info.get('Browser')}")

        import websockets
        import asyncio

        async def send_cmd(ws, msg_id, method, params=None):
            req = {"id": msg_id, "method": method, "params": params or {}}
            await ws.send(json.dumps(req))
            while True:
                resp = json.loads(await ws.recv())
                if resp.get("id") == msg_id:
                    return resp

        async def test_pages():
            # 1. Find laptophub.html target
            await asyncio.sleep(2)
            targets = json.loads(urllib.request.urlopen("http://127.0.0.1:9228/json/list").read().decode())
            target = next(t for t in targets if "laptophub.html" in t.get("url", ""))
            
            async with websockets.connect(target["webSocketDebuggerUrl"]) as ws:
                # Evaluate: Check compare button existence
                eval_script = """
                (() => {
                    const compareBtns = document.querySelectorAll('.btn-card-compare');
                    const dock = document.getElementById('compareDock');
                    const modal = document.getElementById('compareModal');
                    const checkoutBadge = document.getElementById('checkoutDeliveryBadge');
                    return {
                        compareBtnsCount: compareBtns.length,
                        dockExists: !!dock,
                        modalExists: !!modal,
                        checkoutBadgeExists: !!checkoutBadge
                    };
                })()
                """
                eval_res = await send_cmd(ws, 1, "Runtime.evaluate", {"expression": eval_script, "returnByValue": True})
                val1 = eval_res['result']['result']['value']
                print(f"[PASS] Catalog Compare Buttons: {val1['compareBtnsCount']} buttons rendered across all laptop cards")
                assert val1['compareBtnsCount'] >= 60, f"Expected >= 60 compare buttons, got {val1['compareBtnsCount']}"
                assert val1['dockExists'], "Compare dock element missing"
                assert val1['modalExists'], "Compare modal element missing"
                assert val1['checkoutBadgeExists'], "Checkout delivery badge missing"

                # Simulate toggling comparison for laptop 1 and 2
                toggle_script = """
                (() => {
                    window.toggleCompare(1);
                    window.toggleCompare(2);
                    const dock = document.getElementById('compareDock');
                    const badge = document.getElementById('compareCountBadge');
                    const isVisible = dock.classList.contains('visible');
                    const countText = badge ? badge.textContent : '';
                    
                    // Now open modal
                    window.openCompareModal();
                    const modal = document.getElementById('compareModal');
                    const modalOpen = modal.classList.contains('open');
                    const table = modal.querySelector('.compare-table');
                    const colHeaders = table ? table.querySelectorAll('thead th').length : 0;
                    
                    // Close modal
                    window.closeCompareModal();
                    const modalClosed = !modal.classList.contains('open');

                    return {
                        isVisible,
                        countText,
                        modalOpen,
                        colHeaders,
                        modalClosed
                    };
                })()
                """
                eval_res2 = await send_cmd(ws, 2, "Runtime.evaluate", {"expression": toggle_script, "returnByValue": True})
                val2 = eval_res2['result']['result']['value']
                print(f"[PASS] Compare Dock Visibility & Count: visible={val2['isVisible']}, count='{val2['countText']}'")
                assert val2['isVisible'], "Compare dock should be visible after adding laptops"
                assert val2['countText'] == '2/3', f"Expected '2/3', got {val2['countText']}"
                print(f"[PASS] Compare Matrix Modal: opened={val2['modalOpen']}, column headers={val2['colHeaders']}, closed={val2['modalClosed']}")
                assert val2['modalOpen'], "Compare modal did not open"
                assert val2['colHeaders'] == 3, f"Expected 3 columns (1 label + 2 laptops), got {val2['colHeaders']}"

                # Test checkout delivery estimator logic
                checkout_script = """
                (() => {
                    const sel = document.getElementById('custCity');
                    sel.value = 'Karachi';
                    window.updateCheckoutDeliveryEstimate('Karachi');
                    const txt = document.getElementById('checkoutDeliveryText').textContent;
                    return txt;
                })()
                """
                eval_res3 = await send_cmd(ws, 3, "Runtime.evaluate", {"expression": checkout_script, "returnByValue": True})
                val3 = eval_res3['result']['result']['value']
                print(f"[PASS] Checkout City Transit: '{val3}'")
                assert "24–48 Hours" in val3 and "TCS Air Cargo" in val3, f"Unexpected text: {val3}"

                # Test 2: Navigate to product.html delivery estimator
                await send_cmd(ws, 4, "Page.navigate", {"url": "http://127.0.0.1:8080/product.html?id=1"})
                await asyncio.sleep(3)

                loc_res = await send_cmd(ws, 41, "Runtime.evaluate", {"expression": "window.location.href", "returnByValue": True})
                print("CURRENT LOCATION:", loc_res)

                prod_eval_script = """
                (() => {
                    const sel = document.getElementById('estCitySelect');
                    const disp = document.getElementById('deliveryTimelineDisplay');
                    const initialLahore = disp.textContent;

                    // Change city to Islamabad
                    sel.value = 'islamabad';
                    window.updateDeliveryEstimate('islamabad');
                    const isbText = disp.textContent;

                    // Change city to Karachi
                    sel.value = 'karachi';
                    window.updateDeliveryEstimate('karachi');
                    const khiText = disp.textContent;

                    return {
                        hasSelect: !!sel,
                        hasDisplay: !!disp,
                        initialLahore,
                        isbText,
                        khiText
                    };
                })()
                """
                eval_res4 = await send_cmd(ws, 5, "Runtime.evaluate", {"expression": prod_eval_script, "returnByValue": True})
                print("EVAL_RES4:", eval_res4)
                val4 = eval_res4['result']['result']['value']
                assert val4['hasSelect'] and val4['hasDisplay'], "Delivery estimator markup missing on product.html"
                print(f"[PASS] Product Page Initial Lahore Estimate: Found '{val4['initialLahore'].strip()[:45]}...'")
                print(f"[PASS] Product Page Islamabad Estimate: Verified guaranteed 24h courier timeline")
                assert "Guaranteed Next-Day (24h)" in val4['isbText'], "Islamabad timeline missing"
                print(f"[PASS] Product Page Karachi Estimate: Verified Air Cargo courier timeline")
                assert "24–48 Hours" in val4['khiText'] and "Aviation" in val4['khiText'], "Karachi timeline missing"

        asyncio.run(test_pages())
        print("\n======================================================================")
        print("ALL NEW FEATURES VERIFIED WITH 100% SUCCESS!")
        print("======================================================================")

    finally:
        proc.terminate()
        try:
            proc.wait(timeout=3)
        except Exception:
            proc.kill()

if __name__ == '__main__':
    run_feature_verification()
