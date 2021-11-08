# retrieving-tweets
for this code, it can search all the twitters about the screen_name
I download tweepy but I don't kown why I cannot use tweepy module in python, I can just put the code in here.
This program is reference from stackoverflow, retrieving tweepy. It can retieve tweets from BBC twitter account with the twitter API.
Reference code from Twitter API


User story:
1:search specific twitters which contains specific name.
2:Get the users timeline for the twitters.

import tweepy
import json

consumer_key = 'xxxxxxxxx'
consumer_secret = 'xxxxxxxx'
access_token = 'xxxxxxx'
access_token_secret = 'xxxxxxxx'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

screen_name = "BBC"

data = []

for tweets in tweepy.Cursor(api.user_timeline, screen_name = screen_name).pages():
    for tweet in tweets:
        print(tweet.text)
        data.append(tweet._json)
        
filename = screen_name + "_tweets.json"  
with open(filename, "w") as outfile:
    json.dump(data, outfile)
