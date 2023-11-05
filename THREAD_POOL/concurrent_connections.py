import requests
from concurrent.futures import ThreadPoolExecutor

# Define the URL you want to request
url = "https://example.com"  # Replace with the URL you want to request

# Function to send an HTTP GET request to the URL
def send_request(url):
    try:
        response = requests.get(url)
        return response.status_code
    except requests.exceptions.RequestException as e:
        return str(e)

# Number of concurrent requests
num_requests = 700

# Create a ThreadPoolExecutor with the desired number of threads
with ThreadPoolExecutor(max_workers=num_requests) as executor:
    # Use a list comprehension to create a list of futures (results of the send_request function)
    futures = [executor.submit(send_request, url) for _ in range(num_requests)]

    # Wait for all the futures to complete
    for future in futures:
        future.result()  # This will block until the future is complete

print("All requests completed.")
