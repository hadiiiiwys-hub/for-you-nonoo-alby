# 💖 Love Game — A Romantic Interactive Web Game

A beautiful, mobile-first romantic game built with **Flask + HTML/CSS/JS**.
Share it as a link on WhatsApp, Instagram, or any messaging platform.

---

## 📁 Project Structure

```
love_game/
├── app.py                    # Flask app — routes & API
├── config.py                 # ⭐ ALL YOUR CONTENT GOES HERE
├── generate_placeholders.py  # Run once to create placeholder images
├── requirements.txt
├── Procfile                  # For Heroku/Railway deployment
├── runtime.txt               # Python version
├── templates/
│   ├── base.html             # Shared layout, animations, styles
│   ├── index.html            # Welcome screen
│   ├── game.html             # All 6 game levels
│   ├── stats.html            # Relationship statistics
│   └── easter_egg.html       # Secret hidden page
└── static/
    ├── images/               # 📷 Put your photos here
    └── audio/                # 🎵 Put your music & recordings here
```

---

## ✏️ How to Customize

**Open `config.py`** and edit everything:

| Section | What to change |
|---|---|
| `RELATIONSHIP_START_DATE` | Your anniversary / first date |
| `PARTNER_NAME` / `YOUR_NAME` | Names shown in messages |
| `LEVEL1` | The romantic question and its answer |
| `LEVEL2` | Multiple-choice memory question |
| `LEVEL3_CARDS` | Three memory cards (titles, descriptions) |
| `LEVEL4` | Which heart (0–8) is the correct one |
| `LEVEL5` | The secret phrase to unscramble |
| `FINAL_LEVEL` | Love letter text |
| `FINAL_SURPRISE` | The final custom message |
| `EASTER_EGG` | Hidden page content |

---

## 📷 Adding Your Photos

Replace placeholder files in `static/images/`:

| Filename | Used in |
|---|---|
| `level1.jpg` | Level 1 reward |
| `memory1.jpg` | Memory card 1 |
| `memory2.jpg` | Memory card 2 |
| `memory3.jpg` | Memory card 3 |
| `slide1.jpg` – `slide5.jpg` | Final slideshow |
| `easter_egg.jpg` | Secret page |

**Tip:** Any common image format works (jpg, png, webp). Keep images under 2 MB for fast mobile loading.

---

## 🎵 Adding Audio

Place files in `static/audio/`:

| Filename | Used in |
|---|---|
| `music.mp3` | Background music (all pages) |
| `memory.mp3` | Voice recording in Level 2 |

---

## 🚀 Running Locally

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Create placeholder assets
python generate_placeholders.py

# 3. Run the app
python app.py
```

Open **http://localhost:5000** in your browser.

---

## ☁️ Deploying (so you can share a link)

### Option A — Railway (easiest, free tier available)

1. Create a free account at [railway.app](https://railway.app)
2. Click **New Project → Deploy from GitHub repo**
3. Push your project to GitHub first:
   ```bash
   git init && git add . && git commit -m "love game"
   git remote add origin https://github.com/YOUR_USERNAME/love-game.git
   git push -u origin main
   ```
4. Railway auto-detects Python/Flask and deploys
5. You get a URL like `https://love-game-production.up.railway.app`
6. Share that URL on WhatsApp! 💕

### Option B — Heroku

```bash
heroku create my-love-game
git push heroku main
heroku open
```

### Option C — Render (free tier)

1. Go to [render.com](https://render.com)
2. **New Web Service → Connect GitHub repo**
3. Build command: `pip install -r requirements.txt`
4. Start command: `gunicorn app:app`
5. Deploy and share the URL

### Option D — Run on your own VPS / server

```bash
pip install -r requirements.txt
gunicorn app:app -b 0.0.0.0:80 --workers 2
```

---

## 📱 Mobile Sharing Tips

Once deployed, share the link like any other URL:
- **WhatsApp**: Paste URL in chat → it shows a rich preview
- **Instagram Stories**: Use the link sticker
- **Messenger / Telegram**: Works as a clickable link

---

## 🎮 Game Features

| Feature | Details |
|---|---|
| 6 game levels | Question, MCQ, Gallery, Find the Heart, Puzzle, Slideshow |
| Final Surprise | Countdown timer + heart animation |
| Relationship Stats | `/stats` — days, hours, months together |
| Easter Egg | `/secret` — hidden bonus page |
| Progress saving | localStorage keeps progress across visits |
| Background music | Toggle button top-right |
| Animations | Floating hearts, confetti, fireworks, typewriter |
| Mobile-first | Works perfectly on any phone |

---

## 🔧 Technical Notes

- No database needed — everything is in `config.py`
- Progress is saved in the browser's localStorage
- Works offline for everything except fonts (Google Fonts CDN)
- Images gracefully fall back to SVG placeholders if not found

---

*Made with ❤️ — customize it and surprise the one you love.*
