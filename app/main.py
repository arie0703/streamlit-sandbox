import streamlit as st
from api.spreadsheet import get_satisfaction, get_label
import numpy as np
import pandas as pd
from date import get_fourweeks
from api.qiita import get_qiita
from api.twitter import get_tweet_data

st.title("Dash Board")


satisfaction = get_satisfaction()
labels = get_label()
chart_data = pd.DataFrame(
    satisfaction,
    index=labels,
    columns=['満足度']
)
st.line_chart(chart_data)

st.text("直近4週間のアウトプット")

matrix = []
qiita_list = get_qiita()
four_weeks = get_fourweeks()
for q in qiita_list:
    matrix.append(len(q))

print(four_weeks, matrix)
bar_data = pd.DataFrame(
    matrix,
    columns=["Qiita",],
    index=four_weeks
)

st.bar_chart(bar_data)

@st.cache
def twitter_analysis():
    data = get_tweet_data()
    return data


st.text("ツイート分析")

data = twitter_analysis()
avg = sum(data["Score"]) / len(data["Score"])
st.dataframe(pd.DataFrame(data), width=1000)
st.subheader('平均スコア')
st.metric(label='平均', value=avg)
