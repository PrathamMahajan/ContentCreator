import random

def generate_tweet(summary):
    """Formats a summary into a tweet with hashtags."""
    hashtags = ["#Trending", "#BreakingNews", "#Tech", "#Finance", "#AI", "#Crypto"]
    selected_hashtags = " ".join(random.sample(hashtags, 2))
    
    tweet = f"{summary[:240]}... {selected_hashtags}"  # Keep within 280 characters
    return tweet

# Example usage:
# print(generate_tweet("Bitcoin hits $50K after strong institutional support."))
