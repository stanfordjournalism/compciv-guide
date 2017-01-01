from os.path import expanduser
import json
import tweepy

MAX_TWEET_COUNT = 3600

def authenticate_client(credsfilename):
    cf = expanduser(credsfilename)
    creds = json.load(open(cf))
    auth = tweepy.OAuthHandler(consumer_key = creds['consumer_key'],
                               consumer_secret = creds['consumer_secret'])
    auth.set_access_token(creds['access_token'],
                          creds['access_token_secret'])
    client = tweepy.API(auth)
    return client


def fetch_user_timeline(client, screen_name, maxcount=MAX_TWEET_COUNT):
    tweets = []
    cursor = tweepy.Cursor(client.user_timeline,
                           id = screen_name,
                           trim_user = True,
                           exclude_replies = False,
                           include_rts = True)
    for tweet in cursor.items(maxcount):
        tweets.append(tweet._json)

    return tweets


