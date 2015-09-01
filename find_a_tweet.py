#!/usr/bin/env python

import os
import json
import codecs
import sys

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler, Stream, API

from haiku import Haiku


class HaikuListener(StreamListener):

    def on_data(self, data):
        tweet = json.loads(data)

        try:
            haiku = Haiku(tweet['text'])
            if haiku.is_valid():
                retweet = self._retweet_string(tweet, haiku)
                twitter.update_status(status=retweet)
                print retweet
                stream.disconnect()
        except Exception as e:
            print e

    def _retweet_string(self, tweet, haiku):
        return haiku.formatted() + "\n#accidentalhaiku by @{}".format(tweet['user']['screen_name'])


access_token = os.environ['TWITTER_ACCESS_TOKEN']
access_token_secret = os.environ['TWITTER_ACCESS_TOKEN_SECRET']
consumer_key = os.environ['TWITTER_CONSUMER_KEY']
consumer_secret = os.environ['TWITTER_CONSUMER_SECRET']

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
stream = Stream(auth, HaikuListener())
twitter = API(auth)


if __name__ == '__main__':
    stream.sample(languages=["en"])
