import os
import requests

# Discord Webhook URL（固定）
WEBHOOK_URL = "https://discordapp.com/api/webhooks/1422806115460317264/Hmn-ei74I5bNT25z_7mr3AqaXlqvMqVtQpT6NDFvR5OMCnFkbhaONEysLNgk6CVw44lx"

# 監視対象アカウントとキーワード
TWITTER_USER = "WOS_Japan"
KEYWORDS = ["ギフトコード", "🎁"]

def fetch_latest_tweet():
    """
    X(Twitter) API を使わずにスクレイピング代替
    → ここでは実際の取得部分はダミーで書く
    """
    # ★ 本番は snscrape を使うのでここはテスト用
    return "🎁 ギフトコード: TEST1234"

def contains_keywords(text):
    """ツイートにキーワードが含まれているか確認"""
    for kw in KEYWORDS:
        if kw in text:
            return True
    return False

def send_to_discord(message):
    """Discord Webhook に送信"""
    payload = {"content": message}
    response = requests.post(WEBHOOK_URL, json=payload)
    if response.status_code == 204:
        print("✅ Discord送信成功")
    else:
        print("❌ Discord送信失敗:", response.text)

def main():
    tweet = fetch_latest_tweet()
    if contains_keywords(tweet):
        message = f"🐦 新しいツイート: {tweet}"
        send_to_discord(message)
    else:
        print("⚠️ キーワードなし → スキップ")

if __name__ == "__main__":
    main()
