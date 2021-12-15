#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 17:33:12 2021

@author: shenjingyi
"""

import tweepy
from textblob import TextBlob
#from wordcloud import WordCloud
import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt
import sys
plt.style.use('fivethirtyeight')

auth = tweepy.OAuthHandler('jMCXJ1l7bdMmVGF87kn8iBNZ7', 'cwyMm17J0wtW3MubNiUfHeWZj2o0QkapDdfqPw52bDkckGDzPJ')
auth.set_access_token('1440733712258195460-bnsoQHsEAT8Ul8v97mKgNoIt61AHus', 'AUSOLPr074Q1f4oC8DHjI0l6xjVECQkWFwCoPu564GDvD')

api = tweepy.API(auth, wait_on_rate_limit=True)
def work(number):
    if (number==number.isdigit()):
        public_tweets = api.user_timeline(screen_name = "Michigan State Basketball", count = 50, lang = "en", mode = "extended ")
        print("show the 5 recent tweets: \n")
        for tweet in public_tweets[0:number]:
            print(tweet.text, '\n')
            
            df = pd.DataFrame([tweet.text for tweet in public_tweets], columns=["tweets"])
            df.head()
        else:
            print("Error language")
    else:
        print("Error num")

if __name__ == '__main__': 
  number = 'i'
  #term = sys.argv[1]
  #language = "123"
  work(number)