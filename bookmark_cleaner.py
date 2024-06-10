import re
from tqdm import tqdm

# Specify the input and output file names
input_file = 'bookmarks.html'
output_file = 'cleaned_bookmarks.html'

# Read the HTML file
with open(input_file, 'r', encoding='utf-8') as file:
    content = file.read()

# Extract all links
links = re.findall(r'<A HREF="(.*?)"', content)
total_links = len(links)

# Create a set to hold unique links
unique_links = set()
new_content_lines = []
duplicate_count = 0

# Process each line and remove duplicate links
for line in tqdm(content.splitlines(), desc="Removing Duplicate Links"):
    match = re.search(r'<A HREF="(.*?)"', line)
    if match:
        link = match.group(1)
        if link not in unique_links:
            unique_links.add(link)
            new_content_lines.append(line)
        else:
            duplicate_count += 1
    else:
        new_content_lines.append(line)

cleaned_content = '\n'.join(new_content_lines)

# Function to remove empty folders
def remove_empty_folders(html_content):
    pattern = re.compile(r'<DT><H3>.*?</H3>\s*<DL><p>\s*</DL><p>', re.DOTALL)
    while pattern.search(html_content):
        html_content = pattern.sub('', html_content)
    return html_content

cleaned_content = remove_empty_folders(cleaned_content)

# Function to remove outer empty folders
def remove_outer_empty_folders(html_content):
    pattern = re.compile(r'<DL><p>\s*</DL><p>', re.DOTALL)
    while pattern.search(html_content):
        html_content = pattern.sub('', html_content)
    return html_content

cleaned_content = remove_outer_empty_folders(cleaned_content)

# Write the cleaned content to a new file
with open(output_file, 'w', encoding='utf-8') as file:
    file.write(cleaned_content)

print(f"Cleaning complete. {duplicate_count} duplicate links removed. The cleaned file is saved as '{output_file}'.")
