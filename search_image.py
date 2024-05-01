import requests
import random

def get_image_urls(query, orientation):
    API_KEY = "43328343-b9278c71ab9b02120824b9bdc"  # replace with your Pixabay API key
    url = f"https://pixabay.com/api/?key={API_KEY}&q={query}&image_type=photo&orientation={orientation}"
    response = requests.get(url)
    data = response.json()
    urls = [img["webformatURL"] for img in data["hits"]]
    return urls


