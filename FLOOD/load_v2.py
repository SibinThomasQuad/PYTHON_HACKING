import requests
import threading
import sys
import time

# Global variables to track successful and failed requests
successful_requests = 0
failed_requests = 0

# Function to send requests with different speeds
def send_request(method, url, post_params=None, speed='medium'):
    global successful_requests, failed_requests
    try:
        if method.lower() == 'get':
            response = requests.get(url)
        elif method.lower() == 'post':
            response = requests.post(url, data=post_params)
        else:
            print("Invalid method specified.")
            return

        if response.status_code == 200:
            successful_requests += 1
        else:
            failed_requests += 1
    except requests.exceptions.RequestException as e:
        failed_requests += 1

    # Introduce delay based on the selected speed
    if speed == 'slow':
        time.sleep(0.5)
    elif speed == 'medium':
        time.sleep(0.1)
    elif speed == 'fast':
        time.sleep(0.01)

# Function to send multiple requests concurrently
def load_test(method, url, num_requests, concurrency, post_params=None, speed='medium'):
    global successful_requests, failed_requests
    # Create threads for concurrent requests
    threads = []
    for _ in range(concurrency):
        t = threading.Thread(target=lambda: [send_request(method, url, post_params, speed) for _ in range(num_requests // concurrency)])
        threads.append(t)

    # Start threads
    for t in threads:
        t.start()

    # Print loader-style progress
    while threading.active_count() > 1:
        sys.stdout.write("\r" + f"Successful requests: \033[92m{successful_requests}\033[0m | Failed requests: \033[91m{failed_requests}\033[0m")
        sys.stdout.flush()

    sys.stdout.write("\r" + f"Successful requests: \033[92m{successful_requests}\033[0m | Failed requests: \033[91m{failed_requests}\033[0m")
    sys.stdout.flush()
    print("\nLoad testing completed.")

    # Print final status
    print("Final Status:")
    print(f"Successful requests: {successful_requests}")
    print(f"Failed requests: {failed_requests}")

if __name__ == "__main__":
    # Input parameters
    url = input("Enter the URL to test: ")
    method = input("Enter the HTTP method (GET or POST): ").lower()
    
    post_params = None
    if method == 'post':
        post_params = {}
        params_str = input("Enter POST parameters in the format 'key1=value1&key2=value2': ")
        for param in params_str.split('&'):
            key, value = param.split('=')
            post_params[key.strip()] = value.strip()

    num_requests = int(input("Enter the number of requests to send: "))
    concurrency = int(input("Enter the number of concurrent requests: "))

    speed = input("Enter request speed (slow, medium, fast): ").lower()

    # Start load testing
    print("Load testing started...")
    load_test(method, url, num_requests, concurrency, post_params, speed)
