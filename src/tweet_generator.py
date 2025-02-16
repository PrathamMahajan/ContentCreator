import google.generativeai as genai
from config import GEMINI_API_KEY

# Configure Gemini API Key
genai.configure(api_key=GEMINI_API_KEY)

def summarizee_text(text, max_words=250):
    """Uses Google Gemini AI to summarize text."""
    prompt = f"Paraphrase the following as a humorous funny tweet in less than {max_words} words:\n{text}"
    
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)

    return response.text.strip() if response and response.text else "Summarization failed."

def generate_hashtags(text):
    """Uses Gemini AI to generate relevant hashtags based on the text."""
    prompt = f"Generate 5 relevant hashtags for the following text:\n{text}"
    
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)
    
    return response.text.strip().split() if response and response.text else ["#News", "#Update"]

def generate_tweet(text):
    """Paraphrase it as a humorous funny tweet in less than 250 characters."""
    summary = summarizee_text(text)  # Get summary from Gemini API
    return summary[:280]  # Keep within 280 characters (excluding hashtags)

