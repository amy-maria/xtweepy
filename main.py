import tweepy
import os
from dotenv import load_dotenv

load_dotenv()


# from X API v2
api_key = os.getenv("API_KEY")
api_secret = os.getenv("API_SECRET")
bearer_token = os.getenv("BEARER_TOKEN")
access_token = os.getenv("ACCESS_TOKEN")
access_secret = os.getenv("ACCESS_TOKEN_SECRET")

# X APIv2 uses client in place of API
client_token = tweepy.Client(bearer_token)

query = "from:googledevs -is:retweet"
stored_tweets = "tweets.txt"
tweets = client_token.search_recent_tweets(
    query=query,
    tweet_fields=["context_annotations", "created_at"],
    expansions="author_id",
    max_results=10,
)

post_client = tweepy.Client(
    consumer_key=api_key,
    consumer_secret=api_secret,
    access_token=access_token,
    access_token_secret=access_secret,
)


for tweet in tweets.data:
    print(tweet.text)
    if len(tweet.context_annotations) > 0:
        print(tweet.context_annotations)
