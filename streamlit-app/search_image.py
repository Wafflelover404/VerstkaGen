import requests
import random
import streamlit

def get_image_urls(query, orientation):
    API_KEY = st.secrets["search_image"]["API_KEY"]  # replace with your Pixabay API key
    url = f"https://pixabay.com/api/?key={API_KEY}&q={query}&image_type=photo&orientation={orientation}"
    response = requests.get(url)
    data = response.json()
    urls = [img["webformatURL"] for img in data["hits"]]
    return urls
