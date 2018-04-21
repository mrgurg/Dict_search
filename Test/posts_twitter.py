from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream

f = open('train_text.txt','a')

import json

from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream
import re

ACCESS_TOKEN = 'ACCESS_TOKEN'
ACCESS_SECRET = 'ACCESS_SECRET'
CONSUMER_KEY = 'CONSUMER_KEY'
CONSUMER_SECRET = 'CONSUMER_SECRET'

oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

# Initiate the connection to Twitter Streaming API
twitter_stream = TwitterStream(auth=oauth)

# Get a sample of the public data following through Twitter
iterator = twitter_stream.statuses.sample()

tweet_count = 1500
split_ht = []
for tweet in iterator:
    try:
        i = tweet['text']
        if (re.search(r'[а-яА-Я]', i) and not (re.search(r'[a-zA-Z]', i))):
			f.write(i + '\n')
			tweet_count -= 1
	except KeyError:
		continue
	if tweet_count <= 0:
		break

f.close() 


                
