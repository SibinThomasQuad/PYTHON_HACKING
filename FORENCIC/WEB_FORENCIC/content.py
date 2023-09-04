import requests
from bs4 import BeautifulSoup

# Function to search for content in all hyperlinks of a webpage
def search_links_for_content(url, keyword):
    try:
        # Send an HTTP GET request to the URL
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse HTML content with BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find all hyperlinks (anchor tags)
            links = soup.find_all('a')

            # Iterate through each link and check if the keyword is in the link text
            for link in links:
                link_text = link.get_text()
                if keyword in link_text:
                    print(f"Keyword '{keyword}' found in link: {link['href']}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Example usage
if __name__ == "__main__":
    target_url = "https://infocomsoft.com"  # Replace with the URL you want to search
    keyword_to_search = "Game Development"  # Replace with your keyword
    search_links_for_content(target_url, keyword_to_search)
