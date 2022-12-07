# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 11:46:50 2022

@author: Utilisateur
"""

import pandas as pd
import tweepy
from tweepy import OAuth1UserHandler, API
from textblob import TextBlob
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from wordcloud import STOPWORDS

print(type(STOPWORDS))
tweets=pd.DataFrame()


consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

auth = OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
api = API(auth)

KEYWORDS = "BTC"

# Basic keyword search
tweets = api.search_tweets(KEYWORDS,count=10000, tweet_mode="extended", lang="en",result_type="resent")
print("Total:", len(tweets))
"""
for i in tweets:
    print(i.full_text)
    print("-" * 15)
"""

all_tweets = []
all_tweets.extend(tweets)
oldest_id = tweets[-1].id

outtweets = [[tweet.id_str, 
              tweet.created_at, 
              tweet.favorite_count, 
              tweet.retweet_count, 
              tweet.full_text.encode("utf-8").decode("utf-8")] 
             for idx,tweet in enumerate(all_tweets)]
tweets=pd.DataFrame(outtweets,columns=["id","created_at","favorite_count","retweet_count","text"])

tweets=tweets.drop(["id","created_at","favorite_count","retweet_count"],axis=1)
tweets.head(3)


tweets["ressenti"]=tweets["text"]

for i in tweets.index:
    tweets["ressenti"][i]=TextBlob(tweets["ressenti"][i])
    tweets["ressenti"][i]= tweets["ressenti"][i].sentiment.polarity


tweets.to_csv('%s_tweets.csv' % KEYWORDS,index=False)

print("Ressenti des tweets sur les topics {}".format(KEYWORDS),tweets['ressenti'].mean())

















