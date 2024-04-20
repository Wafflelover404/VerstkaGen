import random
import os

def count_files_in_directory(directory):
    return len([f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))])

def merge_html_files(header_file_path, body_file_path, output_file_path):
    with open(header_file_path, 'r') as header_file, open(body_file_path, 'r') as body_file:
        header = header_file.read()
        body = body_file.read()

    merged_html = header + body

    with open(output_file_path, 'w') as output_file:
        output_file.write(merged_html)

header_path_number = random.randint(1, 4)
body_path_number = random.randint(1, 2)
print(str(count_files_in_directory("Header")) + " ~~ Amount of Headers")
print(str(count_files_in_directory("Body")) + " ~~ Amount of Body's")
print(header_path_number , body_path_number)

header_path = f'./Header/ex{header_path_number}/index.html'
body_path = f'./Body/ex{body_path_number}/index.html'

merge_html_files(header_path, body_path, 'output.html')
