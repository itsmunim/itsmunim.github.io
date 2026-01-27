#!/usr/bin/env python3
"""
Simple favicon generator using Pillow.
Generates:
 - favicon/favicon.ico (contains multiple sizes)
 - favicon/favicon-32.png
 - favicon/favicon-16.png
 - favicon/apple-touch-icon.png (180x180)
 - favicon/android-chrome-192x192.png
 - favicon/android-chrome-512x512.png
"""
import os
from PIL import Image

SRC = 'images/profile.jpeg'
OUT_DIR = 'favicon'
SIZES_PNG = {
    'favicon-16.png': (16, 16),
    'favicon-32.png': (32, 32),
    'apple-touch-icon.png': (180, 180),
    'android-chrome-192x192.png': (192, 192),
    'android-chrome-512x512.png': (512, 512),
}
ICO_SIZES = [(16, 16), (32, 32), (48, 48), (64, 64)]

os.makedirs(OUT_DIR, exist_ok=True)

with Image.open(SRC) as im:
    im = im.convert('RGBA')
    w, h = im.size
    # center-crop to square
    size = min(w, h)
    left = (w - size) // 2
    top = (h - size) // 2
    right = left + size
    bottom = top + size
    im_cropped = im.crop((left, top, right, bottom))

    # Save PNG variants
    for name, (sw, sh) in SIZES_PNG.items():
        out_path = os.path.join(OUT_DIR, name)
        im_resized = im_cropped.resize((sw, sh), Image.LANCZOS)
        im_resized.save(out_path, format='PNG')
        print('Saved', out_path)

    # Save multi-size ICO
    ico_path = os.path.join(OUT_DIR, 'favicon.ico')
    # Pillow will generate multiple sizes from the provided sizes list
    im_sizes = [im_cropped.resize(size, Image.LANCZOS) for size in ICO_SIZES]
    im_sizes[0].save(ico_path, format='ICO', sizes=ICO_SIZES)
    print('Saved', ico_path)

print('Favicon generation complete.')
