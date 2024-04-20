import re
from bs4 import BeautifulSoup
import os
import random
import streamlit as st
import streamlit.components.v1 as components
import text_writer
import get_image_topic
from search_image import get_image_urls

# Streamlit (interface) code starts here
st.set_page_config(page_title="VerstkAi", page_icon=":globe_with_meridians:", layout="wide")

st.title("VerstkAi")
st.subheader("A simple Website generator")

# Create an input field for the company name
company_name = st.text_input("Enter the company name")

# Create an input field for the company description
company_description = st.text_area("Enter the company description")

if st.button('Generate'):
    # When pressed, the field content will be written to the variables
    st.write(f'Company Name: {company_name}')
    st.write(f'Company Description: {company_description}')

    if (company_name and company_description):
        # Open and read the HTML file
        with open('output.html', 'r') as f:
            html_string = f.read()

        # Display the HTML file
        components.html(html_string, height=650)

        # Create a button for exporting the HTML file
        # Check if the file exists
        if os.path.exists("output.html"):
            # Read the file
            with open("output.html", "r") as file:
                file_content = file.read()

            # Create a button for downloading the file
            st.download_button(
                label="Export",
                data=file_content,
                file_name="output.html",
                mime="text/html",
            )
        else:
            st.write("The file output.html does not exist in the current directory.")

        # Main logic starts here
        topic = f'{company_name} - {company_description}'

        res = []
        temp = ''
        flag = 1
        for ele in topic:
            if ele == ' ' and flag:
                res.append(temp)
                temp = ''
                flag = 0
            else :
                temp += ele
        res.append(temp) # Define first word which will be used as a company name for page

        company_name = str(res[0])
        print (company_name)

        def replace_background_image_in_file(file_path, new_image_url): # Function to replace background image
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
            print(response)
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
              first_h2_tag.string.replace_with(company_name)

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
            print(response)
            imgurl_horizontal = random.choice(get_image_urls(response, "horizontal"))
            imgurl_vertical = random.choice(get_image_urls(response, "vertical"))
            replace_background_image_in_file('output.html', imgurl_vertical)
            set_img_src_in_file('output.html', imgurl_vertical)
            print("vertical ~> ", f'{imgurl_vertical} dark')
            print("horizontal ~> ", f'{imgurl_vertical} dark')
          else:
            print("An error occurred while communicating with TextAi.")
        except Exception as e:
          print(f"An error occurred: {e}")

    else:
        # Open error, cause input's empty
        with open('error.html', 'r') as f:
            html_string = f.read()

        # Display the HTML file
        components.html(html_string, height=600)
