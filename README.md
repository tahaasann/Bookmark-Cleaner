# Bookmark Cleaner

Bookmark Cleaner is a Python script designed to clean up and organize your browser bookmarks. It removes duplicate links, retains only unique links, and deletes empty bookmark folders. This tool is especially useful for those who have accumulated a large number of bookmarks over time and need a way to clean them up efficiently.

## Features

- Removes duplicate bookmarks, keeping only one instance of each link.
- Deletes empty bookmark folders.
- Outputs a cleaned bookmark file in HTML format.

## Requirements

- Python 3.x
- tqdm: For progress bars in the terminal
- requests: For potential future enhancements or link validation
- BeautifulSoup: For potential future enhancements or HTML parsing

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/bookmark-cleaner.git
    ```
2. Change into the project directory:v
    ```bash
    cd bookmark-cleaner
    ```
3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Export your bookmarks from your browser as an HTML file. Typically, you can do this from the bookmarks manager in your browser.

2. Place the exported `bookmarks.html` file in the project directory.

3. Run the script:
    ```bash
    python bookmark_cleaner.py
    ```

4. The cleaned bookmarks will be saved as `cleaned_bookmarks.html` in the project directory.

## Code

Here is the main code for the script:

```python
import re
from tqdm import tqdm

# Input and output file names
input_file = 'bookmarks.html'
output_file = 'cleaned_bookmarks.html'

# Read the HTML file
with open(input_file, 'r', encoding='utf-8') as file:
    content = file.read()

# Extract all links
links = re.findall(r'<A HREF="(.*?)"', content)
total_links = len(links)

# Track unique links
unique_links = set()
new_content_lines = []
duplicate_count = 0

# Process each line and remove duplicates
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
```


## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
Thanks to the tqdm project for the progress bar utility.

## Contact
If you have any questions or feedback, please contact tahaasann@gmail.com .