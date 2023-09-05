import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Function to download a file from a URL and display the status
def download_file(url, save_directory):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            # Get the file name from the URL
            file_name = os.path.basename(url)
            file_path = os.path.join(save_directory, file_name)
            
            # Save the file to the specified directory
            with open(file_path, 'wb') as file:
                file.write(response.content)
            return True, f"Downloaded '{file_name}'"
        else:
            return False, f"Failed to download '{url}'. Status code: {response.status_code}"
    except Exception as e:
        return False, f"Error downloading '{url}': {str(e)}"

# Function to crawl a URL and extract links with a specific file extension
def crawl_and_extract_links_with_extension(url, save_directory, target_extension):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            content = response.text
            soup = BeautifulSoup(content, 'html.parser')
            
            links = []
            downloaded_count = 0
            
            for link in soup.find_all('a', href=True):
                href = link.get('href')
                if href.endswith(target_extension):
                    links.append(href)
            
            # Download the files with the specified extension
            for link in links:
                full_url = urljoin(url, link)
                success, status_message = download_file(full_url, save_directory)
                if success:
                    downloaded_count += 1
                print(status_message)
            
            return links, downloaded_count
        else:
            return [], 0, f"Failed to retrieve '{url}'. Status code: {response.status_code}"
    except Exception as e:
        return [], 0, f"Error processing '{url}': {str(e)}"

# Input domain URL
domain_url = input("Enter the domain URL: ")
target_extension = input("Enter the file extension to download (e.g., .pdf, .txt, .csv): ")

# Create a directory to store downloaded files
download_directory = 'downloaded_files'
os.makedirs(download_directory, exist_ok=True)

# Crawl the domain and extract links with the specified extension
downloaded_links, downloaded_count = crawl_and_extract_links_with_extension(
    domain_url, download_directory, target_extension)

if downloaded_links:
    print(f"Found {len(downloaded_links)} files with the '{target_extension}' extension.")
else:
    print(f"No files with the '{target_extension}' extension found on the domain.")

print(f"Successfully downloaded {downloaded_count} files to '{download_directory}'")
