#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 23:48:33 2021

@author: shenjingyi
"""
import tweepy
import pandas as pd
from TwitterAPI import TwitterAPI
from TwitterAPI import TwitterPager    
def timeline():
    auth = tweepy.OAuthHandler('jMCXJ1l7bdMmVGF87kn8iBNZ7', 'cwyMm17J0wtW3MubNiUfHeWZj2o0QkapDdfqPw52bDkckGDzPJ')
    auth.set_access_token('1440733712258195460-bnsoQHsEAT8Ul8v97mKgNoIt61AHus', 'AUSOLPr074Q1f4oC8DHjI0l6xjVECQkWFwCoPu564GDvD')
    
    api = tweepy.API(auth)
    
    public_tweets = api.home_timeline()
    for tweet in public_tweets:
        print(tweet.text)
    

 
 
def search_tweets(the_consumer_key, the_consumer_secret, the_access_token_key,
                  the_access_token_secret, the_proxy_url):
    
    api = TwitterAPI(consumer_key=the_consumer_key,
                     consumer_secret=the_consumer_secret,
                     access_token_key=the_access_token_key,
                     access_token_secret=the_access_token_secret,
                     proxy_url=the_proxy_url)
    r = TwitterPager(api, 'search/tweets', {'q': 'MSU', 'count': 10})
    for item in r.get_iterator():
        if 'text' in item:
            print(item['text'])
        elif 'message' in item and item['code'] == 88:
            print ('SUSPEND, RATE LIMIT EXCEEDED: %s\n' % item['message'])
            break
         
 



def test_twitterAPI():
    a = timeline()
    b = search_tweets()
    while True:
        assert a.timeline(screen_name='MSU')=='MSU'
        assert b.search_tweet('xxxxx') == 'xxxxx'
    
    
    
    
    
    
if __name__ == "__main__":
    consumerKey = "jMCXJ1l7bdMmVGF87kn8iBNZ7"  # your key and secrete
    consumerSecret = "cwyMm17J0wtW3MubNiUfHeWZj2o0QkapDdfqPw52bDkckGDzPJ"
    accessToken = "1440733712258195460-bnsoQHsEAT8Ul8v97mKgNoIt61AHus"
    accessTokenSecret = "AUSOLPr074Q1f4oC8DHjI0l6xjVECQkWFwCoPu564GDvD"
    proxyUrl = ""  
    
    search_tweets(the_consumer_key=consumerKey,
                  the_consumer_secret=consumerSecret,
                  the_access_token_key=accessToken,
                  the_access_token_secret=accessTokenSecret,
                  the_proxy_url=proxyUrl)    
    
