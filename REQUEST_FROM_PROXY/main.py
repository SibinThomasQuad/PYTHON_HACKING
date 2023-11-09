import requests
from requests.exceptions import RequestException
from termcolor import colored
def label():
    label = '''
    
    ███████████████████████████████████████████████████████████▀█
    █▄─▄▄─█▄─▄▄▀█─▄▄─█▄─▀─▄█▄─█─▄█▀▀▀▀▀██▄─▄▄─█▄─▄█▄─▀█▄─▄█─▄▄▄▄█
    ██─▄▄▄██─▄─▄█─██─██▀─▀███▄─▄██████████─▄▄▄██─███─█▄▀─██─██▄─█
    ▀▄▄▄▀▀▀▄▄▀▄▄▀▄▄▄▄▀▄▄█▄▄▀▀▄▄▄▀▀▀▀▀▀▀▀▀▄▄▄▀▀▀▄▄▄▀▄▄▄▀▀▄▄▀▄▄▄▄▄▀
    
    '''
    return label

def get_location(ip_address):
    ip_address = ip_address.split(':')[0]
    base_url = f"http://ipinfo.io/{ip_address}/json"

    try:
        response = requests.get(base_url)
        data = response.json()

        country = data.get('country', 'N/A')
        region = data.get('region', 'N/A')
        city = data.get('city', 'N/A')
        loc = data.get('loc', 'N/A').split(',')

        print(f"IP Address: {ip_address}")
        print(f"Country: {country}")
        print(f"Region: {region}")
        print(f"City: {city}")
        print(f"Latitude: {loc[0]}")
        print(f"Longitude: {loc[1]}")

    except requests.exceptions.RequestException as e:
        print("Proxy IP info not found")

def send_request_via_proxy(url, proxy):
    try:
        response = requests.get(url, proxies={'http': proxy, 'https': proxy}, timeout=5)
        get_location(proxy)
        # Process the response as needed
        status_code = response.status_code
        if status_code == 200:
            print(colored(f"Proxy: {proxy}, Status Code: {status_code}", 'green'))
        else:
            print(colored(f"Proxy: {proxy}, Status Code: {status_code}", 'yellow'))
    except RequestException as e:
        print(colored(f"Proxy: {proxy}, Not Connected", 'red'))
    print("="*100)

def main():
    print(colored(label(),'yellow'))
    print("[Tool to test domain from diffrent country with proxy]")
    print("-"*100)
    url = input("Enter Domain (eg: http://example.com) > ")
    proxies_file = input("Enter Proxy list (eg: proxy.txt) > ")  # Replace with the path to your file containing proxies

    with open(proxies_file, 'r') as file:
        proxies = file.read().splitlines()

    for proxy in proxies:
        send_request_via_proxy(url, proxy)

if __name__ == "__main__":
    main()

