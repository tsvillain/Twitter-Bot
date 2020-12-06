import tweepy
import time
from credentials import *

auth = tweepy.OAuthHandler(consumerAPIkey,consumerAPIsecret)
auth.set_access_token(accessToken, accessTokenSecret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

KEY = '#hackathon'

for tweet in tweepy.Cursor(api.search, q=KEY).items():
    try:
        print('Tweet by @'+ tweet.user.screen_name)
        tweet.favorite()
        tweet.retweet()
        print('Liked and Retweeted') 
        time.sleep(300)      

    except tweepy.TweepError as err:
        print(err.reason)

    except StopIteration:
        break