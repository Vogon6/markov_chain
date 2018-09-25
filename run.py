"""This script will let the user choose whether they'd like to enter a search term or a
specific Twitter user, then will collect 3200 tweets from the specified search term or
user. The collected tweets are then fed into Codecademy's Markov Chain function, and
a new tweet 20 words long is generated from them. Due to Twitter's API rate limits you can
only make 15 calls every 15 minutes. If you exceed this rate limit it will throw an error
with error code 429. If this happens simply wait 15 minutes and it should work again."""

"""You MUST have the library Tweepy installed to make this work, and you MUST enter valid
Twitter API authorization keys into fetch_data.py. Apply for a Twitter dev account and
register a new app to get authorization keys. See fetch_data.py for where to enter them."""

import fetch_data
from markov_python.cc_markov import MarkovChain
from time import sleep

# This function will let a user choose what they want to do and checks that they've made a valid choice:
def get_user_choice():
	user_choice = raw_input('Please choose "user" or "search": ').lower()
	if user_choice != "user":
		if user_choice != "search":
			print "Invalid input. Try again."
			get_user_choice()
	else:
		return user_choice

# This function will allow a user to enter a Twitter username and will prompt them to try again if the username is not valid (throws an error):
def twitter_user():
	try:
		username = raw_input("Enter a Twitter handle with public tweets: ")
		tweets = fetch_data.get_tweets(username)
		return tweets
	except:
		print "Invalid Twitter handle entered or no public tweets available. Try again."
		twitter_user()

# Initialize the program by explaining what it does and offer the user a choice:
print
print "This script will generate a new tweet 20 words long based on any user's public tweets or any search term."
sleep(2)
user_choice = get_user_choice()

# Retrieve tweets based on the user's input. This calls functions from the file fetch_data.py:
sleep(1)
if user_choice == "user":
	tweets = twitter_user()
else:
	search = raw_input("Enter a term or hashtag to search: ")
	tweets = fetch_data.get_search(search)


# Create a new tweet using Codecademy's Markov Chain functions:
mc = MarkovChain()
mc.add_string(tweets)
new_tweet = mc.generate_text()

# Print the new tweet:
print
print "Here is your new tweet!"
print " ".join(new_tweet)