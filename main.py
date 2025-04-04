import tweepy
import os
from dotenv import load_dotenv
import json
import requests

load_dotenv()


# from X API v2
api_key = os.getenv("API_KEY")
api_secret = os.getenv("API_SECRET")
bearer_token = os.getenv("BEARER_TOKEN")
access_token = os.getenv("ACCESS_TOKEN")
access_secret = os.getenv("ACCESS_TOKEN_SECRET")

# X APIv2 uses client in place of API
client_token = tweepy.Client(bearer_token)

# query = "from:amymrowell -is:retweet"
stored_tweets = "tweets.txt"
# tweets = client.search_recent_tweets(
#  query=query,
#  tweet_fields=["context_annotations", "created_at"],
#  user_fields=["profile_image_url"],
# expansions="author_id",
#  max_results=10,
# )


post_client = tweepy.Client(
    consumer_key=api_key,
    consumer_secret=api_secret,
    access_token=access_token,
    access_token_secret=access_secret,
)
# api = tweepy.API(auth)

# public_tweets = api.home_timeline()
# users = {u["id"]: u for u in tweets.includes["users"]}
# with open(stored_tweets, "a+") as filehandle:
# for tweet in tweets.data:
# if users[tweet.author_id]:
# user = users[tweet.author_id]
# print(user.profile_image_url)
# print(tweet.text)
# if len(tweet.context_annotations) > 0:
# print(tweet.context_annotations)
# filehandle.write("%s\n" % tweet.data)

# Get users list from the includes object
# users = {u["id"]: u for u in tweets.includes["users"]}

# for tweet in tweets.data:
# if users[tweet.author_id]:
# user = users[tweet.author_id]
# print(user.profile_image_url)

# Replace Tweet ID
# id = "1908126748900016530"

# users = client.get_retweeters(id=id, user_fields=["profile_image_url"])

# for user in users.data:
# print(user)

# Replace User ID
# id = "2244994945"

# tweets = client.get_liked_tweets(
# id=id, tweet_fields=["context_annotations", "created_at", "geo"]
# )

# for tweet in tweets.data:
# print(tweet)

# Replace the text with whatever you want to Tweet about
# response = post_client.create_tweet(text="Playing around with dev api.")


# print(response)
