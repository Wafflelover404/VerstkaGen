import requests
import re
from bs4 import BeautifulSoup
import os
import random

import text_writer  # For page's text
import get_image_topic  # For image's topic
from search_image import get_image_urls  # Image search function

os.system("python merge.py")  # Merge HTML files to get started"

company_name_inp = input("Company name ~> ")
company_desc_inp = input("Company Description ~> ")
topic = f'{company_name_inp} - {company_desc_inp}'

def replace_background_image_in_file(file_path, new_image_url):
    with open(file_path, 'r') as f:
        html_content = f.read()
    pattern = r'background-image:\s*url\("(.*?)"\);'
    replacement = f'background-image: url("{new_image_url}");'
    new_html_content = re.sub(pattern, replacement, html_content)
    with open(file_path, 'w') as f:
        f.write(new_html_content)

def set_img_src_in_file(file_path, new_src):
    with open(file_path, 'r') as f:
        html_content = f.read()
    pattern = fr'<img\s.*?class="vertical-image".*?src="(.*?)"'
    replacement = f'<img src="{new_src}" class="vertical-image"'
    new_html_content = re.sub(pattern, replacement, html_content, flags=re.DOTALL)
    with open(file_path, 'w') as f:
        f.write(new_html_content)

try:
    response = text_writer.send(topic)
    if response != "Error":
        # Load the HTML file
        with open("output.html", "r") as html_file:
            soup = BeautifulSoup(html_file, "html.parser")

        # Find the first <p> tag and replace its content
        first_p_tag = soup.p
        if first_p_tag:
            first_p_tag.string.replace_with(response)

        # Save the modified HTML back to the file
        with open("output.html", "w") as html_file:
            html_file.write(str(soup))

        # Load the HTML file
        with open("output.html", "r") as html_file:
            soup = BeautifulSoup(html_file, "html.parser")

        # Find the first <h2> tag and replace its content
        first_h2_tag = soup.h2
        if first_h2_tag:
            first_h2_tag.string.replace_with(company_name_inp)

        # Save the modified HTML back to the file
        with open("output.html", "w") as html_file:
            html_file.write(str(soup))
    else:
        print("An error occurred while communicating with TextAi.")
except Exception as e:
    print(f"An error occurred: {e}")

try:
    response = get_image_topic.send(topic)
    if response != "Error":
        imgurl_horizontal = random.choice(get_image_urls(response, "horizontal"))
        imgurl_vertical = random.choice(get_image_urls(response, "vertical"))
        replace_background_image_in_file('output.html', imgurl_vertical)
        set_img_src_in_file('output.html', imgurl_vertical)
        print("vertical ~> ", imgurl_vertical)
        print("horizontal ~> ", imgurl_horizontal)
    else:
        print("An error occurred while communicating with TextAi.")
except Exception as e:
    print(f"An error occurred: {e}")

print("All processes have completed successfully, and all changes have been written to the HTML code.")
