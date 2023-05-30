import requests

def clone_web_page(url):
    try:
        # Send a GET request to the specified URL
        response = requests.get(url)
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Save the HTML content to a file
            with open("cloned_page.html", "w", encoding="utf-8") as file:
                file.write(response.text)
            print("Web page cloned successfully!")
        else:
            print("Failed to clone web page. Status code:", response.status_code)
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)

# Example usage
url_to_clone = "https://example.com"
clone_web_page(url_to_clone)
