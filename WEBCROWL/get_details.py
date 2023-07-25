import importlib
import subprocess

def install_missing_library(library):
    try:
        importlib.import_module(library)
    except ImportError:
        print(f"{library} not found. Installing...")
        subprocess.check_call(["py -m pip", "install", library])
        print(f"{library} installed successfully.")

def extract_all_details(url, domain_name):
    required_libraries = ["requests", "bs4", "whois", "socket", "ssl", "re"]

    for library in required_libraries:
        install_missing_library(library)

    import requests
    from bs4 import BeautifulSoup
    import whois
    import socket
    import ssl
    import re

    def extract_server_info(url):
        try:
            response = requests.head(url)
            server_info = response.headers.get('Server')
            return server_info
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            return None

    def extract_domain_registration_date(domain):
        try:
            domain_info = whois.whois(domain)
            registration_date = domain_info.creation_date
            return registration_date
        except Exception as e:
            print(f"Error: {e}")
            return None

    def extract_dns_servers(domain):
        try:
            dns_servers = socket.gethostbyname_ex(domain)[1]
            return dns_servers
        except socket.gaierror as e:
            print(f"Error: {e}")
            return []

    def extract_ssl_details(url):
        try:
            context = ssl.create_default_context()
            with socket.create_connection((url, 443)) as sock:
                with context.wrap_socket(sock, server_hostname=url) as sslsock:
                    ssl_info = sslsock.getpeercert()
            return ssl_info
        except Exception as e:
            print(f"Error: {e}")
            return None

    def extract_third_party_hyperlinks(url):
        try:
            response = requests.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, 'html.parser')
            links = soup.find_all('a', href=True)
            third_party_links = [link['href'] for link in links if not re.match(f'^https?://(www\.)?{domain_name}', link['href'])]
            return third_party_links
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            return []

    def extract_links(url):
        try:
            response = requests.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, 'html.parser')
            links = soup.find_all('a', href=True)
            return [link['href'] for link in links]
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            return []

    def extract_images(url):
        try:
            response = requests.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, 'html.parser')
            images = soup.find_all('img', src=True)
            return [image['src'] for image in images]
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            return []

    def extract_emails(url):
        try:
            response = requests.get(url)
            response.raise_for_status()
            content = response.text
            email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
            return re.findall(email_pattern, content)
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            return []

    server_info = extract_server_info(url)
    if server_info:
        print(f"Server Information for {url}: {server_info}")
    else:
        print("Server information not available.")

    registration_date = extract_domain_registration_date(domain_name)
    if registration_date:
        print(f"Domain Registration Date for {domain_name}: {registration_date}")
    else:
        print("Domain registration date not available.")

    dns_servers = extract_dns_servers(domain_name)
    if dns_servers:
        print(f"DNS Servers for {domain_name}:")
        for server in dns_servers:
            print(server)
    else:
        print("DNS servers not found.")

    ssl_info = extract_ssl_details(url)
    if ssl_info:
        print(f"\nSSL Certificate Details for {url}:")
        print(f"Issuer: {ssl_info['issuer']}")
        print(f"Subject: {ssl_info['subject']}")
        print(f"Expiry Date: {ssl_info['notAfter']}")
    else:
        print("SSL certificate details not available.")

    third_party_links = extract_third_party_hyperlinks(url)
    if third_party_links:
        print(f"\nThird-Party Hyperlinks on {url}:")
        for link in third_party_links:
            print(link)
    else:
        print("No third-party hyperlinks found.")

    links = extract_links(url)
    if links:
        print(f"\nAll Hyperlinks on {url}:")
        for link in links:
            print(link)
    else:
        print("No hyperlinks found.")

    images = extract_images(url)
    if images:
        print(f"\nAll Images on {url}:")
        for image in images:
            print(image)
    else:
        print("No images found.")

    emails = extract_emails(url)
    if emails:
        print(f"\nAll Email Addresses on {url}:")
        for email in emails:
            print(email)
    else:
        print("No email addresses found.")

if __name__ == "__main__":
    website_url = "https://www.example.com"  # Replace with the desired website URL
    domain_name = "infocomsoft.com"  # Replace with the domain name of the website

    extract_all_details(website_url, domain_name)
