****************************
Gathering Tweets with Tweepy
****************************



Simple version
==============



.. code-block:: python

    in [2]: import json

    In [3]: from fetch_user_tweets_simple import authenticate_client, fetch_user_timeline

    In [4]: client = authenticate_client('mycreds-twitter.json')

    In [5]: tweets = fetch_user_timeline(client, 'realdonaldtrump')

    In [6]: len(tweets)
    Out[6]: 3225

    In [7]: destfile = open("realdonaldtrump-tweets.json", "w")

    In [8]: json.dump(tweets, destfile, indent=2)

    In [9]: destfile.close()



