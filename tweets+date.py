import os
import tweepy as tw
import pandas as pd
from tweepy import OAuth1UserHandler, API
from textblob import TextBlob
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from wordcloud import STOPWORDS
from datetime import date
from datetime import datetime, timedelta
import schedule
import time 
import datetime as dt

client = tw.Client(bearer_token='')

query = 'BTC -is:retweet lang:en'
tweets = tw.Paginator(client.search_recent_tweets, query=query,
                              tweet_fields=['context_annotations', 'created_at'], max_results=100).flatten(limit=10000)
tweets_copy=tweets
X=[]
publication_time=[] 
for tweet in tweets:
    shifted = tweet.id >> 22 
    timestamp = shifted + 1288834974657
    time_created = datetime.fromtimestamp(timestamp/1000).strftime('%Y-%m-%d')
    publication_time.append(time_created)
    X.append(tweet.text)
    


df=pd.DataFrame()
df['text']=X
df['date']=publication_time

name="tweets du " + str(df["date"][0])
df.to_csv(name)
