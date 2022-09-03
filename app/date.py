import datetime as dt

# Timezone
JST = dt.timezone(dt.timedelta(hours=+9), 'JST')
now = dt.datetime.now(JST)

def get_fourweeks():
    today = dt.date.today()
    today_weekday = today.weekday()

    # 三週間前の日曜日は何日前か？
    # そこを基準に、直近四週間のデータをとる。
    threeweekago_sunday = 26 - today_weekday
    l = [
        str(today - dt.timedelta(days=threeweekago_sunday-(i * 7))) for i in range(4)
    ]
    return l

# 引数で指定したフォーマット通り本日のdatetimeを返す。
def get_today_datetime(fmt):
    return dt.datetime.strftime(now, fmt)

def get_yesterday_datetime(fmt):
    return dt.datetime.strftime((now - dt.timedelta(days=1)), fmt)