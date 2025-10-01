import os
import requests
import subprocess

===== 設定 =====,
WEBHOOK_URL = "https://discordapp.com/api/webhooks/1422806115460317264/Hmn-ei74I5bNT25z_7mr3AqaXlqvMqVtQpT6NDFvR5OMCnFkbhaONEysLNgk6CVw44lx"
TWITTER_USER = "WOS_Japan"   # 転送元アカウント
KEYWORDS = ["ギフトコード", ""]   # 転送するキーワード
=================,
def get_latest_tweet(user):
    """snscrape で最新ツイートを取得"""
    try:
        result = subprocess.run(
            ["snscrape", "--jsonl", "--max-results", "1", f"twitter-user:{user}"],
            capture_output=True,
            text=True
        )
        if result.returncode != 0 or not result.stdout.strip():
            return None

        import json
        tweet = json.loads(result.stdout.splitlines()[0])
        return tweet["content"]
    except Exception as e:
        print(" ツイート取得エラー:", e)
        return None

def contains_keywords(text):
    """キーワードが含まれているかチェック"""
    for kw in KEYWORDS:
        if kw in text:
            return True
    return False

def send_to_discord(message):
    """Discord Webhook に送信"""
    data = {"content": message}
    response = requests.post(WEBHOOK_URL, json=data)
    if response.status_code == 204:
        print(" Discord送信成功")
    else:
        print(" Discord送信失敗:", response.text)

def main():
    tweet = get_latest_tweet(TWITTER_USER)
    if tweet and contains_keywords(tweet):
        message = f" 新しいツイート\n{tweet}"
        send_to_discord(message)
    else:
        print(" キーワードなし → スキップ")

if name == "main":
    main()
