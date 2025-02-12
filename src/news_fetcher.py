import feedparser
from newspaper import Article
import urllib.parse
import requests
from bs4 import BeautifulSoup
import re

def get_bbc_news_content(topic, max_results=5):
    """Fetches news articles from BBC News search and extracts full content."""
    search_url = f"https://www.bbc.com/search?q={urllib.parse.quote_plus(topic)}"
    feed = feedparser.parse(search_url)  # Parse the BBC search results (RSS not available)
    url = feed["href"] 
    return url


def extract_hrefs(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses

        soup = BeautifulSoup(response.text, 'html.parser')
        hrefs = [a.get('href') for a in soup.find_all('a') if a.get('href')]

        # Filter hrefs containing "/news/articles/"
        filtered_hrefs = [href for href in hrefs if "/news/articles/" in href]

        # Prepend "https://www.bbc.com/" to relative links
        full_links = ["https://www.bbc.com" + href if href.startswith("/") else href for href in filtered_hrefs]

        return full_links
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return []


def extract_paragraphs(url):
    try:
        # Fetch the content of the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract all <p> elements and return their text as a single string
        paragraphs = "\n".join(p.get_text() for p in soup.find_all('p'))
        
        return paragraphs
    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL: {e}")
        return ""  # Return an empty string in case of an error


def get_news_content(topic):
    news_data = get_bbc_news_content(topic)
    links = extract_hrefs(news_data)
    
    content_list = []  # List to store extracted news content
    
    for link in links:
        information = extract_paragraphs(link)
        content_list.append(information)  # Add extracted content to the list
    
    return content_list


