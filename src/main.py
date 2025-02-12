from news_fetcher import get_news_content
from summarizer import summarize_text
from tweet_generator import generate_tweet, generate_hashtags
from twitter_api import post_tweet

def main(): 
    topic = input("Enter a topic: ")

    articles = []
    # Fetch news articles
    articles = get_news_content(topic)
    if not articles:
        print("No news articles found.")
        return

    a = "*"
    for i in range(100):
        a += "*"

    # Summarize first article (can be modified to loop through multiple)
    for article in articles:
        print(a)
        summary = summarize_text(article)
        print(summary)
        print("-------TWEET-------")
        tweet = generate_tweet(summary)
        hashtags = generate_hashtags(summary)
        
        print("Generated Tweet:", tweet)
        print("Generated Hashtags:", " ".join(hashtags))

if __name__ == "__main__":
    main()
