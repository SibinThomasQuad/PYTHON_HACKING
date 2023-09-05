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

# Function to crawl a URL and extract PDF links
def crawl_and_extract_pdf_links(url, save_directory):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            content = response.text
            soup = BeautifulSoup(content, 'html.parser')
            
            pdf_links = []
            
            for link in soup.find_all('a', href=True):
                href = link.get('href')
                if href.endswith('.pdf'):
                    pdf_links.append(href)
            
            downloaded_count = 0
            
            # Download the PDF files
            for pdf_link in pdf_links:
                full_pdf_url = urljoin(url, pdf_link)
                success, status_message = download_file(full_pdf_url, save_directory)
                if success:
                    downloaded_count += 1
                print(status_message)
            
            return pdf_links, downloaded_count
        else:
            return [], 0, f"Failed to retrieve '{url}'. Status code: {response.status_code}"
    except Exception as e:
        return [], 0, f"Error processing '{url}': {str(e)}"

# Input domain URL
domain_url = input("Enter the domain URL: ")

# Create a directory to store downloaded PDFs
pdf_directory = 'downloaded_pdfs'
os.makedirs(pdf_directory, exist_ok=True)

# Crawl the domain and extract PDF links
pdf_links, downloaded_count = crawl_and_extract_pdf_links(domain_url, pdf_directory)

if pdf_links:
    print(f"Found {len(pdf_links)} PDF files.")
else:
    print("No PDF files found on the domain.")

print(f"Successfully downloaded {downloaded_count} PDF files to '{pdf_directory}'")
