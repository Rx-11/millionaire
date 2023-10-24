import tweepy
import json
import time
import os

# Set up your Twitter API credentials
client_id = os.getenv("TWITTER_CLIENT_ID")
client_secret = os.getenv("TWITTER_CLIENT_SECRET")
consumer_key = os.getenv("TWITTER_CONSUMER_KEY")
consumer_secret = os.getenv("TWITTER_CONSUMER_SECRET")
access_token = os.getenv("TWITTER_ACCESS_TOKEN")
access_token_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

# Authenticate with Twitter
client = tweepy.Client(
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token=access_token,
    access_token_secret=access_token_secret,
)

# Load tweets from GitHub Secrets
json_content = os.getenv("TWEET_JSON")
print(json_content)
# tweets = json.loads(json_content).get("millionaire_mindset_tips", [])

# # Function to save the updated JSON content to GitHub Secrets
# def save_tweets_to_secrets(new_tweets):
#     data = {"millionaire_mindset_tips": new_tweets}
#     os.environ["TWEET_JSON"] = json.dumps(data)

# # Main loop to post tweets at regular intervals
# tweet = tweets[0]

# try:
#     client.create_tweet(text=tweet)
#     print(f"Tweeted: {tweet}")
#     tweets.remove(tweet)  # Remove the posted tweet
#     save_tweets_to_secrets(tweets)  # Update the JSON content in GitHub Secrets
# except Exception as e:
#     print(f"Error posting tweet: {e}")
