import requests
from bs4 import BeautifulSoup
import paramiko
import socket
import hashlib
import subprocess

# Example using Requests for sending HTTP requests
def send_get_request(url):
    """
    Sends a GET request to the specified URL using the Requests library.
    """
    response = requests.get(url)
    print(f"GET Request Status Code: {response.status_code}")
    print("Response Content:")
    print(response.text)

# Example using Beautiful Soup for HTML parsing
def parse_html(html_content):
    """
    Parses HTML content using Beautiful Soup.
    """
    soup = BeautifulSoup(html_content, 'html.parser')
    title_text = soup.title.text
    paragraph_text = soup.p.text
    print(f"Title: {title_text}")
    print(f"Paragraph: {paragraph_text}")

# Example using Paramiko for SSH
def ssh_example():
    """
    Demonstrates connecting to an SSH server using Paramiko.
    """
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        client.connect('example.com', username='your_username', password='your_password')
        stdin, stdout, stderr = client.exec_command('ls -l')
        print("SSH Command Output:")
        print(stdout.read().decode())
    finally:
        client.close()

# Example using hashlib for secure hash
def hash_example(data):
    """
    Calculates the SHA-256 hash of the provided data using hashlib.
    """
    sha256_hash = hashlib.sha256(data.encode()).hexdigest()
    print(f"SHA-256 Hash: {sha256_hash}")

# Example using socket for basic networking
def socket_example():
    """
    Demonstrates basic networking using the socket library.
    """
    target_host = 'www.example.com'
    target_port = 80

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((target_host, target_port))

    # Send a simple HTTP request
    request = b"GET / HTTP/1.1\r\nHost: www.example.com\r\n\r\n"
    client.send(request)

    # Receive and print the response
    response = client.recv(4096)
    print("Socket Response:")
    print(response.decode())

# Example using subprocess to run sqlmap
def run_sqlmap(target_url):
    """
    Runs SQLMap on the specified target URL using subprocess.
    """
    sqlmap_cmd = ["sqlmap", "-u", target_url, "--batch", "--random-agent"]

    try:
        subprocess.run(sqlmap_cmd, check=True)
    except subprocess.CalledProcessError as e:
        print(f"SQLMap process failed with error: {e}")

if __name__ == "__main__":
    # Example using Requests
    print("Example 1: Sending GET request using Requests")
    send_get_request("https://www.example.com")
    print("\n")

    # Example using Beautiful Soup
    print("Example 2: Parsing HTML using Beautiful Soup")
    html_content = "<html><head><title>Example</title></head><body><p>Hello, World!</p></body></html>"
    parse_html(html_content)
    print("\n")

    # Example using Paramiko for SSH
    print("Example 3: Using Paramiko for SSH")
    ssh_example()
    print("\n")

    # Example using hashlib for secure hash
    print("Example 4: Using hashlib for secure hash")
    hash_example("example_data")
    print("\n")

    # Example using socket for basic networking
    print("Example 5: Using socket for basic networking")
    socket_example()
    print("\n")

    # Example using subprocess to run sqlmap
    print("Example 6: Running sqlmap using subprocess")
    target_url = "http://example.com/login"
    run_sqlmap(target_url)
