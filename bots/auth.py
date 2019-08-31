import tweepy

sample_acc_tok = "sact"
sample_acc_tok_sec = "sacts"
sample_aut = "sat"
sample_auts = "sats"

def main():
	'''Here we do the Authentication of the app by testng the credentials of the app'''

	# Authenticate to Twitter
	auth = tweepy.OAuthHandler(sample_acc_tok,sample_acc_tok_sec)
	auth.set_access_token(sample_aut,sample_auts)

	api = tweepy.API(auth)

	try:
		api.verify_credentials()
		print("Authentication OK")

	except:
		print("Error during authentication")	

if __name__=='__main__':
	main()	