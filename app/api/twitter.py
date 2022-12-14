import tweepy
import csv
import sys
import os
from dotenv import load_dotenv
from transformers import pipeline 
from transformers import AutoModelForSequenceClassification 
from transformers import BertJapaneseTokenizer 
sys.path.append(os.path.abspath(".."))
from date import get_today_datetime, get_yesterday_datetime

load_dotenv()
TWITTER_API_KEY = os.getenv("TWITTER_API_KEY")
TWITTER_API_SECRET = os.getenv("TWITTER_API_SECRET")
TWITTER_BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")
TWITTER_ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
TWITTER_ACCESS_SECRET = os.getenv("TWITTER_ACCESS_SECRET")

client = tweepy.Client(bearer_token=TWITTER_BEARER_TOKEN,
                        consumer_key=TWITTER_API_KEY,
                        consumer_secret=TWITTER_API_SECRET,
                        access_token=TWITTER_ACCESS_TOKEN,
                        access_token_secret=TWITTER_ACCESS_SECRET
                    )

model = AutoModelForSequenceClassification.from_pretrained('daigo/bert-base-japanese-sentiment') 
tokenizer = BertJapaneseTokenizer.from_pretrained('cl-tohoku/bert-base-japanese-whole-word-masking') 
nlp = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)


count=10
results=[]
# 自分のアカウント情報を取得
user = client.get_me()

fmt = "%Y-%m-%dT00:00:00Z"
today = get_today_datetime(fmt)
yesterday = get_yesterday_datetime(fmt)

tweets = client.get_users_tweets(id = user.data.id, 
                                max_results = count,
                                exclude=("replies"),
                                start_time=yesterday,
                                end_time=today
                                )
tweets_data = tweets.data

# pandasで処理する用の配列を用意

score_list = []
tweet_list = []
label_list = []
if tweets_data != None:
    for tweet in tweets_data:
        em = nlp(tweet.text)
        score_list.append(em[0]["score"])
        label_list.append(em[0]["label"])
        tweet_list.append(tweet.text)


def get_tweet_data():
    data = {
        'Tweet': tweet_list,
        'Score': score_list,
        'Label': label_list
    }
    return data

