"""
generate_placeholders.py
Run once to create SVG placeholder images for all slots
so the game works out of the box before you add real photos.

Usage:  python generate_placeholders.py
"""
import os

IMAGES_DIR = os.path.join("static", "images")
AUDIO_DIR  = os.path.join("static", "audio")
os.makedirs(IMAGES_DIR, exist_ok=True)
os.makedirs(AUDIO_DIR,  exist_ok=True)

def make_svg(filename, label, color="#ff69b4"):
    path = os.path.join(IMAGES_DIR, filename)
    if os.path.exists(path):
        return
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="600" height="400">
  <defs>
    <linearGradient id="g" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#0d0618"/>
      <stop offset="100%" style="stop-color:#1f0f3a"/>
    </linearGradient>
  </defs>
  <rect width="600" height="400" fill="url(#g)"/>
  <text x="300" y="170" text-anchor="middle" font-size="72" font-family="Georgia">📷</text>
  <text x="300" y="230" text-anchor="middle" font-size="22"
        font-family="Georgia" fill="{color}" font-style="italic">{label}</text>
  <text x="300" y="265" text-anchor="middle" font-size="14"
        font-family="Arial" fill="#7c6b8e">Replace with your photo</text>
</svg>'''
    with open(path, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Created: {path}")

# All image placeholders
make_svg("level1.jpg",    "Level 1 — First Memory",       "#ff69b4")
make_svg("memory1.jpg",   "Memory 1 — First Date",        "#c084fc")
make_svg("memory2.jpg",   "Memory 2 — Adventure",         "#ff69b4")
make_svg("memory3.jpg",   "Memory 3 — Quiet Moments",     "#c084fc")
make_svg("slide1.jpg",    "Slideshow 1",                  "#ff69b4")
make_svg("slide2.jpg",    "Slideshow 2",                  "#c084fc")
make_svg("slide3.jpg",    "Slideshow 3",                  "#ff69b4")
make_svg("slide4.jpg",    "Slideshow 4",                  "#c084fc")
make_svg("slide5.jpg",    "Slideshow 5",                  "#ff69b4")
make_svg("easter_egg.jpg","Secret Easter Egg",            "#f9c74f")

# Audio placeholder (silent mp3 marker)
for audio_file in ["music.mp3", "memory.mp3"]:
    path = os.path.join(AUDIO_DIR, audio_file)
    if not os.path.exists(path):
        open(path, "wb").close()  # empty file as placeholder
        print(f"Created audio placeholder: {path}")

print("\n✅ All placeholders created!")
print("📁 Replace files in static/images/ with your photos (.jpg or .png)")
print("🎵 Replace files in static/audio/ with your recordings (.mp3)")
