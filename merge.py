import random

def merge_html_files(header_file_path, body_file_path, output_file_path):
    with open(header_file_path, 'r') as header_file, open(body_file_path, 'r') as body_file:
        header = header_file.read()
        body = body_file.read()

    merged_html = header + body

    with open(output_file_path, 'w') as output_file:
        output_file.write(merged_html)

header_path_number = random.randint(1, 5)
body_path_number = random.randint(1, 1)
print(header_path_number , body_path_number)

header_path = f'./Header/ex{header_path_number}/index.html'
body_path = f'./Body/ex{body_path_number}/index.html'

merge_html_files('./Header/exPivo/index.html', './Body/ex1/index.html', 'output.html')
