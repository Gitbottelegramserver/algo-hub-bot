import requests
import time

PING_URL = "https://algo-hub-bot.onrender.com"
PING_INTERVAL = 5 * 60  # каждые 5 минут

def ping_forever():
    while True:
        try:
            res = requests.get(PING_URL)
            print(f"[OK] Pinged {PING_URL} — Status {res.status_code}")
        except Exception as e:
            print(f"[ERR] Ping failed: {e}")
        time.sleep(PING_INTERVAL)

if __name__ == "__main__":
    ping_forever()
