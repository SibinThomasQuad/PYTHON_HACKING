import requests
import re
import json
import datetime

# Function to search for keywords in a URL's content
def search_keywords_in_url(url, keywords):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            content = response.text.lower()  # Convert content to lowercase for case-insensitive search
            matched_keywords = []
            for keyword in keywords:
                if keyword.lower() in content:
                    matched_keywords.append((keyword, url))
            return matched_keywords
        else:
            print(f"Failed to retrieve {url}. Status code: {response.status_code}")
            return []
    except Exception as e:
        print(f"Error processing {url}: {str(e)}")
        return []

# Function to search keywords in all URLs on a domain
def search_keywords_in_domain(domain, keywords):
    try:
        response = requests.get(domain)
        if response.status_code == 200:
            content = response.text
            urls = re.findall(r'href=["\'](http[s]?://[^"\']+)["\']', content)
            matched_keywords = []
            for url in urls:
                matched_keywords += search_keywords_in_url(url, keywords)
            return matched_keywords
        else:
            print(f"Failed to retrieve {domain}. Status code: {response.status_code}")
            return []
    except Exception as e:
        print(f"Error processing {domain}: {str(e)}")
        return []

# Read domains from a text file (one domain per line)
with open('domains.txt', 'r') as domains_file:
    domains = domains_file.read().splitlines()

# Read keywords from a JSON file
with open('keywords.json', 'r') as keywords_file:
    keywords_data = json.load(keywords_file)
    keywords = keywords_data["keywords"]

# Create an HTML output file with the current date in the name
output_filename = f"output_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.html"
with open(output_filename, 'w') as output_file:
    # Write the HTML table header with colored rows and crawled date
    output_file.write("<html><head><title>OSINT Results</title></head><body>")
    output_file.write("<style>table {border-collapse: collapse;} th, td {border: 1px solid black; padding: 8px;} tr:nth-child(even) {background-color: #f2f2f2;}</style>")
    output_file.write("<table><tr><th>SL No.</th><th>Domain</th><th>Keyword</th><th>URL</th><th>Crawled Date</th></tr>")

    # Crawl URLs on each domain and search for keywords
    for sl_number, domain in enumerate(domains, start=1):
        print(f"Crawling domain: {domain}")
        matched_keywords = search_keywords_in_domain(domain, keywords)
        
        for keyword, url in matched_keywords:
            # Write the data to the HTML table with SL number and crawled date
            crawled_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            output_file.write(f"<tr><td>{sl_number}</td><td>{domain}</td><td>{keyword}</td><td><a href='{url}' target='_blank'>{url}</a></td><td>{crawled_date}</td></tr>")

    # Write the HTML table footer
    output_file.write("</table></body></html>")

print(f"Results saved to {output_filename}")
