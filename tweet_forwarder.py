import os
import requests
from dotenv import load_dotenv
import snscrape.modules.twitter as sntwitter

load_dotenv()

WEBHOOK_URL = os.getenv("import os
import requests
from dotenv import load_dotenv
import snscrape.modules.twitter as sntwitter

load_dotenv()

WEBHOOK_URL = os.getenv("https://discordapp.com/api/webhooks/1422806115460317264/Hmn-ei74I5bNT25z_7mr3AqaXlqvMqVtQpT6NDFvR5OMCnFkbhaONEysLNgk6CVw44lx")  # Discord Webhook
TWITTER_USER = os.getenv("TWITTER_USER", "WOS_Japan")
KEYWORDS = os.getenv("KEYWORDS", "ギフトコード,ギフコ,無料").split(",")
LAST_ID_FILE = "last_sent_id.txt"

def read_last_id():
    if not os.path.exists(LAST_ID_FILE):
        return None
    with open(LAST_ID_FILE, "r", encoding="utf-8") as f:
        return f.read().strip() or None

def write_last_id(tweet_id):
    with open(LAST_ID_FILE, "w", encoding="utf-8") as f:
        f.write(str(tweet_id))

def contains_keyword(text):
    t = text.lower()
    for k in KEYWORDS:
        if k.strip() and k.lower().strip() in t:
            return True
    return False

def main():
    last_id = read_last_id()
    scraper = sntwitter.TwitterUserScraper(TWITTER_USER)

    latest_tweet = None
    for i, tweet in enumerate(scraper.get_items()):
        if i > 20:  # 直近20件だけチェック
            break
        if last_id and str(tweet.id) <= last_id:
            continue
        if contains_keyword(tweet.content):
            latest_tweet = tweet
            break

    if not latest_tweet:
        print("新しい該当ツイートなし")
        return

    tweet_url = f"https://twitter.com/{TWITTER_USER}/status/{latest_tweet.id}"
    payload = {
        "content": f"🎁 キーワード検出！\n{tweet_url}",
        "embeds": [{
            "title": f"新着ツイート by @{TWITTER_USER}",
            "description": latest_tweet.content[:500],
            "url": tweet_url
        }]
    }

    r = requests.post(WEBHOOK_URL, json=payload)
    if r.status_code == 204:
        print("送信成功:", tweet_url)
        write_last_id(str(latest_tweet.id))
    else:
        print("送信失敗:", r.status_code, r.text)

if __name__ == "__main__":
    main()
")  # Discord Webhook
TWITTER_USER = os.getenv("TWITTER_USER", "WOS_Japan")  # 監視するアカウント
KEYWORDS = os.getenv("KEYWORDS", "ギフトコード,ギフコ,無料").split(",")  # 検索キーワード
LAST_ID_FILE = "last_sent_id.txt"

def read_last_id():
    if not os.path.exists(LAST_ID_FILE):
        return None
    with open(LAST_ID_FILE, "r", encoding="utf-8") as f:
        return f.read().strip() or None

def write_last_id(tweet_id):
    with open(LAST_ID_FILE, "w", encoding="utf-8") as f:
        f.write(str(tweet_id))

def contains_keyword(text):
    t = text.lower()
    for k in KEYWORDS:
        if k.strip() and k.lower().strip() in t:
            return True
    return False

def main():
    last_id = read_last_id()
    scraper = sntwitter.TwitterUserScraper(TWITTER_USER)

    latest_tweet = None
    for i, tweet in enumerate(scraper.get_items()):
        if i > 20:  # 直近20件だけチェック
            break
        if last_id and str(tweet.id) <= last_id:
            continue
        if contains_keyword(tweet.content):
            latest_tweet = tweet
            break

    if not latest_tweet:
        print("新しい該当ツイートなし")
        return

    tweet_url = f"https://twitter.com/{TWITTER_USER}/status/{latest_tweet.id}"
    payload = {
        "content": f"🎁 キーワード検出！\n{tweet_url}",
        "embeds": [{
            "title": f"新着ツイート by @{TWITTER_USER}",
            "description": latest_tweet.content[:500],
            "url": tweet_url
        }]
    }

    r = requests.post(WEBHOOK_URL, json=payload)
    if r.status_code == 204:
        print("送信成功:", tweet_url)
        write_last_id(str(latest_tweet.id))
    else:
        print("送信失敗:", r.status_code, r.text)

if __name__ == "__main__":
    main()
