import requests
import time
import threading

# Function to send requests
def send_request(url):
    try:
        response = requests.get(url)
        # You can process the response here if needed
        print(f"Request to {url} completed with status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Request to {url} failed: {e}")

# Function to send multiple requests concurrently
def load_test(url, num_requests, concurrency):
    print(f"Sending {num_requests} requests with concurrency {concurrency} to {url}")
    start_time = time.time()

    # Create threads for concurrent requests
    threads = []
    for _ in range(concurrency):
        t = threading.Thread(target=lambda: [send_request(url) for _ in range(num_requests // concurrency)])
        threads.append(t)

    # Start threads
    for t in threads:
        t.start()

    # Wait for all threads to finish
    for t in threads:
        t.join()

    end_time = time.time()
    total_time = end_time - start_time
    print(f"All requests completed in {total_time} seconds")

if __name__ == "__main__":
    url = input("Enter the URL to test: ")
    total_requests = int(input("Enter the total number of requests to send: "))
    concurrency = int(input("Enter the number of concurrent requests: "))

    load_test(url, total_requests, concurrency)
