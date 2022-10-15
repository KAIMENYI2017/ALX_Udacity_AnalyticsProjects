# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 23:22:55 2022

@author: RONNY
"""
import pandas as pd
import tweepy
import time
import json
import numpy as np
tweet_ids = pd.read_csv("twitter-archive-enhanced.csv")
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

tweets=[]
for i in tweet_ids.tweet_id:
    try:
        status=api.get_status(i)
        tweets.append(status)
    except Exception as e:
        status= '' 
    time.sleep(1)

tweet_dict={'tweet_id':[], 'favorite_count':[], 'retweet_count':[]}
for tweet in tweets:
    tweet_dict['tweet_id'].append(tweet.id_str)
    tweet_dict['favorite_count'].append(tweet.favorite_count)
    tweet_dict['retweet_count'].append(tweet.retweet_count)

tweet_dt=pd.DataFrame(tweet_dict)
with open('tweets_data.csv', 'w') as f:
    f.write((tweet_dt.to_csv(index=False)))

tweet_dt.shape
'''
#this is what i did initially and got a text file.
result=[{'tweet_id':tweet.id_str, 'favorite_count':tweet.favorite_count, 'retweet_count':tweet.retweet_count} for tweet in tweets]
with open('tweets_json2.txt', 'w') as f:
    f.write(json.dumps(result, indent=2))
'''
