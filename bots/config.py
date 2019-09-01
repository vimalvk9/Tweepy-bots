# All the bots built have certain common functionality.
# This module has all the code dealing with functions which are common to all
#
# It contains:
# 				1. Authentication with Twitter API
#			    2. Creating Twitter API object


# tweepy-bots/bots/config.py

# Sample API object structure
# {
#   'auth': <tweepy.auth.OAuthHandlerobjectat0x7fe0c9b0acf8>,
#   'host': 'api.twitter.com',
#   'search_host': 'search.twitter.com',
#   'upload_host': 'upload.twitter.com',
#   'api_root': '/1.1',
#   'search_root': '',
#   'upload_root': '/1.1',
#   'cache': None,
#   'compression': False,
#   'retry_count': 0,
#   'retry_delay': 0,
#   'retry_errors': None,
#   'timeout': 60,
#   'wait_on_rate_limit': True,
#   'wait_on_rate_limit_notify': True,
#   'parser': <tweepy.parsers.ModelParserobjectat0x7fe0c6164d30>,
#   'proxy': {
    
#   },
#   'cached_result': False,
#   'last_response': <Response[
#     200
#   ]
# }

import tweepy
import logging
import os

logger = logging.getLogger()

def create_api():
	
	consumer_key = os.getenv("CONSUMER_KEY")
	consumer_secret = os.getenv("CONSUMER_SECRET")	
	access_token = os.getenv("ACCESS_TOKEN")
	access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

	auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
	auth.set_access_token(access_token,access_token_secret)
	api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

	try:	
		api.verify_credentials()
	
	except Exception as e:
		logger.error("Error creating API",exc_info=True)
		raise e

	logger.info("API created")
	return api		
