import tweepy
import json
import time

# Set up your Twitter API credentials
client_id = "eEZPOGZQa1ktam82NlhWVW9kbkQ6MTpjaQ"
client_secret = "Mpe0IS-dzc94uMy2ai_FboYTMEFtyOacrbzzzBpo9rnzFUPBMI"
consumer_key = "pKP7JTSe41RMfBKcLaE2KCL9J"
consumer_secret = "SWkTaUaJSEVDjrPNzP6qVJkDNnv0BfBKJor92tZIRqhZ43XGUa"
access_token = "1715849789957406720-sWSZpkpQX5L5InypYXA967HisBTq3S"
access_token_secret = "4Yu1nk6xetMkITbqwEVonVhdzax0n96HnoVkllNP0dKFm"

# Authenticate with Twitter
client = tweepy.Client(
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token=access_token,
    access_token_secret=access_token_secret,
)

# Path to your JSON file containing tweets
json_file_path = "x.json"

# Function to load tweets from the JSON file
def load_tweets_from_json(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)
    return data.get("millionaire_mindset_tips", [])

# Function to save the updated JSON file
def save_tweets_to_json(file_path, tweets):
    data = {"millionaire_mindset_tips": tweets}
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)

# Main loop to post tweets at regular intervals

tweets = load_tweets_from_json(json_file_path)
tweet = tweets[0]
try:
    client.create_tweet(text=tweet)
    print(f"Tweeted: {tweet}")
    tweets.remove(tweet)  # Remove the posted tweet
    save_tweets_to_json(json_file_path, tweets)  # Update the JSON file
except Exception as e:
    print(f"Error posting tweet: {e}")
          # Sleep for 4 hours before posting the next tweet
