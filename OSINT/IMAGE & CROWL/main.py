import requests
import re
import json
import datetime
import bs4
import os
import hashlib

# Function to calculate MD5 and SHA-1 checksums of an image
def calculate_checksums(image_path):
    md5_hash = hashlib.md5()
    sha1_hash = hashlib.sha1()
    
    with open(image_path, "rb") as image_file:
        # Read the image file in chunks to conserve memory
        for chunk in iter(lambda: image_file.read(4096), b""):
            md5_hash.update(chunk)
            sha1_hash.update(chunk)
    
    return md5_hash.hexdigest(), sha1_hash.hexdigest()

# Function to download images from a URL and return image URLs, names, MD5, and SHA-1 checksums
def download_images_from_url(url, domain, image_directory):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            content = response.text
            soup = bs4.BeautifulSoup(content, 'html.parser')
            
            # Find all image tags in the HTML content
            img_tags = soup.find_all('img')
            
            image_data = []
            
            for img_tag in img_tags:
                img_url = img_tag.get('src')
                if img_url:
                    # Create the full image URL by joining the relative URL with the domain
                    full_img_url = img_url if img_url.startswith('http') else f"{domain}/{img_url}"
                    
                    # Get the image name from the URL
                    img_name = os.path.basename(full_img_url)
                    
                    # Download the image and save it to the specified directory
                    img_response = requests.get(full_img_url)
                    if img_response.status_code == 200:
                        image_path = os.path.join(image_directory, img_name)
                        with open(image_path, 'wb') as img_file:
                            img_file.write(img_response.content)
                        
                        # Calculate MD5 and SHA-1 checksums
                        md5_checksum, sha1_checksum = calculate_checksums(image_path)
                        
                        image_data.append((full_img_url, img_name, md5_checksum, sha1_checksum))
            
            return image_data
        else:
            print(f"Failed to retrieve {url}. Status code: {response.status_code}")
            return []
    except Exception as e:
        print(f"Error processing {url}: {str(e)}")
        return []

# Function to download images from all URLs on a domain and return image data
def download_images_in_domain(domain, image_directory):
    try:
        response = requests.get(domain)
        if response.status_code == 200:
            content = response.text
            urls = re.findall(r'href=["\'](http[s]?://[^"\']+)["\']', content)
            image_data = []
            
            for url in urls:
                image_data += download_images_from_url(url, domain, image_directory)
            
            return image_data
        else:
            print(f"Failed to retrieve {domain}. Status code: {response.status_code}")
            return []
    except Exception as e:
        print(f"Error processing {domain}: {str(e)}")
        return []

# Read domains from a text file (one domain per line)
with open('domains.txt', 'r') as domains_file:
    domains = domains_file.read().splitlines()

# Create a directory to store downloaded images
image_directory = 'downloaded_images'
os.makedirs(image_directory, exist_ok=True)

# Create an HTML output file with the current date in the name
output_filename = f"image_report_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.html"
with open(output_filename, 'w') as output_file:
    # Write the HTML table header with colored rows and crawled date
    output_file.write("<html><head><title>Image Report</title></head><body>")
    output_file.write("<style>table {border-collapse: collapse;} th, td {border: 1px solid black; padding: 8px;} tr:nth-child(even) {background-color: #f2f2f2;}</style>")
    output_file.write("<table><tr><th>SL No.</th><th>Domain</th><th>Image URL</th><th>Image Name</th><th>MD5 Checksum</th><th>SHA-1 Checksum</th></tr>")

    sl_number = 0  # Serial number counter
    
    # Download images from each domain and gather image data
    for domain in domains:
        print(f"Crawling domain: {domain}")
        image_data = download_images_in_domain(domain, image_directory)
        
        # Increment the serial number
        sl_number += 1
        
        for img_url, img_name, md5_checksum, sha1_checksum in image_data:
            # Write the data to the HTML table with img src tag for displaying images
            output_file.write(f"<tr><td>{sl_number}</td><td>{domain}</td><td><img src='{img_url}' alt='{img_name}'></td><td>{img_name}</td><td>{md5_checksum}</td><td>{sha1_checksum}</td></tr>")
    
    # Write the HTML table footer
    output_file.write("</table></body></html>")

print(f"Image report saved to {output_filename}")
