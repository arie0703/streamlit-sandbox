import requests
import json
import os
from dotenv import load_dotenv
import datetime as dt

load_dotenv()
API_ENDPOINT = "https://qiita.com/api/v2/authenticated_user/items"
TOKEN = os.getenv("QIITA_TOKEN")

headers = {"Authorization": f"Bearer {TOKEN}"}
r = requests.get(API_ENDPOINT, headers=headers)
data = r.json()

today = dt.date.today()
today_weekday = today.weekday()

# 三週間前の日曜日は何日前か？
# そこを基準に、直近四週間のデータをとる。
threeweekago_sunday = 26 - today_weekday

# 直近四週間のlist 1週目から4週目（今週）のリストが作成される
fourweek_matrix = [[] for _ in range(4)]

def get_qiita():
    for d in data:
        dtime = dt.datetime.strptime(d["created_at"][:10], "%Y-%m-%d")
        created_at = dt.date(dtime.year, dtime.month, dtime.day)

        # 今日の日付と投稿日の差分
        diff = (today - created_at).days
        if diff > threeweekago_sunday:
            break
        elif diff > threeweekago_sunday - 7:
            fourweek_matrix[0].append(d["title"])
        elif diff > threeweekago_sunday - 14:
            fourweek_matrix[1].append(d["title"])
        elif diff > threeweekago_sunday - 21:
            fourweek_matrix[2].append(d["title"])
        else:
            fourweek_matrix[3].append(d["title"])

    return fourweek_matrix