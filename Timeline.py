#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 21:11:45 2021

@author: shenjingyi
"""
#This can get the users' timeline

import tweepy


auth = tweepy.OAuthHandler('jMCXJ1l7bdMmVGF87kn8iBNZ7', 'cwyMm17J0wtW3MubNiUfHeWZj2o0QkapDdfqPw52bDkckGDzPJ')
auth.set_access_token('1440733712258195460-bnsoQHsEAT8Ul8v97mKgNoIt61AHus', 'AUSOLPr074Q1f4oC8DHjI0l6xjVECQkWFwCoPu564GDvD')

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)
