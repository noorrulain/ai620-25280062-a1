import os
from newsapi import NewsApiClient
from dotenv import load_dotenv

load_dotenv()

def get_news_data(query="AI job trends"):
    api_key = os.getenv("NEWS_API_KEY")
    newsapi = NewsApiClient(api_key=api_key)
    
    # Extracting articles related to the AI Labor Market theme
    articles = newsapi.get_everything(q=query, language='en', sort_by='relevancy')
    return articles['articles']