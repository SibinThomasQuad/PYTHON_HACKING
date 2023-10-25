import requests
from colorama import Fore, Style

# Function to check the response and print the result with the domain
def check_url(domain):
    url = f"https://{domain}/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"{domain}: {Fore.RED}Yes{Style.RESET_ALL}")
        else:
            print(f"{domain}: {Fore.GREEN}No{Style.RESET_ALL}")
    except requests.exceptions.RequestException:
        print(f"{domain}: {Fore.GREEN}No{Style.RESET_ALL}")

# Read the text file containing domain names
file_path = 'your_text_file.txt'  # Replace with the path to your text file

with open(file_path, 'r') as file:
    for line in file:
        domain = line.strip()
        check_url(domain)
