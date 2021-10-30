#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 21:11:45 2021

@author: shenjingyi
"""
#This can get the users' timeline

import twitter

def oauth_login():
    CONSUMER_KEY = ''
    CONSUMER_SECRET = ''
    OAUTH_TOKEN = '' 
    OAUTH_TOKEN_SECRET = ''
    # Creating the authentification
    auth = twitter.oauth.OAuth( OAUTH_TOKEN,
                                OAUTH_TOKEN_SECRET,
                                CONSUMER_KEY,
                                CONSUMER_SECRET )

    twitter_api = twitter.Twitter(auth=auth)
    return twitter_api


twitter_api = oauth_login()

statuses = twitter_api.statuses.user_timeline(screen_name='SpongeBob')

print ([status['text'] for status in statuses])