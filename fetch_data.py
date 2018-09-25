"""This file contains functions used by run.py. See run.py for a full description of their
purpose. This make's use of the library Tweepy, so you MUST have Tweepy installed in order
for it to work."""

import tweepy

"""The lines below contain authorization keys to access Twitter's APIs.
You MUST provide your own API keys for this to work.
Get them by applying for a Twitter Dev account and registering a new app."""
consumer_key = 'YOUR-CONSUMER-KEY-HERE'
consumer_secret = 'YOUR-CONSUMER-SECRET-HERE'
access_token = 'YOUR-ACCESS-TOKEN-HERE'
access_secret = 'YOUR-ACCESS-SECRET-HERE'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

# Empty lists to store all the tweets in:
tweets = []
filtered_tweets = []

# This function collects the specified user's tweets, filters them, and joins them into a single string:
def get_tweets(username):
	
	# Collect tweets:
	for status in tweepy.Cursor(api.user_timeline, screen_name = username, include_rts = False).items(3200):
		tweets.append(status.text.encode('UTF-8'))
	
	# Split tweets into individual words for filtering:
	for tweet in tweets:
		split = tweet.split()
	
		# Filter each word and remove anything not alphanumeric to avoid errors:
		for word in split:
			if word.isalpha() == True:
				filtered_tweets.append(word)		
	
	# Finally, join all tweets into one long string and return this string:
	all_tweets = " ".join(filtered_tweets)
	return all_tweets

# This function collects tweets from a search, filters them, and joins them into a single string: 
def get_search(search):
	
	# Collect tweets:
	for status in tweepy.Cursor(api.search, q = search).items(3200):
		tweets.append(status.text.encode('UTF-8'))
	
	# Split tweets into individual words for filtering:
	for tweet in tweets:
		split = tweet.split()
	
		# Filter each word and remove anything not alphanumeric to avoid errors:
		for word in split:
			if word.isalpha() == True:
				filtered_tweets.append(word)			
	
	# Finally, join all tweets into one long string and return this string:
	all_tweets = " ".join(filtered_tweets)
	return all_tweets