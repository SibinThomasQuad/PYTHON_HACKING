import requests
from concurrent.futures import ThreadPoolExecutor
from colorama import Fore, Style

# Define the URL of your website
url = "https://example.com"  # Replace with the URL of your website

# Function to send an HTTP GET request to the URL
def send_request(url):
    try:
        response = requests.get(url)
        return response.status_code
    except requests.exceptions.RequestException as e:
        return str(e)

# Number of concurrent requests
num_requests = 100

# Create a ThreadPoolExecutor with the desired number of threads
with ThreadPoolExecutor(max_workers=num_requests) as executor:
    # Use a list comprehension to create a list of futures (results of the send_request function)
    futures = [executor.submit(send_request, url) for _ in range(num_requests)]

    # Wait for all the futures to complete
    response_codes = [future.result() for future in futures]

# Count the number of successful (status code 200) and unsuccessful requests
success_count = response_codes.count(200)
unsuccessful_count = num_requests - success_count

# Print the count of requests and their response codes in green and red
print(f"Total Requests: {num_requests}")
print(f"Successful Requests: {success_count} {Fore.GREEN if success_count > 0 else Fore.RESET}{response_codes.count(200)}{Style.RESET_ALL}")
print(f"Unsuccessful Requests: {unsuccessful_count} {Fore.RED if unsuccessful_count > 0 else Fore.RESET}{unsuccessful_count}{Style.RESET_ALL}")
