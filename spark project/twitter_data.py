__author__ = 'Sulav'

# -*- coding: utf-8 -*-

import tweepy
from tweepy import OAuthHandler

# for streaming data
from tweepy.streaming import StreamListener

import json

import logging

logging.basicConfig(filename='logfile.log',level=logging.DEBUG)
# Twitter Credentials

'''consumer_key = 'bIZgEbNKmgoOEDxheHXS0k6O5'
consumer_secret = 'sqahGfUd11OPMVbihn6LdcB0gccVVwi6CtJby6Ne27LwUTwg3a'
access_token = '327797166-Z5ul856pCScP0UNClnKyvOapLGte6oLBN0ayuh7b'
access_secret = 'AJ8nnTYV9W8hYgYbtqORj8yBruPswHzMNPRZtghfWfMSL' '''



#to auntheticate and stream data
def initialize():
    consumer_key = 'tGgiMdJ7ua3xgHu0I0Gdxbh90'
    consumer_secret = 'fr9vneybOfO6b90Eevg5Hs8NWiQ0HOnF2eB5huVl5a4feVWmra'
    access_token = '400618597-Ui7TksvLKXN4HCI6FMs2D1OzkPjsZX5n8a80Wn10'
    access_secret = 'KsCmcjgR4oRdUYR08ud5w6JVgyAcFwKwyD1UroOp5pXF6'

    #Authentication
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    api = tweepy.API(auth)
    myStreamListener = MyStreamListener()
    myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
    #to extract all tweets worldwide
    myStream.filter(locations=[-180,-90,180,90])




#Overriding the Streamlistener class
class MyStreamListener(StreamListener):

    #for errors
    def on_error(self, status):
        print(status)
        logging.debug('Twitter Error Response Code %s',status)
        return True

    #for handling tweets
    def on_data(self, data):


        try:

                with open('twitter_data.json','ab') as f:
                    if 'limit' in data:
                        return True

                    else:
                        f.write(data)

                        return True
        except BaseException as e:
            print e
            logging.debug('Error %s',e)
            return True


if __name__ == '__main__':

    logging.debug('Process started')
    initialize()