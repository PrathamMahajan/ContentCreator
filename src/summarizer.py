# import google.generativeai as genai
# import os
# from config import GEMINI_API_KEY

# # Configure Gemini API Key
# genai.configure(api_key=GEMINI_API_KEY)

# def summarize_text(text, max_words=100):
#     """Uses Google Gemini AI to summarize text."""
#     prompt = f"Summarize the following in {max_words} words:\n{text}"

#     model = genai.GenerativeModel("gemini-pro")
#     response = model.generate_content(prompt)

#     return response.text.strip() if response and response.text else "Summarization failed."

# import requests
# import os
# from config import DEEPSEEK_API_KEY

# def summarize_text(text, max_words=100):
#     """Uses DeepSeek AI to summarize text."""
#     url = "https://api.deepseek.com/v1/completions"  # Replace with actual DeepSeek API endpoint
#     headers = {
#         "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
#         "Content-Type": "application/json"
#     }
#     payload = {
#         "model": "deepseek-chat",  # Replace with appropriate DeepSeek model
#         "messages": [
#             {"role": "system", "content": "You are a helpful assistant that summarizes text."},
#             {"role": "user", "content": f"Summarize the following in {max_words} words:\n{text}"}
#         ],
#         "max_tokens": 200
#     }
#     response = requests.post(url, headers=headers, json=payload)
    
#     if response.status_code == 200:
#         result = response.json()
#         return result.get("choices", [{}])[0].get("message", {}).get("content", "Summarization failed.").strip()
#     else:
#         return f"Error: {response.status_code} - {response.text}"


# Use a pipeline as a high-level helper
from transformers import pipeline
import textwrap

pipe = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text(text, max_length=150, min_length=50):
    """
    Summarizes the given text using the BART model.
    
    - Splits text into smaller chunks if it exceeds the model limit.
    """
    # BART has a max token limit of 1024
    max_input_length = 1024  
    wrapped_text = textwrap.wrap(text, width=max_input_length)  # Split text into smaller chunks
    summaries = []

    for chunk in wrapped_text:
        summary = pipe(chunk, max_length=max_length, min_length=min_length, do_sample=False)
        summaries.append(summary[0]['summary_text'])
    
    return " ".join(summaries)  # Combine summaries into one
