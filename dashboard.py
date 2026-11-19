from flask import Flask, Response
from collections import deque

app = Flask(__name__)

@app.get("/")
def home():
    try:
        with open("checks.log", "r", encoding="utf-8") as log_file:
            recent_lines = deque(log_file, maxlen=20)

    except FileNotFoundError:
        return Response(
            "No checks recorded yet.",
            mimetype="text/plain"
        )

    content = "SiteWatch - Latest 20 checks\n\n"
    content += "".join(recent_lines)

    return Response(content, mimetype="text/plain")