# tweepy-bots/bots/followfollowers.py

import tweepy
import logging 
from config import create_api
import time
import json

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def follow_followers(api):
	
	logger.info("Retrieving and following followers")
	for follower in tweepy.Cursor(api.followers).items():
		
		#print(follower._json)
		my_json_string = json.dumps(follower._json)
		dict = json.loads(my_json_string)

		if  not dict["following"]:
			logger.info(f"Following {follower.name}")
			follower.follow()

def main():
	api = create_api()

	while True:
		follow_followers(api)
		logger.info("Waiting...")
		time.sleep(60)
	
	### Uncomment this and comment the upper infinite loop to test the followfollowers() 
	#follow_followers(api)

if __name__ == '__main__':
	main()	


