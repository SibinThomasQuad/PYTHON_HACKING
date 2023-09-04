import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

# Function to download content from a URL and save it locally
def download_content(url, save_path):
    try:
        # Send an HTTP GET request to the URL
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            # Determine the file name from the URL
            file_name = os.path.join(save_path, os.path.basename(url))

            # Save the content to a file
            with open(file_name, 'wb') as file:
                file.write(response.content)
            print(f"Downloaded: {file_name}")
        else:
            print(f"Failed to download: {url}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Function to recursively crawl and download content from URLs on a domain
def crawl_and_download(domain_url, save_directory):
    try:
        # Send an HTTP GET request to the domain URL
        response = requests.get(domain_url)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse HTML content with BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')

            # Create a directory for saving downloaded files
            os.makedirs(save_directory, exist_ok=True)

            # Find all hyperlinks (anchor tags)
            links = soup.find_all('a')

            # Iterate through each link
            for link in links:
                href = link.get('href')
                if href:
                    # Join the URL with the base domain URL
                    full_url = urljoin(domain_url, href)

                    # Parse the full URL to extract the domain
                    parsed_url = urlparse(full_url)
                    if parsed_url.netloc == urlparse(domain_url).netloc:
                        # If the link is within the same domain, download the content
                        download_content(full_url, save_directory)

    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Main function
def main():
    domain_url = input("Enter the domain URL (e.g., https://example.com): ")
    save_directory = input("Enter the directory to save downloaded content: ")

    crawl_and_download(domain_url, save_directory)
    print("Download completed.")

if __name__ == "__main__":
    main()
