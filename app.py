from dotenv import load_dotenv
import os

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message
    }
    requests.post(url, json=payload)

@app.route("/")
def home():
    return "Bit Secure Trading Automation is Live 🚀"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json

    symbol = data.get("symbol", "UNKNOWN")
    side = data.get("side", "UNKNOWN")

    message = f"📈 Signal Received\nSymbol: {symbol}\nSide: {side}\nTime: {datetime.now()}"

    send_telegram_message(message)

    return jsonify({"status": "alert_sent"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
