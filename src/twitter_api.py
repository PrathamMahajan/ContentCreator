import tweepy
import os
from config import TWITTER_API_KEY, TWITTER_API_SECRET, TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET

def authenticate_twitter():
    """Authenticates with Twitter API using Tweepy."""
    auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET)
    auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET)
    return tweepy.API(auth)

def post_tweet(tweet):
    """Posts a tweet to Twitter."""
    api = authenticate_twitter()
    try:
        api.update_status(tweet)
        print("Tweet posted successfully!")
    except Exception as e:
        print(f"Error posting tweet: {e}")

# Example usage:
# post_tweet("This is a test tweet.")
