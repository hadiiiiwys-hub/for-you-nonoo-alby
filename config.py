# ============================================================
# LOVE GAME CONFIGURATION FILE
# Edit everything here — questions, answers, photos, messages
# ============================================================

# ── RELATIONSHIP INFO ──────────────────────────────────────
RELATIONSHIP_START_DATE = "2024-12-28"   # Format: YYYY-MM-DD
PARTNER_NAME = "My nonoo"                 # Name shown in messages
YOUR_NAME    = "ayman"               # Your name

# ── WELCOME SCREEN ────────────────────────────────────────
WELCOME_TITLE   = "Welcome to Our Love Journey ya alby ❤️"
WELCOME_MESSAGE = "A little game just for you, to celebrate everything we are."

# ── LEVEL 1 — Romantic Question ──────────────────────────
LEVEL1 = {
    "question": "Do you remember when we first met?",
    "answer":   "sanstifano",          # Correct answer (case-insensitive, partial match OK)
    "hint":     "sanstifano or club or or bank ☕",
    "reward_message": "You remembered! That day changed everything for me. 💕",
    "reward_image": "C:\Users\Hello\Downloads\love_game\love_game\static\images",  # Place your photo at static/images/level1.jpg
}

# ── LEVEL 2 — Memory Challenge ───────────────────────────
LEVEL2 = {
    "question": "Which is the first game we played togethr?",
    "choices":  ["السلم والثعبان", "بلياردو", "لودو", ],
    "answer":   "بلياردو",             # Must match one of the choices exactly
    "voice_file": "audio/memory.mp3",   # Place your recording at static/audio/memory.mp3
    "message": "That trip was pure magic. Every street felt like it was made for us. 🌹",
}

# ── LEVEL 3 — Memory Gallery ─────────────────────────────
LEVEL3_CARDS = [
    {
        "title": "Our second Date ✨",
        "image": "C:\Users\Hello\Downloads\love_game\love_game\static\images",      # static/images/memory1.jpg
        "description": "That evening felt like a dream. The way you laughed...",
        "message": " ده كان احلي يوم في عمري يا نور عيني بجدد.",
    },
    {
        "title": "Adventure Together 🌄",
        "image": "C:\Users\Hello\Downloads\love_game\love_game\static\images",      # static/images/memory2.jpg
        "description": "The world is better with you in it.",
        "message": "Every adventure is ten times better with you by my side.",
    },
    {
        "title": "Quiet Moments 🌙",
        "image": "C:\Users\Hello\Downloads\love_game\love_game\static\images",      # static/images/memory3.jpg
        "description": "Sometimes the best moments are the silent ones.",
        "message": "I love the quiet moments most — just being with you is enough.",
    },
]

# ── LEVEL 4 — Find the Heart ─────────────────────────────
LEVEL4 = {
    "correct_index": 4,   # 0–8, which of the 9 hearts is the right one
    "celebration_message": "You found it! Just like you found your way into my heart. 💖",
}

# ── LEVEL 5 — Secret Message Puzzle ──────────────────────
LEVEL5 = {
    "phrase": "YOU ARE MY EVERYTHING",   # The phrase to unscramble
    "success_message": "Yes! That's exactly how I feel. Every single day. 🎉",
}

# ── FINAL LEVEL — Slideshow ──────────────────────────────
FINAL_LEVEL = {
    "slideshow_images": [
        "C:\Users\Hello\Downloads\love_game\love_game\static\images",   # Place photos at static/images/slideN.jpg
        "C:\Users\Hello\Downloads\love_game\love_game\static\images",
        "C:\Users\Hello\Downloads\love_game\love_game\static\images",
        "C:\Users\Hello\Downloads\love_game\love_game\static\images",
        "C:\Users\Hello\Downloads\love_game\love_game\static\images",
    ],
    "background_music": "audio/music.mp3",   # static/audio/music.mp3
    "love_letter": """My dearest {partner},

From the very first moment I saw you, I knew my life would never be the same.
You are the missing piece I never knew I was searching for.

Every day with you is a gift — your laugh, your warmth, your endless kindness
make me fall in love with you all over again.

Thank you for every memory we've built together. Thank you for choosing me.

This little journey is just a tiny glimpse of how much you mean to me.

Forever yours,
{yours}""",
}

# ── FINAL SURPRISE ────────────────────────────────────────
FINAL_SURPRISE = {
    "custom_message": "i love you so much ya nonyyy albyyyy entyyyy. 💍",
    "button_label":   "Click for the Final Surprise ❤️",
}

# ── EASTER EGG ────────────────────────────────────────────
EASTER_EGG = {
    "title":   "You found the secret! 🥚✨",
    "message": "Not everyone finds this page. But then again, you've always been extraordinary.",
    "image":   "C:\Users\Hello\Downloads\love_game\love_game\static\images",   # static/images/easter_egg.jpg
}
