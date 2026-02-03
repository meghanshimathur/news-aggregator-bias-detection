import os
import requests
from flask import Flask, render_template, redirect, url_for
from dotenv import load_dotenv

# --------------------------------------------------
# ENV SETUP
# --------------------------------------------------
load_dotenv()
GUARDIAN_API_KEY = os.getenv("GUARDIAN_API_KEY")

# --------------------------------------------------
# FLASK APP
# --------------------------------------------------
app = Flask(__name__)

# --------------------------------------------------
# PIPELINE (STABLE MOCK AI)
# --------------------------------------------------
def run_pipeline():
    articles = []

    response = requests.get(
        "https://content.guardianapis.com/search",
        params={
            "api-key": GUARDIAN_API_KEY,
            "q": "politics OR technology OR world",
            "show-fields": "trailText",
            "page-size": 5,
            "order-by": "newest"
        },
        timeout=10
    )

    results = response.json()["response"]["results"]

    for item in results:
        text = item["fields"]["trailText"]

        # ---- Simulated AI Summary ----
        summary = text[:120] + "..." if len(text) > 120 else text

        # ---- Simulated Bias Detection ----
        if "government" in text.lower() or "policy" in text.lower():
            bias = "Right Bias"
            confidence = 0.63
        else:
            bias = "Neutral"
            confidence = 0.52

        articles.append({
            "title": item["webTitle"],
            "summary": summary,
            "bias": bias,
            "confidence": confidence
        })

    return articles

# --------------------------------------------------
# ROUTES
# --------------------------------------------------
@app.route("/")
def home():
    return redirect(url_for("run"))

@app.route("/run")
def run():
    articles = run_pipeline()
    return render_template("index.html", articles=articles)

# --------------------------------------------------
# RUN SERVER
# --------------------------------------------------
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5001, debug=False)
