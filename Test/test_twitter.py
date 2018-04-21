from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream

f = open('test_hashtags.txt','a')

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
        L = tweet['entities']['hashtags']
        for ht in L:
			i = ht['text']
            if (re.search(r'[а-яА-Я]', i) and not (re.search(r'[a-zA-Z]', i))):
                if (len(re.findall('_', i)) > 0 and len(re.findall(r'[А-Я]', i))>1):
                    L =  [x for x in i.split('_') if len(x) > 12]
                    if (len(L)) == 0:
                        split_ht.append(i)
                if (len(re.findall(r'[А-Я]', i)) > 1 and len(re.findall(r'[а-я]', i)) < 25 and len(re.findall(r'[а-я]', i)) > 8): 
                    split_ht.append(i)
        if len(split_ht) == tweet_count:
             break 
    except KeyError:
        continue
       
for x in split_ht:
	f.write(x + '\n')
	
f.close()
