import requests
import subprocess
import json

# ===== 固定設定 =====
WEBHOOK_URL = "https://discordapp.com/api/webhooks/1422806115460317264/Hmn-ei74I5bNT25z_7mr3AqaXlqvMqVtQpT6NDFvR5OMCnFkbhaONEysLNgk6CVw44lx"
TWITTER_USER = "WOS_Japan"
KEYWORDS = ["ギフトコード", "🎁"]

def get_latest_tweet(user):
    """snscrapeで最新ツイートを取得"""
    try:
        result = subprocess.run(
            ["snscrape", "--jsonl", "--max-results", "1", f"twitter-user:{user}"],
            capture_output=True,
            text=True,
            check=True
        )
        tweet_data = json.loads(result.stdout.splitlines()[0])
        return tweet_data
    except Exception as e:
        print("❌ ツイート取得エラー:", e)
        return None

def contains_keywords(text):
    """キーワードが含まれているかチェック"""
    for kw in KEYWORDS:
        if kw in text:
            return True
    return False

def send_to_discord(content):
    """Discord Webhookに送信"""
    data = {"content": content}
    response = requests.post(WEBHOOK_URL, json=data)
    if response.status_code == 204:
        print("✅ Discord送信成功")
    else:
        print("❌ Discord送信失敗:", response.text)

def main():
    tweet = get_latest_tweet(TWITTER_USER)
    if not tweet:
        return
    text = tweet.get("content", "")
    url = tweet.get("url", "")

    if contains_keywords(text):
        message = f"📢 新しいツイート発見！\n{text}\n{url}"
        send_to_discord(message)
    else:
        print("⚠️ キーワードなし → スキップ")

if __name__ == "__main__":
    main()