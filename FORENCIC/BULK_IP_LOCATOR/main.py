import re
import requests
import os

# Function to extract IP addresses from a text file
def extract_ip_addresses(file_path):
    ip_pattern = r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        ip_addresses = re.findall(ip_pattern, text)
    return ip_addresses

# Function to get the location details of an IP address
def get_ip_location(ip_address):
    url = f"https://ipinfo.io/{ip_address}/json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data.get('ip', 'N/A'), data.get('city', 'N/A'), data.get('region', 'N/A'), data.get('country', 'N/A')
    else:
        return ip_address, 'N/A', 'N/A', 'N/A'

# Main function
def main():
    choice = input("Choose an option:\n1. Process a single file\n2. Process all files in a folder\nEnter 1 or 2: ")

    if choice == '1':
        file_path = input("Enter the path to the file: ")
        output_file = "output.log"  # Output file in the current directory
        process_file(file_path, output_file)
    elif choice == '2':
        folder_path = input("Enter the path to the folder: ")
        output_file = "output.log"  # Output file in the current directory
        process_folder(folder_path, output_file)
    else:
        print("Invalid choice. Please enter 1 or 2.")

# Function to process a single file
def process_file(file_path, output_file):
    if not os.path.isfile(file_path):
        print(f"'{file_path}' is not a valid file.")
        return

    ip_addresses = extract_ip_addresses(file_path)
    if not ip_addresses:
        print("No IP addresses found in the file.")
        return

    unique_ips = set()  # Use a set to store unique IP addresses

    with open(output_file, 'a', encoding='utf-8') as log_file:
        for ip_address in ip_addresses:
            if ip_address not in unique_ips:
                unique_ips.add(ip_address)
                ip, city, region, country = get_ip_location(ip_address)
                output_message = f"{ip} - Location: {city}, {region}, {country}\n"
                print(output_message)
                log_file.write(output_message)

# Function to process all files in a folder
def process_folder(folder_path, output_file):
    if not os.path.isdir(folder_path):
        print(f"'{folder_path}' is not a valid folder.")
        return

    with open(output_file, 'a', encoding='utf-8') as log_file:
        for root, _, files in os.walk(folder_path):
            for file_name in files:
                file_path = os.path.join(root, file_name)
                print(f"Processing file: {file_path}")
                log_file.write(f"Processing file: {file_path}\n")
                process_file(file_path, output_file)

if __name__ == "__main__":
    main()
