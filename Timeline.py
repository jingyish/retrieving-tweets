#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 21:11:45 2021

@author: shenjingyi
"""
#This can get the users' timeline

import tweepy


auth = tweepy.OAuthHandler('xxxxxxx', 'xxxxxx')
auth.set_access_token('xxxxxxxx', 'xxxxxxxx')

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)
