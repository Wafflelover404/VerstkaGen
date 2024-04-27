import random
import os


def count_folders(directory):
    # Use os.listdir() to get a list of all items in the directory
    folder_list = [f for f in os.listdir(directory) if os.path.isdir(os.path.join(directory, f))]
    # Return the count of folders
    return len(folder_list)

def merge_html_files(header_file_path, body_file_path, output_file_path):
    with open(header_file_path, 'r') as header_file, open(body_file_path, 'r') as body_file:
        header = header_file.read()
        body = body_file.read()

    # Extract the <style> content from the header
    style_start = header.find("<style>")
    style_end = header.find("</style>") + len("</style>")
    style_content = header[style_start:style_end]

    # Replace the <style> content in the body with the extracted style
    body = body.replace("<style>", style_content)

    # Merge the header and modified body
    merged_html = header[:style_start] + body + header[style_end:]

    with open(output_file_path, 'w') as output_file:
        output_file.write(merged_html)

headers_amount = count_folders('./Header')
body_amount = count_folders('./Body')

print(f"Amount of Headers: {headers_amount}")
print(f"Amount of Body's: {body_amount}")

header_path_number = random.randint(1, headers_amount)
body_path_number = random.randint(1, body_amount)
print(f"Selected Header: ex{header_path_number}")
print(f"Selected Body: ex{body_path_number}")

header_path = f'./Header/ex{header_path_number}/index.html'
body_path = f'./Body/ex{body_path_number}/index.html'

merge_html_files(header_path, body_path, 'output.html')
