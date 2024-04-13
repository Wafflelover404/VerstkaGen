import requests
import random

def get_image_urls(query, orientation):
    API_KEY = "your key"  # replace with your Pixabay API key
    url = f"https://pixabay.com/api/?key={API_KEY}&q={query}&image_type=photo&orientation={orientation}"
    response = requests.get(url)
    data = response.json()
    urls = [img["webformatURL"] for img in data["hits"]]
    return urls

topic = input("Topic to search for ~> ")
print("vertical ~> ", random.choice(get_image_urls(topic, "vertical")))
print("horizontal ~> ", random.choice(get_image_urls(topic, "horizontal")))
