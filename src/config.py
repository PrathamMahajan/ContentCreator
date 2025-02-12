import os
from dotenv import load_dotenv  

# Get the absolute path of the .env file (one level up)
env_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".env"))

# Load the environment variables from the specified file
load_dotenv(env_path)

# Retrieve the API keys
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
TWITTER_API_KEY = os.getenv("TWITTER_API_KEY")
TWITTER_API_SECRET = os.getenv("TWITTER_API_SECRET")
TWITTER_ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
TWITTER_ACCESS_SECRET = os.getenv("TWITTER_ACCESS_SECRET")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
DEEPSEEK_API_KEY=os.getenv("DEEPSEEK_API_KEY")
