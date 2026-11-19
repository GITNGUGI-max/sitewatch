from flask import Flask, render_template
from collections import deque

app = Flask(__name__)

@app.get("/")
def home():
    try:
        with open("checks.log", "r", encoding="utf-8") as log_file:
            recent_lines = deque(log_file, maxlen=20)
    except FileNotFoundError:
        recent_lines = []

    checks = []

    for line in reversed(recent_lines):
        parts = line.strip().split(" | ", 3)

        if len(parts) != 4:
            continue

        timestamp, url, status, duration = parts

        checks.append({
            "timestamp": timestamp,
            "url": url,
            "status": status,
            "duration": duration,
        })

    return render_template("index.html", checks=checks)