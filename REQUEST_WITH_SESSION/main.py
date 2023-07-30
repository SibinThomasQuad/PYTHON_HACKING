import requests
from bs4 import BeautifulSoup

# Function to get all cookie values from a request
def get_all_cookies(url):
    try:
        response = requests.get(url)
        return response.cookies

    except requests.exceptions.RequestException as e:
        print(f"Error occurred while fetching cookies: {e}")
        return None

# Function to get the _token value from the URL
def get_token(url, cookies):
    try:
        response = requests.get(url, cookies=cookies)
        soup = BeautifulSoup(response.content, 'html.parser')
        token = soup.find('input', {'name': '_token'})['value']
        return token
    except requests.exceptions.RequestException as e:
        print(f"Error occurred while fetching the token: {e}")
        return None

# Function to perform the POST request
def post_with_credentials(url, username, password, token, cookies):
    try:
        data = {
            '_token': token,
            'username': username,
            'password': password
        }
        response = requests.post(url, data=data, cookies=cookies)
        print(response.text)  # You can process the response here as needed

    except requests.exceptions.RequestException as e:
        print(f"Error occurred during the POST request: {e}")

if __name__ == "__main__":
    base_url = "https://example.com"  # Replace with the base URL of your website
    login_url = f"{base_url}/login"   # Replace with the actual login URL

    # Get cookies from the first request
    cookies = get_all_cookies(base_url)

    # Make a GET request to get the _token value
    if cookies:
        token = get_token(login_url, cookies)

        if token:
            # Replace 'your_username', and 'your_password' with actual login credentials
            username = 'your_username'
            password = 'your_password'
            post_with_credentials(login_url, username, password, token, cookies)
