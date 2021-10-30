#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 18:21:16 2021

@author: shenjingyi
"""

from TwitterAPI import TwitterAPI
from TwitterAPI import TwitterPager
 
 
def search_tweets(the_consumer_key, the_consumer_secret, the_access_token_key,
                  the_access_token_secret, the_proxy_url):
    
    api = TwitterAPI(consumer_key=the_consumer_key,
                     consumer_secret=the_consumer_secret,
                     access_token_key=the_access_token_key,
                     access_token_secret=the_access_token_secret,
                     proxy_url=the_proxy_url)
    r = TwitterPager(api, 'search/tweets', {'q': 'xxxxx', 'count': 10})
    for item in r.get_iterator():
        if 'text' in item:
            print(item['text'])
        elif 'message' in item and item['code'] == 88:
            print ('SUSPEND, RATE LIMIT EXCEEDED: %s\n' % item['message'])
            break
         
 
if __name__ == "__main__":
    consumerKey = ""  # your key and secrete
    consumerSecret = ""
    accessToken = ""
    accessTokenSecret = ""
    proxyUrl = ""  
    
    search_tweets(the_consumer_key=consumerKey,
                  the_consumer_secret=consumerSecret,
                  the_access_token_key=accessToken,
                  the_access_token_secret=accessTokenSecret,
                  the_proxy_url=proxyUrl)