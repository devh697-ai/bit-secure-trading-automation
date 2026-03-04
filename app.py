import os
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)   # 🔥 Ye line bahut important hai

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")


@app.route("/")
def home():
    return "Bit Secure Trading Automation is Live 🚀"


@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json

    message = f"""
📢 SIGNAL ALERT

Symbol: {data.get('symbol')}
Side: {data.get('side')}
Price: {data.get('price')}
Timeframe: {data.get('timeframe')}
"""

    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"

    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message
    }

    requests.post(url, json=payload)

    return jsonify({"status": "success"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
