#!/usr/bin/env python3
"""
process_image_blending.py
Analyzes laptop images in laptops-data.js, samples edge pixels, classifies background
tone (white, colorful, dark), extracts dominant color and soft tint, and generates
clean transparent WebP cutouts for white-background laptops while keeping originals intact.
Updates laptops-data.js with bgTone, bgColor, tintColor, and processedImg.
"""

import os
import sys
import json
import re
from PIL import Image, ImageDraw, ImageFilter

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_JS = os.path.join(BASE_DIR, 'laptops-data.js')
PROCESSED_DIR = os.path.join(BASE_DIR, 'images', 'processed')

os.makedirs(PROCESSED_DIR, exist_ok=True)


def analyze_image_background(img_path_rel):
    """
    Analyzes an image's edge pixels and returns:
      - tone: 'white', 'colorful', or 'dark'
      - avg_rgb: (r, g, b)
      - lum: float
      - sat: float
      - tint_color: CSS rgba string with capped opacity
      - bg_color: CSS rgb string
    """
    abs_path = os.path.join(BASE_DIR, img_path_rel) if not os.path.isabs(img_path_rel) else img_path_rel
    if not os.path.exists(abs_path):
        return {
            'tone': 'white',
            'avg_rgb': (255, 255, 255),
            'lum': 255.0,
            'sat': 0.0,
            'bg_color': 'rgb(255, 255, 255)',
            'tint_color': 'rgba(76, 124, 255, 0.04)',
            'error': 'File not found'
        }

    with Image.open(abs_path) as im:
        w, h = im.size
        im_rgb = im.convert('RGB')
        edge_pixels = []

        # Sample border pixels (5px outer ring)
        step_x = max(1, w // 40)
        step_y = max(1, h // 40)

        for y in range(0, min(5, h)):
            for x in range(0, w, step_x):
                edge_pixels.append(im_rgb.getpixel((x, y)))
        for y in range(max(0, h - 5), h):
            for x in range(0, w, step_x):
                edge_pixels.append(im_rgb.getpixel((x, y)))
        for x in range(0, min(5, w)):
            for y in range(0, h, step_y):
                edge_pixels.append(im_rgb.getpixel((x, y)))
        for x in range(max(0, w - 5), w):
            for y in range(0, h, step_y):
                edge_pixels.append(im_rgb.getpixel((x, y)))

        if not edge_pixels:
            avg_r, avg_g, avg_b = 255, 255, 255
        else:
            avg_r = sum(p[0] for p in edge_pixels) / len(edge_pixels)
            avg_g = sum(p[1] for p in edge_pixels) / len(edge_pixels)
            avg_b = sum(p[2] for p in edge_pixels) / len(edge_pixels)

        lum = 0.2126 * avg_r + 0.7152 * avg_g + 0.0722 * avg_b
        max_c = max(avg_r, avg_g, avg_b)
        min_c = min(avg_r, avg_g, avg_b)
        sat = (max_c - min_c) / max_c if max_c > 0 else 0

        r_int, g_int, b_int = round(avg_r), round(avg_g), round(avg_b)

        # Classification
        if lum >= 235 and sat < 0.15:
            tone = 'white'
            # Subtle stage glow for white tone (cool blue highlight, capped low)
            tint_color = 'rgba(76, 124, 255, 0.04)'
        elif lum < 60:
            tone = 'dark'
            # Very low capped tint (4-6%), slightly lightened
            tint_r = min(255, r_int + 45)
            tint_g = min(255, g_int + 45)
            tint_b = min(255, b_int + 60)
            tint_color = f'rgba({tint_r}, {tint_g}, {tint_b}, 0.06)'
        else:
            tone = 'colorful'
            # Capped opacity (12-16%) for soft bleed into card
            tint_color = f'rgba({r_int}, {g_int}, {b_int}, 0.15)'

        bg_color = f'rgb({r_int}, {g_int}, {b_int})'

        return {
            'tone': tone,
            'avg_rgb': (r_int, g_int, b_int),
            'lum': round(lum, 1),
            'sat': round(sat, 2),
            'bg_color': bg_color,
            'tint_color': tint_color,
            'width': w,
            'height': h
        }


def generate_transparent_cutout(img_path_rel, laptop_id):
    """
    Creates a transparent WebP cutout by floodfilling white background from image borders.
    Keeps the original image completely untouched as backup.
    Returns:
      (processed_rel_path, keep_ratio, status_message)
    """
    abs_path = os.path.join(BASE_DIR, img_path_rel) if not os.path.isabs(img_path_rel) else img_path_rel
    if not os.path.exists(abs_path):
        return None, 0.0, "Original image file not found"

    try:
        im = Image.open(abs_path).convert('RGB')
        w, h = im.size

        # Downscale for floodfill if image is massive (>1800px) to optimize speed and memory
        orig_w, orig_h = w, h
        max_dim = 1600
        scale = 1.0
        if max(w, h) > max_dim:
            scale = max_dim / max(w, h)
            new_w, new_h = int(w * scale), int(h * scale)
            work_im = im.resize((new_w, new_h), Image.Resampling.LANCZOS)
        else:
            work_im = im

        ww, wh = work_im.size
        gray = work_im.convert('L')
        # Threshold: 244 brightness
        bin_img = gray.point(lambda p: 255 if p >= 244 else 0)

        pix = bin_img.load()
        step_x = max(1, ww // 30)
        step_y = max(1, wh // 30)

        for x in range(0, ww, step_x):
            if pix[x, 0] == 255:
                ImageDraw.floodfill(bin_img, (x, 0), 128)
            if pix[x, wh - 1] == 255:
                ImageDraw.floodfill(bin_img, (x, wh - 1), 128)
        for y in range(0, wh, step_y):
            if pix[0, y] == 255:
                ImageDraw.floodfill(bin_img, (0, y), 128)
            if pix[ww - 1, y] == 255:
                ImageDraw.floodfill(bin_img, (ww - 1, y), 128)

        # In bin_img: 128 is connected background
        alpha_small = bin_img.point(lambda p: 0 if p == 128 else 255)

        # Scale alpha back if needed
        if scale != 1.0:
            alpha = alpha_small.resize((orig_w, orig_h), Image.Resampling.BILINEAR)
        else:
            alpha = alpha_small

        # Check ratio of kept laptop pixels
        hist = alpha.histogram()
        keep_px = sum(hist[1:])
        total_px = orig_w * orig_h
        ratio = keep_px / total_px

        # Health checks:
        # If ratio is too small (< 12%) or too large (> 88%), floodfill may have leaked or failed
        if ratio < 0.12 or ratio > 0.88:
            return None, ratio, f"Keep ratio {ratio*100:.1f}% outside safe range [12%, 88%]"

        # Feather alpha edge with 0.8px Gaussian blur to eliminate aliasing and jagged edges
        alpha_smooth = alpha.filter(ImageFilter.GaussianBlur(0.8))

        out_rgba = im.convert('RGBA')
        out_rgba.putalpha(alpha_smooth)

        # Save transparent WebP
        out_filename = f"laptop-{laptop_id}-cutout.webp"
        out_rel_path = f"images/processed/{out_filename}"
        out_abs_path = os.path.join(BASE_DIR, out_rel_path)

        out_rgba.save(out_abs_path, 'WEBP', quality=92, method=4)

        return out_rel_path, ratio, "Clean cutout generated"

    except Exception as e:
        return None, 0.0, f"Processing exception: {str(e)}"


def run_full_inventory_blending():
    print(f"Reading dataset: {DATA_JS}")
    with open(DATA_JS, 'r', encoding='utf-8') as f:
        text = f.read()

    m = re.search(r'const\s+LAPTOPS_INVENTORY\s*=\s*(\[\s*\{.*\}\s*\]);', text, re.DOTALL)
    if not m:
        m = re.search(r'LAPTOPS_INVENTORY\s*=\s*(\[.*?\])\s*;?\s*$', text, re.DOTALL)
    data = json.loads(m.group(1))

    print(f"Loaded {len(data)} laptops. Starting analysis and processing...")

    summary = []
    review_flagged = []

    for lap in data:
        lid = lap['id']
        name = lap['name']
        orig_img = lap['img']

        # 1. Analyze background
        analysis = analyze_image_background(orig_img)
        tone = analysis['tone']
        tint = analysis['tint_color']
        bg_col = analysis['bg_color']

        lap['bgTone'] = tone
        lap['bgColor'] = bg_col
        lap['tintColor'] = tint

        technique = ""
        processed_path = orig_img

        if tone == 'white':
            cutout_path, ratio, msg = generate_transparent_cutout(orig_img, lid)
            if cutout_path:
                processed_path = cutout_path
                technique = f"Transparent WebP Cutout (kept {ratio*100:.1f}% area)"
                # Flag if ratio is borderline
                if ratio < 0.18:
                    review_flagged.append({
                        'id': lid,
                        'name': name,
                        'reason': f"Area ratio low ({ratio*100:.1f}%), check chassis edges",
                        'path': processed_path
                    })
            else:
                technique = f"Fallback: mix-blend-mode multiply + soft stage ({msg})"
                review_flagged.append({
                    'id': lid,
                    'name': name,
                    'reason': f"Cutout fallback triggered: {msg}",
                    'path': orig_img
                })
        elif tone == 'colorful':
            technique = f"Feather Mask (CSS radial fade) + Dominant Tint ({analysis['avg_rgb']})"
            processed_path = orig_img
        else:  # dark
            technique = f"Feather Mask + Desaturated Low Tint ({analysis['avg_rgb']})"
            processed_path = orig_img

        lap['processedImg'] = processed_path

        summary.append({
            'id': lid,
            'name': name,
            'tone': tone,
            'bgColor': bg_col,
            'tintColor': tint,
            'technique': technique,
            'origImg': orig_img,
            'processedImg': processed_path
        })
        print(f"[{lid:2d}/69] {name[:30]:30s} | Tone: {tone:8s} | Technique: {technique}")

    # Write updated dataset
    js_content = f"// Complete {len(data)}-Laptop Real Inventory Dataset\nconst LAPTOPS_INVENTORY = {json.dumps(data, indent=2)};\n\nif (typeof module !== 'undefined') module.exports = LAPTOPS_INVENTORY;\n"
    with open(DATA_JS, 'w', encoding='utf-8') as f:
        f.write(js_content)

    print(f"\nSuccessfully updated {DATA_JS} with all 69 laptop blending parameters!")
    print(f"Total processed: {len(summary)}")
    print(f"Images flagged for review: {len(review_flagged)}")
    if review_flagged:
        for rf in review_flagged:
            print(f" - ID {rf['id']}: {rf['name']} ({rf['reason']})")

    # Save summary report as JSON for documentation
    summary_path = os.path.join(BASE_DIR, 'scripts', 'blending_report.json')
    with open(summary_path, 'w', encoding='utf-8') as f:
        json.dump({'summary': summary, 'flagged': review_flagged}, f, indent=2)

    return summary, review_flagged


if __name__ == '__main__':
    run_full_inventory_blending()
