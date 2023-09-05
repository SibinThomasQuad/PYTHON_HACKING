import requests
import re
from urllib.parse import urlparse
from bs4 import BeautifulSoup

def get_ip_addresses_from_text(text):
    # Use regular expression to find hardcoded IP addresses
    ip_pattern = r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b'
    ip_addresses = re.findall(ip_pattern, text)
    return ip_addresses

def crawl_and_extract_ips(domain):
    # Ensure the domain starts with 'http://' or 'https://'
    if not domain.startswith('http://') and not domain.startswith('https://'):
        domain = 'http://' + domain

    # Parse the URL
    parsed_url = urlparse(domain)

    # Get the domain name without the www prefix
    domain_name = parsed_url.netloc.lstrip("www.")

    try:
        # Fetch the content of the main URL
        response = requests.get(domain)
        if response.status_code == 200:
            main_content = response.text
            print(f"Content of {domain}:\n{main_content}")

            # Extract IP addresses from the main content
            ip_addresses = get_ip_addresses_from_text(main_content)
            if ip_addresses:
                print(f"Hardcoded IP addresses in {domain}: {', '.join(ip_addresses)}")

            # Parse the content for additional URLs
            soup = BeautifulSoup(main_content, 'html.parser')
            links = [link.get('href') for link in soup.find_all('a', href=True)]
            
            for link in links:
                full_url = link if link.startswith('http') else f"{domain}/{link}"
                print(f"Fetching content from {full_url}")
                sub_response = requests.get(full_url)
                if sub_response.status_code == 200:
                    sub_content = sub_response.text
                    # Extract IP addresses from sub-content
                    sub_ip_addresses = get_ip_addresses_from_text(sub_content)
                    if sub_ip_addresses:
                        print(f"Hardcoded IP addresses in {full_url}: {', '.join(sub_ip_addresses)}")

        else:
            print(f"Failed to retrieve content from {domain}. Status code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching content from {domain}: {e}")

if __name__ == "__main__":
    domain = input("Enter a domain (e.g., http://example.com): ")
    crawl_and_extract_ips(domain)
