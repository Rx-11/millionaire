import tweepy
import json
import time
import os

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

# Load tweets from GitHub Secrets
import json
import os

# Read the tips from the JSON file
json_file = "x.json"
with open(json_file, "r") as file:
    data = json.load(file)
    tips = data["millionaire_mindset_tips"]

# Debugging output
print("Tips:", tips)

# Read and Update Last Tweeted Index
last_tweeted_index_file = "last_tweeted_tip.txt"

# Read the index of the last tweeted tip
last_tweeted_index = 0
if os.path.isfile(last_tweeted_index_file):
    with open(last_tweeted_index_file, "r") as index_file:
        last_tweeted_index = int(index_file.read().strip())

# Debugging output
print("Last tweeted index:", last_tweeted_index)

# Determine the index of the next tip to tweet
next_tip_index = last_tweeted_index + 1
if next_tip_index >= len(tips):
    next_tip_index = 0

# Debugging output
print("Next tip index:", next_tip_index)

# Store the index of the next tip to tweet
with open(last_tweeted_index_file, "w") as index_file:
    index_file.write(str(next_tip_index))

client = tweepy.Client(
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token=access_token,
    access_token_secret=access_token_secret,
)

tweet = tips[next_tip_index]

try:
    client.create_tweet(text=tweet)
    print(f"Tweeted: {tweet}")
except Exception as e:
    print(f"Error posting tweet: {e}")
          
          
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
