#!/usr/bin/python
from twitter import *
config = {}
execfile("config.py", config)

twitter = Twitter(auth = OAuth(config["access_key"], config["access_secret"], config["consumer_key"], config["consumer_secret"]))


#-----------------------------------------------------------------------
# perform a basic search 
# Twitter API docs:
# https://dev.twitter.com/rest/reference/get/search/tweets
#-----------------------------------------------------------------------

def hashy(searchy):
	query = twitter.search.tweets(q = searchy)
	hashlist = []
	for result in query["statuses"]:
		#hashlet = "(%s) @%s %s \n" % (result["created_at"], result["user"]["screen_name"], result["text"])
		hashlet = "@%s %s \n" % (result["user"]["screen_name"], result["text"])
		hashlist.append(hashlet)
	return hashlist
