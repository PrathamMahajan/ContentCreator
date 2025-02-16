import time
import psycopg2
from news_fetcher import get_news_content
from summarizer import summarize_text
from tweet_generator import generate_tweet, generate_hashtags
from twitter_api import post_tweet

def main():
    topic = input("Enter a topic: ").strip()

    if not topic:
        print("Error: Topic cannot be empty. Please enter a valid topic.")
        return []

    try:
        articles = get_news_content(topic)
        if not articles:
            print("No news articles found.")
            return []
    except Exception as e:
        print(f"Error fetching news articles: {e}")
        return []

    
    tweets = []

    for article in articles:
        if not article or not isinstance(article, str):
            print("Skipping invalid or empty article.")
            continue

        try:
            summary = summarize_text(article)
            if not summary or summary.lower().startswith("summarization failed"):
                print("Error summarizing article.")
                continue
        except Exception as e:
            print(f"Error summarizing article: {e}")
            continue

        try:
            tweet = generate_tweet(summary)
            hashtags = generate_hashtags(summary)
            
            if isinstance(hashtags, list):
                hashtags = " ".join(hashtags)

            final_tweet = tweet + " " + hashtags

            tweets.append(final_tweet)
        except Exception as e:
            print(f"Error generating tweet or hashtags: {e}")
            continue

    return tweets

if __name__ == "__main__":
    tweets = main()
    separator = "*" * 100
    for t in tweets:
        time.sleep(5)  # Prevent Twitter API rate limits
        print(separator)
        print(t)
        # post_tweet(t)
