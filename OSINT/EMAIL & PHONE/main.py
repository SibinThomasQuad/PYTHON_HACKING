import requests
import re
import json
import datetime
import bs4

# Function to search valid email addresses and phone numbers in a URL's content
def search_contacts_in_url(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            content = response.text
            soup = bs4.BeautifulSoup(content, 'html.parser')
            
            # Find valid email addresses using a regular expression for common email formats
            email_addresses = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b', content)
            
            # Find phone numbers using regular expression
            phone_numbers = re.findall(r'\b\d{10}\b', content)
            
            return email_addresses, phone_numbers, url
        else:
            print(f"Failed to retrieve {url}. Status code: {response.status_code}")
            return [], [], ""
    except Exception as e:
        print(f"Error processing {url}: {str(e)}")
        return [], [], ""

# Function to search valid email addresses and phone numbers in all URLs on a domain
def search_contacts_in_domain(domain):
    try:
        response = requests.get(domain)
        if response.status_code == 200:
            content = response.text
            urls = re.findall(r'href=["\'](http[s]?://[^"\']+)["\']', content)
            email_addresses = []
            phone_numbers = []
            
            for url in urls:
                email, phone, url_with_contacts = search_contacts_in_url(url)
                email_addresses += email
                phone_numbers += phone
                if email or phone:
                    # Write the data to the HTML table, including the URL
                    output_file.write(f"<tr><td>{sl_number}</td><td>{domain}</td><td>{','.join(email)}</td><td>{','.join(phone)}</td><td>{url_with_contacts}</td></tr>")
            
            return email_addresses, phone_numbers
        else:
            print(f"Failed to retrieve {domain}. Status code: {response.status_code}")
            return [], []
    except Exception as e:
        print(f"Error processing {domain}: {str(e)}")
        return [], []

# Read domains from a text file (one domain per line)
with open('domains.txt', 'r') as domains_file:
    domains = domains_file.read().splitlines()

# Create an HTML output file with the current date in the name
output_filename = f"output_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.html"
with open(output_filename, 'w') as output_file:
    # Write the HTML table header with colored rows and crawled date
    output_file.write("<html><head><title>OSINT Results</title></head><body>")
    output_file.write("<style>table {border-collapse: collapse;} th, td {border: 1px solid black; padding: 8px;} tr:nth-child(even) {background-color: #f2f2f2;}</style>")
    output_file.write("<table><tr><th>SL No.</th><th>Domain</th><th>Email</th><th>Phone</th><th>URL</th></tr>")

    sl_number = 0  # Serial number counter
    
    # Crawl URLs on each domain and search for valid email addresses and phone numbers
    for domain in domains:
        print(f"Crawling domain: {domain}")
        email_addresses, phone_numbers = search_contacts_in_domain(domain)
        
        # Increment the serial number
        sl_number += 1
    
    # Write the HTML table footer
    output_file.write("</table></body></html>")

print(f"Results saved to {output_filename}")
