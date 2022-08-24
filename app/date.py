import datetime as dt

today = dt.date.today()
today_weekday = today.weekday()

# 三週間前の日曜日は何日前か？
# そこを基準に、直近四週間のデータをとる。
threeweekago_sunday = 26 - today_weekday

def get_fourweeks():
    l = [
        str(today - dt.timedelta(days=threeweekago_sunday-(i * 7))) for i in range(4)
    ]
    return l

print(get_fourweeks())