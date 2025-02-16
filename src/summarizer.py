from transformers import pipeline, logging

# Suppress warnings
logging.set_verbosity_error()

# Load the summarization model
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

def summarize_text(text):
    if not text or len(text.strip()) == 0:
        return "Summarization failed: Empty input."
    summary = summarizer(text, max_length=250, min_length=20, do_sample=False)
    return summary[0]['summary_text']

