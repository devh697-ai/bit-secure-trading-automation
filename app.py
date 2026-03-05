import os
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")


@app.route("/")
def home():
    return "Bit Secure Trading Automation is Live 🚀"


@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json

    symbol = data.get("symbol")
    side = data.get("side")
    price = data.get("price")
    timeframe = data.get("timeframe")

    # Market detection
    if symbol in ["BTCUSDT","ETHUSDT","SOLUSDT"]:
        market = "CRYPTO"
    elif symbol in ["NIFTY","BANKNIFTY","NIFTY50"]:
        market = "INDEX"
    else:
        market = "MARKET"

    # Professional Telegram message
    message = f"""
🚨 BIT SECURE TRADE SIGNAL

📊 Symbol : {symbol}
📈 Side : {side}
💰 Entry : {price}
⏱ Timeframe : {timeframe}

⚡ Strategy : HMA + UT Bot
🧠 Market : {market}

━━━━━━━━━━━━━━

⚠️ Trade at your own risk
📡 Powered by Bit Secure Algo
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
