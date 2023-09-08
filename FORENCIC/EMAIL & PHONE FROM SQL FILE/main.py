import re
import os

# Regular expressions to match phone numbers, email addresses, and IP addresses
phone_pattern = r'\b\d{10}\b'  # Matches 10-digit phone numbers
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'  # Matches email addresses
ip_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'  # Matches IPv4 addresses

# Function to extract phone numbers, email addresses, and IP addresses from a SQL file
def extract_contacts_from_sql(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

        # Extract phone numbers and remove duplicates
        phone_numbers = set(re.findall(phone_pattern, text))

        # Extract email addresses and remove duplicates
        email_addresses = set(re.findall(email_pattern, text))

        # Extract IP addresses and remove duplicates
        ip_addresses = set(re.findall(ip_pattern, text))

        return phone_numbers, email_addresses, ip_addresses

# Function to log data to a file
def log_data_to_file(data, file_name):
    with open(file_name, 'w', encoding='utf-8') as log_file:
        for item in data:
            log_file.write(f"{item}\n")

# Main function to process SQL files in a folder
def process_sql_files_in_folder(folder_path):
    if not os.path.isdir(folder_path):
        print(f"'{folder_path}' is not a valid folder.")
        return

    all_phone_numbers = set()
    all_email_addresses = set()
    all_ip_addresses = set()

    for root, _, files in os.walk(folder_path):
        for file_name in files:
            if file_name.endswith('.sql'):
                file_path = os.path.join(root, file_name)
                print(f"Processing file: {file_path}")
                phone_numbers, email_addresses, ip_addresses = extract_contacts_from_sql(file_path)

                all_phone_numbers.update(phone_numbers)
                all_email_addresses.update(email_addresses)
                all_ip_addresses.update(ip_addresses)

    if all_phone_numbers:
        print("Logging Unique Phone Numbers to phone_numbers.txt")
        log_data_to_file(all_phone_numbers, 'phone_numbers.txt')

    if all_email_addresses:
        print("Logging Unique Email Addresses to email_addresses.txt")
        log_data_to_file(all_email_addresses, 'email_addresses.txt')

    if all_ip_addresses:
        print("Logging Unique IP Addresses to ip_addresses.txt")
        log_data_to_file(all_ip_addresses, 'ip_addresses.txt')

if __name__ == "__main__":
    folder_path = "your_folder_path"  # Replace with the path to your folder containing SQL files
    process_sql_files_in_folder(folder_path)
