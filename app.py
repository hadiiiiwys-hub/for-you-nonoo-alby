"""
app.py — Flask backend for the Love Game
Serves all routes and injects config data into templates.
"""

from flask import Flask, render_template, jsonify, send_from_directory
import config, os

app = Flask(__name__)

# ── Helpers ──────────────────────────────────────────────
def cfg():
    """Return a flat dict of all config values for template injection."""
    return {
        "partner":          config.PARTNER_NAME,
        "yours":            config.YOUR_NAME,
        "start_date":       config.RELATIONSHIP_START_DATE,
        "welcome_title":    config.WELCOME_TITLE,
        "welcome_message":  config.WELCOME_MESSAGE,
        "level1":           config.LEVEL1,
        "level2":           config.LEVEL2,
        "level3_cards":     config.LEVEL3_CARDS,
        "level4":           config.LEVEL4,
        "level5":           config.LEVEL5,
        "final_level":      config.FINAL_LEVEL,
        "final_surprise":   config.FINAL_SURPRISE,
        "easter_egg":       config.EASTER_EGG,
        "love_letter": config.FINAL_LEVEL["love_letter"].format(
            partner=config.PARTNER_NAME,
            yours=config.YOUR_NAME,
        ),
    }

# ── Routes ───────────────────────────────────────────────
@app.route("/")
def index():
    return render_template("index.html", **cfg())

@app.route("/game")
def game():
    return render_template("game.html", **cfg())

@app.route("/stats")
def stats():
    return render_template("stats.html", **cfg())

@app.route("/secret")
def easter_egg():
    return render_template("easter_egg.html", **cfg())

# API endpoint — validate level 1 answer
@app.route("/api/check_answer", methods=["POST"])
def check_answer():
    from flask import request
    data   = request.get_json()
    answer = (data.get("answer") or "").strip().lower()
    correct = config.LEVEL1["answer"].lower()
    ok = correct in answer or answer in correct
    return jsonify({"correct": ok})

# Serve static placeholder images/audio if real files are missing
@app.route("/static/images/<path:filename>")
def serve_image(filename):
    img_path = os.path.join(app.static_folder, "images", filename)
    if os.path.exists(img_path):
        return send_from_directory(os.path.join(app.static_folder, "images"), filename)
    # Return SVG placeholder
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="400" height="300">
      <rect width="400" height="300" fill="#1a0a2e"/>
      <text x="50%" y="45%" text-anchor="middle" fill="#ff69b4" font-size="40">📷</text>
      <text x="50%" y="65%" text-anchor="middle" fill="#c084fc" font-size="16">{filename}</text>
    </svg>'''
    from flask import Response
    return Response(svg, mimetype="image/svg+xml")

if __name__ == "__main__":
    # In production use gunicorn; this is for local dev only
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
