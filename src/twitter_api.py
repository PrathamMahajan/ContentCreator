import tweepy
from config import (TWITTER_API_KEY,TWITTER_API_SECRET,TWITTER_ACCESS_TOKEN,TWITTER_ACCESS_SECRET,TWITTER_BEARER_TOKEN )

def authenticate_twitter():
    client = tweepy.Client(
        bearer_token=TWITTER_BEARER_TOKEN, 
        consumer_key=TWITTER_API_KEY,
        consumer_secret=TWITTER_API_SECRET,
        access_token=TWITTER_ACCESS_TOKEN,
        access_token_secret=TWITTER_ACCESS_SECRET
    )
    return client

def post_tweet(tweet):
    client = authenticate_twitter()
    try:
        response = client.create_tweet(text=tweet)  # Fix: Use keyword argument `text=`
        print(f"Tweet posted successfully! Tweet ID: {response.data['id']}")
    except Exception as e:
        print(f"Error posting tweet: {e}")


post_tweet("Elon Musk just offered to buy the company behind ChatGPT for $97.4 billion. Guess he's trying to end the AI apocalypse before it even starts. #MuskBotBusters #ElonMusk #OpenAIAcquisition #ChatGPT #AIRevolution #TechIndustry")

